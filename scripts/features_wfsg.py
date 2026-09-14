"""Feature extraction for the third alternative: the variable-speed wound-field synchronous generator
(InnovaPower Generators-Dataset, bench C: 2 kVA, 4 salient poles, 3L-NPC converter, FOC, 4 kHz).

Harmonised to the PMSG/SCIG pipeline: the same tap-pair map (identical derivation percentages), the same
window features where the measurement exists, the same segment logic (pre-fault split into two halves,
fault interval located from the measured fault current). Differences that cannot be harmonised are kept
explicit: 4 kHz instead of 20 kHz, ~0.55 s pre-fault and ~0.27 s fault instead of 1.0 s / 0.40 s, no PI
actions and no torque transducer, a wound field (field current is an extra observable), operating points
given as electrical speed (rad/s) and torque reference (p.u.), several fault impedances, repetitions.

Usage: python scripts/features_wfsg.py [--ncyc 3] [--zf 2.83|all] [--workers N]
"""
import argparse
import os
import re
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

from features import DPOS, FEATURES, fundamental, phasor, window_features

ROOT = Path("data/mitdev/Generators-Dataset/GEN_2KVA_4_SALIENT_POLES_VARIABLE_SPEED")
OUT = Path("results")
POLE_PAIRS = 2
PAT = re.compile(r"^FAULT_GER_TYPE_(?P<ftype>[A-Z]+?)(?:_(?P<phase>[A-C]))?_POS_(?P<d1>D\d\d)_(?P<d2>D\d\d)"
                 r"_ZF_(?P<zf>[\d.]+)_TRQ_(?P<trq>[\d.]+)_SPD_(?P<spd>\d+)_ID_(?P<id>\d+)\.csv$")
TYPE_MAP = {"INTERTURN": "TURNS", "INTERBRANCH": "WINDINGS", "AB": "PHASE", "AC": "PHASE"}
HOP = 1
PRE_START, PRE_SPLIT = 0.05, 0.30      # s after the start of the record
FLT_MARGIN, POST_OFFSET = (0.03, 0.01), 0.15
EXTRA = ["If_2fe", "If_std"]           # wound-field observables not present in the PMSG/SCIG sets
DROP = ["PId_2fe", "PIq_2fe", "PId_std", "PIq_std", "Tm_std", "Tm_2fe", "Tm_1fe"]   # not measured on bench C


def parse(name):
    m = PAT.match(name)
    if not m:
        raise ValueError(name)
    d = m.groupdict()
    d1, d2 = sorted([d["d1"], d["d2"]])
    ftype = TYPE_MAP[d["ftype"]]
    (p1, x1), (p2, x2) = DPOS[d1], DPOS[d2]
    return dict(case=f"{ftype}_{d1}_{d2}", ftype=ftype, d1=d1, d2=d2, sev_pct=abs(x1 - x2), phases=p1 + p2,
                speed_rpm=int(round(int(d["spd"]) / POLE_PAIRS * 60 / (2 * np.pi))), torque_Nm=np.nan,
                torque_pu=float(d["trq"]), speed_rad_s=int(d["spd"]), zf_ohm=float(d["zf"]), rep=int(d["id"]))


def park(va, vb, vc, theta):
    """dq components of a three-phase set for electrical angle theta (amplitude-invariant)."""
    d = (2 / 3) * (va * np.cos(theta) + vb * np.cos(theta - 2 * np.pi / 3) + vc * np.cos(theta + 2 * np.pi / 3))
    q = -(2 / 3) * (va * np.sin(theta) + vb * np.sin(theta - 2 * np.pi / 3) + vc * np.sin(theta + 2 * np.pi / 3))
    return d, q


def load(path):
    df = pd.read_csv(path)
    df.columns = [c.split("-", 1)[1] if "-" in c else c for c in df.columns]
    t = df["Time"].to_numpy() - df["Time"].iloc[0]
    g = lambda k: df[k].to_numpy(dtype=float)
    theta = g("Ang_enc_cur")
    vd, vq = park(g("Va_conv_gen"), g("Vb_conv_gen"), g("Vc_conv_gen"), theta)
    omega_m = g("Electric_Omega") / POLE_PAIRS
    sig = {
        "Ia": g("Ia_gen"), "Ib": g("Ib_gen"), "Ic": g("Ic_gen"),
        "Va": g("Va_conv_gen"), "Vb": g("Vb_conv_gen"), "Vc": g("Vc_conv_gen"),
        "Da": g("ma_gen"), "Db": g("mb_gen"), "Dc": g("mc_gen"),
        "Id": g("Id_gen"), "Iq": g("Iq_gen"), "Vd": vd, "Vq": vq,
        "Vd_conv": g("Vd_gen"), "Vq_conv": g("Vq_gen"),
        "Action_pi_d": np.zeros(len(t)), "Action_pi_q": np.zeros(len(t)),
        "Torq_ele": g("P_gen") / np.where(np.abs(omega_m) > 1, omega_m, np.nan),
        "Torq_mec": np.zeros(len(t)),
        "Spd": g("Electric_Omega"), "Vdc": g("G_V_LinkDC"), "Ifault": g("I_fault"), "If": g("If_gend"),
    }
    sig["Torq_ele"] = np.nan_to_num(sig["Torq_ele"])
    return t, sig


def process_file(args):
    path, ncyc = args
    meta = parse(path.name)
    t, sig = load(path)
    fs = 1.0 / np.median(np.diff(t))
    ifault = sig["Ifault"]
    quiet = (t >= PRE_START) & (t <= 0.40)
    thr = max(0.3, 6 * np.std(ifault[quiet]))
    # 10 ms moving RMS of the fault current; the fault interval is the first contiguous run above threshold
    n10 = max(1, int(round(0.010 * fs)))
    rms10 = np.sqrt(np.convolve(ifault ** 2, np.ones(n10) / n10, mode="same"))
    hot = np.flatnonzero((rms10 > thr) & (t > 0.40))
    if len(hot) < 10:
        return None, dict(machine="WFSG", file=path.name, **meta, skipped="no fault current above threshold")
    t_on = t[hot[0]]
    after = np.flatnonzero((rms10 < thr) & (t > t_on + 0.05))
    t_off = t[after[0]] if len(after) else t[hot[-1]]
    pre_idx = (t >= PRE_START) & (t < t_on - 0.01)
    fe0, rot = fundamental(sig["Ia"][pre_idx], sig["Ib"][pre_idx], sig["Ic"][pre_idx], fs)
    nwin = int(round(ncyc * fs / fe0))
    nhop = int(round(HOP * fs / fe0))
    segments = {"PRE": (PRE_START, t_on - 0.01), "FLT": (t_on + FLT_MARGIN[0], t_off - FLT_MARGIN[1]),
                "POST": (t_off + POST_OFFSET, t[-1] - 0.01)}
    rows = []
    for segname, (a, b) in segments.items():
        i0, i_end = int(np.searchsorted(t, a)), int(np.searchsorted(t, b))
        for start in range(i0, i_end - nwin + 1, nhop):
            seg = {k: v[start:start + nwin] for k, v in sig.items()}
            f = window_features(seg, fs, fe0, rot)
            x = seg["If"] - seg["If"].mean()
            f["If_2fe"] = abs(phasor(x, 2 * f["fe_Hz"], fs, np.hanning(nwin)))
            f["If_std"] = np.std(x)
            for k in DROP:
                f.pop(k, None)
            f.update(machine="WFSG", file=path.name, segment=segname, t_start=t[start], **meta)
            rows.append(f)
    df = pd.DataFrame(rows)
    pre, flt = df[df.segment == "PRE"], df[df.segment == "FLT"]
    summary = dict(machine="WFSG", file=path.name, **meta, fs=fs, fe0_Hz=fe0, rotation=int(rot), t_on=t_on, t_off=t_off,
                   fault_duration_s=t_off - t_on, n_pre=len(pre), n_flt=len(flt),
                   Ifault_rms_flt=np.sqrt(np.mean(flt["Ifault_rms"] ** 2)) if len(flt) else np.nan,
                   I1_pre=pre["I1"].mean(), I1_flt=flt["I1"].mean() if len(flt) else np.nan)
    for feat in [f for f in FEATURES if f not in DROP] + EXTRA:
        x, y = pre[feat].to_numpy(), flt[feat].to_numpy()
        x, y = x[np.isfinite(x)], y[np.isfinite(y)]
        if len(x) < 3 or len(y) < 3:
            continue
        summary[f"{feat}__pre"], summary[f"{feat}__flt"] = x.mean(), y.mean()
        summary[f"{feat}__rel"] = (y.mean() - x.mean()) / abs(x.mean()) if x.mean() != 0 else np.nan
        u = mannwhitneyu(y, x, alternative="two-sided").statistic
        summary[f"{feat}__auc"] = u / (len(x) * len(y))
    return df, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--ncyc", type=int, default=3)
    ap.add_argument("--zf", default="2.83", help="fault impedance to keep (e.g. 2.83) or 'all'")
    ap.add_argument("--suffix", default="")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    files = sorted(ROOT.glob("FAULT_*.csv"))
    if args.zf != "all":
        files = [p for p in files if f"_ZF_{args.zf}_" in p.name]
    if args.limit:
        files = files[: args.limit]
    print(f"{len(files)} files, ncyc={args.ncyc}, {args.workers} workers")
    windows, summaries, skipped = [], [], []
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        for i, (df, s) in enumerate(ex.map(process_file, [(p, args.ncyc) for p in files], chunksize=4), 1):
            if df is None:
                skipped.append(s)
            else:
                windows.append(df)
                summaries.append(s)
            if i % 100 == 0 or i == len(files):
                print(f"  {i}/{len(files)} done", flush=True)
    win = pd.concat(windows, ignore_index=True)
    fl = pd.DataFrame(summaries)
    win.to_csv(OUT / f"features_wfsg_windows{args.suffix}.csv.gz", index=False)
    fl.to_csv(OUT / f"features_wfsg_files{args.suffix}.csv", index=False)
    print("windows:", win.shape, "files:", fl.shape, "skipped:", len(skipped))
    if skipped:
        pd.DataFrame(skipped).to_csv(OUT / f"features_wfsg_skipped{args.suffix}.csv", index=False)
    print(fl.groupby(["ftype"]).size())
    print("fault duration s: median", fl.fault_duration_s.median().round(3), "min", fl.fault_duration_s.min().round(3),
          "max", fl.fault_duration_s.max().round(3))
    print("n_flt windows: median", fl.n_flt.median(), "min", fl.n_flt.min())


if __name__ == "__main__":
    main()
