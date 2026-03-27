# Frontend Copyable Tokens

Use this as a compact, copy-paste-ready rule set for AI frontend generation.

It is intentionally short.

## Core Prompt Block

Use a premium product-story page with:

- neutral backgrounds first
- product-first hierarchy
- short headings
- restrained CTA count
- large section spacing
- full-width sections as the main page rhythm
- large presentation cards only where they add local proof
- image-first modules with short captions below when the visual already proves the point
- subtle motion only when it clarifies hierarchy

Avoid:

- purple-blue default gradients
- generic card piles
- centered-everything layouts
- too many buttons
- loud glassmorphism
- generic AOS-style fly-in animations

## Color Tokens

```css
:root {
  --accent: #0071e3;
  --text: #1d1d1f;
  --muted: #6e6e73;
  --bg: #f5f5f7;
  --panel: #ffffff;
  --divider: rgba(0, 0, 0, 0.08);

  --bg-dark: #000000;
  --panel-dark: #1c1c1e;
  --surface-dark: #2c2c2e;
  --text-dark: #f5f5f7;
  --muted-dark: rgba(245, 245, 247, 0.72);
  --divider-dark: rgba(255, 255, 255, 0.12);
}
```

Rules:

- default to black, graphite, white, and light gray
- use color atmospheres only locally
- let the product image carry the strongest color moment

## Type Ladder

```text
Hero XL: 96 / 1.0 / 700 / -0.03em
Display 1 Accent: 64 / 1.05 / 700 / -0.025em
Display 1 Default: 56 / 1.06 / 700 / -0.02em
Display 2: 48 / 1.08 / 700 / -0.02em
Display 3: 40 / 1.1 / 700 / -0.015em
Title 1: 32 / 1.15 / 600 / -0.01em
Title 2: 24 / 1.2 / 600 / -0.005em
Subtitle L: 21 / 1.35 / 400 / 0
Subtitle: 19 / 1.4 / 400 / 0
Body L: 17 / 1.6 / 400 / 0
Body: 15 / 1.6 / 400 / 0
Small: 13 / 1.5 / 400 / +0.005em
Nav: 12 / 1.4 / 400 / +0.01em
Eyebrow: 13 / 1 / 500 / +0.04em~+0.08em
```

Weight rules:

- `700` for hero and strongest product-name moments
- `600` for section and card titles
- `500` for buttons and values
- `400` for most explanatory copy
- avoid `300`, avoid `800+` in normal UI

Small-copy rules:

- use `17px` for most explanatory copy
- use `14px~15px` for captions and short support lines
- use `12px~13px` for labels, nav, and footnotes

Heading restraint:

- use `56px` as the normal large desktop section title
- reserve `64px` for rarer, more forceful moments
- do not make every section heading the same maximum size

## Spacing Rules

```text
Base scale: 4 / 8 / 16 / 24 / 40 / 80
Hero offset from header: 80~120
Large section top padding: 160
Dark cinematic section bottom padding: 160~216
Card padding: 32~48
Image-to-copy gap: 16~24
CTA offset below copy: 20~28
```

Rules:

- use the small scale inside components
- use the large scale for narrative sections
- do not equalize every gap across the page
- neighboring proof cards often separate by about `12px`
- compact selector stacks often separate by about `8px`

## Grid Rules

```text
Desktop: 12 columns
Desktop baseline: 1440
Copy width: 980~1200
Mobile: 4 columns
Mobile side padding: 16~20
```

Rules:

- keep copy calmer and narrower than media
- mobile is a rewritten composition, not a shrunk desktop
- full-width section backgrounds can go edge to edge, but the inner content width should stay aligned across the page
- `980px` is a useful calmer content anchor
- `1260px` is a useful wider media-stage anchor for galleries and big proof bands
- desktop inner padding often lands near `22px`, then around `16px` on smaller breakpoints

## Component Rules

```text
Primary CTA height: 36
Circular utility control: 44
Button text: 17
Button horizontal padding: 22~28
Light showcase card radius: 28~30
Dark showcase card radius: 18~20
Utility selection card radius: 12
Card padding: 32~48
Gallery tile width: ~372
Gallery gap: ~25
Overlay max width: ~1420
```

Rules:

- use large rounded cards as presentation stages
- keep full-width bands as the default layout skeleton for computing and lifestyle pages
- do not stack many equal cards vertically
- use slide galleries or value tiles when multiple proof moments need to sit together
- keep shadows restrained
- if the surrounding section already provides the title, avoid another card headline
- keep card copy mostly around `17px` to `21px`
- use captions around `14px~17px` under image-led proof blocks

## Motion Rules

```text
Easing: cubic-bezier(.25, 1, .25, 1)
Fast response: 120~180ms
State change: 180~240ms
Section reveal: 300~500ms
Reveal distance: 8~24px
```

Preferred motion:

- opacity + small translateY
- quiet scale near 1.01
- finish swaps
- detail reveals
- subtle sticky-nav blur and opacity changes

Avoid:

- bounce easing
- looping decorative motion
- large hover scaling
- generic scroll-fly-in presets

## Reusable Page Combos

### Hero Combo

- eyebrow optional
- large product name
- one support line
- one body paragraph
- 1-2 CTA buttons

Hero reduction rule:

- one huge product image
- one compact text block
- title + short support line + CTA only
- no stats, chips, or extra feature rows in the first screen

### Feature Combo

- small accent eyebrow
- large feature title
- one short paragraph

### Image + Caption Combo

- large image or media block
- one bold lead sentence below
- one short muted support sentence

### Spec Card Combo

- compact title
- short description
- 2-column facts or values

### Nav + Meta Combo

- compact nav row
- product name
- price
- legal note

## Product-Type Adjustment

- Everyday laptop: lighter, calmer, more open, object beauty first
- Entry colorful laptop: more playful, more direct, more everyday-value proof
- Flagship pro device: darker, more cinematic, denser evidence
- Sensory product: more close-ups, more invisible-benefit translation

## One-Line AI Prompt

```text
Refactor this into a premium product-story page with neutral backgrounds, product-first hierarchy, short headings, a disciplined type ladder, large section spacing, large showcase cards, only 1-2 CTAs per area, and restrained motion using opacity, small translateY, and premium easing.
```
