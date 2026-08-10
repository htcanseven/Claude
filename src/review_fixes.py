"""Recomputes required by the referee report:
1. Honest significance at the seed level (n=5 paired), replacing the n=30
   seed x fold pseudoreplicated test.
2. Channel mutual-information robustness: full feature set vs excluding the DC
   'mean' feature vs a DC-invariant subset, to test whether the raw-channel
   advantage is an artefact of per-recording DC offsets.
3. Raw vs gravity-compensated AC comparison (power ratio + correlation) to
   settle 'discards' vs 'reshapes'.
"""
from __future__ import annotations
import os, json
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import mutual_info_classif

from dataio import list_recordings, load_signal, CLASSES, CHANNELS, RAW_CHANNELS, USER_CHANNELS
from features import build_feature_matrix, FEATURE_NAMES

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


def per_seed_group(X, y, g):
    out = []
    for s in SEEDS:
        fa = fold_assign(s); accs = []
        for f in range(NF):
            te = np.array([gr in fa[f] for gr in g]); tr = ~te
            m = RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=s)
            m.fit(X[tr], y[tr]); accs.append(accuracy_score(y[te], m.predict(X[te])))
        out.append(np.mean(accs))
    return np.array(out)


def honest_significance():
    cfgs = {
        "baseline": dict(channels=CHANNELS, fs_target=100, win_sec=2.0),
        "fs25":     dict(channels=CHANNELS, fs_target=25, win_sec=2.0),
        "optimal":  dict(channels=RAW_CHANNELS, fs_target=25, win_sec=4.0),
    }
    ps = {}
    for k, c in cfgs.items():
        d = build_feature_matrix(RECS, **c)
        ps[k] = per_seed_group(d["X"], d["y"], d["groups"])
        print(f"  {k}: per-seed {np.round(100*ps[k],1)}  mean {100*ps[k].mean():.1f}")
    out = {}
    for name, (a, b) in {"optimal_vs_baseline": (ps["baseline"], ps["optimal"]),
                          "fs25_vs_fs100": (ps["baseline"], ps["fs25"])}.items():
        diff = b - a  # per-seed paired differences (n=5)
        t_p = stats.ttest_rel(b, a).pvalue
        try:
            w_p = stats.wilcoxon(diff).pvalue
        except ValueError:
            w_p = float("nan")
        out[name] = dict(mean_diff=100*diff.mean(), n=len(diff),
                         p_ttest_n5=float(t_p), p_wilcoxon_n5=float(w_p))
        print(f"  {name}: d={100*diff.mean():+.1f} pts, paired t(n=5) p={t_p:.4f}, "
              f"Wilcoxon p={w_p:.4f}")
    return out


def channel_mi():
    d = build_feature_matrix(RECS)  # 100Hz all6 2s full
    cols, X, y = d["columns"], d["X"], d["y"]
    dc_invariant = ["std", "var", "skew", "kurt", "zcr", "entropy"]
    subsets = {"full": FEATURE_NAMES,
               "no_mean": [f for f in FEATURE_NAMES if f != "mean"],
               "dc_invariant": dc_invariant}
    res = {}
    for sname, feats in subsets.items():
        mi = mutual_info_classif(X, y, random_state=0)
        chm = {}
        for ch in CHANNELS:
            idx = [i for i, c in enumerate(cols)
                   if c.split(":")[0] == ch and c.split(":")[1] in feats]
            chm[ch] = float(np.mean(mi[idx]))
        raw = np.mean([chm[c] for c in RAW_CHANNELS])
        usr = np.mean([chm[c] for c in USER_CHANNELS])
        res[sname] = dict(per_channel=chm, raw_mean=raw, user_mean=usr, ratio=raw/usr)
        print(f"  MI[{sname}]: raw={raw:.3f} user={usr:.3f} ratio={raw/usr:.2f}")
    return res


def ac_comparison():
    ratios, corrs = {}, {}
    for r3, u3 in zip(RAW_CHANNELS, USER_CHANNELS):
        rr, cc = [], []
        for r in RECS:
            s = load_signal(r, [r3, u3])
            ac_raw = s[:, 0] - s[:, 0].mean()
            rr.append(ac_raw.std() / (s[:, 1].std() + 1e-12))
            cc.append(np.corrcoef(ac_raw, s[:, 1])[0, 1])
        ratios[f"{r3}/{u3}"] = float(np.mean(rr))
        corrs[f"{r3}~{u3}"] = float(np.mean(cc))
    print("  AC power ratio raw/user:", {k: round(v, 3) for k, v in ratios.items()})
    print("  AC correlation raw~user:", {k: round(v, 3) for k, v in corrs.items()})
    return dict(ac_power_ratio=ratios, ac_correlation=corrs)


def main():
    print("[1] honest significance (n=5)…"); sig = honest_significance()
    print("[2] channel MI robustness…");     mi = channel_mi()
    print("[3] raw vs user AC…");            ac = ac_comparison()
    rep = dict(significance=sig, channel_mi=mi, ac=ac)
    json.dump(rep, open(os.path.join(RES, "review_fixes.json"), "w"), indent=2)
    L = ["# Review-driven recomputes", "",
         "## Honest significance (seed-level paired, n=5)"]
    for k, v in sig.items():
        L.append(f"- {k}: Δ={v['mean_diff']:+.1f} pts; paired t(n=5) p={v['p_ttest_n5']:.4f}; "
                 f"Wilcoxon p={v['p_wilcoxon_n5']:.4f}")
    L += ["", "## Channel MI (raw vs gravity-compensated)"]
    for s, v in mi.items():
        L.append(f"- {s}: raw={v['raw_mean']:.3f}, user={v['user_mean']:.3f}, ratio={v['ratio']:.2f}")
    L += ["", "## Raw vs gravity-compensated AC content"]
    L.append(f"- AC power ratio (raw/user): {ac['ac_power_ratio']}")
    L.append(f"- AC correlation (raw~user): {ac['ac_correlation']}")
    open(os.path.join(RES, "review_fixes.md"), "w").write("\n".join(L) + "\n")
    print("wrote review_fixes.md/json")


if __name__ == "__main__":
    main()
