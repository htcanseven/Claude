"""Table builders added at the MSSP revision (imported by make_tables.py). They replace the builders whose format the
reviewers criticised and add the new evidence: physical extent levels with bracketed MDEs, cluster-bootstrap
intervals, the decision table with printed probabilities, the inter-turn results per faulted phase, the null
quantile intervals, the decomposition in absolute units and the transfer results with TPR and intervals."""
import numpy as np
import pandas as pd

import make_tables as T

TAB = T.TAB
FT = T.FT
tex, pct, fmt, table = T.tex, T.pct, T.fmt, T.table
SUITE_SHORT = {"drive-internal": "drive", "3 CT": "3CT", "3 CT + 3 VT": "3CT+3VT", "3 CT + 3 VT + drive": "3CT+3VT+drv",
               "excitation (WFSG only)": "exc", "+ torque transducer": "+torque"}
KEY4 = ["V2r_V1", "I2r_I1", "PId_2fe", "Vq_2fe"]


def mde_cell(lo, hi):
    """MDE as a bracket on the physical levels: `lo < MDE <= hi' printed as `(lo, hi]', or `-- ' when undetected."""
    if not np.isfinite(hi):
        return "--"
    return f"$\\le${hi:.1f}" if not np.isfinite(lo) else f"({lo:.1f}, {hi:.1f}]"


def t_mde():
    """Table 5: MDE bracket, detectable share with cluster-bootstrap interval, median SDR with interval, ratio of
    full-sample medians with interval (null re-estimated in every resample)."""
    b = pd.read_csv(TAB / "H_bootstrap.csv")
    req = pd.read_csv(TAB / "R_pair_table.csv")   # not needed for the bracket; kept for the level labels
    sdr = pd.read_csv(TAB / "sdr_per_recording.csv")
    import compare3 as C3
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        for f in KEY4:
            ratio = b[(b.ftype == ft) & (b.feature == f) & (b.machine.str.startswith("SCIG/PMSG"))].iloc[0]
            for k, mach in enumerate(["PMSG", "SCIG"]):
                r = b[(b.ftype == ft) & (b.feature == f) & (b.machine == mach)].iloc[0]
                s = sdr[(sdr.machine == mach) & (sdr.ftype == ft)]
                lo, hi = C3.mde_bracket(s, f"{f}__sdr")
                row = [{"TURNS": "IT", "WINDINGS": "IW"}[ft] if k == 0 else "", tex(f) if k == 0 else "", mach[0], mde_cell(lo, hi),
                       f"{pct(r.share)} [{pct(r.share_ci_lo)}, {pct(r.share_ci_hi)}]",
                       f"{r.median_sdr:.3g} [{r.median_sdr_ci_lo:.3g}, {r.median_sdr_ci_hi:.3g}]",
                       f"{ratio.median_sdr:.3g} [{ratio.median_sdr_ci_lo:.3g}, {ratio.median_sdr_ci_hi:.3g}]" if k == 1 else ""]
                body.append(" & ".join(row))
    cap = ("Minimum detectable extent, detectable share and median SDR with 95\\,\\% intervals for four features, "
           "PMSG and SCIG, five-cycle windows, $\\alpha=0.95$")
    note = ("MDE on the physical extent levels (\\% of a branch): $(a, b]$ means the level $a$ is not detected and every level "
            "from $b$ up is; $\\le b$: every tested level is detected. DS (\\%), median SDR and the SCIG/PMSG ratio of medians "
            "carry percentile intervals from a bootstrap over tap pairs (the same pairs for both machines) in which the null "
            "quantile is re-estimated in every resample. IT: inter-turn; IW: inter-winding; P: PMSG; S: SCIG.")
    head = r"Class & Feature & M. & MDE & DS [CI] & Median SDR [CI] & S/P ratio [CI]"
    return table(body, cap, "tab:mde", "lllcccc", head, size=r"\tabsize", colsep="2pt", note=note)


def t_suites():
    """Table 6: PMSG/SCIG suites at five cycles with the fixed feature, its MDE bracket, DS, false-alarm count and the
    calibrated oracle share."""
    f = pd.read_csv(TAB / "F_sensor_suites.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "+ torque transducer"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{9}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            row = [SUITE_SHORT[s]]
            for m in ["PMSG", "SCIG"]:
                r = f[(f.suite == s) & (f.ftype == ft) & (f.machine == m)].iloc[0]
                fa = f"{int(round(r.fixed_healthy_false_alarm * 9))}/9" if np.isfinite(r.fixed_healthy_false_alarm) else "--"
                row += [tex(r.best_feature), mde_cell(r.fixed_mde_bracket_lo_pct, r.fixed_min_detectable_pct),
                        f"{pct(r.fixed_share_detectable)} ({pct(r.oracle_share_calibrated)})", fa]
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Sensor suites versus what they detect, PMSG and SCIG, five-cycle windows: fixed feature, MDE bracket, "
           "detectable share and false alarms")
    note = ("Suites are cumulative (drive: drive-internal quantities; 3CT: three current transducers; +3VT: three voltage "
            "transducers added; +drv: controller access added; +torque: shaft torque transducer added). DS (\\%) of the fixed "
            "feature, in parentheses the share of the calibrated oracle (per-trial best feature at the threshold that holds the "
            "false-alarm rate of the maximum at 5\\,\\%); FA: false alarms of the fixed feature on the nine healthy trials. "
            "MDE as in Table~\\ref{tab:mde}; features failing the reliability screen are excluded for that machine.")
    head = (r"\multirow{2}{*}{Suite} & \multicolumn{4}{c}{PMSG} & \multicolumn{4}{c}{SCIG} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(l){6-9}" "\n"
            r" & feature & MDE & DS (oracle) & FA & feature & MDE & DS (oracle) & FA")
    return table(body, cap, "tab:suites", "l" * 9, head, size=r"\tabsize", colsep="2.5pt", note=note)


def t_decision():
    """Table 7: every suite's probability of meeting the requirement (joint event MDE <= e_req and DS >= 0.9 above it),
    PMSG/SCIG at five cycles and WFSG at three cycles, alpha = 0.95; the other alphas go to the text."""
    d5 = pd.read_csv(TAB / "R_decision_table_5c.csv")
    d3 = pd.read_csv(TAB / "R_decision_table.csv")
    d = pd.concat([d5[d5.machine.isin(["PMSG", "SCIG"])], d3[d3.machine == "WFSG"]])
    d = d[np.isclose(d.alpha, 0.95)]
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "excitation (WFSG only)"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{14}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            row = [SUITE_SHORT[s]]
            any_ = False
            for m in ["PMSG", "SCIG", "WFSG"]:
                for e in [3, 5, 8, 12]:
                    r = d[(d.machine == m) & (d.ftype == ft) & (d.suite == s) & (d.e_req_pct == e)]
                    if not len(r):
                        row.append("--")
                        continue
                    any_ = True
                    r = r.iloc[0]
                    cell = f"{r.p_meets:.2f}"
                    if r.verdict == "meets":
                        cell = r"\textbf{" + cell + "}"
                    if r.inherited_from:
                        cell += r"$^{\mathrm{b}}$"
                    row.append(cell)
            if any_:
                body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Decision table at $\\alpha=0.95$: bootstrap probability that a suite meets the requirement at "
           "$e_{\\mathrm{req}}=3$, 5, 8 and 12\\,\\%")
    note = ("Meets: $\\mathrm{MDE}\\le e_{\\mathrm{req}}$ and detectable share $\\ge0.9$ for $e\\ge e_{\\mathrm{req}}$; 1000 "
            "resamples of the operating-point trials within each physical level, the null quantile and the fixed feature "
            "re-estimated in every resample. Bold: probability $\\ge0.95$ (meets); below 0.05 the suite fails. PMSG and SCIG at "
            "five-cycle windows, WFSG at three cycles and at its matching fault impedance (inter-turn levels from 11.6\\,\\% only). "
            "Suites as in Table~\\ref{tab:suites}; exc: WFSG field current.")
    lettered = [("b", "Verdict inherited from a cheaper subset of the suite (a suite may always use the features of its subsets).")]
    head = (r"\multirow{2}{*}{Suite} & \multicolumn{4}{c}{PMSG, $e_{\mathrm{req}}$ (\%)} & \multicolumn{4}{c}{SCIG, $e_{\mathrm{req}}$ (\%)} & \multicolumn{4}{c}{WFSG, $e_{\mathrm{req}}$ (\%)} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(l){10-13}" "\n"
            r" & 3 & 5 & 8 & 12 & 3 & 5 & 8 & 12 & 3 & 5 & 8 & 12")
    return table(body, cap, "tab:decision", "l" + "c" * 12, head, size=r"\tabsize", colsep="2.6pt", note=note, lettered=lettered)


def t_phase():
    """New table: inter-turn median SDR and DS per faulted phase, magnitude feature against phasor residual."""
    p = pd.read_csv(TAB / "R_phase_table.csv")
    feats = ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe"]
    body = []
    for m in ["PMSG", "SCIG"]:
        for ph in ["A", "B", "C"]:
            g = p[(p.machine == m) & (p.phase == ph)]
            if not len(g):
                continue
            r0 = g.iloc[0]
            row = [m, f"{ph} ({r0.n_pairs})", r0.extents]
            for f in feats:
                r = g[g.feature == f]
                row.append(f"{r.iloc[0].median_sdr:.2g} / {pct(r.iloc[0].ds)}" if len(r) else "--")
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "Inter-turn median SDR / detectable share (\\%) by faulted phase, five-cycle windows"
    note = ("Number of tap pairs in parentheses; extents: design-level extents of those pairs (\\%). The magnitude ratios "
            "$V_2/V_1$ and $I_2/I_1$ depend on the angle between the inherent and the fault-induced asymmetry, which rotates with "
            "the faulted phase; the phasor residuals $|\\Delta\\bar V_2|/V_1$ and $|\\Delta\\bar I_2|/I_1$ remove that angle.")
    head = r"Machine & Phase (pairs) & Extents & " + " & ".join(tex(f) for f in feats)
    return table(body, cap, "tab:phase", "lllccccc", head, size=r"\tabsize", colsep="3pt", note=note)


def t_decomp():
    """Table 4: decomposition in the relative form of the SDR and in absolute units."""
    d = pd.read_csv(TAB / "R_decomposition.csv")
    d = d[d.feature.isin(["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe", "D2r_D1"])]
    body = []
    for r in d.itertuples():
        body.append(" & ".join([{"TURNS": "IT", "WINDINGS": "IW"}[r.ftype], tex(r.feature),
                                f"{r.ratio_numerator:.2f}", f"{r.ratio_denominator:.2f}", f"{r.ratio_sdr:.2f}",
                                f"{r.ratio_numerator_abs:.2f}", f"{r.ratio_denominator_abs:.2f}", f"{r.ratio_sdr_abs:.2f}"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "SCIG/PMSG ratio of median SDR decomposed into numerator and denominator, relative and absolute form, five-cycle windows"
    note = ("Relative form: the SDR as defined (changes divided by the healthy level); absolute form: changes and null in the "
            "feature's own units. Num.: SCIG/PMSG ratio of the median change under fault; Den.: ratio of null quantiles "
            "$q_{95}^{\\mathrm{PMSG}}/q_{95}^{\\mathrm{SCIG}}$ (a quieter SCIG null raises its SDR); SDR: ratio of median SDR. "
            "IT: inter-turn; IW: inter-winding.")
    head = (r"\multirow{2}{*}{Class} & \multirow{2}{*}{Feature} & \multicolumn{3}{c}{relative (SDR)} & \multicolumn{3}{c}{absolute units} \\" "\n"
            r"\cmidrule(lr){3-5}\cmidrule(l){6-8}" "\n"
            r" & & Num. & Den. & SDR & Num. & Den. & SDR")
    return table(body, cap, "tab:decomp", "llcccccc", head, size=r"\tabsize", colsep="3pt", note=note)


def t_transfer():
    """Table 8: PMSG/SCIG transfer, four referencing rules, AUC and TPR at 1 % FPR on the out-of-reference windows with
    cluster-bootstrap intervals (GBDT; the logistic rows go to the text)."""
    e = pd.read_csv(TAB / "R_transfer2_oor.csv")
    names = {"raw": "physical units", "healthy-z": "$z$, target's healthy trials", "healthy-z-op": "$z$, healthy trial at the operating point",
             "self-ref": "$|z|$ vs own reference"}
    body = []
    for cal in ["raw", "healthy-z", "healthy-z-op", "self-ref"]:
        row = [names[cal]]
        for tr, te in [("PMSG", "PMSG"), ("SCIG", "SCIG"), ("PMSG", "SCIG"), ("SCIG", "PMSG")]:
            r = e[(e.calibration == cal) & (e.model == "gbdt") & (e.train == tr) & (e.test == te)].iloc[0]
            row.append(f"{r.auc_oor:.2f} [{r.auc_oor_ci_lo:.2f}, {r.auc_oor_ci_hi:.2f}]")
            row.append(f"{r.tpr_oor:.2f} [{r.tpr_oor_ci_lo:.2f}, {r.tpr_oor_ci_hi:.2f}]")
        body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer of a GBDT detector between PMSG and SCIG under four referencing rules: AUC and TPR at 1\\,\\% FPR on the "
           "out-of-reference windows, with 95\\,\\% intervals")
    note = ("Intervals from a bootstrap over the trials of the tested machine (500 resamples of its tap pairs and healthy groups). "
            "P$\\to$P, S$\\to$S: cross-validation grouped by tap pair; P$\\to$S, S$\\to$P: trained on one machine, tested on the "
            "other. Out-of-reference windows: those outside the normalising set (Section~\\ref{sec:computation}).")
    head = (r"\multirow{2}{*}{Referencing} & \multicolumn{2}{c}{P$\to$P} & \multicolumn{2}{c}{S$\to$S} & \multicolumn{2}{c}{P$\to$S} & \multicolumn{2}{c}{S$\to$P} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(l){8-9}" "\n"
            r" & AUC & TPR & AUC & TPR & AUC & TPR & AUC & TPR")
    return table(body, cap, "tab:transfer", "lcccccccc", head, size=r"\fontsize{7.5}{9}\selectfont", colsep="2pt", note=note)


def t_transfer3():
    g = pd.read_csv(TAB / "R_transfer3_oor.csv")
    body = []
    for r in g.itertuples():
        fa = "--" if not np.isfinite(r.fpr_healthy_flt_at_1pct) else pct(r.fpr_healthy_flt_at_1pct)
        body.append(f"{r.train} & {r.test} & {r.auc_oor:.2f} [{r.auc_oor_ci_lo:.2f}, {r.auc_oor_ci_hi:.2f}] & "
                    f"{r.tpr_oor:.2f} [{r.tpr_oor_ci_lo:.2f}, {r.tpr_oor_ci_hi:.2f}] & {fa}" + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer between the three alternatives with a self-referenced GBDT detector, three-cycle windows, common "
           "features, out-of-reference windows")
    note = ("Features $|z|$-referenced to the first half of each trial's own reference interval. AUC and TPR at 1\\,\\% FPR on "
            "the out-of-reference windows with 95\\,\\% intervals from a bootstrap over the tested machine's trials; FA: share of "
            "the healthy trials' fault-time windows above the threshold giving 1\\,\\% FPR on all negatives. The WFSG has no "
            "healthy trials, so its negatives are reference and recovery windows only and its rows are optimistic.")
    return table(body, cap, "tab:transfer3", "llccc", r"Trained on & Tested on & AUC [CI] & TPR [CI] & FA healthy (\%)",
                 size=r"\tabsize", note=note)


def t_suites3():
    req = pd.read_csv(TAB / "R_requirement_quantities.csv")
    g = pd.read_csv(TAB / "G_sensor_suites_3alt.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "excitation (WFSG only)"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{9}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            for m in ["PMSG", "SCIG", "WFSG"]:
                r = req[(req.suite == s) & (req.ftype == ft) & (req.machine == m)]
                o = g[(g.suite == s) & (g.ftype == ft) & (g.machine == m)]
                if not len(r) or not len(o):
                    continue
                r, o = r.iloc[0], o.iloc[0]
                mde = mde_cell(r.mde_bracket_lo_pct, r.mde_monotone_pct) + ("$^{\\mathrm{a}}$" if m == "WFSG" and ft == "TURNS" else "")
                fa = f"{int(round(r.healthy_false_alarm * 9))}/9" if np.isfinite(r.healthy_false_alarm) else "--"
                body.append(" & ".join([SUITE_SHORT[s], m, tex(r.fixed_feature), mde, pct(r.ds_all), pct(r.ds_nested), fa,
                                        pct(o.oracle_share_calibrated), pct(o.oracle_fa_calibrated)]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "Sensor suites for the three alternatives, three-cycle windows, common feature set, $\\alpha=0.95$"
    note = ("Fixed feature: highest median SDR among the suite's screened features. MDE bracket (\\%) on the physical levels at "
            "the fault impedance matching the PMSG/SCIG protocol (WFSG: 198 trials, four tap pairs per class). DS: detectable "
            "share (\\%) of the fixed feature; nested: fixed feature chosen on the other tap pairs; FA: its false alarms on the "
            "nine healthy trials; oracle: per-trial best feature at the calibrated threshold, with its false-alarm rate (\\%; the "
            "WFSG has no healthy trials).")
    lettered = [("a", "The smallest inter-turn extent tested on the WFSG at that impedance is 11.6\\,\\%, so the value is an upper bound.")]
    head = r"Suite & Machine & Feature & MDE & DS & DS nested & FA & Oracle DS & Oracle FA"
    return table(body, cap, "tab:suites3", "lllcccccc", head, size=r"\tabsize", colsep="2.5pt", note=note, lettered=lettered)


def t_sens():
    w = pd.read_csv(TAB / "H_sensitivity_window.csv")
    q = pd.read_csv(TAB / "H_sensitivity_quantile.csv")
    feats = ["V2r_V1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]

    def cell(r):
        mde = "--" if not np.isfinite(r.min_detectable_pct) else f"{r.min_detectable_pct:.1f}"
        return f"{mde}/{pct(r.share_detectable)}" + (r"$^{\mathrm{a}}$" if bool(r.screened) else "")
    body = []
    marks = False
    for ft in ["TURNS", "WINDINGS"]:
        for f in feats:
            for m in ["PMSG", "SCIG"]:
                row = [{"TURNS": "IT", "WINDINGS": "IW"}[ft], tex(f), m]
                for n in [3, 5, 8]:
                    rr = w[(w.ftype == ft) & (w.feature == f) & (w.machine == m) & (w.window_cycles == n)].iloc[0]
                    marks |= bool(rr.screened)
                    row.append(cell(rr))
                for a in [0.90, 0.99]:
                    rr = q[(q.ftype == ft) & (q.feature == f) & (q.machine == m) & (np.isclose(q.null_quantile, a))].iloc[0]
                    marks |= bool(rr.screened)
                    row.append(cell(rr))
                body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "Sensitivity of MDE/DS to the window length (3, 5, 8 cycles) and to the null quantile ($\\alpha$ 0.90, 0.99)"
    note = ("Cells: MDE (\\%; upper end of the bracket on the physical levels; `--': largest level not detectable) / DS (\\%). "
            "Window-length columns at $\\alpha=0.95$; quantile columns at five cycles. IT: inter-turn; IW: inter-winding.")
    lettered = [("a", "The feature fails the reliability screen at that setting.")] if marks else []
    head = r"Class & Feature & Machine & 3\,c & 5\,c & 8\,c & $\alpha$\,0.90 & $\alpha$\,0.99"
    return table(body, cap, "tab:sens", "lllccccc", head, size=r"\tabsize", colsep="3pt", note=note, lettered=lettered)


def t_between():
    d = pd.read_csv(TAB / "R_between_trial_null.csv")
    d = d[d.feature.isin(KEY4)]
    body = []
    for r in d.itertuples():
        body.append(" & ".join([{"TURNS": "IT", "WINDINGS": "IW"}[r.ftype], tex(r.feature), r.machine[0],
                                f"{r.q95_within:.3f}", f"{r.q95_between:.3f}",
                                f"{r.median_sdr_within:.3g}", f"{r.median_sdr_between:.3g}", pct(r.ds_within), pct(r.ds_between)]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "Within-trial versus commissioning-baseline null, five-cycle windows, $\\alpha=0.95$"
    note = ("Four key features. Within: reference immediately before the fault; baseline: the healthy trial at the same "
            "operating point, recorded at another time. DS: detectable share (\\%). IT: inter-turn; IW: inter-winding; "
            "P: PMSG; S: SCIG.")
    head = (r"\multirow{2}{*}{Class} & \multirow{2}{*}{Feature} & \multirow{2}{*}{M.} & \multicolumn{2}{c}{$q_{95}$} & \multicolumn{2}{c}{Median SDR} & \multicolumn{2}{c}{DS} \\" "\n"
            r"\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(l){8-9}" "\n"
            r" & & & within & baseline & within & baseline & within & baseline")
    return table(body, cap, "tab:between", "lllcccccc", head, size=r"\tabsize", colsep="2.5pt", note=note)


def t_nullq():
    """New appendix table: the null quantile with its sampling interval."""
    n = pd.read_csv(TAB / "H_null_quantile_ci.csv")
    feats = ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]
    body = []
    for f in feats:
        row = [tex(f)]
        for m in ["PMSG", "SCIG"]:
            r = n[(n.machine == m) & (n.feature == f)]
            if not len(r):
                row += ["--", "--"]
                continue
            r = r.iloc[0]
            row += [f"{r.q95:.3f} [{r.cluster_ci_lo:.3f}, {r.cluster_ci_hi:.3f}]",
                    "--" if not np.isfinite(r.q95_over_1p96sd) else f"{r.q95_over_1p96sd:.2f}"]
        body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "Null quantile $q_{95}$ of seven features with its 95\\,\\% sampling interval, five-cycle windows"
    note = ("Interval from a cluster bootstrap over the 24 tap pairs and the healthy set of each machine (2000 resamples). "
            "$q_{95}/1.96\\sigma$: the quantile relative to the Gaussian value for the same standard deviation of the signed "
            "null; not applicable to the residual features, whose null is a magnitude.")
    head = r"Feature & PMSG $q_{95}$ [CI] & $q_{95}/1.96\sigma$ & SCIG $q_{95}$ [CI] & $q_{95}/1.96\sigma$"
    return table(body, cap, "tab:nullq", "lcccc", head, size=r"\tabsize", colsep="3pt", note=note)


BUILDERS = [("tab_decomp", t_decomp), ("tab_phase", t_phase), ("tab_mde", t_mde), ("tab_suites", t_suites),
            ("tab_decision", t_decision), ("tab_transfer", t_transfer), ("tab_suites3", t_suites3),
            ("tab_sens", t_sens), ("tab_between", t_between), ("tab_transfer3", t_transfer3), ("tab_nullq", t_nullq)]

if __name__ == "__main__":
    for name, builder in BUILDERS:
        T.write_block(name, builder())
    print("tables written into", T.MAIN)
