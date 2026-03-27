---
name: product-story-audit
description: Audit whether a page actually achieves a premium product-story standard across storytelling, typography, spacing, surfaces, motion, responsiveness, and anti-patterns. Use when the user wants a quality review before redesign or launch.
user-invocable: true
---

Run a structured review of the page. Do not fix issues in this skill unless explicitly asked. Diagnose, score, and recommend the next skill to use.

## Mandatory Preparation

Invoke `product-story-design` first. If no saved brand context exists, run `teach-product-story`.

## Scoring Dimensions

Score each area from 0 to 4.

### 1. Narrative Clarity

Check:

- Is there one obvious promise?
- Does the page unfold in meaningful beats?
- Is the final CTA clear?

### 2. Product Focus

Check:

- Does the product or core experience dominate attention?
- Is decoration competing with the main story?
- Are visuals memorable or generic?

### 3. Typography

Check:

- Are headlines concise and strong?
- Is hierarchy immediately legible?
- Is the copy edited enough for a premium page?

### 4. Spatial Quality

Check:

- Does spacing create rhythm?
- Are sections overly repetitive?
- Does the page feel premium rather than crowded?

### 5. Surface And Motion Discipline

Check:

- Are effects restrained?
- Does motion clarify instead of perform?
- Do material cues feel intentional rather than trendy?

### 6. Mobile Fidelity

Check:

- Does the page preserve its hierarchy on small screens?
- Are the hero and key sections still compelling on mobile?
- Do interactions remain simple and tappable?

### 7. Anti-Pattern Risk

Check for:

- AI-style purple gradients
- generic card grids
- centered-everything layouts
- decorative metrics
- overuse of blur or glass
- startup-template energy

## Output Format

Produce:

1. Total score out of 28.
2. One-sentence verdict: `Not there yet`, `Promising`, `Strong`, or `Exceptional`.
3. Top 3 issues holding the page back.
4. Specific evidence for each issue.
5. Recommended next skill in order of impact:
   - `product-story-arrange`
   - `product-story-typeset`
   - `product-story-polish`
   - `product-story-design`

## Review Standard

Be honest. "Looks clean" is not enough.

The bar is whether the page feels:

- intentional
- expensive
- memorable
- calm under close inspection

If it merely looks modern, that is a miss.
