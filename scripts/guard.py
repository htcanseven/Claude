"""Applicability guards: send a design to trial when it lies outside what the calibration has seen.

Three guards act on the intervals of decisions.py (dec_intervals.csv) before the verdict is taken; a
guarded case abstains:
* family: the target's geometry is not among the calibration alternatives' geometries;
* range: the target lies outside the calibrated range of a descriptor: its geometry is not calibrated,
  or its blank-holder force lies outside the range of the calibration alternatives of its geometry;
* novelty: the target's simulated q95 (upper end of the simulation envelope) lies outside the range of
  the calibration alternatives' simulated q95. Like the range guard it uses design-stage information only.
The guards are evaluated where they can fire: new process settings (scope 'setting', where the range and
novelty guards fire for an extrapolated force) and a new family ('transfer'); with a produced sibling
(scope 'within') no guard fires. For every guard, scope and rule: the decisive and safe distances of the
guarded rule over all cases; the cases the guard lets through; right / wrong / trial counts at |d| = 10
floors among them (conditional rates); false alarms (guarded cases that the rule would have decided
correctly at |d| = 10) and misses (cases let through that the rule decides wrongly).

Outputs: results/dec_guard.csv, summary_guard.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS  # noqa: E402
from decisions import distances, with_relation_scopes  # noqa: E402

GUARDS = ("none", "family", "range", "novelty")
SCOPES = ("setting", "transfer")
D_CHECK = 10.0
N_BOOT = 1000


def guarded(iv: pd.DataFrame, guard: str) -> pd.Series:
    fam = ~pd.Series([g in c.split("|") for g, c in zip(iv["geometry"], iv["calib_geometries"])], index=iv.index)
    if guard == "family":
        return fam
    if guard == "range":
        return fam | (iv["bhf_kN"] < iv["calib_bhf_min"]) | (iv["bhf_kN"] > iv["calib_bhf_max"])
    if guard == "novelty":
        return (iv["sim_env_hi"] < iv["calib_env_min"]) | (iv["sim_env_hi"] > iv["calib_env_max"])
    return pd.Series(False, index=iv.index)


def outcomes_at(iv: pd.DataFrame, d: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Correct / wrong / trial counts per case at |d| (both sides; the failing side where feasible) and the
    number of verdicts."""
    q, F, lo, hi = (iv[c].to_numpy(float) for c in ("real_q95", "floor", "lo", "hi"))
    ra, rf = q + d * F, q - d * F
    feas = rf >= 0
    ok = (hi <= ra).astype(int) + (feas & (lo > rf)).astype(int)
    bad = (lo > ra).astype(int) + (feas & (hi <= rf)).astype(int)
    n = 1 + feas.astype(int)
    return ok, bad, n - ok - bad, n


def main() -> None:
    iv = pd.read_csv(RESULTS / "dec_intervals.csv")
    reps = np.load(RESULTS / "dec_q95_reps.npy")
    iv = with_relation_scopes(iv[iv["scope"].isin(SCOPES)])
    rows = []
    for guard in GUARDS:
        flag = guarded(iv, guard)
        gv = iv.assign(lo=np.where(flag, -np.inf, iv["lo"]), hi=np.where(flag, np.inf, iv["hi"]))
        dist = distances(gv, reps, n_boot=N_BOOT, per_qc=False).set_index(["scope", "method"])
        ok, bad, tri, n = outcomes_at(iv, D_CHECK)
        f = flag.to_numpy()
        for (scope, method), ix in iv.groupby(["scope", "method"]).indices.items():
            fi, keep = f[ix], ~f[ix]
            rows.append({"guard": guard, "scope": scope, "method": method,
                         "resolution_floors": dist.loc[(scope, method), "resolution_floors"],
                         "resolution_lo": dist.loc[(scope, method), "resolution_lo"],
                         "resolution_hi": dist.loc[(scope, method), "resolution_hi"],
                         "safe_floors": dist.loc[(scope, method), "safe_floors"],
                         "safe_lo": dist.loc[(scope, method), "safe_lo"], "safe_hi": dist.loc[(scope, method), "safe_hi"],
                         "cases": len(ix), "cases_guarded": int(fi.sum()),
                         "verdicts_through": int(n[ix][keep].sum()), "right_through": int(ok[ix][keep].sum()),
                         "wrong_through": int(bad[ix][keep].sum()), "trial_through": int(tri[ix][keep].sum()),
                         "false_alarms": int(ok[ix][fi].sum()), "verdicts_guarded": int(n[ix][fi].sum()),
                         "share_right_all": float((ok[ix] * keep).sum() / n[ix].sum()),
                         "share_wrong_all": float((bad[ix] * keep).sum() / n[ix].sum())})
    res = pd.DataFrame(rows)
    res["wrong_rate_through"] = res["wrong_through"] / res["verdicts_through"].replace(0, np.nan)
    res["false_alarm_rate"] = res["false_alarms"] / res["verdicts_guarded"].replace(0, np.nan)
    res.to_csv(RESULTS / "dec_guard.csv", index=False)
    show = res[res["method"].isin(["M1", "M2", "M3", "M5", "M5n", "NN"])]
    cols = ["guard", "scope", "method", "resolution_floors", "safe_floors", "cases", "cases_guarded",
            "verdicts_through", "right_through", "wrong_through", "trial_through", "wrong_rate_through",
            "false_alarms", "false_alarm_rate"]
    lines = ["# Applicability guards", "",
             f"New process settings and a new family; counts of verdicts at |d| = {D_CHECK:g} floors among the "
             "cases a guard lets through, and its false alarms.", "",
             show[cols].round(3).to_markdown(index=False)]
    (RESULTS / "summary_guard.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
