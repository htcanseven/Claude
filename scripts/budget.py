"""Calibration budget: how many produced alternatives the simulation needs before its decisions resolve.

decisions.py calibrates the bias-corrected rule (M1), the envelope rule with
a conformal margin (M2) and the Gaussian-process calibration (M5, from k = 2)
on all other alternatives of the same geometry (eight).
Here the calibration set is every subset of size k = 1..8 of those alternatives
(all 255 subsets per held-out alternative), and the verdicts at each
requirement distance d are scored as in decisions.py; subsets of one size have
equal weight. The decisive and safe distances (decisions.py) against k are
the production evidence a design team needs before simulation-based decisions
become reliable. M3 is left out because every subset would need a refit and a
nested leave-one-out.

Outputs: results/budget_curve.csv, budget_resolution.csv, summary_budget.md
"""

from __future__ import annotations

import itertools
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions  # noqa: E402
from common import RESULTS  # noqa: E402
from decisions import CONF_LEVEL, D_GRID, RESOLUTION_TARGET, beyond, conformal_margin, m5_interval  # noqa: E402
from qc import SHARED  # noqa: E402

OUTCOMES = ["correct", "false_accept", "false_reject", "abstain"]


def outcome_counts(verdict: np.ndarray, adequate: np.ndarray) -> np.ndarray:
    """Rows: correct, false accept, false reject, abstain; columns: requirement distances."""
    return np.vstack([((verdict == "meets") & adequate) | ((verdict == "fails") & ~adequate),
                      (verdict == "meets") & ~adequate, (verdict == "fails") & adequate,
                      verdict == "uncertain"]).astype(float)


def main() -> None:
    warnings.filterwarnings("ignore", module="sklearn")      # GP hyperparameters at their bounds for small k
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    decisions._CTX["t"] = t                                   # M5 fits are cached per calibration set
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    adequate = D_GRID >= 0
    acc = {}                                   # (k, method, qc) -> [sum of outcome rows, n]
    for qc in SHARED:
        for geo, g in t[t["qc"] == qc].groupby("geometry"):
            g = g.set_index("alternative")
            F = float(fl.loc[qc, f"floor_{geo}"])
            for a in g.index:
                o = g.drop(index=a)
                r1 = (o["real_q95"] - o["sim_nominal"]).to_numpy()
                r2 = (o["real_q95"] - o["sim_env_hi"]).to_numpy()
                reqs = g.loc[a, "real_q95"] + D_GRID * F
                for k in range(1, len(o) + 1):
                    for sub in itertools.combinations(range(len(o)), k):
                        sub = list(sub)
                        off1, off2 = np.median(r1[sub]), np.median(r2[sub])
                        marg2 = conformal_margin(np.abs(r2[sub] - off2), CONF_LEVEL)
                        m1 = np.where(g.loc[a, "sim_nominal"] + off1 <= reqs, "meets", "fails")
                        lo, hi = g.loc[a, "sim_env_hi"] + off2 - marg2, g.loc[a, "sim_env_hi"] + off2 + marg2
                        m2 = np.where(hi <= reqs, "meets", np.where(lo > reqs, "fails", "uncertain"))
                        rules = [("M1", m1), ("M2", m2)]
                        if k >= 2:
                            lo5, hi5 = m5_interval(list(o.index[sub]), a, qc, g.loc[a, "sim_env_hi"])
                            rules.append(("M5", np.where(hi5 <= reqs, "meets",
                                                         np.where(lo5 > reqs, "fails", "uncertain"))))
                        for name, v in rules:
                            key = (k, name, qc)
                            s, n = acc.get(key, (0.0, 0))
                            acc[key] = (s + outcome_counts(v, adequate), n + 1)
    rows = []
    for (k, name, qc), (s, n) in acc.items():
        for j, d in enumerate(D_GRID):
            rows.append({"k": k, "method": name, "qc": qc, "d": float(d), "n": n,
                         **{o: s[i, j] / n for i, o in enumerate(OUTCOMES)}})
    curve = pd.DataFrame(rows)
    curve.to_csv(RESULTS / "budget_curve.csv", index=False)
    curve["not_wrong"] = curve["correct"] + curve["abstain"]
    res = []
    for (k, name), g in curve.groupby(["k", "method"]):
        at10 = g[g["d"].abs() == 10]
        res.append({"k": k, "method": name, "qc": "all",
                    "resolution_floors": beyond(g.groupby(g["d"].abs())["correct"].mean()),
                    "safe_floors": beyond(g.groupby(g["d"].abs())["not_wrong"].mean()),
                    "abstain_at_10": float(at10["abstain"].mean()),
                    "error_at_10": float((at10["false_accept"] + at10["false_reject"]).mean())})
        for qc, h in g.groupby("qc"):
            res.append({"k": k, "method": name, "qc": qc,
                        "resolution_floors": beyond(h.groupby(h["d"].abs())["correct"].mean()),
                        "safe_floors": beyond(h.groupby(h["d"].abs())["not_wrong"].mean())})
    res = pd.DataFrame(res)
    res.to_csv(RESULTS / "budget_resolution.csv", index=False)
    lines = ["# Calibration budget", "",
             f"Within-geometry calibration on every subset of k of the other alternatives; conformal coverage "
             f"{CONF_LEVEL:.0%}; resolution target {RESOLUTION_TARGET:.0%} correct.", "",
             "## Decisive distance (production floors) against k", "",
             res.pivot_table(index="qc", columns=["method", "k"], values="resolution_floors").round(1).to_markdown(),
             "", "## Safe distance (production floors) against k", "",
             res.pivot_table(index="qc", columns=["method", "k"], values="safe_floors").round(1).to_markdown(),
             "", "## All characteristics: abstention and error at |d| = 10 floors", "",
             res[res["qc"] == "all"].round(3).to_markdown(index=False)]
    (RESULTS / "summary_budget.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
