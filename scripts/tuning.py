"""Sensitivity of the part-level learned rules M3 and M4 to the learner and its settings.

M3 (matched simulation + learned correction) and M4 (learned model without the simulation) use one fixed
gradient-boosting setting (decisions.GBR). Both rules are recomputed for a new variant (scope 'within'),
a new process setting ('setting') and a new family ('transfer') with
  - a more regularised boosting setting (shallower trees, fewer and smaller steps, L2 penalty),
  - a more flexible boosting setting (deeper trees, more and larger steps),
  - a ridge regression on the same standardised inputs (a linear learner),
  - quantile-loss boosting (loss = quantile 0.95), which models the 95th percentile of a part directly
    instead of resampling the pooled in-sample residuals; the alternative's q95 is the median of the
    predicted conditional quantiles over the drawn incoming conditions,
  - the boosting setting selected for each calibration set by the mean absolute leave-one-alternative-out
    error over the calibration alternatives, the residuals that also set the jackknife margin, so nothing
    of the held-out alternative enters the choice.
Every other step (draws of incoming conditions, seeds, offset and margin) is that of decisions.py, so the
reference setting reproduces the stored M3 and M4 intervals.

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
M3_Q95 = D.m3_q95
SETTINGS = {
    "reference": dict(D.GBR),
    "regularised": dict(max_depth=2, max_iter=100, learning_rate=0.05, l2_regularization=1.0, random_state=0),
    "flexible": dict(max_depth=6, max_iter=400, learning_rate=0.1, min_samples_leaf=10, random_state=0),
    "ridge": None,
    "quantile": dict(D.GBR, loss="quantile", quantile=D.ADEQUATE_RATE),
}
BOOSTING = ["reference", "regularised", "flexible"]
RIDGE_ALPHA = 1.0


def m3_q95_quantile(calib, target, qc, rng, use_sim=True) -> float:
    """q95 of a new alternative from quantile-loss boosting: the median predicted conditional 95th
    percentile over the drawn incoming conditions (no residuals are resampled)."""
    fit = D.m3_fit(frozenset(calib), qc, use_sim)
    if fit is None:
        return np.nan
    model, _, tr = fit
    geo, bhf, lub = target.split("/")
    pool = tr[tr["oil_type"] == lub]
    pool = pool if len(pool) else tr
    draw = pool.iloc[rng.integers(0, len(pool), D.M3_DRAWS)][["sheet_um", "oil_gm2"]].reset_index(drop=True)
    new = draw.assign(geometry=geo, bhf_kN=int(float(bhf)), oil_type=lub)
    base = 0.0
    if use_sim:
        idx = D.matched_index(D._CTX["sims"], geo, int(float(bhf)), new["sheet_um"].to_numpy() / 1000.0,
                              new["oil_gm2"].to_numpy())
        if (idx < 0).any():
            return np.nan
        base = D._CTX["sims"][qc].reindex(idx).to_numpy()
    return float(np.median(D.transform(qc, base + model.predict(D.design_matrix(new)))))


def use_setting(name: str) -> None:
    """Point decisions.m3_fit / m3_q95 at the learner of a setting and empty their caches."""
    D.m3_q95 = m3_q95_quantile if name == "quantile" else M3_Q95
    if SETTINGS[name] is None:
        D.HistGradientBoostingRegressor = lambda **_: make_pipeline(StandardScaler(), Ridge(alpha=RIDGE_ALPHA))
    else:
        D.HistGradientBoostingRegressor = HGB
        D.GBR = SETTINGS[name]
    D.m3_fit.cache_clear()
    D.m3_nested.cache_clear()


def nested(calib: tuple[str, ...], qc: str, use_sim: bool) -> tuple[float, float, float]:
    """Offset, jackknife margin and mean absolute centred residual of the leave-one-out over the
    calibration alternatives (as decisions.m3_nested, with the same seeds)."""
    real = D._CTX["t"][D._CTX["t"]["qc"] == qc].set_index("alternative")["real_q95"]
    tag = "nested" if use_sim else "nested-nosim"
    res = np.array([real[b] - D.m3_q95([c for c in calib if c != b], b, qc,
                                       np.random.default_rng(D.stable_seed(tag, b, qc, *calib)), use_sim)
                    for b in calib if b in real.index])
    off = float(np.nanmedian(res))
    return off, D.conformal_margin(np.abs(res - off), D.CONF_LEVEL), float(np.nanmean(np.abs(res - off)))


def cases(alts: list[str]) -> list[tuple[str, list[str], list[str]]]:
    geo_of = {a: a.split("/")[0] for a in alts}
    out = [("within", [b for b in alts if b != a and geo_of[b] == geo_of[a]], [a]) for a in alts]
    for geo, bhf in sorted({(geo_of[a], D.bhf_of(a)) for a in alts}):
        held = [b for b in alts if geo_of[b] == geo and D.bhf_of(b) == bhf]
        out.append(("setting", [b for b in alts if geo_of[b] == geo and b not in held], held))
    out += [("transfer", [b for b in alts if geo_of[b] == s], [b for b in alts if geo_of[b] == d])
            for s, d in (("concave", "convex"), ("convex", "concave"))]
    return out


def job(args: tuple[str, str]) -> list[dict]:
    """Intervals of M3 and M4 for one characteristic under one setting, in all three scopes."""
    from threadpoolctl import threadpool_limits

    qc, name = args
    use_setting(name)
    t, floors = D._CTX["t"], D._CTX["floors"]
    tq = t[t["qc"] == qc].set_index("alternative")
    rows = []
    with threadpool_limits(1):
        for scope, calib, targets in cases(sorted(t["alternative"].unique())):
            for rule, use_sim in (("M3", True), ("M4", False)):
                off, marg, mae = nested(tuple(sorted(calib)), qc, use_sim)
                for a in targets:
                    rng = np.random.default_rng(D.stable_seed("target" if use_sim else "target-nosim", a, qc,
                                                              *sorted(calib)))
                    q = D.m3_q95(calib, a, qc, rng, use_sim)
                    rows.append({"scope": scope, "relation": D.relation(calib, a), "rule": rule, "setting": name,
                                 "method": f"{rule}|{name}", "qc": qc, "alternative": a, "geometry": tq.loc[a, "geometry"],
                                 "lo": q + off - marg, "hi": q + off + marg, "real_q95": float(tq.loc[a, "real_q95"]),
                                 "floor": floors[(qc, tq.loc[a, "geometry"])], "inner_mae": mae, "inner_margin": marg})
    print(f"{qc} {name}: done", flush=True)
    return rows


def with_selected(iv: pd.DataFrame) -> pd.DataFrame:
    """Add the boosting setting chosen per calibration case by the smallest inner leave-one-out error."""
    b = iv[iv["setting"].isin(BOOSTING)].copy()
    b["order"] = b["setting"].map({s: i for i, s in enumerate(BOOSTING)})
    sel = b.sort_values(["inner_mae", "order"]).drop_duplicates(["scope", "rule", "qc", "alternative"])
    sel = sel.assign(chosen=sel["setting"], setting="selected", method=sel["rule"] + "|selected").drop(columns="order")
    return pd.concat([iv, sel], ignore_index=True)


def main() -> None:
    warnings.filterwarnings("ignore")
    parts = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    D.setup(t, sims, D.load_floors(), D.match_sims(parts, sims))

    with Pool(D.N_JOBS) as pool:
        chunks = pool.map(job, [(qc, s) for s in SETTINGS for qc in SHARED], chunksize=1)
    iv = with_selected(pd.DataFrame([r for c in chunks for r in c]))
    iv.to_csv(RESULTS / "tune_intervals.csv", index=False)

    res = D.distances(D.with_relation_scopes(iv), n_boot=0, per_qc=False)
    res[["rule", "setting"]] = res["method"].str.split("|", expand=True)
    res = res.drop(columns="method")
    res.to_csv(RESULTS / "tune_decisions.csv", index=False)

    stored = pd.read_csv(RESULTS / "dec_intervals.csv")
    stored = stored[stored["method"].isin(["M3", "M4"]) & stored["scope"].isin(["within", "setting", "transfer"])]
    mine = iv[iv["setting"] == "reference"].assign(method=lambda d: d["rule"])
    m = stored.merge(mine, on=["scope", "method", "qc", "alternative"], suffixes=("_stored", ""))
    same = bool(np.allclose(m["lo"], m["lo_stored"], equal_nan=True) and np.allclose(m["hi"], m["hi_stored"], equal_nan=True))
    chosen = iv[iv["setting"] == "selected"].groupby(["scope", "rule"])["chosen"].value_counts().unstack(fill_value=0)
    lines = ["# Sensitivity of M3 and M4 to the learner and its settings", "",
             "Settings: " + "; ".join(f"{k}: {v if v is not None else f'ridge (alpha {RIDGE_ALPHA:g})'}"
                                      for k, v in SETTINGS.items()) + "; selected: the boosting setting with the "
             "smallest mean absolute leave-one-out error over the calibration alternatives.", "",
             f"Reference setting reproduces the stored intervals: {same} ({len(m)} cases).", "",
             "## Decisive and safe distances over all characteristics (floors)", "",
             res.sort_values(["scope", "rule", "setting"])[["scope", "rule", "setting", "resolution_floors",
                                                            "safe_floors", "resolution_failing", "safe_failing"]]
             .to_markdown(index=False), "",
             "## Settings chosen by the inner leave-one-out (design cases)", "", chosen.to_markdown()]
    (RESULTS / "summary_tuning.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
