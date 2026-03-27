# Base Language

This reference captures the design language that stays consistent across premium product-marketing pages, even when product stories and page structures change.

Use this file for the stable layer:

- visual tone
- typography behavior
- spacing behavior
- surface treatment
- CTA treatment
- motion philosophy
- interaction expectations

Use `product-page-patterns.md` for the variable layer:

- page archetype
- section order
- narrative pacing
- copy density by product type

## Core Principle

These product pages do not share one fixed layout, but they do share one stable design language.

That language is defined by:

- product-first composition
- editorial restraint
- premium calm
- high legibility
- low interface noise
- polished, non-showy motion

## 1. Product First

The product is always the center of gravity.

This means:

- the strongest image usually carries the section
- surrounding UI should frame, not compete
- decorative devices should be minimized
- the user should remember the product, not the layout trick

If the container or effect is more memorable than the product, the design is off.

## 2. Typography As Primary Structure

Typography is not decoration. It is one of the main layout tools.

Common traits:

- short headlines
- obvious hierarchy
- limited font families
- restrained weight usage
- compact display leading
- clear, readable body copy

The page should still feel premium if imagery is removed and only typography remains.

## 3. Whitespace As Value Signal

Whitespace is used to create:

- focus
- pace
- separation
- perceived quality

These pages usually avoid both cramped density and meaningless emptiness.

Whitespace should feel edited.

## 4. Quiet Surfaces

Surface styling tends to be subtle:

- dark, white, or gray foundations
- large neutral panels
- occasional restrained atmospheric gradients
- crisp edges
- minimal shadow
- gentle tinting only when it serves the product story
- restrained layering

The page may feel dimensional, but rarely noisy.

Effects should support materiality or mood, never replace hierarchy.

What this usually means in practice:

- many pages are built on black, graphite, off-white, or very light gray sections
- color usually comes from the product, the media, or one controlled hero atmosphere
- if a tinted background appears, it is usually broad and quiet, not a rainbow wash
- large rounded cards often sit on neutral page backgrounds instead of the whole page becoming colorful

Common large-card behavior observed across current product pages:

- card corners are often large and soft rather than sharp
- large media cards are frequently around `28px` radius
- cards are used as stage surfaces, not as a generic UI pattern repeated everywhere
- the product image usually occupies most of the card, with copy pinned to an edge or corner

Observed layout correction:

- many important product sections are full-width bands rather than cards
- rounded media cards appear selectively inside that rhythm
- the page usually alternates between open stage sections and more contained proof blocks
- if everything becomes a rounded card, the layout starts to feel more templated than authored

## 5. Controlled Color

Color use is disciplined.

Typical behaviors:

- neutral base palette
- one controlled accent family at most
- product finishes or imagery provide the strongest color moments
- contrast is clean and intentional

This design language rarely relies on multi-accent chaos to create excitement.

Observed correction:

- premium product pages are more neutral than colorful
- black and graphite are common for flagship or cinema-like sections
- white and very light gray are common for approachable, productivity, or accessory sections
- pale blues or soft tints do appear, but usually as a hero atmosphere or a small local moment rather than the whole design language

## 6. Minimal CTA System

Calls to action are simple and repeated consistently.

Typical patterns:

- `Learn more`
- `Buy`
- `Watch the film`
- `Compare`
- `View in your space`

The CTA system is:

- sparse
- predictable
- easy to scan
- visually secondary to the product promise

## 7. Motion With Purpose

Motion usually serves one of a few jobs:

- reveal
- continuity
- focus
- physicality
- state change

It does not usually serve spectacle for its own sake.

Preferred motion character:

- smooth
- quiet
- precise
- measured

Avoid bounce, novelty easing, constant floating, and decorative motion stacks.

## 8. Interaction Feels Effortless

Interactive elements should feel so natural that they almost disappear.

Common traits:

- simple controls
- immediate response
- high hit clarity
- low cognitive load
- tactile but restrained transitions

Examples:

- finish selection
- highlight topic switches
- product viewers
- comparison toggles

These interactions are usually shallow and focused, not tool-like.

## 9. Mobile Is Re-Authored, Not Shrunk

Great mobile implementations preserve the same value hierarchy but often change:

- section composition
- image crop
- text breaks
- interaction density

The mobile page should feel intentionally authored, not like a compressed desktop page.

## 10. Calm Confidence

This may be the most important shared trait.

The page should feel:

- certain
- elegant
- deliberate
- expensive
- unhurried

The design assumes the product is worthy of attention and does not beg for it.

## 11. Observed Typography Scale

Current premium product pages reuse a fairly stable size relationship even when the exact numbers vary by product line.

Common desktop patterns observed across recent pages:

- product name labels near the top often sit around `34/50`
- section wayfinding headlines like `Get the highlights.` and `Take a closer look.` often sit around `56/60`
- large feature chapter headlines often sit around `80/84`
- playful oversized hero statements can go much larger, sometimes around `160/140`
- smaller section labels such as `Design` or `Cameras` often sit around `24/28`
- supporting card or sub-feature titles often sit around `21/29` or `28/32`
- core body copy usually sits around `17/25`
- small price or metadata lines often sit around `17/21`

The important rule is not to copy one exact number everywhere.

The important rule is to preserve the relationship:

- tiny metadata
- product label
- section marker
- major chapter headline
- occasional oversized hero statement

This is a typography ladder, not a random set of sizes.

## 12. Observed Spacing Cadence

Spacing is one of the strongest quality signals.

Common desktop patterns observed across recent pages:

- major sections often begin with around `160px` top padding
- darker or more cinematic sections often carry around `160px` top and up to `216px` bottom padding
- large media or product-viewer stages often live inside very tall blocks rather than tightly packed content bands
- text is usually pinned to edges with generous breathing room instead of centered inside shallow boxes
- cards are large, not dense; many highlight cards are tall presentation stages rather than small content tiles

Practical translation:

- prefer fewer, larger blocks over many medium blocks
- use spacing to separate buyer questions, not just to decorate
- do not equalize every gap
- let hero, highlights, and closer-look sections feel physically larger than utility sections

## 13. Image Followed By Caption

One recurring premium pattern is:

- large image or media block first
- compact text block immediately below
- one strong lead sentence
- one short supporting line in muted text

This appears often in:

- computing lifestyle proof
- portability stories
- app or workflow examples
- size or format comparisons

Why it works:

- the image carries attention first
- the caption lands the buyer takeaway without crowding the media
- the section feels authored and editorial instead of component-driven

Use this pattern when the proof is obvious visually and only needs a short interpretation.

## Base-Language Checklist

Use this before shipping:

- Is the product clearly the hero of the page?
- Does typography carry most of the hierarchy?
- Is the page calm rather than flashy?
- Are the page backgrounds mostly neutral, with color used sparingly?
- Are large cards acting like product stages rather than generic UI boxes?
- Does the type scale follow a clear ladder instead of random jumps?
- Does section spacing feel generous and edited?
- Are effects restrained?
- Are CTAs few and consistent?
- Does motion clarify more than it entertains?
- Does mobile feel authored?

If yes, the design language is aligned even if the page structure differs across product pages.
