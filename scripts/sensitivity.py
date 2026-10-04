"""Sensitivity of the production floor and its conclusions to the constants fixed in advance.

The floor (alternatives.py) rests on three choices made before the analysis:
the batch size BATCH (50 consecutive parts), the quantile ALPHA (0.95) and the
batch centre (10 % trimmed mean). For every batch size in BATCHES, quantile in
ALPHAS and centre in STATS this script recomputes

* the floor of each quality characteristic (QC), pooled and per geometry;
* the share of single-factor contrasts between alternatives with ESR >= 1, per
  factor family (geometry, blank-holder force, lubrication);
* the minimum resolvable change of blank-holder force.

It also splits the floor at the reference choices into scatter and drift.
The scatter floor is the floor after the parts of each alternative have been
permuted (N_PERM permutations, seed SEED): the time order is gone, so only
the scatter of batch centres of independent parts remains. The ratio of the
floor to the scatter floor is the inflation caused by drift within a series.

Outputs: results/sens_floor.csv, sens_esr.csv, sens_drift.csv, summary_sensitivity.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from alternatives import ALPHA, BATCH, analyse, batch_centres, batches, floor_from  # noqa: E402
from common import RESULTS  # noqa: E402
from qc import QCS, parts_qc  # noqa: E402

BATCHES = [25, 50, 100]
ALPHAS = [0.90, 0.95, 0.99]
STATS = ["trim", "median"]
REFERENCE = (BATCH, ALPHA, "trim")
N_PERM = 50
SEED = 1
GEOMETRIES = ("concave", "convex")


def grid(q: pd.DataFrame, qcs: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    fl_rows, esr_rows = [], []
    for b in BATCHES:
        qb = batches(q, b)
        for st in STATS:
            bm_geo = {g: batch_centres(qb[qb["geometry"] == g], qcs, b, st) for g in GEOMETRIES}
            for a in ALPHAS:
                res = analyse(qb, qcs, alpha=a, size=b, stat=st)
                ref = (b, a, st) == REFERENCE
                m = res["mrc"].set_index(["qc", "factor"])["mrc"]
                for c in qcs:
                    fl_rows.append({"batch": b, "alpha": a, "stat": st, "reference": ref, "qc": c,
                                    "floor": res["floors"][c],
                                    **{f"floor_{g}": floor_from(bm_geo[g], c, a) for g in GEOMETRIES},
                                    "mrc_bhf_kN": m.loc[(c, "bhf_kN")]})
                e = res["effects"]
                share = e.assign(res=e["esr"] >= 1).groupby(["qc", "family"])["res"].mean()
                esr_rows += [{"batch": b, "alpha": a, "stat": st, "reference": ref, "qc": c, "family": fam,
                              "share_resolvable": v} for (c, fam), v in share.items()]
    return pd.DataFrame(fl_rows), pd.DataFrame(esr_rows)


def drift(q: pd.DataFrame, qcs: list[str]) -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    bm = batch_centres(batches(q, BATCH), qcs)
    floor = {c: floor_from(bm, c) for c in qcs}
    groups = list(q.groupby("alternative", sort=False).indices.values())
    perm = {c: [] for c in qcs}
    for _ in range(N_PERM):
        order = np.concatenate([rng.permutation(ix) for ix in groups])
        bp = batch_centres(batches(q.iloc[order].reset_index(drop=True), BATCH), qcs)
        for c in qcs:
            perm[c].append(floor_from(bp, c))
    rows = []
    for c in qcs:
        p = np.array(perm[c])
        rows.append({"qc": c, "floor": floor[c], "scatter_floor": float(np.median(p)),
                     "scatter_floor_lo": float(np.percentile(p, 2.5)),
                     "scatter_floor_hi": float(np.percentile(p, 97.5)),
                     "drift_inflation": floor[c] / float(np.median(p))})
    return pd.DataFrame(rows)


def main() -> None:
    q = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    qcs = list(QCS)
    fl, esr = grid(q, qcs)
    fl.to_csv(RESULTS / "sens_floor.csv", index=False)
    esr.to_csv(RESULTS / "sens_esr.csv", index=False)
    dr = drift(q, qcs)
    dr.to_csv(RESULTS / "sens_drift.csv", index=False)

    ref = fl[fl["reference"]].set_index("qc")["floor"]
    cols = ["stat", "batch", "alpha"]
    rel = fl.assign(rel=fl["floor"] / fl["qc"].map(ref)).pivot_table(index="qc", columns=cols, values="rel")
    share = esr.pivot_table(index="family", columns=cols, values="share_resolvable", aggfunc="mean")
    mrc = fl.pivot_table(index="qc", columns=cols, values="mrc_bhf_kN")
    lines = ["# Sensitivity of the production floor to batch size, quantile and batch centre", "",
             f"Reference: batch {REFERENCE[0]}, alpha {REFERENCE[1]}, centre {REFERENCE[2]} (10 % trimmed mean). "
             f"Scatter floor from {N_PERM} within-alternative permutations (seed {SEED}).", "",
             "## Floor relative to the reference", "", rel.round(2).to_markdown(), "",
             "## Share of single-factor contrasts with ESR >= 1 (mean over characteristics)", "",
             share.round(2).to_markdown(), "",
             "## Minimum resolvable change of blank-holder force (kN)", "", mrc.round(0).to_markdown(), "",
             "## Floor against the scatter floor (drift inflation)", "", dr.round(4).to_markdown(index=False)]
    (RESULTS / "summary_sensitivity.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
