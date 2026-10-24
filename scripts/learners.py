"""Learners specified for six to nine produced alternatives, and intervals matched to the evidence relation.

decisions.py fits its Gaussian processes (M5, M5n) by maximum marginal likelihood with hard bounds; in this
design their force length scale and noise variance sit at a bound in most fits and their centres reduce to the
calibration mean or the nearest produced setting (learn_gp_diagnostics.csv). This script adds rules specified
for the small-data regime and scores them exactly like the others:

M7n  trend GP without the simulation (universal kriging): q95 = h(x)'beta + f(x) + e with a linear mean in force
     and lubrication rank (and the geometry indicator when both families calibrate), f a squared-exponential GP
     over the same descriptors and e ~ N(0, s_i^2 + sn^2), s_i the block-bootstrap error of each q95 and sn a
     between-run nugget. beta has a flat prior and is integrated out, so its uncertainty enters the predictive
     variance; the hyperparameters are maximum a posteriori under weakly informative log-normal priors in place
     of hard bounds (length scales centred on the design spacing, 200 kN and one pattern step; GP and nugget
     standard deviations centred on two and one pooled floor). The nugget is estimated, not bounded below by
     the variance between the lubrication series, which contains the lubrication effect that the mean and the
     GP represent.
M7   the autoregressive multi-fidelity model of Kennedy and O'Hagan (2000) with the simulation as the low-
     fidelity output: q95 = rho s0(x) + beta' h(x) + f(x) + e, rho and beta by generalised least squares (the
     same universal kriging with s0 in the mean), f the GP discrepancy. M1s is its special case without f.
Mcd  friction calibration with a discrepancy term (Kennedy and O'Hagan 2001): q95 = eta(x, theta) + delta(x) + e,
     eta the simulation at nominal thickness and friction theta (the 11 DDACS grid values, uniform prior), delta
     a GP with a constant mean. The posterior of theta comes from the two draw-ins, as for Mc; the prediction is
     the posterior mixture over theta, and its 90 % central interval the verdict interval.
P+RM a point predictor P (NN, M1sn, M1s, the centres of M5n, M5 and M4, the means of M7n and M7) with a relation-
     matched split-conformal interval: the 90 % conformal quantile of P's absolute errors (floors) over the cases
     of the same evidence relation in the other family (sibling 63 cases, interpolation 21, extrapolation 42, new
     family 63), borrowed because a family's own calibration set holds no case of its new-setting relation. Under
     exchangeability of the two families' errors it covers at least 90 %.

Few-shot transfer to a new family (fewshot): k = 1-3 alternatives of the target family are produced (every
subset), and its remaining 9 - k alternatives are judged, scored in the target family's floor, with
  NN-target   the nearest produced setting among the k (no use of the other family);
  shift       the other family's q95 at the same setting plus the median offset of the k from it;
  ICM         a two-task GP (intrinsic coregionalisation, free inter-family correlation) with family intercepts
              and shared slopes on both families' records, priors as M7n;
  ICM+sim     the same with the nominal simulation in the mean.

Outputs: results/learn_intervals.csv, learn_resolution.csv, learn_source_floor.csv, learn_paired.csv,
learn_gp_diagnostics.csv, learn_mcd_posterior.csv, learn_fewshot_intervals.csv.gz, learn_fewshot.csv,
summary_learners.md

Usage: python learners.py            fit, score, few-shot transfer and summary (about 40 minutes on four cores)
       python learners.py --score    score the stored intervals again, without refitting
"""

from __future__ import annotations

import itertools
import sys
import warnings
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import brentq, minimize
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
from common import RESULTS  # noqa: E402
from qc import SHARED, sims_qc  # noqa: E402

Z90 = norm.ppf(0.5 + D.CONF_LEVEL / 2)
PRIOR_LS = {"geometry": 1.0, "bhf": 2.0, "lubrication": 1.0}   # medians; force in 100 kN, lubrication in rank steps
PRIOR_LS_SD = 1.0                                               # log-scale standard deviation of the length scales
PRIOR_SF, PRIOR_SF_SD = 2.0, 1.5                                # GP standard deviation, pooled floors
PRIOR_SN, PRIOR_SN_SD = 1.0, 1.0                                # between-run nugget, pooled floors
PRIOR_RHO_SD = 1.0                                              # atanh of the inter-family correlation (ICM)
STARTS = [(1.0, 1.0, 1.0), (0.5, 1.0, 1.0), (2.0, 1.0, 1.0), (1.0, 0.5, 0.3), (1.0, 2.0, 3.0), (0.5, 2.0, 0.3)]
POINT_SOURCES = {"NN": "NN", "M1sn": "M1sn", "M1s": "M1s", "M5n": "M5n", "M5": "M5", "M4": "M4", "M7n": "M7n",
                 "M7": "M7"}                                    # predictor -> rule whose (centre of the) interval it is
NEW_RULES = ["M7n", "M7", "Mcd"]
PAIRS = [("M7n", "NN"), ("M7n", "M5n"), ("M7n", "M1sn"), ("M7", "M7n"), ("M7", "M1s"), ("M7", "M5"), ("Mcd", "Mc"),
         ("Mcd", "M1"), ("Mcd", "M7"), ("NN+RM", "M5"), ("NN+RM", "M5n"), ("NN+RM", "M2"), ("NN+RM", "M7n"),
         ("M1sn+RM", "NN+RM"), ("M5n+RM", "NN+RM"), ("M7n+RM", "NN+RM"), ("M4+RM", "NN+RM"), ("M1s+RM", "M1sn+RM")]
FEWSHOT_K = [1, 2, 3]
N_JOBS = D.N_JOBS


# ── universal kriging with MAP hyperparameters ────────────────────────────────
def _se(X1: np.ndarray, X2: np.ndarray, ls: np.ndarray) -> np.ndarray:
    d = (X1[:, None, :] - X2[None, :, :]) / ls
    return np.exp(-0.5 * np.sum(d * d, axis=-1))


def _task_corr(T1: np.ndarray | None, T2: np.ndarray | None, rho: float) -> np.ndarray | float:
    if T1 is None:
        return 1.0
    return np.where(T1[:, None] == T2[None, :], 1.0, rho)


def _unpack(theta: np.ndarray, d: int, tasks: bool):
    ls = np.exp(theta[:d])
    sf2, sn2 = np.exp(2 * theta[d]), np.exp(2 * theta[d + 1])
    rho = float(np.tanh(theta[d + 2])) if tasks else 1.0
    return ls, sf2, sn2, rho


def _log_prior(theta: np.ndarray, med: np.ndarray, sd: np.ndarray) -> float:
    return float(-0.5 * np.sum(((theta - np.log(med)) / sd) ** 2)) if med.size else 0.0


def _neg_log_post(theta, X, H, y, s2, T, pri_med, pri_sd, tasks) -> float:
    d = X.shape[1]
    ls, sf2, sn2, rho = _unpack(theta, d, tasks)
    K = sf2 * _se(X, X, ls) * _task_corr(T, T, rho) + np.diag(s2 + sn2) + 1e-9 * np.eye(len(y))
    try:
        cf = cho_factor(K, lower=True)
    except np.linalg.LinAlgError:
        return 1e10
    Ki_y, Ki_H = cho_solve(cf, y), cho_solve(cf, H)
    A = H.T @ Ki_H
    sign, logdet_A = np.linalg.slogdet(A)
    if sign <= 0:
        return 1e10
    beta = np.linalg.solve(A, H.T @ Ki_y)
    r = y - H @ beta
    ll = -0.5 * r @ cho_solve(cf, r) - np.sum(np.log(np.diag(cf[0]))) - 0.5 * logdet_A
    lp = _log_prior(theta[:d + 2], pri_med, pri_sd)
    if tasks:
        lp += -0.5 * (theta[d + 2] / PRIOR_RHO_SD) ** 2
    return float(-(ll + lp))


def fit_gp(X: np.ndarray, H: np.ndarray, y: np.ndarray, s2: np.ndarray, ls_med: np.ndarray,
           T: np.ndarray | None = None) -> dict | None:
    """MAP fit of the trend GP; None when the mean is not identified (n <= number of mean terms)."""
    n, m = H.shape
    if n <= m or np.linalg.matrix_rank(H) < m:
        return None
    d = X.shape[1]
    tasks = T is not None
    pri_med = np.r_[ls_med, PRIOR_SF, PRIOR_SN]
    pri_sd = np.r_[np.full(d, PRIOR_LS_SD), PRIOR_SF_SD, PRIOR_SN_SD]
    bounds = [(np.log(0.05), np.log(100.0))] * d + [(np.log(1e-2), np.log(1e3)), (np.log(1e-3), np.log(1e2))]
    if tasks:
        bounds.append((-3.0, 3.0))
    best = None
    for fl, ff, fn in STARTS:
        th0 = np.r_[np.log(ls_med * fl), np.log(PRIOR_SF * ff), np.log(PRIOR_SN * fn)]
        if tasks:
            th0 = np.r_[th0, 0.5]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            r = minimize(_neg_log_post, th0, args=(X, H, y, s2, T, pri_med, pri_sd, tasks), method="L-BFGS-B",
                         bounds=bounds)
        if best is None or r.fun < best.fun:
            best = r
    ls, sf2, sn2, rho = _unpack(best.x, d, tasks)
    K = sf2 * _se(X, X, ls) * _task_corr(T, T, rho) + np.diag(s2 + sn2) + 1e-9 * np.eye(n)
    cf = cho_factor(K, lower=True)
    Ki_H = cho_solve(cf, H)
    A = H.T @ Ki_H
    beta = np.linalg.solve(A, H.T @ cho_solve(cf, y))
    return {"X": X, "H": H, "T": T, "ls": ls, "sf2": sf2, "sn2": sn2, "rho": rho, "cf": cf, "A": A, "beta": beta,
            "alpha": cho_solve(cf, y - H @ beta), "s2_mean": float(np.mean(s2)), "neg_log_post": float(best.fun)}


def predict_gp(fit: dict, Xs: np.ndarray, Hs: np.ndarray, Ts: np.ndarray | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Predictive mean and variance of a new run's q95: latent variance with the uncertainty of beta, plus the
    nugget and the mean sampling variance of the calibration alternatives' q95."""
    ks = fit["sf2"] * _se(fit["X"], Xs, fit["ls"]) * _task_corr(fit["T"], Ts, fit["rho"])
    mean = Hs @ fit["beta"] + ks.T @ fit["alpha"]
    Ki_ks = cho_solve(fit["cf"], ks)
    R = Hs.T - fit["H"].T @ Ki_ks
    var = fit["sf2"] - np.sum(ks * Ki_ks, axis=0) + np.sum(R * np.linalg.solve(fit["A"], R), axis=0)
    return mean, np.maximum(var, 0.0) + fit["sn2"] + fit["s2_mean"]


# ── design of the fits ────────────────────────────────────────────────────────
def pooled_floor() -> dict:
    return pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")["floor"].to_dict()


def features(alts: list[str], keep: np.ndarray | None = None) -> tuple[np.ndarray, list[str]]:
    X = D.descriptors(alts)                       # geometry indicator, force / 100 kN, lubrication rank
    names = np.array(["geometry", "bhf", "lubrication"])
    keep = X.std(axis=0) > 0 if keep is None else keep
    return X[:, keep], list(names[keep])


def m7_design(calib: list[str], qc: str, use_sim: bool):
    """Inputs, mean basis, targets (pooled floors) and sampling variances of an M7 / M7n fit."""
    t, Fp = _CTX["tq"], _CTX["Fp"][qc]
    X0 = D.descriptors(calib)
    keep = X0.std(axis=0) > 0
    X, names = X0[:, keep], list(np.array(["geometry", "bhf", "lubrication"])[keep])
    y = np.array([t[(b, qc)]["real_q95"] for b in calib]) / Fp
    s2 = (np.array([t[(b, qc)]["real_q95_se"] for b in calib]) / Fp) ** 2
    cols = [np.ones(len(calib))]
    if use_sim:
        cols.append(np.array([t[(b, qc)]["sim_nominal"] for b in calib]) / Fp)
    for j, nm in enumerate(names):
        if nm != "bhf" or not use_sim:          # with the simulation, the force trend is the simulation's (rho s0)
            cols.append(X[:, j])
    H = np.column_stack(cols)
    return X, H, y, s2, keep, names


def m7_basis(target: str, qc: str, keep: np.ndarray, names: list[str], use_sim: bool) -> tuple[np.ndarray, np.ndarray]:
    t, Fp = _CTX["tq"], _CTX["Fp"][qc]
    xs = D.descriptors([target])[:, keep]
    cols = [1.0]
    if use_sim:
        cols.append(t[(target, qc)]["sim_nominal"] / Fp)
    for j, nm in enumerate(names):
        if nm != "bhf" or not use_sim:
            cols.append(xs[0, j])
    return xs, np.array(cols)[None, :]


_FITS: dict = {}


def m7_fit(calib: tuple[str, ...], qc: str, use_sim: bool):
    key = ("m7", calib, qc, use_sim)
    if key not in _FITS:
        X, H, y, s2, keep, names = m7_design(list(calib), qc, use_sim)
        ls_med = np.array([PRIOR_LS[n] for n in names])
        _FITS[key] = (fit_gp(X, H, y, s2, ls_med), keep, names)
    return _FITS[key]


def m7_interval(calib: list[str], target: str, qc: str, use_sim: bool) -> tuple[float, float, dict]:
    fit, keep, names = m7_fit(tuple(sorted(calib)), qc, use_sim)
    if fit is None:
        return np.nan, np.nan, {}
    xs, hs = m7_basis(target, qc, keep, names, use_sim)
    mu, var = predict_gp(fit, xs, hs)
    Fp = _CTX["Fp"][qc]
    sd = float(np.sqrt(var[0]))
    info = {f"gp_ls_{n}": float(v) for n, v in zip(names, fit["ls"])}
    info.update({"gp_sf_floors": float(np.sqrt(fit["sf2"])), "gp_sn_floors": float(np.sqrt(fit["sn2"])),
                 "gp_se_floors": float(np.sqrt(fit["s2_mean"])), "gp_beta_sim": float(fit["beta"][1]) if use_sim else np.nan})
    return (mu[0] - Z90 * sd) * Fp, (mu[0] + Z90 * sd) * Fp, info


# ── Mcd: calibration of the friction coefficient with a discrepancy term ─────
def eta(alt: str, qc: str, mu: float) -> float:
    geo, bhf = alt.split("/")[0], D.bhf_of(alt)
    return D.sim_at(geo, bhf, mu, qc)


def disc_fit(calib: tuple[str, ...], qc: str, mu: float):
    key = ("disc", calib, qc, round(mu, 3))
    if key not in _FITS:
        t, Fp = _CTX["tq"], _CTX["Fp"][qc]
        X0 = D.descriptors(list(calib))
        keep = X0.std(axis=0) > 0
        X, names = X0[:, keep], list(np.array(["geometry", "bhf", "lubrication"])[keep])
        y = np.array([t[(b, qc)]["real_q95"] - eta(b, qc, mu) for b in calib]) / Fp
        s2 = (np.array([t[(b, qc)]["real_q95_se"] for b in calib]) / Fp) ** 2
        H = np.ones((len(calib), 1))
        _FITS[key] = (fit_gp(X, H, y, s2, np.array([PRIOR_LS[n] for n in names])), keep)
    return _FITS[key]


def mcd_posterior(calib: tuple[str, ...]) -> pd.Series:
    """Posterior of the friction coefficient on the DDACS grid from the draw-ins (MAP-profiled discrepancy)."""
    key = ("post", calib)
    if key not in _FITS:
        mus = _CTX["mu_grid"]
        lp = np.array([-sum(disc_fit(calib, c, float(m))[0]["neg_log_post"] for c in D.CAL_QCS) for m in mus])
        w = np.exp(lp - lp.max())
        _FITS[key] = pd.Series(w / w.sum(), index=np.round(mus, 3))
    return _FITS[key]


def mixture_quantile(w: np.ndarray, m: np.ndarray, s: np.ndarray, p: float) -> float:
    f = lambda x: float(np.sum(w * norm.cdf((x - m) / s)) - p)  # noqa: E731
    lo, hi = float(np.min(m - 12 * s)), float(np.max(m + 12 * s))
    return brentq(f, lo, hi)


def mcd_interval(calib: list[str], target: str, qc: str) -> tuple[float, float, dict]:
    key = tuple(sorted(calib))
    post = mcd_posterior(key)
    post = post[post > 1e-3]
    post = post / post.sum()
    Fp = _CTX["Fp"][qc]
    ms, ss = [], []
    for mu, wgt in post.items():
        fit, keep = disc_fit(key, qc, float(mu))
        xs = D.descriptors([target])[:, keep]
        dm, dv = predict_gp(fit, xs, np.ones((1, 1)))
        ms.append(eta(target, qc, float(mu)) / Fp + dm[0])
        ss.append(np.sqrt(dv[0]))
    w, m, s = post.to_numpy(), np.array(ms), np.array(ss)
    lo, hi = mixture_quantile(w, m, s, 0.5 - D.CONF_LEVEL / 2), mixture_quantile(w, m, s, 0.5 + D.CONF_LEVEL / 2)
    mean_mu = float(np.sum(post.index.to_numpy() * post.to_numpy()))
    return lo * Fp, hi * Fp, {"mcd_mu_mean": mean_mu, "mcd_mu_map": float(post.idxmax()),
                              "mcd_mu_edge_mass": float(post.get(0.15, 0.0) + post.get(0.05, 0.0))}


# ── jobs ──────────────────────────────────────────────────────────────────────
_CTX: dict = {}


def jobs(alts: list[str]) -> list[tuple[list[str], list[str], str]]:
    geo_of = {a: a.split("/")[0] for a in alts}
    out = []
    for a in alts:
        out.append(([b for b in alts if b != a and geo_of[b] == geo_of[a]], [a], "within"))
        out.append(([b for b in alts if b != a], [a], "pooled"))
    for geo, bhf in sorted({(geo_of[a], D.bhf_of(a)) for a in alts}):
        held = [b for b in alts if geo_of[b] == geo and D.bhf_of(b) == bhf]
        out.append(([b for b in alts if geo_of[b] == geo and b not in held], held, f"setting:{geo}/{bhf}"))
        out.append(([b for b in alts if b not in held], held, f"pooled-setting:{geo}/{bhf}"))
    for src, dst in (("concave", "convex"), ("convex", "concave")):
        out.append(([b for b in alts if b.startswith(src)], [b for b in alts if b.startswith(dst)], f"{src}->{dst}"))
    return out


def qc_rows(qc: str) -> list[dict]:
    from threadpoolctl import threadpool_limits

    t, floors = _CTX["t"], _CTX["floors"]
    alts = sorted(t["alternative"].unique())
    rows = []
    with threadpool_limits(1):
        for calib, targets, label in jobs(alts):
            for target in targets:
                a = _CTX["tq"][(target, qc)]
                base = {"calibration": label, "relation": D.relation(calib, target), "alternative": target,
                        "geometry": a["geometry"], "bhf_kN": int(a["bhf_kN"]), "qc": qc,
                        "real_q95": float(a["real_q95"]), "floor": floors[(qc, a["geometry"])],
                        "sim_env_hi": float(a["sim_env_hi"])}
                for name, fn in (("M7n", lambda: m7_interval(calib, target, qc, False)),
                                 ("M7", lambda: m7_interval(calib, target, qc, True)),
                                 ("Mcd", lambda: mcd_interval(calib, target, qc))):
                    lo, hi, info = fn()
                    rows.append({**base, "method": name, "lo": float(lo), "hi": float(hi), **info})
    print(f"{qc}: done", flush=True)
    return rows


# ── relation-matched intervals for point predictors ──────────────────────────
def scored_floor(iv: pd.DataFrame, floors: dict) -> np.ndarray:
    """Floor in which a case is scored: its own family's, or the produced family's for a new family."""
    other = {"concave": "convex", "convex": "concave"}
    return np.array([floors[(q, other[g])] if s == "transfer" else floors[(q, g)]
                     for q, g, s in zip(iv["qc"], iv["geometry"], iv["scope"])])


def relation_matched(iv_all: pd.DataFrame, floors: dict) -> pd.DataFrame:
    """P+RM intervals: centre of P, half-width the 90 % split-conformal quantile of P's absolute errors (floors in
    which the cases are scored) over the cases of the same relation in the other family."""
    base = iv_all[iv_all["scope"].isin(["within", "setting", "transfer"]) & iv_all["method"].isin(POINT_SOURCES)].copy()
    base["centre"] = (base["lo"] + base["hi"]) / 2
    base["sfloor"] = scored_floor(base, floors)
    base["abs_err"] = np.abs(base["centre"] - base["real_q95"]) / base["sfloor"]
    rows = []
    for (m, rel), g in base.groupby(["method", "relation"]):
        for geo in ("concave", "convex"):
            own, other = g[g["geometry"] == geo], g[g["geometry"] != geo]
            q = D.conformal_margin(other["abs_err"].to_numpy(), D.CONF_LEVEL)
            half = q * own["floor"].to_numpy() if rel != "new family" else q * own["sfloor"].to_numpy()
            out = own.drop(columns=["centre", "sfloor", "abs_err"]).copy()
            out["lo"], out["hi"] = own["centre"].to_numpy() - half, own["centre"].to_numpy() + half
            out["method"] = f"{m}+RM"
            out["rm_quantile_floors"], out["rm_n"] = q, len(other)
            rows.append(out)
    return pd.concat(rows, ignore_index=True)


# ── diagnostics of the Gaussian-process fits (R3a) ────────────────────────────
def gp_diagnostics(iv_all: pd.DataFrame, t: pd.DataFrame) -> pd.DataFrame:
    """By relation: fitted hyperparameters, noise relative to its bound or nugget relative to the sampling error,
    and the distance of each GP centre from the calibration mean, NN and M1sn (floors of the case)."""
    alts = sorted(t["alternative"].unique())
    tq = t.set_index(["alternative", "qc"])["real_q95"]
    key = ["calibration", "alternative", "qc"]
    ref = iv_all[iv_all["method"].isin(["NN", "M1sn"])].pivot_table(index=key, columns="method", values="lo")
    rows = []
    sub = iv_all[iv_all["scope"].isin(["within", "setting", "transfer", "pooled", "pooled-setting"])
                 & iv_all["method"].isin(["M5", "M5n", "M7", "M7n"])]
    for r in sub.to_dict("records"):
        calib = D.calibration_of(r["calibration"], r["alternative"], alts)
        cmean = float(np.mean([tq[(b, r["qc"])] for b in calib]))
        c = (r["lo"] + r["hi"]) / 2
        nn, ms = ref.loc[(r["calibration"], r["alternative"], r["qc"])][["NN", "M1sn"]]
        F = r["floor"]
        row = {"scope": r["scope"], "relation": r["relation"], "method": r["method"], "qc": r["qc"],
               "calibration": r["calibration"], "alternative": r["alternative"],
               "ls_bhf": r.get("gp_ls_bhf", np.nan), "ls_lubrication": r.get("gp_ls_lubrication", np.nan),
               "d_calib_mean": abs(c - cmean) / F, "d_nn": abs(c - nn) / F, "d_m1sn": abs(c - ms) / F,
               "half_width": (r["hi"] - r["lo"]) / 2 / F}
        if r["method"] in ("M5", "M5n"):
            row.update({"ls_at_lower": bool(np.isclose(r["gp_ls_bhf"], D.LS_BOUNDS[0])) if np.isfinite(r["gp_ls_bhf"]) else np.nan,
                        "noise_over_bound": r["gp_noise"] / r["gp_noise_lb"]})
        else:
            row.update({"nugget_floors": r.get("gp_sn_floors", np.nan), "se_floors": r.get("gp_se_floors", np.nan),
                        "gp_sd_floors": r.get("gp_sf_floors", np.nan)})
        rows.append(row)
    d = pd.DataFrame(rows)
    d["relation_scope"] = np.where(d["scope"].str.startswith("pooled"), "pooled " + d["relation"], d["relation"])
    loo = d["calibration"].isin(["within", "pooled"])          # one calibration set per held-out alternative
    d["fit"] = d["calibration"] + np.where(loo, "|" + d["alternative"], "")
    one_fit = d.drop_duplicates(["fit", "qc", "method"])
    agg = d.groupby(["relation_scope", "method"]).agg(
        cases=("qc", "size"), median_ls_bhf=("ls_bhf", "median"), median_ls_lub=("ls_lubrication", "median"),
        median_d_calib_mean=("d_calib_mean", "median"), share_within_001_of_calib_mean=("d_calib_mean", lambda s: float((s <= 0.01).mean())),
        median_d_nn=("d_nn", "median"), p90_d_nn=("d_nn", lambda s: float(np.quantile(s, 0.9))),
        median_d_m1sn=("d_m1sn", "median"), median_half_width=("half_width", "median")).reset_index()
    fits = one_fit.groupby(["relation_scope", "method"]).agg(
        fits=("qc", "size"),
        ls_at_lower_share=("ls_at_lower", lambda s: float(pd.to_numeric(s, errors="coerce").mean())),
        median_noise_over_bound=("noise_over_bound", "median"),
        median_nugget_floors=("nugget_floors", "median"), median_se_floors=("se_floors", "median"),
        median_gp_sd_floors=("gp_sd_floors", "median")).reset_index()
    return agg.merge(fits, on=["relation_scope", "method"], how="left")


# ── few-shot transfer to a new family ─────────────────────────────────────────
def fewshot(t: pd.DataFrame, floors: dict) -> pd.DataFrame:
    Fp = pooled_floor()
    rows = []
    alts = sorted(t["alternative"].unique())
    tq = {(a, q): r for a, q, r in zip(t["alternative"], t["qc"], t.to_dict("records"))}
    for tgt_geo, src_geo in (("concave", "convex"), ("convex", "concave")):
        tgt = [a for a in alts if a.startswith(tgt_geo)]
        src = [a for a in alts if a.startswith(src_geo)]
        for k in FEWSHOT_K:
            for prod in itertools.combinations(tgt, k):
                rest = [a for a in tgt if a not in prod]
                for qc in SHARED:
                    F = floors[(qc, tgt_geo)]
                    y_src = {b: tq[(b, qc)]["real_q95"] for b in src}
                    y_prod = {b: tq[(b, qc)]["real_q95"] for b in prod}
                    setting = lambda a: "/".join(a.split("/")[1:])  # noqa: E731
                    off = float(np.median([y_prod[b] - y_src[f"{src_geo}/{setting(b)}"] for b in prod]))
                    preds = {a: {} for a in rest}
                    for a in rest:
                        dist = np.array([abs(D.bhf_of(b) - D.bhf_of(a)) for b in prod])
                        near = [b for b, x in zip(prod, dist) if x == dist.min()]
                        v = float(np.mean([y_prod[b] for b in near]))
                        preds[a]["NN-target"] = (v, v)
                        v = y_src[f"{src_geo}/{setting(a)}"] + off
                        preds[a]["shift"] = (v, v)
                    for name, use_sim in (("ICM", False), ("ICM+sim", True)):
                        calib = list(src) + list(prod)
                        X = D.descriptors(calib)[:, 1:]                 # force, lubrication rank
                        T = np.array([0.0] * len(src) + [1.0] * len(prod))
                        y = np.array([tq[(b, qc)]["real_q95"] for b in calib]) / Fp[qc]
                        s2 = (np.array([tq[(b, qc)]["real_q95_se"] for b in calib]) / Fp[qc]) ** 2
                        cols = [np.ones(len(calib)), T]
                        cols += [np.array([tq[(b, qc)]["sim_nominal"] for b in calib]) / Fp[qc]] if use_sim else [X[:, 0]]
                        cols.append(X[:, 1])
                        H = np.column_stack(cols)
                        fit = fit_gp(X, H, y, s2, np.array([PRIOR_LS["bhf"], PRIOR_LS["lubrication"]]), T=T)
                        for a in rest:
                            xs = D.descriptors([a])[:, 1:]
                            hs = [1.0, 1.0] + ([tq[(a, qc)]["sim_nominal"] / Fp[qc]] if use_sim else [xs[0, 0]]) + [xs[0, 1]]
                            if fit is None:
                                preds[a][name] = (np.nan, np.nan)
                                continue
                            mu, var = predict_gp(fit, xs, np.array(hs)[None, :], np.array([1.0]))
                            sd = float(np.sqrt(var[0]))
                            preds[a][name] = ((mu[0] - Z90 * sd) * Fp[qc], (mu[0] + Z90 * sd) * Fp[qc])
                    for a in rest:
                        rel = D.relation(list(prod), a)
                        for name, (lo, hi) in preds[a].items():
                            rows.append({"target_family": tgt_geo, "k": k, "produced": "|".join(prod),
                                         "alternative": a, "relation": rel, "qc": qc, "method": name, "lo": lo,
                                         "hi": hi, "real_q95": tq[(a, qc)]["real_q95"], "floor": F})
        print(f"few-shot {tgt_geo}: done", flush=True)
    return pd.DataFrame(rows)


def fewshot_scores(fs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for keys, g in fs.groupby(["k", "method"]):
        rows.append({"k": keys[0], "relation": "all", "method": keys[1], "cases": len(g),
                     **D.distance_pair(*D.exclusion(g), sides=True), "coverage": float(np.mean((g["lo"] <= g["real_q95"]) & (g["real_q95"] <= g["hi"])))})
    for keys, g in fs.groupby(["k", "relation", "method"]):
        rows.append({"k": keys[0], "relation": keys[1], "method": keys[2], "cases": len(g),
                     **D.distance_pair(*D.exclusion(g), sides=True), "coverage": float(np.mean((g["lo"] <= g["real_q95"]) & (g["real_q95"] <= g["hi"])))})
    return pd.DataFrame(rows)


# ── sensitivity of M7n to its priors (C3) ────────────────────────────────────
BASE_PRIORS = {"ls_bhf": PRIOR_LS["bhf"], "ls_lub": PRIOR_LS["lubrication"], "sf": PRIOR_SF, "sn": PRIOR_SN}
SENS_VARIANTS = [("reference", {})] + [(f"{label} x{f:g}", {key: f}) for key, label in
                                       (("ls_bhf", "force length scale"), ("ls_lub", "lubrication length scale"),
                                        ("sf", "GP standard deviation"), ("sn", "nugget standard deviation"))
                                       for f in (0.5, 2.0)]


def set_priors(factors: dict) -> None:
    """Prior medians of M7n scaled by the given factors (one at a time in the sensitivity analysis)."""
    global PRIOR_SF, PRIOR_SN
    PRIOR_LS["bhf"] = BASE_PRIORS["ls_bhf"] * factors.get("ls_bhf", 1.0)
    PRIOR_LS["lubrication"] = BASE_PRIORS["ls_lub"] * factors.get("ls_lub", 1.0)
    PRIOR_SF = BASE_PRIORS["sf"] * factors.get("sf", 1.0)
    PRIOR_SN = BASE_PRIORS["sn"] * factors.get("sn", 1.0)
    _FITS.clear()


def sens_rows(args: tuple[str, dict, str]) -> list[dict]:
    """M7n intervals of one characteristic under one prior variant, for the calibration sets of the four
    relations (within, setting and transfer; not the pooled ones)."""
    from threadpoolctl import threadpool_limits

    name, factors, qc = args
    set_priors(factors)
    t, floors = _CTX["t"], _CTX["floors"]
    alts = sorted(t["alternative"].unique())
    rows = []
    with threadpool_limits(1):
        for calib, targets, label in jobs(alts):
            if label.startswith("pooled"):
                continue
            for target in targets:
                a = _CTX["tq"][(target, qc)]
                lo, hi, info = m7_interval(calib, target, qc, False)
                rows.append({"variant": name, "calibration": label, "relation": D.relation(calib, target),
                             "alternative": target, "geometry": a["geometry"], "qc": qc, "method": "M7n",
                             "real_q95": float(a["real_q95"]), "floor": floors[(qc, a["geometry"])],
                             "lo": float(lo), "hi": float(hi), **info})
    set_priors({})
    return rows


def prior_sensitivity(t: pd.DataFrame, floors: dict) -> pd.DataFrame:
    """Decisive and safe distances, coverage, half-width, length scale and distance from the force trend of M7n
    by relation, with each of its four prior medians halved and doubled; the reference variant reproduces the
    stored M7n intervals."""
    import panel as Pn

    tasks = [(name, f, qc) for name, f in SENS_VARIANTS for qc in SHARED]
    if N_JOBS > 1:
        with Pool(N_JOBS, initializer=_init_worker) as pool:
            chunks = pool.map(sens_rows, tasks)
    else:
        chunks = [sens_rows(x) for x in tasks]
    iv = pd.DataFrame([r for c in chunks for r in c])
    iv["scope"] = iv["calibration"].map(D.scope_of)
    iv = Pn.in_produced_floor(D.with_relation_scopes(iv), floors)
    old = pd.read_csv(RESULTS / "dec_intervals.csv")
    m1sn = old[old["method"] == "M1sn"].set_index(["calibration", "alternative", "qc"])["lo"]
    stored = pd.read_csv(RESULTS / "learn_intervals.csv")
    stored = stored[stored["method"] == "M7n"].set_index(["calibration", "alternative", "qc"])[["lo", "hi"]]
    rows = []
    rel_scope = {"sibling": "within", "interpolation": "setting/interpolation",
                 "extrapolation": "setting/extrapolation", "new family": "transfer"}
    for (name, rel), g in iv.groupby(["variant", iv["scope"].map({v: k for k, v in rel_scope.items()})]):
        r = D.distance_pair(*D.exclusion(g), sides=True)
        inside = (g["lo"] <= g["real_q95"]) & (g["real_q95"] <= g["hi"])
        key = list(zip(g["calibration"], g["alternative"], g["qc"]))
        centre = (g["lo"] + g["hi"]) / 2
        d_trend = np.abs(centre.to_numpy() - m1sn.reindex(key).to_numpy()) / g["floor"].to_numpy()
        row = {"variant": name, "relation": rel, "cases": len(g), **r, "coverage": float(inside.mean()),
               "median_half_width": float(np.median((g["hi"] - g["lo"]) / 2 / g["floor"])),
               "median_ls_bhf": float(g["gp_ls_bhf"].median()) if "gp_ls_bhf" in g else np.nan,
               "median_d_force_trend": float(np.nanmedian(d_trend))}
        if name == "reference":
            ref = stored.reindex(key)
            row["max_abs_diff_from_stored"] = float(np.nanmax(np.abs(g[["lo", "hi"]].to_numpy() - ref.to_numpy())))
        rows.append(row)
    return pd.DataFrame(rows)


# ── main ──────────────────────────────────────────────────────────────────────
def setup() -> tuple[pd.DataFrame, np.ndarray, dict]:
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    reps = np.load(RESULTS / "dec_q95_reps.npy")
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    floors = D.load_floors()
    D.setup(t, sims, floors)
    _CTX.update(t=t, floors=floors, tq={(a, q): r for a, q, r in zip(t["alternative"], t["qc"], t.to_dict("records"))},
                Fp=pooled_floor(), mu_grid=D._CTX["mu_grid"])
    return t, reps, floors


def _init_worker():
    setup()


def fit(t: pd.DataFrame, floors: dict) -> None:
    """Fit M7n, M7 and Mcd for every calibration set and add the relation-matched intervals."""
    if N_JOBS > 1:
        with Pool(min(N_JOBS, len(SHARED)), initializer=_init_worker) as pool:
            chunks = pool.map(qc_rows, SHARED)
    else:
        chunks = [qc_rows(qc) for qc in SHARED]
    new = pd.DataFrame([r for c in chunks for r in c])
    new["scope"] = new["calibration"].map(D.scope_of)
    ref_row = {(a, q): i for i, (a, q) in enumerate(zip(t["alternative"], t["qc"]))}
    new["ref_row"] = [ref_row[(a, q)] for a, q in zip(new["alternative"], new["qc"])]
    old = pd.read_csv(RESULTS / "dec_intervals.csv")
    rm = relation_matched(pd.concat([old, new], ignore_index=True), floors)
    pd.concat([new, rm], ignore_index=True).to_csv(RESULTS / "learn_intervals.csv", index=False)
    post = []
    for calib, targets, label in jobs(sorted(t["alternative"].unique())):
        p = mcd_posterior(tuple(sorted(calib)))
        post.append({"calibration": label, "scope": D.scope_of(label), "targets": "|".join(targets),
                     "mu_map": float(p.idxmax()), "mu_mean": float(np.sum(p.index.to_numpy() * p.to_numpy())),
                     "mass_at_0.15": float(p.get(0.15, 0.0)), "mass_at_0.05": float(p.get(0.05, 0.0)),
                     "entropy_bits": float(-np.sum(p[p > 0] * np.log2(p[p > 0])))})
    pd.DataFrame(post).to_csv(RESULTS / "learn_mcd_posterior.csv", index=False)


def score(t: pd.DataFrame, reps: np.ndarray, floors: dict) -> None:
    """Distances of the new rules with the paired resamples of decisions.py (same seeds per scope), a new family
    also in the produced family's floor (as step 6 scores it), and the diagnostics of the Gaussian processes."""
    import panel as Pn

    old = pd.read_csv(RESULTS / "dec_intervals.csv")
    learn = pd.read_csv(RESULTS / "learn_intervals.csv")
    need = set(learn["method"]) | {m for p in PAIRS for m in p}
    allv = D.with_relation_scopes(pd.concat([old[old["method"].isin(need)], learn], ignore_index=True))
    saved, D.PAIRS = D.PAIRS, PAIRS
    paired, paired_src = [], []
    res = D.distances(allv, reps, paired=paired)
    src = D.distances(Pn.in_produced_floor(allv[allv["scope"] == "transfer"], floors), reps, paired=paired_src)
    D.PAIRS = saved
    res = res[res["method"].isin(set(learn["method"]))]
    res.to_csv(RESULTS / "learn_resolution.csv", index=False)
    src = src[src["method"].isin(set(learn["method"]))].assign(floor="source family")
    src.to_csv(RESULTS / "learn_source_floor.csv", index=False)
    pairs = pd.concat([pd.DataFrame(paired), pd.DataFrame(paired_src).assign(scope="transfer (produced family's floor)")],
                      ignore_index=True)
    pairs.to_csv(RESULTS / "learn_paired.csv", index=False)
    new = learn[learn["method"].isin(NEW_RULES)]
    gpd = gp_diagnostics(pd.concat([old, new], ignore_index=True), t)
    gpd.to_csv(RESULTS / "learn_gp_diagnostics.csv", index=False)


def summarise() -> None:
    res = pd.read_csv(RESULTS / "learn_resolution.csv")
    src = pd.read_csv(RESULTS / "learn_source_floor.csv")
    pairs = pd.read_csv(RESULTS / "learn_paired.csv")
    gpd = pd.read_csv(RESULTS / "learn_gp_diagnostics.csv")
    post = pd.read_csv(RESULTS / "learn_mcd_posterior.csv")
    fss = pd.read_csv(RESULTS / "learn_fewshot.csv")
    cols = ["scope", "method", "n_cases", "resolution_floors", "resolution_lo", "resolution_hi", "safe_floors",
            "safe_lo", "safe_hi", "safe_failing"]
    lines = ["# Learners for the small-data regime and relation-matched intervals", "",
             "## Distances (floors; 1000 family-stratified resamples, the same as decisions.py)", "",
             res[res["qc"] == "all"][cols].round(2).to_markdown(index=False), "",
             "## A new family in the produced family's floor", "",
             src[src["qc"] == "all"][cols].round(2).to_markdown(index=False), "",
             "## Paired differences (a minus b)", "", pairs.round(2).to_markdown(index=False), "",
             "## Gaussian-process diagnostics by relation", "", gpd.round(3).to_markdown(index=False), "",
             "## Mcd: posterior of the friction coefficient", "", post.round(3).to_markdown(index=False), "",
             "## Few-shot transfer to a new family (target family's floor)", "",
             fss[fss["relation"] == "all"].round(2).to_markdown(index=False), "",
             fss[fss["relation"] != "all"].round(2).to_markdown(index=False)]
    (RESULTS / "summary_learners.md").write_text("\n".join(lines) + "\n")


def main(argv: list[str]) -> None:
    """learners.py                      fit, score, few-shot transfer and summary
       learners.py --score              score the stored intervals again (no fits)
       learners.py --prior-sensitivity  M7n with each prior median halved and doubled (learn_m7n_priors.csv)"""
    t, reps, floors = setup()
    if "--prior-sensitivity" in argv:
        prior_sensitivity(t, floors).to_csv(RESULTS / "learn_m7n_priors.csv", index=False)
        print("learn_m7n_priors.csv: written")
        return
    if "--score" not in argv:
        fit(t, floors)
    score(t, reps, floors)
    if "--score" not in argv or not (RESULTS / "learn_fewshot.csv").exists():
        fs = fewshot(t, floors)
        fs.to_csv(RESULTS / "learn_fewshot_intervals.csv.gz", index=False)
        fewshot_scores(fs).to_csv(RESULTS / "learn_fewshot.csv", index=False)
    summarise()


if __name__ == "__main__":
    main(sys.argv[1:])
