"""Small reusable helpers for paperPlot-compliant Matplotlib figures."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

DEFAULT_SINGLE_FIGSIZE = (8, 6)
# Per-panel size for 3- and 4-column layouts, keeping the figure 16-19 in wide.
COLUMN_PANEL_SIZE = {3: (5.6, 4.4), 4: (4.6, 3.9)}
# Panel labels sit this far above the axes; equals 0.03 of a 6 in panel and
# clears the top y-tick label on the smaller panels of 3- and 4-column layouts.
PANEL_LABEL_OFFSET_POINTS = 13.0


def panel_size(columns: int) -> tuple[float, float]:
    """Per-panel size in inches for a layout with this many columns."""
    return COLUMN_PANEL_SIZE.get(columns, DEFAULT_SINGLE_FIGSIZE)


def printed_page_fraction(fig: plt.Figure, text_width: float = 6.5, text_height: float = 9.0) -> float:
    """Fraction of the page text height the tight figure takes when printed at text width.

    Aim for about 0.5 and keep it below about 0.8 so the caption fits on the same page.
    """
    fig.canvas.draw()
    box = fig.get_tightbbox(fig.canvas.get_renderer())
    return text_width * box.height / box.width / text_height


def apply_paper_style(font_size: float = 16) -> list[tuple[float, float, float]]:
    """Apply the default paperPlot style and return the seaborn deep palette."""
    sns.set_theme(style="ticks", palette="deep")
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": font_size,
            "axes.labelsize": font_size,
            "axes.titlesize": font_size,
            "xtick.labelsize": font_size,
            "ytick.labelsize": font_size,
            "legend.fontsize": font_size,
            "axes.linewidth": 1.1,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    return list(sns.color_palette("deep"))


def add_panel_labels(
    axes: Iterable[plt.Axes] | np.ndarray,
    *,
    x: float = -0.08,
    offset_points: float = PANEL_LABEL_OFFSET_POINTS,
    font_size: float = 16,
) -> None:
    """Add uppercase (A), (B), ... labels just above the upper-left corner of each axes.

    The label is offset by a fixed distance in points rather than a fraction of
    the axes height, so it clears the top y-tick label for any panel size.
    """
    for index, ax in enumerate(np.asarray(axes, dtype=object).reshape(-1)):
        ax.annotate(
            f"({chr(65 + index)})",
            xy=(x, 1.0),
            xycoords="axes fraction",
            xytext=(0.0, offset_points),
            textcoords="offset points",
            ha="left",
            va="bottom",
            fontsize=font_size,
            fontweight="bold",
            clip_on=False,
        )


def deduplicated_legend(ax: plt.Axes, **kwargs) -> None:
    """Draw one legend with duplicate labels removed while preserving order."""
    handles, labels = ax.get_legend_handles_labels()
    unique: dict[str, object] = {}
    for handle, label in zip(handles, labels):
        if label and label not in unique:
            unique[label] = handle
    if unique:
        ax.legend(unique.values(), unique.keys(), frameon=False, **kwargs)


def save_pdf_png(
    fig: plt.Figure,
    output_stem: str | Path,
    *,
    dpi: int = 600,
    close: bool = False,
) -> tuple[Path, Path]:
    """Save vector PDF and high-resolution PNG with a tight bounding box."""
    stem = Path(output_stem).with_suffix("")
    stem.parent.mkdir(parents=True, exist_ok=True)
    pdf = stem.with_suffix(".pdf")
    png = stem.with_suffix(".png")
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=dpi, bbox_inches="tight")
    if close:
        plt.close(fig)
    return pdf, png
