"""Stator-side feature extraction for the PMSG vs SCIG comparison (InnovaPower MitDev-Eletrica).

Every recording is 3 s at 20 kHz: ~1 s healthy, a 400 ms short-circuit (contactor commanded at
t = 1.000 s), then recovery. Features are computed on sliding windows of NCYC electrical cycles in
three segments (PRE, FLT, POST) so that every file acts as its own control. Only signals a real
installation could observe are used as features; `Ifault` and `Fault_relay` are ground truth.

Outputs (results/):
  features_windows.csv.gz  one row per (file, window)
  features_files.csv       one row per file with PRE-vs-FLT effect sizes per feature

Usage: python scripts/features.py [--workers N]
"""
import argparse
import os
import re
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.io import loadmat
from scipy.stats import mannwhitneyu

ROOT = Path("data/mitdev")
OUT = Path("results")
MACHINES = {"PMSG": ROOT / "PMSG-3phase-Dataset", "SCIG": ROOT / "SCIG-3phase-Dataset"}

# Winding derivation points: phase and % distance from the neutral (PMSG paper, Table 3). The SCIG
# paper states its derivations are identical to the PMSG's.
DPOS = {
    "D01": ("A", 0.460), "D02": ("B", 2.310), "D03": ("B", 10.000), "D04": ("A", 12.500),
    "D05": ("C", 12.900), "D06": ("A", 14.800), "D07": ("A", 22.200), "D08": ("C", 25.000),
    "D09": ("A", 29.600), "D10": ("A", 32.400), "D11": ("A", 42.200), "D12": ("A", 44.900),
    "D13": ("A", 50.000), "D14": ("B", 52.300), "D15": ("B", 59.700), "D16": ("A", 61.600),
    "D17": ("C", 62.500), "D18": ("A", 64.800), "D19": ("A", 72.200), "D20": ("C", 74.100),
    "D21": ("A", 78.600), "D22": ("A", 82.400), "D23": ("A", 92.100), "D24": ("A", 94.900),
}

NCYC = 5          # window length, electrical cycles
HOP = 1           # hop, electrical cycles
PRE = (0.30, 0.98)            # healthy segment before the relay command
FLT_MARGIN = (0.03, 0.01)     # skip after relay ON / before relay OFF
POST = (0.30, 2.98)           # offset after relay OFF, absolute end
IFAULT_ONSET_A = 0.5          # threshold used to time the fault-current onset
A = np.exp(2j * np.pi / 3)

PAT = re.compile(
    r"^(?P<state>FAULT|HEALTHY)(?:_(?P<ftype>TURNS|WINDINGS)_(?P<d1>D\d\d)_(?P<d2>D\d\d))?"
    r"(?:_R(?P<r>\d+))?_S(?P<spd>\d+)_T(?P<trq>\d+)\.mat$"
)

# Features that a monitoring system could compute from stator-side / controller signals.
FEATURES = [
    "fe_Hz", "I1", "I2", "I2_I1", "I0_I1", "I_unbal_rms",
    "V1", "V2_V1", "D2_D1",
    "Id_std", "Iq_std", "Id_2fe", "Iq_2fe", "Id_1fe", "Iq_1fe",
    "Vd_2fe", "Vq_2fe", "Vdconv_2fe", "Vqconv_2fe", "PId_2fe", "PIq_2fe", "PId_std", "PIq_std",
    "Te_std", "Te_2fe", "Te_1fe", "Tm_std", "Tm_2fe", "Tm_1fe",
    "Ia_h3", "Ia_h5", "Ia_h7", "Ia_thd",
    "Spd_std", "Vdc_std",
]


def parse(name: str):
    m = PAT.match(name)
    if not m:
        raise ValueError(name)
    d = m.groupdict()
    if d["state"] == "HEALTHY":
        return dict(case="HEALTHY", ftype="HEALTHY", d1=None, d2=None, sev_pct=0.0, phases="",
                    speed_rpm=int(d["spd"]), torque_Nm=int(d["trq"]) / 10)
    p1, x1 = DPOS[d["d1"]]
    p2, x2 = DPOS[d["d2"]]
    return dict(case=f"{d['ftype']}_{d['d1']}_{d['d2']}", ftype=d["ftype"], d1=d["d1"], d2=d["d2"],
                sev_pct=abs(x1 - x2), phases=p1 + p2, speed_rpm=int(d["spd"]), torque_Nm=int(d["trq"]) / 10)


def phasor(x, f, fs, win):
    """Complex amplitude of x at frequency f (Hann-windowed projection)."""
    n = np.arange(len(x))
    return 2.0 * np.sum(x * win * np.exp(-2j * np.pi * f * n / fs)) / np.sum(win)


def fundamental(ia, ib, ic, fs):
    """Electrical frequency and rotation sign from the current space vector's phase slope."""
    s = (2.0 / 3.0) * (ia + A * ib + A * A * ic)
    ph = np.unwrap(np.angle(s))
    t = np.arange(len(ph)) / fs
    slope = np.polyfit(t, ph, 1)[0]
    return abs(slope) / (2 * np.pi), np.sign(slope)


def sequences(pa, pb, pc, rot):
    """Zero / positive / negative sequence magnitudes for the measured phase rotation."""
    s0 = (pa + pb + pc) / 3
    s_abc = (pa + A * pb + A * A * pc) / 3
    s_acb = (pa + A * A * pb + A * pc) / 3
    pos, neg = (s_abc, s_acb) if rot > 0 else (s_acb, s_abc)
    return abs(s0), abs(pos), abs(neg)


def window_features(seg, fs, fe0, rot):
    """Features for one window `seg` (dict of arrays)."""
    n = len(seg["Ia"])
    win = np.hanning(n)
    fe, _ = fundamental(seg["Ia"], seg["Ib"], seg["Ic"], fs)
    if not (0.5 * fe0 < fe < 1.5 * fe0):   # fall back to the file-level estimate if the window is odd
        fe = fe0
    pa, pb, pc = (phasor(seg[k], fe, fs, win) for k in ("Ia", "Ib", "Ic"))
    i0, i1, i2 = sequences(pa, pb, pc, rot)
    va, vb, vc = (phasor(seg[k], fe, fs, win) for k in ("Va", "Vb", "Vc"))
    _, v1, v2 = sequences(va, vb, vc, rot)
    da, db, dc = (phasor(seg[k] - seg[k].mean(), fe, fs, win) for k in ("Da", "Db", "Dc"))
    _, d1, d2 = sequences(da, db, dc, rot)
    rms = np.array([np.sqrt(np.mean(seg[k] ** 2)) for k in ("Ia", "Ib", "Ic")])
    f = {"fe_Hz": fe, "I1": i1, "I2": i2, "I2_I1": i2 / i1, "I0_I1": i0 / i1,
         "I_unbal_rms": np.max(np.abs(rms - rms.mean())) / rms.mean(),
         "V1": v1, "V2_V1": v2 / v1, "D2_D1": d2 / d1 if d1 > 1e-9 else np.nan}
    # Vd/Vq are derived from the measured terminal voltages (external transducers); Vd_conv/Vq_conv are
    # the converter's own voltage commands (drive-internal); Torq_mec is the torque transducer.
    for key, name in (("Id", "Id"), ("Iq", "Iq"), ("Vd", "Vd"), ("Vq", "Vq"),
                      ("Vd_conv", "Vdconv"), ("Vq_conv", "Vqconv"),
                      ("Action_pi_d", "PId"), ("Action_pi_q", "PIq"), ("Torq_ele", "Te"), ("Torq_mec", "Tm")):
        x = seg[key] - seg[key].mean()
        if name in ("Id", "Iq", "PId", "PIq", "Te", "Tm"):
            f[f"{name}_std"] = np.std(x)
        f[f"{name}_2fe"] = abs(phasor(x, 2 * fe, fs, win))
        if name in ("Id", "Iq", "Te", "Tm"):
            f[f"{name}_1fe"] = abs(phasor(x, fe, fs, win))
    h1 = abs(pa)
    harm = {k: abs(phasor(seg["Ia"], k * fe, fs, win)) for k in range(2, 21)}
    f["Ia_h3"], f["Ia_h5"], f["Ia_h7"] = harm[3] / h1, harm[5] / h1, harm[7] / h1
    f["Ia_thd"] = np.sqrt(sum(v ** 2 for v in harm.values())) / h1
    f["Spd_std"] = np.std(seg["Spd"])
    f["Vdc_std"] = np.std(seg["Vdc"])
    f["Ifault_rms"] = np.sqrt(np.mean(seg["Ifault"] ** 2))
    return f


def process_file(args):
    machine, path = args
    meta = parse(path.name)
    m = loadmat(path, squeeze_me=True)
    t = m["t"]
    fs = 1.0 / np.median(np.diff(t))
    relay = m["Fault_relay"].astype(int)
    edges_on = np.flatnonzero(np.diff(relay) == 1)
    edges_off = np.flatnonzero(np.diff(relay) == -1)
    t_on = t[edges_on[0] + 1] if len(edges_on) else 1.0
    t_off = t[edges_off[0] + 1] if len(edges_off) else 1.4
    ifault = m["Ifault"]
    onset = np.flatnonzero((np.abs(ifault) > IFAULT_ONSET_A) & (t >= t_on))
    t_onset = t[onset[0]] if len(onset) else np.nan
    keys = ["Ia", "Ib", "Ic", "Va", "Vb", "Vc", "Da", "Db", "Dc", "Id", "Iq", "Vd", "Vq", "Vd_conv", "Vq_conv",
            "Action_pi_d", "Action_pi_q", "Torq_ele", "Torq_mec", "Spd", "Vdc", "Ifault"]
    sig = {k: np.asarray(m[k], dtype=float) for k in keys}

    # File-level fundamental estimate and rotation from the PRE segment.
    pre_idx = (t >= PRE[0]) & (t <= PRE[1])
    fe0, rot = fundamental(sig["Ia"][pre_idx], sig["Ib"][pre_idx], sig["Ic"][pre_idx], fs)
    nwin = int(round(NCYC * fs / fe0))
    nhop = int(round(HOP * fs / fe0))

    segments = {"PRE": PRE, "FLT": (t_on + FLT_MARGIN[0], t_off - FLT_MARGIN[1]),
                "POST": (t_off + POST[0], POST[1])}
    rows = []
    for segname, (a, b) in segments.items():
        i0 = int(np.searchsorted(t, a))
        i_end = int(np.searchsorted(t, b))
        for start in range(i0, i_end - nwin + 1, nhop):
            seg = {k: v[start:start + nwin] for k, v in sig.items()}
            f = window_features(seg, fs, fe0, rot)
            f.update(machine=machine, file=path.name, segment=segname, t_start=t[start], **meta)
            rows.append(f)
    df = pd.DataFrame(rows)

    # Per-file summary: PRE vs FLT effect sizes for every feature.
    pre = df[df.segment == "PRE"]
    flt = df[df.segment == "FLT"]
    summary = dict(machine=machine, file=path.name, **meta, fs=fs, fe0_Hz=fe0, rotation=int(rot),
                   t_on=t_on, t_off=t_off, t_onset=t_onset, onset_delay_ms=(t_onset - t_on) * 1e3,
                   n_pre=len(pre), n_flt=len(flt),
                   Ifault_rms_flt=np.sqrt(np.mean(flt["Ifault_rms"] ** 2)),
                   I1_pre=pre["I1"].mean(), I1_flt=flt["I1"].mean())
    for feat in FEATURES:
        x, y = pre[feat].to_numpy(), flt[feat].to_numpy()
        x, y = x[np.isfinite(x)], y[np.isfinite(y)]
        if len(x) < 3 or len(y) < 3:
            continue
        pooled = np.sqrt((x.var(ddof=1) + y.var(ddof=1)) / 2)
        summary[f"{feat}__pre"] = x.mean()
        summary[f"{feat}__flt"] = y.mean()
        summary[f"{feat}__d"] = (y.mean() - x.mean()) / pooled if pooled > 0 else np.nan
        summary[f"{feat}__rel"] = (y.mean() - x.mean()) / abs(x.mean()) if x.mean() != 0 else np.nan
        u = mannwhitneyu(y, x, alternative="two-sided").statistic
        summary[f"{feat}__auc"] = u / (len(x) * len(y))   # P(fault window > pre window)
    return df, summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--limit", type=int, default=0, help="process only the first N files per machine")
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    jobs = []
    for machine, folder in MACHINES.items():
        files = sorted(folder.glob("*.mat"))
        if args.limit:
            files = files[: args.limit]
        jobs += [(machine, p) for p in files]
    print(f"{len(jobs)} files, {args.workers} workers")
    windows, summaries = [], []
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        for i, (df, s) in enumerate(ex.map(process_file, jobs, chunksize=4), 1):
            windows.append(df)
            summaries.append(s)
            if i % 50 == 0 or i == len(jobs):
                print(f"  {i}/{len(jobs)} done", flush=True)
    win = pd.concat(windows, ignore_index=True)
    files = pd.DataFrame(summaries)
    win.to_csv(OUT / "features_windows.csv.gz", index=False)
    files.to_csv(OUT / "features_files.csv", index=False)
    print("windows:", win.shape, "files:", files.shape)
    print(files.groupby(["machine", "ftype"]).size())


if __name__ == "__main__":
    main()
