# Findings

Design-stage manufacturability decisions qualified with production evidence. Deep drawing and cutting of
DP600 cups: 18 design–process alternatives (2 geometries × 3 blank-holder forces × 3 lubrication patterns),
500 consecutive parts each (RDDAC), against the matching finite-element simulations (DDACS).

Every number below comes from the CSV named in brackets, written by `bash scripts/run_all.sh` (about four hours on
4 cores from the cached feature tables). Distances and floors are in the units of each quality
characteristic unless stated; "floors" means multiples of that characteristic's production floor.

## Q Findings of the second review round (supersede Section P where they differ)

The second round of the simulated panel (`paper/review/cfp_panel/round2/`, AI agents) led to one new rule, the
force trend M1sn (14 rules in all, M6 a robustness variant), to scoring a new family in the produced family's floor,
and to the guard band's prior being stated and varied. The manuscript (`paper/main.tex`) reports these numbers.

**Q1 The force trend M1sn, the counterpart of M1s without the simulation** [dec_resolution.csv, dec_paired.csv,
rob_refit_paired.csv, panel_sibling_strata.csv, panel_force_levels.csv, panel_decomposition.csv]: decisive distance
3.5 floors with a sibling, 8.2 for a new setting (4.7 interpolated, 8.9 extrapolated), 131 for a new family.
M1s − M1sn = +1.35 (+0.65 to +2.95) with a sibling and +11.0 (+5.3 to +13.8) for a new setting with the fits fixed,
+1.35 (+1.35 to +3.6) and +11.0 (+8.8 to +12.05) with refitting; M1s is never the more decisive. With two resolvable
siblings: M1sn 4.45, M1s 4.6, NN 4.85 floors. By force: M1sn 8.85 at 100 and at 500 kN; NN 11.0 and 4.85. Within a
family the rule explains 71 % and the relation 15 % with M1sn (68 and 15 % without). The simulation, offset or
rescaled, adds no information within a family.

**Q2 A new family in the produced family's floor** [panel_source_floor.csv, panel_source_floor_paired.csv]: M1 33,
M2 41/26 (decisive 39–42, safe 9.8–32), M3 40/17 (36–45, 15–19), M5 35/31 (31–39, 28–32), Mc 43 floors; in the new
family's own floor M2 51/16, M3 49/21, M5 38/28. The best rule is safe at 16–17 floors in either floor, but the
safest is not resolved: M3 − M2 safe = −9.3 (−16.1 to +6.9) in the produced family's floor, M3 smaller in 83 % of
resamples; +4.7 (−3.4 to +8.0) in the new family's, 25 %. Decomposition over all relations in the produced
family's floor: relation 67 %, rule 6 % (69 and 6 % in the new family's own floor) [panel_decomposition.csv].

**Q3 Guard bands and their prior** [panel_guard_priors.csv, panel_step6.csv]: the reference prior weights the 47
grid distances within ±20 floors equally (87 % of the weight within ±10). Under it the nearest setting needs 0.25
floors with a sibling, 2.0 interpolating and 7.0 extrapolating; M2 and M5 need 0.75 and 0.5 interpolating but send
31 and 40 % to trial at 10 floors; M2 and M5 never qualify extrapolating, and no rule qualifies for a new family
(cap 20 floors). Grid within ±5: nearest setting 2.0, 4.25 and 14.25. Uniform within ±20: 0, 0.25 and 3.5, with M2
and M5 extrapolating at 6.0 and 5.0. Uniform within ±50: new family M2 6.25, M3 6.5, M5 15. Uncapped under the
reference prior: M2 and M5 extrapolating 23.25 and 23.0; new family M2 41.75, M3 42.25, M5 42.25.

**Q4 Capability-anchored requirements are a one-sided test** [panel_capability.csv]: at Ppk 1.33 the shares of
right verdicts, false rejects and trials are 91/9/0 (nearest setting) and 44/2/53 % (M5) with a sibling, 65/35/0
and 32/16/52 % for a new setting, and 81/19/0 and 79/21/0 % for M1s; for a new family no rule is right in more than
54 % (M1).

**Q5 Table 3 with consistent aggregates** [panel_floor_protocol.csv]: σLT, σb and σw pooled over the series as root
mean squares; one floor is 0.7–1.7 σLT; σw < σLT in every row; series by series σw > σLT in 5 of 126 cases, by at
most 0.3 %. Subgroups of five parts give floors 1.1–2.1 times the reference (median 1.3).

**Q6 Coverage by relation** [dec_coverage.csv; new family computed in make_tables.py]: with a sibling 85–96 %;
interpolated M2n and M5n 93 %, M2 and M5 71 %, M3 43 %, M3n 36 %; extrapolated 33–48 %; new family M2 47 %, M3 40 %,
M2n and M5 12 %, M3n 7 %, M5n 0 %.

**Q7 Other corrections**: short calibration series move no distance within a family by more than 1.5 floors and
for a new family by at most 4.0 [rob_decisions.csv]; the surrogate scored as a rule decides at 108.65 against
108.35 floors as M0 and 15.05 against 15.20 as M1 with a sibling [ds_surrogate_rule.csv]; distances in units are
exact up to 0.05 pooled floors [panel_physical_units.csv].

## P Findings of the revision for the review panel (supersede Section R where they differ)

The simulated review panel (`paper/review/cfp_panel/`, AI agents) led to three changes of the rules and to new
analyses. The GP noise floor is now the variance between the series of one geometry and force. M3 and M3n (M4 in
the code) use jackknife+ intervals. A scaled simulation rule M1s is added (13 rules in all). The manuscript
(`paper/main.tex`, a single file with its appendix) reports these numbers.

**P1 Distances by relation** (decisive/safe, floors; one number for rules that always decide) [dec_resolution.csv]:

| Rule | New variant | New setting | Interpolated | Extrapolated | New family |
|---|---|---|---|---|---|
| NN nearest produced setting | 3.4 (2.0–4.5) | 8.5 (5.5–10.2) | 4.7 | 9.5 | 131 |
| M1s scaled simulation | 4.9 | 19 (false accepts up to 164) | 19 | 19 | 122 |
| M5 GP correction of the envelope | 7.2/0.75 | 19/6.8 | 19/2.8 | 19/8.9 | 38/28 |
| M5n GP without simulation | 7.2/0.55 | 17/6.1 | 16/0 | 18/8.6 | 132/130 |
| M2 envelope + residual margin | 23/0.15 | 18/8.1 | 18/2.7 | 18/9.9 | 51/16 |
| M1 bias-corrected simulation | 15 | 24 | | | 35 |
| M0 nominal simulation | 108 (101–115) | 108 | | | 108 |

**P2 Where the distances come from** [panel_decomposition.csv, panel_sibling_strata.csv, panel_force_levels.csv]:
over the eleven calibrated rules the relation explains 69 % of the variation of the log decisive distance and the
rule 6 %; within a family the rule explains 68 % and the relation 15 %. New variant with neither sibling resolvable
(58 cases): NN 0.85 floors; both resolvable (34): NN 4.9, M5 9.7. Held-out force 100 kN (slower stroke): NN 11 floors;
500 kN: 4.9; 300 kN (interpolated): 4.7. Pooling the other family: M5 7.2 → 11, M2 23 → 53, M2n 19 → 325 floors;
M5 coverage 86 → 90 %, M5 centre 2.9 floors [dec_resolution.csv, dec_coverage.csv].

**P3 What the simulation and learning add** [dec_paired.csv, dec_coverage.csv, dec_gp.csv, panel_force_effect.csv]:
M5 − M5n = 0.0 (−0.4 to +1.1), M2 − M2n = +3.9, M1 − M1n = +6.2 within the family; M1s − M1n = −4.2 (−5.4 to −0.5)
within the family but +8.9 for a new setting; M5 − M5n = −94 for a new family. The simulated force effect on the
draw-ins is 2.7–5.1 times the measured one. Interval centres decide at 3.3 (M5), 3.1 (M5n) and 3.7 floors (M3n)
within the family; coverage within the family 85–86 % (GPs), 89 % (M2), 96 % (M3, jackknife+); 43–55 % for a new
setting; at most 12 % (GPs) for a new family. In the median new-setting GP fit the force length scale sits at its
lower bound (10 kN).

**P4 New family** [panel_source_floor.csv, panel_nominal_offset.csv, panel_m0_split.csv]: in the floor of the
produced family M5 decides at 35 and is safe at 31 floors, M2 at 41 and 26. For the wall angle, the design angle
plus the produced family's deviation decides at 2.0 floors (M5 7.3, M1 16). Removing the cup-depth reference
offset brings M0 from 108 to 65 floors.

**P5 The procedure's decision rule** [panel_step6.csv, panel_step6_curves.csv]: guard bands 0 (interval rules) and
0.25 floors (NN) within the family; 2.0 floors for NN on an interpolated setting (decisive 6.7, safe 2.7, no
trial at 10 floors); 7.0 floors on an extrapolated one (decisive 17, 26 % trial at 10 floors); none up to 20
floors for a new family (every design to trial). The share of correct decided verdicts of NN for a new setting
grows from 85 % at any margin to 95 % beyond 5 floors; M5 for a new family is right in 71–74 % at every margin.

**P6 Requirements anchored in capability** [panel_capability.csv]: limits at Ppk 1.0, 1.33, 1.67 and 2.0 lie a
median 1.0, 1.7, 2.5 and 3.1 floors above q95. At Ppk 1.33, NN says meets in 91 % of the new-variant cases (M5
44 %), 65 % for a new setting (M5 32 %); no rule exceeds 54 % for a new family.

**P7 Floor protocol and measurement** [panel_floor_protocol.csv, panel_variogram.csv, panel_resolution_steps.csv,
inline_drift.csv, meas_floor.csv]: one floor is 0.66–2.2 long-term standard deviations of the parts; the normal
model reproduces the floors to within 12 %; batches one position apart differ by 0.51–0.80 floors, nine apart by
1.1–1.5. Mid-side draw-in quantised in steps of 0.38 floors. Process signals predict the batch drift out of fold
with R² of −0.23 to 0.20; removing it changes the floors by −16 to +12 %.

**P8 Cost** [scen_cost_map.csv]: with c_FR = c_FA/2, NN (or M1s) is cheapest for a new variant at any trial cost;
the production-only interval rules for a new setting while a trial costs at most a tenth of a false accept, NN
beyond; for a new family a trial of every design up to a tenth, M2 at a fifth, M5 beyond.

**P9 Calibration budget by relation** [budget_design.csv]: one produced sibling lets M1, M2 and NN decide at
3.5 floors (2.25–4.6) with no wrong verdict at 10 floors (they coincide by construction). More alternatives leave
NN at 3.35–3.5, make M1 worse (12–18 floors) and M2 safer but less decisive (safe 2.15 → 0.15, decisive 14.5 → 23),
and make the GPs safer and more decisive (M5 decisive 14.3 at k = 2 → 7.15 at k = 8, M5n 11.8 → 7.15). Without a
sibling, bracketing the new force: M2, M5 and M5n safe at 0–4.75 floors with no wrong verdict at 10 floors from
k = 2, but decisive only at 15–25 floors (NN 4.65–6.0). Extrapolation: no rule safe closer than 8.55 floors at any
budget. Subsets with a sibling: 46 % (k = 2) to 96 % (k = 6). M1's odd–even pattern: its median offset averages
two forces only for an even k.

**P10 Robustness** [rob_decisions.csv, rob_floor_between.csv, rob_refit.csv, rob_refit_paired.csv,
panel_q95_unit.csv]: temperature adjustment changes no calibrated distance by more than 2.55 floors; dropping
the first 150 parts shrinks the floors and lengthens the distances (NN 4.1 within, 11.55 for a new setting);
floors between series are 1.45–9.08 times the reference and shorten them (NN 0.75 and 2.7); batches of 25/100
rescale the distances by 0.80–0.96/0.97–1.21, floor quantiles of 0.90/0.99 by 1.17–1.42/0.60–0.76; the GP
variants move them by at most 1.2 (decisive) and 2.1 floors (safe); calibration series of 50/100/250 parts move
no within-family distance by more than 1.15/0.95/0.65 floors (new family 4.0/2.65/0.95). In the unit of the
reproducibility of q95, NN decides at 2.75 (within) and 6.85 floors (new setting). In every variant that includes
it, NN is the most decisive rule within a family and M2 the safest for a new family. M6 (conformalised GP):
17.35/0.05 within, 56.15/6.15 for a new setting, 40.7/24.7 for a new family. Relation-preserving refit bootstrap
(200 resamples of the lubrication patterns): within the family NN 2.25–4.6, M5 4.04–11.21, M5n 4.3–8.8 floors;
NN − M5 = −3.8 (−7.45 to −1.79) and NN − M5n = −3.8 (−5.0 to −2.05), NN smaller in all resamples; for a new
setting NN − M5 = −10.2 (−12.1 to −9.1).

**P11 Part-level learners** [tune_decisions.csv]: with jackknife+ intervals, M3n (M4 in the code) decides at
11.2–12.7 floors within the family under every learner and setting, M3 at 19.9–32.3; for a new setting M3n at
13.1–16.2, M3 at 26.8–36.8. The ranking of the two does not depend on the learner.

## R Revised findings (supersede the first-version headline and Sections 1–10 below)

The revision reorganised the evaluation by the relation of a new design to the produced evidence (grouped
cross-validation), added every calibrated rule without the simulation and a nearest-produced-setting baseline,
replaced the grid by the exact estimator of the distances, redefined two characteristics after the scan
redundancy analysis, and made the floors per geometry. Where the numbers below differ from Sections 1–10, these
hold; the manuscript (`paper/main.tex`) reports them.

**R1 The floor is set by drift.** Floors of 0.051 mm (mid-side draw-in), 0.046 mm (corner draw-in),
0.0028 mm (waviness), 0.078° (wall angle), 0.11° (arm angle), 0.011 mm (cup depth) and 0.0070 mm (dome); the
time order of the parts inflates them by 2.1–4.5 [alt_floor.csv, sens_drift.csv]. Independent part-to-part
noise, the scanner's repeatability included, would produce 15–33 % of each floor; the 95th percentiles of two
batches of 100 parts differ by 0.92–1.49 floors; the three lubrication series of one geometry and force differ
by 1.2–9.8 floors at 95 %, an upper bound of run-to-run variation [meas_floor.csv].

**R2 What production resolves.** All 63 geometry contrasts, 105 of 126 blank-holder force contrasts and 51 of
126 lubrication contrasts exceed the floor; the local minimum resolvable force change is 21–67 kN between 100
and 300 kN and 43–105 kN between 300 and 500 kN for the depth, draw-ins and waviness [alt_effects.csv,
rob_bhf_pairs.csv].

**R3 The nominal simulation** decides correctly only beyond 108 floors (101–115) and errs mostly by false
rejects (safe distance 17 floors for false accepts, 109 for false rejects); its force effect on the draw-in is
2.6–5.1 times the measured one [dec_resolution.csv]. The process-window worst case (M0w) is neither safe nor
decisive (94/119 floors).

**R4 The relation of the new design to the produced evidence governs decision fitness** (decisive/safe
distance in floors) [dec_resolution.csv]:

| Rule | New variant (sibling produced) | New setting | Interpolation | Extrapolation | New family |
|---|---|---|---|---|---|
| NN nearest produced setting | 3.4 | 8.5 | 4.7 | 9.5 | 131 |
| M1 bias-corrected simulation | 15 | 24 | 11 | 25 | 35 |
| M2 envelope + residual margin | 23/0.2 | 18/8.1 | 18/2.7 | 18/9.9 | 51/16 |
| M5 GP correction of the envelope | 6.7/1.4 | 18/7.4 | 19/2.9 | 18/8.9 | 38/30 |
| M5n GP of q95 without simulation | 6.1/1.0 | 18/5.4 | 16/1.3 | 18/8.5 | 131/131 |

**R5 What the simulation and learning add.** Within a family nothing: M5 − M5n = +0.6 floors (0.0 to +1.6),
M2 − M2n = +3.9 (+0.4 to +7.4), M1 − M1n = +6.2 (+4.6 to +9.7); for a new setting the bias correction loses
13.5 floors with the simulation; only for a new family is the simulation decisive (M5 − M5n = −93.3)
[dec_paired.csv]. Learned models match the nearest produced setting when used as point rules (interval centres
of M5, M5n, M4 at 3.4, 2.8, 4.8 floors within the family) and add calibrated abstention: M2 covers 8/9 within
the family, M3 93 %, the GP intervals 71–72 %; for a new setting every calibrated interval covers 39–56 %, for a
new family the GPs cover none [dec_coverage.csv, dec_gp.csv].

**R6 Calibration budget by relation** [budget_design.csv]: one produced sibling lets M1, M2 and NN decide at
3.5 floors (2.3–4.6) with no wrong verdict at 10 floors; bracketing a new force without a sibling makes M2, M5
and M5n safe at 0.5–4.8 floors but decisive only at 15–25 (NN 4.7–6.0); extrapolation is never safe closer
than 8.5 floors. The share of subsets with a sibling grows from 46 % (two alternatives) to 96 % (six).

**R7 Guards** [dec_guard.csv]: for a new setting the range guard refuses the 84 extrapolated cases and M2, M5
and NN are never wrong among the 80 verdicts it lets through; the novelty guard refuses 84 other cases, of
whose verdicts 72–96 % would have been correct. For a new family the novelty guard lets 12 cases through, and
M5 is wrong in 6 of their 24 verdicts (25 %), M2 in none (12 to trial).

**R8 Requirements from ISO 2768-1 angular classes** (108 decisions, 69 failing, 32 within 5 floors)
[scen_scores.csv, scen_strata.csv, scen_cost.csv]: new variant NN 100 % right, M5 93 % (75 % within 5 floors);
new setting NN 97 %, M5n 92 %; new family M5 68 % right, rejecting 46 % of the adequate and accepting 9 % of
the failing alternatives. Cheapest rule with c_FR = c_FA/2: NN within a family; M2n, M4 and M5n (tied) for a
new setting up to c_T = 0.1 c_FA and NN from 0.2; M2 for a new family up to 0.1 and M5 from 0.2.

**R9 Robustness** [rob_decisions.csv, rob_refit.csv, tune_decisions.csv]: in every variant that includes it,
NN stays the most decisive rule for a new variant and a new setting and M2 the safest for a new family; the
rules without the simulation fail for a new family (≥ 91 floors). Temperature adjustment changes the pooled
floors by −14 to +4 % and the calibrated distances by at most 2.6 floors; batch sizes of 25/100 rescale the
distances by 0.80–0.96/0.97–1.16, floor quantiles of 0.90/0.99 by 1.16–1.46/0.54–0.83; the GP variants keep
M5 at 6.4–6.9 floors for a new variant; refitting widens M5's decisive distance to 5.0–18.6 floors within the
family (NN 2.2–7.0).

**R10 Not used in the paper.** The DDACS design-corner sensitivities (Section 6), the in-line verifiability
(Section 7) and the exploratory PA12 case (Section 10.6, `scripts/case2_pa12.py`) remain in the repository but
are not part of the revised manuscript.

## Headline of the first version (superseded by Section R)

1. **Production resolves geometry and, mostly, blank-holder force, but rarely the lubrication pattern.** All
   63 geometry contrasts, 106 of 126 blank-holder force contrasts and 53 of 126 lubrication contrasts exceed
   the production floor [alt_effects.csv].
2. **The nominal simulation is not decision-grade.** Its median offset from production reaches 108 floors
   (16 floors or more for six of seven characteristics on the concave cup) and varies by 10.5 to 38 floors
   between alternatives of one geometry; it needs requirements 150 floors from the truth before 95 % of its
   verdicts are right [dec_alternatives.csv, dec_resolution.csv].
3. **Calibrated on the other alternatives of the family, a Gaussian-process discrepancy model (M5) decides
   correctly beyond 7 floors (bootstrap 95 % CI 6.5–8) and errs in at most 5 % of verdicts beyond 2 floors
   (0.5–4.5).** The conformal envelope (M2) is safer (0.5 floors) but needs 25 floors to decide; learning the
   characteristic from production data alone (M4) needs 12; the intervals of M5, M4, M1 and M2 do not overlap
   [dec_resolution.csv].
4. **Across geometries no rule is safe closer than 20 floors, and machine learning without the simulation
   fails outright** (150 floors). The simulation is what carries a decision into a new geometry, but its
   calibration does not transfer reliably [dec_resolution.csv].
5. **Production evidence buys safety first, and which variants are produced matters.** With 4 to 5 produced
   alternatives of the family the calibrated rules err in under 1 % of verdicts at 10 floors; more alternatives
   make M5 more decisive (20 to 7 floors) but M2 less so (12 to 25) [budget_resolution.csv]. Calibration sets
   whose blank-holder forces bracket the new design make M2 error-free and M5 nearly so at 10 floors from two
   alternatives on; extrapolating sets err in 4.6–7.9 % [budget_design.csv].
6. **The press-force record cannot stand in for the scan.** It explains at most 17 % of the part-to-part and
   11 % of the batch-to-batch variation of any characteristic [inline_lod.csv, inline_drift.csv].
7. **Against general tolerances (ISO 2768) the best rule decides 89 % of 162 design questions correctly, with no
   false accept** (within the family); the nominal simulation is right in 66 % and accepts 19 % that fail
   [scen_scores.csv].
8. **An applicability guard makes the transfer safe by sending it to trial.** For 90.5 % of the cases on a new
   geometry the simulated q95 lies outside the calibration range; the rest are decided with at most 2.4 % wrong
   verdicts [dec_guard.csv].

## 0 Data and characteristics

- 9,000 parts read without failure, 500 per alternative; 10 parts carry no scan in the archive, so the
  characteristics rest on 8,990 parts [features_rddac.csv].
- 396 simulations matched to the experiments (6 sheet thicknesses × 11 friction coefficients per geometry
  and force) and 264 over the DDACS design corners [features_ddacs_rddac.csv, features_ddacs_corners.csv].
- Seven quality characteristics, defined once in `scripts/qc.py` and measured identically on scans and
  simulated nodes about the cup-bottom plane: draw-in at the mid-sides and at the corners, flange waviness,
  wall angle after drawing, arm angle after cutting, cup depth, bottom dome after cutting.
- Centres of batches, alternatives and cells are 10 % trimmed means: edge positions on the scans are
  quantised by the pixel grid, and medians of quantised values jump between grid levels (Section 1).

## 1 Production floor

The floor F is the 95 % quantile of the difference between the centres of two batches of 50 consecutive
parts of one alternative, pooled over alternatives [alt_floor.csv, sens_drift.csv].

| Characteristic | Floor (95 % CI) | Concave | Convex | Part SD | Floor / scatter floor |
|---|---|---|---|---|---|
| Draw-in, mid-side (mm) | 0.085 (0.076–0.095) | 0.079 | 0.094 | 0.131 | 1.40 |
| Draw-in, corner (mm) | 0.046 (0.035–0.052) | 0.053 | 0.030 | 0.027 | 4.49 |
| Flange waviness (mm) | 0.0028 (0.0024–0.0031) | 0.0037 | 0.0021 | 0.0020 | 2.53 |
| Wall angle (°) | 0.081 (0.071–0.092) | 0.089 | 0.075 | 0.130 | 1.47 |
| Arm angle, cut (°) | 0.109 (0.094–0.122) | 0.116 | 0.100 | 0.091 | 2.56 |
| Cup depth (mm) | 0.011 (0.010–0.012) | 0.009 | 0.012 | 0.007 | 3.93 |
| Bottom dome, cut (mm) | 0.0070 (0.0061–0.0081) | 0.0034 | 0.0082 | 0.0036 | 3.86 |

- **Drift, not scatter, sets the floor.** After the parts of each alternative are permuted (time order
  removed), the floor shrinks by a factor of 1.4 (mid-side draw-in, wall angle) to 4.5 (corner draw-in)
  [sens_drift.csv]. Batches of one design drift apart by more than independent parts would.
- **Robust to the analysis constants.** Over batch sizes 25 to 100 and quantiles 0.90 to 0.99 the floor moves
  by a factor of 0.64 to 2.2; the share of resolvable contrasts stays at 0.97–1.00 for geometry, 0.75–0.88
  for blank-holder force and 0.26–0.50 for lubrication [sens_floor.csv, sens_esr.csv].
- **Median against trimmed mean.** Batch medians inflate the floor of mid-side draw-in by 38 % and of the wall
  angle by 31 % (pixel-grid quantisation); the other five change by at most 5 % [sens_floor.csv].

## 2 Which design and process differences production resolves

Effect-to-scatter ratio ESR = |difference of two alternatives' centres| / F, for alternatives that differ in
one factor [alt_effects.csv].

| Factor | Contrasts with ESR ≥ 1 | Median ESR per characteristic | Bootstrap P(ESR ≥ 1) ≥ 0.95 |
|---|---|---|---|
| Geometry | 63 of 63 | 2.8 (waviness) to 130 (wall angle) | 63 of 63 |
| Blank-holder force | 106 of 126 | 0.9 (wall angle) to 10.2 (depth) | 102 of 126 |
| Lubrication pattern | 53 of 126 | 0.5 to 1.6 | 43 of 126 (61 at ≤ 0.05) |

- The wall angle is the one characteristic that does not respond to blank-holder force (39 % of contrasts).
- **Minimum resolvable change of blank-holder force** (F / sensitivity of the cell centres): cup depth 28 kN
  (95 % CI 25–32), waviness 33 kN, corner draw-in 55 kN, mid-side draw-in 90 kN, arm angle 101 kN, wall angle
  346 kN, dome 623 kN, the last two beyond the tested 100–500 kN [alt_mrc.csv].
- **Incoming conditions are too stable to matter.** Shifting a characteristic by one floor would take 19 to
  147 µm of sheet thickness against a within-series SD of 2.9 µm, and 14 to 162 K of punch temperature against
  a drift of 1.1 to 6.4 K per series [alt_mrc.csv, features_rddac.csv].

## 3 Simulation against production

Offset between the parts' 95th percentile and the nominal simulation (t = 0.98 mm, μ = 0.10), median over the
alternatives of a geometry, in floors (concave / convex) [dec_alternatives.csv]:

| Characteristic | Offset (floors) | Offset of the matched simulation (units) |
|---|---|---|
| Cup depth | −106 / −72 | −0.95 / −0.90 mm |
| Draw-in, corner | −59 / −108 | −3.0 / −3.3 mm |
| Arm angle, cut | −30 / +0.7 | −3.5 / +0.04° |
| Bottom dome, cut | −28 / +8 | −0.04 / +0.06 mm |
| Draw-in, mid-side | −17 / −16 | −1.4 / −1.8 mm |
| Wall angle | +16 / +6 | +1.3 / +0.6° |
| Waviness | +9 / +3 | +0.03 / −0.01 mm |

Within one geometry the offset itself varies by 10.5 to 38 floors between alternatives, so a constant bias
correction cannot get below that.

## 4 Design-stage decisions

Each alternative in turn is treated as a new design and judged from simulation, calibrated on other
alternatives: *within* the family (8 alternatives of the same geometry), *pooled* (17, both geometries) or
*transfer* (9 of the other geometry). Requirements are placed d floors from the true 95th percentile.
Decisive distance: beyond it ≥ 95 % of verdicts are correct. Safe distance: beyond it ≤ 5 % are wrong
[dec_resolution.csv; Figure F3].

| Rule | Within: decisive / safe | Pooled | Transfer |
|---|---|---|---|
| M0 nominal simulation | 150 / 150 | 150 / 150 | 150 / 150 |
| M1 bias-corrected | 15 / 15 | 30 / 30 | 40 / 40 |
| M2 envelope + conformal margin | 25 / 0.5 | 50 / 0 | 75 / 20 |
| M3 simulation + ML discrepancy | 20 / 0 | 25 / 0 | 50 / 20 |
| M4 ML only (no simulation) | 12 / 1 | 25 / 0.5 | 150 / 150 |
| M5 Gaussian-process calibration | **7 / 2** | **12 / 1** | 40 / 30 |

At a requirement 10 floors from the truth [dec_curve.csv]:

| Rule | Within: correct / wrong / uncertain | Transfer: correct / wrong / uncertain |
|---|---|---|
| M0 | 69 % / 31 % / 0 | 69 % / 31 % / 0 |
| M1 | 91 % / 9 % / 0 | 71 % / 29 % / 0 |
| M2 | 67 % / 0 / 33 % | 65 % / 9 % / 26 % |
| M3 | 65 % / 0 / 35 % | 66 % / 11 % / 23 % |
| M4 | 94 % / 0 / 6 % | 56 % / 31 % / 14 % |
| M5 | 97 % / 0 / 3 % | 77 % / 21 % / 3 % |

- **M5 per characteristic, within the family** (decisive / safe, floors): waviness 1.5 / 0.5, wall angle
  2.5 / 0.5, corner draw-in 2.5 / 0.5, mid-side draw-in 4.5 / 1.0, depth 5 / 3.5, arm angle 6.5 / 2.5,
  dome 15 / 9.5. In units: 0.004 mm, 0.20°, 0.12 mm, 0.38 mm, 0.054 mm, 0.71° and 0.11 mm
  [dec_resolution.csv, alt_floor.csv].
- **What the simulation adds** (M3 against M4): within a family nothing; ML on the produced alternatives alone
  is more decisive (12 against 20 floors). Across geometries everything: without the simulation the model
  cannot leave the geometry it was trained on (150 floors), with it the rule decides at 50.
- **Where the AI helps and where it does not.** The Gaussian-process discrepancy is the most decisive rule
  within the family and pooled, and ties with bias correction across geometries, but in transfer it is
  over-confident: it abstains in 3 % of verdicts while being wrong in 21 % at 10 floors. The conformal
  envelope knows better what it does not know (26 % uncertain, 9 % wrong).

## 5 Calibration budget

Within-family calibration on every subset of k produced alternatives [budget_resolution.csv; Figure F4]:

| k | M1 decisive | M2 decisive / safe | M5 decisive / safe | Error at 10 floors (M2, M5) |
|---|---|---|---|---|
| 1 | 20 | 12 / 12 | – | 8.1 %, – |
| 2 | 20 | 15 / 8 | 20 / 7.5 | 3.4 %, 3.0 % |
| 3 | 20 | 25 / 4 | 20 / 5 | 1.5 %, 1.8 % |
| 4 | 20 | 25 / 2.5 | 15 / 3.5 | 0.8 %, 0.9 % |
| 5 | 20 | 25 / 1.5 | 10 / 2.5 | 0.4 %, 0.4 % |
| 8 | 15 | 25 / 0.5 | 7 / 2 | 0 %, 0 % |

Bias correction (M1) never gets safe below 15 floors. With a conformal margin, more evidence only makes the
rule safer; with the Gaussian process it also makes it more decisive. Four to five produced alternatives of a
family are the point where both calibrated rules become reliable.

## 6 Design space

Simulated against measured sensitivity [ds_sensitivity.csv; Figure F2]:

- **Blank-holder force:** the simulation overstates the effect on draw-in 3 to 7 times and on the concave
  wall and arm angle 4 to 8 times, understates it on the dome 3 to 7 times, reproduces cup depth on the
  concave cup (1.1) and gets the sign of the convex wall angle and the convex waviness wrong.
- **Sheet thickness:** reproduced for cup depth (1.1) and dome (1.0) on the concave cup and for corner
  draw-in on both (0.85–1.03); wrong in sign for mid-side draw-in.
- **Friction:** 5 to 630 times the effect inferred from the measured oil film, 4 of 14 with the opposite
  sign. This points to the dataset's linear oil-to-friction mapping rather than to the solver.
- **Minimum resolvable change of blank-holder force with simulation as the only evidence** (floor plus the
  calibrated margin over the simulated sensitivity): 75 to 139 kN for draw-in against 36 to 124 kN in
  production; for depth 112 to 321 kN against 23 to 31 kN.
- **Design steps between the DDACS corners**, in floors: the steps move the wall angle by 10 to 264 and the
  corner draw-in by 19 to 152, while the convex steps move the dome by 0.6 to 0.7 floors, below what
  production can resolve.
- **Gaussian-process surrogate of the simulations** (leave-one-out over process conditions): error 0.04 to
  0.12 floors for draw-in, 0.6 to 1.9 for wall angle, arm angle and depth, 5.6 for the convex waviness and 11
  for the concave dome; a surrogate stands in for the simulation only for the smooth characteristics
  [ds_surrogate.csv].

## 7 In-line verifiability

- Part level: from the force record, sheet thickness and oil film, out-of-fold R² is at most 0.17 (cup depth)
  and at most 0.03 for five of seven characteristics; the limit of detection is 3.1 to 3.3 within-alternative
  SDs, i.e. no better than knowing nothing [inline_lod.csv].
- Batch level: the drift between batch centres is explained to at most 11 % (R² out of fold, folds by
  alternative); removing it lowers the floor by at most 16 % (depth) [inline_drift.csv].
- The scan stays the evidence; force monitoring does not tighten the floor.

## 8 Threats to validity

- **One material, one press, two geometries.** The procedure is general, the numbers are not.
- **The floor is short-term.** Each alternative was produced once, as 500 consecutive strokes; days, coils and
  tool states are not covered, so the floor is a lower bound of series-production variation.
- **Blank-holder force and stroke speed are confounded:** 46.8 mm/s at 100 kN against 78.6 mm/s at 300 and
  500 kN [features_rddac.csv]. Force effects include the speed effect.
- **Punch temperature drifts** by 1.1 to 6.4 K within a series (median 4.3 K) and cell medians differ by up to
  5.3 K [features_rddac.csv]; part of every between-alternative effect can be thermal, although the
  temperature sensitivities in Section 2 make it a fraction of a floor.
- **Lubrication is a pattern, not a friction coefficient.** Pattern medians of the oil film are 1.32 (coarse),
  1.11 (medium) and 0.97 g/m² (fine) with a within-series SD of 0.10 g/m²; the simulations are matched through
  a linear oil-to-friction mapping that Section 6 calls into question.
- **Scan measurement.** Edge positions are quantised by the pixel grid (handled by trimmed means, Section 1);
  absolute offsets between scans and simulations carry the scanner calibration uncertainty, floors and
  effects do not.
- **Conformal margins on few alternatives.** With 8 to 17 calibration alternatives the 90 % margin equals the
  largest calibration residual; the guarantee is marginal and assumes exchangeable alternatives, which the
  transfer violates by design.
- **Synthetic requirements.** Requirements are placed at known distances from the truth to score the rules;
  no specification of the real part is used.
- **Design corners co-vary.** DDACS moves curvature radius, bottom radius and wall angle together between two
  corners per base shape, so single geometric effects are not identifiable.

## 9 What this means for the paper

- The object of study is the design-stage decision, not the predictor: which rule, with how much production
  evidence, gives a verdict that production confirms.
- Contributions that survive the data: the production floor as the unit of design decisions; safe and
  decisive distances as decision-level detection limits; the calibration budget; and a clear map of where
  machine learning helps (within a family, where the Gaussian-process calibration halves the decisive
  distance of the best physics-only rule) and where it does not (across geometries, where only the
  simulation carries the decision and no calibration is safe below 20 floors).
- Open items before writing: a realistic requirement scenario taken from the part's function, a procedure
  figure and positioning table, and the simulated three-referee review of the playbook.

## 10 Additions after the publishability review

### 10.1 Calibration design [budget_design.csv]

| Rule | Calibration set | Safe distance k = 2 / 3 / 4 / 5 | Wrong at 10 floors k = 2 / 3 / 4 / 5 |
|---|---|---|---|
| M2 | brackets the new design's force | 3 / 1.5 / 1.5 / 1 | 0 / 0 / 0 / 0 % |
| M2 | extrapolates | 12 / 12 / 12 / 12 | 7.9 / 5.8 / 5.6 / 5.2 % |
| M5 | brackets | 2.5 / 3 / 2.5 / 2 | 0.1 / 0.6 / 0.2 / 0.1 % |
| M5 | extrapolates | 12 / 12 / 10 / 10 | 6.7 / 5.4 / 4.6 / 4.7 % |

### 10.2 Applicability guards [dec_guard.csv]

Across geometries the novelty guard (simulated q95 of the new design outside the range of the calibration
alternatives) fires in 90.5 % of the cases and the family guard in all; the remaining cases are decided with 0 %
(M2) and 2.4 % (M5) wrong verdicts at 10 floors. Within a family neither guard fires.

### 10.3 Requirements from general tolerances [scen_truth.csv, scen_scores.csv]

ISO 2768-1 angular classes (f/m 0.5°, c 1°, v 2°, legs 10–50 mm) on the wall angle (about the tool's design
angle) and the arm angle (about flat), ISO 2768-2 flatness classes (H 0.1, K 0.2, L 0.4 mm, 30–100 mm) on the
bottom dome; values checked against the standards' text (paper/notes/tolerance_sources.md). 162 decisions per
rule and scope. Within the family: M5 89 % right, 0 % false accepts, 1.2 % false rejects, 10 % trial; M1 87 %
right with 6.8 % false accepts; M2 72 % right, no wrong verdicts, 28 % trial; M0 66 % right, 19 % false accepts.
Transfer: M5 65 % right with 9.9 % false accepts; M2 44 % right, 4.3 % false accepts, 39 % trial.

### 10.4 Robustness [rob_floor.csv, rob_bhf_pairs.csv, rob_decisions.csv]

- Punch-temperature correction lowers floors by 1–14 %; M5 within 7/2.5 floors (reference 7/2), pooled 10/1.
- Conformal level 0.80 / 0.95: M2 within unchanged (25/0.5); M5 decisive 6 / 7.5.
- Resolution target 0.90 / 0.99: M5 5 / 12, M4 8 / 15, M1 10 / 30 floors (ranking unchanged).
- Force effects at equal stroke speed (300→500 kN): corner draw-in and depth resolved in 6/6 contrasts, mid-side
  draw-in, arm angle and dome in 5/6, waviness 3/6, wall angle 2/6.
- Oil film replaced by the pattern median for M3: decisive 40 floors (reference 20), safe 3.
- Conformalised GP (M6): safe 0.5 floors, decisive 75 everywhere (negative result).

### 10.5 Related work found

The dataset authors' descriptor paper (Baum et al. 2026, Trans Indian Inst Met, doi:10.1007/s12666-026-03870-5)
decomposes the simulation-to-reality deviation (geometry 77–92 % of its variance) and predicts it with gradient
boosting from process measurements (R² 81–92 %). This paper's question is complementary (design-stage decisions
without process measurements of the new alternative); their R² is mostly between-alternative variation, which
the within-alternative in-line analysis removes.

### 10.6 Second demonstration: build orientation in powder bed fusion of PA12 [case2_*.csv]

NTNU dataset (Leirmo and Semeniuta 2021, doi:10.18710/DHACHZ, CC0): 111 specimens (37 orientations, 0–180° in 5°
steps about one axis, once per build, three builds; anchors excluded), eight characteristics (pin and hole
diameters, across-flats distance, cylindricity, flatness, position), mean of three CMM repetitions (repeatability
0.003–0.012 mm against 0.05–0.32 mm between specimens). Six orientation classes of 30° are the alternatives; a
batch is a class within one build. No simulation: rules M0 (nominal geometry), M1 (median q95 of the other
classes), M2 (with conformal margin), M5 (GP over orientation).

- Floors 0.051–0.31 mm, as large as the single-specimen SD: builds differ.
- Production resolves 18 of 120 orientation-class pairs (cylindricity 5/15, across-flats 6/15, others 0–3/15).
- Decisive/safe distances over all characteristics: M0 5.5/5.5, M1 2/2, M2 4/1, M5 3.5/1 floors.
- Calibration budget: M1 decides at 2 floors with a single produced class; M2 and M5 safe at 1–1.5 floors from k=2.
- Reading: where alternatives barely differ relative to the floor, the record of any one of them answers for the
  others; deep drawing is the opposite case.
