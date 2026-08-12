#!/usr/bin/env python3
"""Extract + convert the downloaded zips into float32 .npz runs + metadata.csv."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mcc5.convert import convert_all  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    args = ap.parse_args()
    meta = convert_all(args.data_dir)
    print(meta.groupby("fault_full").size().sort_values(ascending=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
