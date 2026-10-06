# Referee report, second round: Reviewer A

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design (Springer), special collection "AI in Design for Manufacturing"
**Round:** second (revised version)
**Reviewer focus:** design decision-making under uncertainty, design margins, verification and validation planning, evaluation of design support

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The revision is extensive and, on the whole, responds to my first-round report and to the editor's required revisions R1–R5.

What has improved:
- The general claims are quantified and labelled as hypotheses.
- The headline on the evidence relation is replaced by the best attainable distance per relation and a decomposition. I reproduced both from the released intervals, as I did Table 4.
- The floor is positioned as a repeatability-type limit with a reference protocol.
- The pooled scopes, the sibling strata and the force-level split are reported.
- Step 6 is specified as a guard band on the observable margin.
- A worked example, a design-literature positioning, a reuse section and a notation table have been added, while the paper has shrunk from 38 to 30 pages (main text ending on p. 23).

Three substantive problems remain or are new:
- The rescaled-simulation "exception" to RQ3 does not survive the paired no-simulation counterpart that the paper's own evaluation design calls for.
- The step-6 guard band depends strongly on a requirement prior that the paper does not state, and its evaluation is reported for one rule only.
- The new-family results are headlined in a floor that the procedure itself says a team would not have, and the source-floor results are reported selectively.

These, together with the traceability of numbers that now rest on unnamed result files, are bounded corrections that need no new data. I recommend minor revision.

## 2. Assessment

- **Originality: adequate** (unchanged). The combination of a production-referenced unit, distances for three-way verdicts read as points on operating characteristics, stratification by evidence relation and a guard-banded procedure is new for design-stage DFM decisions. The components are established, and they are now properly positioned (ISO 5725, Bechhofer, conformity assessment).
- **Significance for design research: adequate** (unchanged). The framework now speaks explicitly to verification planning, margins and support evaluation. However, Section 6.4 still maps the constructs onto design strands rather than saying what the results imply for each.
- **Significance for the collection (AI in DFM): adequate** (unchanged). The paper is framed consistently as an evaluation standard for AI-based DFM support, with a black-box formulation and a reporting standard. The AI content remains classical small-data regression, and the black-box route is untested.
- **Technical soundness: adequate** (unchanged). The exact estimator, the grouped evaluation and the relation-preserving refit are sound and reproduce. The remaining weaknesses are specific: the missing paired counterpart for M1s, the unit used for the new family, and the prior-dependent guard band.
- **Evidence supports the claims: weak → adequate.** The claims are now conditioned on the simulator and the data regime and labelled as observations. A handful of statements still go beyond the evidence: p. 15, l. 680–684; p. 20, l. 904–905; p. 14, l. 621; p. 19, l. 837–838 and 856–857; p. 17, l. 778–779; p. 22, l. 986–987.
- **Clarity, organisation and length: weak → adequate.** The length and table targets are met, and a notation table, core rules, physical anchors and a worked example have been added. However, the condensed Results are very dense, and "within the family" is used for two different scopes.
- **Positioning and references: adequate** (unchanged). All the strands I asked for, and ISO 5725, are now cited, but the positioning is a list of correspondences rather than an argument.
- **Fit to RED: adequate** (unchanged). The paper clearly passes the desk-reject criterion: it is a methodology for design decisions, not a case study of an individual design effort. Broad applicability is bounded by stated prerequisites rather than shown, which is acceptable for a first methodology paper with one demonstration.

## 3. First-round major comments, point by point

### A1. Broad applicability claimed but not shown: largely resolved

**Evidence.**
- Scope and conformance level are stated in the abstract (p. 1, l. 28–31) and the introduction (p. 2, l. 82–92).
- The design-research-methodology label is now correct: "prescriptive study with an initial support evaluation … hypotheses for confirmation" (p. 3, l. 93–97).
- The findings are separated into definitional ones and observations (p. 19, l. 866–873).
- p. 22, l. 1011 states plainly: "the procedure is general, the numbers are not".
- The prerequisites, a process mapping and the PA12 attempt as a negative result are given (Sect. 6.5, Table 6), and short calibration series are analysed (p. 17, l. 776–779; Table A2).
- "None is specific to forming" has been removed.
- A second application was not attempted. The editor made it optional, and I accept that.

**What remains.** Two wording points:
- the short-series result is read as showing that *qualification* needs only short runs, whereas only the calibration alternatives were truncated (new minor 2);
- Table 6 is an untested proposal whose "floor" changes construct between processes (new minor 10).

### A2. The floor: positioning, protocol, new family, between-run variation: largely resolved, except the new family

**Evidence.**
- The floor is positioned as a repeatability-type limit (p. 5, l. 217–222; p. 6, l. 271–274).
- A reference protocol is fixed (p. 6, l. 275–276).
- σ_b/F, σ_w/F, F/σ_LT and the drift ratio are reported in Table 3, and the lag profile and model floor in p. 12, l. 549–552.
- The floor is labelled as a within-run production-and-measurement floor and a lower bound (p. 7, l. 284–290), with a between-series variant in Table A2.
- RQ1 and the conclusions now say "common production-referenced scale" (p. 2, l. 66–68; p. 19, l. 867–869), and p. 7, l. 282–284 adds that equal distances do not mean equal nonconforming fractions.
- Step 6 of Fig. 1 names the floor of the produced family for a new family.

**What remains.**
- The new-family distances in Table 4, the abstract (l. 33–34), Table 5 and the conclusions (p. 23, l. 1034–1035) are still in the floor of the unproduced target family. The text gives source-floor values for two rules only (N2).
- Table 3 combines two incompatible aggregates (new minor 4).

### A3. The population behind the distances: resolved

The weighting is described exactly, with feasible failing-side counts (p. 8, l. 353–359). The false-accept-side distances are in Table 4, and per-characteristic distances are discussed (p. 22, l. 998–1001). Now that the weights and the false-accept side are shown, I accept the author's reason for keeping the pooled distances.

### A4. The sibling relation and the pooled scopes: largely resolved

**Evidence.**
- Sibling strata (p. 14, l. 628–632).
- Pooled scopes reported in Table 4 and discussed (p. 14, l. 636–640).
- Development record corrected (p. 12, l. 540).
- Continuous relations proposed (p. 9, l. 410–412; p. 22, l. 993–995).

**What remains.**
- The abstract (l. 31–32) and the conclusions (l. 1032–1033) still give "3.4 floors" without the strata, although Table 5 gives 0.85 for near-replicates (new minor 12).
- The intermediate stratum (nearest produced setting, NN, 2.45 floors) and the other rules' strata are only in `panel_sibling_strata.csv`. There, in the stratum where both siblings differ resolvably, M1s decides at 4.6 floors against NN's 4.85. This is worth a clause, given N1.

### A5. The headline claim on the relation: resolved

The decomposition and the reworded headline are in p. 14, l. 641 to p. 15, l. 673, the abstract (l. 34–35), p. 20, l. 900 and p. 23, l. 1035. The new family is presented as two transfers (abstract l. 33; Table 5). A production-informed transfer baseline is given for the wall angle (p. 15, l. 684–687). The decomposition reproduces exactly from `dec_intervals.csv`: relation 69 % and rule 6 % over all relations; relation 15 % and rule 68 % within a family.

### A6. What simulation and learning contribute: partly resolved

**Evidence.**
- The lubrication independence of the simulation and its consequence are stated (p. 8, l. 324–327).
- RQ3 is conditioned on the simulator and the data regime (abstract l. 36–38; p. 21, l. 935–938; p. 23, l. 1036–1038).
- The learners' inductive biases are named (p. 16, l. 729–732).
- The surrogate contrast has been recomputed with the current definitions (p. 15, l. 687–690).
- The controlled fidelity analysis was optional.

**What remains.**
- The new claim that the rescaled simulation adds information within a family (N1).
- The wording of the surrogate statement (new minor 8).

### A7. The procedure and the guidance: largely resolved for (b)–(e); (a) specified but not adequately evaluated

**Evidence.**
- (a) Step 6 is now a guard band on the observable margin (p. 10, l. 448–456; Fig. 1; p. 18, l. 802–816; Fig. 4).
- (b) The selection optimism is stated (p. 12, l. 536–540; p. 18, l. 813–814; p. 23, l. 1020–1023), and current-practice baselines enter the cost comparison (p. 19, l. 840–845).
- (c) Table 5 has a basis column, and the new-family row has moved to the observed block.
- (d) The validity claim is reworded as structural validity and support evaluation (p. 21, l. 961–966).
- (e) The trial's own error is stated (p. 9, l. 399–401; p. 13, l. 574–577).

**What remains.**
- N3: the requirement prior and the coverage of the step-6 evaluation.
- Table 5 labels prescriptive rows "definitions" (new minor 6).

### A8. Positioning in the design literature: partly resolved

**Evidence.** Sect. 2.2 (p. 3–4, l. 122–142) and Sect. 2.3 (l. 146–150) cite every strand I listed. Sect. 6.4 separates the predictive-uncertainty part of a margin from the part that absorbs change (p. 21, l. 953–954), as requested.

**What remains.** Section 6.4 (l. 948–966) is still a sequence of one-clause correspondences ("For X, the distances say Y"). It does not state what *the results* imply for each strand, which was the core of my comment and of R5a. Two or three sentences would suffice, for example:
- **Process-capability databases.** Tata and Thornton (1999) found such databases under-used. Here, within a family a look-up of the nearest produced setting was the most decisive rule, and learned models added abstention but not accuracy; across families it was useless. A database's value therefore lies in indexing records by their relation to the coming design rather than in model sophistication.
- **Preliminary information.** The decisive distance is a production-referenced measure of the precision of upstream information in the sense of Terwiesch et al. (2002). Its growth from 3.4 to 8.5 to at least 33 floors (35 in Table 4) says for which overlaps simulation-based manufacturability information can be released.
- **Set-based design.** The new-family safe distance (about 16–17 floors, roughly 0.8 mm of draw-in) bounds how far a feasible set can be narrowed before production evidence exists.

In addition, Sect. 2.2 calls the evidence relations "counterparts" of variant, adaptive and original design (l. 127–129). It should say how they differ: the design type concerns the novelty of the solution, whereas the relation concerns the novelty of its realisation relative to the produced evidence.

### A9. Readability, density and length: partly resolved

**Evidence.**
- Length and table targets are met: the main text ends on p. 23, with six tables and four figures.
- A notation table (Table A1) and seven core rules (Table 2) have been added.
- Physical anchors are given (abstract l. 31; p. 14, l. 604–605 and 623–624).
- A worked example is given (p. 18, l. 817–827), and the abstract has been rewritten.

**What remains.**
- The shortening was achieved largely by compressing prose, and Sects. 4.3, 5.1 and 5.7–5.9 are now denser than before. For example, p. 13, l. 566–577 carries more than a dozen numbers, and the sentence at p. 19, l. 840–845 is very hard to parse.
- Sect. 5.3 (l. 596–624) restates most of Table 4. Let the table carry the numbers.
- The worked example appears only at the end of Sect. 5.7, not as a running example. A two-line forward pointer in Sect. 3, where the constructs are introduced, would help RED readers.
- "Within the family" is ambiguous (new minor 3).

## 4. New issues arising from the revision

All figures I quote below are read-only computations on the released result files. They use the author's estimator (`share_curves` and `first_beyond` in `decisions.py`) and guard-band logic (`guard_band` in `panel.py`). I give them so that the author can verify them.

### Major (each must be fixed before acceptance; none needs new data)

#### N1. The rescaled simulation does not add information beyond a trend in force (p. 15, l. 680–684; p. 20, l. 903–905; contrast p. 1, l. 36–37 and p. 23, l. 1036–1038)

**Problem.** The evaluation design pairs every calibrated rule with a counterpart without the simulation, "so that the paired difference isolates what the simulation contributes" (p. 12, l. 520–523). M1s, the new scaled rule, has no such counterpart. Sect. 5.5 compares it instead with M1n, the median of all produced alternatives, which ignores the force.

Within a geometry, the nominal simulation depends only on the blank-holder force, because it does not depend on lubrication (p. 8, l. 324–327). In M1s, s0 therefore acts as a three-level force indicator. The matching no-simulation rule is the same least-squares fit with the force in place of s0.

I computed this rule from `dec_alternatives.csv` with the calibration sets of Sect. 4.4. My re-derivation of M1s matches the stored intervals to 10⁻¹². Decisive distances in floors:

| Relation | M1s, q95 = a + b·s0 | q95 = a + b·force, no simulation | NN | M1n |
|---|---|---|---|---|
| new variant (sibling produced) | 4.9 | 3.5 | 3.4 | 9.1 |
| new process setting | 19 | 8.2 | 8.5 | 10 |
| interpolated | 19 | 4.7 | 4.7 | 4.8 |
| extrapolated | 19 | 8.9 | 9.5 | 12 |

Once rescaled, the simulated force trend is worse than a straight line in force in both within-family relations. For an interpolated setting, the straight line coincides with NN by construction. M1s's advantage over M1n comes from the force, not from the simulation.

**Why it matters.**
- The response presents this as the single exception to the first version's conclusions ("the simulation does add information within a family when it is rescaled"). Sect. 6.1 turns it into an RQ3 finding, which is the paper's most quotable message for this collection.
- It also makes the paper internally inconsistent. The abstract (l. 36–37) and the conclusions (l. 1036–1038) say that the simulation, as used, helped only across families, whereas Sects. 5.5 and 6.1 say that a fitted scale made it useful within a family.

**What would resolve it.**
- Add the force-trend rule as M1s's paired counterpart, as Sect. 4.4 requires, in the lower block of Table 4 or a footnote.
- Rewrite p. 15, l. 680–684 and p. 20, l. 903–905 accordingly, and correct the response's summary. The abstract and the conclusions can then stand as they are.

#### N2. New-family results: unit and selective reporting (p. 7, l. 290–292; Fig. 1; p. 14, l. 618–624; p. 19, l. 856–857; Table 4; Table 5; abstract l. 33–34; p. 23, l. 1034–1035)

**Problem.** For a new family, the framework now prescribes the floor of the produced family (p. 7, l. 290–292; Fig. 1). Yet Table 4, the abstract, Table 5 and the conclusions still report the new-family distances in the floor of the target family, which, as p. 14, l. 622 itself says, a design team would not have. The text gives source-floor values only for M5 and the envelope rule M2 (l. 622–624). I recomputed the source-floor distances; they agree with `panel_source_floor.csv`:

| Rule | target floor δ_d/δ_s (Table 4) | source floor δ_d/δ_s |
|---|---|---|
| M1 | 35/35 | 33/33 |
| M2 | 51/16 | 41/26 |
| M3 | 49/21 | 40/17 |
| M5 | 38/28 | 35/31 |
| Mc | 38/38 | 43/43 |

The headline magnitude, that no rule is safe closer than 16–17 floors, is robust to the unit. The identity of the safest rule is not. "The envelope rule is the safest at 16 floors" (l. 621) and "the envelope rule the safest for a new family" (l. 857) hold only in the unit that the procedure rules out. In the floor a team would have, M3 is the safest rule and M1 the most decisive. Even in the target floor, M2's safe distance of 15.8 floors has a bootstrap interval of 13.7–23.2 floors (`dec_resolution.csv`, fits fixed), which overlaps M3's 16.2–28.4.

**Why it matters.** The new family is the only change of product design in the data and the situation in which, by the paper's own results, a trial is most needed. Reporting it in the unit available at decision time was the substance of my comment A2(c) and of the editor's R2d.

**What would resolve it.**
- Give the new-family column of Table 4 in the source floor, or both floors side by side.
- Add M3 to l. 622–624.
- Reword l. 621, l. 857 and the Table 5 row, for example as "best rule safe at about 16–17 floors; which rule is safest depends on the unit".
- Give the safe-distance interval of the headline figure.

#### N3. Step 6: the guard band depends on a requirement prior that is not stated, and its evaluation is reported for one rule only (p. 10, l. 448–456; p. 18, l. 802–816; Fig. 4; Table 5, "Deciding a single design"; Table A1, *g*)

**Problem (a): the prior.** The guard band g is the smallest observable margin beyond which at least 95 % of decided verdicts were correct, for requirements "within 20 floors of the truth" (l. 450–451).
- **How the prior is built.** In the code, the requirement grid points are weighted equally. They are spaced 0.5 floors apart up to ±10 floors and placed only at 12, 15 and 20 floors beyond, so about 87 % of the weight lies within ±10 floors. The editor asked for this prior to be stated (R4a). The response says it is stated, but the manuscript gives only the ±20 range.
- **Why the prior matters.** The decisive and safe distances are defined at each requirement distance and need no prior. The guard band, by contrast, is a posterior quantity. A large observed margin is reassuring only if large margins usually arise from requirements far from the truth; when requirements lie near the truth, large margins arise from large prediction errors, which are wrong about half the time.
- **Sensitivity.** I re-ran `guard_band` on the stored intervals with other priors. Guard band in floors ("none" means no g up to 20 floors reaches 95 %):

| Relation, rule | paper's grid, ±20 | uniform, ±20 | grid, ±5 | grid, ±3 |
|---|---|---|---|---|
| new variant, NN | 0.25 | 0 | 2.0 | 8.0 |
| new variant, M5 | 0 | 0 | 0 | 6.5 |
| interpolated setting, NN | 2.0 | 0.5 | 4.25 | 5.0 |
| extrapolated setting, NN | 7.0 | 3.5 | 14.25 | 14.75 |
| extrapolated setting, M2 / M5 | none | 5.75 / 5.0 | none | none |

**Consequences.**
- Release-level requirements lie a median 1.0–3.1 floors from q95 (p. 19, l. 830–832), that is, in the ±3 to ±5 regime. There, the guard bands are several times those reported.
- The worked example survives: its NN margin of 6.2 floors exceeds the 4.25–5.0 floors needed under these priors.
- However, Table 5 and Table A1 present g as a property of rule and relation ("Apply the rule's guard band to the observable margin", basis "definitions"), which it is not.

**Problem (b): what is reported.** Section 5.7 gives guard bands and the resulting operating characteristics only for NN, plus the statements that interval rules need none with a sibling and that nothing qualifies for a new family. `panel_step6.csv` shows more:
- M2 and M5 never qualify for an extrapolated (or pooled) new setting.
- M1 and Mc never qualify even with a sibling.
- For an interpolated setting, M2 and M5 qualify with g = 0.75 and 0.5 floors but still send 31 % and 40 % of designs to trial at 10 floors.

These are exactly "the operating characteristics and trial rates of the procedure's actual decision rule for each relation" that R4a required, and they are the procedure's most practical output. In addition, Fig. 4(b) pools interpolation and extrapolation, although the guard bands are set for each separately.

**What would resolve it.**
- State the prior precisely in Sect. 3.6 and in the caption of Fig. 4.
- Say in Sect. 3.6, Table A1 and Table 5 that g must be derived for the distribution of requirement distances the team expects.
- Report g under at least one prior concentrated near the capability, for example ±5 floors.
- Add a compact table of the seven core rules by relation (sibling, interpolated, extrapolated, new family), giving g, δ_d/δ_s under step 6, and the trial share at 10 and 20 floors. All of these are already in `panel_step6.csv`.
- Space can come from Sect. 5.3, which restates Table 4.

### Minor

1. **Traceability of the evidence and the archive: required before acceptance** (whole paper; p. 23, l. 1047–1052; p. 25, l. 1132–1135).
   - The supplementary material was removed. The response says that results the paper does not tabulate "are named by their result file", but the manuscript names no result file.
   - The archive is "deposited on Zenodo [DOI pending]", although the editor required the DOI at resubmission.
   - Numbers that now rest only on unnamed files include: the sibling strata (l. 628–632); the force-level split (l. 634–635); the source-floor distances (l. 622–624); the guard bands and step-6 rates (l. 807–813); the capability shares (l. 830–838); the cost results (l. 840–845); the surrogate accuracy (l. 687–689); and the lag profile and in-line drift (l. 549–571).
   - Either provide electronic supplementary material with compact versions of these tables, as R5c suggested, or add an appendix table that maps each quoted result to its script and file. Mint the DOI before acceptance.
2. **Short calibration series show calibration, not qualification** (p. 17, l. 776–779; p. 22, l. 986–987).
   - In `robustness.py` (variant 16), only the calibration alternatives' q95 come from the first n parts. The truth stays the 500-part q95, and the floors stay the reference floors.
   - The result shows that rules *calibrated* on short runs score almost as well against full-series truths. *Qualifying* rules with short runs would score them against truths that reproduce only to about 1–1.5 floors (p. 13, l. 575–577).
   - Reword "calibration runs of about 50 parts per variant qualified the rules" and "the qualification needs short runs" accordingly.
3. **"Within the family" denotes two different scopes.**
   - It means the new-variant relation only at p. 14, l. 639–640; p. 15, l. 677–681; p. 16, l. 722–726; p. 18, l. 807–808; and p. 19, l. 837–838.
   - It means both within-family relations at p. 14, l. 644; p. 17, l. 777; p. 19, l. 856; and p. 20, l. 900.
   - The result is a self-contradiction at p. 20, l. 904–905: "useful within a family but harmful for a new setting".
   - Use "with a produced sibling" for the first meaning throughout.
4. **Table 3 combines incompatible aggregates** (p. 13, l. 553–564).
   - σ_LT is the median over series of the whole-series standard deviation, whereas σ_w is the root mean of the within-batch variances (`floor_protocol` in `panel.py`).
   - As a result, σ_w exceeds σ_LT in 10 of the 14 geometry–characteristic rows, and √(σ_w² + σ_b²) exceeds σ_LT in 13. A reader will take this as an error, because a within-batch scatter cannot exceed the total scatter.
   - Use the same aggregate for all three quantities.
5. **One of the "definitional" findings is empirical** (p. 19, l. 866–872).
   - The claim that an interval rule "reaches its nominal level only where the calibration alternatives are exchangeable" is not a consequence of the definitions. Exchangeability is sufficient for the coverage guarantees, not necessary.
   - The failures for a new setting (43–55 % coverage) are an observation on this dataset.
   - This reverses the labelling I asked for in first-round minor comment 19. Say instead "is guaranteed its nominal level where … and fell short where they were not".
6. **Table 5: the basis column and the "Fixing a requirement" row** (p. 20, l. 877–889).
   - Rows such as "Choosing a rule: compare it with the nearest produced setting" and "Deciding a single design" are prescriptions motivated by the framework and by this dataset. They are not consequences of definitions. Label them "framework (prescriptive; usefulness not evaluated)".
   - The "Fixing a requirement" row, and p. 20, l. 910–913, compare an *expected*, that is predicted, margin with δ_s, which is defined on the true margin. This is the same issue that step 6 resolved. Call it a planning heuristic and refer to the guard band for the decision itself.
7. **Release-level requirements are decided reliably only with a sibling** (p. 19, l. 837–838). At a performance index of 1.33, NN is right in 91 % of new-variant cases but in only 65 % for a new setting (l. 833–836; `panel_capability.csv`). "Only within a family" should read "only with a produced sibling".
8. **Surrogate statement** (p. 15, l. 687–690; p. 21, l. 937–938).
   - `ds_surrogate.csv` holds the leave-one-out RMSE of the surrogate against the simulation, so "within 1.8 floors" is an RMSE, not a bound.
   - The surrogate's decision fitness was not evaluated; it is inferred. Write "would be essentially that of the simulation", or score the surrogate as a rule.
9. **Worked example** (p. 18, l. 817–827).
   - State that the requirement (15.30 mm, 8.4 floors above q95) was chosen for illustration.
   - State that the guard band of 2.0 floors and the reliability statement were estimated on data that include this very case.
   - Give the full widened intervals and margins of M2, M5 and M5n, as R4b asked.
10. **Table 6 and the black-box route** (p. 22, l. 967–979 and 990–995).
    - The table is an untested proposal and should be labelled as such.
    - Its "Floor" column changes the construct: "between builds" for additive manufacturing and "between cavities" or "between offset intervals" are between-unit quantities. The paper's own between-series variant shows that such floors are 1.5–9.1 times the within-run floor (p. 13, l. 573–574). Distances in floors are therefore comparable within a protocol, not across processes; say so.
    - For a classifier with a fixed threshold, the requirement cannot be swept for each case. The operating characteristic must then be estimated by binning cases by |d|, which is not the exact estimator of Sect. 3.4. One sentence would suffice.
11. **Paired differences in Sect. 5.5: name the relation** (p. 15, l. 677–680). The figures 3.9 and 6.2 floors are for the new-variant relation. For a new setting, M1 decides 13.5 floors further out than M1n (`dec_paired.csv`), so "degrades two rules" understates the effect there.
12. **The 3.4-floor headline** (abstract l. 31–32; p. 23, l. 1033). Add that this is 0.85 floors for near-replicate siblings and 4.9 for resolvably different ones (p. 14, l. 628–632).
13. **Uncertainty of the headline safe distances** (Table 4). The intervals cover only δ_d, and only for four rules. The new-family headline is a safe distance (M2, 15.8 floors, interval 13.7–23.2). Give δ_s intervals for the headline figures and a δ_d interval for M2, as first-round minor comment 23 asked.
14. **Designer-study "hypotheses"** (p. 21, l. 941–945). The questions given are research questions. Give one or two testable hypotheses, as the editor's recommendation 3 asked. An example: "designers shown the guard-banded verdict release fewer designs within the safe distance than designers shown the Gaussian-process interval, at equal trial rates".
15. **The error of a tryout trial** (p. 9, l. 399–401; p. 13, l. 572–577). A trial on another day carries between-run variation, not only the reproducibility of about one floor within a run. Say which applies to the trial that step 6 calls for.

## 5. Remaining minor and editorial points

First-round minor comments 1–8, 10–16, 18, 20–22, 24 and 25 are resolved. Comments 9, 17, 19 and 23 are partly resolved (items 1 and 4 below, and new minor 5 and 13 above).

1. **p. 2, l. 79–80.** "Characterised by two operating characteristics in floors" contradicts p. 8, l. 366–367 ("points on operating characteristics"). Align with the latter.
2. **Table 2 note (p. 9, l. 395–396) and Table 4 note (p. 15, l. 668–669).** Both say that M6 "appears only in the robustness analysis", yet M6 is in Table 4.
3. **p. 9, l. 406–410.** Force and lubrication are both process parameters, yet one defines a "process setting" and the other a "variation". State the general rule: the factor that defines a sibling is the one varied at a fixed setting.
4. **p. 19, l. 838–845.**
   - Rewrite the cost sentence, perhaps as a three-row table.
   - The sensitivity map over cost ratios mentioned in the response (`scen_cost_map.csv`) is not in the paper.
   - The near-limit false-accept statements of the ISO 2768-1 scenario rest on six failing alternatives (first-round minor comment 17); say so.
5. **Fig. 4.** State the prior in the caption, mark the guard bands, and show interpolation and extrapolation separately, as the guard bands are set for each.
6. **p. 19, l. 856–857 and Table A2.** The new-family robustness rows show only M2 and M5. "The envelope rule the safest for a new family" cannot be checked against M3, and it does not hold in the source floor (N2).
7. **p. 5, l. 221–222.** "What is new is its use as the unit of a design decision rule" deserves one more sentence on what this adds to the repeatability limit r, which judges the agreement of results rather than the scale of decisions.
8. **p. 22, l. 1001–1005 (optional).** Say how many builds the PA12 data contain and whether the between-build floor from anchors that is named as the remedy is feasible with them. If it is, applying it would be the most direct answer to the generality concern; if not, say why.
9. **Table 5, l. 878.** "Before trusting a predictor" should be "Before relying on a predictor", in line with R1.
10. **p. 20, l. 917–920.** A single worked example cannot show that "the most decisive rule is also the most transparent". Present this as an argument.
11. **References.**
    - Please check the editions cited as ISO 5725-2:2025 and ISO 22514-2:2026; the editions I know are 2019 and 2017.
    - Montgomery (2019) lacks its place of publication.
12. **p. 13–14, l. 596–624.** Cut the numbers that repeat Table 4 and keep one or two anchors per relation.
13. **Abstract, l. 24–27.** One sentence carries both definitions and the list of relations; consider splitting it.

## 6. Recommendation

**Minor revision.**

The paper is now a methodology paper that fits RED:
- it defines constructs for design-stage decisions (a production-referenced unit, decisive and safe distances by evidence relation, and a guard-banded procedure);
- it evaluates them on real production data against a production-record baseline;
- it labels its evaluation correctly in design-research-methodology terms;
- it bounds its applicability by stated prerequisites.

My first-round concerns about over-general claims, the population behind the distances, the headline on the relation and the unevaluated step 6 have largely been met.

What remains is specific:
- N1 needs one paired rule and two rewritten sentences.
- N2 needs one column re-expressed and three sentences reworded.
- N3 needs the prior stated, one sensitivity computation and one compact table whose content is already in `panel_step6.csv`.
- The traceability of the result files and the DOI must be provided.

None of this needs new data, and the main conclusions stand. If anything, N1 and N3 reinforce the paper's sober message: within a family the production record carries the decision, and release-level requirements need trials. The corrections are substantive rather than cosmetic, however, and they should be made and checked before acceptance.

## 7. Confidential comments to the editor

The revision is responsive and careful, and I now regard the paper as a sound fit for RED and for this collection. I have no concern about its integrity: Table 4, the decomposition, the coverage figures, the paired differences, the worked example and the capability shares all reproduce from the released files. My three substantive points come from read-only checks with the author's own estimator and guard-band code:
- the force-trend counterpart of M1s (N1);
- the prior-dependence of the guard band (N3);
- the source-floor ranking for the new family (N2).

They change specific claims, including the response's one highlighted "exception", but not the paper's main conclusions; you may wish to confirm them. The DOI you required at resubmission is still pending, and several numbers can at present be traced only through the response and a mutable repository. I do not need to see the manuscript again if you can verify N1–N3 and the traceability fix, but I would be glad to check them if that is helpful. As before, I have not assessed the forming physics or the scan extraction in depth.
