# StorySurface Release Readiness

This file is a practical release checklist for the current repository state.

It answers three questions:

1. What should be published
2. What should stay local-only
3. What still blocks a clean public release

## 1. Publish Surface

These files and directories should be part of the public repository.

### Core Skill System

- `product-story-design/`
- `product-story-director/`
- `product-story-launch/`
- `product-story-hero/`
- `product-story-highlights/`
- `product-story-closer-look/`
- `product-story-typeset/`
- `product-story-arrange/`
- `product-story-polish/`
- `product-story-audit/`
- `teach-product-story/`

Each of these should include:

- `SKILL.md`
- `agents/openai.yaml`

### Root Documentation

- `README.md`
- `design-methodology.md`
- `ai-frontend-design-spec.md`
- `ai-frontend-design-prompt-template.md`
- `frontend-copyable-tokens.md`
- `firecrawl-apple-research-workflow.md`
- `LICENSE`

### Reusable Code Assets

- `assets/storysurface-tokens.css`
- `assets/storysurface-primitives.css`

### Research Utilities

- `scripts/firecrawl_collect.py`
- `research/apple-sample-urls.txt`
- `research/apple-folder-findings.md`

### Design References

Inside `product-story-design/references/`, the intended public set is:

- `audio-product-patterns.md`
- `base-language.md`
- `component-patterns.md`
- `computing-product-patterns.md`
- `copy-and-motion.md`
- `hero-patterns.md`
- `iphone-family-patterns.md`
- `motion-showcase-patterns.md`
- `narrative-archetypes.md`
- `product-page-patterns.md`
- `spatial-platform-patterns.md`
- `wearable-product-patterns.md`
- `web-design-tokens.md`
- `web-principles.md`

Publication note:

- outward-facing docs should stay largely de-branded
- deeper reference files may still include sample product families and source links as research context
- this is acceptable as long as the top-level README, core skills, and AI-facing spec layer stay method-first rather than brand-first

## 2. Local-Only Surface

These should stay local unless the release strategy changes.

### Prototypes And Test Pages

- `examples/`

Reason:

- these are working local prototypes
- they are helpful during development
- they are not currently part of the intended public skill surface

Current repository rule:

- `examples/` is ignored in `.gitignore`

## 3. Must-Track Before Release

These files are part of the intended public surface and should be added to version control before release:

- `assets/storysurface-primitives.css`
- `assets/storysurface-tokens.css`
- `firecrawl-apple-research-workflow.md`
- `research/apple-folder-findings.md`
- `research/apple-sample-urls.txt`
- `scripts/firecrawl_collect.py`
- `release-readiness.md`

## 3.1 Current Release-Candidate Add Set

If releasing the repository in its current intended shape, the missing add set is:

```text
assets/storysurface-primitives.css
assets/storysurface-tokens.css
firecrawl-apple-research-workflow.md
research/apple-folder-findings.md
research/apple-sample-urls.txt
scripts/firecrawl_collect.py
release-readiness.md
```

## 4. Already-Tracked But Still In Progress

These tracked files currently contain important local modifications and should be reviewed before release:

- `.gitignore`
- `README.md`
- `ai-frontend-design-spec.md`
- `product-story-design/references/base-language.md`
- `product-story-design/references/component-patterns.md`
- `product-story-design/references/computing-product-patterns.md`
- `product-story-design/references/wearable-product-patterns.md`
- `product-story-design/references/web-design-tokens.md`
- `frontend-copyable-tokens.md`

## 5. Remaining Release Blockers

The repository is close, but these still block a clean public release:

### Blocker 1: Public Surface Not Fully Tracked

Some files that the README now presents as part of the public surface are still untracked.

### Blocker 2: Version Not Yet Collected Into One Release Pass

A set of tracked files has local modifications but has not yet been reviewed as one release candidate.

### Non-Blocker: Research References Still Cite Sample Families

Some deeper reference files still name sample product families and link to source pages.

This is currently treated as acceptable for release because:

- the public-facing README and core skill layer have been de-branded
- the remaining sample naming is mostly confined to research references
- the repository presents these references as study material, not as brand-cloning instructions

## 6. Release Decision

Current status:

- methodology quality: ready
- repository packaging: close, but not fully release-ready yet

Operational judgment:

- safe for continued local iteration
- not yet ideal for a clean public publish
- one release-candidate collection pass away from publishable

## 7. Minimum Release Sequence

Use this order:

1. Review and keep the intended public files listed above
2. Add the missing public files to version control
3. Confirm `examples/` and `apple/` stay local-only
4. Run one final README and repository consistency pass
5. Publish
