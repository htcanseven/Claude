"""A1 - decompose the optimism gap into its mechanisms.

The paper attributes the collapse from ~100% to ~53% to two causes at once:
overlapping windows sharing samples, and windows inheriting the identity of
their recording. Those are separable, and a third cause (temporal proximity
within a recording) sits between them. Ladder of partitionings, each removing
one more source:

  RANDOM (50% overlap)      shared samples + proximity + recording identity
  RANDOM (no overlap)       proximity + recording identity
  BLOCKED (no overlap)      recording identity only
  GROUP                     none of the three
  CROSS-SPEED / CROSS-LOAD  none, plus a deliberate operating-condition shift

Successive differences attribute the gap to each mechanism.
"""
from __future__ import annotations
import os, json
import numpy as np
import protocols_v2 as P

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]


def run(d, fn, tag, **kw):
    accs, f1s, pers = [], [], []
    for s in SEEDS:
        a, f, per = fn(d, s, **kw)
        accs.append(a); f1s.append(f); pers.append(per)
    m, h, n, per_rec = P.clustered_ci(pers)
    print(f"  {tag:34s} {100*np.mean(accs):5.1f} +/- {h:4.1f}")
    return dict(acc_mean=float(100*np.mean(accs)), acc_ci95=h, n_recordings=n,
                macro_f1=float(100*np.mean(f1s)), per_recording=per_rec)


def main():
    print("building feature matrices...")
    d_ov = P.build_custom(win_sec=2.0, overlap=0.5)    # as used throughout the paper
    d_no = P.build_custom(win_sec=2.0, overlap=0.0)    # non-overlapping windows
    print(f"  overlapping: {d_ov['X'].shape[0]} windows; non-overlapping: {d_no['X'].shape[0]}")

    out = {"n_windows_overlap": int(d_ov["X"].shape[0]),
           "n_windows_nonoverlap": int(d_no["X"].shape[0])}
    print("evaluating...")
    out["random_overlap"]    = run(d_ov, P.eval_random,  "RANDOM, 50% overlap")
    out["random_nonoverlap"] = run(d_no, P.eval_random,  "RANDOM, no overlap")
    out["blocked_nonoverlap"]= run(d_no, P.eval_blocked, "BLOCKED within recording")
    out["group_nonoverlap"]  = run(d_no, P.eval_group,   "GROUP, no overlap")
    out["group_overlap"]     = run(d_ov, P.eval_group,   "GROUP, 50% overlap (paper)")
    out["cross_speed"]       = run(d_ov, P.eval_leave_one, "CROSS-SPEED", key="speed")
    out["cross_load"]        = run(d_ov, P.eval_leave_one, "CROSS-LOAD",  key="load")
    json.dump(out, open(os.path.join(RES, "leakage_decomposition.json"), "w"), indent=2)

    g = lambda k: out[k]["acc_mean"]
    L = ["# A1 - decomposition of the optimism gap (RF-200, 5 seeds)", "",
         "| partitioning | leakage sources retained | accuracy (%) | macro-F1 (%) |",
         "|---|---|---|---|",
         f"| RANDOM, 50% overlap | shared samples, proximity, recording identity | {g('random_overlap'):.1f} +/- {out['random_overlap']['acc_ci95']:.1f} | {out['random_overlap']['macro_f1']:.1f} |",
         f"| RANDOM, no overlap | proximity, recording identity | {g('random_nonoverlap'):.1f} +/- {out['random_nonoverlap']['acc_ci95']:.1f} | {out['random_nonoverlap']['macro_f1']:.1f} |",
         f"| BLOCKED within recording | recording identity | {g('blocked_nonoverlap'):.1f} +/- {out['blocked_nonoverlap']['acc_ci95']:.1f} | {out['blocked_nonoverlap']['macro_f1']:.1f} |",
         f"| GROUP, no overlap | none | {g('group_nonoverlap'):.1f} +/- {out['group_nonoverlap']['acc_ci95']:.1f} | {out['group_nonoverlap']['macro_f1']:.1f} |",
         f"| GROUP, 50% overlap | none | {g('group_overlap'):.1f} +/- {out['group_overlap']['acc_ci95']:.1f} | {out['group_overlap']['macro_f1']:.1f} |",
         f"| CROSS-SPEED | none, + speed shift | {g('cross_speed'):.1f} +/- {out['cross_speed']['acc_ci95']:.1f} | {out['cross_speed']['macro_f1']:.1f} |",
         f"| CROSS-LOAD | none, + load shift | {g('cross_load'):.1f} +/- {out['cross_load']['acc_ci95']:.1f} | {out['cross_load']['macro_f1']:.1f} |",
         "", "## Attribution (successive differences)", "",
         f"- window overlap (shared samples): {g('random_overlap')-g('random_nonoverlap'):+.1f} points",
         f"- temporal proximity:              {g('random_nonoverlap')-g('blocked_nonoverlap'):+.1f} points",
         f"- recording identity:              {g('blocked_nonoverlap')-g('group_nonoverlap'):+.1f} points",
         f"- total optimism gap:              {g('random_overlap')-g('group_nonoverlap'):+.1f} points"]
    open(os.path.join(RES, "leakage_decomposition.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[-6:]))


if __name__ == "__main__":
    main()
