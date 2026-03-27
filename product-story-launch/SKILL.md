---
name: product-story-launch
description: Plan or build a full premium product launch page with the right page archetype, section sequence, hero logic, highlights, deep-dive chapters, ecosystem blocks, and closing CTA. Use when the user wants a complete product-marketing landing page.
user-invocable: true
---

Create a full premium product-marketing page. This skill is for whole-page structure, not isolated visual polish.

## Mandatory Preparation

Invoke `product-story-design` first. If project brand context is missing, run `teach-product-story`.

Read `../product-story-design/references/product-page-patterns.md` before planning the page.
Use `product-story-hero`, `product-story-highlights`, and `product-story-closer-look` when a section needs deeper refinement.

## Step 1: Classify The Page

Choose exactly one archetype first:

- `flagship launch`
- `value launch`
- `creator device`
- `accessory decision page`
- `performance wearable`
- `new-platform manifesto`
- `sensory experience product`
- `co-branded variant`
- `everyday computing device`
- `workstation computing flagship`

If unsure, choose based on the buyer's top question:

- `Why is this extraordinary?` -> flagship launch
- `Why is this worth it?` -> value launch
- `How does this fit my workflow?` -> creator device
- `Which one should I choose?` -> accessory decision page
- `How does this help me all day?` -> performance wearable
- `What even is this new thing?` -> new-platform manifesto
- `What will this feel like?` -> sensory experience product
- `Why this edition specifically?` -> co-branded variant
- `How will this fit into my everyday work and life?` -> everyday computing device
- `Can this justify serious work?` -> workstation computing flagship

## Step 2: Define The Buying Story

Before writing sections, define:

- the one-line promise
- the proof image or proof interaction for the hero
- the 3-6 decision categories the buyer cares about
- the final CTA

Sections should answer buying questions in the order users naturally ask them.

## Step 3: Build The Section Sequence

Use a structure like:

1. Product-local nav
2. Hero
3. Highlights
4. Design or closer-look section if industrial design matters
5. 2-5 feature deep-dive chapters
6. Ecosystem, accessories, or compatibility section if relevant
7. Comparison or buying help if relevant
8. Closing CTA
9. Fine print

Do not include every section by default. Omit sections that do not serve the product type.

The hero should be treated as a distinct deliverable, not just the first block on the page.

## Step 4: Match Density To Product Tier

- Flagship pages: fewer words, more visual dominance, more breathing room
- Value pages: slightly more explicit copy, more practical proof
- Wearables: organize by daily-life scenarios
- Sensory products: visualize invisible benefits
- New-platform pages: explain the mental model before feature breakdown
- Accessory pages: reduce drama and increase comparison clarity
- Everyday computing pages: blend object beauty with friendly workflow proof
- Workstation pages: keep harder evidence closer to the top

## Step 5: Implement With Restraint

Build real, production-grade code. Do not leave the result as a strategy memo unless the user asked only for planning.

Prefer:

- one dominant visual idea per section
- short headlines
- limited CTAs
- large, quiet spacing
- simple supporting labels

Avoid:

- generic card grids
- dashboard-style feature summaries
- repeating the same section composition
- over-explaining early in the page

## Deliverable Standard

When finished, the page should:

- read like a launch narrative, not a marketing collage
- feel product-led
- preserve its hierarchy on mobile
- make the right sections feel inevitable for that product type
