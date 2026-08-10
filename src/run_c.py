"""Analysis C: deployment-realistic evaluation (the optimism gap).

Builds the default feature matrix once, then evaluates the same features under
four protocols and quantifies how much the leaky random split inflates accuracy.
"""
from __future__ import annotations

import os, json
import numpy as np

from dataio import list_recordings, CLASSES, CLASS_NAME
from features import build_feature_matrix
from evaluation import (
    protocol_random, protocol_group, protocol_leave_value_out,
)
import viz
import matplotlib.pyplot as plt

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEED = 0


def main():
    viz.set_style()
    recs = list_recordings()
    print("building feature matrix (2s/50%, 100Hz, 6ch, full features)...")
    d = build_feature_matrix(recs)
    X, y = d["X"], d["y"]
    print(f"X={X.shape}, groups={len(set(d['groups']))}")

    results = {}
    print("[1/4] RANDOM (leaky)…");   r_rand = protocol_random(X, y, n_splits=5, seed=SEED)
    print("[2/4] GROUP…");            r_grp  = protocol_group(X, y, d["groups"], n_splits=6, seed=SEED)
    print("[3/4] CROSS-SPEED…");      r_spd  = protocol_leave_value_out(
        X, y, d["speed"], [30, 40, 50], seed=SEED, name="CROSS-SPEED (LOSpeedO)")
    print("[4/4] CROSS-LOAD…");       r_load = protocol_leave_value_out(
        X, y, d["load"], [0, 1], seed=SEED, name="CROSS-LOAD (LOLoadO)")

    protocols = [r_rand, r_grp, r_spd, r_load]
    for p in protocols:
        results[p.name] = p.summary()

    # ---- markdown report ----
    lines = ["# Analysis C — Deployment-realistic evaluation", ""]
    lines.append(f"Features: {X.shape[1]} (full set, 6 channels) · windows: {X.shape[0]} "
                 f"· 2 s / 50% · 100 Hz · seed {SEED}")
    lines.append("")
    lines.append("## Accuracy by protocol (mean ± std over folds)")
    lines.append("")
    lines.append("| Protocol | folds | RF | KNN | SVM |")
    lines.append("|---|---|---|---|---|")
    for p in protocols:
        s = p.summary()
        row = [p.name, str(s["RF"]["n_folds"])]
        for m in ["RF", "KNN", "SVM"]:
            row.append(f"{100*s[m]['acc_mean']:.2f} ± {100*s[m]['acc_std']:.2f}")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    # optimism gap (RANDOM - GROUP)
    lines.append("## Optimism gap  (RANDOM − GROUP), accuracy points")
    lines.append("")
    lines.append("| Model | RANDOM | GROUP | gap |")
    lines.append("|---|---|---|---|")
    sg = r_grp.summary(); srnd = r_rand.summary()
    for m in ["RF", "KNN", "SVM"]:
        a = 100*srnd[m]["acc_mean"]; b = 100*sg[m]["acc_mean"]
        lines.append(f"| {m} | {a:.2f} | {b:.2f} | **{a-b:+.2f}** |")
    lines.append("")
    lines.append("## Macro-F1 by protocol (mean over folds)")
    lines.append("")
    lines.append("| Protocol | RF | KNN | SVM |")
    lines.append("|---|---|---|---|")
    for p in protocols:
        s = p.summary()
        lines.append("| " + p.name + " | " +
                     " | ".join(f"{100*s[m]['f1_mean']:.2f}" for m in ['RF','KNN','SVM']) + " |")
    lines.append("")

    with open(os.path.join(RES, "analysis_C.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(RES, "analysis_C.json"), "w") as f:
        json.dump(results, f, indent=2)
    print("\n".join(lines))

    # ---- Figure: optimism gap bars ----
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    names = [p.name.split(" (")[0].split(" ")[0] for p in protocols]
    models = ["RF", "KNN", "SVM"]
    xpos = np.arange(len(protocols)); w = 0.25
    for i, m in enumerate(models):
        means = [100*p.summary()[m]["acc_mean"] for p in protocols]
        errs = [100*p.summary()[m]["acc_std"] for p in protocols]
        ax.bar(xpos + (i-1)*w, means, w, yerr=errs, capsize=3, label=m)
    ax.set_xticks(xpos); ax.set_xticklabels(names)
    ax.set_ylabel("Accuracy (%)"); ax.set_ylim(0, 100)
    ax.set_title("Accuracy collapses once evaluation is leakage-free")
    ax.legend(ncol=3, loc="lower left", frameon=False)
    ax.axhline(100/6, ls="--", c="0.5", lw=1)
    ax.text(len(protocols)-0.5, 100/6+2, "chance (1/6)", color="0.4", fontsize=8, ha="right")
    viz.savefig(fig, os.path.join(RES, "fig_optimism_gap.png"))

    # ---- Figure: RF confusion matrix under GROUP ----
    yt, yp = r_grp.oof["RF"]
    cm = np.zeros((6, 6), dtype=int)
    for t, p_ in zip(yt, yp):
        cm[t, p_] += 1
    cmn = cm / cm.sum(axis=1, keepdims=True)
    fig, ax = plt.subplots(figsize=(5.6, 5))
    im = ax.imshow(cmn, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(6)); ax.set_yticks(range(6))
    ax.set_xticklabels(CLASSES); ax.set_yticklabels(CLASSES)
    ax.set_xlabel("Predicted"); ax.set_ylabel("True")
    ax.set_title("RF confusion (GROUP protocol, pooled OOF)")
    for i in range(6):
        for j in range(6):
            ax.text(j, i, f"{cmn[i,j]:.2f}", ha="center", va="center",
                    color="white" if cmn[i, j] > 0.5 else "black", fontsize=8)
    fig.colorbar(im, fraction=0.046, pad=0.04)
    viz.savefig(fig, os.path.join(RES, "fig_confusion_group.png"))


if __name__ == "__main__":
    main()
