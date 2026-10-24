# Data dictionary of the result files

Written by `scripts/data_dictionary.py` from the headers of `results/*.csv`; it translates file names, columns, scopes and rule codes into the terms of the paper and names the floor each file uses. `findings.md` maps the numbers of the paper and of Online Resource 1 to these files.

## Units and floors

Quantities are in the unit of the characteristic (mm or degree) unless a column ends in `_floors` or is a distance or band, which are in within-run floors. The floor of a characteristic is the 95 % quantile of the difference between the 10 % trimmed means of two batches of 50 consecutive parts of one alternative (all pairs of the ten batches of a run). Floor codes used below:

- **G**: geometry floor: each characteristic in the floor of the alternative's own geometry (reference protocol); a new family in the floor of the produced family that calibrates, as step 6 scores it
- **G***: geometry floor, but a new family (`transfer`) in its own floor, that of the held-out family; the paper's new-family numbers, in the produced family's floor, are in panel_source_floor.csv and learn_source_floor.csv
- **G/O**: both floors for a new family, named in the `floor` column (`source family`: the produced family's, the paper's reference; `target family`: its own) or in the scope (`transfer (produced family's floor)`)
- **O**: a new family in its own floor (the floor of its nine runs)
- **P**: pooled floor over both geometries
- **U**: the unit of the characteristic (mm or degree); no floor
- **V**: varies by row: the floor protocol or variant named in the row
- **-**: no distances

M7n, M7 and Mcd are fitted in pooled floors; their distances, like those of every rule, are scored in the geometry floor.

## Rule codes

| Code | Rule in the paper |
|---|---|
| M0 | nominal simulation |
| M0w | range of the simulation over thickness and friction |
| M1 | nominal simulation plus the median offset of the calibration alternatives |
| M1s | scaled simulation, q_p = a + b M0 by least squares |
| M1n | median q_p of the calibration alternatives |
| M1sn | force trend, q_p = a + b force by least squares |
| NN | nearest produced setting |
| M2 | envelope plus residual margin |
| M2n | M2 without the simulation |
| M3 | boosting correction of the matched simulations, jackknife+ interval |
| M4 | M3n of the paper: boosting without the simulation, jackknife+ interval |
| M5 | GP-corrected envelope |
| M5n | M5 without the simulation |
| M6 | conformal margin on standardised residuals around the centre of M5 |
| M7 | autoregressive multi-fidelity GP (simulation in the mean) |
| M7n | trend GP |
| Mc | friction-calibrated simulation without discrepancy |
| Mcd | friction calibration with a GP discrepancy, posterior mixture over the friction grid |
| P+RM | point prediction of rule P with the relation-matched interval (e.g. NN+RM, M4+RM = M3n+RM) |
| ICM, ICM+sim | two-task Gaussian processes of the few-shot transfer, without and with the simulation |
| NN-target, shift | few-shot rules: the new family's own nearest setting; its offset to the other family's record |
| M3|reference, M3|regularised, M3|flexible (and M4|...) | settings of the boosting tuning study |
| nominal + offset | M0 with the depth offset removed (Section 5.2) |

## Scopes (evidence relations)

| `scope` | Relation in the paper | Scheme |
|---|---|---|
| `within` | sibling | the alternative alone held out; the eight others of its geometry calibrate |
| `setting/interpolation` | new process setting, interpolated | 300 kN of a geometry held out |
| `setting/extrapolation` | new process setting, extrapolated | 100 or 500 kN of a geometry held out |
| `setting` | new process setting | both of the above |
| `transfer` | new family | one geometry calibrates the rules for the other; the floor follows the file's floor code (G*: the new family's own floor; G: the produced family's) |
| `transfer (produced family's floor)` | new family | as `transfer`, labelled explicitly |
| `pooled` | sibling, both families calibrating | with a family term (Gaussian processes only) |
| `pooled-setting[/interpolation|/extrapolation]` | new setting, both families calibrating | with a family term |
| `lubricant` | earlier scheme | one lubrication pattern held out (first version; archive only) |

## Characteristics (`qc`)

| Code | Characteristic |
|---|---|
| `drawin_mid` | mid-side draw-in (mm) |
| `drawin_corner` | corner draw-in (mm) |
| `waviness` | flange waviness (mm) |
| `wall_op10` | wall angle after drawing (degree) |
| `arm_op20` | arm angle of the cut part (degree) |
| `depth_op10` | cup depth after drawing (mm) |
| `dome_op20` | bottom dome of the cut part (mm) |

## Columns

**Identifiers**

| Column | Meaning |
|---|---|
| `alternative` | produced alternative as geometry/force/lubrication, e.g. concave/300/medium |
| `geometry, family` | design family: concave or convex |
| `bhf_kN` | blank-holder force (kN), the process setting |
| `lubrication` | lubrication pattern: coarse, medium or fine |
| `qc` | quality characteristic (codes above); `all` pools the seven |
| `method, rule` | rule code (table of code names) |
| `scope, relation_scope, calibration` | evidence relation as coded (table of scopes) |
| `relation` | evidence relation in words: sibling, interpolation, extrapolation, new family; `pooled ...` when both families calibrate |
| `subset` | `all`, a characteristic, `family: concave|convex`, or a decision-time stratum (`siblings resolvable`, `siblings not resolvable`) |
| `prior` | prior of requirement distances: `reference (+-20)` (47 grid distances within +-20 floors) or `release-like (+-5)` |
| `variant` | label of a sensitivity or robustness variant |
| `tau` | standard deviation of the between-run component added to every truth (floors) |
| `ref_row` | row of the case in dec_verdicts.csv.gz |

**Cases and intervals**

| Column | Meaning |
|---|---|
| `real_q95` | the truth q_p: 95th percentile of the alternative's 500 parts (unit) |
| `lo, hi` | the rule's interval for q_p (unit); equal for a point rule |
| `floor` | floor in which the case is scored (unit) |
| `sim_env_hi` | top of the simulation envelope over thickness and friction (unit) |
| `calib_env_min, calib_env_max, calib_bhf_min, calib_bhf_max, calib_geometries` | ranges of the calibration alternatives, used by the applicability guards |
| `gp_ls_bhf, gp_ls_lubrication, gp_ls_geometry` | fitted length scales (force in 100 kN, pattern steps) |
| `gp_noise, gp_noise_lb, gp_noise_at_bound, gp_ls_at_bound` | fitted noise variance, its lower bound (the noise-variance bound) and flags at a bound |
| `gp_sf_floors, gp_sn_floors, gp_se_floors` | GP, nugget and sampling standard deviations (pooled floors) |
| `gp_beta_sim` | coefficient of the simulation in the mean of M7 |
| `mcd_mu_mean, mcd_mu_map, mcd_mu_edge_mass` | posterior mean and mode of Mcd's friction and its mass at the edges of the grid |
| `rm_quantile_floors, rm_n` | relation-matched quantile (floors) and the number of borrowed cases behind it |

**Distances**

| Column | Meaning |
|---|---|
| `n_cases, cases` | number of cases (alternative times characteristic) |
| `resolution_floors` | decisive distance delta_d (floors) |
| `safe_floors` | safe distance delta_s (floors) |
| `resolution_lo, resolution_hi, safe_lo, safe_hi` | 95 % bootstrap intervals of the two distances |
| `resolution_adequate, safe_adequate` | distances from the verdicts on adequate alternatives; safe_adequate is the safe distance on the false-reject side |
| `resolution_failing, safe_failing` | distances from the verdicts on failing alternatives; safe_failing is the safe distance on the false-accept side |
| `decisive_*, safe_*` | the same distances in files that use these names (e.g. decisive_median over between-run draws, decisive_units in the unit) |
| `abs_error_p90, abs_error_median` | absolute error of a point rule (floors) |
| `design_decisive, design_safe, marginal_decisive, marginal_safe` | distances of the design-level verdict (all seven characteristics) and of the marginal verdicts |
| `pooled_floor, decisive_units, safe_units, decisive_sigma_lt, ppk_at_decisive_median` | Table 6: the distance computed in the unit (cases scored in the pooled floor), in long-term standard deviations, and the median performance index of a limit at the decisive distance |

**Guard bands and verdicts**

| Column | Meaning |
|---|---|
| `band, band_concave, band_convex, median_band, band_95, band_opt, in_sample_band` | guard band g (floors) on its 0.25-floor grid; inf: no band up to the search limit reaches 95 % |
| `scheme` | validation of the band: own family with one alternative left out; the other family's band; 'leave force cell out', the band from both families' cases except the held-out geometry-force cell (interpolating, only the other family's cell remains); 'strictly nested', predictions behind the band refitted without the held-out alternative |
| `share_correct_<geometry>, trial_rate_<geometry>, decided_<geometry>, verdicts_<geometry>` | the same quantities per family (concave, convex) |
| `share_correct, share_correct_lo, share_correct_hi` | share correct among decided verdicts, with a cluster bootstrap interval over alternatives |
| `trial_rate, trial_lo, trial_hi` | share of verdicts sent to trial |
| `decided, verdicts` | numbers of decided and of all verdicts over the prior |
| `false_accept_share` | false accepts per verdict |
| `share_<qc>, decided_<qc>` | share correct and number of decided verdicts per characteristic |
| `worst_characteristic, worst_share_correct` | characteristic with the lowest share correct |

**Costs**

| Column | Meaning |
|---|---|
| `c_fr, c_trial` | costs of a false reject and of a trial, in units of the cost of a false accept |
| `cost_*` | expected cost per verdict (units of the false-accept cost): alone (no band), with the 95 % band, with the cost-minimising band under step 5's rule (opt: from the 95 % band up to 20 floors, inf: every design to trial), or trying every design |
| `fa_*, fr_*, trial_*` | false-accept, false-reject and trial rates per verdict under the same bands |
| `cheapest, runner_up, margin, fa_of_cheapest` | cheapest option, the next one, their cost difference and the false-accept rate of the cheapest |
| `error_cost, failing_share_of_verdicts` | expected cost of a trial's own errors; share of verdicts on failing designs under the prior |

**Coverage**

| Column | Meaning |
|---|---|
| `level` | level of an interval rule: guaranteed only with a sibling (largest residual, jackknife+), where the held-out alternative is exchangeable with the calibration ones; otherwise nominal |
| `coverage, coverage_lo, coverage_hi` | share of truths inside the interval; cluster interval over alternatives with a sibling only |
| `ci_note` | why an interval is given or not, and which given intervals are degenerate |
| `median_half_width` | median half-width of the interval (floors) |
| `interval_score` | mean interval score at level 0.9 (floors) |

**Floors and effects**

| Column | Meaning |
|---|---|
| `floor_lo, floor_hi` | 95 % interval of the floor over resampled batches |
| `floor_lo_alt, floor_hi_alt` | 95 % interval of the floor over resampled alternatives |
| `floor_concave, floor_convex` | floor of each geometry (the reference) |
| `sd_within, sigma_st, sigma_lt, sigma_b, sigma_w` | standard deviations within the series, between batch means and between parts |
| `effect, esr, esr_lo, esr_hi, p_resolvable` | difference of the centres of two alternatives, its effect-to-scatter ratio in the pooled floor, interval and bootstrap probability that it exceeds one |
| `slope, mrc, mrc_lo, mrc_hi` | local sensitivity and minimum resolvable change (pooled floor over slope) |

## Files

Where: the place in the paper (Online Resource 1 as OR); `archive` marks files of earlier versions that the paper no longer cites.

| File | Script | Contents | Floor | Where |
|---|---|---|---|---|
| `alt_effects.csv` | `alternatives.py` | contrasts between alternatives and their effect-to-scatter ratios | P | Section 5.2 |
| `alt_floor.csv` | `alternatives.py` | floors per characteristic, pooled and per geometry, with intervals | U | Table 4 |
| `alt_mrc.csv` | `alternatives.py` | minimum resolvable changes of force and lubrication | P | Section 5.2 |
| `budget_design.csv` | `budget.py` | distances against the number and choice of produced alternatives | G | Section 5.3 |
| `budget_resolution.csv` | `budget.py` | supporting or earlier analysis | see script | archive |
| `case2_budget.csv` | `case2_pa12.py` | supporting or earlier analysis | see script | archive |
| `case2_effects.csv` | `case2_pa12.py` | supporting or earlier analysis | see script | archive |
| `case2_floor.csv` | `case2_pa12.py` | floor attempt on powder-bed fusion data | U | Section 6.4 |
| `case2_resolution.csv` | `case2_pa12.py` | supporting or earlier analysis | see script | archive |
| `dec_alternatives.csv` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `dec_coverage.csv` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `dec_curve.csv` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `dec_gp.csv` | `decisions.py` | hyperparameters of M5 and M5n at their bounds | - | OR S5 |
| `dec_guard.csv` | `decisions.py` | applicability guards | G | archive |
| `dec_intervals.csv` | `decisions.py` | one row per case and rule: interval, truth and floor | G* | Tables 5-7, Figs. 1, 5 |
| `dec_margins.csv` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `dec_paired.csv` | `decisions.py` | paired differences of decisive distances | G* | Section 5.7 |
| `dec_reliability.csv` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `dec_resolution.csv` | `decisions.py` | decisive and safe distances by scope and rule | G* | Table 5; OR S1 |
| `dec_scores.csv` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `ds_sensitivity.csv` | `design_space.py` | supporting or earlier analysis | see script | archive |
| `ds_surrogate.csv` | `design_space.py` | supporting or earlier analysis | see script | archive |
| `ds_surrogate_rule.csv` | `design_space.py` | a GP surrogate of the simulations scored as a rule | G | Section 5.2 |
| `features_ddacs_corners.csv` | `features_ddacs.py` | simulations at the corners of the design space | U | archive |
| `features_ddacs_rddac.csv` | `features_ddacs.py` | one row per simulation of the RDDAC tools (thickness, friction) | U | Section 4.2 |
| `features_rddac.csv` | `features_rddac.py` | one row per produced part: alternative, position in the series, process signals and the seven characteristics | U | Sections 4.1, 4.3 |
| `features_rddac_sample.csv` | `features_rddac.py` | the same for the sample scans | U | Fig. 3 |
| `inline_drift.csv` | `inline.py` | batch centres predicted from process signals | - | Section 5.1 |
| `inline_lod.csv` | `inline.py` | supporting or earlier analysis | see script | archive |
| `learn_fewshot.csv` | `learners.py` | few-shot transfer with one to three alternatives of the new family | O | Section 5.4 |
| `learn_gp_diagnostics.csv` | `learners.py` | fitted Gaussian processes and where their centres lie (hyperparameters of M7n, M7 and Mcd in pooled floors, centre distances in the floor of the case) | G | Section 5.4; OR S5 |
| `learn_intervals.csv` | `learners.py` | intervals of M7n, M7, Mcd and the P+RM rules per case | G* | Tables 5, 7; Figs. 1, 5 |
| `learn_m7n_priors.csv` | `learners.py --prior-sensitivity` | M7n with each prior median halved or doubled | G | Section 5.4; OR S6 |
| `learn_mcd_posterior.csv` | `learners.py` | posterior of Mcd's friction | - | Section 5.2 |
| `learn_paired.csv` | `learners.py` | paired differences | G/O | Section 5.4 |
| `learn_resolution.csv` | `learners.py` | distances of M7n, M7, Mcd and the P+RM rules | G* | Table 5; OR S1, S7 |
| `learn_source_floor.csv` | `learners.py` | a new family in its own floor | G/O | OR S1 |
| `meas_characteristics.csv` | `simcheck.py` | measurement of the characteristics and their redundancy | U | Table 3 |
| `meas_cut_walls.csv` | `simcheck.py` | walls of the cut part seen by the scanner | U | Table 3 |
| `meas_floor.csv` | `measurement.py` | components of the floor: sigma_b, sigma_w, white-noise share | P | Section 5.1; OR S4 |
| `meas_run_floors.csv` | `simcheck.py` | floors of single runs | V | Table 4 |
| `meas_scan.csv` | `measurement.py` | redundancy of the scans per series | U | Table 3; OR S4 |
| `meas_sim.csv` | `measurement.py` | extraction noise of the simulated characteristics | G | Section 4.2; OR S3 |
| `meas_tooling_reference.csv` | `simcheck.py` | flange and cup widths fixed by the tools; scale-drift bound | U | Section 5.1 |
| `panel_arm_sign.csv` | `panel.py` | sign of the arm angle, simulated and measured | U | Section 5.2 |
| `panel_capability.csv` | `panel.py` | limits at performance indices 1.0-2.0 above the 95th percentile | G | Section 5.6 |
| `panel_decomposition.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_failing_weight.csv` | `panel.py` | weight of the failing side against the distance | G | Section 3.4 |
| `panel_floor_protocol.csv` | `panel.py` | other floor protocols | V | Section 5.7; OR S4 |
| `panel_force_effect.csv` | `panel.py` | simulated against measured force effects | U | Section 5.2 |
| `panel_force_levels.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_guard_priors.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_m0_split.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_nominal_offset.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_physical_units.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_q95_unit.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_resolution_steps.csv` | `panel.py` | quantisation steps of the characteristics (mean of the two geometry floors) | P | Table 3 |
| `panel_runs.csv` | `panel.py` | run metadata: warm-up, thickness, speed | U | Section 4.1 |
| `panel_sibling_strata.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_source_floor.csv` | `panel.py` | a new family in its own floor | G/O | OR S1 |
| `panel_source_floor_curve.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_source_floor_paired.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_step6.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_step6_curves.csv` | `panel.py` | supporting or earlier analysis | see script | archive |
| `panel_variogram.csv` | `panel.py` | batch differences against their lag | G | Section 5.1 |
| `qual_between_run.csv` | `qualify.py` | distances and bands with a between-run component | G | Sections 5.5, 5.7; OR S14 |
| `qual_between_run_trial.csv` | `qualify.py` | the trial under the same between-run component | G | Section 5.6; OR S14 |
| `qual_cost_cheapest.csv` | `qualify.py` | cheapest option per relation and cost setting | G | Section 5.6; OR S13 |
| `qual_costs.csv` | `qualify.py` | expected cost per verdict by prior, cost ratio and trial cost, bands under step 5's rule | G | Fig. 6, Section 5.6; OR S13 |
| `qual_coverage.csv` | `qualify.py` | coverage and interval score per relation, family, characteristic, stratum | G | Section 5.4; OR S8, S9 |
| `qual_crossfit.csv` | `qualify.py` | rules and bands selected on one geometry, evaluated on the other | G | Section 5.7; OR S15 |
| `qual_decomposition.csv` | `qualify.py` | paired decomposition of the pre-specified rules | G | archive |
| `qual_design_level.csv` | `qualify.py` | design-level verdicts over all characteristics | G | Section 5.7 |
| `qual_floor_loao.csv` | `qualify.py` | floors without the held-out alternative's own series | V | Section 5.7 |
| `qual_guard_characteristic.csv` | `qualify.py` | bands per characteristic (earlier version) | G | archive |
| `qual_guard_decision.csv` | `qualify.py` | guard bands available when deciding, validated by the matching scheme | G | Table 7, Sections 5.5, 6.2; OR S10, S11 |
| `qual_guard_family.csv` | `qualify.py` | in-sample bands per family | G | archive |
| `qual_guard_nested.csv` | `qualify.py` | sibling validation of the nearest setting with strictly nested fits | G | Table 7 note |
| `qual_guard_oos.csv` | `qualify.py` | out-of-sample bands, including a force cell left out | G | Section 5.5; OR S10 |
| `qual_guard_prior_width.csv` | `qualify.py` | band and trial rate against the width of the prior | G | OR S12 |
| `qual_m6_coverage.csv` | `qualify.py` | coverage of M6 | G | OR S8 |
| `qual_per_characteristic.csv` | `qualify.py` | distances per characteristic, also in the unit | G | Table 6; OR S2 |
| `qual_release_capability.csv` | `qualify.py` | release scored on the mean plus four standard deviations, and the true performance index this confirms | G | Section 5.6 |
| `qual_resolvable_difference.csv` | `qualify.py` | smallest paired difference this design resolves | G | Section 5.7 |
| `qual_strata.csv` | `qualify.py` | decision-time sibling strata | - | Section 5.3 |
| `qual_strata_cases.csv` | `qualify.py` | stratum of every case | - | Section 5.3 |
| `qual_trial.csv` | `qualify.py` | a trial of the first 20 or 50 parts scored as a rule | G | Section 5.6 |
| `qual_trial_cost.csv` | `qualify.py` | expected cost of the errors of a 20- or 50-part trial | G | Section 5.6; OR S13 |
| `qual_variants.csv` | `qualify.py` | lower limits, short runs, the capability statistic, refitted reference | G | Sections 5.6, 5.7 |
| `qual_worked_example.csv` | `qualify.py` | every number of the worked example | G | Section 3.7 |
| `rob_bhf_pairs.csv` | `robustness.py` | supporting or earlier analysis | see script | archive |
| `rob_decisions.csv` | `robustness.py` | robustness variants of data and constants | V | Section 5.7; OR S1 |
| `rob_floor.csv` | `robustness.py` | supporting or earlier analysis | see script | archive |
| `rob_floor_between.csv` | `robustness.py` | supporting or earlier analysis | see script | archive |
| `rob_refit.csv` | `robustness.py` | refitted variants | V | Section 5.7 |
| `rob_refit_paired.csv` | `robustness.py` | supporting or earlier analysis | see script | archive |
| `scen_cost.csv` | `scenarios.py` | supporting or earlier analysis | see script | archive |
| `scen_cost_map.csv` | `scenarios.py` | supporting or earlier analysis | see script | archive |
| `scen_scores.csv` | `scenarios.py` | supporting or earlier analysis | see script | archive |
| `scen_scores_by_class.csv` | `scenarios.py` | supporting or earlier analysis | see script | archive |
| `scen_strata.csv` | `scenarios.py` | supporting or earlier analysis | see script | archive |
| `scen_truth.csv` | `scenarios.py` | supporting or earlier analysis | see script | archive |
| `sens_drift.csv` | `sensitivity.py` | floors with and without the time order | V | Section 5.1; OR S4 |
| `sens_esr.csv` | `sensitivity.py` | supporting or earlier analysis | see script | archive |
| `sens_floor.csv` | `sensitivity.py` | supporting or earlier analysis | see script | archive |
| `sim_depth_offset.csv` | `simcheck.py` | depth and wall offsets of the simulation | U | Section 5.2 |
| `sim_envelope_ranges.csv` | `simcheck.py` | supporting or earlier analysis | see script | archive |
| `sim_envelope_variant.csv` | `simcheck.py` | envelope over the measured incoming variation | G* | Section 5.2 |
| `sim_grid_comparisons.csv` | `simcheck.py --grid` | comparisons independent of blank and scales over the whole friction-thickness grid | U | Section 5.2; OR S3 note |
| `sim_mc_friction.csv` | `simcheck.py` | friction fitted by Mc | - | Section 5.2; OR S3 |
| `sim_oil_mapping.csv` | `simcheck.py` | draw-in per g/m2 of oil, simulated and measured | U | Section 5.2 |
| `sim_validation.csv` | `simcheck.py` | simulation against measurement per characteristic, geometry and force | G | Section 5.2; OR S3 |
| `tune_decisions.csv` | `tuning.py` | boosting tuning study | G* | Section 5.4 |
| `tune_intervals.csv` | `tuning.py` | intervals of the tuning study | G* | Section 5.4 |
| `dec_verdicts.csv.gz` | `decisions.py` | supporting or earlier analysis | see script | archive |
| `learn_fewshot_intervals.csv.gz` | `learners.py` | supporting or earlier analysis | see script | archive |

## Columns of every file

Columns not in the glossary above are defined where the producing function writes them.

- `alt_effects.csv`: `family`, `a`, `b`, `qc`, `effect`, `esr`, `esr_lo`, `esr_hi`, `p_resolvable`
- `alt_floor.csv`: `qc`, `label`, `unit`, `floor`, `floor_lo`, `floor_hi`, `floor_lo_alt`, `floor_hi_alt`, `floor_concave`, `floor_convex`, `sd_within`
- `alt_mrc.csv`: `qc`, `factor`, `slope`, `mrc`, `mrc_lo`, `mrc_hi`
- `budget_design.csv`: `relation`, `k`, `method`, `cases`, `resolution_floors`, `safe_floors`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`, `error_at_10`, `abstain_at_10`, `pairs`, `pairs_with_wrong_at_10`, `wrong_share_p90`
- `budget_resolution.csv`: `relation`, `k`, `method`, `cases`, `resolution_floors`, `safe_floors`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`, `error_at_10`, `abstain_at_10`, `pairs`, `pairs_with_wrong_at_10`, `wrong_share_p90`
- `case2_budget.csv`: `k`, `method`, `resolution_floors`, `safe_floors`, `wrong_at_10`, `uncertain_at_10`
- `case2_effects.csv`: `qc`, `a`, `b`, `esr`
- `case2_floor.csv`: `qc`, `floor`, `n_batches`, `sd_within`, `measurement_note`
- `case2_resolution.csv`: `scope`, `method`, `qc`, `resolution_floors`, `safe_floors`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`
- `dec_alternatives.csv`: `alternative`, `geometry`, `bhf_kN`, `oil_type`, `qc`, `n_parts`, `real_centre`, `real_q95`, `real_q95_se`, `real_sd`, `sim_nominal`, `sim_env_lo`, `sim_env_hi`, `sim_matched_centre`, `real_centre_signed`, `sim_nominal_signed`, `sim_matched_centre_signed`, `gap_matched`, `gap_matched_signed`
- `dec_coverage.csv`: `scope`, `method`, `n_cases`, `coverage`, `half_width_floors`, `centre_decisive`
- `dec_curve.csv`: `scope`, `method`, `d`, `correct`, `false_accept`, `false_reject`, `abstain`, `error_when_decided`
- `dec_gp.csv`: `scope`, `method`, `fits`, `noise_at_bound`, `length_scale_at_bound`, `median_ls_bhf`, `median_noise`
- `dec_guard.csv`: `guard`, `scope`, `method`, `resolution_floors`, `resolution_lo`, `resolution_hi`, `safe_floors`, `safe_lo`, `safe_hi`, `cases`, `cases_guarded`, `verdicts_through`, `right_through`, `wrong_through`, `trial_through`, `false_alarms`, `verdicts_guarded`, `share_right_all`, `share_wrong_all`, `wrong_rate_through`, `false_alarm_rate`
- `dec_intervals.csv`: `calibration`, `relation`, `alternative`, `geometry`, `bhf_kN`, `qc`, `method`, `lo`, `hi`, `real_q95`, `floor`, `sim_env_hi`, `calib_env_min`, `calib_env_max`, `calib_bhf_min`, `calib_bhf_max`, `calib_geometries`, `gp_ls_bhf`, `gp_ls_lubrication`, `gp_noise`, `gp_noise_lb`, `gp_noise_at_bound`, `gp_ls_at_bound`, `gp_ls_geometry`, `scope`, `ref_row`
- `dec_margins.csv`: `qc`, `offset_env`, `margin`, `offset_nominal`, `n_alternatives`
- `dec_paired.csv`: `scope`, `rule_a`, `rule_b`, `resolution_diff`, `resolution_diff_lo`, `resolution_diff_hi`, `resolution_share_a_smaller`, `safe_diff`, `safe_diff_lo`, `safe_diff_hi`, `safe_share_a_smaller`
- `dec_reliability.csv`: `scope`, `method`, `margin_floors`, `n_decided`, `share_of_verdicts`, `correct_when_decided`
- `dec_resolution.csv`: `scope`, `method`, `qc`, `n_cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`
- `dec_scores.csv`: `calibration`, `qc`, `method`, `correct`, `false_accept`, `false_reject`, `abstain`, `error_when_decided`
- `ds_sensitivity.csv`: `geometry`, `qc`, `factor`, `unit`, `sim_sensitivity`, `sim_sens_sd`, `real_sensitivity`, `floor`, `resolvable_steps_real`, `n_pairs`, `mrc_real_floor`, `mrc_sim_floor`, `mrc_sim_floor_plus_margin`
- `ds_surrogate.csv`: `geometry`, `qc`, `rmse_loo`, `n`, `floor`, `rmse_over_floor`
- `ds_surrogate_rule.csv`: `rule`, `source`, `resolution_floors`, `safe_floors`
- `features_ddacs_corners.csv`: `blankholder_force`, `bottom_radius`, `curvature_radius`, `friction_coefficient`, `geometry`, `index`, `material_scaling_factor`, `sheet_metal_thickness`, `wall_angle`, `op10_dome_mm`, `op10_depth_mm`, `op10_wall_r15_x_mm`, `op10_wall_angle_x_deg`, `op10_theta_x_deg`, `op10_rise_x_mm`, `op10_seg_x_mm`, `op10_wall_r15_y_mm`, `op10_wall_angle_y_deg`, `op10_theta_y_deg`, `op10_rise_y_mm`, `op10_seg_y_mm`, `op10_theta_mean_deg`, `op10_Wx_mm`, `op10_Wy_mm`, `op10_Ld_mm`, `op10_drawin_mid_mm`, `op10_drawin_corner_mm`, `op10_wav_sd_mm`, `op20_dome_mm`, `op20_depth_mm`, `op20_wall_r15_x_mm`, `op20_wall_angle_x_deg`, `op20_theta_x_deg`, `op20_rise_x_mm`, `op20_seg_x_mm`, `op20_wall_r15_y_mm`, `op20_wall_angle_y_deg`, `op20_theta_y_deg`, `op20_rise_y_mm`, `op20_seg_y_mm`, `op20_theta_mean_deg`, `sim_thin_min_ratio`, `sim_thick_max_ratio`, `sim_eps_max`, `sim_op20_springback_max_mm`, `status`, `member`, `seconds`
- `features_ddacs_rddac.csv`: `blankholder_force`, `bottom_radius`, `curvature_radius`, `friction_coefficient`, `geometry`, `index`, `material_scaling_factor`, `sheet_metal_thickness`, `wall_angle`, `op10_dome_mm`, `op10_depth_mm`, `op10_wall_r15_x_mm`, `op10_wall_angle_x_deg`, `op10_theta_x_deg`, `op10_rise_x_mm`, `op10_seg_x_mm`, `op10_wall_r15_y_mm`, `op10_wall_angle_y_deg`, `op10_theta_y_deg`, `op10_rise_y_mm`, `op10_seg_y_mm`, `op10_theta_mean_deg`, `op10_Wx_mm`, `op10_Wy_mm`, `op10_Ld_mm`, `op10_drawin_mid_mm`, `op10_drawin_corner_mm`, `op10_wav_sd_mm`, `op20_dome_mm`, `op20_depth_mm`, `op20_wall_r15_x_mm`, `op20_wall_angle_x_deg`, `op20_theta_x_deg`, `op20_rise_x_mm`, `op20_seg_x_mm`, `op20_wall_r15_y_mm`, `op20_wall_angle_y_deg`, `op20_theta_y_deg`, `op20_rise_y_mm`, `op20_seg_y_mm`, `op20_theta_mean_deg`, `sim_thin_min_ratio`, `sim_thick_max_ratio`, `sim_eps_max`, `sim_op20_springback_max_mm`, `status`, `member`, `seconds`
- `features_rddac.csv`: `index`, `experiment_id`, `category`, `geometry`, `bhf_kN`, `oil_type`, `mean_punch_temp_attr`, `F10_kN`, `F20_kN`, `F25_kN`, `W_draw_J`, `F_peak_kN`, `F_rest_kN`, `imbalance20`, `v_form_mm_s`, `punch_temp_C`, `pos_bdc_mm`, `cycle_s`, `sheet_um`, `sheet_sd_um`, `sheet_n`, `oil_gm2`, `oil_sd_gm2`, `oil_n`, `fc_equiv`, `op10_dome_mm`, `op10_bottom_tilt_deg`, `op10_n_valid`, `op10_n_flange`, `op10_depth_mm`, `op10_wall_r15_E_mm`, `op10_wall_angle_E_deg`, `op10_theta_E_deg`, `op10_rise_E_mm`, `op10_seg_E_mm`, `op10_wall_r15_W_mm`, `op10_wall_angle_W_deg`, `op10_theta_W_deg`, `op10_rise_W_mm`, `op10_seg_W_mm`, `op10_wall_r15_S_mm`, `op10_wall_angle_S_deg`, `op10_theta_S_deg`, `op10_rise_S_mm`, `op10_seg_S_mm`, `op10_wall_r15_N_mm`, `op10_wall_angle_N_deg`, `op10_theta_N_deg`, `op10_rise_N_mm`, `op10_seg_N_mm`, `op10_theta_mean_deg`, `op10_theta_range_deg`, `op10_Wx_mm`, `op10_Wy_mm`, `op10_Ld1_mm`, `op10_Ld2_mm`, `op10_drawin_mid_mm`, `op10_drawin_corner_mm`, `op10_ext_E_mm`, `op10_ext_W_mm`, `op10_ext_S_mm`, `op10_ext_N_mm`, `op10_band_rows`, `op10_band_cols`, `op10_wav_sd_mm`, `op10_wav_p99_mm`, `op20_dome_mm`, `op20_bottom_tilt_deg`, `op20_n_valid`, `op20_n_flange`, `op20_depth_mm`, `op20_wall_r15_E_mm`, `op20_wall_angle_E_deg`, `op20_theta_E_deg`, `op20_rise_E_mm`, `op20_seg_E_mm`, `op20_wall_r15_W_mm`, `op20_wall_angle_W_deg`, `op20_theta_W_deg`, `op20_rise_W_mm`, `op20_seg_W_mm`, `op20_wall_r15_S_mm`, `op20_wall_angle_S_deg`, `op20_theta_S_deg`, `op20_rise_S_mm`, `op20_seg_S_mm`, `op20_wall_r15_N_mm`, `op20_wall_angle_N_deg`, `op20_theta_N_deg`, `op20_rise_N_mm`, `op20_seg_N_mm`, `op20_theta_mean_deg`, `op20_theta_range_deg`, `status`, `seconds`
- `features_rddac_sample.csv`: `index`, `experiment_id`, `category`, `geometry`, `bhf_kN`, `oil_type`, `mean_punch_temp_attr`, `F10_kN`, `F20_kN`, `F25_kN`, `W_draw_J`, `F_peak_kN`, `F_rest_kN`, `imbalance20`, `v_form_mm_s`, `punch_temp_C`, `pos_bdc_mm`, `cycle_s`, `sheet_um`, `sheet_sd_um`, `sheet_n`, `oil_gm2`, `oil_sd_gm2`, `oil_n`, `fc_equiv`, `op10_dome_mm`, `op10_bottom_tilt_deg`, `op10_n_valid`, `op10_n_flange`, `op10_depth_mm`, `op10_wall_r15_E_mm`, `op10_wall_angle_E_deg`, `op10_theta_E_deg`, `op10_rise_E_mm`, `op10_seg_E_mm`, `op10_wall_r15_W_mm`, `op10_wall_angle_W_deg`, `op10_theta_W_deg`, `op10_rise_W_mm`, `op10_seg_W_mm`, `op10_wall_r15_S_mm`, `op10_wall_angle_S_deg`, `op10_theta_S_deg`, `op10_rise_S_mm`, `op10_seg_S_mm`, `op10_wall_r15_N_mm`, `op10_wall_angle_N_deg`, `op10_theta_N_deg`, `op10_rise_N_mm`, `op10_seg_N_mm`, `op10_theta_mean_deg`, `op10_theta_range_deg`, `op10_Wx_mm`, `op10_Wy_mm`, `op10_Ld1_mm`, `op10_Ld2_mm`, `op10_drawin_mid_mm`, `op10_drawin_corner_mm`, `op10_ext_E_mm`, `op10_ext_W_mm`, `op10_ext_S_mm`, `op10_ext_N_mm`, `op10_band_rows`, `op10_band_cols`, `op10_wav_sd_mm`, `op10_wav_p99_mm`, `op20_dome_mm`, `op20_bottom_tilt_deg`, `op20_n_valid`, `op20_n_flange`, `op20_depth_mm`, `op20_wall_r15_E_mm`, `op20_wall_angle_E_deg`, `op20_theta_E_deg`, `op20_rise_E_mm`, `op20_seg_E_mm`, `op20_wall_r15_W_mm`, `op20_wall_angle_W_deg`, `op20_theta_W_deg`, `op20_rise_W_mm`, `op20_seg_W_mm`, `op20_wall_r15_S_mm`, `op20_wall_angle_S_deg`, `op20_theta_S_deg`, `op20_rise_S_mm`, `op20_seg_S_mm`, `op20_wall_r15_N_mm`, `op20_wall_angle_N_deg`, `op20_theta_N_deg`, `op20_rise_N_mm`, `op20_seg_N_mm`, `op20_theta_mean_deg`, `op20_theta_range_deg`, `status`
- `inline_drift.csv`: `qc`, `n_batches`, `r2_oof_batch`, `floor`, `floor_drift_removed`, `floor_reduction`
- `inline_lod.csv`: `qc`, `label`, `unit`, `n`, `r2_oof`, `r2_oof_linear`, `sd_within`, `sd_error`, `lod`, `lod_over_sd`, `recall_top5_at_fa5`
- `learn_fewshot.csv`: `k`, `relation`, `method`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `coverage`
- `learn_gp_diagnostics.csv`: `relation_scope`, `method`, `cases`, `median_ls_bhf`, `median_ls_lub`, `median_d_calib_mean`, `share_within_001_of_calib_mean`, `median_d_nn`, `p90_d_nn`, `median_d_m1sn`, `median_half_width`, `fits`, `ls_at_lower_share`, `median_noise_over_bound`, `median_nugget_floors`, `median_se_floors`, `median_gp_sd_floors`
- `learn_intervals.csv`: `calibration`, `relation`, `alternative`, `geometry`, `bhf_kN`, `qc`, `real_q95`, `floor`, `sim_env_hi`, `method`, `lo`, `hi`, `gp_ls_bhf`, `gp_ls_lubrication`, `gp_sf_floors`, `gp_sn_floors`, `gp_se_floors`, `gp_beta_sim`, `mcd_mu_mean`, `mcd_mu_map`, `mcd_mu_edge_mass`, `gp_ls_geometry`, `scope`, `ref_row`, `calib_env_min`, `calib_env_max`, `calib_bhf_min`, `calib_bhf_max`, `calib_geometries`, `gp_noise`, `gp_noise_lb`, `gp_noise_at_bound`, `gp_ls_at_bound`, `rm_quantile_floors`, `rm_n`
- `learn_m7n_priors.csv`: `variant`, `relation`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `coverage`, `median_half_width`, `median_ls_bhf`, `median_d_force_trend`, `max_abs_diff_from_stored`
- `learn_mcd_posterior.csv`: `calibration`, `scope`, `targets`, `mu_map`, `mu_mean`, `mass_at_0.15`, `mass_at_0.05`, `entropy_bits`
- `learn_paired.csv`: `scope`, `rule_a`, `rule_b`, `resolution_diff`, `resolution_diff_lo`, `resolution_diff_hi`, `resolution_share_a_smaller`, `safe_diff`, `safe_diff_lo`, `safe_diff_hi`, `safe_share_a_smaller`
- `learn_resolution.csv`: `scope`, `method`, `qc`, `n_cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`
- `learn_source_floor.csv`: `scope`, `method`, `qc`, `n_cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`, `floor`
- `meas_characteristics.csv`: `qc`, `unit`, `operation`, `region`, `directions`, `resolution_step`, `step_over_floor`, `distinct_per_series`, `zero_se_alternatives`, `known_biases`
- `meas_cut_walls.csv`: `cut_wall_north_minus_east_convex`, `cut_wall_west_minus_east_convex`
- `meas_floor.csv`: `qc`, `unit`, `floor`, `sigma_st`, `sigma_lt`, `sigma_ss`, `sigma_batch`, `lt_over_st`, `white_floor`, `white_share`, `floor_first_half`, `q95_floor_b100`, `q95_halves_max`, `q95_halves_median`, `between_series_q95`, `between_series_median`, `white_floor_floors`, `floor_first_half_floors`, `q95_floor_b100_floors`, `q95_halves_max_floors`, `q95_halves_median_floors`, `between_series_q95_floors`, `between_series_median_floors`
- `meas_run_floors.csv`: `qc`, `floor`, `batch_interval`, `cluster_interval`, `run_floor_min`, `run_floor_median`, `run_floor_max`, `floor_without_warm_up`, `warm_up_ratio`
- `meas_scan.csv`: `alternative`, `geometry`, `sd_wx`, `sd_wy`, `r_wx_wy`, `lag1_wx`, `lag1_wy`, `wy_minus_wx`, `diag_difference`, `sd_E`, `sd_W`, `sd_N`, `r_E_W`, `r_E_N`, `lag1_N`, `N_minus_EW`, `sd_EW_mean`, `sd_EWN_mean`, `noise_bound_EW_mean`
- `meas_sim.csv`: `qc`, `geometry`, `floor`, `xy_sd_floors`, `xy_max_floors`, `xy_share_over_1_floor`, `roughness_sd_floors`, `roughness_max_floors`, `env_hi_minus_smooth_floors_median`, `env_hi_minus_smooth_floors_max`
- `meas_tooling_reference.csv`: `geometry`, `r_wx_cupwidth`, `floor_cup_width_mm`, `floor_wx_mm`, `floor_depth_mm`, `cup_width_mm`, `wx_mm`, `lateral_scale_drift_bound`
- `panel_arm_sign.csv`: `geometry`, `bhf_kN`, `simulations`, `sims_downward`, `parts`, `parts_downward`
- `panel_capability.csv`: `ppk`, `scope`, `method`, `median_d`, `right`, `false_reject`, `trial`, `adequate`
- `panel_decomposition.csv`: `rule_set`, `distance`, `relations`, `rules`, `share_relation`, `share_rule`, `share_interaction`, `best_rule_range`, `new_family_floor`
- `panel_failing_weight.csv`: `delta`, `cases`, `feasible_failing`, `weight_failing`
- `panel_floor_protocol.csv`: `qc`, `geometry`, `floor`, `sigma_lt`, `sigma_st`, `sigma_within_batch`, `sigma_between_batch`, `floor_over_sigma_lt`, `floor_over_sigma_st`, `normal_model_floor`, `series_with_sigma_w_above_sigma_lt`, `max_excess_sigma_w_over_sigma_lt`, `sigma_lt_median_series`, `model_floor_subgroups_of_5`, `subgroup5_over_batch50`
- `panel_force_effect.csv`: `qc`, `geometry`, `real_effect`, `sim_effect`, `ratio`
- `panel_force_levels.csv`: `bhf_kN`, `relation`, `method`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`
- `panel_guard_priors.csv`: `scope`, `method`, `prior`, `guard_band`, `guard_band_uncapped`, `trial_10_uncapped`, `trial_20_uncapped`
- `panel_m0_split.csv`: `variant`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`
- `panel_nominal_offset.csv`: `method`, `cases`, `resolution_floors`, `safe_floors`, `median_abs_error`, `abs_error_p90`
- `panel_physical_units.csv`: `scope`, `method`, `qc`, `pooled_floor`, `resolution_units`, `safe_units`, `resolution_pooled_floors`, `safe_pooled_floors`
- `panel_q95_unit.csv`: `scope`, `method`, `resolution_floors`, `safe_floors`
- `panel_resolution_steps.csv`: `qc`, `median_step`, `step_over_floor`, `distinct_values_total`, `distinct_per_series_median`, `distinct_per_series_min`, `distinct_per_series_max`, `alternatives_with_zero_q95_se`
- `panel_runs.csv`: `alternative`, `start_temp_C`, `rise_first_150_K`, `rise_series_K`, `sheet_median_um`, `oil_median_gm2`, `stroke_speed_mm_s`
- `panel_sibling_strata.csv`: `resolved_siblings`, `method`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `abs_error_p90`
- `panel_source_floor.csv`: `scope`, `method`, `qc`, `n_cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `resolution_lo`, `resolution_hi`, `safe_lo`, `safe_hi`, `floor`
- `panel_source_floor_curve.csv`: `scope`, `method`, `d`, `correct`, `false_accept`, `false_reject`, `abstain`, `error_when_decided`
- `panel_source_floor_paired.csv`: `scope`, `rule_a`, `rule_b`, `resolution_diff`, `resolution_diff_lo`, `resolution_diff_hi`, `resolution_share_a_smaller`, `safe_diff`, `safe_diff_lo`, `safe_diff_hi`, `safe_share_a_smaller`, `floor`
- `panel_step6.csv`: `scope`, `method`, `guard_band`, `decisive_alone`, `safe_alone`, `right_10_alone`, `wrong_10_alone`, `trial_10_alone`, `right_20_alone`, `wrong_20_alone`, `trial_20_alone`, `decisive_step6`, `safe_step6`, `right_10_step6`, `wrong_10_step6`, `trial_10_step6`, `right_20_step6`, `wrong_20_step6`, `trial_20_step6`
- `panel_step6_curves.csv`: `margin`, `correct_when_decided`, `scope`, `method`
- `panel_variogram.csv`: `qc`, `geometry`, `lag_batches`, `pairs`, `q95_floors`
- `qual_between_run.csv`: `tau`, `relation`, `method`, `decisive_median`, `decisive_p05`, `decisive_p95`, `safe_median`, `band_median`, `share_record_rule_best`, `best_rules`
- `qual_between_run_trial.csv`: `tau`, `rule`, `decisive_median`, `decisive_p05`, `decisive_p95`, `safe_median`
- `qual_cost_cheapest.csv`: `prior`, `c_fr`, `relation`, `c_trial`, `cheapest`, `cost`, `runner_up`, `runner_up_cost`, `margin`, `fa_of_cheapest`
- `qual_costs.csv`: `prior`, `relation`, `method`, `c_fr`, `c_trial`, `cost_alone`, `fa_alone`, `fr_alone`, `trial_alone`, `band_95`, `cost_band_95`, `trial_band_95`, `band_opt`, `cost_opt`, `trial_opt`, `fa_opt`, `fr_opt`, `cost_always_trial`
- `qual_coverage.csv`: `relation`, `method`, `level`, `subset`, `cases`, `coverage`, `coverage_lo`, `coverage_hi`, `median_half_width`, `interval_score`, `rm_n`, `rm_quantile_floors`, `ci_note`
- `qual_crossfit.csv`: `relation`, `criterion`, `pool`, `selected_on`, `evaluated_on`, `rule`, `in_sample`, `cross_fitted`, `best_on_evaluation`, `band`, `share_correct`, `trial_rate`
- `qual_decomposition.csv`: `rule_set`, `distance`, `relations`, `rules`, `share_relation`, `share_rule`, `share_interaction`, `best_rule_range`
- `qual_design_level.csv`: `relation`, `method`, `designs`, `design_decisive`, `design_safe`, `marginal_decisive`, `marginal_safe`
- `qual_floor_loao.csv`: `kind`, `relation`, `method`, `alternative`, `ratio_loao_to_full`, `resolution_floors`, `safe_floors`, `resolution_loao`, `safe_loao`
- `qual_guard_characteristic.csv`: `relation`, `method`, `group`, `name`, `pooled_band`, `share_correct`, `trial_rate`, `own_band`, `own_band_correct`, `own_band_trial`
- `qual_guard_decision.csv`: `prior`, `relation`, `method`, `scheme`, `band_concave`, `band_convex`, `share_correct`, `share_correct_lo`, `share_correct_hi`, `trial_rate`, `trial_lo`, `trial_hi`, `decided`, `verdicts`, `false_accept_share`, `alternatives`, `worst_characteristic`, `worst_share_correct`, `share_correct_concave`, `trial_rate_concave`, `decided_concave`, `verdicts_concave`, `share_correct_convex`, `trial_rate_convex`, `decided_convex`, `verdicts_convex`, `share_arm_op20`, `share_depth_op10`, `share_dome_op20`, `share_drawin_corner`, `share_drawin_mid`, `share_wall_op10`, `share_waviness`, `decided_arm_op20`, `decided_depth_op10`, `decided_dome_op20`, `decided_drawin_corner`, `decided_drawin_mid`, `decided_wall_op10`, `decided_waviness`
- `qual_guard_family.csv`: `relation`, `method`, `band_pooled`, `band_concave`, `correct_concave`, `trial_concave`, `correct_concave_with_other_band`, `trial_concave_with_other_band`, `band_convex`, `correct_convex`, `trial_convex`, `correct_convex_with_other_band`, `trial_convex_with_other_band`
- `qual_guard_nested.csv`: `prior`, `method`, `scheme`, `share_correct`, `trial_rate`, `decided`, `verdicts`, `check_max_dev_stored`
- `qual_guard_oos.csv`: `prior`, `relation`, `method`, `scheme`, `median_band`, `share_correct`, `share_correct_lo`, `share_correct_hi`, `trial_rate`, `trial_lo`, `trial_hi`, `in_sample_band`, `in_sample_correct`, `in_sample_trial`
- `qual_guard_prior_width.csv`: `relation`, `method`, `prior_half_width`, `band`, `trial_rate`, `share_correct`, `decided_share`
- `qual_m6_coverage.csv`: `relation`, `method`, `cases`, `coverage`, `coverage_lo`, `coverage_hi`, `interval_score`, `median_half_width`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`
- `qual_per_characteristic.csv`: `relation`, `method`, `subset`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `unit`, `pooled_floor`, `decisive_units`, `safe_units`, `decisive_sigma_lt`, `ppk_at_decisive_median`
- `qual_release_capability.csv`: `relation`, `method`, `decisive_on_centre_plus_4sd`, `true_ppk_min`, `true_ppk_median`, `true_ppk_max`
- `qual_resolvable_difference.csv`: `scope`, `pairs`, `n_pairs`, `median_half_width`, `min_half_width`, `max_half_width`
- `qual_strata.csv`: `stratum`, `method`, `cases`, `alternatives`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `abs_error_p90`, `coverage`
- `qual_strata_cases.csv`: `alternative`, `qc`, `stratum`
- `qual_trial.csv`: `rule`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `abs_error_p90`, `abs_error_median`
- `qual_trial_cost.csv`: `rule`, `prior`, `c_fr`, `false_accept`, `false_reject`, `error_cost`, `failing_share_of_verdicts`
- `qual_variants.csv`: `variant`, `relation`, `method`, `cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`
- `qual_worked_example.csv`: `quantity`, `value`, `note`
- `rob_bhf_pairs.csv`: `qc`, `pair`, `share_resolvable`, `median_esr`, `slope_per_100kN`, `mrc_kN`
- `rob_decisions.csv`: `variant`, `scope`, `method`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`
- `rob_floor.csv`: `variant`, `qc`, `floor`, `floor_concave`, `floor_convex`, `share_bhf`, `share_geometry`, `share_lubrication`, `mrc_bhf_kN`
- `rob_floor_between.csv`: `qc`, `geometry`, `floor_between_series`, `floor`
- `rob_refit.csv`: `scope`, `method`, `resolution_floors`, `resolution_lo`, `resolution_hi`, `safe_floors`, `safe_lo`, `safe_hi`
- `rob_refit_paired.csv`: `scope`, `kind`, `rule_a`, `rule_b`, `diff`, `diff_lo`, `diff_hi`, `share_a_smaller`
- `scen_cost.csv`: `scope`, `method`, `c_trial`, `cost`
- `scen_cost_map.csv`: `scope`, `c_fr`, `c_trial`, `cost`, `cheapest`
- `scen_scores.csv`: `scope`, `method`, `correct`, `false_accept`, `false_reject`, `uncertain`, `n`, `false_accept_given_fails`, `false_reject_given_meets`, `n_failing`
- `scen_scores_by_class.csv`: `scope`, `method`, `qc`, `tol_class`, `correct`, `false_accept`, `false_reject`, `uncertain`
- `scen_strata.csv`: `scope`, `method`, `stratum`, `correct`, `false_accept`, `false_reject`, `uncertain`, `n`, `false_accept_given_fails`, `false_reject_given_meets`, `n_failing`
- `scen_truth.csv`: `qc`, `tol_class`, `row_mm`, `alternative`, `geometry`, `real_q95`, `limit`, `meets`, `margin_floors`, `worst_side_q95`, `worst_side_meets`
- `sens_drift.csv`: `qc`, `floor`, `scatter_floor`, `scatter_floor_lo`, `scatter_floor_hi`, `drift_inflation`
- `sens_esr.csv`: `batch`, `alpha`, `stat`, `reference`, `qc`, `family`, `share_resolvable`
- `sens_floor.csv`: `batch`, `alpha`, `stat`, `reference`, `qc`, `floor`, `floor_concave`, `floor_convex`, `mrc_bhf_kN`
- `sim_depth_offset.csv`: `geometry`, `bhf_kN`, `depth_measured`, `depth_sim`, `depth_sim_minus_measured`, `flange_angle_measured_deg`, `flange_angle_sim_deg`, `flange_rise_measured`, `flange_rise_sim`, `rise_difference`, `wall_r15_measured`, `wall_r15_sim`, `wall_r15_measured_minus_sim`, `press_bdc_median_mm`, `press_bdc_sd_mm`
- `sim_envelope_ranges.csv`: `alternative`, `env_thickness`, `env_friction`
- `sim_envelope_variant.csv`: `envelope`, `scope`, `method`, `resolution_floors`, `safe_floors`, `median_width_floors`
- `sim_grid_comparisons.csv`: `comparison`, `qc`, `geometry`, `measured`, `combinations`, `sim_min`, `sim_max`, `sim_nominal`, `ratio_min`, `ratio_max`, `share_within_0.5_of_measured`
- `sim_mc_friction.csv`: `scope`, `target`, `lubrication`, `mu`, `at_upper_edge`, `at_lower_edge`
- `sim_oil_mapping.csv`: `geometry`, `bhf_kN`, `qc`, `sim_mm_per_mu`, `implied_mm_per_gm2`, `within_run_mm_per_gm2`, `between_patterns_min`, `between_patterns_max`, `between_patterns_median`, `oil_traverse_sd_median`, `oil_between_parts_sd`
- `sim_validation.csv`: `qc`, `unit`, `geometry`, `bhf_kN`, `measured_centre`, `measured_min_series`, `measured_max_series`, `sim_nominal`, `sim_minus_measured`, `sim_minus_measured_floors`, `sim_min_over_friction`, `sim_max_over_friction`, `measured_inside_friction_range`, `closest_mu`, `sim_at_closest_mu`, `residual_at_closest_floors`, `sim_xy_sd_floors`, `sim_roughness_sd_floors`
- `tune_decisions.csv`: `scope`, `qc`, `n_cases`, `resolution_floors`, `safe_floors`, `resolution_adequate`, `safe_adequate`, `resolution_failing`, `safe_failing`, `rule`, `setting`
- `tune_intervals.csv`: `scope`, `relation`, `rule`, `setting`, `method`, `qc`, `alternative`, `geometry`, `lo`, `hi`, `real_q95`, `floor`, `inner_mae`, `chosen`
- `dec_verdicts.csv.gz`: `calibration`, `relation`, `alternative`, `geometry`, `qc`, `method`, `d`, `R`, `verdict`, `adequate`
- `learn_fewshot_intervals.csv.gz`: `target_family`, `k`, `produced`, `alternative`, `relation`, `qc`, `method`, `lo`, `hi`, `real_q95`, `floor`
