---
name: product-story-design
description: Create premium product-marketing pages and product surfaces with restrained polish, cinematic hierarchy, crisp typography, generous whitespace, and product-first storytelling. Use when the user wants a calm, high-end launch page, hero section, product storytelling page, or premium redesign for a web interface.
---

Design premium web experiences for product-storytelling pages. Do not clone any brand literally. Extract the underlying principles: calm confidence, editorial pacing, product-first hierarchy, disciplined motion, and extreme visual refinement.

This skill is especially suited for premium consumer-hardware and product-launch pages. The goal is not just "clean UI" but a product page with a strong story arc, sharp merchandising logic, and premium visual control.

## Mandatory Preparation

Before making design decisions, confirm the project's brand context.

Check in this order:

1. Current instructions for a `Design Context` or equivalent brand brief.
2. `.product-story.md` in the project root.
3. If neither exists, invoke `teach-product-story` before doing design work.

Never infer brand personality only from the current code. Code reveals implementation, not taste, positioning, or emotional intent.

## Target Outcome

Build interfaces that feel:

- premium, not flashy
- minimal, not empty
- precise, not sterile
- confident, not loud
- product-led, not decoration-led

The result should feel like it belongs to a world-class hardware or software launch page: high trust, few distractions, strong focus, and impeccable finishing.

## Core Design Logic

### 1. Narrative Before Layout

Strong product-story pages are built as a sequence of revelations, not as a grid of features.

For every page, define:

- the single main promise
- the hero proof that makes the promise believable
- the 3-5 beats that unfold afterward
- the final action the user should take

Each section should advance the story. If a block does not create momentum, remove it.

### 2. Product First

The product, image, or core interaction should carry the page. Decorative UI must support it, never compete with it.

Prefer:

- oversized product imagery or renders
- restrained framing
- strong silhouette contrast
- a single memorable visual per section

Avoid generic SaaS filler like icon cards, dashboard mosaics, testimonial walls, and metric strips unless the product truly needs them.

### 3. Typography Carries Authority

Typography should do most of the work.

Prefer:

- short headlines with clean rhythm
- medium to large type with obvious hierarchy
- tight display leading
- neutral, refined body text
- limited font families, ideally one family across weights

When appropriate, use the San Francisco system stack or a similarly neutral grotesk. Avoid novelty fonts, decorative serif pairings, and startup-style overdesigned type systems.

### 4. Whitespace Is Structure

Spacing is not leftover room. It is the mechanism that creates luxury, focus, and pace.

Use:

- wide section spacing
- compact grouping inside related content
- deliberate empty space around hero copy and product imagery
- clear rhythm changes between dense and airy moments

Do not fill every gap. The best product-story pages often feel expensive because they leave room for attention to land.

### 5. Surfaces Should Feel Physical

Visual treatment should hint at materiality without turning into gimmicks.

Favor:

- soft gradients
- subtle tinting
- restrained shadows
- crisp separators
- layered depth with minimal noise

Use glass, blur, reflections, or glow only when they support the product story. If the effect calls attention to itself first, it is too much.

### 6. Motion Should Clarify, Not Perform

Motion should reveal hierarchy, depth, or continuity.

Prefer:

- staggered entrances
- smooth fades and transforms
- subtle parallax or scale shifts
- transitions that make sections feel connected

Avoid:

- bouncy easing
- ornamental looping animations
- dramatic hover theatrics
- too many simultaneous moving elements

If reduced motion is enabled, preserve hierarchy without spectacle.

### 7. Copy Should Be Calm and Exact

Use concise, assured language.

Prefer:

- short declarative headlines
- one idea per line
- supporting copy that explains value, not marketing fluff
- simple CTA pairs like `Learn more` + `Buy` or `Explore` + `Watch`

Avoid:

- hype adjectives stacked together
- enterprise jargon
- long paragraphs in hero areas
- forced cleverness

## Section Patterns

Consult the references before implementing:

- `references/base-language.md` for the stable visual and interaction layer
- `references/narrative-archetypes.md` for choosing the right storytelling structure
- `references/web-principles.md` for overall aesthetic rules
- `references/component-patterns.md` for layout and section patterns
- `references/copy-and-motion.md` for tone, CTA structure, and motion behavior
- `references/computing-product-patterns.md` for laptop and desktop launch-page structures
- `references/motion-showcase-patterns.md` for premium product-motion roles and anti-patterns
- `references/product-page-patterns.md` for product-page archetypes across iPhone, iPad, and accessories

Typical page structure:

1. Quiet global nav or minimal header
2. Hero with one strong promise
3. Product reveal or signature capability
4. Alternating feature beats with visual contrast
5. Optional ecosystem or comparison band
6. Clear closing CTA
7. Fine print only where required

Choose the page archetype before designing:

- `flagship launch`: cinematic, immersive, feature-led, strongest for Pro-tier products
- `value launch`: simpler, clearer, more comparative, strongest for entry products
- `creator device`: balances performance with lifestyle and accessory workflows, strongest for iPad Air and iPad mini
- `accessory decision page`: feature explanation plus compatibility and comparison, strongest for stylus or accessory families
- `performance wearable`: sectioned by daily activity, health, fitness, or outdoor capability, strongest for smartwatch-like products
- `new-platform manifesto`: sells a new mental model before features, strongest for spatial-computing or new-category products
- `sensory experience product`: translates invisible benefits like sound, comfort, or noise control into imagery and proof, strongest for audio products
- `co-branded variant`: shorter, affinity-driven, and merchandising-forward, strongest for Nike-style collaboration pages
- `everyday computing device`: blends object appeal with approachable daily-use proof, strongest for MacBook Air, MacBook Neo, and iMac-like products
- `workstation computing flagship`: balances premium industrial design with heavier proof, strongest for MacBook Pro-like products

Do not use the same section cadence for all of them.

## Anti-Patterns

Never default to these:

- purple-blue AI gradients
- dense cards on cards
- centered everything
- giant rounded badges everywhere
- glassmorphism as a default style
- overly dark neon interfaces
- feature sections that all look the same
- generic icon plus title plus paragraph grids
- verbose marketing copy
- decorative charts or fake metrics

If the design looks like a startup template with better spacing, it is not done yet.

## Execution Workflow

1. Confirm context and page goal.
2. Identify the one thing this page must make the user feel.
3. Outline the narrative beats before touching styling.
4. Choose one dominant visual idea for the hero.
5. Build a restrained, premium type and spacing system.
6. Add only the motion that improves hierarchy or continuity.
7. Review for reduction: remove anything that feels generic, busy, or self-conscious.

## Quality Bar

Before finishing, verify:

- The page has one unmistakable core promise.
- The product remains the visual center of gravity.
- Typography and spacing do more work than decorative elements.
- Each section feels intentional and not templated.
- The page still feels premium on mobile.
- Motion is subtle, coherent, and optional for reduced-motion users.

The best result should feel inevitable, not busy.
