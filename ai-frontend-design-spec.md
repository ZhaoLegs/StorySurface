# AI Frontend Design Spec

This document is a practical design spec for improving AI-generated frontend pages.

It is derived from the `product-story-*` methodology, but rewritten as an optimization guide for actual implementation work.

If you need the shortest copy-paste version for prompting, also use:

- [frontend-copyable-tokens.md](frontend-copyable-tokens.md)

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

Desktop heading restraint:

- treat `56px` as the default large section-heading size
- use `64px` only for rarer, more forceful moments
- if every large heading is `64px`, the page loses pacing and the hierarchy flattens

### 2.3 Whitespace Is A Tool

- Leave room around important content.
- Group related content tightly.
- Separate unrelated content clearly.
- Do not make every gap equal.

### 2.4 Surfaces Stay Quiet

- Use black, white, graphite, and light gray as the main background families.
- Use subtle gradients and restrained shadow.
- Prefer soft depth over flashy effects.
- Keep cards large, rare, and purposeful.
- Never stack cards inside cards by default.

Observed pattern:

- many premium product pages are built from neutral full-width sections plus a few large rounded presentation cards
- color is usually introduced by the product, the media, or one controlled hero atmosphere
- pale color washes should be occasional, not the default page treatment
- do not wrap every major section in the same rounded card
- for computing and lifestyle product pages, full-width narrative bands should usually be the default rhythm
- keep one stable inner content width even when backgrounds go full bleed

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

Default premium rule:

- let the product image take most of the first screen
- keep the copy cluster visually small
- do not add stats, chips, feature bullets, or explanatory grids in the hero
- if the category is already familiar, simplify even further

Hero background guidance:

- default to neutral or nearly neutral grounds
- use color atmospheres only when they directly reinforce the product mood
- do not turn the whole hero into a decorative gradient experiment

### 4.2 Highlights

Use a highlights section when the page has multiple strong selling points.

Rules:

- 3-6 topics
- each topic gets one visual anchor
- each topic gets one sentence of proof
- prefer large cards or large slides over small equal cards
- keep card surfaces simple and mostly neutral
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

Common premium pattern:

- large image first
- compact caption block directly below
- one bold takeaway sentence
- one short muted support sentence

Use this often when the image already proves the value.

Card copy rule:

- if the section already provides the title, avoid another headline inside the card
- keep most card text in the `17px` to `21px` range

Card surface rule:

- use `28px` to `30px` for large light-surface showcase cards
- use `18px` to `20px` for darker showcase cards
- use `12px` for utility selection cards, not for hero media stages

When multiple proof moments need to sit together:

- prefer a horizontal gallery or a small set of value tiles
- keep the outer section title outside the cards
- keep card-internal text quiet and body-sized

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
- full-width design or lifestyle bands as the default skeleton
- image plus short caption-below modules for app proof, portability, and size decisions
- a calm copy anchor near `980px` with wider media stages that can stretch toward `1260px`
- slide galleries and value tiles as reusable proof modules
- expanded detail overlays when one proof needs richer inspection without bloating the main page

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

### 6.0 Use A Neutral Foundation

Prefer a restrained base token set:

- `--bg: #000` or `#1d1d1f` for dark product-story sections
- `--bg: #f5f5f7` or nearby values for light sections
- `--panel: #fff` or near-white for large cards on light pages
- `--panel-dark: #000` or near-black for cinematic cards on dark pages

Avoid making the whole page colorful just to make it feel premium.

If you use a tint:

- keep it pale
- keep it local
- keep it subordinate to the product image

### 6.1 Use Design Tokens

Prefer:

- `--bg`
- `--bg-alt`
- `--panel`
- `--panel-dark`
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

Suggested desktop type ladder, based on observed product-page relationships:

- product name / eyebrow heading: about `2.125rem`
- section marker heading: about `3.5rem`
- major chapter heading: about `5rem`
- oversized hero statement: larger only when the product tone supports it
- body copy: about `1.0625rem`
- small metadata: about `1.0625rem` with tighter leading

Suggested desktop leading relationships:

- display text should be tight
- body text should be relaxed
- metadata should be compact

Do not use one uniform line-height system for every text role.

### 6.3 Use Layout Systems Intentionally

- Flex for simple one-dimensional composition
- Grid for larger section layout
- `gap` for spacing instead of margin hacks

Suggested spacing rhythm, based on observed product-page cadence:

- major section top padding often starts around `8rem` to `10rem`
- large dark story sections often carry heavier bottom padding than light utility sections
- presentation cards should feel tall and roomy, not compressed
- avoid many medium-sized blocks stacked with identical gaps

Suggested working grid:

- desktop: `12` columns
- mobile: `4` columns
- desktop design baseline can start around `1440px`
- copy-heavy sections should usually be calmer and narrower than full-bleed media sections
- mobile side padding should usually stay around `16px` to `20px`
- calm copy rows can stay near `980px`
- media-led stages can widen toward `1260px` without changing the overall page rhythm

### 6.4 Keep The DOM Calm

- Avoid excessive wrapper divs
- Avoid unnecessary nested containers
- Keep semantics clear

### 6.5 Respect Mobile Early

- Design mobile-first or at least mobile-aware
- Keep tap targets large enough
- Re-author composition for smaller screens

### 6.6 Use Component Tokens Consistently

Suggested working values:

- CTA button height around `44px`
- CTA text around `17px`
- large showcase-card radius around `28px`
- smaller utility-card radius around `14px` to `20px`
- card padding around `32px` to `48px`
- gallery tiles can be larger and wider than standard cards
- utility close controls or media controls should use `44px` hit areas

Do not use the same radius and padding values for every component on the page.

## 7. Motion Guidance For AI

When asking AI to add motion, ask for one of these explicitly:

- hero drift
- reveal on scroll
- finish swap transition
- detail zoom
- capability simulation

Working motion values:

- easing: `cubic-bezier(.25, 1, .25, 1)`
- fast response: about `120ms` to `180ms`
- section reveal: about `300ms` to `500ms`
- reveal distance: usually small, such as `8px` to `24px`

Do not ask for “more animation” in general. That usually makes the page worse.

Do not ask for generic AOS-like fly-ins across the whole page.

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
