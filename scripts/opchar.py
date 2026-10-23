"""Operating characteristics of a design-stage decision rule: a small scoring module, independent of the pipeline.

A rule judges cases: a design treated as new, one characteristic. For each case it gives an interval [lo, hi]
for the decided statistic (lo = hi for a point rule); production gives the true value, and the case is scored in
a floor (any positive unit; in the paper the within-run floor of the characteristic). Requirements are upper
limits R = truth + d * floor at known distances d; the verdict is meets (hi <= R), fails (lo > R) or trial.

    distances(lo, hi, truth, floor)        decisive and safe distance, overall and per side
    guard_band(lo, hi, truth, floor)       the band of step 6 under a prior of requirement distances
    step6(lo, hi, truth, floor, band)      verdict shares of the rule with its interval widened by the band
    expected_cost(...)                     c_FA P(false accept) + c_FR P(false reject) + c_T P(trial)

The decisive distance is the smallest delta beyond which at least `target` of the verdicts at |d| = delta are
correct; the safe distance the smallest beyond which at most 1 - target are wrong. Every case gives one verdict on
an adequate design (d = +delta) and, where the requirement is feasible, one on a failing design (d = -delta);
for a non-negative characteristic a limit below zero is not a requirement. The distances are exact up to the
evaluation step: the verdict of a case changes only where delta crosses u = (hi - truth)/floor, v = (truth -
lo)/floor or their negatives.

Command line, for a CSV with the columns lo, hi, truth, floor and optionally a grouping column:
    python opchar.py cases.csv --group relation --prior-width 20
    python opchar.py --selfcheck           reproduces the distances of results/dec_resolution.csv (fits fixed)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

STEP = 0.05
GRID = np.round(np.arange(0.0, 600.0 + 1e-9, STEP), 2)        # evaluation points of delta (floors)
_POS = np.r_[np.arange(0.5, 10.01, 0.5), 12, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 300, 500]
EVAL_GRID = np.r_[-_POS[::-1], 0.0, _POS]                      # requirement distances of the paper's evaluation
BANDS = np.round(np.arange(0.0, 20.0 + 1e-9, 0.25), 2)


def _arrays(lo, hi, truth, floor, nonnegative: bool):
    lo, hi, q, F = (np.asarray(x, dtype=float) for x in (lo, hi, truth, floor))
    u, v = (hi - q) / F, (q - lo) / F
    u, v = np.where(np.isnan(u), np.inf, u), np.where(np.isnan(v), np.inf, v)   # no interval: never decides
    cap = np.where(q > 0, q / F, np.inf) if nonnegative else np.full(q.shape, np.inf)
    return u, v, cap


def share_curves(u: np.ndarray, v: np.ndarray, cap: np.ndarray, grid: np.ndarray = GRID) -> dict[str, np.ndarray]:
    """Shares of correct and wrong verdicts at every delta of the grid, overall and per side."""
    n = len(u)
    le = lambda a: np.searchsorted(np.sort(a), grid, side="right")  # noqa: E731
    lt = lambda a: np.searchsorted(np.sort(a), grid, side="left")   # noqa: E731
    pos = grid > 0
    n_cap = le(cap)
    feas = np.where(pos, n - n_cap, 0)
    a_ok, a_bad = le(u), n - le(-v)
    f_ok = np.where(pos, np.maximum(lt(v) - le(np.maximum(v, cap)), 0), 0)
    f_bad = np.where(pos, np.maximum((n - lt(-u)) - (n_cap - le(np.maximum(cap, -u))), 0), 0)
    with np.errstate(invalid="ignore", divide="ignore"):
        return {"correct": (a_ok + f_ok) / (n + feas), "wrong": (a_bad + f_bad) / (n + feas),
                "correct_adequate": a_ok / n, "wrong_adequate": a_bad / n,
                "correct_failing": np.where(feas > 0, f_ok / feas, np.nan),
                "wrong_failing": np.where(feas > 0, f_bad / feas, np.nan)}


def _first_beyond(share: np.ndarray, target: float, grid: np.ndarray = GRID) -> float:
    bad = np.flatnonzero(share < target)
    if bad.size == 0:
        return float(grid[0])
    return float(grid[bad[-1] + 1]) if bad[-1] + 1 < grid.size else np.inf


def distances(lo, hi, truth, floor, target: float = 0.95, nonnegative: bool = True, band: float = 0.0) -> dict:
    """Decisive and safe distances (floors) of a set of cases, overall and for adequate designs (false-reject
    side) and failing designs (false-accept side); band widens every interval by that many floors."""
    u, v, cap = _arrays(lo, hi, truth, floor, nonnegative)
    s = share_curves(u + band, v + band, cap)
    fb = lambda x: _first_beyond(x, target)  # noqa: E731
    return {"cases": int(len(u)), "decisive": fb(s["correct"]), "safe": fb(1 - s["wrong"]),
            "decisive_fr_side": fb(s["correct_adequate"]), "safe_fr_side": fb(1 - s["wrong_adequate"]),
            "decisive_fa_side": fb(s["correct_failing"]), "safe_fa_side": fb(1 - s["wrong_failing"])}


def prior_grid(width: float = 20.0) -> np.ndarray:
    """The reference prior of requirement distances: the evaluation grid within +-width floors, equal weights."""
    return EVAL_GRID[np.abs(EVAL_GRID) <= width]


def _verdicts(lo, hi, truth, floor, band: float, grid: np.ndarray, nonnegative: bool):
    lo, hi, q, F = (np.asarray(x, dtype=float)[:, None] for x in (lo, hi, truth, floor))
    reqs = q + grid[None, :] * F
    feas = reqs >= 0 if nonnegative else np.ones_like(reqs, dtype=bool)
    meets, fails = (hi + band * F <= reqs) & feas, (lo - band * F > reqs) & feas
    margin = np.where(meets, (reqs - hi) / F, np.where(fails, (lo - reqs) / F, np.nan))
    adequate = (grid >= 0)[None, :]
    return feas, meets, fails, adequate, margin


def guard_band(lo, hi, truth, floor, prior: np.ndarray | None = None, target: float = 0.95,
               bands: np.ndarray = BANDS, nonnegative: bool = True) -> float:
    """Smallest observable margin (floors) beyond which at least `target` of the decided verdicts were correct,
    for requirements at the distances of the prior (every feasible distance and case weighted equally). inf: no
    band on the search grid qualifies, so the procedure sends every design to trial."""
    grid = prior_grid() if prior is None else np.asarray(prior, dtype=float)
    feas, meets, fails, adequate, margin = _verdicts(lo, hi, truth, floor, 0.0, grid, nonnegative)
    correct = ((meets & adequate) | (fails & ~adequate)).ravel()
    m = margin.ravel()
    share = np.array([correct[np.isfinite(m) & (m >= b)].mean() if (np.isfinite(m) & (m >= b)).any() else np.nan
                      for b in bands])
    ok = np.where(np.isnan(share), True, share >= target)
    bad = np.flatnonzero(~ok)
    if bad.size == 0:
        return 0.0
    return float(bands[bad[-1] + 1]) if bad[-1] + 1 < bands.size else np.inf


def step6(lo, hi, truth, floor, band: float, prior: np.ndarray | None = None, nonnegative: bool = True) -> dict:
    """Shares of correct, false-accept, false-reject and trial verdicts over the prior with the band applied."""
    grid = prior_grid() if prior is None else np.asarray(prior, dtype=float)
    if not np.isfinite(band):
        return {"correct": 0.0, "false_accept": 0.0, "false_reject": 0.0, "trial": 1.0, "correct_when_decided": np.nan}
    feas, meets, fails, adequate, _ = _verdicts(lo, hi, truth, floor, band, grid, nonnegative)
    n = feas.sum()
    c = ((meets & adequate) | (fails & ~adequate)).sum()
    fa, fr = (meets & ~adequate).sum(), (fails & adequate).sum()
    dec = c + fa + fr
    return {"correct": c / n, "false_accept": fa / n, "false_reject": fr / n, "trial": (n - dec) / n,
            "correct_when_decided": c / dec if dec else np.nan}


def expected_cost(lo, hi, truth, floor, band: float, c_trial: float, c_fr: float = 0.5, c_fa: float = 1.0,
                  prior: np.ndarray | None = None, nonnegative: bool = True) -> float:
    """Expected cost per verdict over the prior, relative to the cost of a false accept."""
    s = step6(lo, hi, truth, floor, band, prior, nonnegative)
    return c_fa * s["false_accept"] + c_fr * s["false_reject"] + c_trial * s["trial"]


def score(df: pd.DataFrame, prior_width: float = 20.0, target: float = 0.95) -> dict:
    cols = [df[c].to_numpy(float) for c in ("lo", "hi", "truth", "floor")]
    prior = prior_grid(prior_width)
    g = guard_band(*cols, prior=prior, target=target)
    out = {**distances(*cols, target=target), "guard_band": g}
    if np.isfinite(g):
        w = distances(*cols, target=target, band=g)
        out.update({"decisive_step6": w["decisive"], "safe_step6": w["safe"]})
    out.update({f"step6_{k}": v for k, v in step6(*cols, g, prior).items()})
    return out


def selfcheck() -> None:
    """Reproduce the stored distances of every rule and scope (fits fixed) from the stored intervals."""
    results = Path(__file__).resolve().parents[1] / "results"
    iv = pd.read_csv(results / "dec_intervals.csv")
    res = pd.read_csv(results / "dec_resolution.csv")
    res = res[res["qc"] == "all"].set_index(["scope", "method"])
    bad = 0
    for (scope, m), g in iv.groupby(["scope", "method"]):
        d = distances(g["lo"], g["hi"], g["real_q95"], g["floor"])
        ref = res.loc[(scope, m)]
        if not (np.isclose(d["decisive"], ref["resolution_floors"]) and np.isclose(d["safe"], ref["safe_floors"])):
            bad += 1
            print(f"mismatch {scope} {m}: {d['decisive']}/{d['safe']} against {ref['resolution_floors']}/{ref['safe_floors']}")
    print("selfcheck:", "all distances reproduced" if bad == 0 else f"{bad} mismatches")
    sys.exit(1 if bad else 0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("csv", nargs="?", help="cases with the columns lo, hi, truth, floor")
    ap.add_argument("--group", help="column to score separately (e.g. relation)")
    ap.add_argument("--prior-width", type=float, default=20.0)
    ap.add_argument("--target", type=float, default=0.95)
    ap.add_argument("--selfcheck", action="store_true")
    a = ap.parse_args()
    if a.selfcheck:
        selfcheck()
    df = pd.read_csv(a.csv)
    groups = df.groupby(a.group) if a.group else [("all", df)]
    rows = [{"group": k, **score(g, a.prior_width, a.target)} for k, g in groups]
    print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
