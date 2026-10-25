# Findings

Design-stage manufacturability decisions qualified with production evidence. Deep drawing and cutting of
DP600 cups: 18 design–process alternatives (2 geometries × 3 blank-holder forces × 3 lubrication patterns),
500 consecutive parts each (RDDAC), against the matching finite-element simulations (DDACS).

This file holds the current numbers only: a map of the paper to the scripts and result
files, the headline findings of the current version and the computation details. The findings of earlier versions,
superseded where they differ, are in `findings_history.md`; `DATA_DICTIONARY.md` explains the columns, scopes and
code names of every result file and the floor each one uses. Every number comes from a CSV written by
`bash scripts/run_all.sh` (about five hours on 4 cores from the cached feature tables). Distances are in within-run
floors of each characteristic unless stated. M3n is named M4 in the code.

## Map of the paper (33 pages, a single document)

| Paper | Results | Script: result files |
|---|---|---|
| Table 3; Sections 3.4, 4.1, 4.3 | characteristics, scan redundancy and biases, resolution, failing-side weight, run metadata | `simcheck.py`: meas_characteristics, meas_cut_walls; `measurement.py`: meas_scan; `panel.py`: panel_resolution_steps, panel_failing_weight, panel_runs |
| Section 3.7 | worked example: six-series floor, quantisation, resolvable force change from two levels, the convex family's band widened by the trial cost, margins and truth | `qualify.py`: qual_worked_example |
| Section 4.2 | extraction noise of the simulated characteristics | `measurement.py`: meas_sim |
| Table 4; Section 5.1; Fig. 4 | floors, interval over alternatives, single-run floors, warm-up, σb, σw, F/σLT, time order and lag profile, tooling reference, process signals | `alternatives.py`: alt_floor; `simcheck.py`: meas_run_floors, meas_tooling_reference; `panel.py`: panel_floor_protocol, panel_variogram; `sensitivity.py`: sens_drift; `measurement.py`: meas_floor; `inline.py`: inline_drift |
| Section 5.2 | resolvable contrasts, comparisons independent of blank and scales over the whole grid (force effect, arm sign, dome), levels, friction fits, oil mapping, depth offset, envelope over measured inputs, surrogate | `alternatives.py`: alt_effects, alt_mrc; `simcheck.py`: sim_grid_comparisons, sim_validation, sim_mc_friction, sim_oil_mapping, sim_depth_offset, sim_envelope_variant; `learners.py`: learn_mcd_posterior; `panel.py`: panel_force_effect, panel_arm_sign, panel_m0_split; `design_space.py`: ds_surrogate_rule |
| Table 5; Section 5.3; Fig. 5 | distances and their intervals, FA/FR sides, trial rows, decision-time strata, one sibling; a new family in the produced family's floor | `decisions.py`: dec_resolution, dec_intervals, dec_paired; `learners.py`: learn_resolution, learn_intervals, learn_source_floor, learn_paired; `panel.py`: panel_source_floor; `qualify.py`: qual_trial, qual_strata; `budget.py`: budget_design |
| Table 6 | decisive distance per characteristic, in the unit, performance index | `qualify.py`: qual_per_characteristic |
| Section 5.4 | GP diagnostics, prior sensitivity of M7n, predictors crossed with the relation-matched interval, trend GP on both families, coverage and interval score, tuning study, few-shot transfer | `learners.py`: learn_gp_diagnostics, learn_m7n_priors, learn_resolution, learn_fewshot; `decisions.py`: dec_gp; `qualify.py`: qual_coverage, qual_m6_coverage; `tuning.py`: tune_decisions |
| Table 7; Section 5.5 | guard bands available when deciding (a family's own sibling cases; for a new setting the other family's band), shares per family, force cell left out, strictly nested sibling validation, per characteristic, under a between-run component | `qualify.py`: qual_guard_decision, qual_guard_oos, qual_guard_nested, qual_between_run |
| Section 5.6; Fig. 6 | costs (bands under step 5's rule, in sample, pooled over the families), cheapest option per cost setting, trial as a rule and the cost of its errors, limits at performance indices, release as a capability decision, the trial under between-run variation | `qualify.py`: qual_costs, qual_cost_cheapest, qual_trial, qual_trial_cost, qual_release_capability, qual_between_run_trial; `panel.py`: panel_capability |
| Section 5.7 | between-run sensitivity, cross-fitting (decisiveness, safety, step 6), resolvable difference, design level, variants, floors without the held-out series, robustness | `qualify.py`: qual_between_run, qual_crossfit, qual_resolvable_difference, qual_design_level, qual_variants, qual_floor_loao; `robustness.py`: rob_decisions, rob_refit; `panel.py`: panel_floor_protocol |
| Section 6.2 | 100 verdicts with the band available when deciding | `qualify.py`: qual_guard_decision |
| Section 6.4 | scoring function; PA12 attempt | `opchar.py` (self-checks against dec_resolution and qual_guard_decision); `case2_pa12.py`: case2_floor |
| Fig. 1, Fig. 3 | schematic (M7n, extrapolated setting); scanned parts | `figs.py` from dec_intervals and learn_intervals; from the RDDAC sample scans |

## Headline findings of the current version

- **Floor** (alt_floor, sens_drift, meas_floor): two batches of 50 consecutive parts differ by up to 0.051 mm in
  mid-side draw-in and 0.078° in wall angle in 95 % of pairs, 0.7–1.7 long-term standard deviations. Drift within the
  run sets it (2.1–4.5 times larger than without the time order); independent part-to-part noise is 15–33 % of it.
  A common lateral scale drift of the scanner is below 0.05 % (about 0.9 floor of mid-side draw-in).
- **Simulation dataset** (sim_grid_comparisons, sim_validation, panel_arm_sign, sim_mc_friction): it does not
  contain the produced process. Independent of blank and scales, at every friction and thickness of the grid: the
  simulated force effect on the mid-side draw-in is 2.8–7.4 times the measured one; the concave cut arms bend
  downwards in 89–100 % of the simulations, upwards in every part; the dome ranks the geometries in reverse in 76 % of
  the 198 simulated combinations. The concave wall-angle trend (−1.5° from 100 to 500 kN) holds only at the nominal
  friction (−1.9 to +1.7° over the grid) and is no longer used. The level comparisons (11 of 42 cells inside the friction range; draw-in gaps; Mc censored
  at 0.15) hold only if the assumed 210 mm blank and the scanner's scales hold.
- **Sibling** (dec_resolution, qual_strata): the nearest setting decides at 3.4 floors (2.0–4.5), 1.60 when
  the produced siblings do not differ resolvably and 4.40 when they do; M5 and M7n at 6.8–7.2, safe below one floor.
- **New setting**: the force trend and the nearest setting at 8.2 and 8.5 floors (4.7 interpolating, 9.5
  extrapolating); interval rules at 15–19, safe at 5–8; M1s and M7 falsely accept up to 165 and 118 floors on the cup
  depth.
- **New family** (panel_source_floor, learn_source_floor; produced family's floor): Mcd 30 and M5 35 floors; M3 safe
  at 17, M2 at 26; rules without the simulation 130–135.
- **Learners** (learn_gp_diagnostics, learn_m7n_priors, learn_resolution, qual_coverage): M7n reduces to the force
  trend; its intervals cover 52/56 % for a new setting; halving or doubling its priors moves its distances by at most
  1.4 floors. NN+RM, borrowing the other family's errors, is safe below one floor for a new setting at 19.5 floors;
  M7n on both families is safe at 2.75; NN+RM's 88/93 % coverage for a new setting comes from two family swaps (76–100 %
  by family, 67–100 % by characteristic); no guarantee applies. The largest-residual and jackknife+ levels are
  guaranteed only with a sibling.
- **Guard bands available when deciding** (qual_guard_decision, qual_guard_oos, qual_guard_nested,
  qual_between_run): reference prior, nearest setting 0/0.5, 2.5/1.5 and 5.75/9.5 floors (concave/convex), 95 %
  correct pooled over the two families (92–100 % per family: 97/93 interpolating, 92/100 extrapolating), 2, 18 and
  58 % trials; release-like prior 41, 67 and 92 % trials and 75 % correct extrapolating (6 of 8 decided verdicts).
  With the band from both families' cases except the held-out force cell, NN 0.72 and NN+RM 0.73 extrapolating;
  interpolating only the other family's cell remains (M5 0.88, M7n 0.87, as in Table 7). Strictly nested sibling
  validation: NN 96 and 95 % correct, 3 and 52 % trials (reference and release-like). With τ = 3 floors the pooled
  bands grow to 2.9, 4.0 and 8.9. No rule qualifies for a new family.
- **Costs and release** (qual_costs, qual_cost_cheapest, qual_trial_cost, qual_release_capability,
  qual_between_run_trial): cost bands follow step 5 (from the 95 % band up to 20 floors), in sample and pooled; for
  a new setting the nearest setting or the force trend is cheapest at every trial cost under both priors and every
  cost ratio, with a sibling the nearest setting from a trial cost of a tenth of a false accept (below that the
  cheapest rules differ by at most 0.003), and for a new family no rule qualifies, so every design goes to trial. The 20-part trial's own errors cost
  0.017 of a false accept per verdict (0.037 release-like). A limit at Ppk 1.33 lies 1.75 floors above the 95th
  percentile; scored on m̄ + 4σ, the nearest setting confirms Ppk ≥ 1.33 only for true indices of 2.1–3.3 with a
  sibling and 3.8–7.4 extrapolating. Within a run the 20- and 50-part trials decide at 1.35 and 0.90 floors; once
  runs differ by a floor (τ = 1, 2, 3) the 20-part trial needs 2.1, 3.6 and 5.1, so near release level the evidence
  must come from replicated runs.
- **Selection** (qual_crossfit): selected for safety on one geometry, a rule is safe on the other only at up to 18
  floors interpolating and 11 extrapolating; rule and band selected together keep 0.92–0.97 correct within a family
  (below 0.95 in four of six cases) and 0.73 for a new family.

**Computation details.** Batches need at least 80 % valid values. M5 and M5n are Gaussian-process regressions
(constant times anisotropic squared-exponential kernel plus white noise, normalised targets, hyperparameters by
maximum marginal likelihood without hyperpriors, three restarts, length scales in [0.1, 100]) on a geometry
indicator, the force in 100 kN and the lubrication rank; the lower bound of the noise variance is the larger of the
mean sampling variance of the calibration alternatives' q_p and the pooled variance between their series of one
geometry and force. M7n and M7 work in pooled floors: the mean basis is an intercept, the force (or, for M7, the
nominal simulation) and the lubrication rank, plus the geometry indicator when both families calibrate; the
coefficients have a flat prior and are integrated out (restricted likelihood); the hyperparameters are maximum a
posteriori under log-normal priors with medians of 200 kN and one pattern step for the length scales, two floors for
the GP and one floor for the nugget standard deviation, and log-scale standard deviations of 1, 1.5 and 1; the
predictive variance adds the nugget and the mean sampling variance of the calibration q_p. Mcd has a uniform prior
over the 11 friction values of the grid, a GP discrepancy with a constant mean and the same priors, a posterior from
the two draw-ins, and a 90 % interval from the posterior mixture. NN takes the mean q_p at the nearest force of the
family, both neighbours when equally near; M1sn fits q_p = a + b·force by least squares. Mc calibrates, per
lubrication pattern, the friction coefficient whose simulated draw-ins are closest to the calibration centres,
without a discrepancy. M3 and M3n use histogram gradient boosting (depth 3, 200 iterations, rate 0.08) on geometry,
force, lubrication, sheet thickness and oil film, with 500 incoming conditions drawn from calibration parts of the
same pattern, and jackknife+ intervals. Guard bands lie on a grid of 0.25 floors. Software: Python 3.11 with NumPy,
pandas, SciPy, scikit-learn and Matplotlib (versions in `requirements.txt`).

## Earlier versions

The findings of earlier versions (Sections S, Q, P and R and the first version, Sections 0–10) are kept for the
record in `findings_history.md`; where they differ from the numbers above, they are superseded.
