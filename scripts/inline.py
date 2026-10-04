"""In-line verifiability of the quality characteristics from the press-force record.

In production the alternative is known, so the question is whether the force
record of a part reveals how far its quality characteristic (QC) deviates
from the alternative's typical value. For every QC:

* deviation y = QC - median of its alternative; features are the force and
  incoming-condition signals, centred and scaled within the alternative;
* a gradient-boosting regressor (depth 3, 200 iterations, learning rate 0.08,
  random state 0) predicts y out of fold, with folds formed by production
  batches (GroupKFold over alternative x batch), so neighbouring parts never
  sit on both sides of a split;
* the limit of detection LOD = (z_{1-a} + z_{1-b}) * s_e with a = b = 0.05,
  s_e the robust SD of the out-of-fold error: the smallest deviation flagged
  with 95 % probability at a 5 % false-alarm rate;
* detection of the parts beyond their alternative's 95th percentile: recall
  at a 5 % false-alarm threshold on the predicted deviation.

Outputs: results/inline_lod.csv, summary_inline.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import GroupKFold

sys.path.insert(0, str(Path(__file__).resolve().parent))
from alternatives import BATCH  # noqa: E402
from common import RESULTS, robust_sd  # noqa: E402
from qc import QCS, SHARED, parts_qc  # noqa: E402

FEATURES = ["F10_kN", "F20_kN", "F25_kN", "W_draw_J", "F_peak_kN", "imbalance20", "punch_temp_C", "sheet_um",
            "oil_gm2"]
GBR = dict(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
N_FOLDS = 5
ALPHA = BETA = 0.05


def within(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    g = df.groupby("alternative")[cols]
    return (df[cols] - g.transform("median")) / g.transform(lambda v: robust_sd(v.to_numpy()) or 1.0)


def main() -> None:
    q = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    q["batch"] = q.groupby("alternative").cumcount() // BATCH
    q["group"] = q["alternative"] + "#" + q["batch"].astype(str)
    X_all = within(q, FEATURES)
    rows = []
    for qc in SHARED:
        y = q[qc] - q.groupby("alternative")[qc].transform("median")
        m = y.notna() & X_all.notna().all(axis=1)
        X, yv, grp = X_all[m].to_numpy(), y[m].to_numpy(), q.loc[m, "group"].to_numpy()
        pred = np.full(yv.size, np.nan)
        n_splits = min(N_FOLDS, len(np.unique(grp)))
        if n_splits < 2:
            continue
        for tr, te in GroupKFold(n_splits).split(X, yv, grp):
            pred[te] = HistGradientBoostingRegressor(**GBR).fit(X[tr], yv[tr]).predict(X[te])
        err = yv - pred
        s_e, s_y = robust_sd(err), robust_sd(yv)
        lod = (norm.ppf(1 - ALPHA) + norm.ppf(1 - BETA)) * s_e
        # parts beyond their alternative's 95th percentile
        alt = q.loc[m, "alternative"].to_numpy()
        thr = pd.Series(yv).groupby(alt).transform(lambda v: np.quantile(v, 0.95)).to_numpy()
        out_tol = yv > thr
        alarm_thr = np.quantile(pred[~out_tol], 1 - ALPHA)
        recall = float(np.mean(pred[out_tol] > alarm_thr)) if out_tol.any() else np.nan
        r2 = 1 - np.sum(err ** 2) / np.sum((yv - yv.mean()) ** 2)
        rows.append({"qc": qc, "label": QCS[qc][0], "unit": QCS[qc][1], "n": int(yv.size), "r2_oof": float(r2),
                     "sd_within": s_y, "sd_error": s_e, "lod": float(lod), "lod_over_sd": float(lod / s_y),
                     "recall_top5_at_fa5": recall})
    t = pd.DataFrame(rows)
    t.to_csv(RESULTS / "inline_lod.csv", index=False)
    lines = ["# In-line verifiability from the force record", "",
             f"Gradient boosting {GBR}; {N_FOLDS}-fold GroupKFold over production batches of {BATCH}.", "",
             t.round(4).to_markdown(index=False)]
    (RESULTS / "summary_inline.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
