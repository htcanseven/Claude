#!/usr/bin/env python3
"""Generate the paper's tables from the benchmark CSVs.

Writes ``paper/tables.md`` (and one CSV per table) so the manuscript is always a
rendering of the artifacts rather than a transcription of them.

  T1  protocol x model, the headline table
  T2  physics-feature ablation (plain vs plain+order)
  T3  test-time noise robustness
  T4  compound-fault protocols with multi-label metrics
  T5  per-condition detail for the two condition-shift protocols
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mcc5.protocols import PROTOCOL_ORDER, group_name  # noqa: E402

MULTILABEL_GROUPS = {"compositional_control", "leave_combination_out",
                     "compositional_zeroshot"}


def load(out_dir: Path) -> pd.DataFrame:
    frames = []
    for p in sorted(out_dir.glob("bench_*.csv")):
        d = pd.read_csv(p)
        d["source"] = p.name
        frames.append(d)
    if not frames:
        raise SystemExit(f"no bench_*.csv in {out_dir}; run the campaign first")
    df = pd.concat(frames, ignore_index=True)
    df["group"] = df["protocol"].map(group_name)
    if "noise_snr_db" not in df:
        df["noise_snr_db"] = np.nan
    return df


def md_table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    lines = ["| " + " | ".join(str(c) for c in cols) + " |",
             "| " + " | ".join("---" for _ in cols) + " |"]
    for _, r in df.iterrows():
        lines.append("| " + " | ".join(
            "" if pd.isna(r[c]) else str(r[c]) for c in cols) + " |")
    return "\n".join(lines)


def agg(g: pd.DataFrame, col: str) -> str:
    """mean ± std over seeds and folds, or a bare mean when there is one value."""
    if col not in g:
        return ""
    v = pd.to_numeric(g[col], errors="coerce").dropna()
    if v.empty:
        return ""
    if len(v) == 1:
        return f"{v.iloc[0]:.3f}"
    return f"{v.mean():.3f} ± {v.std():.3f}"


def order_key(group: str) -> int:
    return (PROTOCOL_ORDER.index(group) if group in PROTOCOL_ORDER
            else len(PROTOCOL_ORDER))


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Rows measured without injected noise."""
    return df[df["noise_snr_db"].isna()]


def t1_protocol_by_model(df: pd.DataFrame) -> pd.DataFrame:
    d = clean(df)
    d = d[d.features == "plain"]
    rows = []
    for (grp, model), g in d.groupby(["group", "model"]):
        rows.append(dict(protocol=grp, model=model, accuracy=agg(g, "acc"),
                         macro_f1=agg(g, "macro_f1"),
                         folds=g["protocol"].nunique(),
                         seeds=g["seed"].nunique()))
    out = pd.DataFrame(rows)
    out["_o"] = out["protocol"].map(order_key)
    return out.sort_values(["_o", "model"]).drop(columns="_o")


def t2_physics_ablation(df: pd.DataFrame) -> pd.DataFrame:
    d = clean(df)
    d = d[d.model.isin(["rf", "svm", "logreg"])]
    rows = []
    for (grp, model), g in d.groupby(["group", "model"]):
        if g.features.nunique() < 2:
            continue
        r = dict(protocol=grp, model=model)
        for fs, gg in g.groupby("features"):
            r[fs] = agg(gg, "acc")
        plain = pd.to_numeric(g[g.features == "plain"]["acc"],
                              errors="coerce").mean()
        both = pd.to_numeric(g[g.features == "plain+order"]["acc"],
                             errors="coerce").mean()
        if np.isfinite(plain) and np.isfinite(both):
            r["delta"] = f"{both - plain:+.3f}"
        rows.append(r)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out["_o"] = out["protocol"].map(order_key)
    return out.sort_values(["_o", "model"]).drop(columns="_o")


def t3_noise(df: pd.DataFrame) -> pd.DataFrame:
    d = df[df.model == "cnn"]
    if d.empty:
        return pd.DataFrame()
    rows = []
    for grp, g in d.groupby("group"):
        r = {"protocol": grp, "clean": agg(g[g.noise_snr_db.isna()], "acc")}
        for snr, gg in g[g.noise_snr_db.notna()].groupby("noise_snr_db"):
            r[f"{snr:g} dB"] = agg(gg, "acc")
        rows.append(r)
    out = pd.DataFrame(rows)
    out["_o"] = out["protocol"].map(order_key)
    return out.sort_values("_o").drop(columns="_o")


def t4_compound(df: pd.DataFrame) -> pd.DataFrame:
    d = clean(df)
    d = d[d.group.isin(MULTILABEL_GROUPS)]
    if d.empty:
        return pd.DataFrame()
    rows = []
    for (grp, model, fs), g in d.groupby(["group", "model", "features"]):
        rows.append(dict(
            protocol=grp, model=model, features=fs,
            exact_match=agg(g, "acc"), micro_f1=agg(g, "micro_f1"),
            any_found=agg(g, "any_component_found"),
            all_zero=agg(g, "all_zero_prediction_rate"),
            topk_exact=agg(g, "topk_exact"), topk_recall=agg(g, "topk_recall")))
    out = pd.DataFrame(rows)
    out["_o"] = out["protocol"].map(order_key)
    return out.sort_values(["_o", "model", "features"]).drop(columns="_o")


def t5_per_condition(df: pd.DataFrame) -> pd.DataFrame:
    d = clean(df)
    d = d[d.group.isin(["unknown_condition", "single_source"])
          & (d.features == "plain") & (d.model == "rf")]
    if d.empty:
        return pd.DataFrame()
    d = d.assign(condition=d.protocol.str.extract(r"\[(.*)\]")[0])
    rows = []
    for cond, g in d.groupby("condition"):
        r = {"condition": cond}
        for grp, gg in g.groupby("group"):
            r[grp] = agg(gg, "acc")
        rows.append(r)
    return pd.DataFrame(rows).sort_values("condition")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--paper", type=Path, default=Path("paper"))
    args = ap.parse_args()
    args.paper.mkdir(parents=True, exist_ok=True)

    df = load(args.out)
    tables = [
        ("T1", "Protocol x model (plain features)", t1_protocol_by_model(df)),
        ("T2", "Physics-feature ablation: plain vs plain+order",
         t2_physics_ablation(df)),
        ("T3", "Test-time noise robustness (CNN)", t3_noise(df)),
        ("T4", "Compound-fault protocols, multi-label metrics", t4_compound(df)),
        ("T5", "Per-condition detail (random forest, plain features)",
         t5_per_condition(df)),
    ]

    md = ["# Generated tables", "",
          f"Source: {df['source'].nunique()} result file(s), "
          f"{len(df)} rows.", ""]
    for tag, title, tab in tables:
        md += [f"## {tag}. {title}", ""]
        if tab is None or tab.empty:
            md += ["*(no data yet — stage still running or not scheduled)*", ""]
            continue
        md += [md_table(tab), ""]
        tab.to_csv(args.paper / f"table_{tag}.csv", index=False)

    (args.paper / "tables.md").write_text("\n".join(md))
    print("\n".join(md))
    print(f"written -> {args.paper / 'tables.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
