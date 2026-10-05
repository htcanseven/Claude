# Referee report

**Manuscript:** "Qualifying design-stage manufacturability decisions with production evidence" (H. T. Canseven)
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Referee 2:** machine learning and uncertainty quantification (Gaussian-process calibration of computer models, conformal prediction, gradient boosting, model validation, resampling statistics)
**Version reviewed:** main_v1.pdf (28 pages), read together with the LaTeX source, the released analysis scripts and the result CSVs

---

## 1. Summary

The manuscript proposes a unit, the *production floor*: the 95th percentile of the absolute difference between the trimmed-mean centres of two 50-part batches of one design. It uses this unit to measure how close a requirement lies to the truth. It then characterises three-way design-stage decision rules (meets / fails / trial) by two distances: the *decisive distance*, beyond which at least 95 % of verdicts are correct, and the *safe distance*, beyond which at most 5 % are wrong.

- **Rules compared.** Six rules: the nominal simulation, a bias correction, the simulation envelope with a split-conformal margin, a Gaussian-process (GP) correction of the envelope, and part-level gradient boosting with and without the simulation.
- **Data and protocol.** The rules are scored by leaving one alternative out on the open RDDAC/DDACS deep-drawing data: 18 alternatives (2 geometries × 3 blank-holder forces × 3 lubrication patterns) of 500 parts each. Three calibration scopes are used, and the analysis is supplemented by calibration-budget and calibration-design analyses, an applicability guard, ISO 2768 scenarios, robustness checks and a second, simulation-free case on PA12 powder bed fusion.
- **Headline claims.**
  - The GP correction is the best rule within a design family (decisive at 7, safe at 2 floors).
  - Four to five produced alternatives that bracket the new design's process settings make calibrated rules reliable.
  - No rule is safe closer than 20 floors across geometries.
  - Machine learning helps where it corrects a physical model.

The question is important: it scores *decisions* rather than predictions, against production. The open and reproducible pipeline is exemplary. However, my checks with the released code show that the central machine-learning and calibration-design conclusions do not survive simple baselines and a grouped evaluation, and that several uncertainty-quantification components are mislabelled or misreported.

## 2. Assessment of contribution and fit

**Strengths.**

- The paper asks the question design research needs answered: not "how accurate is the model?" but "how close to a requirement can a verdict be trusted?".
- It answers it against the production record of the very alternatives judged.
- Abstention is treated as a legitimate outcome, and the decisive/safe pair makes the trade-off between deciding and not misleading explicit.
- The data are open and the pipeline is genuinely reproducible: I could re-run the alternative-level rules in minutes.
- The threats-to-validity section is candid, and several robustness checks are provided.

**Nature of the contribution.** The learning and UQ components are off-the-shelf: a scikit-learn GP, histogram gradient boosting and a split-conformal-type margin. The case for publication therefore rests on two things.

1. **The scoring framework must be a general, well-characterised method.** The framework is floor + two distances + calibration budget. It is not yet characterised:
   - The two distances are quantiles of standard interval-error functionals, normalised by the floor (Major 5).
   - Their estimation on a coarse grid with test-set-only bootstrap is ad hoc (Majors 5 and 6).
   - They are not positioned against operating characteristics, guard-banded conformity assessment, coverage-width scores or risk-coverage curves.
2. **The design conclusions must hold.** The conclusions about machine learning, simulation and calibration design are not robust to simple baselines and a grouped protocol (Majors 1, 2, 7).

**Fit to RED.** The topic is squarely within the special collection. In its current form, however, the manuscript is essentially a case study of one dataset: 18 alternatives of one tool set, two geometries and two transfer instances. The second case cannot test the main claims. This is close to RED's desk-reject description ("case studies of individual design efforts", "applying existing tools").

The "design" content also needs clarifying. Within a family, the "new designs" are process settings on an existing tool. The only geometric design change is the transfer, where no rule is reliable.

A revision could fit RED if it does three things:

1. Establish the distances as a general evaluation method, with stated properties, an estimator and inference, positioned against existing decision-oriented validation measures.
2. Base the ML/UQ conclusions on fair baselines and a grouped evaluation.
3. Either add a second dataset with a design-stage predictor, or narrow the claims to what one dataset supports.

## 3. How the claims were checked

I read the following scripts in full: decisions.py, budget.py, guard.py, robustness.py, case2_pa12.py, alternatives.py, common.py, qc.py and scenarios.py. I also read the result CSVs.

For the checks reported below I wrote separate scratch scripts:

- **Functions reused.** They import the authors' own functions: `decisions.verdicts`, `is_correct`, `beyond`, `conformal_margin`, `m5_fit` and `m5_interval`.
- **Inputs.** They read `results/dec_alternatives.csv`, `alt_floor.csv`, `dec_intervals.csv` and `features_rddac.csv`.
- **Settings.** They use the same requirement grid, the same per-geometry floors and the same kernel and optimiser settings.
- **Fidelity.** They reproduce the published values, for example M5 within the family at 7/2 floors and the budget figures.

No repository file was changed. These are referee checks. The authors should reproduce them and treat my numbers as indicative.

## 4. Major comments

### Major 1. The model comparison lacks the baselines its conclusions about simulation and machine learning require (Secs 3.3, 5.4, 6.3; Tables 7, 12)

**What is wrong.** The six rules differ in four respects at once:

- (a) the simulation baseline: none, the nominal run, or the upper end of the envelope;
- (b) the level of modelling: alternative-level q95, or a part-level generative model;
- (c) the learner: constant offset, GP, or gradient boosting;
- (d) the uncertainty wrapper: none, a maximum-residual conformal margin, the GP predictive interval, or a nested jackknife.

Only one contrast is controlled: M3 versus M4 isolates the simulation for part-level boosting. There is no GP without the simulation and no data-only baseline at the alternative level.

This matters most within a family. As Sec. 5.5 itself notes, the simulation envelope of a new alternative there equals that of the two calibration alternatives at the same blank-holder force. The simulation is therefore identical for exactly the alternatives that carry most of the information. Within a family the envelope maximum takes only three distinct values, one per force.

**Re-analysis.** Within the family, with requirements, floors and scoring exactly as in decisions.py:

| Rule | δd | δs | right / wrong / trial at abs(d) = 10 |
|---|---|---|---|
| M5 as published (reproduced) | 7 | 2 | 97 / 0 / 3 % |
| GP of q95 without any simulation (same kernel, descriptors, optimiser) | 6 | 1.5 | 99 / 0 / 1 % |
| Same-force sibling rule: mean q95 of the two calibration alternatives at the new design's force (point rule) | 3.5 | 3.5 | 100 / 0 / 0 % |
| Same sibling rule with an M2-type margin (median offset, maximum leave-one-out residual) | 9 | 0.5 | 96 / 0 / 4 % |
| M5 interval centre used as a point rule | 4.5 | 4.5 | 99 / 1 / 0 % |
| M4 interval centre used as a point rule | 5 | 5 | - |

The sibling rule coincides, up to ties, with a two-nearest-neighbour rule in M5's own descriptor scaling. It therefore uses no information M5 does not have. In the pooled scope, the GP without simulation reaches 9.0/1.0 floors against M5's 12/1.

Three conclusions follow.

1. The simulation adds nothing to the GP. Without it the GP is as safe and slightly more decisive.
2. A rule with neither simulation nor learning is twice as decisive as M5, at a safe distance of 3.5 floors.
3. As point predictors M4 (5.0) and M5 (4.5) are close. Most of the published 12-versus-7 gap therefore comes from the uncertainty wrapper, not from the learner or the simulation. M4's margin is the largest of eight nested leave-one-out residuals; its median half-width is 3.0 floors, against 1.0 for M5.

In addition, M3's baseline inherits the oil-to-friction matching that Appendix A.2 calls into question (simulated friction sensitivities 5-630 times the measured ones). M3 minus M4 therefore measures "this matched simulation", not "the simulation".

**Why it matters.** Several statements are not supported within the family, which is where the paper's evidence is strongest:

- the abstract;
- Sec. 5.4: "the best rule combines the simulation envelope with a Gaussian-process correction";
- Sec. 6.3: "Machine learning helps where it corrects a physical model ... halves the decisive distance of the best rule without learning", and "learning carries the production evidence within it";
- Table 12.

The sentence "a flexible model trained on parts adds nothing over it" compares two different things. One is a part-level model whose q95 is generated by resampling pooled in-sample residuals. The other is a model of q95 itself. That is not a test of flexible learners.

**What would fix it.** Run a factorial ablation over (a)-(d), with at least the following variants:

- nearest-neighbour and kriging of q95 without the simulation;
- alternative-level boosting and linear models, with and without the simulation;
- part-level models that target the 95th percentile directly: quantile-loss boosting, distributional regression, or conformalised quantile regression (Romano et al. 2019). The current approach resamples in-sample residuals pooled across alternatives. That understates out-of-sample scatter and assumes equal scatter across alternatives, contrary to Fig. 2.
- one uncertainty wrapper across all learners (e.g., jackknife+ for all), and one learner across all wrappers.

In addition:

- Tune the boosting hyperparameters inside the calibration folds, or show sensitivity to them.
- Encode lubrication the same way in all models. It is one-hot in M3/M4 but an ordinal rank in M5.
- Rewrite Secs 6.1-6.3, the abstract and Table 12 accordingly.

### Major 2. Within the family, the held-out "new design" always has near-replicates in the calibration set (Secs 3.4, 3.5, 5.4, 5.5; Table 8; Fig. 4; Table 12)

**What is wrong.** Each held-out alternative has two calibration siblings that differ from it only in lubrication. Production resolves lubrication in only 53 of 126 contrasts (Table 5), and the siblings share the held-out alternative's simulation envelope.

The fitted GPs exploit exactly this. In 67 of the 126 within-family M5 fits, the length-scale of the blank-holder force sits at its lower bound. That bound is 0.1, i.e. 10 kN, so the three force levels are treated as uncorrelated. The prediction is then effectively an average of the same-force siblings.

The calibration-design analysis has the same structure. budget.py classifies a subset as "brackets" when min(BHF) ≤ BHF_new ≤ max(BHF), with inclusive bounds. Every subset that contains a same-force sibling therefore "brackets". For new designs at 100 or 500 kN, that is the only way to bracket.

**Re-analysis, part (i): leave one force level out.** The three alternatives of one force are held out together, and the six others of the geometry calibrate.

| Rule | δd | δs | empirical coverage of nominal 90 % interval |
|---|---|---|---|
| M1 | 20 | 20 | - |
| M2 | 20 | 7.5 | 54 % |
| M5 | 20 | 7.5 | 53 % |
| GP of q95 without simulation | 20 | 5.5 | 52 % |

When extrapolating to 100 or 500 kN, M5 is safe only at 10 floors and M2 at 12. When interpolating to 300 kN, both are safe at 2.5.

**Re-analysis, part (ii): splitting the "brackets" class of budget.py.** Same code and scoring, k = 1-4:

| k | Calibration subset | cases | M1 δd = δs | M2 δd/δs | M5 δd/δs |
|---|---|---|---|---|---|
| 1 | a same-force sibling | 252 | 4 | 4 / 4 | - |
| 1 | one alternative at another force | 756 | 25 | 15 / 15 | - |
| 2 | contains a same-force sibling | 1638 | 12 | 15 / 2.5 | 15 / 2 |
| 2 | strict bracket (100 and 500 kN for a 300 kN target) | 378 | 12 | 20 / 5 | 20 / 4 |
| 2 | not bracketing | 1512 | 25 | 15 / 12 | 20 / 12 |
| 4 | contains a same-force sibling | 6930 | 15 | 25 / 1.5 | 7.5 / 2.5 |
| 4 | strict bracket without sibling | 630 | 15 | 25 / 4 | 20 / 3.5 |
| 4 | not bracketing | 1260 | 25 | 25 / 12 | 20 / 10 |

- **Share of siblings in "brackets".** 81 %, 86 % and 92 % of the bracketing subsets at k = 2, 3 and 4 contain a same-force sibling.
- **A single sibling.** One same-force sibling (k = 1) gives M1 and M2 a decisive and safe distance of 4 floors, with no wrong verdict at 10 floors. This is already in the authors' budget_design.csv but not in Table 8. It is better than M5 with eight alternatives.
- **Strict interpolation without a sibling.** M5 is decisive only at 20-25 floors and safe at 3.5-4 floors.

**Why it matters.** The within-family results describe interpolation next to near-replicates in a 3 × 3 factorial with one nearly inert factor. This applies to:

- the 7/2 floors of M5;
- "four to five produced alternatives that bracket the new design's process settings make calibrated rules reliable";
- the guidance in Sec. 6.2 and Table 12.

"Choose alternatives that bracket the new design" largely means "produce a variant that production cannot tell apart from the new design". That is a property of this dataset, not a calibration-design principle, and it does not characterise decisions on a genuinely new design.

**What would fix it.**

- Report grouped evaluations (leave one force level out; leave one lubrication pattern out) alongside plain leave-one-out (cf. Roberts et al. 2017).
- Split the calibration-design classes into same-setting sibling, strict interpolation and extrapolation, including k = 1.
- Restate the calibration-design guidance.
- Discuss how the budget depends on the number of design factors that production can resolve.

### Major 3. The GP rule (M5): hyperparameters are not identified on 8 points, the nominal 90 % interval covers 71 % within the family, and the Kennedy-O'Hagan framing is overstated (Secs 2.2, 3.3, 5.4, 5.7, 6.3; A.1)

**What is wrong: specification and fit.** M5 is a scikit-learn GP with this specification:

- kernel: constant × anisotropic squared-exponential + white noise;
- fitting: type-II maximum likelihood with three restarts and normalised targets;
- inputs: two or three descriptors (geometry indicator, force in units of 100 kN, ordinal lubrication rank);
- data: 8 offsets within a family, 17 pooled.

In the 126 within-family fits I find:

- the force length-scale at its lower bound in 53 % (Major 2);
- the noise level at its lower bound (1e-6) in 25 %;
- the lubrication length-scale at its upper bound in 13.5 %;
- a median noise share of the prior variance of 0.3 %, i.e. near-interpolation.

budget.py suppresses the corresponding scikit-learn warnings, with the comment "GP hyperparameters at their bounds for small k".

**What is wrong: coverage.** From dec_intervals.csv, the empirical coverage of the nominal 90 % predictive interval is:

- 71 % within the family;
- 81 % pooled;
- 11 % in transfer.

M5 is therefore over-confident within the family as well, not only "when the alternatives are not exchangeable" (Sec. 6.3). Its safe distance hides this because its misses are short in floor units.

The 75-floor result of the conformalised GP (M6, Sec. 5.7) is a symptom of the same degeneracy. Near-zero predictive standard deviations inflate the standardised leave-one-out residuals, and the largest of eight of them sets the margin.

**What is wrong: framing.** M5 has no calibration parameter, no emulator and no joint posterior. Its target, the parts' q95 minus the envelope maximum, mixes model discrepancy with production scatter. Calling it "Gaussian-process calibration" (keywords, Table 2) "in the manner of a calibration discrepancy (Kennedy and O'Hagan 2001)" overstates the method. The identifiability literature cited in Sec. 2.2 does not apply to it. The ordinal lubrication rank also imposes an order and a spacing that the paper itself questions (Sec. 6.5).

**Why it matters.** The paper's best rule rests on unstable maximum-likelihood solutions on eight points, and its "90 %" interval is not a calibrated probability statement.

**What would fix it.**

- Report the fitted hyperparameters, how often they hit their bounds, and the empirical coverage.
- Use priors on the hyperparameters, either MAP or fully Bayesian.
- Bound the nugget below by, or fix it at, the known sampling variance of the q95 estimates. A block bootstrap gives a standard error of about 0.1 floor (Major 5(e)).
- Consider a linear mean in force (universal kriging), Matérn kernels, and a categorical kernel for lubrication.
- Compare with the GP without the simulation (Major 1).
- Either rename M5 (e.g., "GP bias correction of the envelope"), or implement a genuine Kennedy-O'Hagan calibration. That would treat the friction coefficient of each lubrication pattern as the calibration parameter and the tabulated DDACS runs as the simulator. It would also address the oil-to-friction mapping that the paper calls into question (Sec. 6.5, A.2).

### Major 4. The "split-conformal 90 %" margins are not 90 % conformal intervals for 1-17 calibration alternatives, and the M3/M4 margins are jackknife rather than jackknife+ (Table 2; Secs 3.3, 5.5, 5.7, 6.5; A.1)

**What is wrong: attainable coverage.** `conformal_margin` returns the ⌈(n+1)·0.9⌉-th smallest absolute residual, or the largest when that rank exceeds n.

- For n ≤ 8 the split-conformal 90 % quantile is infinite.
- Even with a fixed offset, the maximum of n residuals covers a new exchangeable residual with probability n/(n+1). For n = 8 that is 0.889.

**What is wrong: no split.** The offset is the median of the same residuals, so the calibration scores are not exchangeable with the test score. The only distribution-free statement is that the interval contains [r(1), r(n)]. That guarantees (n-1)/(n+1): 0.78 for n = 8 and 0.89 for n = 17, below 90 % in both scopes.

**Consequences in the calibration budget.** They are severe:

- At k = 1 the margin is zero, so M2 is a point rule.
- At k = 2 the M2 interval is the range of the two offsets. It covers a new exchangeable offset with probability exactly 1/3.
- At k = 3 the coverage is at least 1/2.

The robustness rows "conformal level 0.80 / 0.95" (Table 10) are uninformative within the family by construction: the margin is the maximum at all three levels.

**M3/M4.** Their margins come from a nested leave-one-out, i.e. the jackknife. The jackknife has no coverage guarantee; jackknife+ has (Barber et al. 2021, cited in the manuscript).

**Why it matters.** Conformal versus model-based uncertainty is one of the paper's themes (Sec. 6.3). Table 2 and Table 12 ("Two or three produced alternatives: M2 envelope with conformal margin") present intervals with nominal coverage between 1/3 and 3/4 as 90 % conformal intervals.

**What would fix it.**

- State the attainable levels.
- Use a genuine split (offset estimated on alternatives not used for the scores), full conformal, jackknife+ or CV+.
- Consider pooling conformity scores across characteristics in floor units. The floor normalisation makes them comparable and gives 7 × 8 = 56 scores within a family.
- Consider Mondrian conformal by characteristic.
- For transfer, use weighted conformal prediction under covariate shift (Tibshirani et al. 2019).
- Report empirical coverage for every interval rule and scope. My computation from dec_intervals.csv:

| Rule | within | pooled | transfer |
|---|---|---|---|
| M2 | 87 % | 94 % | 41 % |
| M3 | 93 % | 94 % | 38 % |
| M4 | 86 % | 91 % | 6 % |

### Major 5. The two distances: closed form, grid inflation, pooled sides, conditioning on the unknown truth (Secs 3.2, 3.4, 3.6, 6.2; Table 1)

**(a) Closed form and relation to existing measures.** Take a case with interval [lo, hi], true q95 and floor F, and define u = (hi - q95)/F and v = (q95 - lo)/F.

- **Decisive distance.** κ(δ) = ½[P(u ≤ δ) + P(v < δ)] is the distribution function of an equal mixture of u and v. δd is therefore its 95th percentile.
- **Safe distance.** Likewise, δs is the 95th percentile of the equal mixture of the signed exclusion distances (lo - q95)/F and (q95 - hi)/F.
- **Point rules.** For a point rule, δd = δs is exactly the 90th percentile of |prediction error|/F. For M1 within the family this is 12.4 floors; the grid reports 15.

The distances are therefore well defined, but they are standard interval-error quantiles expressed in a new unit. They are close to several established measures:

- coverage-and-width evaluation and the interval score (Gneiting and Raftery 2007);
- operating-characteristic curves and indifference zones in acceptance sampling and selection (Bechhofer 1954);
- guard-banded conformity assessment with specific and global risks (JCGM 106, which is cited but not used);
- risk-coverage curves of selective prediction (Chow 1970; Geifman and El-Yaniv 2017);
- validation metrics for model-based design (Ferson et al. 2008; Liu et al. 2011).

Table 1 and Sec. 2 should position the distances against these and say what the floor normalisation adds.

**(b) Grid.** No grid is needed, because every case contributes exact thresholds. The coarse grid (..., 40, 50, 75, 100, 150, ...) combined with "first grid point beyond" inflates the results. Grid-free values computed from dec_intervals.csv:

| Rule and scope | Grid-free | Reported |
|---|---|---|
| M0 | 105 | 150 (abstract, Sec. 5.4, Table 12, conclusions) |
| M2, transfer, δd | 54 | 75 |
| M4, pooled, δd | 20 | 25 |
| M1, within | 12.4 | 15 |
| M5, within, δd / δs | 6.6 / 1.75 | 7 / 2 |
| M5, pooled, δd / δs | 10.4 / 0.92 | 12 / 1 |

**(c) The two sides are pooled.** Each |d| pools d = +δ (adequate designs) and d = -δ (inadequate designs) with equal weight. Consequences:

- ω(δ) ≤ 0.05 permits up to 10 % false accepts among inadequate designs when there are no false rejects.
- The cost bounds of Sec. 3.4 hold only for this symmetric population.

Since cFA and cFR differ, report one-sided false-accept and false-reject distances.

**(d) Truth versus prediction.** d is measured from the true q95, which is unknown at the design stage. Yet:

- Sec. 3.4 calls δd "the smallest margin between prediction and requirement that the design stage can resolve".
- Step 6 (Sec. 3.6) and Sec. 6.2 ("A design-stage verdict should state its distance from the requirement in floors, so that it can be compared with the rule's decisive and safe distances") compare an observable margin with a quantity defined on the unobservable one.

Either give the operational quantity, namely error rates as a function of |R - prediction|/F (a reliability diagram), or present the distances explicitly as operating characteristics.

**(e) Unit and reference.**

- **Centres versus tail quantile.** The floor resolves batch *centres*, whereas the requirement concerns the 95th percentile of a whole series. The paper should argue why a centre resolution is the right unit for a tail-quantile requirement.
- **Dependence on constants.** Floors change by up to about 2.8× across reasonable batch sizes, quantiles and centre statistics (sens_floor.csv). Absolute distances are therefore conditional on these constants.
- **Uncertainty of the reference.** The "true" q95 is itself an estimate. A block bootstrap over the 50-part batches gives:
  - a median standard error of 0.11 floor (interquartile range 0.07-0.15, maximum 0.34);
  - a median 95 % interval width of 0.39 floor (maximum 1.2).

  This is the order of the reported safe distances (0-2 floors). The scoring should propagate it.

**(f) Physically impossible requirements.** For non-negative characteristics, R = q95 + dF becomes negative within the scored range:

- dome: from d ≈ -7 to -17 (median -13);
- arm angle: -3 to -53;
- waviness: -15 to -40.

The dome's 15-floor decisive distance is partly computed on such requirements. Truncate the grid at R ≥ 0, or score these cases separately.

### Major 6. The bootstrap intervals understate uncertainty and do not support the inferences drawn from them (Secs 3.4, 5.4; Table A1; A.1)

**What is wrong: what is resampled.** `distance_table` resamples the 18 held-out alternatives with replacement. It does not stratify by family and does not refit any rule.

- The intervals therefore only show which test alternatives were drawn, conditional on fixed fits.
- They ignore calibration-set variability, which dominates with eight points.
- In transfer only two calibrations exist (one per direction), so the main source of variation is missing altogether.

**What is wrong: grid-valued intervals.** The intervals are grid-valued, with lower/higher percentile rounding. Degenerate intervals (transfer M1 40-40, M2 75-75, M3 50-50, M5 40-40) reflect gaps in the grid, not precision.

**What is wrong: knife-edge thresholds.** With 252 verdicts per |d| within the family:

- M5's κ is 0.948 at 6.5 floors and 0.952 at 7;
- M5's 1 - ω is 0.948 at 1.5 floors and 0.956 at 2.

Each threshold hinges on a single verdict. Safe distances are driven by the few largest misses. These are extreme-type functionals, for which the percentile bootstrap is least reliable.

**What is wrong: the overlap claim.** p. 13 states that the Table A1 intervals "do not overlap between M5, M4, M1 and M2". This is inaccurate: M4 (10-12) and M1 (12-20) share 12. In any case, non-overlap of marginal intervals is not the right test for rules scored on the same cases.

**Perspective.** I ran a paired, family-stratified bootstrap of grid-free distances, still conditional on the fits. It does support the ordering M5 < M4 < M1 < M2 within the family (M4 - M5: 4.2 floors, 95 % interval 2.4-5.2). I am therefore not arguing that the ranking among the six rules is an artefact; the problem lies in Majors 1 and 2. But the reported intervals understate uncertainty, and the transfer intervals carry no information.

**What would fix it.**

- Compute grid-free distances.
- Use a paired, stratified (cluster) bootstrap that refits the rules, or repeated grouped subsampling. Refitting is cheap for M1, M2 and M5; a subsample suffices for M3/M4.
- Report κ and ω curves with confidence bands, one-sided.
- Report the number of verdicts behind each threshold.
- State explicitly that transfer rests on two instances.

### Major 7. Transfer and the applicability guard: two instances, a failure by construction, and a misreported post-guard error (Secs 3.5, 5.4, 5.5; abstract; Table 12)

**What is wrong.**

1. **Two instances.** "Across geometries" means two calibrations.
2. **M4 fails by construction.** With one geometry in training, the geometry indicator is constant and the trees cannot use it. A GP of q95 without simulation fails the same way (150/150 floors). This follows from the setup; it is not a finding about machine learning.
3. **The novelty guard is close to trivial.** It fires for 114 of 126 transfer cases (90.5 %).
   - For five of the seven characteristics it fires for every alternative, because the simulated values of the two geometries do not overlap. It then reduces to the family guard, which in this design is a tautology.
   - The 12 cases that pass come from two characteristics (mid-side draw-in and waviness) and six alternatives.
4. **The post-guard error rate is misreported.** Sec. 5.5 states: "in the remaining cases M2 is never wrong at 10 floors and M5 in 2.4 %". The 2.4 % is the share of all 252 transfer verdicts at |d| = 10, most of which the guard sends to trial. Among the 24 verdicts the guard lets through, the counts are:

| Rule | wrong (of 24) | trial (of 24) |
|---|---|---|
| M5 | 6 (25 %) | 0 |
| M1 | 4 | 0 |
| M0 | 3 | 0 |
| M3 | 3 | 1 |
| M4 | 1 | 5 |
| M2 | 0 | 12 |

**Why it matters.** Three statements rest on 12 cases from two characteristics:

- the abstract: "the simulation carries a decision into a new family, while an applicability guard sends it to trial";
- the conclusions;
- Table 12: "New geometry: M2 with the applicability guard".

The GP rule's error rate after the guard is ten times the reported one.

**What would fix it.**

- Correct the statement and report counts.
- Evaluate guards that use the descriptor space or model uncertainty: distance to the calibration designs, GP predictive variance, or weighted conformal prediction.
- Use the 264 DDACS geometry-variation simulations to turn transfer into a design-space question: learn the geometry dependence of the discrepancy from simulation, or at least test the guard against those runs.
- State that the transfer conclusions rest on two instances.

### Major 8. The PA12 case does not test the claims it is used to support (Secs 5.8, 6.4; Table 11; abstract)

**What is wrong.**

- **No simulation.** M2 and M5 are data-only rules here, and there is no transfer and no guard.
- **Not "applied unchanged".** The alternatives are 30° bins of a continuous orientation, with six or seven orientations each. A batch is a class within one build, so batches mix orientations. The procedure is therefore not "applied unchanged" (Sec. 6.4).
- **Floor estimate.** The floor is the 95 % quantile of only 18 build-centre differences (three per class), reported without an interval.
- **Noisy reference.** The true q95 of a class comes from 18-21 specimens. For a normal sample of 18, the empirical 95th percentile has a standard deviation of about 0.40 SD and a bias of about -0.22 SD (my simulation). Since the floor is close to the part SD here (Table 11), that is roughly 0.4 floor of noise in the reference, against reported safe distances of 0.5-1 floor.
- **Nearly trivial problem.** Only 18 of 120 class pairs are resolvable. M1 from a single class already decides at 2 floors.

**Why it matters.** This case is the only evidence for the generality claimed in Sec. 6.4 and in the abstract.

**What would fix it.** Replace or complement it with a case that has a design-stage predictor (simulation or surrogate) and more than one family. Otherwise, present PA12 as a sanity check, give intervals for its floors and distances, and remove the generality claim.

### Major 9. Dataset-specific numbers are presented as guidance, and the rules were developed on the evaluation data (abstract; Secs 4.4, 6.1-6.2, 7; Table 12)

**What is wrong: dataset-specific guidance.** The abstract, Table 12 and the conclusions present the following as guidance:

- distances of 150, 25, 7 and 2 floors;
- "four to five" produced alternatives;
- "nine in ten" decisions to trial.

These come from one tool set with 18 alternatives. They depend on the grid (Major 5(b)), on near-replicates (Major 2) and on the floor constants (Major 5(e)).

**What is wrong: development on the evaluation data.** The rules were developed on the same 18 alternatives, with no untouched hold-out.

- The public repository history shows M5 being added after the floor-based scoring and M3/M4 were already in place.
- robustness.py introduces M6 as "a candidate for a rule that is both safe and decisive".

This is normal in exploratory work, but the "best rule" then carries selection optimism (Cawley and Talbot 2010). Sec. 4.4 states that "All constants were fixed before the analysis". That does not cover the choice of rules, descriptors, kernels or baselines.

**What would fix it.**

- Present Table 12 as observations on this dataset.
- List all rule variants tried.
- If possible, test rules fixed in advance on a second dataset as a confirmatory step.

## 5. Minor comments

1. **p. 1-2, abstract and Sec. 1.** The unit of evidence for comparing rules is 18 alternatives (126 alternative-characteristic cases per scope, and two transfer calibrations), not 9,000 parts. Say so. "for the first time on open data" (p. 2) should be softened or supported.
2. **p. 6, Sec. 3.2, eq. (2).** The floor pools 45 non-independent pairs from 10 batches per alternative.
   - Scoring uses per-geometry floors (A.1). These differ by up to 2.4× (dome: 0.0034 vs 0.0082 mm) and have no intervals in Table 4.
   - Eq. (4) should carry the geometry index, i.e. the floor of characteristic c on geometry g.
3. **p. 6, eq. (3) and Table 5.** The effect-to-scatter ratio and the minimum resolvable change concern alternative *centres*, whereas verdicts concern q95. A change below the centre's minimum resolvable change can still move q95 through the scatter. The last row of Table 12 ("do not iterate on it") needs qualification.
4. **p. 7, Table 2.** Relabel and clarify:
   - "split-conformal, 90 %" should read "maximum-residual margin around a median offset (nominal coverage at most n/(n+1))";
   - "nested leave-one-out, 90 %" should read "jackknife";
   - say that the resampled part residuals of M3/M4 are in-sample residuals.
5. **p. 7, Sec. 3.3.** M1 uses the nominal run, whereas M2 and M5 use the envelope maximum.
   - The baseline alone matters: used as a point rule, M2's centre reaches 8.5 floors against M1's 15. M1 versus M2/M5 therefore conflates the baseline with the offset model.
   - Justify treating the full DDACS ranges (0.95-1.00 mm; friction 0.05-0.15) as "plausible incoming conditions".
6. **p. 7-8, Sec. 3.4.** State the following:
   - each |d| pools both signs with equal weight;
   - d = 0 contributes one side only;
   - how many verdicts enter each |d| (252 within the family);
   - "smallest δ beyond which" is evaluated at grid points only.

   On the Currie analogy: Currie separates a critical (decision) level from a detection limit, with separate α and β, whereas δd pools both error types.
7. **p. 8, cost paragraph of Sec. 3.4.** The bounds hold per |d| for a population with equal numbers of adequate and inadequate designs. In a real population with unequal shares, a side-specific error rate of up to 10 % is compatible with them.
8. **p. 8, Sec. 3.5 and Table 8 footnote.** Define "bracket" exactly: the bounds are inclusive, and a same-setting sibling counts as bracketing.
9. **p. 9, Sec. 4.2, and leakage generally.** I found no leakage of the held-out alternative's production data into any rule. I checked `decide()`, `rule_intervals()`, `m3_q95()`, `m3_nested()` and `m5_fit()`. For a strict leave-one-out, two residual points should nevertheless be noted:
   - The nominal thickness of 0.98 mm was set with reference to the measured thickness of all parts, held-out ones included (code comment: median 0.985-0.99 mm).
   - The per-geometry floor that places a held-out alternative's requirements includes that alternative's own batches. Recomputing the floors without the target would show invariance.
10. **p. 10, Sec. 4.4.** The repository history shows that the requirement grid was extended from 100 to 500 floors after the first runs (benign) and that the rules were added one after another. Describe this sequence.
11. **p. 13, Sec. 5.3.** "within one geometry the offset varies by 10.5 to 38 floors ..., so no constant correction can bring a decision rule below that". A constant correction centred in the range leaves errors of about half the range (M1's grid-free δd within the family is 12.4), so rephrase. Table 6's smallest spread prints as 10 while the text says 10.5.
12. **p. 14 and p. 24, Table 7 and Table A2.** The per-characteristic distances rest on 36 verdicts per |d|: one wrong verdict is 2.8 %, two are 5.6 %. Give intervals or counts. Add the number of cases to the Table 7 footnote.
13. **p. 16, Fig. 4 and Table 8.** The subset-averaged distances hide the spread over subsets, and a design team chooses only one subset. Show the distribution, e.g. of the per-subset wrong share at 10 floors. Include k = 1 in Table 8.
14. **p. 15 and p. 17, Sec. 5.6 and Table 9.** The 162 decisions are 9 requirement classes × 18 alternatives.
    - 70 of them (43 %) lie within 10 floors of the limit.
    - Several classes are met or failed by every alternative: wall angle f/m and c (0/18), flatness K and L (18/18). Every alternative lies at least 31 floors inside the flatness class L limit.

    Stratify the results by margin and add the nearest-neighbour baseline.
15. **p. 17, Table 10.** The conformal-level rows are uninformative within the family by construction (Major 4). The temperature correction uses a slope pooled over all alternatives, including the held-out one. That is acceptable for a data variant, but say so.
16. **p. 17, Sec. 5.7.** Read the M6 result (75 floors) in light of the GP degeneracy (Major 3), not as an inherent limit of conformalised GPs.
17. **p. 20, Sec. 6.3.** "the Gaussian-process interval is decisive but over-confident when the alternatives are not exchangeable": its coverage within the family is 71 %.
18. **p. 20-21, Sec. 6.5.** Add to the threats to validity:
    - the near-replicate siblings;
    - the two-instance transfer;
    - the reference uncertainty of q95;
    - the attainable conformal levels.

    On "its guarantee assumes exchangeable alternatives": the margin falls below 90 % even under exchangeability (Major 4).
19. **p. 22-23, A.1.**
    - Report the fitted GP hyperparameters and mention the suppressed warnings.
    - For M3/M4, state that the resampled residuals are in-sample boosting residuals pooled across the calibration alternatives.
    - For the distance intervals, state that there is no stratification and no refitting.
    - guard.py uses 200 resamples and gives 6.5-8.5 for M5 within the family, against 6.5-8 in Table A1. Harmonise, and report the Monte Carlo error.
20. **p. 15, Fig. 3.** Label the x-axis transformation (symmetric log), add M1 and M3, and give the number of verdicts per point.
21. **p. 18, Table 11.** Add intervals for the floors and distances, and describe the class binning and the batch definition.
22. **p. 22, code availability.** Before acceptance, archive the code under a descriptive repository name with a DOI. Include the scripts for any added baselines and grouped evaluations.

## 6. Recommendation

**Major revision.**

The question is important for design research, the data and code are open and reproducible, and the floor-referenced scoring could become a useful tool for qualifying design-stage decisions.

However, the central machine-learning and uncertainty-quantification conclusions do not survive checks with the authors' own code:

- Within a family, two simple rules do as well as or better than the recommended GP correction: a GP without the simulation, and a nearest-sibling rule that uses neither the simulation nor learning.
- The GP's success depends on near-replicate siblings and disappears when a whole process setting is held out.
- The "bracketing" effect is largely a sibling effect.
- Across geometries, the post-guard error of the GP rule is 25 %, not 2.4 %.

In addition:

- the conformal margins are not 90 % intervals;
- the GP is poorly identified and over-confident;
- the distances need grid-free estimation, one-sided reporting, inference with refitting, and positioning against existing decision-oriented metrics.

All of this can be addressed with the existing data. But the conclusions will change materially, and so will much of the abstract, Section 6 and Table 12. The general claims must either be demonstrated on a second dataset with a design-stage predictor, or narrowed. Without that, the manuscript would remain a single-dataset case study outside RED's scope. With it, it could be a valuable contribution, and I would be glad to review a revised version.

## References suggested in this report (not in the manuscript)

- Bechhofer RE (1954) A single-sample multiple decision procedure for ranking means of normal populations with known variances. Annals of Mathematical Statistics 25(1):16-39
- Cawley GC, Talbot NLC (2010) On over-fitting in model selection and subsequent selection bias in performance evaluation. Journal of Machine Learning Research 11:2079-2107
- Chow CK (1970) On optimum recognition error and reject tradeoff. IEEE Transactions on Information Theory 16(1):41-46
- Ferson S, Oberkampf WL, Ginzburg L (2008) Model validation and predictive capability for the thermal challenge problem. Computer Methods in Applied Mechanics and Engineering 197(29-32):2408-2430
- Geifman Y, El-Yaniv R (2017) Selective classification for deep neural networks. Advances in Neural Information Processing Systems 30
- Gneiting T, Raftery AE (2007) Strictly proper scoring rules, prediction, and estimation. Journal of the American Statistical Association 102(477):359-378
- Liu Y, Chen W, Arendt P, Huang H-Z (2011) Toward a better understanding of model validation metrics. Journal of Mechanical Design 133(7):071005
- Roberts DR, Bahn V, Ciuti S, et al. (2017) Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. Ecography 40(8):913-929
- Romano Y, Patterson E, Candès EJ (2019) Conformalized quantile regression. Advances in Neural Information Processing Systems 32
- Tibshirani RJ, Barber RF, Candès EJ, Ramdas A (2019) Conformal prediction under covariate shift. Advances in Neural Information Processing Systems 32
