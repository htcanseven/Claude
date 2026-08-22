"""A4 - nested recording-wise cross-validation.

The frugal configuration was previously chosen by inspecting the same GROUP
cross-validation scores that were then quoted as its performance, which biases
the quoted figure upward. Here selection and estimation are separated: an inner
recording-wise loop, run strictly inside each outer training set, picks the
configuration, and the outer held-out recordings - never seen by the selector -
provide the estimate. The gap between the two is the selection bias itself,
which is worth reporting.

Inner selection uses 100 trees (the comparison between configurations is what
matters there); outer estimation uses the 200 trees used throughout the paper.
"""
from __future__ import annotations
import os, json, time
import numpy as np
import protocols_v2 as P
from dataio import CHANNELS, RAW_CHANNELS, CLASSES

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2]
N_INNER = 5

GRID = []
for fs, rs in [(100.0, P.rs_identity), (25.0, P.rs_polyphase(4)), (12.5, P.rs_polyphase(8))]:
    for chn, chl in [("all6", CHANNELS), ("raw3", RAW_CHANNELS)]:
        for win in [2.0, 4.0]:
            GRID.append((f"fs{fs:g}_{chn}_w{win:g}",
                         dict(channels=chl, resampler=rs, fs_out=fs, win_sec=win)))


def inner_folds(train_recs, seed):
    """Split the outer training recordings into N_INNER recording-wise folds."""
    rng = np.random.default_rng(1000 + seed)
    by = {}
    for nm in train_recs:
        by.setdefault(nm.split("_")[0], []).append(nm)
    fa = {i: set() for i in range(N_INNER)}
    for c, names in by.items():
        names = sorted(names)
        perm = rng.permutation(len(names))
        for i, nm in enumerate(names):
            fa[int(perm[i]) % N_INNER].add(nm)
    return fa


def score(d, tr_names, te_names, seed, n_est):
    tr = np.isin(d["groups"], list(tr_names))
    te = np.isin(d["groups"], list(te_names))
    m = P.rf(seed, n_est)
    m.fit(d["X"][tr], d["y"][tr])
    from sklearn.metrics import accuracy_score
    return float(accuracy_score(d["y"][te], m.predict(d["X"][te])))


def main():
    t0 = time.time()
    print(f"building {len(GRID)} feature matrices...")
    mats = {}
    for key, kw in GRID:
        kw = dict(kw); w = kw.pop("win_sec")
        mats[key] = P.build_custom(win_sec=w, overlap=0.5, **kw)
        print(f"  {key}: {mats[key]['X'].shape}")

    all_names = sorted({r.name for r in P.RECS})
    outer_acc, chosen, naive_best = [], [], []
    for seed in SEEDS:
        fa = P.fold_assign(seed)
        for f in range(P.NF):
            te_names = sorted(fa[f])
            tr_names = [n for n in all_names if n not in fa[f]]
            ifa = inner_folds(tr_names, seed)
            inner = {}
            for key, _ in GRID:
                d = mats[key]
                accs = [score(d, [n for n in tr_names if n not in ifa[i]], sorted(ifa[i]), seed, 100)
                        for i in range(N_INNER)]
                inner[key] = float(np.mean(accs))
            best = max(inner, key=inner.get)
            a = score(mats[best], tr_names, te_names, seed, 200)
            outer_acc.append(a); chosen.append(best)
            print(f"  seed {seed} fold {f}: selected {best} (inner {100*inner[best]:.1f}) "
                  f"-> outer {100*a:.1f}%  [{(time.time()-t0)/60:.0f} min]")

    # naive (biased) reference: best configuration judged on the outer folds themselves
    for key, _ in GRID:
        accs = []
        for seed in SEEDS:
            fa = P.fold_assign(seed)
            for f in range(P.NF):
                te_names = sorted(fa[f])
                tr_names = [n for n in all_names if n not in fa[f]]
                accs.append(score(mats[key], tr_names, te_names, seed, 200))
        naive_best.append((key, float(100*np.mean(accs))))
    naive_best.sort(key=lambda x: -x[1])

    nested = float(100*np.mean(outer_acc))
    u_sel, c_sel = np.unique(chosen, return_counts=True)
    out = dict(nested_estimate=nested,
               nested_sd=float(100*np.std(outer_acc, ddof=1)),
               n_outer=len(outer_acc),
               selected={str(k): int(v) for k, v in zip(u_sel, c_sel)},
               naive_ranking=naive_best,
               selection_bias=float(naive_best[0][1] - nested))
    json.dump(out, open(os.path.join(RES, "nested_cv.json"), "w"), indent=2, default=str)
    L = ["# A4 - nested recording-wise cross-validation", "",
         f"- nested (unbiased) estimate: **{nested:.1f}%** over {len(outer_acc)} outer folds",
         f"- best configuration judged on the outer folds themselves: {naive_best[0][0]} at {naive_best[0][1]:.1f}%",
         f"- selection bias: **{out['selection_bias']:+.1f} points**", "",
         "## Configurations selected by the inner loop", ""]
    u, c = np.unique(chosen, return_counts=True)
    for k, n in sorted(zip(u, c), key=lambda x: -x[1]):
        L.append(f"- {k}: chosen in {n}/{len(chosen)} outer folds")
    L += ["", "## Naive ranking (biased, for reference)", ""]
    for k, v in naive_best:
        L.append(f"- {k}: {v:.1f}%")
    open(os.path.join(RES, "nested_cv.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[:6]))


if __name__ == "__main__":
    main()
