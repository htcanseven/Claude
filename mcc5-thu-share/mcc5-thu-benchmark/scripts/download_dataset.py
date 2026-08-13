#!/usr/bin/env python3
"""Download the MCC5-THU motor dataset (two zips, ~13 GB) from Hugging Face.

Creates <data-dir> and downloads with resume support, so an interrupted
download continues where it left off.
"""
import argparse
import sys
from pathlib import Path

import requests

FILES = {
    "speed_circulation.zip": (
        "https://huggingface.co/datasets/Samlzy/MCC5-THU-Motor/resolve/main/"
        "MCC5-THU%20Motor_speed_circulation.zip"
    ),
    "torque_circulation.zip": (
        "https://huggingface.co/datasets/Samlzy/MCC5-THU-Motor/resolve/main/"
        "MCC5-THU%20Motor_torque_circulation.zip"
    ),
}

CHUNK = 1 << 20  # 1 MiB


def download(url: str, dest: Path) -> None:
    pos = dest.stat().st_size if dest.exists() else 0
    headers = {"Range": f"bytes={pos}-"} if pos else {}
    with requests.get(url, headers=headers, stream=True, timeout=60) as r:
        if r.status_code == 416:  # range not satisfiable -> already complete
            print(f"{dest.name}: already complete")
            return
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0)) + pos
        mode = "ab" if pos and r.status_code == 206 else "wb"
        done = pos if mode == "ab" else 0
        with open(dest, mode) as f:
            for chunk in r.iter_content(CHUNK):
                f.write(chunk)
                done += len(chunk)
                pct = 100 * done / total if total else 0
                print(f"\r{dest.name}: {done / 1e9:.2f} GB ({pct:.1f}%)",
                      end="", flush=True)
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"),
                    help="folder to create and download into (default ./data)")
    args = ap.parse_args()

    args.data_dir.mkdir(parents=True, exist_ok=True)
    for name, url in FILES.items():
        download(url, args.data_dir / name)
    print(f"Done. Files are in {args.data_dir.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
