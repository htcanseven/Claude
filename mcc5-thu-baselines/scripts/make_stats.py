#!/usr/bin/env python3
"""Significance tests for the paper's headline contrasts.

Each contrast is tested with the pairing that matches how the numbers were
produced, because the wrong pairing is the usual way these tests mislead:

* Contrasts sharing folds (the same twelve operating conditions appear in both
  ``unknown_condition`` and ``single_source``) are paired by fold, so the test
  removes per-condition difficulty rather than treating it as noise.
* Contrasts over independent groups (two cross-profile directions) use an
  unpaired test.
* Effect sizes accompany every p-value. With twelve folds a small difference can
  be highly significant and still irrelevant, and the headline gaps here are
  large enough that the effect size is the more informative number.

Writes ``paper/stats.md`` and ``paper/table_T7.csv``.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mcc5.protocols import group_name  # noqa: E402


def load(out_dir: Path) -> pd.DataFrame:
    frames = [pd.read_csv(p) for p in sorted(out_dir.glob("bench_*.csv"))]
    if not frames:
        raise SystemExit(f"no bench_*.csv in {out_dir}")
    df = pd.concat(frames, ignore_index=True)
    df["group"] = df["protocol"].map(group_name)
    if "noise_snr_db" not in df:
        df["noise_snr_db"] = np.nan
    return df[df.noise_snr_db.isna()]


def cohens_d(a, b) -> float:
    a, b = np.asarray(a, float), np.asarray(b, float)
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return float("nan")
    s = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1))
                / (na + nb - 2))
    return float((a.mean() - b.mean()) / s) if s > 0 else float("nan")


def fold_means(df, group, model, features, metric="acc") -> pd.Series:
    d = df[(df.group == group) & (df.model == model)
           & (df.features == features)]
    if d.empty:
        return pd.Series(dtype=float)
    # average seeds within a fold so the unit of analysis is the fold
    return d.groupby("protocol")[metric].mean()


def condition_of(protocol: str) -> str:
    return protocol.split("[", 1)[1].rstrip("]") if "[" in protocol else ""


def paired_test(a: pd.Series, b: pd.Series, name_a: str, name_b: str,
                pair_on_condition=True):
    """Paired over shared folds; falls back to unpaired when they differ."""
    if pair_on_condition:
        a = a.rename(index=condition_of)
        b = b.rename(index=condition_of)
    common = sorted(set(a.index) & set(b.index))
    if len(common) >= 3:
        x, y = a.loc[common].to_numpy(), b.loc[common].to_numpy()
        t, p = stats.ttest_rel(x, y)
        try:
            _, pw = stats.wilcoxon(x, y)
        except ValueError:
            pw = float("nan")
        return dict(contrast=f"{name_a} vs {name_b}", pairing="paired by fold",
                    n=len(common), mean_a=round(float(x.mean()), 4),
                    mean_b=round(float(y.mean()), 4),
                    delta=round(float((x - y).mean()), 4),
                    t=round(float(t), 3), p_ttest=f"{p:.2e}",
                    p_wilcoxon=("" if np.isnan(pw) else f"{pw:.2e}"),
                    cohens_d=round(cohens_d(x, y), 3))
    if len(a) and len(b):
        t, p = stats.ttest_ind(a.to_numpy(), b.to_numpy(), equal_var=False)
        return dict(contrast=f"{name_a} vs {name_b}", pairing="unpaired",
                    n=f"{len(a)}/{len(b)}", mean_a=round(float(a.mean()), 4),
                    mean_b=round(float(b.mean()), 4),
                    delta=round(float(a.mean() - b.mean()), 4),
                    t=round(float(t), 3), p_ttest=f"{p:.2e}", p_wilcoxon="",
                    cohens_d=round(cohens_d(a, b), 3))
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--paper", type=Path, default=Path("paper"))
    ap.add_argument("--model", default="rf")
    args = ap.parse_args()
    args.paper.mkdir(parents=True, exist_ok=True)

    df = load(args.out)
    m, f = args.model, "plain"
    rows = []

    # 1. The headline protocol contrast: the same twelve conditions, held out
    #    versus used as the sole training source.
    r = paired_test(fold_means(df, "unknown_condition", m, f),
                    fold_means(df, "single_source", m, f),
                    "unknown_condition", "single_source")
    if r:
        rows.append(r)

    # 2. In-condition versus each condition-shift protocol.
    for grp in ("unknown_condition", "single_source",
                "steady_to_transitional", "cross_profile"):
        a = fold_means(df, "in_condition", m, f)
        b = fold_means(df, grp, m, f)
        if len(a) and len(b):
            r = paired_test(a, b, "in_condition", grp,
                            pair_on_condition=False)
            if r:
                rows.append(r)

    # 3. Cross-profile asymmetry: independent directions, so unpaired.
    cp = df[(df.group == "cross_profile") & (df.model == m)
            & (df.features == f)]
    if not cp.empty:
        sp = cp[cp.protocol.str.contains("speed_circulation")]["acc"]
        tq = cp[cp.protocol.str.contains("torque_circulation")]["acc"]
        if len(sp) and len(tq):
            r = paired_test(pd.Series(sp.to_numpy()),
                            pd.Series(tq.to_numpy()),
                            "cross_profile[train=speed]",
                            "cross_profile[train=torque]",
                            pair_on_condition=False)
            if r:
                rows.append(r)

    # 4. Physics-feature ablation, paired by fold within each protocol.
    for grp in sorted(df.group.unique()):
        a = fold_means(df, grp, m, "plain+order")
        b = fold_means(df, grp, m, "plain")
        if len(a) >= 3 and len(b) >= 3:
            r = paired_test(a, b, f"{grp}[plain+order]", f"{grp}[plain]",
                            pair_on_condition=False)
            if r:
                rows.append(r)

    # 5. The compound-fault control contrast.
    a = fold_means(df, "compositional_control", m, f)
    b = fold_means(df, "compositional_zeroshot", m, f)
    if len(a) and len(b):
        r = paired_test(a, b, "compositional_control",
                        "compositional_zeroshot", pair_on_condition=False)
        if r:
            rows.append(r)

    if not rows:
        print("no contrasts computable yet; campaign still running")
        return 0

    tab = pd.DataFrame(rows)
    tab.to_csv(args.paper / "table_T7.csv", index=False)
    cols = list(tab.columns)
    md = ["# T7. Significance of the headline contrasts", "",
          "Paired by fold where both protocols share folds, unpaired otherwise. "
          "`delta` is mean(a) - mean(b). With twelve folds, statistical "
          "significance is easy to reach, so the effect size is the number to "
          "read.", "",
          "| " + " | ".join(cols) + " |",
          "| " + " | ".join("---" for _ in cols) + " |"]
    for _, r in tab.iterrows():
        md.append("| " + " | ".join(
            "" if pd.isna(r[c]) else str(r[c]) for c in cols) + " |")
    (args.paper / "stats.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))
    print(f"\nwritten -> {args.paper / 'stats.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
