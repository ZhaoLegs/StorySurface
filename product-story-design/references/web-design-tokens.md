# Web Design Tokens

This reference turns the design language into implementation-facing web tokens and working ranges.

Use this file when the goal is no longer just:

- understanding the design

and is now:

- translating the design into actual frontend decisions
- constraining AI-generated HTML/CSS
- building a reusable token layer for premium product pages

This file is intentionally split into two ideas:

- observed patterns from current premium product pages
- portable working values that can be reused in new projects

Do not treat every number here as a literal brand rule.
Treat them as a disciplined operating range.

## 1. Color Foundation

### 1.1 Core Light Tokens

- `--accent: #0071e3`
- `--text: #1d1d1f`
- `--muted: #6e6e73`
- `--bg: #f5f5f7`
- `--panel: #ffffff`
- `--divider: rgba(0, 0, 0, 0.08)`

Use these as the default light-page foundation.

### 1.2 Core Dark Tokens

- `--bg-dark: #000000`
- `--panel-dark: #1c1c1e`
- `--surface-dark: #2c2c2e`
- `--text-dark: #f5f5f7`
- `--muted-dark: rgba(245, 245, 247, 0.72)`
- `--divider-dark: rgba(255, 255, 255, 0.12)`

Use these for cinematic, flagship, or sensory sections.

### 1.3 Atmosphere Colors

These are not default page colors.

These are occasional atmosphere colors:

- pale sky blue
- soft silver-blue
- restrained warm orange
- subtle product-finish tint

Rules:

- keep them local
- keep them pale
- let the product image carry the strongest color moment
- never let a decorative gradient become the main design language

Avoid presenting purple or purple-to-blue gradients as standard premium UI color behavior.

At most, they are rare atmosphere accents.

## 2. Typography Ladder

Observed desktop relationships from current premium product pages:

- product name or top label: about `34/50`
- section wayfinding headings like `Get the highlights.`: about `56/60`
- small section labels like `Design`: about `24/28`
- major chapter headlines: about `80/84`
- oversized hero statements: roughly `96` to `160`, depending on tone
- body text: about `17/25`
- metadata, pricing, and supporting UI copy: about `17/21`
- small legal or nav text: about `12`

### 2.0 Screenshot-Derived Type Roles

From the latest screenshot study, these roles are especially reusable for premium product pages:

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Hero XL | `96px` | `700` | `1.0` | `-0.03em` |
| Display 1 | `64px` | `700` | `1.05` | `-0.025em` |
| Display 1 Default | `56px` | `700` | `1.06` | `-0.02em` |
| Display 2 | `48px` | `700` | `1.08` | `-0.02em` |
| Display 3 | `40px` | `700` | `1.1` | `-0.015em` |
| Title 1 | `32px` | `600` | `1.15` | `-0.01em` |
| Title 2 | `24px` | `600` | `1.2` | `-0.005em` |
| Subtitle Large | `21px` | `400` | `1.35` | `0` |
| Subtitle | `19px` | `400` | `1.4` | `0` |
| Body Large | `17px` | `400` | `1.6` | `0` |
| Body Standard | `15px` | `400` | `1.6` | `0` |
| Small | `13px` | `400` | `1.5` | `+0.005em` |
| Nav / Label | `12px` | `400` | `1.4` | `+0.01em` |
| Legal | `12px` | `400` | `1.45` | `0` |
| Eyebrow | `13px` | `500` | `1.0` | `+0.04em` to `+0.08em` |

Use this table as a working style library, not as a mandate to use every role on every page.

Important restraint rule:

- treat `56px` as the default large desktop section heading
- use `64px` more sparingly for stronger launch or hero-adjacent moments
- do not make every major section headline `64px`, or the page loses pacing and emphasis

### 2.1 Portable Working Type Tokens

- `--font-size-meta: 0.75rem`
- `--font-size-body: 1.0625rem`
- `--font-size-section-label: 1.5rem`
- `--font-size-wayfinding: 3.5rem`
- `--font-size-chapter: 5rem`

For hero display text, do not use one fixed value.

Use:

- `clamp(4rem, 8vw, 6rem)` for restrained hero statements
- `clamp(5rem, 12vw, 10rem)` only when the page truly supports oversized type

### 2.2 Weight And Tracking

Working rules:

- hero weight: `700` or strong `600`
- major headings: `600`
- body text: `400`
- large headings often use slightly negative tracking
- body copy usually stays at `0` to slightly positive tracking

Portable guidance:

- display tracking: about `-1%` to `-2.5%`
- body tracking: `0` to `+1%`
- display leading: about `1.05` to `1.12`
- body leading: about `1.5` to `1.65`

Explicit guardrails from screenshot study:

- avoid `300` Light in most product-page UI
- avoid `800` to `900` for normal web hierarchy
- use `700` for hero and strongest product-name moments
- use `600` for section titles and card titles
- use `500` for buttons, values, or hover-emphasis labels
- use `400` for most explanatory copy

Tracking ranges:

- `64px+`: around `-0.03em` to `-0.025em`
- `56px`: around `-0.02em` to `-0.018em`
- `40px` to `56px`: around `-0.02em` to `-0.015em`
- `24px` to `36px`: around `-0.01em` to `-0.005em`
- `17px` to `21px`: `0`
- `12px` to `15px`: `0` to `+0.01em`
- uppercase eyebrow: `+0.04em` to `+0.08em`

### 2.3 Language Handling

For Chinese and mixed-language interfaces:

- use a neutral sans stack
- keep CJK body copy slightly roomier than Latin-only copy
- do not force extremely tight leading on dense Chinese paragraphs

Recommended stack:

- `PingFang SC`
- `Noto Sans CJK`
- system sans fallback

## 3. Spacing Scale

### 3.1 Base Scale

Portable working values:

- `4`
- `8`
- `16`
- `24`
- `40`
- `80`

Interpretation:

- `4`: smallest correction
- `8`: tight UI gap
- `16`: related content gap
- `24`: module gap
- `40`: section-internal rhythm change
- `80`: large-block separation

### 3.2 Large-Section Rhythm

Observed product-page cadence often exceeds the base scale:

- hero offset from header: about `80` to `120`
- large section top padding: about `160`
- dark or cinematic sections often use up to `216` bottom padding
- card padding often sits around `32` to `48`
- image-to-copy spacing often sits around `16` to `24`
- CTA offset below copy often sits around `20` to `28`

Working rule:

- use the small scale inside components
- use the large cadence for major narrative sections

Do not run the whole page on one repeated spacing number.

## 4. Grid System

Exact grids vary by page.
Use this as a portable working grid rather than a literal clone.

### 4.1 Desktop

Recommended:

- `12` columns
- desktop design baseline around `1440px`
- content width usually tighter than full viewport
- media may go full bleed, but copy often sits in a calmer inner frame

Working ranges:

- copy-driven sections: about `980` to `1200`
- media-heavy sections: can expand much wider
- ultra-wide screens: allow media staging to grow while keeping copy disciplined

Important layout rule:

- full-width section backgrounds can go edge to edge
- the inner content frame should stay aligned across the page
- do not let hero, design, display, and compare all use noticeably different content widths without a strong reason

### 4.2 Tablet

Recommended:

- maintain the same hierarchy
- reduce interaction density
- collapse local navigation when needed
- simplify multi-column beats earlier than a generic dashboard would

### 4.3 Mobile

Recommended:

- `4` columns
- side padding around `16` to `20`
- single-column narrative flow
- larger cards become stacked presentation blocks

Mobile is a rewrite of composition, not a shrunken desktop grid.

## 5. Component Tokens

### 5.1 Buttons

Working values:

- height: about `44`
- text size: about `17`
- horizontal padding: about `22` to `28`
- radius: pill or very large capsule

Common button roles:

- filled primary
- quiet secondary outline
- text or link-style tertiary

Rules:

- keep CTA count low
- reuse labels consistently
- avoid multiple equally loud buttons in one area

Observed button pattern from screenshot study:

- primary: filled accent button
- secondary: stroked accent button on light background
- dark variant: filled dark button when needed on light surfaces
- the most reusable desktop button height is `44px`

### 5.2 Radius

Useful radius ladder:

- `4`
- `8`
- `14`
- `20`
- `28`
- `9999px` for pills

Use `28` for large showcase cards more often than for small utility cards.

### 5.3 Cards

Working values:

- large product cards: `28px` radius
- smaller cards: `14` to `20`
- internal padding: `32` to `48`
- default backgrounds: `#fff`, `#f5f5f7`, `#000`, `#1c1c1e`

Rules:

- cards are presentation stages, not generic feature containers
- avoid stacking many equal cards vertically
- avoid card-inside-card patterns by default
- keep shadows restrained or remove them entirely when the product image is already strong
- if the surrounding section already provides the title, do not repeat another headline inside the card
- when cards contain text, default to quiet copy in the `17px` to `21px` range

### 5.4 Images

Rules:

- hero imagery may go full bleed
- product imagery often sits on white, gray, or black stages
- do not add heavy shadow when the real page behavior is cleaner without it
- prefer web delivery formats such as `AVIF` and `WebP`

## 5.5 Reusable Composition Combos

These combinations came up repeatedly in the screenshot study and are useful as AI-facing layout presets.

### Combo A: Hero Lead

Use:

- product name in display scale
- one large supporting line
- one body paragraph
- one or two CTA buttons
- optional eyebrow above the main title

Typical values:

- main title: `96px` down to `56px`, depending on viewport and page tone
- support line: `28px` or `21px`
- body: `17px`

### Combo B: Feature Section

Use:

- small accent eyebrow
- one large feature title
- one short explanatory paragraph

Typical values:

- eyebrow: `13px`
- title: `48px`
- description: `19px`

### Combo C: Specification Card

Use:

- compact title
- one short description line
- 2-column facts or values

Typical values:

- heading: `24px`
- body: `15px`
- label: `12px`
- value: `15px` with `500`

### Combo D: Nav Plus Meta

Use:

- compact navigation row
- product name
- price
- legal note

Typical values:

- nav: `12px`
- product name: `17px` with `600`
- price: `13px`
- footnote: `12px`

## 6. Motion Tokens

### 6.1 Easing

Working default:

- `cubic-bezier(.25, 1, .25, 1)`

This gives a fast-but-controlled premium feel.

### 6.2 Duration

Working ranges:

- micro response: `120ms` to `180ms`
- UI state change: `180ms` to `240ms`
- section transition or reveal: `300ms` to `500ms`

### 6.3 Motion Types

Preferred:

- opacity plus slight `translateY(8px~24px)`
- quiet scale change near `1.01`
- finish or state crossfade
- pin, scrub, and reveal for product storytelling
- blur and opacity shift for sticky navigation only when subtle

Avoid:

- generic AOS-style fly-in behavior as the page default
- bounce easing
- looping decorative motion
- exaggerated hover scaling

### 6.4 Sticky Navigation

Working behavior:

- transparent to slightly frosted
- subtle blur
- slight opacity transition
- no dramatic shrink gimmicks

## 7. AI Usage Rules

When feeding this into AI, express the rules like this:

- use a neutral background foundation
- keep color local and restrained
- use a clear typography ladder, not random font sizes
- use large section spacing and large presentation cards
- build on a calm desktop grid and a rewritten mobile flow
- keep button height around `44` and body text around `17/25`
- use restrained motion with premium easing

If the AI output becomes:

- colorful by default
- card-heavy
- gradient-led
- centered everywhere
- over-animated

then it is drifting away from the intended system.
