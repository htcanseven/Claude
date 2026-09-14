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
           "its minimum detectable extent (MDE, \\%; limit-of-detection convention) and detectable share (DS, \\%; per-trial "
           "oracle share in brackets). Features failing the reliability screen (three or more false alarms on the nine healthy "
           "trials, or null quantile above one) are excluded for that machine; the oracle false-alarm rates are in Online Resource~1, Table~S1.")
    head = r"Suite & PMSG feature & MDE & DS [oracle] & SCIG feature & MDE & DS [oracle]"
    return table(body, cap, "tab:suites", "l" * 7, head, size=r"\scriptsize", colsep="3pt")








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


# ============================================================================= revision (overrides and new tables)
SUITE_SHORT = {"drive-internal": "drive", "3 CT": "3CT", "3 CT + 3 VT": "3CT+3VT", "3 CT + 3 VT + drive": "3CT+3VT+drv",
               "excitation (WFSG only)": "exc", "none": "none", "": ""}


def screened_mark(r):
    """dagger for features excluded by the screen (>= 3 of 9 healthy false alarms at alpha = 0.95, or null q > 1)"""
    bad = False
    if "healthy_false_alarm_count" in r and np.isfinite(r.healthy_false_alarm_count) and r.n_healthy > 0:
        from scipy.stats import binom
        bad |= bool(binom.sf(int(r.healthy_false_alarm_count) - 1, int(r.n_healthy), 0.05) < 0.05)
    if "null_q" in r and np.isfinite(r.null_q) and r.null_q > 1:
        bad = True
    return r"$^{\dagger}$" if bad else ""


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
           "adjacent healthy intervals, pooled over all trials of a machine ($N=225$ for the PMSG and the SCIG; $N=438$ for "
           "the WFSG, all its inter-turn and inter-winding trials at every fault impedance), for five-cycle windows "
           "(PMSG, SCIG) and three-cycle windows (all three).")
    return table(body, cap, "tab:null", "lccccc",
                 r"Feature & PMSG (5\,c) & SCIG (5\,c) & PMSG (3\,c) & SCIG (3\,c) & WFSG (3\,c)")


def t_mde():
    """MDE (limit-of-detection convention) with bootstrap interval, DS with Wilson interval, median SDR with tap-pair
    bootstrap interval, and the SCIG/PMSG ratio: one table replaces the former MDE and bootstrap tables."""
    b = pd.read_csv(TAB / "H_bootstrap.csv")
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        for f in ["V2_V1", "I2_I1", "PId_2fe", "Vq_2fe"]:
            ratio = b[(b.ftype == ft) & (b.feature == f) & (b.machine.str.startswith("SCIG/PMSG"))].iloc[0]
            for k, mach in enumerate(["PMSG", "SCIG"]):
                r = b[(b.ftype == ft) & (b.feature == f) & (b.machine == mach)].iloc[0]
                mde = "--" if not np.isfinite(r.mde) else f"{r.mde:.1f} [{r.mde_ci_lo:.1f}, {r.mde_ci_hi:.1f}]"
                row = [{"TURNS": "IT", "WINDINGS": "IW"}[ft] if k == 0 else "", tex(f) if k == 0 else "", mach[0], mde,
                       f"{pct(r.share)} [{pct(r.share_wilson_lo)}, {pct(r.share_wilson_hi)}]",
                       f"{r.median_sdr:.3g} [{r.median_sdr_ci_lo:.3g}, {r.median_sdr_ci_hi:.3g}]",
                       f"{ratio.median_sdr:.3g} [{ratio.median_sdr_ci_lo:.3g}, {ratio.median_sdr_ci_hi:.3g}]" if k == 1 else ""]
                body.append(" & ".join(row))
    cap = ("Minimum detectable extent (MDE, \\% of the winding branch between the taps; limit-of-detection convention; "
           "bootstrap 95\\,\\% interval over operating points within each extent level), detectable share (DS, \\%; Wilson "
           "95\\,\\% interval), median SDR (95\\,\\% interval from a bootstrap over tap pairs, the same pairs for both "
           "machines) and the SCIG/PMSG ratio of medians, for four representative features; five-cycle windows, $\\alpha=0.95$. "
           "IT: inter-turn; IW: inter-winding; P: PMSG; S: SCIG. `--': the largest tested extent is not detectable. "
           "Smallest tested extents: 2.7\\,\\% (inter-turn), 2.3\\,\\% (inter-winding).")
    head = r"Class & Feature & M. & MDE [CI] & DS [CI] & Median SDR [CI] & S/P ratio [CI]"
    return table(body, cap, "tab:mde", "lllcccc", head, size=r"\scriptsize", colsep="2pt")


def t_suites3():
    req = pd.read_csv(TAB / "R_requirement_quantities.csv")
    g = pd.read_csv(TAB / "G_sensor_suites_3alt.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "excitation (WFSG only)"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{8}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            for m in ["PMSG", "SCIG", "WFSG"]:
                r = req[(req.suite == s) & (req.ftype == ft) & (req.machine == m)]
                o = g[(g.suite == s) & (g.ftype == ft) & (g.machine == m)]
                if not len(r) or not len(o):
                    continue
                r, o = r.iloc[0], o.iloc[0]
                mde = ("--" if not np.isfinite(r.mde_monotone_pct) else f"{r.mde_monotone_pct:.1f}") + ("$^{\\ddagger}$" if m == "WFSG" and ft == "TURNS" else "")
                body.append(" & ".join([SUITE[s], m, tex(r.fixed_feature), mde, pct(r.ds_all), pct(r.ds_nested),
                                        pct(o.oracle_share_detectable), pct(o.oracle_healthy_false_alarm)]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Observation suites for the three alternatives, three-cycle windows, common feature set, $\\alpha=0.95$. Fixed feature: "
           "highest median SDR among the suite's screened features. MDE (\\%) at the fault impedance matching the PMSG/SCIG "
           "protocol (WFSG: 198 trials, four tap pairs per class); $^{\\ddagger}$the smallest inter-turn extent tested on the "
           "WFSG at that impedance is 11.6\\,\\%, so the value is an upper bound. DS: detectable share (\\%) of the fixed feature; "
           "nested: fixed feature chosen on the other tap pairs; oracle: per-trial best feature, with its false-alarm rate on "
           "the healthy trials (FA, \\%; not available for the WFSG). `--': largest tested extent not detectable.")
    head = r"Suite & Machine & Feature & MDE & DS & DS nested & Oracle DS & Oracle FA"
    return table(body, cap, "tab:suites3", "llllcccc", head, size=r"\scriptsize", colsep="3pt")


def t_transfer():
    e = pd.read_csv(TAB / "R_transfer2_oor.csv")
    body = []
    names = {"raw": "physical units", "healthy-z": "$z$ on target's healthy trials", "self-ref": "$|z|$ vs own reference"}
    for cal in ["raw", "healthy-z", "self-ref"]:
        for model in ["logistic", "gbdt"]:
            row = [names[cal], {"logistic": "logistic", "gbdt": "GBDT"}[model]]
            for tr, te in [("PMSG", "PMSG"), ("SCIG", "SCIG"), ("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                r = e[(e.calibration == cal) & (e.model == model) & (e.train == tr) & (e.test == te)].iloc[0]
                row.append(f"{r.auc_all:.2f}/{r.auc_oor:.2f}")
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer of a window-level detector between PMSG and SCIG: AUC on all windows / AUC on the windows outside the "
           "normalising reference windows (second half of the reference interval, recovery windows and fault-time windows of "
           "the healthy trials). Within-machine columns use five-fold cross-validation grouped by tap pair (healthy trials "
           "grouped by speed); cross columns train on all trials of one machine and test on all trials of the other.")
    head = r"Referencing & Model & P$\to$P & S$\to$S & P$\to$S & S$\to$P"
    return table(body, cap, "tab:transfer", "llcccc", head, size=r"\scriptsize")


def t_transfer3():
    g = pd.read_csv(TAB / "R_transfer3_oor.csv")
    body = []
    for r in g.itertuples():
        fa = "--" if not np.isfinite(r.fpr_healthy_flt_at_1pct) else pct(r.fpr_healthy_flt_at_1pct)
        body.append(f"{r.train} & {r.test} & {r.auc_all:.2f} & {r.auc_oor:.2f} & {r.tpr_oor:.2f} & {fa}" + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer between the three alternatives (three-cycle windows, common features, $|z|$ against the first half of each "
           "trial's own reference interval, GBDT with fixed seed). AUC on all windows and on the out-of-reference windows; TPR "
           "at 1\\,\\% FPR on the out-of-reference windows; FA: share of the fault-time windows of the healthy trials (contactor "
           "operation without a fault) above the threshold that gives 1\\,\\% FPR on all negatives. Same-machine rows: five-fold "
           "cross-validation grouped by tap pair. The WFSG has no healthy trials, so its negatives are reference and recovery "
           "windows only and its rows are optimistic.")
    return table(body, cap, "tab:transfer3", "llcccc", r"Trained on & Tested on & AUC all & AUC o.o.r. & TPR o.o.r. & FA healthy (\%)",
                 size=r"\scriptsize")


def t_groups():
    g = pd.read_csv(TAB / "B_strongest_group_share.csv")
    groups = ["stator current", "terminal voltage", "dq / control", "mechanical"]
    body = []
    for m in ["PMSG", "SCIG"]:
        for ft in ["TURNS", "WINDINGS"]:
            s = g[(g.machine == m) & (g.ftype == ft)].set_index("group")
            body.append(f"{m} & {FT[ft]} & " + " & ".join(
                f"{pct(s.loc[grp, 'share_of_recordings_where_group_is_strongest'])} ({tex(s.loc[grp, 'representative_feature'])})"
                if grp in s.index else "--" for grp in groups) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Signature location: share of fault trials (\\%) in which each measurement group's best screened feature attains "
           "the highest SDR (representative feature in parentheses). PMSG and SCIG, five-cycle windows.")
    return table(body, cap, "tab:groups", "llcccc", r"Machine & Class & Stator currents & Terminal voltages & Controller/$dq$ & Mechanical",
                 size=r"\scriptsize", colsep="3pt")


def t_sens():
    w = pd.read_csv(TAB / "H_sensitivity_window.csv")
    q = pd.read_csv(TAB / "H_sensitivity_quantile.csv")
    feats = ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]

    def cell(r):
        mde = "--" if not np.isfinite(r.min_detectable_pct) else f"{r.min_detectable_pct:.1f}"
        return f"{mde}/{pct(r.share_detectable)}" + (r"$^{s}$" if bool(r.screened) else "")
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        for f in feats:
            for m in ["PMSG", "SCIG"]:
                row = [{"TURNS": "IT", "WINDINGS": "IW"}[ft], tex(f), m]
                for n in [3, 5, 8]:
                    row.append(cell(w[(w.ftype == ft) & (w.feature == f) & (w.machine == m) & (w.window_cycles == n)].iloc[0]))
                for a in [0.90, 0.99]:
                    row.append(cell(q[(q.ftype == ft) & (q.feature == f) & (q.machine == m) & (np.isclose(q.null_quantile, a))].iloc[0]))
                body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Sensitivity of MDE (\\%; limit-of-detection convention, `--' = largest extent not detectable)/DS (\\%) to the window "
           "length (3, 5, 8 cycles at $\\alpha=0.95$) and to the null quantile ($\\alpha=0.90$ and $0.99$ at five cycles). "
           "$^{s}$: the feature fails the reliability screen at that setting. IT: inter-turn; IW: inter-winding.")
    head = r"Class & Feature & Machine & 3\,c & 5\,c & 8\,c & $\alpha$\,0.90 & $\alpha$\,0.99"
    return table(body, cap, "tab:sens", "lllccccc", head, size=r"\scriptsize", colsep="3pt")


def t_topfeat():
    d = pd.read_csv(TAB / "G_sdr_by_feature_3alt.csv")
    body = []
    for m in ["PMSG", "SCIG", "WFSG"]:
        for ft in ["TURNS", "WINDINGS"]:
            top = d[(d.machine == m) & (d.ftype == ft)].sort_values("median_sdr", ascending=False).head(5)
            body.append(f"{m} & {FT[ft]} & " + "; ".join(f"{tex(r.feature)}{screened_mark(r)} {r.median_sdr:.1f} ({pct(r.frac_detectable)})"
                                                         for r in top.itertuples()) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Five features with the highest median SDR per alternative and fault class (three-cycle windows; WFSG at all its "
           "fault impedances, trials with at least one full fault window); detectable share in parentheses (\\%). "
           "$^{\\dagger}$: fails the reliability screen for that machine (three or more false alarms on the nine healthy "
           "trials, or null quantile above one) and is therefore not used in the suite tables.")
    return table(body, cap, "tab:topfeat", "llp{7.6cm}", r"Machine & Class & Features: median SDR (DS)", size=r"\scriptsize")


def t_decision():
    s = pd.read_csv(TAB / "R_decision_cheapest.csv")
    body = []
    for a in [0.90, 0.95, 0.99]:
        for e in [3, 5, 8, 12]:
            row = [f"{a:.2f}", str(e)]
            for m in ["PMSG", "SCIG", "WFSG"]:
                for ft in ["TURNS", "WINDINGS"]:
                    r = s[(np.isclose(s.alpha, a)) & (s.e_req_pct == e) & (s.machine == m) & (s.ftype == ft)]
                    if not len(r):
                        row.append("--")
                        continue
                    r = r.iloc[0]
                    c = SUITE_SHORT.get(r.cheapest_meets, r.cheapest_meets)
                    if r.cheapest_meets == "none" and r.cheapest_not_failing != "none":
                        c = f"({SUITE_SHORT.get(r.cheapest_not_failing, r.cheapest_not_failing)})?"
                    row.append(c)
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Decision table: cheapest observation suite whose minimum detectable extent meets the requirement $e_{\\mathrm{req}}$ "
           "with bootstrap probability $\\ge0.95$, per alternative, fault class and false-alarm level $\\alpha$ (three-cycle windows; "
           "suites ordered drive-internal $<$ 3\\,CT $<$ 3\\,CT+3\\,VT $<$ 3\\,CT+3\\,VT+drive; exc: WFSG field current). "
           "`(suite)?': no suite meets with that confidence, the cheapest suite whose verdict is uncertain is shown; `none': every "
           "suite fails. WFSG inter-turn verdicts are bounded by its smallest tested extent at the matching impedance (11.6\\,\\%).")
    head = (r"\multirow{2}{*}{$\alpha$} & \multirow{2}{*}{$e_{\mathrm{req}}$ (\%)} & \multicolumn{2}{c}{PMSG} & \multicolumn{2}{c}{SCIG} & \multicolumn{2}{c}{WFSG} \\" "\n"
            r"\cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(l){7-8}" "\n"
            r" & & IT & IW & IT & IW & IT & IW")
    return table(body, cap, "tab:decision", "llcccccc", head, size=r"\scriptsize", colsep="3pt")


def t_decomp():
    d = pd.read_csv(TAB / "R_decomposition.csv")
    body = []
    for r in d.itertuples():
        body.append(" & ".join([FT[r.ftype], tex(r.feature), f"{r.abs_delta_median_PMSG:.3f}", f"{r.abs_delta_median_SCIG:.3f}",
                                f"{r.q95_PMSG:.3f}", f"{r.q95_SCIG:.3f}", f"{r.ratio_numerator:.2f}", f"{r.ratio_denominator:.2f}",
                                f"{r.ratio_sdr:.2f}"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Decomposition of the SCIG/PMSG ratio of median SDR into its numerator (ratio of median $|\\delta|$, the relative "
           "change under fault) and its denominator (ratio $q_{0.95}^{\\mathrm{PMSG}}/q_{0.95}^{\\mathrm{SCIG}}$ of the null "
           "quantiles); five-cycle windows.")
    head = r"Class & Feature & $|\delta|$ P & $|\delta|$ S & $q_{95}$ P & $q_{95}$ S & Num. & Den. & SDR ratio"
    return table(body, cap, "tab:decomp", "llccccccc", head, size=r"\scriptsize", colsep="3pt")


def t_between():
    d = pd.read_csv(TAB / "R_between_trial_null.csv")
    body = []
    for r in d.itertuples():
        body.append(" & ".join([{"TURNS": "IT", "WINDINGS": "IW"}[r.ftype], tex(r.feature), r.machine[0],
                                f"{r.q95_within:.3f}", f"{r.q95_between:.3f}",
                                f"{r.median_sdr_within:.3g}", f"{r.median_sdr_between:.3g}", pct(r.ds_within), pct(r.ds_between)]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Within-trial null (reference immediately before the fault) versus commissioning-baseline null (reference: the healthy "
           "trial at the same operating point, recorded at a different time): null quantile $q_{95}$, median SDR and detectable "
           "share DS (\\%), five-cycle windows, $\\alpha=0.95$. IT: inter-turn; IW: inter-winding; P: PMSG; S: SCIG.")
    head = (r"\multirow{2}{*}{Class} & \multirow{2}{*}{Feature} & \multirow{2}{*}{M.} & \multicolumn{2}{c}{$q_{95}$} & \multicolumn{2}{c}{Median SDR} & \multicolumn{2}{c}{DS} \\" "\n"
            r"\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(l){8-9}" "\n"
            r" & & & within & baseline & within & baseline & within & baseline")
    return table(body, cap, "tab:between", "lllcccccc", head, size=r"\scriptsize", colsep="2.5pt")


def t_z2():
    d = pd.read_csv(TAB / "R_baselines_z2.csv")
    body = []
    for r in d.itertuples():
        body.append(" & ".join([r.machine, FT[r.ftype], f"{r.I2_I1_pre:.4f}", f"{r.V2_V1_pre:.4f}", f"{r.D2_D1_pre:.4f}",
                                f"{r.dI2_A_rms:.3f}", f"{r.dV2_V_rms:.2f}", f"{r.dV2_dI2_ohm:.1f} [{r.dV2_dI2_q25:.1f}, {r.dV2_dI2_q75:.1f}]"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Healthy baselines of the three asymmetry ratios (median over fault trials, reference interval) and the incremental "
           "negative-sequence response under fault: median change of the negative-sequence current $\\Delta I_2$ (A, RMS) and "
           "terminal voltage $\\Delta V_2$ (V, RMS), and their ratio $\\Delta V_2/\\Delta I_2$ ($\\Omega$; interquartile range in "
           "brackets), three-cycle windows; WFSG at the matching fault impedance.")
    head = r"Machine & Class & $I_2/I_1$ & $V_2/V_1$ & $D_2/D_1$ & $\Delta I_2$ & $\Delta V_2$ & $\Delta V_2/\Delta I_2$"
    return table(body, cap, "tab:z2", "llcccccc", head, size=r"\scriptsize", colsep="3pt")


def t_screen():
    d = pd.read_csv(TAB / "R_screened_features.csv")
    body = []
    for (n, m), g in d.groupby(["window_cycles", "machine"]):
        body.append(f"{n} & {m} & " + ", ".join(f"{tex(r.feature)} ({int(r.n_false)})" for r in g.itertuples()) + r" \\")
    if body:
        body[-1] = body[-1].rstrip(r"\\").rstrip()
    else:
        body = ["-- & -- & none"]
    cap = ("Features failing the reliability screen (three or more false alarms on the nine healthy trials at $\\alpha=0.95$; "
           "count in parentheses) per window length and machine.")
    return table(body, cap, "tab:screen", "llp{8cm}", r"Window (cycles) & Machine & Excluded features (false alarms)", size=r"\scriptsize")


if __name__ == "__main__":
    (OUT / "tab_null.tex").write_text(t_null())
    (OUT / "tab_mde.tex").write_text(t_mde())
    (OUT / "tab_suites.tex").write_text(t_suites())
    (OUT / "tab_transfer.tex").write_text(t_transfer())
    (OUT / "tab_transfer3.tex").write_text(t_transfer3())
    (OUT / "tab_groups.tex").write_text(t_groups())
    (OUT / "tab_decision.tex").write_text(t_decision())
    (OUT / "tab_decomp.tex").write_text(t_decomp())
    (OUT / "tab_z2.tex").write_text(t_z2())
    (OUT / "tab_between.tex").write_text(t_between())
    (OUT / "appendix_tables.tex").write_text("\n".join([t_suites3(), t_topfeat(), t_opgrid(), t_sens(), t_screen(), t_suitetransfer()]))
    print("tables written")
