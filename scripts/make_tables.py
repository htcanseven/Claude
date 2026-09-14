"""Generate the LaTeX tables of the manuscript from the result CSVs (no hand transcription).
Every table is kept to at most six narrow columns so that it fits the journal text block."""
from pathlib import Path

import numpy as np
import pandas as pd

TAB = Path("results/tables")
OUT = Path("paper/sections")
FT = {"TURNS": "inter-turn", "WINDINGS": "inter-winding"}
TEX = {"I2_I1": r"$I_2/I_1$", "V2_V1": r"$V_2/V_1$", "Id_2fe": r"$I_d$\,2$f_e$", "Iq_2fe": r"$I_q$\,2$f_e$",
       "PId_2fe": r"PI$_d$\,2$f_e$", "PIq_2fe": r"PI$_q$\,2$f_e$", "Vq_2fe": r"$V_q$\,2$f_e$", "Vd_2fe": r"$V_d$\,2$f_e$",
       "Vdconv_2fe": r"$V_d^{\mathrm{cmd}}$\,2$f_e$", "Vqconv_2fe": r"$V_q^{\mathrm{cmd}}$\,2$f_e$", "D2_D1": r"$D_2/D_1$",
       "Ia_h3": r"$I_a$\,h3", "Ia_h5": r"$I_a$\,h5", "Ia_h7": r"$I_a$\,h7", "Ia_thd": r"$I_a$\,THD", "I0_I1": r"$I_0/I_1$",
       "I_unbal_rms": r"RMS unbal.", "Te_2fe": r"$T_e$\,2$f_e$", "Te_1fe": r"$T_e$\,1$f_e$", "Te_std": r"$T_e$\,std",
       "Tm_2fe": r"$T_m$\,2$f_e$", "Tm_1fe": r"$T_m$\,1$f_e$", "Tm_std": r"$T_m$\,std", "Spd_std": r"speed std",
       "Vdc_std": r"$V_{dc}$\,std", "If_2fe": r"$I_f$\,2$f_e$", "If_std": r"$I_f$\,std", "Id_1fe": r"$I_d$\,1$f_e$",
       "Iq_1fe": r"$I_q$\,1$f_e$", "Id_std": r"$I_d$\,std", "Iq_std": r"$I_q$\,std", "PId_std": r"PI$_d$\,std",
       "PIq_std": r"PI$_q$\,std"}
SUITE = {"drive-internal": "drive-internal", "3 CT": "3 CT", "3 CT + 3 VT": "3 CT + 3 VT",
         "3 CT + 3 VT + drive": "3 CT + 3 VT + drive", "+ torque transducer": "+ torque transducer",
         "excitation (WFSG only)": "excitation (field current)"}


def tex(f):
    return TEX.get(f, f.replace("_", r"\_"))


def fmt(x, nd=2):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "--"
    return f"{x:.{nd}f}"


def pct(x):
    return "--" if not np.isfinite(x) else f"{100 * x:.0f}"


def table(body, caption, label, cols, head, size=r"\footnotesize", colsep=None):
    """Rows are joined with line breaks here; any trailing \\\\ a builder added is stripped first."""
    rows = []
    for r in body:
        r = r.rstrip()
        for suf in (r"\\[2pt]", r"\\"):
            if r.endswith(suf):
                r = r[: -len(suf)].rstrip()
        rows.append(r)
    sep = f"\\setlength{{\\tabcolsep}}{{{colsep}}}\n" if colsep else ""
    return (f"\\begin{{table}}[t]\n{size}\n{sep}\\caption{{{caption}}}\\label{{{label}}}\n"
            f"\\begin{{tabular}}{{@{{}}{cols}@{{}}}}\n\\toprule\n{head} \\\\\n\\midrule\n"
            + " \\\\\n".join(rows) + f" \\\\\n\\botrule\n\\end{{tabular}}\n\\end{{table}}\n")


def t_null():
    q5 = pd.read_csv(TAB / "sdr_null_q95.csv", index_col=0)
    q3 = pd.read_csv(TAB / "G_sdr_null_q95_3alt.csv", index_col=0)
    feats = ["I2_I1", "V2_V1", "Id_2fe", "Iq_2fe", "Vq_2fe", "Vdconv_2fe", "D2_D1", "Ia_h3", "Te_2fe", "Spd_std", "If_2fe"]
    body = []
    for f in feats:
        row = [tex(f)]
        for m in ["PMSG", "SCIG"]:
            row.append(fmt(q5.loc[m, f], 3) if f in q5.columns else "--")
        for m in ["PMSG", "SCIG", "WFSG"]:
            row.append(fmt(q3.loc[m, f], 3) if (f in q3.columns and m in q3.index and np.isfinite(q3.loc[m, f])) else "--")
        body.append(" & ".join(row))
    cap = ("Null of the signal-to-drift ratio: 95th percentile of the absolute relative change of a feature between two "
           "adjacent healthy intervals, pooled over all trials of a machine ($N=225$ for PMSG and SCIG, 618 for the WFSG), "
           "for five-cycle windows (PMSG, SCIG) and three-cycle windows (all three).")
    return table(body, cap, "tab:null", "lccccc",
                 r"Feature & PMSG (5\,c) & SCIG (5\,c) & PMSG (3\,c) & SCIG (3\,c) & WFSG (3\,c)")


def t_mde():
    m = pd.read_csv(TAB / "C_min_detectable_severity.csv")
    b = pd.read_csv(TAB / "H_bootstrap.csv")
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        for f in ["V2_V1", "I2_I1", "PId_2fe", "Vq_2fe"]:
            row = [FT[ft], tex(f)]
            for mach in ["PMSG", "SCIG"]:
                r = m[(m.feature == f) & (m.ftype == ft) & (m.machine == mach)].iloc[0]
                bb = b[(b.feature == f) & (b.ftype == ft) & (b.machine == mach)].iloc[0]
                row.append(f"{r.min_detectable_sev_pct:.1f} [{bb.mde_ci_lo:.1f}, {bb.mde_ci_hi:.1f}]")
                row.append(pct(bb.share))
            body.append(" & ".join(row))
    cap = ("Minimum detectable extent (MDE, \\% of the winding between the taps, bootstrap 95\\,\\% interval in brackets) "
           "and detectable share (DS, \\%) of four representative features, PMSG and SCIG, five-cycle windows, $\\alpha=0.95$. "
           "The smallest tested extents are 2.7\\,\\% (inter-turn) and 2.3\\,\\% (inter-winding).")
    head = r"Fault class & Feature & PMSG MDE & PMSG DS & SCIG MDE & SCIG DS"
    return table(body, cap, "tab:mde", "llcccc", head)


def t_suites():
    f = pd.read_csv(TAB / "F_sensor_suites.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "+ torque transducer"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{6}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            row = [SUITE[s]]
            for m in ["PMSG", "SCIG"]:
                r = f[(f.suite == s) & (f.ftype == ft) & (f.machine == m)].iloc[0]
                row += [tex(r.best_feature), f"{r.fixed_min_detectable_pct:.1f}", f"{pct(r.fixed_share_detectable)} [{pct(r.oracle_share_detectable)}]"]
            body.append(" & ".join(row) if s != order[-1] or ft == "WINDINGS" else " & ".join(row) + r" \\[2pt]")
    body = [x if x.endswith(r"\\") or x.endswith(r"\\[2pt]") else x + r" \\" for x in body]
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Observation suites versus what they detect, PMSG and SCIG (five-cycle windows): best fixed feature of the suite, "
           "its minimum detectable extent (MDE, \\%) and detectable share (DS, \\%; per-trial oracle share in brackets). "
           "Features firing on more than one of the nine healthy trials of a machine are excluded for that machine.")
    head = r"Suite & PMSG feature & MDE & DS [oracle] & SCIG feature & MDE & DS [oracle]"
    return table(body, cap, "tab:suites", "l" * 7, head, size=r"\scriptsize", colsep="3pt")


def t_suites3():
    f = pd.read_csv(TAB / "G_sensor_suites_3alt.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "excitation (WFSG only)"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{6}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            for m in ["PMSG", "SCIG", "WFSG"]:
                r = f[(f.suite == s) & (f.ftype == ft) & (f.machine == m)]
                if not len(r):
                    continue
                r = r.iloc[0]
                mde = f"{r.fixed_min_detectable_pct:.1f}" + ("$^{\\dagger}$" if m == "WFSG" and ft == "TURNS" else "")
                body.append(" & ".join([SUITE[s], m, tex(r.best_feature), mde, pct(r.fixed_share_detectable), pct(r.oracle_share_detectable)]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Observation suites for the three alternatives, three-cycle windows, common feature set. MDE (\\%) at the fault "
           "impedance matching the PMSG/SCIG protocol; $^{\\dagger}$the smallest inter-turn extent tested on the WFSG at that "
           "impedance is 11.6\\,\\%, so the value is an upper bound. DS: detectable share (\\%) of the fixed feature; oracle: "
           "per-trial best feature.")
    head = r"Suite & Machine & Feature & MDE & DS & Oracle DS"
    return table(body, cap, "tab:suites3", "llllcc", head, size=r"\scriptsize")


def t_transfer():
    e = pd.read_csv(TAB / "E_transfer.csv")
    body = []
    names = {"raw": "physical units", "healthy-z": "$z$ on target's healthy trials", "self-ref": "$|z|$ vs own reference"}
    for cal in ["raw", "healthy-z", "self-ref"]:
        for model in ["logistic", "gbdt"]:
            row = [names[cal], {"logistic": "logistic", "gbdt": "GBDT"}[model]]
            for tr, te in [("PMSG", "PMSG"), ("SCIG", "SCIG"), ("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                r = e[(e.calibration == cal) & (e.model == model) & (e.train == tr) & (e.test == te)].iloc[0]
                row.append(f"{r.auc:.2f}/{r.tpr_at_1pct_fpr:.2f}")
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer of a window-level detector between PMSG and SCIG: AUC/true-positive rate at 1\\,\\% false-alarm rate. "
           "Within-machine columns use five-fold cross-validation grouped by tap pair; cross columns train on all trials of "
           "one machine and test on all trials of the other. Negatives are the reference and recovery windows of all trials "
           "and the fault-time windows of the healthy trials.")
    head = r"Referencing & Model & P$\to$P & S$\to$S & P$\to$S & S$\to$P"
    return table(body, cap, "tab:transfer", "llcccc", head, size=r"\scriptsize")


def t_transfer3():
    g = pd.read_csv(TAB / "G_transfer_3alt.csv")
    body = [f"{r.train} & {r.test} & {r.auc:.2f} & {r.tpr_at_1pct_fpr:.2f}" + r" \\" for r in g.itertuples()]
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer between the three alternatives (three-cycle windows, common features, $|z|$ against each trial's own "
           "reference, GBDT). Same-machine rows: five-fold cross-validation grouped by tap pair. The WFSG has no healthy "
           "trials, so its negatives are reference and recovery windows only.")
    return table(body, cap, "tab:transfer3", "llcc", r"Trained on & Tested on & AUC & TPR at 1\,\% FPR")


def t_sens():
    w = pd.read_csv(TAB / "H_sensitivity_window.csv")
    q = pd.read_csv(TAB / "H_sensitivity_quantile.csv")
    feats = ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        for f in feats:
            for m in ["PMSG", "SCIG"]:
                row = [{"TURNS": "IT", "WINDINGS": "IW"}[ft], tex(f), m]
                for n in [3, 5, 8]:
                    r = w[(w.ftype == ft) & (w.feature == f) & (w.machine == m) & (w.window_cycles == n)].iloc[0]
                    row.append(f"{r.min_detectable_pct:.1f}/{pct(r.share_detectable)}")
                for a in [0.90, 0.99]:
                    r = q[(q.ftype == ft) & (q.feature == f) & (q.machine == m) & (np.isclose(q.null_quantile, a))].iloc[0]
                    row.append(f"{r.min_detectable_pct:.1f}/{pct(r.share_detectable)}")
                body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Sensitivity of MDE (\\%)/DS (\\%) to the window length (3, 5, 8 cycles at $\\alpha=0.95$) and to the null "
           "quantile ($\\alpha=0.90$ and $0.99$ at five cycles). IT: inter-turn; IW: inter-winding.")
    head = r"Class & Feature & Machine & 3\,c & 5\,c & 8\,c & $\alpha$\,0.90 & $\alpha$\,0.99"
    return table(body, cap, "tab:sens", "lllccccc", head, size=r"\scriptsize", colsep="3pt")


def t_boot():
    b = pd.read_csv(TAB / "H_bootstrap.csv")
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        for f in ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]:
            r = {m: b[(b.ftype == ft) & (b.feature == f) & (b.machine == m)].iloc[0] for m in ["PMSG", "SCIG"]}
            ratio = b[(b.ftype == ft) & (b.feature == f) & (b.machine.str.startswith("SCIG/PMSG"))].iloc[0]
            body.append(" & ".join([FT[ft], tex(f)]
                                   + [f"{r[m].median_sdr:.2f} [{r[m].median_sdr_ci_lo:.2f}, {r[m].median_sdr_ci_hi:.2f}]" for m in ["PMSG", "SCIG"]]
                                   + [f"{ratio.median_sdr:.2f} [{ratio.median_sdr_ci_lo:.2f}, {ratio.median_sdr_ci_hi:.2f}]"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Bootstrap over trials (2000 resamples, 95\\,\\% percentile intervals): median SDR per machine and ratio of "
           "medians SCIG/PMSG. Five-cycle windows, $\\alpha=0.95$. Intervals of the detectable shares are in Fig.~\\ref{fig:boot}.")
    head = r"Class & Feature & PMSG median SDR & SCIG median SDR & SCIG/PMSG"
    return table(body, cap, "tab:boot", "llccc", head, size=r"\scriptsize")


def t_topfeat():
    d = pd.read_csv(TAB / "G_sdr_by_feature_3alt.csv")
    body = []
    for m in ["PMSG", "SCIG", "WFSG"]:
        for ft in ["TURNS", "WINDINGS"]:
            top = d[(d.machine == m) & (d.ftype == ft)].sort_values("median_sdr", ascending=False).head(5)
            body.append(f"{m} & {FT[ft]} & " + "; ".join(f"{tex(r.feature)} {r.median_sdr:.1f} ({pct(r.frac_detectable)})" for r in top.itertuples()) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Five features with the highest median SDR per alternative and fault class (three-cycle windows, all WFSG "
           "impedances); detectable share in parentheses (\\%).")
    return table(body, cap, "tab:topfeat", "llp{7.6cm}", r"Machine & Class & Features: median SDR (DS)", size=r"\scriptsize")


def t_opgrid():
    g = pd.read_csv(TAB / "D_operating_point_grid.csv")
    body = []
    for m in ["PMSG", "SCIG"]:
        for s in [1200, 1500, 1800]:
            row = [m, str(s)]
            for t in [5.2, 6.4, 8.0]:
                r = g[(g.machine == m) & (g.speed_rpm == s) & (np.isclose(g.torque_Nm, t))].iloc[0]
                row.append(f"{r.median_best_sdr:.1f} / {pct(r.frac_detectable)}")
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Operating-point dependence: median SDR of the best of $V_2/V_1$, $V_q$\\,2$f_e$, $I_2/I_1$, PI$_d$\\,2$f_e$ "
           "and detectable share (\\%) per cell of the speed--torque grid, 24 fault trials per cell.")
    return table(body, cap, "tab:opgrid", "llccc", r"Machine & Speed (rpm) & 5.2\,N\,m & 6.4\,N\,m & 8.0\,N\,m")


def t_groups():
    g = pd.read_csv(TAB / "B_strongest_group_share.csv")
    body = []
    for m in ["PMSG", "SCIG"]:
        for ft in ["TURNS", "WINDINGS"]:
            s = g[(g.machine == m) & (g.ftype == ft)].set_index("group")
            body.append(f"{m} & {FT[ft]} & " + " & ".join(
                f"{pct(s.loc[grp, 'share_of_recordings_where_group_is_strongest'])} ({tex(s.loc[grp, 'representative_feature'])})"
                for grp in ["stator current", "dq / control", "mechanical"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Signature location: share of fault trials (\\%) in which each measurement group's best reliable feature attains "
           "the highest SDR (representative feature in parentheses). PMSG and SCIG, five-cycle windows.")
    return table(body, cap, "tab:groups", "llccc", r"Machine & Class & Stator currents & $dq$/controller & Mechanical", size=r"\scriptsize")


def t_suitetransfer():
    t = pd.read_csv(TAB / "F_suite_transfer.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "+ torque transducer"]
    body = []
    for s in order:
        row = [SUITE[s]]
        for cal in ["healthy-z", "self-ref"]:
            for a, b in [("PMSG", "PMSG"), ("SCIG", "SCIG"), ("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                r = t[(t.suite == s) & (t.calibration == cal) & (t.train == a) & (t.test == b)].iloc[0]
                row.append(f"{r.auc:.2f}")
        body.append(" & ".join(row))
    cap = ("Transfer of a GBDT detector restricted to each suite's features (AUC), PMSG and SCIG, five-cycle windows: "
           "features $z$-scored on the target's healthy trials (left block) and $|z|$ against each trial's own reference "
           "(right block). P: PMSG, S: SCIG; same-machine columns use five-fold cross-validation grouped by tap pair.")
    head = (r"\multirow{2}{*}{Suite} & \multicolumn{4}{c}{$z$ on target's healthy trials} & \multicolumn{4}{c}{$|z|$ vs own reference} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(l){6-9}" "\n"
            r" & P$\to$P & S$\to$S & P$\to$S & S$\to$P & P$\to$P & S$\to$S & P$\to$S & S$\to$P")
    return table(body, cap, "tab:suitetransfer", "lcccccccc", head, size=r"\scriptsize", colsep="3pt")


if __name__ == "__main__":
    (OUT / "tab_null.tex").write_text(t_null())
    (OUT / "tab_mde.tex").write_text(t_mde())
    (OUT / "tab_suites.tex").write_text(t_suites())
    (OUT / "tab_transfer.tex").write_text(t_transfer())
    (OUT / "tab_transfer3.tex").write_text(t_transfer3())
    (OUT / "tab_groups.tex").write_text(t_groups())
    (OUT / "appendix_tables.tex").write_text("\n".join([t_suites3(), t_topfeat(), t_opgrid(), t_sens(), t_boot(), t_suitetransfer()]))
    print("tables written")
