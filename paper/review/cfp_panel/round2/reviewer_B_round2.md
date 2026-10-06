# Referee report, second round: Reviewer B

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal and collection:** Research in Engineering Design (Springer), special collection "AI in Design for Manufacturing"
**Round:** second (revised version)
**Focus:** AI for design for manufacturing: data-driven manufacturability prediction, machine learning for process design and design for additive manufacturing, uncertainty quantification and trustworthy AI in engineering design

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The revision is substantial and responsive: the claims about learning and simulation are now conditioned on the data regime and the simulator, the headline on the evidence relation is replaced by a decomposition, the learned models have a fair small-data specification (a between-run GP noise floor that lifts coverage with a produced sibling from 71–72 % to 85–86 %, jackknife+ intervals and a scaled multi-fidelity rule, M1s), the pooled scopes and M6 are reported, the refit bootstrap preserves the evidence relation, and step 6 is specified as a guard band, evaluated and worked through for one decision. The paper is shorter (the main text ends on p. 23, with six tables and four figures) and now presents itself, rightly, as an evaluation standard for AI-based DFM support rather than as evidence on the value of machine learning in DFM. I re-checked all of Table 4 and Table A2, the worked example and the numbers quoted in Sections 5.1–5.9 against the released code and result files, and they are correct. What remains concerns mainly material that is new in this round: the guard band depends on an unstated requirement prior, several numbers that carry RQ3 are no longer shown in the paper or traceably referenced, and the abstract and conclusions still overstate in a few places. My overall view is positive, and I recommend minor revision.

## 2. Assessment

- **Originality: adequate.** The production-referenced unit, the split by evidence relation and now the design-stage guard band are new in this setting, but they combine established ideas: operating characteristics, guard-banded conformity decisions, selective prediction and conformal margins.
- **Significance for design research: adequate.** The distances now give margins, testing strategy, overlapped development and set-based design a production-referenced measure (Sect. 6.4). The evidence, however, is still one process, two geometries and one simulator.
- **Significance for the collection (AI in DFM): adequate.** The paper now offers what the collection needs: an evaluation standard for AI-based manufacturability support, with a production-record baseline, abstention and a guard band. The AI evaluated is still classical small-data regression, and the guidance for other AI tools (Sect. 6.5) is brief.
- **Technical soundness: adequate.** The specification problems of the first round are fixed; I checked in the code that the new GP noise floor uses calibration data only. However, the new guard band depends on an unstated prior (N1), and the refit bootstrap and the jackknife+ guarantee are described inaccurately (N4, N5).
- **Evidence supports the claims: weak → adequate.** The claims are now conditioned on the data regime and the simulator, and every number I checked is right. The abstract and conclusions still overreach in places (N3), and several figures that carry RQ3 are no longer shown in the paper (N2).
- **Clarity, organisation and length: adequate.** The paper is shorter and better organised, with a worked example, a notation table and physical anchors. It is still very dense: some condensed passages are hard to parse (l. 807–813, 841–845), and two key terms are used in two senses (N8).
- **Positioning and references: adequate.** The positioning against design theory, V&V and conformity assessment is much stronger (Sects. 2.2–2.5). The AI-for-DFM side remains thin: nothing is cited on how LLM- or VLM-based manufacturability checks have been evaluated, although Sect. 6.5 proposes to score them.
- **Fit to RED: adequate.** This is clearly a methodological contribution to design decision-making, now argued strand by strand against the design literature (Sect. 6.4). Its broad applicability is set out through prerequisites and a process mapping (Table 6) rather than shown.

## 3. First-round major comments

### B1. The conclusions about learning depend on a very small, factorial data regime

**Status: largely resolved.**

*Evidence.*

- **Data regime.** It is stated in the abstract (l. 36) and beside each RQ3 statement (l. 903–904, 938; "small-data regime", l. 1036).
- **New-variant relation.** It is stratified, as the editor decided (l. 628–632). With near-replicate siblings (58 cases) the nearest produced setting (NN) decides at 0.85 floors. With two resolvable siblings (34 cases) NN needs 4.9 floors and M5 9.7. I reproduced these from `panel_sibling_strata.csv`.
- **Headline.** It is replaced by the decomposition (l. 641–644, 671; reproduced from `panel_decomposition.csv`). The relation explains 69 % of the variation over all relations, while within a family the rule explains 68 %.
- **Inductive biases.** The explanation is given (l. 729–732). In the median new-setting fit the force length scale indeed sits at its 10 kN bound (`dec_gp.csv`).
- **Interval centres.** They are reported as point predictors (l. 721–723).

*What remains.* Wording only: N3(c), N7(b) and N8.

### B2. The conclusions about simulation concern one low-fidelity simulator, used additively, and two transfers

**Status: largely resolved.**

*Evidence.*

- **The scaled rule M1s** is added (l. 311–313). Its decisive distances of 4.9, 19 and 122 floors match the figures I computed in the first round.
- **The fitted trend** is reported, to the paper's credit, to falsely accept failing alternatives up to 164 floors from the limit when extrapolated (l. 615–617).
- **"Adds nothing"** now refers to the additive use only (l. 678).
- **The simulator's limitations** are stated:
  - the stroke speed is not represented, and the material model is not documented (l. 485–487);
  - the offset, the exaggerated force effect and the wrong arm sign (l. 587–590);
  - low fidelity, used through offsets and one scale (l. 937);
  - a large and partly sign-inconsistent bias (l. 1037).
- **Surrogates** are stated to inherit the simulator's distance (l. 938–939).
- **The new family** is presented as two transfers (l. 33; l. 1011–1013; Table 5).

*What remains.*

- The abstract and the Conclusions contradict the M1s result (N3a).
- An interval version of M1s would complete my request (point 10, optional).

### B3. The learned models lacked a fair, current small-data specification

**Status: resolved, subject to N5 and N6.**

*Evidence.*

- **(a) GP noise floor.** The GP noise is now bounded by the variance between series (l. 316–320). Coverage with a sibling is 85–86 % (l. 724–726).
- **(b) Jackknife+.** M3 and M3n now use jackknife+ intervals (l. 323–324).
- **(c) Multi-task GP.** The explanation of why a multi-task model is not used (l. 933–936) is acceptable for the new family.
- **(d) Risk control.** Conformal risk control and covariate-shift conformal prediction are positioned (l. 155–158). The 1/(n+1) consequence for the calibration budget (l. 333–335) is a useful general rule for the collection.

*What remains.*

- The jackknife+ guarantee is overstated (N5).
- The noise floor needs a fuller description (N6).
- The multi-task statement needs a wording fix (point 5).

### B4. Computed results were not reported, and exploratory comparisons were not separated

**Status: resolved.**

*Evidence.*

- **Pooled scopes and M6.** They are in Table 4 for every relation and are discussed (l. 636–640, 933–936). I re-checked them against `dec_resolution.csv` and `rob_decisions.csv`.
- **Development record.** Sect. 4.5 is corrected, and the comparison of rules is declared exploratory (l. 532–541).
- **Findings.** Sect. 6.1 separates findings that follow from the definitions from observations (l. 866–906; but see N7a).
- **Held-back confirmation.** The reason it was not possible is accepted.

*Caveat.* Part of the supporting evidence is now outside the paper (N2).

### B5. The precision of the main comparisons was overstated, and the refit bootstrap mixed relations

**Status: largely resolved.**

*Evidence.*

- **Refit bootstrap.** It now resamples whole lubrication patterns within each geometry, as I suggested, and every case keeps its relation (l. 527–529, 1087–1088). The refit intervals of the decisive distances are in Table A2; I verified them against `rob_refit.csv`.
- **Ranking.** NN is more decisive than M5 and M5n in every resample, with a sibling and for a new setting (l. 857–860; share 1.00 in `rob_refit_paired.csv`). The main ranking is therefore robust.
- **Small differences** of a few floors are no longer interpreted.

*What remains.*

- What the new bootstrap measures needs describing (N4).
- One comparison has no refit interval (N4).
- The paired refit intervals are not in the paper (N2).

### B6. Trust, abstention and decision support were treated only as population-level statistics

**Status: partly resolved.**

*Evidence.*

- **Fig. 4** shows the share of correct verdicts by observable margin for each relation.
- **Step 6** is specified (l. 448–456) and evaluated (l. 802–816).
- **Worked example** (l. 817–827). I reproduced every number of it from `dec_intervals.csv`.
- **Human–AI decision-making.** Expert-versus-trial deferral and appropriate reliance are raised (l. 943–945) and positioned (l. 176–179).
- **Wording.** "Reliable" replaces "trusted".

*What remains.*

- I asked for the requirement prior to be stated *and its influence shown*. It is stated only as a range, and its influence is large (N1).
- The transparency claim (N9) needs tightening.
- The designer-study hypotheses (point 4) also need tightening.

### B7. How developers and evaluators of AI-based DFM tools could use the framework

**Status: partly resolved.**

*Evidence.*

- **Sect. 6.5 and Table 6** give:
  - the prerequisites;
  - a black-box formulation;
  - relations for continuous novelty;
  - a minimal report;
  - the PA12 attempt as a negative result.
- **Keywords and Sect. 2.1** are updated.
- **Protocol dependence** is handled by a reference protocol and reported variance components (l. 275–287; Table 3).

*What remains.*

- **Length.** Sect. 6.5 is about two-thirds of a page, against the "about two pages" of R5b.
- **Black-box formulation.** It is a single sentence (l. 990–995) and leaves open exactly the cases this collection cares about (point 1).
- **Minimal report.** It would be more usable as a checklist (point 2), and the paper does not yet meet it itself (N2).
- **References.** LLM-based checks are proposed for scoring without any reference to how such checks have been evaluated (point 3).

## 4. New issues arising from the revision

### Major (both can be fixed from the stored results, without new data or modelling)

**N1. The guard band of step 6 depends on an unstated requirement prior and on a 20-floor cap**
(Sect. 3.6, l. 448–451; Sect. 5.7, l. 802–816; Fig. 4; worked example, l. 822–824)

*The problem.* The guard band g is defined as the smallest observable margin beyond which at least 95 % of the decided verdicts were correct, "for requirements within 20 floors of the truth".

- The code (`guard_band` in `panel.py`, following `reliability` in `decisions.py`) weights the points of the requirement grid equally.
- That grid is 0, ±0.5, …, ±10, ±12, ±15 and ±20 floors, so 41 of its 47 points, 87 % of the weight, lie within ±10 floors.
- The share of correct verdicts at a given observed margin depends on this base rate. This is unavoidable for any reliability-given-observation statement, but it must be explicit.

I recomputed g from `dec_intervals.csv` with the paper's own logic. The first column below reproduces the paper's values.

| Relation | Rule | Paper's grid, ±20 | Uniform, ±20 | Uniform, ±10 | Uniform, ±50 |
|---|---|---|---|---|---|
| Sibling | NN | 0.25 | 0 | 0.25 | 0 |
| Interpolated setting | NN | 2.0 | 0.5 | 2.25 | 0 |
| Interpolated setting | M5 | 0.5 | 0 | 1.25 | 0 |
| Extrapolated setting | NN | 7.0 | 3.5 | 8.75 | 0 |
| Extrapolated setting | M2 | 23.25* | 5.75 | 24.0* | 0 |
| Extrapolated setting | M5 | 23.0* | 5.0 | 23.75* | 0 |
| New family | M2 | 28.5* | 27.25* | 28.5* | 3.75 |
| New family | M5 | 33.25* | 32.0* | 33.5* | 11.75 |

Guard bands in floors. \*Beyond the paper's 20-floor cap on g, so the paper reports these rules as unqualified. NN and M5n never qualify for a new family.

*Why it matters.* The guard band is what a designer sees with each verdict, and the abstract presents the procedure as a contribution.

- **Uniform prior.** Over the same ±20 floors, the bands for NN shrink two- to four-fold, and M2 and M5 become qualified for extrapolated settings.
- **Wider prior.** M2 decides new-family designs with a band of 3.75 floors.
- **The new-family conclusion.** "For a new family no guard band up to 20 floors reaches 95 %, so every design goes to trial" (l. 812–813) therefore describes the prior and the cap rather than the rules. It also sits uneasily with M2's safe distance of 16 floors: M2 errs on at most 5 % of verdicts beyond 16 floors, yet step 6 refuses all its verdicts, because the prior puts most of the weight where M2 errs.
- **Unqualified rules.** The text does not say that M2 and M5 are unqualified for extrapolated settings.
- **Worked example.** Its verdict would not change, but its stated guard band (2.0 floors) would.

*What would fix it.*

- State the prior exactly in Sect. 3.6 and in the caption of Fig. 4, and say why it represents the requirements a team faces.
- Report g, and the step-6 distances and trial rates, under at least one alternative prior: for example, uniform within ±20 floors, or one anchored on the capability-based requirement positions of Sect. 5.8. Better still, let step 1 ask the team for its own distribution of requirement-to-capability margins.
- Alternatively, define g without a prior. One option is the smallest widening for which the widened rule's safe distance is zero, so that at most 5 % of its verdicts are wrong at every true margin. The prior then affects only the trial rate.
- Name the unqualified rules for each relation, qualify l. 812–813, and remove or justify the 20-floor cap.
- In Fig. 4, show the interpolation and extrapolation curves from which the reported bands come; panel (b) pools them. Say that the share is taken over verdicts whose margin is at least g.

**N2. Much of the evidence behind RQ3 is no longer in the paper, which does not meet its own minimal report**
(Appendix A, l. 1050–1053; Sect. 6.5, l. 995–998; Code availability, l. 1133–1136)

*The problem.* The supplementary material and Tables A3 (coverage) and A7 (GP diagnostics) of the first version were removed rather than moved to Electronic Supplementary Material.

- The paper names no result files; the response names them.
- The archive is "deposited on Zenodo [DOI pending]", although the editor asked for the DOI at resubmission.

Against its own minimal report (l. 995–998), the paper gives the following:

- **Refit intervals:** only for the decisive distances of four rules (Table A2).
- **One-sided distances:** only for the false-accept side.
- **Coverage of the interval rules:** only as ranges in the text (l. 724–729), with no half-widths.
- **Guard bands:** only for NN.
- **Guard performance:** not at all, only "refuses many cases that would have been decided correctly" (l. 815–816). According to `dec_guard.csv`, the range guard's refusals for a new setting would have been right, at 10 floors, in 96 % of NN's verdicts and 72 % of M5's.
- **GP diagnostics:** not given. The noise sits at its new lower bound in 97 % (M5) and 99 % (M5n) of the sibling fits, and in all new-setting and new-family fits (`dec_gp.csv`). This matters for interpreting the intervals (N6).
- **Paired refit comparisons:** summarised only as "all 200 resamples" (l. 859–860).

*Why it matters.* The paper's contribution is an evaluation and reporting standard, so readers must be able to see, and check, the numbers on which RQ3 rests. With the DOI pending, they currently cannot.

*What would fix it.*

- **One appendix or ESM table** giving, for each interval rule and relation:
  - coverage and median half-width;
  - the centre's decisive distance;
  - the guard band g;
  - the step-6 decisive and safe distances;
  - the trial share at 10 floors.

  The table note can give the share of GP fits at the noise bound.
- **Guard performance** in one or two sentences.
- **A short list** mapping each remaining number in the text to its result file.
- **The archive**, deposited with its DOI cited before acceptance.

### Minor

**N3. The headline statements still overreach in five places**
(abstract, l. 32–38; Sect. 5.4, l. 672; Table 5; Conclusions, l. 1033–1038)

- **(a) The simulation within a family.** The abstract says "the simulation, as used, helped only across families" (l. 36–37), and the Conclusions say the same (l. 1036–1038). This contradicts Sect. 5.5 (l. 681–684): rescaled, the simulation decides 4.2 floors closer than the produced median within a family (interval −5.4 to −0.5). Sect. 6.1 (l. 903–905) gets it right, and the response calls this the one conclusion that changed. Use the wording of Sect. 6.1: added as an offset, the simulation helped only across families; rescaled, it improved on the median of the produced alternatives within a family, but not on the nearest produced setting.
- **(b) The 8.5 floors for a new setting.** The figure is quoted without splitting interpolation from extrapolation (l. 32–33, 672, 1034), although R3c asked for the split wherever 8.5 floors is quoted. The nearest setting decides at 4.7 floors when the new force lies between produced ones. It needs 9.5 floors when the new force lies outside them, and there force is confounded with stroke speed.
- **(c) "Learned models added abstention rather than accuracy"** (l. 37–38, 1038). This should say where the abstention held its level. The intervals cover 85–86 % with a sibling, 43–55 % for a new setting and at most 12 % for a new family (l. 724–729). This is what R1 meant by "naming the rules whose coverage is close to nominal".
- **(d) "Requirements at a performance index of 1.33 lay inside every decisive distance"** (l. 35–36, 832, 1035–1036; Table 5). This does not hold for near-replicate siblings:
  - there NN decides at 0.85 floors (l. 631), whereas these requirements lie a median 1.7 floors above q95;
  - NN says *meets* at Ppk = 1.33 in 91 % of the new-variant cases (l. 834);
  - Table 5 contradicts itself on this point (l. 891–892 against l. 896–897).
- **(e) "None was safe closer than 16"** (l. 33–34, 1034; Table 5). This is measured in the floor of the target family. The paper rightly calls the floor of the produced family the one a team would have (l. 622). In that floor the safest rule is M3, at 40/17 floors (`panel_source_floor.csv`), not the envelope rule (41/26). Only M5 and M2 are reported there (l. 622–623), so "the envelope rule the safest for a new family" (l. 857) holds only in the target floor. State the unit with the 16 floors, and report the best rule in both floors.

**N4. The refit bootstrap preserves the relation but degrades the design, and the paper does not say so**
(Sect. 4.4, l. 527–529; Sect. 5.9, l. 857–860; Table A2, last row; Appendix, l. 1087–1088)

*How the resampling works.* Each geometry's three lubrication patterns are drawn with replacement until at least two are distinct (`refit_one` in `robustness.py`).

- There are only seven distinct outcomes per geometry, 49 in all, and the original design occurs with probability 1/16.
- In 75 % of draws per geometry, one pattern is duplicated and another is missing. Then:
  - every new-variant target has a single distinct sibling;
  - the calibration set has five distinct alternatives instead of eight;
  - duplicated series enter `noise_floor` as zero-variance pairs, which lowers the GP noise bound.

*The consequence.* For several rules the point estimate sits at the edge of its own refit interval. Examples from Table A2 and `rob_refit.csv`:

- M1s with a sibling: 4.9 floors, refit interval 4.9–7.3;
- M2 safe distance: 0.15, interval 0.15–1.35;
- M5 safe distance: 0.75, interval 0.75–2.96.

These intervals describe the distances when one pattern is replaced by a copy of another. They are not sampling uncertainty around the reported values.

*What still holds.* The main ranking survives every configuration: NN is more decisive than M5 and M5n. But "all 200 resamples" means all of at most 49 configurations.

*A missing interval.* The one conclusion that changed in this revision, that the rescaled simulation adds information within a family (l. 681–683), has only a fixed-fit interval. `rob_refit_paired.csv` contains M1s−NN and M1s−M1, but not M1s−M1n.

*What would fix it.*

- Describe the bootstrap as above in Sect. 4.4 and in the note to Table A2.
- Compute the noise floor over distinct series only.
- Report the refit paired interval for M1s−M1n.
- Consider the all-subsets design of Fig. 3, conditional on the relation, as the measure of calibration-set variability.

**N5. The jackknife+ guarantee is overstated**
(Sect. 3.3, l. 335–336; Appendix, l. 1084–1086)

- **The quantile does not exist for n ≤ 8.** With six to eight calibration alternatives and α = 0.1, ⌈(1−α)(n+1)⌉ exceeds n, so the jackknife+ upper bound of Barber et al. (2021) is infinite.
- **What the code does instead.** `jackknife_plus` in `decisions.py` uses the extreme leave-one-out values. This guarantees at least 1 − 2/(n+1): 0.78 with eight alternatives and 0.71 with six, not "at least 0.8".
- **Median centring.** The interval is centred by the median of all the leave-one-out residuals, so each leave-one-out predictor depends on its own left-out point, and the guarantee is only approximate.
- **Empirical coverage** is fine: 96 % for M3 and 89 % for M3n with a sibling.

Correct l. 335–336, and say in the appendix that this is a median-centred jackknife+ using extreme order statistics. This parallels the (n−1)/(n+1) correction the editor required for the largest-residual margin.

**N6. Say how the GP noise floor is computed, and what it implies**
(Sect. 3.3, l. 317–320; Table 2 note; Appendix, l. 1054–1057)

- **No leakage.** I checked `noise_floor` and `m5_fit`: the between-series variance is pooled over the calibration alternatives only, so the held-out series does not leak into its own interval. Please say so, since in the sibling relation the target's own cell contributes two series.
- **The bound is almost always active.** It binds in 97–100 % of fits, so the noise level is in effect a plug-in estimate. With a sibling, M5n then behaves essentially like a one-way random-effects prediction interval around a smoothed force-level mean.
- **What this supports.** It supports "learning adds intervals rather than accuracy" (l. 721).
- **The transferable lesson.** The near-nominal coverage came from quasi-replicate series in every calibration cell, not from the learner. With the sampling-only bound of the first version, coverage was 71–72 %.
- **Minimal report.** Add "how the noise floor or replicate variance was obtained" to the minimal report of Sect. 6.5.
- **Appendix.** State that the hyperparameters are maximum-marginal-likelihood estimates without hyperpriors, and that the noise bound is expressed on the normalised scale.

**N7. Sect. 6.1 mislabels one finding and overgeneralises another**

- **(a) Not definitional** (l. 870–872). The clause "reaches its nominal level only where the calibration alternatives are exchangeable with the new design" is listed as following from the definitions, but it does not:
  - exchangeability gives the distribution-free rules (M2, M3) their guarantees;
  - the GP interval is model-based, and it under-covered even with a sibling (85–86 %);
  - nothing in the definitions implies failure without exchangeability.

  Move the clause to the observations, or restrict it to distribution-free intervals.
- **(b) Overgeneralised** (l. 905–906). "Learned models predicted as well as the nearest produced setting" holds for M5, M5n and M3n with a sibling, whose centres decide at 3.3, 3.1 and 3.7 floors (l. 721–723). It does not hold:
  - for M3, whose centre decides at 9.9 floors;
  - for a new setting, where the learned centres decide at 10–21 floors against NN's 8.5 (`dec_coverage.csv`).

  Add "with a produced sibling".

**N8. Two key terms are used in two senses**

- **"Within the family."** It means the sibling relation in l. 722, 725 and 808, but both within-family relations in l. 34, 644 and 900.
- **"Six to nine produced settings per fit"** (l. 36, 903, 938). This means six to nine produced alternatives at two or three force levels, whereas a "process setting" elsewhere is a force level.

For readers from machine learning, the number of distinct force levels is the binding constraint. Use "with a produced sibling" and "six to nine produced alternatives at two or three force levels".

**N9. The transparency argument misdescribes the nearest produced setting**
(Sect. 6.2, l. 916–919)

NN does not point to "the produced alternative it copies". It averages:

- the two siblings, in the new-variant relation;
- all six alternatives at the two neighbouring forces, for an interpolated setting (Appendix, l. 1057–1058; `nn_point` in `decisions.py`).

"Points to the produced alternatives whose record it averages" keeps the argument and is accurate. Also, the worked example shows NN's verdict but not its transparency, so "the worked example shows" is too strong.

**N10. The surrogate contrast is one unsupported sentence**
(Sect. 5.5, l. 688–690)

- **The surrogate is not described.** It is a GP over blank-holder force, friction and sheet thickness, fitted to 66 simulations per geometry and scored by leave-one-out (`design_space.py`).
- **Its decision fitness was not computed.** It is inferred from the surrogate's closeness to the simulation.
- **The count is generous.** "Within 1.8 floors for 12 of the 14" includes the convex wall angle at 1.82 floors (`ds_surrogate.csv`).

This is the result closest to surrogate-based DFM, the commonest AI use case in the collection. Give one sentence of method, and either compute M0 with the surrogate in place of the simulation or phrase the claim as an inference.

## 5. Remaining minor and editorial points

Of my 22 first-round minor comments, all are addressed or answered with reasons, except 16 (point 6 below) and 21 (the DOI, N2). I accept the reasons given for 8, 10 and 14 and the partial changes to 1 and 9.

1. **Make the black-box formulation operational (Sect. 6.5, l. 990–995; B7).** Three to five sentences would do:
   - **Classifiers with a fixed threshold.** Such a classifier does not take the requirement as input, so it cannot be scored "by sweeping the requirement". It can be scored by binning its test cases by their true margin d, which needs cases spread over d; or the requirement can be made an input. A probabilistic classifier needs two thresholds to return *trial*.
   - **Black-box tools.** The exact estimator assumes interval verdicts. A black-box tool, and certainly an LLM-based check, may return verdicts that are not monotone in R and that vary between repeated queries. κ and ω must then be computed on a requirement grid with repeated queries, and the share of non-monotone verdict sequences should be reported.
   - **Continuous relations.** Say how strata are formed and how many cases each needs. With about 240 verdicts per relation, the 95 % threshold already rests on the dozen worst.
   - **Generative design.** Say what is scored: the manufacturability check inside the generator, applied to requirements on the generated designs.
2. **Give the minimal report as a numbered checklist or short table (Sect. 6.5, l. 995–998).** Add the source of the noise floor (N6) and, for LLM-based tools, the prompt and query protocol.
3. **Add AI-for-DFM references (Sect. 2.1, l. 113–120).** Sect. 6.5 proposes to score LLM-based checks, so cite one or two evaluations of language or vision–language models on design and manufacturing tasks. Examples are Makatura et al. (2023), "How can large language models help humans in design and manufacturing?", and Picard et al. (2023), "From concept to manufacturing: evaluating vision-language models for engineering design".
4. **Turn the designer-study questions into hypotheses (Sect. 6.3, l. 943–945).** As written they are research questions. State one testable hypothesis with its measure. For example: showing the relation-specific guard band with each verdict reduces the acceptance of wrong verdicts without increasing the rejection of right ones, compared with showing the verdict alone. Zhang et al. (2021) is cited only in Sect. 2.4, although the response says it is discussed in Sects. 6.2–6.3. It is directly relevant here, since it found that the same AI assistance helped some design teams and hindered others.
5. **Reword the multi-task statement (Sect. 6.3, l. 933–936).** It is correct for the new family. But in the pooled scopes both families have data, so cross-family correlation is estimable there. The pooled GP, with a 0/1 geometry input in a squared-exponential kernel, is a restricted intrinsic coregionalisation model: equal variances, one positive cross-family correlation and shared length scales. Say so, rather than "the borrowing of strength the data allow". A less restricted coregionalised or hierarchical model remains a possible extension.
6. **M5 at two alternatives (Sect. 5.6, l. 767–769; Fig. 3; first-round comment 16).** M5 at k = 2 still fits three or four hyperparameters to two points, and the text interprets the value ("12–14 floors with two alternatives"). Fix the hyperparameters for small k, or start the M5 curves at k = 3. Also, "the Gaussian processes" should read "M5", since Fig. 3 shows only M5.
7. **Abstract wording (l. 31–32).** "Decided within 3.4 floors" can be read as the opposite of what is meant. Write "was right for requirements more than 3.4 floors from the truth".
8. **Number of rules (abstract l. 29; Sect. 3.3, l. 307).** These say "thirteen rules", but Table 4 lists fourteen including M6, whose note says it "appears only in the robustness analysis". Write "thirteen rules and, as a robustness variant, M6".
9. **Split the cost sentence (Sect. 5.8, l. 841–845).** It is too condensed to parse, and it does not say clearly that it concerns the ISO 2768-1 scenario. Split it, or list the cheapest rule for each relation.
10. **Optional: an interval version of M1s.** For example, apply M2's largest-residual margin to the residuals of the scaled fit. This would show whether a rescaled simulation can be both safe and decisive with a sibling, and would complete my first-round request for "a scaled rule and its interval version". The full Kennedy–O'Hagan formulation remains optional, as the editor decided.

## 6. Recommendation

**Minor revision.**

The revision addresses the substance of all seven of my first-round major comments, and of the editor's required revisions within my remit (R1, R3a, R3d, R3f, R4a and R5b). Every number I re-checked is right.

The paper now makes a defensible contribution to this collection: a production-referenced standard for evaluating simulation- and AI-based manufacturability decisions. It offers a production-record baseline, explicit abstention, a procedure for single decisions, and a sober, conditioned answer about what classical small-data learning adds.

The two issues I label major concern material new in this round, and both can be fixed from the stored intervals and result files without new data or modelling:

- the guard band must be tied to a stated requirement prior with its influence shown, or made prior-free (N1);
- the evidence behind the quoted coverage, guard and refit figures must be in the paper or in a citable archive (N2).

In addition, the abstract and conclusions need the corrections in N3, and the descriptions of the refit bootstrap and the jackknife+ need correcting (N4, N5).

I do not need to see the manuscript again if the editor is satisfied that N1–N3 have been dealt with.

## 7. Confidential comments to the editor

The revision is honest and careful. I found no errors in the numbers I re-checked: all of Table 4 and Table A2, the worked example and the figures quoted in Sections 5.1–5.9, against the released code and result files. I also checked that the new GP noise floor does not leak the held-out series into its own interval, and it does not.

The response overstates in a few places:

- the paired refit intervals and the result files are named in the response rather than in the paper;
- the requirement prior is "stated" only as a range;
- the "concrete hypotheses" are research questions;
- Zhang et al. (2021) is not discussed where the response says it is.

I read these as compression rather than misrepresentation.

The DOI archive you required at resubmission has not been deposited. Several numbers can now be verified only from the result files, so I would make the deposit a condition of acceptance.

The AI content remains modest, but the paper now fits the collection on the terms you set: as an evaluation standard. My main technical concern (N1) took minutes to verify from the stored intervals, and it should not take the author much longer to address.
