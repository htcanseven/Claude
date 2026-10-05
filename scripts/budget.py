"""Calibration budget and calibration design: how many, and which, produced alternatives a rule needs.

decisions.py calibrates the rules on all other alternatives of a family (or on all but one force level).
Here the calibration set of a held-out alternative is every subset of size k = 1..8 of the other eight
alternatives of its geometry (255 subsets), and each (subset, target) pair is classified by how the target
relates to the produced evidence:
  sibling        the subset holds an alternative at the target's blank-holder force (another lubrication
                 pattern, which production mostly cannot tell apart: a near-replicate);
  interpolation  no sibling, and the subset's forces lie on both sides of the target's force;
  extrapolation  no sibling, and the target's force lies outside the subset's forces.
Rules: M1 (bias-corrected nominal simulation), M2 (envelope with the maximum-residual margin), M5 (GP
correction of the envelope, k >= 2), M5n (GP of q95 without the simulation, k >= 2) and NN (nearest produced
setting). The decisive and safe distances are computed exactly as in decisions.py over all (subset, target,
characteristic) cases of a class; subsets of one size have equal weight. Bands: 200 resamples of the held-out
alternatives within each geometry (fits fixed). Spread over subsets: the share of wrong verdicts at
|d| = 10 floors of each (subset, target) pair over its seven characteristics, as a distribution.

Outputs: results/budget_resolution.csv, budget_design.csv, summary_budget.md
"""

from __future__ import annotations

import itertools
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
from common import RESULTS  # noqa: E402
from qc import SHARED, sims_qc  # noqa: E402

RULES = ["M1", "M2", "M5", "M5n", "NN"]
RELATIONS = ["sibling", "interpolation", "extrapolation"]
N_BAND = 200
D_CHECK = 10.0


def classify(bhf_sub: np.ndarray, bhf_t: int) -> str:
    if bhf_t in bhf_sub:
        return "sibling"
    return "interpolation" if bhf_sub.min() < bhf_t < bhf_sub.max() else "extrapolation"


def wrong_at(u: np.ndarray, v: np.ndarray, cap: np.ndarray, d: float = D_CHECK) -> tuple[np.ndarray, np.ndarray]:
    """Wrong and trial verdict counts per case at |d| (adequate side, and failing side where feasible)."""
    feas = cap > d
    wrong = (-v > d).astype(int) + (feas & (-u >= d)).astype(int)
    right = (u <= d).astype(int) + (feas & (v < d)).astype(int)
    n = 1 + feas.astype(int)
    return wrong, n - wrong - right, n


def main() -> None:
    warnings.filterwarnings("ignore", module="sklearn")      # bound hits are reported by decisions.py
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    D.setup(t, sims, D.load_floors())
    floors = D._CTX["floors"]
    alts = sorted(t["alternative"].unique())
    aid = {a: i for i, a in enumerate(alts)}
    store = {}                                  # (k, rule, relation) -> list of (u, v, cap, target, pair id)
    pair_id = {}                                # (target, subset) -> id, shared by its characteristics
    for qc in SHARED:
        for geo, g in t[t["qc"] == qc].groupby("geometry"):
            g = g.set_index("alternative")
            F = floors[(qc, geo)]
            for a in g.index:
                o = g.drop(index=a)
                r1 = (o["real_q95"] - o["sim_nominal"]).to_numpy()
                r2 = (o["real_q95"] - o["sim_env_hi"]).to_numpy()
                bhf = np.array([D.bhf_of(x) for x in o.index])
                q, env, nom = g.loc[a, "real_q95"], g.loc[a, "sim_env_hi"], g.loc[a, "sim_nominal"]
                for k in range(1, len(o) + 1):
                    for sub in itertools.combinations(range(len(o)), k):
                        sub = list(sub)
                        rel = classify(bhf[sub], D.bhf_of(a))
                        calib = list(o.index[sub])
                        off2 = np.median(r2[sub])
                        marg2 = D.conformal_margin(np.abs(r2[sub] - off2), D.CONF_LEVEL)
                        p1 = nom + np.median(r1[sub])
                        ivs = {"M1": (p1, p1), "M2": (env + off2 - marg2, env + off2 + marg2),
                               "NN": (D.nn_point(calib, a, qc),) * 2}
                        if k >= 2:
                            ivs["M5"] = D.m5_interval(calib, a, qc, env)
                            ivs["M5n"] = D.m5_interval(calib, a, qc, 0.0, use_sim=False)
                        pid = pair_id.setdefault((a, tuple(calib)), len(pair_id))
                        for rule, (lo, hi) in ivs.items():
                            store.setdefault((k, rule, rel), []).append(((hi - q) / F, (q - lo) / F, q / F, aid[a], pid))
    rng = np.random.default_rng(D.SEED)
    fam = np.array([a.split("/")[0] for a in alts])
    idx = np.concatenate([rng.choice(np.flatnonzero(fam == f), (N_BAND, int((fam == f).sum())))
                          for f in np.unique(fam)], axis=1)
    res, des = [], []
    for rel_set in [("all", RELATIONS)] + [(r, [r]) for r in RELATIONS]:
        name, members = rel_set
        for k in range(1, 9):
            for rule in RULES:
                parts = [np.array(store[(k, rule, r)]) for r in members if (k, rule, r) in store]
                if not parts:
                    continue
                arr = np.vstack(parts)
                u, v, cap, tgt, un = arr[:, 0], arr[:, 1], arr[:, 2], arr[:, 3].astype(int), arr[:, 4]
                u, v = np.where(np.isnan(u), np.inf, u), np.where(np.isnan(v), np.inf, v)
                dist = D.distance_pair(u, v, cap)
                wrong, trial, n = wrong_at(u, v, cap)
                by_t = [np.flatnonzero(tgt == i) for i in range(len(alts))]
                bd, bs = [], []
                for b in range(N_BAND):
                    sel = np.concatenate([by_t[i] for i in idx[b]])
                    r = D.distance_pair(u[sel], v[sel], cap[sel])
                    bd.append(r["resolution_floors"])
                    bs.append(r["safe_floors"])
                per_unit = pd.DataFrame({"u": un, "w": wrong, "n": n}).groupby("u")[["w", "n"]].sum()
                share = per_unit["w"] / per_unit["n"]
                row = {"relation": name, "k": k, "method": rule, "cases": len(u), **dist,
                       "resolution_lo": float(np.percentile(bd, 2.5)), "resolution_hi": float(np.percentile(bd, 97.5)),
                       "safe_lo": float(np.percentile(bs, 2.5)), "safe_hi": float(np.percentile(bs, 97.5)),
                       "error_at_10": float(wrong.sum() / n.sum()), "abstain_at_10": float(trial.sum() / n.sum()),
                       "pairs": len(share), "pairs_with_wrong_at_10": float((share > 0).mean()),
                       "wrong_share_p90": float(share.quantile(0.9))}
                (res if name == "all" else des).append(row)
    res, des = pd.DataFrame(res), pd.DataFrame(des)
    res.to_csv(RESULTS / "budget_resolution.csv", index=False)
    des.to_csv(RESULTS / "budget_design.csv", index=False)
    cols = ["relation", "k", "method", "cases", "resolution_floors", "resolution_lo", "resolution_hi", "safe_floors",
            "safe_lo", "safe_hi", "error_at_10", "abstain_at_10", "pairs_with_wrong_at_10", "wrong_share_p90"]
    lines = ["# Calibration budget and calibration design", "",
             f"Within-geometry calibration on every subset of k of the other alternatives; interval level "
             f"{D.CONF_LEVEL:.0%}; target {D.RESOLUTION_TARGET:.0%}; bands from {N_BAND} resamples of the targets.", "",
             "## All subsets", "", res[cols].round(3).to_markdown(index=False), "",
             "## By the relation of the target to the subset", "", des[cols].round(3).to_markdown(index=False)]
    (RESULTS / "summary_budget.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:30]))


if __name__ == "__main__":
    main()
