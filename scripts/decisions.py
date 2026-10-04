"""Design-stage decisions from simulation, scored against production.

For each of the 18 alternatives and each quality characteristic (QC), the
production verdict at a requirement R is *adequate* when at least
ADEQUATE_RATE of its 500 parts conform (y <= R; |y| <= R for two-sided QCs),
i.e. when the 95th percentile q95 of the parts is within R.

At the design stage only simulations exist. Three decision rules are scored
with each alternative held out in turn (leave-one-alternative-out), so that
every alternative is judged as a new design:

M0  nominal simulation: meets if the simulation at nominal sheet thickness and
    friction is within R, otherwise fails;
M1  bias-corrected simulation: as M0 after adding the median offset between
    the parts' q95 and the nominal simulation, learnt on the other alternatives;
M2  envelope with a calibrated margin: the upper end of the simulation envelope
    over plausible incoming conditions (all DDACS sheet thicknesses and friction
    coefficients for the geometry and blank-holder force) plus the median
    offset, with a split-conformal margin from the other alternatives' offsets.
    Meets if the upper bound is within R, fails if the lower bound exceeds R,
    otherwise uncertain (send to trial).

The requirement R sweeps the range of the parts' q95 values. The transfer test
calibrates M1/M2 on one geometry and applies them to the other.

Outputs: results/dec_alternatives.csv (per-alternative quantities),
dec_scores.csv (rates per method, QC and calibration), summary_decisions.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS, oil_to_friction  # noqa: E402
from qc import QCS, SHARED, parts_qc, sims_qc  # noqa: E402

ADEQUATE_RATE = 0.95
CONF_LEVEL = 0.90            # coverage of the split-conformal margin
NOMINAL_THICKNESS = 0.98     # mm; median of the measured sheet thickness is 0.985-0.99
NOMINAL_FRICTION = 0.10      # middle of the DDACS friction range
N_REQ = 41                   # requirement levels per QC


def transform(qc: str, v):
    return np.abs(v) if QCS[qc][2] == "abs" else v


def match_sims(parts: pd.DataFrame, sims: pd.DataFrame) -> pd.DataFrame:
    """Matched simulation of every part (rddac rule: geometry, force, nearest thickness and friction)."""
    out = []
    for (geo, bhf), g in parts.groupby(["geometry", "bhf_kN"]):
        cand = sims[(sims["geometry"] == geo) & (sims["bhf_kN"] == bhf)].reset_index(drop=True)
        if cand.empty:
            out.append(g.reset_index(drop=True).assign(**{f"sim_{c}": np.nan for c in SHARED}))
            continue
        t = g["sheet_um"].to_numpy() / 1000.0
        fc = np.array([oil_to_friction(o) if np.isfinite(o) else NOMINAL_FRICTION for o in g["oil_gm2"]])
        err = np.abs(cand["sheet_metal_thickness"].to_numpy()[None, :] - t[:, None]) + \
            np.abs(cand["friction_coefficient"].to_numpy()[None, :] - fc[:, None])
        best = np.nanargmin(np.where(np.isfinite(err), err, np.inf), axis=1)
        m = cand.iloc[best][SHARED].reset_index(drop=True)
        m.columns = [f"sim_{c}" for c in m.columns]
        out.append(pd.concat([g.reset_index(drop=True), m], axis=1))
    return pd.concat(out, ignore_index=True)


def alternative_table(parts: pd.DataFrame, sims: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for alt, g in parts.groupby("alternative"):
        geo, bhf = g["geometry"].iloc[0], int(g["bhf_kN"].iloc[0])
        env = sims[(sims["geometry"] == geo) & (sims["bhf_kN"] == bhf)]
        if env.empty:
            continue
        nom = env.iloc[[int(np.argmin(np.abs(env["sheet_metal_thickness"] - NOMINAL_THICKNESS)
                                      + np.abs(env["friction_coefficient"] - NOMINAL_FRICTION)))]]
        for qc in SHARED:
            y = transform(qc, g[qc].dropna().to_numpy())
            e = transform(qc, env[qc].dropna().to_numpy())
            ms = transform(qc, g[f"sim_{qc}"].dropna().to_numpy())
            if y.size < 20 or e.size == 0:
                continue
            rows.append({
                "alternative": alt, "geometry": geo, "bhf_kN": bhf, "oil_type": g["oil_type"].iloc[0], "qc": qc,
                "n_parts": int(y.size), "real_median": float(np.median(y)),
                "real_q95": float(np.quantile(y, ADEQUATE_RATE)), "real_sd": float(np.std(y)),
                "sim_nominal": float(transform(qc, nom[qc].to_numpy())[0]),
                "sim_env_lo": float(e.min()), "sim_env_hi": float(e.max()),
                "sim_matched_median": float(np.median(ms)) if ms.size else np.nan,
            })
    t = pd.DataFrame(rows)
    t["gap_matched"] = t["real_median"] - t["sim_matched_median"]
    return t


def conformal_margin(res: np.ndarray, level: float) -> float:
    n = res.size
    k = int(np.ceil((n + 1) * level))
    if k > n:
        return float(np.max(res)) if n else np.nan
    return float(np.sort(res)[k - 1])


def decide(t: pd.DataFrame, calib_mask, test_mask, qc: str, reqs: np.ndarray) -> list[dict]:
    """Verdicts of M0-M2 for the test alternatives at every requirement level."""
    c, s = t[calib_mask & (t["qc"] == qc)], t[test_mask & (t["qc"] == qc)]
    off1 = np.median(c["real_q95"] - c["sim_nominal"])
    r2 = c["real_q95"] - c["sim_env_hi"]
    off2 = np.median(r2)
    marg = conformal_margin(np.abs(r2 - off2).to_numpy(), CONF_LEVEL)
    out = []
    for _, a in s.iterrows():
        truth_adequate = a["real_q95"] <= reqs
        m0 = np.where(a["sim_nominal"] <= reqs, "meets", "fails")
        m1 = np.where(a["sim_nominal"] + off1 <= reqs, "meets", "fails")
        up, lo = a["sim_env_hi"] + off2 + marg, a["sim_env_hi"] + off2 - marg
        m2 = np.where(up <= reqs, "meets", np.where(lo > reqs, "fails", "uncertain"))
        for name, v in (("M0", m0), ("M1", m1), ("M2", m2)):
            for R, verdict, ok in zip(reqs, v, truth_adequate):
                out.append({"alternative": a["alternative"], "qc": qc, "method": name, "R": R, "verdict": verdict,
                            "adequate": bool(ok)})
    return out


def score(d: pd.DataFrame) -> pd.DataFrame:
    d = d.assign(
        correct=((d["verdict"] == "meets") & d["adequate"]) | ((d["verdict"] == "fails") & ~d["adequate"]),
        false_accept=(d["verdict"] == "meets") & ~d["adequate"],
        false_reject=(d["verdict"] == "fails") & d["adequate"],
        abstain=d["verdict"] == "uncertain",
    )
    return d.groupby(["calibration", "qc", "method"])[["correct", "false_accept", "false_reject", "abstain"]].mean()


def main() -> None:
    parts = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    parts = match_sims(parts, sims)
    t = alternative_table(parts, sims)
    t.to_csv(RESULTS / "dec_alternatives.csv", index=False)

    records = []
    alts = sorted(t["alternative"].unique())
    for qc in SHARED:
        tq = t[t["qc"] == qc]
        lo, hi = tq["real_q95"].min(), tq["real_q95"].max()
        span = hi - lo
        reqs = np.linspace(lo - 0.1 * span, hi + 0.1 * span, N_REQ)
        for a in alts:                                   # leave one alternative out
            for r in decide(t, t["alternative"] != a, t["alternative"] == a, qc, reqs):
                records.append({**r, "calibration": "loao"})
        for src, dst in (("concave", "convex"), ("convex", "concave")):   # transfer between geometries
            for r in decide(t, t["geometry"] == src, t["geometry"] == dst, qc, reqs):
                records.append({**r, "calibration": f"{src}->{dst}"})
    d = pd.DataFrame(records)
    sc = score(d).reset_index()
    sc.to_csv(RESULTS / "dec_scores.csv", index=False)
    overall = score(d.assign(qc="all")).reset_index()

    lines = ["# Design-stage decisions scored against production", "",
             f"Adequate: at least {ADEQUATE_RATE:.0%} of the parts conform. Margin coverage {CONF_LEVEL:.0%}. "
             f"Nominal simulation: t = {NOMINAL_THICKNESS} mm, friction {NOMINAL_FRICTION}.", "",
             "## Offsets between parts and matched simulations (median per alternative)", "",
             t.pivot_table(index="qc", columns="geometry", values="gap_matched", aggfunc="median").round(3).to_markdown(),
             "", "## Decision rates, all characteristics", "", overall.round(3).to_markdown(index=False), "",
             "## Decision rates per characteristic (leave-one-alternative-out)", "",
             sc[sc["calibration"] == "loao"].round(3).to_markdown(index=False)]
    (RESULTS / "summary_decisions.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
