"""Production resolution floor and effect-to-scatter ratios between alternatives.

Each of the 18 alternatives (geometry x blank-holder force x lubrication) was
run as one series of 500 consecutive parts. The series is cut into batches of
BATCH consecutive parts; a batch with fewer than MIN_FILL * BATCH valid values
is dropped. Centres of batches and alternatives are 10 % trimmed means
(common.centre). For every quality characteristic (QC):

* the production floor F is the ALPHA-quantile of |m_i - m_j| over all pairs
  of batch centres within the same alternative, pooled over alternatives. It
  is what drift and scatter alone produce between two batches of one design;
* the effect between two alternatives is the difference of their centres; the
  effect-to-scatter ratio ESR = |effect| / F. ESR >= 1 means the difference is
  larger than what the same design shows between two of its own batches;
* the minimum resolvable change of a continuous factor (blank-holder force;
  measured oil film, sheet thickness and punch temperature within a series)
  is F divided by the sensitivity of the QC to that factor.

Uncertainty: batches are resampled within alternatives (N_BOOT, seed SEED);
the floor, effects, ratios and sensitivities are recomputed on each replicate.

Outputs: results/alt_floor.csv, alt_effects.csv, alt_mrc.csv, summary_alternatives.md
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS, group_centres  # noqa: E402
from qc import QCS, parts_qc  # noqa: E402

BATCH = 50
MIN_FILL = 0.8
ALPHA = 0.95
N_BOOT = 2000
SEED = 1
FACTORS = {  # contrast family -> (factor column, ordered levels)
    "bhf": ("bhf_kN", [100, 300, 500]),
    "lubrication": ("oil_type", ["coarse", "medium", "fine"]),
    "geometry": ("geometry", ["concave", "convex"]),
}


def batches(q: pd.DataFrame, size: int = BATCH) -> pd.DataFrame:
    q = q.copy()
    q["batch"] = (q.groupby("alternative").cumcount() // size).astype(int)
    return q


def batch_centres(q: pd.DataFrame, qcs: list[str], size: int = BATCH, stat: str = "trim") -> pd.DataFrame:
    """Centre of each batch and QC; NaN where the batch holds fewer than MIN_FILL * size valid values."""
    g = q.groupby(["alternative", "batch"])[qcs]
    c = g.median() if stat == "median" else group_centres(q, ["alternative", "batch"], qcs)
    return c.where(g.count() >= MIN_FILL * size)


def floor_from(bm: pd.DataFrame, qc: str, alpha: float = ALPHA) -> float:
    diffs = []
    for _, g in bm[qc].groupby(level=0):
        v = g.dropna().to_numpy()
        if v.size >= 2:
            i, j = np.triu_indices(v.size, 1)
            diffs.append(np.abs(v[i] - v[j]))
    return float(np.quantile(np.concatenate(diffs), alpha)) if diffs else np.nan


def contrasts(alts: list[str]) -> list[tuple[str, str, str]]:
    """Pairs of alternatives that differ in exactly one factor."""
    parts = {a: dict(zip(["geometry", "bhf_kN", "oil_type"], a.split("/"))) for a in alts}
    out = []
    for a, b in itertools.combinations(alts, 2):
        diff = [k for k in parts[a] if parts[a][k] != parts[b][k]]
        if len(diff) == 1:
            fam = {"geometry": "geometry", "bhf_kN": "bhf", "oil_type": "lubrication"}[diff[0]]
            out.append((fam, a, b))
    return out


def within_slope(q: pd.DataFrame, qc: str, x: str, min_n: int = 20) -> float:
    """Pooled within-alternative slope of a QC on a measured covariate (alternatives with >= min_n parts)."""
    y, xv = q[qc].to_numpy(dtype=float), q[x].to_numpy(dtype=float)
    ok = np.isfinite(y) & np.isfinite(xv)
    codes = pd.factorize(q["alternative"])[0][ok]
    y, xv = y[ok], xv[ok]
    n = np.bincount(codes)
    use = (n >= min_n)[codes]
    xc = xv - (np.bincount(codes, xv) / np.maximum(n, 1))[codes]
    yc = y - (np.bincount(codes, y) / np.maximum(n, 1))[codes]
    den = float(np.sum(xc[use] ** 2))
    return float(np.sum(xc[use] * yc[use])) / den if den > 0 else np.nan


def bhf_slope(cell_med: pd.DataFrame, qc: str) -> float:
    """Pooled slope of the cell centres on blank-holder force (per kN) within geometry x lubrication."""
    slopes = []
    for _, g in cell_med.groupby(["geometry", "oil_type"]):
        g = g[["bhf_kN", qc]].dropna()
        if len(g) >= 2:
            slopes.append(np.polyfit(g["bhf_kN"].astype(float), g[qc], 1)[0])
    return float(np.mean(slopes)) if slopes else np.nan


def analyse(q: pd.DataFrame, qcs: list[str], alpha: float = ALPHA, size: int = BATCH, stat: str = "trim") -> dict:
    bm = batch_centres(q, qcs, size, stat)
    floors = {c: floor_from(bm, c, alpha) for c in qcs}
    med = q.groupby("alternative")[qcs].median() if stat == "median" else group_centres(q, "alternative", qcs)
    effects = []
    for fam, a, b in contrasts(sorted(med.index)):
        for c in qcs:
            e = med.loc[b, c] - med.loc[a, c]
            effects.append({"family": fam, "a": a, "b": b, "qc": c, "effect": e, "esr": abs(e) / floors[c]})
    keys = ["alternative", "geometry", "bhf_kN", "oil_type"]
    cell = (q.groupby(keys)[qcs].median() if stat == "median" else group_centres(q, keys, qcs)).reset_index()
    mrc = []
    for c in qcs:
        s_bhf = bhf_slope(cell, c)
        mrc.append({"qc": c, "factor": "bhf_kN", "slope": s_bhf, "mrc": floors[c] / abs(s_bhf)})
        for x in ["oil_gm2", "sheet_um", "punch_temp_C"]:
            s = within_slope(q, c, x)
            mrc.append({"qc": c, "factor": x, "slope": s, "mrc": floors[c] / abs(s) if s else np.nan})
    return {"floors": floors, "effects": pd.DataFrame(effects), "mrc": pd.DataFrame(mrc)}


def bootstrap(q: pd.DataFrame, qcs: list[str], n_boot: int, seed: int) -> list[dict]:
    rng = np.random.default_rng(seed)
    groups = {k: g for k, g in q.groupby(["alternative", "batch"])}
    alts = q["alternative"].unique()
    nb = q.groupby("alternative")["batch"].nunique()
    reps = []
    for _ in range(n_boot):
        pieces = []
        for a in alts:
            for new_b, b in enumerate(rng.integers(0, nb[a], nb[a])):
                g = groups[(a, int(b))].copy()
                g["batch"] = new_b
                pieces.append(g)
        reps.append(analyse(pd.concat(pieces, ignore_index=True), qcs))
    return reps


def main() -> None:
    f = pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False)
    q = batches(parts_qc(f))
    qcs = list(QCS)
    n_parts = q.groupby("alternative").size()
    base = analyse(q, qcs)
    n_boot = N_BOOT if n_parts.min() >= 400 else 200     # partial data: quick check only
    reps = bootstrap(q, qcs, n_boot, SEED)

    fl = pd.DataFrame({"qc": qcs})
    fl["label"] = [QCS[c][0] for c in qcs]
    fl["unit"] = [QCS[c][1] for c in qcs]
    fl["floor"] = [base["floors"][c] for c in qcs]
    boot_fl = np.array([[r["floors"][c] for c in qcs] for r in reps])
    fl["floor_lo"], fl["floor_hi"] = np.nanpercentile(boot_fl, 2.5, axis=0), np.nanpercentile(boot_fl, 97.5, axis=0)
    for geo in ["concave", "convex"]:
        sub = batch_centres(q[q["geometry"] == geo], qcs)
        fl[f"floor_{geo}"] = [floor_from(sub, c) for c in qcs]
    fl["sd_within"] = [q.groupby("alternative")[c].std().median() for c in qcs]
    fl.to_csv(RESULTS / "alt_floor.csv", index=False)

    eff = base["effects"].copy()
    be = np.stack([r["effects"]["esr"].to_numpy() for r in reps])
    eff["esr_lo"], eff["esr_hi"] = np.percentile(be, 2.5, axis=0), np.percentile(be, 97.5, axis=0)
    eff["p_resolvable"] = (be >= 1.0).mean(axis=0)
    eff.to_csv(RESULTS / "alt_effects.csv", index=False)

    mrc = base["mrc"].copy()
    bm_ = np.stack([r["mrc"]["mrc"].to_numpy() for r in reps])
    mrc["mrc_lo"], mrc["mrc_hi"] = np.nanpercentile(bm_, 2.5, axis=0), np.nanpercentile(bm_, 97.5, axis=0)
    mrc.to_csv(RESULTS / "alt_mrc.csv", index=False)

    lines = ["# Production floor and effects between alternatives", "",
             f"Parts per alternative: {n_parts.min()}-{n_parts.max()}; batch size {BATCH} (batches below "
             f"{MIN_FILL:.0%} valid dropped); centres: 10 % trimmed means; alpha {ALPHA}; "
             f"bootstrap {n_boot} (seed {SEED}).", "", "## Floor per characteristic", "",
             fl.round(4).to_markdown(index=False), "", "## Share of single-factor contrasts with ESR >= 1", ""]
    share = eff.assign(res=eff["esr"] >= 1).groupby(["qc", "family"])["res"].mean().unstack().round(2)
    lines += [share.to_markdown(), "", "## Minimum resolvable change", "", mrc.round(4).to_markdown(index=False)]
    (RESULTS / "summary_alternatives.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
