"""Regenerate the GROUP-protocol confusion matrix at publication resolution,
using the same reconciled protocol as Tables VI-IX (fixed five-partition GROUP,
RF-200, baseline config: 100 Hz, six channels, 2 s). Writes the seed-averaged
row-normalised matrix to results/confusion_group.json and the figure."""
from __future__ import annotations
import os, json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

from dataio import list_recordings, CLASSES
from features import build_feature_matrix
import viz

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]
NF = 6
RECS = list_recordings()


def fold_assign(seed):
    rng = np.random.default_rng(seed)
    by = {c: [] for c in CLASSES}
    for r in RECS:
        by[r.cls].append(r.name)
    a = {f: set() for f in range(NF)}
    for c, names in by.items():
        names = sorted(names); perm = rng.permutation(len(names))
        for i, nm in enumerate(names):
            a[int(perm[i]) % NF].add(nm)
    return a


def main():
    viz.set_style()
    d = build_feature_matrix(RECS)
    X, y, g = d["X"], d["y"], d["groups"]

    cms = []
    for s in SEEDS:
        fa = fold_assign(s)
        cm = np.zeros((6, 6))
        for f in range(NF):
            te = np.array([gr in fa[f] for gr in g]); tr = ~te
            m = RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=s)
            m.fit(X[tr], y[tr])
            for t_, p_ in zip(y[te], m.predict(X[te])):
                cm[t_, p_] += 1
        cms.append(cm / cm.sum(axis=1, keepdims=True))
        print(f"  seed {s} done")
    cmn = np.mean(cms, axis=0)
    json.dump({"classes": list(CLASSES), "matrix": cmn.tolist()},
              open(os.path.join(RES, "confusion_group.json"), "w"), indent=2)

    fig, ax = plt.subplots(figsize=(5.6, 5))
    im = ax.imshow(cmn, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(6)); ax.set_xticklabels(CLASSES)
    ax.set_yticks(range(6)); ax.set_yticklabels(CLASSES)
    ax.set_xlabel("Predicted"); ax.set_ylabel("True")
    ax.set_title("RF confusion, GROUP protocol (seed-averaged)")
    ax.grid(False)
    for i in range(6):
        for j in range(6):
            ax.text(j, i, f"{cmn[i, j]:.2f}", ha="center", va="center",
                    color="white" if cmn[i, j] > 0.5 else "black", fontsize=8)
    fig.colorbar(im, fraction=0.046, pad=0.04)
    viz.savefig(fig, os.path.join(RES, "fig_confusion_group.png"))
    print("per-class recall:", {c: round(cmn[i, i], 3) for i, c in enumerate(CLASSES)})


if __name__ == "__main__":
    main()
