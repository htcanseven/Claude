# Review report: Reviewer B (AI for design for manufacturing)

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design, Special Collection "AI in Design for Manufacturing"
**Recommendation:** Major revision

---

## 1. Summary of the submission

The manuscript proposes a framework for judging whether a design-stage prediction is fit to decide a manufacturability requirement. Errors are expressed in a unit taken from production itself, the "production floor" (the 95 % quantile of the difference between the centres of two 50-part batches of one alternative). Every decision rule that returns *meets*, *fails* or *trial* is summarised by two operating characteristics: the requirement distance beyond which 95 % of its verdicts are correct (the decisive distance) and the distance beyond which at most 5 % are wrong (the safe distance). Both are evaluated separately for each relation between a new design and the produced evidence (a sibling at a produced setting, a new process setting, a new family), using grouped cross-validation. The demonstration uses the open RDDAC/DDACS deep-drawing data: 18 alternatives (2 geometries × 3 blank-holder forces × 3 lubrication patterns), each with 500 consecutive parts and matched finite-element simulations. Twelve rules are compared, from the nominal simulation through bias correction, conformal-style margins, Gaussian processes and gradient boosting to a nearest-produced-setting baseline, and each calibrated rule is also run without the simulation. The paper concludes that the relation sets the attainable distance (about 3 floors with a produced sibling; no rule decides closer than 8.5 floors for a new setting; none is safe closer than 16 floors for a new family). It also concludes that the simulation helps only for a new family, and that learned models match the nearest produced setting in accuracy while adding abstention.

## 2. Assessment

- **Originality: adequate.** The paper combines known ideas (operating characteristics, three-way guard-banded decisions, selective prediction, grouped cross-validation, conformal margins) into a production-referenced evaluation of DFM decisions; the floor unit and the split by evidence relation are new in this setting, but the distances themselves reduce to familiar error and coverage statistics.
- **Significance for design research: adequate.** It gives design margins, testing strategy and front-loading a production-referenced quantity they lack, but it rests on one process and two geometries, and its use by designers is not studied.
- **Significance for the collection (AI in DFM): adequate.** It addresses a real gap (when can an AI-based manufacturability prediction be trusted to decide?), but the AI evaluated is classical small-data regression on 6–9 design points, and human–AI aspects are not examined.
- **Technical soundness: adequate.** The estimator is exact, the bootstraps are paired and the robustness checks are extensive and openly reported, but the GP noise model, the additive-only use of the simulation, the refit bootstrap and one quantised characteristic need attention.
- **Evidence supports the claims: weak.** The numbers for this dataset are well supported and reproducible, but the general claims about what simulation and learning contribute rest on two geometries, two transfer calibrations, two force levels per extrapolation and a narrow set of model forms.
- **Clarity, organisation and length: adequate.** The structure is logical and the prose precise, but the text is very dense in numbers and coined terms; readers outside sheet-metal forming will struggle, and some of the forming detail could be condensed.
- **Positioning and references: adequate.** Coverage of V&V, conformal prediction, decision-based design, margins and testing is strong; coverage is thin on recent AI-for-DFM work, multi-fidelity modelling and the literature on human reliance on AI.
- **Fit to RED: adequate.** This is a methodological contribution to design decision-making with an empirical evaluation, not merely a case study, but the design-theoretic contribution should be sharpened and the process-specific material shortened.

## 3. Major comments

**Strengths and verification.** The paper asks a question the collection needs answered and treats it with unusual care. It uses grouped evaluation by evidence relation, a strong naive baseline (NN), ablations with and without the simulation, intervals that include the uncertainty of the reference, and an honest record of which rules were added after the first results (Section 4.5). The threats to validity are candid (Section 6.6), and Table 13 separates general guidance from dataset-specific observations. Its central practical message deserves to reach the AI-in-DFM community: learned models must be compared with a production-record baseline and scored by evidence relation. I spot-checked Tables 8, 10, A3 and A4 against the released result files and reproduced the M1 distances with the released estimator; everything I checked matched. The comments below concern scope, model specification, reporting and framing, not the integrity of the numbers.

### 1. The conclusions about what learning contributes depend on a very small, factorial data regime, and this should be stated wherever they appear

*Problem.* The abstract (p. 1), the fifth finding of Section 6.1 (p. 26), Section 6.3 (p. 27) and the Conclusions (p. 28) state that learned models "matched the nearest produced setting in accuracy while adding calibrated abstention". Section 6.3 turns this into a lesson for "the evaluation of AI-based DFM support". The evidence is narrow in ways that largely determine the outcome:

- Each alternative-level model (M2, M2n, M5, M5n) is fitted to 8 (new variant), 6 (new setting) or 9 (new family) alternatives with two or three descriptors, and the GPs estimate four hyperparameters from these points (Appendix A.1). The part-level boosting models (M3, M4) see thousands of parts but only the same 6–9 distinct design–process points.
- In the new-variant relation, the held-out alternative differs from its two produced siblings only in lubrication. Production resolves lubrication in only 51 of 126 contrasts (Table 6). NN is therefore essentially the mean of two quasi-replicates, and its 3.4 floors largely measure how reproducible q95 is between runs (compare the "between series" column of Table 5). NN is better read as the replicate bound for this relation than as a competitor that beats learning.
- In the new-setting relation, the calibration set contains only two force levels, so no learner can identify the non-linear force response. Table 6 shows that the minimum resolvable change differs between 100–300 and 300–500 kN, and the 100 kN series ran at a slower stroke (Sections 5.2 and 6.6). Tree ensembles cannot extrapolate beyond the produced settings, so they reduce structurally to a nearest-setting prediction. In the median new-setting GP fit, the force length scale sits at its lower bound (0.1, i.e. 10 kN; `dec_gp.csv`), so the GP reverts to its mean. "Learning adds little over the nearest produced setting" is thus the expected outcome given how the data were designed, not evidence about learning in DFM in general.
- As point predictors, the learned models are not worse than NN within the family. The interval centre of M5n decides at 2.8 floors and that of M5 at 3.4, against 3.4 for NN (Table A3). Their disadvantage in decisive distance comes from their intervals, which is a separate issue and partly a matter of specification (Comment 3).

The headline that "the relation of a new design to the produced evidence governed decision fitness more than the model did" is not formally supported either. For M0 the relation has essentially no effect (106–109 floors throughout Table 8). Within a relation, the spread across calibrated rules (3.4–27 floors for a new variant, 8.5–39 for a new setting) is of the same order as the spread across relations. What the data do show is that the best attainable distance grows with the novelty of the design. This is the design-stage counterpart of the familiar loss of accuracy under distribution shift, which is the motivation for the grouped cross-validation of Roberts et al. (2017) that the paper cites. The relation is also confounded with the size and composition of the calibration set (8, 6, or 9 alternatives of the other geometry).

*Why it matters.* Readers of this collection will take the abstract and Section 6.3 as evidence about the value of machine learning for manufacturability decisions. Without its data regime, the result invites over-generalisation in either direction.

*What would fix it.*
- (a) State the data regime in the abstract and next to each RQ3 statement in Sections 6.1, 6.3 and 7: the number of distinct produced settings per fit, the descriptors, and the 3×3 factorial within two geometries. Phrase the conclusions as conditional on it.
- (b) Present the new-variant relation explicitly as the replicate (reproducibility) bound for any rule.
- (c) Replace "governed … more than the model did" with a claim the analysis supports, for example the best-rule distance per relation with its interval alongside the range across rules, or a simple decomposition of the calibrated rules' log-distances into relation and rule effects.
- (d) Explain the observed behaviour through the learners' inductive biases: trees do not extrapolate, a GP reverts to its mean, and two force levels identify at most a linear trend. That explanation, not the numbers, is what will carry over to other settings.

### 2. The conclusions about the simulation concern one low-fidelity simulator used only additively, and, for a new family, two transfers

*Problem.* "The simulation contributed only to the new family" (abstract; Section 7) is stated generally, but four things limit it.

- (i) The DDACS model is of low fidelity for this production. Its median offset from production reaches 109 floors (Table 7), it gets the sign of the concave arm angle wrong, exaggerates the blank-holder-force effect 2.6- to 5.1-fold, carries extraction noise of up to about 10 floors and has an undocumented material model (Sections 4.2 and 5.3; Table A9).
- (ii) It does not model the stroke-speed change that accompanies the 100 kN setting, so in the extrapolation cases it is asked to predict an effect it does not contain.
- (iii) The simulation enters every calibrated rule either as an additive offset (M1, M2, M5, and the discrepancy target of M3) or through a friction parameter without a discrepancy term (Mc). The standard multi-fidelity correction y = ρ·s + δ(x) (Kennedy and O'Hagan 2000), or simply a linear calibration of production on simulation, is not among the rules. This is so even though the paper itself diagnoses a scale error in the force effect.
  - As a check, I applied the paper's own estimator (`exclusion` and `distance_pair` in `decisions.py`) to the released `dec_alternatives.csv`. It reproduces M1 exactly: 15.2, 23.75 and 35.3 floors for a new variant, a new setting and a new family.
  - A two-parameter calibration, q95 ≈ a + b·s₀, fitted on the same calibration alternatives, decides at 4.9 floors within the family (M1n: 9.1; NN: 3.4), but at 19 floors for a new setting and 122 for a new family.
  - The paper's conclusion for new settings and new families therefore survives. However, "within a family it adds nothing" (Section 5.5) describes the additive use of the simulation, not its information content, and the paired differences M1−M1n, M2−M2n and M5−M5n (Table A4) measure that use.
- (iv) The new-family results rest on two transfer calibrations between geometries that differ in three features at once (Section 4.1). The intervals in Tables A1 and A4 hold these two fits fixed, so they say nothing about what a further family would do. Even so, "for a new family no rule was safe closer than 16 floors" appears in the abstract, and Table 13 turns it into guidance.

*Why it matters.* Surrogates trained on simulation are a central AI-in-DFM use case. A general statement that simulation helps only across families would be read as a verdict on simulation and on surrogates trained on it, whereas the evidence concerns one specific, poorly calibrated simulator used in a restricted way.

*What would fix it.*
- Add a scaled (multi-fidelity) rule and its interval version. The full Kennedy–O'Hagan formulation, with friction calibrated jointly with a discrepancy term (Mc and M5 each implement half of it), would be the natural reference if it is feasible.
- Phrase the comparisons with and without the simulation as conditional on how the simulation is used.
- State in the abstract and conclusions that the simulator has a large, partly sign-inconsistent bias and lacks the stroke-speed effect.
- Present the new-family numbers as two illustrative transfers.
- Note that any surrogate trained on DDACS inherits M0's bias, so the M0–M5 results bound what such surrogates could achieve for this process without production data. That is a useful, transferable statement for the collection.

### 3. The learned models do not yet have a fair, current small-data specification

I am not asking for deep learning, which six to nine design points cannot support. But the conclusions that learned intervals are over-confident outside exchangeable settings, and that learning adds abstention rather than accuracy, should rest on a specification that reflects current small-data practice.

- **(a) GP noise model.** The lower bound on the white-noise level is the mean squared block-bootstrap standard error of the calibration alternatives' q95 (Table 2 footnote; Appendix A.1; `m5_fit` in `decisions.py`).
  - That standard error is about 0.1 floor (Section 5.1). By contrast, the q95 values of the three lubrication series of one geometry and force differ on average by 0.7 floors (waviness) to 4.4 floors (dome) in `dec_alternatives.csv`, consistent with Table 5. The bound therefore ignores the between-run variation that the paper itself shows to dominate.
  - With four hyperparameters and 6–9 points, maximum-likelihood fitting leaves the noise at this bound in 35–45 % of fits (Table A7), and coverage of 71–72 % against a nominal 90 % (Table A3) is the predictable result. The "no noise floor" variant (Table 12) changes nothing because the bound is negligible.
  - Natural remedies are a nugget informed by the quasi-replicate series, hyperpriors with marginalisation over the hyperparameters, or a hierarchical model with a random effect for the run or lubrication series.
- **(b) Jackknife margins.** M3 and M4 use a plain leave-one-out margin, which can fail (Barber et al. 2021, cited). The jackknife+ needs no extra fits here, because the leave-one-out fits already exist, and it carries a coverage guarantee.
- **(c) Borrowing strength across families.** The only model that sees both geometries is a single GP with a 0/1 geometry input, and its results are not reported (Comment 4). A multi-task (coregionalised) GP or a hierarchical model is the current standard for transfer between related products. It would directly test the call's premise of learning from other products' data.
- **(d) Methods aimed at the quantity being scored.** The safe distance measures a false-accept and false-reject rate.
  - Conformal risk control (Angelopoulos et al. 2024) and Learn-then-Test calibrate a rule to control such a rate directly, and weighted conformal prediction (Tibshirani et al. 2019, cited) addresses the non-exchangeability identified in Section 5.5.
  - With *n* calibration alternatives, a distribution-free interval cannot certify a miss rate below 1/(*n*+1). A 5 % miss rate therefore needs at least 19 produced alternatives in the relevant relation, and even the 10 % implied by the 90 % intervals needs 9, one more than the eight available within a family. Saying so would turn the paper's observation about the largest-residual margin (p. 9) into a general rule for the calibration budget.

*What would fix it.* Add (a) and (b), which are cheap with the existing pipeline. Report (c), or explain why it is infeasible, and discuss (d). If the conclusions survive, as I expect they largely will for new settings and families, they become much more convincing; if not, the paper's message about AI should change accordingly.

### 4. Some computed results are not reported, and exploratory comparisons should be separated from confirmed ones

*Problem.* Section 4.4 introduces pooled versions of the new-variant and new-setting schemes, and Section 4.5 states that "every variant tried is reported". The decision results for these scopes, however, appear only through the GP diagnostics in Table A7. In the released `dec_resolution.csv` and `dec_coverage.csv`, adding the other geometry's alternatives changes the picture as follows:

| Rule | Relation | Family only | Pooled with other geometry |
|---|---|---|---|
| M2 | new variant | 23 | 53 |
| M2 | new setting | 18 | 53 |
| M3 | new variant | 17 | 25 |
| M5 | new variant | 6.7 | 11 |
| M5 | new setting | 18 | 33 |
| M5n | new setting | 18/5.4 | 16/2.6 |

Decisive distances in floors; M5n shows decisive/safe. In addition, M5 coverage rises from 72 % to 80 % in the pooled scope, and the pooled M5 interval centre is the most accurate point predictor within the family (2.6 floors, against 3.4 for NN).

These results bear directly on whether models can learn from other products' production records, which is the premise of the call, so they belong in the paper. Similarly, the conformalised GP M6 is reported only within the family (Section 5.9), although `rob_decisions.csv` also gives it for a new setting (95/4.7) and a new family (40/22).

Separately, the author discloses that NN (the rule that carries the main conclusion), M5n, the grouped schemes and the exact estimator were added after the first results had been seen (Section 4.5). The disclosure is commendable. Adding a simple baseline after the fact is conservative with respect to claims about learning, but rankings between rules within a few floors of each other remain exploratory.

*Why it matters.* Selective reporting, even if inadvertent, weakens a paper whose main contribution is an evaluation methodology. The omitted results are also the most informative ones for the collection's question about learning across products.

*What would fix it.*
- Report and discuss the pooled scopes, in Table 8 or an appendix table.
- Report M6 for all relations.
- State which comparisons are confirmatory and which exploratory.
- If at all possible, confirm the frozen procedure on data not used to develop it, for example a further RDDAC release, or characteristics or alternatives held back from the second round of analysis.

### 5. The precision of the main comparisons is overstated, and the refit bootstrap mixes evidence relations

*Problem.*
- (a) Both distances are tail statistics. Over 126 cases (about 240 verdicts per distance), the 95 % threshold is set by the dozen worst verdicts; per characteristic (Table A5) it is set by one or two verdicts, as the footnote acknowledges.
- (b) The intervals in Tables A1 and A4 hold the fits fixed. The refit bootstrap (Table 12, last row) is much wider and overlaps for the paper's central comparison: for a new variant, NN gives 2.2–7.0 floors, M5 5.0–19 and M5n 4.1–16. Paired refit differences are not reported.
- (c) The refit bootstrap resamples alternatives with replacement and then defines the within-family calibration set by name (`refit_one` and `jobs_for` in `robustness.py`).
  - When both siblings of a target are absent from a resample, the case becomes an interpolation or extrapolation case but is still scored as a new variant. A simple calculation gives about 13 % of target copies affected, which is enough to shift a statistic decided by the worst 5 % of verdicts.
  - Duplicated alternatives also shrink the largest-residual margins.
  - This is consistent with several point estimates lying outside their own refit intervals in `rob_refit.csv`. For example, M2's within-family safe distance is 0.15 against an interval of 0.40–5.76, and M2n's is 0.00 against 0.25–4.81.
- (d) The new-family intervals are conditional on the two fits (Comment 2).

*Why it matters.* The rankings between rules (NN the most decisive; M5 two floors safer than NN; the simulation's contribution) are the paper's main empirical outputs, and design guidance is drawn from them.

*What would fix it.*
- Use resampling that preserves the relation, for example resampling whole force levels or lubrication patterns within a geometry. Alternatively, use the all-subsets design of Table 9, conditional on the relation, as the measure of calibration-set variability.
- Report paired refit intervals for the key comparisons: NN against M5 and M5n, M5 against M5n, and M2 against M2n.
- Express rankings with their uncertainty, for example the bootstrap probability that each rule is the most decisive.
- Avoid interpreting differences of two or three floors.

### 6. Trust, abstention and decision support are treated only as population-level statistical reliability

*Problem.* The abstract ends: "The findings show which design-stage decisions can be trusted". The paper defines trust as the share of correct and wrong verdicts conditional on the *true* margin, averaged over a population (Section 3.4). That operating characteristic is the right tool for choosing a rule, but it is not what a designer faces at decision time.

- The quantity relevant at decision time is the reliability of a verdict given the *observed* margin between the predicted interval and the requirement. It is covered in a single paragraph (Section 5.5, pp. 20–21). It also depends on an implicit, unstated prior over requirement positions: the `reliability` function in `decisions.py` weights every point of the evaluation grid within ±20 floors equally.
- The *trial* verdict is deferral to a physical test, not to an expert. How designers would perceive, weigh and act on a verdict, its margin, or a guard that fires is not discussed.
- There is no engagement with the literature on appropriate reliance on automation (Lee and See 2004), learning to defer to experts (Madras et al. 2018; Mozannar and Sontag 2020) or AI-assisted design teams (e.g. Zhang et al. 2021).
- Explanation is not discussed, although the paper's own results offer a notable point: the most decisive rule, NN, is also the most transparent, since it points to a produced sibling. A GP interval is not transparent in that way, and the difference matters for designer trust.

*Why it matters.* Designer trust, explainable AI and decision-support systems are explicit topics of the call. As it stands, the paper contributes a measure that could underpin calibrated trust but does not examine trust.

*What would fix it.*
- (a) Add a figure of the share of correct verdicts against the observed margin, by relation and rule, with the requirement prior stated and its influence shown.
- (b) Work through step 6 (Fig. 1) for one held-out alternative, showing exactly what the designer receives: relation, guard, interval, margin, verdict, and the reliability at that margin.
- (c) Discuss the implications for human–AI decision-making, such as when an abstention should go to an expert rather than to a trial, and the interpretability of NN compared with a GP, and relate them to the literature above.
- (d) Use "reliable" rather than "trusted" where the claim is statistical, and give the designer study proposed as future work (Sections 6.4 and 7) concrete hypotheses. For example: does showing the safe distance with each verdict improve how well designers' reliance matches the rule's actual reliability?

### 7. How developers and evaluators of AI-based DFM tools could use the framework, and where it sits in that literature, needs to be made explicit

*Problem.* Section 6.3 recommends that AI-based DFM support be "compared with a production-record baseline and scored by evidence relation, in a unit that production defines". This is a valuable message, but the paper does not show how the developer of a surrogate, a generative-design pipeline or an LLM-based manufacturability check would follow it.

- (i) The floor depends on the protocol. It ranges from 0.49 to 0.95 of its value over the first half of a series, and varies by a factor of 0.6–2.2 across batch sizes and quantiles (Sections 5.1 and 5.9). Distances in floors are therefore not comparable across studies unless the protocol is fixed, or unless the floor is derived from a reported model of variance components and drift.
- (ii) The data prerequisites, consecutive series of several variants spanning the relations of future designs, are rarely met; the PA12 attempt in Section 6.5 failed on them. The paper does not say what reduced evidence (for example replicate batches or pilot runs) would suffice.
- (iii) Rules must return an interval for q_p. Many AI-DFM tools instead return classes, feature-level flags with text rationales (LLM- or VLM-based checks) or geometries (generative design).
- (iv) Evidence relations are defined by a factorial (same force, other force, other geometry). They are not defined for the continuous geometric novelty typical of generative design.

The positioning (Section 2.1, Table 1) is correspondingly thin on recent AI-for-DFM work: learning manufacturability from CAD models, deep generative design (e.g. Regenwetter et al. 2022), and evaluations of LLMs and vision–language models for design and manufacturing. The keywords do not mention machine learning or AI.

*Why it matters.* For this collection, the framework's value lies in being reusable beyond deep drawing and beyond regression models.

*What would fix it.* Add a short section or appendix on applying the framework to an AI-based DFM tool, covering:
- a minimal reporting standard: the floor with its protocol and variance components; decisive and safe distances by relation with refit intervals; coverage; the NN and no-simulation baselines; and guard performance;
- a black-box formulation. Any tool that can return meets, fails or trial for a given requirement value can be scored by sweeping the requirement; an interval is sufficient but not necessary. For classifiers with a fixed threshold, report the score at the operating threshold and a risk–coverage curve; for LLM-based checks, include the requirement value in the prompt;
- relations for continuous novelty, for example strata by distance in a descriptor or learned-embedding space, or by position inside or outside the convex hull of produced designs;
- minimal data requirements.

Update the positioning and keywords accordingly.

## 4. Minor comments

1. **Terminology (title onwards).** In manufacturing usage, "production floor" means the shop floor; DFM readers will be confused. Consider another term, such as "production resolution", or define it prominently. "At 95 % confidence" (p. 2; Section 5.1, p. 14) describes a quantile of batch differences, not a confidence level.
2. **Abstract (p. 1).** It is very dense. Give the physical size of a floor for at least one characteristic (e.g. 0.05 mm of draw-in), and state the structure of the data, including that within a family the "new designs" are process settings on an existing tool (Section 4.1). "Calibrated abstention" sits poorly with GP coverage of 71–72 % at a nominal 90 % (Table A3). "Twelve rules" omits M6 (Section 5.9).
3. **Keywords (p. 1).** For this collection, add "machine learning" or "artificial intelligence".
4. **Section 1 (p. 2).** Liu et al. (2026) concerns causal failure reasoning in design FMEA, not the automation of manufacturability checks for which it is cited.
5. **Section 3.1 (p. 7) versus the title and abstract.** The scope statement (release of variants and process settings in process planning and tryout; transfer to a new family) is clear, but the title and abstract speak of design-stage decisions in general. Make clear throughout that the framework presupposes production evidence for the family, so early-stage DFM is covered only by the new-family relation.
6. **Section 3.2, Eq. (2) (pp. 7–8).** The floor pools all batch pairs regardless of their separation in time, so under drift it grows with series length. Consider a fixed lag, or report σ_b, σ_w and the drift model so that F can be recomputed for other protocols (see Major comment 7).
7. **Section 3.3, margins paragraph (p. 9).** The coverage of "(n−1)/(n+1) when [the offset is] estimated from the same residuals" is a lower bound. Say "at least" and give the one-line argument: a new residual is covered whenever it falls within the range of the calibration residuals.
8. **Section 3.3 and Table 2 (pp. 8–9).** The GP treats lubrication as an ordinal rank, while the oil amounts of the patterns overlap (Section 4.1). The patterns' nominal oil amounts would be a natural continuous descriptor.
9. **Section 3.4 (pp. 9–10).** Relate the decisive and safe distances explicitly to selective risk and coverage (Geifman and El-Yaniv 2017), and consider showing risk–coverage curves for the main rules so that ML readers can place the results. Explain how the distances of interval rules relate to the coverage and half-width in Table A3.
10. **Section 3.5 and Table 10 (pp. 10–11, 23).** The novelty guard is one-dimensional (the simulated q_p within the calibration range). A multivariate applicability measure, such as GP predictive variance or Mahalanobis distance over the descriptors, could be evaluated alongside it.
11. **Section 4.3 and assumption A3 (pp. 7, 12–14).** In the released features, the mid-side draw-in is strongly quantised.
    - It takes 102 distinct values over 8,990 parts, in steps of 0.019 mm, which is about 0.38 floors.
    - Each 500-part series has between 7 and 27 distinct values (median 14.5).
    - The block-bootstrap standard error of q95 is exactly zero for 5 of the 18 alternatives (`dec_alternatives.csv`), which also sets the GP noise bound to zero there.
    - Assumption A3 should therefore be checked for measurement resolution as well as repeatability. Report the resolution of each characteristic relative to its floor, and either use sub-pixel edge estimation or add a sensitivity analysis without this characteristic.
12. **Section 4.4 (p. 13).** New-family distances are normalised by the new family's own floors, which a design team would not yet have. The floors differ by up to 2.4-fold between geometries (dome, Table 4); discuss this, or use the source family's floor.
13. **Section 5.4 (p. 18).** "Every calibrated rule improves by an order of magnitude": Mc (27 floors) and M2 (23) improve only four- to five-fold over M0 (108).
14. **Table 8 (p. 19).** A plot of decisive and safe distances with their intervals, by relation, would be easier to read than the twelve-by-five table; Fig. 3 shows only four rules.
15. **Fig. 3 (p. 20).** The red/green coding is not safe for readers with colour-vision deficiency. Give the number of verdicts per panel, not only the number of cases.
16. **Section 5.6, Table 9 and Fig. 4 (pp. 21–22).** M5 "from k = 2" fits three or four hyperparameters to two points. Fix the hyperparameters for small k, or omit these cases. The odd/even sawtooth of M1 in Fig. 4(a, c) needs a sentence of explanation.
17. **Section 5.8 and Table 11 (pp. 23–24).** State the nominal angles against which the ISO 2768-1 limits are applied (judging from `scen_truth.csv`, 20° and 10° for the walls and 0° for the arms). In all 18 alternatives the wall angle fails class f/m (by 13–17 floors) and class c (by 6–11 floors) and meets class v (by 2–7 floors) (`scen_truth.csv`). The wall-angle half of the scenario is therefore dominated by clear outcomes, and it should be stated which decisions the borderline cases come from. The linear classes of ISO 2768-1 applied to the cup depth and flange width would extend the evidence on realistic margins beyond two angles.
18. **Section 6.3 (p. 27).** Avoid referring to "the call for this collection" in the article itself; state the question directly. "Predict about as well as the nearest produced setting" could say that the GP centres are at least as accurate (Table A3).
19. **Table 13 (p. 26).** "Keep it only where it is closer or safer" needs a joint criterion, because a rule can be safer but far less decisive (M6: 39/0.4 floors). Point to the cost analysis in Section 5.8.
20. **Section 6.5 (pp. 27–28).** Turn the PA12 experience into explicit minimum data requirements: the number of variants, series length, and replicate structure.
21. **Declarations (p. 29).** Deposit a versioned archive with a DOI at revision rather than at acceptance; the review currently relies on a mutable repository.
22. **References (pp. 35–38).** The NeurIPS entries (Geifman and El-Yaniv 2017; Romano et al. 2019; Tibshirani et al. 2019) lack volume and pages, and AIAG (2010) lacks a place of publication. Suggested additions, according to the major comments above:
    - Kennedy and O'Hagan (2000, *Biometrika*), on multi-fidelity modelling;
    - Angelopoulos et al. (2024, ICLR), on conformal risk control;
    - Lee and See (2004, *Human Factors*), on appropriate reliance on automation;
    - Madras et al. (2018) and Mozannar and Sontag (2020), on learning to defer;
    - Zhang et al. (2021, *Design Studies*), on AI-assisted design teams;
    - Regenwetter et al. (2022, *Journal of Mechanical Design*), on deep generative models in engineering design.

## 5. Recommendation

**Major revision.** The manuscript asks a question this collection needs answered: when is a design-stage manufacturability prediction, including an AI-based one, fit to decide? It answers it with care, through a transparent framework, grouped evaluation by evidence relation, a strong naive baseline, honest disclosure of post-hoc choices, and released code whose outputs I could verify. It is not a mere case study, and its central practical lesson for evaluators of AI-based DFM tools is sound. However, the general claims about what machine learning and simulation contribute go well beyond the evidence: a 3×3 factorial within two geometries, one low-fidelity simulator used only additively, and two family transfers. The learned models are not yet specified in a way that makes the comparison fair, notably the GP noise model. Results that bear directly on learning across products are computed but not reported, and the uncertainty of the main comparisons is understated. Trust and decision support are treated only statistically. All of this can be addressed without new data: by conditioning and narrowing the claims, adding a few standard small-data models, reporting the pooled scopes, using resampling that preserves the relation, and adding a view of the verdicts as a designer would see them. I would be glad to review a revised version.

## 6. Confidential comments to the editor

This is a serious, transparent and technically careful submission. I checked Tables 8, 10, A3 and A4 against the released result files and reproduced one rule's distances with the released estimator, and found no errors. My reservations concern scope, model specification and framing, not integrity. The AI content is modest (classical regression on 6–9 design points), so the editor may wish to consider whether the collection is well served by a paper on evaluation methodology of this kind. I think it is, provided the claims about AI are made conditional on the data regime and the AI baselines are strengthened. The statement that "every variant tried is reported" is inaccurate for the pooled scopes, but because those results are in the released files I read this as an oversight rather than concealment. The paper declares substantial LLM assistance with code, analysis and drafting, in line with Springer policy. Because the open code makes independent checking possible, I suggest requiring the archived DOI at revision.
