#!/usr/bin/env python3
"""Aggregate all result CSVs into a Markdown summary ordered by difficulty."""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

# Protocols in the order the paper presents them: optimistic first, then the
# progressively harder honest ones.
ORDER = ["leaky_random", "in_condition", "unknown_condition",
         "cross_profile", "single_source", "steady_to_transitional",
         "compositional_zeroshot"]

RESULT_FILES = ("feature_baseline*.csv", "cnn_baseline*.csv", "proposed*.csv")


def to_markdown(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |",
             "| " + " | ".join("---" for _ in cols) + " |"]
    for _, r in df.iterrows():
        lines.append("| " + " | ".join("" if pd.isna(r[c]) else str(r[c])
                                       for c in cols) + " |")
    return "\n".join(lines)


def fmt(g: pd.DataFrame, col: str) -> str:
    if col not in g or g[col].isna().all():
        return ""
    v = g[col].dropna()
    return f"{v.mean():.3f}" + (f" ± {v.std():.3f}" if len(v) > 1 else "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("results"))
    args = ap.parse_args()

    frames = []
    for pat in RESULT_FILES:
        for p in sorted(args.out.glob(pat)):
            d = pd.read_csv(p)
            d["source"] = p.name
            frames.append(d)
    if not frames:
        print("no result CSVs found in", args.out)
        return 1

    df = pd.concat(frames, ignore_index=True)
    if "feature_set" not in df:
        df["feature_set"] = ""
    df["feature_set"] = df["feature_set"].fillna("")
    # collapse leave-one-condition-out folds into one row per model
    df["protocol_group"] = df["protocol"].str.replace(r"\[.*\]", "",
                                                      regex=True)

    rows = []
    for (grp, model, fset), g in df.groupby(
            ["protocol_group", "model", "feature_set"], dropna=False):
        rows.append(dict(
            protocol=grp, model=model, features=fset,
            acc=fmt(g, "acc"), macro_f1=fmt(g, "macro_f1"),
            micro_f1=fmt(g, "micro_f1"),
            n_runs=len(g),
            folds=g["protocol"].nunique(),
        ))
    summary = pd.DataFrame(rows)
    summary["_o"] = summary["protocol"].apply(
        lambda p: ORDER.index(p) if p in ORDER else len(ORDER))
    summary = (summary.sort_values(["_o", "model", "features"])
                      .drop(columns="_o"))

    md = ["# MCC5-THU baseline and proposed-model results", "",
          "`acc` is exact-match accuracy (for the multi-label compositional "
          "protocol, all components of a compound fault must be correct). "
          "Values are mean ± std over seeds and folds.", "",
          to_markdown(summary), ""]

    # Headline: how far each honest protocol falls below the leaky one
    leak = df[df.protocol_group == "leaky_random"]["acc"]
    if len(leak):
        base = leak.mean()
        md += ["## Drop relative to the leaky random split", "",
               f"Reference (leaky_random, all models): **{base:.3f}**", ""]
        drops = []
        for grp, g in df.groupby("protocol_group"):
            if grp == "leaky_random":
                continue
            drops.append(dict(protocol=grp, acc=f"{g.acc.mean():.3f}",
                              drop=f"{base - g.acc.mean():+.3f}"))
        dd = pd.DataFrame(drops)
        dd["_o"] = dd["protocol"].apply(
            lambda p: ORDER.index(p) if p in ORDER else len(ORDER))
        md += [to_markdown(dd.sort_values("_o").drop(columns="_o")), ""]

    (args.out / "SUMMARY.md").write_text("\n".join(md))
    print("\n".join(md))
    print(f"written -> {args.out / 'SUMMARY.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
