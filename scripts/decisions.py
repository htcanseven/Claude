"""Design-stage decisions from simulation, scored against production.

For each of the 18 alternatives and each quality characteristic (QC), the
production verdict at a requirement R is *adequate* when at least
ADEQUATE_RATE of its 500 parts conform (y <= R; |y| <= R for two-sided QCs),
i.e. when the 95th percentile q95 of the parts is within R.

At the design stage only simulations exist. The decision rules are scored
with alternatives held out, so that every alternative is judged as a new
design. The calibration scopes differ in how the new design relates to the
produced evidence:
  within          the other alternatives of the same geometry; the two
                  alternatives at the same blank-holder force (other
                  lubrication) are produced, so the new design is a new
                  variant of a produced process setting;
  setting         all three alternatives of one blank-holder force of a
                  geometry are held out together and the six others of the
                  geometry calibrate, so the new design is a new process
                  setting (300 kN: interpolation; 100 or 500 kN: extrapolation);
  pooled          as within, with the other geometry's alternatives added;
  pooled-setting  as setting, with the other geometry's alternatives added;
  transfer        only the alternatives of the other geometry (a new family).
The rules:

M0  nominal simulation: meets if the simulation at nominal sheet thickness and
    friction is within R, otherwise fails;
M1  bias-corrected simulation: as M0 after adding the median offset between
    the parts' q95 and the nominal simulation of the calibration alternatives;
M1s scaled simulation: q95 = a + b s0, a straight line fitted by least squares
    to the calibration alternatives' q95 against their nominal simulation s0,
    so that a simulated trend of the wrong size is rescaled (a linear
    multi-fidelity correction);
M2  envelope with a calibrated margin: the upper end of the simulation envelope
    over plausible incoming conditions (all DDACS sheet thicknesses and friction
    coefficients at the geometry and blank-holder force) plus the median offset,
    with a split-conformal margin from the calibration alternatives' offsets.
    Meets if the upper bound is within R, fails if the lower bound exceeds R,
    otherwise uncertain (send to trial);
M3  simulation corrected by machine learning: a gradient-boosting model learns,
    on the parts of the calibration alternatives, the discrepancy between the
    measured QC and the matched simulation from the design and process
    descriptors (geometry, blank-holder force, lubrication pattern) and the
    incoming conditions (sheet thickness, oil film). For the new alternative
    the incoming conditions are drawn from calibration parts with the same
    lubrication pattern (none of its own measurements are used); its
    simulation plus the predicted discrepancy and a resampled residual give
    the predicted parts. A leave-one-out over the calibration alternatives
    gives residuals and, from the same fits, predictions of the new
    alternative; the interval is the jackknife+ interval (Barber et al. 2021)
    of these, centred by the median residual. Verdicts as M2;
M4  machine learning without simulation: as M3 with the measured QC itself as
    the target, so the prediction rests on the produced alternatives alone.
    The difference between M3 and M4 is what the simulation adds;
M5  Gaussian-process correction of the envelope: the offset between the
    parts' q95 and the upper end of the simulation envelope is a Gaussian
    process over the alternative descriptors (geometry, blank-holder force,
    lubrication rank) fitted on the calibration alternatives; the verdict
    interval is its central CONF_LEVEL predictive interval. The noise variance
    is bounded below by the variation between the produced series of one
    geometry and force (noise_floor). Unlike M2 the offset may vary with the
    descriptors, and the margin comes from the model instead of a rank.
Practice baseline and ablations:
M0w worst case over the process window: the simulation envelope itself
    (lowest to highest simulated value over the DDACS sheet thicknesses and
    friction coefficients) without production evidence, as a robustness
    simulation is read in practice;
M1n, M2n, M5n  M1, M2 and M5 without the simulation: the median q95 of the
    calibration alternatives, the same with a conformal margin, and a Gaussian
    process of q95 itself over the descriptors. Against M1, M2 and M5 they
    isolate what the simulation contributes.

Requirements are placed at fixed distances d from each alternative's true q95,
measured in production floors F of the characteristic (alternatives.py):
R = q95 + d F, so the alternative is adequate exactly when d >= 0. Two
distances summarise a rule: the decisive distance (resolution) is the
smallest |d| beyond which at least RESOLUTION_TARGET of its verdicts are
correct (an abstention is not correct), the decision-level counterpart of a
limit of detection; the safe distance is the smallest |d| beyond which at
most 1 - RESOLUTION_TARGET of its verdicts are wrong (an abstention is not
wrong). For rules that always decide (M0, M1) the two coincide. The two
distances are operating characteristics of a rule: functions of the true
margin d, as the operating characteristic of an acceptance plan is a function
of the true quality. They are also given one-sided, for failing alternatives
(d < 0, where the error is a false accept) and adequate ones (d >= 0, false
reject). The observable counterpart, the share of decided verdicts that are
correct given the margin between the predicted interval and the requirement,
is given for requirements within 20 floors of the truth (dec_reliability.csv).

Uncertainty of the two distances: the design cases (held-out alternatives)
are resampled with replacement (N_BOOT_DEC resamples), and the distances
recomputed, which gives a percentile interval for each rule and scope. The
resamples are common to all rules of a scope, so that differences between
rules have paired intervals (dec_paired.csv).

Outputs: results/dec_alternatives.csv, dec_margins.csv, dec_intervals.csv,
dec_verdicts.csv.gz, dec_scores.csv, dec_resolution.csv, dec_curve.csv,
dec_paired.csv, dec_coverage.csv, dec_gp.csv, dec_reliability.csv, summary_decisions.md
"""

from __future__ import annotations

import os
import sys
import zlib
from functools import lru_cache
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, DotProduct, Matern, WhiteKernel

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS, centre, oil_to_friction  # noqa: E402
from qc import QCS, SHARED, parts_qc, sims_qc  # noqa: E402

ADEQUATE_RATE = 0.95
CONF_LEVEL = 0.90            # coverage of the split-conformal margin
NOMINAL_THICKNESS = 0.99     # mm; grid value nearest the measured median thickness (0.990 mm; series 0.986-0.993)
NOMINAL_FRICTION = 0.10      # middle of the DDACS friction range
_POS = np.r_[np.arange(0.5, 10.01, 0.5), 12, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 300, 500]
D_GRID = np.r_[-_POS[::-1], 0.0, _POS]   # requirement distance from the true q95, in production floors
RESOLUTION_TARGET = 0.95     # resolution: smallest |d| beyond which this share of verdicts is correct
GBR = dict(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
M3_DRAWS = 500               # incoming conditions drawn for a new alternative
SEED = 7
N_BOOT_DEC = 1000            # resamples of the design cases for the intervals of the two distances
N_JOBS = min(4, os.cpu_count() or 1)   # parallel characteristics for M3/M4 (results do not depend on it)
LUB_RANK = {"coarse": 0.0, "medium": 1.0, "fine": 2.0}   # order of the oil amount (series medians 1.15-1.48,
GP_RESTARTS = 3                                             # 0.92-1.23 and 0.85-1.13 g/m2)
N_REF = 1000                 # block-bootstrap replicates of each alternative's q95 (uncertainty of the reference)
REF_BLOCK = 50               # consecutive parts resampled together (the batch of alternatives.py)
CAL_QCS = ["drawin_mid", "drawin_corner"]   # Mc calibrates the friction coefficient on the draw-in
FINE = np.round(np.arange(0.0, 600.0 + 1e-9, 0.05), 2)   # floors; evaluation points of the distance curves
INTERVAL_RULES = ["M0w", "M2", "M3", "M4", "M5", "M2n", "M5n"]


def bhf_of(alt: str) -> int:
    return int(float(alt.split("/")[1]))


def scope_of(label: str) -> str:
    """Calibration scope of a calibration label ('within', 'setting:concave/300', 'concave->convex', ...)."""
    return "transfer" if "->" in label else label.split(":")[0]


def with_relation_scopes(df: pd.DataFrame) -> pd.DataFrame:
    """Append the new-setting scopes split by interpolation and extrapolation ('setting/interpolation', ...)."""
    sub = df[df["scope"].isin(["setting", "pooled-setting"])]
    return pd.concat([df, sub.assign(scope=sub["scope"] + "/" + sub["relation"])], ignore_index=True)


def relation(calib: list[str], target: str) -> str:
    """How a new design relates to the produced evidence: a produced sibling at its process setting,
    interpolation or extrapolation in blank-holder force within its family, or a new family."""
    geo = target.split("/")[0]
    same = [bhf_of(b) for b in calib if b.split("/")[0] == geo]
    if not same:
        return "new family"
    if bhf_of(target) in same:
        return "sibling"
    return "interpolation" if min(same) < bhf_of(target) < max(same) else "extrapolation"


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


def q95_replicates(y: np.ndarray, rng: np.random.Generator, n: int = N_REF) -> np.ndarray:
    """Block-bootstrap replicates of the q95 of a series in time order (blocks of REF_BLOCK parts)."""
    blocks = [y[i:i + REF_BLOCK] for i in range(0, len(y), REF_BLOCK)]
    idx = rng.integers(0, len(blocks), (n, len(blocks)))
    return np.array([np.quantile(np.concatenate([blocks[j] for j in row]), ADEQUATE_RATE) for row in idx])


def alternative_table(parts: pd.DataFrame, sims: pd.DataFrame) -> tuple[pd.DataFrame, np.ndarray]:
    """One row per alternative and QC: production truth (q95 with its block-bootstrap standard error and
    replicates), simulation summaries, and signed centres for the credibility of the simulation."""
    rows, reps = [], []
    for alt, g in parts.groupby("alternative"):
        geo, bhf = g["geometry"].iloc[0], int(g["bhf_kN"].iloc[0])
        env = sims[(sims["geometry"] == geo) & (sims["bhf_kN"] == bhf)]
        if env.empty:
            continue
        nom = env.iloc[[int(np.argmin(np.abs(env["sheet_metal_thickness"] - NOMINAL_THICKNESS)
                                      + np.abs(env["friction_coefficient"] - NOMINAL_FRICTION)))]]
        for qc in SHARED:
            raw = g[qc].dropna().to_numpy()
            y = transform(qc, raw)
            e = transform(qc, env[qc].dropna().to_numpy())
            ms_raw = g[f"sim_{qc}"].dropna().to_numpy()
            if y.size < 20 or e.size == 0:
                continue
            r = q95_replicates(y, np.random.default_rng(stable_seed("reference", alt, qc)))
            reps.append(r)
            rows.append({
                "alternative": alt, "geometry": geo, "bhf_kN": bhf, "oil_type": g["oil_type"].iloc[0], "qc": qc,
                "n_parts": int(y.size), "real_centre": centre(y),
                "real_q95": float(np.quantile(y, ADEQUATE_RATE)), "real_q95_se": float(np.std(r, ddof=1)),
                "real_sd": float(np.std(y)),
                "sim_nominal": float(transform(qc, nom[qc].to_numpy())[0]),
                "sim_env_lo": float(e.min()), "sim_env_hi": float(e.max()),
                "sim_matched_centre": centre(transform(qc, ms_raw)) if ms_raw.size else np.nan,
                "real_centre_signed": centre(raw), "sim_nominal_signed": float(nom[qc].to_numpy()[0]),
                "sim_matched_centre_signed": centre(ms_raw) if ms_raw.size else np.nan,
            })
    t = pd.DataFrame(rows)
    t["gap_matched"] = t["real_centre"] - t["sim_matched_centre"]
    t["gap_matched_signed"] = t["real_centre_signed"] - t["sim_matched_centre_signed"]
    return t, np.array(reps)


def conformal_margin(res: np.ndarray, level: float) -> float:
    res = res[np.isfinite(res)]
    n = res.size
    if n == 0:
        return np.nan
    k = int(np.ceil((n + 1) * level))
    return float(np.max(res)) if k > n else float(np.sort(res)[k - 1])


# ── M3: simulation + gradient-boosting correction ─────────────────────────────
def design_matrix(df: pd.DataFrame) -> np.ndarray:
    """Design and process descriptors and incoming conditions of parts."""
    return np.column_stack([
        (df["geometry"] == "convex").astype(float), df["bhf_kN"].astype(float),
        (df["oil_type"] == "coarse").astype(float), (df["oil_type"] == "medium").astype(float),
        df["sheet_um"].astype(float), df["oil_gm2"].astype(float),
    ])


@lru_cache(maxsize=None)
def m3_fit(calib: frozenset, qc: str, use_sim: bool = True):
    """Model, residuals and training rows of M3 (target: QC - simulation) or M4 (target: QC), cached."""
    parts = _CTX["parts"]
    need = [qc, "sheet_um", "oil_gm2"] + ([f"sim_{qc}"] if use_sim else [])
    tr = parts[parts["alternative"].isin(calib)].dropna(subset=need)
    if len(tr) < 100:
        return None
    y = tr[qc].to_numpy() - (tr[f"sim_{qc}"].to_numpy() if use_sim else 0.0)
    X = design_matrix(tr)
    model = HistGradientBoostingRegressor(**GBR).fit(X, y)
    return model, y - model.predict(X), tr[["oil_type", "sheet_um", "oil_gm2"]].reset_index(drop=True)


def m3_q95(calib: list[str], target: str, qc: str, rng: np.random.Generator, use_sim: bool = True) -> float:
    """Predicted q95 of a new alternative from a model trained on the calibration alternatives' parts."""
    fit = m3_fit(frozenset(calib), qc, use_sim)
    if fit is None:
        return np.nan
    model, resid, tr = fit
    geo, bhf, lub = target.split("/")
    pool = tr[tr["oil_type"] == lub]
    pool = pool if len(pool) else tr
    draw = pool.iloc[rng.integers(0, len(pool), M3_DRAWS)][["sheet_um", "oil_gm2"]].reset_index(drop=True)
    new = draw.assign(geometry=geo, bhf_kN=int(float(bhf)), oil_type=lub)
    base = 0.0
    if use_sim:
        sims = _CTX["sims"]
        idx = matched_index(sims, geo, int(float(bhf)), new["sheet_um"].to_numpy() / 1000.0,
                            new["oil_gm2"].to_numpy())
        if (idx < 0).any():
            return np.nan
        base = sims[qc].reindex(idx).to_numpy()
    yhat = base + model.predict(design_matrix(new)) + rng.choice(resid, M3_DRAWS)
    return float(np.quantile(transform(qc, yhat), ADEQUATE_RATE))


def stable_seed(*keys: str) -> int:
    return SEED + zlib.crc32("|".join(keys).encode()) % 100_000


_CTX: dict = {}


@lru_cache(maxsize=None)
def m3_nested(calib: tuple[str, ...], qc: str, use_sim: bool = True) -> tuple[float, float, tuple]:
    """Offset, plain jackknife margin and signed residuals (in the order of calib) of M3 (M4) from a
    leave-one-out over the calibration alternatives."""
    t = _CTX["t"]
    real = t[t["qc"] == qc].set_index("alternative")["real_q95"]
    tag = "nested" if use_sim else "nested-nosim"
    res = []
    for b in calib:
        if b in real.index:
            rng = np.random.default_rng(stable_seed(tag, b, qc, *calib))
            res.append(real[b] - m3_q95([c for c in calib if c != b], b, qc, rng, use_sim))
        else:
            res.append(np.nan)
    res = np.array(res, dtype=float)
    off = float(np.nanmedian(res)) if np.isfinite(res).any() else np.nan
    return off, conformal_margin(np.abs(res - off), CONF_LEVEL), tuple(res)


def jackknife_plus(preds: np.ndarray, res: np.ndarray, off: float, level: float = CONF_LEVEL) -> tuple[float, float]:
    """Jackknife+ interval (Barber et al. 2021): the leave-one-out models' predictions of the target, shifted by
    the median leave-one-out residual, minus and plus the centred absolute residuals; the bounds are the
    floor(alpha (n+1))-th and ceil((1-alpha)(n+1))-th smallest values, the extreme ones when n is too small."""
    ok = np.isfinite(preds) & np.isfinite(res)
    p, r = preds[ok], np.abs(res[ok] - off)
    n = p.size
    if n == 0:
        return np.nan, np.nan
    k_hi = min(int(np.ceil((n + 1) * level)), n)
    k_lo = max(int(np.floor((n + 1) * (1 - level))), 1)
    return float(np.sort(p + off - r)[k_lo - 1]), float(np.sort(p + off + r)[k_hi - 1])


def m3_calibrated(calib: list[str], target: str, qc: str, use_sim: bool = True) -> tuple[float, float]:
    """Jackknife+ interval of M3 (M4 without simulation) for a new alternative. The leave-one-out fits that
    give the residuals also predict the target, so the interval needs no further fits."""
    key = tuple(sorted(calib))
    off, _, res = m3_nested(key, qc, use_sim)
    tag = "jkplus" if use_sim else "jkplus-nosim"
    preds = np.array([m3_q95([c for c in key if c != b], target, qc,
                             np.random.default_rng(stable_seed(tag, target, b, qc, *key)), use_sim) for b in key])
    return jackknife_plus(preds, np.array(res), off)


# ── M5: Gaussian-process discrepancy on the alternatives ─────────────────────
def descriptors(alts) -> np.ndarray:
    """Geometry indicator, blank-holder force in 100 kN and lubrication rank (or, in the robustness variant
    'onehot', two lubrication indicators)."""
    rows = []
    for a in alts:
        geo, bhf, lub = a.split("/")
        lubv = [float(lub == "coarse"), float(lub == "medium")] if _CTX.get("gp_variant") == "onehot" \
            else [LUB_RANK[lub]]
        rows.append([1.0 if geo == "convex" else 0.0, float(bhf) / 100.0] + lubv)
    return np.array(rows)


LS_BOUNDS = (1e-1, 1e2)


def noise_floor(calib, y: np.ndarray, se: np.ndarray, between: bool = True) -> float:
    """Lower bound of the GP noise variance: the larger of the mean sampling variance of the calibration
    alternatives' q95 (block bootstrap within a series) and, with between, the pooled variance between the
    series of one geometry and force (the quasi-replicate lubrication series), which bounds the variation
    between runs from above. A new series of a produced setting is then not predicted more precisely than
    the produced series of that setting reproduce each other."""
    sampling = float(np.mean(se ** 2))
    if not between:
        return sampling
    cells = pd.Series(y, index=[(a.split("/")[0], bhf_of(a)) for a in calib])
    g = cells.groupby(level=0)
    ss = float(sum(((v - v.mean()) ** 2).sum() for _, v in g if len(v) >= 2))
    dof = int(sum(len(v) - 1 for _, v in g if len(v) >= 2))
    return max(sampling, ss / dof) if dof > 0 else sampling


@lru_cache(maxsize=None)
def m5_fit(calib: tuple[str, ...], qc: str, use_sim: bool = True):
    """GP of the offset real_q95 - sim_env_hi (M5) or of real_q95 itself (M5n) over the calibration
    alternatives (cached per calibration set). The noise variance is bounded below by the sampling variance
    of the calibration alternatives' q95 (block bootstrap), so the GP cannot claim to know a produced
    alternative's q95 better than its own series does."""
    c = _CTX["t"][_CTX["t"]["qc"] == qc].set_index("alternative").loc[list(calib)]
    X = descriptors(calib)
    keep = X.std(axis=0) > 0                     # a descriptor constant over the calibration set carries nothing
    y = (c["real_q95"] - c["sim_env_hi"] if use_sim else c["real_q95"]).to_numpy()
    var = float(np.var(y))
    variant = _CTX.get("gp_variant", "reference")         # robustness.py varies the specification
    floor_var = noise_floor(calib, y, c["real_q95_se"].to_numpy(), between=variant != "se_floor")
    lb = float(np.clip(floor_var / var, 1e-6, 1e2)) if var > 0 else 1e-6
    nk = int(keep.sum())
    if variant == "matern":
        corr = Matern(np.ones(nk), LS_BOUNDS, nu=2.5)
    elif variant == "ls_floor":                           # length scales of at least 100 kN / one pattern step
        corr = RBF(np.full(nk, 2.0), (1.0, 1e2))
    else:
        corr = RBF(np.ones(nk), LS_BOUNDS)
    kern = ConstantKernel(1.0, (1e-3, 1e3)) * corr
    if variant == "linear":                               # universal kriging: a linear trend in the descriptors
        kern = kern + ConstantKernel(0.1, (1e-4, 1e2)) * DotProduct(1.0, (1e-2, 1e2))
    noise = WhiteKernel(1e-2, (1e-6, 1e1)) if variant == "no_noise_floor" else \
        WhiteKernel(max(1e-2, lb), (lb, max(1e1, 10 * lb)))
    gp = GaussianProcessRegressor(kern + noise, normalize_y=True, n_restarts_optimizer=GP_RESTARTS, random_state=0)
    return gp.fit(X[:, keep], y), keep


def gp_info(calib: list[str], qc: str, use_sim: bool) -> dict:
    """Fitted hyperparameters of an M5 / M5n fit and the number of them at a bound."""
    gp, keep = m5_fit(tuple(sorted(calib)), qc, use_sim)
    k = gp.kernel_
    ls = np.atleast_1d(k.k1.k2.length_scale)
    names = np.array(["geometry", "bhf", "lubrication"])[keep]
    out = {f"gp_ls_{n}": float(v) for n, v in zip(names, ls)}
    nb = k.k2.hyperparameter_noise_level.bounds[0]
    out.update({"gp_noise": float(k.k2.noise_level), "gp_noise_lb": float(nb[0]),
                "gp_noise_at_bound": bool(np.isclose(k.k2.noise_level, nb[0])),
                "gp_ls_at_bound": int(np.sum(np.isclose(ls, LS_BOUNDS[0]) | np.isclose(ls, LS_BOUNDS[1])))})
    return out


def nn_point(calib: list[str], target: str, qc: str) -> float:
    """Nearest produced setting (no simulation, no learning): mean q95 of the calibration alternatives of
    the target's geometry at the nearest blank-holder force, both neighbours when two are equally near;
    without alternatives of the geometry, those of the other geometry."""
    tq = _CTX["t"][_CTX["t"]["qc"] == qc].set_index("alternative")["real_q95"]
    geo, bhf = target.split("/")[0], bhf_of(target)
    same = [b for b in calib if b.split("/")[0] == geo] or list(calib)
    dist = np.array([abs(bhf_of(b) - bhf) for b in same])
    return float(tq.loc[[b for b, x in zip(same, dist) if x == dist.min()]].mean())


def sim_at(geo: str, bhf: int, mu: float, qc: str) -> float:
    """Simulated QC at the nominal sheet thickness and friction coefficient mu (DDACS grid)."""
    return _CTX["simgrid"][(geo, bhf, round(float(mu), 3))][qc]


@lru_cache(maxsize=None)
def friction_fit(calib: tuple[str, ...], lub: str) -> float:
    """Friction coefficient of a lubrication pattern calibrated on the produced alternatives: the DDACS
    grid value whose simulated draw-in (CAL_QCS, in floors) is closest in least squares to the parts'
    centres of the calibration alternatives with that pattern (all of them if none has it)."""
    t, floors = _CTX["tq"], _CTX["floors"]
    use = [b for b in calib if b.split("/")[2] == lub] or list(calib)
    best, mu_best = np.inf, np.nan
    for mu in _CTX["mu_grid"]:
        err = sum(((t[(b, c)]["real_centre"] - sim_at(b.split("/")[0], bhf_of(b), mu, c)) /
                   floors[(c, b.split("/")[0])]) ** 2 for b in use for c in CAL_QCS)
        if err < best:
            best, mu_best = err, mu
    return float(mu_best)


def mc_point(calib: list[str], target: str, qc: str) -> float:
    """Friction-calibrated simulation (a calibration parameter in the sense of Kennedy and O'Hagan, without
    a discrepancy model): the simulation at the target's setting with its pattern's calibrated friction, plus
    the median offset of the calibration alternatives' q95 from their own calibrated simulations."""
    key = tuple(sorted(calib))
    t = _CTX["tq"]
    geo, lub = target.split("/")[0], target.split("/")[2]
    offs = [t[(b, qc)]["real_q95"] - sim_at(b.split("/")[0], bhf_of(b), friction_fit(key, b.split("/")[2]), qc)
            for b in calib]
    return sim_at(geo, bhf_of(target), friction_fit(key, lub), qc) + float(np.median(offs))


def m5_interval(calib: list[str], target: str, qc: str, env_hi: float, use_sim: bool = True) -> tuple[float, float]:
    gp, keep = m5_fit(tuple(sorted(calib)), qc, use_sim)
    mu, sd = gp.predict(descriptors([target])[:, keep], return_std=True)
    z = norm.ppf(0.5 + CONF_LEVEL / 2)
    base = env_hi if use_sim else 0.0
    return base + mu[0] - z * sd[0], base + mu[0] + z * sd[0]


# ── decisions and scoring ─────────────────────────────────────────────────────
def verdicts(lo: float, hi: float, reqs: np.ndarray) -> np.ndarray:
    return np.where(hi <= reqs, "meets", np.where(lo > reqs, "fails", "uncertain"))


def calibration_stats(c: pd.DataFrame) -> dict[str, float]:
    """Offsets and conformal margins of M1, M2, M1n and M2n from the calibration alternatives' rows."""
    r2 = (c["real_q95"] - c["sim_env_hi"]).to_numpy()
    q = c["real_q95"].to_numpy()
    s0 = c["sim_nominal"].to_numpy()
    off1 = float(np.median(q - s0))
    off2, med_q = float(np.median(r2)), float(np.median(q))
    # M1s: q95 = a + b s0 by least squares (the bias correction with the simulated trend rescaled)
    b1, a1 = np.polyfit(s0, q, 1) if np.ptp(s0) > 0 and len(q) >= 2 else (1.0, off1)
    return {"off1": off1, "off2": off2, "a1s": float(a1), "b1s": float(b1),
            "marg2": conformal_margin(np.abs(r2 - off2), CONF_LEVEL),
            "med_q": med_q, "marg_q": conformal_margin(np.abs(q - med_q), CONF_LEVEL)}


def rule_intervals(a: pd.Series, calib: list[str], qc: str, stats: dict[str, float],
                   with_m3: bool) -> dict[str, tuple[float, float]]:
    """Predicted interval of the target's q95 under every rule; M0, M1 and M1n are points (lo = hi)."""
    s = stats
    target = a["alternative"]
    iv = {"M0": (a["sim_nominal"], a["sim_nominal"]),
          "M0w": (a["sim_env_lo"], a["sim_env_hi"]),
          "M1": (a["sim_nominal"] + s["off1"], a["sim_nominal"] + s["off1"]),
          "M1s": (s["a1s"] + s["b1s"] * a["sim_nominal"],) * 2,
          "M2": (a["sim_env_hi"] + s["off2"] - s["marg2"], a["sim_env_hi"] + s["off2"] + s["marg2"]),
          "M5": m5_interval(calib, target, qc, a["sim_env_hi"]),
          "Mc": (mc_point(calib, target, qc),) * 2,
          "M1n": (s["med_q"], s["med_q"]),
          "NN": (nn_point(calib, target, qc),) * 2,
          "M2n": (s["med_q"] - s["marg_q"], s["med_q"] + s["marg_q"]),
          "M5n": m5_interval(calib, target, qc, 0.0, use_sim=False)}
    if with_m3:
        iv["M3"] = m3_calibrated(calib, target, qc)
        iv["M4"] = m3_calibrated(calib, target, qc, use_sim=False)
    return {k: (float(lo), float(hi)) for k, (lo, hi) in iv.items()}


def decide(t: pd.DataFrame, calib: list[str], targets: list[str], qc: str, floors: dict, label: str,
           with_m3: bool) -> tuple[list[dict], list[dict]]:
    """Verdicts at every requirement distance, and the intervals behind them, for the targets of one calibration."""
    c = t[t["alternative"].isin(calib) & (t["qc"] == qc)]
    stats = calibration_stats(c)
    out, ivs = [], []
    for target in targets:
        s = t[(t["alternative"] == target) & (t["qc"] == qc)]
        if s.empty:
            continue
        a = s.iloc[0]
        F = floors[(qc, a["geometry"])]
        feasible = a["real_q95"] + D_GRID * F >= 0      # a negative limit on a non-negative QC is not a requirement
        grid = D_GRID[feasible]
        reqs = a["real_q95"] + grid * F
        rel = relation(calib, target)
        same = c[c["geometry"] == a["geometry"]]["bhf_kN"]
        for name, (lo, hi) in rule_intervals(a, calib, qc, stats, with_m3).items():
            row = {"calibration": label, "relation": rel, "alternative": target, "geometry": a["geometry"],
                   "bhf_kN": int(a["bhf_kN"]), "qc": qc, "method": name, "lo": lo, "hi": hi,
                   "real_q95": float(a["real_q95"]), "floor": F,
                   "sim_env_hi": float(a["sim_env_hi"]), "calib_env_min": float(c["sim_env_hi"].min()),
                   "calib_env_max": float(c["sim_env_hi"].max()),
                   "calib_bhf_min": float(same.min()) if len(same) else np.nan,
                   "calib_bhf_max": float(same.max()) if len(same) else np.nan,
                   "calib_geometries": "|".join(sorted(c["geometry"].unique()))}
            if name in ("M5", "M5n"):
                row.update(gp_info(calib, qc, name == "M5"))
            ivs.append(row)
            for d, R, verdict in zip(grid, reqs, verdicts(lo, hi, reqs)):
                out.append({"calibration": label, "relation": rel, "alternative": target, "geometry": a["geometry"],
                            "qc": qc, "method": name, "d": float(d), "R": float(R), "verdict": verdict,
                            "adequate": bool(d >= 0)})
    return out, ivs


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


def beyond_rows(rates: np.ndarray, ad: np.ndarray, target: float = RESOLUTION_TARGET) -> np.ndarray:
    """beyond() for every row of a matrix of shares whose columns are the ascending |d| values ad."""
    bad = rates < target
    last = ad.size - 1 - np.argmax(bad[:, ::-1], axis=1)          # last |d| with a share below the target
    nxt = np.where(last + 1 < ad.size, ad[np.minimum(last + 1, ad.size - 1)], np.inf)
    return np.where(bad.any(axis=1), nxt, ad[0])


#: rule pairs whose differences in the two distances get paired bootstrap intervals
PAIRS = [("M5", "M2"), ("M5", "M1"), ("M5", "M4"), ("M5", "M3"), ("M3", "M4"), ("M1", "M1n"), ("M2", "M2n"),
         ("M5", "M5n"), ("M5", "NN"), ("M5n", "NN"), ("Mc", "M1"), ("M2", "M0w"), ("M1s", "M1"), ("M1s", "M1n"),
         ("M1s", "NN"), ("M2", "NN"), ("M2n", "NN")]


def exclusion(iv: pd.DataFrame, q: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Exclusion distances of every case in floors, u = (hi - q95)/F and v = (q95 - lo)/F, and the largest
    feasible distance on the failing side, cap = q95/F (a limit below zero is no requirement for these
    non-negative characteristics). A rule without an interval never decides (u = v = inf)."""
    F = iv["floor"].to_numpy(float)
    q = iv["real_q95"].to_numpy(float) if q is None else q
    u = (iv["hi"].to_numpy(float) - q) / F
    v = (q - iv["lo"].to_numpy(float)) / F
    return np.where(np.isnan(u), np.inf, u), np.where(np.isnan(v), np.inf, v), np.where(q > 0, q / F, np.inf)


def share_curves(u: np.ndarray, v: np.ndarray, cap: np.ndarray, grid: np.ndarray = FINE) -> dict[str, np.ndarray]:
    """Shares of correct and of wrong verdicts at every distance delta of the grid. The requirement lies at
    q95 + delta F (an adequate alternative) and, for delta > 0 and where feasible, at q95 - delta F (a
    failing one); every case and side has equal weight. The verdict of a case changes only where delta
    crosses u, v, -u or -v, so the curves are exact between grid points."""
    n = len(u)

    def le(a):                                                  # count of a <= delta
        return np.searchsorted(np.sort(a), grid, side="right")

    def lt(a):                                                  # count of a < delta
        return np.searchsorted(np.sort(a), grid, side="left")

    pos = grid > 0
    n_cap = le(cap)
    feas = np.where(pos, n - n_cap, 0)
    a_correct, a_wrong = le(u), n - le(-v)                      # hi <= R ; lo > R
    f_correct = np.where(pos, np.maximum(lt(v) - le(np.maximum(v, cap)), 0), 0)                   # lo > R
    f_wrong = np.where(pos, np.maximum((n - lt(-u)) - (n_cap - le(np.maximum(cap, -u))), 0), 0)   # hi <= R
    den = n + feas
    with np.errstate(invalid="ignore", divide="ignore"):
        return {"correct": (a_correct + f_correct) / den, "wrong": (a_wrong + f_wrong) / den,
                "correct_adequate": a_correct / n, "wrong_adequate": a_wrong / n,
                "correct_failing": np.where(feas > 0, f_correct / feas, np.nan),
                "wrong_failing": np.where(feas > 0, f_wrong / feas, np.nan)}


def first_beyond(share: np.ndarray, grid: np.ndarray = FINE, target: float = RESOLUTION_TARGET) -> float:
    """Smallest delta of the grid beyond which the share stays at or above the target (NaN: no case)."""
    bad = np.flatnonzero(share < target)
    if bad.size == 0:
        return float(grid[0])
    return float(grid[bad[-1] + 1]) if bad[-1] + 1 < grid.size else np.inf


def distance_pair(u: np.ndarray, v: np.ndarray, cap: np.ndarray, sides: bool = False,
                  target: float = RESOLUTION_TARGET) -> dict[str, float]:
    """Decisive and safe distance of a set of cases; with sides, also for adequate alternatives only (where
    the error is a false reject) and failing alternatives only (a false accept)."""
    s = share_curves(u, v, cap)
    fb = lambda x: first_beyond(x, target=target)  # noqa: E731
    out = {"resolution_floors": fb(s["correct"]), "safe_floors": fb(1 - s["wrong"])}
    if sides:
        out.update({"resolution_adequate": fb(s["correct_adequate"]), "safe_adequate": fb(1 - s["wrong_adequate"]),
                    "resolution_failing": fb(s["correct_failing"]), "safe_failing": fb(1 - s["wrong_failing"])})
    return out


def distances(iv: pd.DataFrame, reps: np.ndarray | None = None, n_boot: int = N_BOOT_DEC,
              paired: list | None = None, per_qc: bool = True) -> pd.DataFrame:
    """Decisive and safe distances per scope and rule over all characteristics ('all') and, as point
    estimates, per characteristic. Intervals: the design cases (held-out alternatives, with all their
    characteristics) are resampled with replacement within each geometry, and every resample takes one
    block-bootstrap replicate of the true q95 (reps, rows indexed by iv['ref_row']), so that the uncertainty
    of the reference enters. The resamples are common to all rules of a scope; the paired differences of
    the rule pairs in PAIRS are appended to `paired` when a list is given. The fits are not repeated."""
    rows = []
    for scope, gs in iv.groupby("scope"):
        alts = np.sort(gs["alternative"].unique())
        fam = np.array([a.split("/")[0] for a in alts])
        rng = np.random.default_rng(stable_seed("boot", scope))
        idx = np.concatenate([rng.choice(np.flatnonzero(fam == f), (n_boot, int((fam == f).sum())))
                              for f in np.unique(fam)], axis=1)
        ref = rng.integers(0, N_REF, n_boot)
        boot = {}
        for method, gm in gs.groupby("method", sort=False):
            gm = gm.sort_values(["alternative", "qc"])
            u, v, cap = exclusion(gm)
            row = {"scope": scope, "method": method, "qc": "all", "n_cases": len(gm),
                   **distance_pair(u, v, cap, sides=True)}
            if n_boot and reps is not None:
                galt = gm["alternative"].to_numpy()
                pos = [np.flatnonzero(galt == a) for a in alts]
                rr = gm["ref_row"].to_numpy()
                F, lo, hi = (gm[c].to_numpy(float) for c in ("floor", "lo", "hi"))
                bc, bs = np.empty(n_boot), np.empty(n_boot)
                for b in range(n_boot):
                    sel = np.concatenate([pos[i] for i in idx[b]])
                    q, f = reps[rr[sel], ref[b]], F[sel]
                    ub, vb = (hi[sel] - q) / f, (q - lo[sel]) / f
                    r = distance_pair(np.where(np.isnan(ub), np.inf, ub), np.where(np.isnan(vb), np.inf, vb),
                                      np.where(q > 0, q / f, np.inf))
                    bc[b], bs[b] = r["resolution_floors"], r["safe_floors"]
                boot[method] = (bc, bs)
                row.update({"resolution_lo": float(np.percentile(bc, 2.5)), "resolution_hi": float(np.percentile(bc, 97.5)),
                            "safe_lo": float(np.percentile(bs, 2.5)), "safe_hi": float(np.percentile(bs, 97.5))})
            rows.append(row)
            if per_qc:
                for qc, h in gm.groupby("qc"):
                    rows.append({"scope": scope, "method": method, "qc": qc, "n_cases": len(h),
                                 **distance_pair(*exclusion(h), sides=True)})
        if paired is not None:
            point = {r["method"]: r for r in rows if r["scope"] == scope and r["qc"] == "all"}
            for a, b in PAIRS:
                if a in boot and b in boot:
                    p = {"scope": scope, "rule_a": a, "rule_b": b}
                    for j, kind in enumerate(("resolution", "safe")):
                        x, y = boot[a][j], boot[b][j]
                        diff = np.where(np.isinf(x) & np.isinf(y), 0.0, x - y)
                        p.update({f"{kind}_diff": point[a][f"{kind}_floors"] - point[b][f"{kind}_floors"],
                                  f"{kind}_diff_lo": float(np.percentile(diff, 2.5)),
                                  f"{kind}_diff_hi": float(np.percentile(diff, 97.5)),
                                  f"{kind}_share_a_smaller": float(np.mean(x < y))})
                    paired.append(p)
    return pd.DataFrame(rows)


def coverage(iv: pd.DataFrame) -> pd.DataFrame:
    """Empirical coverage of the interval rules (share of cases whose true q95 lies in the interval), the
    median half-width in floors, and the decisive distance of the interval centre used as a point rule."""
    rows = []
    for (scope, method), g in iv[iv["method"].isin(INTERVAL_RULES)].groupby(["scope", "method"]):
        q, lo, hi, F = (g[c].to_numpy(float) for c in ("real_q95", "lo", "hi", "floor"))
        mid = (lo + hi) / 2
        centre_d = distance_pair(*exclusion(g.assign(lo=mid, hi=mid)))["resolution_floors"]
        rows.append({"scope": scope, "method": method, "n_cases": len(g),
                     "coverage": float(np.mean((lo <= q) & (q <= hi))),
                     "half_width_floors": float(np.nanmedian((hi - lo) / 2 / F)), "centre_decisive": centre_d})
    return pd.DataFrame(rows)


MARGIN_STEPS = [0.0, 1.0, 2.0, 5.0, 10.0, 20.0]


def reliability(iv: pd.DataFrame, max_d: float = 20.0) -> pd.DataFrame:
    """Observable view of the verdicts: the share of decided verdicts that are correct given the margin
    (floors) between the predicted interval and the requirement, for requirements on the grid within
    max_d floors of the truth (every grid point weighted equally)."""
    grid = D_GRID[np.abs(D_GRID) <= max_d]
    lo, hi = iv["lo"].to_numpy()[:, None], iv["hi"].to_numpy()[:, None]
    F = iv["floor"].to_numpy()[:, None]
    reqs = iv["real_q95"].to_numpy()[:, None] + grid[None, :] * F
    meets, fails = hi <= reqs, lo > reqs
    margin = np.where(meets, (reqs - hi) / F, np.where(fails, (lo - reqs) / F, np.nan))
    correct = (meets & (grid >= 0)[None, :]) | (fails & (grid < 0)[None, :])
    rows = []
    for (scope, method), ix in iv.groupby(["scope", "method"]).indices.items():
        m, c = margin[ix].ravel(), correct[ix].ravel()
        for step in MARGIN_STEPS:
            sel = np.isfinite(m) & (m >= step)
            rows.append({"scope": scope, "method": method, "margin_floors": step, "n_decided": int(sel.sum()),
                         "share_of_verdicts": float(sel.mean()),
                         "correct_when_decided": float(c[sel].mean()) if sel.any() else np.nan})
    return pd.DataFrame(rows)


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


def qc_records(qc: str) -> list[dict]:
    """All verdicts of one characteristic: within the family, pooled and across geometries."""
    from threadpoolctl import threadpool_limits

    t, floors, with_m3 = _CTX["t"], _CTX["floors"], _CTX["with_m3"]
    alts = sorted(t["alternative"].unique())
    geo_of = {a: a.split("/")[0] for a in alts}
    records, intervals = [], []
    with threadpool_limits(1 if N_JOBS > 1 else None):
        jobs = []
        for a in alts:
            # within the design family: the other alternatives of the same geometry
            jobs.append(([b for b in alts if b != a and geo_of[b] == geo_of[a]], [a], "within"))
            # pooled: all other alternatives, both geometries
            jobs.append(([b for b in alts if b != a], [a], "pooled"))
        for geo, bhf in sorted({(geo_of[a], bhf_of(a)) for a in alts}):
            # new process setting: the three lubrication variants of one force are held out together
            held = [b for b in alts if geo_of[b] == geo and bhf_of(b) == bhf]
            jobs.append(([b for b in alts if geo_of[b] == geo and b not in held], held, f"setting:{geo}/{bhf}"))
            jobs.append(([b for b in alts if b not in held], held, f"pooled-setting:{geo}/{bhf}"))
        for src, dst in (("concave", "convex"), ("convex", "concave")):
            jobs.append(([b for b in alts if b.startswith(src)], [b for b in alts if b.startswith(dst)],
                         f"{src}->{dst}"))
        for calib, targets, label in jobs:
            v, iv = decide(t, calib, targets, qc, floors, label, with_m3)
            records += v
            intervals += iv
    print(f"{qc}: done", flush=True)
    return records, intervals


def setup(t: pd.DataFrame, sims: pd.DataFrame, floors: dict, parts: pd.DataFrame | None = None) -> None:
    """Context of the decision rules: alternative table, floors, the simulation grid at the nominal sheet
    thickness (for Mc) and, for M3/M4, the parts with their matched simulations. Empties every cache."""
    nomt = sims[np.isclose(sims["sheet_metal_thickness"], NOMINAL_THICKNESS)]
    simgrid = {(g, int(b), round(float(m), 3)): {qc: float(transform(qc, r[qc])) for qc in SHARED}
               for g, b, m, r in zip(nomt["geometry"], nomt["bhf_kN"], nomt["friction_coefficient"],
                                     nomt.to_dict("records"))}
    _CTX.update(t=t, sims=sims, floors=floors, simgrid=simgrid,
                tq={(a, q): r for a, q, r in zip(t["alternative"], t["qc"], t.to_dict("records"))},
                mu_grid=np.sort(nomt["friction_coefficient"].round(3).unique()))
    if parts is not None:
        _CTX["parts"] = parts
    for f in (m3_fit, m3_nested, m5_fit, friction_fit):
        f.cache_clear()


def load_floors() -> dict:
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    return {(qc, geo): float(fl.loc[qc, f"floor_{geo}"]) for qc in SHARED for geo in ("concave", "convex")}


def gp_diagnostics(iv: pd.DataFrame) -> pd.DataFrame:
    """Share of the Gaussian-process fits (one per calibration set and characteristic) with the noise level
    or a length scale at a bound."""
    g = iv[iv["method"].isin(["M5", "M5n"])].copy()
    loo = g["calibration"].isin(["within", "pooled"])          # one calibration set per held-out alternative
    g["fit"] = g["calibration"] + np.where(loo, "|" + g["alternative"], "")
    g = g.drop_duplicates(["scope", "fit", "qc", "method"])
    return g.groupby(["scope", "method"]).agg(
        fits=("qc", "size"), noise_at_bound=("gp_noise_at_bound", "mean"),
        length_scale_at_bound=("gp_ls_at_bound", lambda s: float((s > 0).mean())),
        median_ls_bhf=("gp_ls_bhf", "median"), median_noise=("gp_noise", "median")).reset_index()


def main(with_m3: bool = True) -> None:
    parts = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    parts = match_sims(parts, sims)
    t, reps = alternative_table(parts, sims)
    t.to_csv(RESULTS / "dec_alternatives.csv", index=False)
    np.save(RESULTS / "dec_q95_reps.npy", reps)
    setup(t, sims, load_floors(), parts)
    mg = []
    for qc, g in t.groupby("qc"):
        r2 = g["real_q95"] - g["sim_env_hi"]
        mg.append({"qc": qc, "offset_env": float(np.median(r2)),
                   "margin": conformal_margin(np.abs(r2 - np.median(r2)).to_numpy(), CONF_LEVEL),
                   "offset_nominal": float(np.median(g["real_q95"] - g["sim_nominal"])),
                   "n_alternatives": int(len(g))})
    pd.DataFrame(mg).to_csv(RESULTS / "dec_margins.csv", index=False)

    _CTX["with_m3"] = with_m3
    if with_m3 and N_JOBS > 1:            # characteristics are independent; each worker fits its own models
        with Pool(min(N_JOBS, len(SHARED))) as pool:
            chunks = pool.map(qc_records, SHARED)
    else:
        chunks = [qc_records(qc) for qc in SHARED]
    d = pd.DataFrame([r for c, _ in chunks for r in c])
    iv = pd.DataFrame([r for _, c in chunks for r in c])
    iv["scope"] = iv["calibration"].map(scope_of)
    ref_row = {(a, q): i for i, (a, q) in enumerate(zip(t["alternative"], t["qc"]))}
    iv["ref_row"] = [ref_row[(a, q)] for a, q in zip(iv["alternative"], iv["qc"])]
    iv.to_csv(RESULTS / "dec_intervals.csv", index=False)
    d.to_csv(RESULTS / "dec_verdicts.csv.gz", index=False)
    sc = score(d, ["calibration", "qc", "method"]).reset_index()
    sc.to_csv(RESULTS / "dec_scores.csv", index=False)
    d["scope"] = d["calibration"].map(scope_of)
    d = with_relation_scopes(d)
    ivr = with_relation_scopes(iv)
    overall = score(d, ["scope", "method"]).reset_index()
    paired = []
    res = distances(ivr, reps, paired=paired)
    res.to_csv(RESULTS / "dec_resolution.csv", index=False)
    pairs = pd.DataFrame(paired)
    pairs.to_csv(RESULTS / "dec_paired.csv", index=False)
    cov = coverage(ivr)
    cov.to_csv(RESULTS / "dec_coverage.csv", index=False)
    gpd = gp_diagnostics(ivr)
    gpd.to_csv(RESULTS / "dec_gp.csv", index=False)
    rel = reliability(ivr)
    rel.to_csv(RESULTS / "dec_reliability.csv", index=False)
    curve = score(d, ["scope", "method", "d"]).reset_index()
    curve.to_csv(RESULTS / "dec_curve.csv", index=False)

    allq = res[res["qc"] == "all"].copy()
    allq["decisive (95 % CI)"] = [f"{r:g} ({lo:g}-{hi:g})" for r, lo, hi in
                                 zip(allq["resolution_floors"], allq["resolution_lo"], allq["resolution_hi"])]
    allq["safe (95 % CI)"] = [f"{r:g} ({lo:g}-{hi:g})" for r, lo, hi in
                             zip(allq["safe_floors"], allq["safe_lo"], allq["safe_hi"])]
    lines = ["# Design-stage decisions scored against production", "",
             f"Adequate: at least {ADEQUATE_RATE:.0%} of the parts conform. Interval level {CONF_LEVEL:.0%}. "
             f"Nominal simulation: t = {NOMINAL_THICKNESS} mm, friction {NOMINAL_FRICTION}. Distances are exact "
             f"(evaluation step {FINE[1]:g} floors); requirements below zero are left out.", "",
             "## Offset between parts and matched simulations (median over alternatives; signed)", "",
             t.pivot_table(index="qc", columns="geometry", values="gap_matched_signed", aggfunc="median")
             .round(3).to_markdown(), "",
             f"## Distances over all characteristics ({N_BOOT_DEC} family-stratified resamples of the design cases "
             f"with reference replicates)", "",
             allq[["scope", "method", "n_cases", "decisive (95 % CI)", "safe (95 % CI)", "resolution_failing",
                   "safe_failing", "resolution_adequate", "safe_adequate"]].to_markdown(index=False), "",
             "## Paired differences between rules (all characteristics; a minus b, floors)", "",
             pairs.round(3).to_markdown(index=False), "",
             "## Interval rules: empirical coverage, median half-width (floors), interval centre as a point rule", "",
             cov.round(3).to_markdown(index=False), "",
             "## Gaussian-process fits: hyperparameters at a bound", "", gpd.round(3).to_markdown(index=False), "",
             "## Share of decided verdicts that are correct, by the margin between prediction and requirement "
             "(requirements within 20 floors of the truth)", "",
             rel.pivot_table(index=["scope", "method"], columns="margin_floors", values="correct_when_decided")
             .round(3).to_markdown(), "",
             "## Decision rates over all characteristics (requirement grid)", "",
             overall.round(3).to_markdown(index=False), "",
             "## Decisive distance per characteristic (floors)", "",
             res.pivot_table(index="qc", columns=["scope", "method"], values="resolution_floors").round(2).to_markdown(),
             "", "## Safe distance per characteristic (floors)", "",
             res.pivot_table(index="qc", columns=["scope", "method"], values="safe_floors").round(2).to_markdown()]
    (RESULTS / "summary_decisions.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:40]))


if __name__ == "__main__":
    main(with_m3="--no-m3" not in sys.argv)
