"""PMSG vs SCIG: same winding short-circuits, different generator topology.

Reads results/features_files.csv and results/features_windows.csv.gz (from scripts/features.py)
and produces results/tables/*.csv, results/figures/*.png and results/summary.md.

Detectability statistic — signal-to-drift ratio (SDR)
  For every recording and feature f:
      delta      = (mean_f[FLT] - mean_f[PRE-late]) / |mean_f[PRE-late]|      change under fault
      delta_null = (mean_f[PRE-late] - mean_f[PRE-early]) / |mean_f[PRE-early]|  change with no fault
  PRE-late is the ~0.36 s immediately before the relay command (same duration as FLT), PRE-early the
  0.32 s before that. delta_null is pooled over all 225 recordings of a machine (every recording's
  pre-fault segment is healthy), giving a 225-sample null of ordinary within-recording drift.
      SDR = |delta| / q95(|delta_null|)        SDR >= 1  <=>  detectable at ~5 % per-recording false alarm
  SDR is scale-free, so it can be compared across features, operating points and topologies.

Analyses
  A  physical severity equivalence   same tap pair -> fault current in each topology
  B  where the signature shows up    median SDR per feature / signal group
  C  detectability vs fault extent   SDR versus winding fraction between taps
  D  operating-point dependence      share of recordings detectable over the 3x3 grid
  E  cross-topology transfer         window-level detector trained on one machine, tested on the other
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

RES = Path("results")
TAB = RES / "tables"
FIG = RES / "figures"
TAB.mkdir(exist_ok=True, parents=True)
FIG.mkdir(exist_ok=True, parents=True)

# Validated categorical slots 1 and 2 (dataviz reference palette) + chart chrome.
COL = {"PMSG": "#2a78d6", "SCIG": "#eb6834"}
INK, INK2, MUTED, GRID, AXIS, SURF = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7", "#fcfcfb"
SEQ = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5", "#2a78d6",
       "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]
RATED_A = {"PMSG": 6.3, "SCIG": 7.7}   # nameplate armature current (YY), from the data papers
PRE_SPLIT = 0.62                      # s: PRE-early = windows starting before, PRE-late = after

plt.rcParams.update({
    "font.family": "sans-serif", "font.size": 9, "axes.edgecolor": AXIS, "axes.labelcolor": INK2,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.titlecolor": INK, "axes.titlesize": 10,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": GRID,
    "grid.linewidth": 0.6, "axes.axisbelow": True, "figure.facecolor": SURF, "axes.facecolor": SURF,
    "legend.frameon": False, "legend.fontsize": 8, "savefig.dpi": 160, "savefig.bbox": "tight",
})

GROUPS = {
    "stator current": ["I2_I1", "I0_I1", "I_unbal_rms", "Ia_h3", "Ia_h5", "Ia_h7", "Ia_thd"],
    "dq / control": ["Id_2fe", "Iq_2fe", "Id_1fe", "Iq_1fe", "Id_std", "Iq_std",
                     "Vd_2fe", "Vq_2fe", "PId_2fe", "PIq_2fe", "PId_std", "PIq_std", "D2_D1", "V2_V1"],
    "mechanical": ["Te_2fe", "Te_1fe", "Te_std", "Spd_std", "Vdc_std"],
}
ALL_FEATS = [f for g in GROUPS.values() for f in g]
GROUP_OF = {f: g for g, fs in GROUPS.items() for f in fs}
FT_LABEL = {"TURNS": "Inter-turn", "WINDINGS": "Inter-winding"}


def header(fig, title, sub, top):
    fig.text(0.01, 0.985, title, fontsize=11, color=INK, va="top")
    fig.text(0.01, 0.985 - 0.9 / fig.get_size_inches()[1] * 0.28, sub, fontsize=8, color=INK2, va="top")
    fig.subplots_adjust(top=top)


def load():
    files = pd.read_csv(RES / "features_files.csv")
    win = pd.read_csv(RES / "features_windows.csv.gz")
    files["is_fault"] = files.ftype != "HEALTHY"
    # File names are identical across the two machines: every per-recording key must include the machine.
    win["rid"] = win.machine + "/" + win.file
    return files, win


# ----------------------------------------------------------------------------- SDR
def sdr_table(win):
    """Per-recording relative changes and the pooled null -> SDR per feature."""
    w = win.replace([np.inf, -np.inf], np.nan)
    pre_e = w[(w.segment == "PRE") & (w.t_start < PRE_SPLIT)].groupby("rid")[ALL_FEATS].mean()
    pre_l = w[(w.segment == "PRE") & (w.t_start >= PRE_SPLIT)].groupby("rid")[ALL_FEATS].mean()
    flt = w[w.segment == "FLT"].groupby("rid")[ALL_FEATS].mean()
    meta = w.groupby("rid")[["machine", "file", "case", "ftype", "sev_pct", "phases", "speed_rpm", "torque_Nm"]].first()
    delta = (flt - pre_l) / pre_l.abs()
    null = (pre_l - pre_e) / pre_e.abs()
    q95 = null.abs().groupby(meta.machine).quantile(0.95)          # machine x feature
    sdr = delta.abs() / q95.reindex(meta.machine).set_axis(delta.index)
    sign = np.sign(delta)
    out = meta.join(sdr.add_suffix("__sdr")).join(delta.add_suffix("__delta")).join(null.add_suffix("__null"))
    out["is_fault"] = out.ftype != "HEALTHY"
    out.to_csv(TAB / "sdr_per_recording.csv")
    q95.to_csv(TAB / "sdr_null_q95.csv")
    return out, q95, sign


# ----------------------------------------------------------------------------- A: severity
def severity(files):
    f = files[files.is_fault].copy()
    f["Ifault_pu"] = f.Ifault_rms_flt / f.machine.map(RATED_A)
    f["Ifault_over_I1"] = f.Ifault_rms_flt / f.I1_pre
    g = f.groupby(["case", "ftype", "sev_pct", "phases", "machine"]).agg(
        Ifault_A=("Ifault_rms_flt", "mean"), Ifault_min=("Ifault_rms_flt", "min"),
        Ifault_max=("Ifault_rms_flt", "max"), Ifault_pu=("Ifault_pu", "mean"),
        Ifault_over_I1=("Ifault_over_I1", "mean"), onset_ms=("onset_delay_ms", "mean")).reset_index()
    wide = g.pivot_table(index=["case", "ftype", "sev_pct", "phases"], columns="machine",
                         values=["Ifault_A", "Ifault_pu", "Ifault_over_I1"]).reset_index()
    wide.columns = ["_".join(c).strip("_") if isinstance(c, tuple) else c for c in wide.columns]
    wide["ratio_SCIG_over_PMSG"] = wide["Ifault_A_SCIG"] / wide["Ifault_A_PMSG"]
    wide = wide.sort_values(["ftype", "sev_pct"])
    wide.to_csv(TAB / "A_fault_current_by_case.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 5.4))
    fig.subplots_adjust(wspace=0.6)
    for ax, ft in zip(axes, ["TURNS", "WINDINGS"]):
        sub = g[g.ftype == ft].sort_values("sev_pct")
        cases = list(dict.fromkeys(sub.case))
        y = {c: i for i, c in enumerate(cases)}
        for m in ["PMSG", "SCIG"]:
            s = sub[sub.machine == m]
            ax.hlines([y[c] for c in s.case], s.Ifault_min, s.Ifault_max, color=COL[m], lw=1.2, alpha=0.5)
            ax.plot(s.Ifault_A, [y[c] for c in s.case], "o", ms=5, color=COL[m], label=m, zorder=3)
        ax.set_yticks(range(len(cases)))
        ax.set_yticklabels([f"{c.split('_', 1)[1].replace('_', '–')}  ({sv:.1f} %)" for c, sv in
                            zip(cases, [sub[sub.case == c].sev_pct.iloc[0] for c in cases])], fontsize=7.5)
        ax.set_title(f"{FT_LABEL[ft]} short-circuits")
        ax.set_xlabel("Fault current, RMS during the 400 ms fault (A)")
        ax.grid(axis="y", visible=False)
    axes[0].set_ylabel("Tap pair (winding fraction between taps)")
    axes[0].legend(loc="lower right")
    header(fig, "Same tap pair, different topology: the fault current differs",
           "Dot = mean over the 9 operating points, bar = min–max. Rated current: PMSG 6.3 A, SCIG 7.7 A.", top=0.86)
    fig.savefig(FIG / "A_fault_current_by_case.png")
    plt.close(fig)
    return wide


# ----------------------------------------------------------------------------- B: where the signature is
def where_signature(sdr):
    rows = []
    for m in ["PMSG", "SCIG"]:
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            for feat in ALL_FEATS:
                s = f[f"{feat}__sdr"].dropna()
                rows.append(dict(machine=m, ftype=ft, feature=feat, group=GROUP_OF[feat],
                                 median_sdr=s.median(), q25=s.quantile(.25), q75=s.quantile(.75),
                                 frac_detectable=(s >= 1).mean(),
                                 healthy_false_alarm=(h[f"{feat}__sdr"] >= 1).mean(),
                                 median_delta=f[f"{feat}__delta"].median()))
    det = pd.DataFrame(rows)
    det.to_csv(TAB / "B_sdr_by_feature.csv", index=False)

    # Which signal group carries the strongest signature, recording by recording?
    rows = []
    for (m, ft), f in sdr[sdr.is_fault].groupby(["machine", "ftype"]):
        best_group = f[[f"{x}__sdr" for x in ALL_FEATS]].set_axis(ALL_FEATS, axis=1).idxmax(axis=1).map(GROUP_OF)
        for gname in GROUPS:
            rows.append(dict(machine=m, ftype=ft, group=gname, share_of_recordings_where_group_is_strongest=(best_group == gname).mean()))
    best = pd.DataFrame(rows)
    best.to_csv(TAB / "B_strongest_group_share.csv", index=False)

    fig, axes = plt.subplots(3, 2, figsize=(9.5, 9.2), sharex=True,
                             gridspec_kw={"height_ratios": [len(v) for v in GROUPS.values()], "hspace": 0.18, "wspace": 0.08})
    for j, ft in enumerate(["TURNS", "WINDINGS"]):
        sub = det[det.ftype == ft]
        for i, (gname, feats) in enumerate(GROUPS.items()):
            ax = axes[i, j]
            ypos = {f: k for k, f in enumerate(feats[::-1])}
            for m in ["PMSG", "SCIG"]:
                s = sub[sub.machine == m].set_index("feature").loc[feats]
                ax.hlines([ypos[f] for f in feats], s.q25.clip(lower=0.02), s.q75, color=COL[m], lw=1.2, alpha=0.45)
                ax.plot(s.median_sdr.clip(lower=0.02), [ypos[f] for f in feats], "o", ms=5, color=COL[m], label=m, zorder=3)
            ax.axvline(1, color=AXIS, lw=0.8, ls="--")
            ax.set_xscale("log")
            ax.set_xlim(0.03, 60)
            ax.set_ylim(-0.6, len(feats) - 0.4)
            ax.set_yticks(range(len(feats)))
            ax.set_yticklabels(feats[::-1] if j == 0 else [], fontsize=8)
            ax.grid(axis="y", visible=False)
            if i == 0:
                ax.set_title(f"{FT_LABEL[ft]} faults (108 recordings)")
            if j == 1:
                ax.text(1.02, 0.5, gname, transform=ax.transAxes, rotation=270, va="center", fontsize=8, color=MUTED)
    fig.text(0.5, 0.045, "Signal-to-drift ratio (median over recordings; ≥ 1 = detectable)", ha="center", fontsize=9, color=INK2)
    axes[0, 0].legend(loc="lower right")
    header(fig, "Where the short-circuit becomes visible depends on the topology",
           "Dot = median SDR over recordings, bar = interquartile range. SDR = |relative change under fault| ÷ "
           "95th percentile of |relative change with no fault| (225 recordings per machine).", top=0.91)
    fig.savefig(FIG / "B_sdr_by_feature.png")
    plt.close(fig)
    return det, best


# ----------------------------------------------------------------------------- C: severity curve
MAX_FALSE_ALARM = 0.2   # a feature that fires on > 1 of the 9 healthy recordings of either machine is not trusted


def severity_curve(sdr, det, n_feats=4):
    unreliable = set(det[det.healthy_false_alarm > MAX_FALSE_ALARM].feature)
    pooled = (det[~det.feature.isin(unreliable)].groupby("feature").median_sdr.median()
              .sort_values(ascending=False))
    feats = list(pooled.index[:n_feats])
    pd.Series(sorted(unreliable), name="feature_excluded_for_healthy_false_alarms").to_csv(
        TAB / "C_excluded_features.csv", index=False)
    f = sdr[sdr.is_fault]
    rows = []
    for m in ["PMSG", "SCIG"]:
        for ft in ["TURNS", "WINDINGS"]:
            for feat in feats:
                s = f[(f.machine == m) & (f.ftype == ft)]
                med = s.groupby("sev_pct")[f"{feat}__sdr"].median()
                ok = med[med >= 1]
                rows.append(dict(machine=m, ftype=ft, feature=feat,
                                 min_detectable_sev_pct=ok.index.min() if len(ok) else np.nan,
                                 n_sev_levels=len(med), n_levels_detectable=len(ok),
                                 spearman_sdr_vs_sev=s[["sev_pct", f"{feat}__sdr"]].corr(method="spearman").iloc[0, 1]))
    mds = pd.DataFrame(rows)
    mds.to_csv(TAB / "C_min_detectable_severity.csv", index=False)

    fig, axes = plt.subplots(len(feats), 2, figsize=(9, 2.3 * len(feats)), sharex="col", sharey=True,
                             gridspec_kw={"hspace": 0.25, "wspace": 0.08})
    rng = np.random.RandomState(0)
    for i, feat in enumerate(feats):
        for j, ft in enumerate(["TURNS", "WINDINGS"]):
            ax = axes[i, j]
            for m in ["PMSG", "SCIG"]:
                s = f[(f.machine == m) & (f.ftype == ft)]
                jit = np.exp((rng.rand(len(s)) - 0.5) * 0.08)
                ax.plot(s.sev_pct * jit, s[f"{feat}__sdr"].clip(lower=0.02), "o", ms=2.5, alpha=0.3, color=COL[m], mec="none")
                med = s.groupby("sev_pct")[f"{feat}__sdr"].median()
                ax.plot(med.index, med.values.clip(0.02), "D", ms=6, color=COL[m], mec=SURF, mew=0.8, label=m, zorder=3)
            ax.axhline(1, color=AXIS, lw=0.8, ls="--")
            ax.set_xscale("log"); ax.set_yscale("log")
            ax.set_ylim(0.03, 400)
            ax.set_xticks([2, 3, 5, 10, 20, 40]); ax.set_xticklabels(["2", "3", "5", "10", "20", "40"])
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            if i == 0:
                ax.set_title(FT_LABEL[ft])
            if j == 0:
                ax.set_ylabel(f"{feat}\nSDR")
            if i == len(feats) - 1:
                ax.set_xlabel("Winding fraction between the shorted taps (%)")
    axes[0, 0].legend(loc="upper left")
    header(fig, "Detectability versus fault extent, per topology",
           "Small dots = recordings (9 operating points per tap pair); diamonds = median per tap pair. Dashed = SDR 1.", top=0.90)
    fig.savefig(FIG / "C_sdr_vs_severity.png")
    plt.close(fig)
    return mds, feats


# ----------------------------------------------------------------------------- D: operating point
def operating_point(sdr, feats):
    f = sdr[sdr.is_fault].copy()
    f["best_sdr"] = f[[f"{x}__sdr" for x in feats]].max(axis=1)
    f["detectable"] = f.best_sdr >= 1
    grid = f.groupby(["machine", "speed_rpm", "torque_Nm"]).agg(
        median_best_sdr=("best_sdr", "median"), frac_detectable=("detectable", "mean")).reset_index()
    grid.to_csv(TAB / "D_operating_point_grid.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.9))
    fig.subplots_adjust(top=0.74, wspace=0.35)
    cmap = matplotlib.colors.ListedColormap(SEQ)
    for ax, m in zip(axes, ["PMSG", "SCIG"]):
        p = grid[grid.machine == m].pivot(index="torque_Nm", columns="speed_rpm", values="frac_detectable")
        ax.imshow(p.values, cmap=cmap, vmin=0.4, vmax=1.0, aspect="auto")
        ax.set_xticks(range(3)); ax.set_xticklabels([f"{c} rpm" for c in p.columns])
        ax.set_yticks(range(3)); ax.set_yticklabels([f"{r:.1f} Nm" for r in p.index])
        ax.set_title(m, color=COL[m])
        ax.grid(False)
        for (i, j), v in np.ndenumerate(p.values):
            ax.text(j, i, f"{v:.0%}", ha="center", va="center", fontsize=9, color=INK if v < 0.8 else "#ffffff")
    header(fig, "Share of fault recordings detectable, by operating point",
           f"Detectable = SDR ≥ 1 on the best of {', '.join(feats)}. 24 recordings per cell.", top=0.74)
    fig.savefig(FIG / "D_operating_point_grid.png")
    plt.close(fig)
    return grid


# ----------------------------------------------------------------------------- E: transfer
def build_window_table(win):
    """Label 1 = FLT window of a FAULT recording; 0 = PRE windows of every recording plus FLT windows
    of HEALTHY recordings (the relay clicks but nothing is shorted)."""
    w = win[win.segment.isin(["PRE", "FLT"])].copy()
    w["y"] = ((w.segment == "FLT") & (w.ftype != "HEALTHY")).astype(int)
    w["group"] = w.case + "|" + w.machine
    w = w.replace([np.inf, -np.inf], np.nan).dropna(subset=ALL_FEATS)
    return w, ALL_FEATS


def calibrate(w, feats, mode):
    x = w[feats].copy()
    if mode == "raw":
        return x
    if mode == "healthy-z":   # per machine: z-score against that machine's healthy recordings
        out = x.copy()
        for m in w.machine.unique():
            ref = w[(w.machine == m) & (w.ftype == "HEALTHY")][feats]
            mu, sd = ref.mean(), ref.std().replace(0, 1)
            out.loc[w.machine == m] = (x.loc[w.machine == m] - mu) / sd
        return out
    if mode == "self-ref":    # per recording: |z| against its own pre-fault windows (change detection)
        pre_mean = w[w.segment == "PRE"].groupby("rid")[feats].mean()
        pre_sd = w[w.segment == "PRE"].groupby("rid")[feats].std().replace(0, np.nan)
        z = (x - pre_mean.reindex(w.rid).values) / pre_sd.reindex(w.rid).values
        return z.abs().fillna(0)
    raise ValueError(mode)


def tpr_at_fpr(y, s, fpr_target=0.01):
    fpr, tpr, _ = roc_curve(y, s)
    return float(np.interp(fpr_target, fpr, tpr))


def transfer(win):
    w, feats = build_window_table(win)
    models = {
        "logistic": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=1.0)),
        "gbdt": lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08),
    }
    rows = []
    for mode in ["raw", "healthy-z", "self-ref"]:
        X = calibrate(w, feats, mode)
        for mname, mk in models.items():
            for m in ["PMSG", "SCIG"]:      # within machine, unseen fault cases
                idx = (w.machine == m).to_numpy()
                Xm, ym, gm = X[idx].to_numpy(), w.y[idx].to_numpy(), w.group[idx].to_numpy()
                scores = np.zeros(len(ym))
                for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
                    scores[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
                rows.append(dict(calibration=mode, model=mname, train=m, test=m, setting="within (unseen cases)",
                                 auc=roc_auc_score(ym, scores), tpr_at_1pct_fpr=tpr_at_fpr(ym, scores), n_test=len(ym)))
            for tr_m, te_m in [("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                tr, te = (w.machine == tr_m).to_numpy(), (w.machine == te_m).to_numpy()
                s = mk().fit(X[tr].to_numpy(), w.y[tr].to_numpy()).predict_proba(X[te].to_numpy())[:, 1]
                rows.append(dict(calibration=mode, model=mname, train=tr_m, test=te_m, setting="cross-topology",
                                 auc=roc_auc_score(w.y[te], s), tpr_at_1pct_fpr=tpr_at_fpr(w.y[te], s), n_test=int(te.sum())))
    tr = pd.DataFrame(rows)
    tr.to_csv(TAB / "E_transfer.csv", index=False)

    X = calibrate(w, feats, "healthy-z")
    coefs = {}
    for m in ["PMSG", "SCIG"]:
        idx = (w.machine == m).to_numpy()
        clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=0.3)).fit(X[idx], w.y[idx])
        coefs[m] = pd.Series(clf[-1].coef_[0], index=feats)
    coef = pd.DataFrame(coefs)
    coef["abs_mean"] = coef.abs().mean(axis=1)
    coef = coef.sort_values("abs_mean", ascending=False)
    coef.to_csv(TAB / "E_logistic_coefficients_healthy_z.csv")
    cos = float(np.dot(coef.PMSG, coef.SCIG) / (np.linalg.norm(coef.PMSG) * np.linalg.norm(coef.SCIG)))

    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2), sharey=True)
    fig.subplots_adjust(top=0.8, bottom=0.26, wspace=0.08)
    settings = [("PMSG", "PMSG"), ("SCIG", "SCIG"), ("PMSG", "SCIG"), ("SCIG", "PMSG")]
    labels = ["PMSG → PMSG", "SCIG → SCIG", "PMSG → SCIG", "SCIG → PMSG"]
    shades = {"raw": SEQ[3], "healthy-z": SEQ[7], "self-ref": SEQ[11]}
    width = 0.26
    for ax, mname in zip(axes, ["logistic", "gbdt"]):
        sub = tr[tr.model == mname]
        xs = np.arange(len(settings))
        for k, mode in enumerate(["raw", "healthy-z", "self-ref"]):
            vals = [sub[(sub.calibration == mode) & (sub.train == a) & (sub.test == b)].auc.iloc[0] for a, b in settings]
            bars = ax.bar(xs + (k - 1) * width, vals, width * 0.9, color=shades[mode], label=mode, linewidth=0)
            for b_, v in zip(bars, vals):
                ax.text(b_.get_x() + b_.get_width() / 2, max(v, 0.505) + 0.006, f"{v:.2f}", ha="center", va="bottom",
                        fontsize=6.5, color=INK2)
        ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=8)
        ax.set_ylim(0.5, 1.03)
        ax.set_title(f"{mname} classifier")
        ax.grid(axis="x", visible=False)
        ax.axvline(1.5, color=GRID, lw=0.8)
        ax.text(0.5, -0.2, "within topology (unseen fault cases)", transform=ax.transAxes, ha="right", va="top", fontsize=7.5, color=MUTED)
        ax.text(0.52, -0.2, "cross topology (train → test)", transform=ax.transAxes, ha="left", va="top", fontsize=7.5, color=MUTED)
    axes[0].set_ylabel("ROC AUC, window level")
    axes[1].legend(title="feature calibration", loc="upper center", bbox_to_anchor=(-0.04, -0.27), ncol=3, title_fontsize=7.5)
    header(fig, "Does a detector trained on one topology transfer to the other?",
           "raw = physical units · healthy-z = z-scored on the target machine's healthy recordings · "
           "self-ref = |z| against each recording's own pre-fault segment", top=0.8)
    fig.savefig(FIG / "E_transfer.png")
    plt.close(fig)
    return tr, coef, cos, w


# ----------------------------------------------------------------------------- report
def md_table(df, floatfmt="{:.3f}"):
    cols = list(df.columns)
    out = ["| " + " | ".join(str(c) for c in cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, (float, np.floating)):
                cells.append(floatfmt.format(v) if np.isfinite(v) else "")
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def report(files, sdr, q95, sev, det, best, mds, feats, grid, tr, coef, cos, w):
    L = ["# PMSG vs SCIG under identical winding short-circuits — first comparison\n",
         "Recordings: 225 per machine (24 fault cases + healthy, × 3 speeds × 3 torques). Windows of 5 electrical "
         "cycles, hop 1 cycle. PRE-early = 0.30–0.62 s, PRE-late = 0.62–0.98 s, FLT = relay-on + 30 ms to relay-off − 10 ms. "
         "Features use only stator-side / controller signals; `Ifault` and `Fault_relay` are ground truth.\n",
         "**Detectability statistic.** Signal-to-drift ratio SDR = |relative change of a feature between PRE-late and FLT| "
         "÷ 95th percentile of |relative change between PRE-early and PRE-late| over all 225 recordings of that machine. "
         "SDR ≥ 1 means the change under fault exceeds what ordinary within-recording drift produces in 95 % of healthy "
         "segments, i.e. detectable at ≈5 % per-recording false alarm. It is scale-free and directly comparable across "
         "features, operating points and topologies.\n",
         "**Caveat on every number:** one physical machine per topology, no repeated tests. Differences between the two "
         "columns are differences between *these two machines*; attributing them to topology needs the simulation "
         "populations planned for the paper.\n"]

    L.append("## A. Same tap pair ≠ same physical severity\n")
    a = sev
    L.append(f"Mean fault current over the 24 cases: PMSG {a.Ifault_A_PMSG.mean():.2f} A, SCIG {a.Ifault_A_SCIG.mean():.2f} A "
             f"(SCIG/PMSG median {a.ratio_SCIG_over_PMSG.median():.2f}, range {a.ratio_SCIG_over_PMSG.min():.2f}–{a.ratio_SCIG_over_PMSG.max():.2f}). "
             f"In per-unit of rated current: PMSG {a.Ifault_pu_PMSG.mean():.2f}, SCIG {a.Ifault_pu_SCIG.mean():.2f}. "
             f"Relative to the pre-fault stator current I1: PMSG {a.Ifault_over_I1_PMSG.mean():.2f}, SCIG {a.Ifault_over_I1_SCIG.mean():.2f} "
             "— the SCIG's magnetising current makes the same fault a much smaller fraction of what the stator sensors see.\n")
    L.append(md_table(a[["case", "sev_pct", "phases", "Ifault_A_PMSG", "Ifault_A_SCIG", "ratio_SCIG_over_PMSG",
                        "Ifault_over_I1_PMSG", "Ifault_over_I1_SCIG"]].round(3)))
    L.append("\n![A](figures/A_fault_current_by_case.png)\n")

    L.append("## B. Where the signature shows up, per topology\n")
    L.append("Null (95th percentile of |no-fault relative change|) per machine, selected features:\n")
    q = q95[["I2_I1", "V2_V1", "Id_2fe", "Iq_2fe", "PIq_2fe", "Vq_2fe", "Ia_h3", "Te_2fe", "Vdc_std"]].T.reset_index().rename(columns={"index": "feature"})
    L.append(md_table(q.round(3)))
    top = (det.sort_values("median_sdr", ascending=False).groupby(["machine", "ftype"]).head(6)
           [["machine", "ftype", "feature", "group", "median_sdr", "frac_detectable", "healthy_false_alarm", "median_delta"]])
    L.append("\nTop-6 features by median SDR per machine and fault type (`median_delta` = median relative change, sign = direction):\n")
    L.append(md_table(top.round(3)))
    L.append("\nShare of fault recordings in which each signal group holds the strongest signature:\n")
    L.append(md_table(best.round(3)))
    L.append("\n![B](figures/B_sdr_by_feature.png)\n")

    L.append("## C. Minimum detectable fault extent\n")
    L.append(f"Features with the highest pooled median SDR (both machines): {', '.join(feats)}. Smallest tap-pair severity "
             "level whose median SDR is ≥ 1:\n")
    L.append(md_table(mds.round(3)))
    L.append("\n![C](figures/C_sdr_vs_severity.png)\n")

    L.append("## D. Operating-point dependence\n")
    L.append(md_table(grid.round(3)))
    L.append("\n![D](figures/D_operating_point_grid.png)\n")

    L.append("## E. Cross-topology transfer\n")
    L.append(f"Window-level detector (1 = fault window of a fault recording; 0 = pre-fault windows of all recordings and "
             f"fault-time windows of healthy recordings). n windows = {len(w)}; positives = {int(w.y.sum())}. Within-topology "
             "rows use 5-fold GroupKFold over fault cases (unseen tap pairs).\n")
    L.append(md_table(tr.round(3)))
    L.append(f"\nCosine similarity of the two logistic weight vectors (healthy-z features), PMSG vs SCIG: **{cos:.2f}** "
             "(1 = identical feature weighting).\n")
    L.append("Largest-weight features (healthy-z logistic):\n")
    L.append(md_table(coef.head(12).reset_index().rename(columns={"index": "feature"}).round(3)))
    L.append("\n![E](figures/E_transfer.png)\n")
    (RES / "summary.md").write_text("\n".join(L))


if __name__ == "__main__":
    files, win = load()
    sdr, q95, _ = sdr_table(win)
    sev = severity(files)
    det, best = where_signature(sdr)
    mds, feats = severity_curve(sdr, det)
    grid = operating_point(sdr, feats)
    tr, coef, cos, w = transfer(win)
    report(files, sdr, q95, sev, det, best, mds, feats, grid, tr, coef, cos, w)
    print("done ->", RES / "summary.md")
