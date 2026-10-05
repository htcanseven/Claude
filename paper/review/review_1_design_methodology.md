# Referee report

**Manuscript:** *Qualifying design-stage manufacturability decisions with production evidence* (main_v1.pdf, 28 pp.)
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Referee 1:** design theory and methodology (design decision-making under uncertainty, verification and validation in design, DFM, evaluation of design support)
**Date:** 5 October 2026

---

## 1. Summary

The manuscript asks how close to a requirement a design-stage manufacturability decision rule can be trusted. A decision rule here is a procedure that turns simulations of a new alternative, and the production record of alternatives already made, into the verdict *meets*, *fails* or *trial*. The paper proposes a production-referenced unit, the *production floor*: the 95 % quantile of the difference between the centres of two 50-part batches of one alternative. Each rule is characterised by a *decisive distance*, beyond which at least 95 % of verdicts are correct, and a *safe distance*, beyond which at most 5 % are wrong. These are complemented by a calibration budget and calibration design, an applicability guard and a six-step procedure.

The constructs are demonstrated on an open deep-drawing dataset: 18 alternatives (2 geometries × 3 blank-holder forces × 3 lubrication patterns, 500 parts each) with matched FE simulations. Six rules, from the nominal simulation to Gaussian-process (GP) and gradient-boosting corrections, are compared under three calibration scopes, and a small powder-bed-fusion case without simulation is added. The headline findings are:
- the nominal simulation needs requirements about 150 floors away;
- a GP discrepancy calibrated on the design family decides beyond 7 floors and is safe beyond 2;
- four to five bracketing alternatives suffice;
- no rule transfers safely to a new geometry.

The paper closes with a table of design guidelines.

## 2. Assessment of contribution and fit

### Strengths

- **The right question.** The paper asks whether a prediction is fit to *decide*, not merely whether a model is accurate on average, and it treats abstention as a legitimate outcome. This is a design-methodological question, and the analogy to guard-banded conformity assessment and to Currie's detection limits is apt.
- **Verdicts scored against production.** Verdicts are scored against the actual production of many alternatives, which almost no DFM/ML study is able to do.
- **An honest negative result.** No rule is safe closer than 20 floors on a new geometry. This finding is valuable.
- **Exemplary reproducibility.** I checked Tables 4, 5, 7–11, A1 and A2 and the rates quoted in Sections 5.4–5.6 against the released CSVs, and they agree. The exceptions are the denominator and wording problems in Major comment 7 and Minor comments 20, 21 and 25. With the author's own functions I also reproduced the within-family leave-one-out distances of M1, M2 and M5 exactly.
- **A candid threats-to-validity section.**

### Contribution beyond the case; novelty and generality of the constructs

At present the generalisable contribution is under-developed relative to the case.
- **Framing.** The contributions (p. 3) are stated as artefacts applied to deep drawing. The abstract carries about fifteen numerical results.
- **Balance.** The constructs receive about 2.5 pages and the procedure one paragraph, against about nine pages of results.
- **Source of novelty.** All six decision rules are existing methods: bias correction, split-conformal margins, a Kennedy–O'Hagan-type GP discrepancy and gradient boosting. Any novelty must therefore come from the evaluation framework. That framework is neither formalised as a design-theoretic contribution nor positioned against its closest relatives:

| Construct | Closest existing concept | What is new here | Main concern |
|---|---|---|---|
| Production floor | Between-subgroup variation in SPC (X̄ chart); MSA repeatability; "noise floor" | Used as the unit for design-stage decisions across characteristics | Not shown to be the resolution of the decided statistic (q95); depends on the sampling design (Major 3) |
| Effect-to-scatter ratio; minimum resolvable change | Signal-to-noise ratio; minimum detectable effect | Expressed in production terms | MRC treated as global, although sensitivity varies by more than an order of magnitude (Major 3) |
| Safe and decisive distances | Operating characteristic of guard-banded acceptance (ISO 14253-1); Currie's L_D; risk–coverage curves of selective classification | Two summary points of an OC curve, in floors | Defined on the unobservable true margin; false accepts and false rejects pooled (Major 4) |
| Calibration budget and design | Learning curves; predictive maturity; design of calibration and validation experiments | In floors, per design family | Confounded by near-replicates in the calibration set (Major 5) |
| Applicability guard | Valid-input or applicability domain; out-of-distribution detection | One-dimensional range check on the simulated q95 | Trivial with two geometries; benefit misreported (Major 7) |
| Six-step procedure | V&V and credibility workflows (ASME V&V 10, NASA-STD-7009); Kennedy–O'Hagan workflow | Ordering of the steps for DFM decisions | Neither specified nor evaluated as design support (Major 10) |

**Generality.**
- *Evidence base.* Generality rests on one process with simulation (two geometries, 18 alternatives), plus one process without simulation in which production resolves only 18 of 120 alternative pairs. The second case therefore cannot discriminate between rules.
- *Scope of the decisions.* Most decisions evaluated are new process settings on an existing tool rather than product design decisions (Major 6).
- *Requirement form.* The requirement is a one-sided limit on the 95th percentile, which is far from the capability levels used in DFM practice.

### Fit with RED and the special collection

- **Topic.** Whether simulation and learning can support manufacturability decisions fits RED and the special collection well. The decision and verification perspective is genuinely design-methodological.
- **AI content.** The "AI" content is modest: a GP and gradient boosting trained on 8–17 design points. The machine-learning conclusions in Section 6.3 rest on comparisons that do not isolate what they claim (Major 8).
- **Fit with DFM.** Fit is weakened because the decisions studied are mostly process-setting decisions (Major 6).

### Clarity, structure and length

- **Length and balance.** At 28 pages (21 of main text, 4 of appendix, 3 of references) the length is acceptable for RED, but the balance is not:
  - Section 3 is short, the procedure is a single paragraph, and the implications for design take about 1.5 pages.
  - The results read as dense lists of numbers; many sentences carry four or five values.
- **Prose and naming.** The prose is economical but often elliptical; for example, "the simulation carries a decision into a new family, while an applicability guard sends it to trial". The rule numbering (M0, M1, M2, M5, M3, M4, later M6) is confusing.
- **Appendix.** Tables A3 and A5 are tangential. A "design-space analysis" is referred to repeatedly but never shown.
- **Recommendation.** Expand Sections 3 and 6, compress Section 5 and the appendix, and keep a similar total length.

### Desk-rejection risk and how to reduce it

As written, the risk is high. An editor reading the abstract sees a benchmarking study of existing UQ/ML methods on one open dataset. That is close to the two criteria RED applies: "primarily present case studies of individual design efforts" and "focus solely on applying existing tools or methods".

To reduce the risk:
1. Open the abstract and introduction with an explicit design-research question and the conceptual contribution, and use at most two or three numbers. The conceptual contribution is a production-referenced account of how finely design-stage verification can decide.
2. Present the constructs as a general framework, with stated assumptions and properties, before the demonstration.
3. Position the work in design decision theory, the margins literature, verification strategy and design-support evaluation (Major 2).
4. Present the deep-drawing and PBF studies explicitly as an *evaluation* of the framework, i.e. an initial Descriptive Study II in DRM terms, using the grouped cross-validation of Major 5.
5. State the scope and evidence strength of every guideline.
6. Consider a title that makes the conceptual contribution visible rather than the qualification activity alone.

---

## 3. Major comments

### 1. The contribution to design research is not separated from the case (desk-rejection risk)

**Problem.** The paper states no research question at the level of design research.
- **Contributions.** The four contributions (p. 3) are artefacts, and the fourth is "a six-step procedure ... and its demonstration".
- **Abstract.** It lists case results but says nothing about what the constructs mean for design theory or practice beyond the case.
- **Constructs.** Section 3 introduces them without stated assumptions or properties.
- **Discussion.** Section 6.1 ("What the demonstration establishes") restates case results.
- **Novelty.** Since the decision rules are existing methods, novelty can only come from the evaluation framework, and that framework is not developed as such.

**Why it matters.** This is exactly what RED's desk-rejection criterion targets. It also makes it hard for design researchers to reuse the constructs outside sheet-metal forming.

**What would fix it.**
- (a) **Research questions.** State two or three research questions for design research. For example:
  - How can the fitness of a design-stage prediction for a manufacturability decision be expressed independently of the predictor and the characteristic?
  - How does that fitness depend on the amount and placement of production evidence in a design family, and on transfer to a new family?
- (b) **Formal framework.** Present the framework independently of deep drawing:
  - *Definitions.*
  - *Assumptions:* exchangeable batches, stationarity within a run, a one-sided requirement on a quantile.
  - *Properties:* invariance to affine changes of the characteristic's unit; δs ≤ δd; behaviour as B and the series length change; relation to OC curves, guard bands and capability indices.
  - *Use in a decision:* how the distances enter a decision that has costs and base rates.
- (c) **Abstract and conclusions.** Rewrite them around the generalisable findings that the paper has but buries:
  - decision fitness is limited by the *spread* of model discrepancy between alternatives rather than by its mean;
  - production evidence buys safety before decisiveness;
  - interval rules trade abstention for safety, and the two distances make this trade visible;
  - transfer to a new product family is not safe without an applicability check.

  Case numbers should support these statements, not replace them.
- (d) **Discussion for design methodology.** Discuss what the results imply for verification planning, for front-loading (the paper cites Thomke but does not return to it) and for how AI-based DFM tools should be evaluated.
- (e) **Space.** Make room by compressing Section 5 and moving Tables A3 and A5 to supplementary material.

### 2. Positioning in the design literature is thin, and Table 1 understates the closest prior work

**Problem.** The background covers DFM, V&V, Bayesian calibration, conformal prediction and SPC/MSA. It omits the design-research streams that the claims bear on most directly:

- **Decision-based design and decision-making under uncertainty.** E.g. Hazelrigg (1998, *J Mech Des*); Lewis, Chen and Schmidt (2006, *Decision Making in Engineering Design*); de Weck, Eckert and Clarkson (2007, ICED) on uncertainty in early design.
- **Design margins.** The safe distance is in effect the margin a designer must keep between prediction and requirement. See Eckert, Isaksson and Earl (2019, *Design Science*) and Brahma and Wynn (2020, *RED*).
- **Verification and testing strategy, and the value of information.** The "trial" verdict and calibration design are test-planning decisions. See Thomke and Bell (2001) and Loch, Terwiesch and Thomke (2001), both *Management Science*; Panchal et al. (2008, *Eng Optim*) on value-of-information-based model refinement; Salado and Kannan (2018, *Syst Eng*) on verification strategies.
- **The valid input domain of predictive models in design.** Malak and Paredis (2010, *J Mech Des*), directly relevant to the applicability guard.
- **Variation risk management, key characteristics and process capability.** Thornton (1999, *RED*); Thornton (2004, *Variation Risk Management*); Kane (1986, *J Qual Technol*).
- **Set-based design.** A way to defer commitment under uncertainty (Sobek, Ward and Liker 1999).
- **V&V.**
  - *Predictive maturity and sequential design of validation/calibration experiments:* Hemez, Atamturktur and Unal (2010); Williams et al. (2011); Arendt, Apley and Chen (2016).
  - *Validation metrics in physical units:* Ferson, Oberkampf and Ginzburg (2008).
- **Machine learning: classification with a reject option and risk–coverage analysis.** Chow (1970); Geifman and El-Yaniv (2017). This is the nearest formal analogue of a three-verdict rule characterised by two distances.

Table 1 says that V&V does not abstain and that only this paper scores decisions against production. Yet guard-banded conformity decisions (ISO 14253-1, cited in the paper) and acceptance sampling are characterised precisely by their probabilities of false acceptance and false rejection as a function of the true value. That is an operating-characteristic curve, and δs and δd are two summary points of such a curve.

**Why it matters.** Without this positioning the novelty claims cannot be assessed. These include "for the first time on open data" (p. 2), "has not been available before" (p. 4) and the last row of Table 1. The paper also does not yet speak to RED's core readership.

**What would fix it.**
- Add a subsection positioning the constructs against these streams.
- Revise Table 1 to include guard-banded acceptance and acceptance sampling, predictive maturity, selective classification and margin methods.
- State precisely what is new. I would argue it is (i) a production-referenced unit that makes decision fitness comparable across characteristics and predictors, and (ii) an empirical decomposition of decision fitness by calibration scope and calibration budget.

### 3. Construct validity of the production floor as the unit of decision

**Problem.**

- **(a) Batch centre vs. decided statistic.**
  - The floor (Eq. 2) is defined on batch *centres* (10 % trimmed means), whereas adequacy is defined on the *95th percentile* of the alternative's parts.
  - The paper argues that "a difference between two alternatives smaller than the floor cannot be resolved in production, so no design-stage decision needs to be finer" (p. 2). That argument needs the resolution of the decided quantity, q95.
  - The reproducibility of q95 depends on spread and tail behaviour, not only on location.
- **(b) Dependence on the sampling design.**
  - F is a function of the batch size B = 50, the quantile α = 0.95, the series length (10 batches per alternative), the robust centre and the time order.
  - Because drift dominates (drift factor 1.4–4.5, Table 4), longer series would give larger floors.
  - Neither B nor the series length is varied in Table 10. The floor is presented as "the resolution of production itself" (p. 5), but it is a property of a measurement protocol.
- **(c) Run-to-run variation.**
  - Each alternative was produced once. The floor therefore excludes between-run variation; this is acknowledged on p. 20.
  - The same omission affects the effect-to-scatter ratios: differences between alternatives contain run effects that are confounded with factor effects.
  - ESR ≥ 1 may therefore overstate what production resolves between designs in series production.
- **(d) Commensurability across characteristics and processes.**
  - *Across characteristics.* The headline distances pool verdicts over seven characteristics whose floors relate very differently to design tolerances. Table A2 shows M5's within-family safe distance ranging from 0.5 to 9.5 floors (dome 9.5, cup depth 3.5), which the pooled "2 floors" hides.
  - *Across processes.* The PBF floor is estimated from 18 within-class batch pairs from three builds (results/case2_floor.csv). At α = 0.95 it is effectively the largest pair difference.
  - So "5.5 floors" for the PBF nominal geometry and "150 floors" for the deep-drawing nominal simulation are not comparable statements about predictor quality, although Section 6.4 invites that comparison.
- **(e) The minimum resolvable change is local.**
  - F/|s| assumes a constant sensitivity. Table A4 shows the blank-holder-force sensitivity changing by more than an order of magnitude over the tested range: the arm-angle MRC is 48 kN between 100 and 300 kN and 1083 kN between 300 and 500 kN.
  - The single values in Table 5 come from the 100 → 500 kN contrast, which also contains the stroke-speed change, and can mislead.

**Why it matters.** The floor is the paper's first contribution and the unit of every result and guideline. If it does not measure the resolution relevant to the decision, the distances and the guidelines inherit the problem.

**What would fix it.**
- Define the floor for the decided statistic, or show empirically how a q95-based floor relates to the centre-based one. A q95-based floor could be computed, for example, from batch quantiles with larger B or from halves of each series.
- Write the dependence on B, α and the series length into the definition.
- Add B ∈ {25, 50, 100}, α ∈ {0.90, 0.99} and the adequacy share p to the robustness analysis.
- Treat run-to-run variation explicitly as a missing component and discuss its effect on ESR.
- Report per-characteristic distances in the main text. Give a tolerance-to-floor ratio, or relate the floor to capability indices, so that a designer can judge whether a distance is design-relevant.
- Give the uncertainty of the PBF floor.
- Present the MRC as a local quantity.

### 4. The safe and decisive distances are defined on an unobservable quantity, and their pooled definition hides the asymmetry that matters in design

**Problem.**

- **Truth vs. prediction.**
  - The distances are defined on d = (R − q95)/F, the distance of the requirement from the *unknown true* q95 (Eq. 4).
  - Yet Section 3.4 calls the decisive distance "the smallest margin between *prediction* and requirement that the design stage can resolve". Step 6 returns "a verdict with the distance of the requirement from the prediction expressed in floors". Section 6.2 asks designers to compare that distance with δd and δs.
  - These are different quantities. The designer observes the prediction-to-requirement margin. The probability that a verdict is right *given that observed margin* depends on the rule's error distribution and on the distribution of true margins in the design context, just as the predictive value of a diagnostic test depends on prevalence.
  - The problem is serious for biased rules: for M0, a predicted margin of 100 floors is compatible with a true margin near zero.
- **Pooling of false accepts and false rejects.**
  - ω pools false accepts (d < 0) with false rejects (d > 0), although Section 3.4 itself recognises that c_FA ≠ c_FR.
  - The rules are strongly asymmetric (results/dec_curve.csv): within the family, M1 errs by false accept in 12.7 % of verdicts at d = −10 but by false reject in only 5.6 % at d = +10, and M0 errs by false reject in 50 % of verdicts at d = +10.
- **The cost bound.** The bound in Section 3.4 holds on average over the evaluation population at a given |d|, not per design, and it assumes error-free trials.

**Why it matters.** A design-support construct must be usable at the moment of decision. As written, the guidance invites a category error: comparing an observed margin with a threshold defined on the true margin.

**What would fix it.**
- Choose one of two remedies:
  - (i) present δs and δd explicitly as *operating characteristics* of a rule, and explain how designers use them: choosing a rule, judging whether a requirement placed near the expected capability is decidable at the design stage at all, and planning trials; or
  - (ii) add the observable view: the empirical share of correct verdicts conditional on the *predicted* margin (a reliability curve), if necessary under stated priors on true margins.
- Report one-sided (accept-side and reject-side) distances next to the pooled ones.
- Give one worked cost example over a range of c_T/c_FA ratios showing when the decisive rule (M5) or the safe rule (M2) should be preferred.

### 5. The within-family evaluation puts near-replicates of the "new design" into the calibration set; the main positive results and the calibration-design finding depend on it

**Problem.**

*Why near-replicates arise.*
- Within a geometry, the nine alternatives form a 3 × 3 factorial (blank-holder force × lubrication).
- The paper itself shows that lubrication is not resolved by production in 73 of 126 contrasts (Table 5), and that the simulation envelope does not depend on lubrication (Section 5.5).
- Under leave-one-alternative-out, every held-out alternative therefore has two calibration siblings at the same blank-holder force (BHF) that differ only in lubrication pattern. For most characteristics production cannot tell these siblings apart from the held-out design, so the "new design" is close to a re-run of a produced design.

*Two checks.* I ran both read-only, using the author's own functions (`m5_interval`, `conformal_margin` and `beyond` in scripts/decisions.py) and the released tables (results/dec_alternatives.csv, alt_floor.csv, budget_design.csv). They are indicative only and should be redone by the author with M3/M4 and bootstrap intervals.

- **What "bracketing" means.**
  - *The definition.* In scripts/budget.py a calibration set "brackets" the new design when min BHF ≤ BHF_new ≤ max BHF. With three BHF levels, a new design at 100 or 500 kN is bracketed *only* if the set contains a same-BHF sibling. At k = 1, bracketing *is* a sibling.
  - *Effect at k = 1.* budget_design.csv then gives M1 safe and decisive at 4 floors with no wrong verdict at 10 floors (252 cases). That is better than M5 with all eight alternatives.
  - *Share of bracketing sets with a sibling.* 81 % at k = 2, 86 % at k = 3, 92 % at k = 4 and 96 % at k = 5.
  - *M2 under true interpolation.* Without a sibling, M2 still makes no wrong verdict at 10 floors, so part of the bracketing effect is genuine. But its safe distance is 5, 4.5, 4 and 3 floors for k = 2–5, against 2.5, 1.5, 1.5 and 1 floors when a sibling is present (appendix to this report).
  - *M5 under true interpolation (k = 2–3).* M5 is also safe (essentially no wrong verdicts at 10 floors; safe at 4 and 3.5 floors), but it sends about twice as many designs to trial (23–24 % vs. 10–12 %) and is less decisive (20–25 vs. 15 floors) than with a sibling in the set.
- **Grouped cross-validation.**
  - *Results.* I held out all three lubrication variants of one BHF level and calibrated on the remaining six alternatives of the family. The within-family decisive/safe distances become M1 20/20, M2 20/7.5 and M5 20/7.5 floors.
  - *M5 at |d| = 10.* It is right in 75 %, wrong in 2.8 % and sends 22 % to trial.
  - *Comparison with the paper.* Table 7 reports 15/15, 25/0.5 and 7/2, with M5 right in 97 % at 10 floors. The same code reproduces Table 7's leave-one-out values exactly.
  - *Not an effect of fewer alternatives.* Going from eight to six calibration alternatives alone moves M5 only from 7/2 to 8/2 (Fig. 4, budget_resolution.csv). The deterioration therefore comes from removing the siblings, not from the smaller calibration set.
  - *Interpolation case.* For 300 kN predicted from 100 and 500 kN, M2 and M5 are both safe at 2.5 floors but decisive only at 20.

*Consequence.* The following claims hold when the produced set contains a near-replicate of the new design, not for a genuinely new process setting:
- "the Gaussian-process calibration is the most decisive rule ... right beyond 7 floors";
- "four to five produced alternatives that bracket the new design's process settings make calibrated rules reliable";
- the guideline "four or more produced alternatives → M5, right beyond 7–10 floors".

Bracketing by interpolation buys safety, not decisiveness.

**Why it matters.** This is the paper's central positive result. It also underlies two of the five guidelines (rows 2 and 3 of Table 12), the calibration-design advice in Section 6.2 and three sentences of the abstract.

**What would fix it.**
- Use cross-validation schemes that match the decision being qualified: leave-one-BHF-level-out and leave-one-lubrication-level-out within the family, alongside the transfer scope.
- Report Table 7, Fig. 3, Fig. 4, Table 8 and Table 9 under these schemes.
- Split "brackets" into "sibling present", "interpolation" and "extrapolation".
- Re-derive the guidelines.
- If leave-one-alternative-out is retained, describe it accurately as judging "a new lubrication variant of an already produced process setting".

### 6. The evaluated decisions are mostly process-setting decisions on an existing tool, and the requirement model is far from design practice

**Problem.**

- **(a) What kind of decisions are evaluated.**
  - The title, abstract and keywords present the work as design-stage DFM, i.e. product design decisions made before tooling exists.
  - In the demonstration, product geometry has only two levels. The within-family "new designs" are new BHF/lubrication settings on an existing tool set, whose siblings have each been produced as 500-part series. Several variants produced as consecutive series is evidence normally available at tryout or ramp-up, not at the design stage.
  - The one genuinely design-stage case, a new geometry, gives a negative result: no rule is safe closer than 20 floors, and the guard sends 90.5 % of decisions to trial.
- **(b) The requirement model.**
  - The requirement is a one-sided upper limit on q95, so an alternative is "adequate" with up to 5 % nonconforming parts.
  - DFM works with two-sided tolerances, and industrial capability targets (e.g. Cpk ≥ 1.33, i.e. tens of ppm) concern tails that 500 parts per run cannot estimate.
  - The paper does not discuss how the constructs extend to two-sided or high-conformance requirements.
- **(c) The general-tolerance scenario.** Section 5.6 uses three of the seven characteristics (wall angle, arm angle, flatness). It omits linear dimensions such as the cup depth, for which the simulation's offset is among the largest (about 0.9 mm, i.e. 72–106 floors; Table 6).

**Why it matters.** Fit with RED and with DFM depends on whether the decisions studied are design decisions. The generality of the constructs depends on whether they work for realistic requirement forms.

**What would fix it.**
- State the scope precisely, e.g. "decisions on new variants of a produced design family, and transfer to a new family".
- Say where in the product development process the procedure applies: process planning, tryout, or variant and platform design.
- Make the negative transfer result a headline finding.
- Add a section on two-sided and high-conformance requirements. A conceptual treatment is the minimum; ideally demonstrate it on the existing data with p = 0.99 or two-sided limits.
- Include linear dimensions in the tolerance scenario if nominal dimensions are available.
- The unreported analysis of the 264 geometry-varying DDACS simulations (Minor 15) could help connect the framework to decisions on product geometry.

### 7. The applicability guard is minimal, is evaluated on two geometries, and its benefit is misreported

**Problem.**

- **The guard is trivial here.** The family guard fires for every new geometry by definition, and the novelty guard is a one-dimensional range check on the simulated q95. With two geometries the guard reduces to "do not transfer": 90.5 % of transfer cases go to trial.
- **The misreported rate.**
  - Section 5.5 states that "in the remaining cases M2 is never wrong at 10 floors and M5 in 2.4 %".
  - In results/dec_guard.csv the 2.4 % is the share of wrong verdicts among *all* transfer verdicts. For M5 the shares are correct 7.1 %, uncertain 90.5 % and wrong 2.4 %.
  - Only 12 of the 126 transfer cases (alternative × characteristic) are unguarded, all of them mid-side draw-in or waviness.
  - Of their 24 verdicts at |d| = 10, M5 gets **6 wrong (25 %)**, M1 gets 4 wrong and M0 gets 3 wrong. M2 makes no wrong verdict but sends 12 of the 24 to trial (results/dec_intervals.csv).
- **No protection within the family.** Within the family the guard never fires, so it gives no protection against within-family errors either.

**Why it matters.** The guard is presented as a contribution and underpins the "new geometry" guideline. On the evidence, M5 is not safe when the guard lets a design through.

**What would fix it.**
- Correct the statement and report conditional rates (wrong given not guarded) with counts.
- Position the guard against applicability-domain and validity-domain work: Malak and Paredis (2010); the distinction between validation domain and application domain in Oberkampf and Roy (2010); out-of-distribution detection.
- Evaluate the guard where it is non-trivial, e.g. with a multi-dimensional descriptor space built from the geometry-varying DDACS simulations, or under leave-one-BHF-level-out within the family.
- Report both its false-alarm rate (designs sent to trial that the rule would have decided correctly) and its miss rate.

### 8. The claims about where machine learning helps (Section 6.3) are not supported by the comparisons made

**Problem.**

- **(a) The physical model is not isolated.**
  - "Machine learning helps where it corrects a physical model" rests on M5, a GP on the offset from the simulation envelope.
  - The ablation that would isolate the physical model is missing: the same GP on q95 over the same descriptors, *without* the simulation.
  - The part-level M3/M4 comparison does not substitute for it, because M3 and M4 differ from M5 in model class, level of aggregation and margin construction.
  - Within a family the envelope depends only on BHF (three values), so the GP may be doing most of the work.
- **(b) M4's transfer failure holds by construction.** Trained on one geometry, its geometry indicator is constant, so it has no information about the other geometry. This shows that a model without geometric descriptors cannot extrapolate in geometry, not that "learning" fails.
- **(c) The simulation does not carry decisions into a new family.** The claim that "the simulation is what carries a decision into a new design family" is not borne out. With the simulation, the best transfer rule decides only at 40 floors, M5 is wrong in 21 % of verdicts at 10 floors, and the guard sends 90.5 % of decisions to trial.
- **(d) Data regime.** All learned rules see 8–17 distinct design points. The conclusions are specific to that regime.

**Why it matters.** These claims tie the paper to the special collection, and they will be cited as findings about AI in DFM.

**What would fix it.**
- Add the "GP without simulation" ablation and, for completeness, M1/M2 applied to q95 without the simulation.
- Reformulate (b) and (c), and state the data regime.
- If possible, give the learned rules continuous geometric descriptors (e.g. the DDACS geometry parameters) so that transfer can be tested meaningfully.

### 9. The design guidelines (Table 12) go beyond the evidence

**Problem.**

- **(a) The numbers are properties of this simulation and dataset.**
  - "Reliable beyond about 150 floors" for the nominal simulation is driven by two characteristics with offsets of 59–108 floors (cup depth, corner draw-in). The other five lie at 20–40 floors (Table A2).
  - Appendix A.2 traces the offsets largely to the oil-to-friction mapping (friction sensitivity overstated 5–630 times, Table A3). Another simulation would give another number.
- **(b) "Four or more produced alternatives → M5, right beyond 7–10 floors".** The unconditional decisive distance at k = 4 is 15 floors (results/budget_resolution.csv). The 7–10 range holds only for bracketing subsets and, by Major 5, mainly when a sibling is present.
- **(c) "Two or three → M2 ... about a quarter sent to trial".** For bracketing subsets, abstention at 10 floors is 11 % at k = 2 and 26 % at k = 3 (results/budget_design.csv).
- **(d) "New geometry → M2 with the applicability guard".** This rests on two geometries and on a guard that almost always fires.
- **(e) "Design or process change below the minimum resolvable change → do not iterate on it".**
  - This conflates statistical detectability between two 50-part batches with practical significance. A mean shift below the floor:
    - still changes the nonconforming fraction when the requirement lies near the tail;
    - may matter for another characteristic;
    - can be detected with more data.
  - The MRC is also local (Major 3e).
  - Guidance on iteration should engage with the iteration literature, e.g. Wynn and Eckert (2017, *RED*).
- **(f) Evidence strength.** No guideline states the strength of its evidence: number of families, alternatives and processes, and the uncertainty.

**Why it matters.** Guidelines are the part that practitioners adopt and researchers cite. RED readers expect design guidance to be justified and scoped.

**What would fix it.**
- Split Table 12 into two parts:
  - (i) procedure-level guidance that is plausibly general, e.g. "measure the M0 distance of your own simulation before relying on it", "plan calibration alternatives so that they bracket the window of future designs", "report every verdict together with the rule's distances";
  - (ii) findings for this dataset, clearly labelled, with their evidence base and intervals.
- Remove or qualify (e).
- Re-derive the k-dependent rows under grouped cross-validation (Major 5).

### 10. As an evaluation of design support, the study evaluates the instruments, not the support

**Problem.**

- **What has been evaluated.** In DRM terms (Blessing and Chakrabarti 2009), the paper is a Prescriptive Study (constructs plus procedure) followed by a retrospective evaluation of the *accuracy of decision rules*. The six-step procedure, claimed as a contribution, receives one paragraph and Fig. 1, and is not itself evaluated.
- **What is missing:**
  - *Success criteria:* no success criteria are defined, and no measurable criteria link the distances to design outcomes such as fewer trials, fewer late changes, or lower cost or lead time.
  - *Application evaluation:* can design teams obtain several produced variants with consecutive series when they need them? What effort does the procedure take? Can engineers interpret "floors"?
  - *Comparison with current practice:* experience-based compensation, safety margins, tryout loops. M0, the raw nominal simulation without any margin, is not a realistic practice baseline.
- **Validation Square.** In the terms of Pedersen et al. (2000) and Seepersad et al. (2006), the paper offers some *empirical performance validity* on two examples. It does not establish:
  - *theoretical structural validity*: the internal consistency of the constructs (Majors 3 and 4);
  - *empirical structural validity*: whether the examples represent the intended use (Majors 5 and 6);
  - *theoretical performance validity*: why the results should generalise.

  Frey and Dym (2006, *RED*) is also relevant here.

**Why it matters.** RED readers will judge the paper as a contribution to design methodology. A method whose use is not evaluated, and whose evaluation criteria are not linked to design outcomes, is weakly supported.

**What would fix it.**
- Position the work explicitly in DRM: a Prescriptive Study plus an initial Descriptive Study II.
- Define success criteria and measurable criteria and the link between them, e.g. through the cost model of Section 3.4 combined with a distribution of requirement margins taken from real drawings.
- Specify the procedure fully: inputs and outputs of each step, decision points, roles, timing in the development process, data requirements and effort.
- Add a realistic practice baseline: M0 or M1 with an engineer-chosen fixed safety margin, or the decision record of an actual tryout.
- Add at least a small application evaluation, e.g. a structured walkthrough or interviews with forming and process engineers on whether the floor table, distance table and budget curve would change their decisions.
- If this is not feasible, reduce the claim from a "procedure" to an "evaluation framework" and state that support evaluation is future work.

---

## 4. Minor comments

1. **Abstract (p. 1).**
   - See Major 1; use at most three numbers.
   - Define "decides correctly beyond X floors" once.
   - State the scope: variants of a produced family vs. a new family.
   - Rewrite the elliptical last-but-two sentence ("the simulation carries a decision into a new family, while an applicability guard sends it to trial").
2. **p. 2 and p. 4, novelty claims.** "For the first time on open data" and "has not been available before" should be qualified or substantiated.
3. **p. 2, para. 3 and Section 3.2.** "No design-stage decision needs to be finer [than the floor]" is overstated; see Majors 3(a) and 9(e).
4. **p. 5, Section 3.1.**
   - Say how the requirement form applies to characteristics governed by a lower limit (e.g. the hole diameters in Section 5.8) and to two-sided tolerances.
   - Say that "adequate" refers to a single 500-part run.
5. **p. 6, Eq. (2).**
   - Specify the pair set: all i < j within an alternative, and whether alternatives have equal weight.
   - Specify how many batches were dropped by the 80 % validity rule (A.1).
   - State in the main text that the decision analysis uses per-geometry floors (A.1), while the first column of Table 4 and the physical conversions in Section 5.4 use the pooled floor (e.g. "0.004 mm of waviness" = 1.5 × 0.0028 mm). Per-geometry floors differ by up to a factor of 2.4 (dome: 0.0034 vs. 0.0082 mm).
6. **p. 6, Eq. (3).**
   - Define m̄: is it the trimmed mean over all 500 parts?
   - Justify ESR ≥ 1 as the resolvability threshold: what error rates does it imply for a comparison of two alternatives?
7. **pp. 6–7, Section 3.3 and Table 2.** Number the rules in order of presentation (M0–M5). Having M5 between M2 and M3, and M6 appearing only in Section 5.7, is confusing.
8. **p. 7, M2.**
   - With n = 8 calibration alternatives at the 0.9 level, ⌈(n+1)·0.9⌉ = 9 > n. The "split-conformal margin" is therefore the maximum absolute residual, and no finite-sample 90 % guarantee exists.
   - The median offset and the residuals are computed on the same alternatives, so this is not split conformal in the strict sense.
   - Say this in Section 3.3, not only in the threats to validity. The same applies to the nested leave-one-out margins of M3/M4.
9. **p. 7, M5.**
   - An anisotropic squared-exponential GP with white noise and ML-II hyperparameters, fitted on 2–8 points, is prone to over-confident intervals; scripts/budget.py itself notes hyperparameters at their bounds for small k.
   - Report the hyperparameter behaviour, and consider a fully Bayesian GP or fixed, physically motivated length scales as a robustness check.
10. **pp. 7–8, Section 3.4.**
    - (a) "The smallest margin between prediction and requirement that the design stage can resolve" contradicts Eq. (4); see Major 4.
    - (b) State that κ and ω are averaged with equal weight over alternatives and characteristics, and that "beyond" means "at all grid points ≥ δ", as implemented in `beyond()`.
    - (c) The grid is coarse above 10 floors (12, 15, 20, 25, 30, 40, 50, 75, 100, 150, ...), so "150" means "somewhere in (100, 150]". Say so in the footnote of Table 7, and avoid formulations such as "needs requirements 150 floors away".
11. **p. 8, cost bound.** State that correct verdicts are assumed to cost nothing and trials to be error-free, that u depends on δ, and that the bound is an average over the evaluation population.
12. **p. 8, Section 3.5.**
    - Weighting all subsets of size k equally mixes good and poor calibration designs; say so.
    - In Fig. 4, show bracketing and non-bracketing curves separately (and sibling vs. interpolation; Major 5), with bootstrap bands.
13. **pp. 8–9, Section 3.6 and Fig. 1.**
    - Separate the per-family steps (2–5) from the per-design step (6).
    - Show the decision points, e.g. "requirement below the floor → no design-stage decision possible" and "budget curve not yet flat → produce another calibration alternative".
    - Show the output of each step.
14. **p. 9, Section 4.1.**
    - Make explicit that within-family "new designs" are new process settings on an existing tool.
    - Give the production order and dates of the 18 series, since run order matters for drift and for run effects (Major 3c).
15. **p. 9, Section 4.2; p. 20, Section 6.5; p. 23, A.2: the unreported design-space analysis.**
    - The "design-space analysis" of the 264 geometry-varying DDACS simulations is referred to. It is used to question the oil-to-friction mapping and appears in the threats to validity, but its geometric results are not reported; only the process sensitivities (Table A3) and one sentence on a surrogate appear.
    - Report it, since it is the most product-design-relevant part of the work, or remove the references.
16. **p. 9, nominal friction.**
    - The nominal friction of 0.10 is simply the middle of the DDACS range. Given Table A3, M0's 150 floors partly reflect this choice.
    - Consider an "engineer-calibrated" M0 that uses the friction value best matching the production of the other geometry. That would be a more realistic practice baseline.
17. **p. 10, Table 3.** On the scans the wall angle is the mean of three sides (the south wall is shadowed). Confirm that the simulated value uses the same three sides, to support "measured identically".
18. **p. 10, Section 4.4.** "All constants were fixed before the analysis": how can a reader verify this (e.g. time-stamped repository history, a preregistration)? Otherwise rephrase as "chosen a priori and not tuned on the decision results".
19. **pp. 10–11, Section 5.1 and Table 4.** The floor CI resamples batches within alternatives as if they were exchangeable, but under drift adjacent batches are correlated. Use block or alternative-level resampling, or state the limitation.
20. **p. 11, Section 5.2.**
    - "For the wall angle and the dome it exceeds the tested range of 400 kN" is wrong for the wall angle: Table 5 gives 346 kN (289–405).
    - "A design-stage decision between them has nothing to resolve" should be qualified: the patterns are unresolvable in batch centres for these seven characteristics only.
21. **p. 13, Section 5.4.**
    - "Every rule improves by an order of magnitude": M2 (150 → 25) and M3 (150 → 20) improve by factors of only 6 and 7.5.
    - "The intervals in Table A1 do not overlap between M5, M4, M1 and M2": M4 (10–12) and M1 (12–20) share the value 12.
    - In any case, non-overlap of marginal intervals is not a test of a paired difference. Bootstrap the paired differences between rules on common resamples, resampling calibration sets as well as held-out alternatives.
22. **p. 13, internal tension.** "Within a family, the simulation therefore adds little that the production record ... does not already carry, and the best rule combines the simulation envelope with a Gaussian-process correction": the two halves pull in opposite directions (Major 8a).
23. **p. 14, Table 7.** Add one-sided distances (Major 4), and add the right/wrong/trial shares at |d| = 10 for the pooled and transfer scopes.
24. **p. 14, Section 5.5.** Correct the 2.4 % for M5 after the guard; see Major 7.
25. **p. 15, Section 5.6 and Table 9.**
    - (a) "Accepts 6.8 % of the decisions in which the alternative fails" (M1) and "accepts 19 % that fail" (M0) are shares of *all* 162 decisions. Of the 76 decisions in which the alternative fails (results/scen_truth.csv), M1 accepts 11 (14.5 %) and M0 accepts 31 (41 %). Report the conditional false-accept rate, because that is what a designer needs.
    - (b) Report how far the 162 requirements lie from the truth in floors, so that readers can judge how demanding the scenario is. From scen_truth.csv, about 28 % lie within 7 floors, about 60 % within 15 and about a third beyond 25.
    - (c) Explain how the ISO 2768-1 angular classes were turned into one-sided limits: which leg lengths were used, and why only the upper side.
    - (d) On the choice of characteristics, see Major 6(c).
26. **p. 15, Fig. 3.** The symmetric logarithmic axis compresses |d| < 1, which is where the safe distances lie. State the linear threshold of the axis and mark δs and δd on each panel.
27. **p. 17, Table 10.** Add variants for B, α and p (Major 3) and for grouped cross-validation (Major 5).
28. **pp. 17–18, Section 5.8.**
    - (a) Give the uncertainty of the floor, which rests on 18 within-class pairs, and discuss the fact that each batch mixes six or seven orientations.
    - (b) Say how the upper-limit requirement on q95 is applied to hole diameters and to position.
    - (c) Since production resolves only 18 of 120 class pairs, this case cannot discriminate between rules. It shows that the procedure *runs* on another process, not that its findings generalise. Rephrase "a different but equally useful answer" (Section 6.4) accordingly.
29. **p. 19, Section 6.2.** "Four to five produced variants make a calibrated rule reliable ... removes almost all wrong verdicts—a calibration design rather than a sample size": see Majors 5 and 9.
30. **p. 20, Section 6.4.**
    - "Injection moulding with warpage simulations and machining with deflection models fit the same pattern" is unsupported.
    - Replace it with the conditions under which the procedure applies and the practical obstacles, such as the availability of consecutive-series data per variant.
31. **p. 20, Section 6.5.** Add the threats identified in Majors 3–8:
    - near-replicates in the calibration set;
    - a centre-based floor used for a quantile-based decision;
    - dependence of the floor on B and series length;
    - one-sided p = 0.95 requirements;
    - the selection of characteristics in the tolerance scenario;
    - a PBF floor resting on 18 pairs;
    - a single analyst without independent replication.
32. **p. 21, Section 7.** "An applicability guard ... sent nine in ten of these decisions to trial" reads as a feature. In a two-geometry dataset it amounts to "never transfer", and M5 decides a quarter of the unguarded remainder wrongly (Major 7).
33. **pp. 23–25, appendix.**
    - Tables A3 and A5 and the paragraph on in-line verifiability are tangential to the argument; move them to supplementary material.
    - The footnote of Table 5 should state which BHF contrast defines the sensitivity (100 → 500 kN).
34. **Terminology and style.**
    - "Floor" invites confusion with "noise floor"; relate the two explicitly or choose another term.
    - Use "alternative", "design", "variant" and "family" consistently (here, family = geometry).
    - Many sentences carry four or five numbers (e.g. Sections 5.4, 5.5, 6.1). Move numbers into tables and let the text carry the argument.
35. **p. 22, code and data.** Provide an archived, citable version (DOI) already at review, so that reviewers and readers refer to a fixed state. Consider a more descriptive repository name.

---

## 5. Recommendation

**Major revision.**

The core idea deserves publication in RED: score design-stage manufacturability decision rules against production, in a unit that production defines, with explicit abstention and a calibration budget. It addresses a real gap between prediction-accuracy studies in DFM/ML and the decisions designers actually take, and the work is transparent and reproducible.

In its present form, however, the paper has six problems:
- (i) it does not develop or position its constructs as a contribution to design theory and methodology, which creates a substantial desk-rejection risk;
- (ii) it has construct-validity problems, both in the unit and in the operational use of the two distances;
- (iii) its main positive result and two of its guidelines rest on a cross-validation scheme that puts near-replicates of the "new design" into the calibration set, and under grouped cross-validation these results weaken substantially;
- (iv) it misreports the benefit of the applicability guard;
- (v) it states guidelines and machine-learning conclusions beyond its evidence;
- (vi) it does not evaluate its procedure as design support.

Most of these problems can be addressed with the existing data, additional analyses and a substantial reframing, but the revision is large. If the author cannot reframe the contribution beyond the case, I would recommend rejection with encouragement to resubmit.

---

## Appendix: referee's verification notes

- **Checked against the released results.** The following agree with the CSVs in `results/`, except for the items listed in Major 7 and Minor 20, 21 and 25:
  - Table 4 (`alt_floor.csv`);
  - Table 5 (`rob_floor.csv`, `rob_bhf_pairs.csv`);
  - Table 7 and Tables A1–A2 (`dec_resolution.csv`);
  - Table 8 (`budget_design.csv`);
  - the budget statements in Section 5.5 (`budget_resolution.csv`);
  - Table 9 (`scen_scores.csv`);
  - Table 10 (`rob_decisions.csv`);
  - Table 11 (`case2_resolution.csv`);
  - the guard rates (`dec_guard.csv`, `dec_intervals.csv`).
- **Re-analyses.** These were run read-only with the author's own functions in `scripts/decisions.py` and the released tables; no project files were modified. With the same code, the within-family leave-one-out values of Table 7 for M1, M2 and M5 (15/15, 25/0.5, 7/2) were reproduced exactly. The differences below are therefore due to the cross-validation scheme, not to the implementation.

**Within-family decisive/safe distances (floors) under grouped cross-validation:**

| Scheme | M1 | M2 | M5 | M5 at \|d\| = 10: right / wrong / trial |
|---|---|---|---|---|
| Leave-one-alternative-out (paper; reproduced) | 15/15 | 25/0.5 | 7/2 | 97 / 0 / 3 % |
| Leave-one-BHF-level-out, all held-out alternatives | 20/20 | 20/7.5 | 20/7.5 | 75 / 2.8 / 22 % |
| of which held out at 300 kN (interpolation from 100 and 500 kN) | 12/12 | 20/2.5 | 20/2.5 | 77 / 0 / 23 % |
| of which held out at 100 or 500 kN (extrapolation) | 25/25 | 20/12 | 20/10 | 74 / 4.2 / 21 % |

**M2 under the calibration-design subsets of Table 8, with "brackets" split by whether the set contains a same-BHF sibling (safe distance in floors / wrong verdicts at |d| = 10):**

| Calibration set | k = 2 | k = 3 | k = 4 | k = 5 |
|---|---|---|---|---|
| Brackets, same-BHF sibling present | 2.5 / 0 % | 1.5 / 0 % | 1.5 / 0 % | 1 / 0 % |
| Brackets by interpolation, no sibling | 5 / 0 % | 4.5 / 0 % | 4 / 0 % | 3 / 0 % |
| Extrapolates | 12 / 7.9 % | 12 / 5.8 % | 12 / 5.6 % | 12 / 5.2 % |
| Share of bracketing sets that contain a sibling | 81 % | 86 % | 92 % | 96 % |

At k = 1, a bracketing set is a single same-BHF sibling. M1 is then decisive and safe at 4 floors with no wrong verdict at 10 floors (`budget_design.csv`, 252 cases).

**M5 under the same split (k = 2 and 3; decisive/safe distance in floors; wrong / trial at |d| = 10):**

| Calibration set | k = 2 | k = 3 |
|---|---|---|
| Brackets, same-BHF sibling present | 15/2; 0.2 % / 12 % | 15/3; 0.6 % / 10 % |
| Brackets by interpolation, no sibling | 20/4; 0 % / 23 % | 25/3.5; 0.1 % / 24 % |
| Extrapolates | 20/12; 6.7 % / 10.5 % | 20/12; 5.4 % / 18 % |

**Applicability guard, transfer scope.**
- Unguarded cases: 12 of 126 (alternative × characteristic), all of them mid-side draw-in or waviness.
- Wrong verdicts among the 24 unguarded verdicts at |d| = 10: M5 6 (25 %), M1 4, M0 3, M2 0 (M2 sends 12 of the 24 to trial).

**General-tolerance scenario.**
- 76 of the 162 decisions concern alternatives that fail the requirement.
- False accepts: M0 31 (41 % of failing decisions), M1 11 (14.5 %).
- Requirement distances from the truth: about 28 % within 7 floors, about 60 % within 15, and about one third beyond 25.
