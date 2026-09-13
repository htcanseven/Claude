"""Inventory of the InnovaPower MitDev-Eletrica datasets (PMSG, SCIG, wound-field SGs).

Verifies that the PMSG and SCIG test matrices are identical, reports the variables stored in the
.mat files, and summarises the parameter space encoded in the wound-field SG file names.

Usage: python scripts/inventory.py [DATA_ROOT]
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.io import loadmat

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "data/mitdev")

PMSG = ROOT / "PMSG-3phase-Dataset"
SCIG = ROOT / "SCIG-3phase-Dataset"
GENS = ROOT / "Generators-Dataset"

# FAULT_WINDINGS_D16_D18_R026_S1200_T52.mat / HEALTHY_R000_S1200_T52.mat (healthy naming verified below)
PAT_3PH = re.compile(
    r"^(?P<state>FAULT|HEALTHY)(?:_(?P<ftype>TURNS|WINDINGS)_(?P<d1>D\d\d)_(?P<d2>D\d\d))?"
    r"(?:_R(?P<r>\d+))?_S(?P<spd>\d+)_T(?P<trq>\d+)\.mat$"
)


def parse_3ph(name: str):
    m = PAT_3PH.match(name)
    if not m:
        return None
    d = m.groupdict()
    case = "HEALTHY" if d["state"] == "HEALTHY" else f"{d['ftype']}_{d['d1']}_{d['d2']}"
    return dict(case=case, state=d["state"], ftype=d["ftype"] or "NONE", d1=d["d1"], d2=d["d2"],
                r=d["r"], speed_rpm=int(d["spd"]), torque_Nm=int(d["trq"]) / 10)


def describe_3ph(folder: Path, label: str):
    files = sorted(p for p in folder.rglob("*.mat"))
    other = sorted(p.name for p in folder.rglob("*") if p.is_file() and p.suffix != ".mat")
    print(f"\n=== {label}: {folder} ===")
    print(f"{len(files)} .mat files; non-mat files: {other}")
    parsed, unparsed = [], []
    for p in files:
        d = parse_3ph(p.name)
        (parsed if d else unparsed).append((p, d))
    if unparsed:
        print("UNPARSED names (first 10):", [p.name for p, _ in unparsed[:10]])
    cases = Counter(d["case"] for _, d in parsed)
    speeds = sorted({d["speed_rpm"] for _, d in parsed})
    torques = sorted({d["torque_Nm"] for _, d in parsed})
    rs = sorted({str(d["r"]) for _, d in parsed})
    print(f"cases: {len(cases)} distinct ({sum(1 for c in cases if c != 'HEALTHY')} fault + "
          f"{'1' if 'HEALTHY' in cases else '0'} healthy); files per case: {sorted(set(cases.values()))}")
    print(f"speeds (rpm): {speeds}; torques (Nm): {torques}; fault resistance codes: {rs}")
    print("fault types:", Counter(d["ftype"] for _, d in parsed))
    total_mb = sum(p.stat().st_size for p in files) / 1e6
    print(f"total size: {total_mb:.0f} MB; per file ~{total_mb / max(len(files), 1):.1f} MB")
    return set(cases), files


def peek_mat(path: Path, label: str):
    print(f"\n--- variables in {label} example: {path.name} ---")
    m = loadmat(path, squeeze_me=True, struct_as_record=False)
    keys = [k for k in m if not k.startswith("__")]
    print("top-level keys:", keys)
    for k in keys:
        v = m[k]
        if isinstance(v, np.ndarray):
            print(f"  {k:14s} ndarray {v.shape} {v.dtype}")
        else:
            attrs = [a for a in dir(v) if not a.startswith("_")]
            print(f"  {k:14s} {type(v).__name__} with fields: {attrs}")
    # Try to locate the time vector and the fault relay to report timing.
    flat = {}
    for k in keys:
        v = m[k]
        if isinstance(v, np.ndarray) and v.ndim == 1 and v.dtype.kind in "fiu":
            flat[k] = v
        elif not isinstance(v, np.ndarray):
            for a in dir(v):
                if not a.startswith("_"):
                    x = getattr(v, a)
                    if isinstance(x, np.ndarray) and x.ndim == 1 and x.dtype.kind in "fiu":
                        flat[a] = x
    t = next((flat[k] for k in flat if k.lower() in ("t", "time")), None)
    if t is not None and len(t) > 2:
        dt = np.median(np.diff(t))
        print(f"  time: n={len(t)}, t0={t[0]:.4f}, t_end={t[-1]:.4f}, dt={dt * 1e6:.1f} us -> fs={1 / dt:.0f} Hz")
    relay = next((flat[k] for k in flat if "relay" in k.lower()), None)
    if relay is not None and t is not None:
        on = np.flatnonzero(np.diff((relay > 0.5).astype(int)) == 1)
        off = np.flatnonzero(np.diff((relay > 0.5).astype(int)) == -1)
        if len(on):
            print(f"  fault relay ON at t={t[on[0] + 1]:.4f}s"
                  + (f", OFF at t={t[off[0] + 1]:.4f}s (duration {t[off[0] + 1] - t[on[0] + 1]:.4f}s)" if len(off) else ""))
    ifault = next((flat[k] for k in flat if k.lower() in ("ifault", "i_fault")), None)
    if ifault is not None:
        print(f"  Ifault: max |I| = {np.max(np.abs(ifault)):.2f} A")
    for k in ("Ia", "Ib", "Ic", "Id", "Iq", "Spd", "Torq_mec"):
        if k in flat:
            x = flat[k]
            print(f"  {k:9s} mean={np.mean(x):9.3f} std={np.std(x):8.3f} min={np.min(x):9.3f} max={np.max(x):9.3f}")
    return flat


PAT_GEN = re.compile(
    r"^(?P<state>FAULT|HEALTHY)_GER(?:_TYPE_(?P<ftype>[A-Z]+)(?:_(?P<phase>[A-C]))?_POS_(?P<d1>D\d\d)_(?P<d2>D\d\d)"
    r"_ZF_(?P<zf>[\d.]+))?_TRQ_(?P<trq>[\d.]+)_SPD_(?P<spd>\d+)_ID_(?P<id>\d+)\.csv$"
)


def describe_gens(folder: Path):
    print(f"\n=== Generators-Dataset (wound-field SGs): {folder} ===")
    for bench in sorted(p for p in folder.iterdir() if p.is_dir() and p.name != "Figures"):
        files = sorted(bench.glob("*.csv"))
        vals = defaultdict(set)
        unparsed = []
        cases = Counter()
        for p in files:
            m = PAT_GEN.match(p.name)
            if not m:
                unparsed.append(p.name)
                continue
            d = m.groupdict()
            for k, v in d.items():
                if v is not None:
                    vals[k].add(v)
            cases[(d["ftype"] or "HEALTHY", d["phase"], d["d1"], d["d2"], d["zf"])] += 1
        mb = sum(p.stat().st_size for p in files) / 1e6
        print(f"\n{bench.name}: {len(files)} csv, {mb:.0f} MB, {len(cases)} distinct (type,phase,D,D,ZF) cases")
        for k in ("state", "ftype", "phase", "zf", "trq", "spd", "id"):
            if k in vals:
                v = sorted(vals[k], key=lambda s: float(s) if re.fullmatch(r"[\d.]+", s) else s)
                print(f"  {k:6s}: {v}")
        if unparsed:
            print("  UNPARSED (first 5):", unparsed[:5])
        # header of first file
        with open(files[0]) as fh:
            head = fh.readline().strip()
            n = sum(1 for _ in fh) + 1
        print(f"  columns ({len(head.split(','))}): {head[:300]}{'...' if len(head) > 300 else ''}")
        print(f"  rows in first file: {n}")


if __name__ == "__main__":
    pm_cases, pm_files = describe_3ph(PMSG, "PMSG")
    sc_cases, sc_files = describe_3ph(SCIG, "SCIG")
    print("\n=== PMSG vs SCIG test matrix ===")
    print("identical case sets:", pm_cases == sc_cases)
    print("only in PMSG:", sorted(pm_cases - sc_cases))
    print("only in SCIG:", sorted(sc_cases - pm_cases))
    pm_names = {p.name for p in pm_files}
    sc_names = {p.name for p in sc_files}
    print(f"identical file names: {pm_names == sc_names} ({len(pm_names & sc_names)} shared)")
    for files, label in ((pm_files, "PMSG"), (sc_files, "SCIG")):
        fault = next(p for p in files if p.name.startswith("FAULT"))
        healthy = next((p for p in files if p.name.startswith("HEALTHY")), None)
        peek_mat(fault, label)
        if healthy is not None:
            peek_mat(healthy, label + " (healthy)")
    describe_gens(GENS)
