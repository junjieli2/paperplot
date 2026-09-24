# User plotting rules

This file stores additional durable preferences explicitly supplied in later prompts. Read it on every invocation of `paperplot`. Add only reusable rules, keep each rule concise, and merge duplicates.

## Additional rules

- For distinct lines and points within one figure, prefer Seaborn’s `deep` categorical palette. When a perceptually uniform colormap is needed for continuous values, prefer `viridis`. Keep the same category color across panels and legends.
