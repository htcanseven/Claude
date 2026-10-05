"""Sensitivity of the learned rules M3 and M4 to the learner and its settings.

M3 (matched simulation + learned correction) and M4 (learned model without the
simulation) use one fixed gradient-boosting setting (decisions.GBR). Both rules
are recomputed within the design family and across families (transfer) with
  - a more regularised boosting setting (shallower trees, fewer and smaller steps, L2 penalty),
  - a more flexible boosting setting (deeper trees, more and larger steps),
  - a ridge regression on the same standardised inputs (a linear learner),
  - the boosting setting selected for each calibration set by the mean absolute
    leave-one-alternative-out error over the calibration alternatives, the same
    residuals that set the conformal margin, so nothing of the held-out
    alternative enters the choice.
Every other step (draws of incoming conditions, seeds, offset and margin) is that
of decisions.py, so the reference setting reproduces the stored M3 and M4
distances. The pooled scope is left out to bound the run time; it lies between
the two scopes in decisions.py.

Outputs: results/tune_intervals.csv, tune_decisions.csv, summary_tuning.md
"""

from __future__ import annotations

import sys
import warnings
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
from common import RESULTS  # noqa: E402
from qc import SHARED, parts_qc, sims_qc  # noqa: E402

HGB = D.HistGradientBoostingRegressor
SETTINGS = {
    "reference": dict(D.GBR),
    "regularised": dict(max_depth=2, max_iter=100, learning_rate=0.05, l2_regularization=1.0, random_state=0),
    "flexible": dict(max_depth=6, max_iter=400, learning_rate=0.1, min_samples_leaf=10, random_state=0),
    "ridge": None,
}
BOOSTING = ["reference", "regularised", "flexible"]
RIDGE_ALPHA = 1.0


def use_setting(name: str) -> None:
    """Point decisions.m3_fit at the learner of a setting and empty its caches."""
    if SETTINGS[name] is None:
        D.HistGradientBoostingRegressor = lambda **_: make_pipeline(StandardScaler(), Ridge(alpha=RIDGE_ALPHA))
    else:
        D.HistGradientBoostingRegressor = HGB
        D.GBR = SETTINGS[name]
    D.m3_fit.cache_clear()
    D.m3_nested.cache_clear()


def nested(calib: tuple[str, ...], qc: str, use_sim: bool) -> tuple[float, float, float]:
    """Offset, conformal margin and mean absolute centred residual of the leave-one-out over the
    calibration alternatives (as decisions.m3_nested, with the same seeds)."""
    real = D._CTX["t"][D._CTX["t"]["qc"] == qc].set_index("alternative")["real_q95"]
    tag = "nested" if use_sim else "nested-nosim"
    res = np.array([real[b] - D.m3_q95([c for c in calib if c != b], b, qc,
                                       np.random.default_rng(D.stable_seed(tag, b, qc, *calib)), use_sim)
                    for b in calib if b in real.index])
    off = float(np.nanmedian(res))
    return off, D.conformal_margin(np.abs(res - off), D.CONF_LEVEL), float(np.nanmean(np.abs(res - off)))


def job(args: tuple[str, str]) -> list[dict]:
    """Intervals of M3 and M4 for one characteristic under one setting, within the family and in transfer."""
    from threadpoolctl import threadpool_limits

    qc, name = args
    use_setting(name)
    t = D._CTX["t"]
    alts = sorted(t["alternative"].unique())
    geo_of = {a: a.split("/")[0] for a in alts}
    cases = [("within", [b for b in alts if b != a and geo_of[b] == geo_of[a]], [a]) for a in alts]
    cases += [("transfer", [b for b in alts if geo_of[b] == s], [b for b in alts if geo_of[b] == d])
              for s, d in (("concave", "convex"), ("convex", "concave"))]
    rows = []
    with threadpool_limits(1):
        for scope, calib, targets in cases:
            for rule, use_sim in (("M3", True), ("M4", False)):
                off, marg, mae = nested(tuple(sorted(calib)), qc, use_sim)
                for a in targets:
                    rng = np.random.default_rng(D.stable_seed("target" if use_sim else "target-nosim", a, qc,
                                                              *sorted(calib)))
                    q = D.m3_q95(calib, a, qc, rng, use_sim)
                    rows.append({"scope": scope, "rule": rule, "setting": name, "qc": qc, "alternative": a,
                                 "lo": q + off - marg, "hi": q + off + marg, "inner_mae": mae, "inner_margin": marg})
    print(f"{qc} {name}: done", flush=True)
    return rows


def with_selected(iv: pd.DataFrame) -> pd.DataFrame:
    """Add the boosting setting chosen per calibration case by the smallest inner leave-one-out error."""
    b = iv[iv["setting"].isin(BOOSTING)].copy()
    b["order"] = b["setting"].map({s: i for i, s in enumerate(BOOSTING)})
    sel = b.sort_values(["inner_mae", "order"]).drop_duplicates(["scope", "rule", "qc", "alternative"])
    sel = sel.assign(chosen=sel["setting"], setting="selected").drop(columns="order")
    return pd.concat([iv, sel], ignore_index=True)


def verdict_rows(iv: pd.DataFrame, t: pd.DataFrame, floors: dict) -> pd.DataFrame:
    tq = t.set_index(["qc", "alternative"])
    rows = []
    for r in iv.itertuples(index=False):
        s = tq.loc[(r.qc, r.alternative)]
        reqs = s["real_q95"] + D.D_GRID * floors[(r.qc, s["geometry"])]
        for d, v in zip(D.D_GRID, D.verdicts(r.lo, r.hi, reqs)):
            rows.append({"scope": r.scope, "method": f"{r.rule}|{r.setting}", "qc": r.qc,
                         "alternative": r.alternative, "d": float(d), "verdict": v, "adequate": bool(d >= 0)})
    return pd.DataFrame(rows)


def main() -> None:
    warnings.filterwarnings("ignore")
    parts = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    floors = {(c, g): float(fl.loc[c, f"floor_{g}"]) for c in SHARED for g in ("concave", "convex")}
    D._CTX.update(parts=D.match_sims(parts, sims), sims=sims, t=t, floors=floors)

    with Pool(D.N_JOBS) as pool:
        chunks = pool.map(job, [(qc, s) for s in SETTINGS for qc in SHARED], chunksize=1)
    iv = with_selected(pd.DataFrame([r for c in chunks for r in c]))
    iv.to_csv(RESULTS / "tune_intervals.csv", index=False)

    res = D.distance_table(verdict_rows(iv, t, floors))
    res[["rule", "setting"]] = res["method"].str.split("|", expand=True)
    res = res.drop(columns="method")[["scope", "rule", "setting", "qc", "resolution_floors", "safe_floors",
                                       "resolution_lo", "resolution_hi", "safe_lo", "safe_hi"]]
    res.to_csv(RESULTS / "tune_decisions.csv", index=False)

    ref = pd.read_csv(RESULTS / "dec_resolution.csv")
    ref = ref[(ref["qc"] == "all") & ref["method"].isin(["M3", "M4"]) & ref["scope"].isin(["within", "transfer"])]
    allq = res[res["qc"] == "all"]
    check = allq[allq["setting"] == "reference"].merge(ref, left_on=["scope", "rule"], right_on=["scope", "method"],
                                                         suffixes=("", "_stored"))
    same = bool((check["resolution_floors"] == check["resolution_floors_stored"]).all()
                and (check["safe_floors"] == check["safe_floors_stored"]).all())
    chosen = iv[iv["setting"] == "selected"].groupby(["scope", "rule"])["chosen"].value_counts().unstack(fill_value=0)
    tab = allq.assign(decisive=[f"{r:g} ({lo:g}-{hi:g})" for r, lo, hi in
                                zip(allq["resolution_floors"], allq["resolution_lo"], allq["resolution_hi"])],
                      safe=[f"{r:g} ({lo:g}-{hi:g})" for r, lo, hi in
                            zip(allq["safe_floors"], allq["safe_lo"], allq["safe_hi"])])
    lines = ["# Sensitivity of M3 and M4 to the learner and its settings", "",
             "Settings: " + "; ".join(f"{k}: {v if v is not None else f'ridge (alpha {RIDGE_ALPHA:g})'}"
                                      for k, v in SETTINGS.items()) + "; selected: the boosting setting with the "
             "smallest mean absolute leave-one-out error over the calibration alternatives.", "",
             f"Reference setting reproduces the stored distances: {same}.", "",
             "## Decisive and safe distances over all characteristics (floors, bootstrap 95 % interval)", "",
             tab[["scope", "rule", "setting", "decisive", "safe"]].sort_values(["scope", "rule", "setting"])
             .to_markdown(index=False), "",
             "## Settings chosen by the inner leave-one-out (design cases)", "", chosen.to_markdown(), "",
             "## Decisive distance per characteristic", "",
             res.pivot_table(index="qc", columns=["scope", "rule", "setting"], values="resolution_floors")
             .round(1).to_markdown()]
    (RESULTS / "summary_tuning.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
