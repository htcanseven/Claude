# Response to the reviewers

**Manuscript:** *Evaluating design-stage manufacturability decisions against the resolution of production*. The original title was *Qualifying design-stage manufacturability decisions with production evidence*.
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"

The three referees reviewed the first version (`paper/review/main_v1.pdf`) independently and recommended major revision. Each report was checked against the released code and data, and every re-analysis that the referees reported was reproduced before the corresponding change was made. Several of their checks overturned conclusions of the first version, and the revised manuscript says so.

This document first summarises the changes that cut across the reports. It then answers every comment in turn: the response, then the change in the manuscript with its section, table or figure. Section, table and figure numbers refer to the revised manuscript unless marked "v1". All numbers come from the released result files and can be regenerated with `scripts/run_all.sh`.

---

## Summary of the main changes

1. **Reframing as a framework.** The paper now poses three research questions for design research (Section 1):
   - how to express the fitness of a design-stage prediction for a manufacturability decision independently of the predictor and the characteristic;
   - how that fitness depends on the amount of production evidence and on its relation to the new design;
   - what simulation and machine learning contribute once production evidence exists.

   It presents the floor and the two distances as a framework with stated assumptions, properties and an exact estimator (Section 3). It positions the work in:
   - decision-based design, design margins, testing and verification strategies, variation risk management, the design research methodology and the validation square (Section 2.2);
   - validation metrics, predictive maturity and valid input domains (Section 2.3);
   - decisions with abstention: conformity assessment, operating characteristics and selective classification (Section 2.4).

   The distances are now introduced explicitly as operating characteristics (Section 3.4).

2. **Evaluation by evidence relation (grouped cross-validation).** All three referees found that leave-one-alternative-out within a family keeps two near-replicate siblings in the calibration set. The evaluation is now organised by the relation of the new design to the produced evidence (Section 4.4):
   - a new variant with a produced sibling (the former "within" scope);
   - a new process setting, with all three alternatives of one blank-holder force held out together, split into interpolation (300 kN) and extrapolation (100 or 500 kN);
   - a new family;
   - pooled versions of the first two.

   The calibration design is classified the same way, as sibling, interpolation or extrapolation, including k = 1 (Section 5.6, Table 10, Fig. 4).

3. **Baselines and ablations.** Every calibrated rule is now evaluated with and without the simulation:
   - M1 and M1n;
   - M2 and M2n;
   - M3 and M4;
   - M5 and the Gaussian process of q95 without the simulation, M5n.

   Three further rules were added:
   - the nearest produced setting NN, which uses neither simulation nor learning;
   - a friction-calibrated simulation Mc, with a calibration parameter in the Kennedy–O'Hagan sense;
   - the worst case of a process-window simulation M0w, as a practice baseline.

   Paired bootstrap differences isolate what the simulation and learning add (Section 5.5, Table A4).

4. **Exact distances and inference.**
   - **Estimator.** The distances are now computed exactly, as order statistics of the exclusion distances, instead of on the coarse grid. Requirements below zero are excluded for the non-negative characteristics. One-sided distances (false accept, false reject) are reported (Table A2).
   - **Bootstrap intervals.** The intervals come from a family-stratified bootstrap of the held-out alternatives. Each resample draws a block-bootstrap replicate of the true q95, so the uncertainty of the reference enters. The resamples are common to all rules, which gives paired intervals.
   - **Refitting bootstrap.** A second bootstrap refits every alternative-level rule on resampled calibration sets (Table 13).

5. **Measurement and the floor.** Referee 3 showed that the scan direction along the lines and the north wall carry measurement noise and bias. The redundancy of the scans is now analysed (Section 4.3, Table A8), and the characteristics are redefined:
   - mid-side draw-in from the flange widths across the scan lines;
   - wall angle from the east and west walls.

   A new table of the floor's components (Table 5) reports:
   - the short-term and long-term standard deviations;
   - the share of the floor that independent part-to-part noise, including scanner repeatability, could explain (15–33 %);
   - the floor from half-length series;
   - a floor of the decided statistic q95 itself (0.92–1.49 floors);
   - an upper bound of the variation between runs, from the quasi-replicate lubrication series (1.2–9.8 floors).

   The extraction noise of the simulated characteristics is quantified (Table A9), and a smoothed-simulation variant enters the robustness analysis.

6. **Gaussian-process rule.**
   - **Renaming.** M5 is renamed "GP correction of the envelope". The Kennedy–O'Hagan framing is dropped; a genuine calibration parameter now appears in Mc.
   - **Noise floor.** The GP noise is bounded below by the sampling variance of the calibration alternatives' q95.
   - **Reporting.** Hyperparameters at their bounds and empirical coverage are reported (Tables A3 and A7).
   - **Variants.** The robustness analysis adds a Matérn kernel, a linear trend, one-hot lubrication, length scales of at least one step, and the original specification.

7. **Interval labels.** The "split-conformal 90 %" margin is now described as what it is: a largest-residual margin whose attainable coverage is n/(n+1) (or (n−1)/(n+1) with an estimated offset). The M3/M4 margin is described as a jackknife. Empirical coverage is reported for every interval rule and evidence relation.

8. **Guard.** The misreported post-guard error is corrected: among the 24 verdicts the novelty guard lets through for a new family, M5 is wrong in 6. The guards are now also evaluated where they can fire within a family, for new process settings. A range guard was added. False alarms and misses are reported with counts (Section 5.7, Table 11).

9. **Tolerance scenario.** The scenario has been corrected:
   - the ISO 2768-1 rows follow the shorter leg; the convex arms use the "up to 10 mm" row;
   - the ISO 2768-2 flatness scenario of the dome is removed;
   - false accepts are reported conditional on failing alternatives;
   - the results are stratified by the distance of the limit from the truth;
   - the effect of deciding the worst side instead of the mean is counted;
   - a cost comparison is added (Section 5.8, Table 12).

10. **PA12 case removed and claims narrowed.** The powder bed fusion case violated the batch definition and could not test the claims, so it has been removed. Section 6.5 states the data requirements it revealed.
    - **Guidelines.** They are split into general guidance that follows from the framework and observations on this dataset with their evidence base (Table 14).
    - **Development record.** The record and the selection optimism of rules added after review are stated (Section 4.5).
    - **Threats to validity.** These are extended (Section 6.6).

### How the conclusions changed

| First version | Revised version |
|---|---|
| The GP calibration of the simulation is the best rule within a family (decisive at 7, safe at 2 floors). | With a produced sibling, the nearest produced setting, which uses neither simulation nor learning, is the most decisive rule (3.4 floors). The GP with and without the simulation is equally good (6.6/1.4 and 6.0/1.0 floors). The paired difference is +0.6 floors (0.0 to +1.6). |
| Four to five bracketing alternatives make calibrated rules reliable. | Bracketing was mostly the presence of a sibling. [B1: budget finding]. Production evidence buys safety before decisiveness. |
| Machine learning helps where it corrects a physical model. | Within a family the simulation adds nothing to a calibrated rule, and its force trend makes the bias correction worse. Learned models match the nearest produced setting in accuracy and add calibrated abstention where the calibration alternatives resemble the new design. The simulation is indispensable only for a new family. |
| The nominal simulation needs 150 floors. | 108 floors with the exact estimator, mostly through false rejects. |
| The guard leaves M5 wrong in 2.4 % across geometries. | M5 is wrong in 6 of the 24 verdicts the novelty guard lets through (25 %). |
| 89 % of 162 tolerance decisions correct. | Corrected scenario with 108 decisions. For a new variant the nearest setting is right in all, and M5 in 93 % (75 % within 5 floors of the limit). For a new setting the nearest setting is right in 97 % and M5 in 75 %, with 22 % sent to trial. |

---

## Referee 1 (design theory and methodology)

### Major 1. Contribution to design research not separated from the case

**Response.** Agreed; this was the most important structural weakness.

**Change.**
- **Section 1** states three research questions for design research and the contribution as a framework plus its evaluation design. It ties the work to decision-based design, design margins and verification planning.
- **Section 3** presents the framework independently of deep drawing:
  - the decision problem and its scope (Section 3.1);
  - the floor with assumptions A1–A3 and its properties: unit invariance, its relation to the short- and long-term standard deviations under a normal model, and its dependence on the protocol (Section 3.2);
  - the distances as operating characteristics, with five stated properties and a decision-theoretic reading whose assumptions are explicit (Section 3.4).
- **Abstract and conclusions** are rewritten around the generalisable findings, with three numbers in the abstract.
- **Section 6.4** discusses the implications for margins, verification planning, front-loading and the evaluation of AI-based DFM support.
- **Appendix.** Tables A3 and A5 of v1 (sensitivity ratios, in-line verifiability) have been removed from the paper and remain in the repository.

### Major 2. Positioning in the design literature; Table 1

**Response.** Agreed. The suggested streams have been added wherever the revised text uses them. Every reference was checked against Crossref or arXiv.

**Change.**
- **Section 2.2** adds:
  - decision-based design (Hazelrigg 1998; Lewis et al. 2006);
  - design margins (Eckert et al. 2019; Brahma and Wynn 2020);
  - testing and verification strategies (Thomke and Bell 2001; Loch et al. 2001; Salado and Kannan 2018);
  - variation risk management (Thornton 1999);
  - design-support evaluation (DRM, Blessing and Chakrabarti 2009; validation square, Seepersad et al. 2006; Frey and Dym 2006).
- **Section 2.3** adds validation metrics (Ferson et al. 2008; Liu et al. 2011), predictive maturity (Hemez et al. 2010) and the valid input domain (Malak and Paredis 2010).
- **Section 2.4** is new. It covers guard-banded conformity assessment, operating characteristics (Bechhofer 1954), selective classification (Chow 1970; Geifman and El-Yaniv 2017) and interval scores (Gneiting and Raftery 2007).
- **Table 1** now includes design margins, conformity assessment with OC curves and selective classification.
- **Novelty claim.** "For the first time on open data" and "has not been available before" are removed. Section 2.4 states the novelty precisely: a unit set by production, which makes the operating characteristics comparable across characteristics and predictors, and their evaluation by evidence relation.
- **Not cited.** Set-based design and the predictive-maturity sequel papers are not cited, because the revised text does not rely on them.

### Major 3. Construct validity of the floor

**Response.** Agreed on all five points. Each is now analysed or stated.

**Change.**
- **(a) Batch centre against q95.** Section 3.2 states that the floor is a unit, not a resolution of q95. Section 5.1 and Table 5 report a floor of q95 itself: the 95th percentiles of two batches of 100 parts differ by 0.92–1.49 floors. The block-bootstrap standard error of an alternative's q95 is 0.11 floors (median). Distances below about one floor are therefore at the limit of what production can confirm.
- **(b) Dependence on the protocol.**
  - Section 3.2 writes the dependence on B, α and the series length into the definition.
  - Table 5 gives the floor from the first half of each series (0.49–0.95 of the full floor).
  - Table 13 adds batch sizes of 25 and 100 and quantiles of 0.90 and 0.99, and adequacy shares p = 0.90 and 0.99.
- **(c) Run-to-run variation.** Each geometry and force cell has three lubrication series that production mostly cannot tell apart; these serve as quasi-replicates. Their centres differ by 0.5–1.6 floors in the median and by 1.2–9.8 floors at 95 %, an upper bound of run-to-run variation (Table 5). The floor is called a lower bound for series production throughout, and Section 6.6 discusses the effect on the effect-to-scatter ratios.
- **(d) Commensurability.**
  - Per-characteristic distances are given for two relations (Table A5) and, for the safe distances, one-sided (Table A2).
  - The tolerance scenario relates the floor to drawing tolerances: its stratification gives the distances in tolerance terms.
  - The PA12 comparison has been removed together with the case.
- **(e) Local MRC.** The MRC is defined as a local quantity (Section 3.2). Table 6 reports it separately for 100–300 and 300–500 kN.

### Major 4. Distances defined on the unobservable truth; pooled sides

**Response.** Agreed. Both remedies (i) and (ii) were adopted, and the one-sided distances were added.

**Change.**
- **Operating characteristics.** Section 3.4 presents δd and δs explicitly as operating characteristics: functions of the true margin over a population of design situations, like the OC curve of an acceptance plan. It explains how a design team uses them (choosing a rule, judging decidability before the requirement is fixed, planning trials). The v1 sentence calling δd "the smallest margin between prediction and requirement" has been removed.
- **Observable view.** Section 5.5 reports the share of correct verdicts as a function of the margin between the predicted interval and the requirement. It rises from 86 % to 99 % for the nearest setting on a new setting, but stays at 72–75 % for M5 on a new family. The observable margin is therefore informative only where the rule is calibrated.
- **One-sided distances.** These are in Table A2. M0, for example, has a false-accept safe distance of 17 floors and a false-reject one of 109.
- **Cost bound.** Its assumptions are stated (Section 3.4).
- **Worked cost example.** It uses the realistic margins of the tolerance scenario (Section 5.8). With c_FR = c_FA/2, the cheapest rule is NN for a new variant at any trial cost; for a new setting it is M2n up to c_T = 0.1 c_FA and NN beyond; for a new family it is M2 up to 0.1 and M5 beyond.

### Major 5. Near-replicates in the within-family evaluation

**Response.** Agreed. This comment, which Referees 2 and 3 also made, changed the paper the most. The referee's re-analysis was reproduced: under leave-one-force-level-out, M5 drops to decisive 17.8 and safe 7.4 floors with the revised definitions and estimator.

**Change.**
- **Evidence relations.** The evaluation is organised by evidence relation (Section 4.4); Table 8 and Fig. 3 report every rule for each relation.
- **Calibration design.** It is split into sibling, interpolation and extrapolation, including k = 1 (Table 10, Fig. 4). [B2: budget numbers].
- **Guidelines.** They are re-derived (Table 14).
- **Leave-one-out description.** Leave-one-alternative-out is now described as judging "a new variant of a produced process setting".

### Major 6. Process-setting decisions; requirement model

**Response.** Agreed.

**Change.**
- **Scope.** Section 3.1 states the scope of the decisions: the release of variants and process settings in process planning and tryout, and the transfer of production knowledge to a new family in platform and variant design. Section 4.1 states that within a geometry the new designs are process settings on an existing tool, and that the geometry change is the only product-design change.
- **Negative transfer result.** It is now a headline finding in the abstract and conclusions.
- **Requirement forms.** Two-sided and high-conformance requirements are discussed in Sections 3.1 and 6.5. The adequacy shares p = 0.90 and 0.99 are evaluated (Table 13).
- **Linear dimensions.** These are not added to the scenario. The cup depth's "nominal" is the drawing depth of the simulation model (30 mm), and its offset from the scans reflects a difference of reference surfaces (Section 5.3), so no design nominal is available.
- **DDACS corners.** These are not reported, because they have no production counterpart (see Minor 15).

### Major 7. Guard minimal, evaluated on two geometries, misreported

**Response.** Agreed; the misreported rate was an error.

**Change.**
- **Corrected rate.** Section 5.7 and Table 11 report conditional counts. For a new family, the novelty guard lets 12 of 126 cases through, all of them mid-side draw-in or waviness. Among their 24 verdicts at 10 floors, M5 is wrong in 6 and M1 in 6; M2 is wrong in none and sends 12 to trial.
- **Non-trivial setting.** The guards are now evaluated for a new process setting, where they can fire within a family. A range guard was added, which refuses the extrapolated forces, together with the novelty guard. False alarms and misses are reported: 73–96 % of the verdicts the novelty guard refuses would have been correct.
- **Positioning.** The guard is positioned against the valid input domain (Malak and Paredis 2010) in Section 3.5.
- **Conclusions.** The "nine in ten" sentence has been removed from the conclusions.

### Major 8. Claims about where machine learning helps

**Response.** Agreed. The requested ablation (a GP without the simulation) and M1/M2 without the simulation were added. They reverse the v1 claim.

**Change.**
- **Ablations.** Section 5.5 and Table A4 report paired differences. Within a family, M5 − M5n = +0.6 (0.0 to +1.6), M2 − M2n = +3.9 (+0.5 to +7.4) and M1 − M1n = +6.2 (+4.6 to +9.7). For a new family the simulation gains about 93 floors.
- **M4's transfer failure.** It is described as following from the setup: no geometric descriptor is learnable from one geometry.
- **Data regime.** It is stated in Section 6.3.
- **Continuous geometric descriptors.** These would need geometry-varying production, which the data do not have. Section 7 names this as an extension.

### Major 9. Guidelines go beyond the evidence

**Response.** Agreed.

**Change.**
- **Guidelines table.** Table 14 is split into general guidance that follows from the framework and observations on this dataset. The evidence base (18 alternatives, 2 geometries, 7 characteristics; the new family on two calibrations) is stated in the header.
- **Minimum resolvable change.** The guideline "do not iterate below the MRC" now says that such changes are invisible in batch centres but may still matter in the tail. The MRC is local.
- **k-dependent rows.** These are re-derived from the grouped budget.

### Major 10. Evaluation of the support, not only the instruments

**Response.** Agreed that the use of the procedure by design teams has not been evaluated. A walkthrough or interview study is not possible within this revision, so the claim has been reduced as the referee suggests.

**Change.**
- **DRM positioning.** Sections 1 and 6.4 position the paper in DRM: a prescriptive study whose framework and procedure receive an initial evaluation on production data. That evaluation establishes empirical performance validity in the sense of the validation square, but not use by design teams.
- **Procedure.** It is specified with inputs, outputs, decision points, and once-per-family versus per-design steps (Section 3.6, Fig. 1).
- **Practice baseline.** M0w, the worst case of a process-window simulation, was added. It is neither safe nor decisive (94 and 119 floors).
- **Future work.** Success criteria linking the distances to trials and late changes, and an evaluation with design teams, are stated as future work (Sections 6.4 and 7).

### Minor comments

1. **Abstract.** Rewritten (250 words, three result numbers), with the scope by relation, and the elliptical sentence removed.
2. **Novelty claims.** Removed; see Major 2.
3. **"No design-stage decision needs to be finer".** Removed. Section 3.2 now says that a difference below the floor is not a question the design stage needs to answer finer, and that the MRC concerns centres.
4. **Lower limits, two-sided requirements, single run.** Covered in Section 3.1. "Adequate" refers to a single 500-part run (Sections 3.2 and 6.6).
5. **Pair set and per-geometry floors.**
   - The pair set is all i < j within an alternative, pooled (Eq. 2).
   - Batches below 80 % valid are dropped; the count of dropped batches is in the summary files.
   - Per-geometry floors are used in the decision analysis (Section 3.2, Table 4 note), and Table 4 now shows both.
6. **m̄ in Eq. (3) and the ESR ≥ 1 threshold.** m̄ is the centre (trimmed mean) of all parts of the alternative. ESR ≥ 1 means a difference larger than two batches of one design show at 95 %. The error rates this implies are not claimed.
7. **Rule numbering.** The rules are presented in groups (simulation only; simulation and production; production only) in Table 2, in the order of presentation. M6 is introduced in the robustness section as a variant.
8. **M2 margin.** Its attainable coverage and the non-split offset are stated in Section 3.3. The same is done for the jackknife of M3/M4.
9. **M5 identification.** The GP noise floor was added, hyperparameter bound hits are reported (Table A7), and the variants are in Table 13.
10. **Grid and "beyond".**
    - (a) Addressed (Major 4).
    - (b) Equal weights are stated.
    - (c) The grid is replaced by the exact estimator, which removes the "somewhere in (100, 150]" problem.
11. **Cost-bound assumptions.** Stated (Section 3.4).
12. **Subset weighting.** Weighting is stated. Fig. 4 shows the sibling, interpolation and extrapolation curves with bands, and Table 10 reports the spread over subsets (the share of subsets with a wrong verdict at 10 floors) in `budget_design.csv`.
13. **Fig. 1.** Redrawn: per-family steps 1–5, per-design step 6, decision points and outputs.
14. **Process settings and series order.** Section 4.1 states that new designs are process settings on an existing tool. The production order and dates of the series are not given in the dataset documentation; Section 6.6 lists the unknown run order.
15. **DDACS corners.** Removed from the paper; they are mentioned in Appendix A.2 as provided with the code but unused. The incorrect limitation statement has been removed.
16. **Nominal friction.** Mc is the "engineer-calibrated" counterpart the referee suggests, with friction calibrated on the produced draw-in. It does not improve on M1 (Section 5.4). The nominal thickness is now 0.99 mm, the grid value nearest the measured median (Referee 3, Minor 5).
17. **Wall angle and the simulation.** The wall angle is now the E/W mean on the scans. The simulation averages its two symmetric axes (Section 4.3), and the remaining differences are listed.
18. **"All constants fixed before".** Rephrased with a development record (Section 4.5): constants chosen before the decision results were seen, the dates in the repository history, rules added after review named, and selection optimism stated.
19. **Floor CI under drift.** A cluster bootstrap over alternatives was added (Table 4).
20. **Wall-angle MRC; lubrication statement.** The wall-angle MRC statement is corrected; with the E/W definition, force resolves 4 of 18 wall-angle contrasts (Section 5.2). The lubrication statement is qualified to these characteristics.
21. **"Order of magnitude"; overlap claim.** The "order of magnitude" sentence and the overlap claim are removed. Paired bootstrap differences replace marginal intervals (Table A4).
22. **Internal tension.** Removed with the new results.
23. **One-sided distances and shares at 10 floors.** One-sided distances are in Table A2, and right/wrong/trial shares at 10 floors are given in the text for each relation.
24. **Post-guard rate.** Corrected (Major 7).
25. **Tolerance scenario.**
    - (a) Conditional false-accept rates are reported.
    - (b) Requirement distances are reported: of 108 decisions, 32 lie within 5 floors and 55 within 10.
    - (c) The leg rows are stated (Appendix A.1). Only the upper side binds for the wall, and the arm uses |angle|.
    - (d) Linear dimensions: see Major 6.
26. **Fig. 3.** Linear threshold stated in the caption (±10 floors), with 126 cases per point. Distances are given in Table 8 rather than marked on the panels, to keep them readable.
27. **Table 13 variants.** B, α and p variants and the grouped schemes are added.
28. **PA12.** The case has been removed (Section 6.5 explains why).
29. **Section 6.2.** Rewritten (Major 5).
30. **Section 6.4.** The injection-moulding and machining sentence has been removed. The conditions and obstacles are stated instead (Section 6.5).
31. **Threats.** All listed threats are added (Section 6.6).
32. **Conclusions sentence.** Removed.
33. **Appendix.** Tables A3 and A5 of v1 have been removed. The Table 5 note on contrasts now distinguishes the force intervals.
34. **Terminology.** The floor is related to process variation (Section 2.5). "Alternative", "variant" and "family" are used consistently: a family is a geometry, an alternative is a produced design–process combination, and a variant is a new alternative of a family. The number density in Sections 5 and 6 is reduced, with numbers moved into tables.
35. **Archive.** A Zenodo DOI will be deposited for the archived code before resubmission (see the submission checklist). A more descriptive repository name is planned with it.

---

## Referee 2 (machine learning and uncertainty quantification)

### Major 1. Missing baselines

**Response.** Agreed; the conclusions change accordingly.

**Change.** The following baselines and ablations were added:

- **Without simulation.** A GP without the simulation (M5n), the median (M1n), and the median with a residual margin (M2n).
- **Nearest produced setting (NN).** It is equivalent to the referee's sibling rule when a sibling exists and becomes the nearest-force rule otherwise.
- **Interval centres as point rules.** These separate learner from wrapper (Table A3).
- **Part-level learners.**
  - Quantile-loss boosting, which models the 95th percentile directly without resampled residuals (Table A6).
  - Ridge regression.
  - Regularised and flexible boosting settings.
  - Settings selected by an inner leave-one-out.

The referee's numbers were reproduced: GP without simulation 6.0/1.0 against M5 6.6/1.4, and the sibling rule 3.4. The abstract, Section 6.3 and Table 14 now state that the simulation adds nothing within a family and that learning adds calibrated abstention rather than accuracy over NN.

**Lubrication encoding.** It is kept ordinal in M5 because the rank follows the oil amount (series medians 1.15–1.48, 0.92–1.23 and 0.85–1.13 g/m²), and one-hot lubrication is added as a robustness variant (Table 13). Alternative-level boosting was not added: with 6–17 points per fit it is a nearest-neighbour rule in effect, which NN represents.

### Major 2. Near-replicates; bracketing

**Response.** Agreed (see Referee 1, Major 5).

**Change.**
- **Grouped evaluations.** Leave one force level out is the new-setting relation, split into interpolation and extrapolation. Leave one lubrication pattern out is a robustness variant (Table 13).
- **Calibration design.** Classes are sibling, strict interpolation and extrapolation, including k = 1 (Table 10).
- **Dependence on resolvable factors.** How the budget depends on the number of factors production can resolve is discussed in Section 6.1.

### Major 3. GP identification, coverage, framing

**Response.** Agreed.

**Change.**
- **Identification and coverage.**
  - Bound hits and empirical coverage are reported (Tables A3 and A7).
  - The noise level is bounded below by the sampling variance of the calibration q95. Even so, coverage within a family remains 72 %, which the text states.
  - The robustness variants are a Matérn 5/2 kernel, a linear trend (universal kriging), one-hot lubrication, length scales of at least one step, and the original specification without the noise floor.
  - A fully Bayesian GP was not implemented; the length-scale floor plays the role of an informative prior.
- **Framing.**
  - M5 is renamed "GP correction of the envelope", and the KOH framing is removed.
  - Mc implements a calibration parameter (the friction of each lubrication pattern) on the tabulated DDACS runs, as suggested. It does not help (27 floors for a new variant).
  - M6 is read in light of the GP's over-confidence.

### Major 4. Conformal labels and attainable coverage

**Response.** Agreed.

**Change.**
- **Labels.** Table 2 and Section 3.3 now describe a "largest residual" margin with attainable coverage n/(n+1), or (n−1)/(n+1) with the estimated offset. M3/M4 use a "jackknife".
- **Empirical coverage.** Reported per rule and relation (Table A3). M2 covers exactly 8/9 within a family and 17/18 pooled, confirming the referee's analysis.
- **Interval-level variants.** These are kept only for the pooled and transfer scopes where they can change M2; the table note says so.
- **Not implemented.** A pooled-score conformal variant across characteristics, Mondrian and weighted conformal are not implemented. With 6–8 alternatives per fit, the attainable levels, not the method, are the limitation, and the text states this.

### Major 5. Closed form, grid, sides, truth, unit

**Response.** Agreed with (a)–(f).

**Change.**
- **(a) Closed form and positioning.** The distances are derived as order statistics of exclusion distances (Section 3.4) and positioned against interval scores, OC curves, guard-banded conformity assessment, risk–coverage and validation metrics (Section 2.4, Table 1).
- **(b) Exact estimator.** It replaces the grid; M0 is 108 floors instead of 150.
- **(c) One-sided distances.** Added (Table A2).
- **(d) Operating-characteristic view.** Added, together with the observable reliability view (see Referee 1, Major 4).
- **(e) Unit and reference.** The q95 floor and the protocol dependence are reported, and the reference uncertainty is propagated by block-bootstrap replicates of the true q95 in every resample.
- **(f) Infeasible requirements.** Requirements below zero are excluded.

### Major 6. Bootstrap intervals

**Response.** Agreed.

**Change.**
- **Exact and paired.** Grid-free intervals, a family-stratified paired bootstrap with reference replicates, and paired differences (Table A4).
- **Refitting.** A refitting bootstrap of every alternative-level rule (200 resamples; Table 13, last row).
- **Disclosure.** The statement that the fits are held fixed in the main intervals, the number of cases per scope (126), and that a new family rests on two calibrations.
- **Overlap claim.** Removed.

### Major 7. Transfer and guard

**Response.** Agreed (see Referee 1, Major 7).

**Change.**
- **Corrected counts.** Reported in Table 11.
- **New guards.** A range (descriptor) guard was added, and the guards are evaluated for new process settings.
- **Not added.** A GP-variance guard is not added: within a family the GP's predictive variance does not separate the cases it gets wrong (its coverage is 72 %). Using the 264 geometry-varying DDACS runs to test the guard was not possible without production counterparts; Section 7 names geometry-varying production as an extension.
- **Disclosure.** That transfer rests on two instances is stated.

### Major 8. PA12

**Response.** Agreed. The case has been removed, and the generality claim narrowed (Section 6.5).

### Major 9. Dataset-specific guidance; development on the evaluation data

**Response.** Agreed.

**Change.**
- **Guidelines.** Table 14 separates general guidance from observations on this dataset.
- **Development record.** Section 4.5 lists the rules defined first, the rule added during the first analysis (M6), and the rules and schemes added after review. It states the selection optimism (Cawley and Talbot 2010).
- **Confirmatory study.** A confirmatory test on a second dataset is named as future work.

### Minor comments

1. **Unit of evidence.** 126 cases per scope and two transfer calibrations (Section 4.4). The novelty claim has been removed.
2. **Floor pairs and geometry index.** The floor pairs are now described in the text. Per-geometry floors and intervals are given (Table 4). The geometry index is mentioned in Section 3.2.
3. **Centres against tails; "do not iterate".** See Referee 1, Majors 3 and 9.
4. **Table 2 labels.** Relabelled, and the in-sample residuals are stated (Appendix A.1).
5. **M1's nominal baseline against M2's envelope.**
   - The centres of the interval rules are reported as point rules (Table A3).
   - The DDACS ranges are not claimed to be "plausible incoming conditions" beyond the dataset's design. M0w shows that reading the window's worst case does not help, and the smoothed-simulation variant shows the envelope's sensitivity to extraction noise.
6. **Equal weights and d = 0.** Equal weights and the side of d = 0 are stated; the grid is no longer used.
7. **Cost bounds and base rates.** Stated (Section 3.4).
8. **Bracketing.** Replaced by the exact classes (Section 3.5).
9. **Leakage.**
   - The nominal thickness (0.99 mm) is the grid value nearest the median of all parts, which is a population property of the material.
   - Recomputing the floors without each held-out alternative moves them by little, because each alternative contributes 45 of 810 pairs. It is not repeated per alternative.
10. **Development sequence.** Described (Section 4.5).
11. **Constant correction.** Rephrased in Section 5.3 (the spread of the offset).
12. **Per-characteristic cases.** Case counts are in the Table A5 note: 36 verdicts per distance and side, where one wrong verdict moves a share by 2.8 points.
13. **Spread over subsets; k = 1.** The spread is in `budget_design.csv` (share of subset–target pairs with a wrong verdict at 10 floors, 90th percentile of the wrong share). k = 1 is included in Table 10 and Fig. 4.
14. **Scenario stratification.** Stratified by margin, with the nearest-setting baseline (Table 12).
15. **Interval-level and temperature variants.** The interval-level rows are qualified. The temperature slope is pooled over all alternatives; this is acceptable for a data variant and is stated in the table note.
16. **M6.** Read in light of the GP's over-confidence (Section 5.9).
17. **GP coverage.** 72 % is stated.
18. **Threats.** Added.
19. **Appendix A.1.** Hyperparameters, residuals and the fixed fits are reported. The guard and decision intervals now use the same estimator.
20. **Fig. 3.** The axis transformation and case counts are given; M1 and M3 are in Table 8. The figure shows M2, M5, M5n and NN, the rules the text compares.
21. **Table 11 (PA12).** Removed.
22. **Archive.** See Referee 1, Minor 35.

---

## Referee 3 (sheet-metal forming and manufacturing metrology)

### Major 1. No measurement-system analysis

**Response.** Agreed. The redundancy of the scans was used as suggested, and the findings were reproduced:
- **Flange widths.** The width along the scan lines has 4–18 times the part-to-part SD of the width across them, uncorrelated with it and without serial correlation.
- **North wall.** It carries about 0.3° of uncorrelated scatter.

**Change.**
- **Redefinitions.** The characteristics are redefined (Section 4.3, Table 3), and Table A8 reports the redundancy statistics.
- **Effect on the floors.** The mid-side draw-in floor falls from 0.085 to 0.051 mm and its part SD from 0.13 to 0.039 mm. The wall-angle floor is unchanged (0.081 to 0.078°) because the north-wall scatter averaged out within batches.
- **Floor decomposition.** Table 5 decomposes the floor. Independent part-to-part noise, which bounds the repeatability of the scanner from above, would produce 15–33 % of each floor; the rest is variation between batches.
- **Scanner drift.** It cannot be separated from process drift without a reference artefact, and this is stated as a threat (Section 6.6).
- **Gauge study.** Repeat scans with re-fixturing and a traceable reference are not available in the dataset. The note to the dataset authors (`paper/submission/note_to_dataset_authors.md`) asks whether such scans exist.

### Major 2. Systematic scan errors

**Response.** Agreed.

**Change.**
- **South wall.** It returns biased values rather than gaps, and is excluded (stated in `qc.py` and Section 4.3).
- **North-wall bias and Wy − Wx.** Removed by the redefinitions.
- **Diagonals.** The 1.6–2.2 mm diagonal difference is reported; the corner draw-in uses the mean of the diagonals, which is first-order insensitive to a non-orthogonality.
- **Absolute offsets.** The sentence "measured identically" is replaced by an explicit statement that the remaining differences (scanned surface against shell mid-surface, edge treatment, resolution) enter the absolute offsets but not the floors and effects (Section 4.3). The cup-depth offset is interpreted as a reference difference (Section 5.3).
- **Not added.** A mid-surface offset correction is not applied, because the local thickness field is not part of the extracted features. It is listed as a threat.

### Major 3. Extraction noise of the simulations

**Response.** Agreed. The noise was quantified with both suggested measures, the x–y arm difference and the roughness along the friction grid.

**Change.**
- **Noise levels.** Table A9 and Section 5.3 report 1.7–3.1 floors for the wall angle and 2.4–9.8 floors for the dome, with the raw envelope maximum of the dome inflated by up to 21 floors.
- **Smoothed simulation.** A variant replaces the raw values by a quadratic response surface over thickness and friction (Table 13). [R1: smoothed-simulation result].
- **Not done.** Re-extraction from interpolated shell surfaces would need the full simulation archive again (650 GB) and is left as a limitation.

### Major 4. Interpretation of the discrepancies

**Response.** Agreed with (a)–(f).

**Change.**
- **(a) Signed offsets.** Table 7 reports signed matched offsets. The concave arm angle's sign error is stated in Section 5.3: parts bend upwards in every case, simulations downwards in 89–100 %.
- **(b) Force effect.** The force effect, three to seven times the measured one, is attributed to the friction law (pressure dependence; Hol et al. 2012) and the blank-holder model (Section 5.3). Mc tests a calibrated friction coefficient, and it does not repair the trend (Section 6.3). The asymmetry of the flange and the load-cell imbalance are noted as effects a quarter model cannot represent.
- **(c) Friction ratios.** The friction-sensitivity ratios (Table A3 of v1) are removed.
- **(d) Cup-depth offset.** Interpreted as a reference difference.
- **(e) DDACS models.** The documented models are stated (Section 4.2): LS-DYNA, a scaled DP600 flow curve, constant Coulomb friction and springback after both operations. The documentation does not state the yield criterion or unloading model, and Yoshida and Uemori (2002) is cited.
- **(f) Bistable bottom.** The possible bistability of the bottom is mentioned among the threats.

### Major 5. The floor and SPC, capability, short- and long-term variation

**Response.** Agreed.

**Change.**
- **(a) SPC terms.** Table 5 gives σ_ST from subgroups of five, σ_LT, their ratio (1.10–1.41), the white-noise share, and the floor from half series. Section 3.2 relates F to σ_b and σ_w under a normal model. A REML variance-component model was not fitted: the one-way analysis of variance within series gives the batch component (σ_batch in `meas_floor.csv`).
- **(b) q95 floor.** Added.
- **(c) Between-series variation.** Bounded by the quasi-replicate lubrication series, as the referee suggested (1.2–9.8 floors at 95 %).
- **(d) Adequacy share.** p = 0.90 and 0.99 are evaluated. The 3σ level of 0.99865 needs a parametric tail beyond what 500 parts estimate, which is stated (Section 6.5).
- **(e) Physical units.** Distances relate to tolerances through the scenario (Section 5.8). Interruptions are not identifiable without time stamps in the dataset, and this is listed.

### Major 6. GP without simulation does as well as M5

**Response.** Agreed; reproduced (6.0/1.0 against 6.6/1.4 floors).

**Change.** See Referee 2, Major 1. The control is now part of every relation, and Section 6.3 states that the value of the simulation is confined to a new family.

### Major 7. Scope; bracketing as near-twins

**Response.** Agreed.

**Change.** See Referee 1, Majors 5 and 6, and Referee 2, Major 2. The guarded transfer is reported with counts, and the speed confound in force bracketing is noted.

### Major 8. ISO 2768 scenarios

**Response.** Agreed with the main points.

**Change.**
- **(a, b, c) Flatness.** The ISO 2768-2 flatness scenario is removed: it was withdrawn, used the wrong row, and the sag is not a minimum-zone flatness. The text states that drawings of deep-drawn parts would carry ISO 1101 profile and position tolerances to datums (ISO 22081 for general specifications), which the data do not allow to evaluate.
- **Angular rows.** These follow the shorter leg; the convex arm is about 9 mm long, so the "up to 10 mm" row applies.
- **(d) Per-feature tolerances.** The count of decisions whose truth changes when the worst side is decided is reported (12 of 108).
- **(e) Stratification.** The results are stratified by margin: within 5 floors of the limit, M5 is right in 75 % for a new variant and 44 % for a new setting.
- **(f) Acceptance criterion.** p = 0.95 is kept as the scenario's criterion, and p = 0.99 is evaluated on the grid (Table 13).

### Major 9. DDACS corners

**Response.** Agreed.

**Change.** The corners are removed from the paper; they are provided with the code. The inaccurate limitation statement is removed.

### Major 10. PA12 case

**Response.** Agreed with the diagnosis.

**Change.** The case is removed rather than redone. A proper redesign would rest on three builds and eight anchor specimens per build, and could not test the main claims (see also Referee 2, Major 8). Section 6.5 states what the case showed about the data requirements.

### Minor comments

1. **Floor sentence.** Rephrased (see Referee 1, Minor 3).
2. **Pairs.** Pooling, per-geometry floors and the cluster bootstrap are reported.
3. **Quantisation.** The v1 attribution of the median-floor difference to quantisation is dropped. The mid-side draw-in is redefined, and with it the heavy-tailed y-edge noise is removed.
4. **Tool and press data.** The dataset documentation provides the tool data partly. The note to the dataset authors asks for the blank dimensions, the scanner and fixture, and the order and dates of the series.
5. **Nominal thickness.** 0.99 mm.
6. **Lubrication.** The oil amounts per pattern are stated (Section 4.1).
7. **Scan–simulation differences.** Listed, and the weighting is now symmetric (E/W, x/y).
8. **Tilt.** E/W cancels the tilt.
9. **"Incoming material".** The statement is restricted (the thickness MRC sentence is removed).
10. **Local MRC.** Reported per interval (Table 6).
11. **Signed entries.** Table 7.
12. **Overlap and bootstrap.** See Referee 2, Major 6.
13. **Guarded transfer.** Correct-verdict shares are reported with counts.
14. **Leg lengths.** Stated (Appendix A.1); the convex arm uses the "up to 10 mm" row. The design wall angle refers to the DDACS wall-angle parameter of the tool.
15. **Temperature correction.** Its limitation is stated in the table note.
16. **M3 oil variant.** The confound is noted. The variant is kept, with the caveat that it changes both the match and the input.
17. **Threats.** Corrected and extended (Section 6.6).
18. **Constants.** See Referee 1, Minor 18.
19. **Sign information and numbering.** Sign information is discarded for two-sided characteristics (Section 3.1). Numbering: see Referee 1, Minor 7.
20. **Corner tip.** The blank-corner condition is noted among the remaining differences.
21. **Figures.** Fig. 2 is shortened so that the float page leaves room for the caption and page number; it already shows per-geometry floors. The Fig. 3 tick labels are reduced, and its caption gives the case counts.
22. **References.** VDI/VDE 2634 Part 2, ISO 22514-7, ISO 1101, ISO 22081, Hol et al. (2012) and Yoshida and Uemori (2002) are added where the text uses them. ISO 10360-8 and ISO 12781 are not cited, because the revised text does not use them.
