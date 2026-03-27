#!/usr/bin/env python3
"""Collect research snapshots from product pages using Firecrawl.

This script is intentionally simple:
- reads URLs from --url and/or --url-file
- calls Firecrawl scrape once per URL
- stores markdown/html/screenshot/branding/raw response in a stable folder layout

Environment:
- FIRECRAWL_API_KEY must be set
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests


API_URL = "https://api.firecrawl.dev/v2/scrape"
DEFAULT_FORMATS = ["markdown", "html", "screenshot", "branding"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect Firecrawl research snapshots for StorySurface."
    )
    parser.add_argument(
        "--url",
        action="append",
        default=[],
        help="Page URL to scrape. Can be passed multiple times.",
    )
    parser.add_argument(
        "--url-file",
        help="Text file with one URL per line.",
    )
    parser.add_argument(
        "--output-dir",
        default="research/firecrawl-runs/latest",
        help="Directory where the run output will be stored.",
    )
    parser.add_argument(
        "--formats",
        default=",".join(DEFAULT_FORMATS),
        help="Comma-separated Firecrawl formats. Default: markdown,html,screenshot,branding",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay in seconds between requests. Default: 1.0",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=90,
        help="Request timeout in seconds. Default: 90",
    )
    return parser.parse_args()


def load_urls(args: argparse.Namespace) -> list[str]:
    urls: list[str] = []
    urls.extend(args.url)

    if args.url_file:
        file_urls = Path(args.url_file).read_text(encoding="utf-8").splitlines()
        urls.extend(line.strip() for line in file_urls if line.strip() and not line.startswith("#"))

    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        if url not in seen:
            seen.add(url)
            deduped.append(url)
    return deduped


def slugify_url(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.replace(".", "-")
    path = parsed.path.strip("/") or "home"
    path = re.sub(r"[^a-zA-Z0-9/_-]+", "-", path)
    path = path.replace("/", "__")
    return f"{host}__{path}".strip("-")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def maybe_write_text(path: Path, value: object) -> None:
    if isinstance(value, str) and value:
        path.write_text(value, encoding="utf-8")


def maybe_write_base64_png(path: Path, value: object) -> None:
    if not isinstance(value, str) or not value:
        return

    payload = value
    if "," in value and value.startswith("data:image"):
        payload = value.split(",", 1)[1]

    try:
        path.write_bytes(base64.b64decode(payload))
    except Exception:
        # Save the original value for debugging if decoding fails.
        path.with_suffix(".txt").write_text(str(value), encoding="utf-8")


def build_payload(url: str, formats: Iterable[str]) -> dict:
    return {
        "url": url,
        "formats": list(formats),
        "onlyMainContent": False,
    }


def scrape_url(
    session: requests.Session,
    api_key: str,
    url: str,
    formats: list[str],
    timeout: int,
) -> dict:
    response = session.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=build_payload(url, formats),
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def save_result(output_root: Path, url: str, data: dict) -> None:
    slug = slugify_url(url)
    target = output_root / slug
    ensure_dir(target)

    write_json(target / "raw.json", data)

    payload = data.get("data", data)
    maybe_write_text(target / "markdown.md", payload.get("markdown"))
    maybe_write_text(target / "page.html", payload.get("html"))
    maybe_write_base64_png(target / "screenshot.png", payload.get("screenshot"))

    branding = payload.get("branding")
    if branding is not None:
        write_json(target / "branding.json", branding)

    meta = {
        "url": url,
        "title": payload.get("metadata", {}).get("title"),
        "description": payload.get("metadata", {}).get("description"),
        "sourcePath": str(target),
    }
    write_json(target / "meta.json", meta)


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        print("FIRECRAWL_API_KEY is not set.", file=sys.stderr)
        return 1

    urls = load_urls(args)
    if not urls:
        print("No URLs provided. Use --url or --url-file.", file=sys.stderr)
        return 1

    formats = [item.strip() for item in args.formats.split(",") if item.strip()]
    output_root = Path(args.output_dir)
    ensure_dir(output_root)

    session = requests.Session()
    run_summary: list[dict] = []

    for index, url in enumerate(urls, start=1):
        print(f"[{index}/{len(urls)}] Scraping {url}")
        try:
            data = scrape_url(session, api_key, url, formats, args.timeout)
            save_result(output_root, url, data)
            run_summary.append({"url": url, "status": "ok"})
        except Exception as exc:
            run_summary.append({"url": url, "status": "error", "error": str(exc)})
            print(f"  error: {exc}", file=sys.stderr)

        if index < len(urls):
            time.sleep(args.delay)

    write_json(output_root / "run-summary.json", run_summary)
    print(f"Saved run to {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
