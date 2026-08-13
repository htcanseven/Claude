#!/usr/bin/env python3
"""Quantify how strongly acquisition session is recoverable from the features.

Creating a compound fault requires disassembling and reassembling the machine, so
in this dataset every compound run was recorded on a different day from the
single-fault run it would naturally be compared against. Any "A+B versus B"
analysis therefore varies fault *and* session together.

This control isolates the session term: it takes recordings that share a fault
label and an operating condition but differ in acquisition day, and tries to
predict the day. If the day is highly predictable, then separability between two
recordings that also differ in fault cannot be attributed to the fault.

Acquisition timestamps come from the trailing YYMMDDHHMMSS in each filename.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sklearn.ensemble import RandomForestClassifier             # noqa: E402
from sklearn.metrics import roc_auc_score                       # noqa: E402

from mcc5.cache import load_cache                               # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--train-frac", type=float, default=0.6)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    meta["ts"] = meta.file.str.extract(r"_(\d{12})d?$")[0]
    meta["date"] = meta.ts.str[:6]

    print("=== acquisition dates by fault label ===")
    for f, g in meta.groupby("fault_full"):
        dates = sorted(g.date.dropna().unique())
        flag = "  <-- multiple sessions" if len(dates) > 1 else ""
        kind = "compound" if g.is_compound.iloc[0] else "single  "
        print(f"  {kind} {f:45s} {dates}{flag}")

    single_dates = sorted(meta[~meta.is_compound].date.dropna().unique())
    comp_dates = sorted(meta[meta.is_compound].date.dropna().unique())
    print(f"\nsingle-fault sessions:   {single_dates}")
    print(f"compound-fault sessions: {comp_dates}")

    cache_path = args.data_dir / "cache" / "window_cache.npz"
    if not cache_path.exists():
        print("\n(no window cache; run scripts/build_cache.py for the "
              "day-classification control)")
        return 0

    cache = load_cache(args.data_dir / "cache", mmap_signals=False)
    F = np.nan_to_num(cache["features"], nan=0.0, posinf=0.0, neginf=0.0)
    run = cache["run"]

    print("\n=== control: predict acquisition day from the features ===")
    print("Same fault label, same operating condition, different day. Trained on "
          f"the first {args.train_frac:.0%} of each run and tested on the rest.\n")
    found = False
    for fault, sub in meta.groupby("fault_full"):
        for cond, cs in sub.groupby("condition"):
            if cs.date.nunique() < 2:
                continue
            dates = sorted(cs.date.unique())
            sel = np.isin(run, cs.index.to_numpy())
            if not sel.any():
                continue
            day = np.array([dates.index(meta.loc[r, "date"]) for r in run[sel]])
            X, rr = F[sel], run[sel]
            tr = np.zeros(len(day), dtype=bool)
            for r in np.unique(rr):
                w = np.flatnonzero(rr == r)
                tr[w[: int(len(w) * args.train_frac)]] = True
            te = ~tr
            if len(np.unique(day[tr])) < 2 or len(np.unique(day[te])) < 2:
                continue
            clf = RandomForestClassifier(n_estimators=200, n_jobs=-1,
                                         random_state=args.seed)
            clf.fit(X[tr], day[tr])
            auc = roc_auc_score(day[te], clf.predict_proba(X[te])[:, 1])
            print(f"  {fault:20s} {cond:34s} days={dates} "
                  f"AUC(day)={auc:.3f}  n_test={int(te.sum())}")
            found = True
    if not found:
        print("  (no fault label was recorded twice at one condition)")
        return 0

    print("\nInterpretation: an AUC near 1 means two recordings of the same fault "
          "at the same\noperating point are almost perfectly separable, so "
          "separability between recordings\nthat also differ in fault is not "
          "evidence that the fault caused it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
