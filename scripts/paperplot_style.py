"""Small reusable helpers for paperPlot-compliant Matplotlib figures."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

DEFAULT_SINGLE_FIGSIZE = (8, 6)


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
    y: float = 1.03,
    font_size: float = 16,
) -> None:
    """Add uppercase (A), (B), ... labels at the upper-left of each axes."""
    for index, ax in enumerate(np.asarray(axes, dtype=object).reshape(-1)):
        ax.text(
            x,
            y,
            f"({chr(65 + index)})",
            transform=ax.transAxes,
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
