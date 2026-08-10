"""Significance tests + measurement-uncertainty for the headline claims (MST reframe).

Uses a fixed recording-level fold assignment per seed so that configurations are
compared on the *same held-out recordings* (a valid paired design). Reports:
  - per-config GROUP accuracy with Type A expanded uncertainty (seeds as repeats);
  - paired tests for  (baseline vs resource-optimal)  and  (100 Hz vs 25 Hz).
Anchor model: Random Forest (200 trees), matching the recipe tables.
"""
from __future__ import annotations
import os, json
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from dataio import list_recordings, CLASSES, CHANNELS, RAW_CHANNELS
from features import build_feature_matrix

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]
NFOLDS = 6


def fold_assignments(recs, seed):
    """Assign the 6 recordings of each class to 6 folds (1 per class per fold)."""
    rng = np.random.default_rng(seed)
    by_class = {c: [] for c in CLASSES}
    for r in recs:
        by_class[r.cls].append(r.name)
    assign = {f: set() for f in range(NFOLDS)}
    for c, names in by_class.items():
        names = sorted(names)
        perm = rng.permutation(len(names))
        for i, name in enumerate(names):
            assign[int(perm[i]) % NFOLDS].add(name)
    return assign


def eval_config(cfg, recs):
    d = build_feature_matrix(recs, **cfg)
    X, y, g = d["X"], d["y"], d["groups"]
    per_fold = {}          # (seed,fold) -> acc
    per_seed = []
    for seed in SEEDS:
        fa = fold_assignments(recs, seed)
        s_acc = []
        for f in range(NFOLDS):
            te = np.array([gr in fa[f] for gr in g])
            tr = ~te
            rf = RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=seed)
            rf.fit(X[tr], y[tr])
            a = accuracy_score(y[te], rf.predict(X[te]))
            per_fold[(seed, f)] = a
            s_acc.append(a)
        per_seed.append(float(np.mean(s_acc)))
    return per_fold, np.array(per_seed)


def type_a(per_seed):
    """Type A uncertainty from seed-level repeats (n=5). Returns dict in %."""
    n = len(per_seed)
    mean = per_seed.mean()
    s = per_seed.std(ddof=1)
    u = s / np.sqrt(n)                       # standard uncertainty of the mean
    t = stats.t.ppf(0.975, n - 1)            # ~2.776 for n=5
    return dict(mean=100*mean, s=100*s, u=100*u, U95=100*t*u, k=float(t), n=n)


def paired(a, b, keys):
    """Paired difference b-a over common (seed,fold) keys."""
    da = np.array([a[k] for k in keys]); db = np.array([b[k] for k in keys])
    diff = db - da
    t_stat, p_t = stats.ttest_rel(db, da)
    try:
        w_stat, p_w = stats.wilcoxon(diff)
    except ValueError:
        w_stat, p_w = np.nan, np.nan
    return dict(mean_diff=100*diff.mean(), sd_diff=100*diff.std(ddof=1),
                n=len(diff), p_ttest=float(p_t), p_wilcoxon=float(p_w))


def main():
    recs = list_recordings()
    configs = {
        "baseline": dict(channels=CHANNELS, fs_target=100, win_sec=2.0),
        "optimal":  dict(channels=RAW_CHANNELS, fs_target=25, win_sec=4.0),
        "fs25":     dict(channels=CHANNELS, fs_target=25, win_sec=2.0),
    }
    pf, ps, unc = {}, {}, {}
    for name, cfg in configs.items():
        print("eval", name, cfg)
        pf[name], ps[name] = eval_config(cfg, recs)
        unc[name] = type_a(ps[name])
        print(f"  {name}: {unc[name]['mean']:.1f} ± {unc[name]['U95']:.1f} (U95), s={unc[name]['s']:.1f}")

    common = sorted(set(pf["baseline"]) & set(pf["optimal"]))
    tests = {
        "optimal_vs_baseline": paired(pf["baseline"], pf["optimal"], common),
        "fs25_vs_fs100": paired(pf["baseline"], pf["fs25"], sorted(set(pf["baseline"]) & set(pf["fs25"]))),
    }

    # ---- report ----
    L = ["# Significance & measurement-uncertainty (RF, 200 trees)", "",
         f"Seeds {SEEDS}; fixed recording-level 6-fold partition; Type A uncertainty "
         "from seed-level repeats (n=5, k=t_{0.975,4}).", "",
         "## GROUP accuracy with expanded uncertainty", "",
         "| Config | Accuracy (%) | U95 | reproducibility s (%) |", "|---|---|---|---|"]
    for name in ["baseline", "fs25", "optimal"]:
        u = unc[name]
        L.append(f"| {name} | {u['mean']:.1f} | ±{u['U95']:.1f} | {u['s']:.1f} |")
    L += ["", "## Paired comparisons (difference over common (seed,fold) test folds)", ""]
    for k, t in tests.items():
        L.append(f"- **{k}**: Δ = {t['mean_diff']:+.1f} pts "
                 f"(paired t p={t['p_ttest']:.3g}, Wilcoxon p={t['p_wilcoxon']:.3g}, n={t['n']})")
    with open(os.path.join(RES, "analysis_stats.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(RES, "analysis_stats.json"), "w") as f:
        json.dump({"uncertainty": unc, "tests": tests}, f, indent=2)
    print("\n".join(L))


if __name__ == "__main__":
    main()
