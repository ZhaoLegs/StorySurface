---
name: product-story-director
description: Direct premium product-story design work by choosing the right narrative archetype, section strategy, and supporting sub-skills before implementation. Use when the user wants the best product-story approach for a page, section, or redesign but has not specified which sub-skill to use.
user-invocable: true
---

Act as the top-level routing skill for this product-story design system.

Use this skill when the user wants premium product-story design work but has not specified whether they need:

- a full product page
- a hero section
- a highlights section
- a closer-look module
- typography refinement
- layout refinement
- final polish
- an audit

## Mandatory Preparation

Read these references first:

- `../product-story-design/references/base-language.md`
- `../product-story-design/references/narrative-archetypes.md`
- `../product-story-design/references/product-page-patterns.md`

If no saved project design context exists, run `teach-product-story`.

## Step 1: Classify The Request

Determine which of these is being asked for:

- `full launch page`
- `page strategy only`
- `hero or highlights section`
- `hero section only`
- `closer-look or design showcase section`
- `typography refinement`
- `layout refinement`
- `final premium polish`
- `quality review`

## Step 2: Choose The Narrative Archetype

Pick the right archetype based on the buyer's first important question:

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

## Step 3: Route To The Right Skill

Map the task to the smallest useful sub-skill:

- full page -> `product-story-launch`
- first screen -> `product-story-hero`
- top summary rail -> `product-story-highlights`
- product-object showcase -> `product-story-closer-look`
- typography issues -> `product-story-typeset`
- layout and rhythm issues -> `product-story-arrange`
- finishing pass -> `product-story-polish`
- review or scoring -> `product-story-audit`
- broad visual direction -> `product-story-design`

If the task spans multiple concerns, sequence them instead of blending them carelessly.

Recommended order:

1. `teach-product-story` if context is missing
2. `product-story-design` for base direction
3. `product-story-launch` for full-page structure
4. `product-story-hero`, `product-story-highlights`, or `product-story-closer-look` for specific modules
5. `product-story-typeset` and `product-story-arrange` for refinement
6. `product-story-polish`
7. `product-story-audit` if a review is needed

## Step 4: Execute, Not Just Advise

If the user wants actual implementation, perform the design or code work after choosing the route.

Do not stop at naming the right skill unless the user only asked for planning.

## Output Standard

When responding, make the routing explicit:

- chosen archetype
- chosen sub-skill or sequence
- one-sentence reason for the choice

Then carry out the work.
