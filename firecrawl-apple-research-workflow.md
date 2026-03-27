# Firecrawl Apple Research Workflow

This workflow turns premium product pages into reusable StorySurface research material.

It is designed for:

- collecting page structure at scale
- saving screenshots, markdown, html, and branding data
- comparing multiple product families side by side
- feeding recurring observations back into StorySurface references

It is not designed to replace visual analysis of motion-heavy pages.

## What Firecrawl Is Good For

Use Firecrawl for:

- collecting multiple pages quickly
- extracting page copy and section order
- saving one consistent screenshot per page
- comparing CTA structure, headline density, and module cadence
- building a repeatable research corpus

Do not rely on Firecrawl alone for:

- sticky behavior
- scroll choreography
- pinned storytelling
- timing curves
- frame-by-frame motion analysis

For those, pair Firecrawl with browser observation and screenshots.

## Recommended Workflow

## Prerequisites

Install the Python dependency once:

```bash
python3 -m pip install requests
```

Then set your API key:

```bash
export FIRECRAWL_API_KEY=your_key_here
```

### 1. Capture The Pages

Prepare a URL list of premium product pages you want to study.

Run:

```bash
python3 scripts/firecrawl_collect.py \
  --url-file research/apple-sample-urls.txt \
  --output-dir research/firecrawl-runs/apple-batch-01
```

This will save, for each page:

- `raw.json`
- `markdown.md`
- `page.html`
- `screenshot.png` when available
- `branding.json` when available
- `meta.json`

### 2. Compare The Corpus

Once a batch is saved, compare:

- hero copy length
- CTA count
- headline size and density
- section order
- whether a section is a full-width stage or a local card
- how often image-plus-caption blocks appear

### 3. Turn Observation Into Rules

Only promote repeated patterns into StorySurface.

Good candidates:

- default hero reduction rules
- section-width rules
- image-first section patterns
- caption sizing and rhythm
- card-vs-stage heuristics

Do not promote one-off visual quirks unless they repeat across product families.

### 4. Write Back Into The Right Layer

Use this mapping:

- stable visual rule -> `product-story-design/references/base-language.md`
- token-like rule -> `product-story-design/references/web-design-tokens.md`
- page cadence rule -> `product-story-design/references/narrative-archetypes.md`
- module rule -> `product-story-design/references/component-patterns.md`
- hero-specific rule -> `product-story-design/references/hero-patterns.md`
- family-specific tone shift -> family reference files such as `iphone-family-patterns.md`

## Suggested Apple Study Questions

Use each batch to answer a few specific questions:

- How small is the hero copy relative to the product image?
- Which sections are true full-width stages, and which are local cards?
- How often does the page use image-plus-caption instead of image-plus-headline?
- When does a page use `56px` section titles versus stronger hero moments?
- Which product families become darker, denser, or more comparative?
- Which modules are visual proof, and which are buying support?

## Practical Notes

- Respect the target site's policies and robots behavior.
- Treat the captured pages as research input, not cloning material.
- Use source pages to learn patterns, not to reproduce trademarked assets or copy.
- Keep public StorySurface docs method-first even if deeper research files name sample families.

## Output Strategy

Commit:

- workflow docs
- scripts
- URL lists

Do not commit:

- large scrape output batches
- temporary screenshots from research runs

The default ignored output folder is:

```text
research/firecrawl-runs/
```
