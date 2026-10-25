"""Write results/DATA_DICTIONARY.md: the result files, their columns, scopes and code names in the terms of the paper,
and the floor that each file uses.

The descriptions are kept here; the column lists are read from the headers of results/*.csv(.gz), so the dictionary
lists every column of every file. Run after the pipeline: python3 data_dictionary.py
"""
from __future__ import annotations

import gzip
from pathlib import Path

from common import RESULTS

OUT = RESULTS / "DATA_DICTIONARY.md"

FLOORS = {
    "G": "geometry floor: each characteristic in the floor of the alternative's own geometry (reference protocol); "
         "a new family in the floor of the produced family that calibrates, as step 6 scores it",
    "G*": "geometry floor, but a new family (`transfer`) in its own floor, that of the held-out family; the paper's "
          "new-family numbers, in the produced family's floor, are in panel_source_floor.csv and "
          "learn_source_floor.csv",
    "G/O": "both floors for a new family, named in the `floor` column (`source family`: the produced family's, the "
           "paper's reference; `target family`: its own) or in the scope (`transfer (produced family's floor)`)",
    "O": "a new family in its own floor (the floor of its nine runs)",
    "P": "pooled floor over both geometries",
    "U": "the unit of the characteristic (mm or degree); no floor",
    "V": "varies by row: the floor protocol or variant named in the row",
    "-": "no distances",
}

CODES = [
    ("M0", "nominal simulation"), ("M0w", "range of the simulation over thickness and friction"),
    ("M1", "nominal simulation plus the median offset of the calibration alternatives"),
    ("M1s", "scaled simulation, q_p = a + b M0 by least squares"), ("M1n", "median q_p of the calibration alternatives"),
    ("M1sn", "force trend, q_p = a + b force by least squares"), ("NN", "nearest produced setting"),
    ("M2", "envelope plus residual margin"), ("M2n", "M2 without the simulation"),
    ("M3", "boosting correction of the matched simulations, jackknife+ interval"),
    ("M4", "M3n of the paper: boosting without the simulation, jackknife+ interval"),
    ("M5", "GP-corrected envelope"), ("M5n", "M5 without the simulation"),
    ("M6", "conformal margin on standardised residuals around the centre of M5"),
    ("M7", "autoregressive multi-fidelity GP (simulation in the mean)"), ("M7n", "trend GP"),
    ("Mc", "friction-calibrated simulation without discrepancy"),
    ("Mcd", "friction calibration with a GP discrepancy, posterior mixture over the friction grid"),
    ("P+RM", "point prediction of rule P with the relation-matched interval (e.g. NN+RM, M4+RM = M3n+RM)"),
    ("ICM, ICM+sim", "two-task Gaussian processes of the few-shot transfer, without and with the simulation"),
    ("NN-target, shift", "few-shot rules: the new family's own nearest setting; its offset to the other family's record"),
    ("M3|reference, M3|regularised, M3|flexible (and M4|...)", "settings of the boosting tuning study"),
    ("nominal + offset", "M0 with the depth offset removed (Section 5.2)"),
]

SCOPES = [
    ("within", "sibling", "the alternative alone held out; the eight others of its geometry calibrate"),
    ("setting/interpolation", "new process setting, interpolated", "300 kN of a geometry held out"),
    ("setting/extrapolation", "new process setting, extrapolated", "100 or 500 kN of a geometry held out"),
    ("setting", "new process setting", "both of the above"),
    ("transfer", "new family", "one geometry calibrates the rules for the other; the floor follows the file's floor code "
                                "(G*: the new family's own floor; G: the produced family's)"),
    ("transfer (produced family's floor)", "new family", "as `transfer`, labelled explicitly"),
    ("pooled", "sibling, both families calibrating", "with a family term (Gaussian processes only)"),
    ("pooled-setting[/interpolation|/extrapolation]", "new setting, both families calibrating", "with a family term"),
    ("lubricant", "earlier scheme", "one lubrication pattern held out (first version; archive only)"),
]

QCS = [("drawin_mid", "mid-side draw-in (mm)"), ("drawin_corner", "corner draw-in (mm)"),
       ("waviness", "flange waviness (mm)"), ("wall_op10", "wall angle after drawing (degree)"),
       ("arm_op20", "arm angle of the cut part (degree)"), ("depth_op10", "cup depth after drawing (mm)"),
       ("dome_op20", "bottom dome of the cut part (mm)")]

GLOSSARY = [
    ("Identifiers", [
        ("alternative", "produced alternative as geometry/force/lubrication, e.g. concave/300/medium"),
        ("geometry, family", "design family: concave or convex"),
        ("bhf_kN", "blank-holder force (kN), the process setting"),
        ("lubrication", "lubrication pattern: coarse, medium or fine"),
        ("qc", "quality characteristic (codes above); `all` pools the seven"),
        ("method, rule", "rule code (table of code names)"),
        ("scope, relation_scope, calibration", "evidence relation as coded (table of scopes)"),
        ("relation", "evidence relation in words: sibling, interpolation, extrapolation, new family; `pooled ...` "
                     "when both families calibrate"),
        ("subset", "`all`, a characteristic, `family: concave|convex`, or a decision-time stratum "
                   "(`siblings resolvable`, `siblings not resolvable`)"),
        ("prior", "prior of requirement distances: `reference (+-20)` (47 grid distances within +-20 floors) or "
                  "`release-like (+-5)`"),
        ("variant", "label of a sensitivity or robustness variant"),
        ("tau", "standard deviation of the between-run component added to every truth (floors)"),
        ("ref_row", "row of the case in dec_verdicts.csv.gz"),
    ]),
    ("Cases and intervals", [
        ("real_q95", "the truth q_p: 95th percentile of the alternative's 500 parts (unit)"),
        ("lo, hi", "the rule's interval for q_p (unit); equal for a point rule"),
        ("floor", "floor in which the case is scored (unit)"),
        ("sim_env_hi", "top of the simulation envelope over thickness and friction (unit)"),
        ("calib_env_min, calib_env_max, calib_bhf_min, calib_bhf_max, calib_geometries",
         "ranges of the calibration alternatives, used by the applicability guards"),
        ("gp_ls_bhf, gp_ls_lubrication, gp_ls_geometry", "fitted length scales (force in 100 kN, pattern steps)"),
        ("gp_noise, gp_noise_lb, gp_noise_at_bound, gp_ls_at_bound",
         "fitted noise variance, its lower bound (the noise-variance bound) and flags at a bound"),
        ("gp_sf_floors, gp_sn_floors, gp_se_floors", "GP, nugget and sampling standard deviations (pooled floors)"),
        ("gp_beta_sim", "coefficient of the simulation in the mean of M7"),
        ("mcd_mu_mean, mcd_mu_map, mcd_mu_edge_mass", "posterior mean and mode of Mcd's friction and its mass at the "
                                                      "edges of the grid"),
        ("rm_quantile_floors, rm_n", "relation-matched quantile (floors) and the number of borrowed cases behind it"),
    ]),
    ("Distances", [
        ("n_cases, cases", "number of cases (alternative times characteristic)"),
        ("resolution_floors", "decisive distance delta_d (floors)"),
        ("safe_floors", "safe distance delta_s (floors)"),
        ("resolution_lo, resolution_hi, safe_lo, safe_hi", "95 % bootstrap intervals of the two distances"),
        ("resolution_adequate, safe_adequate", "distances from the verdicts on adequate alternatives; safe_adequate is "
                                               "the safe distance on the false-reject side"),
        ("resolution_failing, safe_failing", "distances from the verdicts on failing alternatives; safe_failing is "
                                             "the safe distance on the false-accept side"),
        ("decisive_*, safe_*", "the same distances in files that use these names (e.g. decisive_median over "
                               "between-run draws, decisive_units in the unit)"),
        ("abs_error_p90, abs_error_median", "absolute error of a point rule (floors)"),
        ("design_decisive, design_safe, marginal_decisive, marginal_safe",
         "distances of the design-level verdict (all seven characteristics) and of the marginal verdicts"),
        ("pooled_floor, decisive_units, safe_units, decisive_sigma_lt, ppk_at_decisive_median",
         "Table 6: the distance computed in the unit (cases scored in the pooled floor), in long-term standard "
         "deviations, and the median performance index of a limit at the decisive distance"),
    ]),
    ("Guard bands and verdicts", [
        ("band, band_concave, band_convex, median_band, band_95, band_opt, in_sample_band",
         "guard band g (floors) on its 0.25-floor grid; inf: no band up to the search limit reaches 95 %"),
        ("scheme", "validation of the band: own family with one alternative left out; the other family's band; "
                   "'leave force cell out', the band from both families' cases except the held-out geometry-force cell "
                   "(interpolating, only the other family's cell remains); 'strictly nested', predictions behind the band "
                   "refitted without the held-out alternative"),
        ("share_correct_<geometry>, trial_rate_<geometry>, decided_<geometry>, verdicts_<geometry>",
         "the same quantities per family (concave, convex)"),
        ("share_correct, share_correct_lo, share_correct_hi", "share correct among decided verdicts, with a cluster "
                                                              "bootstrap interval over alternatives"),
        ("trial_rate, trial_lo, trial_hi", "share of verdicts sent to trial"),
        ("decided, verdicts", "numbers of decided and of all verdicts over the prior"),
        ("false_accept_share", "false accepts per verdict"),
        ("share_<qc>, decided_<qc>", "share correct and number of decided verdicts per characteristic"),
        ("worst_characteristic, worst_share_correct", "characteristic with the lowest share correct"),
    ]),
    ("Costs", [
        ("c_fr, c_trial", "costs of a false reject and of a trial, in units of the cost of a false accept"),
        ("cost_*", "expected cost per verdict (units of the false-accept cost): alone (no band), with the 95 % band, "
                   "with the cost-minimising band under step 5's rule (opt: from the 95 % band up to 20 floors, inf: "
                   "every design to trial), or trying every design"),
        ("fa_*, fr_*, trial_*", "false-accept, false-reject and trial rates per verdict under the same bands"),
        ("cheapest, runner_up, margin, fa_of_cheapest", "cheapest option, the next one, their cost difference and the "
                                                        "false-accept rate of the cheapest"),
        ("error_cost, failing_share_of_verdicts", "expected cost of a trial's own errors; share of verdicts on failing "
                                                  "designs under the prior"),
    ]),
    ("Coverage", [
        ("level", "level of an interval rule: guaranteed only with a sibling (largest residual, jackknife+), where the "
                  "held-out alternative is exchangeable with the calibration ones; otherwise nominal"),
        ("coverage, coverage_lo, coverage_hi", "share of truths inside the interval; cluster interval over "
                                               "alternatives with a sibling only"),
        ("ci_note", "why an interval is given or not, and which given intervals are degenerate"),
        ("median_half_width", "median half-width of the interval (floors)"),
        ("interval_score", "mean interval score at level 0.9 (floors)"),
    ]),
    ("Floors and effects", [
        ("floor_lo, floor_hi", "95 % interval of the floor over resampled batches"),
        ("floor_lo_alt, floor_hi_alt", "95 % interval of the floor over resampled alternatives"),
        ("floor_concave, floor_convex", "floor of each geometry (the reference)"),
        ("sd_within, sigma_st, sigma_lt, sigma_b, sigma_w", "standard deviations within the series, between batch means "
                                                            "and between parts"),
        ("effect, esr, esr_lo, esr_hi, p_resolvable", "difference of the centres of two alternatives, its "
                                                      "effect-to-scatter ratio in the pooled floor, interval and "
                                                      "bootstrap probability that it exceeds one"),
        ("slope, mrc, mrc_lo, mrc_hi", "local sensitivity and minimum resolvable change (pooled floor over slope)"),
    ]),
]

# file: (script, contents, floor code, where in the paper)
FILES = {
    "features_rddac.csv": ("features_rddac.py", "one row per produced part: alternative, position in the series, "
                           "process signals and the seven characteristics", "U", "Sections 4.1, 4.3"),
    "features_rddac_sample.csv": ("features_rddac.py", "the same for the sample scans", "U", "Fig. 3"),
    "features_ddacs_rddac.csv": ("features_ddacs.py", "one row per simulation of the RDDAC tools (thickness, friction)",
                                 "U", "Section 4.2"),
    "features_ddacs_corners.csv": ("features_ddacs.py", "simulations at the corners of the design space", "U", "archive"),
    "alt_floor.csv": ("alternatives.py", "floors per characteristic, pooled and per geometry, with intervals", "U",
                      "Table 4"),
    "alt_effects.csv": ("alternatives.py", "contrasts between alternatives and their effect-to-scatter ratios", "P",
                        "Section 5.2"),
    "alt_mrc.csv": ("alternatives.py", "minimum resolvable changes of force and lubrication", "P", "Section 5.2"),
    "dec_intervals.csv": ("decisions.py", "one row per case and rule: interval, truth and floor", "G*",
                          "Tables 5-7, Figs. 1, 5"),
    "dec_resolution.csv": ("decisions.py", "decisive and safe distances by scope and rule", "G*", "Table 5"),
    "dec_paired.csv": ("decisions.py", "paired differences of decisive distances", "G*", "Section 5.7"),
    "dec_gp.csv": ("decisions.py", "hyperparameters of M5 and M5n at their bounds", "-", "Section 5.4"),
    "dec_guard.csv": ("decisions.py", "applicability guards", "G", "archive"),
    "learn_intervals.csv": ("learners.py", "intervals of M7n, M7, Mcd and the P+RM rules per case", "G*",
                            "Tables 5, 7; Figs. 1, 5"),
    "learn_resolution.csv": ("learners.py", "distances of M7n, M7, Mcd and the P+RM rules", "G*",
                             "Table 5"),
    "learn_paired.csv": ("learners.py", "paired differences", "G/O", "Section 5.4"),
    "learn_gp_diagnostics.csv": ("learners.py", "fitted Gaussian processes and where their centres lie (hyperparameters of "
                                 "M7n, M7 and Mcd in pooled floors, centre distances in the floor of the case)", "G",
                                 "Section 5.4"),
    "learn_m7n_priors.csv": ("learners.py --prior-sensitivity", "M7n with each prior median halved or doubled", "G",
                             "Section 5.4"),
    "learn_mcd_posterior.csv": ("learners.py", "posterior of Mcd's friction", "-", "Section 5.2"),
    "learn_fewshot.csv": ("learners.py", "few-shot transfer with one to three alternatives of the new family",
                          "O", "Section 5.4"),
    "learn_source_floor.csv": ("learners.py", "a new family in its own floor", "G/O", "Table 5 (a new family)"),
    "qual_strata.csv": ("qualify.py", "decision-time sibling strata", "-", "Section 5.3"),
    "qual_strata_cases.csv": ("qualify.py", "stratum of every case", "-", "Section 5.3"),
    "qual_guard_decision.csv": ("qualify.py", "guard bands available when deciding, validated by the matching scheme",
                                "G", "Table 7, Sections 5.5, 6.2"),
    "qual_guard_oos.csv": ("qualify.py", "out-of-sample bands, including a force cell left out", "G",
                           "Section 5.5"),
    "qual_guard_family.csv": ("qualify.py", "in-sample bands per family", "G", "archive"),
    "qual_guard_prior_width.csv": ("qualify.py", "band and trial rate against the width of the prior", "G", "Section 5.5"),
    "qual_guard_characteristic.csv": ("qualify.py", "bands per characteristic (earlier version)", "G", "archive"),
    "qual_costs.csv": ("qualify.py", "expected cost per verdict by prior, cost ratio and trial cost, bands under "
                       "step 5's rule", "G",
                       "Fig. 6, Section 5.6"),
    "qual_cost_cheapest.csv": ("qualify.py", "cheapest option per relation and cost setting", "G",
                               "Section 5.6"),
    "qual_trial_cost.csv": ("qualify.py", "expected cost of the errors of a 20- or 50-part trial", "G",
                            "Section 5.6"),
    "qual_trial.csv": ("qualify.py", "a trial of the first 20 or 50 parts scored as a rule", "G", "Section 5.6"),
    "qual_release_capability.csv": ("qualify.py", "release scored on the mean plus four standard deviations, and the "
                                    "true performance index this confirms", "G", "Section 5.6"),
    "qual_between_run.csv": ("qualify.py", "distances and bands with a between-run component", "G",
                             "Sections 5.5, 5.7"),
    "qual_between_run_trial.csv": ("qualify.py", "the trial under the same between-run component", "G",
                                   "Section 5.6"),
    "qual_crossfit.csv": ("qualify.py", "rules and bands selected on one geometry, evaluated on the other", "G",
                          "Section 5.7"),
    "qual_coverage.csv": ("qualify.py", "coverage and interval score per relation, family, characteristic, stratum",
                          "G", "Section 5.4"),
    "qual_m6_coverage.csv": ("qualify.py", "coverage of M6", "G", "Section 5.4"),
    "qual_per_characteristic.csv": ("qualify.py", "distances per characteristic, also in the unit", "G",
                                    "Table 6"),
    "qual_design_level.csv": ("qualify.py", "design-level verdicts over all characteristics", "G", "Section 5.7"),
    "qual_variants.csv": ("qualify.py", "lower limits, short runs, the capability statistic, refitted reference", "G",
                          "Sections 5.6, 5.7"),
    "qual_floor_loao.csv": ("qualify.py", "floors without the held-out alternative's own series", "V", "Section 5.7"),
    "qual_decomposition.csv": ("qualify.py", "paired decomposition of the pre-specified rules", "G", "archive"),
    "qual_resolvable_difference.csv": ("qualify.py", "smallest paired difference this design resolves", "G",
                                       "Section 5.7"),
    "qual_worked_example.csv": ("qualify.py", "every number of the worked example", "G", "Section 3.7"),
    "qual_guard_nested.csv": ("qualify.py", "sibling validation of the nearest setting with strictly nested fits", "G",
                              "Table 7 note"),
    "meas_characteristics.csv": ("simcheck.py", "measurement of the characteristics and their redundancy", "U",
                                 "Table 3"),
    "meas_cut_walls.csv": ("simcheck.py", "walls of the cut part seen by the scanner", "U", "Table 3"),
    "meas_scan.csv": ("measurement.py", "redundancy of the scans per series", "U", "Table 3"),
    "meas_floor.csv": ("measurement.py", "components of the floor: sigma_b, sigma_w, white-noise share", "P",
                       "Section 5.1"),
    "meas_run_floors.csv": ("simcheck.py", "floors of single runs", "V", "Table 4"),
    "meas_sim.csv": ("measurement.py", "extraction noise of the simulated characteristics", "G",
                     "Section 4.2"),
    "meas_tooling_reference.csv": ("simcheck.py", "flange and cup widths fixed by the tools; scale-drift bound", "U",
                                   "Section 5.1"),
    "sim_validation.csv": ("simcheck.py", "simulation against measurement per characteristic, geometry and force",
                           "G", "Section 5.2"),
    "sim_mc_friction.csv": ("simcheck.py", "friction fitted by Mc", "-", "Section 5.2"),
    "sim_grid_comparisons.csv": ("simcheck.py --grid", "comparisons independent of blank and scales over the whole "
                                 "friction-thickness grid", "U", "Section 5.2"),
    "sim_oil_mapping.csv": ("simcheck.py", "draw-in per g/m2 of oil, simulated and measured", "U", "Section 5.2"),
    "sim_depth_offset.csv": ("simcheck.py", "depth and wall offsets of the simulation", "U", "Section 5.2"),
    "sim_envelope_variant.csv": ("simcheck.py", "envelope over the measured incoming variation", "G*", "Section 5.2"),
    "sens_drift.csv": ("sensitivity.py", "floors with and without the time order", "V", "Section 5.1"),
    "inline_drift.csv": ("inline.py", "batch centres predicted from process signals", "-", "Section 5.1"),
    "ds_surrogate_rule.csv": ("design_space.py", "a GP surrogate of the simulations scored as a rule", "G",
                              "Section 5.2"),
    "panel_source_floor.csv": ("panel.py", "a new family in its own floor", "G/O", "Table 5 (a new family)"),
    "panel_floor_protocol.csv": ("panel.py", "other floor protocols", "V", "Section 5.7"),
    "panel_variogram.csv": ("panel.py", "batch differences against their lag", "G", "Section 5.1"),
    "panel_force_effect.csv": ("panel.py", "simulated against measured force effects", "U", "Section 5.2"),
    "panel_arm_sign.csv": ("panel.py", "sign of the arm angle, simulated and measured", "U", "Section 5.2"),
    "panel_capability.csv": ("panel.py", "limits at performance indices 1.0-2.0 above the 95th percentile", "G",
                             "Section 5.6"),
    "panel_failing_weight.csv": ("panel.py", "weight of the failing side against the distance", "G", "Section 3.4"),
    "panel_resolution_steps.csv": ("panel.py", "quantisation steps of the characteristics (mean of the two geometry "
                                   "floors)", "P", "Table 3"),
    "panel_runs.csv": ("panel.py", "run metadata: warm-up, thickness, speed", "U", "Section 4.1"),
    "rob_decisions.csv": ("robustness.py", "robustness variants of data and constants", "V", "Section 5.7"),
    "rob_refit.csv": ("robustness.py", "refitted variants", "V", "Section 5.7"),
    "tune_decisions.csv": ("tuning.py", "boosting tuning study", "G*", "Section 5.4"),
    "tune_intervals.csv": ("tuning.py", "intervals of the tuning study", "G*", "Section 5.4"),
    "budget_design.csv": ("budget.py", "distances against the number and choice of produced alternatives", "G",
                          "Section 5.3"),
    "case2_floor.csv": ("case2_pa12.py", "floor attempt on powder-bed fusion data", "U", "Section 6.4"),
}

PREFIX = {"alt_": "alternatives.py", "budget_": "budget.py", "case2_": "case2_pa12.py", "dec_": "decisions.py",
          "ds_": "design_space.py", "inline_": "inline.py", "learn_": "learners.py", "panel_": "panel.py",
          "qual_": "qualify.py", "rob_": "robustness.py", "scen_": "scenarios.py", "sens_": "sensitivity.py",
          "sim_": "simcheck.py", "tune_": "tuning.py", "meas_": "measurement.py or simcheck.py"}


def header(path: Path) -> list[str]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as f:
        return f.readline().rstrip("\n").split(",")


def main() -> None:
    files = sorted(RESULTS.glob("*.csv")) + sorted(RESULTS.glob("*.csv.gz"))
    out = ["# Data dictionary of the result files", "",
           "Written by `scripts/data_dictionary.py` from the headers of `results/*.csv`; it translates file names, "
           "columns, scopes and rule codes into the terms of the paper and names the floor each file uses. "
           "`findings.md` maps the numbers of the paper to these files.", "",
           "## Units and floors", "",
           "Quantities are in the unit of the characteristic (mm or degree) unless a column ends in `_floors` or is a "
           "distance or band, which are in within-run floors. The floor of a characteristic is the 95 % quantile of "
           "the difference between the 10 % trimmed means of two batches of 50 consecutive parts of one alternative "
           "(all pairs of the ten batches of a run). Floor codes used below:", ""]
    out += [f"- **{k}**: {v}" for k, v in FLOORS.items()]
    out += ["", "M7n, M7 and Mcd are fitted in pooled floors; their distances, like those of every rule, are scored in "
            "the geometry floor.", "", "## Rule codes", "", "| Code | Rule in the paper |", "|---|---|"]
    out += [f"| {c} | {d} |" for c, d in CODES]
    out += ["", "## Scopes (evidence relations)", "", "| `scope` | Relation in the paper | Scheme |", "|---|---|---|"]
    out += [f"| `{s}` | {r} | {d} |" for s, r, d in SCOPES]
    out += ["", "## Characteristics (`qc`)", "", "| Code | Characteristic |", "|---|---|"]
    out += [f"| `{c}` | {d} |" for c, d in QCS]
    out += ["", "## Columns", ""]
    for group, rows in GLOSSARY:
        out += [f"**{group}**", "", "| Column | Meaning |", "|---|---|"]
        out += [f"| `{c}` | {d} |" for c, d in rows]
        out.append("")
    out += ["## Files", "",
            "Where: the place in the paper; `archive` marks files of earlier versions that "
            "the paper no longer cites.", "", "| File | Script | Contents | Floor | Where |", "|---|---|---|---|---|"]
    for f in files:
        name = f.name
        if name in FILES:
            script, what, fl, where = FILES[name]
        else:
            script = next((v for k, v in PREFIX.items() if name.startswith(k)), "")
            what, fl, where = "supporting or earlier analysis", "see script", "archive"
        out.append(f"| `{name}` | `{script}` | {what} | {fl} | {where} |")
    out += ["", "## Columns of every file", "",
            "Columns not in the glossary above are defined where the producing function writes them.", ""]
    for f in files:
        out.append(f"- `{f.name}`: " + ", ".join(f"`{c}`" for c in header(f)))
    OUT.write_text("\n".join(out) + "\n")
    print(f"written {OUT}")


if __name__ == "__main__":
    main()
