"""Design-stage decisions from simulation, scored against production.

For each of the 18 alternatives and each quality characteristic (QC), the
production verdict at a requirement R is *adequate* when at least
ADEQUATE_RATE of its 500 parts conform (y <= R; |y| <= R for two-sided QCs),
i.e. when the 95th percentile q95 of the parts is within R.

At the design stage only simulations exist. Four decision rules are scored
with each alternative held out in turn, so that every alternative is judged
as a new design. Three calibrations: *within* the design family (the other
alternatives of the same geometry), *pooled* (all other alternatives) and
*transfer* (only the alternatives of the other geometry):

M0  nominal simulation: meets if the simulation at nominal sheet thickness and
    friction is within R, otherwise fails;
M1  bias-corrected simulation: as M0 after adding the median offset between
    the parts' q95 and the nominal simulation of the calibration alternatives;
M2  envelope with a calibrated margin: the upper end of the simulation envelope
    over plausible incoming conditions (all DDACS sheet thicknesses and friction
    coefficients at the geometry and blank-holder force) plus the median offset,
    with a split-conformal margin from the calibration alternatives' offsets.
    Meets if the upper bound is within R, fails if the lower bound exceeds R,
    otherwise uncertain (send to trial);
M3  simulation corrected by machine learning: a gradient-boosting model learns,
    on the parts of the calibration alternatives, the measured QC from the
    matched simulation, the design and process descriptors (geometry,
    blank-holder force, lubrication pattern) and the incoming conditions. For
    the new alternative the incoming conditions are drawn from calibration
    parts with the same lubrication pattern (none of its own measurements are
    used); the predicted q95 gets an offset and a conformal margin from a
    nested leave-one-out over the calibration alternatives. Verdicts as M2.

Requirements are placed at fixed distances d from each alternative's true q95,
measured in production floors F of the characteristic (alternatives.py):
R = q95 + d F, so the alternative is adequate exactly when d >= 0. Two
distances summarise a rule: the decisive distance (resolution) is the
smallest |d| beyond which at least RESOLUTION_TARGET of its verdicts are
correct (an abstention is not correct), the decision-level counterpart of a
limit of detection; the safe distance is the smallest |d| beyond which at
most 1 - RESOLUTION_TARGET of its verdicts are wrong (an abstention is not
wrong). For rules that always decide (M0, M1) the two coincide. The transfer
test calibrates on one geometry and applies the rules to the other.

Outputs: results/dec_alternatives.csv, dec_margins.csv, dec_verdicts.csv.gz,
dec_scores.csv, summary_decisions.md
"""

from __future__ import annotations

import sys
import zlib
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS, centre, oil_to_friction  # noqa: E402
from qc import QCS, SHARED, parts_qc, sims_qc  # noqa: E402

ADEQUATE_RATE = 0.95
CONF_LEVEL = 0.90            # coverage of the split-conformal margin
NOMINAL_THICKNESS = 0.98     # mm; the measured sheet thickness has its median at 0.985-0.99 mm
NOMINAL_FRICTION = 0.10      # middle of the DDACS friction range
_POS = np.r_[np.arange(0.5, 10.01, 0.5), 12, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 300, 500]
D_GRID = np.r_[-_POS[::-1], 0.0, _POS]   # requirement distance from the true q95, in production floors
RESOLUTION_TARGET = 0.95     # resolution: smallest |d| beyond which this share of verdicts is correct
GBR = dict(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
M3_DRAWS = 500               # incoming conditions drawn for a new alternative
SEED = 7


def transform(qc: str, v):
    return np.abs(v) if QCS[qc][2] == "abs" else v


def matched_index(sims: pd.DataFrame, geo: str, bhf: int, thickness_mm: np.ndarray, oil: np.ndarray) -> np.ndarray:
    """Row of the matched simulation (rddac rule: nearest thickness + friction from the oil film)."""
    cand = sims[(sims["geometry"] == geo) & (sims["bhf_kN"] == bhf)]
    if cand.empty:
        return np.full(len(thickness_mm), -1)
    fc = np.array([oil_to_friction(o) if np.isfinite(o) else NOMINAL_FRICTION for o in oil])
    t = np.where(np.isfinite(thickness_mm), thickness_mm, NOMINAL_THICKNESS)
    err = np.abs(cand["sheet_metal_thickness"].to_numpy()[None, :] - t[:, None]) + \
        np.abs(cand["friction_coefficient"].to_numpy()[None, :] - fc[:, None])
    return cand.index.to_numpy()[np.argmin(err, axis=1)]


def match_sims(parts: pd.DataFrame, sims: pd.DataFrame) -> pd.DataFrame:
    out = []
    for (geo, bhf), g in parts.groupby(["geometry", "bhf_kN"]):
        idx = matched_index(sims, geo, int(bhf), g["sheet_um"].to_numpy() / 1000.0, g["oil_gm2"].to_numpy())
        m = pd.DataFrame({f"sim_{c}": np.where(idx >= 0, sims[c].reindex(idx).to_numpy(), np.nan) for c in SHARED},
                         index=g.index)
        out.append(pd.concat([g, m], axis=1))
    return pd.concat(out).sort_index()


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
                "n_parts": int(y.size), "real_centre": centre(y),
                "real_q95": float(np.quantile(y, ADEQUATE_RATE)), "real_sd": float(np.std(y)),
                "sim_nominal": float(transform(qc, nom[qc].to_numpy())[0]),
                "sim_env_lo": float(e.min()), "sim_env_hi": float(e.max()),
                "sim_matched_centre": centre(ms) if ms.size else np.nan,
            })
    t = pd.DataFrame(rows)
    t["gap_matched"] = t["real_centre"] - t["sim_matched_centre"]
    return t


def conformal_margin(res: np.ndarray, level: float) -> float:
    res = res[np.isfinite(res)]
    n = res.size
    if n == 0:
        return np.nan
    k = int(np.ceil((n + 1) * level))
    return float(np.max(res)) if k > n else float(np.sort(res)[k - 1])


# ── M3: simulation + gradient-boosting correction ─────────────────────────────
def design_matrix(df: pd.DataFrame, qc: str) -> np.ndarray:
    return np.column_stack([
        (df["geometry"] == "convex").astype(float), df["bhf_kN"].astype(float),
        (df["oil_type"] == "coarse").astype(float), (df["oil_type"] == "medium").astype(float),
        df[f"sim_{qc}"].astype(float), df["sheet_um"].astype(float), df["oil_gm2"].astype(float),
    ])


@lru_cache(maxsize=None)
def m3_fit(calib: frozenset, qc: str):
    """Model, residuals and training rows of M3 for one calibration set (cached; reused across targets)."""
    parts = _CTX["parts"]
    tr = parts[parts["alternative"].isin(calib)].dropna(subset=[qc, f"sim_{qc}", "sheet_um", "oil_gm2"])
    if len(tr) < 100:
        return None
    model = HistGradientBoostingRegressor(**GBR).fit(design_matrix(tr, qc), tr[qc].to_numpy())
    resid = tr[qc].to_numpy() - model.predict(design_matrix(tr, qc))
    return model, resid, tr[["oil_type", "sheet_um", "oil_gm2"]].reset_index(drop=True)


def m3_q95(calib: list[str], target: str, qc: str, rng: np.random.Generator) -> float:
    """Predicted q95 of a new alternative from a model trained on the calibration alternatives' parts."""
    fit = m3_fit(frozenset(calib), qc)
    if fit is None:
        return np.nan
    model, resid, tr = fit
    sims = _CTX["sims"]
    geo, bhf, lub = target.split("/")
    pool = tr[tr["oil_type"] == lub]
    pool = pool if len(pool) else tr
    draw = pool.iloc[rng.integers(0, len(pool), M3_DRAWS)][["sheet_um", "oil_gm2"]].reset_index(drop=True)
    new = draw.assign(geometry=geo, bhf_kN=int(float(bhf)), oil_type=lub)
    idx = matched_index(sims, geo, int(float(bhf)), new["sheet_um"].to_numpy() / 1000.0, new["oil_gm2"].to_numpy())
    if (idx < 0).any():
        return np.nan
    new[f"sim_{qc}"] = sims[qc].reindex(idx).to_numpy()
    yhat = model.predict(design_matrix(new, qc)) + rng.choice(resid, M3_DRAWS)
    return float(np.quantile(transform(qc, yhat), ADEQUATE_RATE))


def stable_seed(*keys: str) -> int:
    return SEED + zlib.crc32("|".join(keys).encode()) % 100_000


_CTX: dict = {}


@lru_cache(maxsize=None)
def m3_nested(calib: tuple[str, ...], qc: str) -> tuple[float, float]:
    """Offset and conformal margin of M3 from a leave-one-out over the calibration alternatives."""
    t = _CTX["t"]
    real = t[t["qc"] == qc].set_index("alternative")["real_q95"]
    res = []
    for b in calib:
        if b in real.index:
            rng = np.random.default_rng(stable_seed("nested", b, qc, *calib))
            res.append(real[b] - m3_q95([c for c in calib if c != b], b, qc, rng))
    res = np.array(res)
    off = float(np.nanmedian(res)) if res.size else np.nan
    return off, conformal_margin(np.abs(res - off), CONF_LEVEL)


def m3_calibrated(calib: list[str], target: str, qc: str) -> tuple[float, float, float]:
    """(predicted q95, offset, margin) of M3 for a new alternative."""
    rng = np.random.default_rng(stable_seed("target", target, qc, *sorted(calib)))
    q_target = m3_q95(calib, target, qc, rng)
    off, marg = m3_nested(tuple(sorted(calib)), qc)
    return q_target, off, marg


# ── decisions and scoring ─────────────────────────────────────────────────────
def verdicts(lo: float, hi: float, reqs: np.ndarray) -> np.ndarray:
    return np.where(hi <= reqs, "meets", np.where(lo > reqs, "fails", "uncertain"))


def decide(t: pd.DataFrame, calib: list[str], targets: list[str], qc: str, floors: dict, label: str,
           with_m3: bool) -> list[dict]:
    c = t[t["alternative"].isin(calib) & (t["qc"] == qc)]
    off1 = np.median(c["real_q95"] - c["sim_nominal"])
    r2 = c["real_q95"] - c["sim_env_hi"]
    off2 = np.median(r2)
    marg2 = conformal_margin(np.abs(r2 - off2).to_numpy(), CONF_LEVEL)
    out = []
    for target in targets:
        s = t[(t["alternative"] == target) & (t["qc"] == qc)]
        if s.empty:
            continue
        a = s.iloc[0]
        F = floors[(qc, a["geometry"])]
        reqs = a["real_q95"] + D_GRID * F
        rules = {
            "M0": np.where(a["sim_nominal"] <= reqs, "meets", "fails"),
            "M1": np.where(a["sim_nominal"] + off1 <= reqs, "meets", "fails"),
            "M2": verdicts(a["sim_env_hi"] + off2 - marg2, a["sim_env_hi"] + off2 + marg2, reqs),
        }
        if with_m3:
            q3, off3, marg3 = m3_calibrated(calib, target, qc)
            rules["M3"] = verdicts(q3 + off3 - marg3, q3 + off3 + marg3, reqs)
        for name, v in rules.items():
            for d, R, verdict in zip(D_GRID, reqs, v):
                out.append({"calibration": label, "alternative": target, "geometry": a["geometry"], "qc": qc,
                            "method": name, "d": float(d), "R": float(R), "verdict": verdict,
                            "adequate": bool(d >= 0)})
    return out


def beyond(rate: pd.Series) -> float:
    """Smallest |d| beyond which the share (indexed by |d|) stays at or above RESOLUTION_TARGET."""
    rate = rate.sort_index()
    bad = rate[rate < RESOLUTION_TARGET]
    if bad.empty:
        return float(rate.index.min())
    above = rate.index[rate.index > bad.index.max()]
    return float(above.min()) if len(above) else np.inf


def is_correct(d: pd.DataFrame) -> pd.Series:
    return ((d["verdict"] == "meets") & d["adequate"]) | ((d["verdict"] == "fails") & ~d["adequate"])


def resolution(d: pd.DataFrame) -> float:
    """Decisive distance: smallest |d| beyond which at least RESOLUTION_TARGET of the verdicts are correct."""
    return beyond(is_correct(d).groupby(d["d"].abs()).mean())


def safe_distance(d: pd.DataFrame) -> float:
    """Safe distance: smallest |d| beyond which at most 1 - RESOLUTION_TARGET of the verdicts are wrong."""
    return beyond((is_correct(d) | (d["verdict"] == "uncertain")).groupby(d["d"].abs()).mean())


def score(d: pd.DataFrame, by: list[str]) -> pd.DataFrame:
    d = d.assign(
        correct=((d["verdict"] == "meets") & d["adequate"]) | ((d["verdict"] == "fails") & ~d["adequate"]),
        false_accept=(d["verdict"] == "meets") & ~d["adequate"],
        false_reject=(d["verdict"] == "fails") & d["adequate"],
        abstain=d["verdict"] == "uncertain",
    )
    s = d.groupby(by)[["correct", "false_accept", "false_reject", "abstain"]].mean()
    decided = d[d["verdict"] != "uncertain"]
    s["error_when_decided"] = decided.groupby(by).apply(
        lambda g: ((g["verdict"] == "meets") != g["adequate"]).mean(), include_groups=False)
    return s


def main(with_m3: bool = True) -> None:
    parts = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    parts = match_sims(parts, sims)
    t = alternative_table(parts, sims)
    t.to_csv(RESULTS / "dec_alternatives.csv", index=False)
    _CTX.update(parts=parts, sims=sims, t=t)
    mg = []
    for qc, g in t.groupby("qc"):
        r2 = g["real_q95"] - g["sim_env_hi"]
        mg.append({"qc": qc, "offset_env": float(np.median(r2)),
                   "margin": conformal_margin(np.abs(r2 - np.median(r2)).to_numpy(), CONF_LEVEL),
                   "offset_nominal": float(np.median(g["real_q95"] - g["sim_nominal"])),
                   "n_alternatives": int(len(g))})
    pd.DataFrame(mg).to_csv(RESULTS / "dec_margins.csv", index=False)

    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    floors = {(qc, geo): float(fl.loc[qc, f"floor_{geo}"]) for qc in SHARED for geo in ("concave", "convex")}
    alts = sorted(t["alternative"].unique())
    records = []
    geo_of = {a: a.split("/")[0] for a in alts}
    for qc in SHARED:
        for a in alts:
            # within the design family: the other alternatives of the same geometry
            records += decide(t, [b for b in alts if b != a and geo_of[b] == geo_of[a]], [a], qc, floors,
                              "within", with_m3)
            # pooled: all other alternatives, both geometries
            records += decide(t, [b for b in alts if b != a], [a], qc, floors, "pooled", with_m3)
        for src, dst in (("concave", "convex"), ("convex", "concave")):
            calib = [b for b in alts if b.startswith(src)]
            targets = [b for b in alts if b.startswith(dst)]
            records += decide(t, calib, targets, qc, floors, f"{src}->{dst}", with_m3)
        print(f"{qc}: done", flush=True)
    d = pd.DataFrame(records)
    d.to_csv(RESULTS / "dec_verdicts.csv.gz", index=False)
    sc = score(d, ["calibration", "qc", "method"]).reset_index()
    sc.to_csv(RESULTS / "dec_scores.csv", index=False)
    d["scope"] = np.where(d["calibration"].str.contains("->"), "transfer", d["calibration"])
    overall = score(d, ["scope", "method"]).reset_index()
    res = []
    for (scope, method), g in d.groupby(["scope", "method"]):
        res.append({"scope": scope, "method": method, "qc": "all", "resolution_floors": resolution(g),
                    "safe_floors": safe_distance(g)})
        for qc, h in g.groupby("qc"):
            res.append({"scope": scope, "method": method, "qc": qc, "resolution_floors": resolution(h),
                        "safe_floors": safe_distance(h)})
    res = pd.DataFrame(res)
    res.to_csv(RESULTS / "dec_resolution.csv", index=False)
    curve = score(d, ["scope", "method", "d"]).reset_index()
    curve.to_csv(RESULTS / "dec_curve.csv", index=False)

    lines = ["# Design-stage decisions scored against production", "",
             f"Adequate: at least {ADEQUATE_RATE:.0%} of the parts conform. Conformal coverage {CONF_LEVEL:.0%}. "
             f"Nominal simulation: t = {NOMINAL_THICKNESS} mm, friction {NOMINAL_FRICTION}. "
             f"Requirements at d = {D_GRID.min():g} to {D_GRID.max():g} production floors from the true q95.", "",
             "## Offset between parts and matched simulations (median over alternatives)", "",
             t.pivot_table(index="qc", columns="geometry", values="gap_matched", aggfunc="median").round(3).to_markdown(),
             "", "## Decision rates over all characteristics", "", overall.round(3).to_markdown(index=False), "",
             "## Decisive distance (production floors): beyond it at least 95 % of verdicts are correct", "",
             res.pivot_table(index="qc", columns=["scope", "method"], values="resolution_floors").round(1).to_markdown(),
             "", "## Safe distance (production floors): beyond it at most 5 % of verdicts are wrong", "",
             res.pivot_table(index="qc", columns=["scope", "method"], values="safe_floors").round(1).to_markdown(),
             "",
             "## Decision rates per characteristic", "", sc.round(3).to_markdown(index=False)]
    (RESULTS / "summary_decisions.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main(with_m3="--no-m3" not in sys.argv)
