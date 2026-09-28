#!/usr/bin/env python3
"""Regenerate Figure 6 with error rates instead of pooled error counts.

The original figure labelled each bar with a raw error count ("3 err.", ..., "48 err.",
"22 err."). Classical rows count errors over 607 files, while CNN rows pool three seeds
(1821 file-level predictions), so the counts are not comparable across bars; the
48-error bar standing above the 22-error bar is what Reviewer 1 questioned. This
version keeps the same form, style and data but labels each bar with its error rate,
which is comparable across all rows.

Usage:  python3 tools/make_fig6.py [output_dir]
Writes fig6_macro_f1.pdf (vector, for LaTeX) and fig6_macro_f1.png (preview).
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (x-label, macro-F1, errors, n predictions) exactly as reported in Table 4
ROWS = [
    ("ExtraTrees\nall numeric", 0.9951, 3, 607),
    ("SVM-RBF\nnorm. spectral", 0.9935, 4, 607),
    ("LogReg-L2\nband-energy", 0.9935, 4, 607),
    ("SC-CNN\nseverity calib.", 0.9935, 12, 1821),
    ("Raw-CNN\nmajority vote", 0.9737, 48, 1821),
    ("RF\ncross-channel", 0.9632, 22, 607),
]

BAR = "#1f77b4"  # sampled from the original figure (matplotlib tab:blue)
INK = "#222222"
GRID = "#c8c8c8"


def main(out_dir: Path) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Liberation Serif", "Times New Roman", "DejaVu Serif"],
        "font.size": 9,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "pdf.fonttype": 42,  # embed TrueType so the PDF passes publisher checks
    })

    labels = [r[0] for r in ROWS]
    f1 = [r[1] for r in ROWS]
    rates = [100.0 * r[2] / r[3] for r in ROWS]

    fig, ax = plt.subplots(figsize=(6.0, 2.85))
    x = range(len(ROWS))
    ax.bar(x, f1, width=0.8, color=BAR, zorder=2)

    for xi, v, rate in zip(x, f1, rates):
        ax.text(xi, v + 0.0007, f"{v:.4f}\n{rate:.2f}% err.",
                ha="center", va="bottom", fontsize=7.5, color=INK, linespacing=1.15,
                zorder=3, bbox=dict(facecolor="white", edgecolor="none", pad=0.8))

    ax.set_ylim(0.94, 1.007)
    ax.set_yticks([0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00])
    ax.set_ylabel("Macro-F1")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=8)
    ax.tick_params(axis="x", length=0, pad=4)
    ax.grid(axis="y", color=GRID, linestyle="--", linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)

    fig.tight_layout(pad=0.4)
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "fig6_macro_f1.pdf")
    fig.savefig(out_dir / "fig6_macro_f1.png", dpi=300)
    print(f"wrote {out_dir / 'fig6_macro_f1.pdf'} and .png")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("revision/figures"))
