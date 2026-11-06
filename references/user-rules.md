# User plotting rules

This file stores additional durable preferences explicitly supplied in later prompts. Read it on every invocation of `paperplot`. Add only reusable rules, keep each rule concise, and merge duplicates.

## Additional rules

- For distinct lines and points within one figure, prefer Seaborn’s `deep` categorical palette. When a perceptually uniform colormap is needed for continuous values, prefer `viridis`. Keep the same category color across panels and legends.
- Layout and printed size: 2-, 3-, and 4-column layouts are all allowed. Choose based on panel count, content density, and readability; generally keep the number of rows to 3 or fewer. At manuscript text width, size the exported figure to occupy less than a full page, ideally about half a page; if it would exceed one page, reduce panel sizes or split it into two figures.
