"""Sensor-suite analysis: which monitoring architecture reaches which minimum detectable fault extent,
per generator topology — the design decision behind the PMSG vs SCIG comparison.

Suites are ordered by added hardware / integration. Features are assigned to the cheapest suite whose
measurements can compute them; angle-dependent (dq-frame) quantities require the drive's rotor/flux angle
and therefore drive access.

Reads the outputs of scripts/features.py and reuses scripts/compare.py. Writes
  results/tables/F_sensor_suites.csv      per suite × machine × fault type: best fixed feature, oracle
  results/tables/F_suite_transfer.csv     cross-topology transfer restricted to each suite's features
  results/figures/F_sensor_suites.png
  results/summary_suites.md
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

SUITES = {
    "drive-internal": dict(
        cost="no added sensors; access to the converter controller",
        feats=["Id_2fe", "Iq_2fe", "Id_1fe", "Iq_1fe", "Id_std", "Iq_std", "Vdconv_2fe", "Vqconv_2fe",
               "PId_2fe", "PIq_2fe", "PId_std", "PIq_std", "D2_D1", "Te_2fe", "Te_1fe", "Te_std", "Vdc_std", "Spd_std"]),
    "3 CT": dict(
        cost="3 current transducers at the terminals; no angle information",
        feats=["I2_I1", "I_unbal_rms", "Ia_h3", "Ia_h5", "Ia_h7", "Ia_thd"]),
    "3 CT + 3 VT": dict(
        cost="3 current + 3 voltage transducers; no angle information",
        feats=["I2_I1", "I_unbal_rms", "Ia_h3", "Ia_h5", "Ia_h7", "Ia_thd", "V2_V1"]),
    "3 CT + 3 VT + drive": dict(
        cost="external transducers plus controller access (dq transform of measured voltages)",
        feats=None),   # filled below: 3 CT + 3 VT + drive-internal + Vd_2fe, Vq_2fe
    "+ torque transducer": dict(
        cost="everything above plus a shaft torque transducer",
        feats=None),
}
SUITES["3 CT + 3 VT + drive"]["feats"] = (SUITES["3 CT + 3 VT"]["feats"] + SUITES["drive-internal"]["feats"]
                                          + ["Vd_2fe", "Vq_2fe"])
SUITES["+ torque transducer"]["feats"] = SUITES["3 CT + 3 VT + drive"]["feats"] + ["Tm_2fe", "Tm_1fe", "Tm_std"]
ORDER = list(SUITES)


def min_detectable(s, col):
    """Limit-of-detection convention (see compare3.min_detectable): smallest tested extent above which every
    tested extent has median SDR >= 1; equal extents are pooled."""
    med = s.groupby("sev_pct")[col].median().sort_index()
    ok = (med >= 1).to_numpy()
    idx = len(ok)
    for i in range(len(ok) - 1, -1, -1):
        if ok[i]:
            idx = i
        else:
            break
    return float(med.index[idx]) if idx < len(ok) else np.nan


def suite_detectability(sdr, det, q95=None):
    rows = []
    for m in ["PMSG", "SCIG"]:
        # screen: binomial false-alarm rule (share > MAX_FALSE_ALARM) and null quantile above one (uninformative)
        bad = set(det[(det.machine == m) & (det.healthy_false_alarm > C.MAX_FALSE_ALARM)].feature)
        if q95 is not None:
            bad |= set(q95.loc[m][q95.loc[m] > 1].index)
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            for suite, spec in SUITES.items():
                feats = [x for x in spec["feats"] if x not in bad and f"{x}__sdr" in f.columns]
                cols = [f"{x}__sdr" for x in feats]
                med = f[cols].median().set_axis(feats)   # selection rule: highest median SDR among screened features
                best = med.idxmax()
                fixed = f[f"{best}__sdr"]
                oracle = f[cols].max(axis=1)
                rows.append(dict(
                    suite=suite, machine=m, ftype=ft, n_features=len(feats), excluded=",".join(sorted(bad & set(spec["feats"]))),
                    best_feature=best, fixed_median_sdr=fixed.median(), fixed_share_detectable=(fixed >= 1).mean(),
                    fixed_min_detectable_pct=min_detectable(f.assign(v=fixed), "v"),
                    oracle_median_sdr=oracle.median(), oracle_share_detectable=(oracle >= 1).mean(),
                    oracle_min_detectable_pct=min_detectable(f.assign(v=oracle), "v"),
                    oracle_healthy_false_alarm=(h[cols].max(axis=1) >= 1).mean() if len(h) else np.nan))
    out = pd.DataFrame(rows)
    out.to_csv(C.TAB / "F_sensor_suites.csv", index=False)
    return out


def suite_transfer(win):
    w, _ = C.build_window_table(win)
    rows = []
    for suite, spec in SUITES.items():
        feats = [x for x in spec["feats"] if x in w.columns]
        for mode in ["healthy-z", "self-ref"]:
            X = C.calibrate(w, feats, mode)
            mk = lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
            for m in ["PMSG", "SCIG"]:
                idx = (w.machine == m).to_numpy()
                Xm, ym, gm = X[idx].to_numpy(), w.y[idx].to_numpy(), w.group[idx].to_numpy()
                scores = np.zeros(len(ym))
                for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
                    scores[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
                rows.append(dict(suite=suite, calibration=mode, train=m, test=m, setting="within",
                                 auc=roc_auc_score(ym, scores), tpr_at_1pct_fpr=C.tpr_at_fpr(ym, scores)))
            for a, b in [("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                tr, te = (w.machine == a).to_numpy(), (w.machine == b).to_numpy()
                s = mk().fit(X[tr].to_numpy(), w.y[tr].to_numpy()).predict_proba(X[te].to_numpy())[:, 1]
                rows.append(dict(suite=suite, calibration=mode, train=a, test=b, setting="cross",
                                 auc=roc_auc_score(w.y[te], s), tpr_at_1pct_fpr=C.tpr_at_fpr(w.y[te], s)))
    out = pd.DataFrame(rows)
    out.to_csv(C.TAB / "F_suite_transfer.csv", index=False)
    return out


def figure(res, tr):
    fig, axes = plt.subplots(3, 2, figsize=(10, 9.6), sharex=True, gridspec_kw={"hspace": 0.3, "wspace": 0.1})
    xs = np.arange(len(ORDER))
    off = {"PMSG": -0.13, "SCIG": 0.13}
    for j, ft in enumerate(["TURNS", "WINDINGS"]):
        # row 0: minimum detectable extent
        ax = axes[0, j]
        for m in ["PMSG", "SCIG"]:
            s = res[(res.ftype == ft) & (res.machine == m)].set_index("suite").loc[ORDER]
            ax.plot(xs + off[m], s.oracle_min_detectable_pct, "o", ms=7, mfc="none", mec=C.COL[m], mew=1.4, zorder=3)
            ax.plot(xs + off[m], s.fixed_min_detectable_pct, "o", ms=6, color=C.COL[m], label=m, zorder=4)
            # PMSG labels above-left, SCIG labels below-right, so coincident points stay legible
            dy, ha = (8, "right") if m == "PMSG" else (-11, "left")
            for x, (feat, y) in zip(xs + off[m], zip(s.best_feature, s.fixed_min_detectable_pct)):
                if np.isfinite(y):
                    ax.annotate(feat, (x, y), xytext=(0, dy), textcoords="offset points", ha=ha,
                                fontsize=6.3, color=C.INK2)
        ax.set_yscale("log")
        ax.set_yticks([2, 3, 5, 10, 20, 40]); ax.set_yticklabels(["2", "3", "5", "10", "20", "40"])
        ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
        ax.set_ylim(1.6, 60)
        ax.set_title(f"{C.FT_LABEL[ft]} faults")
        if j == 0:
            ax.set_ylabel("Minimum detectable extent\n(% of winding between taps)")
            ax.legend(loc="upper right")
        # row 1: share of recordings detectable
        ax = axes[1, j]
        for m in ["PMSG", "SCIG"]:
            s = res[(res.ftype == ft) & (res.machine == m)].set_index("suite").loc[ORDER]
            ax.plot(xs + off[m], s.oracle_share_detectable, "o", ms=7, mfc="none", mec=C.COL[m], mew=1.4, zorder=3)
            ax.plot(xs + off[m], s.fixed_share_detectable, "o", ms=6, color=C.COL[m], zorder=4)
        ax.set_ylim(0, 1.05)
        ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
        if j == 0:
            ax.set_ylabel("Share of fault recordings\ndetectable (SDR ≥ 1)")
        # row 2: cross-topology transfer (self-ref GBDT), colour = machine being monitored
        ax = axes[2, j]
        sub = tr[tr.calibration == ("self-ref" if j == 0 else "healthy-z")]
        for m in ["PMSG", "SCIG"]:
            cross = sub[(sub.setting == "cross") & (sub.test == m)].set_index("suite").loc[ORDER]
            within = sub[(sub.setting == "within") & (sub.test == m)].set_index("suite").loc[ORDER]
            ax.plot(xs + off[m], within.auc, "o", ms=7, mfc="none", mec=C.COL[m], mew=1.4, zorder=3)
            ax.plot(xs + off[m], cross.auc, "o", ms=6, color=C.COL[m], zorder=4)
        ax.set_ylim(0.5, 1.02)
        ax.set_title("features as |z| vs own pre-fault segment" if j == 0 else "features z-scored on target's healthy recordings",
                     fontsize=8.5, color=C.INK2)
        if j == 0:
            ax.set_ylabel("Detector AUC on the monitored machine\n(filled: trained on the other topology)")
        ax.set_xticks(xs); ax.set_xticklabels(ORDER, rotation=20, ha="right", fontsize=8)
    C.header(fig, "Monitoring architecture vs. what it can detect, per topology",
             "Filled = one fixed feature per suite (the best by median SDR, named); hollow = best feature per recording (upper "
             "bound). Bottom row: hollow = trained and tested on the same machine (unseen tap pairs).", top=0.92)
    C.savefig_both(fig, "F_sensor_suites")
    plt.close(fig)


def figure_paper(res):
    """Two-row version for the manuscript (larger type; the transfer row is a table there)."""
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.6), sharex=True, gridspec_kw={"hspace": 0.18, "wspace": 0.12})
    xs = np.arange(len(ORDER))
    off = {"PMSG": -0.13, "SCIG": 0.13}
    for j, ft in enumerate(["TURNS", "WINDINGS"]):
        ax = axes[0, j]
        for m in ["PMSG", "SCIG"]:
            s = res[(res.ftype == ft) & (res.machine == m)].set_index("suite").loc[ORDER]
            ax.plot(xs + off[m], s.oracle_min_detectable_pct, "o", ms=8, mfc="none", mec=C.COL[m], mew=1.5, zorder=3)
            ax.plot(xs + off[m], s.fixed_min_detectable_pct, "o", ms=7, color=C.COL[m], label=m, zorder=4)
            dy, ha = (9, "right") if m == "PMSG" else (-13, "left")
            for x, (feat, y) in zip(xs + off[m], zip(s.best_feature, s.fixed_min_detectable_pct)):
                if np.isfinite(y):
                    ax.annotate(C.lab(feat), (x, y), xytext=(0, dy), textcoords="offset points", ha=ha, fontsize=7, color=C.INK2)
        ax.set_yscale("log"); ax.set_yticks([2, 3, 5, 10, 20]); ax.set_yticklabels(["2", "3", "5", "10", "20"])
        ax.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter()); ax.set_ylim(1.6, 30)
        ax.set_title(f"{C.FT_LABEL[ft]} faults", fontsize=10)
        ax = axes[1, j]
        for m in ["PMSG", "SCIG"]:
            s = res[(res.ftype == ft) & (res.machine == m)].set_index("suite").loc[ORDER]
            ax.plot(xs + off[m], s.oracle_share_detectable, "o", ms=8, mfc="none", mec=C.COL[m], mew=1.5, zorder=3)
            ax.plot(xs + off[m], s.fixed_share_detectable, "o", ms=7, color=C.COL[m], zorder=4)
        ax.set_ylim(0, 1.05); ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
        ax.set_xticks(xs); ax.set_xticklabels(ORDER, rotation=25, ha="right", fontsize=8.5)
    axes[0, 0].set_ylabel("Minimum detectable\nextent (%)", fontsize=9)
    axes[1, 0].set_ylabel("Share of fault trials\ndetectable (SDR ≥ 1)", fontsize=9)
    axes[0, 0].legend(loc="upper right", fontsize=8.5)
    fig.subplots_adjust(top=0.94, bottom=0.2, left=0.12, right=0.98)
    C.savefig_both(fig, "F_sensor_suites_paper")


def report(res, tr):
    L = ["# Sensor-suite analysis — which monitoring architecture detects what, per topology\n",
         "Suites, ordered by added hardware / integration:\n"]
    for k, v in SUITES.items():
        L.append(f"- **{k}** — {v['cost']} ({len(v['feats'])} candidate features)")
    L.append("\nFeatures that fire on more than one of the nine healthy recordings of a machine are excluded for that "
             "machine (`excluded` column). `fixed_*` = one feature per suite chosen once by median SDR; `oracle_*` = best "
             "feature per recording (upper bound for a multi-feature detector).\n")
    cols = ["suite", "machine", "ftype", "n_features", "best_feature", "fixed_median_sdr", "fixed_share_detectable",
            "fixed_min_detectable_pct", "oracle_share_detectable", "oracle_min_detectable_pct", "excluded"]
    L.append(C.md_table(res[cols].round(3)))
    L.append("\n## Transfer restricted to each suite (GBDT)\n")
    piv = tr.pivot_table(index=["suite", "calibration"], columns=["train", "test"], values="auc").reset_index()
    piv.columns = ["suite", "calibration"] + [f"{a}→{b}" for a, b in piv.columns[2:]]
    L.append(C.md_table(piv.round(3)))
    L.append("\n![F](figures/F_sensor_suites.png)\n")
    (C.RES / "summary_suites.md").write_text("\n".join(L))


if __name__ == "__main__":
    files, win = C.load()
    sdr, q95, _ = C.sdr_table(win)
    det, _ = C.where_signature(sdr)
    res = suite_detectability(sdr, det, q95)
    tr = suite_transfer(win)
    figure(res, tr)
    figure_paper(res)
    report(res, tr)
    print(res[["suite", "machine", "ftype", "best_feature", "fixed_min_detectable_pct", "fixed_share_detectable",
               "oracle_min_detectable_pct", "oracle_share_detectable"]].round(3).to_string(index=False))
    print("done ->", C.RES / "summary_suites.md")
