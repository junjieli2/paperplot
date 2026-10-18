---
name: paperplot
description: Create or revise publication-quality scientific plots with Python. Use whenever a request involves Python plotting, figure generation, data visualization, subplot styling, or preparing figures for a paper; do not use for non-Python graphics unless the user asks to reproduce them in Python.
---

# paperPlot

Create scientifically accurate, visually restrained figures that are ready for manuscript use.

## At every invocation

1. Read [references/user-rules.md](references/user-rules.md) completely and apply its durable preferences in addition to this file.
2. Inspect the data, existing plotting code, and nearby manuscript conventions before changing a figure. Preserve correct units, definitions, uncertainty, and distribution basis.
3. Implement or update the Python plotting code, run it, and inspect the generated figure when visual inspection is available. Check clipping, overlaps, legibility, misleading scales, legends, and output dimensions.
4. Save both PDF and PNG. Treat PDF as the publication vector output and render PNG at no less than 600 dpi unless the current prompt specifies otherwise.

The current prompt overrides defaults. Preserve existing project styling when the user explicitly asks for consistency with an established figure set.

## Default scientific style

- Prefer Seaborn’s `deep` palette for distinct lines and points within one figure. When a perceptually uniform colormap is needed for continuous values, prefer `viridis`, unless the prompt or an established journal/project palette specifies another choice.
- Use 16 pt as the base font size for labels, ticks, annotations, and legends. Reduce text only when necessary to prevent overlap, and report the exception.
- Use `(8, 6)` inches for a typical single-panel figure. Scale multi-panel figures proportionally to their layout and content rather than squeezing panels into this size.
- Choose the multi-panel layout from the content and the printed size. When the panels are not dense, or the number of panels is a multiple of three, a 3- or 4-column layout may be used. The exported figure, printed at the manuscript text width, should occupy less than a full page and ideally about half a page (height/width of roughly 0.5–0.75 at text width). If a figure would exceed one page, reduce the per-panel size or the number of panels, or split it into two separate figures. Check the printed height (text width × height/width of the exported figure) against the page text height before finishing; `printed_page_fraction` in the helper returns this fraction.
- Label subplots `(A)`, `(B)`, `(C)`, ... in uppercase at the upper-left of each axes. Prefer a position just outside the axes, such as `(-0.08, 1.03)` in axes coordinates with `clip_on=False`, so labels do not cover data or legends. On small panels, anchor the label a fixed distance above the axes (about 13 pt, as `add_panel_labels` does) so it does not collide with the top y-tick label.
- When multiple panels use the same legend, show it once in panel `(A)` or use one shared figure legend. Deduplicate repeated legend entries.
- Prefer clear axis labels with physical units, restrained grid lines, inward ticks, consistent significant figures, and sufficient padding at axes corners. Avoid title text unless it adds information not already conveyed by captions, axes, or panel labels.
- Keep number-, area-, mass-, and volume-weighted quantities explicitly distinguished. Do not compare unlike distribution bases as though they were identical.
- Show uncertainty and sample size when they materially affect interpretation. Do not hide data selection, smoothing, normalization, exclusions, or post-hoc optimization.
- Use log axes only when scientifically appropriate. Ensure transformations, density normalization, bin widths, KDE bandwidths, and cumulative curves are mathematically consistent and documented in code or output metadata.
- Favor clean lines, colorblind-readable contrasts, minimal decoration, and balanced whitespace. Avoid rainbow maps, unnecessary 3D effects, heavy backgrounds, and redundant encodings.

Use [scripts/paperplot_style.py](scripts/paperplot_style.py) directly or adapt its small helper functions when they fit the project. Do not force the helper onto an existing codebase when a focused edit is clearer.

## Persisting new rules from prompts

The skill supports durable user-specific plotting rules.

- If a prompt explicitly signals a lasting preference with wording such as “以后”, “每当”, “始终”, “加入规则”, “remember”, or “from now on”, automatically append a concise, actionable rule to `references/user-rules.md` after completing the plot.
- Treat ordinary one-off figure instructions as local to that request; do not persist them merely because they differ from a default.
- Deduplicate or update an existing rule instead of adding near-duplicates. If a new durable rule conflicts with an older one, keep the newest explicit preference and remove or revise the obsolete rule.
- Briefly tell the user which durable rule was added or changed.
- Writable copies of this skill normally exist at `~/.codex/skills/paperplot`, `~/.claude/skills/paperplot`, and `/home/kemove/WorkpaceP2/junjie/paper/skills/paperplot`. Keep their `references/user-rules.md` files synchronized. If one copy cannot be updated, continue the plotting task and report the unsynchronized location.

## Handoff

Return clickable paths to the plotting script, PDF, and PNG. Summarize data selection and any non-obvious statistical choices. Report validation warnings that could affect scientific interpretation rather than presenting a cosmetically successful plot as sufficient.
