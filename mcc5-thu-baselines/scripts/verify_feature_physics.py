"""Empirical checks on two feature-construction choices used in the paper.

Both checks answer questions a reader can legitimately raise about the curated
physical-signature features, and both are answered from the released signals
rather than from convention.

1. Band width. Order-domain descriptors integrate spectral energy in a fixed
   +/-0.12 order window around a target order. A fixed *absolute* window is a
   constant *relative* window only at the fundamental: at the second harmonic
   the same 0.12 orders covers half the relative span, while the physical
   deviation of a bearing order (rolling-element slip) scales with the
   harmonic. This measures where the peak actually lands.

2. Broken-bar sideband placement. Descriptors are evaluated at o_e +/- 1 and
   o_e +/- 2, i.e. offsets of one and two *shaft* orders from the electrical
   carrier. The classical broken-bar signature is at (1 +/- 2s) f_e, an offset
   of 2*s*o_e shaft orders. This computes slip per run from the key-phase
   tachometer and compares the two spacings.

Outputs a JSON summary and the per-run measurements as CSV.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from mcc5 import physics
from mcc5.dataset import load_run

FS = physics.FS
SPR = 256          # samples per revolution, matching the paper's resampling
WIN_SEC = 2.0
MAX_WINDOWS = 6    # per run; evenly spaced


def _windows(n_samples: int, win: int, k: int) -> list[tuple[int, int]]:
    if n_samples < win:
        return []
    starts = np.linspace(0, n_samples - win, num=k, dtype=int)
    return [(int(s), int(s) + win) for s in np.unique(starts)]


def _peak_near(orders: np.ndarray, amp: np.ndarray, target: float,
               search: float) -> tuple[float, float]:
    """Highest spectral line within +/-`search` orders of `target`.

    Returns (peak_order, peak_amplitude); (nan, nan) if the window is empty.
    """
    sel = (orders >= target - search) & (orders <= target + search)
    if not sel.any():
        return float("nan"), float("nan")
    idx = np.flatnonzero(sel)
    j = idx[int(np.argmax(amp[idx]))]
    return float(orders[j]), float(amp[j])


def _half_power_width(orders: np.ndarray, amp: np.ndarray, j_center: int,
                      max_span: float) -> float:
    """Width in orders where the power falls to half the peak."""
    if j_center <= 0 or j_center >= len(amp) - 1:
        return float("nan")
    half = (amp[j_center] ** 2) / 2.0
    lo = j_center
    while lo > 0 and amp[lo] ** 2 > half and \
            (orders[j_center] - orders[lo]) < max_span:
        lo -= 1
    hi = j_center
    while hi < len(amp) - 1 and amp[hi] ** 2 > half and \
            (orders[hi] - orders[j_center]) < max_span:
        hi += 1
    return float(orders[hi] - orders[lo])


# Candidate half-widths for the order-integration band, in orders. 0.12 is the
# value used in the paper; the others bracket it.
HALF_WIDTHS = (0.06, 0.12, 0.25, 0.50)

# A window must span this many revolutions for the order resolution (1/n_revs)
# to be fine enough to distinguish these half-widths at all.
MIN_REVS = 30


def _band_ratio(orders: np.ndarray, amp: np.ndarray, center: float,
                half_width: float) -> float:
    """Normalized band energy, as defined in the paper's feature equation."""
    num = (orders >= center - half_width) & (orders <= center + half_width)
    den = (orders >= 0.25) & (orders <= 60.0)
    if not num.any() or not den.any():
        return float("nan")
    return float((amp[num] ** 2).sum() / ((amp[den] ** 2).sum() + 1e-12))


def band_width_check(data_dir: Path, meta: pd.DataFrame) -> pd.DataFrame:
    """Per-run band energy at BPFO/BPFI (H1, H2) for several half-widths.

    Reported per run so that the discriminative value of each half-width can
    be scored against the healthy runs, which is the question that matters:
    not where a peak nominally sits, but whether the integration window is
    wide enough for the descriptor to separate faulty from healthy.

    The peak offset is recorded alongside to explain *why* a width helps.
    """
    families = {"bearing_inner_": ("BPFI", physics.BEARING_ORDERS["BPFI"]),
                "bearing_outer_": ("BPFO", physics.BEARING_ORDERS["BPFO"]),
                "bearing_ball_": ("BSF", physics.BEARING_ORDERS["BSF"])}
    win = int(WIN_SEC * FS)
    rows: list[dict] = []

    for _, r in meta.iterrows():
        if bool(r["is_compound"]):
            continue        # single-fault runs isolate one bearing order
        healthy = r["fault_full"] == "health"
        fam = next((k for k in families if r["fault_full"].startswith(k)), None)
        if fam is None and not healthy:
            continue
        arr = load_run(data_dir, r["npz"])      # (channel, sample)
        kp = arr[0].astype(np.float64)
        vib = arr[2].astype(np.float64)         # vib_de_h
        angle = physics.shaft_angle(kp)
        if len(angle) == 0:
            continue

        per_window: list[dict] = []
        for (a, b) in _windows(len(vib), win, MAX_WINDOWS):
            ang_w = angle[a:b]
            if not np.isfinite(ang_w).all() or \
                    (ang_w[-1] - ang_w[0]) < MIN_REVS:
                continue
            # Envelope-order spectrum: demodulate the resonance band, then
            # order-track (the chain that exposes bearing orders at all).
            o, amp = physics.envelope_order_spectrum(
                vib[a:b], ang_w, samples_per_rev=SPR)
            if len(o) == 0:
                continue
            rec: dict = {"order_resolution": float(o[1] - o[0])}
            for name, o_nom in families.values():
                for h in (1, 2):
                    tgt = o_nom * h
                    for w in HALF_WIDTHS:
                        rec[f"{name}_h{h}_w{w}"] = _band_ratio(o, amp, tgt, w)
                    # Offset of the local maximum, searched only within the
                    # widest candidate band so the statistic stays comparable.
                    pk, _ = _peak_near(o, amp, tgt, max(HALF_WIDTHS))
                    rec[f"{name}_h{h}_offset"] = \
                        abs(pk - tgt) if np.isfinite(pk) else np.nan
            per_window.append(rec)

        if not per_window:
            continue
        agg = pd.DataFrame(per_window).median(numeric_only=True).to_dict()
        agg.update({"file": Path(r["file"]).stem, "fault": r["fault_full"],
                    "condition": r["condition"], "healthy": healthy,
                    "family": "healthy" if healthy else families[fam][0],
                    "n_windows": len(per_window)})
        rows.append(agg)
    return pd.DataFrame(rows)


def _auroc(pos: np.ndarray, neg: np.ndarray) -> float:
    """Rank-based AUROC; ties contribute 0.5."""
    pos = pos[np.isfinite(pos)]
    neg = neg[np.isfinite(neg)]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    allv = np.concatenate([pos, neg])
    ranks = pd.Series(allv).rank().to_numpy()
    r_pos = ranks[:len(pos)].sum()
    return float((r_pos - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def band_width_auroc(bw: pd.DataFrame) -> pd.DataFrame:
    """Does a wider integration band make the descriptor more diagnostic?"""
    pairs = [("BPFO", "BPFO"), ("BPFI", "BPFI"), ("BSF", "BSF")]
    healthy = bw[bw["healthy"]]
    out: list[dict] = []
    for fam, name in pairs:
        faulty = bw[bw["family"] == fam]
        if faulty.empty:
            continue
        for h in (1, 2):
            for w in HALF_WIDTHS:
                col = f"{name}_h{h}_w{w}"
                out.append({
                    "family": fam, "harmonic": h, "half_width": w,
                    "n_faulty": int(len(faulty)), "n_healthy": int(len(healthy)),
                    "auroc": _auroc(faulty[col].to_numpy(),
                                    healthy[col].to_numpy()),
                })
    return pd.DataFrame(out)


def _carrier_order(o: np.ndarray, amps: list[np.ndarray]) -> tuple[float, int]:
    """Dominant electrical order from summed three-phase energy, 0.5-30."""
    tot = np.zeros_like(amps[0])
    for a in amps:
        tot = tot + a ** 2
    sel = (o >= 0.5) & (o <= 30.0)
    if not sel.any():
        return float("nan"), -1
    idx = np.flatnonzero(sel)
    j = idx[int(np.argmax(tot[idx]))]
    return float(o[j]), int(j)


def infer_pole_pairs(carrier_orders: np.ndarray) -> int:
    """Pole pairs from the carrier order itself.

    o_e = f_e/f_r and f_r = (1-s) f_e / p, so o_e = p/(1-s): with the few
    percent of slip an induction motor actually runs at, o_e sits just above
    the integer p. Worth inferring rather than reading off a table: the
    descriptor lists "poles of pair 2", and the measured carrier (50.06 Hz
    supply against a 49.69 Hz shaft at the 3000 rpm setting) shows that this
    means two poles, i.e. one pole pair.
    """
    med = float(np.nanmedian(carrier_orders))
    return max(int(round(med)), 1)


def slip_sideband_check(data_dir: Path, meta: pd.DataFrame,
                        pole_pairs: int | None) -> pd.DataFrame:
    """Slip per run, and where the (1+/-2s) sidebands sit versus o_e +/- 1."""
    win = int(WIN_SEC * FS)
    keep = meta["fault_full"].str.startswith(("broken_bar", "health"))
    rows: list[dict] = []

    for _, r in meta[keep].iterrows():
        arr = load_run(data_dir, r["npz"])      # (channel, sample)
        kp = arr[0].astype(np.float64)
        cur = [arr[5].astype(np.float64), arr[6].astype(np.float64),
               arr[7].astype(np.float64)]
        angle = physics.shaft_angle(kp)
        if len(angle) == 0:
            continue
        rpm = physics.speed_series(kp)

        for (a, b) in _windows(len(kp), win, MAX_WINDOWS):
            ang_w = angle[a:b]
            if not np.isfinite(ang_w).all() or (ang_w[-1] - ang_w[0]) < 10:
                continue
            spec = [physics.order_spectrum(c[a:b], ang_w, samples_per_rev=SPR)
                    for c in cur]
            o = spec[0][0]
            if len(o) == 0:
                continue
            o_e, j_e = _carrier_order(o, [s[1] for s in spec])
            if not np.isfinite(o_e) or o_e <= 0:
                continue
            f_r = float(np.nanmean(rpm[a:b])) / 60.0 if len(rpm) else np.nan
            rows.append({
                "file": Path(r["file"]).stem,
                "fault": r["fault_full"],
                "condition": r["condition"],
                "shaft_hz": f_r,
                "supply_hz": o_e * f_r if np.isfinite(f_r) else np.nan,
                "carrier_order": o_e,
                # the offset actually used by the o_e +/- 1 descriptors
                "descriptor_offset_orders": 1.0,
                "order_resolution": float(o[1] - o[0]) if len(o) > 1 else np.nan,
            })

    df = pd.DataFrame(rows)
    if df.empty:
        return df
    p = pole_pairs if pole_pairs else infer_pole_pairs(df["carrier_order"])
    # o_e = f_e/f_r and the synchronous shaft order is p, so s = 1 - p/o_e.
    df["pole_pairs"] = p
    df["slip"] = 1.0 - p / df["carrier_order"]
    # classical broken-bar sideband offset (1 +/- 2s)f_e, in shaft orders
    df["bb_offset_orders"] = (2.0 * df["slip"] * df["carrier_order"]).abs()
    return df


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--pole-pairs", type=int, default=None,
                    help="override; inferred from the carrier order if unset")
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    summary: dict = {"samples_per_rev": SPR, "window_sec": WIN_SEC}

    bw = band_width_check(args.data_dir, meta)
    bw.to_csv(args.out_dir / "band_width_check.csv", index=False)
    if bw.empty:
        raise SystemExit("band-width check produced no rows; check channel "
                         "layout and key-phase parsing")
    auc = band_width_auroc(bw)
    auc.to_csv(args.out_dir / "band_width_auroc.csv", index=False)
    summary["band_width"] = {
        "n_runs": int(len(bw)),
        "n_healthy_runs": int(bw["healthy"].sum()),
        "median_order_resolution": float(bw["order_resolution"].median()),
        "min_revs_per_window": MIN_REVS,
        "auroc": {
            f"{r.family}_h{r.harmonic}_w{r.half_width}": round(float(r.auroc), 4)
            for r in auc.itertuples()
        },
    }
    for fam in ("BPFO", "BPFI"):
        for h in (1, 2):
            col = f"{fam}_h{h}_offset"
            sub = bw[(bw["family"] == fam) & bw[col].notna()]
            if not sub.empty:
                summary["band_width"][f"{fam}_h{h}_median_peak_offset"] = \
                    float(sub[col].median())
                summary["band_width"][f"{fam}_h{h}_frac_offset_within_0.12"] = \
                    float((sub[col] <= 0.12).mean())

    sl = slip_sideband_check(args.data_dir, meta, args.pole_pairs)
    sl.to_csv(args.out_dir / "slip_sideband_check.csv", index=False)
    if not sl.empty:
        bar = sl[sl["fault"].str.startswith("broken_bar")]
        by_speed = {}
        rpm_tag = sl["condition"].str.extract(r"(\d+)rpm")[0]
        for tag, sub in sl.groupby(rpm_tag):
            by_speed[f"{tag}rpm"] = {
                "median_shaft_hz": round(float(sub["shaft_hz"].median()), 3),
                "median_supply_hz": round(float(sub["supply_hz"].median()), 3),
                "median_slip": round(float(sub["slip"].median()), 5),
                "median_bb_offset_orders": round(
                    float(sub["bb_offset_orders"].median()), 5),
            }
        summary["slip"] = {
            "n": int(len(sl)),
            "pole_pairs_used": int(sl["pole_pairs"].iloc[0]),
            "by_speed": by_speed,
            "median_carrier_order": float(sl["carrier_order"].median()),
            "median_slip": float(sl["slip"].median()),
            "slip_iqr": [float(sl["slip"].quantile(0.25)),
                         float(sl["slip"].quantile(0.75))],
            "median_supply_hz": float(sl["supply_hz"].median()),
            "median_bb_offset_orders": float(sl["bb_offset_orders"].median()),
            "bb_offset_iqr": [float(sl["bb_offset_orders"].quantile(0.25)),
                              float(sl["bb_offset_orders"].quantile(0.75))],
            "frac_bb_offset_within_0.12": float(
                (sl["bb_offset_orders"] <= 0.12).mean()),
            "median_slip_broken_bar_runs": (
                float(bar["slip"].median()) if not bar.empty else None),
            "median_bb_offset_broken_bar_runs": (
                float(bar["bb_offset_orders"].median())
                if not bar.empty else None),
        }

    (args.out_dir / "feature_physics.json").write_text(
        json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
