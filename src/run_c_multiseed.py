"""Analysis C, multi-seed: consistent optimism-gap numbers for the paper.

Pools accuracy/F1 over 5 seeds x folds for every protocol and model, so the
Results section reports one coherent, reliable set of figures. Also regenerates
the optimism-gap figure and a seed-averaged GROUP confusion matrix.
"""
from __future__ import annotations
import os, json
import numpy as np

from dataio import list_recordings, CLASSES
from features import build_feature_matrix
from evaluation import protocol_random, protocol_group, protocol_leave_value_out
import viz
import matplotlib.pyplot as plt

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]
MODELS = ["RF", "KNN", "SVM"]


def pool(results):
    """results: list[ProtocolResult] over seeds -> {model: dict(acc_mean,...)}."""
    out = {}
    for m in MODELS:
        accs, f1s = [], []
        for r in results:
            accs += r.per_model[m]["acc"]
            f1s += r.per_model[m]["f1"]
        accs, f1s = np.array(accs), np.array(f1s)
        out[m] = dict(acc_mean=100*accs.mean(), acc_std=100*accs.std(),
                      f1_mean=100*f1s.mean(), f1_std=100*f1s.std(), n=len(accs))
    return out


def main():
    viz.set_style()
    recs = list_recordings()
    d = build_feature_matrix(recs)
    X, y, g = d["X"], d["y"], d["groups"]
    sp, ld = d["speed"], d["load"]

    protos = {}
    print("RANDOM…");     protos["RANDOM"] = pool([protocol_random(X, y, 5, s) for s in SEEDS])
    print("GROUP…");      grp = [protocol_group(X, y, g, 6, s) for s in SEEDS]
    protos["GROUP"] = pool(grp)
    print("CROSS-SPEED…");protos["CROSS-SPEED"] = pool(
        [protocol_leave_value_out(X, y, sp, [30, 40, 50], s, "s") for s in SEEDS])
    print("CROSS-LOAD…"); protos["CROSS-LOAD"] = pool(
        [protocol_leave_value_out(X, y, ld, [0, 1], s, "l") for s in SEEDS])

    # ---- report ----
    order = ["RANDOM", "GROUP", "CROSS-SPEED", "CROSS-LOAD"]
    L = ["# Analysis C (multi-seed) — optimism gap", "",
         f"Seeds {SEEDS}; means pooled over seeds x folds. 100 Hz, 6 ch, 2 s, "
         "full features.", "", "## Accuracy (%)", "",
         "| Protocol | RF | KNN | SVM |", "|---|---|---|---|"]
    for p in order:
        s = protos[p]
        L.append(f"| {p} | " + " | ".join(
            f"{s[m]['acc_mean']:.1f} ± {s[m]['acc_std']:.1f}" for m in MODELS) + " |")
    L += ["", "## Macro-F1 (%)", "", "| Protocol | RF | KNN | SVM |", "|---|---|---|---|"]
    for p in order:
        s = protos[p]
        L.append(f"| {p} | " + " | ".join(f"{s[m]['f1_mean']:.1f}" for m in MODELS) + " |")
    L += ["", "## Optimism gap (RANDOM − GROUP), accuracy points", ""]
    for m in MODELS:
        gap = protos["RANDOM"][m]["acc_mean"] - protos["GROUP"][m]["acc_mean"]
        L.append(f"- {m}: {protos['RANDOM'][m]['acc_mean']:.1f} → "
                 f"{protos['GROUP'][m]['acc_mean']:.1f}  (**{gap:+.1f}**)")
    with open(os.path.join(RES, "analysis_C_multiseed.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(RES, "analysis_C_multiseed.json"), "w") as f:
        json.dump(protos, f, indent=2)
    print("\n".join(L))

    # ---- figure: optimism gap (multi-seed) ----
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    xpos = np.arange(len(order)); w = 0.25
    for i, m in enumerate(MODELS):
        means = [protos[p][m]["acc_mean"] for p in order]
        errs = [protos[p][m]["acc_std"] for p in order]
        ax.bar(xpos + (i-1)*w, means, w, yerr=errs, capsize=3, label=m)
    ax.set_xticks(xpos); ax.set_xticklabels(order, fontsize=9)
    ax.set_ylabel("Accuracy (%)"); ax.set_ylim(0, 100)
    ax.axhline(100/6, ls="--", c="0.5", lw=1)
    ax.text(len(order)-0.5, 100/6+2, "chance (1/6)", color="0.4", fontsize=8, ha="right")
    ax.set_title("Optimism gap under leakage-free evaluation (5 seeds)")
    ax.legend(ncol=3, frameon=False, loc="upper right")
    viz.savefig(fig, os.path.join(RES, "fig_optimism_gap.png"))

    # ---- seed-averaged GROUP confusion (RF) ----
    cms = []
    for r in grp:
        yt, yp = r.oof["RF"]
        cm = np.zeros((6, 6))
        for t, p_ in zip(yt, yp):
            cm[t, p_] += 1
        cms.append(cm / cm.sum(axis=1, keepdims=True))
    cmn = np.mean(cms, axis=0)
    fig, ax = plt.subplots(figsize=(5.6, 5))
    im = ax.imshow(cmn, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(6)); ax.set_yticks(range(6))
    ax.set_xticklabels(CLASSES); ax.set_yticklabels(CLASSES)
    ax.set_xlabel("Predicted"); ax.set_ylabel("True")
    ax.set_title("RF confusion, GROUP protocol (seed-averaged)")
    for i in range(6):
        for j in range(6):
            ax.text(j, i, f"{cmn[i,j]:.2f}", ha="center", va="center",
                    color="white" if cmn[i, j] > 0.5 else "black", fontsize=8)
    fig.colorbar(im, fraction=0.046, pad=0.04)
    viz.savefig(fig, os.path.join(RES, "fig_confusion_group.png"))
    print("done multiseed C")


if __name__ == "__main__":
    main()
