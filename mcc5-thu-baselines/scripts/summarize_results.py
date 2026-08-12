#!/usr/bin/env python3
"""Aggregate baseline CSVs into a single Markdown summary table."""
import argparse
from pathlib import Path

import pandas as pd


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("results"))
    args = ap.parse_args()

    frames = []
    for name in ("feature_baseline.csv", "cnn_baseline.csv"):
        p = args.out / name
        if p.exists():
            frames.append(pd.read_csv(p))
    if not frames:
        print("no baseline CSVs found in", args.out)
        return 1

    df = pd.concat(frames, ignore_index=True)
    # collapse leave-one-condition-out folds to mean +/- std per model
    df["protocol_group"] = df["protocol"].str.replace(r"\[.*\]", "",
                                                      regex=True)
    rows = []
    for (grp, model), g in df.groupby(["protocol_group", "model"]):
        rows.append(dict(
            protocol=grp, model=model,
            acc=f"{g.acc.mean():.3f}" + (f" ± {g.acc.std():.3f}"
                                         if len(g) > 1 else ""),
            macro_f1=f"{g.macro_f1.mean():.3f}" + (f" ± {g.macro_f1.std():.3f}"
                                                   if len(g) > 1 else ""),
            n_folds=len(g),
        ))
    summary = pd.DataFrame(rows).sort_values(["protocol", "model"])
    md = to_markdown(summary)
    (args.out / "SUMMARY.md").write_text(
        "# MCC5-THU baseline results\n\n" + md + "\n")
    print(md)
    print(f"\nwritten -> {args.out / 'SUMMARY.md'}")
    return 0


def to_markdown(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |",
             "| " + " | ".join("---" for _ in cols) + " |"]
    for _, r in df.iterrows():
        lines.append("| " + " | ".join(str(r[c]) for c in cols) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
