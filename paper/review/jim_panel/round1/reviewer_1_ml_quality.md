# Referee report: Reviewer 1

**Manuscript:** Evaluating AI-based manufacturability decisions against the resolution of production
**Journal:** Journal of Intelligent Manufacturing
**Round:** First submission
**Reviewer focus:** Machine learning for manufacturing quality: predictive quality and virtual metrology, learned manufacturability assessment, uncertainty quantification and conformal prediction, small-data and transfer learning
**Date:** 22 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary of the submission

The manuscript proposes a framework that evaluates design-stage manufacturability predictions as decision rules returning *meets*, *fails* or *trial*. The rules are scored against production in units of a "production floor": the 95 % quantile of the difference between the trimmed-mean centres of two 50-part batches of one design within a run. For each evidence relation between a new design and the produced alternatives (produced sibling, new process setting, new family), a rule is characterised by a decisive and a safe distance in floors, and a guard band derived from these turns the rule into a procedure for single verdicts. The demonstration uses the open RDDAC/DDACS deep-drawing data: 18 alternatives of 500 parts (two geometries, three blank-holder forces, three lubrication patterns), seven dimensional characteristics and matched LS-DYNA simulations. Fourteen rules are compared under grouped cross-validation, among them simulation offsets and rescalings, Gaussian processes, part-level gradient boosting with jackknife+ intervals and production-record baselines. The author concludes that within a family the nearest produced setting or a straight line in force is the most decisive rule, that the simulation as used helps only across families, and that the learners add intervals but not accuracy; the comparison of rules is declared exploratory.

## 2. Assessment

- **Originality:** adequate. Scoring design-stage predictions as abstaining decision rules in a unit defined by production, stratified by evidence relation, is a new combination for AI-based DFM. Its components (repeatability-type limits, operating characteristics with an indifference zone, guard bands, grouped cross-validation, conformal margins) are established, however, and the learners themselves are standard.
- **Significance for intelligent manufacturing:** adequate. The question "can this prediction be relied on to decide?" matters to practitioners, and the production-record baseline is a valuable lesson, but the evidence is one small dataset and the AI conclusions do not carry over to data-richer AI-based DFM tools.
- **Technical soundness:** adequate. The definitions and the exact computation of the distances are correct and reproducible, but the Gaussian-process noise bound counts a modelled effect as noise, the interval calibration is not matched to the evidence relation, and a pooled tail statistic hides characteristic-level behaviour.
- **AI/ML methodology, baselines and evaluation protocol:** weak. Grouped cross-validation by relation with no-simulation ablations and a production-record baseline is exemplary, but the Gaussian-process fits are degenerate (they reproduce the baselines), stronger small-data approaches are missing, and rules, strata and guard bands were selected on the evaluation data.
- **Evidence supports the claims:** weak. The descriptive results for RQ1–RQ2 are adequately supported as exploratory findings, but the RQ3 statements on what learning and simulation contribute, and the best-of numbers in the abstract, go beyond what the analyses show.
- **Clarity, organisation and length:** weak. The length is acceptable, but the abstract and results are so dense with numbers and undefined terms that the procedure is hard to follow for JIM's readership.
- **Positioning and references:** adequate. The literature on design decisions, verification and validation, and conformity assessment is well covered, but current ML for manufacturing quality (multi-fidelity and discrepancy modelling, transfer learning, virtual-metrology reliability indices, quantile and conformal UQ) is thin.
- **Fit to JIM's scope:** adequate. Evaluating AI-based decisions in manufacturing design is squarely in scope, but the AI content currently needs strengthening, or the framing narrowing, for this journal.

## 3. Major comments

Before turning to the criticisms I want to acknowledge real strengths. The paper asks the right question and builds the baselines that AI-for-manufacturing papers usually omit: a production-record baseline (NN) and a version of every calibrated rule without the simulation. The development record (Section 4.5) and threats to validity (Section 6.6) are unusually candid. The released material holds up. All 127 SHA-256 checksums in `SHA256SUMS` verify. Generating Tables 3, 4, A2, A3 and A4 in memory with the table functions of `make_tables.py` from the archived CSVs reproduces the manuscript's tables exactly, and the numbers I spot-checked in Sections 5.3–5.5 match `dec_resolution.csv`, `dec_paired.csv` and `panel_*.csv`. The conformal statements in Section 3.3 (ll. 315–322) are correct. The comments below concern what the evaluation can and cannot show.

**1. The learners evaluated reduce to the baselines in this design, so the paper does not yet show what learning contributes.**

*Problem.* The Gaussian processes M5 and M5n are fitted by maximum marginal likelihood without hyperpriors, with five hyperparameters on six to nine alternatives (Appendix, ll. 1084–1091). The released diagnostics (`results/dec_gp.csv`) put the force length scale at its lower bound of 0.1 (10 kN, against training forces 200 kN apart) in the median new-setting fit, and the noise at its bound in every fit. With such a length scale, the posterior mean at an unproduced force is the prior mean, that is the mean of the calibration targets.

I confirmed this by refitting nine of these GPs with the released `m5_fit` on `dec_alternatives.csv` (three held-out force cells and three characteristics; a few seconds of computation, nothing written). In all nine the predicted mean equals the calibration mean to four decimals. For example, with the concave 100 kN cell held out, the mid-side draw-in is predicted at 14.8333 mm by both, against 14.95 mm from the force trend. Across the stored intervals, the M5n centre for a new setting lies a median of 0.3 floors from M1n. For the 300 kN cases it coincides exactly with NN and M1sn, because 300 kN is the midpoint of a balanced 3 + 3 calibration set; this is why the NN and M1sn rows of Table A4 are identical in the interpolated block. With a produced sibling, the M5n centre lies within a median of 0.28 floors (90th percentile 1.2) of NN.

The statement that the interval centres "decide at 3.3, 3.1 and 3.7 floors with a produced sibling, as close as the nearest setting" (ll. 718–720) is therefore not independent support: to within a fraction of a floor, the fitted GP *is* the nearest setting or the calibration mean. The "GP linear" robustness variant does not change this. In eight of the nine fits I inspected, its DotProduct amplitude went to its lower bound (0.01²), which explains why the variant leaves M5n at 17.2/6.1 floors for a new setting (`rob_decisions.csv`).

The part-level boosting rules (M3, M3n) cannot extrapolate in force (ll. 728–729). The archive's own learner study (`scripts/tuning.py`, `results/tune_decisions.csv`) compares regularised and flexible boosting, ridge, quantile-loss boosting and a setting chosen by inner leave-one-out. It shows that no learner setting changes the ranking against NN, which is a useful result that the paper does not report. Finally, NN is a nearest-neighbour regressor and M1sn is ordinary least squares, so the line drawn between rules that use "neither simulation nor learning" (ll. 306–307) and learned rules is a matter of framing.

*Why it matters.* JIM's audience will read the RQ3 conclusions as evidence about AI-based manufacturability support: "Learning adds intervals rather than accuracy" (l. 718), the abstract (ll. 037–038), Section 6.3 and the Conclusions (ll. 1058–1063). What the analysis shows is narrower, though still worth reporting: with a 3 × 3 design, one run per cell and six to nine calibration alternatives, flexible learners fitted by ML-II collapse to cell or neighbour means. That is a finding about identifiability and about this fitting procedure, not about what learning can add.

It also skews the comparison. With a sibling, M5 and M5n are significantly *safer* than NN: their paired safe-distance differences are −2.6 (−3.5 to −1.6) and −2.8 (−3.45 to −1.7) floors, and M5n's for a new setting is −2.35 (−3.2 to −0.5) (`dec_paired.csv`). Yet the narrative ("the simplest is the most decisive", "the production record carried the decision") rests on decisiveness alone.

*What would resolve it.*
- (a) Show the centre equivalences and the fitted hyperparameters explicitly, in a short appendix table by relation.
- (b) Add learners specified for this regime. One option is a GP with an explicit linear (or monotone) mean in force, whose coefficients are estimated by generalised least squares and propagated into the predictive variance, together with weakly informative length-scale priors tied to the force spacing or full Bayesian marginalisation of the hyperparameters. Another is a Bayesian linear or hierarchical model in force and lubrication.
- (c) Separate prediction from uncertainty by crossing the predictors (NN, M1sn, GP mean, boosting) with the interval constructions (none, a relation-matched conformal margin, model-based). Credit for "intervals" can then be assigned correctly: an interval can be put around NN without any learning.
- (d) Report the tuning study.
- (e) Either define what counts as a learned rule, or phrase RQ3 in terms of model classes and data regimes.

**2. Multi-fidelity modelling, Bayesian calibration, transfer learning and physics-informed approaches are under-represented or mislabelled.**

*Problem.* The paper says it scores calibration and conformal methods "as decision rules against production" (ll. 216–218), but the representatives it uses are restricted versions:

- *Multi-fidelity.* M1s is called "a linear multi-fidelity correction (Kennedy and O'Hagan, 2000)" (ll. 296–297), but it contains only the scale term, while M5 is a GP discrepancy with the scale fixed at one. The autoregressive model of Kennedy and O'Hagan (2000) combines a fitted scale with a GP discrepancy. Its recursive successor (Le Gratiet and Garnier, 2014, *International Journal for Uncertainty Quantification*) and nonlinear successor (Perdikaris et al., 2017, *Proceedings of the Royal Society A*) were developed for exactly this situation: 396 cheap runs over thickness, friction, force and geometry against six to nine expensive observations. The conclusion that the rescaled simulation "does no better" than a line in force (ll. 703–708) therefore concerns the most restricted member of this family.
- *Bayesian calibration.* Mc is cited to Kennedy and O'Hagan (2001) (l. 308). In the code (`decisions.py`, `friction_fit` and `mc_point`) it is a least-squares grid search for one friction coefficient per lubrication pattern on the draw-in centres, plus a median offset, explicitly "without a discrepancy model" and without a posterior. The observation that calibrating friction "did not repair" the simulated force trend (ll. 941–943) is the textbook case in which calibration without a discrepancy term is biased and over-confident (Brynjarsdóttir and O'Hagan, 2014, *Inverse Problems*).
- *Transfer learning.* Transfer is tested only zero-shot (new family) and by naive pooling. In the pooled scopes, M1n, M2n and M1sn have no family term, which is why the pooled columns of Table 4 show 77–325 floors, and the GP is a restricted coregionalisation model (ll. 945–948). The case that is both practically relevant and open is few-shot: one or two tryout series of the new family, together with the other family's full record and the simulations of both. Section 5.6 shows that one produced sibling carries most of the information within a family, which makes this case especially interesting. The remark that "a multi-task model cannot help a family with no produced alternative" (ll. 943–945) is correct but leaves this case unanswered.
- *Physics-informed and hybrid models.* The residual model M3 is a fair representative of hybrid learning, but its trees cannot extrapolate. A smooth residual learner, or shape constraints such as the monotone dependence of draw-in on blank-holder force, would test whether physical structure helps where the data identify at most a linear trend.

*Why it matters.* JIM expects engagement with the current state of the art in AI for manufacturing, and these are the approaches a reader would reach for with a low-fidelity simulator and a handful of produced alternatives. Without them, the finding that "the simulation as used ... helped only across families" cannot be generalised to simulation-based or AI-based support.

*What would resolve it.* Add at least the following:
- (i) an AR(1)-type multi-fidelity GP with a fitted scale and a GP discrepancy;
- (ii) a calibration with a discrepancy term in the spirit of Kennedy and O'Hagan (2001) and Higdon et al. (2004, *SIAM Journal on Scientific Computing*), or else a description of Mc as a least-squares parameter fit, without the citation that implies more;
- (iii) a few-shot new-family experiment, with k = 1–3 produced alternatives of the target geometry, with and without the other family's record. It should compare NN within the target family against a multi-task GP with a free inter-family correlation (Bonilla et al., 2008, NeurIPS) or a hierarchical model with family-specific intercepts and partially pooled slopes.

If the author prefers not to extend the experiments, the abstract, Section 6.3 and the Conclusions should restrict the claims explicitly to the model classes evaluated. Physics-informed learning (e.g. Karniadakis et al., 2021, *Nature Reviews Physics*) and sim-to-real transfer in manufacturing (e.g. Tercan et al., 2018, *Procedia CIRP*, for injection moulding) should then be discussed as untested alternatives.

**3. The uncertainty quantification conflates an imposed variance bound with learned uncertainty, the coverage figures are imprecise, and the interval calibration is not matched to the evidence relation.**

*Problem.*

(a) *Noise bound.* The lower bound of the GP noise variance is the pooled variance between the lubrication series of one geometry and force (ll. 302–305; Appendix, ll. 1088–1091; `noise_floor` in `decisions.py`). These series differ by the lubrication effect, which the GP also receives as an input and which production resolves in 51 of 126 contrasts (ll. 578–580), so modelled signal is counted as noise. The bound rests on four or five degrees of freedom, and because ML-II prefers less noise, the fitted noise sits on the bound in 97–100 % of fits (Table A3 note). In the new-setting fits I inspected for the wall angle, the bound exceeds the total variance of the six training targets (normalised noise level about 1.5), so the GP explains all variation as noise. The coverage of 85–86 % with a sibling is thus a property of this plug-in variance, not a learned interval, as ll. 721–724 partly acknowledge. The abstract's "learned 90 % intervals" (ll. 037–038; also ll. 1059–1060) also include the largest-residual margins of M2 and M2n, which involve no learning.

(b) *Precision of coverage.* Coverage is estimated from 126 cases that share 18 alternatives and their calibration sets. A cluster bootstrap over alternatives, which I ran on `dec_intervals.csv`, gives roughly 0.75–0.94 for M5's 85.7 % with a sibling and 0.93–0.98 for M3's 96 %. "85–86 % against a nominal 90 %" therefore does not demonstrate under-coverage, while M3's intervals appear conservative.

(c) *Relation mismatch.* The under-coverage for a new setting (43–55 %, ll. 726–727) is built into the interval constructions. The jackknife+ residuals of M3/M3n, the standardised leave-one-out residuals of M6 and the residual spreads of M2/M2n are all computed within the calibration set. There, each left-out alternative still has produced siblings at its own force, so these are sibling-type residuals, whereas the test case is an interpolation or extrapolation in force. The paper says that the guarantees require exchangeability (ll. 906–907) but does not design the calibration to approximate it.

*Why it matters.* Uncertainty quantification is central to the claimed evaluation standard for AI-based support, and readers will take the coverage figures as properties of GPs, jackknife+ and conformal margins in manufacturing.

*What would resolve it.*
- (i) Estimate the noise from replicate information that excludes modelled effects, for example the within-series block-bootstrap variance plus a between-run component estimated from near-replicate siblings only. Alternatively, place a prior on the noise instead of a hard bound. In either case, report the fitted noise relative to the bound.
- (ii) Report coverage with cluster-robust intervals, per characteristic and per sibling stratum.
- (iii) Calibrate the nonconformity scores by relation. Options include leave-one-force-out residuals within the calibration set, borrowed across the two families (Mondrian or group-conditional conformal prediction; Vovk et al., 2005, *Algorithmic Learning in a Random World*), weighted conformal prediction under covariate shift (Tibshirani et al., 2019, already cited), and the non-exchangeable methods of Barber et al. (2023, *Annals of Statistics*). Otherwise, state plainly that no distribution-free guarantee is attainable for the new-setting and new-family relations with these data; ll. 318–320 nearly do already.
- (iv) Add a proper scoring rule for intervals, such as the interval score (Gneiting and Raftery, 2007, *JASA*), so that interval quality can be compared independently of the decision threshold.
- (v) Because the target is a quantile, conformalised quantile regression on the parts (Romano et al., 2019, NeurIPS) is a natural part-level baseline. The quantile-loss boosting already in `tuning.py` could be conformalised.
- (vi) Discuss M6. Its distribution-free margin costs about ten floors of decisiveness with a sibling (17 against 7.2 floors, Table 4), which is itself an informative result about the price of guarantees with n = 8.

**4. Rules, strata and guard bands were selected on the evaluation data, and the abstract quotes best-of figures.**

*Problem.* Section 4.5 (ll. 522–531) records the following development history:
- NN, M2n, M5n, the grouped schemes, the exact estimator and the GP noise bound were added after the first results;
- M1s, the jackknife+ intervals, the between-run bound and M1sn were added after two internal review rounds;
- the guard bands and their prior were chosen on the evaluation data (ll. 808–809).

The two rules that carry the headline within-family findings (NN and M1sn), and the component that produces the GP coverage, were therefore all introduced after the results had been seen.

The abstract and Conclusions then quote minima over rules and post hoc strata. "4.9 extrapolating to 500 kN and 8.9 to 100 kN" (l. 033) combines NN at 500 kN (4.85) with M1sn at 100 kN (8.85), each computed from 42 cases on six alternatives (`panel_force_levels.csv`). A team that had committed in advance to one rule for an extrapolated setting would face 9.45 (NN) or 8.85 (M1sn) floors. Likewise, "safe at 16–17 floors" for a new family (l. 034) combines M3 in the produced family's floor with M2 in the new family's floor.

*Why it matters.* The optimism of selecting on the evaluation data (Cawley and Talbot, 2010, cited; Varma and Simon, 2006, *BMC Bioinformatics*) may be of the same order as the differences discussed. The transparency of Section 4.5 is commendable, but the abstract presents the selected minima as results.

*What would resolve it.*
- (a) State the exploratory status in the abstract and the Conclusions, not only in Sections 4.5 and 6.6.
- (b) Mark the pre-specified rules (M0–M5) and the post hoc rules in Tables 4 and A4.
- (c) Cross-fit the selection: choose the rule and guard band for each relation on one geometry, evaluate them on the other, and vice versa. This is cheap with the stored intervals. The per-geometry distances I computed suggest that the within-family ranking would survive: with a sibling, NN is at 2.0 and 3.6 floors against M5's 6.4 and 8.5, and for an interpolated setting NN = M1sn at 4.2 and 5.3. The cross-fit would therefore probably strengthen the ranking while giving honest distances and trial rates.
- (d) Estimate g by leave-one-alternative-out cross-fitting and report the out-of-sample share of correct decided verdicts and the trial rates. This would quantify the optimism acknowledged on ll. 808–809 and l. 826.
- (e) Quote in the abstract the distance of the rule a team would commit to for each relation.
- (f) Deposit the frozen procedure now, so that the confirmatory test proposed in Section 7 is genuinely prospective.

**5. Pooling seven heterogeneous characteristics into one tail statistic hides where the simulation and the learners help.**

*Problem.* For a point rule, the decisive distance is about the 90 % quantile of the absolute error pooled over seven characteristics (ll. 376–377; I reproduced 3.28 against 3.35 floors for NN with a sibling). It is therefore set by the worst one or two characteristics. The archived per-characteristic distances (`dec_resolution.csv`) are strikingly heterogeneous:
- For a new family, in its own floor, M5 is safe at 2.1–3.5 floors for both draw-ins and the wall angle, but at 15–35 floors for cup depth, waviness, arm angle and dome.
- For an extrapolated setting, the scaled simulation beats the force trend for the mid-side draw-in (4.0 against 5.7 floors) and the arm angle (5.9 against 9.4), but fails badly for cup depth (165 against 9.8). The "164 floors" false accept (l. 630) is a cup-depth effect.
- For an interpolated setting, the scaled simulation beats the force trend for both draw-ins.

These values rest on 6–18 cases each and are noisy, but they indicate that "the simulation ... helped only across families" (l. 037; ll. 1058–1059) is a property of the pooled metric rather than of the characteristics the forming model represents directly. The sibling relation cannot test the simulation by construction (ll. 311–314), so the within-family conclusion on the simulation rests on six calibration alternatives at two forces.

Two further points. First, the composition of the failing side changes with δ (ll. 368–372), so κ at large δ is computed over a different mix of characteristics than at small δ. Second, the release decision for a design is joint over its characteristics, which pooled marginal verdicts do not measure.

*Why it matters.* A practitioner would qualify rules per characteristic, which the framework allows, and it is precisely in this heterogeneity that the answer to RQ3 lies.

*What would resolve it.*
- Report per-characteristic distances with intervals, or distances for groups of characteristics (process indicators, drawn geometry, cut and springback).
- Allow step 5 to qualify rules per characteristic and relation.
- Add a design-level analysis in which a design meets only if all its characteristics meet.
- Quantify the effect of the δ-dependent composition, for example by restricting the distances to characteristics that are feasible over the whole range, or by using per-characteristic weights.

**6. The uncertainty of the distances, and of the comparisons between rules, is understated.**

*Problem.*
- (i) The main intervals (Table 4, Fig. 3) hold the fits fixed and resample nine alternatives per geometry (ll. 509–512). This is a percentile bootstrap of a tail functional with 18 clusters, which is unreliable, and holding the fits fixed omits the variability most relevant to comparing rules.
- (ii) The replicates of the truth carry within-run uncertainty only, although the paper bounds the missing between-run component at 1.2–9.8 floors (ll. 1033–1034). The target is thus the q95 of one realised run.
- (iii) The refitting bootstrap reflects the loss of a lubrication pattern, not sampling uncertainty (ll. 517–518).
- (iv) For the new family, the two fits are held fixed.
- (v) Twenty-two rule pairs across five scopes and 27 robustness variants are compared without multiplicity control.

As a result, differences of one to three floors carry intervals that understate the uncertainty; examples are NN at 3.4, M1sn at 3.5 and M1s at 4.9 floors with a sibling. The paper is appropriately cautious in places (ll. 637–639), but not in the abstract.

*What would resolve it.*
- Make a refit-based resampling the primary interval and state exactly what it represents, or fit a hierarchical model of the exclusion distances with alternative and characteristic effects.
- Add a between-run component to the uncertainty of the truth, for example estimated from near-replicate siblings.
- State the minimum difference in floors that this design can resolve.
- Adjust for multiplicity, or say explicitly that the paired intervals are descriptive.

Bates, Hastie and Tibshirani (2024, *Journal of the American Statistical Association*) is a useful reference on what cross-validation estimates and on the coverage of naive intervals around it.

**7. The title, contributions and scope promise more generality than the demonstration supports.**

*Problem.* The title and contributions (ll. 093–098) promise an evaluation of AI-based manufacturability decisions, "including classifiers and language-model checks". In fact:
- (i) The learned rules are two GPs, two boosting models and M6. No learned manufacturability classifier, CAD-based model or language model is evaluated; Section 6.5 (ll. 999–1009) is an untested proposal.
- (ii) The decisions evaluated are one-sided upper limits on the 95th percentile of dimensional characteristics averaged over sides (ll. 1036–1037). Manufacturability in deep drawing is commonly a matter of splits and wrinkles, attribute outcomes that the framework "does not yet cover" (ll. 997–998), and real tolerances on draw-in, wall angle and depth are two-sided. With upper limits only, whether a rule's errors fall as false accepts or false rejects depends on the sign of its bias (cf. ll. 834–835).
- (iii) The evidence comes from one material, one press and two geometries, in a 3 × 3 factorial in which lubrication is mostly unresolved.
- (iv) The simulator is of low fidelity: its force effect is 2.7–5.1 times too large, and it gets the sign of the arm angle wrong.

*What would resolve it.*
- Retitle so that the title says what was done. Something along the lines of "Production-referenced operating characteristics for design-stage predictions: a deep-drawing case study" would serve, though the author will find better wording.
- Present classifiers and language-model checks as a proposal.
- Add lower or two-sided limits, using the 5th percentile with a change of sign.
- Include a short treatment of attribute outcomes, or extend the demonstration with a learned classifier for a feasibility outcome if one can be defined on these data.
- Reword the "Observed on this dataset" block of Table 5 so that it cannot be read as general guidance.

**8. The presentation is too dense for JIM's readership.**

*Problem.* The abstract (ll. 021–040) relies on terms it does not define (sibling, near-replicate, floor, decisive distance) and on parenthetical numbers. Sections 5.3–5.9 often put five to ten numbers in one sentence. Fourteen rules, plus M6 and 27 robustness variants, are hard to keep apart. The new-family distances are reported in the produced family's floor in Table 4 and in the new family's own floor in Table A2. The term "noise floor" (the GP's variance bound) collides with "production floor".

*Why it matters.* A procedure meant for practitioners has to be understood before it can be applied, and at present the reader has to reconstruct definitions from the appendix.

*What would resolve it.*
- Rewrite the abstract in plain terms with three or four key numbers.
- Add a conceptual figure showing κ(δ) and ω(δ) for one rule, with δd, δs and the guard band marked.
- Keep the pre-specified rules and the key baselines in the main text and move the rest to the appendix.
- Provide one compact table per relation, giving the best pre-specified rule, NN and the best learned rule, each with δd/δs, refit intervals and coverage.
- Rename the GP bound, for example to "noise-variance bound".
- Align the M3n/M4 naming between the paper and the code.

## 4. Minor comments

1. **Ll. 263–265 and Eq. (2).** "With per-geometry floors where geometries differ": the code (`decisions.load_floors`) scores every characteristic in its per-geometry floor. Please say so unambiguously, and state where the pooled F of Table 3 is used.
2. **Ll. 479–480 and Table 3 (minor leakage).** The floors (`alt_floor.csv`) and the nominal thickness of 0.99 mm (the grid value nearest the median thickness) are computed from all series, including the held-out one. The floors also weight the two draw-ins in the friction fit of Mc. The effect is surely small, but recomputing the floors leave-one-alternative-out would close the point.
3. **Ll. 315–322.** Please state n per relation (8, 6 and 9; 15–17 when pooled). For n = 9 the standard jackknife+ at α = 0.1 already uses the extreme values, so "at or beyond" differs by relation.
4. **Ll. 368–372.** Report the one-sided distances (false-accept and false-reject side) for every relation in the main text, and add a sentence on how the δ-dependent weight of the failing side affects the comparisons.
5. **Ll. 509–518.** Specify that in the new-setting scope the jointly held-out alternatives are resampled individually, that one block-bootstrap replicate of the truth is drawn per case and resample, and how many distinct resamples nine clusters allow.
6. **Table 4, pooled columns.** M1n, M2n and M1sn have no family term when pooled, hence 130, 325 and 77–111 floors. Explain this or omit these cells; at present they look like findings.
7. **Tables A3 and A4, ll. 776–778.** For an interpolated setting, NN, M1sn and the M5n centre coincide by construction, because 300 kN is the midpoint of a balanced design. Please say so: the interpolated stratum cannot discriminate between mean-type rules.
8. **Ll. 629–630.** Attribute the 164-floor false accept of the scaled simulation to cup depth (see Major comment 5).
9. **Ll. 688–694.** The variance shares of relation and rule depend on which rules are included, among them rules that fail by construction. Present them as descriptive, or drop them.
10. **Ll. 718–729.** Reword the lead sentence "Learning adds intervals rather than accuracy" in the light of Major comments 1 and 3, and note that the centres of M5 and M5n coincide with NN.
11. **Table A3.** Add cluster-robust intervals for coverage, the coverage of M6, and the interval score.
12. **L. 1009.** "A generative tool's manufacturability check is scored." is incomplete. Say how it is scored, or delete the sentence.
13. **Section 2.1 and Table 1 (positioning).** Engage with virtual-metrology work on the reliability of individual predictions. The reliance and global-similarity indices of automatic virtual metrology (Cheng and co-workers, e.g. Cheng et al., 2008, *IEEE Transactions on Semiconductor Manufacturing*) are conceptually close to the novelty guard and the guard band. The paper should also engage with regression with a reject option (selective regression), and with studies of uncertainty-aware predictive quality and transfer learning in manufacturing, which appear regularly in JIM.
14. **Code and data availability (ll. 1206–1216; reference Canseven 2026), to be fixed before acceptance.**
    - (a) `RELEASE_NOTES.md` refers to a `LICENSE` file that is not in the deposit, and `.zenodo.json` has no licence field, so the code is not licensed for reuse.
    - (b) The Zenodo record is "[DOI pending]". Please make the archive available to reviewers (a DOI can be reserved) and add the DOI to `CITATION.cff`.
    - (c) `requirements.txt` omits `tabulate`, which `DataFrame.to_markdown` requires in 13 scripts, so an environment built from that file alone fails when the summaries are written. `pyarrow` and `remotezip` are unpinned.
    - (d) Table A5 does not map `tuning.py` or `tune_decisions.csv`.
    - (e) The statement that the constants were fixed before the results were seen, "as the repository history records" (ll. 522–523), can be verified only if the history, or a timestamped snapshot, is part of the deposit.

    On the positive side, all checksums verify and the generated tables reproduce exactly (see the preamble to Section 3).
15. **Fig. 2.** The negative side of the symmetric-logarithmic axis has no tick labels beyond −10, and the fonts are small. Consider marking the near-replicate and resolvable sibling strata.
16. **Fig. 4.** At large margins the shares rest on few verdicts, so give the number of decided verdicts behind each point there. The filled markers for g are hard to see.
17. **Section 5.8 (ll. 843–849).** Show the cost model (costs of false accepts, false rejects and trials) in a small table or figure; the cost conclusions are hard to follow in prose.
18. **Ll. 182–184 and 258–262.** Cite the clauses of the ISO standards that define the repeatability limit and intermediate precision, so that readers can check the correspondence with Eq. (2).
19. **L. 097 and Section 6.5.** Call the six-item list a "proposed reporting checklist" rather than a standard until it has been applied beyond one dataset.

## 5. Recommendation

**Major revision.** The manuscript asks a question that matters for intelligent manufacturing: can a design-stage prediction be relied on to decide, and how close to a requirement? The evaluation design is careful, with grouped cross-validation by evidence relation, no-simulation ablations and a production-record baseline, and the work is unusually transparent and, in my checks, reproducible. The AI content, however, does not yet meet the standard the title sets for this journal:
- the GPs degenerate to the calibration mean in the new-setting relation, and to within a fraction of a floor of the nearest-setting baseline with a sibling, so the conclusions on what learning contributes are not established;
- the approaches a reader would expect (multi-fidelity GPs, calibration with discrepancy, few-shot transfer, quantile and relation-matched conformal UQ) are missing or mislabelled;
- the coverage figures reflect an imposed variance bound and carry wide uncertainty;
- the headline numbers are best-of selections made on the evaluation data;
- pooling over characteristics hides where the simulation helps.

All of this can be addressed with the existing data and code, since most of the requested analyses are cheap at alternative level, or by narrowing the title and claims to what is shown. I therefore recommend major revision rather than rejection.

## 6. Confidential comments to the editor

The paper is careful and transparent, and its tables regenerate exactly from the deposited results. My reservations concern the AI framing relative to the machine learning actually evaluated, together with the post hoc selection of rules, which the author discloses; Section 4.5 states that some of it followed internal reviews simulated with a language model. I would support publication in JIM if the revision either adds well-specified small-data learners and relation-matched uncertainty quantification, or recasts the paper as an evaluation methodology with correspondingly modest AI claims. Otherwise a design-methodology journal may be a more natural home. A reviewer with expertise in sheet-metal forming should judge the simulation matching, the measurement extraction and the assumptions behind the floor, which I did not examine in depth. Before acceptance, the code archive also needs a licence and a minted DOI.
