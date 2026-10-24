"""Qualification of the rules as a team would use them: strata, guard bands, costs, uncertainty and selection.

All analyses use the stored intervals of decisions.py and learners.py (fits fixed) or, where the truth or the
decided statistic changes, refit the alternative-level rules with robustness.fast_intervals.

 1. Decision-time sibling strata: a new variant is classed by whether its two produced siblings differ resolvably
    from each other (effect-to-scatter ratio >= 1 between them), which a team knows before deciding; the strata of
    panel.py, which use the held-out alternative's own contrasts, remain as a diagnostic.
 2. Guard bands per family, out of sample and under other priors: the band of step 5 estimated per geometry, then
    validated leaving one alternative out (within a family and pooled) and, for new settings, one force cell out,
    and moved between the geometries; band and trial rate against the half-width of the prior (the evaluation
    grid within +-3 to +-50 floors); the share correct per characteristic and per class of characteristic.
 3. Costs: expected cost per verdict, c_FA P(false accept) + c_FR P(false reject) + c_T P(trial), over the
    requirement prior, for each rule alone, with its 95 % band and with the cost-minimising band, against the cost
    of a trial relative to a false accept; the trial of n parts as a reference rule (first 20 or 50 parts of the
    design's own run, a within-run lower bound of a trial's error).
 4. Uncertainty: coverage of the interval rules with cluster-bootstrap intervals over alternatives, per relation,
    characteristic and decision-time stratum, with each rule's guaranteed or nominal level and the interval score
    (Gneiting and Raftery 2007); the width of the paired intervals between point rules (the smallest difference
    the design resolves); a sensitivity analysis that adds a between-run component to every truth (standard
    deviation tau floors of a future run's q95 about the observed one) and reports distances, ranking and guard
    bands.
 5. Selection: the rule with the smallest decisive (or safe) distance selected on one geometry (one transfer) and
    evaluated on the other, with and without its guard band; the distances of a rule committed to in advance; the
    variance decomposition restricted to the pre-specified rules.
 6. Per characteristic: decisive and safe distances per characteristic and group in floors and physical units,
    relative to the long-term standard deviation and as the performance index of a requirement at that distance.
 7. Extensions: a design-level verdict (a design meets only if all seven characteristics meet), lower limits (the
    5th percentile of draw-ins, wall angle and depth, by a change of sign), truths and calibration from the first
    20 or 50 parts (short runs), and the decided statistic mu + 4 sigma (a performance index of 1.33).

Outputs: results/qual_*.csv, summary_qualify.md
"""

from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
import panel as P  # noqa: E402
from common import RESULTS, centre  # noqa: E402
from qc import QCS, SHARED, parts_qc  # noqa: E402

PRESPECIFIED = ["M0", "M1", "M2", "M3", "M4", "M5"]            # defined before the decision results were seen
MAIN = ["M0", "M1s", "M2", "M5", "NN", "M1sn", "M7n"]           # rules of the main text
INTERVAL = ["M2", "M2n", "M3", "M4", "M5", "M5n", "M7", "M7n", "Mcd"]
RELATIONS = {"sibling": "within", "interpolation": "setting/interpolation",
             "extrapolation": "setting/extrapolation", "new family": "transfer"}
CLASSES = {"drawin_mid": "process indicators", "drawin_corner": "process indicators", "waviness": "process indicators",
           "wall_op10": "drawn geometry", "depth_op10": "drawn geometry", "arm_op20": "cut part", "dome_op20": "cut part"}
PRIOR_WIDTHS = [3.0, 5.0, 10.0, 20.0, 50.0]
COST_TRIAL = [0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5]
COST_FR = [0.25, 0.5, 1.0]
COST_BANDS = np.round(np.arange(0.0, 40.0 + 1e-9, 0.25), 2)
COST_BAND_MAX = 20.0                                            # step 5 searches bands up to 20 floors
TAUS = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]
N_TAU_DRAWS = 200
N_CLUSTER = 2000
TRIAL_PARTS = [20, 50]
LOWER_QCS = ["drawin_mid", "drawin_corner", "wall_op10", "depth_op10"]
SHORT_PARTS = [20, 50]
PPK_TARGET = 1.33
SEED = 11


def nominal_level(method: str, n: int, relation: str = "sibling") -> str:
    """Level of an interval rule with n calibration alternatives. The largest-residual and jackknife+ levels are
    guaranteed only with a sibling, where the held-out alternative is exchangeable with the calibration ones; a
    held-out force or family is not, so there they are nominal, like the model-based and relation-matched levels
    (with a single calibration family, P+RM has no guarantee even if the families were exchangeable)."""
    held_out = "guaranteed" if relation == "sibling" else "nominal, held-out cases not exchangeable"
    if method.endswith("+RM"):
        return "0.90 nominal (split conformal across families, no guarantee)"
    if method in ("M2", "M2n"):
        return f"{(n - 1) / (n + 1):.2f} {held_out} (largest residual)"
    if method in ("M3", "M4"):
        return f"{1 - 2 / (n + 1):.2f} {held_out} (jackknife+)"
    if method in ("M5", "M5n", "M7", "M7n", "Mcd"):
        return "0.90 nominal (model-based, no guarantee)"
    return ""


# ── data ──────────────────────────────────────────────────────────────────────
def load() -> dict:
    old = pd.read_csv(RESULTS / "dec_intervals.csv")
    new = pd.read_csv(RESULTS / "learn_intervals.csv")
    iv = pd.concat([old, new], ignore_index=True)
    floors = D.load_floors()
    ivr = D.with_relation_scopes(iv)
    ivs = P.in_produced_floor(ivr, floors)        # a new family in the produced family's floor (step 6)
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    return {"iv": iv, "ivs": ivs, "floors": floors, "t": t, "reps": np.load(RESULTS / "dec_q95_reps.npy")}


def relation_cases(ivs: pd.DataFrame, rel: str, method: str) -> pd.DataFrame:
    return ivs[(ivs["scope"] == RELATIONS[rel]) & (ivs["method"] == method)]


# ── 1. decision-time strata ──────────────────────────────────────────────────
def decision_time_strata(iv: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    eff = pd.read_csv(RESULTS / "alt_effects.csv")
    lub = eff[eff["family"] == "lubrication"]
    res = {(frozenset((a, b)), q): bool(e >= 1) for a, b, q, e in zip(lub["a"], lub["b"], lub["qc"], lub["esr"])}
    alts = sorted(iv["alternative"].unique())

    def stratum(alt: str, qc: str) -> str:
        geo, f, _ = alt.split("/")
        sibs = [a for a in alts if a.startswith(f"{geo}/{f}/") and a != alt]
        return "siblings resolvable" if res[(frozenset(sibs), qc)] else "siblings not resolvable"

    w = iv[iv["scope"] == "within"].copy()
    w["stratum"] = [stratum(a, q) for a, q in zip(w["alternative"], w["qc"])]
    rows = []
    for (s, m), g in w.groupby(["stratum", "method"]):
        mid = (g["lo"] + g["hi"]) / 2
        err = np.abs(mid - g["real_q95"]) / g["floor"]
        rows.append({"stratum": s, "method": m, "cases": len(g), "alternatives": g["alternative"].nunique(),
                     **P.dist(g), "abs_error_p90": float(np.quantile(err, 0.9)),
                     "coverage": float(np.mean((g["lo"] <= g["real_q95"]) & (g["real_q95"] <= g["hi"])))})
    cases = w.drop_duplicates(["alternative", "qc"])[["alternative", "qc", "stratum"]]
    return pd.DataFrame(rows), cases


# ── 2. guard bands ────────────────────────────────────────────────────────────
def prior_grid(width: float) -> np.ndarray:
    return D.D_GRID[np.abs(D.D_GRID) <= width]


def verdict_outcomes(g: pd.DataFrame, band: float, grid: np.ndarray) -> dict:
    """Counts of correct, wrong and trial verdicts over the feasible requirements of the prior grid, with the
    rule's interval widened by band floors (band = inf: every design to trial)."""
    q, F = g["real_q95"].to_numpy(float)[:, None], g["floor"].to_numpy(float)[:, None]
    lo, hi = g["lo"].to_numpy(float)[:, None], g["hi"].to_numpy(float)[:, None]
    reqs = q + grid[None, :] * F
    feas = reqs >= 0
    if not np.isfinite(band):
        n = int(feas.sum())
        return {"verdicts": n, "decided": 0, "correct": 0, "false_accept": 0, "false_reject": 0, "trial": n}
    meets, fails = (hi + band * F <= reqs) & feas, (lo - band * F > reqs) & feas
    adequate = (grid >= 0)[None, :]
    fa, fr = int((meets & ~adequate).sum()), int((fails & adequate).sum())
    correct = int((meets & adequate).sum() + (fails & ~adequate).sum())
    n = int(feas.sum())
    return {"verdicts": n, "decided": correct + fa + fr, "correct": correct, "false_accept": fa, "false_reject": fr,
            "trial": n - correct - fa - fr}


def share_correct(o: dict) -> float:
    return o["correct"] / o["decided"] if o["decided"] else np.nan


def band_of(g: pd.DataFrame, grid: np.ndarray) -> float:
    return P.guard_band(g, grid)[0]


def guard_per_family(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """In-sample bands per geometry, the pooled band, and the bands moved between geometries."""
    rows = []
    grid = prior_grid(20.0)
    for rel in RELATIONS:
        for m in rules:
            g = relation_cases(ivs, rel, m)
            if g.empty:
                continue
            pooled = band_of(g, grid)
            row = {"relation": rel, "method": m, "band_pooled": pooled}
            for geo in ("concave", "convex"):
                own = g[g["geometry"] == geo]
                other = g[g["geometry"] != geo]
                b_own, b_other = band_of(own, grid), band_of(other, grid)
                o_own = verdict_outcomes(own, b_own, grid)
                o_moved = verdict_outcomes(own, b_other, grid)
                row.update({f"band_{geo}": b_own, f"correct_{geo}": share_correct(o_own),
                            f"trial_{geo}": o_own["trial"] / o_own["verdicts"],
                            f"correct_{geo}_with_other_band": share_correct(o_moved),
                            f"trial_{geo}_with_other_band": o_moved["trial"] / o_moved["verdicts"]})
            rows.append(row)
    return pd.DataFrame(rows)


def cluster_ci(values: dict[str, tuple[np.ndarray, np.ndarray]], rng: np.random.Generator,
               n: int = N_CLUSTER) -> tuple[float, float]:
    """Cluster-bootstrap interval of a ratio sum(num)/sum(den) over alternatives (resampled within geometry)."""
    alts = np.array(sorted(values))
    fam = np.array([a.split("/")[0] for a in alts])
    num = np.array([values[a][0] for a in alts], dtype=float)
    den = np.array([values[a][1] for a in alts], dtype=float)
    out = []
    groups = [np.flatnonzero(fam == f) for f in np.unique(fam)]
    for _ in range(n):
        idx = np.concatenate([rng.choice(g, g.size) for g in groups])
        d = den[idx].sum()
        out.append(num[idx].sum() / d if d > 0 else np.nan)
    out = np.array(out)
    return float(np.nanpercentile(out, 2.5)), float(np.nanpercentile(out, 97.5))


def guard_out_of_sample(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """Leave one alternative out (within its family, and pooled over the families) and, for new settings, one
    force cell out: the band is estimated without the held-out cases and applied to them."""
    rows = []
    rng = np.random.default_rng(SEED)
    for prior_name, width in (("reference (+-20)", 20.0), ("release-like (+-5)", 5.0)):
        grid = prior_grid(width)
        for rel in RELATIONS:
            for m in rules:
                g = relation_cases(ivs, rel, m)
                if g.empty:
                    continue
                schemes = {"LOAO within family": lambda a, h: h[(h["alternative"] != a) & (h["geometry"] == a.split("/")[0])],
                           "LOAO pooled": lambda a, h: h[h["alternative"] != a]}
                if rel in ("interpolation", "extrapolation"):
                    schemes["leave force cell out"] = lambda a, h: h[~((h["geometry"] == a.split("/")[0]) &
                                                                       (h["bhf_kN"] == int(a.split("/")[1])))]
                for scheme, rest_of in schemes.items():
                    per_alt, tot = {}, {"correct": 0, "decided": 0, "trial": 0, "verdicts": 0}
                    bands = []
                    for a, own in g.groupby("alternative"):
                        b = band_of(rest_of(a, g), grid)
                        bands.append(b)
                        o = verdict_outcomes(own, b, grid)
                        per_alt[a] = (o["correct"], o["decided"], o["trial"], o["verdicts"])
                        for k in tot:
                            tot[k] += o[k]
                    sc = tot["correct"] / tot["decided"] if tot["decided"] else np.nan
                    lo, hi = cluster_ci({a: (v[0], v[1]) for a, v in per_alt.items()}, rng)
                    tlo, thi = cluster_ci({a: (v[2], v[3]) for a, v in per_alt.items()}, rng)
                    ins = verdict_outcomes(g, band_of(g, grid), grid)
                    rows.append({"prior": prior_name, "relation": rel, "method": m, "scheme": scheme,
                                 "median_band": float(np.median(bands)), "share_correct": sc,
                                 "share_correct_lo": lo, "share_correct_hi": hi,
                                 "trial_rate": tot["trial"] / tot["verdicts"], "trial_lo": tlo, "trial_hi": thi,
                                 "in_sample_band": band_of(g, grid), "in_sample_correct": share_correct(ins),
                                 "in_sample_trial": ins["trial"] / ins["verdicts"]})
    return pd.DataFrame(rows)


def guard_decision_time(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """The band a team can have when it decides. With a sibling, the band of the family's own sibling cases,
    validated leaving one alternative out within the family. For a new setting or a new family, which the family's
    own production cannot exercise (a family produced at two forces has no interpolation case), the band of the
    same relation in the other family, applied to this family and so validated out of family. Shares correct among
    decided verdicts with cluster intervals over alternatives (sibling only: for a new setting the alternatives of a
    held-out cell share one fit), trial rate, verdict counts and the worst characteristic under the band."""
    rows = []
    rng = np.random.default_rng(SEED + 7)
    keys = ("correct", "decided", "trial", "verdicts", "false_accept", "false_reject")
    for prior_name, width in (("reference (+-20)", 20.0), ("release-like (+-5)", 5.0)):
        grid = prior_grid(width)
        for rel in RELATIONS:
            for m in rules:
                g = relation_cases(ivs, rel, m)
                if g.empty:
                    continue
                tot = dict.fromkeys(keys, 0)
                per_alt, per_qc, band_used = {}, {}, {}
                per_geo = {geo: dict.fromkeys(keys, 0) for geo in ("concave", "convex")}
                for geo in ("concave", "convex"):
                    own = g[g["geometry"] == geo]
                    if rel == "sibling":
                        band_used[geo] = band_of(own, grid)
                        band_for = {a: band_of(own[own["alternative"] != a], grid) for a in own["alternative"].unique()}
                    else:
                        band_used[geo] = band_of(g[g["geometry"] != geo], grid)
                        band_for = dict.fromkeys(own["alternative"].unique(), band_used[geo])
                    for a, h in own.groupby("alternative"):
                        o = verdict_outcomes(h, band_for[a], grid)
                        per_alt[a] = (o["correct"], o["decided"], o["trial"], o["verdicts"])
                        for k in keys:
                            tot[k] += o[k]
                            per_geo[geo][k] += o[k]
                        for qc, hq in h.groupby("qc"):
                            oq = verdict_outcomes(hq, band_for[a], grid)
                            c, d = per_qc.get(qc, (0, 0))
                            per_qc[qc] = (c + oq["correct"], d + oq["decided"])
                sc = tot["correct"] / tot["decided"] if tot["decided"] else np.nan
                lo = hi = tlo = thi = np.nan
                if rel == "sibling":
                    lo, hi = cluster_ci({a: (v[0], v[1]) for a, v in per_alt.items()}, rng)
                    tlo, thi = cluster_ci({a: (v[2], v[3]) for a, v in per_alt.items()}, rng)
                qshare = {qc: c / d for qc, (c, d) in per_qc.items() if d >= 20}
                worst = min(qshare, key=qshare.get) if qshare else ""
                rows.append({"prior": prior_name, "relation": rel, "method": m,
                             "scheme": "own family, one alternative left out" if rel == "sibling" else "other family's band",
                             "band_concave": band_used["concave"], "band_convex": band_used["convex"],
                             "share_correct": sc, "share_correct_lo": lo, "share_correct_hi": hi,
                             "trial_rate": tot["trial"] / tot["verdicts"], "trial_lo": tlo, "trial_hi": thi,
                             "decided": tot["decided"], "verdicts": tot["verdicts"],
                             "false_accept_share": tot["false_accept"] / tot["verdicts"],
                             "alternatives": g["alternative"].nunique(),
                             "worst_characteristic": worst, "worst_share_correct": qshare.get(worst, np.nan),
                             **{f"{k}_{geo}": v for geo, o in per_geo.items() for k, v in (
                                 ("share_correct", o["correct"] / o["decided"] if o["decided"] else np.nan),
                                 ("trial_rate", o["trial"] / o["verdicts"] if o["verdicts"] else np.nan),
                                 ("decided", o["decided"]), ("verdicts", o["verdicts"]))},
                             **{f"share_{qc}": c / d if d else np.nan for qc, (c, d) in per_qc.items()},
                             **{f"decided_{qc}": d for qc, (c, d) in per_qc.items()}})
    return pd.DataFrame(rows)


def guard_nested_sibling(ivs: pd.DataFrame, t: pd.DataFrame) -> pd.DataFrame:
    """Sibling validation of the nearest setting with strictly nested fits. Table 7 leaves one alternative out of
    the band's cases, but those cases' predictions were fitted with it; here every prediction behind the band of a
    held-out alternative is recomputed without it (the mean q_p of the remaining siblings at the same force)."""
    rows = []
    g = relation_cases(ivs, "sibling", "NN")
    q = t.set_index(["alternative", "qc"])["real_q95"]
    alts = sorted(g["alternative"].unique())
    stored = g.set_index(["alternative", "qc"])
    for prior_name, width in (("reference (+-20)", 20.0), ("release-like (+-5)", 5.0)):
        grid = prior_grid(width)
        tot = {"correct": 0, "decided": 0, "trial": 0, "verdicts": 0}
        max_dev = 0.0
        for a in alts:
            geo, f, _ = a.split("/")
            others = [b for b in alts if b.startswith(geo + "/") and b != a]
            cases = []
            for b in others:
                bf = b.split("/")[1]
                sibs = [c for c in alts if c.startswith(f"{geo}/{bf}/") and c not in (a, b)]
                for qc in g["qc"].unique():
                    r = stored.loc[(b, qc)]
                    if a.split("/")[1] != bf:          # a was not among b's siblings: the stored prediction stands
                        max_dev = max(max_dev, abs(r["lo"] - np.mean([q[(c, qc)] for c in sibs])))
                    pred = float(np.mean([q[(c, qc)] for c in sibs]))
                    cases.append({"lo": pred, "hi": pred, "real_q95": r["real_q95"], "floor": r["floor"]})
            b_a = band_of(pd.DataFrame(cases), grid)
            o = verdict_outcomes(g[g["alternative"] == a], b_a, grid)
            for k in tot:
                tot[k] += o[k]
        rows.append({"prior": prior_name, "method": "NN", "scheme": "strictly nested (predictions refitted without "
                     "the held-out alternative)", "share_correct": tot["correct"] / tot["decided"],
                     "trial_rate": tot["trial"] / tot["verdicts"], "decided": tot["decided"],
                     "verdicts": tot["verdicts"], "check_max_dev_stored": max_dev})
    return pd.DataFrame(rows)


def guard_prior_width(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    rows = []
    for rel in RELATIONS:
        for m in rules:
            g = relation_cases(ivs, rel, m)
            if g.empty:
                continue
            for w in PRIOR_WIDTHS:
                grid = prior_grid(w)
                b = band_of(g, grid)
                o = verdict_outcomes(g, b, grid)
                rows.append({"relation": rel, "method": m, "prior_half_width": w, "band": b,
                             "trial_rate": o["trial"] / o["verdicts"], "share_correct": share_correct(o),
                             "decided_share": o["decided"] / o["verdicts"]})
    return pd.DataFrame(rows)


def guard_per_characteristic(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    rows = []
    grid = prior_grid(20.0)
    for rel in RELATIONS:
        for m in rules:
            g = relation_cases(ivs, rel, m)
            if g.empty:
                continue
            b = band_of(g, grid)
            for qc, h in g.groupby("qc"):
                o = verdict_outcomes(h, b, grid)
                rows.append({"relation": rel, "method": m, "group": "characteristic", "name": qc, "pooled_band": b,
                             "share_correct": share_correct(o), "trial_rate": o["trial"] / o["verdicts"],
                             "own_band": band_of(h, grid)})
            for cls, h in g.groupby(g["qc"].map(CLASSES)):
                o = verdict_outcomes(h, b, grid)
                ob = band_of(h, grid)
                oo = verdict_outcomes(h, ob, grid)
                rows.append({"relation": rel, "method": m, "group": "class", "name": cls, "pooled_band": b,
                             "share_correct": share_correct(o), "trial_rate": o["trial"] / o["verdicts"],
                             "own_band": ob, "own_band_correct": share_correct(oo),
                             "own_band_trial": oo["trial"] / oo["verdicts"]})
    return pd.DataFrame(rows)


# ── 3. costs and the trial ────────────────────────────────────────────────────
def costs(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """Expected cost per verdict (in units of a false accept) by prior, cost ratio, relation and trial cost. The
    cost-minimising band follows step 5: stated costs only widen the 95 % band, so it is searched from that band up
    to the step's limit of 20 floors, or every design goes to trial; a rule without a 95 % band sends every design to
    trial. Bands are chosen in sample, pooled over the families; cost_alone is the rule without a band."""
    rows = []
    for prior_name, width in (("reference (+-20)", 20.0), ("release-like (+-5)", 5.0)):
        grid = prior_grid(width)
        for rel in RELATIONS:
            for m in rules:
                g = relation_cases(ivs, rel, m)
                if g.empty:
                    continue
                outs = [verdict_outcomes(g, b, grid) for b in COST_BANDS]
                n = outs[0]["verdicts"]
                fa = np.array([o["false_accept"] for o in outs]) / n
                fr = np.array([o["false_reject"] for o in outs]) / n
                tr = np.array([o["trial"] for o in outs]) / n
                b95 = band_of(g, grid)
                i95 = int(np.argmin(np.abs(COST_BANDS - b95))) if np.isfinite(b95) else None
                allowed = ((COST_BANDS >= b95 - 1e-9) & (COST_BANDS <= COST_BAND_MAX + 1e-9)) if i95 is not None \
                    else np.zeros(len(COST_BANDS), dtype=bool)
                for cfr in COST_FR:
                    for ct in COST_TRIAL:
                        c = fa + cfr * fr + ct * tr
                        j = int(np.flatnonzero(allowed)[np.argmin(c[allowed])]) if allowed.any() else None
                        use = j is not None and c[j] < ct     # otherwise every design goes to trial
                        rows.append({"prior": prior_name, "relation": rel, "method": m, "c_fr": cfr, "c_trial": ct,
                                     "cost_alone": float(c[0]), "fa_alone": fa[0], "fr_alone": fr[0],
                                     "trial_alone": tr[0],
                                     "band_95": b95, "cost_band_95": float(c[i95]) if i95 is not None else ct,
                                     "trial_band_95": float(tr[i95]) if i95 is not None else 1.0,
                                     "band_opt": float(COST_BANDS[j]) if use else np.inf,
                                     "cost_opt": float(c[j]) if use else float(ct),
                                     "trial_opt": float(tr[j]) if use else 1.0,
                                     "fa_opt": float(fa[j]) if use else 0.0,
                                     "fr_opt": float(fr[j]) if use else 0.0, "cost_always_trial": ct})
    return pd.DataFrame(rows)


def trial_cases(t: pd.DataFrame, q: pd.DataFrame, floors: dict, n: int) -> pd.DataFrame:
    """A trial of the first n parts of the design's own run as a point rule: one case per alternative and
    characteristic, scored in the floor of its geometry."""
    cases = []
    for (alt, qc), r in t.set_index(["alternative", "qc"]).iterrows():
        y = D.transform(qc, q.loc[q["alternative"] == alt, qc].dropna().to_numpy())[:n]
        v = float(np.quantile(y, D.ADEQUATE_RATE))
        cases.append({"alternative": alt, "geometry": r["geometry"], "qc": qc, "lo": v, "hi": v,
                      "real_q95": r["real_q95"], "floor": floors[(qc, r["geometry"])]})
    return pd.DataFrame(cases)


def trial_reference(t: pd.DataFrame, q: pd.DataFrame, floors: dict) -> pd.DataFrame:
    """A trial of the first n parts of the design's own run, scored as a point rule (within-run: variation
    between runs would add to its error)."""
    rows = []
    for n in TRIAL_PARTS:
        g = trial_cases(t, q, floors, n)
        err = np.abs(g["lo"] - g["real_q95"]) / g["floor"]
        rows.append({"rule": f"trial, first {n} parts", "cases": len(g), **P.dist(g),
                     "abs_error_p90": float(np.quantile(err, 0.9)), "abs_error_median": float(np.median(err))})
    return pd.DataFrame(rows)


def trial_cost(t: pd.DataFrame, q: pd.DataFrame, floors: dict) -> pd.DataFrame:
    """The trial's own error priced like a rule's (Fig. 6 prices a trial verdict at c_T alone): expected cost of
    its false accepts and false rejects per verdict over each prior, and the share of the prior's feasible
    verdicts that fall on failing designs."""
    rows = []
    for n in TRIAL_PARTS:
        g = trial_cases(t, q, floors, n)
        for prior_name, width in (("reference (+-20)", 20.0), ("release-like (+-5)", 5.0)):
            grid = prior_grid(width)
            o = verdict_outcomes(g, 0.0, grid)
            reqs = g["real_q95"].to_numpy(float)[:, None] + grid[None, :] * g["floor"].to_numpy(float)[:, None]
            feas = reqs >= 0
            failing_share = float((feas & (grid < 0)[None, :]).sum() / feas.sum())
            for cfr in COST_FR:
                rows.append({"rule": f"trial, first {n} parts", "prior": prior_name, "c_fr": cfr,
                             "false_accept": o["false_accept"] / o["verdicts"],
                             "false_reject": o["false_reject"] / o["verdicts"],
                             "error_cost": (o["false_accept"] + cfr * o["false_reject"]) / o["verdicts"],
                             "failing_share_of_verdicts": failing_share})
    return pd.DataFrame(rows)


def release_capability() -> pd.DataFrame:
    """Release as a capability decision: with the decided statistic centre + 4 sd (a performance index of 1.33 at
    the limit), a rule's decisive distance delta (floors) means it confirms Ppk >= 1.33 only for designs whose
    true Ppk exceeds 4/3 + delta (F / sigma_LT) / 3; F / sigma_LT over characteristics and geometries."""
    v = pd.read_csv(RESULTS / "qual_variants.csv")
    v = v[v["variant"] == f"decided statistic: centre + {3 * PPK_TARGET:g} sd"]
    ratio = pd.read_csv(RESULTS / "panel_floor_protocol.csv")["floor_over_sigma_lt"].to_numpy(float)
    rows = []
    for r in v.to_dict("records"):
        dd = r["resolution_floors"]
        ppk = 4.0 / 3.0 + dd * ratio / 3.0
        rows.append({"relation": r["relation"], "method": r["method"], "decisive_on_centre_plus_4sd": dd,
                     "true_ppk_min": float(ppk.min()), "true_ppk_median": float(np.median(ppk)),
                     "true_ppk_max": float(ppk.max())})
    return pd.DataFrame(rows)


def cost_cheapest(costs_table: pd.DataFrame) -> pd.DataFrame:
    """Cheapest option per prior, cost ratio, relation and trial cost: each rule with its cost-minimising band
    (chosen in-sample, pooled over the families) or a trial of every design, and the margin to the runner-up."""
    rows = []
    tol = 1e-9
    for (prior, cfr, rel, ct), g in costs_table.groupby(["prior", "c_fr", "relation", "c_trial"]):
        # a rule whose cost-minimising band sends every design to trial is the trial itself
        opts = {m: c for m, c in zip(g["method"], g["cost_opt"]) if c < ct - tol}
        opts["trial every design"] = float(ct)
        best = min(opts.values())
        tied = sorted(m for m, c in opts.items() if c <= best + tol)
        rest = sorted((c, m) for m, c in opts.items() if c > best + tol)
        first = tied[0]
        rows.append({"prior": prior, "c_fr": cfr, "relation": rel, "c_trial": ct, "cheapest": " = ".join(tied),
                     "cost": best, "runner_up": rest[0][1] if rest else "", "runner_up_cost": rest[0][0] if rest else np.nan,
                     "margin": rest[0][0] - best if rest else np.nan,
                     "fa_of_cheapest": float(g.loc[g["method"] == first, "fa_opt"].iloc[0]) if first in set(g["method"]) else 0.0})
    return pd.DataFrame(rows)


# ── 4. uncertainty ───────────────────────────────────────────────────────────
def interval_score(lo, hi, y, alpha: float = 1 - D.CONF_LEVEL):
    return (hi - lo) + (2 / alpha) * np.maximum(lo - y, 0) + (2 / alpha) * np.maximum(y - hi, 0)


def coverage(ivs: pd.DataFrame, strata: pd.DataFrame) -> pd.DataFrame:
    """Coverage and interval score per relation, and per family, characteristic and (with a sibling) decision-time
    stratum. Cluster intervals over alternatives only with a sibling, where every alternative has its own
    calibration set; for a new setting or family the alternatives of a held-out cell share one fit, and an
    interval over alternatives would be degenerate or too narrow. The pooled scopes (both families calibrate,
    with a family term) are added for the Gaussian processes."""
    rng = np.random.default_rng(SEED + 1)
    st = strata.set_index(["alternative", "qc"])["stratum"]
    rows = []
    methods = [m for m in ivs["method"].unique() if m in INTERVAL or m.endswith("+RM")]
    n_cal = {"sibling": 8, "interpolation": 6, "extrapolation": 6, "new family": 9,
             "pooled sibling": 17, "pooled interpolation": 15, "pooled extrapolation": 15}
    scopes = {**RELATIONS, "pooled sibling": "pooled", "pooled interpolation": "pooled-setting/interpolation",
              "pooled extrapolation": "pooled-setting/extrapolation"}

    def ci(h: pd.DataFrame, ins: np.ndarray, rel: str) -> tuple[float, float]:
        if rel != "sibling":
            return np.nan, np.nan
        per = {a: (float(ins[(h["alternative"] == a).to_numpy()].sum()), float((h["alternative"] == a).sum()))
               for a in h["alternative"].unique()}
        return cluster_ci(per, rng)

    for rel, scope in scopes.items():
        for m in methods:
            if rel.startswith("pooled") and m not in ("M5", "M5n", "M7", "M7n"):
                continue
            g = ivs[(ivs["scope"] == scope) & (ivs["method"] == m)]
            if g.empty:
                continue
            inside = ((g["lo"] <= g["real_q95"]) & (g["real_q95"] <= g["hi"])).to_numpy()
            isc = interval_score(g["lo"], g["hi"], g["real_q95"]) / g["floor"]
            lo, hi = ci(g, inside, rel)
            base = {"relation": rel, "method": m, "level": nominal_level(m, n_cal[rel], rel)}
            rows.append({**base, "subset": "all", "cases": len(g), "coverage": float(inside.mean()),
                         "coverage_lo": lo, "coverage_hi": hi,
                         "median_half_width": float(np.nanmedian((g["hi"] - g["lo"]) / 2 / g["floor"])),
                         "interval_score": float(np.nanmean(isc)),
                         "rm_n": float(g["rm_n"].median()) if "rm_n" in g and g["rm_n"].notna().any() else np.nan})
            subsets = list(g.groupby("qc")) + [(f"family: {geo}", h) for geo, h in g.groupby("geometry")]
            if rel == "sibling":
                subsets += list(g.groupby([st.get((a, q), "") for a, q in zip(g["alternative"], g["qc"])]))
            for name, h in subsets:
                ins = ((h["lo"] <= h["real_q95"]) & (h["real_q95"] <= h["hi"])).to_numpy()
                lo, hi = ci(h, ins, rel)
                row = {**base, "subset": name, "cases": len(h), "coverage": float(ins.mean()),
                       "coverage_lo": lo, "coverage_hi": hi,
                       "interval_score": float(np.nanmean(interval_score(h["lo"], h["hi"], h["real_q95"]) / h["floor"]))}
                if name.startswith("family: ") and m.endswith("+RM"):
                    row["rm_quantile_floors"] = float(h["rm_quantile_floors"].median())
                    row["rm_n"] = float(h["rm_n"].median())
                rows.append(row)
    # point rules: interval score of the point prediction (no width)
    for rel, scope in RELATIONS.items():
        for m in ["M0", "M1", "M1s", "M1n", "M1sn", "NN", "Mc"]:
            g = ivs[(ivs["scope"] == scope) & (ivs["method"] == m)]
            if len(g):
                rows.append({"relation": rel, "method": m, "level": "point", "subset": "all", "cases": len(g),
                             "interval_score": float(np.nanmean(interval_score(g["lo"], g["hi"], g["real_q95"]) / g["floor"]))})
    out = pd.DataFrame(rows)

    def note(r) -> str:     # why an interval is or is not given, and which given intervals are degenerate
        if r["level"] == "point":
            return "point rule: interval score only"
        if r["relation"] != "sibling":
            return "no interval: the alternatives of a held-out cell share one fit"
        if np.isclose(r["coverage_lo"], r["coverage_hi"]):
            return "degenerate: every resample gives the same share"
        return "cluster bootstrap over alternatives"
    out["ci_note"] = out.apply(note, axis=1)
    return out


def m6_coverage(t: pd.DataFrame, floors: dict) -> pd.DataFrame:
    """Coverage and interval score of M6 (the M5 mean with a conformal margin on standardised leave-one-out
    residuals of the calibration set), whose intervals robustness.py does not store."""
    import panel
    import robustness as R

    iv = R.m6_intervals(t, floors)
    iv = panel.in_produced_floor(D.with_relation_scopes(iv), floors)
    rng = np.random.default_rng(SEED + 5)
    rows = []
    for rel, scope in RELATIONS.items():
        g = iv[iv["scope"] == scope]
        if g.empty:
            continue
        inside = ((g["lo"] <= g["real_q95"]) & (g["real_q95"] <= g["hi"])).to_numpy()
        per = {a: (float(inside[(g["alternative"] == a).to_numpy()].sum()), float((g["alternative"] == a).sum()))
               for a in g["alternative"].unique()}
        lo, hi = cluster_ci(per, rng)
        r = P.dist(g)
        rows.append({"relation": rel, "method": "M6", "cases": len(g), "coverage": float(inside.mean()),
                     "coverage_lo": lo, "coverage_hi": hi,
                     "interval_score": float(np.nanmean(interval_score(g["lo"], g["hi"], g["real_q95"]) / g["floor"])),
                     "median_half_width": float(np.nanmedian((g["hi"] - g["lo"]) / 2 / g["floor"])), **r})
    return pd.DataFrame(rows)


def floor_loao(q: pd.DataFrame, ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """The floor of each geometry recomputed without the held-out alternative's series, and the distances with
    every case scored in that floor: does computing the floors from all series, the held-out one included, leak
    into the distances? A new family is scored in the produced family's floor, which never contains it."""
    import alternatives as A

    qb = A.batches(q)
    ratio = {}
    rows = []
    for geo in ("concave", "convex"):
        sub = A.batch_centres(qb[qb["geometry"] == geo], SHARED)
        for qc in SHARED:
            full = A.floor_from(sub, qc)
            for a in sub.index.get_level_values(0).unique():
                f = A.floor_from(sub.drop(index=a, level=0), qc)
                ratio[(a, qc)] = f / full
                rows.append({"kind": "floor ratio", "relation": geo, "method": qc, "alternative": a,
                             "ratio_loao_to_full": f / full})
    out = ivs.copy()
    own = out["scope"] != "transfer"
    out.loc[own, "floor"] = out.loc[own, "floor"].to_numpy() * np.array(
        [ratio.get((a, c), 1.0) for a, c in zip(out.loc[own, "alternative"], out.loc[own, "qc"])])
    for rel, scope in RELATIONS.items():
        if rel == "new family":
            continue
        for m in rules:
            g0 = ivs[(ivs["scope"] == scope) & (ivs["method"] == m)]
            g1 = out[(out["scope"] == scope) & (out["method"] == m)]
            if g0.empty:
                continue
            r0, r1 = P.dist(g0), P.dist(g1)
            rows.append({"kind": "distances", "relation": rel, "method": m,
                         "resolution_floors": r0["resolution_floors"], "safe_floors": r0["safe_floors"],
                         "resolution_loao": r1["resolution_floors"], "safe_loao": r1["safe_floors"]})
    return pd.DataFrame(rows)


def resolvable_difference() -> pd.DataFrame:
    p = pd.read_csv(RESULTS / "dec_paired.csv")
    point = {"M1", "M1s", "M1n", "M1sn", "NN", "Mc"}
    rows = []
    for scope in ("within", "setting/interpolation", "setting/extrapolation", "setting", "transfer"):
        s = p[p["scope"] == scope]
        for kind, sel in (("point-rule pairs", s["rule_a"].isin(point) & s["rule_b"].isin(point)), ("all pairs", slice(None))):
            h = s[sel] if not isinstance(sel, slice) else s
            if len(h):
                half = (h["resolution_diff_hi"] - h["resolution_diff_lo"]) / 2
                rows.append({"scope": scope, "pairs": kind, "n_pairs": len(h), "median_half_width": float(half.median()),
                             "min_half_width": float(half.min()), "max_half_width": float(half.max())})
    return pd.DataFrame(rows)


def tau_draws(t: pd.DataFrame) -> tuple[dict, dict, np.ndarray]:
    """The between-run draws shared by every rule and the trial: each characteristic's between-series bound
    (as a standard deviation in floors), the position of every alternative and characteristic, and z."""
    mf = pd.read_csv(RESULTS / "meas_floor.csv").set_index("qc")["between_series_q95_floors"]
    tau_bound = (mf / (1.96 * np.sqrt(2))).to_dict()
    alts = sorted(t["alternative"].unique())
    keys = [(a, q) for a in alts for q in SHARED]
    pos = {k: i for i, k in enumerate(keys)}
    rng = np.random.default_rng(SEED + 2)
    return tau_bound, pos, rng.standard_normal((N_TAU_DRAWS, len(keys)))


def between_run_trial(t: pd.DataFrame, q: pd.DataFrame, floors: dict) -> pd.DataFrame:
    """The trial of the first n parts under the same between-run component as the rules: a future run's q95 is
    the observed one plus tau F z, while the trial saw the observed run (the draws of between_run)."""
    tau_bound, pos, Z = tau_draws(t)
    rows = []
    for n in TRIAL_PARTS:
        g = trial_cases(t, q, floors, n)
        idx = np.array([pos[(a, c)] for a, c in zip(g["alternative"], g["qc"])])
        F = g["floor"].to_numpy(float)
        for tau in TAUS + ["bound"]:
            scale = np.array([tau_bound[c] for c in g["qc"]]) if tau == "bound" else float(tau)
            dd, ds = [], []
            for b in range(N_TAU_DRAWS if tau != 0.0 else 1):
                qq = np.maximum(g["real_q95"].to_numpy(float) + scale * F * Z[b, idx], 1e-12)
                r = D.distance_pair(*D.exclusion(g, qq))
                dd.append(r["resolution_floors"])
                ds.append(r["safe_floors"])
            rows.append({"tau": str(tau), "rule": f"trial, first {n} parts", "decisive_median": float(np.median(dd)),
                         "decisive_p05": float(np.percentile(dd, 5)), "decisive_p95": float(np.percentile(dd, 95)),
                         "safe_median": float(np.median(ds))})
    return pd.DataFrame(rows)


def between_run(ivs: pd.DataFrame, t: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """Every truth plus tau F z (z standard normal per alternative and characteristic, common to all rules and
    relations): distances, ranking and guard bands; tau = 'bound' uses each characteristic's between-series bound."""
    tau_bound, pos, Z = tau_draws(t)
    grid = prior_grid(20.0)
    cand = sorted(set(ivs["method"]) - {"M0w"})
    rows = []
    for tau in TAUS + ["bound"]:
        for rel in RELATIONS:
            sub = ivs[(ivs["scope"] == RELATIONS[rel]) & ivs["method"].isin(cand)]
            frames = {m: g for m, g in sub.groupby("method")}
            idx = {m: np.array([pos[(a, q)] for a, q in zip(g["alternative"], g["qc"])]) for m, g in frames.items()}
            scale = {m: (np.array([tau_bound[q] for q in g["qc"]]) if tau == "bound" else float(tau)) for m, g in frames.items()}
            dd = {m: [] for m in frames}
            ds = {m: [] for m in frames}
            bands = {m: [] for m in rules}
            best_nn = []
            draws = N_TAU_DRAWS if tau != 0.0 else 1
            for b in range(draws):
                best, best_m = np.inf, None
                for m, g in frames.items():
                    q = g["real_q95"].to_numpy(float) + scale[m] * g["floor"].to_numpy(float) * Z[b, idx[m]]
                    q = np.maximum(q, 1e-12)            # the characteristics are non-negative
                    r = D.distance_pair(*D.exclusion(g, q))
                    dd[m].append(r["resolution_floors"])
                    ds[m].append(r["safe_floors"])
                    if r["resolution_floors"] < best:
                        best, best_m = r["resolution_floors"], m
                    if m in rules and b < 50:
                        bands[m].append(band_of(g.assign(real_q95=q), grid))
                best_nn.append(best_m)
            for m in frames:
                if m not in rules:
                    continue
                best = pd.Series(best_nn)
                rows.append({"tau": str(tau), "relation": rel, "method": m,
                             "decisive_median": float(np.median(dd[m])), "decisive_p05": float(np.percentile(dd[m], 5)),
                             "decisive_p95": float(np.percentile(dd[m], 95)), "safe_median": float(np.median(ds[m])),
                             "band_median": float(np.median(bands[m])) if bands[m] else np.nan,
                             "share_record_rule_best": float(best.isin(["NN", "M1sn", "M1n"]).mean()),
                             "best_rules": "; ".join(f"{k} {v:.2f}" for k, v in best.value_counts(normalize=True).items())})
    return pd.DataFrame(rows)


WE_TARGET, WE_QC, WE_LIMIT, WE_TRIAL_COST = "concave/300/medium", "drawin_mid", 15.30, 0.05


def worked_example(ivs: pd.DataFrame, q: pd.DataFrame, t: pd.DataFrame) -> pd.DataFrame:
    """The worked example of Section 3.7 with only what the planner knows: the concave cup produced at 100 and
    500 kN, the floor of those six series, the force change they resolve, and the interpolation band and distance
    of the convex family (the concave family's production cannot exercise interpolation); with a stated trial
    cost, the cost-minimising band on the convex cases, never narrower than the 95 % band."""
    import alternatives as A

    rows = []

    def put(name: str, value: float, note: str = "") -> None:
        rows.append({"quantity": name, "value": float(value), "note": note})

    geo, bhf = WE_TARGET.split("/")[0], int(WE_TARGET.split("/")[1])
    produced = sorted(a for a in t["alternative"].unique() if a.startswith(geo + "/") and D.bhf_of(a) != bhf)
    qb = A.batches(q[q["alternative"].isin(produced)])
    F6 = A.floor_from(A.batch_centres(qb, [WE_QC]), WE_QC)
    put("floor of the six produced series (mm)", F6)
    put("floor of all nine series (mm)", float(pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc").loc[WE_QC, f"floor_{geo}"]))
    tt = t[(t["qc"] == WE_QC) & t["alternative"].isin(produced)]
    slopes = []
    for lub, g in tt.groupby("oil_type"):
        c = g.set_index("bhf_kN")["real_centre"]
        slopes.append((c[500] - c[100]) / 400.0)
    mean_slope = (tt[tt["bhf_kN"] == 500]["real_centre"].mean() - tt[tt["bhf_kN"] == 100]["real_centre"].mean()) / 400.0
    put("resolvable force change, mean secant (kN)", F6 / abs(mean_slope))
    put("resolvable force change, per pattern, min (kN)", F6 / max(abs(s) for s in slopes))
    put("resolvable force change, per pattern, max (kN)", F6 / min(abs(s) for s in slopes))
    case = ivs[(ivs["scope"] == "setting/interpolation") & (ivs["alternative"] == WE_TARGET) & (ivs["qc"] == WE_QC)]
    truth = float(case["real_q95"].iloc[0])
    put("true q95 (mm)", truth)
    put("truth below the limit (floors of the six series)", (WE_LIMIT - truth) / F6)
    grid = prior_grid(20.0)
    for m in ["NN", "M7n", "M2", "M5", "M5n", "M1sn", "NN+RM"]:
        r = case[case["method"] == m]
        if r.empty:
            continue
        lo, hi = float(r["lo"].iloc[0]), float(r["hi"].iloc[0])
        conv = relation_cases(ivs, "interpolation", m)
        conv = conv[conv["geometry"] != geo]
        b = band_of(conv, grid)
        put(f"{m}: upper end of the interval (mm)", hi)
        put(f"{m}: margin to the limit (floors)", (WE_LIMIT - hi) / F6)
        put(f"{m}: band of the convex family, interpolation (floors)", b)
        put(f"{m}: margin beyond the band (floors)", (WE_LIMIT - hi) / F6 - b if np.isfinite(b) else -np.inf)
        if m == "NN":
            put("NN: decisive distance of the convex family, interpolation (floors)", P.dist(conv, sides=False)["resolution_floors"])
            own = relation_cases(ivs, "interpolation", m)
            own = own[own["geometry"] == geo]
            o = verdict_outcomes(own, b, grid)
            put("NN: convex band on the concave interpolation cases, share correct", share_correct(o))
            put("NN: convex band on the concave interpolation cases, trial rate", o["trial"] / o["verdicts"])
            outs = [verdict_outcomes(conv, x, grid) for x in COST_BANDS]
            n = outs[0]["verdicts"]
            cost = np.array([(o_["false_accept"] + 0.5 * o_["false_reject"] + WE_TRIAL_COST * o_["trial"]) / n for o_ in outs])
            ok = COST_BANDS >= b
            j = int(np.flatnonzero(ok)[np.argmin(cost[ok])])
            put("NN: cost band, convex family, c_T = 0.05 c_FA (floors)", COST_BANDS[j],
                "cost-minimising band over the reference prior, not narrower than the 95 % band")
            put("NN: margin beyond the cost band (floors)", (WE_LIMIT - hi) / F6 - COST_BANDS[j])
    m0 = ivs[(ivs["method"] == "M0") & (ivs["alternative"] == WE_TARGET) & (ivs["qc"] == WE_QC)]
    put("M0: prediction (mm)", float(m0["lo"].iloc[0]))
    shares, steps = [], []
    for a in sorted(t["alternative"].unique()):
        y = q.loc[q["alternative"] == a, WE_QC].dropna().round(6)
        shares.append(float(y.value_counts(normalize=True).iloc[:3].sum()))
        u = np.unique(y.to_numpy())
        steps.append(float(np.median(np.diff(u))) if u.size > 1 else np.nan)
    put("mid-side draw-in: share of a series in its three most frequent values (median)", float(np.median(shares)))
    put("mid-side draw-in: median step between adjacent values (mm)", float(np.nanmedian(steps)))
    return pd.DataFrame(rows)


# ── 5. selection ─────────────────────────────────────────────────────────────
def cross_fit(ivs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    grid = prior_grid(20.0)
    cand = sorted(set(ivs["method"]) - {"M6"})
    for rel in RELATIONS:
        sub = ivs[ivs["scope"] == RELATIONS[rel]]
        for crit in ("resolution_floors", "safe_floors"):
            for pool_name, pool in (("all rules", cand), ("pre-specified", PRESPECIFIED)):
                for sel_geo, eval_geo in (("concave", "convex"), ("convex", "concave")):
                    score = {}
                    for m in pool:
                        g = sub[(sub["method"] == m) & (sub["geometry"] == sel_geo)]
                        if len(g):
                            score[m] = P.dist(g, sides=False)[crit]
                    if not score:
                        continue
                    pick = min(score, key=score.get)
                    ev = sub[(sub["method"] == pick) & (sub["geometry"] == eval_geo)]
                    best_eval = min(P.dist(sub[(sub["method"] == m) & (sub["geometry"] == eval_geo)], sides=False)[crit]
                                    for m in pool if len(sub[(sub["method"] == m) & (sub["geometry"] == eval_geo)]))
                    rows.append({"relation": rel, "criterion": crit, "pool": pool_name, "selected_on": sel_geo,
                                 "evaluated_on": eval_geo, "rule": pick, "in_sample": score[pick],
                                 "cross_fitted": P.dist(ev, sides=False)[crit], "best_on_evaluation": best_eval})
        # rule and guard band selected on one geometry, applied to the other
        for sel_geo, eval_geo in (("concave", "convex"), ("convex", "concave")):
            best = None
            for m in cand:
                g = sub[(sub["method"] == m) & (sub["geometry"] == sel_geo)]
                if g.empty:
                    continue
                b = band_of(g, grid)
                if not np.isfinite(b):
                    continue
                u, v, cap = D.exclusion(g)
                dd = D.distance_pair(u + b, v + b, cap)["resolution_floors"]
                if best is None or dd < best[2]:
                    best = (m, b, dd)
            if best is None:
                rows.append({"relation": rel, "criterion": "step 6", "pool": "all rules", "selected_on": sel_geo,
                             "evaluated_on": eval_geo, "rule": "none qualifies"})
                continue
            m, b, dd = best
            ev = sub[(sub["method"] == m) & (sub["geometry"] == eval_geo)]
            o = verdict_outcomes(ev, b, grid)
            u, v, cap = D.exclusion(ev)
            rows.append({"relation": rel, "criterion": "step 6", "pool": "all rules", "selected_on": sel_geo,
                         "evaluated_on": eval_geo, "rule": m, "band": b, "in_sample": dd,
                         "cross_fitted": D.distance_pair(u + b, v + b, cap)["resolution_floors"],
                         "share_correct": share_correct(o), "trial_rate": o["trial"] / o["verdicts"]})
    return pd.DataFrame(rows)


def decomposition_prespecified(ivs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    rules = ["M1", "M2", "M3", "M4", "M5"]
    res = []
    for rel, scope in (("sibling", "within"), ("new setting", "setting"), ("new family", "transfer")):
        for m in rules:
            g = ivs[(ivs["scope"] == scope) & (ivs["method"] == m)]
            res.append({"scope": {"sibling": "within", "new setting": "setting", "new family": "transfer"}[rel],
                        "method": m, "qc": "all", **P.dist(g, sides=False)})
    frame = pd.DataFrame(res)
    for r in P.decomposition_of(frame, "pre-specified calibrated rules (M1-M5), produced family's floor"):
        rows.append(r)
    return pd.DataFrame(rows)


# ── 6. per characteristic ────────────────────────────────────────────────────
def per_characteristic(ivs: pd.DataFrame, t: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")["floor"]
    prot = pd.read_csv(RESULTS / "panel_floor_protocol.csv")
    f_over_lt = prot.groupby("qc")["floor_over_sigma_lt"].mean()
    tt = t.set_index(["alternative", "qc"])
    rows = []
    for rel, scope in RELATIONS.items():
        for m in rules:
            g = ivs[(ivs["scope"] == scope) & (ivs["method"] == m)]
            for name, h in list(g.groupby("qc")) + list(g.groupby(g["qc"].map(CLASSES))) + [("all", g)]:
                if h.empty:
                    continue
                r = P.dist(h)
                row = {"relation": rel, "method": m, "subset": name, "cases": len(h), **r}
                if name in QCS:
                    Fp = float(fl.loc[name])
                    ru = P.dist(h, np.full(len(h), Fp), sides=False)
                    cen = np.array([tt.loc[(a, name), "real_centre"] for a in h["alternative"]])
                    sd = np.array([tt.loc[(a, name), "real_sd"] for a in h["alternative"]])
                    dd = r["resolution_floors"]
                    ppk = (h["real_q95"].to_numpy() + dd * h["floor"].to_numpy() - cen) / (3 * sd) if np.isfinite(dd) else np.full(len(h), np.inf)
                    row.update({"unit": QCS[name][1], "pooled_floor": Fp, "decisive_units": ru["resolution_floors"] * Fp,
                                "safe_units": ru["safe_floors"] * Fp,
                                "decisive_sigma_lt": dd * float(f_over_lt.loc[name]) if np.isfinite(dd) else np.inf,
                                "ppk_at_decisive_median": float(np.median(ppk))})
                rows.append(row)
    return pd.DataFrame(rows)


# ── 7. extensions ────────────────────────────────────────────────────────────
def design_level(ivs: pd.DataFrame, rules: list[str]) -> pd.DataFrame:
    """A design meets only if all its characteristics meet. Requirements on every characteristic lie delta floors
    above its truth (adequate design), or one characteristic delta floors below and the others above (a failing
    design, each feasible choice of the failing characteristic weighted equally); both sides weigh equally."""
    grid = D.FINE[D.FINE <= 200]
    rows = []
    for rel, scope in RELATIONS.items():
        for m in rules:
            g = ivs[(ivs["scope"] == scope) & (ivs["method"] == m)]
            if g.empty:
                continue
            correct = np.zeros(grid.size)
            wrong = np.zeros(grid.size)
            weight = np.zeros(grid.size)
            for _, h in g.groupby("alternative"):
                u, v, cap = D.exclusion(h)
                U, V, C = u[:, None], v[:, None], cap[:, None]
                dl = grid[None, :]
                meets_a = U <= dl                       # adequate side, every characteristic at +delta
                fails_a = -V > dl
                all_meet = meets_a.all(axis=0)
                any_fail = fails_a.any(axis=0)
                correct += all_meet
                wrong += any_fail & ~all_meet
                weight += 1.0
                feas = C > dl                           # characteristic j can fail at -delta
                nf = feas.sum(axis=0)
                cf = np.zeros(grid.size)
                wf = np.zeros(grid.size)
                for j in range(len(u)):
                    others = np.delete(np.arange(len(u)), j)
                    fail_j = v[j] < grid                # verdict fails for the failing characteristic
                    meet_j = u[j] <= -grid              # false accept on it
                    o_fail = fails_a[others].any(axis=0)
                    o_meet = meets_a[others].all(axis=0)
                    ok = (fail_j | o_fail) & feas[j]
                    fa = (meet_j & o_meet) & feas[j]
                    cf += ok
                    wf += fa
                with np.errstate(invalid="ignore", divide="ignore"):
                    share = np.where(nf > 0, 1.0 / nf, 0.0)
                correct += cf * share
                wrong += wf * share
                weight += (nf > 0).astype(float)
            kappa, omega = correct / weight, wrong / weight
            dd = D.first_beyond(kappa, grid)
            ds = D.first_beyond(1 - omega, grid)
            marg = P.dist(g, sides=False)
            rows.append({"relation": rel, "method": m, "designs": g["alternative"].nunique(),
                         "design_decisive": dd, "design_safe": ds, "marginal_decisive": marg["resolution_floors"],
                         "marginal_safe": marg["safe_floors"]})
    return pd.DataFrame(rows)


def refit_variant(t_var: pd.DataFrame, floors: dict, label: str, rules: list[str],
                  qcs: list[str] | None = None) -> pd.DataFrame:
    from robustness import fast_intervals

    D._CTX.update(t=t_var, floors=floors)
    iv = fast_intervals(t_var, floors, rules=rules)
    if qcs is not None:
        iv = iv[iv["qc"].isin(qcs)]
    iv = D.with_relation_scopes(iv)
    iv = P.in_produced_floor(iv, floors)
    rows = []
    for rel, scope in RELATIONS.items():
        for m, g in iv[iv["scope"] == scope].groupby("method"):
            rows.append({"variant": label, "relation": rel, "method": m, "cases": len(g), **P.dist(g)})
    return pd.DataFrame(rows)


def block_se(y: np.ndarray, stat, rng: np.random.Generator, n: int = 200) -> float:
    blocks = [y[i:i + D.REF_BLOCK] for i in range(0, len(y), D.REF_BLOCK)]
    if len(blocks) < 2:
        return float(np.std([stat(rng.choice(y, y.size)) for _ in range(n)], ddof=1))
    return float(np.std([stat(np.concatenate([blocks[k] for k in rng.integers(0, len(blocks), len(blocks))]))
                         for _ in range(n)], ddof=1))


def lower_table(t: pd.DataFrame, q: pd.DataFrame) -> pd.DataFrame:
    """Lower limits on the 5th percentile by a change of sign: the truth is q95(-y) = -q05(y), the simulation -s
    (rows of the other characteristics unchanged; they are not scored)."""
    rng = np.random.default_rng(SEED + 3)
    out = t.copy()
    for i, r in out[out["qc"].isin(LOWER_QCS)].iterrows():
        y = -q.loc[q["alternative"] == r["alternative"], r["qc"]].dropna().to_numpy(float)
        stat = lambda v: float(np.quantile(v, D.ADEQUATE_RATE))  # noqa: E731
        out.loc[i, "real_q95"] = stat(y)
        out.loc[i, "real_q95_se"] = block_se(y, stat, rng)
        out.loc[i, "real_centre"] = centre(y)
        out.loc[i, "sim_nominal"] = -r["sim_nominal"]
        out.loc[i, "sim_env_lo"], out.loc[i, "sim_env_hi"] = -r["sim_env_hi"], -r["sim_env_lo"]
    return out


def short_table(t: pd.DataFrame, q: pd.DataFrame, n: int) -> pd.DataFrame:
    rng = np.random.default_rng(SEED + 4 + n)
    out = t.copy()
    for i, r in out.iterrows():
        y = D.transform(r["qc"], q.loc[q["alternative"] == r["alternative"], r["qc"]].dropna().to_numpy(float))[:n]
        stat = lambda v: float(np.quantile(v, D.ADEQUATE_RATE))  # noqa: E731
        out.loc[i, "real_q95"] = stat(y)
        out.loc[i, "real_q95_se"] = float(np.std([stat(rng.choice(y, y.size)) for _ in range(200)], ddof=1))
    return out


def capability_table(t: pd.DataFrame, q: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(SEED + 5)
    out = t.copy()
    k = 3 * PPK_TARGET
    for i, r in out.iterrows():
        y = D.transform(r["qc"], q.loc[q["alternative"] == r["alternative"], r["qc"]].dropna().to_numpy(float))
        stat = lambda v: float(centre(v) + k * np.std(v, ddof=1))  # noqa: E731
        out.loc[i, "real_q95"] = stat(y)
        out.loc[i, "real_q95_se"] = block_se(y, stat, rng)
    return out


# ── main ──────────────────────────────────────────────────────────────────────
def main(only: list[str] | None = None) -> None:
    warnings.simplefilter("ignore", RuntimeWarning)
    d = load()
    iv, ivs, floors, t = d["iv"], d["ivs"], d["floors"], d["t"]
    q = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    guard_rules = ["M1", "M1s", "M2", "M5", "M5n", "NN", "M1sn", "M7n", "M7", "Mcd", "M3", "M4", "NN+RM", "M1sn+RM",
                   "M7n+RM"]
    fast = ["M0", "M1", "M1s", "M2", "M5", "M5n", "NN", "M1sn", "M1n", "M2n"]
    strata, cases = decision_time_strata(iv)

    def variants() -> pd.DataFrame:
        parts = [refit_variant(lower_table(t, q), floors, "lower limits (5th percentile)", fast, LOWER_QCS)]
        for n in SHORT_PARTS:
            parts.append(refit_variant(short_table(t, q, n), floors, f"short runs: first {n} parts", fast))
        parts.append(refit_variant(capability_table(t, q), floors, f"decided statistic: centre + {3 * PPK_TARGET:g} sd", fast))
        parts.append(refit_variant(t, floors, "reference (refitted)", fast))
        return pd.concat(parts, ignore_index=True)

    jobs = {
        "strata": lambda: strata, "strata_cases": lambda: cases,
        "guard_family": lambda: guard_per_family(ivs, guard_rules),
        "guard_oos": lambda: guard_out_of_sample(ivs, ["M2", "M5", "M5n", "NN", "M1sn", "M7n", "M7", "NN+RM"]),
        "guard_prior_width": lambda: guard_prior_width(ivs, guard_rules),
        "guard_characteristic": lambda: guard_per_characteristic(ivs, ["M2", "M5", "NN", "M1sn", "M7n"]),
        "costs": lambda: costs(ivs, ["M0", "M1s", "M2", "M5", "M5n", "NN", "M1sn", "M7n", "M7", "M3", "NN+RM"]),
        "trial": lambda: trial_reference(t, q, floors),
        "coverage": lambda: coverage(ivs, cases),
        "resolvable_difference": resolvable_difference,
        "between_run": lambda: between_run(ivs, t, MAIN + ["M5n", "M7", "M3"]),
        "crossfit": lambda: cross_fit(ivs),
        "decomposition": lambda: decomposition_prespecified(ivs),
        "per_characteristic": lambda: per_characteristic(ivs, t, MAIN + ["M5n", "M7", "M3", "M4"]),
        "design_level": lambda: design_level(ivs, MAIN + ["M5n", "M7", "M3", "M4", "NN+RM"]),
        "variants": variants,
        "m6_coverage": lambda: m6_coverage(t, floors),
        "floor_loao": lambda: floor_loao(q, ivs, MAIN + ["M5n", "M3", "NN+RM"]),
        "guard_decision": lambda: guard_decision_time(ivs, ["M2", "M5", "M5n", "NN", "M1sn", "M7n", "M7", "Mcd", "M3",
                                                            "NN+RM"]),
        "between_run_trial": lambda: between_run_trial(t, q, floors),
        "trial_cost": lambda: trial_cost(t, q, floors),
        "release_capability": release_capability,
        "cost_cheapest": lambda: cost_cheapest(pd.read_csv(RESULTS / "qual_costs.csv")),
        "worked_example": lambda: worked_example(ivs, q, t),
        "guard_nested": lambda: guard_nested_sibling(ivs, t),
    }
    for name, fn in jobs.items():
        if only and name not in only:
            continue
        fn().to_csv(RESULTS / f"qual_{name}.csv", index=False)
        print(f"{name}: written", flush=True)

    lines = ["# Qualification of the rules: strata, guard bands, costs, uncertainty, selection", ""]
    for name in jobs:
        f = RESULTS / f"qual_{name}.csv"
        if name == "strata_cases" or not f.exists():
            continue
        show = pd.read_csv(f)
        if "method" in show and name not in ("crossfit", "trial"):
            show = show[show["method"].isin(MAIN + ["M5n", "M7", "Mcd", "NN+RM", "M3", "M4"])]
        lines += [f"## {name}", "", show.round(3).to_markdown(index=False), ""]
    (RESULTS / "summary_qualify.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or None)
