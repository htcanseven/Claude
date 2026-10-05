"""Analyses requested in review, computed from the stored decision results and the parts.

 1. Decomposition: two-way partition of the sums of squares of the log decisive distances of the calibrated rules
    by evidence relation and rule, over all three relations and within the family only (without replication, so
    the interaction is the residual).
 2. Sibling strata: the new-variant cases split by how many of the two siblings production resolves from the held-out
    alternative (effect-to-scatter ratio >= 1, alt_effects.csv).
 3. Force levels: the new-setting cases split by the held-out force (100 kN: extrapolation at a slower stroke; 500 kN:
    extrapolation at the same speed; 300 kN: interpolation).
 4. New family in the source family's floor: transfer cases rescored with the floor of the produced family, which a
    design team would have, and every scope per characteristic in the characteristic's unit.
 5. Weight of the failing side: feasible failing-side requirements at given distances (a limit below zero on a
    non-negative characteristic is no requirement).
 6. The procedure's decision rule (step 6): a guard band g on the observable margin between the predicted interval
    and the requirement, the smallest margin beyond which at least 95 % of the decided verdicts are correct for
    requirements on the grid within 20 floors of the truth (the prior of decisions.reliability), and the operating
    characteristics of the rule with that guard band (its interval widened by g floors on both sides).
 7. Capability-anchored requirements: upper limits at which each alternative has Ppk = 1.0, 1.33, 1.67 and 2.0
    (centre + 3 Ppk sd of its parts); every alternative meets them, so a verdict is right (meets), a false reject or
    a trial.
 8. The nominal simulation without the definitional offset of the cup depth (reference surface and drawing depth):
    the median matched centre difference of the cup depth is added to its nominal simulation.
 9. A production-informed baseline for a new family where a drawing nominal exists (wall angle): the target's design
    angle plus the median deviation q95 - design angle of the produced family.
10. Floor protocol: batch-centre differences by time lag (a variogram of the floor), the within-batch and
    between-batch standard deviations, and the floor in units of the long- and short-term standard deviations.
11. Measurement resolution: the step between adjacent values of each characteristic relative to its floor.
12. Run metadata: start temperature, warm-up rise, sheet thickness and stroke speed per series.

Outputs: results/panel_*.csv, summary_panel.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
from alternatives import BATCH, batch_centres, batches  # noqa: E402
from common import RESULTS  # noqa: E402
from qc import SHARED, parts_qc  # noqa: E402

CAL_RULES = ["M1", "M1s", "Mc", "M2", "M3", "M5", "M1n", "NN", "M2n", "M4", "M5n"]
CORE = ["M0", "M1", "M1s", "M2", "M5", "M5n", "NN"]
SCOPES = ["within", "setting", "transfer"]
PPK = [1.0, 1.33, 1.67, 2.0]
GUARD_GRID = np.round(np.arange(0.0, 20.0 + 1e-9, 0.25), 2)
CHECK = [10.0, 20.0]
DESIGN_WALL_DEG = {"concave": 20.0, "convex": 10.0}
DELTAS = [1.0, 3.4, 8.5, 16.0, 35.0, 108.0]


def dist(g: pd.DataFrame, floor: np.ndarray | None = None, sides: bool = True) -> dict:
    """Exact decisive and safe distances of a set of cases, optionally with other floors."""
    g = g if floor is None else g.assign(floor=floor)
    return D.distance_pair(*D.exclusion(g), sides=sides)


def outcomes(g: pd.DataFrame, d: float, band: float = 0.0) -> dict:
    """Shares of right, wrong and trial verdicts at |d| floors (failing side where feasible), interval widened by band."""
    q, F = g["real_q95"].to_numpy(float), g["floor"].to_numpy(float)
    lo, hi = g["lo"].to_numpy(float) - band * F, g["hi"].to_numpy(float) + band * F
    ra, rf = q + d * F, q - d * F
    feas = rf >= 0
    right = (hi <= ra).astype(int) + (feas & (lo > rf)).astype(int)
    wrong = (lo > ra).astype(int) + (feas & (hi <= rf)).astype(int)
    n = 1 + feas.astype(int)
    tot = n.sum()
    return {f"right_{d:g}": right.sum() / tot, f"wrong_{d:g}": wrong.sum() / tot,
            f"trial_{d:g}": (n - right - wrong).sum() / tot}


# 1 ─────────────────────────────────────────────────────────────────────────────
def decomposition(res: pd.DataFrame) -> pd.DataFrame:
    rows = []
    r = res[(res["qc"] == "all") & res["method"].isin(CAL_RULES)]
    for kind, tf in (("resolution_floors", np.log), ("safe_floors", np.log1p)):
        for name, scopes in (("all relations", SCOPES), ("within the family", SCOPES[:2])):
            m = r[r["scope"].isin(scopes)].pivot(index="method", columns="scope", values=kind)
            m = m.replace([np.inf, -np.inf], np.nan).dropna()
            y = tf(m.to_numpy(float))
            grand = y.mean()
            ss_t = ((y - grand) ** 2).sum()
            ss_rel = y.shape[0] * ((y.mean(axis=0) - grand) ** 2).sum()
            ss_rule = y.shape[1] * ((y.mean(axis=1) - grand) ** 2).sum()
            rows.append({"distance": kind, "relations": name, "rules": len(m), "share_relation": ss_rel / ss_t,
                         "share_rule": ss_rule / ss_t, "share_interaction": 1 - (ss_rel + ss_rule) / ss_t,
                         "best_rule_range": f"{np.exp(y.min(axis=0)).round(2).tolist()}" if kind.startswith("res") else ""})
    return pd.DataFrame(rows)


# 2 ─────────────────────────────────────────────────────────────────────────────
def sibling_strata(iv: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    eff = pd.read_csv(RESULTS / "alt_effects.csv")
    lub = eff[eff["family"] == "lubrication"]
    res = {}
    for a, b, qc, e in zip(lub["a"], lub["b"], lub["qc"], lub["esr"]):
        res.setdefault((a, qc), []).append(e >= 1)
        res.setdefault((b, qc), []).append(e >= 1)
    w = iv[iv["scope"] == "within"].copy()
    w["resolved_siblings"] = [int(sum(res.get((a, q), []))) for a, q in zip(w["alternative"], w["qc"])]
    rows = []
    for (k, m), g in w.groupby(["resolved_siblings", "method"]):
        mid = (g["lo"] + g["hi"]) / 2
        rows.append({"resolved_siblings": k, "method": m, "cases": len(g), **dist(g),
                     "abs_error_p90": float(np.quantile(np.abs(mid - g["real_q95"]) / g["floor"], 0.9))})
    counts = w.drop_duplicates(["alternative", "qc"]).groupby("resolved_siblings").size().rename("cases").reset_index()
    return pd.DataFrame(rows), counts


# 3 ─────────────────────────────────────────────────────────────────────────────
def force_levels(iv: pd.DataFrame) -> pd.DataFrame:
    s = iv[iv["scope"] == "setting"]
    rows = []
    for (bhf, m), g in s.groupby(["bhf_kN", "method"]):
        rows.append({"bhf_kN": bhf, "relation": "interpolation" if bhf == 300 else "extrapolation", "method": m,
                     "cases": len(g), **dist(g)})
    return pd.DataFrame(rows)


# 4 ─────────────────────────────────────────────────────────────────────────────
def source_floor(iv: pd.DataFrame, floors: dict) -> pd.DataFrame:
    tr = iv[iv["scope"] == "transfer"]
    other = {"concave": "convex", "convex": "concave"}
    rows = []
    for m, g in tr.groupby("method"):
        f_src = np.array([floors[(q, other[geo])] for q, geo in zip(g["qc"], g["geometry"])])
        rows.append({"method": m, "floor": "target family", **dist(g)})
        rows.append({"method": m, "floor": "source family", **dist(g, f_src)})
    return pd.DataFrame(rows)


def physical_units(iv: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (scope, m, qc), g in iv[iv["scope"].isin(SCOPES) & iv["method"].isin(CORE + ["M3", "M4"])].groupby(
            ["scope", "method", "qc"]):
        rows.append({"scope": scope, "method": m, "qc": qc, **dist(g, np.ones(len(g)), sides=False)})
    return pd.DataFrame(rows)


# 5 ─────────────────────────────────────────────────────────────────────────────
def failing_weight(iv: pd.DataFrame) -> pd.DataFrame:
    w = iv[(iv["scope"] == "within") & (iv["method"] == "NN")]
    cap = (w["real_q95"] / w["floor"]).to_numpy()
    n = len(cap)
    return pd.DataFrame([{"delta": d, "cases": n, "feasible_failing": int((cap > d).sum()),
                          "weight_failing": float((cap > d).sum() / (n + (cap > d).sum()))} for d in DELTAS])


# 6 ─────────────────────────────────────────────────────────────────────────────
def guard_band(g: pd.DataFrame) -> tuple[float, pd.DataFrame]:
    """Smallest observable margin g beyond which >= 95 % of the decided verdicts are correct (grid prior)."""
    grid = D.D_GRID[np.abs(D.D_GRID) <= 20.0]
    lo, hi = g["lo"].to_numpy()[:, None], g["hi"].to_numpy()[:, None]
    F = g["floor"].to_numpy()[:, None]
    reqs = g["real_q95"].to_numpy()[:, None] + grid[None, :] * F
    feas = reqs >= 0
    meets, fails = (hi <= reqs) & feas, (lo > reqs) & feas
    margin = np.where(meets, (reqs - hi) / F, np.where(fails, (lo - reqs) / F, np.nan)).ravel()
    correct = ((meets & (grid >= 0)[None, :]) | (fails & (grid < 0)[None, :])).ravel()
    share = []
    for b in GUARD_GRID:
        sel = np.isfinite(margin) & (margin >= b)
        share.append(correct[sel].mean() if sel.any() else np.nan)
    share = np.array(share)
    ok = np.where(np.isnan(share), True, share >= D.RESOLUTION_TARGET)
    bad = np.flatnonzero(~ok)
    band = 0.0 if bad.size == 0 else (float(GUARD_GRID[bad[-1] + 1]) if bad[-1] + 1 < GUARD_GRID.size else np.inf)
    return band, pd.DataFrame({"margin": GUARD_GRID, "correct_when_decided": share})


def step6(ivr: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, curves = [], []
    scopes = SCOPES + ["setting/interpolation", "setting/extrapolation"]
    for (scope, m), g in ivr[ivr["scope"].isin(scopes) & ivr["method"].isin(CAL_RULES + ["M0", "M0w"])].groupby(
            ["scope", "method"]):
        band, curve = guard_band(g)
        curves.append(curve.assign(scope=scope, method=m))
        base = {"scope": scope, "method": m, "guard_band": band}
        alone = dist(g, sides=False)
        row = {**base, "decisive_alone": alone["resolution_floors"], "safe_alone": alone["safe_floors"]}
        for d in CHECK:
            row.update({f"{k}_alone": v for k, v in outcomes(g, d).items()})
        if np.isfinite(band):
            u, v, cap = D.exclusion(g)
            wide = D.distance_pair(u + band, v + band, cap)
            row.update({"decisive_step6": wide["resolution_floors"], "safe_step6": wide["safe_floors"]})
            for d in CHECK:
                row.update({f"{k}_step6": val for k, val in outcomes(g, d, band).items()})
        rows.append(row)
    return pd.DataFrame(rows), pd.concat(curves, ignore_index=True)


# 7 ─────────────────────────────────────────────────────────────────────────────
def capability(iv: pd.DataFrame, t: pd.DataFrame) -> pd.DataFrame:
    tt = t.set_index(["alternative", "qc"])
    rows = []
    sub = iv[iv["scope"].isin(SCOPES)]
    cen = np.array([tt.loc[(a, q), "real_centre"] for a, q in zip(sub["alternative"], sub["qc"])])
    sd = np.array([tt.loc[(a, q), "real_sd"] for a, q in zip(sub["alternative"], sub["qc"])])
    for p in PPK:
        R = cen + 3 * p * sd
        d = (R - sub["real_q95"].to_numpy()) / sub["floor"].to_numpy()
        meets, fails = sub["hi"].to_numpy() <= R, sub["lo"].to_numpy() > R
        frame = sub.assign(d=d, R=R, right=meets, false_reject=fails, trial=~meets & ~fails)
        for (scope, m), g in frame.groupby(["scope", "method"]):
            rows.append({"ppk": p, "scope": scope, "method": m, "median_d": float(np.median(g["d"])),
                         "right": g["right"].mean(), "false_reject": g["false_reject"].mean(), "trial": g["trial"].mean(),
                         "adequate": float((g["real_q95"] <= g["R"]).mean())})
    return pd.DataFrame(rows)


# 8 ─────────────────────────────────────────────────────────────────────────────
def m0_split(iv: pd.DataFrame, t: pd.DataFrame) -> pd.DataFrame:
    w = iv[(iv["scope"] == "within") & (iv["method"] == "M0")].copy()
    gap = float(t.loc[t["qc"] == "depth_op10", "gap_matched_signed"].median())
    rows = [{"variant": "nominal simulation", **dist(w)}]
    shift = np.where(w["qc"] == "depth_op10", gap, 0.0)
    rows.append({"variant": f"cup-depth reference offset removed ({gap:+.3f} mm)",
                 **dist(w.assign(lo=w["lo"] + shift, hi=w["hi"] + shift))})
    return pd.DataFrame(rows)


# 9 ─────────────────────────────────────────────────────────────────────────────
def nominal_offset(iv: pd.DataFrame, t: pd.DataFrame) -> pd.DataFrame:
    w = t[t["qc"] == "wall_op10"].set_index("alternative")
    other = {"concave": "convex", "convex": "concave"}
    tr = iv[(iv["scope"] == "transfer") & (iv["qc"] == "wall_op10")]
    rows = []
    base = tr[tr["method"] == "NN"].copy()
    dev = {g: float(np.median(w.loc[w["geometry"] == g, "real_q95"] - DESIGN_WALL_DEG[g])) for g in DESIGN_WALL_DEG}
    pred = np.array([DESIGN_WALL_DEG[g] + dev[other[g]] for g in base["geometry"]])
    frames = [base.assign(method="nominal + offset", lo=pred, hi=pred)]
    frames += [tr[tr["method"] == m] for m in ["M0", "M1", "M1s", "Mc", "M2", "M5", "M1n", "NN"]]
    for g in frames:
        m = g["method"].iloc[0]
        mid = (g["lo"] + g["hi"]) / 2
        err = np.abs(mid - g["real_q95"]) / g["floor"]
        rows.append({"method": m, "cases": len(g), **dist(g, sides=False), "median_abs_error": float(np.median(err)),
                     "abs_error_p90": float(np.quantile(err, 0.9))})
    return pd.DataFrame(rows)


# 10–12 ─────────────────────────────────────────────────────────────────────────
def floor_protocol(q: pd.DataFrame, floors: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
    qb = batches(q)
    bc = batch_centres(qb, list(SHARED))
    vario, prot = [], []
    for c in SHARED:
        for geo in ("concave", "convex"):
            F = floors[(c, geo)]
            sub = bc[c][[a.startswith(geo) for a in bc.index.get_level_values(0)]]
            by_lag = {}
            for _, s in sub.groupby(level=0):
                v = s.droplevel(0).dropna()
                idx, val = v.index.to_numpy(), v.to_numpy()
                for i in range(len(val)):
                    for j in range(i + 1, len(val)):
                        by_lag.setdefault(int(idx[j] - idx[i]), []).append(abs(val[i] - val[j]))
            for lag, dd in sorted(by_lag.items()):
                vario.append({"qc": c, "geometry": geo, "lag_batches": lag, "pairs": len(dd),
                              "q95_floors": float(np.quantile(dd, 0.95)) / F})
            parts = q[q["geometry"] == geo]
            lt, st, wb, bm = [], [], [], []
            for _, g in parts.groupby("alternative"):
                y = g[c].to_numpy(float)
                ok = np.isfinite(y)
                lt.append(np.nanstd(y))
                sub5 = pd.Series(y).groupby(np.arange(len(y)) // 5)
                st.append(np.sqrt(np.nanmean(sub5.var(ddof=1))))
                bw = pd.Series(y).groupby(np.arange(len(y)) // BATCH)
                wb.append(np.nanmean(bw.var(ddof=1)))
                bm.append(np.nanvar(bw.mean(), ddof=1))
            sw = float(np.sqrt(np.mean(wb)))
            sb = float(np.sqrt(max(np.mean(bm) - sw ** 2 / BATCH, 0.0)))
            prot.append({"qc": c, "geometry": geo, "floor": F, "sigma_lt": float(np.median(lt)),
                         "sigma_st": float(np.median(st)), "sigma_within_batch": sw, "sigma_between_batch": sb,
                         "floor_over_sigma_lt": F / float(np.median(lt)), "floor_over_sigma_st": F / float(np.median(st)),
                         "normal_model_floor": 1.96 * np.sqrt(2) * np.sqrt(sb ** 2 + sw ** 2 / BATCH)})
    return pd.DataFrame(vario), pd.DataFrame(prot)


def resolution_steps(q: pd.DataFrame, floors: dict, t: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for c in SHARED:
        steps, distinct = [], []
        for _, g in q.groupby("alternative"):
            v = np.unique(np.round(g[c].dropna().to_numpy(float), 6))
            distinct.append(v.size)
            if v.size > 1:
                steps.append(np.median(np.diff(v)))
        Fp = np.mean([floors[(c, g)] for g in ("concave", "convex")])
        allv = np.unique(np.round(q[c].dropna().to_numpy(float), 6))
        rows.append({"qc": c, "median_step": float(np.median(steps)), "step_over_floor": float(np.median(steps)) / Fp,
                     "distinct_values_total": int(allv.size), "distinct_per_series_median": float(np.median(distinct)),
                     "distinct_per_series_min": int(np.min(distinct)), "distinct_per_series_max": int(np.max(distinct)),
                     "alternatives_with_zero_q95_se": int((t.loc[t["qc"] == c, "real_q95_se"] < 1e-9).sum())})
    return pd.DataFrame(rows)


def run_metadata(q: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for a, g in q.groupby("alternative", sort=True):
        T = g["punch_temp_C"].to_numpy(float)
        rows.append({"alternative": a, "start_temp_C": float(np.nanmedian(T[:10])),
                     "rise_first_150_K": float(np.nanmedian(T[140:150]) - np.nanmedian(T[:10])),
                     "rise_series_K": float(np.nanmedian(T[-10:]) - np.nanmedian(T[:10])),
                     "sheet_median_um": float(np.nanmedian(g["sheet_um"])),
                     "stroke_speed_mm_s": float(np.nanmedian(g["v_form_mm_s"]))})
    return pd.DataFrame(rows)


def force_effect(t: pd.DataFrame) -> pd.DataFrame:
    """Blank-holder force effect (100 to 500 kN) of the nominal simulation over the measured one, for the
    draw-ins: the simulated trend that M1 adds to the produced offset."""
    rows = []
    for qc in ("drawin_mid", "drawin_corner"):
        for geo in ("concave", "convex"):
            a = t[(t["qc"] == qc) & (t["geometry"] == geo)].groupby("bhf_kN")[["real_centre", "sim_nominal"]].mean()
            real, sim = a.loc[500] - a.loc[100]
            rows.append({"qc": qc, "geometry": geo, "real_effect": real, "sim_effect": sim, "ratio": sim / real})
    return pd.DataFrame(rows)


def main() -> None:
    iv = pd.read_csv(RESULTS / "dec_intervals.csv")
    ivr = D.with_relation_scopes(iv)
    res = pd.read_csv(RESULTS / "dec_resolution.csv")
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    floors = D.load_floors()
    q = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))

    out = {"decomposition": decomposition(res)}
    out["sibling_strata"], counts = sibling_strata(iv)
    out["force_levels"] = force_levels(iv)
    out["source_floor"] = source_floor(iv, floors)
    out["physical_units"] = physical_units(iv)
    out["failing_weight"] = failing_weight(iv)
    out["step6"], out["step6_curves"] = step6(ivr)
    out["capability"] = capability(iv, t)
    out["m0_split"] = m0_split(iv, t)
    out["nominal_offset"] = nominal_offset(iv, t)
    out["variogram"], out["floor_protocol"] = floor_protocol(q, floors)
    out["resolution_steps"] = resolution_steps(q, floors, t)
    out["runs"] = run_metadata(q)
    out["force_effect"] = force_effect(t)
    for name, frame in out.items():
        frame.to_csv(RESULTS / f"panel_{name}.csv", index=False)

    lines = ["# Analyses requested in review", ""]
    for name, frame in out.items():
        if name == "step6_curves":
            continue
        show = frame
        if name in ("sibling_strata", "force_levels", "source_floor", "step6", "capability"):
            show = frame[frame["method"].isin(CORE + ["M3", "M4", "M2n", "M1n"])]
        lines += [f"## {name}", "", show.round(3).to_markdown(index=False), ""]
    lines += ["## sibling strata: cases", "", counts.to_markdown(index=False)]
    (RESULTS / "summary_panel.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:60]))


if __name__ == "__main__":
    main()
