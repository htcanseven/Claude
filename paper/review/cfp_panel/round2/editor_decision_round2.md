# Editorial decision, second round

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design (Springer)
**Collection:** special collection "AI in Design for Manufacturing"
**Version considered:** the revised manuscript (a single file of 30 pages, in the line-numbered copy the reviewers read) and the author's point-by-point response
**Reports considered:**
- second-round reports of Reviewer A (design theory and methodology), Reviewer B (AI in design for manufacturing) and Reviewer C (manufacturing process design and production quality), all three recommending minor revision;
- for reference, the three first-round reports and my first-round decision of 5 October 2026.

**Date:** 6 October 2026

*Written by an AI agent in the persona of a fictional handling guest editor of a simulated review panel; it does not come from the journal or speak for any real person.*

---

## Part 1: Decision letter to the author

Dear Hüseyin Tayyer Canseven,

Thank you for the revised manuscript, and for a response that takes up every comment of the first round. The three reviewers of the first version have reported on the revision, and their reports are attached. I have read the revised manuscript, your response and the three reports against my first-round letter.

As in the first round, I re-checked some points myself, read-only, against your released code and result files and with your own estimator (`exclusion`, `distance_pair`) and guard-band code (`guard_band`). I did so wherever my decision depends on a reviewer's figure, wherever the reviewers disagree, and wherever a reviewer might be mistaken. Section 6 lists what I checked and what I found.

**Decision: minor revision.**

The revision is substantial, and it is a good one:

- the claims are conditioned on one simulator and one small factorial;
- the pooled scopes, M6, the sibling strata and the force-level split are reported;
- the learned models have a fair small-data specification;
- the refit bootstrap keeps every case in its evidence relation;
- step 6 is specified, and one decision is worked through;
- the paper is positioned in the design literature and offers a reuse section and a reporting standard;
- it is eight pages shorter.

The paper now presents itself as what my first letter asked it to be: a production-referenced evaluation standard for design-stage manufacturability decisions, AI-based or not. All three reviewers recommend minor revision, and I agree.

What remains concerns claims and reporting, not data or method:

- Your response presents one conclusion as changed: that a rescaled simulation adds information within a family. It does not survive the comparison without the simulation that your own evaluation design calls for.
- The guard band of step 6 depends on a requirement prior that the paper does not state, and the procedure's operating characteristics are reported for one rule only.
- The new-family results are headlined in a floor that, by the procedure's own account, a team would not have.
- The abstract and the conclusions have not taken up the strata and the force split that the body now reports.
- Several descriptions of methods and analyses are inaccurate.
- The numbers cannot yet be traced to a citable archive.

None of this needs new data or new modelling. Two of the corrections strengthen your sober message rather than weaken it:

- within a family, the production record carries the decision even against a rescaled simulation;
- release-level requirements need trials even more clearly once the prior of the guard band is explicit.

### 1. Synthesis of the second-round reports

**Where the reviewers agree.**

- **Their verdict.** All three:
  - find the revision responsive and careful;
  - raise "evidence supports the claims" from weak to adequate;
  - rate the fit to RED and to the collection as adequate;
  - recommend minor revision.
- **Their checks.** Between them they re-derived from your released files all of Table 4 and Table A2, the decomposition, the strata and force split, the paired differences, the coverage figures, the guard bands, the worked example and the capability shares. They found no computational error.
- **No leakage.** Reviewers B and C checked that the new noise floor of the Gaussian processes uses the calibration alternatives only, so that a held-out truth cannot leak into its own interval. I confirm this from `noise_floor` and `m5_fit`.
- **No new data, no further round.** None of them asks for new data. None needs to see the manuscript again if I check the changes; Reviewer A offers to check the three substantive points.
- **The remaining issues.** They raised most of them independently:

| Issue | A | B | C | Item |
|---|---|---|---|---|
| The rescaled simulation (M1s) and the "exception" | N1 | N3(a) | C5(c) | S1 |
| The requirement prior of the guard band; step 6 reported for one rule only | N3 | N1, N2 | N6 | S2 |
| New family scored in the floor of the unproduced family | N2, m13, r6 | N3(e) | N3 | S3 |
| 3.4 and 8.5 floors quoted without the strata and the split | m12 | N3(b) | C4 | S4 |
| Release-level requirements "inside every decisive distance"; one-sided capability test | m7 | N3(d) | N2, m12 | S4 |
| Findings labelled as following from the definitions | m5, m6 | N7 | – | S4 |
| "Within the family" used in two senses | m3 | N8 | m1 | S4 |
| Table 3 combines different aggregates | m4 | – | N4 | S5 |
| Short calibration series read as qualification | m2 | – | N1 | S5 |
| The jackknife+ guarantee; the design of the refit bootstrap | – | N5; N4 | – | S5 |
| The trial is itself a run | m15 | – | C3 | S5 |
| The surrogate statement | m8 | N10 | – | S5 |
| No result file named; DOI pending | m1 | N2 | N5 | S6 |
| The reuse section and Table 6 | m10 | B7; p1, p2 | C7 | S7 |
| The cost sentence of Section 5.8 | r4 | p9 | N7 | recommended |
| The designer-study "hypotheses" | m14 | p4 | – | recommended |
| The transparency of the nearest produced setting | r10 | N9 | – | recommended |
| The editions of ISO 5725-2 and ISO 22514-2 | r11 | – | C1(ii) | recommended |
| M6 in Table 4 against the table notes | r2 | p8 | m9 | editorial |

*Notation.*

- A-N1 is Reviewer A's new issue N1, and A-m4 is A's new minor point 4.
- A-r4 is point 4 of A's Section 5, and likewise B-p4 for Reviewer B and C-m4 for Reviewer C.
- C-C4 is Reviewer C's remaining comment under the first-round comment C4.

**Where they differ.**

- **The rescaled simulation.** All three see a contradiction between two statements:
  - the abstract and the conclusions say that "the simulation, as used, helped only across families";
  - Sections 5.5 and 6.1 say that "a fitted scale made it useful within a family".

  Reviewers B and C would correct the abstract to follow Section 6.1. Reviewer A would correct Section 6.1, because the rescaled simulation does worse than a straight line in force without the simulation. I checked, and Reviewer A is right (S1).
- **Section 6.4.** Reviewer A finds it still a list of correspondences; Reviewers B and C find it now argued strand by strand. I make A's suggestions a strong recommendation, not a condition.
- **The within-family headline.** Reviewer C would restate it as "about 5 floors whenever the new design differs resolvably, except where force and stroke speed changed together". Reviewers A and B ask only for the strata and the split. I require the stratified figures, not C's interpretation (Section 6).
- **Supplementary material.** The reviewers propose different remedies:
  - A would accept either electronic supplementary material or an appendix table that maps numbers to files;
  - B asks for one appendix or supplementary table and a mapping list;
  - C asks for a mapping table.

  Section 2 sets out what I require.

### 2. My assessment, fit and format

**Assessment.** I share the reviewers' view of the revision. My own checks (Section 6) add five observations, which shape the requirements below.

1. **The rescaled simulation.** Reviewer A's comparison of the scaled simulation with a straight line in force reproduces exactly, and the difference is resolvable in both within-family relations. My own first-round letter (R3d) invited the opposite reading: it suggested that "within a family it adds nothing" should refer only to the additive use of the simulation. I withdraw that suggestion.
2. **The guard band.** Both reviewers' tables of the guard band under other requirement priors reproduce. The guard band is therefore a property of a rule, a relation and a distribution of requirement distances, not of the rule and the relation alone.
3. **The new family.** The reviewers are right that which rule is safest depends on the floor used. But the ranking they report in the produced family's floor (M3 safest) is no better resolved than yours. Neither ranking is a finding of two transfers.
4. **Table 3.** That σ_w exceeds σ_LT is an artefact of combining a median with a pooled root mean square. Series by series, σ_w does not exceed σ_LT beyond a degrees-of-freedom effect of at most 0.4 %.
5. **Traceability.** The manuscript names no result file; the LaTeX source contains none. The archive DOI is still pending, although my first letter required it at resubmission.

**Accuracy of the response.** In several places, listed at the end of Section 6, the response says more than the manuscript does. Like Reviewer B, I read this as compression rather than misrepresentation. The next response must, however, be exact, because I shall check it against the manuscript and the archive myself.

**Fit to RED: yes.** The paper:

- defines constructs for design-stage decisions: a production-referenced unit, decisive and safe distances by evidence relation, and a guard-banded procedure;
- evaluates them on production data against a production-record baseline;
- labels that evaluation correctly, in the terms of the design research methodology, as a prescriptive study with an initial support evaluation;
- bounds its applicability by stated prerequisites.

It is neither a case study of an individual design effort nor a mere application of existing tools. Broad applicability is argued through prerequisites and a process mapping rather than shown. For a first methodology paper with one demonstration that is acceptable, provided Table 6 is marked as a proposal (S7).

**Fit to the collection: yes.** My first letter set four conditions under which the paper's modest AI content earns it a place:

1. a fair small-data specification of the learned models;
2. the pooled scopes reported;
3. the AI conclusions conditioned on the data regime;
4. a demonstration of how the framework applies to AI tools other than interval regressors.

The first three are met, subject to wording corrections (S4). The fourth is partly met: Section 6.5 gives the black-box formulation in a single sentence (S7). The paper belongs in the collection as an evaluation standard for AI-based manufacturability support, which is how it now presents itself. I no longer see a case for moving it to RED's regular stream.

**Format and length.** A single file of 30 pages without electronic supplementary material is acceptable for the journal. The main text ends on page 23, with six tables and four figures, which meets the targets I set; the appendix carries the notation and the robustness results.

What is not acceptable is the present state of the references to results that the paper quotes but does not tabulate: the manuscript does not name them, and they sit in a repository without a DOI. I therefore accept the format on three conditions (S6):

- the numbers that carry claims are in the paper itself: the table of S2 and the new-family figures of S3;
- every other number quoted in the text is traced, by a short appendix table, to its script and result file;
- those files are deposited in a versioned archive with a DOI, which the paper cites.

If you prefer, Springer's electronic supplementary material is an equally acceptable route for the second condition. Additions should go to the appendix; the main text should not grow by more than about half a page.

### 3. Status of the required revisions of the first round

**R1. Bring every general claim into line with the evidence: partly satisfied (largely met).**

*Met:*

- **The headline** is replaced by the best attainable distance per relation and a decomposition of the log decisive distance. Reviewers A and B reproduced the decomposition, and I confirm it:

  | Relations included | Relation | Rule |
  |---|---|---|
  | all three | 69 % | 6 % |
  | within a family | 15 % | 68 % |

- **RQ3** is conditioned on the simulator and the data regime, and the learners' behaviour is explained by their inductive biases.
- **The new family** is presented as two transfers.
- **Scope and anchors.** Scope, conformance level and physical and capability anchors are in the abstract and the introduction.
- **Wording.**
  - "Reliable" replaces "trusted", and "calibrated abstention" is gone.
  - Section 6.4 claims structural validity and a support evaluation.
  - Table 5 has a basis column.
  - "None is specific to forming" is removed.

*Open:*

- the new claim about the rescaled simulation (S1);
- overstatements in the abstract and conclusions, and two mislabelled findings (S4).

**R2. Make the unit and the two distances well defined for every relation: partly satisfied.**

*Met:*

- **(a) Positioning.** The floor is positioned against ISO 5725 and ISO 22514-2; a refinement is recommended in Section 5.
- **(b) Protocol.** A reference protocol, the lag profile, σ_b, σ_w and F/σ_LT are reported, and RQ1 now says "common production-referenced scale". Table 3's components are, however, inconsistent (S5).
- **(c) Between-run variation and measurement.**
  - The floor is labelled a within-run production-and-measurement floor.
  - A between-series variant is in Table A2.
  - The unknown scan order is stated.
  - The measurement resolution is reported.
- **(e) Weighting and sides.** The weighting is described exactly, with the feasible failing-side counts, and Table 4 gives the false-accept distances.

*Open:*

- **(d) The new family.**
  - The text gives two rules in the produced family's floor.
  - Table 4, the abstract, Table 5 and the conclusions remain in the floor of the unproduced family.
  - A claim about the safest rule depends on that choice (S3).

**R3. Report the evaluation completely and make its comparisons fair: partly satisfied (largely met).**

*Met:*

- **(a)** The pooled scopes and M6 are in Table 4 and discussed.
- **(d) Fair baselines.**
  - The between-run noise floor raises the coverage of the Gaussian processes with a sibling from 71–72 % to 85–86 %.
  - M3 and M3n have jackknife+ intervals.
  - M1s is added.
- **(e)** The drawing-nominal baseline decides the wall angle at 2.0 floors, against 7.3 for M5.
- **(f) Refit bootstrap.**
  - It keeps every case in its relation.
  - The nearest produced setting is more decisive than M5 and M5n in every resample, both with a sibling and for a new setting; I confirm the shares of 1.00.

*Open:*

- **(b) and (c)** are reported in the body and in Tables 4 and 5, but not where 3.4 and 8.5 floors are quoted: in the abstract, Sections 5.4 and 6.1 and the conclusions (S4).
- M1s lacks its paired counterpart (S1).
- The jackknife+ guarantee and the design of the refit bootstrap are misdescribed (S5).

**R4. Specify and evaluate the procedure's decision rule, and work one decision through: partly satisfied.**

*Met:*

- **(a)** Step 6 compares the observable margin with a guard band.
- **(b)** The worked example takes one decision from the floor in millimetres to what production showed; Reviewers B and C reproduced it.
- The selection optimism is stated in Sections 4.5, 5.7 and 6.6.

*Open:*

- **(a)** The requirement prior that I asked you to state appears only as a range. Its influence is large, and the operating characteristics of the procedure are reported for the nearest produced setting only (S2).
- **(c)** The trial's own error is given for within-run reproducibility only (S5).

**R5. Make the contribution legible and reusable, in a shorter paper: partly satisfied.**

*Met:*

- **(a)** Section 2.2 positions the constructs. Section 6.4 separates the predictive-uncertainty part of a margin from change absorption; Reviewer A would go further, which I recommend.
- **(c)** The length and table targets are met, with a notation table, seven core rules and physical anchors.

*Open:*

- **(b)** The black-box formulation is a single sentence, the minimal report is not a checklist, and Table 6 is not marked as a proposal (S7).
- **(c)** The supplementary material was removed rather than replaced by citable references (S6), and the Results prose is denser than before (Section 5).

### 4. Required changes (the decision depends on these)

There are seven items, in priority order. Most are sentence-level corrections. The only new computations use the stored results:

- the force-trend rule (S1);
- the guard bands under other priors, and one compact table (S2);
- the new-family column in the produced family's floor, with its intervals (S3);
- consistent aggregates in Table 3 (S5).

#### S1. Withdraw the claim that a rescaled simulation adds information within a family
*(A-N1; supersedes B-N3(a) and C-C5(c); corrects my first-round R3d)*

**Why the paired counterpart is a line in force.** Within a geometry the nominal simulation depends only on the blank-holder force (p. 8, l. 324–327). M1s therefore fits a straight line through a function of force at three levels, or at two levels for a new setting. Section 4.4 requires every calibrated rule to be paired with a counterpart without the simulation (p. 12, l. 520–523). For M1s, that counterpart is the same least-squares line in force.

**What I computed.** I computed that line from `dec_alternatives.csv`, with the calibration sets of Section 4.4. My re-derivation of M1s agrees with the stored intervals to within 10⁻¹¹ floors. Decisive distances in floors:

| Relation | M1s, a + b·s₀ | a + b·force, without the simulation | NN | M1n |
|---|---|---|---|---|
| New variant (sibling produced) | 4.85 | 3.50 | 3.35 | 9.05 |
| New process setting | 19.15 | 8.15 | 8.45 | 10.3 |
| … interpolated (300 kN) | 19.25 | 4.65 (equal to NN by construction) | 4.65 | 4.8 |
| … extrapolated | 19.10 | 8.85 | 9.45 | 11.75 |

**The paired difference.** I held the fits fixed and resampled the held-out alternatives as in Section 4.4. M1s minus the force trend is then +0.7 to +3.1 floors for a new variant and +5.5 to +13.8 floors for a new setting, and the force trend is the more decisive in every resample. The 4.2-floor gain of M1s over M1n (Section 5.5) therefore comes from the force level, not from the simulation.

*What would satisfy it:*

- Add the force-trend rule to Table 2, and to the lower block of Table 4 (or a footnote) as M1s's paired counterpart, with its paired interval.
- Rewrite Section 5.5 (p. 15, l. 680–684), Section 6.1 (p. 20, l. 903–905) and Table 5 accordingly:
  - within this family the simulation added no information beyond the force level, whether added as an offset or rescaled;
  - across families it was decisive.
- Keep the statement in the abstract (l. 36–37) and the conclusions (l. 1036–1038), but make it explicit: "as used, as an offset or rescaled".
- Where the force trend becomes the best rule, report it without interpreting a difference of half a floor:
  - for a new setting, 8.2 against 8.5 floors;
  - for an extrapolated one, 8.9 against 9.5.

  Say whether the decomposition includes it.
- Correct the summary in your response that calls this "one exception".

#### S2. State the prior of the guard band, show its influence, and report the procedure's operating characteristics
*(A-N3, B-N1, B-N2, C-N6; my R4a)*

**Why the prior matters.** The guard band g is the smallest observable margin beyond which at least 95 % of the decided verdicts were correct. That is a posterior quantity, so it depends on how requirement distances are distributed.

**The prior as coded.** In `guard_band`:

- the 47 grid points within ±20 floors carry equal weight, and 41 of them (87 % of the weight) lie within ±10 floors;
- infeasible requirements are dropped;
- g is capped at 20 floors.

The manuscript states only the range of ±20 floors.

**The bands under other priors.** Recomputed with your code, guard bands in floors:

| Relation, rule | Your prior (grid within ±20) | Grid within ±5 | Grid within ±3 | Uniform within ±20 | Uniform within ±50 |
|---|---|---|---|---|---|
| Sibling, NN | 0.25 | 2.0 | 8.0 | 0 | 0 |
| Interpolated setting, NN | 2.0 | 4.25 | 5.0 | 0.25–0.5 | 0 |
| Extrapolated setting, NN | 7.0 | 14.25 | 14.75 | 3.5 | 0 |
| Extrapolated setting, M2 / M5 | none / none | none / none | none / none | 5.75–6.0 / 5.0 | 0 / 0 |
| New family, M2 / M5 | none / none | none / none | none / none | none / none | 3.75 / 11.75 |

- "None" means that no band up to your cap of 20 floors qualifies. Lifting the cap gives 23 floors for M2 and M5 in an extrapolated setting under your prior, and 27 and 32 floors for M2 and M5 in a new family under a uniform prior within ±20 floors.
- The ranges for the uniform priors reflect a grid step of 0.05–0.25 floors.

**What follows.**

- **Release-level requirements.** They lie a median 1.0–3.1 floors above the 95th percentile (Section 5.8). A team that sets such requirements faces the near-truth priors, under which the bands are several times those reported.
- **The worked example survives.** Its margin of 6.2 floors exceeds the 5.0 floors needed even under the narrowest prior.

*What would satisfy it:*

- **(a) The prior.** State it exactly in Section 3.6, the caption of Fig. 4 and Table A1, and say why it represents the requirements a team faces.
- **(b) Its influence.** Either route is acceptable:
  - report g under at least two further priors:
    - one concentrated near the truth, where release-level requirements lie (for example your grid within ±5 floors, or a prior built on the capability positions of Section 5.8);
    - one broader (uniform within ±20 or ±50 floors);
  - or define g without a prior and use the prior only for the trial rates. Reviewer B suggests one such definition: the smallest widening for which the widened rule's safe distance is zero.
- **(c) Its status.** Say in Section 3.6, Table 5 ("Deciding a single design") and Table A1 that g is derived for the distribution of requirement distances the team expects. It is not fixed by rule and relation alone.
- **(d) One compact table**, in the appendix if you wish.
  - *Rows:* the seven core rules and M3/M3n, by relation (sibling, interpolated, extrapolated, new family).
  - *Columns:* g; δ_d/δ_s under step 6; the trial share at 10 and 20 floors; and, for interval rules, the coverage, the median half-width and the decisive distance of the interval centre.

  Everything needed is in `panel_step6.csv` and `dec_coverage.csv`. Name the rules that never qualify under your prior:
  - in every relation: M0 and M0w;
  - with a sibling: also M1 and Mc;
  - for an interpolated setting: M1s;
  - for an extrapolated setting: M1, M1s, M2, M5 and Mc;
  - for a new family: every rule.

  Add a sentence on guard performance, so that the paper meets its own minimal report.
- **(e) The new family.** "Every design goes to trial" (p. 18, l. 812–813) is a consequence of the prior and the 20-floor cap; under a wide prior, M2 qualifies for gross margins. Present it as such. You may add that it agrees with die-tryout practice.
- **(f) Fig. 4.** Show interpolation and extrapolation separately, since their bands are set separately, and mark g. Say that the share is taken over verdicts whose margin is at least g.
- **(g) Worked example.** Say that the requirement was chosen for illustration, and that g was estimated on data that include this case.

#### S3. Report the new family in the floor that the procedure prescribes
*(A-N2, A-m13, B-N3(e), C-N3; my R2d)*

**The inconsistency.** Section 3.2 (p. 7, l. 290–292) and step 6 use the produced family's floor. Table 4, the abstract, Table 5 and the conclusions use the floor of the unproduced family, and the note to Table 4 does not say so.

**Both floors.** I recomputed the distances in both (δ_d/δ_s, in floors):

| Rule | Floor of the unproduced family (Table 4) | Floor of the produced family |
|---|---|---|
| M1 | 35/35 | 33/33 |
| M2 | 51/16 | 41/26 |
| M3 | 49/21 | 40/17 |
| M5 | 38/28 | 35/31 |
| Mc | 38/38 | 43/43 |

**What is robust and what is not.**

- The headline magnitude is robust: the best rule is safe at about 16–17 floors in either floor.
- Which rule is safest is not robust, and in neither floor is it resolved. I held the fits fixed and resampled the held-out alternatives and the reference. The safe distance of M3 minus that of M2 then lies:
  - between −3 and +8 floors in the floor of the unproduced family, with M3 the safer in 28 % of resamples;
  - between −16 and +7 floors in the floor of the produced family, with M3 the safer in 79 %.

*What would satisfy it:*

- Give the new-family column of Table 4 in the produced family's floor, or both floors side by side. Add safe-distance intervals for the headline rules and a decisive-distance interval for M2.
- State the unit wherever the 16 floors appear: the abstract (l. 33–34), Table 5 and the conclusions (l. 1034–1035).
- Replace "the envelope rule is the safest" (p. 14, l. 621; p. 19, l. 857; Table 5) by a statement such as "the best rule was safe at about 16–17 floors in either floor; which rule is safest is not resolved by two transfers". Do not replace it by "M3 is the safest".
- Add M3 at l. 622–624.

#### S4. Carry the strata and the force split into the abstract, the conclusions and the guidance, and label the findings correctly
*(C-C4, A-m12, B-N3(b)–(d), A-m7, C-N2, C-m12, A-m5, B-N7, A-m6, A-m3, B-N8, C-m1; my R3b and R3c)*

*What would satisfy it:*

- **3.4 floors.** Wherever it is quoted (abstract, l. 31–32; Section 5.4, l. 671–673; Section 6.1; conclusions, l. 1033), add how the nearest produced setting decides in the strata:
  - at 0.85 floors when neither sibling differs resolvably (58 of 126 cases);
  - at 4.9 floors when both do (34 cases).
- **8.5 floors.** Wherever it is quoted (abstract, l. 32–33; l. 672; conclusions, l. 1034), give the split:
  - 4.7 floors interpolated;
  - 9.5 floors extrapolated: 11 at 100 kN, where the stroke speed also changed, and 4.9 at 500 kN.

  In Section 6.6 (l. 1017–1019), write "the extrapolation to 100 kN".
- **Release-level requirements.**
  - Write "inside every decisive distance except that of a near-replicate sibling" (abstract, l. 35–36; l. 832; Table 5; conclusions).
  - Write "decided at the design stage only with a produced sibling" (l. 837–838).
  - State that the capability-anchored test is one-sided by construction: every alternative meets those limits. Present its shares as rates of right verdicts, false rejects and trials. A rule biased towards "meets" scores well there: at a performance index of 1.33, M1s is right in 79 % of new-setting cases and the nearest produced setting in 65 %.
  - Soften p. 6, l. 259–260: Section 5.8 locates release-level limits relative to the distances; it does not decide them.
- **Learning.**
  - Replace "learned models added abstention rather than accuracy" (abstract; conclusions) by a statement that names where the intervals held their level: 85–86 % with a sibling, 43–55 % for a new setting and at most 12 % for a new family.
  - Qualify "predicted as well as the nearest produced setting" (l. 905–906) by "with a produced sibling".
- **Labels.**
  - In Section 6.1 (l. 870–872), move "reaches its nominal level only where the calibration alternatives are exchangeable" to the observations, or restrict it to the guarantee of the distribution-free intervals.
  - In Table 5, label the prescriptive rows "framework (prescriptive; usefulness not evaluated)" rather than "definitions".
  - Present the "Fixing a requirement" row, and p. 20, l. 910–913, as a planning heuristic. It compares a predicted margin with δ_s, which is defined on the true margin, so the decision itself needs the guard band.
- **Terms.**
  - Use "with a produced sibling" for the sibling relation, and keep "within a family" for both within-family relations together.
  - Write "six to nine produced alternatives at two or three force levels" instead of "six to nine produced settings".

#### S5. Correct the description of three methods and three analyses
*(B-N5, B-N4, A-m4, C-N4, A-m2, C-N1, A-m15, C-C3, A-m8, B-N10)*

**Jackknife+** (p. 8, l. 335–336; Appendix, l. 1084–1086).

- *The problem.* With six or eight calibration alternatives, ⌈0.9(n+1)⌉ exceeds n, so the interval of Barber et al. is unbounded. `jackknife_plus` uses the extreme leave-one-out values instead. Under exchangeability, that guarantees at least 1 − 2/(n+1):

  | Calibration alternatives | Guaranteed coverage |
  |---|---|
  | six | 0.71 |
  | eight | 0.78 |
  | nine (a new family) | 0.80 |

  The median centring makes even these guarantees approximate.
- *What to do.* Describe the interval as a median-centred jackknife+ with extreme order statistics, give these guarantees, and quote the empirical coverage (96 % for M3 and 89 % for M3n with a sibling). This parallels the (n−1)/(n+1) correction of the first round.

**Refit bootstrap** (Section 4.4, l. 527–529; Section 5.9; note to Table A2; Appendix, l. 1087–1088). Describe what it does:

- *The configurations.* Drawing three lubrication patterns with replacement until at least two differ gives seven distinct outcomes per geometry, 49 in all. Your 200 resamples contain 48 of them. They contain the original design in both geometries 10 times, against 1/16 of the resamples in expectation.
- *The duplicated patterns.* In three draws of four per geometry, one pattern is duplicated and another is missing. Then:
  - a new-variant target keeps a single distinct sibling;
  - the calibration set has five distinct alternatives instead of eight;
  - the duplicated series enter the noise floor as zero-variance pairs.
- *What to say.*
  - "All 200 resamples" means all of 48 configurations.
  - The intervals show the effect of losing a pattern, not the sampling uncertainty around the reported values. Several point estimates sit at the edge of their own intervals: M1s at 4.9 floors [4.9–7.3], M2's safe distance at 0.15 [0.15–1.35], and M5's at 0.75 [0.75–2.96].
  - Either compute the noise floor over distinct series only, or say that it is not.

I do not require a new resampling design.

**Table 3** (p. 13, l. 553–564).

- *The cause.* σ_LT is the median of the per-series standard deviations, whereas σ_w and σ_b are pooled as root mean squares over series (`floor_protocol`).
  - Series by series, σ_w does not exceed σ_LT: in 120 of 126 alternative–characteristic cases it is smaller, and in the other six it is larger by at most 0.4 %, a degrees-of-freedom effect.
  - Pooled, it exceeds σ_LT in 10 of the 14 rows, because the scatter differs between series. For the concave cup depth, for example, the 100 kN series contribute 79 % of the within-batch variance.
- *What to do.* Use one aggregate for all three quantities, and say whether they are classical or trimmed.

Section 3.2 invites readers to recompute F from these components, so this is a correction, not a cosmetic change.

**Short calibration series** (p. 17, l. 776–779; p. 22, l. 985–987; note to Table A2). Only the calibration alternatives' q95 come from their first n parts; the truths and the floors are those of the full series. Write "calibrated", not "qualified". Alternatively, repeat the variant with truths from the same short series (optional).

**The trial's own error** (p. 9, l. 399–401; p. 13, l. 574–577). The trial that step 6 calls for is itself a run. The between-run component (1.2–9.8 floors) therefore applies to it, as well as the within-run reproducibility of 0.92–1.49 floors. One clause suffices.

**Surrogate** (p. 15, l. 687–690; p. 21, l. 937–938).

- "Within 1.8 floors" is a leave-one-out RMSE against the simulation, and the count of 12 of 14 includes the convex wall angle at 1.82.
- The surrogate's decision fitness was inferred, not computed.
- Either give one sentence of method and write "would be essentially that of the simulation", or score the surrogate as a rule.

#### S6. Make every number traceable and deposit the archive
*(A-m1, B-N2, C-N5; my first-round instructions)*

Many numbers in the text now rest only on result files that the manuscript does not name. Among them are:

- the lag profile and the in-line drift analysis (l. 549–571);
- the sibling strata (l. 628–632) and the force split (l. 634–635);
- the source-floor distances (l. 622–624);
- the guard bands and step-6 rates (l. 807–813);
- the capability shares (l. 830–838) and the cost results (l. 840–845);
- the surrogate accuracy (l. 687–689);
- the paired refit comparisons (l. 859–860).

The archive is "deposited on Zenodo [DOI pending]" (p. 25, l. 1135).

*What would satisfy it:*

- **The archive.** Deposit a versioned archive with a DOI, holding the code, the feature tables and the result files of the revised version. Cite it in the code and data availability statements and in the reference list.
  - Send the DOI with the revised manuscript: I shall check against it, and acceptance depends on it.
  - The GitHub link may stay as a convenience, but not as the reference of record.
- **Numbers that carry claims** go in the paper: the table of S2 and the new-family figures of S3.
- **A mapping table.** Add a short appendix table that maps every other number quoted in the text to its script and result file. Part 5 of your response, completed, is essentially that table. Electronic supplementary material is an acceptable alternative.
- **Result files.** Before depositing:
  - regenerate or remove `panel_physical_units.csv`, which evaluates distances on a grid of 0.05 units (about 18 floors of flange waviness);
  - make `alt_mrc.csv` match what your response says of it, or correct the response.

#### S7. Make the reuse section operational for other AI-based DFM tools
*(B-B7, B-p1, B-p2, A-m10, C-C7; my R5b and the fourth condition of fit)*

About half a page will do, rather than the two pages of my first letter: length matters more.

*What would satisfy it:*

- **Fixed-threshold classifiers.** They do not take the requirement as input, so the requirement cannot be swept case by case. Either:
  - estimate the operating characteristic by binning test cases by their true margin, which is not the exact estimator of Section 3.4; or
  - make the requirement an input.

  A probabilistic classifier needs two thresholds to return a trial.
- **Language-model checks.** Their verdicts may be non-monotone in the requirement and vary between queries.
  - Compute κ and ω on a requirement grid, with repeated queries.
  - Report the share of non-monotone verdict sequences, and the prompt and query protocol.
- **Continuous relations.** Say how strata are formed and how many cases each needs. With about 240 verdicts per relation, the 95 % threshold already rests on about a dozen.
- **Minimal report.** Give it as a numbered checklist. Add the source of the noise floor or replicate variance (B-N6) and, for language-model tools, the query protocol.
- **Table 6.**
  - Mark it as an untested proposal.
  - Say that distances in floors are comparable within a protocol, not across processes. Floors between builds, cavities or offset intervals are between-unit quantities, and here the between-series floor is 1.5–9.1 times the within-run one.
  - For injection moulding, take the floor within a cavity and treat cavity offsets as resolvable effects (C-C7).

### 5. Recommended, optional and editorial points

**Recommended.** These would strengthen the paper. Where time is short, a narrower wording is an acceptable alternative.

1. **Section 6.4** (A-A8).
   - State what the results imply for each strand, as Reviewer A illustrates for capability databases, preliminary information and set-based design.
   - Say in Section 2.2 how the evidence relation differs from the design type: the design type concerns the novelty of the solution, the evidence relation the novelty of its realisation relative to the produced evidence.
2. **Density** (A-A9, B, C).
   - Cut the numbers in Section 5.3 that repeat Table 4.
   - Split the sentences at l. 566–577, 807–813 and 838–845.
   - Add a two-line forward pointer to the worked example in Section 3.
3. **Cost comparison** (A-r4, B-p9, C-N7).
   - Rewrite l. 838–845 as a short list.
   - Say that the comparison inherits the coarseness of the ISO 2768-1 scenario: only 32 of its 108 decisions lie within 5 floors of the limit, and only six of those concern failing alternatives.
   - Name ties: with a sibling, M1s and the nearest setting tie at zero cost.
   - Alternatively, repeat the comparison on the requirement grid or on the capability-anchored requirements.
4. **Positioning of the floor** (C-C1, C-C2, A-r7, A-r11). This refines the wording my own first letter suggested.
   - The floor pools batch pairs up to 450 parts apart and grows with the lag. It is therefore closer to a time-different intermediate-precision limit (ISO 5725-3) of batch centres within a run than to a repeatability limit.
   - ISO 22514-2 would class the runs as a time-dependent model with varying location.
   - Restate assumption A2 as concerning within-run variation.
   - Add "and measurement" to the definition of the floor in the abstract.
   - Check the editions cited as ISO 5725-2:2025 and ISO 22514-2:2026, and cite those you consulted.
5. **Designer-study hypotheses** (A-m14, B-p4).
   - The questions at l. 941–945 are research questions; give one or two testable hypotheses with their measures.
   - Zhang et al. (2021) is now cited only in Section 2.4; discuss it where it bears on these hypotheses.
6. **Transparency** (B-N9, A-r10).
   - The nearest produced setting "points to the produced alternatives whose record it averages", not to one alternative that it copies.
   - Present the point as an argument, since a single example cannot show it.
7. **Noise floor of the Gaussian processes** (B-N6). Say:
   - that it is computed over the calibration alternatives only;
   - that it binds in 97–100 % of the fits outside the pooled scopes;
   - that the near-nominal coverage comes from the quasi-replicate series rather than from the learner;
   - that the hyperparameters are maximum-marginal-likelihood estimates without hyperpriors.
8. **Simulation statements** (C-C5(a), C-C5(b), C-C4).
   - Where the envelope is introduced, say that it varies sheet thickness and friction but not material properties.
   - Say in Section 6.3 that the force-effect ratio of 2.7–5.1 concerns the two draw-ins.
   - Note at l. 687 that, for the arm angle and the dome, whose nominal is zero in both families, "drawing nominal plus the produced family's deviation" is M1n. In Table 4's unit, M1n decides these two characteristics at 47 and 28 floors.
9. **Where the procedure sits** (C-C6(b), C-C6(c), C-C8).
   - Reword the placement at production part approval (l. 922–924), and say which evidence relation each source of evidence can support.
   - Once Table 3 is consistent, add one sentence on what sampled measurement does to the floor.
   - Consider Reviewer C's sharper practical statement: the rules decide reliably where a trial is cheapest, and none is reliable near release-level limits where a trial is dearest.
10. **Other points.**
    - Describe the multi-task statement as a restricted coregionalisation model (B-p5).
    - Cite one or two studies of how language-model or vision-language-model checks have been evaluated (B-p3), after checking them.
    - In the worked example, give the widened intervals of M2, M5 and M5n, say how typical the case is, and say why the mid-side draw-in was chosen (A-m9, C-m7).
    - In the note to Table A2, say that the between-series floor contains the lubrication effect and is close to circular for the sibling relation (C-m2).
    - Give a refit paired interval for M1s against the force trend, in place of the M1s–M1n interval requested in B-N4.

**Optional**, left to you:

- repeat the short-series variant with truths from the same short series (C-N1);
- an interval version of the scaled or force-trend rule (B-p10);
- fixed hyperparameters, or M5 from k = 3, in Fig. 3 (B-p6);
- one line of two-sided results for the wall angle (C-m11);
- a between-build floor from the PA12 anchors, or a reason why it is infeasible (A-r8);
- ask the dataset's authors about the scan order (C-C2);
- a capability decision on the index itself, or on a parametric high quantile with its own floor (C-N2).

**Editorial.**

- **M6.** The notes to Tables 2 and 4 say that M6 "appears only in the robustness analysis", but it has a row in Table 4. Write "thirteen rules and, as a robustness variant, M6" (abstract, l. 29; l. 307).
- **Abstract.** Write "was right for requirements more than 3.4 floors from the truth" (B-p7), and split the sentence at l. 24–27 (A-r13).
- **Wording.**
  - p. 2, l. 79–80: write "points on operating characteristics" (A-r1).
  - p. 9, l. 406–410: say that the factor that defines a sibling is the one varied at a fixed setting (A-r3).
  - Table 5, l. 878: write "relying on" (A-r9).
- **Sections 5.3–5.6.**
  - Section 5.5: name the relation of the paired differences. For a new setting, M1 decides 13.5 floors further out than M1n (A-m11).
  - Section 5.3, l. 612: name the interval rules meant (C-m10).
  - Section 5.6: write "M5" for "the Gaussian processes" (B-p6).
- **Precision of terms.**
  - l. 361: the distances are exact up to the 0.05-floor evaluation grid (C-m4).
  - Avoid "capability" for the 95th percentile (C-m5).
  - Use "measurement resolution" for the gauge sense, in Table A1 too (C-m6).
  - l. 550–552: the lag ranges are averages over the two geometries (C-m3).
- **References.** Give the place of publication of Montgomery (2019).

### 6. Where I overrule or qualify the reviewers, and what I checked

Where this letter and a report differ, follow this letter.

| Reviewer point | My decision | Reason and check |
|---|---|---|
| B-N3(a), C-C5(c): make the abstract and the conclusions say that the rescaled simulation helped within a family | Overruled in direction | Reviewer A's force-trend rule reproduces (S1), so the body is wrong, not the abstract. I also withdraw my own first-round sentence (R3d), which invited this reading. |
| A-N2, B-N3(e), C-N3: in the produced family's floor, M3 is the safest rule | Qualified | The point estimates reproduce (17 against 26 floors), but the paired difference is not resolved in either floor (S3). Report both floors, and name no safest rule. |
| C-C4: restate the within-family result as about 5 floors whenever the design differs resolvably, with the gradient coming from composition rather than novelty | Qualified | The stratified figures are required (S4); the causal reading is not. Each stratum has 34–42 cases, each distance is set by a handful of verdicts, and at 100 kN force and speed changed together. You may offer the reading as an observation. |
| A-A8 and my R5a: Section 6.4 must state what the results imply | Recommended, not required | Reviewers B and C find Section 6.4 adequate, Reviewer A does not make it a condition, and the fit to RED no longer depends on it. |
| B-B7 and my R5b: about two pages on reuse | Relaxed | Half a page of operational detail and a checklist (S7) meet the point without lengthening the paper. |
| B-N1: remove or justify the 20-floor cap; ask the team for its distribution of requirements; a prior-free band | Options | S2 sets the minimum; any of these routes is acceptable. |
| A-m1, B-N2, C-N5: supplementary material or an appendix table | Your choice | S6 sets the minimum; the single-file format remains acceptable. |
| C-N1: repeat the short-series variant with short-series truths | Optional | Narrowing the wording suffices. |
| B-N4: noise floor over distinct series; the all-subsets design as the measure of calibration-set variability | Describe; recomputation optional | The ranking these intervals support, the nearest produced setting more decisive than M5 and M5n, holds in all 48 configurations. |
| B-N4: refit paired interval for M1s against M1n | Superseded | After S1 the relevant pair is M1s against the force trend (recommended). |
| C-C1(ii): the floor is closer to an intermediate-precision limit than to a repeatability limit | Accepted as a recommendation | It refines the wording that my own first letter asked for. |

**What I checked.** All checks were read-only, with your code and result files; no part of the pipeline was rerun.

- **Reviewer A:**
  - the force-trend rule and its comparison with M1s (S1);
  - the same comparison in the sibling strata: with two resolvable siblings, the force trend reaches 4.45 floors, against 4.6 for M1s and 4.85 for the nearest setting;
  - the guard bands under the paper's grid restricted to ±5 and ±3 floors (S2);
  - the source-floor distances (S3);
  - the step-6 trial shares at 10 floors for an interpolated setting: 31 % for M2 and 40 % for M5;
  - in Table 3, the counts of 10 and 13 of 14 rows;
  - the intermediate sibling stratum (2.45 floors).
- **Reviewer B:**
  - the composition of the prior: 47 grid points, 41 of them within ±10 floors;
  - the guard bands under uniform priors, which reproduce with a uniform grid at 0.25-floor spacing;
  - the refit configurations, the duplication rate and the edge-of-interval examples;
  - the jackknife+ order statistics and guarantees;
  - the coverage figures: 96 % and 89 % for M3 and M3n with a sibling; 85–86 %, 43–55 % and at most 12 % for the Gaussian processes;
  - the noise bound, which binds in 97 % (M5) and 99 % (M5n) of the sibling fits and in every new-setting and new-family fit;
  - the range guard's refusals that would have been right: 96 % for the nearest setting, 72 % for M5;
  - the surrogate count;
  - that `rob_refit_paired.csv` has no M1s–M1n pair.
- **Reviewer C:**
  - the cause of the Table 3 inconsistency, which I traced by recomputing every series;
  - the one-sidedness of the capability test (every alternative is adequate) and the 79 % against 65 %;
  - the force-level split;
  - the tie of M1s and the nearest setting in `scen_cost_map.csv`;
  - the quantisation of `panel_physical_units.csv`;
  - that `alt_mrc.csv` still gives numbers such as 5,613 kN;
  - that the LaTeX source names no result file;
  - the lag ranges per geometry.
- **Your own figures.** These reproduce:
  - Table 4's new-family entries;
  - the decomposition;
  - the paired refit shares of 1.00;
  - the guard bands and step-6 figures of Section 5.7, including the worked example's guard band.

**Small inaccuracies in the reports.** None changes a request.

- **C-C4, smaller point.** "Nominal plus the produced family's deviation" is indeed M1n for the arm angle and the dome. But M1n's new-family decisive distances for these two characteristics are 47 and 28 floors, not about 130. The 130 floors pool all characteristics and are driven by the wall angle (129).
- **C-N4.** "For every alternative σ_w is below σ_LT" holds for 120 of 126 alternative–characteristic cases; in the other six σ_w exceeds σ_LT by at most 0.4 %. The diagnosis stands.
- **B-N1.** The uniform-prior bands depend slightly on the grid step. At 0.05 floors, for example:
  - the interpolated band of the nearest setting is 0.25 floors, not 0.5;
  - the extrapolated band of M2 is 6.0 floors, not 5.75.
- **B-N4.** The original design occurs with probability 1/16 in expectation; among your 200 resamples it occurs 10 times.

**Where the response said more than the manuscript.** Please correct these in the next response:

| The response says | The manuscript |
|---|---|
| results are "named by their result file" | names none |
| the requirement prior is "stated" | states only its range |
| the strata and the split are "in the abstract-level statements" | does not give them in the abstract or the conclusions |
| "concrete hypotheses" are given | gives research questions |
| Zhang et al. (2021) is "discussed in Sects. 6.2–6.3" | cites it in Section 2.4 only |
| `alt_mrc.csv` reports ">200" | the file gives numbers |
| `panel_physical_units.csv` gives the per-characteristic distances in units | the file is quantised at 0.05 units |
| the DOI will be deposited "at resubmission" | the DOI is pending |
| the M1s result is "one exception" | is not supported (S1) |

### 7. Practical instructions

- **Response document.**
  - Begin with a map of S1–S7, with page and line numbers in the new version.
  - Then answer every numbered point of the second-round reports:
    - Reviewer A: N1–N3, new minor points 1–15 and remaining points 1–13;
    - Reviewer B: N1–N10 and remaining points 1–10;
    - Reviewer C: the open points under C1–C8, N1–N8 and remaining points 1–12.
  - Quote each point, and state "changed (where)" or "not changed (why)". Where I have marked a point as recommended, optional, qualified or superseded, you may refer to this letter.
  - Add one paragraph that corrects the overstatements listed at the end of Section 6.
- **New numbers.** Name the script and the result file for each of them:
  - the force-trend rule and its paired interval;
  - the guard bands under other priors;
  - the table of S2;
  - the source-floor intervals;
  - the consistent Table 3.
- **Versions.** Upload a clean manuscript and a version marked up against the second-round manuscript.
- **Archive.** Deposit it with a DOI before you resubmit, and cite it. It should hold exactly the code and result files that produce the numbers of the new version.
- **Length.** The main text should not grow by more than about half a page; put new tables in the appendix. The whole paper may grow by a page or two.
- **Declaration on generative AI.** Keep it, and update it if the assistant's role changes.
- **Timeline.**
  - Please resubmit within four weeks, by 3 November 2026.
  - If you need longer, write to me by 20 October 2026. I can extend the deadline to 1 December 2026, which keeps the paper on the collection's schedule.
  - If time is short, do S1–S3 and S6 first.
- **Who sees the next version.**
  - I shall check it myself against the manuscript, your response and the archive; it will not go out for another round.
  - If a doubt remains on S1–S3, I shall ask Reviewer A, who has offered to look at them.
  - All three reviewers will receive this letter and, later, your response.
  - If S1–S7 are met, I expect to recommend acceptance.

I look forward to the revised manuscript.

Yours sincerely,

The handling guest editor
Special collection "AI in Design for Manufacturing", Research in Engineering Design

---

## Part 2: Confidential note to the Editor-in-Chief

**Recommendation: minor revision, to be checked by me without a further review round.** The three reviewers (design theory, AI in DFM, manufacturing) independently recommend minor revision, and I concur. The revision answers the first round in substance: claims conditioned on one simulator and a 3×3 factorial, the omitted pooled scopes reported, fair small-data baselines, a refit bootstrap that preserves the evidence relation, a specified step 6 with a worked example, design-literature positioning and a reuse section. The paper is eight pages shorter (30 pages, one file, no supplementary material), which I accept. What remains is specific and needs no new data. The one new conclusion that the response highlights, that a rescaled simulation adds information within a family, does not survive the comparison without the simulation. I verified Reviewer A's check; my own first-round letter had invited the claim, and I have said so in the letter. In addition, the new guard band depends on an unstated requirement prior, the new-family headline uses a unit that the procedure rules out, the abstract lags behind the body, and several method descriptions need correcting. I have no integrity concerns: every figure I re-checked reproduces from the released files. The response overstates in places (for example, it says that results are named by their result file, when the manuscript names none); I read this as compression and have asked for an exact response. The author's declaration of LLM assistance, which now also covers simulated peer review of earlier versions, is in line with Springer policy.

**Prospects and risks.** I expect the next version to be acceptable without a further round, and put the chance at about nine in ten. With the revision due on 3 November 2026, acceptance is possible in November or December 2026, within the collection's timeline. Three risks remain. *The archive:* the DOI I required at resubmission is still pending, and several numbers can at present be traced only through a mutable repository. I have made a DOI-archived deposit, cited in the paper, a condition of acceptance and asked for it with the revision. *The AI content* remains classical small-data regression. The paper's place in the collection rests on two things: its being an evaluation standard for AI-based DFM support, which it now says consistently; and a short operational extension to classifiers and language-model checks, which I have required. I no longer see a case for moving it to the regular stream. *Generality:* the evidence is one process, two geometries and two family transfers. That is acceptable for a methodology paper whose claims are bounded, as they now are. The reviewer load is light: no further round is planned, and Reviewer A has offered to check the three substantive points if I want a second opinion.
