#!/usr/bin/env python3
"""Generate the paper's figures from the benchmark CSVs and the cached data.

  fig3_protocol_ladder   accuracy against protocol difficulty, per model
  fig4_order_spectra     envelope-order spectra, healthy vs each bearing defect
  fig5_zeroshot          per-component F1 on the zero-shot compound test
  fig6_noise             accuracy against test-time SNR
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mcc5.protocols import PROTOCOL_ORDER, group_name   # noqa: E402
from mcc5.physics import (envelope_order_spectrum, shaft_angle,  # noqa: E402
                          BEARING_ORDERS)

plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 300, "font.size": 9,
    "axes.grid": True, "grid.alpha": 0.3, "axes.spines.top": False,
    "axes.spines.right": False, "savefig.bbox": "tight",
})

SHORT = {
    "leaky_random": "leaky\nrandom",
    "in_condition": "in\ncondition",
    "unknown_condition": "unknown\ncondition",
    "cross_profile": "cross\nprofile",
    "single_source": "single\nsource",
    "steady_to_transitional": "steady→\ntransitional",
    "compositional_control": "compositional\ncontrol",
    "leave_combination_out": "leave\ncombination out",
    "compositional_zeroshot": "compositional\nzero-shot",
}


def load_bench(out_dir: Path) -> pd.DataFrame:
    frames = [pd.read_csv(p) for p in sorted(out_dir.glob("bench_*.csv"))]
    if not frames:
        raise SystemExit("no bench_*.csv found")
    df = pd.concat(frames, ignore_index=True)
    df["group"] = df["protocol"].map(group_name)
    if "noise_snr_db" not in df:
        df["noise_snr_db"] = np.nan
    return df


def fig_protocol_ladder(df, path: Path):
    d = df[df.noise_snr_db.isna() & (df.features == "plain")]
    groups = [g for g in PROTOCOL_ORDER if g in set(d.group)]
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    for model, g in d.groupby("model"):
        xs, ys, es = [], [], []
        for i, grp in enumerate(groups):
            v = pd.to_numeric(g[g.group == grp]["acc"], errors="coerce").dropna()
            if v.empty:
                continue
            xs.append(i)
            ys.append(v.mean())
            es.append(v.std() if len(v) > 1 else 0.0)
        ax.errorbar(xs, ys, yerr=es, marker="o", capsize=3, label=model, lw=1.6)
    ax.set_xticks(range(len(groups)))
    ax.set_xticklabels([SHORT.get(g, g) for g in groups], fontsize=7.5)
    ax.set_ylabel("accuracy / exact match")
    ax.set_ylim(-0.03, 1.03)
    ax.axhline(1 / 24, ls=":", c="grey", lw=1)
    ax.text(0.02, 1 / 24 + 0.02, "chance (24 classes)", fontsize=7, c="grey",
            transform=ax.get_yaxis_transform())
    ax.set_title("One dataset, one feature set: accuracy is set by the protocol")
    ax.legend(frameon=False, fontsize=8, loc="lower left",
              bbox_to_anchor=(0.02, 0.06))
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path)


def fig_order_spectra(data_dir: Path, path: Path):
    base = data_dir / "converted"
    cases = [("health_torque_circulation_20Nm_3000rpm*", "healthy"),
             ("bearing_outer_H_torque_circulation_20Nm_3000rpm*",
              "outer-race defect"),
             ("bearing_inner_H_torque_circulation_20Nm_3000rpm*",
              "inner-race defect"),
             ("bearing_ball_H_torque_circulation_20Nm_3000rpm*",
              "ball defect")]
    fig, axes = plt.subplots(len(cases), 1, figsize=(7.2, 7.0), sharex=True)
    for ax, (pat, label) in zip(axes, cases):
        files = sorted(base.glob(pat))
        if not files:
            ax.set_visible(False)
            continue
        with np.load(files[0]) as z:
            x = z["x"]
        seg = slice(0, 8192 * 30)
        kp = x[0][seg].astype(np.float64)
        ang = shaft_angle(kp)
        orders, amp = envelope_order_spectrum(x[2][seg].astype(np.float64), ang)
        if len(orders) == 0:
            ax.set_visible(False)
            continue
        amp = amp / (amp.max() + 1e-12)
        ax.plot(orders, amp, lw=0.7, c="0.25")
        for name, o in BEARING_ORDERS.items():
            ax.axvline(o, ls="--", lw=1, alpha=0.8,
                       c={"BPFO": "tab:red", "BPFI": "tab:blue",
                          "BSF": "tab:green"}[name])
            ax.text(o, 1.02, name, fontsize=7, ha="center",
                    c={"BPFO": "tab:red", "BPFI": "tab:blue",
                       "BSF": "tab:green"}[name])
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 1.18)
        ax.set_ylabel("norm. amp.")
        ax.set_title(label, fontsize=9, loc="left")
    axes[-1].set_xlabel("order (multiples of shaft rate)")
    fig.suptitle("Envelope-order spectra: each raceway defect raises its own "
                 "order", fontsize=10)
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path)


def fig_zeroshot_components(out_dir: Path, path: Path):
    cands = sorted(out_dir.glob("components_compositional_zeroshot*.csv"))
    if not cands:
        print("skip zero-shot component figure (no CSV yet)")
        return
    d = pd.read_csv(cands[0])
    d = d[d.support_test > 0].sort_values("f1")
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    colors = ["tab:orange" if "bearing" in c else "tab:red"
              for c in d.component]
    ax.barh(d.component, d.f1, color=colors)
    ax.set_xlabel("F1 on unseen compound faults")
    ax.set_xlim(0, max(0.25, d.f1.max() * 1.15))
    ax.set_title("Non-bearing components are annihilated when a bearing\n"
                 "defect co-occurs (orange = bearing, red = other)",
                 fontsize=9)
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path)


def fig_noise(df, path: Path):
    d = df[(df.model == "cnn")]
    if d.empty or d.noise_snr_db.notna().sum() == 0:
        print("skip noise figure (no CNN noise rows yet)")
        return
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    for grp, g in d.groupby("group"):
        clean = pd.to_numeric(g[g.noise_snr_db.isna()]["acc"],
                              errors="coerce").mean()
        pts = (g[g.noise_snr_db.notna()]
               .groupby("noise_snr_db")["acc"].mean().sort_index())
        if pts.empty or not np.isfinite(clean):
            continue
        xs = list(pts.index) + [np.inf]
        ys = list(pts.values) + [clean]
        order = np.argsort([1e9 if np.isinf(v) else v for v in xs])
        xs = [xs[i] for i in order]
        ys = [ys[i] for i in order]
        labels = ["clean" if np.isinf(v) else f"{v:g}" for v in xs]
        ax.plot(range(len(xs)), ys, marker="o", lw=1.5,
                label=SHORT.get(grp, grp).replace("\n", " "))
        ax.set_xticks(range(len(xs)))
        ax.set_xticklabels(labels)
    ax.set_xlabel("test-time SNR (dB)")
    ax.set_ylabel("accuracy")
    ax.set_title("Clean-data accuracy is optimistic under additive noise",
                 fontsize=9)
    ax.legend(frameon=False, fontsize=7.5)
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--figs", type=Path, default=Path("paper/figures"))
    args = ap.parse_args()
    args.figs.mkdir(parents=True, exist_ok=True)

    df = load_bench(args.out)
    fig_protocol_ladder(df, args.figs / "fig3_protocol_ladder.png")
    fig_noise(df, args.figs / "fig6_noise.png")
    fig_zeroshot_components(args.out, args.figs / "fig5_zeroshot.png")
    if (args.data_dir / "converted").exists():
        fig_order_spectra(args.data_dir, args.figs / "fig4_order_spectra.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
