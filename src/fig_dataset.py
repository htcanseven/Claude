"""Section III figure: representative time-domain signals per health class.
Original figure generated from the dataset (loaded, 50 Hz supply, gUserX)."""
from __future__ import annotations
import os
import numpy as np
from dataio import list_recordings, load_signal, CLASSES, CLASS_NAME, FS
import viz
import matplotlib.pyplot as plt

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")


def main():
    viz.set_style()
    recs = {r.name: r for r in list_recordings()}
    seg_s, start_s, ch = 3.0, 60.0, "gUserX"        # 3 s window, skip first 60 s
    n = int(seg_s * FS); s0 = int(start_s * FS)
    # shared y-limit from the data shown
    segs = {}
    for c in CLASSES:
        x = load_signal(recs[f"{c}_1_50Hz"], [ch])[s0:s0 + n, 0]
        segs[c] = x
    ymax = 1.05 * max(np.abs(v).max() for v in segs.values())
    t = np.arange(n) / FS

    fig, axes = plt.subplots(3, 2, figsize=(7.4, 5.2), sharex=True, sharey=True)
    for ax, c in zip(axes.ravel(), CLASSES):
        ax.plot(t, segs[c], lw=0.7, color=viz.PALETTE[0])
        ax.set_title(f"{c} — {CLASS_NAME[c]}", fontsize=9)
        ax.set_ylim(-ymax, ymax)
    for ax in axes[-1, :]:
        ax.set_xlabel("time (s)")
    for ax in axes[:, 0]:
        ax.set_ylabel(f"{ch} (g)")
    fig.suptitle("Representative gravity-compensated vibration (loaded, 50 Hz supply)",
                 fontsize=10)
    viz.savefig(fig, os.path.join(RES, "fig_example_signals.png"))


if __name__ == "__main__":
    main()
