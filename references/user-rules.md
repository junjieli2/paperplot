# User plotting rules

This file stores additional durable preferences explicitly supplied in later prompts. Read it on every invocation of `paperplot`. Add only reusable rules, keep each rule concise, and merge duplicates.

## Additional rules

- For distinct lines and points within one figure, prefer Seaborn’s `deep` categorical palette. When a perceptually uniform colormap is needed for continuous values, prefer `viridis`. Keep the same category color across panels and legends.
- Layout and printed size: use a 3- or 4-column layout when the panels are not dense or the panel count is a multiple of three. Size the exported figure so that at text width it occupies less than a full page, ideally about half a page; if it would exceed one page, shrink the panels or split it into two figures.
