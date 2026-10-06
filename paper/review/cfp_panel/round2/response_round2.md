# Response to the guest editor and the reviewers: second round

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Revision of:** the version reviewed on 6 October 2026 (frozen as `paper/review/cfp_panel/round2/main_reviewed.tex`)

> **Note on this document.** The decision letter and the three reports it answers (`editor_decision_round2.md`, `reviewer_A_round2.md`, `reviewer_B_round2.md`, `reviewer_C_round2.md`) were written by AI agents acting as a simulated review panel. They do not come from the journal or its reviewers. The response is written as it would be to a real panel.

**Locations.** Page and line numbers refer to the revised manuscript `paper/main.pdf`, which is compiled with line numbers. The abstract, tables and captions carry no line numbers and are named instead. A version marked up against the second-round manuscript is `paper/review/cfp_panel/round2/main_diff.pdf`. The manuscript remains a single file with no supplementary material. Table A5 in the appendix maps every number that the text quotes but does not tabulate to its script and result file. The archive that holds these files is cited as Canseven (2026); its DOI is **[DOI to be inserted after deposit]** (see S6).

Dear Guest Editor, dear Reviewers,

Thank you for a second set of careful reports, and for a letter that again checked the reviewers' figures against the released files. All seven required items are addressed in the manuscript. The one step that the manuscript cannot complete by itself is the DOI of S6, which is minted when the archive is deposited, before resubmission (Part 8). The revision follows the letter wherever it qualifies a report.

Two of the corrections strengthen the paper's sober message, as the letter anticipated:

- **Within a family, the production record carries the decision even against a rescaled simulation.** The force-trend rule M1sn, the paired counterpart of the scaled simulation M1s, is more decisive than M1s in every resample (S1).
- **Release-level requirements need trials.** This holds even more clearly once the prior of the guard band is explicit (S2).

**Length.** The main text, from the abstract to the conclusions, still ends on page 23. The whole paper still has 30 pages. The new material is in the appendix:

- Table A3: the interval rules by relation;
- Table A4: the procedure's decision rule by relation;
- Table A5: the mapping of numbers to scripts and result files.

The main text keeps six tables and four figures. Compensating cuts, mostly of numbers that repeat Tables 4 and A2, keep it on 23 pages.

**Headline numbers that changed.** So that you can check them quickly:

- **A new process setting.** The best attainable distance is now 8.2 floors, set by the force trend M1sn, against 8.5 for the nearest setting. By stratum it is 4.7 floors interpolated, 4.9 extrapolated to 500 kN (the nearest setting) and 8.9 extrapolated to 100 kN (the force trend).
- **A new family.** New-family distances are now in the produced family's floor in Table 4, Figs. 2 and 4, Table A3 and the step-6 analysis; Table A4 has no new-family column, because no band qualifies. The decomposition is given in both floors. Table A2 keeps the new family's own floor, as its note says (Part 4, A-r6). The best attainable new-family decisive distance is therefore 33 floors (M1), not 35. The headline share of the decomposition is 67 % (69 % in the new family's own floor).
- **Short calibration series.** The bound is 1.5 floors, not 1.2. The previous figure covered the two relations but not their interpolated and extrapolated cases. The 100-part variant is back in Table A2.
- **Gaussian-process specifications.** They move the decisive distances by at most 1.2 floors and the safe distances by at most 2.1. The reviewed version attributed the 2.1 floors to the decisive distances.

---

## Part 1. Map of the required changes S1–S7

| Item | What was done | Where |
|---|---|---|
| **S1** Withdraw the claim that a rescaled simulation adds information within a family | **The rule.** The force trend M1sn ($q_{95} = a + b\cdot$force, least squares) is added as the paired counterpart of M1s. It is in Table 2, in the lower block of Table 4 and in the evaluation design, and it enters the strata, force levels, decomposition, step 6, guard priors, guards, capability, robustness and refit analyses (not the calibration budget). Because it now carries headline numbers, Sect. 3.3 and the caption of Table 2 say that the first seven rules and M1sn carry the main results. **The result.** M1sn decides 1.4 floors closer than M1s with a sibling (paired interval +0.65 to +3.0; refit +1.35 to +3.6) and 11 floors closer for a new setting (+5.3 to +13.8; refit +8.8 to +12). Within a family, M1s is never the more decisive in a resample or a refit configuration. For a new family M1s is the more decisive, by about 10 floors, since the simulation carries the change of geometry. **The text.** Section 5.5 and Section 6.1 now say that the simulation, as an offset or rescaled, added no information within the family; across families it was decisive. The abstract and the conclusions say "the simulation as used, offset or rescaled". **Where the force trend is best.** For a new setting it decides at 8.2 floors against the nearest setting's 8.5. Extrapolated, it decides at 8.9 against 9.5 (Table 4). These differences are reported without interpretation (paired −0.3, −2.0 to +2.6 floors). **The decomposition.** It excludes M1sn in its headline figures and gives the within-family shares with M1sn in brackets (71 % rule, 15 % relation; over all relations with M1sn, 68 and 6 %, in `panel_decomposition.csv`). **The response.** The "one exception" is withdrawn (Part 3). | Table 2; p. 7, l. 303; p. 11, l. 499; Table 4 and its note; Sect. 5.3 p. 13, l. 591; Sect. 5.4 p. 15, l. 684; Sect. 5.5 p. 16, l. 697; Sect. 5.9 p. 19, l. 857; Sect. 6.1 p. 20, l. 909; abstract; Sect. 7 p. 23, l. 1052 |
| **S2** State the prior of the guard band, show its influence, report the procedure's operating characteristics | **(a) The prior.** It is stated exactly: the 47 distances of the evaluation grid within ±20 floors, equally weighted (0, ±0.5 to ±10 in steps of 0.5, ±12, ±15 and ±20; 87 % of the weight within ±10). Infeasible requirements are dropped, and g is searched in steps of 0.25 floors up to 20. The text says why the prior represents the requirements a team faces. The prior is stated in Sect. 3.6, in the caption of Fig. 4 and in Table A1. **(b) Its influence.** g is computed under four further priors (grid within ±5 and ±3; uniform within ±20 and ±50; `panel_guard_priors.csv`). Sect. 5.7 quotes the near-truth prior (±5) and both uniform ones, and the worked example the ±3 grid. **(c) Its status.** Sect. 3.6, Table 5 ("Deciding a single design") and Table A1 say that g is derived for the distribution of requirement distances the team expects, not for rule and relation alone. **(d) The tables.** Table A4 gives g, δd/δs under step 6 and the trial shares at 10 and 20 floors for M1, M1s, M2, M5, M5n, NN, M3, M3n and M1sn, with a sibling, interpolating and extrapolating. Its note covers M0, M0w, Mc and the new family, for which no band up to the cap qualifies (Mc interpolating at 18 floors). Table A3 gives coverage, half-width and the decisive distance of the interval centre for the interval rules, by relation including the new family. The rules that never qualify are named in the text and in the note to Table A4. Guard performance has one sentence. **(e) The new family.** "Every design goes to trial" is presented as a consequence of the reference prior and the 20-floor cap. Under a uniform prior within ±50 floors, M2, M3 and M5 qualify for a new family at 6.25, 6.5 and 15 floors. The letter's 3.75 and 11.75 floors for M2 and M5 are the same bands in the new family's own floor. Die-tryout practice is noted. **(f) Fig. 4.** It shows the sibling, interpolated, extrapolated and new-family relations in separate panels, marks g with filled markers and takes the share over verdicts whose margin is at least the given value. **(g) The worked example.** The requirement is chosen for illustration, and g was estimated on data that include the case. | Sect. 3.6 p. 9, l. 407; p. 9, l. 406; Fig. 4 caption; Table A1 (row g); Table 5; Sect. 5.7 p. 17, l. 772; p. 17, l. 779; p. 18, l. 803; p. 18, l. 805; p. 18, l. 810; p. 18, l. 820; Tables A3, A4 |
| **S3** Report the new family in the floor that the procedure prescribes | **The floor.** The new-family columns of Table 4 are in the produced family's floor, and the note says so. The new-family row of Fig. 2 and the new-family column of Table A3 use the same floor. The text gives both floors: M1 33, M5 35 (decisive), M3 17, M2 26, M5 31 (safe) in the produced family's floor; M2 16, M3 21, M5 28 (safe) in the new family's. **Intervals.** Table 4 gives the safe-distance intervals of M2, M3 and M5 and the decisive-distance interval of M2 for a new family. **No safest rule.** "The envelope rule is the safest" is gone. The text says that the best rule was safe at about 16–17 floors in either floor and that two transfers do not resolve which rule is safest. The safe distance of M3 minus that of M2 lies between −16 and +7 floors in the produced family's floor and between −3 and +8 in the new family's. M3 is named in Sect. 5.3. **The unit.** It is stated wherever the 16–17 floors appear: the abstract, Table 5 and the conclusions. | Sect. 3.2 p. 6, l. 271; Table 4 and its note; Fig. 2 caption; Sect. 5.3 p. 13, l. 596; p. 14, l. 634; abstract; Table 5 (row "New family"); Sect. 7 p. 23, l. 1049 |
| **S4** Carry the strata and the force split into the abstract, the conclusions and the guidance; label the findings correctly | **3.4 floors.** Wherever it is quoted as a headline, the nearest setting's strata are given: 0.85 floors for near-replicates (58 cases) and 4.9 when both siblings differ resolvably (34 cases). See the abstract, Sects. 5.4 and 6.1, Table 5 and the conclusions. Sect. 5.3 gives the pooled 3.4 floors with its interval before Sect. 5.4 splits it. Sect. 5.4 also gives the intermediate stratum (2.5 floors) and the force trend and M5 in the resolvable stratum (4.5 and 9.7). The sentence in Sect. 5.4 that pools the strata says so. **The new setting.** The abstract and the conclusions give 4.7 interpolated, 4.9 extrapolated to 500 kN and 8.9 to 100 kN, where the stroke speed also changed. Sect. 5.4 gives the nearest setting at 11 (100 kN) and 4.9 (500 kN), with the force trend at 8.9 at both. Sect. 6.6 says "the extrapolation to 100 kN". **Release-level requirements.** "Inside every decisive distance except a near-replicate's" (abstract, Table 5, conclusions). Sect. 5.8 restricts this to indices up to 1.33: the limits at 1.67 and 2.0, 2.5 and 3.1 floors above the 95th percentile, lie beyond the 2.5 floors of the nearest setting with one resolvable sibling. "Decided at the design stage only with a produced sibling" (Sect. 5.8, Table 5). The test is stated to be one-sided by construction, and its shares are given as right/false-reject/trial rates; the 79 % of M1s against 65 % for the nearest setting is shown. Sect. 3.1 is softened to "locates such limits relative to the distances, without deciding them". **Learning.** The abstract and the conclusions name where the intervals held their level: 85–96 % with a sibling, under 50 % when extrapolating or for a new family. Sect. 5.5 gives 85–86 % for the Gaussian processes with a sibling, 43–55 % for a new setting (93 % for M2n and M5n when interpolating) and at most 12 % for the Gaussian processes for a new family. "Predicted as well as the nearest produced setting" is qualified by "with a produced sibling". **Labels.** The exchangeability clause in Sect. 6.1 is restricted to the guarantee of the distribution-free intervals. The prescriptive block of Table 5 is labelled "From the framework (prescriptive; usefulness not evaluated)". "Fixing a requirement" is now "Planning a requirement", a heuristic in Table 5 and in Sect. 6.2; the decision itself needs the guard band. **Terms.** "With a produced sibling" denotes the sibling relation, and "within a family" both within-family relations. "Six to nine produced alternatives at two or three force levels" replaces "six to nine produced settings". | Abstract; Sect. 5.4 p. 14, l. 640; p. 15, l. 685; Sect. 5.5 p. 16, l. 720; Sect. 5.8 p. 18, l. 826; p. 18, l. 827; p. 19, l. 834; Sect. 3.1 p. 6, l. 239; Sect. 6.1 p. 19, l. 869; p. 20, l. 906; p. 20, l. 910; Sect. 6.2 p. 20, l. 915; Sect. 6.6 p. 23, l. 1031; Table 5; Sect. 7 |
| **S5** Correct the description of three methods and three analyses | **Jackknife+.** It is described as a median-centred jackknife+ with extreme order statistics. The guarantee is $1-2/(n+1)$, that is 0.71 to 0.80, and it is approximate because of the median centring. The empirical coverage is quoted: 96 % (M3) and 89 % (M3n) with a sibling, against a guarantee of 7/9. **Refit bootstrap.** The text says that the 200 resamples contain 48 of the 49 configurations. In three of four draws a pattern is duplicated, so a new variant keeps one distinct sibling and five distinct calibration alternatives, and the duplicated series enter the noise floor as identical pairs. The intervals show the effect of losing a pattern, not sampling uncertainty. Point estimates at the edge of their intervals are named: M1s with a sibling and the safe distances of M2 and M5. "All 200 resamples" now reads "all 200 resamples (48 configurations)". The appendix says that the noise floor is not restricted to distinct series. **Table 3.** σLT, σb and σw are all classical statistics pooled over the series as root mean squares; σw is below σLT in every row. One floor is now 0.7 to 1.7 long-term standard deviations, against 0.66 to 2.2 with the mixed aggregates (Sect. 5.1). **Short series.** "Calibrated", not "qualified"; the truths and floors are those of the full series (Sect. 5.6, Sect. 6.5, note to Table A2). **The trial's own error.** As a run, the trial also carries the variation between runs (Sects. 3.4 and 5.1). **Surrogate.** It is described in one clause (a Gaussian process over force, friction and thickness, with its leave-one-out RMSE) and scored as a rule: 109 against 108 floors as M0, 15 against 15 as M1 with a sibling. | Sect. 3.3 p. 7, l. 313; Sect. 5.5 p. 16, l. 719; Appendix p. 24, l. 1082; Sect. 4.4 p. 12, l. 508; Sect. 5.9 p. 19, l. 855; p. 19, l. 858; Appendix p. 24, l. 1085; Table 3 note; Sect. 5.6 p. 17, l. 762; Sect. 6.5 p. 22, l. 990; Sect. 3.4 p. 9, l. 379; Sect. 5.1 p. 12, l. 549; Sect. 5.5 p. 16, l. 707 |
| **S6** Make every number traceable and deposit the archive | **In the paper.** The numbers that carry claims are in the paper: the step-6 table (Table A4), the interval table (Table A3) and the new-family figures in both floors (Table 4, Sect. 5.3). **Table A5.** A new appendix table maps every other number quoted in the text, section by section, to its script and result file. For the oil-film medians of Sect. 4.1, the run metadata (`panel_runs.csv`) now hold them. **The archive.** It is cited in Sect. 4.5, the appendix, the data and code availability statements and the reference list. It will hold the code, the feature tables and the result files of this version, as `.zenodo.json` describes. **The DOI.** It is **[DOI to be inserted after deposit]**. The deposit metadata (`.zenodo.json`) and the release notes are prepared; the author mints the DOI before resubmission and inserts it in the reference list (`canseven2026archive`). The GitHub link is kept as a working copy only. **Result files.** `panel_physical_units.csv` is regenerated. Each characteristic is scored in its pooled floor and converted to its unit, exact up to 0.05 pooled floors instead of 0.05 units. `alt_mrc.csv` is unchanged; the response's statement about it is corrected (Part 3). | Table A5; Sect. 4.5 p. 12, l. 525; Appendix p. 24, l. 1064; Data and Code availability; References |
| **S7** Make the reuse section operational for other AI-based DFM tools | **Classifiers with a fixed threshold.** The operating characteristic is estimated by binning test cases by their true margin, which is not the exact estimator, unless the requirement is made an input. A probabilistic classifier needs two thresholds to return a trial. **Language-model checks.** κ and ω are computed on a requirement grid with repeated queries, and the share of non-monotone verdict sequences is reported. **Continuous relations.** Strata are formed by distance from the produced designs or by position relative to their hull, and each needs about as many cases as a relation here: with 126 cases, some 240 verdicts, the 95 % threshold already rests on about a dozen. **The minimal report.** It is a numbered checklist of six items, including the source of the noise variance and, for language-model tools, the prompt and query protocol. **Table 6.** It is marked as an untested proposal. The text says that distances in floors are comparable within a protocol, not across processes, because floors between builds, cavities or offset intervals are between-unit quantities (here 1.5–9.1 times the within-run floor). For injection moulding the floor is taken per cavity, with cavity offsets as effects. | Sect. 6.5 p. 22, l. 993; p. 22, l. 997; p. 22, l. 1002; p. 22, l. 1004; p. 23, l. 1013; Table 6 |

---

## Part 2. Recommended, optional and editorial points of the letter

### Recommended (Section 5 of the letter)

1. **Section 6.4 and the design type.** *Changed.* Sect. 6.4 now states what the results imply for each strand:
   - capability databases: index production records by their relation to the coming design, rather than add a more sophisticated model on top;
   - margins: the safe distance is the predictive-uncertainty part of a margin;
   - overlapped development: the growth of the decisive distance from about 3 to 8 and over 30 floors says for which overlaps preliminary manufacturability information can be released;
   - set-based design: the new-family safe distance, some 0.8 mm of draw-in, bounds how far a feasible set can be narrowed;
   - testing: the distances and trial rates say when a test is cheaper than a decision.

   Sect. 2.2 says how the evidence relation differs from the design type: the design type concerns the novelty of the solution, the relation the novelty of its realisation relative to what has been produced. See p. 21, l. 958 and p. 3, l. 118.
2. **Density.** *Changed.*
   - Sect. 5.3 is about a fifth shorter, and the nominal simulation takes one sentence. The new-family paragraph keeps the figures that S3 requires.
   - Sect. 5.9 no longer repeats the entries of Table A2.
   - In Sect. 5.1, the drift sentence is split from the normal-model sentence, and the in-line drift sentence is shortened.
   - The cost passage is a list (p. 19, l. 839).
   - The guard-band passage of Sect. 5.7 is split into separate paragraphs on the margin, the guard bands, their prior and the worked example.
   - Sect. 3.6 points forward to the worked example (p. 10, l. 437).
3. **Cost comparison.** *Changed.* It is a three-item list that names the tie at zero cost with a produced sibling (nearest setting, scaled simulation and force trend). It also says that the comparison inherits the coarseness of the ISO 2768-1 scenario: 32 of 108 decisions lie within 5 floors of the limit, 6 of them on failing alternatives (p. 19, l. 837). The comparison on the capability-anchored requirements was not added, because that test is one-sided (S4).
4. **Positioning of the floor.** *Changed.*
   - The floor is described as closer to a time-different intermediate-precision limit of batch centres within a run (ISO 5725-3:2023, now cited), and the runs as a time-dependent model with varying location in the terms of ISO 22514-2 (p. 6, l. 254).
   - A2 concerns within-run variation (p. 6, l. 260).
   - The abstract defines the floor by the "drift and scatter of production and measurement".
   - *Editions.* The editions are correct and current. ISO's open deliverables data list ISO 5725-2:2025 as the third edition, published 18 December 2025, which replaces ISO 5725-2:2019. ISO 22514-2:2026 is the third edition, published 6 February 2026, which replaces ISO 22514-2:2017. The paper uses only the definition of the repeatability limit (ISO 5725-2) and the classification of time-dependent process models (ISO 22514-2).
5. **Designer-study hypotheses.** *Changed.* Sect. 6.3 now gives two testable hypotheses with their measures:
   - designers shown the guard-banded verdict accept a smaller share of wrong verdicts within the safe distance than designers shown the verdict alone, at an equal rate of right acceptances;
   - the guard band narrows the spread of that share between teams.

   Zhang et al. (2021) is discussed there, as the motivation of the second hypothesis (p. 21, l. 947).
6. **Transparency.** *Changed.* "The nearest produced setting points to the produced alternatives whose record it averages". The point is presented as an argument ("arguably"), and the worked example is no longer cited for it (p. 21, l. 924).
7. **Noise floor of the Gaussian processes.** *Changed.*
   - It is computed over the calibration alternatives only (p. 7, l. 295).
   - It binds in 97 and 99 % of the M5 and M5n fits with a sibling and in every new-setting and new-family fit (84–93 % in the pooled scopes, `dec_gp.csv`), so the near-nominal coverage comes from the quasi-replicate series rather than from the learner (p. 16, l. 715; note to Table A3).
   - The hyperparameters are maximum-marginal-likelihood estimates without hyperpriors, and the bound is expressed on the normalised scale (appendix).
8. **Simulation statements.** *Changed.*
   - The envelope varies sheet thickness and friction but not material properties (p. 7, l. 292).
   - The force-effect ratio concerns the two draw-ins (Sect. 5.2 and p. 21, l. 935).
   - For the arm angle and the dome, whose nominal is zero in both families, the drawing-nominal baseline is M1n, at 44 and 27 floors in the produced family's floor (p. 16, l. 706). The letter's 47 and 28 floors are the same distances in the new family's floor.
9. **Where the procedure sits.** *Changed.*
   - Production part approval supplies the floor but not the variants. Process development and tryout supply the sibling and new-setting relations, and a family's production history across part numbers the new-family relation (p. 21, l. 929).
   - Sampled measurement: for subgroups of five parts the model gives floors 1.1 to 2.1 times as large, with a median of 1.3, computed from the now consistent components (p. 12, l. 537).
   - Reviewer C's sharper statement is adopted: the rules decide reliably where a trial is cheapest, and none does near release-level limits where a trial is dearest (p. 21, l. 921).
10. **Other points.** *Changed.*
    - The pooled GP is described as a restricted intrinsic coregionalisation model (p. 21, l. 940).
    - Makatura et al. (2024) and Picard et al. (2025) are cited for how language and vision-language models have been evaluated on design and manufacturing tasks. Both records were checked against Crossref: Harvard Data Science Review, Special Issue 5, doi:10.1162/99608f92.cc80fe30; Artificial Intelligence Review 58(9):288, doi:10.1007/s10462-025-11290-y (p. 3, l. 109).
    - The worked example gives the widened intervals of M2, M5 and M5n, says how typical the case is and why the mid-side draw-in was chosen (p. 18, l. 817).
    - The note to Table A2 says that the between-series floor contains the lubrication effect and is close to circular for a new variant.
    - The refit paired interval of M1s against the force trend is quoted in Sect. 5.9 (+1.35 to +3.6 floors with a sibling, +8.8 to +12 for a new setting).

### Optional points

Not done, except where stated:

- **Short-series truths (C-N1).** Not done. The wording was narrowed instead (S5).
- **An interval version of M1s or M1sn (B-p10).** Not done. Once the force trend dominates the scaled simulation as a point rule (S1), an interval version of the scaled rule would no longer answer whether the simulation adds information. M2n is the interval rule without the simulation.
- **M5 in Fig. 3 (B-p6).** Done. M5 is shown from three alternatives, and the text says why.
- **Two-sided results for the wall angle (C-m11).** Not done, for length.
- **A between-build floor from the PA12 anchors (A-r8).** Sect. 6.5 gives the reason it is infeasible: eight identical anchors per build are too few for a floor within a build, and three builds give three differences between builds.
- **The scan order (C-C2).** The question is in the author's note to the dataset authors (`paper/submission/note_to_dataset_authors.md`, item 3). The note has not been sent; the paper states that the documentation gives neither the order nor the dates.
- **A capability decision on the index or a parametric quantile (C-N2).** Not done. The one-sidedness of the present test is stated instead.

### Editorial points

- **M6.** The notes to Tables 2 and 4 say "M6, a conformalised GP, is a robustness variant" and "as a robustness variant, M6". The abstract counts fourteen rules: the thirteen of the reviewed version and M1sn. M6 is not counted.
- **Abstract.** It now reads "was right for requirements over 3.4 floors from the truth", and the definitions are split into two sentences.
- **Wording.**
  - "Two points on its operating characteristics" (p. 2, l. 76).
  - The sibling is defined by "the factor varied at a fixed setting" (p. 9, l. 387).
  - Table 5 says "Before relying on a predictor".
- **Sections 5.3–5.6.**
  - Sect. 5.5 names the relation of every paired difference, including M1 at 13.5 floors further out than M1n for a new setting (p. 16, l. 693).
  - Sect. 5.3 names the interval rules (p. 13, l. 592).
  - Sect. 5.6 says "M5" (p. 16, l. 731).
- **Precision of terms.**
  - The distances are exact up to the 0.05-floor grid (p. 9, l. 369).
  - "Capability" is no longer used for the 95th percentile: Table 5 and Sect. 6.2 say "predicted 95th percentile".
  - "Measurement resolution" is used for the gauge sense and is defined in Table A1.
  - The lag ranges are averages over the two geometries (p. 12, l. 535).
- **References.** Montgomery (2019) gives Hoboken, NJ.

---

## Part 3. Corrections to the first-round response

The first-round response said more than the manuscript did in the places listed at the end of Section 6 of the letter. We regret this. Each statement is corrected below, against the manuscript as it now stands:

| The first-round response said | What was true then | What is true now |
|---|---|---|
| results are "named by their result file" | the manuscript named none | Table A5 names the script and result file of every number quoted but not tabulated |
| the requirement prior is "stated" | only its range was stated | the prior is stated exactly in Sect. 3.6, the Fig. 4 caption and Table A1 |
| the strata and the split are "in the abstract-level statements" | they were in the body (Sects. 5.3–5.4) and Table 5 only | they are in the abstract, Sects. 5.4 and 6.1, Table 5 and the conclusions |
| "concrete hypotheses" are given | research questions were given | two testable hypotheses with measures (Sect. 6.3) |
| Zhang et al. (2021) is "discussed in Sects. 6.2–6.3" | it was cited in Sect. 2.4 only | it is discussed in Sect. 6.3, with the second hypothesis |
| `alt_mrc.csv` reports ">200, beyond the interval" | the file gives the slope-based minimum resolvable change as a number, e.g. 5,613 kN for the wall angle, and no script writes such a label | unchanged file; the statement was wrong. The paper's wording ("lies beyond either force interval for the wall angle and the dome") rests on the pairwise contrasts in `rob_bhf_pairs.csv`, which agree with it |
| `panel_physical_units.csv` gives the per-characteristic distances in units | the file was quantised at 0.05 units | regenerated (S6): each characteristic is scored in its pooled floor and converted, exact up to 0.05 pooled floors |
| the DOI will be deposited "at resubmission" | the DOI was pending | the deposit is prepared, and the DOI is **[DOI to be inserted after deposit]**. The manuscript will not be resubmitted without it |
| the M1s result is "one exception" to the first version's conclusions | it did not survive the comparison with the force trend | withdrawn (S1). The first version's statement holds for the simulation used as an offset or rescaled |

---

## Part 4. Reviewer A

### New issues

**A-N1. "The rescaled simulation does not add information beyond a trend in force."** *Changed* (S1). The force-trend rule is added as M1sn, and its decisive distances reproduce yours: 3.5 floors with a sibling, 8.2 for a new setting, 4.7 interpolated and 8.9 extrapolated. Sects. 5.5 and 6.1 are rewritten, and the response's summary is corrected (Part 3). In the stratum with two resolvable siblings, the force trend decides at 4.5 floors, against 4.6 for M1s and 4.9 for the nearest setting (`panel_sibling_strata.csv`). Sect. 5.4 gives the force trend and M5 for that stratum.

**A-N2. "New-family results: unit and selective reporting."** *Changed* (S3).
- Table 4's new-family columns are in the produced family's floor.
- M3 is added to Sect. 5.3.
- "The envelope rule is the safest" is replaced by "the best rule was safe at about 16–17 floors in either floor; two transfers do not resolve which rule is safest", with the paired interval of M3 − M2 in both floors.
- The safe-distance intervals of the headline rules and the decisive-distance interval of M2 are in Table 4.

In the produced family's floor M1 is the most decisive rule (33 floors), and M3 has the smallest safe distance (17). Following the letter, no rule is named safest. The paired difference is not resolved: M3 has the smaller safe distance in 83 % of resamples in the produced family's floor and in 25 % in the new family's (`panel_source_floor_paired.csv`; the letter computed 79 % and 28 %).

**A-N3. "Step 6: the guard band depends on a requirement prior that is not stated, and its evaluation is reported for one rule only."** *Changed* (S2).
- The prior is stated exactly in Sect. 3.6 and the caption of Fig. 4.
- Its conditional status is stated in Sect. 3.6, Table A1 and Table 5.
- g is computed under the grid within ±5 and ±3 floors and the uniform priors within ±20 and ±50 (`panel_guard_priors.csv`); Sect. 5.7 quotes three of them and the worked example the fourth. Your figures reproduce, except for the uniform priors, where a step of 0.05 floors gives 0.25 rather than 0.5 floors for the nearest setting interpolating, as the letter notes.
- Table A4 covers the core rules, M3, M3n and M1sn by relation, and Fig. 4 shows interpolation and extrapolation separately.
- The space came from Sect. 5.3, as you suggested.

### New minor points

1. **Traceability and the archive.** *Changed* (S6): Table A5, and the archive cited in the paper. The DOI is to be inserted after deposit (Part 3).
2. **Short calibration series show calibration, not qualification.** *Changed.* "Rules can be calibrated on short runs, here scored against the truths and floors of the full series" (Sect. 5.6). "Rules calibrated on about 50 parts per variant scored as well as with full series" (Sect. 6.5). The note to Table A2 says that only the calibration $q_{95}$ come from the first n parts.
3. **"Within the family" in two senses.** *Changed* (S4). "With a produced sibling" is used for the sibling relation throughout. "Within a family" is kept for both within-family relations, as in Sects. 5.4, 5.6, 5.9, 6.1, 6.3 and 6.6 and the conclusions. The contradiction at the former l. 904–905 is removed with the M1s claim.
4. **Table 3 combines incompatible aggregates.** *Changed* (S5). All three quantities are classical statistics pooled over the series as root mean squares. σw is now below σLT in every row. Series by series, σw exceeds σLT in 5 of 126 alternative–characteristic cases, by at most 0.3 %, a degrees-of-freedom effect (`panel_floor_protocol.csv`).
5. **One "definitional" finding is empirical.** *Changed.* Sect. 6.1 restricts the clause to the guarantee of the distribution-free intervals. Where they fell short is an observation: interval rules held their level with a produced sibling but not when extrapolating or for a new family.
6. **Table 5: basis column and "Fixing a requirement".** *Changed.* The prescriptive block is labelled "From the framework (prescriptive; usefulness not evaluated)". The row is "Planning a requirement", stated as a heuristic, and Sect. 6.2 refers the decision itself to the guard band, since δs is defined on the true margin.
7. **Release-level requirements only with a sibling.** *Changed.* "Decided at the design stage only with a produced sibling" (Sect. 5.8, Table 5).
8. **Surrogate statement.** *Changed* (S5). The surrogate is scored as a rule (`ds_surrogate_rule.csv`), and its accuracy is given as a leave-one-out RMSE below 2 floors for 12 of the 14 characteristic–geometry pairs.
9. **Worked example.** *Changed* (S2(g)). The requirement is chosen for illustration, g was estimated on data that include the case, and the widened intervals of M2, M5 and M5n are given: 14.41–15.41, 14.23–15.61 and 14.66–15.33 mm.
10. **Table 6 and the black-box route.** *Changed* (S7). Table 6 is marked as an untested proposal. Comparability within a protocol is stated, and so is the binning estimator for fixed-threshold classifiers.
11. **Paired differences in Sect. 5.5: name the relation.** *Changed.* Every difference names its relation, and M1's 13.5 floors for a new setting is given.
12. **The 3.4-floor headline.** *Changed* (S4).
13. **Uncertainty of the headline safe distances.** *Changed* (S3). Table 4 gives δs intervals for M2, M3 and M5 and a δd interval for M2 for a new family. In the produced family's floor M2 is safe at 26 floors (9.8–32), M3 at 17 (15–19) and M5 at 31 (28–32).
14. **Designer-study hypotheses.** *Changed* (recommendation 5). The first hypothesis follows your example: guard-banded verdict against verdict alone, measured by wrong verdicts accepted within the safe distance at an equal rate of right acceptances.
15. **The error of a tryout trial.** *Changed* (S5). The trial that step 6 calls for is itself a run, so the between-run variation applies to it as well as the within-run reproducibility (Sects. 3.4 and 5.1).

### Remaining minor and editorial points

1. **"Characterised by two operating characteristics".** *Changed* to "two points on its operating characteristics".
2. **M6 in the notes to Tables 2 and 4.** *Changed* (editorial).
3. **The factor that defines a sibling.** *Changed* (Sect. 3.5).
4. **The cost sentence.** *Changed* (recommendation 3). `scen_cost_map.csv` is named in Table A5, and the six failing alternatives near the limit are stated.
5. **Fig. 4.** *Changed* (S2(f)).
6. **The new-family robustness rows.** *Changed in substance.* "The envelope rule the safest for a new family" is removed. Table A2 keeps M2 and M5 for a new family, in the new family's own floor, as the note says. The robustness variants refit the whole pipeline, and their reference row in that floor (51/16 and 38/28) makes the variants comparable with each other. The produced-family values are in Table 4.
7. **What the floor adds to the repeatability limit r.** *Changed* (Sect. 2.5): "what is new is its use not to judge whether two results agree but as the unit in which a design decision rule is scored and its guard band set".
8. **PA12 builds (optional).** Answered in Sect. 6.5: three builds, eight anchors per build, a between-build floor infeasible.
9. **"Before relying on a predictor".** *Changed.*
10. **Transparency as an argument.** *Changed* (recommendation 6).
11. **Editions and Montgomery.** Checked (recommendation 4); Montgomery's place is given.
12. **Cut the numbers in Sect. 5.3 that repeat Table 4.** *Changed* (recommendation 2).
13. **Split the abstract's first definitional sentence.** *Changed.*

---

## Part 5. Reviewer B

### New issues

**B-N1. "The guard band of step 6 depends on an unstated requirement prior and on a 20-floor cap."** *Changed* (S2).
- The prior is stated exactly, with the reason it represents the requirements a team faces.
- g is reported under four further priors, including the uniform ones within ±20 and ±50 floors. The step-6 distances and trial rates under the reference prior are in Table A4.
- The unqualified rules are named for each relation, and the new-family statement is qualified as a consequence of the prior and the cap.

*The cap.* It marks where a band stops being of use. The uncapped bands are in `panel_guard_priors.csv` (`guard_band_uncapped`): 23.25 and 23.0 floors for M2 and M5 extrapolated, and 41.75, 42.25 and 42.25 floors for M2, M3 and M5 for a new family in the produced family's floor. Widened by these bands, the rules send 94–100 % of the verdicts at requirements 10 floors from the truth to trial and 82–100 % of those at 20 floors (recomputed from `dec_intervals.csv` with `panel.guard_band`). They decide almost nothing within the range of requirements that the reference prior covers. Your 28.5 and 33.25 floors reproduce exactly in the new family's own floor, as do the letter's 3.75 and 11.75 floors under the uniform prior within ±50.

*A prior-free g.* The letter accepts either route, and we took the first. The smallest widening for which the widened rule's safe distance is zero answers a different question: it bounds the worst error at every true margin, whereas the designer conditions on the observed margin. It is a natural extension for a team without a prior.

*Asking the team for its prior.* Step 1 frames the form of the requirement, and Sect. 3.6 and Table 5 now ask for the distribution of requirement distances the team expects. Your uniform-prior figures reproduce up to the grid step, as the letter notes.

**B-N2. "Much of the evidence behind RQ3 is no longer in the paper."** *Changed* (S6).
- Table A3 gives coverage, median half-width and the centre's decisive distance for every interval rule by relation, with the share of GP fits at the noise bound in its note.
- Table A4 gives g, the step-6 distances and the trial shares at 10 and 20 floors.
- Guard performance has a sentence: 96 % of the range guard's refusals for a new setting would have been right for the nearest setting and 72 % for M5.
- The paired refit comparisons are quoted for M1s and the force trend. The others are in `rob_refit_paired.csv`, which Table A5 names.
- One-sided distances: Table 4 gives the false-accept side, and Table A5 names `dec_resolution.csv` for both sides.
- The archive is cited (DOI to be inserted after deposit).

**B-N3. "The headline statements still overreach in five places."** *Changed.*
- (a) S1. Following the letter, the direction is the opposite of your suggestion: the body is corrected, and the abstract keeps "helped only across families" with "offset or rescaled". Rescaled, the simulation improved on the median of the produced alternatives (4.2 floors), and Sect. 5.5 attributes this to the force level.
- (b) S4: the interpolated and extrapolated split, with 100 and 500 kN, wherever the new-setting figure is quoted.
- (c) S4: coverage by relation.
- (d) S4: "except a near-replicate's", for indices up to 1.33; Table 5 no longer contradicts itself.
- (e) S3: the unit is stated, and both floors are given.

**B-N4. "The refit bootstrap preserves the relation but degrades the design."** *Changed* (S5). Sect. 4.4 describes the configurations, the duplication and its consequences, including the single distinct sibling and the five distinct calibration alternatives; the note to Table A2 refers to it. The appendix says that the noise floor is not restricted to distinct series. The letter made recomputation optional, and the ranking holds in all 48 configurations. The missing pair is supplied in the form the letter asked for: M1s against the force trend, with a refit interval of +1.35 to +3.6 floors with a sibling and +8.8 to +12 for a new setting (`rob_refit_paired.csv`). The M1s–M1n pair is not added, since the letter supersedes it. The all-subsets design of Fig. 3 is reported by relation, but not as a substitute for the refit intervals.

**B-N5. "The jackknife+ guarantee is overstated."** *Changed* (S5): 1 − 2/(n+1), 0.71 to 0.80, approximate under median centring; median-centred with extreme order statistics in the appendix; empirical coverage 96 % and 89 %.

**B-N6. "Say how the GP noise floor is computed, and what it implies."** *Changed* (recommendation 7):
- no leakage: the bound is computed over the calibration alternatives' series;
- the bound binds in 97–100 % of the fits outside the pooled scopes and in 84–93 % within them;
- the near-nominal coverage comes from the quasi-replicate series;
- the minimal report asks for the source of the noise variance (item 3);
- ML-II without hyperpriors, and the bound on the normalised scale.

**B-N7. "Sect. 6.1 mislabels one finding and overgeneralises another."** *Changed* (S4). (a) The exchangeability clause is restricted to the distribution-free guarantee. (b) "With a produced sibling" is added. The interval centres of M3 and of all learned rules for a new setting are in Table A3.

**B-N8. "Two key terms are used in two senses."** *Changed* (S4).

**B-N9. "The transparency argument misdescribes the nearest produced setting."** *Changed* (recommendation 6).

**B-N10. "The surrogate contrast is one unsupported sentence."** *Changed* (S5). It now has one clause of method: a GP over force, friction and thickness, with its leave-one-out RMSE against the simulation. It is scored as a rule in place of the simulation: M0 at 109 against 108 floors, and M1 with a sibling at 15 against 15 (`ds_surrogate_rule.csv`).

### Remaining minor and editorial points

1. **Make the black-box formulation operational.** *Changed* (S7), in about half a page as the letter set: classifiers, language-model checks, continuous relations and generative tools.
2. **Minimal report as a numbered checklist.** *Changed.*
3. **AI-for-DFM references.** *Changed.* Makatura et al. and Picard et al. are cited in Sect. 2.1, in their published versions (2024 and 2025).
4. **Hypotheses.** *Changed* (recommendation 5). Your example is close to the first hypothesis. Zhang et al. motivates the second.
5. **The multi-task statement.** *Changed* (recommendation 10).
6. **M5 at two alternatives.** *Changed*: M5 is shown from three alternatives, and Sect. 5.6 says "M5".
7. **Abstract wording "decided within 3.4 floors".** *Changed.*
8. **Number of rules.** *Changed* (editorial).
9. **The cost sentence.** *Changed* (recommendation 3).
10. **An interval version of M1s (optional).** Not done; see the optional points in Part 2.

---

## Part 6. Reviewer C

### Open points under the first-round comments

**C-C1 (i) Table 3.** *Changed* (S5).

**C-C1 (ii) Intermediate precision; editions.** *Changed* (recommendation 4).

**C-C1 (iii) Assumption A2.** *Changed*: "the variation within the runs from which it is estimated is like that within future runs".

**C-C2. Scan order; "and measurement" in the abstract.** The abstract now reads "drift and scatter of production and measurement". The question on scan order and dates is in the unsent note to the dataset authors (Part 2, optional points).

**C-C3. The capability-anchored test; the trial's error.** *Changed* (S4 and S5).

**C-C4. The headline in stratified terms.** *Changed* (S4). Following the letter, the stratified figures are given wherever 3.4 floors and the new-setting figure appear, and your reading is offered as an observation in Sect. 5.4: the nearest setting decided at about 5 floors whenever the new design differed resolvably and force and speed did not change together. The caveat is attached: each stratum has 34 to 58 cases, and each distance rests on a handful of verdicts. Sect. 6.6 says "the extrapolation to 100 kN". The smaller point (the drawing nominal for the arm angle and the dome is M1n) is in Sect. 5.5 (recommendation 8). Note that the force trend decides at 8.9 floors at both extrapolated forces, so the 4.9 floors at 500 kN is the nearest setting's.

**C-C5. (a) Material properties; (b) the two draw-ins; (c) "as an offset".** *Changed* (recommendation 8 and S1). For (c), the letter overrules the direction (Part 4, A-N1).

**C-C6. (a) Short runs.** *Changed* (S5). **(b) Production part approval.** *Changed* (recommendation 9), with the evidence relation each source supports. **(c) Sampled measurement.** *Changed*: subgroups of five give floors 1.1 to 2.1 times as large, median 1.3.

**C-C7. Suggestions for Table 6.**
- (a) Injection moulding: the floor is taken per cavity, with cavity offsets as effects. Set-up and material lot are listed as variation. They are not named in the table as the excluded between-run component; the text's statement on between-unit floors covers them.
- (b) Machining: "batch centres within an offset interval".
- (c) The two further columns: not added, for length.

**C-C8. The sharper practical statement.** *Changed* (Sect. 6.2; recommendation 9).

### New issues

**C-N1. "The short-series analysis truncated only the calibration side."** *Changed* by narrowing the wording (S5); the repeat with short-series truths was optional and is not done. Sect. 5.6 now also gives the correct bound: 1.5 floors within a family, including the interpolated and extrapolated cases, and 4 for a new family.

**C-N2. "The capability-anchored test scores only one side."** *Changed* (S4):
- (a) The one-sidedness is stated. The positions (1.0, 1.7, 2.5 and 3.1 floors) are the result, and the shares are given as right/false-reject/trial rates.
- (b) "Decided at the design stage only with a produced sibling".
- (c) Sect. 3.1 is softened.
- The two-sided capability decision is left open (optional).

**C-N3. "The new family is qualified in one floor and decided in another."** *Changed* (S3).

**C-N4. "Table 3 combines different summaries."** *Changed* (S5). One summary is used for all three quantities, and the statistics are labelled classical. The force dependence of the part scatter is not added to the table note, for length. It shows in the drift and between-series results.

**C-N5. "Numbers no longer tabulated have no reference a reader can follow."** *Changed* (S6): Table A5 and the cited archive. The DOI is to be inserted after deposit.

**C-N6. "The guard bands exist only in one sentence."** *Changed* (S2). Table A4 shows that M2 and M5 never qualify for an extrapolated setting under the reference prior. M5n, M3n, M1sn and the nearest setting qualify at 6.0–7.0 floors, and M3 at 16.75. The new-family statement is conditioned on the prior, with the die-tryout practice you describe.

**C-N7. "The relation-specific cost comparison rests on the gross-failure scenario."** *Changed* (recommendation 3). The coarseness and the tie are stated.

**C-N8. "The result file cited for distances in physical units is quantised."** *Changed* (S6). For the waviness with a sibling, the nearest setting is now listed at 0.0032 mm (1.15 pooled floors), not 0.05 mm.

### Remaining minor points

1. **"Within a family" in two senses.** *Changed* (S4).
2. **Note to Table A2: the between-series floor.** *Changed*: it contains the lubrication effect and is close to circular for a new variant.
3. **Lag ranges.** *Changed*: averages over the two geometries. The per-geometry ranges are in `panel_variogram.csv`.
4. **"The distances are exact".** *Changed*: up to the 0.05-floor grid.
5. **"Capability" for the 95th percentile.** *Changed*: "predicted 95th percentile" in Table 5 and Sect. 6.2.
6. **"Resolution" in the gauge sense.** *Changed*: "measurement resolution", defined in Table A1.
7. **Worked example: typicality and the choice of characteristic.** *Changed.*
   - Typicality: at 8.5 floors above the truth, step 6 with the nearest setting is right in all 42 interpolated cases.
   - The choice of characteristic: the mid-side draw-in is the characteristic by which tryout sets the blank-holder force. Its measurement resolution, 0.38 floors (Sect. 4.3), is small against the example's margin of 6.2 floors.
8. **`alt_mrc.csv`.** The response was wrong (Part 3). The file is unchanged.
9. **M6.** *Changed* (editorial).
10. **Name the interval rules in Sect. 5.3.** *Changed.*
11. **Two-sided results for the wall angle (optional).** Not done.
12. **"Except that of a near-replicate sibling".** *Changed* (S4).

---

## Part 7. Provenance of the new numbers

Every number below is written by the released pipeline (`scripts/run_all.sh` runs the scripts in order). The tables are generated by `scripts/make_tables.py` and the figures by `scripts/figs.py`.

| Number | Script | Result file |
|---|---|---|
| Force-trend rule M1sn: intervals and distances (Table 4) | `decisions.py` (rule `M1sn`) | `dec_intervals.csv`, `dec_resolution.csv` |
| M1s − M1sn with fits fixed: +1.35 (+0.65 to +2.95) with a sibling, +11.0 (+5.3 to +13.8) for a new setting | `decisions.py` | `dec_paired.csv` (rows M1s/M1sn) |
| M1s − M1sn with refitting: +1.35 (+1.35 to +3.60), +11.0 (+8.8 to +12.05); share with M1s more decisive 0 | `robustness.py` | `rob_refit_paired.csv` |
| M1sn in the strata (4.45 floors with two resolvable siblings) and by force level (8.85 at 100 and 500 kN) | `panel.py` | `panel_sibling_strata.csv`, `panel_force_levels.csv` |
| Decomposition with and without M1sn, in both floors | `panel.py` | `panel_decomposition.csv` |
| Guard bands under the reference and four further priors, capped and uncapped | `panel.py` (`guard_priors`) | `panel_guard_priors.csv` |
| Table A4: g, step-6 distances and trial shares by relation | `panel.py` (`step6`); `make_tables.py` | `panel_step6.csv` |
| Fig. 4: share correct by margin, the new family in the produced family's floor | `panel.py`; `figs.py` | `panel_step6_curves.csv` |
| Table A3: coverage, half-width and centre by relation; the new family in the produced family's floor | `decisions.py`; `make_tables.py` (new-family column from the stored intervals) | `dec_coverage.csv`, `dec_intervals.csv`, `dec_gp.csv` |
| New family in the produced family's floor: distances, intervals and paired differences (M3 − M2 safe: −9.3, −16.1 to +6.9) | `panel.py` (`source_floor`) | `panel_source_floor.csv`, `panel_source_floor_paired.csv` |
| Fig. 2, new-family row | `panel.py`; `figs.py` | `panel_source_floor_curve.csv` |
| Table 3: consistent aggregates; σw against σLT per series; subgroups of five | `panel.py` (`floor_protocol`); `make_tables.py` | `panel_floor_protocol.csv` |
| Capability-anchored rates (right/false reject/trial) | `panel.py` (`capability`) | `panel_capability.csv` |
| Distances in physical units (regenerated) | `panel.py` (`physical_units`) | `panel_physical_units.csv` |
| Drawing-nominal baseline (1.9 against 7.5 floors) and M1n for the arm angle and the dome (44 and 27 floors) | `panel.py` | `panel_nominal_offset.csv`, `panel_source_floor.csv` |
| Surrogate scored as a rule | `design_space.py` | `ds_surrogate.csv`, `ds_surrogate_rule.csv` |
| Short calibration series (at most 1.5 floors within a family, 4.0 for a new family) | `robustness.py` | `rob_decisions.csv` |
| $q_{95}$ unit, including M1sn | `panel.py` (`q95_unit`) | `panel_q95_unit.csv` |
| Oil-film medians of the series (Sect. 4.1) | `panel.py` (`run_metadata`) | `panel_runs.csv` |
| Guards, including M1sn (refusal rates unchanged: 96 % for the nearest setting, 72 % for M5) | `guard.py` | `dec_guard.csv` |
| Gaussian-process specifications: at most 1.2 floors (decisive), 2.1 (safe) | `robustness.py` | `rob_decisions.csv` |

---

## Part 8. Versions, archive and declaration

- **Clean manuscript:** `paper/main.pdf`, 30 pages, with line numbers. The upload zip is `paper/submission/manuscript_source.zip`, built by `paper/submission/make_zip.sh`, which compiles it in an empty directory.
- **Marked-up version:** `paper/review/cfp_panel/round2/main_diff.pdf`, against the second-round manuscript.
- **Archive.** The deposit will hold exactly the code, the feature tables and the result files of this version. Its metadata are in `.zenodo.json`. The DOI is **[DOI to be inserted after deposit]**. It will replace the placeholder in `canseven2026archive` (`paper/refs.bib`) before resubmission.
- **Declaration on generative AI.** The declaration is kept. It already covers the assistant's role in this revision: code development, data analysis, drafting and editing, and simulated peer review of earlier versions.

Yours sincerely,

Hüseyin Tayyer Canseven
