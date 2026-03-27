# AI Frontend Design Spec

This document is a practical design spec for improving AI-generated frontend pages.

It is derived from the `product-story-*` methodology, but rewritten as an optimization guide for actual implementation work.

Use it when:

- asking AI to generate a landing page
- polishing an existing frontend page
- reviewing whether an AI-generated page feels generic
- turning a product brief into a premium web interface

The goal is simple:

make AI-generated frontend pages feel intentional, premium, readable, and product-led instead of templated.

## 1. Core Rule

Most AI-generated pages fail for the same reason:

they are assembled as components, not authored as attention flow.

So the first rule is:

design the page as a sequence of attention, not as a list of sections.

Before generating code, define:

- the one main promise
- the first visual proof
- the next 3-5 buyer questions
- the final action

If the page cannot answer those clearly, styling will not save it.

## 2. Stable Design Rules

These are the rules AI should keep consistent across most premium product pages.

### 2.1 Product First

- The product or core experience must be the visual center of gravity.
- Decorative UI must support the product, never compete with it.
- Avoid generic supporting clutter such as icon storms, metric strips, and badge piles.

### 2.2 Typography First

- Headlines should be short.
- Hierarchy should be obvious at a glance.
- Use one primary font family in most cases.
- Let size, spacing, and rhythm do more work than color and decoration.
- Body text should be readable and not overly wide.

### 2.3 Whitespace Is A Tool

- Leave room around important content.
- Group related content tightly.
- Separate unrelated content clearly.
- Do not make every gap equal.

### 2.4 Surfaces Stay Quiet

- Use subtle gradients and restrained shadow.
- Prefer soft depth over flashy effects.
- Keep cards rare and purposeful.
- Never stack cards inside cards by default.

### 2.5 CTAs Stay Sparse

- Use one primary action and one optional secondary action.
- Reuse the same CTA language consistently.
- Do not fill the page with equally loud actions.

### 2.6 Motion Needs Purpose

- Use motion to reveal, compare, clarify depth, or show state change.
- Avoid bounce, constant floating, gimmicky hover effects, and unnecessary scroll tricks.
- Reduced motion must preserve clarity.

## 3. Common AI Failure Patterns

When reviewing AI-generated frontend work, look for these immediately:

- centered-everything layout
- purple-blue gradients by default
- generic rounded cards everywhere
- too many sections with the same composition
- long hero paragraphs
- too many buttons
- fake metrics with no narrative value
- decorative glow overpowering the content
- weak mobile adaptation
- overuse of glassmorphism

If several of these appear together, the page will feel AI-generated even if the code is clean.

## 4. Section Rules

### 4.1 Hero

The hero should do four jobs:

1. identify the product
2. state the promise
3. create an emotional first impression
4. point to the next action

Hero checklist:

- one strong headline
- one supporting sentence or two at most
- one dominant visual
- one primary CTA and optional secondary CTA
- no clutter

### 4.2 Highlights

Use a highlights section when the page has multiple strong selling points.

Rules:

- 3-6 topics
- each topic gets one visual anchor
- each topic gets one sentence of proof
- this section previews the page, it does not repeat the whole page

### 4.3 Closer Look

Use a closer-look section when the object itself matters.

Rules:

- sparse copy
- object-led interaction
- finish, color, or material changes should feel direct and tactile
- the product should remain the interface

### 4.4 Feature Chapters

Organize feature sections by buyer decision category, not by internal engineering categories.

Examples:

- design
- sound
- comfort
- battery
- continuity
- workflow
- safety
- display

Each section should answer one clear question.

### 4.5 Comparison

Comparison sections should become quieter and more factual than the emotional parts of the page.

Their job is to reduce hesitation.

## 5. Product-Type Guidance

AI should change the page structure based on product type.

### 5.1 Audio Product

Main challenge:

sound is invisible

Use:

- close-up object detail
- sensory language
- comfort storytelling
- state-change demos for ANC, transparency, or audio modes

### 5.2 Wearable

Main challenge:

the product lives inside daily life

Use:

- life-context chapters
- health, safety, or activity framing
- personalization cues

### 5.3 Computing Device

Main challenge:

balance industrial design and workflow proof

Use:

- thinness staging
- screen-content curation
- everyday vs pro proof density
- platform and continuity benefits

### 5.4 New Platform

Main challenge:

the user must understand a new mental model

Use:

- declarative hero
- worldview chapters
- interface explanation
- staged reveals

## 6. Practical CSS Guidance

These rules help AI-generated pages feel cleaner in code and output.

### 6.1 Use Design Tokens

Prefer:

- `--bg`
- `--panel`
- `--text`
- `--muted`
- `--accent`
- `--space-*`
- `--radius-*`

Avoid hard-coding unrelated values all over the page.

### 6.2 Use Relative Units

- Use `rem`, `%`, `vw`, and `clamp()` where appropriate.
- Keep typography and spacing responsive.
- Avoid pixel-locked layouts.

### 6.3 Use Layout Systems Intentionally

- Flex for simple one-dimensional composition
- Grid for larger section layout
- `gap` for spacing instead of margin hacks

### 6.4 Keep The DOM Calm

- Avoid excessive wrapper divs
- Avoid unnecessary nested containers
- Keep semantics clear

### 6.5 Respect Mobile Early

- Design mobile-first or at least mobile-aware
- Keep tap targets large enough
- Re-author composition for smaller screens

## 7. Motion Guidance For AI

When asking AI to add motion, ask for one of these explicitly:

- hero drift
- reveal on scroll
- finish swap transition
- detail zoom
- capability simulation

Do not ask for “more animation” in general. That usually makes the page worse.

## 8. Prompting AI Well

Bad prompt:

`Make this page look better and more premium.`

Better prompt:

`Refactor this page into a premium product-story layout. Keep the product as the visual center, reduce copy density, use stronger type hierarchy, replace repetitive cards with clearer section rhythm, keep one primary CTA, and add only restrained motion that helps reveal content.`

Best prompt shape:

1. what the page is selling
2. who it is for
3. what emotional tone it should have
4. what product type it is
5. which sections are required
6. what anti-patterns to avoid

## 9. Review Checklist

Before accepting AI-generated frontend code, ask:

- Is the product the hero of the page?
- Can I understand the structure by scanning headings alone?
- Are there too many words?
- Are there too many repeated section patterns?
- Does the page feel calm instead of noisy?
- Is motion actually useful?
- Does mobile still feel intentional?
- Would this still look good if most decorative effects were removed?

If the answer to the last question is no, the page is depending too much on surface polish.

## 10. Implementation Workflow

A reliable workflow for AI-generated premium frontend pages:

1. Define the main promise.
2. Choose the product type.
3. Pick the right page narrative.
4. Draft the section sequence.
5. Build the hero first.
6. Build highlights and closer-look sections only if they help.
7. Refine typography and spacing.
8. Add restrained motion.
9. Review for reduction.

## 11. Short Version

If you only remember one compact rule set, use this:

- lead with one promise
- let the product own the page
- cut copy aggressively
- use typography and spacing as the main hierarchy
- keep CTAs few
- keep motion purposeful
- vary section rhythm
- adapt the page structure to the product type

That alone will improve most AI-generated frontend pages dramatically.
