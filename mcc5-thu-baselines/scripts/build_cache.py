#!/usr/bin/env python3
"""Precompute the window cache (features + decimated raw windows) once."""
import argparse
import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mcc5.cache import build_cache, save_cache  # noqa: E402

WIN = 8192   # 0.64 s at 12.8 kHz
HOP = 8192   # non-overlapping


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--win", type=int, default=WIN)
    ap.add_argument("--hop", type=int, default=HOP)
    ap.add_argument("--decimate", type=int, default=4)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--no-signals", action="store_true",
                    help="skip caching raw windows (features only)")
    args = ap.parse_args()

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    print(f"{len(meta)} runs | {meta.fault_full.nunique()} classes | "
          f"{meta.condition.nunique()} conditions")

    t0 = time.time()
    cache = build_cache(args.data_dir, meta, args.win, args.hop,
                        decimate=args.decimate,
                        want_signals=not args.no_signals,
                        workers=args.workers)
    print(f"{len(cache['run'])} windows in {time.time() - t0:.0f}s")
    save_cache(cache, args.data_dir / "cache")
    return 0


if __name__ == "__main__":
    sys.exit(main())
