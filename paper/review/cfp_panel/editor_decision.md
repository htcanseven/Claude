# Editorial decision

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design (Springer), special collection "AI in Design for Manufacturing"
**Reports:** Reviewer A (design theory and methodology), Reviewer B (AI in design for manufacturing), Reviewer C (manufacturing process design and production quality)
**Date:** 5 October 2026

*Written in the persona of a fictional handling guest editor. It does not speak for the collection's actual guest editors or for any other real person.*

---

## Part 1: Decision letter to the author

Dear Hüseyin Tayyer Canseven,

Thank you for submitting your manuscript to the special collection "AI in Design for Manufacturing". Three reviewers have reported on it, and their reports are attached. I have read the manuscript, your cover letter and the three reports. Some reviewer findings rest on figures the reviewer computed from your released files. Where the decision depends on such a finding, I re-checked it against the same files, read-only, using your own estimator.

**Decision: major revision.**

All three reviewers recommend major revision, and I agree. The paper asks a question that design research and this collection need answered: when is a design-stage manufacturability prediction, AI-based or not, fit to decide? It answers that question with unusual care:

- grouped evaluation by evidence relation;
- a production-record baseline (the nearest produced setting) that AI-for-DFM studies routinely omit;
- paired ablations with and without the simulation;
- an exact estimator;
- released code from which the reviewers and I could reproduce the numbers.

As submitted, however, the paper has five problems:

- its general claims outrun a single 3×3 factorial within two geometries;
- several constructs are not yet coherent for every evidence relation;
- results that bear directly on the collection's question were computed but not reported;
- the procedure's own decision rule has not been evaluated;
- the text is too dense for RED's readers.

None of this requires new data. It does require substantial reanalysis and rewriting, which is why the decision is major rather than minor revision.

### 1. Synthesis of the reports

**Where the reviewers agree.** All three value the same things:

- **The question:** how close to a requirement a design-stage prediction can be relied on, judged against production rather than against held-out accuracy.
- **The data:** a rare open dataset in which every alternative was produced as a long series, with matched simulations.
- **The evaluation design:** grouped cross-validation, paired ablations, a production-record baseline, and bootstrap intervals that carry the uncertainty of the reference.
- **The candour** of the development record and of the threats to validity.

Each reviewer checked tables against the released result files and found no computational errors. Their reservations concern scope, constructs, model specification, reporting and framing, and they converge on six points:

1. **Generality.** The general claims go beyond the evidence: one material, one press and one tool set; a 3×3 factorial per geometry; one simulator; and only two transfers for the only change of product design. In addition, the key constructs were introduced after the first results had been seen (Section 4.5).
2. **Headline claims.** The headline that the evidence relation "governed decision fitness more than the model did" is not supported in the general form given, and neither are the RQ3 statements about simulation and learning.
3. **The new-variant relation** is largely a near-replicate relation: lubrication is resolved in only 51 of 126 contrasts. The simulation does not depend on lubrication, so it cannot contribute in this relation by construction.
4. **The floor:**
   - it depends on the protocol;
   - it excludes run-to-run variation;
   - it is not available for a new family when the decision is taken;
   - it is not positioned against the precision limits of ISO 5725.
5. **Unreported results.** The pooled scopes are defined but not reported, although Section 4.5 says that every variant tried is reported.
6. **Readability.** The text is too dense for RED's readers. It needs a worked example, fewer rules and tables in the main text, and physical units.

**Where they differ.** The reports differ in emphasis and in how much they ask.

- **Reviewer A** concentrates on design-theoretic coherence: the population behind the distances, the unevaluated decision rule of step 6, and the design literature in which the constructs belong.
- **Reviewer B** concentrates on the AI:
  - a data regime that largely fixes the learning results in advance;
  - the Gaussian-process noise model;
  - the additive-only use of the simulation;
  - a refit bootstrap that mixes relations;
  - a purely statistical treatment of trust.
- **Reviewer C** concentrates on production:
  - whether the floor measures the process or the scanner;
  - what the distances mean in capability terms;
  - confounds in the relations (force with stroke speed, and possibly lubrication with run order);
  - transfer to the processes named in the call.

They also differ on new work. Reviewer A would ideally like a second process and a forward evaluation of the procedure. Reviewer C would welcome a second process but does not make it a condition. Reviewer B asks for no new data. Section 6 below sets out what I require.

**My own assessment.** I share the reviewers' view of the paper's value and of its main weaknesses. Two further observations shape what I require.

First, the paper's most useful practical result is currently hidden. I reproduced Reviewer C's capability translation from `dec_alternatives.csv`. At the median over the 126 alternative–characteristic cases:

| Requirement position | Ppk equivalent |
|---|---|
| at the true q95 | about 0.5 |
| 3.4 floors above it | about 2 |
| 8.5 floors above it | about 4.5 |
| 16 floors above it | about 8 |

Even the best rule therefore decides reliably only where the requirement lies far from the capability. The decisions that matter for process release fall inside every decisive distance reported. That is the substance behind "when a physical trial is unavoidable", and the paper should say it plainly, in physical and capability terms.

Second, the paper's contribution to this collection is an evaluation standard for AI-based DFM support. That is how your cover letter frames it. It is not evidence about the value of machine learning in DFM in general, which a 3×3 factorial within two geometries cannot provide. The revision should adopt that framing consistently, in the abstract, in RQ3 and in Sections 6.3 and 7.

### 2. Fit to RED and to the collection

**RED.** The manuscript proposes and evaluates a framework for design decisions. It is neither a case study of an individual design effort nor a mere application of existing tools, and it is within the journal's scope. Whether it meets RED's standard of broad applicability depends on the revision, in two ways:

- the design-methodological contribution has to be argued against the design literature (R5a);
- the applicability has to be bounded by stated prerequisites, not asserted (R1).

**The collection.** The call invites work on:

- automated manufacturability checks;
- learning from design and manufacturing data;
- knowledge transfer;
- designer trust and decision support.

It also asks how AI can "support, augment, or transform engineering design reasoning in DFM". A production-referenced standard for deciding when a simulation-based or AI-based manufacturability prediction may be relied on, with a production-record baseline and explicit abstention, is within that remit. A sober answer is as welcome as an enthusiastic one.

**Is the AI content sufficient?** On its own, no. The AI content is modest: classical Gaussian-process and gradient-boosting models fitted to 6–9 distinct produced settings. What earns the paper a place in the collection is its evaluation methodology, on four conditions:

- the learned models are given a fair small-data specification;
- the results on learning across products (the pooled scopes) are reported;
- the AI-specific conclusions are conditioned on the data regime;
- the paper shows how the framework applies to AI tools other than interval regressors.

These conditions are part of R1, R3 and R5.

### 3. Required revisions (the decision depends on these)

The revisions are listed in priority order, and for each I say what would satisfy me. Every analysis requested here can be done with the released data and pipeline. References such as "A3" denote a reviewer's major comment and "A-m3" a minor comment.

#### R1. Bring every general claim into line with the evidence
*(A1, A5, A6, A7c–d, A-m1, A-m2, A-m14, A-m19, A-m20; B1, B2, B6d, B-m2, B-m5; C3a, C5, C8)*

The evidence is limited:

- one material, one press and one tool set;
- a 3×3 factorial per geometry;
- one simulator;
- two transfers between geometries that differ in three features at once.

The evidence relations, the baseline that carries the main findings and the exact estimator were added after first results had been seen.

The headline sentence on the evidence relation is not supported as written. I reproduced Reviewer A's decomposition of the log decisive distances of the ten calibrated rules, in shares of the variation:

| Relations included | Relation | Rule | Interaction |
|---|---|---|---|
| all three | 67 % | 7 % | 26 % |
| new variant and new setting only | 13 % | 72 % | 15 % |

The dominance of the relation comes from the new-family column, where the production-only rules fail by construction.

*What would satisfy it:*

- **The headline.** Replace it in the abstract, Section 6.1 and the Conclusions with a quantified statement. Either of two forms would do:
  - the best attainable distance per relation, with its interval, beside the range across rules;
  - the decomposition itself.

  Either way, say that within a family the choice of rule mattered at least as much as the relation.
- **RQ3.** State the RQ3 conclusions as conditional on this simulator and this data regime wherever they appear (abstract, Sections 5.5, 6.1, 6.3 and 7, Table 13).
  - The simulator does not depend on lubrication: its nominal value and envelope are identical across the three lubrication variants, which I confirmed in `dec_alternatives.csv`.
  - It carries a large and partly sign-inconsistent bias.
  - It overstates the blank-holder-force effect 2.6–5.1-fold.
  - It apparently does not represent the stroke-speed change at 100 kN; please confirm.
  - It enters the rules only additively.
  - Each learned model sees 6–9 distinct produced settings with two or three descriptors.
- **Inductive biases.** Explain the learners' behaviour through their inductive biases; that explanation is what will transfer to other settings.
  - Trees do not extrapolate.
  - In the median new-setting fit the GP force length scale sits at its lower bound of 10 kN, so the GP reverts to its mean.
  - Two force levels identify at most a linear trend.
- **The new family.** Present the new-family results as two illustrative transfers. Qualify, or remove from the abstract, "for a new family no rule was safe closer than 16 floors".
- **Scope in the abstract and introduction.** State that:
  - two of the three relations concern process settings on an existing tool, that is, process planning and tryout rather than early product design;
  - the demonstration uses a 95 % conformance level.

  Give one physical anchor (for example, a floor of about 0.05 mm of mid-side draw-in, and 16 floors as about 0.8 mm of draw-in or 1.3° of wall angle) and the capability anchor above.
- **Wording.**
  - Use "reliable" rather than "trusted" where the claim is statistical.
  - Replace "calibrated abstention" by naming the rules whose coverage is close to nominal. Within the family the GP intervals cover only 71–72 %.
- **Section 6.4.** Reword the validity claim. What is shown is that the metrics discriminate between rules and relations on real data. That is structural validity, and support evaluation in the terms of the design research methodology; it is not performance validity.
- **Table 13 and Section 6.**
  - Give every row of Table 13 its evidence base.
  - Move dataset-specific rows (for example, "A new design family: use the simulation for gross margins only") out of the general block.
  - State in Section 6.1 which findings are confirmatory and which exploratory.
  - Present "None is specific to forming" (Section 6.5) as an expectation, with the prerequisites stated.

#### R2. Make the unit and the two distances well defined for every relation
*(A2, A3; B-m6, B-m11, B-m12; C1, C2, C-m1, C-m3, C-m10, C-m24)*

*What would satisfy it:*

**(a) Positioning.** State that, under your stationary model, the floor is a repeatability-type limit in the sense of ISO 5725, applied to batch centres under within-run conditions. Relate it to the time-dependent process models of ISO 22514-2, and say what is new in using it as a decision unit.

**(b) Protocol and comparability.** The protocol changes the floor in two ways:

- Eq. (2) pools batch pairs at all time lags, so under drift the floor grows with the length of the series: the first 250 parts give 0.49–0.95 of the full value.
- Batch size and quantile change the floor by factors of 0.6–2.2.

Required:

- Either define the floor at a stated lag (a variogram of batch centres), or fix a reference protocol.
- Report σ_b, σ_w and the drift, so that others can recompute F for their own protocol.
- Report F/σ for each characteristic and geometry. In your data it ranges from about 0.7 (wall angle, convex) to 2.2 (cup depth, concave).
- Reword RQ1 and the Conclusions from "independently of the predictor and of the characteristic" to "on a common production-referenced scale". Add that equal distances in floors do not mean equal nonconforming fractions.

**(c) Between-run variation and measurement.**

- Label the floor as a within-run construct.
- Add to Table 12 a variant whose floor includes the between-series component, as an upper bound.
- State whether the parts were scanned in production order, and when. Then either:
  - give evidence that scanner drift is negligible (assumption A3 for drift, not only for repeatability); or
  - call the unit a production-and-measurement floor and state the consequences.
- Report the measurement resolution of each characteristic relative to its floor. The mid-side draw-in is quantised in steps of about 0.38 floors. For five of the 18 alternatives the bootstrap standard error of its q95 is zero to numerical precision, which also sets the GP noise bound to zero there.

**(d) The new family.** Every transfer case is scored in the floor of the unproduced target family, which I confirmed in `dec_intervals.csv`. A design team would not have that floor, and the per-geometry floors differ by up to a factor of 2.4. Report the new-family distances in the source family's floor and in physical units, and add a new-family branch to Fig. 1.

**(e) Weighting and sides.**

- *Weighting.* The text says that both signs are weighted equally, but `share_curves` in `decisions.py` weights every feasible verdict equally. As failing-side requirements become infeasible, the failing side loses weight:

  | Distance (floors) | Failing-side cases still feasible (of 126) | Weight of the failing side |
  |---|---|---|
  | 3.4 | 124 | 0.50 |
  | 16 | 98 | 0.44 |
  | 35 | 84 | 0.40 |
  | 108 | 63 | 0.33 |

- *Sides.* The pooled figures can also hide the false-accept side, where errors cost most. For a new setting:
  - M5n is "safe" at 5.4 floors, but its false-accept side needs 9.1;
  - the nearest produced setting's false-accept side needs 10.2 floors, against a pooled 8.5.

- *What to do.*
  - Describe the weighting exactly.
  - Give the one-sided distances (Table A2) in Table 8, as the primary figures or beside the pooled ones.
  - Give the number of feasible failing-side cases at the reported distances.

#### R3. Report the evaluation completely and make its comparisons fair
*(A4, A5; B1, B2, B3a–b, B4, B5; C4, C8)*

*What would satisfy it:*

**(a) Pooled scopes and M6.** Report the pooled scopes, in Table 8 or an appendix table, discuss them, and correct the statement in Section 4.5. They test the call's premise of learning from other products' production records, and they are mixed:

- **Decisiveness:** pooling makes most rules less decisive:
  - M5 for a new variant goes from 6.7 to 11 floors;
  - M2 goes from 23 to 53;
  - M2n goes from 19 to 325.
- **Coverage and accuracy:** pooling raises M5's coverage from 72 % to 80 %, and makes its interval centre the most accurate point predictor within the family (2.6 floors, against 3.4 for the nearest produced setting).

Also report M6 for every relation: decisive/safe distances of 95/4.7 floors for a new setting and 40/22 for a new family.

**(b) Split the new-variant relation by whether the siblings are resolvable.** Using the effect-to-scatter ratios in `alt_effects.csv`, the 90 % quantile of the absolute error of the nearest produced setting is:

| Siblings resolvable | Cases | 90 % quantile of absolute error (floors) |
|---|---|---|
| neither | 58 | about 0.8 |
| one | 34 | 2.3 |
| both | 34 | 4.8 |

Report the distances for these strata and interpret the headline 3.4 floors accordingly.

**(c) Split extrapolation by force level, and discuss stroke speed.** The nearest produced setting decides at:

| Held-out force | Relation | Decisive distance (floors) |
|---|---|---|
| 100 kN (slower stroke) | extrapolation | 11.0 |
| 500 kN | extrapolation | 4.85 |
| 300 kN | interpolation | 4.65 |

The production-only interval rules lose safety almost only at 100 kN, whereas M2 and M5 are unsafe at both ends. Report interpolation and extrapolation separately wherever "8.5 floors" is quoted.

**(d) Fair small-data baselines.**

- **GP noise.** The present lower bound is the sampling variance of q95; the median standard error is about 0.1 floor. That is an order of magnitude below the mean pairwise differences between the lubrication series (0.5–3.0 floors by characteristic). Bound the noise by the between-run variation instead: for example, a nugget estimated from the quasi-replicate lubrication series, or a random effect per series.
- **Jackknife+ for M3 and M4.** It needs no extra fits.
- **A scaled simulation rule** (q95 ≈ a + b·s₀). I reproduced Reviewer B's version: it decides at 4.85 floors for a new variant, 19 for a new setting and 122 for a new family. Your conclusions survive, but "within a family it adds nothing" should then refer to the additive use of the simulation.

**(e) A credible production-informed baseline for a new family,** so that the new-family comparison is not decided by construction. One example is the drawing nominal plus the source family's deviation, for characteristics that have a nominal.

- For the wall angle, this predicts the new family's q95 within 0.33 floors at the median and 1.75 at the 90 % quantile. M1 achieves 5.3 and 15.9. These are Reviewer C's figures, which I reproduced.
- For the arm angles it would fail, and that contrast shows where the simulation is needed.

**(f) Uncertainty that preserves the relation.**

- *The problem.* In the refit bootstrap (`jobs_for` and `refit_one` in `robustness.py`), the "within" scope keeps its label when both siblings of a target are missing from a resample, which affects about 13 % of target copies. Duplicated alternatives also shrink the largest-residual margins. As a result, some point estimates lie outside their own refit intervals; for example, M2's within-family safe distance is 0.15 floors, against a refit interval of 0.40–5.76.
- *What to do.*
  - Resample in a way that preserves the relation: whole force levels or lubrication patterns within a geometry, or the all-subsets design of Table 9 conditional on the relation.
  - Give paired refit intervals for the key comparisons: the nearest produced setting against M5 and against M5n, M5 against M5n, and M2 against M2n.
  - Do not interpret differences of two or three floors.

#### R4. Specify and evaluate the procedure's own decision rule, and work one decision through
*(A7a, A7b, A7e, A9a, A-m6; B6a–b; C3d, C6)*

*What would satisfy it:*

**(a) Specify and evaluate step 6.**

- *The problem.* Step 6 returns a trial "when the margin lies below the rule's safe distance". But δ_s is defined on the true margin, which the designer cannot observe. Applied to the observable margin, step 6 defines a new rule that has not been evaluated, and how conservative that rule is depends on which margin is meant.
- *The evidence.* I reproduced Reviewer A's figures. At a true margin of 10 floors, the share of designs sent to trial is:

  | Relation and rule | Rule alone | Step 6, margin from interval edge | Step 6, margin from interval centre |
  |---|---|---|---|
  | new setting, M2 | 25 % | 69 % | 38 % |
  | new setting, nearest produced setting | 0 % (always decides) | 33 % | 33 % |
  | new family, M2 | 26 % | 87 % | 66 % |

  At a true margin of 20 floors, M2 under step 6 still sends 61 % of new-family designs to trial (edge reading).
- *What to do.*
  - Specify which margin step 6 compares with δ_s.
  - Derive any threshold on the observable margin from the reliability-by-margin analysis of Section 5.5. State its requirement prior: `reliability()` weights the grid points within ±20 floors equally, and the grid is dense only within ±10 floors.
  - Report the operating characteristics and trial rates of the procedure's actual decision rule for each relation.

**(b) A running worked example from Section 3 onwards,** for one alternative and one characteristic, showing:

- its floor in millimetres;
- a requirement;
- the relation and the guard;
- the intervals, verdicts and margins of three rules;
- what step 6 returns, with the reliability at that margin;
- what production showed.

Say who takes the decision, at which milestone and with what evidence in hand.

**(c) The trial's own error.** State how it enters: a trial of 100 parts reproduces q95 only to about one to one and a half floors, and a separate run may differ by more.

A nested or prequential evaluation of the whole procedure is encouraged but not required (see Section 6). If you do not do it, state the resulting selection optimism plainly in Sections 6.2 and 6.6.

#### R5. Make the contribution legible to RED's readers and reusable for this collection, in a shorter paper
*(A8, A9; B7, B-m1 to B-m3; C7, C8, C-m26, C-m27)*

*What would satisfy it:*

**(a) Design-theory positioning.** Add a short positioning subsection, and rewrite Section 6.4 as an argument that states, strand by strand, what the framework adds to:

- variant, adaptive and original design, and product-family and platform design;
- the use of process-capability data in design (the nearest produced setting is in effect a capability-database look-up);
- the release of preliminary information in overlapped development;
- set-based concurrent engineering;
- prototyping strategy;
- the V&V distinction between validation and application domains, and risk-informed credibility assessment (ASME V&V 40).

Distinguish what the safe distance quantifies, the predictive-uncertainty part of a margin, from design margins that absorb change.

**(b) Applying the framework to other AI-based DFM tools.** Add a short section, of about two pages, covering:

- **A black-box formulation.** Any tool that returns meets, fails or trial for a stated requirement can be scored by sweeping the requirement. A classifier is scored at its operating threshold; an LLM-based check is given the requirement value in the prompt.
- **A minimal reporting standard:**
  - the floor, with its protocol and variance components;
  - the distances by relation, with refit intervals;
  - coverage;
  - the nearest-produced-setting and no-simulation baselines;
  - guard performance.
- **Relations for continuous novelty,** for example a distance in descriptor space, or whether the new design lies inside or outside the hull of produced designs.
- **The minimum evidence required,** with a compact table mapping what a batch, a run and a floor would be for additive manufacturing, injection moulding, machining and casting.

Add "machine learning" or "artificial intelligence" to the keywords. In Section 2.1, cite a few AI-for-DFM studies that were evaluated by held-out accuracy only, to make the evaluation gap concrete.

**(c) Density and length.**

- Add a notation and glossary table.
- Keep a core set of rules in the main text (I suggest M0, M1, M2, M5, M5n and NN) and move the others to the appendix.
- Move to Electronic Supplementary Material:
  - Tables 5, 6, 7, 10 and 12;
  - Tables A5–A9;
  - much of Sections 4.3, 5.1 and 5.3.
- Let the tables carry the numbers and the text the interpretation.
- Rewrite the abstract around the design question.

The main text must not grow; Section 8 gives the target.

### 4. Recommended revisions

These would materially strengthen the paper. Where time is short, narrowing a claim is an acceptable alternative to a new analysis.

1. **Quantify the prerequisites** *(A1c, C6, B-m20).*
   - Recompute the distances with the calibration alternatives truncated to their first 50, 100 and 250 parts. That shows whether tryout-scale evidence supports the framework.
   - Derive a minimal evidence protocol from the results.
   - Say what replaces the floor when no consecutive series exist.
2. **Capability-anchored operating characteristics** *(C3a, C-m23).* Report the shares of correct verdicts at requirement positions where each alternative has Ppk = 1.0, 1.33, 1.67 and 2.0, or add a capability axis to Fig. 3. Discuss early how a high conformance level would be handled (A-m5).
3. **The designer's view** *(B6).*
   - Add a figure of the share of correct verdicts against the observed margin, by relation and rule, with the requirement prior stated.
   - Discuss briefly when an abstention should go to an expert rather than to a trial.
   - Discuss the transparency of the nearest produced setting compared with a GP interval.
   - Give concrete hypotheses for the designer study proposed as future work.
4. **A surrogate contrast** *(A6).* The released surrogate of the simulations reproduces the simulation closely, while the simulation misses production by tens of floors. That makes concrete that a surrogate's accuracy says little about its decision fitness. Note that `ds_surrogate.csv` predates the current characteristic definitions (its concave mid-side draw-in floor is 0.079 mm, against 0.050 mm in Table 4), so it must be recomputed.
5. **Borrowing strength across families** *(B3c).* Fit a multi-task (coregionalised) GP or a hierarchical model across families, or explain why that is infeasible.
6. **Run and measurement metadata** *(C2, C4c, C-m7, C-m21).*
   - Report run order and dates, start temperatures, coils, warm-up handling, and the scanning set-up and timing.
   - Regenerate the in-line drift analysis with the current definitions and report it briefly.
   - Add a Table 12 variant that excludes the thermal transient.
7. **Characteristic roles and requirement forms** *(C3b, C3c, C-m9, C-m19, A-m17, B-m17).*
   - Label each characteristic as a product requirement or a process indicator.
   - Illustrate two-sided limits for the cup depth or the wall angle.
   - State the design angles.
   - Either complement the ISO 2768-1 scenario with requirements anchored after die compensation, or stop describing it as giving "realistic margins". Only 32 of its 108 decisions lie within 5 floors of the limit, and only six of those concern failing alternatives.
8. **Per-characteristic distances and costs** *(A3, A-m10, C3d, C-m20).*
   - Discuss how a team would obtain per-characteristic distances from realistic amounts of data.
   - Make the cost and the error of a trial specific to the evidence relation.
   - Justify the cost ratios, or show a sensitivity map.
9. **Separate definitional offsets from physical simulation error when reporting M0** *(C5, C-m13),* and qualify "reliable beyond about 108 floors" in Table 13 (see Section 6).
10. **Calibration design and applicability guard** *(A-m11, A-m12, B-m10, C-m18).*
    - Rename the "calibration design", or formulate it as a design problem.
    - Shorten the applicability guard, or relate it to established applicability-domain methods.

### 5. Optional extensions, left to you

- **A second application in another process** *(A1a, C7, B4),* for example a between-build floor from the PA12 anchor specimens for build-orientation decisions.
- **A forward evaluation of the whole procedure** *(A7b):* a nested or prequential evaluation, and a comparison with current-practice baselines in wrong releases, trials and expected cost.
- **The value of simulation fidelity** *(A6):* a controlled or semi-synthetic analysis that gives the value of fidelity in floors.
- **A fuller calibration of the simulation** *(B2, C5):* the full Kennedy–O'Hagan formulation, with friction calibrated jointly with a discrepancy term, or Mc with a pressure-dependent friction law.
- **Methods aimed at the error rates being scored** *(B3d, B-m9):* conformal risk control, Learn-then-Test or weighted conformal prediction, and risk–coverage curves.
- **Renaming the "production floor"** *(B-m1),* to avoid the shop-floor reading. At a minimum, define the term prominently.

### 6. Where I overrule or qualify the reviewers

Where this letter and a report differ, follow this letter.

| Request | My decision | Reason |
|---|---|---|
| Second dataset or process (A1a "ideally"; C7 "ideally"; B4 "if at all possible") | Encouraged, not required | The one attempt (PA12) failed the first prerequisite, and suitable open data may not exist. A second demonstration would make this a different paper and cannot reasonably be done within the collection's timeline. Narrowed claims and stated prerequisites (R1, R5b, recommendation 1) answer the concern for this paper. |
| Forward (nested or prequential) evaluation of the procedure (A7b) | Encouraged, not required. Required instead: specify and evaluate step 6 (R4a) | Step 6's operating characteristics can be computed from the stored intervals. A full nested evaluation with six to eight calibration alternatives per fold is heavy, and its inner qualification would be noisy. The decision does not depend on it, provided the selection optimism is stated. |
| Usefulness evaluation with design teams (A7d, B6d, C8) | Not required | It is outside the scope of a first evaluation. Required instead are the correct methodological label (R1) and concrete hypotheses for future work (recommendation 3). |
| Relabel the new-variant relation as a "replicate bound" (B1b) or as prediction of a near-replicate run (C4a) | Qualified | The relation is mixed: in 34 of 126 cases both siblings are resolvably different, and there the nearest produced setting's 90 % error is 4.8 floors. Reviewer A's stratification (R3b) is the right fix, not a blanket relabelling. |
| Restrict the requirements to characteristics a drawing would carry (C3b) | Not required | Draw-in and waviness are legitimate tryout and process-planning quantities, and removing them would thin an already narrow evidence base. Labelling the roles and illustrating two-sided limits suffice (recommendation 7). |
| Remove definitional offsets before scoring M0 (C5) | Qualified | M0 should remain the raw nominal simulation as used in practice. But Reviewer C's point is material. In my check, removing only the near-constant cup-depth offset brings M0's decisive distance from 108 to about 65 floors. (I used the offset's observed median as a stand-in for its definitional value.) Report the split and reword Table 13; no ranking changes. |
| Full Kennedy–O'Hagan, multi-task GP, risk-control methods (B2, B3c, B3d) | Recommended or optional | The cheap fixes required in R3d are enough to make the comparison fair. The others would improve it. |
| Evidence from the in-line drift analysis (C2) | Qualified | Reviewer C draws on `inline_drift.csv`. As Reviewer C notes (C-m28), that file was produced with the superseded mid-side draw-in definition (floor 0.085 mm). For the other six characteristics its floors agree with the current ones to within 2 %, so his inference is probably robust, but regenerate the file before relying on it either way. |

**Reviewer figures I re-checked.** Every figure listed below reproduces from your released files:

- Table 8 and all the pooled-scope numbers;
- Reviewer A's decomposition, sibling split and step-6 trial rates;
- the feasible failing-side counts, and the target-family floors of the transfer cases;
- Reviewer B's reproduction of M1 and scaled rule, the GP length scale at its bound, the refit intervals, M6 and the pooled coverage;
- Reviewer C's capability translation and force-level split, the wall-angle baseline, the structure of the ISO 2768-1 scenario, and the count of 42 lubrication contrasts with a bootstrap probability of resolvability of at least 0.95.

There are small discrepancies, none of which changes a request:

- **A3.** At the 16-floor safe distance for a new family, the failing side carries 44 % of the weight. A's "one third to two fifths" applies from 35 floors upwards.
- **B-m11.** The mid-side draw-in takes 71 distinct values, not 102. The higher count comes from floating-point noise; the step of 0.019 mm is as stated.
- **B3a.** The "0.7–4.4 floors" are mean ranges of the three lubrication series; the mean pairwise differences are 0.5–3.0 floors. The argument holds either way.
- **C4c.** The start temperature rises in the order coarse, medium, fine strictly in only two of the six geometry–force cells. Run order is therefore a question for you to answer, not an established confound.
- **B-m16.** The sawtooth of M1 appears in Fig. 4(b, c, e, f), not in panel (a).

### 7. Minor and editorial points

Please respond to every minor comment in the three reports. The following have factual consequences:

- **p. 18:** "every calibrated rule improves by an order of magnitude" is not correct for Mc and M2, which improve four- to five-fold.
- **p. 19:** "exactly the n/(n+1) = 8/9". With the offset estimated from the same residuals, the guarantee is at least (n−1)/(n+1), and the cases are not exchangeable, so the agreement with 8/9 is coincidental. The footnote to Table 2 ("at most") needs the same correction.
- **Section 4.5:** "every variant tried is reported" (see R3a).
- **pp. 2 and 14:** "at 95 % confidence" should read "in 95 % of batch pairs".
- **p. 2, citations:**
  - Liu et al. (2026) concerns causal failure reasoning in design FMEA, not automated manufacturability checks.
  - In the Whitney (1996) sentence, the link to production variation should be clearly your own.
- **Rule names:** name the paired rules consistently (for example M3/M3n). State in Section 3.3 that the nominal simulation and the envelope do not depend on lubrication.
- **Table 6:** report minimum resolvable changes beyond the 200 kN interval as "beyond the interval", not as numbers.
- **Table 8:** give bootstrap intervals for at least the headline rules.
- **Fig. 3:** use a palette that is safe for readers with colour-vision deficiency, and mark δ_d and δ_s on each panel.
- **Section 6.3:** state the question directly rather than referring to "the call for this collection".
- **References:** complete the NeurIPS entries, and give the place of publication for AIAG (2010).

### 8. Practical instructions for the resubmission

- **Response document.**
  - Begin with a short map of where R1–R5 are addressed, with page and line numbers in the revised manuscript.
  - Then respond point by point to every numbered comment of Reviewers A, B and C. Quote each comment and state either "changed (where)" or "not changed (why)".
  - Where I have marked a request as optional or qualified, you may refer to this letter.
- **Versions.** Upload a clean manuscript and a marked-up version (for example produced with latexdiff).
- **New analyses.** For every new number, name the script and the result file that produce it. Regenerate or remove the result files that no longer match the paper's definitions (`inline_drift.csv`, `ds_surrogate.csv`, `budget_curve.csv`).
- **Code and data archive.** Deposit a versioned archive of the code and the extracted feature tables with a DOI (for example on Zenodo) at resubmission, not at acceptance, and cite it in the availability statements. The re-review should not rely on a mutable repository.
- **Length.**
  - The main text, from the abstract to the conclusions, must not be longer than now. Aim for about a fifth shorter, roughly 22–23 pages in the present format.
  - Keep no more than about eight tables and five figures in the main text, with the rest in the appendix or the Electronic Supplementary Material.
  - If the additions (R4b, R5a, R5b) make this hard, cut numerical detail from Sections 4 and 5.
- **Declaration on generative AI.** Keep it, and update it if the assistant's role changed during the revision.
- **Timeline.**
  - Please submit the revision within 12 weeks, by 28 December 2026, so that the paper stays on the collection's schedule.
  - If you need longer, write to me by 30 November 2026.
  - If time is short, finish R1–R5 before any recommended item.
  - I intend to send the revised manuscript to all three reviewers.

I look forward to receiving the revised manuscript.

Yours sincerely,

The handling guest editor
Special collection "AI in Design for Manufacturing", Research in Engineering Design

---

## Part 2: Confidential note to the Editor-in-Chief

**Recommendation: major revision.** The three reviewers (design theory, AI in DFM, manufacturing) concur independently. The manuscript passes RED's criteria: it proposes and evaluates a framework for design decisions, not a case study or an application of tools. It is technically careful and unusually transparent. The reviewers and I re-derived the key numbers from the released code and result files, and everything I checked reproduces; I have no integrity concerns. Its weaknesses are:

- over-general claims drawn from one 3×3 factorial within two geometries;
- constructs not yet coherent for every relation;
- unreported results (the pooled scopes) that bear directly on the collection's question;
- an unevaluated procedure;
- excessive density (38 pages, 22 tables).

All of these can be fixed without new data. The author declares the use of an LLM assistant for code, analysis and drafting, in line with Springer policy. I have asked for a DOI-archived code release at resubmission, so that the re-review does not depend on a mutable repository.

**Chances and risks.** If R1–R5 are addressed well, I expect a second round of minor revisions and eventual acceptance; I would put the chance at about two in three. There are five risks:

- **Scope of the AI content.** The AI is classical small-data regression. The paper belongs in this collection as an evaluation methodology for AI-based DFM support, not as evidence about machine learning in DFM, and I have made that framing a condition. If the revision does not deliver it, I would suggest treating the paper as a regular RED submission rather than as part of the collection.
- **Generality.** The evidence comes from one process and one dataset. That is acceptable for a methodology paper only if the claims are narrowed and the prerequisites stated. I deliberately did not require a second dataset, a forward evaluation of the procedure or a designer study, which would turn this into a different paper and could not be done within the timeline.
- **Length.** The revision must add a worked example, positioning and a section on reuse while still becoming shorter. I have set a target.
- **Timing.** The revision is due on 28 December 2026, just before the collection's submission deadline of 31 December 2026, so any second round would fall in early 2027. Please confirm that a paper submitted before the deadline may complete its review after it.
- **Reviewer load.** The three reports are long and detailed. Reviewers B and C have offered to review the revision. If the second round concerns only minor points, I will handle it myself.
