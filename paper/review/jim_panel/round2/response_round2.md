# Response to the editor and the reviewers, second round

**Manuscript:** "When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing", by Hüseyin Tayyer Canseven
**Journal:** Journal of Intelligent Manufacturing
**Answers:** the decision of 24 October 2026 (minor revision: required changes C1–C11, the ruling on length and supplementary material, and the conditions for acceptance) and the second-round reports of Reviewers 1, 2 and 3
**Revision of:** the version considered in the second round (frozen as `paper/review/jim_panel/round2/main_reviewed.tex`)

> **Note on this document.** The decision letter and the three reports it answers were written by AI agents acting as a simulated review panel; they do not come from the journal, its editors or its reviewers. The response is written as it would be to a real editor. Items that only the author can complete before a real submission are marked **[author]**: the licence and the DOI of the archive, a timestamped registration of the procedure, and the request to the dataset providers.

**Locations.** Page and line numbers refer to the revised manuscript, `paper/main.pdf`, compiled with line numbers. Tables, captions and figures carry no line numbers and are named. Tables S1–S15 are those of Online Resource 1 (`paper/online_resource_1.pdf`). The version marked up against the reviewed manuscript is `paper/review/jim_panel/round2/main_diff.pdf`; latexdiff shows the regenerated tables in their new form.

**Length and Online Resource 1.** The revised paper has 31 pages, including the declarations and the references (31 before), and its main text ends on page 27 (27 before), as your ruling requires. Online Resource 1 is restored as electronic supplementary material, not as an appendix: 15 tables on 16 pages, captioned in the paper's terms, each naming its result files and each cited where the text uses it as "Online Resource 1, Table Sn". It holds the ten groups of your ruling and nothing else:

| Ruling | Online Resource 1 |
|---|---|
| 1. all rules by relation, Mcd included | S1 (with a new family in both floors) |
| 2. GP diagnostics with the M7n prior sensitivity | S5, S6 |
| 3. the crossing, with the pooled trend GP | S7 |
| 4. coverage by relation, family, characteristic and stratum | S8, S9 |
| 5. both distances per characteristic (R9) | S2 |
| 6. the simulation against the measurement, with the extraction noise (R4) | S3 |
| 7. scan redundancy per series (R5) | S4 |
| 8. decision-time guard bands by scheme and prior, against the prior's width, per characteristic | S10, S12, S11 |
| 9. costs by prior, c_FR and c_T | S13 |
| 10. between-run sensitivity with the trial rows; the cross-fits | S14; S15 |

To pay for C1–C9 within the same length, numbers moved from the main text to Online Resource 1 or stay in the archive, notably from the paragraphs you named: the second paragraph of Section 5.4 lost the conformal margin of M6, the two-task GP and the list of model-based rules, and Section 5.7 the selection by decisiveness per relation, which Table S15 holds. Smaller moves: the GP hyperparameters to S5, the simulation's per-characteristic advantage when extrapolating to S2, the dome levels to S3, the requirement grid and the round-by-round development record to the Online Resource's text, and the stratified distances of the force trend and M5 to the archive (`qual_strata.csv`). Four figures were drawn slightly smaller from unchanged data.

**Archive.** Version 3 of the archive holds every script and result file of this revision. `RELEASE_NOTES.md` lists what was added and changed and gives the checksums of the main new result files; `SHA256SUMS` covers every script and result file. The result files of version 2 are unchanged except `qual_coverage.csv` (columns added, coverage values unchanged) and four redrawn figures. New: `results/DATA_DICTIONARY.md` (C10), `results/findings.md` with the current numbers only and `results/findings_history.md` with the superseded ones (C10), and a self-check of `scripts/opchar.py` that reproduces the decision-time guard bands. Licence and DOI: **[author]**.

Dear Editor,

Thank you for a decision that names, for each point, what would satisfy it, and for checking the reports against the archive yourself. Your checks were right on every point. The revision follows C1–C11 and the ruling. In brief:

- **RQ3 (C1–C3).** The safety for new settings is credited to the evidence borrowed from the other family on the same relation, with the three like-for-like comparisons in Section 5.4 and the crossing in Table S7. The relation-matched intervals are described as carrying no guarantee, with their level labelled nominal and their coverage given per family and characteristic. The trend GP's intervals are explained, its priors are tested, and M7's failure is reported and counted.
- **The part a factory would deploy (C4, C5).** Table 7 now gives the guard band a team has when it decides (the family's own band with a sibling, the other family's for a new setting), validated by the matching scheme under both priors; step 5 says what happens when a family's production cannot exercise a relation; the worked example uses only what the planner knows.
- **Messages to practitioners (C6–C8).** The simulation finding rests first on comparisons that depend on neither the assumed blank nor the scales; release is treated as a capability decision; the trial joins the between-run sensitivity; the costs set the band in step 5 and the cost statements are restricted to those that hold under both priors and all cost ratios.
- **Reporting (C9–C11).** Both cross-fits are reported, "committed to in advance" and "bounds" are replaced, Online Resource 1 and the data dictionary are in place, and every correction of detail is made.

Three new analyses were run from the stored results with the released code, as you asked: the prior sensitivity of M7n, the trial under between-run variation and the decision-time guard bands; three more follow from them (the trial's own error cost, release scored on m̄ + 4σ, and the worked example). Part 1 takes C1–C11 in turn, Part 2 the recommended changes, Part 3 your qualifications and Part 4 the conditions for acceptance; Parts 5–7 answer every point of the three reports, and Part 8 lists the numbers that changed.

---

## Part 1. Required changes C1–C11

### C1. Credit for the safety for new settings

- **The claim** now names the evidence. Abstract: "Borrowing the other family's errors on the same relation, not learning, made the production record safe for new settings" (p. 1, l. 37). Section 6.1: "what made rules safe for new settings was evidence borrowed from the other family on the same relation" (p. 23, l. 1030). Conclusions: "evidence borrowed from the other family on the same relation, not learning, made it safe for new settings" (p. 26, l. 1196).
- **Section 5.4 states the three results** (p. 19, l. 871):
  - around the trend GP and force-trend centres, the same interval decides closer when extrapolating (17.6 and 17.8 against 20.1 floors) (p. 20, l. 897);
  - around simulation-based centres it does not make the rule safe, with false accepts up to 151–155 floors (p. 20, l. 898);
  - a trend GP calibrated on both families, borrowing through a family term, is safe at 2.75 floors (p. 20, l. 899). As your first qualification asks, the text does not reverse the finding: NN+RM remains the safest rule for new settings (safe below one floor).
- **The crossing** of the eight predictors with the relation-matched interval, plus the trend GP on both families, is Table S7, with each rule's own interval alongside.
- **The interval-score sentence** is limited to production-record and trend centres (p. 20, l. 902); Table S8 gives every score, including the 76–155 around M1s and M7.

### C2. No coverage guarantee for the relation-matched intervals

- **Section 3.3** now says that the cases behind a quantile come from one family and from one or a few shared fits, are not exchangeable with the other family's cases, and that the interval carries no coverage guarantee, citing Barber et al. (2023) (p. 7, l. 305); "its 90 % is nominal" (p. 7, l. 306).
- **Table 2** labels the level of every GP and relation-matched interval "nominal 0.9".
- **The cases behind each quantile** are given: 21 (interpolated), 42 (extrapolated) or 63, all from one family (p. 7, l. 303). `qual_coverage.csv` now carries the number of borrowed cases and the quantile per family (`rm_n`, `rm_quantile_floors`).
- **88 and 93 %** are described as the results of two family swaps, not of a guarantee, with their range in the text: 73–100 % between the families and 61–100 % between characteristics (p. 20, l. 900); Table S9 gives coverage per family, characteristic and decision-time stratum.
- **The jackknife+ guarantee** cites Barber et al. (2021) in Section 3.3 (p. 7, l. 316); the 0.78 in Section 5.4 is that guarantee (p. 20, l. 906).

### C3. The trend GP's intervals, its priors and M7

- **Why M7n's intervals undercover.** Section 5.4: they cover only 52 % interpolating and 56 % extrapolating (17 and 33 % on the mid-side draw-in, none on the waviness), "because their width is learned from the variation between lubrication patterns at produced forces, sibling-type information" (p. 19, l. 861). The force length scale staying near the prior's 200 kN, which two force levels cannot inform, is stated just before (p. 19, l. 855).
- **Prior sensitivity.** `learners.py --prior-sensitivity` refits M7n with each of its four prior medians halved and doubled, one at a time (Table S6; `learn_m7n_priors.csv`; the reference variant reproduces the stored fits exactly). One sentence in the text: halving or doubling any median moves the decisive distances by at most 1.4 floors, keeps M7n within 0.4 floor of the force trend and its coverage for a new setting at 48–62 % (p. 19, l. 862). No conclusion changes.
- **M7 as it behaves here.** Section 3.3: "with two calibration forces its scale on the simulation acts as a force slope" (p. 7, l. 298); Section 5.3 reports its false accepts up to 118 floors on the cup depth next to M1s's 165 (p. 17, l. 772); Section 6.1 repeats both (p. 23, l. 1033).
- **M7 is counted:** "Besides M7, ten further rules complete the comparison" (p. 7, l. 309); Online Resource 1 lists it among the rules added in the fifth simulated round.

### C4. The guard band a team has when it decides

- **Table 7** now gives the band available at decision time (`qualify.guard_decision_time`; `qual_guard_decision.csv`):
  - with a sibling, the family's own band from its sibling cases, validated leaving one alternative out within the family;
  - for a new setting, which a family produced at two forces cannot exercise, the band of the same relation in the other family, applied to this family and so validated out of family.

  Bands are per family (concave/convex), under both priors, with the share correct among decided verdicts and the trial rate; Table S10 adds the cluster intervals (sibling), the numbers of decided verdicts and of all verdicts, the worst characteristic, and the share with the family's own band estimated without the held-out force cell. Your own check reproduces: NN keeps 0.951 interpolating and 0.952 extrapolating under the reference prior and 0.75 extrapolating under the release-like prior.
- **Step 5** says what happens when a family's production cannot exercise a relation: it "borrows the band of the same relation in another family, with the caveat of Section 3.3, or sends the design to trial" (p. 10, l. 438). Table 8 ("Deciding a single design") and Table 9 ("decision-time, two priors") match.
- **Section 5.5** reports (p. 20, l. 914):
  - the release-like failures with a force cell left out: NN 0.72 and NN+RM 0.74 extrapolating, M5 0.88 and M7n 0.87 interpolating (p. 21, l. 930);
  - the worst characteristics under the decision-time band: 89 % on the dome with a sibling, 88 % on the waviness interpolating, 85 % on the cup depth extrapolating (p. 21, l. 921);
  - that the bands are within-run: with τ = 3 floors the pooled bands of NN grow from 0.25, 2.0 and 7.0 to 2.9, 4.0 and 8.9 floors (p. 21, l. 923).
- **Band and trial rate against the prior's width** are Table S12 (within ±3 floors NN with a sibling needs 8 floors and sends 99 % of the verdicts to trial).

### C5. The worked example with what the planner knows

Section 3.7 is rewritten (p. 10, l. 454); every number is in `qual_worked_example.csv`:

- the floor of the six produced series, 0.041 mm (p. 10, l. 458);
- the resolvable force change from the two produced levels, about 40 kN (mean secant 39.8 kN; 37–45 kN per pattern) (p. 11, l. 462);
- the convex family's interpolation distance and band, 5.3 and 2.5 floors, with the statement that this family was produced at all three forces and the exchangeability caveat ("assuming that the two families err alike") (p. 11, l. 465);
- the trial cost as C8 defines it: the stated cost of a twentieth of a false accept widens the band to 5.0 floors (p. 11, l. 467);
- the quantisation of the mid-side draw-in: steps of 0.019 mm, three values holding a median 89 % of a series (p. 11, l. 461).

The release survives with a margin of 7.4 floors; the trend GP agrees at 5.4 floors, the truth lay 10.0 floors below the limit, and a forward reference to Section 5.5 says how often such verdicts are right.

### C6. Simulated against measured levels, conditional on what is assumed

- **The blank.** Section 4.1 says the blank is "taken as 210 mm wide, the blank of the simulation dataset", and gives the sensitivity: 1 mm of width moves the measured draw-in by 0.5 mm, 10 floors (p. 11, l. 482); Section 4.3 gives that of a 1 % lateral scale error (0.9 mm, 18 floors) (p. 12, l. 533).
- **What the simulation finding rests on.** Section 5.2 now leads with the comparisons that depend on neither the blank nor the scales (p. 16, l. 716): a force effect 2.7–5.1 times too large, a concave wall angle that falls by 1.5° in simulation but not in production, concave arms that bend the other way, and a reversed dome ranking. The level comparisons (11 of 42, the draw-in gaps, the censored Mc) follow as conditional: "The levels, which depend on blank and scales, disagree as well if both hold" (p. 16, l. 723).
- **"Partly fitted to the simulation"** is explained in Section 4.3: the line spacing was estimated from the scans and corrected by a fit of the simulation's scale, which the corner draw-in, the arm angle and the dome use and the mid-side draw-in, the wall angle and the depth do not (p. 12, l. 530).
- **The depth offset** is corrected (p. 17, l. 744): a 1 mm shorter drawing depth moves the wall at 15 mm depth by only 0.2–0.4 mm, a scale error would give an offset proportional to the radius, not 2.0–2.2 mm at both, and another tool geometry fits best but is unconfirmed.
- **Extraction noise** of the simulated characteristics is in Section 4.2 (p. 12, l. 518) and Table S3.
- **Details.** "Reaches" is replaced: the simulated draw-in comes within 0.011 mm of the measurement at 300 kN only at the edge of the grid (p. 16, l. 727) (the recomputed gap at μ = 0.15 is 0.0111 mm). The corner gap is given at both frictions, 2.6–3.5 mm at 0.10 and 1.3–3.3 mm at 0.15 (p. 16, l. 728). "Calibrated" in Section 6.3 becomes "a friction-fitted (censored) or rescaled simulation" (p. 23, l. 1056).

### C7. Release-level and trial messages

- **Release as a capability decision.** Section 5.6: "Release, however, asks whether the index is at least 1.33, a decision on m̄ + 4σ" (p. 21, l. 960). Scored on it, NN needs 3.35 floors with a sibling and 10.55 extrapolating, so it confirms an index of 1.33 only for designs whose true within-run index is 2.1–3.3 with a sibling and 3.8–7.4 extrapolating (`qual_release_capability.csv`).
- **The trial joins the between-run sensitivity.** Perturbed as the rules' truths are, the 20-part trial decides at 2.1, 3.6 and 5.1 floors for τ = 1, 2 and 3, the nearest setting with a sibling at 3.45, 4.45 and 5.75 (p. 21, l. 963) (Table S14; `qual_between_run_trial.csv`; the 50-part trial in the file).
- **Table 8, Section 6.2 and the conclusions** say that near release level neither a prediction nor a short trial decides once runs differ by a floor or more, so the evidence must come from replicated runs (p. 22, l. 987); Section 6.2 (p. 23, l. 1044); conclusions (p. 26, l. 1188).
- **Section 6.2** gives the release-like figures next to the reference ones (of 100 verdicts on extrapolated settings, 58 sent to trial under the reference prior and 92 under the release-like prior) (p. 23, l. 1044), and "the few close ones" is dropped.
- **"Bounds its effect"** is now "explores its effect" (p. 26, l. 1163).

### C8. Costs in the procedure, labelled as in-sample

- **Step 5:** "Stated costs may only widen the band, to the one minimising Eq. (2) over the prior, so they never lower the share correct below 95 %" (p. 10, l. 440); the pseudocode raises g accordingly (p. 10, l. 448). Step 6 applies the cheapest qualified rule when costs are stated. The worked example follows (band 2.5 widened to 5.0); `opchar.cost_band` is the stand-alone version.
- **Section 5.6** says that the cost bands are chosen in sample and pooled over the families (p. 21, l. 947) and keeps only statements that hold under both priors and all three cost ratios, as stated at its start (p. 21, l. 938) (Table S13; `qual_cost_cheapest.csv`). Differences of thousandths of a false accept are called unresolved (p. 21, l. 942). The new-family statement is qualified: trying every design is the cheapest up to a twentieth of a false accept, beyond which the cheapest rule changes with the prior and the cost ratio (p. 21, l. 945).
- **Fig. 6** says in its caption that trials are priced as error-free and that its band search runs to 40 floors; the text gives the 20-part trial's own error cost, 0.017 of a false accept per verdict (0.037 under the release-like prior), against NN's whole 0.018 with a sibling at a trial cost of 0.05 (p. 21, l. 952) (`qual_trial_cost.csv`).
- **Failing designs and the source of the trial-cost claim.** The text states that both priors place 47 % of the verdicts on failing designs (p. 21, l. 955) and calls the lower cost of a trial of a new force on an existing tool an assumption (p. 21, l. 949).

### C9. Selection, reported completely

- **"Committed to in advance"** is replaced by "one rule for every relation" in the abstract (p. 1, l. 34) and the conclusions (p. 26, l. 1185), and by "a production-record rule applied to every relation" in Section 6.1 (p. 23, l. 1023).
- **"Bounds" becomes "estimates"** in Section 4.5 (p. 14, l. 631) and in the threats (p. 26, l. 1173).
- **Both cross-fits** are in Section 5.7 and Table S15 (p. 22, l. 999): selected for safety, a rule is safe on the other geometry only at up to 18 floors interpolating and 11 extrapolating; rule and band selected together keep 0.92–0.97 of the decided verdicts correct within a family, below 0.95 in four of six cases, and 0.73 for a new family.

### C10. Online Resource 1 and a readable archive

- **Online Resource 1** follows your ruling (table above); the main text did not grow beyond page 27. The "Supplementary information" section points to it (p. 27, l. 1204).
- **Data dictionary.** `results/DATA_DICTIONARY.md`, written by `scripts/data_dictionary.py` from the headers of the result files, translates columns, scopes and rule codes into the paper's terms (`within` = sibling, `transfer` = new family, M4 = M3n, `resolution_floors` = δd, `safe_failing` = δs on the false-accept side) and names the floor each file uses. One point it makes explicit: in `dec_*` and `learn_*` files the new family is scored in its own floor, while the paper's reference, the produced family's floor, is in `panel_source_floor.csv` and `learn_source_floor.csv` (and in every `qual_*` file). The Code availability statement names it (p. 27, l. 1224).
- **`findings.md`** now holds only the current numbers, the map of the paper and of Online Resource 1, and the computation details; the superseded sections are in `findings_history.md`.

### C11. Corrections of detail

- **Cluster intervals** with a sibling span 0.72–0.94 (p. 20, l. 905). For M3 the recomputed file gives 0.929–0.984, which the text prints as 0.93–0.98; the cluster bootstrap now draws from a stream that the added per-family subsets changed, which moves bounds by at most one alternative in 18.
- **M0 without the held-out series** moves by 3.75 floors (p. 22, l. 1012).
- **Of 100 verdicts with a sibling**, the nearest setting with the decision-time band sends 2 to trial and gets 92 to 95 of the other 98 right (share 0.954, 0.936–0.971) (p. 23, l. 1042).
- **The few-shot distances** are said to be in the floor of the new family's nine runs, which a team with one to three alternatives does not have (p. 20, l. 910); the corresponding claim in Section 6.5 is removed.
- **Table 6 note**: the bracketed values are "the decisive distance computed in the unit, every case scored in the pooled floor (not the distance in floors times a floor)".
- **A3** "holds for repeatability and, except for the mid-side draw-in, for resolution" (p. 15, l. 670).
- **The drift bound** is given in floors: below 0.05 %, about 0.9 floor of mid-side draw-in (p. 15, l. 679).
- **Table 5** has an Mcd row.
- **Conclusions:** "a guard band validated for an assumed prior of requirements" (p. 26, l. 1181).
- **`qual_coverage.csv`** gives cluster intervals only with a sibling; a `ci_note` column says why the others are absent (the alternatives of a held-out cell share one fit) and flags the 26 degenerate sibling intervals (subsets in which every resample gives the same share).
- **Friedman (2001)** is cited for gradient boosting (p. 7, l. 315).

---

## Part 2. Recommended changes

- **R1, marginalise M7n's hyperparameters:** not adopted. Its decisive distances move by at most 1.4 floors over a fourfold range of each prior median (Table S6), so marginalising would not change a conclusion.
- **R1, a normalised nonconformity score:** not adopted as a new rule. M6 is such a construction around M5's centre, and it costs ten floors of decisiveness (Table S8).
- **R1, the finite-sample paragraph:** adopted as one sentence: no interval from n exchangeable cases promises a miss rate below 1/(n+1), so a guaranteed 5 % needs 19 produced alternatives in a relation (p. 7, l. 307).
- **R1, cite conformal risk control and "learn then test":** not adopted, for length. Their finite-sample risk guarantees need exchangeable calibration cases, which the few shared fits of a family do not give; the paper says so for the relation-matched intervals.
- **R2, an m̄ + 5σ variant:** not adopted. The m̄ + 4σ variant answers the release question the paper poses (Ppk ≥ 1.33).
- **R2, the north-wall check:** not adopted. As your third qualification notes, it cannot separate a non-square blank from an edge-detection bias.
- **R2, the request to the providers:** **[author]**. The draft (`paper/submission/note_to_dataset_authors.md`) asks for the blank dimensions and the tool drawing.
- **R2, the draw-in saturating between 300 and 500 kN, and the OP10-to-OP20 change of wall angle as a scale-free target:** not adopted, for length.
- **R2, what a confirmatory dataset needs from the measurement:** adopted in the conclusions: "series from several days, coils and tool states, scanned in a documented order with a reference artefact" (p. 27, l. 1199).
- **R2, the new family as the pre-tryout question, with the PPAP caveat:** adopted in the introduction (p. 2, l. 81), which also notes that a customer may require a resubmission run.
- **R2, mark the warm-up in Fig. 4:** adopted (shaded, named in the caption). The punch temperature is not added, because it would need a second axis.
- **R3, estimate the cost bands out of sample:** not adopted. C8 is met by restricting the statements to those that hold under both priors and all cost ratios.
- **R3, rarer failing designs:** not adopted. The text states that both priors place 47 % of the verdicts on failing designs.
- **R3, plot Fig. 6 relative to NN, and add the decided share to Fig. 1b:** not adopted. A relative plot would hide the trial-every-design reference, and Fig. 1b would need a second axis.
- **R3, one-sided monitoring and the participants:** adopted. The control chart "sees false accepts only, rejected designs never being made", a rise to 10 % takes about 150 decided verdicts to detect (p. 25, l. 1144), and the study names process planners and quality engineers and how often they override a trial verdict (p. 26, l. 1153).
- **R3, items for Table 9:** not adopted, for length. Its guard-band row now cites the decision-time bands.
- **R3, checks in `opchar.py`:** adopted. `--selfcheck` reproduces the 40 new-setting guard bands of Table 7 with their shares correct and trial rates, and the worked example's cost band; `cost_band` gives the band widened by stated costs.
- **R3, a forward reference in Section 3.7:** adopted ("the concave cup of Section 4.1") (p. 10, l. 453).
- **Length, thin Section 5.4 and Section 5.7:** adopted (see "Length" above).
- **Length, a validation figure in Section 5.2:** not added. The validation is Table S3, as your second qualification rules.

## Part 3. Your qualifications of the reports

1. **The pooled trend GP.** The text says that it is safe at 2.75 floors and that the relation-matched interval around NN is safe below one floor; the finding that NN+RM is the safest rule for new settings stands.
2. **Placement.** The crossing and the validation are in Online Resource 1 (S7, S3), and Section 5.2 carries the conditional wording of C6. The M7n prior sensitivity is reported (S6).
3. **The offsets.** The tool geometry is called the best fit, "unconfirmed" by the documentation; the north-wall check is not used.
4. **The worked example** keeps the mid-side draw-in and its quantisation, and uses the planner's 40 kN.
5. **The extrapolation scheme.** Table 7 uses the other family's band for a new setting, labelled as such in its note. The family's own band with the force cell left out is reported in Section 5.5 and Table S10.
6. **Costs.** C8 is met by consistency and labels. The within-run statement with the τ = 3 bands stands in Section 5.5 in place of a between-run column in Table 7.
7. **"Committed to in advance"** is replaced throughout.
8. **Generative AI.** The declaration now counts six simulated rounds and points to Online Resource 1 for the list of what each round added.

## Part 4. Conditions for acceptance

- **Licence: [author].** A `LICENSE` file for the code and the licence fields of `.zenodo.json` and `CITATION.cff`. The data-derived files keep CC BY 4.0. `paper/submission/CHECKLIST.md` gives the steps.
- **DOI: [author].** The deposit of version 3 (tag `v3`), then the DOI in `paper/refs.bib`, `CITATION.cff` and the cover letter. `sha256sum -c SHA256SUMS` checks the deposited files against this revision.
- **Registration.** The word "frozen" is gone. The conclusions name "a confirmatory test of the procedure, registered before the analysis, on other data" as an extension (p. 27, l. 1200). Depositing `paper/notes/frozen_procedure.md` with a timestamp before any confirmatory analysis is **[author]**.
- **Data dictionary:** done (C10).

---

## Part 5. Reviewer 1

**Major 1 (RQ3 not like-for-like; the crossing for one predictor).** Done as C1: the claim names the borrowed evidence; Section 5.4 gives the three like-for-like comparisons; Table S7 crosses all eight predictors and adds M7n on both families.

**Major 2 (the guarantee; coverage averaged).** Done as C2: there is no guarantee, the level is nominal, the borrowed cases are named, and coverage is given per family, characteristic and stratum (S9) with its range in the text.

**Major 3 (the trend GP's intervals; M7).** Done as C3: the undercoverage is explained, the prior sensitivity is S6, and M7's force-slope behaviour and its 118 floors are reported, with M7 counted.

**Major 4 (selection and validation).** Done as C4 and C9. Table 7 is the decision-time band, validated by the matching scheme under both priors; the force-cell-out shares, the cross-fit by safety and the cross-fitted step-6 shares are reported.

**Major 5 (where the tables went).** Done as C10: Online Resource 1, as ruled.

**Minors.**

1. Finite-sample sentence restored; Barber et al. (2021) and Friedman (2001) cited (C2, C11).
2. Not adopted, for length (Part 2).
3. The interval-score sentence is restricted to production-record and trend centres (C1). The "best interval score" claim of the previous response is withdrawn for extrapolation, where M1sn+RM scores better, as you found.
4. 0.72–0.94 corrected. For M3 the recomputed interval is 0.929–0.984, printed as 0.93–0.98 (C11).
5. The intervals are blanked for new settings and a new family and flagged where degenerate (`ci_note`).
6. M0's 3.75 floors are stated.
7. M7 is counted.
8. The few-shot floor is stated (Section 5.4); the claim in Section 6.5 is removed.
9. "92 to 95 of the other 98", from the decision-time band.
10. Table 7 shows per-family bands, available at decision time.
11. The paragraph is thinned and its numbers moved to S7–S9.

## Part 6. Reviewer 2

**Major 1 (two undocumented inputs).** Done as C6: the assumed blank and both scale sensitivities are stated, and the simulation finding rests first on the scale-free comparisons, with the level comparisons conditional.

**Major 2 (validation and scan redundancy).** Done as C10: the validation with the extraction noise is S3, the redundancy per series S4, and `findings.md` holds only current numbers.

**Major 3 (release and trial).** Done as C7: (a) release as a capability decision on m̄ + 4σ, with the true within-run indices this confirms; (b) the trial under the between-run component, with your numbers reproduced (2.1, 3.6 and 5.1 floors for the 20-part trial; 1.9, 3.45 and 5.05 for the 50-part trial in `qual_between_run_trial.csv`); (c) the release-like figures next to the reference ones in Section 6.2, and "the few close ones" dropped. The reference prior is described as requirements a few to some tens of floors from the 95th percentile, the release-like prior as those near capability limits.

**Major 4 (the worked example).** Done as C5, with the six-series floor, the planner's 40 kN, the convex band with the exchangeability caveat, the cost band and the quantisation. Following the editor's fourth qualification, the characteristic is kept.

**Minors.**

1. The bound is given in floors (about 0.9 floor of draw-in); your variance estimate is not added.
2. "Except for the mid-side draw-in" added.
3. "Reaches" replaced (0.011 mm at the grid edge); the corner gap is given at both frictions.
4. (a) Section 6.3 reads "friction-fitted (censored)", and Section 5.2 states that Mcd's posterior piles at the lower edge (0.05). (b) The saturation is not added, for length.
5. Extraction noise in Section 4.2 and S3.
6. Table 6 note reworded.
7. Not added, for length (Part 2).
8. (a) "Explores". (b) The measurement needs are in the conclusions.
9. Adopted in the introduction (pre-tryout feasibility; resubmission runs).
10. Warm-up shaded; no second axis for the temperature.

## Part 7. Reviewer 3

**Major 1 (the band in Table 7 and the worked example).** Done as C4 and C5. Table 7 is the decision-time band per family; for a new setting it is the other family's band, validated out of family. The worked example borrows the convex band and widens it by the stated trial cost.

**Major 2 (costs beside the procedure, in-sample).** Done as C8: costs set the band in step 5 and choose the rule in step 6; the statements are labelled in-sample and pooled and restricted to those that hold under both priors and all cost ratios; the trial's own error cost is given.

**Major 3 (the evidence for the deployed part).** Done as C10: S10–S13 hold the bands, their validation, the prior's width and the costs.

**Minors.**

1. "One rule for every relation".
2. Mcd in Table 5.
3. With the decision-time band, 92–95 of 98; the worst characteristic (89 % on the dome) is in Section 5.5.
4. "An assumed prior".
5. The cross-fitted step-6 shares are reported (0.92–0.97; four of six below 0.95; 0.73).
6. Adopted: one-sided monitoring, about 150 verdicts, process planners and quality engineers, overrides as an outcome.
7. The guard-band row of Table 9 now cites the decision-time bands; further items are not added, for length.
8. `opchar.py` checks the guard bands, shares, trial rates and a cost band. A grouped out-of-sample function and prior weights are left to users of the module.
9. Thinned (C10).
10. Fig. 6's caption states the error-free trials and the 40-floor search; the reference prior is named in the caption and the text. The relative plot and the second axis are not adopted (Part 2).
11. Forward reference added.
12. Stated as an assumption.
13. Table 7 is per family; the threats say the band was "estimated pooled over characteristics and, for new settings, borrowed between two families" (p. 26, l. 1170).

## Part 8. Numbers that changed in this revision

- **Table 7** (guard bands): now the decision-time bands per family, NN 0/0.5, 2.5/1.5 and 5.75/9.5 floors (concave/convex) under the reference prior, against the in-sample pooled 0.25, 2.0 and 7.0 before. The shares correct and trial rates follow from them (NN: 95 %; 2, 18 and 58 % trials).
- **Section 6.2:** "92 to 95 of the other 98" (before: "at least 93"); 58 trials of 100 extrapolated verdicts, 41 and 92 under the release-like prior.
- **Section 3.7:** floor 0.041 mm (0.050 before); resolvable force change about 40 kN (21–67 kN before); band 2.5 widened to 5.0 floors (1.5 before); margin 7.4 floors; truth 10.0 floors below the limit.
- **Section 5.4:** cluster intervals 0.72–0.94 (0.71–0.94 before).
- **Section 5.7:** M0 moves by 3.75 floors without the held-out series (before: "at most 1.4" for all rules).
- **Table 5:** Mcd added. Table S1 lists every rule; no distance changed.
- **New numbers** (C3, C4, C7, C8): the M7n prior sensitivity; the force-cell-out shares; the worst characteristics; the τ = 3 bands; release scored on m̄ + 4σ; the trial under τ; the trial's own error cost; the 47 % share of failing designs; both cross-fits.
- **No distance, floor or coverage value of version 2 changed.** The cluster intervals of `qual_coverage.csv` were re-drawn, and Table 7's guard-band values reflect the new scheme.

With thanks to you and the three reviewers,

Hüseyin Tayyer Canseven
