"""A2 — separate band-limiting from sampling rate (the Nyquist question).

The paper reports 25 Hz as the best sampling rate while arguing elsewhere that
the shaft rotational fundamental carries the discriminative content. Shaft
speeds in this dataset span 13.1-24.9 Hz, all of which lie above the 12.5 Hz
Nyquist frequency of a 25 Hz stream, so proper decimation removes every one of
them. This experiment establishes which effect is actually responsible:

  (a) 100 Hz, unmodified                      -- full band, full rate
  (b) 100 Hz, low-pass filtered at 12.5 Hz    -- same band as (c), full rate
  (c) 25 Hz, polyphase decimation             -- same band as (b), quarter rate
  (d) 25 Hz, subsampled with no anti-alias    -- quarter rate, content aliased

(a)->(b) isolates band-limiting, (b)->(c) isolates rate and window sample count,
(c)->(d) isolates aliasing.
"""
from __future__ import annotations
import os, json
import numpy as np
import protocols_v2 as P

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]

CONDS = [
    ("a_100hz_full",      dict(resampler=P.rs_identity,            fs_out=100.0), "100 Hz, unmodified"),
    ("b_100hz_lp12.5",    dict(resampler=P.rs_lowpass_only(12.5),  fs_out=100.0), "100 Hz, low-pass 12.5 Hz"),
    ("c_25hz_decimated",  dict(resampler=P.rs_polyphase(4),        fs_out=25.0),  "25 Hz, anti-alias decimation"),
    ("d_25hz_aliased",    dict(resampler=P.rs_naive_decimate(4),   fs_out=25.0),  "25 Hz, no anti-alias filter"),
]


def main():
    out = {}
    for key, kw, label in CONDS:
        d = P.build_custom(win_sec=2.0, overlap=0.5, **kw)
        accs, f1s, pers = [], [], []
        for s in SEEDS:
            a, f, per = P.eval_group(d, s)
            accs.append(a); f1s.append(f); pers.append(per)
            print(f"  {key} seed {s}: {100*a:.1f}%")
        m, h, n, per_rec = P.clustered_ci(pers)
        out[key] = dict(label=label, windows=int(d["X"].shape[0]),
                        feat_dim=int(d["X"].shape[1]),
                        acc_mean=float(100*np.mean(accs)), acc_ci95=h,
                        n_recordings=n, macro_f1=float(100*np.mean(f1s)),
                        per_recording=per_rec, per_seed=[float(100*a) for a in accs])
        print(f"{key:20s} {label:32s} -> {out[key]['acc_mean']:.1f} +/- {h:.1f} "
              f"(macro-F1 {out[key]['macro_f1']:.1f}, {out[key]['windows']} windows)")
    json.dump(out, open(os.path.join(RES, "antialias.json"), "w"), indent=2)

    L = ["# A2 - band-limiting vs sampling rate (GROUP protocol, RF-200, 5 seeds)", "",
         "| condition | windows | accuracy (%) | macro-F1 (%) |", "|---|---|---|---|"]
    for key, _, label in CONDS:
        r = out[key]
        L.append(f"| {label} | {r['windows']} | {r['acc_mean']:.1f} +/- {r['acc_ci95']:.1f} | {r['macro_f1']:.1f} |")
    a, b = out["a_100hz_full"], out["b_100hz_lp12.5"]
    c, dd = out["c_25hz_decimated"], out["d_25hz_aliased"]
    L += ["", "## Decomposition", "",
          f"- band-limiting alone (a->b): {b['acc_mean']-a['acc_mean']:+.1f} points",
          f"- rate/sample-count (b->c):   {c['acc_mean']-b['acc_mean']:+.1f} points",
          f"- aliasing (c->d):            {dd['acc_mean']-c['acc_mean']:+.1f} points",
          f"- total (a->c):               {c['acc_mean']-a['acc_mean']:+.1f} points"]
    open(os.path.join(RES, "antialias.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[-6:]))


if __name__ == "__main__":
    main()
