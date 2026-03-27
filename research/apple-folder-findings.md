# Apple Folder Findings

This file captures what was learned from the local saved Apple page code under `apple/`.

The purpose is not to preserve every literal value.

The purpose is to decide:

1. which values are stable enough to promote into StorySurface
2. which values should stay as sample-specific research

## Source Set

Local pages reviewed:

- `apple/iPhone Air - Apple (中国大陆).html`
- `apple/iPhone 17 - Apple (中国大陆).html`
- `apple/iMac - Apple (中国大陆).html`
- `apple/iPad Air - Apple (中国大陆).html`
- `apple/Apple Watch Series 11 - Apple (中国大陆).html`

Key source files reviewed:

- `overview.built.css`
- `overview(1).built.css`
- `ac-localnav.built.css`
- `globalheader.css`
- `sfpro-cn.css`
- `main.built.js`
- `autofilms.built.js`

## High-Confidence Findings

These appeared often enough, or clearly enough in code, to be useful as StorySurface rules.

### 1. Content Frame Stays Calm Even When Backgrounds Go Full Width

Code-backed signals:

- local nav content often uses `max-width: 980px`
- desktop inner padding often sits around `22px`
- smaller breakpoints reduce that toward `16px`

Promote into skills:

- full-width section backgrounds are fine
- inner content width should stay aligned across the page
- `980px` is a useful calmer content anchor for copy-driven rows

### 2. Small UI Type Is More Stable Than Hero Type

Code-backed signals seen repeatedly:

- body copy near `17px`
- supporting text near `14px` to `15px`
- labels and micro UI near `12px` to `13px`
- compact proof-card copy can rise to `21px`

Promote into skills:

- keep explanation copy around `17px`
- keep captions around `14px` to `15px`
- keep labels and nav around `12px` to `13px`
- keep most card copy around `17px` to `21px`

### 3. Card Radius Depends On Context

Cross-checking page captures and CSS supports a contextual ladder, not one fixed radius.

Promote into skills:

- dark showcase cards: `18px` to `20px`
- light showcase cards: `28px` to `30px`
- utility selection cards: `12px`
- compact icon or comparison surfaces: around `16px`

### 4. CTA Height Splits Into Two Main Families

Promote into skills:

- primary commerce CTA: about `36px`
- circular utility or media control: about `44px`

### 5. Card Gaps Are Tighter Than Section Gaps

Promote into skills:

- neighboring proof cards often separate by `12px`
- compact selector stacks often separate by `8px`
- caption spacing often sits around `16px` to `20px`

### 6. Image-Led Proof Blocks Are A Real Repeating Pattern

Observed in structure and supported by saved assets:

- large image or visual card first
- short text below
- minimal internal chrome

Promote into skills:

- image plus short caption is a first-class module
- if the section already owns the headline, the card should usually not add another one

### 7. Local Nav Has A Calm, Reusable Structure

Code-backed signals:

- local nav content often uses `max-width: 980px`
- desktop side padding sits around `22px`
- smaller breakpoints reduce that to around `16px`
- sticky scrim background uses light `rgba(250, 250, 252, 0.8)` and dark `rgba(22, 22, 23, 0.8)`
- menu curtain blur reaches `20px`
- nav action spacing uses roughly `24px` before the first action and `10px` between actions

Promote into skills:

- keep local navigation narrow and calm
- use subtle blur and translucent neutral backgrounds
- space actions with clear but restrained gaps rather than button piles

### 8. Compare Tiles Collapse Aggressively Across Breakpoints

Code-backed signals:

- compare or proof tiles can use `28px` radius and `24px` gaps on desktop
- the same tiles collapse to `12px` radius and `16px` gaps on medium screens
- mobile variants can reduce down to around `192px` height
- card-internal proof copy can move from `21px` desktop to `14px` medium

Promote into skills:

- big rounded cards are not universal across all breakpoints
- medium and mobile should compress card radius and internal typography earlier than generic marketing pages
- comparison and proof grids should simplify aggressively before they feel dashboard-like

### 9. Media Stages Can Be Wider Than Copy Frames

The newer saved pages confirm an important split:

- calm copy-driven rows can stay near `980px`
- media-led stages can stretch wider, often around `1260px`

Promote into skills:

- treat copy width and media-stage width as separate controls
- full-width backgrounds can contain a stable, wider media frame without changing the page's main copy rhythm
- do not let every section invent its own content width; use a small set of repeatable inner frames

### 10. Slide Galleries Are A Reusable Premium Module

The saved `iPad Air` code shows a stable gallery pattern:

- gallery border radius around `30px`
- gallery item width near `372px`
- gallery gap near `25px`

Promote into skills:

- when a section needs multiple proof moments, prefer a horizontal gallery or rail over stacking many equal cards vertically
- use large media tiles with calm spacing and restrained controls
- the gallery should still feel like a product stage, not like a dashboard carousel

### 11. Value Tiles Have Their Own Rhythm

The newer computing pages confirm that value or proof tiles are not generic cards.

Useful recurring values:

- light value tiles around `28px` radius
- desktop tile padding near `28px 76px 48px 32px`
- medium tile padding near `28px 56px 48px 28px`
- mobile tile padding near `24px 24px 48px`
- desktop tile min width near `372px`, collapsing toward `344px` and `260px`

Promote into skills:

- treat value tiles as a separate proof surface with more breathing room than utility cards
- keep them large, sparse, and image-led
- compress them quickly across breakpoints so they do not become heavy blocks on medium screens

### 12. Expanded Detail Layers Are Part Of The Pattern Library

The saved `iPad Air` code confirms that premium product pages sometimes open richer detail views instead of forcing every detail into the main scroll.

Useful recurring values:

- modal or overlay max width near `1420px`
- overlay card radius near `25px`
- close icon near `36px`
- close-button hit area near `44px`
- backdrop blur near `20px`

Promote into skills:

- expanded detail layers are valid when a gallery, closer-look, or comparison needs more depth without overloading the page
- overlays should stay quiet, large, and easy to exit
- close controls should be generous even when the visual chrome is minimal

### 13. Wearable Pages Segment By Daily Task Buckets

The saved `Apple Watch Series 11` assets reinforce that wearable pages are deeply structured around daily-life chapters:

- health
- fitness
- go
- safety

Promote into skills:

- do not organize wearables by hardware components first
- organize by the life task or readiness state the watch supports
- use each bucket as a distinct chapter with its own proof media

### 14. Control Rows Stay Compact And Repeatable

Saved watch-page UI confirms a stable compact-control rhythm:

- control-group gap near `12px`
- color-swatch-row gap near `8px`

Promote into skills:

- use tight, deliberate gaps for compact control rows
- keep swatches and segmented controls visually calm rather than oversized

## Findings To Keep As Research, Not Global Rules

These are useful observations, but not stable enough to become default system rules.

- exact hero type sizes such as `72px`, `80px`, or `96px`
- one page's exact section heights
- page-specific grid row math from comparison components
- one-off animation durations buried in specialized scripts
- product-family-specific darkness or copy density

These belong in:

- `product-page-patterns.md`
- `iphone-family-patterns.md`
- `computing-product-patterns.md`
- `wearable-product-patterns.md`

not in the most general token layer.

## What Was Added To StorySurface

The following files were updated from this review:

- `product-story-design/references/web-design-tokens.md`
- `product-story-design/references/base-language.md`
- `product-story-design/references/component-patterns.md`
- `product-story-design/references/computing-product-patterns.md`
- `product-story-design/references/wearable-product-patterns.md`
- `ai-frontend-design-spec.md`
- `frontend-copyable-tokens.md`

## Practical Judgment

The most valuable thing in the saved Apple code is not the exact hero CSS.

It is the repeated lower-level discipline:

- calm content widths
- stable body and label sizing
- context-aware radius choices
- sparse CTA sizing
- selective card use
- image-first proof modules
- calm sticky navigation
- aggressive breakpoint simplification for proof grids

Those are the parts most worth transferring into StorySurface.
