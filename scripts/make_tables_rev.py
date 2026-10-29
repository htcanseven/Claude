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
                mde_iv = (f"{r.mde_ci_lo:.1f}--{r.mde_ci_hi:.1f}" if r.mde_ci_lo != r.mde_ci_hi else f"{r.mde_ci_lo:.1f}")
                row = [{"TURNS": "IT", "WINDINGS": "IW"}[ft] if k == 0 else "", tex(f) if k == 0 else "", mach[0], mde_cell(lo, hi) + f" [{mde_iv}]",
                       f"{pct(r.share)} [{pct(r.share_ci_lo)}, {pct(r.share_ci_hi)}]",
                       f"{r.median_sdr:.3g} [{r.median_sdr_ci_lo:.3g}, {r.median_sdr_ci_hi:.3g}]",
                       f"{ratio.median_sdr:.3g} [{ratio.median_sdr_ci_lo:.3g}, {ratio.median_sdr_ci_hi:.3g}]" if k == 1 else ""]
                body.append(" & ".join(row))
    cap = ("Minimum detectable extent, detectable share and median SDR with 95\\,\\% intervals, four features, "
           "PMSG and SCIG, five-cycle windows")
    note = ("$\\alpha=0.95$. MDE on the physical extent levels (\\% of a branch): $(a, b]$, level $a$ not detected and every level "
            "from $b$ up detected; $\\le b$, every tested level detected; in brackets its 95\\,\\% interval over the operating-point "
            "trials of each level. DS (\\%), median SDR and the SCIG/PMSG ratio of medians "
            "carry percentile intervals from a bootstrap over tap pairs (the same pairs for both machines) with the null "
            "quantile re-estimated in every resample. IT: inter-turn; IW: inter-winding; P: PMSG; S: SCIG.")
    head = r"Class & Feature & M. & MDE [CI] & DS [CI] & Median SDR [CI] & SCIG/PMSG [CI]"
    return table(body, cap, "tab:mde", "lllcccc", head, size=r"\tabsize", colsep="2pt", note=note)


def t_suites():
    """Table 6: PMSG/SCIG suites at five cycles with the fixed feature, its MDE bracket, DS, false-alarm count and the
    calibrated oracle share."""
    f = pd.read_csv(TAB / "F_sensor_suites.csv")
    e9 = pd.read_csv(TAB / "R3_e90.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "+ torque transducer"]
    body = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{11}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        short = {"drive-internal": "drive", "3 CT": "3CT", "3 CT + 3 VT": "+3VT", "3 CT + 3 VT + drive": "+drv", "+ torque transducer": "+torque"}
        for s in order:
            row = [short[s]]
            for m in ["PMSG", "SCIG"]:
                r = f[(f.suite == s) & (f.ftype == ft) & (f.machine == m)].iloc[0]
                fa = f"{int(round(r.fixed_healthy_false_alarm * 9))}/9" if np.isfinite(r.fixed_healthy_false_alarm) else "--"
                q = e9[(e9.suite == s) & (e9.ftype == ft) & (e9.machine == m)]
                if len(q):
                    e = q.iloc[0].e90_95
                    e95 = f"{e:.1f}" if np.isfinite(e) else "--"
                else:   # the torque suite is not in the decision table; its fixed feature is the +drv suite's
                    q = e9[(e9.suite == "3 CT + 3 VT + drive") & (e9.ftype == ft) & (e9.machine == m)]
                    e = q.iloc[0].e90_95
                    e95 = (f"{e:.1f}" if np.isfinite(e) else "--") + r"$^{\mathrm{a}}$"
                lab = {"I2r_I1": r"$\Delta\bar I_2$", "V2r_V1": r"$\Delta\bar V_2$", "D2r_D1": r"$\Delta\bar D_2$"}.get(r.best_feature, tex(r.best_feature))
                row += [lab, mde_cell(r.fixed_mde_bracket_lo_pct, r.fixed_min_detectable_pct).replace(", ", ","), e95,
                        f"{pct(r.fixed_share_detectable)} ({pct(r.oracle_share_calibrated)})", fa]
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Sensor suites versus what they detect, PMSG and SCIG, five-cycle windows: fixed feature, MDE bracket, "
           "$e_{90}^{\\mathrm{B}}$, detectable share and false alarms")
    note = ("drive: drive-internal quantities alone; 3CT: three current transducers; +3VT, +drv, +torque: voltage "
            "transducers, controller access and a shaft torque transducer added cumulatively to 3CT (each row includes the "
            "rows above it from 3CT on). $\\Delta\\bar X_2$ stands for the residual $|\\Delta\\bar X_2|/X_1$. MDE: median-crossing "
            "extent (Table~\\ref{tab:mde}); $e_{90}^{\\mathrm{B}}$: smallest tested level (\\%) from which the detectable share at the "
            "level itself is at least 0.9, at that level and above, with bootstrap support of at least 0.95 (Section~\\ref{sec:derived}; not a confidence bound). DS (\\%) of the "
            "fixed feature pooled over all tested extents, in parentheses the share of the calibrated oracle (Section~\\ref{sec:sdr}); "
            "the nested selection of the fixed feature on the other tap pairs changes these shares by at most one point at this window length (Table~\\ref{tab:heldout} gives the held-out run of the whole procedure). FA: false "
            "alarms of the fixed feature on the nine healthy trials; screened-out features are excluded.")
    lettered = [("a", "Same fixed feature as +drv; the torque features add nothing.")]
    head = (r"\multirow{2}{*}{Suite} & \multicolumn{5}{c}{PMSG} & \multicolumn{5}{c}{SCIG} \\" "\n"
            r"\cmidrule(lr){2-6}\cmidrule(l){7-11}" "\n"
            r" & feature & MDE & $e_{90}^{\mathrm{B}}$ & DS (or.) & FA & feature & MDE & $e_{90}^{\mathrm{B}}$ & DS (or.) & FA")
    return table(body, cap, "tab:suites", "l" * 11, head, size=r"\fontsize{8}{10}\selectfont", colsep="1.3pt", note=note, lettered=lettered)


def t_decision():
    """Table 7: every suite's probability of meeting the requirement (joint event MDE <= e_req and DS >= 0.9 above it),
    PMSG/SCIG at five cycles and WFSG at three cycles, alpha = 0.95; the other alphas go to the text."""
    d5 = pd.read_csv(TAB / "R_decision_table_5c.csv")
    d3 = pd.read_csv(TAB / "R_decision_table.csv")
    d = pd.concat([d5[d5.machine.isin(["PMSG", "SCIG"])], d3[d3.machine == "WFSG"]])
    d = d[np.isclose(d.alpha, 0.95)]
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "excitation (WFSG only)"]
    machines = ["PMSG", "SCIG", "WFSG"]
    # the requirement values are the tested physical levels of the common bench; the two largest inter-winding
    # levels (33.7-37.5 and 40.2 %) add no information and are stated in the note
    grid = {ft: sorted(d[d.ftype == ft].e_req_pct.unique()) for ft in ["TURNS", "WINDINGS"]}
    omitted = [e for e in grid["WINDINGS"] if e > 30]
    grid["WINDINGS"] = [e for e in grid["WINDINGS"] if e <= 30]
    ncol = max(len(v) for v in grid.values())
    big = d[(d.ftype == "WINDINGS") & d.e_req_pct.isin(omitted) & (d.verdict != "untested")]
    assert (big.verdict == "meets").all(), big[["machine", "suite", "e_req_pct", "p_meets", "verdict"]]
    body = []
    used = set()
    for ft in ["TURNS", "WINDINGS"]:
        E = grid[ft]
        pad = [""] * (ncol - len(E))
        body.append(r"\multicolumn{" + str(1 + 3 * ncol) + r"}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        body.append(" & ".join([r"$e_{\mathrm{req}}$ (\%)"] + sum([[f"{e:.1f}" for e in E] + pad for _ in machines], [])) + r" \\")
        for s in order:
            row = [SUITE_SHORT[s]]
            any_ = False
            for m in machines:
                for e in E:
                    r = d[(d.machine == m) & (d.ftype == ft) & (d.suite == s) & (d.e_req_pct == e)]
                    if not len(r):
                        row.append("--")
                        continue
                    any_ = True
                    r = r.iloc[0]
                    if r.verdict == "untested":
                        row.append("n.t.")
                        continue
                    pv = r.p_meets_level
                    cell = f"{pv:.3f}" if 0.045 <= pv < 0.05 else f"{pv:.2f}"
                    if pv >= 0.95:
                        cell = r"\textbf{" + cell + "}"
                    marks = ""
                    if isinstance(r.inherited_from_level, str) and r.inherited_from_level and f"{r.p_meets_level_own:.2f}" != f"{pv:.2f}":
                        marks += "b"
                    nres = 10000 if m in ("PMSG", "SCIG") else 1000
                    se = max(np.sqrt(pv * (1 - pv) / nres), np.sqrt(0.05 * 0.95 / nres))
                    if abs(pv - 0.05) <= 2 * se or abs(pv - 0.95) <= 2 * se:
                        marks += "c"
                    if marks:
                        cell += r"$^{\mathrm{" + ",".join(marks) + "}}$"
                        used.update(marks)
                    row.append(cell)
                row += pad
            if any_:
                body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Decision table at $\\alpha=0.95$: bootstrap support for a suite meeting the empirical requirement at each "
           "tested extent level")
    note = ("Cell: fraction of resamples (10\\,000 for the PMSG and SCIG, 1000 for the WFSG) in which $\\mathrm{MDE}\\le e_{\\mathrm{req}}$ and the detectable share at the "
            "tested level that $e_{\\mathrm{req}}$ maps to is $\\ge0.9$; resampling support, an empirical stability measure of the decision, not a posterior probability "
            "and not a confidence level; a cell of 1.00 means no resample failed. $e_{\\mathrm{req}}$ at the physical levels of the common bench (\\% of a branch; the "
            "WFSG, unscreened for lack of healthy trials, is assessed against the same values on its own tested extents); the "
            "operating-point trials of a level are resampled with its tap pairs treated as exchangeable, null quantile and fixed "
            "feature re-estimated in every resample. Bold: support $\\ge0.95$ (meets); $\\le0.05$: fails; between: uncertain; "
            "n.t.: no tested extent on the required side of $e_{\\mathrm{req}}$. PMSG and SCIG at five-cycle windows, WFSG at "
            "three cycles and its matching fault impedance; the inter-winding levels "
            + " and ".join(f"{e:.1f}" for e in omitted) + "\\,\\% are omitted (every suite meets them). Suites as in "
            "Table~\\ref{tab:suites}; exc: WFSG field current. Table~\\ref{tab:cells} gives the cells that change under the "
            "pooled share or the tap-pair resampling unit.")
    lettered = [("b", "Support inherited from a cheaper subset of the suite: a suite may use the features of its subsets, so its "
                      "support is at least theirs (e.g. 3CT+3VT+drv inherits the voltage residual of 3CT+3VT)."),
                ("c", "Borderline: within two Monte-Carlo standard errors of a verdict boundary (0.05 or 0.95).")]
    lettered = [(k, v) for k, v in lettered if k in used]
    head = (r"Suite & \multicolumn{" + str(ncol) + r"}{c}{PMSG} & \multicolumn{" + str(ncol) + r"}{c}{SCIG} & \multicolumn{"
            + str(ncol) + r"}{c}{\shortstack{WFSG\\(exploratory, unscreened)}} \\" "\n"
            + r"\cmidrule(lr){2-" + str(1 + ncol) + r"}\cmidrule(lr){" + str(2 + ncol) + "-" + str(1 + 2 * ncol) + r"}\cmidrule(l){"
            + str(2 + 2 * ncol) + "-" + str(1 + 3 * ncol) + "}" "\n"
            + r" & \multicolumn{" + str(3 * ncol) + r"}{c}{bootstrap support for meeting the empirical requirement at $e_{\mathrm{req}}$}")
    return table(body, cap, "tab:decision", "l" + "c" * (3 * ncol), head, size=r"\tabsize", colsep="2.6pt", note=note, lettered=lettered)


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
    head = r"Machine & Phase (pairs) & Extents (\%) & " + " & ".join(tex(f) for f in feats)
    return table(body, cap, "tab:phase", "llL{2.1cm}ccccc", head, size=r"\tabsize", colsep="2.5pt", note=note)


def t_decomp():
    """Table 4: decomposition in the relative form of the SDR and in absolute units."""
    d = pd.read_csv(TAB / "R_decomposition.csv")
    d = d[d.feature.isin(["V2r_V1", "I2r_I1", "Id_2fe", "D2r_D1"])]
    body = []
    for r in d.itertuples():
        body.append(" & ".join([{"TURNS": "IT", "WINDINGS": "IW"}[r.ftype], tex(r.feature),
                                f"{r.ratio_numerator:.2f}", f"{r.ratio_denominator:.2f}", f"{r.ratio_sdr:.2f}",
                                f"{r.ratio_numerator_abs:.2f}", f"{r.ratio_denominator_abs:.2f}", f"{r.ratio_sdr_abs:.2f}"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = "SCIG/PMSG ratio of median SDR decomposed into numerator and denominator, five-cycle windows"
    note = ("Relative form: the SDR as defined (changes divided by the healthy level); absolute form: changes and null in the "
            "feature's own units. Num.: SCIG/PMSG ratio of the median change under fault; Den.: ratio of null quantiles "
            "$q_{95}^{\\mathrm{PMSG}}/q_{95}^{\\mathrm{SCIG}}$ (a quieter SCIG null raises its SDR); SDR: ratio of median SDR. "
            "IT: inter-turn; IW: inter-winding.")
    head = (r"\multirow{2}{*}{Class} & \multirow{2}{*}{Feature} & \multicolumn{3}{c}{relative (SDR)} & \multicolumn{3}{c}{absolute units} \\" "\n"
            r"\cmidrule(lr){3-5}\cmidrule(l){6-8}" "\n"
            r" & & Num. & Den. & SDR & Num. & Den. & SDR")
    return table(body, cap, "tab:decomp", "llcccccc", head, size=r"\tabsize", colsep="6pt", note=note)


def t_envelope():
    """Operating envelope: median SDR (detectable share) of the fixed inter-turn features by speed, the torque
    factor at fixed speed, and the incremental negative-sequence impedance by speed; PMSG and SCIG, five cycles."""
    e = pd.read_csv(TAB / "R_envelope_fixed.csv")
    z = pd.read_csv(TAB / "R_z2_by_speed.csv")
    speeds = [1200, 1500, 1800]
    body = [r"\multicolumn{6}{@{}l}{\emph{Median SDR (detectable share, \%) of the fixed inter-turn features}} \\"]
    want = [("PMSG", "V2r_V1"), ("PMSG", "D2r_D1"), ("PMSG", "I2r_I1"), ("SCIG", "I2r_I1"), ("SCIG", "D2r_D1"), ("SCIG", "V2r_V1")]
    for m, f in want:
        r = e[(e.machine == m) & (e.ftype == "TURNS") & (e.feature == f)].iloc[0]
        cells = [f"{r[f'median_{s}']:.1f} ({100 * r[f'share_{s}']:.0f})" for s in speeds]
        body.append(" & ".join([m, tex(f)] + cells + [f"{r.torque_factor_max:.2f}"]) + r" \\")
    body.append(r"\multicolumn{6}{@{}l}{\emph{Incremental negative-sequence impedance $|\Delta\bar V_2/\Delta\bar I_2|$ ($\Omega$), median [IQR]}} \\")
    for m in ["PMSG", "SCIG"]:
        for ft, lab in [("TURNS", "inter-turn"), ("WINDINGS", "inter-winding")]:
            cells = []
            for s in speeds:
                r = z[(z.machine == m) & (z.ftype == ft) & (z.speed_rpm == s)].iloc[0]
                cells.append(f"{r.Z2_ohm:.1f} [{r.Z2_q25:.1f}, {r.Z2_q75:.1f}]")
            body.append(" & ".join([m, lab] + cells + [""]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Operating envelope: fixed inter-turn features and terminal impedance by speed, PMSG and SCIG, "
           "five-cycle windows")
    note = ("Speeds 1200, 1500 and 1800\\,rpm ($2f_e$ = 80, 100 and 120\\,Hz; 79, 99 and 119\\,Hz on the SCIG, which "
            "generates with slip); each cell pools the three torques (36 inter-turn trials per machine and speed). "
            "Torque factor: largest ratio of per-torque medians at a fixed speed. The impedance is the per-trial "
            "complex ratio of the phasor residuals (Section~\\ref{sec:res-where}), 36 trials per cell.")
    head = (r"Machine & Feature / class & 1200\,rpm & 1500\,rpm & 1800\,rpm & Torque factor")
    return table(body, cap, "tab:envelope", "llcccc", head, size=r"\tabsize", colsep="3pt", note=note)


def t_decision_cells():
    """Cells of the decision table whose verdict depends on the definition of the power (pooled share above e_req
    against the share at e_req itself) or on the resampling unit within a level (trials against tap pairs)."""
    def load(suffix):
        d5 = pd.read_csv(TAB / f"R_decision_table_5c{suffix}.csv")
        d3 = pd.read_csv(TAB / f"R_decision_table{suffix}.csv")
        d = pd.concat([d5[d5.machine.isin(["PMSG", "SCIG"])], d3[d3.machine == "WFSG"]])
        return d[np.isclose(d.alpha, 0.95) & (d.verdict != "untested")]
    tr, pa = load(""), load("_pairs")
    key = ["machine", "ftype", "suite", "e_req_pct"]
    m = tr.merge(pa[key + ["p_meets", "p_meets_level"]], on=key, suffixes=("", "_pairs"))
    def verdict(p):
        return np.where(p >= 0.95, "meets", np.where(p <= 0.05, "fails", "uncertain"))
    cols = ["p_meets_level", "p_meets_level_pairs", "p_meets", "p_meets_pairs"]
    V = np.column_stack([verdict(m[c].to_numpy()) for c in cols])
    m = m[(V != V[:, [0]]).any(axis=1)].copy()
    order = {s: i for i, s in enumerate(["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive", "excitation (WFSG only)"])}
    m["o"] = m.suite.map(order)
    m = m.sort_values(["machine", "ftype", "e_req_pct", "o"])
    body = []
    for r in m.itertuples():
        cells = [(f"{getattr(r, c):.3f}" if 0.045 <= getattr(r, c) < 0.055 or 0.945 <= getattr(r, c) < 0.955 else f"{getattr(r, c):.2f}") for c in cols]
        body.append(" & ".join([r.machine, FT[r.ftype], SUITE_SHORT[r.suite], f"{r.e_req_pct:.1f}", f"{100 * r.ds_at_level:.0f}"] + cells) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Decision-table cells whose verdict depends on the definition of the power or on the resampling unit "
           "within a level, or lies at a boundary")
    note = ("$\\alpha=0.95$; every other cell of Table~\\ref{tab:decision} keeps its verdict under all four variants. "
            "At level, trials: 10\\,000 resamples (Table~\\ref{tab:decision}); the other three variants 1000. "
            "DS at level: share of the fixed feature at the level $e_{\\mathrm{req}}$ maps to (\\%). At level: share at that "
            "level (Table~\\ref{tab:decision}); pooled: share over all tested levels $\\ge e_{\\mathrm{req}}$; trials, pairs: "
            "resampling unit within a level. Meets at $\\ge0.95$, fails at $\\le0.05$, classified on the unrounded fraction.")
    head = (r"\multirow{2}{*}{Machine} & \multirow{2}{*}{Class} & \multirow{2}{*}{Suite} & \multirow{2}{*}{$e_{\mathrm{req}}$ (\%)} & "
            r"\multirow{2}{*}{DS at level} & \multicolumn{2}{c}{at level} & \multicolumn{2}{c}{pooled} \\" "\n"
            r"\cmidrule(lr){6-7}\cmidrule(l){8-9}" "\n"
            r" & & & & & trials & pairs & trials & pairs")
    # reorder the probability columns to match the header: pooled (trials, pairs), at level (trials, pairs)
    body = [b for b in body]
    return table(body, cap, "tab:cells", "lllccCCCC".replace("C", "c"), head, size=r"\tabsize", colsep="4pt", note=note)


def t_heldout():
    """Held-out run of the complete procedure (null quantile, screen and fixed feature fitted on the development tap
    pairs, frozen, scored on the held-out pair): per suite and class the fixed feature in sample and the features
    chosen in the folds, e90 in sample and held out, the share at the smallest tested level in sample and held out,
    and the false alarms of the frozen procedure on the healthy trials, each held out in turn."""
    su = pd.read_csv(TAB / "R4_heldout_suites.csv")
    lv = pd.read_csv(TAB / "R4_heldout_levels.csv")
    order = ["drive-internal", "3 CT", "3 CT + 3 VT", "3 CT + 3 VT + drive"]
    lab = {"I2r_I1": r"$\Delta\bar I_2$", "V2r_V1": r"$\Delta\bar V_2$", "D2r_D1": r"$\Delta\bar D_2$"}
    f = lambda e: "--" if not np.isfinite(e) else f"{e:.1f}"
    body = []
    lettered = []
    for ft in ["TURNS", "WINDINGS"]:
        body.append(r"\multicolumn{9}{@{}l}{\emph{" + FT[ft].capitalize() + r" faults}} \\")
        for s in order:
            row = [SUITE_SHORT[s]]
            for m in ["PMSG", "SCIG"]:
                r = su[(su.machine == m) & (su.ftype == ft) & (su.suite == s)].iloc[0]
                g = lv[(lv.machine == m) & (lv.ftype == ft) & (lv.suite == s)].sort_values("level_pct").iloc[0]
                others = [x for x in str(r.features_heldout).split("/") if x != r.feature_in]
                feat = lab.get(r.feature_in, tex(r.feature_in))
                if others:
                    letter = "abcdefgh"[len(lettered)]
                    lettered.append((letter, "Some folds chose " + " or ".join(lab.get(x, tex(x)) for x in others) + " instead."))
                    feat += r"$^{\mathrm{" + letter + "}}$"
                row += [feat, f"{f(r.e90_in)} / {f(r.e90_heldout)}", f"{100 * g.share_in:.0f} / {100 * g.share_heldout:.0f}",
                        f"{int(r.fa_heldout)}/{int(r.n_healthy)}"]
            body.append(" & ".join(row) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Held-out run of the complete procedure, PMSG and SCIG, five-cycle windows: fixed feature, $e_{90}$ and "
           "share at the smallest level, in sample / held out, and false alarms of the frozen procedure")
    note = ("Held out: for each tap pair in turn, the pooled null quantile, the screen and the suite's fixed feature are "
            "fitted on the records of the other tap pairs and the healthy trials, frozen, and applied to the held-out pair's "
            "nine trials, which keep their own pre-fault reference; shares aggregate the held-out trials by physical level. "
            "Feature: in-sample fixed feature; a letter marks a suite whose folds chose another feature as well. "
            "$e_{90}$ (\\%): smallest tested level from which the share at the level is $\\ge0.9$ at every level up; -- when none. "
            "Share (\\%) at the smallest tested level of the class. FA: false alarms of the frozen procedure on the nine healthy "
            "trials, each held out of the null and the selection in turn.")
    head = (r"\multirow{2}{*}{Suite} & \multicolumn{4}{c}{PMSG} & \multicolumn{4}{c}{SCIG} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(l){6-9}" "\n"
            r" & feature & $e_{90}$ in/out & share in/out & FA & feature & $e_{90}$ in/out & share in/out & FA")
    return table(body, cap, "tab:heldout", "l" * 9, head, size=r"\tabsize", colsep="3pt", note=note, lettered=lettered)


def t_conventions():
    """Detectable share and MDE of the fixed inter-turn features on the common bench under the baseline convention,
    a stricter fault start, the WFSG interval geometry, a per-speed null and a between-trial (commissioning) reference."""
    ab = pd.read_csv(TAB / "R3_interval_ablation.csv")
    ps = pd.read_csv(TAB / "R3_per_speed_null.csv")
    rh = pd.read_csv(TAB / "R3_reference_horizon.csv")
    want = [("PMSG", "V2r_V1"), ("PMSG", "D2r_D1"), ("PMSG", "I2r_I1"), ("SCIG", "I2r_I1"), ("SCIG", "D2r_D1"), ("SCIG", "V2r_V1")]
    def cell(ds, mde):
        return f"{100 * ds:.0f} ({mde:.1f})" if np.isfinite(mde) else f"{100 * ds:.0f} (--)"
    rows = []
    for name, label in [("baseline", "Baseline (Section~\\ref{sec:computation})"),
                        ("strict start (+120 ms)", "Fault interval from 120\\,ms after the command"),
                        ("WFSG geometry (150 ms fault, 190 ms halves)", "WFSG geometry: 150\\,ms fault, 190\\,ms reference halves")]:
        cells = []
        for m, f in want:
            r = ab[(ab.geometry == name) & (ab.machine == m) & (ab.ftype == "TURNS") & (ab.feature == f)].iloc[0]
            cells.append(cell(r.ds, r.mde))
        rows.append(" & ".join([label] + cells) + r" \\")
    cells = []
    for m, f in want:
        r = ps[(ps.machine == m) & (ps.ftype == "TURNS") & (ps.feature == f)].iloc[0]
        cells.append(cell(r.ds_per_speed, r.mde_per_speed))
    rows.append(" & ".join(["Null quantile per speed (75 records each)"] + cells) + r" \\")
    cells = []
    for m, f in want:
        r = rh[(rh.machine == m) & (rh.ftype == "TURNS") & (rh.feature == f)].iloc[0]
        cells.append(cell(r.ds_between, r.mde_between))
    rows.append(" & ".join(["Reference: healthy trial at the same operating point"] + cells) + r" \\")
    rows[-1] = rows[-1].rstrip(r"\\").rstrip()
    cap = ("Detectable share (\\%) and MDE of the fixed inter-turn features under other interval, null and "
           "reference conventions, five-cycle windows")
    note = ("Cells: detectable share over the 108 inter-turn trials (MDE, \\% of a branch; --: largest level not "
            "detected). The stricter start excludes the relay pick-up; the WFSG geometry shortens the faulted interval "
            "and the reference halves to those of the WFSG bench; the per-speed null replaces the pooled 95th percentile "
            "by one per speed; the last row replaces the trial's own reference by the healthy trial recorded at the "
            "same operating point at another time (Section~\\ref{sec:res-robust}).")
    short = {"I2r_I1": r"$\Delta\bar I_2$", "V2r_V1": r"$\Delta\bar V_2$", "D2r_D1": r"$\Delta\bar D_2$"}
    head = (r"\multirow{2}{*}{Convention} & \multicolumn{3}{c}{PMSG} & \multicolumn{3}{c}{SCIG} \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(l){5-7}" "\n"
            r" & " + " & ".join(short[f] for _, f in want))
    note = note.replace("Cells: detectable share", "$\\Delta\\bar X_2$ stands for the residual $|\\Delta\\bar X_2|/X_1$. Cells: detectable share")
    return table(rows, cap, "tab:conventions", "L{4.8cm}cccccc", head, size=r"\tabsize", colsep="3pt", note=note)


def t_transfer():
    """Table 8: PMSG/SCIG transfer, four referencing rules, AUC and TPR at 1 % FPR on the out-of-reference windows with
    cluster-bootstrap intervals (GBDT; the logistic rows go to the text)."""
    e = pd.read_csv(TAB / "R_transfer2_oor.csv")
    cals = ["raw", "healthy-z", "healthy-z-op", "self-ref"]
    names = {"raw": "physical units", "healthy-z": "$z$, all healthy trials of the target",
             "healthy-z-op": "$z$, healthy trial at the operating point", "self-ref": "$|z|$ against own reference"}
    body = []
    for tr, te in [("PMSG", "PMSG"), ("SCIG", "SCIG"), ("PMSG", "SCIG"), ("SCIG", "PMSG")]:
        rows = {"AUC": [], "TPR": []}
        for cal in cals:
            r = e[(e.calibration == cal) & (e.model == "gbdt") & (e.train == tr) & (e.test == te)].iloc[0]
            rows["AUC"].append(f"{r.auc_oor:.2f} [{r.auc_oor_ci_lo:.2f}, {r.auc_oor_ci_hi:.2f}]")
            rows["TPR"].append(f"{r.tpr_oor:.2f} [{r.tpr_oor_ci_lo:.2f}, {r.tpr_oor_ci_hi:.2f}]")
        body.append(" & ".join([f"{tr[0]}$\\to${te[0]}", "AUC"] + rows["AUC"]) + r" \\")
        body.append(" & ".join(["", "TPR"] + rows["TPR"]) + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("GBDT detector transferred between PMSG and SCIG under four referencing rules, out-of-reference windows")
    note = ("AUC and true-positive rate at 1\\,\\% false-positive rate (TPR) on the out-of-reference windows "
            "(Section~\\ref{sec:computation}); intervals from 500 cluster resamples of the tested machine's trials. "
            "P$\\to$P, S$\\to$S: cross-validation grouped by tap pair; P$\\to$S, S$\\to$P: trained on one machine, tested on the other.")
    head = "Direction & Metric & " + " & ".join(names[c] for c in cals)
    return table(body, cap, "tab:transfer", "llC{2.05cm}C{2.05cm}C{2.05cm}C{2.05cm}", head, size=r"\fontsize{8}{10}\selectfont",
                 colsep="2pt", note=note)


def t_transfer3():
    g = pd.read_csv(TAB / "R_transfer3_oor.csv")
    body = []
    for r in g.itertuples():
        fa = "--" if not np.isfinite(r.fpr_healthy_flt_at_1pct) else pct(r.fpr_healthy_flt_at_1pct)
        body.append(f"{r.train} & {r.test} & {r.auc_oor:.2f} [{r.auc_oor_ci_lo:.2f}, {r.auc_oor_ci_hi:.2f}] & "
                    f"{r.tpr_oor:.2f} [{r.tpr_oor_ci_lo:.2f}, {r.tpr_oor_ci_hi:.2f}] & {fa}" + r" \\")
    body[-1] = body[-1].rstrip(r"\\").rstrip()
    cap = ("Transfer between the three alternatives, self-referenced GBDT detector, three-cycle windows, out-of-reference "
           "windows")
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
    note = ("Fixed feature: the suite's screened feature with the smallest MDE, then the highest share, then the highest median "
            "SDR. MDE bracket (\\%) on the physical levels at "
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


BUILDERS = [("tab_decomp", t_decomp), ("tab_phase", t_phase), ("tab_mde", t_mde), ("tab_suites", t_suites), ("tab_envelope", t_envelope), ("tab_cells", t_decision_cells), ("tab_heldout", t_heldout), ("tab_conventions", t_conventions),
            ("tab_decision", t_decision), ("tab_transfer", t_transfer), ("tab_suites3", t_suites3),
            ("tab_sens", t_sens), ("tab_between", t_between), ("tab_transfer3", t_transfer3), ("tab_nullq", t_nullq)]

if __name__ == "__main__":
    for name, builder in BUILDERS:
        T.write_block(name, builder())
    print("tables written into", T.MAIN)
