# Editorial decision, third round

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design (Springer)
**Collection:** special collection "AI in Design for Manufacturing"
**Version considered:** the second revision (a single file of 30 pages, in the line-numbered copy the reviewers read), the version marked up against the second-round manuscript, the author's point-by-point response, and the archive metadata prepared for deposit (`.zenodo.json`, `CITATION.cff`)
**Reports considered:**
- third-round reports of Reviewer A (design theory and methodology), Reviewer B (AI in design for manufacturing) and Reviewer C (manufacturing process design and production quality), each a short check of the points in their remit and each recommending acceptance subject to minor corrections;
- for reference, the three second-round reports and my second-round decision of 6 October 2026.

**Date:** 6 October 2026

*Written by an AI agent in the persona of a fictional handling guest editor of a simulated review panel; it does not come from the journal or speak for any real person.*

---

## Part 1: Decision letter to the author

Dear Hüseyin Tayyer Canseven,

Thank you for the second revision, the marked-up version and a response that again takes up every point. As my last letter said I would, I have checked this version myself against the manuscript, your response and your released files. I worked read-only, with your own estimator (`exclusion`, `distance_pair`) and guard-band code (`guard_band`, `outcomes`). I also asked the three reviewers for a short check of the points in their remit; their reports are attached.

**Decision: accept in principle, subject to conditions C1–C7 in Section 3.**

The substance of my last letter is met, and every number behind it that the reviewers and I re-derived reproduces:

- **S1.** The force trend M1sn is in the paper as the paired counterpart of the scaled simulation. The claim that a rescaled simulation helps within a family is withdrawn throughout.
- **S2.** The guard band has an exactly stated prior and a stated conditional status. Its influence is shown under four further priors, and the procedure's operating characteristics are tabulated by rule and relation.
- **S3.** The new family is scored in the produced family's floor, both floors are reported with intervals, and no rule is named safest.
- **S7.** The reuse section is operational for classifiers and language-model checks, with a numbered minimal report.

S4 and S5 are largely met. Four things stand between this version and acceptance:

- **The archive has no DOI (S6).** My letter made acceptance depend on it and asked for it with this version. Your response says three times that the manuscript would not be resubmitted without it.
- **Step 6 is specified with the applicability guards but evaluated without them** (Reviewer B). Table A4 therefore does not describe the procedure that Section 3.6 states. The inconsistency was already in the last version, and I missed it.
- **Three headline sentences say more than the body (S4):**
  - the new-setting split credits one rule with another's figures;
  - the release-level statement has lost its performance index;
  - Section 6.4 quotes the pooled gradient without its strata.
- **Two method statements remain incomplete (S5):**
  - the short-series clauses claim that only the floor needs long runs, which was not tested;
  - the refit intervals of the safe distances that Section 5.9 cites are not in the paper.

None of this needs new data or new analysis, and the paper will not go out for another round. I shall check the final version myself. Once the DOI resolves to a deposit that holds this version's files and C1–C7 are met, I shall recommend acceptance to the Editor-in-Chief.

This applies the conditions of my last letter as I set them. C2 is the one new condition. It completes S2, and Section 3 says why.

### 1. Synthesis of the third-round reports and my own checks

**Where the reviewers agree.**

- **Their verdict.** All three recommend acceptance subject to minor corrections, and none needs to see the manuscript again.
- **Their checks.** Between them they re-derived from your files:
  - M1sn and its paired intervals, with the fits fixed and refitted; Reviewer A also re-ran the fixed-fit bootstrap with your code;
  - the new-family entries of Table 4 in both floors, with their intervals and the paired differences of M3 and M2;
  - every cell of Tables A3 and A4, and the guard bands under all five priors;
  - the decomposition, the sibling strata and the force levels;
  - the worked example, Table 3, the capability shares, the surrogate and the short-series bounds.

  They found no computational error.
- **The archive.** All three find the DOI missing and the response's statements about it inaccurate.
- **The ISO editions.** Reviewers A and C withdraw their second-round queries about ISO 5725-2:2025 and ISO 22514-2:2026.

**The remaining issues, and who raised them.**

| Issue | A | B | C | Here |
|---|---|---|---|---|
| No DOI; the availability statements say the files "are archived" | m1; Sect. 5 | S6; Sect. 5 | N5; S6 | C1 |
| Step 6 specified with guards but evaluated without them; the guard-performance sentence lacks its requirement distance | – | A, B | – | C2 |
| The new-setting split attached to the wrong rules | 4.1 | – (N3(b): "resolved") | C | C3 |
| The release-level statement without its index | 4.2 | – (N3(d): "resolved") | A | C4 |
| Section 6.4 quotes the pooled gradient | – | – | B | C5 |
| "Only the floor needs long runs" | 4.4 (m2: "resolved") | – | N1 | C6 |
| Refit intervals of the safe distances | – | C | – | C7 |
| The ±3-grid bands in Section 5.7 | 4.3 | – | – | recommended |
| Table A2 keeps the new family's own floor | r6; 4.4 | – | – | editorial |
| No licence for the deposit | – | – | S6, note | recommended |

*Notation.*

- A-4.1 is Section 4.1 of Reviewer A's report; A-m2 and A-r6 are A's new minor point 2 and remaining point 6.
- B-A, B-B and B-C are Reviewer B's new issues A to C; B-N3(b) is B's point N3(b).
- C-A, C-B and C-C are Reviewer C's new issues A to C; C-N1 is C's point N1; C-C2 and C-C6 are C's open points under the first-round comments C2 and C6.

**Where they differ.**

- **The new-setting split.** Reviewers A and C find it misattributed. Reviewer B checked the best rule at each force and calls it resolved. I agree with A and C (C3).
- **The release-level index.** Reviewers A and C ask for it back, and Reviewer B did not flag it. I agree with A and C (C4).
- **The short-series clause.** Reviewer C requires its removal. Reviewer A considers the point resolved and asks only for "within 1.5 floors" in Section 6.5. I agree with C (C6).
- **Step 6.** Only Reviewer B raised the guards; A and C rate S2 as met. B is right, and I make the correction a condition (C2).

**My own checks** (Section 5) reproduce every figure I re-derived, including every numerical claim of the three reports that bears on this decision. They add three observations.

1. **The guards.**
   - The second-round manuscript specified step 6 in the same words.
   - This revision deleted the one sentence that showed where the guards fire: "the range guard refuses exactly the extrapolated forces".
   - My own S2(e), which asked you to present the new-family trials as a consequence of the prior and the cap, presumed the unguarded procedure.
2. **The short series.**
   - The variant resets every held-out truth to its full-series value (`robustness.py`, item 16).
   - Section 6.5 replaced the second-round caveat "how many long runs a floor needs was not tested" with the claim "only the floor needed long runs".
3. **The response** is exact on almost every point I checked. Where it is not (Section 5), the statement that matters is the one about the DOI.

**Fit and format.**

- **Fit.** My assessment of the fit to RED and to the collection is unchanged. The paper presents itself throughout as a production-referenced evaluation standard for design-stage manufacturability decisions, AI-based or not.
- **Format.** The main text still ends on page 23 and the paper still has 30 pages. The new Tables A3–A5 are in the appendix, as I asked.

### 2. Status of the required changes S1–S7

| Item | Status | Open |
|---|---|---|
| S1 The rescaled simulation | met | – |
| S2 The guard band and the procedure's operating characteristics | met, subject to C2 | C2 |
| S3 The new family in the prescribed floor | met | editorial (Table A2) |
| S4 Strata, split and labels | largely met | C3, C4, C5 |
| S5 Methods and analyses | largely met | C6, C7 |
| S6 Traceability and archive | partly met; the DOI, on which acceptance depends, is missing | C1 |
| S7 Reuse for other AI-based DFM tools | met | – |

Page and line numbers below refer to the revised manuscript. The abstract and the tables are named.

#### S1. Withdraw the claim that a rescaled simulation adds information within a family: met

| What would satisfy it | Status | Evidence |
|---|---|---|
| The force trend in Table 2 and below the line in Table 4, with its paired interval | met | **Where.** Table 2 (p. 8, l. 343); Table 4 (p. 14, l. 618), whose note calls it "the counterpart of M1s without the simulation"; paired intervals in Sect. 5.5 (l. 699–701); refit pair in Sect. 5.9 (l. 857). **Check.** With the fits fixed, M1s − M1sn is +1.35 floors [0.65, 2.95] with a sibling and +11.0 [5.3, 13.8] for a new setting (`dec_paired.csv`). Refitted, it is +1.35 [1.35, 3.6] and +11.0 [8.8, 12.05] (`rob_refit_paired.csv`). M1s is never the more decisive. |
| Sections 5.5 and 6.1 and Table 5 rewritten | met | Sect. 5.5, l. 697–704; Sect. 6.1, l. 909–910; Sect. 6.3, l. 933–934. Table 5 no longer credits the simulation within a family. |
| The abstract and the conclusions made explicit: "as used, as an offset or rescaled" | met | Abstract; conclusions, l. 1052–1053. |
| The force trend reported without interpreting half a floor; whether the decomposition includes it | met | **Where.** Sect. 5.3, l. 590–591 (8.2 against 8.5 floors); Table 4 (8.9 against 9.5 extrapolated); Sect. 5.4, l. 680–684 (the decomposition). **Check.** The paired difference, −0.3 floors [−2.0, +2.55], need not be quoted. The decomposition reproduces (`panel_decomposition.csv`): relation and rule explain 66.5 and 6.2 % in the produced family's floor, 68.6 and 6.0 % in the new family's own, and 14.8 and 68.1 % within a family (14.7 and 71.2 % with M1sn). |
| The response's "one exception" corrected | met | Response, Part 3. |

#### S2. State the prior of the guard band, show its influence and report the procedure's operating characteristics: met, subject to C2

| What would satisfy it | Status | Evidence |
|---|---|---|
| (a) The prior stated exactly in Sect. 3.6, the caption of Fig. 4 and Table A1, and why it represents the requirements a team faces | met | **Where.** Sect. 3.6, p. 9, l. 408–411 (47 points, 87 % of the weight within ±10 floors, as coded); Fig. 4 caption; Table A1, row *g*. **Qualification.** The sentence at l. 411–412 says what the prior covers, not why a team faces it. Since (c) now makes the team's own distribution govern, I accept it, with a rewording (editorial point 3). |
| (b) g under a near-truth prior and a broader one | met | Sect. 5.7, l. 779–803, gives the grid within ±5 floors and uniform priors within ±20 and ±50 floors; the worked example gives the ±3 grid (l. 816). Every band reproduces (`panel_guard_priors.csv`). |
| (c) The conditional status of g in Sect. 3.6, Table 5 and Table A1 | met | l. 406–408; Table 5, "Deciding a single design"; Table A1. |
| (d) One compact table; the rules that never qualify; a sentence on guard performance | met in content; C2 | **Where.** Tables A3 and A4; the rules that never qualify at l. 776–778, exactly those my letter listed; the guard-performance sentence at l. 805–807. **Check.** Every cell of Table A4 reproduces (`panel_step6.csv`), and so does the guard sentence (`dec_guard.csv`). **Open.** That sentence omits its requirement distance, and Table A4 describes step 6 without the guards that Sect. 3.6 applies (C2). |
| (e) "Every design goes to trial" for a new family presented as a consequence of the prior and the cap | met as worded; C2 | **Where.** l. 801–804. Under a uniform prior within ±50 floors, M2, M3 and M5 qualify at 6.25, 6.5 and 15 floors. **Open.** Under step 6 as specified, the family guard sends every new-family design to trial whatever the prior (C2). |
| (f) Fig. 4: interpolation and extrapolation shown apart, g marked, and the share taken over verdicts with at least that margin | met | Fig. 4 has four panels and filled markers; caption, l. 797–799. Editorial point 1: name the new family's floor in the caption. |
| (g) Worked example: the requirement chosen for illustration; g estimated on data that include the case | met | **Where.** l. 810–811 and 820–821. **Check.** The example reproduces: the nearest setting predicts 14.99 mm, a margin of 6.2 floors; the truth lies 8.4 floors below the limit; the widened intervals of M2, M5 and M5n are as printed. |

#### S3. Report the new family in the floor that the procedure prescribes: met

| What would satisfy it | Status | Evidence |
|---|---|---|
| The new-family column of Table 4 in the produced family's floor, or both floors; safe-distance intervals for the headline rules and a decisive-distance interval for M2 | met | **Where.** Table 4 and its note (l. 624–625): M2 39–42/9.8–32, M3 36–45/15–19, M5 31–39/28–32. Both floors are in Sect. 5.3 (l. 629–636). **Check.** I re-derived the point estimates in both floors with `distance_pair`. In the produced family's floor: M1 32.9; M2 40.75/26.4; M3 40.15/17.1; M5 35.2/31.3; Mc 42.6. In the new family's own floor, the safe distances of M2, M3 and M5 are 15.8, 20.5 and 27.5. |
| The unit wherever the 16–17 floors appear | met | Abstract; Table 5; conclusions, l. 1049–1050; caption of Fig. 2. |
| "The envelope rule is the safest" replaced, without naming M3 instead | met | **Where.** Sect. 5.3, l. 633–636; Table 5 ("which rule not resolved"). The phrase no longer occurs in the source. **Check.** The safe distance of M3 minus that of M2 (`panel_source_floor_paired.csv`): −9.3 floors [−16.1, +6.9] in the produced family's floor, with M3 the smaller in 83 % of resamples; +4.7 [−3.4, +8.0] in the new family's own, 25 %. |
| M3 added | met | l. 630–631. |

*Residual (editorial point 5).* Table A2 keeps the new family in its own floor, as its note says. Its reference row (51/16, 38/28) therefore differs from Table 4 (41/26, 35/31), and Section 5.6's "by at most 4" is stated in that floor.

#### S4. Carry the strata and the force split into the abstract, the conclusions and the guidance, and label the findings correctly: largely met

| What would satisfy it | Status | Evidence |
|---|---|---|
| 3.4 floors with the strata (0.85 and 4.9) wherever quoted | met where my letter named; not in a new sentence (C5) | **Where.** Abstract; Sect. 5.4, l. 640–644; Sect. 6.1, l. 872–874; conclusions, l. 1045–1047; Table 5. **Check.** The strata reproduce: 0.85, 2.45 and 4.85 floors in 58, 34 and 34 cases. **Open.** Sect. 6.4 (l. 961–962) newly quotes "from about 3 to 8 and over 30 floors" without them. |
| The new-setting split wherever quoted; "the extrapolation to 100 kN" in Sect. 6.6 | partly met (C3) | **Where.** The split is in the abstract, Sect. 6.1 (l. 904–905), the conclusions (l. 1047–1048) and Table 5. Sect. 6.6 reads "The extrapolation to 100 kN" (l. 1030). **Open.** The split now mixes the force trend's figures with the nearest setting's. |
| Release-level requirements: "except a near-replicate's"; "only with a produced sibling"; the test declared one-sided, its shares as rates, 79 against 65 %; p. 6 softened | met in Sect. 5.8, Table 5 and Sect. 3.1; the abstract and the conclusions overstate (C4) | **Where.** Sect. 5.8, l. 826–835; Table 5; Sect. 3.1, l. 239. **Check.** The shares reproduce: 91/9/0, 65/35/0, 44/2/53, 32/16/52, 81/19/0 and 79/21/0 %, and at most 54 % for a new family. **Open.** The abstract and the conclusions (l. 1050–1051) have dropped "at a performance index of 1.33". |
| Learning: where the intervals held their level; "with a produced sibling" | met | Abstract and conclusions (l. 1053–1055): 85–96 % with a sibling, under 50 % extrapolating or for a new family, as Table A3 shows. Sect. 6.1, l. 910–911. See editorial point 6. |
| Labels: the exchangeability clause; the prescriptive rows of Table 5; the planning heuristic | met | Sect. 6.1, l. 869–871. Table 5: "From the framework (prescriptive; usefulness not evaluated)" and "Planning a requirement". Sect. 6.2, l. 915–919. |
| Terms: "with a produced sibling"; "within a family" for both within-family relations; "six to nine produced alternatives at two or three force levels" | met | For example l. 683, 761, 852, 905 and 1050; the abstract; l. 908 and 942–943. |

#### S5. Correct the description of three methods and three analyses: largely met

| What would satisfy it | Status | Evidence |
|---|---|---|
| Jackknife+: median-centred, with extreme order statistics; guarantees of 0.71–0.80; the empirical coverage | met | Sect. 3.3, l. 312–316; appendix, l. 1080–1083; Sect. 5.5, l. 718–720 (96 % and 89 % against 7/9). This matches `jackknife_plus`. |
| Refit bootstrap: 48 of 49 configurations; the duplicated patterns; what the intervals show; the estimates at the edge of their intervals; the noise floor | met in description; C7 | **Where.** Sect. 4.4, l. 507–513; Sect. 5.9, l. 855–859; appendix, l. 1084–1085. **Open.** Sect. 5.9 says that the safe distances of M2 and M5 lie at the edge of their refit intervals, but those intervals are only in `rob_refit.csv`: 0.15 [0.15, 1.35] and 0.75 [0.75, 2.96] floors with a sibling. Table A2 gives refit intervals of decisive distances only. |
| Table 3: one aggregate, classical or trimmed | met | **Where.** Note to Table 3. **Check** (`panel_floor_protocol.csv`): σ_w is below σ_LT in all 14 rows; series by series it exceeds σ_LT in 5 of 126 cases, by at most 0.27 %; √(σ_b² + σ_w²) is within 2 % of σ_LT; the normal model is within 12 % of the floors. |
| Short series: "calibrated", not "qualified"; the truths and floors are those of the full series | partly met (C6) | **Where.** "Calibrated" and "here scored against the truths and floors of the full series" (Sect. 5.6, l. 762–763; note to Table A2). **Open.** The same sentence ends "and only the floor needs a run long enough to show the drift". Sect. 6.5 (l. 990–991) now reads "scored as well as with full series, and only the floor needed long runs". |
| The trial's own error | met | Sect. 3.4, l. 377–380; Sect. 5.1, l. 549–551. |
| The surrogate | met | Sect. 5.5, l. 707–711 scores it as a rule: 108.65 against 108.35 floors as M0, and 15.05 against 15.2 as M1 with a sibling. 12 of the 14 leave-one-out errors lie below 2 floors. |

#### S6. Make every number traceable and deposit the archive: partly met

| What would satisfy it | Status | Evidence |
|---|---|---|
| A versioned archive with a DOI, cited in the availability statements and the reference list; the DOI sent with the revision; GitHub as a convenience only | not met (C1) | **The DOI.** The reference list (p. 28, l. 1267–1268) reads "Zenodo, version 3, [DOI pending]", and `refs.bib` holds the placeholder. `.zenodo.json` is prepared for version 3, without a DOI. **The statements.** The availability statements (p. 24, l. 1098–1104; p. 25, l. 1130–1132) say that the files "are archived", which is not yet true. **GitHub.** It is called a working copy (met). |
| The numbers that carry claims in the paper | met | Tables A3 and A4; Table 4 and Sect. 5.3. |
| A mapping table | met | Table A5 (p. 27) names 47 result files, all present. The numbers I sampled trace through it. |
| The result files corrected | met | `panel_physical_units.csv` is exact to 0.05 pooled floors; the flange waviness with a sibling is 0.0032 mm. The response's statement on `alt_mrc.csv` is withdrawn (Part 3). |

#### S7. Make the reuse section operational for other AI-based DFM tools: met

| What would satisfy it | Status | Evidence |
|---|---|---|
| Fixed-threshold and probabilistic classifiers | met | Sect. 6.5, l. 993–997. |
| Language-model checks | met | l. 997–1000; checklist item 6. |
| Continuous relations | met | l. 1000–1003. |
| The minimal report as a numbered checklist, with the source of the noise variance and the query protocol | met | l. 1004–1010. The paper meets its own checklist except items 2 and 5, which C7 and C2 complete. |
| Table 6 marked as an untested proposal; floors comparable within a protocol; a floor per cavity | met | Caption of Table 6; l. 1013–1016. |

### 3. Conditions of acceptance and further corrections

**Conditions.** I shall check each of them in the final version.

#### C1. Deposit the archive and cite its DOI
*(S6; A-m1, B-S6, C-N5)*

*What would satisfy it:*

- **The deposit.** Deposit the code, the feature tables and every result file named in Table A5, as they produce the numbers of the final version. If a result file changes, for example under route 2 of C2, deposit the version that holds the changed file.
- **The DOI.** Mint its DOI. Zenodo can reserve one before the record is published, as Reviewer B notes.
- **The citation.** Cite it in `canseven2026archive`, so that Section 4.5, the appendix and both availability statements cite a resolving DOI. The GitHub link may stay as the working copy.
- **My check.** Send me the DOI with the final version. I shall check that it resolves and that the deposited files are identical to those I re-derived numbers from, at least:
  - `dec_intervals.csv` and `dec_q95_reps.npy`;
  - `dec_resolution.csv`;
  - `panel_source_floor.csv`;
  - `panel_guard_priors.csv` and `panel_step6.csv`;
  - `rob_refit.csv`.

  Checksums in the release notes would make that quick.
- **Until then.** The availability statements must not say that the files "are archived". As my last letter said, acceptance depends on the deposit.

#### C2. Specify which applicability guards step 6 applies
*(B-A, B-B; completes S2(d) and S2(e))*

*The problem.*

- **The specification.** Section 3.6 (p. 10, l. 434–437), the step-6 box of Fig. 1 and Table 5 ("Deciding a single design") apply the family, range and novelty guards.
- **The evaluation.** `step6` in `panel.py` widens each interval by g and applies no guard. Table A4, Fig. 4 and Section 5.7 therefore describe step 6 without guards.
- **Where the guards fire** (`dec_guard.csv`):
  - the range guard, in all 84 extrapolated and all 126 new-family cases;
  - the family guard, in all 126 new-family cases;
  - the novelty guard, in 18 of the 42 interpolated cases. These hold 35 of the nearest setting's 80 interpolated verdicts at 10 floors, all of them right.
- **The consequence.** A reader who implements Section 3.6 as written:
  - sends every extrapolated and every new-family design to trial, whatever g and whatever the prior;
  - sends 44 % of the nearest setting's interpolated verdicts to trial, where Table A4 shows 0 %.

*Why it is a condition.*

- S2 asked for the operating characteristics of the procedure, and they must describe the procedure that the paper specifies.
- The sentence I required under S2(e) is true only of the unguarded procedure. I should have seen this in the second round.

*What would satisfy it.* Either route is acceptable.

- **Route 1, which I prefer: no new numbers.**
  - Say in Section 3.6, in Fig. 1 and in Table 5 that the guard band qualified for the relation takes the place of the range and family guards, which in this design coincide with the extrapolated and new-family relations.
  - Say that the novelty guard is reported as a diagnostic, not applied, since most of its refusals would have been right.
  - Add "no applicability guard is applied" to the note to Table A4.
- **Route 2: keep the guards in step 6.** Then:
  - Table A4 and l. 775–776 and 801–804 must report that every extrapolated and every new-family design goes to trial, whatever the prior;
  - the interpolated trial shares must include the novelty guard's refusals;
  - the new-family statement must attribute the trials to the family guard.

  I would check the new numbers against the files.
- **On either route,** amend the guard-performance sentence (l. 805–807):
  - add "at requirements 10 floors from the truth" (`D_CHECK` in `guard.py`);
  - say that the range guard refuses exactly the extrapolated designs (84 of the 126 new-setting cases).

#### C3. Attribute the new-setting split to its rules
*(A-4.1, C-C; S4)*

*The problem.* Decisive distances in floors (`panel_force_levels.csv`; `dec_resolution.csv` for the pooled column):

| Rule | Interpolated (300 kN) | Extrapolated to 500 kN | Extrapolated to 100 kN | Pooled |
|---|---|---|---|---|
| Force trend (M1sn) | 4.65 | 8.85 | 8.85 | 8.15 |
| Nearest setting (NN) | 4.65 | 4.85 | 11.0 | 8.45 |

- **Sections 6.1 and 7.** Section 6.1 (l. 904–905) and the conclusions (l. 1047–1048) put "4.7 interpolated; 4.9 and 8.9 extrapolated" after the force trend's 8.2 floors. There the parenthesis reads as that rule's decomposition, yet no single rule decided at 4.9 and 8.9.
- **Table 5.** It credits all three figures to "nearest setting or force trend". A planner who uses the nearest setting at 100 kN would read 8.9 floors where that rule needs 11.

*What would satisfy it.*

- **Sections 6.1 and 7.** Attribute each figure to its rule, for example: "8.2 for a new setting (the force trend; the nearest setting 8.5); by stratum, the nearest setting needed 4.7 interpolated and 4.9 extrapolated to 500 kN, and the force trend 8.9 to 100 kN, where the nearest setting needed 11".
- **Table 5.** Either name the rule of each figure, or write "the better of the nearest setting and the force trend" and add the nearest setting's 11 floors at 100 kN.
- **The abstract.** I recommend naming the rules there as well, because the best rule for each stratum is chosen after the results.

#### C4. Restore the index of the release-level statement
*(A-4.2, C-A; S4)*

*The problem.*

- **The statement.** The abstract and the conclusions (l. 1050–1051) say that release-level requirements lay inside every decisive distance except a near-replicate's.
- **Section 5.8** (l. 826–828) restricts this, rightly, to indices up to 1.33:
  - at indices of 1.67 and 2.0, the limits lie a median 2.46 and 3.14 floors above the 95th percentile (`panel_capability.csv`);
  - with one resolvable sibling, the nearest setting decides at 2.45 floors (34 cases; `panel_sibling_strata.csv`).
- **The definition.** Section 3.1 defines release criteria as an index of 1.33 or more, and the second-round abstract carried the qualifier.

*What would satisfy it.* In the abstract and the conclusions, write "Requirements at a performance index of 1.33 lay inside every decisive distance except a near-replicate's", as Table 5 does.

#### C5. Label the pooled gradient in Section 6.4
*(C-B; S4)*

*What would satisfy it.* At l. 961–962, write "The growth of the decisive distance, pooled over strata, from about 3 to 8 and over 30 floors …", or give the strata. S4 asked for the strata wherever the pooled figures are quoted, and here they carry a design implication.

#### C6. Withdraw the untested short-series claim
*(C-N1, A-4.4; S5)*

*The problem.*

- **What the variant does.** It takes only the calibration alternatives' q95 from the first n parts. Every held-out truth and every floor is that of the 500-part series.
- **What it shows.** It shows that rules can be calibrated on short runs. It does not show that only the floor needs long runs, because qualifying a rule needs truths.
- **Why truths from short runs matter.** By your own figure, the 95th percentiles of two 100-part batches differ by 0.92–1.49 floors, more than the near-replicate distance.
- **Where the claim sits.** Section 6.5 is the paragraph a team reads before it plans its runs.

*What would satisfy it:*

- **Section 5.6 (l. 762–763).** Delete "and only the floor needs a run long enough to show the drift". Alternatively, write instead: "the floors and the held-out truths came from the full 500-part series; whether truths from short runs suffice to qualify the rules was not tested".
- **Section 6.5 (l. 990–991).** Write "here rules calibrated on about 50 parts per variant scored within 1.5 floors of those calibrated on full series, against truths and floors from the full series", and drop "only the floor needed long runs".

#### C7. Give the refit intervals of the safe distances
*(B-C; S5 and checklist item 2)*

*What would satisfy it.* Either is acceptable:

- give the refit row of Table A2 as δd/δs, from `rob_refit.csv`;
- or quote the two intervals in Section 5.9 (l. 857–859): with a sibling, M2 at 0.15 [0.15, 1.35] floors and M5 at 0.75 [0.75, 2.96].

No computation is needed. This completes the S5 bullet that named these intervals.

**Editorial corrections.** Please make these too. I shall look at them, but they do not hold up acceptance.

1. **Fig. 4 caption.** Add "a new family in the produced family's floor", as in the caption of Fig. 2 and the note to Table A3 (A-4.4).
2. **Section 3.6, l. 408.** Write "the requirement grid", not "the evaluation grid", which invites confusion with the 0.05-floor grid of l. 369 (A-4.4).
3. **Section 3.6, l. 411–412.** Present the reference prior as a reference that a team replaces by its own distribution of requirement distances. At present it is said to "represent" the requirements a team faces (Reviewer A, Sect. 5, item 2; Reviewer B, S2(a)).
4. **Section 5.4, l. 674–676.** Write "at up to about 5 floors": with one resolvable sibling the nearest setting decided at 2.5 floors (A-4.4).
5. **Note to Table A2.** Point to Table 4 for the new family in the produced family's floor, and say in Section 5.6 that "by at most 4" is in the new family's own floor (A-r6).
6. **Section 6.1, l. 910–911.** Write "M5, M5n and M3n predicted as well as the nearest produced setting": M3's interval centre decides at 9.9 floors with a sibling (B-N7).
7. **Section 5.1, l. 540–541.** Write "measurement resolution" (Reviewer C, remaining point 6).
8. **Introduction, l. 72.** Write "drift and scatter of production and measurement", as in the abstract (C-C2).

**Recommended.**

1. **The near-truth prior** (A-4.3). Add the ±3-grid bands to Section 5.7, l. 779–782: "(under the grid within ±3 floors, 8.0, 5.0 and 14.75)".
   - Between the two near-truth priors, the sibling band of the nearest setting moves by a factor of four.
   - With a band of 8.0 floors, step 6 sends 99 % of sibling cases to trial at the median release-level position.
   - This strengthens your own conclusion that release-level requirements need trials.
2. **A licence for the deposit** (Reviewer C).
   - Neither `.zenodo.json` nor `CITATION.cff` names one, and the repository has no licence file.
   - The derived feature tables redistribute material from datasets under CC BY 4.0, which requires attribution and a licence notice; the metadata already name the sources.
   - A code licence makes the archive reusable as well as citable.

   I do not make acceptance depend on which licence you choose.
3. **`CITATION.cff`.** Add the DOI once it is minted.

**Optional**, left to you:

- one clause on why g is capped at 20 floors (B-N1);
- the interpolated coverage in the conclusions (B-N3(c));
- in Table 4, intervals for two figures that now head the results (A-m13):
  - the force trend's 8.2 floors for a new setting [6.7, 9.0];
  - the bias correction's 33 floors for a new family [30.7, 36.1];
- the sampling protocol of a production part approval study as the protocol of the floor it supplies (C-C6(b));
- the 1.67 acceptance criterion in Section 3.1 (C-A);
- that the cost ranking for a new setting rests on three verdicts: the nearest setting makes three false rejects among 108 decisions, the force trend none (C-N7).

### 4. Where I overrule or qualify the reviewers

Where this letter and a report differ, follow this letter.

| Reviewer point | My decision | Reason and check |
|---|---|---|
| B-N3(b): the force split is resolved | Overruled; A-4.1 and C-C upheld (C3) | In `panel_force_levels.csv` the best rule at each force is as Reviewer B says. But Sect. 6.1 and the conclusions attach the split to the force trend's pooled figure, and Table 5 credits both rules with every figure. |
| A-4.1: name the rules, "as Table 5 already does" | Qualified | Table 5 names both rules but credits each figure to both. It needs the same correction (C-C). |
| B-N3(d): the release-level statement is resolved | Qualified; A-4.2 and C-A upheld (C4) | It is resolved in Sect. 5.8 and Table 5, but the abstract and the conclusions have dropped the index. |
| A-m2: the short-series point is resolved | Overruled; C-N1 upheld (C6) | `robustness.py` resets every truth to its full-series value, and Sect. 6.5 replaced the second-round caveat with a stronger claim. A's own editorial point on Sect. 6.5 points the same way. |
| A and C: S2 is met | Qualified by B-A (C2) | I verified B-A in the code and in `dec_guard.csv`. My own S2(e) presumed the unguarded procedure. |
| B-C: refit intervals of the safe distances | Accepted as a condition (C7) | A table edit that completes my S5 bullet and the paper's own checklist. |
| C-B: the pooled gradient in Sect. 6.4 | Accepted as a condition (C5) | S4 asked for the strata wherever the pooled figures are quoted. Reviewer A judged Sect. 6.4 on its argument strand by strand, which I agree is now adequate. |
| A-4.3: the ±3-grid bands | Recommended, not required, as Reviewer A proposes | The ±5 grid was one of the near-truth priors my letter named, so S2(b) is met. |
| Reviewer C: a licence for the deposit | Recommended | It was not among my conditions, but it serves the reuse the archive is for. |
| A-4.4, A-r6, B-N7, C's remaining point 6, C-C2 | Editorial | See the editorial corrections in Section 3. |
| B-N1 (the cap), B-N3(c), A-m13, C-C6(b), C-A (the 1.67 criterion), C-N7 | Optional | They would sharpen the paper, but no claim rests on them. |

**Small inaccuracies in the reports.**

- **Numbers.** None. Every numerical claim of the three reports that I re-derived reproduces.
- **A misquotation (B-N3(c)).** Reviewer B quotes the abstract's coverage clause as "or for a new family". The abstract says "or across families"; the conclusions say "for a new family". This changes nothing.
- **Judgements.** The judgements I overrule or qualify are in the table above.

### 5. What I checked

All checks were read-only.

- **Files.** I used `results/*.csv`, and your functions (`exclusion`, `distance_pair`, `guard_band`, `outcomes`, `in_produced_floor`) applied to `dec_intervals.csv`.
- **Method.** Python ran without writing bytecode, and no part of the pipeline was rerun.

**By item.**

- **S1:**
  - M1sn's distances by relation and by force level;
  - the fixed-fit and refit pairs of M1s and M1sn;
  - the pair of M1sn and the nearest setting: −0.3 floors [−2.0, +2.55];
  - the decomposition in both floors, with and without M1sn.
- **S2:**
  - the guard bands of the nearest setting, M2, M3, M5, M5n and M1sn under all five priors, capped and uncapped, which include every band quoted in Sect. 5.7 and the worked example;
  - every cell of Table A4;
  - the new-family bands under the uniform prior within ±50 floors in the new family's own floor: M2 3.75, M5 11.75. This confirms your explanation of the bands in my last letter;
  - the worked example;
  - where the guards fire and their false alarms (`dec_guard.csv`, at |d| = 10 floors);
  - the code of `step6` and `guard.py`;
  - the step-6 wording of the second-round manuscript, and the sentence deleted in the marked-up version.
- **S3:**
  - the new-family distances in both floors, re-derived with `distance_pair` and compared with `panel_source_floor.csv`;
  - their intervals and the paired differences of M3 and M2;
  - that "the envelope rule is the safest" no longer occurs.
- **S4:**
  - the force levels;
  - the sibling strata and their case counts;
  - the capability positions and the shares at an index of 1.33;
  - the coverage by relation (Table A3);
  - every use of "within a family";
  - the release-level wording of the second-round abstract.
- **S5:**
  - the order statistics of `jackknife_plus`;
  - the refit intervals (`rob_refit.csv`);
  - Table 3 against `panel_floor_protocol.csv`;
  - the short-series variant in `robustness.py`, and its bounds of 1.5 floors within a family and 4.0 for a new family (`rob_decisions.csv`);
  - the surrogate.
- **S6:**
  - no DOI in `main.tex`, `refs.bib` or `.zenodo.json`;
  - the 47 result files named in Table A5, all present;
  - the regenerated `panel_physical_units.csv`;
  - no licence in the metadata or the repository.

**Section 5.9 and other sections.**

- **Section 5.9:**
  - punch-temperature adjustment changes no calibrated distance by more than 2.55 floors;
  - the GP specifications move the decisive distances by at most 1.2 floors and the safe distances by at most 2.1;
  - in every variant, the most decisive rule within a family is the nearest setting or the force trend, tied once with a sibling.
- **The cost map:** the three-way tie at zero cost with a sibling; the force trend at every trial cost for a new setting; for a new family, trials up to a tenth of the cost of a false accept, then M2, then M5.
- **The drawing-nominal baseline:** 1.90 against 7.45 floors.
- **M1n for the arm angle and the dome:** 44.05 and 26.80 floors in the produced family's floor, 46.70 and 28.15 in the new family's own.
- **The cup-depth offset:** removing it takes the nominal simulation from 108 to 65 floors.
- **The noise bound:** it binds in 96.8 % and 99.2 % of the fits with a sibling, in 100 % for a new setting and a new family, and in 84–93 % in the pooled scopes.
- **The new family's reliability:** at most 79 % correct among decided verdicts.

**The reviewers' figures.**

- Reviewer A's ±3-grid bands, and the trial shares of 6, 54 and 99 % at the median release-level position.
- Reviewer B's uncapped trial rates: 96.9–100 % at 10 floors and 82–99 % at 20.
- Reviewer C's checks of Table 3 and of the Section 5.8 shares.

**Not checked by me.**

- The Crossref records, which Reviewer B checked, and the ISO editions, which Reviewers A and C checked. I accept their checks.
- I did not re-run the paired bootstrap. The stored shares show that M1s is never the more decisive.

**The response against the manuscript.** Most of what the response says matches the manuscript and the files. This includes the map in Part 1, which I sampled, and the provenance table in Part 7. The statements below do not; please correct them in the final response.

| The response says | The manuscript and the files |
|---|---|
| The DOI is minted "before resubmission", and "The manuscript will not be resubmitted without it" (preamble; Part 1, S6; Part 3; Part 8) | It cites "[DOI pending]"; no DOI exists. |
| "The text says why the prior represents the requirements a team faces" (Part 1, S2(a)) | It says what the prior covers (l. 411–412). |
| The truths and floors are those of the full series "(Sect. 5.6, Sect. 6.5, note to Table A2)" (Part 1, S5) | Sect. 6.5 does not say so; it says that "only the floor needed long runs". |
| The narrowed short-series sentences (Part 4, A-m2; Part 6, C-N1) | They are quoted without their final clauses, and the deletion of the second-round caveat is not mentioned. |
| "Wherever it is quoted as a headline, the nearest setting's strata are given" (Part 1, S4) | They are given everywhere except in the new sentence of Sect. 6.4 (C5). |
| The measurement resolution, 0.38 floors, is small against the example's margin (Part 6, C-m7) | The manuscript has no such sentence (immaterial). |
| The uncapped bands send "94–100 %" of the verdicts at 10 floors to trial (Part 5, B-N1) | 96.9–100 % (immaterial; the paper does not quote it). |

### 6. Next steps

- **Final version.** Please upload:
  - a clean manuscript;
  - a version marked up against this one;
  - a short response that maps C1–C7 and the editorial corrections to page and line, gives the DOI, and corrects the statements listed in Section 5.
- **Timeline.** Please send it within two weeks, by 20 October 2026. If you need longer, tell me. 3 November 2026, the deadline my last letter set, still keeps the paper on the collection's schedule.
- **Who sees it.** I shall check it myself against this letter, the manuscript and the archive; it will not go to the reviewers again. All three reviewers will receive this letter.
- **Then.** When C1–C7 are met, I shall recommend acceptance to the Editor-in-Chief. For production, remove the `lineno` option.

Yours sincerely,

The handling guest editor
Special collection "AI in Design for Manufacturing", Research in Engineering Design

---

## Part 2: Confidential note to the Editor-in-Chief

**Recommendation: accept in principle, subject to conditions that I shall check myself, without a further review round.** All three reviewers (design theory, AI in DFM, manufacturing) recommend acceptance subject to minor corrections, and I concur in substance. The three substantive requirements of my second-round letter are met:

- the claim that a rescaled simulation adds information within a family is withdrawn, against a paired force-trend baseline;
- the guard band of the procedure has a stated prior, a sensitivity analysis and a table of operating characteristics;
- the new-family results are reported in the unit a team would have, without a ranking that two transfers cannot support.

Every figure that the reviewers and I re-derived from the released files reproduces, and I have no integrity concern. What remains is short:

- **The archive DOI.** I made it a condition of acceptance, and the author said three times that it would accompany this version; it is still pending.
- **The guards.** Reviewer B found that the single-decision step is specified with applicability guards but evaluated without them. The inconsistency predates this revision, and I missed it in the second round.
- **Wording.** Five small corrections (C3–C7) bring the abstract, the conclusions, Table 5 and two method statements into line with the body.

None needs new analysis. The author's declaration of LLM assistance covers code, analysis, drafting and the simulated peer review of earlier versions, and is in line with Springer policy.

**Risks.** The archive is the main one. The DOI has now slipped twice, first promised "at resubmission" and then "before resubmission", and until it exists several numbers can be traced only through a mutable repository. I shall not recommend final acceptance until the DOI resolves and the deposit's result files match those I checked. The other risks are those I reported before, and the paper now states them:

- the evidence is one process, two geometries and two family transfers;
- some rules were chosen after earlier results had been seen, which the paper declares as selection optimism;
- the AI content is classical small-data regression, so the paper's place in the collection is as an evaluation standard, not as a new AI method.

The final version is due on 20 October 2026, so acceptance is possible in late October, within the collection's timeline. I put the chance that it meets every condition at about nine in ten. No further reviewer time is needed.
