"""Applicability guards: send a design to trial when it lies outside what the calibration has seen.

Across geometries every calibrated rule loses its safety (decisions.py, scope
'transfer'): the calibration alternatives are not exchangeable with the new
design. Two guards are applied to the intervals of decisions.py
(dec_intervals.csv) before the verdict is taken:

* family guard: the target's geometry is not among the calibration
  alternatives' geometries -> uncertain;
* novelty guard: the target's simulated q95 (upper end of the simulation
  envelope) lies outside the range spanned by the calibration alternatives'
  simulated q95 -> uncertain. It uses only design-stage information.

Within one geometry the envelope of a target equals that of the calibration
alternatives with the same blank-holder force, so the guards act on the
transfer scope only. Distances and rates are computed as in decisions.py.

Outputs: results/dec_guard.csv, summary_guard.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS  # noqa: E402
from decisions import D_GRID, distance_table  # noqa: E402

GUARDS = ("none", "family", "novelty")


def guarded(iv: pd.DataFrame, guard: str) -> pd.Series:
    if guard == "family":
        return ~pd.Series([g in c.split("|") for g, c in zip(iv["geometry"], iv["calib_geometries"])], index=iv.index)
    if guard == "novelty":
        return (iv["sim_env_hi"] < iv["calib_env_min"]) | (iv["sim_env_hi"] > iv["calib_env_max"])
    return pd.Series(False, index=iv.index)


def verdict_table(iv: pd.DataFrame, flag: pd.Series) -> pd.DataFrame:
    """Verdicts on the distance grid for every interval row; flagged rows abstain."""
    lo, hi = iv["lo"].to_numpy()[:, None], iv["hi"].to_numpy()[:, None]
    reqs = iv["real_q95"].to_numpy()[:, None] + D_GRID[None, :] * iv["floor"].to_numpy()[:, None]
    v = np.where(hi <= reqs, "meets", np.where(lo > reqs, "fails", "uncertain"))
    v[flag.to_numpy()] = "uncertain"
    n = len(D_GRID)
    return pd.DataFrame({"scope": np.repeat(iv["scope"].to_numpy(), n), "method": np.repeat(iv["method"].to_numpy(), n),
                         "qc": np.repeat(iv["qc"].to_numpy(), n), "alternative": np.repeat(iv["alternative"].to_numpy(), n),
                         "d": np.tile(D_GRID, len(iv)), "verdict": v.ravel(), "adequate": np.tile(D_GRID >= 0, len(iv))})


def main() -> None:
    iv = pd.read_csv(RESULTS / "dec_intervals.csv")
    rows = []
    for guard in GUARDS:
        flag = guarded(iv, guard)
        d = verdict_table(iv, flag)
        dist = distance_table(d, n_boot=200)
        dist = dist[dist["qc"] == "all"]
        at10 = d[d["d"].abs() == 10]
        ok = ((at10["verdict"] == "meets") & at10["adequate"]) | ((at10["verdict"] == "fails") & ~at10["adequate"])
        rates = pd.DataFrame({"scope": at10["scope"], "method": at10["method"], "correct": ok,
                              "uncertain": at10["verdict"] == "uncertain"}).groupby(["scope", "method"]).mean()
        share = flag.groupby([iv["scope"], iv["method"]]).mean().rename("share_guarded")
        out = dist.set_index(["scope", "method"]).join(rates).join(share).reset_index()
        out["wrong"] = 1 - out["correct"] - out["uncertain"]
        out.insert(0, "guard", guard)
        rows.append(out)
    res = pd.concat(rows, ignore_index=True)
    res.to_csv(RESULTS / "dec_guard.csv", index=False)
    show = res[res["scope"] == "transfer"][["guard", "method", "resolution_floors", "safe_floors", "correct",
                                             "wrong", "uncertain", "share_guarded"]]
    lines = ["# Applicability guards", "",
             "Transfer across geometries; correct / wrong / uncertain shares at |d| = 10 floors.", "",
             show.round(3).to_markdown(index=False)]
    (RESULTS / "summary_guard.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
