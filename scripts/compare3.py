"""Three architectural alternatives under the same winding short-circuits: PMSG, SCIG and the
variable-speed wound-field synchronous generator (WFSG, InnovaPower bench C).

The WFSG records are shorter (0.55 s pre-fault, ~0.27 s fault) and sampled at 4 kHz, so all three
alternatives are compared on 3-cycle windows (PMSG/SCIG re-extracted with --ncyc 3) and on the common
feature set. WFSG has no healthy recordings: its null is the pre-fault split only, and the healthy
false-alarm screen is applied only where healthy recordings exist (PMSG, SCIG).

Outputs: results/tables/G_*.csv, results/figures/G_*.png|pdf, results/summary3.md
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupKFold

import compare as C

MACH = ["PMSG", "SCIG", "WFSG"]
COL3 = {"PMSG": "#2a78d6", "SCIG": "#eb6834", "WFSG": "#1baf7a"}   # validated 3-slot categorical palette
WFSG_EXTRA = ["If_2fe", "If_std"]
NOT_ON_WFSG = ["PId_2fe", "PIq_2fe", "PId_std", "PIq_std", "Tm_std", "Tm_2fe", "Tm_1fe"]
COMMON = [f for f in C.ALL_FEATS if f not in NOT_ON_WFSG]
FEATS3 = COMMON + WFSG_EXTRA
GROUP_OF = dict(C.GROUP_OF, If_2fe="excitation", If_std="excitation")
SUITES3 = {
    "drive-internal": [f for f in ["Id_2fe", "Iq_2fe", "Id_1fe", "Iq_1fe", "Id_std", "Iq_std", "Vdconv_2fe", "Vqconv_2fe",
                                   "D2_D1", "Te_2fe", "Te_1fe", "Te_std", "Vdc_std", "Spd_std"]],
    "3 CT": ["I2_I1", "I_unbal_rms", "Ia_h3", "Ia_h5", "Ia_h7", "Ia_thd"],
    "3 CT + 3 VT": ["I2_I1", "I_unbal_rms", "Ia_h3", "Ia_h5", "Ia_h7", "Ia_thd", "V2_V1"],
    "3 CT + 3 VT + drive": None,
    "excitation (WFSG only)": WFSG_EXTRA,
}
SUITES3["3 CT + 3 VT + drive"] = SUITES3["3 CT + 3 VT"] + SUITES3["drive-internal"] + ["Vd_2fe", "Vq_2fe"]
RATED_A = dict(C.RATED_A, WFSG=np.nan)   # bench C armature current not stated in the data paper


ZF_REF = {"PMSG": 2.6, "SCIG": 2.6}      # fault resistance of the PMSG/SCIG protocol
WFSG_ZF_MATCH = 2.83                     # WFSG impedance closest to the PMSG/SCIG value


def load3(wfsg_suffix="_allzf"):
    """All WFSG trials are loaded; the fault impedance is kept as a covariate (in the WFSG benchmark it
    was raised with fault extent, so extent and impedance are confounded on that bench)."""
    w2 = pd.read_csv(C.RES / "features_windows_ncyc3.csv.gz")
    w3 = pd.read_csv(C.RES / f"features_wfsg_windows{wfsg_suffix}.csv.gz")
    # the WFSG benchmark also contains phase-to-phase faults (AB/AC at 11-34 ohm), a class absent from the
    # PMSG/SCIG protocol: they are excluded everywhere (null, ranking, MDE, transfer)
    w3 = w3[w3.ftype.isin(["TURNS", "WINDINGS", "HEALTHY"])]
    win = pd.concat([w2, w3], ignore_index=True, sort=False)
    win["rid"] = win.machine + "/" + win.file
    win["zf_ohm"] = win.zf_ohm.fillna(win.machine.map(ZF_REF))
    f2 = pd.read_csv(C.RES / "features_files_ncyc3.csv")
    f3 = pd.read_csv(C.RES / f"features_wfsg_files{wfsg_suffix}.csv")
    f3 = f3[f3.ftype.isin(["TURNS", "WINDINGS", "HEALTHY"])]
    files = pd.concat([f2, f3], ignore_index=True, sort=False).copy()
    files["zf_ohm"] = files.zf_ohm.fillna(files.machine.map(ZF_REF))
    files["is_fault"] = files.ftype != "HEALTHY"
    files["sev_pct"] = files.sev_pct.round(1)   # pool equal extents from different tap pairs
    win["sev_pct"] = win.sev_pct.round(1)
    return files, win


def sdr_from_windows(win, feats, q=0.95, pre_split=C.PRE_SPLIT):
    """Per-recording SDR for the given features and null quantile (generalisation of compare.sdr_table).
    For the WFSG the pre-fault split point is 0.30 s (its records start ~0.55 s before the fault)."""
    w = win.replace([np.inf, -np.inf], np.nan)
    split = np.where(w.machine == "WFSG", 0.30, pre_split)
    pre = w.segment == "PRE"
    pre_e = w[pre & (w.t_start < split)].groupby("rid")[feats].mean()
    pre_l = w[pre & (w.t_start >= split)].groupby("rid")[feats].mean()
    flt = w[w.segment == "FLT"].groupby("rid")[feats].mean()
    meta_cols = [c for c in ["machine", "file", "case", "ftype", "sev_pct", "phases", "speed_rpm", "torque_Nm",
                             "torque_pu", "zf_ohm", "rep"] if c in w.columns]
    meta = w.groupby("rid")[meta_cols].first()
    delta = (flt - pre_l) / pre_l.abs()
    null = (pre_l - pre_e) / pre_e.abs()
    qv = null.abs().groupby(meta.machine).quantile(q)
    sdr = delta.abs() / qv.reindex(meta.machine).set_axis(delta.index)
    out = meta.join(sdr.add_suffix("__sdr")).join(delta.add_suffix("__delta"))
    out["is_fault"] = out.ftype != "HEALTHY"
    return out, qv


def per_feature(sdr, feats, qv=None):
    rows = []
    for m in MACH:
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            if not len(f):
                continue
            for feat in feats:
                s = f[f"{feat}__sdr"].dropna()
                if not len(s):
                    continue
                rows.append(dict(machine=m, ftype=ft, feature=feat, group=GROUP_OF[feat], n=len(s), n_trials=len(f),
                                 median_sdr=s.median(), q25=s.quantile(.25), q75=s.quantile(.75),
                                 frac_detectable=(s >= 1).mean(),
                                 healthy_false_alarm=(h[f"{feat}__sdr"] >= 1).mean() if len(h) else np.nan,
                                 healthy_false_alarm_count=int((h[f"{feat}__sdr"] >= 1).sum()) if len(h) else np.nan,
                                 n_healthy=len(h),
                                 null_q=float(qv.loc[m, feat]) if qv is not None and feat in qv.columns else np.nan,
                                 median_delta=f[f"{feat}__delta"].median()))
    return pd.DataFrame(rows)


def unreliable(det, m, alpha=0.95):
    """Features excluded from the design quantities of machine m: (i) healthy false-alarm count incompatible
    with the nominal rate 1 - alpha (binomial screen; not applicable when a machine has no healthy trials),
    (ii) null quantile above one, i.e. the healthy relative change exceeds 100 % (uninformative feature)."""
    d = det[det.machine == m].groupby("feature").first()
    bad = {f for f, r in d.iterrows() if C.screen_flag(r.healthy_false_alarm_count, r.n_healthy, alpha)}
    bad |= {f for f, r in d.iterrows() if np.isfinite(r.null_q) and r.null_q > 1}
    return bad


def min_detectable(s, col):
    """Minimum detectable extent, limit-of-detection convention: the smallest tested extent above which
    every tested extent has median SDR >= 1 over its trials (equal extents from different tap pairs are
    pooled; NaN if the largest extent is not detectable)."""
    med = s.groupby("sev_pct")[col].median().sort_index()
    ok = (med >= 1).to_numpy()
    idx = len(ok)
    for i in range(len(ok) - 1, -1, -1):
        if ok[i]:
            idx = i
        else:
            break
    return float(med.index[idx]) if idx < len(ok) else np.nan


def min_detectable_first(s, col):
    """Smallest tested extent whose median SDR reaches one (the original, non-monotone convention)."""
    med = s.groupby("sev_pct")[col].median()
    ok = med[med >= 1]
    return float(ok.index.min()) if len(ok) else np.nan


def suites(sdr, det):
    rows = []
    for m in MACH:
        bad = unreliable(det, m)
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            if not len(f):
                continue
            # MDE needs a constant fault impedance: for the WFSG only the trials at the impedance matching
            # the PMSG/SCIG protocol are used, and the smallest extent tested at that impedance is reported.
            fm = f if m != "WFSG" else f[np.isclose(f.zf_ohm, WFSG_ZF_MATCH)]
            for suite, feats in SUITES3.items():
                feats = [x for x in feats if x not in bad and f"{x}__sdr" in f.columns and f[f"{x}__sdr"].notna().any()]
                if not feats or (suite.startswith("excitation") and m != "WFSG"):
                    continue
                cols = [f"{x}__sdr" for x in feats]
                med = f[cols].median().set_axis(feats)   # selection rule: highest median SDR among screened features
                best = med.idxmax()
                fixed = f[f"{best}__sdr"]
                oracle = f[cols].max(axis=1)
                rows.append(dict(suite=suite, machine=m, ftype=ft, best_feature=best, n_trials=len(f), n_features=len(feats),
                                 fixed_median_sdr=fixed.median(), fixed_share_detectable=(fixed >= 1).mean(),
                                 fixed_min_detectable_pct=min_detectable(fm.assign(v=fm[f"{best}__sdr"]), "v"),
                                 fixed_min_detectable_first_pct=min_detectable_first(fm.assign(v=fm[f"{best}__sdr"]), "v"),
                                 smallest_extent_tested_pct=fm.sev_pct.min(),
                                 oracle_share_detectable=(oracle >= 1).mean(),
                                 oracle_min_detectable_pct=min_detectable(fm.assign(v=fm[cols].max(axis=1)), "v"),
                                 oracle_healthy_false_alarm=(h[cols].max(axis=1) >= 1).mean() if len(h) else np.nan))
    return pd.DataFrame(rows)


def fault_current(files):
    f = files[files.is_fault].copy()
    # I1_pre is the fundamental amplitude (peak) of the Hann projection; the fault current is an RMS value
    f["Ifault_over_I1"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))
    g = f.groupby(["case", "ftype", "sev_pct", "machine", "zf_ohm"]).agg(Ifault_A=("Ifault_rms_flt", "median"),
                                                                          Ifault_over_I1=("Ifault_over_I1", "median"),
                                                                          n=("file", "size")).reset_index()
    return g


ZF_MARK = {1.0: "^", 2.6: "D", 2.83: "D", 5.66: "s", 11.32: "p"}


def fig_physical_severity(sdr, files, feats):
    """SDR against the measured fault current relative to the pre-fault stator current: a physical
    severity axis that is comparable across benches and independent of the tap-pair/impedance design."""
    f = sdr[sdr.is_fault].join(files.set_index(files.machine + "/" + files.file)[["Ifault_rms_flt", "I1_pre"]])
    f["ratio"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))   # RMS / RMS
    fig, axes = plt.subplots(len(feats), 2, figsize=(9, 2.3 * len(feats)), sharex="col", sharey=True,
                             gridspec_kw={"hspace": 0.25, "wspace": 0.08})
    for i, feat in enumerate(feats):
        for j, ft in enumerate(["TURNS", "WINDINGS"]):
            ax = axes[i, j]
            for m in MACH:
                s = f[(f.machine == m) & (f.ftype == ft)].dropna(subset=[f"{feat}__sdr", "ratio"])
                for zf, g in s.groupby("zf_ohm"):
                    ax.plot(g.ratio, g[f"{feat}__sdr"].clip(lower=0.02), ZF_MARK.get(round(zf, 2), "o"), ms=3.2,
                            alpha=0.55, color=COL3[m], mec="none", label=f"{m}" if zf in (2.6, 2.83) else None)
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.03, 400)
            ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5]); ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "5"])
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            if i == 0:
                ax.set_title(C.FT_LABEL[ft])
            if j == 0:
                ax.set_ylabel(f"{C.lab(feat)}\nSDR")
            if i == len(feats) - 1:
                ax.set_xlabel("Fault current / pre-fault stator current (RMS)")
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    axes[0, 0].legend(uniq.values(), uniq.keys(), loc="upper left")
    C.header(fig, "Detectability against physical fault severity, three topologies",
             "Marker = fault impedance: ▲ 1 Ω, ◆ 2.6/2.83 Ω, ■ 5.66 Ω, ⬟ 11.32 Ω (WFSG impedance rises with extent). Dashed = SDR 1.", top=0.90)
    save(fig, "G_sdr_vs_fault_current_3alt")


def transfer3(win):
    w = win[win.segment.isin(["PRE", "FLT", "POST"])].copy()   # POST (recovery) windows are negatives
    w["y"] = ((w.segment == "FLT") & (w.ftype != "HEALTHY")).astype(int)
    w["group"] = C.make_groups(w)
    feats = COMMON
    w = w.replace([np.inf, -np.inf], np.nan).dropna(subset=feats)
    X = C.calibrate(w, feats, "self-ref")
    mk = lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
    rows = []
    for m in MACH:
        idx = (w.machine == m).to_numpy()
        Xm, ym, gm = X[idx].to_numpy(), w.y[idx].to_numpy(), w.group[idx].to_numpy()
        scores = np.zeros(len(ym))
        for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
            scores[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
        rows.append(dict(train=m, test=m, auc=roc_auc_score(ym, scores), tpr_at_1pct_fpr=C.tpr_at_fpr(ym, scores)))
    for a in MACH:
        for b in MACH:
            if a == b:
                continue
            tr, te = (w.machine == a).to_numpy(), (w.machine == b).to_numpy()
            s = mk().fit(X[tr].to_numpy(), w.y[tr].to_numpy()).predict_proba(X[te].to_numpy())[:, 1]
            rows.append(dict(train=a, test=b, auc=roc_auc_score(w.y[te], s), tpr_at_1pct_fpr=C.tpr_at_fpr(w.y[te], s)))
    for b in MACH:   # leave-one-alternative-out
        tr, te = (w.machine != b).to_numpy(), (w.machine == b).to_numpy()
        s = mk().fit(X[tr].to_numpy(), w.y[tr].to_numpy()).predict_proba(X[te].to_numpy())[:, 1]
        rows.append(dict(train="+".join(m for m in MACH if m != b), test=b, auc=roc_auc_score(w.y[te], s),
                         tpr_at_1pct_fpr=C.tpr_at_fpr(w.y[te], s)))
    return pd.DataFrame(rows), int(w.y.sum()), len(w)


# ----------------------------------------------------------------------------- figures
def save(fig, name):
    fig.savefig(C.FIG / f"{name}.png")
    fig.savefig(C.FIG / f"{name}.pdf")
    plt.close(fig)


def fig_features(det, feats):
    groups = {g: [f for f in feats if GROUP_OF[f] == g]
              for g in ["stator current", "terminal voltage", "dq / control", "mechanical", "excitation"]}
    groups = {k: v for k, v in groups.items() if v}
    fig, axes = plt.subplots(len(groups), 2, figsize=(9.5, 9.6), sharex=True,
                             gridspec_kw={"height_ratios": [len(v) for v in groups.values()], "hspace": 0.2, "wspace": 0.08})
    for j, ft in enumerate(["TURNS", "WINDINGS"]):
        sub = det[det.ftype == ft]
        for i, (gname, fs) in enumerate(groups.items()):
            ax = axes[i, j]
            ypos = {f: k for k, f in enumerate(fs[::-1])}
            for m in MACH:
                s = sub[sub.machine == m].set_index("feature").reindex(fs)
                y = [ypos[f] for f in fs]
                ax.hlines(y, s.q25.clip(lower=0.02), s.q75, color=COL3[m], lw=1.2, alpha=0.45)
                ax.plot(s.median_sdr.clip(lower=0.02), y, "o", ms=5, color=COL3[m], label=m, zorder=3)
            ax.axvline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.set_xscale("log"); ax.set_xlim(0.03, 200)
            ax.set_ylim(-0.6, len(fs) - 0.4)
            ax.set_yticks(range(len(fs))); ax.set_yticklabels([C.lab(f) for f in fs[::-1]] if j == 0 else [], fontsize=8)
            ax.grid(axis="y", visible=False)
            if i == 0:
                ax.set_title(f"{C.FT_LABEL[ft]} faults")
            if j == 1:
                ax.text(1.02, 0.5, gname, transform=ax.transAxes, rotation=270, va="center", fontsize=8, color=C.MUTED)
    fig.text(0.5, 0.045, "Signal-to-drift ratio (median over recordings; ≥ 1 = detectable)", ha="center", fontsize=9, color=C.INK2)
    axes[0, 0].legend(loc="lower right")
    C.header(fig, "Where the short-circuit becomes visible, for three generator topologies",
             "3-cycle windows; ZF = 2.6 Ω (PMSG, SCIG) and 2.83 Ω (WFSG). Dot = median SDR, bar = interquartile range.", top=0.91)
    save(fig, "G_sdr_by_feature_3alt")


def fig_severity(sdr, feats):
    f = sdr[sdr.is_fault]
    fig, axes = plt.subplots(len(feats), 2, figsize=(9, 2.3 * len(feats)), sharex="col", sharey=True,
                             gridspec_kw={"hspace": 0.25, "wspace": 0.08})
    rng = np.random.RandomState(0)
    for i, feat in enumerate(feats):
        for j, ft in enumerate(["TURNS", "WINDINGS"]):
            ax = axes[i, j]
            for m in MACH:
                s = f[(f.machine == m) & (f.ftype == ft)].dropna(subset=[f"{feat}__sdr"])
                if not len(s):
                    continue
                jit = np.exp((rng.rand(len(s)) - 0.5) * 0.08)
                ax.plot(s.sev_pct * jit, s[f"{feat}__sdr"].clip(lower=0.02), "o", ms=2.3, alpha=0.3, color=COL3[m], mec="none")
                for zf, g in s.groupby("zf_ohm"):
                    med = g.groupby("sev_pct")[f"{feat}__sdr"].median()
                    ax.plot(med.index, med.values.clip(0.02), ZF_MARK.get(round(zf, 2), "o"), ms=6, color=COL3[m],
                            mec=C.SURF, mew=0.8, label=m if zf in (2.6, 2.83) else None, zorder=3)
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.03, 400)
            ax.set_xticks([2, 3, 5, 10, 20, 40]); ax.set_xticklabels(["2", "3", "5", "10", "20", "40"])
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            if i == 0:
                ax.set_title(C.FT_LABEL[ft])
            if j == 0:
                ax.set_ylabel(f"{C.lab(feat)}\nSDR")
            if i == len(feats) - 1:
                ax.set_xlabel("Winding fraction between the shorted taps (%)")
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    axes[0, 0].legend(uniq.values(), uniq.keys(), loc="upper left")
    C.header(fig, "Detectability versus fault extent for three generator topologies",
             "Small dots = recordings; large markers = median per tap pair and impedance (▲ 1 Ω, ◆ 2.6/2.83 Ω, ■ 5.66 Ω, ⬟ 11.32 Ω). "
             "3-cycle windows. Dashed = SDR 1.", top=0.90)
    save(fig, "G_sdr_vs_severity_3alt")


def fig_suites(res):
    order = [s for s in SUITES3 if not s.startswith("excitation")]
    xs = np.arange(len(order)); off = {"PMSG": -0.2, "SCIG": 0.0, "WFSG": 0.2}
    fig, axes = plt.subplots(2, 2, figsize=(9.5, 6.4), sharex=True, gridspec_kw={"hspace": 0.25, "wspace": 0.1})
    for j, ft in enumerate(["TURNS", "WINDINGS"]):
        for m in MACH:
            s = res[(res.ftype == ft) & (res.machine == m)].set_index("suite").reindex(order)
            ax = axes[0, j]
            ax.plot(xs + off[m], s.oracle_min_detectable_pct, "o", ms=7, mfc="none", mec=COL3[m], mew=1.3, zorder=3)
            ax.plot(xs + off[m], s.fixed_min_detectable_pct, "o", ms=6, color=COL3[m], label=m, zorder=4)
            ax = axes[1, j]
            ax.plot(xs + off[m], s.oracle_share_detectable, "o", ms=7, mfc="none", mec=COL3[m], mew=1.3, zorder=3)
            ax.plot(xs + off[m], s.fixed_share_detectable, "o", ms=6, color=COL3[m], zorder=4)
        axes[0, j].set_yscale("log"); axes[0, j].set_yticks([2, 3, 5, 10, 20, 40]); axes[0, j].set_yticklabels(["2", "3", "5", "10", "20", "40"])
        axes[0, j].yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter()); axes[0, j].set_ylim(1.6, 60)
        axes[0, j].set_title(f"{C.FT_LABEL[ft]} faults")
        axes[1, j].set_ylim(0, 1.05); axes[1, j].yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
        axes[1, j].set_xticks(xs); axes[1, j].set_xticklabels(order, rotation=20, ha="right", fontsize=8)
    axes[0, 0].set_ylabel("Minimum detectable extent\n(% of winding between taps)")
    axes[1, 0].set_ylabel("Share of fault recordings\ndetectable (SDR ≥ 1)")
    axes[0, 0].legend(loc="upper right")
    C.header(fig, "Monitoring architecture versus what it can detect, three topologies",
             "Filled = one fixed feature per suite (best median SDR); hollow = best feature per recording (upper bound). 3-cycle windows.", top=0.9)
    save(fig, "G_sensor_suites_3alt")


def fig_transfer(tr):
    labels = [f"{r.train}→{r.test}" for r in tr.itertuples()]
    fig, ax = plt.subplots(figsize=(9.5, 3.4))
    fig.subplots_adjust(bottom=0.3, top=0.8)
    xs = np.arange(len(tr))
    colors = [COL3[r.test] for r in tr.itertuples()]
    ax.bar(xs, tr.auc, 0.7, color=colors, linewidth=0)
    for x, v in zip(xs, tr.auc):
        ax.text(x, v + 0.006, f"{v:.2f}", ha="center", va="bottom", fontsize=6.5, color=C.INK2)
    ax.set_xticks(xs); ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=7.5)
    ax.set_ylim(0.5, 1.03); ax.set_ylabel("ROC AUC on the tested machine"); ax.grid(axis="x", visible=False)
    C.header(fig, "Transfer of a change detector between three generator topologies",
             "GBDT on |z| features against each recording's own pre-fault segment, common feature set; colour = tested machine. "
             "Diagonal entries: 5-fold GroupKFold over unseen tap pairs.", top=0.8)
    save(fig, "G_transfer_3alt")


def main():
    files, win = load3()
    feats = [f for f in FEATS3 if f in win.columns]
    sdr, qv = sdr_from_windows(win, feats)
    sdr.to_csv(C.TAB / "G_sdr_per_recording_3alt.csv")
    qv.to_csv(C.TAB / "G_sdr_null_q95_3alt.csv")
    det = per_feature(sdr, feats, qv)
    det.to_csv(C.TAB / "G_sdr_by_feature_3alt.csv", index=False)
    res = suites(sdr, det)
    res.to_csv(C.TAB / "G_sensor_suites_3alt.csv", index=False)
    fc = fault_current(files)
    fc.to_csv(C.TAB / "G_fault_current_3alt.csv", index=False)
    tr, npos, nwin = transfer3(win)
    tr.to_csv(C.TAB / "G_transfer_3alt.csv", index=False)
    key = ["V2_V1", "I2_I1", "Id_2fe", "Vqconv_2fe"]
    fig_features(det, feats)
    fig_severity(sdr, key)
    fig_physical_severity(sdr, files, ["V2_V1", "I2_I1", "Id_2fe"])
    fig_suites(res)
    fig_transfer(tr)
    L = ["# Three alternatives: PMSG, SCIG, WFSG (3-cycle windows, common features)\n",
         f"Recordings: {files.groupby('machine').size().to_dict()}; WFSG at all fault impedances "
         f"(coverage: {files[files.machine == 'WFSG'].groupby(['ftype', 'zf_ohm']).size().to_dict()}).\n",
         "## Null (95th percentile of |no-fault relative change|)\n", C.md_table(qv[key + ["If_2fe"] if "If_2fe" in qv.columns else key].T.reset_index().rename(columns={"index": "feature"}).round(3)),
         "\n## Fault current per tap pair (median over recordings)\n",
         C.md_table(fc.pivot_table(index=["case", "ftype", "sev_pct"], columns="machine", values=["Ifault_A", "Ifault_over_I1"]).reset_index().round(3).rename(columns=lambda c: "_".join(c) if isinstance(c, tuple) else c)),
         "\n## Per-feature SDR (top 6 per machine and fault type)\n",
         C.md_table(det.sort_values("median_sdr", ascending=False).groupby(["machine", "ftype"]).head(6)
                    [["machine", "ftype", "feature", "group", "n", "median_sdr", "frac_detectable", "healthy_false_alarm"]].round(3)),
         "\n## Sensor suites\n", C.md_table(res.round(3)),
         f"\n## Transfer (self-ref |z|, GBDT; {nwin} windows, {npos} positives)\n", C.md_table(tr.round(3)),
         "\n![G1](figures/G_sdr_by_feature_3alt.png)\n![G2](figures/G_sdr_vs_severity_3alt.png)\n![G3](figures/G_sensor_suites_3alt.png)\n![G4](figures/G_transfer_3alt.png)\n"]
    (C.RES / "summary3.md").write_text("\n".join(L))
    print(res.round(3).to_string(index=False))
    print(tr.round(3).to_string(index=False))
    print("done -> results/summary3.md")


if __name__ == "__main__":
    main()
