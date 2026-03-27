# StorySurface

The product-story vocabulary your AI frontend still needs.

11 modular skills, reusable design references, and practical examples for building premium product-story landing pages with AI.

> **Quick start:** Start with [product-story-design/SKILL.md](product-story-design/SKILL.md), then use [product-story-director/SKILL.md](product-story-director/SKILL.md) to route the work by page type, section type, and narrative archetype.

## Why StorySurface?

Most AI frontend output is not bad because the code is broken. It is bad because the design language is under-specified.

Without guidance, AI tends to fall back to the same predictable mistakes:

- long hero copy
- generic card piles
- repeated section structure
- loud gradients without product logic
- too many buttons
- motion that decorates instead of clarifies

StorySurface pushes against that bias with:

- **A product-story design system** centered on calmer, more product-led landing pages
- **11 modular skills** for directing, building, refining, and reviewing pages
- **Curated design references** for hierarchy, archetypes, modules, copy, and motion
- **Practical examples** that show the system working across different product categories
- **Explicit anti-patterns** that tell the AI what not to do

## What's Included

### The Core Skill: `product-story-design`

A central design skill supported by focused references:

| Reference | Covers |
|-----------|--------|
| [base-language.md](product-story-design/references/base-language.md) | Product-first hierarchy, spacing, restraint, CTA philosophy |
| [narrative-archetypes.md](product-story-design/references/narrative-archetypes.md) | Page structures by product type and buyer intent |
| [component-patterns.md](product-story-design/references/component-patterns.md) | Reusable landing-page modules and section logic |
| [hero-patterns.md](product-story-design/references/hero-patterns.md) | First-screen composition, promise framing, CTA rhythm |
| [copy-and-motion.md](product-story-design/references/copy-and-motion.md) | Short-form copy style and purposeful motion rules |
| [motion-showcase-patterns.md](product-story-design/references/motion-showcase-patterns.md) | Reveal pacing, finish swap, detail zoom, capability demos |
| [product-page-patterns.md](product-story-design/references/product-page-patterns.md) | Shared structure across premium product pages |

### 11 Skills

| Skill | What it does |
|-------|--------------|
| [teach-product-story](teach-product-story/SKILL.md) | Gather project context and save reusable guidance into `.product-story.md` |
| [product-story-director](product-story-director/SKILL.md) | Route work by page type, module type, and narrative archetype |
| [product-story-design](product-story-design/SKILL.md) | Apply the overall design language and page-building logic |
| [product-story-launch](product-story-launch/SKILL.md) | Plan and build a full launch or landing page |
| [product-story-hero](product-story-hero/SKILL.md) | Build the first screen, promise, and CTA structure |
| [product-story-highlights](product-story-highlights/SKILL.md) | Build highlight rails and top-of-page summary modules |
| [product-story-closer-look](product-story-closer-look/SKILL.md) | Build product-led detail sections such as finishes, materials, and object views |
| [product-story-typeset](product-story-typeset/SKILL.md) | Fix typography, hierarchy, and copy rhythm |
| [product-story-arrange](product-story-arrange/SKILL.md) | Fix layout, spacing, sequence, and visual rhythm |
| [product-story-polish](product-story-polish/SKILL.md) | Run a final refinement pass before shipping |
| [product-story-audit](product-story-audit/SKILL.md) | Review the page for design quality, consistency, and regressions |

### Examples

| Example | Category | What it validates |
|---------|----------|-------------------|
| [lumen-buds-pro-product-story.md](examples/lumen-buds-pro-product-story.md) | Audio | Sensory-experience product narrative |
| [lumen-buds-pro-demo.html](examples/lumen-buds-pro-demo.html) | Audio | A complete premium product showcase page |
| [northlight-air-product-story.md](examples/northlight-air-product-story.md) | Computing | Everyday-computing narrative structure |
| [northlight-air-demo.html](examples/northlight-air-demo.html) | Computing | A second category implementation test |

## Anti-Patterns

The system includes strong guidance on what to avoid:

- do not make every section a card
- do not use long sales paragraphs in hero areas
- do not overload the page with CTA buttons
- do not rely on decorative gradients as a substitute for hierarchy
- do not make motion louder than the product
- do not force one fixed page skeleton onto every product category

## Installation

### Option 1: Use Directly From This Repository

Open the skills in place and work from the repo:

- [product-story-design/SKILL.md](product-story-design/SKILL.md)
- [product-story-director/SKILL.md](product-story-director/SKILL.md)

This is the easiest way to study, edit, and evolve the system.

### Option 2: Install Into Codex

Copy the skill folders into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -r product-story-* teach-product-story ~/.codex/skills/
```

For project-specific use:

```bash
mkdir -p .codex/skills
cp -r product-story-* teach-product-story .codex/skills/
```

## Usage

Once installed, use the skills in this order:

1. Start with [teach-product-story/SKILL.md](teach-product-story/SKILL.md) to capture product, audience, tone, and visual direction.
2. Use [product-story-director/SKILL.md](product-story-director/SKILL.md) to choose the right route.
3. Build with [product-story-launch/SKILL.md](product-story-launch/SKILL.md) or section skills like [product-story-hero/SKILL.md](product-story-hero/SKILL.md), [product-story-highlights/SKILL.md](product-story-highlights/SKILL.md), and [product-story-closer-look/SKILL.md](product-story-closer-look/SKILL.md).
4. Refine with [product-story-typeset/SKILL.md](product-story-typeset/SKILL.md), [product-story-arrange/SKILL.md](product-story-arrange/SKILL.md), and [product-story-polish/SKILL.md](product-story-polish/SKILL.md).
5. Review with [product-story-audit/SKILL.md](product-story-audit/SKILL.md).

Example prompts:

```text
Use StorySurface to design a premium launch page for a lightweight laptop.

Use product-story-director to choose the right archetype, then build the page.

Use product-story-hero to improve the first screen of this product page.

Use product-story-audit to review this landing page for hierarchy, pacing, and interaction quality.
```

## What It Helps You Build

StorySurface is especially useful for:

- product landing pages
- launch pages
- premium marketing pages
- hardware and software showcase pages
- AI-assisted frontend generation and refinement

## What It Is Not

StorySurface is not a brand-cloning kit.

It studies premium product-marketing patterns and extracts reusable principles such as:

- product-first hierarchy
- restrained typography
- edited whitespace
- quiet surfaces
- sparse CTA systems
- purposeful motion
- narrative page structure based on buyer intent

Research examples include well-known premium product pages, but the goal is transfer learning, not literal imitation.

Do not use this repository to copy trademarked assets, proprietary copy, or brand-identical page designs.

## Related Docs

- [design-methodology.md](design-methodology.md)
- [ai-frontend-design-spec.md](ai-frontend-design-spec.md)
- [ai-frontend-design-prompt-template.md](ai-frontend-design-prompt-template.md)

## Supported Setup

StorySurface is currently organized as a local skill repository for Codex-style workflows using `SKILL.md` plus `agents/openai.yaml`.

The methodology can still be reused manually in other AI coding tools, but this repository is currently structured and tested as a Codex-friendly skill set.

## License

Choose and add a license before wider publication.

I have intentionally not selected one automatically because that decision has legal consequences.
