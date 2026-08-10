"""Hardening: multi-seed stabilization + combined operating point.

Two goals:
1. Re-estimate the headline numbers over several seeds so the wide single-seed
   CIs (from only 36 recordings) are tightened and the "low-rate helps" trend is
   confirmed or tempered.
2. Test whether the individually-beneficial frugal choices STACK: an incremental
   recipe baseline -> 25 Hz -> raw-3ch -> 4 s window, all under the leakage-free
   GROUP protocol.
"""
from __future__ import annotations

import os, json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.metrics import accuracy_score, f1_score

from dataio import list_recordings, CHANNELS, RAW_CHANNELS
from features import build_feature_matrix
import viz
import matplotlib.pyplot as plt

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]


def _model(name, seed):
    if name == "RF":
        return RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=seed)
    if name == "KNN":
        return make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5, n_jobs=-1))
    if name == "LogReg":
        return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    raise ValueError(name)


def group_multiseed(X, y, g, models=("RF", "KNN", "LogReg"), seeds=SEEDS):
    """Return {model: (mean_acc, std_acc, mean_f1)} pooled over seeds x folds."""
    out = {}
    for m in models:
        accs, f1s = [], []
        for seed in seeds:
            sgkf = StratifiedGroupKFold(n_splits=6, shuffle=True, random_state=seed)
            for tr, te in sgkf.split(X, y, g):
                clf = _model(m, seed)
                clf.fit(X[tr], y[tr])
                yp = clf.predict(X[te])
                accs.append(accuracy_score(y[te], yp))
                f1s.append(f1_score(y[te], yp, average="macro"))
        out[m] = (100*np.mean(accs), 100*np.std(accs), 100*np.mean(f1s))
    return out


def main():
    viz.set_style()
    recs = list_recordings()
    report = {}

    # ---------- 1. incremental frugal recipe (does it stack?) ----------
    print("Incremental recipe (multi-seed GROUP)…")
    recipe = [
        ("baseline: 100Hz/6ch/2s", dict(channels=CHANNELS, fs_target=100, win_sec=2.0)),
        ("+ 25 Hz",                 dict(channels=CHANNELS, fs_target=25,  win_sec=2.0)),
        ("+ raw-3ch",               dict(channels=RAW_CHANNELS, fs_target=25, win_sec=2.0)),
        ("+ 4 s window (optimal)",  dict(channels=RAW_CHANNELS, fs_target=25, win_sec=4.0)),
    ]
    rows = []
    for label, cfg in recipe:
        d = build_feature_matrix(recs, **cfg)
        res = group_multiseed(d["X"], d["y"], d["groups"])
        rows.append((label, cfg, res))
        print(f"  {label:26s} RF={res['RF'][0]:.1f}±{res['RF'][1]:.1f}  "
              f"KNN={res['KNN'][0]:.1f}±{res['KNN'][1]:.1f}  "
              f"LogReg={res['LogReg'][0]:.1f}±{res['LogReg'][1]:.1f}")
    report["recipe"] = [
        dict(label=l, cfg={k: (v if not isinstance(v, list) else "raw3" if v == RAW_CHANNELS else "all6")
                           for k, v in c.items()},
             results={m: dict(acc=r[m][0], acc_std=r[m][1], f1=r[m][2]) for m in r})
        for (l, c, r) in rows
    ]

    # ---------- 2. sampling-rate sweep, multi-seed (confirm the trend) ----------
    print("Sampling-rate sweep (multi-seed, RF)…")
    d1 = []
    for fs in [100, 50, 25, 20, 12.5, 10]:
        d = build_feature_matrix(recs, fs_target=fs)
        res = group_multiseed(d["X"], d["y"], d["groups"], models=("RF",))
        d1.append(dict(fs=fs, acc=res["RF"][0], acc_std=res["RF"][1]))
        print(f"  fs={fs:>5}Hz -> {res['RF'][0]:.1f}±{res['RF'][1]:.1f}")
    report["sampling_multiseed"] = d1

    # ---------- report ----------
    L = ["# Hardening — multi-seed + combined operating point",
         f"", f"Seeds: {SEEDS} · GROUP protocol (StratifiedGroupKFold-6) · "
         "means pooled over seeds×folds.", ""]
    L += ["## Incremental frugal recipe (does it stack?)", "",
          "| configuration | RF | KNN | LogReg |", "|---|---|---|---|"]
    for (label, cfg, r) in rows:
        L.append(f"| {label} | {r['RF'][0]:.1f} ± {r['RF'][1]:.1f} | "
                 f"{r['KNN'][0]:.1f} ± {r['KNN'][1]:.1f} | "
                 f"{r['LogReg'][0]:.1f} ± {r['LogReg'][1]:.1f} |")
    L += ["", "## Sampling-rate sweep (multi-seed, RF)", "",
          "| fs (Hz) | acc | ±std |", "|---|---|---|"]
    for x in d1:
        L.append(f"| {x['fs']:g} | {x['acc']:.1f} | {x['acc_std']:.1f} |")
    with open(os.path.join(RES, "analysis_harden.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(RES, "analysis_harden.json"), "w") as f:
        json.dump(report, f, indent=2)

    # ---------- figure: recipe stacking ----------
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    labels = [r[0] for r in rows]
    xpos = np.arange(len(rows)); w = 0.26
    for i, m in enumerate(["RF", "KNN", "LogReg"]):
        means = [r[2][m][0] for r in rows]; errs = [r[2][m][1] for r in rows]
        ax.bar(xpos + (i-1)*w, means, w, yerr=errs, capsize=3, label=m)
    ax.set_xticks(xpos); ax.set_xticklabels(labels, rotation=15, ha="right", fontsize=8)
    ax.set_ylabel("GROUP accuracy (%)"); ax.set_ylim(0, 100)
    ax.axhline(100/6, ls="--", c="0.6", lw=1)
    ax.set_title("Frugal choices stack: the resource-optimal node beats the naive baseline")
    ax.legend(ncol=3, frameon=False, loc="upper left")
    viz.savefig(fig, os.path.join(RES, "fig_recipe_stacking.png"))
    print("\n".join(L))
    print("wrote analysis_harden.*")


if __name__ == "__main__":
    main()
