"""Analysis D: accuracy-resource trade-off sweeps (leakage-free GROUP protocol).

Anchored on Random Forest (the article's best model) for comparability; the
GROUP protocol (whole-recording holdout) is used throughout so every number is
deployment-realistic. Each sweep varies one sensing/communication knob.
"""
from __future__ import annotations

import os, json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.metrics import accuracy_score, f1_score

from dataio import list_recordings, CHANNELS, RAW_CHANNELS, USER_CHANNELS, FS
from features import build_feature_matrix, FEATURE_NAMES, PAPER_FEATURES
import viz
import matplotlib.pyplot as plt

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEED = 0
N_SPLITS = 6


def group_rf(X, y, groups, Xtest=None, n_estimators=200):
    """Mean±std accuracy/F1 over GROUP folds. If Xtest given, train on X[tr],
    test on Xtest[te] (used for the coupling-robustness sweep)."""
    sgkf = StratifiedGroupKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    accs, f1s = [], []
    for tr, te in sgkf.split(X, y, groups):
        rf = RandomForestClassifier(n_estimators=n_estimators, n_jobs=-1,
                                    random_state=SEED)
        rf.fit(X[tr], y[tr])
        Xe = X if Xtest is None else Xtest
        yp = rf.predict(Xe[te])
        accs.append(accuracy_score(y[te], yp))
        f1s.append(f1_score(y[te], yp, average="macro"))
    return (100*np.mean(accs), 100*np.std(accs), 100*np.mean(f1s))


def raw_bitrate(fs, n_ch, bytes_per_sample=2):
    return fs * n_ch * bytes_per_sample * 8  # bits/s


def quantize_transform(bits):
    def t(sig, rec):
        lo = sig.min(0, keepdims=True); hi = sig.max(0, keepdims=True)
        rng = np.maximum(hi - lo, 1e-9)
        levels = 2 ** bits - 1
        q = np.round((sig - lo) / rng * levels) / levels * rng + lo
        return q.astype(np.float32)
    return t


def packetloss_transform(p, rng_seed=0):
    def t(sig, rec):
        rng = np.random.default_rng(rng_seed + hash(rec.name) % 1000)
        mask = rng.random(len(sig)) < p
        out = sig.copy()
        # sample-and-hold concealment (forward fill lost samples)
        idx = np.where(~mask)[0]
        if len(idx) == 0:
            return out
        # forward-fill: for each row, use last good index
        last_good = np.maximum.accumulate(np.where(mask, -1, np.arange(len(sig))))
        last_good[last_good < 0] = idx[0]
        return sig[last_good].astype(np.float32)
    return t


def rodrigues(axis, theta_deg):
    a = np.asarray(axis, float); a = a/np.linalg.norm(a)
    th = np.deg2rad(theta_deg)
    K = np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3) + np.sin(th)*K + (1-np.cos(th))*(K@K)


def rotation_transform(theta_deg, axis=(1,1,0)):
    R = rodrigues(axis, theta_deg)
    def t(sig, rec):
        out = sig.copy()
        out[:, 0:3] = sig[:, 0:3] @ R.T   # raw triad
        if sig.shape[1] >= 6:
            out[:, 3:6] = sig[:, 3:6] @ R.T  # gravity-compensated triad
        return out.astype(np.float32)
    return t


def main():
    viz.set_style()
    recs = list_recordings()
    results = {}

    # ===== base matrix (reused by channel & feature sweeps) =====
    print("base build…")
    base = build_feature_matrix(recs)  # 100Hz, all ch, 2s, full
    X0, y, g = base["X"], base["y"], base["groups"]
    cols = base["columns"]
    a, s, f = group_rf(X0, y, g)
    results["baseline"] = dict(acc=a, acc_std=s, f1=f)
    print(f"baseline GROUP RF: {a:.1f}±{s:.1f}")

    # ===== D1 sampling rate =====
    print("D1 sampling rate…")
    d1 = []
    for fs in [100, 50, 25, 20, 12.5, 10]:
        if fs == 100:
            a, s, f = results["baseline"]["acc"], results["baseline"]["acc_std"], results["baseline"]["f1"]
        else:
            d = build_feature_matrix(recs, fs_target=fs)
            a, s, f = group_rf(d["X"], d["y"], d["groups"])
        d1.append(dict(fs=fs, acc=a, acc_std=s, f1=f, bitrate_kbps=raw_bitrate(fs, 6)/1e3))
        print(f"  fs={fs:>5}Hz -> {a:.1f}±{s:.1f}  ({raw_bitrate(fs,6)/1e3:.1f} kbps raw)")
    results["D1_sampling"] = d1

    # ===== D2 channel subsets =====
    print("D2 channels…")
    subsets = {
        "all6": CHANNELS, "raw3": RAW_CHANNELS, "user3": USER_CHANNELS,
        "gUserZ": ["gUserZ"], "gUserX": ["gUserX"], "gUserY": ["gUserY"],
    }
    d2 = []
    for name, chs in subsets.items():
        idx = [i for i, c in enumerate(cols) if c.split(":")[0] in chs]
        a, s, f = group_rf(X0[:, idx], y, g)
        d2.append(dict(subset=name, n_ch=len(chs), acc=a, acc_std=s, f1=f,
                       bitrate_kbps=raw_bitrate(100, len(chs))/1e3))
        print(f"  {name:>7} ({len(chs)}ch) -> {a:.1f}±{s:.1f}")
    results["D2_channels"] = d2

    # ===== D3 window length =====
    print("D3 window length…")
    d3 = []
    for win_sec in [4.0, 2.0, 1.0, 0.5]:
        if win_sec == 2.0:
            a, s, f = results["baseline"]["acc"], results["baseline"]["acc_std"], results["baseline"]["f1"]
        else:
            d = build_feature_matrix(recs, win_sec=win_sec)
            a, s, f = group_rf(d["X"], d["y"], d["groups"])
        d3.append(dict(win_sec=win_sec, acc=a, acc_std=s, f1=f, latency_s=win_sec))
        print(f"  win={win_sec}s -> {a:.1f}±{s:.1f}")
    results["D3_window"] = d3

    # ===== D4 feature set =====
    print("D4 feature set…")
    idx_paper = [i for i, c in enumerate(cols) if c.split(":")[1] in PAPER_FEATURES]
    a, s, f = group_rf(X0[:, idx_paper], y, g)
    results["D4_features"] = [
        dict(feature_set="full", n_feat=len(cols), acc=results["baseline"]["acc"],
             acc_std=results["baseline"]["acc_std"], f1=results["baseline"]["f1"]),
        dict(feature_set="paper6", n_feat=len(idx_paper), acc=a, acc_std=s, f1=f),
    ]
    print(f"  paper6 ({len(idx_paper)} feat) -> {a:.1f}±{s:.1f}")

    # ===== D5 quantization =====
    print("D5 quantization…")
    d5 = [dict(bits=32, acc=results["baseline"]["acc"], acc_std=results["baseline"]["acc_std"])]
    for bits in [8, 6, 4]:
        d = build_feature_matrix(recs, signal_transform=quantize_transform(bits))
        a, s, f = group_rf(d["X"], d["y"], d["groups"])
        d5.append(dict(bits=bits, acc=a, acc_std=s, f1=f))
        print(f"  {bits}-bit -> {a:.1f}±{s:.1f}")
    results["D5_quantization"] = d5

    # ===== D6 packet loss =====
    print("D6 packet loss…")
    d6 = [dict(loss=0.0, acc=results["baseline"]["acc"], acc_std=results["baseline"]["acc_std"])]
    for p in [0.05, 0.10, 0.20]:
        d = build_feature_matrix(recs, signal_transform=packetloss_transform(p))
        a, s, f = group_rf(d["X"], d["y"], d["groups"])
        d6.append(dict(loss=p, acc=a, acc_std=s, f1=f))
        print(f"  loss={p:.0%} -> {a:.1f}±{s:.1f}")
    results["D6_packetloss"] = d6

    # ===== D7 mounting/coupling robustness (train nominal, test rotated) =====
    print("D7 rotation robustness…")
    d7 = [dict(angle=0, acc=results["baseline"]["acc"], acc_std=results["baseline"]["acc_std"])]
    for ang in [5, 10, 20, 30]:
        drot = build_feature_matrix(recs, signal_transform=rotation_transform(ang))
        a, s, f = group_rf(X0, y, g, Xtest=drot["X"])
        d7.append(dict(angle=ang, acc=a, acc_std=s, f1=f))
        print(f"  rot={ang}deg -> {a:.1f}±{s:.1f}")
    results["D7_rotation"] = d7

    with open(os.path.join(RES, "analysis_D.json"), "w") as fjson:
        json.dump(results, fjson, indent=2)

    _make_figures(results)
    _make_report(results)
    print("done D")


def _make_figures(R):
    # sampling & channels & window Pareto-style panels
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.6))
    d1 = R["D1_sampling"]
    axes[0].errorbar([x["bitrate_kbps"] for x in d1], [x["acc"] for x in d1],
                     yerr=[x["acc_std"] for x in d1], marker="o", capsize=3)
    for x in d1:
        axes[0].annotate(f"{x['fs']:g}Hz", (x["bitrate_kbps"], x["acc"]),
                         fontsize=7, xytext=(3, 3), textcoords="offset points")
    axes[0].set_xlabel("raw stream bitrate (kbps, 6ch·int16)")
    axes[0].set_ylabel("GROUP accuracy (%)"); axes[0].set_title("D1 sampling rate")

    d3 = R["D3_window"]
    axes[1].errorbar([x["latency_s"] for x in d3], [x["acc"] for x in d3],
                     yerr=[x["acc_std"] for x in d3], marker="s", color=viz.PALETTE[1], capsize=3)
    axes[1].set_xlabel("window / detection latency (s)")
    axes[1].set_title("D3 window length")

    d2 = R["D2_channels"]
    names = [x["subset"] for x in d2]
    axes[2].bar(range(len(d2)), [x["acc"] for x in d2],
                yerr=[x["acc_std"] for x in d2], capsize=3, color=viz.PALETTE[2])
    axes[2].set_xticks(range(len(d2))); axes[2].set_xticklabels(names, rotation=30, ha="right")
    axes[2].set_title("D2 channel subset")
    for ax in axes:
        ax.axhline(100/6, ls="--", c="0.6", lw=1)
    viz.savefig(fig, os.path.join(RES, "fig_tradeoffs_main.png"))

    # robustness panel: quant, loss, rotation
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.4))
    d5 = R["D5_quantization"]
    axes[0].errorbar([x["bits"] for x in d5], [x["acc"] for x in d5],
                     yerr=[x.get("acc_std", 0) for x in d5], marker="o", capsize=3)
    axes[0].set_xlabel("bits/sample"); axes[0].set_ylabel("GROUP accuracy (%)")
    axes[0].set_title("D5 quantization"); axes[0].invert_xaxis()
    d6 = R["D6_packetloss"]
    axes[1].errorbar([100*x["loss"] for x in d6], [x["acc"] for x in d6],
                     yerr=[x.get("acc_std", 0) for x in d6], marker="s",
                     color=viz.PALETTE[1], capsize=3)
    axes[1].set_xlabel("packet loss (%)"); axes[1].set_title("D6 packet loss")
    d7 = R["D7_rotation"]
    axes[2].errorbar([x["angle"] for x in d7], [x["acc"] for x in d7],
                     yerr=[x.get("acc_std", 0) for x in d7], marker="^",
                     color=viz.PALETTE[3], capsize=3)
    axes[2].set_xlabel("mounting rotation (deg)"); axes[2].set_title("D7 coupling robustness")
    for ax in axes:
        ax.axhline(100/6, ls="--", c="0.6", lw=1)
    viz.savefig(fig, os.path.join(RES, "fig_tradeoffs_robustness.png"))


def _row(x, keys, pct=("acc", "acc_std", "f1")):
    out = []
    for k in keys:
        v = x.get(k)
        out.append("" if v is None else (f"{v:.1f}" if k in pct else f"{v}"))
    return out


def _make_report(R):
    L = ["# Analysis D — Accuracy-resource trade-offs (GROUP protocol, RF)", ""]
    L.append(f"Baseline (100 Hz, 6ch, 2 s, full features): "
             f"**{R['baseline']['acc']:.1f} ± {R['baseline']['acc_std']:.1f}%** GROUP accuracy.")
    L += ["", "## D1 · Sampling rate", "",
          "| fs (Hz) | raw kbps | acc | ±std | F1 |", "|---|---|---|---|---|"]
    for x in R["D1_sampling"]:
        L.append(f"| {x['fs']:g} | {x['bitrate_kbps']:.1f} | {x['acc']:.1f} | {x['acc_std']:.1f} | {x['f1']:.1f} |")
    L += ["", "## D2 · Channel subset", "",
          "| subset | #ch | raw kbps | acc | ±std |", "|---|---|---|---|---|"]
    for x in R["D2_channels"]:
        L.append(f"| {x['subset']} | {x['n_ch']} | {x['bitrate_kbps']:.1f} | {x['acc']:.1f} | {x['acc_std']:.1f} |")
    L += ["", "## D3 · Window length", "",
          "| window (s) | latency (s) | acc | ±std |", "|---|---|---|---|"]
    for x in R["D3_window"]:
        L.append(f"| {x['win_sec']} | {x['latency_s']} | {x['acc']:.1f} | {x['acc_std']:.1f} |")
    L += ["", "## D4 · Feature set", "",
          "| set | #feat | acc | ±std |", "|---|---|---|---|"]
    for x in R["D4_features"]:
        L.append(f"| {x['feature_set']} | {x['n_feat']} | {x['acc']:.1f} | {x['acc_std']:.1f} |")
    L += ["", "## D5 · Quantization", "", "| bits | acc | ±std |", "|---|---|---|"]
    for x in R["D5_quantization"]:
        L.append(f"| {x['bits']} | {x['acc']:.1f} | {x.get('acc_std',0):.1f} |")
    L += ["", "## D6 · Packet loss", "", "| loss | acc | ±std |", "|---|---|---|"]
    for x in R["D6_packetloss"]:
        L.append(f"| {x['loss']:.0%} | {x['acc']:.1f} | {x.get('acc_std',0):.1f} |")
    L += ["", "## D7 · Mounting/coupling robustness (train 0°, test rotated)", "",
          "| rotation (deg) | acc | ±std |", "|---|---|---|"]
    for x in R["D7_rotation"]:
        L.append(f"| {x['angle']} | {x['acc']:.1f} | {x.get('acc_std',0):.1f} |")
    with open(os.path.join(RES, "analysis_D.md"), "w") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
