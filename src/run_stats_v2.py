"""A3 - headline comparisons on a defensible statistical footing.

Replaces the earlier n=5 seed-level paired t-test. Scores are computed per
held-out recording, so the sampling unit is the recording (n=36) rather than a
seed re-run of the same partition; intervals cluster on recording and
configurations are compared with a two-sided paired permutation test, which
makes no normality assumption and does not run out of resolution the way a
Wilcoxon test on five values does. Ten seeds are used so the per-recording
means are stable.
"""
from __future__ import annotations
import os, json
import numpy as np
import protocols_v2 as P
from dataio import CHANNELS, RAW_CHANNELS

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = list(range(10))

CFGS = {
    "baseline": dict(channels=CHANNELS,     resampler=P.rs_identity,    fs_out=100.0, win_sec=2.0),
    "fs25":     dict(channels=CHANNELS,     resampler=P.rs_polyphase(4), fs_out=25.0,  win_sec=2.0),
    "frugal":   dict(channels=RAW_CHANNELS, resampler=P.rs_polyphase(4), fs_out=25.0,  win_sec=4.0),
}


def main():
    res, per_rec = {}, {}
    for name, kw in CFGS.items():
        win_sec = kw.pop("win_sec")
        d = P.build_custom(win_sec=win_sec, overlap=0.5, **kw)
        accs, f1s, pers = [], [], []
        for s in SEEDS:
            a, f, per = P.eval_group(d, s)
            accs.append(a); f1s.append(f); pers.append(per)
            print(f"  {name} seed {s}: {100*a:.1f}%")
        m, h, n, pr = P.clustered_ci(pers)
        per_rec[name] = pr
        res[name] = dict(acc_mean=m, ci95=h, n_recordings=n,
                         macro_f1=float(100*np.mean(f1s)),
                         seed_mean=float(100*np.mean(accs)),
                         per_seed=[float(100*a) for a in accs])
        print(f"{name:10s} {m:.1f} +/- {h:.1f}  (macro-F1 {res[name]['macro_f1']:.1f}, n={n})")

    comps = {}
    for label, (a, b) in {"frugal_vs_baseline": ("baseline", "frugal"),
                          "fs25_vs_baseline":   ("baseline", "fs25")}.items():
        diff, p, n = P.paired_permutation(per_rec[a], per_rec[b])
        comps[label] = dict(mean_diff=diff, p_permutation=p, n_recordings=n)
        print(f"{label:22s} d={diff:+.1f} pts, paired permutation p={p:.4f} (n={n})")

    json.dump(dict(configs=res, comparisons=comps, per_recording=per_rec),
              open(os.path.join(RES, "stats_v2.json"), "w"), indent=2)
    L = ["# A3 - recording-level statistics (GROUP, RF-200, 10 seeds)", "",
         "| configuration | accuracy (%) | macro-F1 (%) |", "|---|---|---|"]
    nm = {"baseline": "Baseline (100 Hz, 6 ch, 2 s)", "fs25": "25 Hz, 6 ch, 2 s",
          "frugal": "Frugal (25 Hz, 3 raw ch, 4 s)"}
    for k in CFGS:
        L.append(f"| {nm[k]} | {res[k]['acc_mean']:.1f} +/- {res[k]['ci95']:.1f} | {res[k]['macro_f1']:.1f} |")
    L += ["", "Intervals are 95% clustered on recording (n=36).", "",
          "## Paired permutation tests on per-recording differences", ""]
    for k, v in comps.items():
        L.append(f"- {k}: {v['mean_diff']:+.1f} points, p = {v['p_permutation']:.4f} (n = {v['n_recordings']})")
    open(os.path.join(RES, "stats_v2.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
