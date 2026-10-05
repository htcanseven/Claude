"""Robustness of the findings to the known weaknesses of the data and to the analysis constants.

1. Punch temperature drifts by a few kelvin within each series. Every
   characteristic is corrected for it (pooled within-alternative slope on
   the punch temperature) and the floor, the effect-to-scatter shares and
   the fast decision rules (M1, M2, M5) are recomputed.
2. Blank-holder force is confounded with stroke speed (the 100 kN series ran
   slower). The force effects are split into 100->300 kN pairs (speed
   changes) and 300->500 kN pairs (same speed).
3. Analysis constants: conformal level 0.80 and 0.95 instead of 0.90 (M2, M5)
   and resolution target 0.90 and 0.99 instead of 0.95 (all rules).
4. Oil-to-friction mapping: every part's oil film is replaced by the median
   film of its lubrication pattern, both in the simulation match and in the
   model inputs of M3, which removes the within-series friction variation
   the mapping implies (within-family calibration).
5. A conformalised Gaussian process (M6: the M5 mean with a conformal margin
   on leave-one-out standardised residuals) as a candidate for a rule that
   is both safe and decisive.

Outputs: results/rob_floor.csv, rob_bhf_pairs.csv, rob_decisions.csv, summary_robustness.md
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

CONF_LEVELS = [0.80, 0.90, 0.95]
RESOLUTION_TARGETS = [0.90, 0.95, 0.99]


# ── 1. temperature correction ────────────────────────────────────────────────
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


# ── fast rules (M1, M2, M5) at a given conformal level ────────────────────────
def fast_verdicts(t: pd.DataFrame, floors: dict, level: float) -> pd.DataFrame:
    D._CTX["t"] = t
    D.m5_fit.cache_clear()
    alts = sorted(t["alternative"].unique())
    geo_of = {a: a.split("/")[0] for a in alts}
    z = norm.ppf(0.5 + level / 2)
    rows = []
    for qc in SHARED:
        tq = t[t["qc"] == qc].set_index("alternative")
        jobs = []
        for a in alts:
            jobs.append(("within", [b for b in alts if b != a and geo_of[b] == geo_of[a]], [a]))
            jobs.append(("pooled", [b for b in alts if b != a], [a]))
        for src, dst in (("concave", "convex"), ("convex", "concave")):
            jobs.append(("transfer", [b for b in alts if geo_of[b] == src], [b for b in alts if geo_of[b] == dst]))
        for scope, calib, targets in jobs:
            c = tq.loc[calib]
            off1 = float(np.median(c["real_q95"] - c["sim_nominal"]))
            r2 = (c["real_q95"] - c["sim_env_hi"]).to_numpy()
            off2 = float(np.median(r2))
            marg2 = D.conformal_margin(np.abs(r2 - off2), level)
            gp, keep = D.m5_fit(tuple(sorted(calib)), qc)
            for a in targets:
                F = floors[(qc, geo_of[a])]
                reqs = tq.loc[a, "real_q95"] + D.D_GRID * F
                mu, sd = gp.predict(D.descriptors([a])[:, keep], return_std=True)
                env = tq.loc[a, "sim_env_hi"]
                ivs = {"M1": (tq.loc[a, "sim_nominal"] + off1,) * 2, "M2": (env + off2 - marg2, env + off2 + marg2),
                       "M5": (env + mu[0] - z * sd[0], env + mu[0] + z * sd[0])}
                for name, (lo, hi) in ivs.items():
                    for d, v in zip(D.D_GRID, D.verdicts(lo, hi, reqs)):
                        rows.append({"scope": scope, "method": name, "qc": qc, "alternative": a, "d": float(d),
                                     "verdict": v, "adequate": bool(d >= 0)})
    return pd.DataFrame(rows)


def distances(d: pd.DataFrame, target: float = D.RESOLUTION_TARGET) -> pd.DataFrame:
    """Decisive and safe distances over all characteristics, per scope and rule, for a resolution target."""
    d = d.assign(correct=D.is_correct(d), ad=d["d"].abs())
    d["not_wrong"] = d["correct"] | (d["verdict"] == "uncertain")

    def beyond(rate):
        bad = rate[rate < target]
        if bad.empty:
            return float(rate.index.min())
        above = rate.index[rate.index > bad.index.max()]
        return float(above.min()) if len(above) else np.inf

    rows = []
    for (scope, method), g in d.groupby(["scope", "method"]):
        rows.append({"scope": scope, "method": method,
                     "decisive": beyond(g.groupby("ad")["correct"].mean().sort_index()),
                     "safe": beyond(g.groupby("ad")["not_wrong"].mean().sort_index())})
    return pd.DataFrame(rows)


# ── 4. M3 with the friction of the pattern's median oil film ─────────────────
def m3_within(qc: str) -> list[dict]:
    from threadpoolctl import threadpool_limits

    t, floors = D._CTX["t"], D._CTX["floors"]
    alts = sorted(t["alternative"].unique())
    geo_of = {a: a.split("/")[0] for a in alts}
    rows = []
    with threadpool_limits(1):
        for a in alts:
            calib = [b for b in alts if b != a and geo_of[b] == geo_of[a]]
            q3, off3, marg3 = D.m3_calibrated(calib, a, qc)
            s = t[(t["alternative"] == a) & (t["qc"] == qc)].iloc[0]
            reqs = s["real_q95"] + D.D_GRID * floors[(qc, s["geometry"])]
            for d, v in zip(D.D_GRID, D.verdicts(q3 + off3 - marg3, q3 + off3 + marg3, reqs)):
                rows.append({"scope": "within", "method": "M3", "qc": qc, "alternative": a, "d": float(d),
                             "verdict": v, "adequate": bool(d >= 0)})
    return rows


# ── 5. conformalised Gaussian process ────────────────────────────────────────
def m6_verdicts(t: pd.DataFrame, floors: dict) -> pd.DataFrame:
    D._CTX["t"] = t
    alts = sorted(t["alternative"].unique())
    geo_of = {a: a.split("/")[0] for a in alts}

    def gp_pred(calib, target, qc):
        gp, keep = D.m5_fit(tuple(sorted(calib)), qc)
        mu, sd = gp.predict(D.descriptors([target])[:, keep], return_std=True)
        return float(mu[0]), float(sd[0])

    rows = []
    for qc in SHARED:
        tq = t[t["qc"] == qc].set_index("alternative")
        jobs = []
        for a in alts:
            jobs.append(("within", [b for b in alts if b != a and geo_of[b] == geo_of[a]], [a]))
            jobs.append(("pooled", [b for b in alts if b != a], [a]))
        for src, dst in (("concave", "convex"), ("convex", "concave")):
            jobs.append(("transfer", [b for b in alts if geo_of[b] == src], [b for b in alts if geo_of[b] == dst]))
        for scope, calib, targets in jobs:
            z = []
            for b in calib:
                mu_b, sd_b = gp_pred([x for x in calib if x != b], b, qc)
                z.append(abs(tq.loc[b, "real_q95"] - tq.loc[b, "sim_env_hi"] - mu_b) / max(sd_b, 1e-12))
            qz = D.conformal_margin(np.array(z), D.CONF_LEVEL)
            for a in targets:
                mu, sd = gp_pred(calib, a, qc)
                env = tq.loc[a, "sim_env_hi"]
                reqs = tq.loc[a, "real_q95"] + D.D_GRID * floors[(qc, geo_of[a])]
                for d, v in zip(D.D_GRID, D.verdicts(env + mu - qz * sd, env + mu + qz * sd, reqs)):
                    rows.append({"scope": scope, "method": "M6", "qc": qc, "alternative": a, "d": float(d),
                                 "verdict": v, "adequate": bool(d >= 0)})
    return pd.DataFrame(rows)


def main() -> None:
    warnings.filterwarnings("ignore")
    f = pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False)
    q = parts_qc(f)
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    floors = {(c, g): float(fl.loc[c, f"floor_{g}"]) for c in SHARED for g in ("concave", "convex")}
    t_ref = pd.read_csv(RESULTS / "dec_alternatives.csv")

    # 1. temperature correction: floors, shares, fast rules
    qa = temperature_adjusted(q)
    fl_rows = floors_and_shares(q, "reference") + floors_and_shares(qa, "temperature-adjusted")
    rob_floor = pd.DataFrame(fl_rows)
    rob_floor.to_csv(RESULTS / "rob_floor.csv", index=False)
    fl_adj = rob_floor[rob_floor["variant"] == "temperature-adjusted"].set_index("qc")
    floors_adj = {(c, g): float(fl_adj.loc[c, f"floor_{g}"]) for c in SHARED for g in ("concave", "convex")}
    t_adj = D.alternative_table(D.match_sims(qa, sims), sims)
    dec = [distances(fast_verdicts(t_ref, floors, D.CONF_LEVEL)).assign(variant="reference"),
           distances(fast_verdicts(t_adj, floors_adj, D.CONF_LEVEL)).assign(variant="temperature-adjusted")]

    # 3. conformal level and resolution target
    for level in CONF_LEVELS:
        if level != D.CONF_LEVEL:
            v = fast_verdicts(t_ref, floors, level)
            dec.append(distances(v[v["method"] != "M1"]).assign(variant=f"conformal level {level:.2f}"))
    ref_verdicts = pd.read_csv(RESULTS / "dec_verdicts.csv.gz")
    ref_verdicts["scope"] = np.where(ref_verdicts["calibration"].str.contains("->"), "transfer",
                                     ref_verdicts["calibration"])
    for target in RESOLUTION_TARGETS:
        if target != D.RESOLUTION_TARGET:
            dec.append(distances(ref_verdicts, target).assign(variant=f"resolution target {target:.2f}"))

    # 2. blank-holder force pairs: speed change (100->300) against same speed (300->500)
    eff = pd.read_csv(RESULTS / "alt_effects.csv")
    eff = eff[eff["family"] == "bhf"].copy()
    eff["pair"] = [f"{min(int(a.split('/')[1]), int(b.split('/')[1]))}->{max(int(a.split('/')[1]), int(b.split('/')[1]))}"
                   for a, b in zip(eff["a"], eff["b"])]
    cent = q.groupby(["alternative"])[list(QCS)].agg(lambda s: centre(s.to_numpy()))
    pairs = []
    for (qc, pair), g in eff.groupby(["qc", "pair"]):
        lo, hi = map(int, pair.split("->"))
        slope = np.mean([(cent.loc[b, qc] - cent.loc[a, qc]) / (int(b.split("/")[1]) - int(a.split("/")[1]))
                         for a, b in zip(g["a"], g["b"])])
        pairs.append({"qc": qc, "pair": pair, "share_resolvable": float((g["esr"] >= 1).mean()),
                      "median_esr": float(g["esr"].median()),
                      "slope_per_100kN": float(slope * 100), "mrc_kN": float(fl.loc[qc, "floor"] / abs(slope))})
    pairs = pd.DataFrame(pairs)
    pairs.to_csv(RESULTS / "rob_bhf_pairs.csv", index=False)

    # 4. M3 with the pattern's median oil film for the simulation match (within the family)
    parts = q.copy()
    oil_med = parts.groupby("oil_type")["oil_gm2"].transform("median")
    matched = D.match_sims(parts.assign(oil_gm2=oil_med), sims)
    D._CTX.update(parts=matched, sims=sims, t=t_ref, floors=floors)
    D.m3_fit.cache_clear()
    D.m3_nested.cache_clear()
    with Pool(min(D.N_JOBS, len(SHARED))) as pool:
        m3 = pd.DataFrame([r for chunk in pool.map(m3_within, SHARED) for r in chunk])
    dec.append(distances(m3).assign(variant="M3, friction of the pattern's median oil film"))

    # 5. conformalised Gaussian process
    D.m5_fit.cache_clear()
    dec.append(distances(m6_verdicts(t_ref, floors)).assign(variant="M6 conformalised GP"))

    rob = pd.concat(dec, ignore_index=True)[["variant", "scope", "method", "decisive", "safe"]]
    rob.to_csv(RESULTS / "rob_decisions.csv", index=False)
    lines = ["# Robustness", "",
             "## Floors and effect-to-scatter shares, reference against temperature-adjusted", "",
             rob_floor.round(4).to_markdown(index=False), "",
             "## Blank-holder force pairs: 100->300 kN (stroke speed changes) against 300->500 kN (same speed)", "",
             pairs.round(3).to_markdown(index=False), "",
             "## Decision distances (floors) under the variants", "",
             rob.pivot_table(index=["variant", "method"], columns="scope", values=["decisive", "safe"]).to_markdown()]
    (RESULTS / "summary_robustness.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
