---
name: teach-product-story
description: Gather project-specific brand and product context for premium product-story design work, then save it to .product-story.md so future sessions can apply a consistent visual language.
user-invocable: true
---

Gather the missing context required for `product-story-design`, then persist it for future sessions.

## Step 1: Explore What Already Exists

Scan the project before asking questions:

- README, docs, and landing-page copy
- package manifests and framework config
- current components and page structure
- color tokens, typography tokens, spacing variables
- logos, renders, screenshots, and product assets

Summarize what is already clear and what remains unknown.

## Step 2: Ask Only For Missing Design Context

Ask focused questions only for information that could not be inferred from the codebase.

Required categories:

### Product

- What is the product or feature being presented?
- What is the single most important promise the page should communicate?
- What action should the visitor take after viewing the page?

### Audience

- Who is this for?
- In what mindset do they arrive: curious, comparing, ready to buy, skeptical, learning?

### Brand Tone

- Which 3 words should define the visual tone?
- Should it feel more restrained, futuristic, warm, technical, or editorial?
- What should it explicitly not feel like?

### Visual Constraints

- Light mode, dark mode, or both?
- Any required or forbidden colors?
- Is the page allowed to feel highly cinematic, or should it stay sober and product-documentation-like?

## Step 3: Write `.product-story.md`

Create or update a `## Design Context` section in the project root file `.product-story.md`.

Use this structure:

```md
## Design Context

### Product
[What is being promoted, the core promise, the desired action]

### Audience
[Who they are, what they care about, what mindset they are in]

### Brand Tone
[3-word tone, emotional target, anti-references]

### Visual Direction
[Light/dark preference, cinematic level, color constraints, material cues]

### Design Principles
- [Principle 1]
- [Principle 2]
- [Principle 3]
- [Principle 4]
```

The principles should be concrete and reusable, for example:

- Lead with one product promise per screen.
- Let typography and spacing do more work than decoration.
- Keep motion subtle and explanatory.
- Favor premium calm over startup energy.

## Step 4: Confirm Reuse

After writing the file:

- summarize the final design context
- state that future `product-story-design` work should read `.product-story.md` first
- call out any open questions that still affect design quality
