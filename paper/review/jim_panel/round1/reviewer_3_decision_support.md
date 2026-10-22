# Referee report: Reviewer 3

**Manuscript:** Evaluating AI-based manufacturability decisions against the resolution of production
**Journal:** Journal of Intelligent Manufacturing
**Round:** First submission
**Reviewer focus:** Industrial decision support: decisions under uncertainty, cost-aware decisions, human–AI collaboration and trust, and the deployment of AI tools in factories
**Date:** 22 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the submission

The paper asks how close to a requirement a design-stage manufacturability prediction can be trusted to decide. Its answer is an evaluation framework rather than a new predictor. Any rule that turns simulation and production evidence into an interval for the 95th percentile of a quality characteristic returns *meets*, *fails* or *trial*. The rule is scored by two points on its operating characteristic: a decisive distance, beyond which at least 95 % of its verdicts are correct, and a safe distance, beyond which at most 5 % are wrong. Both are expressed in "production floors" (the 95 % quantile of the difference between two 50-part batch centres within one run) and are reported separately for each relation of the new design to what has been produced: a sibling, a new force setting, or a new family. A six-step procedure turns them into a guard band for single decisions. On open data of 18 deep-drawn geometry–process alternatives with matched LS-DYNA simulations, fourteen rules are compared. Within a family, the most decisive rules are a look-up of the nearest produced setting and a straight line in force. The simulation, as used, helps only across the two geometries; learned intervals reach close to their nominal coverage only when a sibling has been produced; and release-level requirements (performance index 1.33) lie inside nearly every decisive distance.

## 2. Assessment

- **Originality: adequate.** The building blocks are established: operating characteristics with an indifference zone, conformity-assessment guard bands, selective prediction and grouped cross-validation. Combining them to score manufacturability rules against production, in a unit that production defines and separately by evidence relation, is new in this literature and worth publishing.
- **Significance for intelligent manufacturing: adequate.** When an AI or simulation prediction may replace a physical trial is a central question for deploying such tools. The demonstrated value, however, is confined to process-setting decisions within one die family on one dataset, and there a look-up table wins.
- **Technical soundness: adequate.** The definitions are precise and are implemented as described; my spot checks of the archive reproduced the reported numbers. The guard band, which is the part a factory would deploy, is estimated in-sample, pooled over two families and seven characteristics, and under a prior chosen for convenience (major comment 2).
- **AI/ML methodology, baselines and evaluation protocol: adequate.** The production-record baseline, the paired with/without-simulation ablations and the relation-specific grouped cross-validation are exemplary. The learners themselves are minimal (Gaussian processes on three descriptors, boosting with fixed settings), their intervals are largely set by an imposed noise floor, and the learner-sensitivity analysis in the archive is not reported.
- **Evidence supports the claims: weak.** The dataset-specific findings are carefully hedged. The title and abstract, however, claim an evaluation standard for AI-based manufacturability support, extending to classifiers and language-model checks. That claim rests on one process, two geometries, two transfers between families and an unvalidated procedure.
- **Clarity, organisation and length: weak.** The text is very dense, saturated with numbers, coined terms and cryptic rule labels. Readers of this journal will find it hard to extract the main message.
- **Positioning and references: adequate.** Engineering design, V&V, conformity assessment and statistical quality control are covered well. The intelligent-manufacturing streams closest to the contribution are missing: reliance indices in virtual metrology, transfer learning across products, human–AI decision-making with uncertainty displays, and cost-sensitive evaluation.
- **Fit to JIM's scope: adequate.** An evaluation methodology for AI decision support, demonstrated on real production data, is within scope. The paper is currently written for an engineering-design and metrology audience rather than for people who develop and deploy AI in manufacturing.

**Main strengths.**

- **A clearly posed, practically important question.** "Can this prediction be relied on to decide?" (L058–060) is answered with an explicit trial/abstain verdict, which matches how tryout engineers actually work.
- **Decisiveness and safety are kept apart, and rules are qualified per evidence relation.** This exposes failures that pooled accuracy hides. The scaled simulation looks good with a sibling (4.9 floors) but falsely accepts failing alternatives up to 164 floors from their limit when extrapolating (L629–631). That single finding justifies the relation-specific design.
- **The right baselines.** The nearest-produced-setting and no-simulation baselines (L505–508) are exactly the comparisons that machine-learning-for-manufacturing papers often omit.
- **Unusual candour.** The paper keeps a development record (Section 4.5), names its selection optimism, discusses threats to validity, and reports a failed attempt on a second process (L1020–1024).
- **Open data and a verifiable archive.** All 127 entries of `SHA256SUMS` verify. Every number I spot-checked against the result files matched: Table A4, the worked example, the shares in Section 5.8, and the decomposition and sibling strata in Section 5.4.

## 3. Major comments

### 1. The main message is hard for this journal's readers to reach

**Problem.** The density of the text, rather than its length, hides the findings.

- **Abstract (L020–040).** It gives about 25 numbers before the reader knows what a floor, a sibling, a near-replicate or "95 % conformance" is. The closing sentence states a conclusion (a "standard") rather than a finding.
- **Concentrated definitions.** Six coined terms are introduced in one paragraph (L075–083), and fourteen rules in another (L292–314). The definition of the guard band, its prior, the search grid and the role of the guards share a single 40-line paragraph (L403–446).
- **Numbers in the Results.** Results paragraphs carry 15–25 numbers each (e.g. L625–639, L698–729, L829–849). Section 5.8 combines capability limits, a tolerance scenario and a cost analysis in one paragraph.
- **Inconsistent names for the same object.**
  - "new variant", "sibling", "with a produced sibling" and "sibling produced";
  - "nearest produced setting", "nearest setting" and NN;
  - "force trend" and M1sn;
  - M3n is "M4" in the code;
  - $q_p$ and $q_{95}$ alternate.
- **Table 4.** It mixes δd/δs pairs, single values for point rules, an FA column, interval rows, interpolation/extrapolation sub-columns and pooled scopes in one table.

**Why it matters.** The findings are useful to practitioners but buried:
- a simple production look-up beat the learned models within a family;
- nothing was reliable near release-level limits without a produced sibling;
- relation-specific qualification catches dangerous extrapolation.

**What would fix it.**
- **(a) A schematic figure** early in Section 3: the verdict shares of one rule against $d$, with δd and δs marked, and how a guard band acts on the observable margin.
- **(b) An early worked example.** Introduce the worked example now at L813–826 in Section 3 and carry it through steps 1–6.
- **(c) Lead with the reading of L376–377.** For a rule that always decides, δd is close to the 90th percentile of its absolute error in floors. Most readers will grasp this at once, and it shows what the framework adds for rules that abstain.
- **(d) Fewer rules in the main text.** Keep five or six rules (M0, M1s, M1sn, M2, M5, NN) with descriptive labels. Move the remaining rules, M6, the surrogate, the variance decomposition, Table 6 and most of Section 5.9 to supplementary material.
- **(e) A shorter abstract**, with at most five numbers and one plain-language conclusion.
- **(f) An "implications for practice" paragraph** or box.

The space freed by (d) would pay for (a)–(c).

### 2. The guard band does not follow the procedure as defined and has not been validated

**Problem.** The way g is estimated in the demonstration differs from the procedure in three respects:
- **Per family vs pooled.** Step 5 is defined once per design family (L403–410), and step 6 applies the band to single verdicts on one characteristic. In the demonstration, g (Table A4) is computed once per rule and relation, pooled over both geometries and all seven characteristics.
- **In-sample.** g is chosen on the same cases on which the step-6 distances and trial rates are then reported. The paper acknowledges this (L808–809, L824–826).
- **A convenient prior.** The reference prior (47 grid distances within ±20 floors, L412–439) is a convenience, not an estimate. The paper's own capability analysis (L830–833) places release-level requirements about 1.7 floors from $q_{95}$. Under the corresponding ±5-floor prior, the bands of the nearest setting grow from 0.25 / 2.0 / 7.0 to 2.0 / 4.25 / 14.25 floors (L800–804).

**My checks.** I recomputed g from `results/dec_intervals.csv` with the archived definitions, which reproduce Table A4 exactly. The author should confirm these figures:
- **Leave-one-alternative-out.** Estimating g this way barely changes the share of correct decided verdicts under the reference prior: 0.945–0.99 for NN, M1sn, M2 and M5. This is reassuring and worth reporting. Under the ±5-floor prior it falls to about 0.91–0.93 for NN and M5n when extrapolating, where few verdicts are decided at all.
- **Per geometry, as step 5 prescribes.** The bands differ between the two geometries:
  - NN interpolating: 1.5 vs 2.5 floors;
  - NN extrapolating: 9.5 vs 5.75 floors;
  - M5 extrapolating: qualifies in one geometry (5.0 floors) and not in the other.

  Applying the extrapolation bands of M2 and M5 from the convex to the concave geometry gives only about 83–84 % correct decided verdicts.
- **Per characteristic.** With a sibling and g = 0.25, NN is right in about 89 % of decided verdicts on the bottom dome and 98.5 % on the flange waviness. The 95 % holds on average over characteristics, but a team decides per characteristic.
- **Trial rates under a release-like prior.** Under the ±5-floor prior, the nearest setting with its band decides only about 63 %, 32 % and 2 % of feasible verdicts with a sibling, interpolating and extrapolating respectively.

**Why it matters.** The guard band is the element a practitioner would put into service. A 95 % claim that holds only pooled over families and characteristics, in-sample and under a convenient prior, invites over-reliance.

**What would fix it.**
- **(a) Estimate g per family** as step 5 prescribes, or justify pooling families and reconcile that with the new-family relation.
- **(b) Estimate g by cross-validation**, leaving out one alternative or one force level. Report the out-of-sample share correct and the trial rate, with bootstrap intervals.
- **(c) Report g per characteristic or per class of characteristic** (draw-ins, angles, form), or state plainly that the 95 % is an average over characteristics.
- **(d) Ground the prior in data a team would have**, such as the capability margins of released parts in the family. Alternatively, show g and the trial rate as functions of the prior's width. Since Section 5.8 argues that requirements lie near release level, use a release-like prior as the reference.
- **(e) Move Table A4 into the main text**, and add a curve of g against the number of produced alternatives, analogous to Fig. 3.

### 3. The distances support planning and comparison; deployment decisions also need costs, trial rates and part-level verdicts

**Problem.** δd and δs have four properties that limit them as deployment quantities:
- they are defined on the true margin;
- they use fixed 95 %/5 % thresholds;
- they weight false accepts and false rejects equally (the one-sided values appear only as a footnoted column);
- they treat a trial as neither costly nor fallible.

Costs appear only at L842–849, and only for the ISO 2768-1 scenario of two angular characteristics.
- **Within a family**, the cheapest rules have zero expected cost in that scenario (`scen_cost_map.csv`), so the analysis cannot discriminate between them there.
- **The only informative case** is the new family, which rests on two transfers.
- **The expected-cost formula** used ($c_\mathrm{FA}P_\mathrm{FA} + c_\mathrm{FR}P_\mathrm{FR} + c_\mathrm{T}P_\mathrm{trial}$) is in `scripts/scenarios.py` but not in the paper.

**Why it matters.** Whether to deploy a rule, and how wide its guard band should be, are cost questions, and the 95 % target fixes one implicit cost ratio. I made a rough recomputation from `dec_intervals.csv` under the reference prior, with $c_\mathrm{FR} = 0.5\,c_\mathrm{FA}$, letting the trial cost fall from 0.5 to 0.02 of a false accept:
- **Cost-minimising bands for the nearest setting** ranged from 0 to about 4.5 floors with a sibling, and from 0 to about 15 floors when extrapolating.
- **The reported 95 % bands** correspond roughly to a trial costing a tenth to a half of a false accept, depending on the relation.
- **In practice**, trying a new force on an existing die is probably cheaper than that, so cost-optimal bands would be wider than those reported.

**Missing deployment aspects.**
- **The trial is itself a noisy measurement.** It reproduces $q_{95}$ to about one floor within a run (L382–385), and series differ by up to 9.8 floors (L567–570). The end-to-end error of the procedure (rule plus trial) is never estimated. The test-planning models the paper already cites (Thomke and Bell 2001; Salado and Kannan 2018) treat test fidelity explicitly and could be used.
- **Release is a part-level decision over all characteristics.** With seven characteristics each decided at 95 %, the joint verdict can be wrong far more often than any single one. The paper neither defines nor scores a part-level verdict.
- **The economic message is buried.** The paper notes that the rules decide reliably where trials are cheapest and never where they are dearest (L925–930). This deserves a number, such as expected trials saved and errors incurred per 100 decisions under stated costs, and a place in the abstract.

**What would fix it.**
- **A loss function in Section 3**, introduced next to Eq. (1).
- **Expected cost and trial rate** reported alongside δd and δs.
- **A decision-curve-style figure** showing the cost-optimal band and rule as functions of $c_\mathrm{T}/c_\mathrm{FA}$ and $c_\mathrm{FR}/c_\mathrm{FA}$.
- **One-sided distances** in the main table.
- **A defined and scored part-level verdict.**
- **A treatment of the trial's own error**, by discussion or by a model.

### 4. The claims outrun the evidence and the scope of the demonstration

**Problem.** The title, the closing sentence of the abstract (L038–040: "This gives AI-based manufacturability support a production-referenced evaluation standard") and the contribution list (L096–098: "including classifiers and language-model checks") promise more than the study can show:

- **Mostly process settings, and a thin new-family test.** The only change of product design is one binary geometry contrast that changes three features at once (L455–456). The new-family evidence rests on two transfers (L1029–1031).
- **The sibling relation is close to a replicate test.** Lubrication is resolved in only 51 of 126 contrasts (L578–580), so in 58 of the 126 sibling cases the "new design" is a near-replicate run (L643–646). The simulation also cannot distinguish siblings, by construction (L311–314). The finding that the simulation adds nothing with a sibling is therefore partly built into the design.
- **The tools that motivate the paper are not scored.** The "AI" evaluated is a three-descriptor Gaussian process and gradient boosting fitted to 6–9 alternatives. The GP noise variance sits at its imposed lower bound in 97–99 % of the fits with a sibling and in every other fit (L720–724). None of the tools named as motivation (L053–058, L107–118) is evaluated: CAD-based learned models, surrogates trained across geometries, or language-model checks.
- **The reuse claims are untested.** The classifier and language-model adaptations (L999–1005) and Table 6 have not been tried, and the one attempt on another process failed (L1020–1024).
- **Post-hoc choices.** The rule set, the grouped schemes, the guard bands and their prior were partly chosen after results had been seen (L522–531).

**Why it matters.** Readers of this journal will take the title to promise an evaluation of AI-based manufacturability tools. The evidence supports a narrower statement.

**What would fix it.**
- **(a) Reframe and retitle around what was shown.** For example: a production-referenced evaluation of design-stage decision rules for process-setting changes and die-family transfer in deep drawing, with AI tools as one class of rule.
- **(b) End the abstract with a finding**, not with the claim of a standard.
- **(c) Score one representative AI tool, or call Section 6.5 a proposal.** Possible tools are a language-model check scored with the protocol of L1002–1005 on the 126 cases, or a learned model pre-trained on the DDACS geometries and transferred. Otherwise, present Section 6.5 explicitly as an untested proposal.
- **(d) Freeze and test the procedure.** Freeze the procedure, state the protocol of the confirmatory test, and if possible report it on a second production dataset. If that cannot be done, say so in the abstract.

### 5. The unit is hard to communicate and hides differences between characteristics

**Problem.** Three properties of the floor make it a difficult unit for engineers:
- **It depends on the protocol.** Other floor protocols rescale the decisive distances by 0.60–1.42 (L855–856; Table A2).
- **It is a within-run quantity.** The floor between series is 1.5–9.1 times larger (L567–570). Measured in that floor, NN's sibling distance is 0.75 rather than 3.4, although the footnote of Table A2 rightly calls this partly circular.
- **It is unfamiliar.** Engineers think in tolerance, mm, $P_\mathrm{pk}$ or ppm.

Results are also pooled over seven characteristics with different physics. The archive contains per-characteristic distances in physical units (`results/panel_physical_units.csv`) that the paper does not report, and they vary widely (in pooled floors):
- the nearest setting needs about 1.8 (wall angle) to 14.6 (waviness) for a new setting;
- M5 needs 2.4 (waviness) to 13.7 (dome) with a sibling.

**Why it matters.** A guard band shown to an engineer "in floors" means something only if the floor's protocol is clear, together with its relation to the tolerance and to run-to-run variation. Pooled numbers can mislead decisions made on one characteristic.

**What would fix it.**
- **Physical units.** Report the main distances also in physical units, and relative to the tolerance or to $\sigma_\mathrm{LT}$.
- **Per-characteristic results.** Add an appendix table of results per characteristic.
- **Translations in the guidance.** In Table 5, say what a margin of so many floors means in mm for each characteristic, and that run-to-run variation can exceed it.
- **What the within-run floor implies.** State what it means for decisions about future series, which are other runs.
- **Between-run units where possible.** Where replicate runs exist, report results in a between-run unit as well.

### 6. The reuse section and the reporting checklist need to be operational

**Problem.** Section 6.5 compresses three adaptations into a few sentences (L998–1009), and the checklist (L1010–1016) is incomplete.
- **(i) Classifiers.** Scoring a classifier "by binning test cases by their true margin" requires a continuous, production-referenced outcome for every test design. CAD-based manufacturability datasets normally lack this, which limits reuse and should be said.
- **(ii) Language-model checks.** The protocol (repeated queries, monotonicity) omits:
  - the model's identity and version, and the query date;
  - decoding settings;
  - prompt paraphrases;
  - the handling of refusals and hedged answers, which are natural "trial" verdicts;
  - contamination: RDDAC, DDACS and the papers describing them are public.
- **(iii) Generative tools.** "A generative tool's manufacturability check is scored." (L1009) is an incomplete thought.
- **(iv) The checklist omits five items:**
  - the decision thresholds and costs;
  - whether g was estimated out of sample;
  - per-characteristic results;
  - case counts per relation, where the unit of replication is the alternative, not the case;
  - the development record that the paper itself models well in Section 4.5.

**Why it matters.** For readers who build or buy such tools, the checklist is the most reusable output of the paper. If it is to serve as a reporting standard, it must be precise enough to audit a published evaluation.

**What would fix it.**
- **Present the checklist as a table** (item, why it matters, how this paper reports it, and where). Model it on established reporting guidance for prediction models, such as model cards (Mitchell et al. 2019, FAT\* conference) and TRIPOD+AI (Collins et al. 2024, BMJ).
- **Add the missing items** listed under (iv).
- **Expand the language-model protocol** with the elements listed under (ii).
- **Release the scoring as a small documented function**, separate from the dataset-specific pipeline. It would take a table of intervals, truths and floors and return δd, δs, g and trial rates, so that others can apply it to their own tools.

### 7. Positioning within the intelligent-manufacturing literature

**Problem.** Table 1 and Section 2 position the framework against design theory, V&V, conformal prediction and statistical quality control, but not against the intelligent-manufacturing work closest to it.

- **Reliance indices in virtual metrology.** Automatic virtual metrology attaches to each prediction a reliance index, and a global similarity index that flags samples unlike the training data (e.g. Cheng et al. 2008, *IEEE Transactions on Semiconductor Manufacturing*). These are the direct analogue of the guard band and the applicability guards.
- **Conformity-assessment risks.** JCGM 106:2012 computes the global consumer's and producer's risks of conformity assessment from a prior on the measurand. The prior-dependent guard band is the design-stage counterpart of these risks, and this framing would explain why g "belongs to the prior" (L800).
- **Domain shift.** The new-family relation is a domain-shift problem. The substantial literature in this journal and elsewhere on transfer learning and domain adaptation across machines, products and process conditions is not discussed.
- **Human–AI decision-making.** Showing confidence can calibrate trust without improving joint accuracy (Zhang, Liao and Bellamy 2020, FAT\* conference). This bears directly on the hypotheses at L951–958.
- **Cost-sensitive evaluation.** Cost-sensitive learning (Elkan 2001) and decision curve analysis (Vickers and Elkin 2006) are established ways to present the costs asked for in comment 3.

**What would fix it.**
- **A paragraph on these streams** in Section 2.
- **A row in Table 1** for virtual metrology with reliance indices.
- **A clear account of what is adopted and what is new.** Adopted: the indifference zone, the guard band, selective risk and grouped cross-validation. New: the production-defined unit, the evidence relations, and their combination for design-stage decisions.

### 8. Human–AI collaboration and the deployment lifecycle are asserted rather than addressed

**Problem.** As the paper states, the framework is evaluated for structural validity only (L985–988), and usefulness is "not evaluated" (Table 5). The two hypotheses on reliance (L951–958) are sensible but under-specified. The paper leaves three practical matters unaddressed:
- how a verdict, its margin and its guard band would be shown to a tryout engineer;
- how a qualification is maintained after deployment, as production varies between runs (1.2–9.8 floors between series, L567–570) and dies wear;
- how evidence added later should be handled ("repeated when production evidence is added", L403–405).

**Why it matters.** AI decision support in factories fails through miscalibrated reliance and silent drift as often as through model error.

**What would fix it.**
- **(a) Specify the planned user study:** the task, cases of known outcome, outcome measures (over- and under-reliance, decision cost) and the design.
- **(b) Describe the interface** through which a step-6 verdict is presented.
- **(c) Add a monitoring step.** Track the realised errors of step-6 verdicts against later production, for example with a control chart on decision outcomes, and define when a rule must be re-qualified.
- **(d) Weigh the cost of the evidence itself** against the trials it saves: several 500-part series per family must be produced before any rule qualifies.

## 4. Minor comments

1. **Abstract (L020–040).** Besides major comment 1: "learned 90 % intervals covered 85–96 %" includes M2 and M2n. These are not learned, and their attainable level is below 90 % (L315–318).
2. **Keywords (L041–042).** Consider adding *decision support*, *selective prediction* (or *abstention*) and *conformity assessment*.
3. **L149–152.** "Conformal prediction gives … and have entered": the subject and verb do not agree.
4. **L315–322 and the footnote of Table A3 (L1159–1161).** "Nominal 90" is stated for all interval rules. The largest-residual margins and the jackknife+ intervals guarantee only $(n-1)/(n+1)$ and 0.71–0.80 here. Give the guaranteed or nominal level for each rule.
5. **L362–373.** As δ grows, failing-side requirements become infeasible, so the pooled κ and ω drift towards the adequate side (from half to a third of the weight). A rule biased towards *meets* therefore gains at large δ. Weighting the two sides equally, or giving one-sided distances priority, would remove this drift.
6. **L372–377.** δd is the last crossing of the threshold, so a few verdicts far out can move it (e.g. 325 floors for M2n, pooled, in Table 4). State how many verdicts determine each distance.
7. **L403–446.** Split this paragraph, and give pseudocode for steps 5 and 6.
8. **Fig. 1 (L415–430).** The italic text in the boxes of steps 3 and 5 appears to run into the bottom border. The requirement prior and the costs are inputs to step 5 and could be drawn as dashed input boxes.
9. **L507–508.** "A scope comprises 126 cases": the units of replication are 18 alternatives (9 per family), and the characteristics of one alternative are correlated. Say so wherever case counts support a claim, including the "Basis" column of Table 5.
10. **L520–535.** "… drafting and these reviews" is unclear. State that the internal reviews were simulated with a language model and which additions they caused. The statement on AI use belongs in the declarations; the development record can stay in Section 4.5.
11. **Fig. 2 (L599–623).** The tick labels are small, and the solid and dashed lines for δd and δs are hard to tell apart on the coloured areas. Fewer panels or a larger figure would help.
12. **L629–631.** The scaled simulation's false accepts up to 164 floors away when extrapolating is a key safety result. Carry it into the Discussion and the abstract.
13. **L687–694.** The share of variance attributed to the rule rather than the relation depends on which rules are included, and several rules are deliberately weak. Report the decomposition for a pre-specified subset of rules, or drop it.
14. **L718–729.** The GP noise variance sits at its imposed lower bound in 97–99 % of the fits with a sibling and in every other fit, so the coverage of the "learned" intervals is largely the analyst's choice. Say so wherever that coverage is claimed (abstract; L1059–1060).
15. **Sections 5.5 and 5.9.** The archive includes a learner-sensitivity analysis of M3/M3n in `scripts/tuning.py` (regularised, flexible, ridge, quantile-loss and nested-selected settings). The paper neither mentions it nor maps it in Table A5. A two-sentence summary would answer the obvious question of whether the learned rules were handicapped by their settings.
16. **L760–766.** State the minimum series length and number of produced alternatives that steps 2 and 5 need. The floors and the reference truths here came from full 500-part series.
17. **Section 5.8 (L829–849).** Split it into capability-anchored limits and costs, and give the cost formula and a results table. Note that within a family the ISO 2768-1 scenario gives zero expected cost for the best rules, so it cannot discriminate there.
18. **Fig. 4 (L783–799).** The filled markers for g are hard to see; label g explicitly.
19. **Table 5 (L875–903).** Give numbers of alternatives and transfers in the "Basis" column rather than cases. The prescriptive rows ("Choosing a rule", "Deciding a single design") should mention costs.
20. **L930–932.** The transparency of the nearest setting is a genuine advantage in deployment. Consider making explainability an explicit criterion for choosing a rule.
21. **L1009.** This sentence is incomplete (see major comment 6).
22. **L1017–1024.** The PA12 attempt is a useful negative result. State what data would have sufficed: alternatives, parts per build, and builds.
23. **Section 6.6 (L1026–1041).** Add four threats: the pooling of g over families and characteristics, the reference prior, the missing part-level decision, and the cost assumptions.
24. **References.** The archive is cited as Canseven (2026) with "[DOI pending]"; a DOI is needed before acceptance. Please also check the editions cited as ISO 5725-2:2025 and ISO 22514-2:2026; the editions I know are 2019 and 2017.
25. **Data and code availability (L1206–1215).**
    - `RELEASE_NOTES.md` refers to a `LICENSE` file for the code, but no such file is among the release files.
    - `.zenodo.json` and `CITATION.cff` state no licence.
    - `requirements.txt` leaves `pyarrow` and `remotezip` unpinned.

## 5. Recommendation

**Major revision.**

The paper addresses a question that matters for deploying AI in manufacturing: when may a design-stage prediction replace a trial? It brings an idea that I would like to see in the journal: score decision rules, including abstention, against production, in a unit production defines, separately by how novel the new design is. The analysis is careful, candid and reproducible, and its sobering results are valuable. Within a family, a look-up of the produced record beat the learned models; near release-level limits nothing replaced a trial; and qualification by relation catches dangerous extrapolation.

In its present form, however, the paper is not ready, for four reasons:
1. Its main message is buried under its density.
2. The guard band, the element practitioners would deploy, is estimated in a way that departs from the procedure as defined and is not validated out of sample, per family or per characteristic.
3. The decision quantities are not connected to the costs of errors and trials that decide deployment.
4. The title and abstract claim an evaluation standard for AI-based manufacturability support, including classifiers and language-model checks, that one dataset with two family transfers cannot carry.

All four can be fixed with the data and code the author already has: a rewrite, cross-validated per-family guard bands, a loss-based presentation and narrowed claims. I would be glad to review a revised version.

## 6. Confidential comments to the editor

I see a publishable contribution here, but only after a substantial rewrite and narrower claims. My spot checks against the archive reproduced every number I checked, and all checksums verify, which speaks well for the integrity of the analysis.

The manuscript discloses extensive use of a language model: for code, data analysis and drafting, and for simulated internal reviews that led to rules and analyses being added after results were seen (Section 4.5). The disclosure is explicit, and the author retains responsibility. The editor may nonetheless wish to confirm that this extent of use is acceptable under the journal's policy, and to ask for the wording to be made unambiguous ("these reviews", L534–535). Because the rule set and the guard-band prior were partly shaped after results were seen, a confirmatory test or clearly narrowed claims matter more than usual.

My report concentrates on decision support. The estimation of the floor and the bootstrap designs would benefit from a statistician's view if the panel does not already include one.
