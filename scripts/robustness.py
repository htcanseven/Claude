"""Robustness of the findings to the known weaknesses of the data and to the analysis constants.

The alternative-level rules (M0, M0w, M1, M1s, M2, M5, and without the simulation M1sn, M1n, NN, M2n, M5n) are refitted
for every variant and scored exactly as in decisions.py (point estimates). Scopes: within (a sibling at the
target's force is produced), setting (a new process setting; interpolation and extrapolation), transfer
(a new family) and, in variant 9, lubricant.

1. Punch temperature drifts by a few kelvin within a series: every characteristic is corrected with the
   pooled within-alternative slope on the punch temperature, and floors, effect-to-scatter shares and rules
   are recomputed.
2. Blank-holder force is confounded with stroke speed (the 100 kN series ran slower): the force effects are
   split into 100->300 kN pairs (speed changes) and 300->500 kN pairs (same speed).
3. Interval level 0.80 / 0.95 instead of 0.90 (M2, M5, M2n, M5n). Within a family M2's margin is the largest
   of eight residuals at every level, so only the pooled and transfer rows can change for M2.
4. Resolution target 0.90 / 0.99 instead of 0.95 (all rules; stored intervals).
5. Floor constants: batch size 25 / 100 and quantile 0.90 / 0.99 (all rules; stored intervals rescaled by the
   per-geometry floors of sensitivity.py).
6. Adequacy share p = 0.90 / 0.99: the decided statistic is the 90th / 99th percentile.
7. Smoothed simulation: nominal value and envelope from a quadratic response surface over sheet thickness and
   friction in each geometry x force cell, which removes the extraction noise of the 1 mm mesh.
8. Specification of the Gaussian processes (M5, M5n): Matern 5/2 instead of the squared exponential; with a
   linear trend (universal kriging); lubrication as two indicators; length scales of at least 100 kN and one
   pattern step; and without the noise floor (the first version of M5).
9. Leave one lubrication pattern out of a family (scope 'lubricant').
10. M3 with the pattern's median oil film for the simulation match and the model input (within the family).
11. M6: the M5 mean with a conformal margin on standardised leave-one-out residuals.
12. Refitting bootstrap: the lubrication patterns of each geometry are resampled with replacement (at least two
    distinct patterns, so that every target keeps a sibling; copies of the target never calibrate it), and every
    fast rule is refitted and rescored on each resample (within, setting, transfer). The forces are kept, so
    every case keeps its evidence relation. There are seven distinct draws per geometry (49 configurations, the
    original one among them); in a draw with a duplicated pattern a new variant keeps one distinct sibling, the
    calibration set has fewer distinct alternatives, and the duplicated series enter the GP noise floor as
    identical pairs. The interval therefore shows how the distances change when a pattern is lost, not the
    sampling uncertainty around the reported values; paired refit intervals are given for key rule pairs.
13. The GP noise floor of the first version (the sampling variance of q95 alone; GP variant 'se_floor').
14. Thermal transient: the first 150 parts of every series (the punch warm-up) are dropped; floors, truths and
    rules are recomputed from parts 151-500.
15. Between-series floor: the floor taken over batch pairs from different series of one geometry and force,
    which contains the variation between runs (and the lubrication effect), an upper bound of the unit.
16. Short calibration series: the calibration alternatives' q95 from their first 50, 100 or 250 parts only
    (the truth of the held-out alternative and the floors stay those of the full series).

Outputs: results/rob_floor.csv, rob_bhf_pairs.csv, rob_decisions.csv, rob_refit.csv, rob_refit_paired.csv,
summary_robustness.md
"""

from __future__ import annotations

import sys
import warnings
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
from alternatives import analyse, batch_centres, batches, floor_from, within_slope  # noqa: E402
from common import RESULTS, centre  # noqa: E402
from qc import QCS, SHARED, parts_qc, sims_qc  # noqa: E402

FAST = ["M0", "M0w", "M1", "M1s", "M2", "M5", "M1sn", "M1n", "NN", "M2n", "M5n"]
SCOPES = ("within", "setting", "transfer")
CONF_LEVELS = [0.80, 0.95]
RESOLUTION_TARGETS = [0.90, 0.99]
ADEQUACY = [0.90, 0.99]
GP_VARIANTS = ["matern", "linear", "onehot", "ls_floor", "no_noise_floor", "se_floor"]
N_REFIT = 200
REFIT_RULES = ["M1", "M1s", "M2", "M5", "NN", "M5n", "M2n", "M1n", "M1sn"]
REFIT_PAIRS = [("NN", "M5"), ("NN", "M5n"), ("M5", "M5n"), ("M2", "M2n"), ("M1s", "NN"), ("M1", "M1n"),
               ("M1s", "M1"), ("M1s", "M1sn"), ("M1sn", "NN")]
WARM_UP = 150                  # parts dropped at the start of every series (thermal transient)
SHORT_SERIES = [50, 100, 250]  # parts per calibration series in the short-series variant


# ── fast rules ────────────────────────────────────────────────────────────────
def jobs_for(alts: list[str], scopes) -> list[tuple[str, list[str], list[str]]]:
    geo_of = {a: a.split("/")[0] for a in alts}
    jobs = []
    if "within" in scopes:          # targets once; repeated calibration alternatives act as weights
        jobs += [("within", [b for b in alts if b != a and geo_of[b] == geo_of[a]], [a]) for a in dict.fromkeys(alts)]
    for scope, key in (("setting", D.bhf_of), ("lubricant", lambda a: a.split("/")[2])):
        if scope in scopes:
            for geo, lev in sorted({(geo_of[a], key(a)) for a in alts}):
                held = [b for b in alts if geo_of[b] == geo and key(b) == lev]
                jobs.append((scope, [b for b in alts if geo_of[b] == geo and b not in held], held))
    if "transfer" in scopes:
        for s, d in (("concave", "convex"), ("convex", "concave")):
            jobs.append(("transfer", [b for b in alts if geo_of[b] == s], [b for b in alts if geo_of[b] == d]))
    return jobs


def fast_intervals(t: pd.DataFrame, floors: dict, scopes=SCOPES, level: float = D.CONF_LEVEL,
                   rules=FAST, alts: list[str] | None = None) -> pd.DataFrame:
    """Intervals of the alternative-level rules for every scope; alts may repeat alternatives (bootstrap)."""
    D._CTX.update(t=t, floors=floors)
    D.m5_fit.cache_clear()
    z = norm.ppf(0.5 + level / 2)
    alts = sorted(t["alternative"].unique()) if alts is None else alts
    rows = []
    for qc in SHARED:
        tq = t[t["qc"] == qc].drop_duplicates("alternative").set_index("alternative")
        for scope, calib, targets in jobs_for(alts, scopes):
            if not calib:
                continue
            c = tq.loc[calib]
            r2 = (c["real_q95"] - c["sim_env_hi"]).to_numpy()
            qv = c["real_q95"].to_numpy()
            off2, med = float(np.median(r2)), float(np.median(qv))
            m2 = D.conformal_margin(np.abs(r2 - off2), level)
            m2n = D.conformal_margin(np.abs(qv - med), level)
            off1 = float(np.median(c["real_q95"] - c["sim_nominal"]))
            s0 = c["sim_nominal"].to_numpy()
            b1, a1 = np.polyfit(s0, qv, 1) if np.ptp(s0) > 0 and len(qv) >= 2 else (1.0, off1)
            fv = c["bhf_kN"].to_numpy(float)
            bf, af = np.polyfit(fv, qv, 1) if np.ptp(fv) > 0 and len(qv) >= 2 else (0.0, float(np.mean(qv)))
            gps = {}
            for name, use_sim in (("M5", True), ("M5n", False)):
                if name in rules and len(set(calib)) >= 2:
                    gps[name] = D.m5_fit(tuple(sorted(calib)), qc, use_sim)
            for a in dict.fromkeys(targets):
                s = tq.loc[a]
                iv = {"M0": (s["sim_nominal"],) * 2, "M0w": (s["sim_env_lo"], s["sim_env_hi"]),
                      "M1": (s["sim_nominal"] + off1,) * 2, "M1s": (a1 + b1 * s["sim_nominal"],) * 2,
                      "M2": (s["sim_env_hi"] + off2 - m2, s["sim_env_hi"] + off2 + m2),
                      "M1sn": (af + bf * float(s["bhf_kN"]),) * 2,
                      "M1n": (med, med), "NN": (D.nn_point(calib, a, qc),) * 2, "M2n": (med - m2n, med + m2n)}
                for name, (gp, keep) in gps.items():
                    mu, sd = gp.predict(D.descriptors([a])[:, keep], return_std=True)
                    base = s["sim_env_hi"] if name == "M5" else 0.0
                    iv[name] = (base + mu[0] - z * sd[0], base + mu[0] + z * sd[0])
                rel = D.relation(calib, a)
                for name in rules:
                    if name in iv:
                        rows.append({"scope": scope, "relation": rel, "method": name, "qc": qc, "alternative": a,
                                     "geometry": s["geometry"], "lo": float(iv[name][0]), "hi": float(iv[name][1]),
                                     "real_q95": float(s["real_q95"]), "floor": floors[(qc, s["geometry"])]})
    return pd.DataFrame(rows)


def point_distances(iv: pd.DataFrame, label: str, target: float = D.RESOLUTION_TARGET) -> pd.DataFrame:
    iv = D.with_relation_scopes(iv)
    rows = []
    for (scope, method), g in iv.groupby(["scope", "method"]):
        u, v, cap = D.exclusion(g)
        rows.append({"variant": label, "scope": scope, "method": method,
                     **D.distance_pair(u, v, cap, sides=True, target=target)})
    return pd.DataFrame(rows)


# ── variants of the data ──────────────────────────────────────────────────────
def temperature_adjusted(q: pd.DataFrame) -> pd.DataFrame:
    q = q.copy()
    t_mean = q.groupby("alternative")["punch_temp_C"].transform("mean")
    for c in QCS:
        b = within_slope(q, c, "punch_temp_C")
        q[c] = q[c] - b * (q["punch_temp_C"] - t_mean).fillna(0.0)
    return q


def floors_and_shares(q: pd.DataFrame, label: str) -> list[dict]:
    qb = batches(q)
    res = analyse(qb, list(QCS))
    e = res["effects"].assign(res=lambda x: x["esr"] >= 1)
    share = e.groupby(["qc", "family"])["res"].mean().unstack()
    mrc = res["mrc"].set_index(["qc", "factor"])["mrc"]
    out = []
    for c in QCS:
        geo = {g: floor_from(batch_centres(qb[qb["geometry"] == g], list(QCS)), c) for g in ("concave", "convex")}
        out.append({"variant": label, "qc": c, "floor": res["floors"][c], "floor_concave": geo["concave"],
                    "floor_convex": geo["convex"], "share_bhf": share.loc[c, "bhf"],
                    "share_geometry": share.loc[c, "geometry"], "share_lubrication": share.loc[c, "lubrication"],
                    "mrc_bhf_kN": mrc.loc[(c, "bhf_kN")]})
    return out


def quantile_table(parts: pd.DataFrame, t: pd.DataFrame, p: float) -> pd.DataFrame:
    """The alternative table with the p-quantile of the parts (and its block-bootstrap error) as the truth."""
    t = t.copy()
    for i, r in t.iterrows():
        y = D.transform(r["qc"], parts.loc[parts["alternative"] == r["alternative"], r["qc"]].dropna().to_numpy())
        rng = np.random.default_rng(D.stable_seed("quantile", str(p), r["alternative"], r["qc"]))
        blocks = [y[j:j + D.REF_BLOCK] for j in range(0, len(y), D.REF_BLOCK)]
        reps = [np.quantile(np.concatenate([blocks[k] for k in rng.integers(0, len(blocks), len(blocks))]), p)
                for _ in range(200)]
        t.loc[i, "real_q95"] = float(np.quantile(y, p))
        t.loc[i, "real_q95_se"] = float(np.std(reps, ddof=1))
    return t


def smoothed_table(t: pd.DataFrame, sims: pd.DataFrame) -> pd.DataFrame:
    """Nominal simulation and envelope from a quadratic response surface over thickness and friction."""
    t = t.copy()
    for (geo, bhf), h in sims.groupby(["geometry", "bhf_kN"]):
        th, mu = h["sheet_metal_thickness"].to_numpy(), h["friction_coefficient"].to_numpy()
        A = np.column_stack([np.ones_like(th), th, mu, th * th, mu * mu, th * mu])
        a0 = np.array([1.0, D.NOMINAL_THICKNESS, D.NOMINAL_FRICTION, D.NOMINAL_THICKNESS ** 2,
                       D.NOMINAL_FRICTION ** 2, D.NOMINAL_THICKNESS * D.NOMINAL_FRICTION])
        for qc in SHARED:
            ok = np.isfinite(h[qc].to_numpy())
            coef, *_ = np.linalg.lstsq(A[ok], h[qc].to_numpy()[ok], rcond=None)
            fit = D.transform(qc, A @ coef)
            sel = (t["geometry"] == geo) & (t["bhf_kN"] == bhf) & (t["qc"] == qc)
            t.loc[sel, "sim_nominal"] = float(D.transform(qc, a0 @ coef))
            t.loc[sel, "sim_env_lo"], t.loc[sel, "sim_env_hi"] = float(fit.min()), float(fit.max())
    return t


# ── 10. M3 with the friction of the pattern's median oil film ────────────────
def m3_within(qc: str) -> list[dict]:
    from threadpoolctl import threadpool_limits

    t, floors = D._CTX["t"], D._CTX["floors"]
    alts = sorted(t["alternative"].unique())
    geo_of = {a: a.split("/")[0] for a in alts}
    rows = []
    with threadpool_limits(1):
        for a in alts:
            calib = [b for b in alts if b != a and geo_of[b] == geo_of[a]]
            lo3, hi3 = D.m3_calibrated(calib, a, qc)
            s = t[(t["alternative"] == a) & (t["qc"] == qc)].iloc[0]
            rows.append({"scope": "within", "relation": "sibling", "method": "M3", "qc": qc, "alternative": a,
                         "geometry": s["geometry"], "lo": lo3, "hi": hi3,
                         "real_q95": float(s["real_q95"]), "floor": floors[(qc, s["geometry"])]})
    return rows


# ── 11. conformalised Gaussian process ───────────────────────────────────────
def m6_intervals(t: pd.DataFrame, floors: dict) -> pd.DataFrame:
    D._CTX.update(t=t, floors=floors)
    D.m5_fit.cache_clear()
    alts = sorted(t["alternative"].unique())
    rows = []

    def gp_pred(calib, target, qc):
        gp, keep = D.m5_fit(tuple(sorted(calib)), qc)
        mu, sd = gp.predict(D.descriptors([target])[:, keep], return_std=True)
        return float(mu[0]), float(sd[0])

    for qc in SHARED:
        tq = t[t["qc"] == qc].set_index("alternative")
        for scope, calib, targets in jobs_for(alts, SCOPES):
            z = []
            for b in calib:
                mu_b, sd_b = gp_pred([x for x in calib if x != b], b, qc)
                z.append(abs(tq.loc[b, "real_q95"] - tq.loc[b, "sim_env_hi"] - mu_b) / max(sd_b, 1e-12))
            qz = D.conformal_margin(np.array(z), D.CONF_LEVEL)
            for a in targets:
                mu, sd = gp_pred(calib, a, qc)
                env = tq.loc[a, "sim_env_hi"]
                rows.append({"scope": scope, "relation": D.relation(calib, a), "method": "M6", "qc": qc,
                             "alternative": a, "geometry": tq.loc[a, "geometry"], "lo": env + mu - qz * sd,
                             "hi": env + mu + qz * sd, "real_q95": float(tq.loc[a, "real_q95"]),
                             "floor": floors[(qc, tq.loc[a, "geometry"])]})
    return pd.DataFrame(rows)


# ── 12. refitting bootstrap ───────────────────────────────────────────────────
def refit_one(b: int) -> pd.DataFrame:
    """One refitting resample: the lubrication patterns of each geometry are drawn with replacement (at least
    two distinct ones), all forces kept. A target's copies never calibrate it (jobs_for excludes its name), so a
    new variant keeps a sibling, a new setting its forces and a new family its source."""
    from threadpoolctl import threadpool_limits

    t, floors = D._CTX["t_ref"], D._CTX["floors_ref"]
    alts = sorted(t["alternative"].unique())
    rng = np.random.default_rng(D.stable_seed("refit-patterns", str(b)))
    pick = []
    for geo in ("concave", "convex"):
        pats = sorted({a.split("/")[2] for a in alts if a.startswith(geo)})
        draw = rng.choice(pats, len(pats))
        while len(set(draw)) < 2:
            draw = rng.choice(pats, len(pats))
        for pat in draw:
            pick += [a for a in alts if a.startswith(geo) and a.split("/")[2] == pat]
    with threadpool_limits(1):
        iv = fast_intervals(t, floors, ("within", "setting", "transfer"), rules=REFIT_RULES, alts=sorted(pick))
    # every copy of a resampled target counts once
    mult = pd.Series(pick).value_counts()
    iv = iv.loc[iv.index.repeat(iv["alternative"].map(mult).to_numpy())]
    return point_distances(iv, f"refit {b}").assign(boot=b)


# ── 14.-16. variants of the parts used ───────────────────────────────────────
def part_slice(q: pd.DataFrame, start: int = 0, stop: int | None = None) -> pd.DataFrame:
    """Parts start..stop-1 of every series, in production order."""
    pos = q.groupby("alternative").cumcount()
    keep = (pos >= start) & ((pos < stop) if stop is not None else True)
    return q[keep]


def geometry_floors(q: pd.DataFrame) -> dict:
    qb = batches(q)
    return {(c, g): floor_from(batch_centres(qb[qb["geometry"] == g], [c]), c) for c in SHARED
            for g in ("concave", "convex")}


def between_series_floors(q: pd.DataFrame) -> dict:
    """ALPHA-quantile of |m_i - m_j| over pairs of batches from different series of one geometry and force."""
    qb = batches(q)
    bc = batch_centres(qb, list(SHARED))
    out = {}
    for c in SHARED:
        for geo in ("concave", "convex"):
            diffs = []
            cells = {}
            for (alt, _), v in bc[c].dropna().items():
                if alt.startswith(geo):
                    cells.setdefault(D.bhf_of(alt), {}).setdefault(alt, []).append(v)
            for series in cells.values():
                names = list(series)
                for i in range(len(names)):
                    for j in range(i + 1, len(names)):
                        a, b = np.array(series[names[i]]), np.array(series[names[j]])
                        diffs.append(np.abs(a[:, None] - b[None, :]).ravel())
            out[(c, geo)] = float(np.quantile(np.concatenate(diffs), 0.95))
    return out


def main() -> None:
    warnings.filterwarnings("ignore")
    f = pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False)
    q = parts_qc(f)
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    floors = D.load_floors()
    t_ref = pd.read_csv(RESULTS / "dec_alternatives.csv")
    iv_ref = pd.read_csv(RESULTS / "dec_intervals.csv")
    D.setup(t_ref, sims, floors)
    dec = [point_distances(fast_intervals(t_ref, floors), "reference")]

    # 1. temperature
    qa = temperature_adjusted(q)
    rob_floor = pd.DataFrame(floors_and_shares(q, "reference") + floors_and_shares(qa, "temperature-adjusted"))
    rob_floor.to_csv(RESULTS / "rob_floor.csv", index=False)
    fa = rob_floor[rob_floor["variant"] == "temperature-adjusted"].set_index("qc")
    floors_adj = {(c, g): float(fa.loc[c, f"floor_{g}"]) for c in SHARED for g in ("concave", "convex")}
    t_adj, _ = D.alternative_table(D.match_sims(qa, sims), sims)
    dec.append(point_distances(fast_intervals(t_adj, floors_adj), "temperature-adjusted"))

    # 3. interval level
    for level in CONF_LEVELS:
        dec.append(point_distances(fast_intervals(t_ref, floors, level=level, rules=["M2", "M5", "M2n", "M5n"]),
                                   f"interval level {level:.2f}"))
    # 4. resolution target (stored intervals of every rule)
    for target in RESOLUTION_TARGETS:
        dec.append(point_distances(iv_ref, f"resolution target {target:.2f}", target=target))
    # 5. floor constants (stored intervals, floors of sensitivity.py)
    sf = pd.read_csv(RESULTS / "sens_floor.csv")
    for (b, a, stat), g in sf.groupby(["batch", "alpha", "stat"]):
        if stat != "trim" or (b, a) == (50, 0.95) or not ((b == 50) ^ (a == 0.95)):
            continue
        fl = g.set_index("qc")
        F = {(c, geo): float(fl.loc[c, f"floor_{geo}"]) for c in SHARED for geo in ("concave", "convex")}
        dec.append(point_distances(iv_ref.assign(floor=[F[(c, geo)] for c, geo in zip(iv_ref["qc"], iv_ref["geometry"])]),
                                   f"floor with batch {b} and quantile {a:.2f}"))
    # 6. adequacy share
    D._CTX["t"] = t_ref
    for p in ADEQUACY:
        dec.append(point_distances(fast_intervals(quantile_table(q, t_ref, p), floors), f"adequacy share {p:.2f}"))
    # 7. smoothed simulation
    dec.append(point_distances(fast_intervals(smoothed_table(t_ref, sims), floors), "smoothed simulation"))
    # 8. Gaussian-process specification
    for var in GP_VARIANTS:
        D._CTX["gp_variant"] = var
        dec.append(point_distances(fast_intervals(t_ref, floors, rules=["M5", "M5n"]), f"GP {var}"))
    D._CTX.pop("gp_variant", None)
    # 9. leave one lubrication pattern out
    dec.append(point_distances(fast_intervals(t_ref, floors, scopes=("lubricant",)), "leave one pattern out"))
    # 14. thermal transient excluded
    late = part_slice(q, WARM_UP)
    floors_late = geometry_floors(late)
    t_late, _ = D.alternative_table(D.match_sims(late, sims), sims)
    dec.append(point_distances(fast_intervals(t_late, floors_late), f"first {WARM_UP} parts dropped"))
    D._CTX["t"] = t_ref
    # 15. floor with the between-series component (stored intervals rescaled)
    fbs = between_series_floors(q)
    pd.DataFrame([{"qc": c, "geometry": g, "floor_between_series": v, "floor": floors[(c, g)]}
                  for (c, g), v in fbs.items()]).to_csv(RESULTS / "rob_floor_between.csv", index=False)
    dec.append(point_distances(iv_ref.assign(floor=[fbs[(c, g)] for c, g in zip(iv_ref["qc"], iv_ref["geometry"])]),
                               "floor between series"))
    # 16. short calibration series: q95 of the calibration alternatives from their first n parts
    truth = t_ref.set_index(["alternative", "qc"])["real_q95"]
    for n in SHORT_SERIES:
        t_n, _ = D.alternative_table(D.match_sims(part_slice(q, 0, n), sims), sims)
        iv_n = fast_intervals(t_n, floors)
        iv_n["real_q95"] = [truth[(a, c)] for a, c in zip(iv_n["alternative"], iv_n["qc"])]
        dec.append(point_distances(iv_n, f"calibration series of {n} parts"))
    D._CTX["t"] = t_ref

    # 2. blank-holder force pairs: speed change (100->300) against same speed (300->500)
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    eff = pd.read_csv(RESULTS / "alt_effects.csv")
    eff = eff[eff["family"] == "bhf"].copy()
    eff["pair"] = [f"{min(D.bhf_of(a), D.bhf_of(b))}->{max(D.bhf_of(a), D.bhf_of(b))}" for a, b in zip(eff["a"], eff["b"])]
    cent = q.groupby(["alternative"])[list(QCS)].agg(lambda s: centre(s.dropna().to_numpy()))
    pairs = []
    for (qc, pair), g in eff.groupby(["qc", "pair"]):
        slope = np.mean([(cent.loc[b, qc] - cent.loc[a, qc]) / (D.bhf_of(b) - D.bhf_of(a)) for a, b in zip(g["a"], g["b"])])
        pairs.append({"qc": qc, "pair": pair, "share_resolvable": float((g["esr"] >= 1).mean()),
                      "median_esr": float(g["esr"].median()), "slope_per_100kN": float(slope * 100),
                      "mrc_kN": float(fl.loc[qc, "floor"] / abs(slope))})
    pairs = pd.DataFrame(pairs)
    pairs.to_csv(RESULTS / "rob_bhf_pairs.csv", index=False)

    # 10. M3 with the pattern's median oil film for the simulation match and the input (within the family)
    parts = q.copy()
    oil_med = parts.groupby("oil_type")["oil_gm2"].transform("median")
    D.setup(t_ref, sims, floors, D.match_sims(parts.assign(oil_gm2=oil_med), sims))
    with Pool(min(D.N_JOBS, len(SHARED))) as pool:
        m3 = pd.DataFrame([r for chunk in pool.map(m3_within, SHARED) for r in chunk])
    dec.append(point_distances(m3, "M3, friction of the pattern's median oil film"))
    # 11. conformalised Gaussian process
    dec.append(point_distances(m6_intervals(t_ref, floors), "M6 conformalised GP"))

    rob = pd.concat(dec, ignore_index=True)
    rob.to_csv(RESULTS / "rob_decisions.csv", index=False)

    # 12. refitting bootstrap
    D._CTX.update(t_ref=t_ref, floors_ref=floors)
    with Pool(D.N_JOBS) as pool:
        boots = pd.concat(pool.map(refit_one, range(N_REFIT)), ignore_index=True)
    ref = rob[rob["variant"] == "reference"].set_index(["scope", "method"])
    paired = []
    for scope, g in boots.groupby("scope"):
        for kind in ("resolution_floors", "safe_floors"):
            w = g.pivot_table(index="boot", columns="method", values=kind)
            for a, b in REFIT_PAIRS:
                if a in w and b in w:
                    x, y = w[a].to_numpy(), w[b].to_numpy()
                    diff = np.where(np.isinf(x) & np.isinf(y), 0.0, x - y)
                    paired.append({"scope": scope, "kind": kind, "rule_a": a, "rule_b": b,
                                   "diff": ref.loc[(scope, a), kind] - ref.loc[(scope, b), kind]
                                   if (scope, a) in ref.index and (scope, b) in ref.index else np.nan,
                                   "diff_lo": float(np.percentile(diff, 2.5)), "diff_hi": float(np.percentile(diff, 97.5)),
                                   "share_a_smaller": float(np.mean(x < y))})
    paired = pd.DataFrame(paired)
    paired.to_csv(RESULTS / "rob_refit_paired.csv", index=False)
    refit = []
    for (scope, method), g in boots.groupby(["scope", "method"]):
        if (scope, method) in ref.index:
            refit.append({"scope": scope, "method": method,
                          "resolution_floors": ref.loc[(scope, method), "resolution_floors"],
                          "resolution_lo": float(np.percentile(g["resolution_floors"], 2.5)),
                          "resolution_hi": float(np.percentile(g["resolution_floors"], 97.5)),
                          "safe_floors": ref.loc[(scope, method), "safe_floors"],
                          "safe_lo": float(np.percentile(g["safe_floors"], 2.5)),
                          "safe_hi": float(np.percentile(g["safe_floors"], 97.5))})
    refit = pd.DataFrame(refit)
    refit.to_csv(RESULTS / "rob_refit.csv", index=False)
    lines = ["# Robustness", "",
             "## Floors and effect-to-scatter shares, reference against temperature-adjusted", "",
             rob_floor.round(4).to_markdown(index=False), "",
             "## Blank-holder force pairs: 100->300 kN (stroke speed changes) against 300->500 kN (same speed)", "",
             pairs.round(3).to_markdown(index=False), "",
             "## Decision distances (floors) under the variants", "",
             rob.pivot_table(index=["variant", "method"], columns="scope", values=["resolution_floors", "safe_floors"])
             .round(2).to_markdown(), "",
             f"## Refitting bootstrap ({N_REFIT} resamples of the lubrication patterns within each geometry)", "",
             refit.round(2).to_markdown(index=False), "",
             "## Paired refit differences (a minus b, floors)", "", paired.round(2).to_markdown(index=False)]
    (RESULTS / "summary_robustness.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[-20:]))


if __name__ == "__main__":
    main()
