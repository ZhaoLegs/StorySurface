# StorySurface License Recommendation

This file is a practical recommendation for choosing a license for StorySurface.

It is not legal advice.

## Recommended Default

For this repository, the most practical default is:

- `MIT`

## Why MIT Fits StorySurface

StorySurface is primarily:

- a skill repository
- a methodology and reference library
- prompt and design guidance
- reusable frontend design heuristics

It is not currently:

- a framework runtime
- a hosted service
- a patent-heavy technical platform
- a dependency with complicated redistribution requirements

That makes `MIT` a strong fit because it is:

- easy for people to understand
- easy for companies to approve
- friendly for reuse, remixing, and adaptation
- low-friction for prompt, skill, and documentation repositories

If your goal is broad adoption, `MIT` is usually the cleanest choice.

## When To Choose Apache-2.0 Instead

Choose `Apache-2.0` if you specifically want:

- explicit patent language
- a slightly more formal license posture for commercial reuse
- stronger comfort for organizations that prefer explicit grant language

This is more relevant when the repository contains substantial software implementation or patent-sensitive technical work.

For StorySurface as it exists today, `Apache-2.0` is reasonable, but probably not necessary.

## When Not To Use GPL

Avoid GPL-family licenses here unless you explicitly want downstream derivative work to stay under the same license.

Why this is usually a poor fit for StorySurface:

- many users will want to adapt the skills privately inside product teams
- strong copyleft can reduce adoption for prompt and workflow repositories
- the project value here is portability and reuse, not reciprocity enforcement

## Practical Recommendation

If your goal is:

### Maximum Reuse And Adoption

Choose:

- `MIT`

### More Formal Commercial Comfort

Choose:

- `Apache-2.0`

## Suggested Decision

Current recommendation:

1. publish StorySurface under `MIT`
2. keep the repository disclaimer language in `README.md`
3. state clearly that the repository extracts reusable design principles and does not distribute proprietary brand assets

## Next Step

Current local state:

- `LICENSE` has been prepared as `MIT`

If you later decide to switch:

- replace `LICENSE` with the Apache-2.0 text
- update the `README.md` license line
