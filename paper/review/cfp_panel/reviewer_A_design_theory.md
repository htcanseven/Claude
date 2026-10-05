# Referee report: Reviewer A

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Reviewer focus:** design decision-making under uncertainty, design margins, verification and validation planning, evaluation of design support

---

## 1. Summary of the submission

The manuscript proposes a framework for judging whether a design-stage prediction is fit to decide a manufacturability question, measured against what production actually delivers.

Its unit, the *production floor*, is the 95 % quantile of the difference between the centres of two 50-part batches of one design. Decision rules that return meets, fails or trial are summarised by two distances in floors:
- the *decisive distance*, beyond which at least 95 % of verdicts are correct;
- the *safe distance*, beyond which at most 5 % are wrong.

Both are evaluated separately for three relations between a new design and the produced evidence: a sibling of a produced setting, a new process setting, and a new family. A calibration budget, applicability guards and a six-step procedure complement them.

The framework is demonstrated on an open deep-drawing dataset of 18 geometry–force–lubrication alternatives of 500 parts each, with matched finite-element simulations. Twelve rules are scored, from the nominal simulation to Gaussian-process and gradient-boosting models, and each calibrated rule is also scored without the simulation.

The author concludes that the evidence relation governs decision fitness more than the model does. The nearest produced setting is the most decisive rule within a family, the simulation helps only for a new family, and learned models add abstention rather than accuracy. Guidance for design practice is derived and split into general and dataset-specific parts.

## 2. Assessment

- **Originality: adequate.** The combination is new for design-stage manufacturability decisions: a production-defined unit, operating-characteristic distances for three-way verdicts, and stratification by evidence relation. Each component, however, is established: repeatability limits, guard-banded conformity decisions, OC curves and indifference zones, grouped cross-validation and applicability domains.
- **Significance for design research: adequate.** When a design-stage prediction is fit to decide is a central question for verification planning and margin management. The design-theoretic implications (Section 6.4), however, are asserted rather than developed, and they rest on one dataset.
- **Significance for the collection (AI in DFM): adequate.** The paper addresses trust in, and the evaluation of, AI-based DFM support, and delivers a useful sober result: learned models do not beat the nearest produced setting. The AI content is classical and modest, and product-design (geometry) decisions are represented by only two transfers.
- **Technical soundness: adequate.** The evaluation is careful, exact and reproducible; Table 8 reproduces from the released results. Several constructs are not coherent for every relation (the floor for a new family, the population behind the distances, the sibling relation), and the procedure's own decision rule is not evaluated.
- **Evidence supports the claims: weak.** The dataset-level numbers are well supported. The general claims go beyond one dataset, two product geometries and an unevaluated procedure: that the relation governs more than the model, the "general" guidance of Table 13, "which design-stage decisions can be trusted", and empirical performance validity.
- **Clarity, organisation and length: weak.** The structure is logical and the language precise, but the prose is extremely dense with numbers. The paper carries 22 tables, twelve rules, about a dozen coined terms and no worked example; RED readers will struggle to extract the design message.
- **Positioning and references: adequate.** Coverage of V&V, calibration, conformal prediction, conformity assessment and testing strategy is good. The design-theory strands in which the constructs naturally belong are missing (variant and platform design, process-capability data in design, preliminary-information release, set-based design), as is ISO 5725.
- **Fit to RED: adequate.** This is not a case study of an individual design effort, and it passes the desk-reject criterion. In its present form, however, it reads as a statistical evaluation study; the design-methodological contribution needs to be made explicit, and its applicability shown or bounded.

## 3. Major comments

### Strengths

The paper has real strengths, and the comments below are meant to make them count for RED's readership.

- **The question.** It asks a question that design research has mostly left to intuition: how close to a requirement can a design-stage prediction be trusted, judged against production rather than against held-out model accuracy?
- **The data.** It uses a rare open dataset in which every alternative was produced as a long series, and it releases a pipeline that reproduces the results. I re-derived Table 8 from `results/dec_resolution.csv`.
- **The evaluation design.** It is better than is usual in AI-for-DFM work:
  - grouped cross-validation by evidence relation;
  - paired with/without-simulation ablations;
  - a production-record baseline (the nearest produced setting) that such studies routinely omit;
  - an exact estimator;
  - a block bootstrap that carries the uncertainty of the reference, plus a refit bootstrap.
- **Transparency.** The development record (Section 4.5) and the threats to validity are unusually candid.
- **Substantive findings.** Several are useful well beyond deep drawing, if suitably qualified:
  - learned models add abstention rather than accuracy;
  - intervals are calibrated only under exchangeability;
  - "what a produced alternative is worth depends on its relation to the designs to come".

Where I quote figures computed from the released result files (`results/*.csv`), these were read-only checks. I give them so that the author can verify and, if appropriate, adopt them, not as a substitute for the author's analysis.

### 1. Broad applicability is claimed but not yet shown (Abstract; Sections 1, 4.1, 4.5, 6.5, 6.6, 7)

**Problem.** The framework is evaluated on a single dataset:
- one material, one press and one tool set;
- a 3×3 factorial of blank-holder force and lubrication per geometry;
- two geometries that differ in three features at once (Section 4.1).

Within a geometry, the "new designs" are process settings on an existing tool. The only change of product design, the geometry, enters solely through the new-family relation, which rests on two transfers (Section 6.6). The one attempt to apply the framework elsewhere (PA12 powder bed fusion, Section 6.5) failed its first prerequisite.

In addition, the author's own commendably transparent development record (Section 4.5) shows that three central elements were introduced after first results had been seen:
- the grouped schemes that define the evidence relations;
- the nearest-produced-setting baseline that carries the main findings;
- the exact estimator.

The constructs were therefore shaped on the data that evaluate them.

**Why it matters.** RED's criterion is design theory or methodology with broad applicability. With one dataset from which the key constructs emerged, the evaluation is exploratory. The following statements are hypotheses, not findings:
- "None is specific to forming" (Section 6.5);
- "The findings show which design-stage decisions can be trusted and when a physical trial is unavoidable" (Abstract);
- the "general" block of Table 13.

**What would resolve it.**
- (a) Ideally, a second application in another process. Section 6.5 notes that the PA12 data contain eight identical anchor specimens per build. A floor taken from these anchors, or from the residuals of a model of orientation, build and position, would allow decisive and safe distances to be computed for build-orientation decisions. These are canonical design-for-AM decisions and squarely within the collection's scope.
- (b) If that is not possible, narrow the claims throughout and present the evidence-relation findings as hypotheses for confirmation.
- (c) In either case, state the prerequisites quantitatively.
  - The calibration budget (Section 5.6) counts produced alternatives but always uses all 500 parts of each. Recomputing the distances with the calibration alternatives truncated to their first 50, 100 or 250 parts would show whether tryout-scale evidence supports the framework. That is what a design team typically has before release.
  - Say also what replaces the floor when no consecutive series exist, for example a replicate-based or tolerance-based unit.
- (d) State in the abstract and the introduction that two of the three relations concern process settings on one tool. Readers can then place these decisions in tryout and process planning, rather than in the early product design where the call locates DFM.

### 2. The production floor as a unit: positioning, protocol dependence and the new-family case (Sections 2.5, 3.2, 3.6, 5.1; Tables 4, 5, 12; Fig. 1)

**Problem.**
- (a) **Positioning.** Under the stationary normal model of Section 3.2, F = 1.96·√2·√(σ_b² + σ_w²/B). This is the repeatability limit of ISO 5725-6 (r = 1.96·√2·σ_r) applied to batch centres under within-run conditions. The effect-to-scatter ratio and the minimum resolvable change are close relatives of least-significant-difference and minimum-detectable-change concepts. None of this lineage is cited; Section 2.5 positions the floor only against capability indices and measurement systems analysis.
- (b) **Protocol dependence.**
  - The first 250 parts give 0.49–0.95 of the full value.
  - Batch size and quantile change the floor by factors of 0.6–2.2 (Section 5.1), and the distances rescale accordingly (Table 12).
  - Eq. (2) pools all batch pairs regardless of their separation in time, so under drift the floor grows with the length of the series.
- (c) **The new-family case.** The floor of a new family does not exist before that family is produced.
  - In the evaluation, new-family cases are expressed in the floor of the unproduced target family. I confirmed this in `results/dec_intervals.csv`: every transfer case carries the target geometry's floor.
  - The per-geometry floors differ by factors of up to 2.4 (bottom dome: 0.0034 against 0.0082 mm) and 1.8 (corner draw-in) (Table 4).
  - Step 2 of the procedure, carried out "once per design family" (Fig. 1), therefore cannot be executed in the very situation where, by the paper's own results, a trial is most needed.
- (d) **Between-run variation.** The floor excludes variation between runs. At 95 %, that variation ranges from 1.2 floors (waviness) to 9.8 floors (dome) (Table 5). Characteristics whose run-to-run variation is large relative to their within-run drift will show long distances under every rule.

**Why it matters.** The unit is the paper's main conceptual novelty. Two claims depend on it being well defined, portable between studies, and available when the decision is taken:
- that it expresses fitness "independently of the predictor and of the characteristic" (RQ1; Section 7);
- that it makes distances "comparable across characteristics and predictors" (Section 2.4).

**What would resolve it.**
- Position the floor explicitly as a repeatability limit of batch centres (ISO 5725), and say what is new in using it as a decision unit.
- Either make the definition lag-specific (for example, a variogram of batch centres evaluated at a stated time lag) or prescribe a standard protocol, so that floors can be compared between studies.
- For a new family, report distances in the source family's floor, which is what a design team would have, and in physical units. Add a new-family branch to Fig. 1.
- Reword RQ1 and the Conclusions from "independently of" to "on a common production-referenced scale", and discuss the between-run component.

### 3. The population behind the decisive and safe distances changes with the distance (Section 3.4; Tables 8, A2, A5)

**Problem.** κ(δ) and ω(δ) are pooled over cases and over both signs, with "both signs weighted equally and requirements below zero excluded". Because negative requirements are excluded, the failing side drops out first for characteristics close to zero.

From the released intervals, the failing-side requirement is feasible for:

| Distance (floors) | Feasible failing-side cases (of 126) |
|---|---|
| 3.4 | 124 |
| 16 | 98 |
| 35 | 84 |
| 108 | 63 |

The concave arm angle leaves the failing side at 3–8 floors, the dome at 7–17 and the waviness at 15–40. Two consequences follow:
- At the distances reported for a new family and for the nominal simulation, the failing side carries one third to two fifths of the weight, not one half.
- Long distances describe a different mix of characteristics from short ones.

Separately, the pooled distances average over seven characteristics, whereas a design decision concerns one characteristic. A per-characteristic distance rests on 18 cases; in Table A5, one wrong verdict moves a share by 2.8 points.

**Why it matters.** The distances are offered as operating characteristics with which a design team chooses rules and plans trials. If their population shifts with δ, a 3-floor distance and a 108-floor distance are not statements about the same set of decisions. Large distances are then dominated by false rejects on characteristics far from zero.

**What would resolve it.**
- Describe the weighting precisely, and report with Table 8 how many failing-side cases are feasible at each reported distance.
- Consider making the one-sided distances (Table A2) primary, since they also match how errors cost. Alternatively, restrict the pooled distances to the range in which every case is feasible.
- Discuss how a design team would obtain per-characteristic distances from realistic amounts of data.

### 4. The evidence relation: the sibling relation mixes replicates with variants, and the relevance of evidence is not reported (Sections 3.5, 4.4, 4.5, 5.2, 5.4)

**Problem.** Lubrication is resolved in only 51 of 126 contrasts (Table 6), and Section 5.2 itself calls a lubrication variant a "near-replicate".

I split the new-variant cases using the paper's own effect-to-scatter ratios (`results/alt_effects.csv`, which is based on the pooled floor). For each split I took the 90 % quantile of the absolute error of the nearest produced setting; for a point rule, this equals its decisive distance.

| Sibling contrasts (ESR) | Cases | 90 % quantile of NN error (floors) |
|---|---|---|
| neither sibling resolvable (both ESR < 1) | 58 | about 0.8 |
| one sibling resolvable | 34 | about 2.3 |
| both siblings resolvable | 34 | about 4.8 |

M5 and M5n behave alike. The headline "within about 3 floors" therefore blends the run-to-run reproducibility of q95 with the prediction of genuinely different variants.

Two further problems:
- The relation is defined categorically, on one ordered factor. A continuous design space would need a distance.
- The pooled scopes are defined in Section 4.4 but appear in no results table, although Section 4.5 states that every variant tried is reported.

In `results/dec_resolution.csv`, adding the other family's alternatives to the calibration set makes most rules far less decisive (decisive distances in floors):

| Rule | New variant: within family | New variant: pooled | New setting: within family | New setting: pooled |
|---|---|---|---|---|
| M5 | 6.7 | 11 | 18 | 33 |
| M2 | 23 | 53 | 18 | 53 |
| M2n | 19 | 325 | (not checked) | (not checked) |

**Why it matters.** The evidence relation carries the paper's main claim. Its value for design theory is that it tells a team which evidence is relevant to a coming design. Separating replication from variation, and showing that irrelevant evidence costs decisiveness, would make that contribution precise. As it stands, much of the sibling result is replication presented as a design finding.

**What would resolve it.**
- Split the sibling relation by effect-to-scatter ratio (sibling unresolved, sibling resolved) and report the distances for each.
- Report the pooled scopes; they bear directly on RQ2, which asks about both the amount and the relevance of evidence.
- Propose how the relation generalises beyond a factorial. Two options are a distance in descriptor space, or the effect-to-scatter ratio of the predicted difference to the nearest produced alternative.

### 5. The headline claim that the relation "governed decision fitness more than the model did" (Abstract; Sections 6.1, 7)

**Problem.** I decomposed the logarithms of the decisive distances in Table 8 for the ten calibrated rules (M1, Mc, M2, M3, M5, M1n, NN, M2n, M4, M5n). The decomposition is a two-way partition of sums of squares, without replication. Share of variation explained:

| Distances | Relations included | Relation | Rule | Interaction |
|---|---|---|---|---|
| decisive | all three | 67 % | 7 % | 26 % |
| decisive | new variant and new setting only | 13 % | 72 % | 15 % |
| safe | all three | 64 % | 15 % | 21 % |
| safe | new variant and new setting only | 35 % | 49 % | 16 % |

The dominance of the relation therefore comes from the new-family column. There, the five production-only rules fail by construction, because they have no information about the other geometry, and the column rests on two transfers.

Within a family, the choice of rule changes the decisive distance by a factor of 8 for a new variant (3.4–27 floors) and 4.6 for a new setting (8.5–39). Moving from a new variant to a new setting changes the best rule's distance by a factor of 2.5.

**Why it matters.** This is the sentence that readers will remember and cite. It suggests that the choice of model is secondary, whereas within a family it is the larger effect.

**What would resolve it.**
- Quantify and reword the claim, for example: "the best attainable fitness depended strongly on the relation; within a family the choice of rule mattered at least as much".
- Present the new-family result as an observation on two transfers with one simulation.
- Consider adding a credible production-informed transfer rule, so that the new-family comparison is not decided by construction. One example is scaling the source family's capability by the simulated difference between the families.

### 6. What simulation and learning contribute: the conclusions concern this simulation and this evaluation design (Abstract; Sections 3.3, 5.3, 5.5, 6.3)

**Problem.** The conclusion that "the simulation contributed only to the new family" has two structural ingredients.
- **The simulation cannot see lubrication.** The nominal simulation and the envelope used by M0, M0w, M1, M2 and M5 do not depend on lubrication. In `results/dec_alternatives.csv` they are identical for the three lubrication variants of each geometry and force. A new variant differs from its siblings only in lubrication, so in that relation these rules' simulation input cannot, by design, distinguish the new design from its siblings.
- **Across forces, the simulation is poor.**
  - Its blank-holder-force effect is 2.6–5.1 times too large.
  - The concave arm angle has the wrong sign.
  - The material model is undocumented.
  - Extraction noise reaches 9.8 floors (Sections 4.2, 5.3).

As applied here, the framework cannot separate "simulation adds nothing" from "this simulation is poor here".

**Why it matters.** RQ3 is the paper's most quotable message for a collection on AI in DFM. Generalised beyond this simulation, it would mislead.

**What would resolve it.**
- Qualify RQ3 throughout as a finding about this simulation and this evaluation design, and explain why the simulation cannot contribute in the sibling relation.
- A stronger option, and a genuinely methodological result, would be a controlled or semi-synthetic analysis. Replace the simulation's force trend with the production trend plus a controlled bias or trend error, and show how the distances respond to simulation fidelity. That would give a value of fidelity expressed in floors.
- For the collection's readers, report a contrast the released code already supports.
  - The code evaluates a Gaussian-process surrogate of the simulations (`scripts/design_space.py`; `results/ds_surrogate.csv`).
  - For most characteristics the surrogate reproduces the simulation to within about one to two floors; the error is larger for the dome and the convex waviness.
  - The simulation itself misses production by tens of floors, up to 109 (Table 7).
  - This makes concrete the point the collection most needs: a surrogate's accuracy against its simulation says little about decision fitness against production.
  - The stored file appears to predate the current characteristic definitions (its concave mid-side draw-in floor is 0.079 mm, against 0.050 mm in Table 4), so it would need recomputing.

### 7. The procedure and the guidance for practice are not evaluated as such (Section 3.6, Fig. 1; Sections 3.4, 6.2, 6.4; Table 13)

**Problem.**
- (a) **Step 6 defines a new, unevaluated rule.** Step 6 returns "a trial when the guard fires or the margin lies below the rule's safe distance". The safe distance is defined on the true margin, which the designer cannot observe. Applied to the observable margin, it defines a new decision rule that is not among the twelve evaluated. I recomputed it from `results/dec_intervals.csv`, reading the margin as measured from the edge of the predicted interval. Share of designs sent to trial:

  | Relation and rule | True margin 10 floors | True margin 20 floors |
  |---|---|---|
  | new setting, M2 with step 6 | 69 % | |
  | new setting, M2 alone | about 25 % | |
  | new setting, nearest produced setting with step 6 | 33 % | |
  | new family, M2 with step 6 | 87 % | 61 % |

- (b) **No forward run.** Rule qualification (step 5) and decision (step 6) use the same evaluation data. The selection optimism is acknowledged (Sections 4.5, 6.6), but the procedure is never run forward.
- (c) **Table 13 mixes kinds of guidance.** Its "general" block mixes consequences of the definitions ("Fixing a requirement") with findings on this dataset. In particular, "A new design family: use the simulation for gross margins only" rests on two transfers with one simulation.
- (d) **The validation claim goes too far.** Section 6.4 claims "empirical performance validity in the sense of the validation square".
  - What is shown is that the metrics discriminate between rules and relations on appropriate example problems. That is evidence of empirical structural validity, and a first step towards performance validity.
  - It does not show usefulness: that decisions taken with the framework are better than decisions taken without it (fewer wrong releases, fewer or better-targeted trials), and that the improvement is due to the framework.
  - In the terms of the design research methodology, this is support evaluation, not application or success evaluation.
- (e) **Trials are treated as error-free.** The decision model treats a trial as error-free (Section 3.4). By the paper's own data, a 100-part batch reproduces q95 only to about one floor, and a separate run may differ by up to 9.8 floors (Table 5).

**Why it matters.** RED readers will judge the paper by the procedure and the guidance. As written, these are logically motivated but empirically untested. Step 6 may be far more conservative than the reported distances suggest. And "when a physical trial is unavoidable" cannot be answered without the trial's own error.

**What would resolve it.**
- Specify the margin used in step 6, and report the operating characteristics and trial rates of the procedure's actual decision rule. The reliability analysis of Section 5.5 (share correct by observed margin and relation) is the natural basis for a threshold on the observable margin.
- Run a nested or prequential evaluation of the whole procedure: for each held-out design, qualify the rules on the alternatives produced so far, decide, and score.
- Compare the result with current-practice baselines in wrong releases, trials and expected cost. Candidates are the nominal simulation with an experience-based margin, the process-window worst case, and always trialling.
- Score a trial of n parts of the new design as a rule in its own right. Its distances are the benchmark against which design-stage rules should be judged.
- Give every row of Table 13 its evidence base, move dataset-specific rows out of the general block, and reword Section 6.4 accordingly.

### 8. Positioning in the design literature (Sections 2 and 6.4)

**Problem.** The background is strong on V&V, calibration, conformal prediction, conformity assessment and testing strategy. It is thin on the design-theory strands in which the constructs naturally belong:
- **Design types and product families.** The distinction between variant, adaptive and original design (Pahl et al. 2007), and product-family and platform design (Simpson et al. 2006; Jiao et al. 2007). Section 3.1 invokes "platform and variant design" without citing them.
- **Process-capability data in design.** The use of capability data in design (Tata and Thornton 1999; Thornton 2004), and statistical tolerance analysis in this journal (Chase and Parkinson 1991). The nearest produced setting is in effect a capability-database look-up.
- **Preliminary information.** The release of preliminary information in overlapped development (Krishnan et al. 1997; Terwiesch et al. 2002). Their question, when upstream information is fit to act on, is the paper's own.
- **Set-based concurrent engineering.** It codifies production knowledge as trade-off and limit curves for feasibility decisions on new designs (Sobek et al. 1999).
- **Prototyping strategy.** It addresses when physical trials are unavoidable (e.g. Camburn et al. 2017).
- **V&V domains and credibility.** The distinction between validation domain and application domain (Oberkampf and Roy 2010, already cited), and risk-informed credibility assessment (ASME V&V 40). Both are close relatives of the evidence relation, and of comparing the safe distance with the requirement margin.

Section 6.4 also states that the safe distance "puts a number on what design margins are for". Margins also absorb changes to requirements and to the design (Eckert et al. 2019), and the margin value method (Brahma and Wynn 2020) concerns excess margin and change absorption. The safe distance quantifies only the part of a margin that covers predictive uncertainty. The distinction between safety margins and design margins (Eckert and Isaksson 2017) would make this precise.

**Why it matters.** Without these links, the contribution to design theory is asserted rather than shown, and RED readers cannot see what is new relative to their own literature.

**What would resolve it.**
- Add a short subsection that positions the evidence relation, the floor and the procedure against these strands.
- Turn Section 6.4 from a list of mappings into an argument that states, for each strand, what the framework adds and what the results imply for it.

### 9. Readability, density and length for RED's readership (whole manuscript, especially Sections 5.4–5.9)

**Problem.**
- The manuscript runs to 38 pages, with 13 main-text tables, 9 appendix tables, 4 figures and twelve rules.
- It coins about a dozen terms: production floor, effect-to-scatter ratio, minimum resolvable change, decisive and safe distances, evidence relation, sibling, calibration alternatives, calibration budget, calibration design, and the family, range and novelty guards.
- Paragraphs routinely carry 20–30 numbers (e.g. Sections 5.4, 5.6 and 5.9).
- No single decision is worked through.
- The abstract strings definitions together with nested colons and gives no physical sense of a floor.

**Why it matters.** The design message is buried. RED's readership consists of design researchers rather than statisticians or forming specialists, and it needs to see a decision being made with the framework.

**What would resolve it.**
- (a) Add a running worked example from Section 3 onwards: one alternative and one characteristic, its floor in millimetres, a requirement, the verdicts of three rules, their margins, what step 6 returns, and what production showed.
- (b) Add a notation and glossary table.
- (c) Keep a core set of rules in the main text (e.g. M0, M1, M2, M5, NN and M5n) and move the rest to the appendix.
- (d) Move Tables 5, 6, 7, 10 and 12, Tables A5–A9, and much of Sections 4.3, 5.1 and 5.3 to supplementary material.
- (e) Translate the key distances into physical units and tolerances. For example, 16 floors correspond to about 0.8 mm of mid-side draw-in and about 1.3° of wall angle, the same order as the ISO 2768-1 angular tolerances of Section 5.8 (±0.5° to ±2°).
- (f) Let the tables carry the numbers and the text the interpretation.
- (g) Rewrite the abstract around the design question, with one physical anchor.

## 4. Minor comments

1. **Abstract, first and last sentences.**
   - Design-stage manufacturability decisions *increasingly* rest on simulation and machine learning; many still rest on rules, guidelines and experience.
   - "The findings show which design-stage decisions can be trusted and when a physical trial is unavoidable" should be restricted to this dataset, or rephrased as what the framework allows a team to determine.
2. **Abstract and Section 5.5: "adding calibrated abstention".** Within the family, the Gaussian-process intervals cover 71–72 % against a nominal 90 % (Table A3). Only M2 and M3 (and roughly M4) are close to nominal. Use "safe abstention", or name the rules.
3. **Section 1, p. 2.** Whitney (1996) grounded his argument mainly in the power-carrying nature of mechanical components, their side effects and their multi-functionality, not in production variation. Please rephrase so that the link to production variation is clearly the author's own, supported by Thornton et al. (2000).
4. **Section 1, p. 2 ("at a chosen confidence") and Section 5.1, p. 14 ("at 95 % confidence").** The floor is a 95 % quantile of batch differences, not a confidence level. Say "in 95 % of batch pairs".
5. **Section 3.1: the adequacy share.** p = 0.95 is far below the conformance that series-production requirements imply (capability indices of 1.33 or 1.67 correspond to non-conformance in parts per million). Discuss early how the framework would extend, using the parametric tail mentioned only in Section 6.5, and how that would affect the distances. This governs relevance to DFM practice.
6. **Section 3.1: the decision situation.** Describe it concretely:
   - who decides (product designer, process planner or tryout engineer);
   - at which stage (e.g. tool tryout or production part approval);
   - with what evidence in hand.
   A design-theory reader needs the actor and the timing.
7. **Sections 3.2 and 3.6 (step 3).** "A design question below the floor is not one the design stage needs to answer finer" conflicts with "a change below it can still move the tail of the distribution" (Section 3.2) and with the last row of Table 13. Align the procedure with the caveat.
8. **Section 3.3 and Table 2: naming.** The with/without-simulation pairs are named M1/M1n, M2/M2n and M5/M5n, but M3/M4. Consider M3/M3n for consistency. State in the text that the nominal simulation and the envelope do not depend on lubrication (see major comment 6).
9. **Section 3.4: what the distances are.** δ_d and δ_s are points on the operating characteristic rather than operating characteristics themselves. δ_d is the analogue of the indifference-zone parameter δ* of Bechhofer (1954), already cited, for P* = 0.95. The pair plays the role of the acceptable and rejectable quality levels of an acceptance plan. Saying so would help readers trained in quality engineering and sharpen the positioning.
10. **Section 3.4: the interval level.** The cost paragraph fixes the interval level (90 %) rather than deriving it from the cost ratio, whereas in Chow's (1970) reject-option rule the optimal threshold depends on the costs. Treat the level as a decision variable; Table 12 already varies it.
11. **Section 3.5: "the calibration design asks which alternatives to produce first".** Section 5.6 classifies subsets by relation; it does not solve a sequential design problem. Either formulate one (for example, the expected reduction in δ_d per produced alternative, given the anticipated designs) or rename the construct.
12. **Sections 3.5 and 5.7: the applicability guard.** This is the least developed construct: three heuristic domain checks, one of which (the novelty guard) refuses verdicts of which 72–96 % would have been correct. Consider shortening it, or relating it to established applicability-domain methods.
13. **Section 4.1 and throughout: terminology.** Use "design–process alternatives" consistently, as in the abstract. "Design alternatives" and "new designs" invite readers to treat lubrication and force changes as product design.
14. **Sections 4.5 and 6.1: confirmatory and exploratory findings.** NN, the headline baseline, and the grouped schemes were added after first results. State in Section 6.1 which findings are confirmatory and which exploratory.
15. **Section 5.4, p. 18: "every calibrated rule improves by an order of magnitude".** Mc (27 floors) and M2 (23) improve on M0 (108) by a factor of about 4–5.
16. **Section 5.6 and Table 9: k = 1.** At k = 1, M1, M2 and NN coincide by construction. The sibling differs only in lubrication, on which the nominal simulation and the envelope do not depend, and a single residual gives a zero margin. Present the common 3.5 floors as an identity rather than a finding.
17. **Section 5.8 and Table 11: the ISO 2768-1 scenario.**
    - State the design wall angles (20° and 10°) in the text.
    - In `results/scen_truth.csv`, the wall angle fails classes f/m and c for every alternative and meets class v for every alternative, and the convex arm angle fails every class.
    - The 32 near-limit decisions contain only six failing alternatives, all concave arm angles in class f/m, so the near-limit false-accept statements rest on six cases.
    - Justify the cost ratio c_FR = 0.5·c_FA.
18. **Section 5.9 and Table 12: refit bootstrap.** For a new variant, the refit-bootstrap interval of M5 (5.0–19 floors) overlaps that of NN (2.2–7.0). Present "remains the most decisive" as a ranking of point estimates.
19. **Section 6.1: "Five findings answer the three research questions beyond the particular numbers".** The third and fourth findings (safety before decisiveness; calibration only under exchangeability) are good hypotheses, but they rest on one factorial. Label them as such.
20. **Section 6.5: the PA12 attempt.** Either report it briefly in an appendix (what was tried, what failed and why) or omit it. State "None is specific to forming" as an expectation.
21. **Section 2.1: related work for the collection.** A few representative studies that evaluate learned manufacturability or forming-outcome predictors by held-out accuracy only would make concrete the evaluation gap the paper fills. That gap is its strongest argument for this collection.
22. **Table 1.** "Conformal prediction: coverage only" and "V&V: abstains: no" undersell those approaches: conformal predictors can be scored per decision, and a V&V credibility assessment can conclude that a test is needed. Soften these entries, or define the columns more narrowly.
23. **Table 8.** Give bootstrap intervals for at least the headline rules (NN, M2, M5) in the main table, not only in Table A1.
24. **Fig. 1 and Fig. 3.**
    - Fig. 1 needs the new-family branch (major comment 2) and a statement of which margin step 6 compares with δ_s (major comment 7).
    - In Fig. 3, mark δ_d and δ_s on each panel, so that the figure shows the constructs it illustrates.
25. **Section 7: extensions.** The list should include a second process or dataset, and a forward (prequential) evaluation of the procedure.

## 5. Recommendation

**Major revision.**

The submission tackles a question that matters to design research and to this collection, and does so with unusual care and transparency:
- a rare open dataset;
- a reproducible pipeline;
- a production-record baseline;
- paired with/without-simulation ablations;
- an honest development record.

Its sober central message is valuable for the AI-in-DFM community: within a family, neither the simulation nor learned models improved on the nearest produced setting. The paper is not a case study of an individual design effort, and it falls within RED's scope.

In its present form, however, the general claims outrun the evidence. The data come from one dataset whose evidence relations emerged from the analysis, and the only product-design relation rests on two transfers. Several constructs are not coherent for every relation: the floor for a new family, the sibling relation, and the population behind the distances. The procedure's own decision rule, and its usefulness, are not evaluated, and the text is too dense for RED's readership.

These problems can be addressed with analyses that the released pipeline largely supports, together with substantial rewriting and a better-developed link to design theory. I therefore recommend major revision rather than rejection.

## 6. Confidential comments to the editor

I regard the submission as within RED's scope and not a desk-reject case: its contribution is a framework and an evaluation methodology, not an individual design effort. It is technically careful and unusually transparent. I reproduced Table 8 and spot-checked several other figures from the released result files, and they match. My reservations concern the generality of the claims, the design-theoretic articulation and the readability. All of these can be addressed in a major revision, although the requested second application and the forward evaluation of the procedure are substantial work; whether they fit the collection's timeline is for you to judge. This report does not assess the scan feature extraction, the forming physics or the statistical-learning implementations in depth. Reviewers with forming and metrology expertise, and with ML and uncertainty-quantification expertise, would complement it.

---

### References suggested in this report

- ASME (2018) Assessing credibility of computational modeling through verification and validation: application to medical devices. ASME V&V 40-2018. American Society of Mechanical Engineers, New York
- Camburn B, Viswanathan V, Linsey J, et al (2017) Design prototyping methods: state of the art in strategies, techniques, and guidelines. Design Science 3:e13
- Chase KW, Parkinson AR (1991) A survey of research in the application of tolerance analysis to the design of mechanical assemblies. Research in Engineering Design 3(1):23–37
- Eckert C, Isaksson O (2017) Safety margins and design margins: a differentiation between interconnected concepts. Procedia CIRP 60:267–272
- ISO 5725-6:1994 Accuracy (trueness and precision) of measurement methods and results, Part 6: Use in practice of accuracy values. International Organization for Standardization, Geneva
- Jiao J, Simpson TW, Siddique Z (2007) Product family design and platform-based product development: a state-of-the-art review. Journal of Intelligent Manufacturing 18(1):5–29
- Krishnan V, Eppinger SD, Whitney DE (1997) A model-based framework to overlap product development activities. Management Science 43(4):437–451
- Pahl G, Beitz W, Feldhusen J, Grote KH (2007) Engineering Design: A Systematic Approach, 3rd edn. Springer, London
- Simpson TW, Siddique Z, Jiao J (eds) (2006) Product Platform and Product Family Design: Methods and Applications. Springer, New York
- Sobek DK II, Ward AC, Liker JK (1999) Toyota's principles of set-based concurrent engineering. Sloan Management Review 40(2):67–83
- Tata M, Thornton AC (1999) Process capability database usage in industry: myth vs. reality. In: Proceedings of the ASME Design Engineering Technical Conferences (Design for Manufacturing)
- Terwiesch C, Loch CH, De Meyer A (2002) Exchanging preliminary information in concurrent engineering: alternative coordination strategies. Organization Science 13(4):402–419
- Thornton AC (2004) Variation Risk Management: Focusing Quality Improvements in Product Development and Production. Wiley, Chichester
