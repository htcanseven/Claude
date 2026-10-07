# Response to the guest editor: final version

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Answers:** the third-round decision of 6 October 2026 (accept in principle, subject to conditions C1–C7)
**Revision of:** the version considered in the third round (frozen as `paper/review/cfp_panel/round3/main_reviewed.tex`)

> **Note on this document.** The decision letter it answers (`editor_decision_round3.md`) and the three third-round reports were written by AI agents acting as a simulated review panel. They do not come from the journal, its editors or its reviewers. The response is written as it would be to a real editor.

**Archive.** Zenodo, version 4, DOI **[DOI to be inserted after deposit]**. `RELEASE_NOTES.md` in the deposit gives the SHA-256 checksums of the seven files your letter names. `SHA256SUMS` gives those of every script and result file, so `sha256sum -c SHA256SUMS` in the unpacked deposit checks them all.

**Locations.** Page and line numbers refer to the final manuscript, `paper/main.pdf`, which is compiled with line numbers. The abstract, the tables, the captions and the boxes of Fig. 1 carry no line numbers and are named. The version marked up against the third-round manuscript is `paper/review/cfp_panel/round3/main_diff.pdf`. In it, latexdiff shows changed tables and captions in their new form without markup, and it does not mark Fig. 1, which is drawn in `fig_procedure.tex`. Their changes are therefore listed below. The main text still ends on page 23, and the paper still has 30 pages.

Dear Guest Editor,

Thank you for checking the second revision yourself against the released files, and for a decision that says exactly what remains. This version meets C1–C7 and makes all eight editorial corrections. It also adds the recommended ±3-grid bands and takes up three of the six optional points (Parts 1–3).

No number of the third-round version has changed. One result file gained two columns, which the new clause on the cap of the guard band cites. The six other files your letter names are byte-identical to those you checked (Part 5). Part 4 corrects the statements of the second-round response that your letter lists.

---

## Part 1. Conditions C1–C7

| Condition | What was done | Where |
|---|---|---|
| **C1** Deposit the archive and cite its DOI | **The deposit.** The code, the feature tables and every result file named in Table A5 are deposited on Zenodo, as they produce the numbers of this version. They form version 4, DOI **[DOI to be inserted after deposit]**. It is the first deposit. It is numbered 4, after the manuscript's fourth version, because one result file differs from the version 3 prepared for the third round (Part 5). **The citation.** The reference `canseven2026archive` cites the DOI. Sect. 4.5, the appendix and both availability statements cite that reference, so each now cites a resolving DOI. The GitHub link remains the working copy. `CITATION.cff` gives the DOI. **Your check.** The checksums are in `RELEASE_NOTES.md` and `SHA256SUMS` (see above). | Sect. 4.5 p. 12, l. 524; Appendix p. 24, l. 1065; Data availability p. 24, l. 1100; Code availability p. 24, l. 1103; References p. 28, l. 1267 |
| **C2** Specify which applicability guards step 6 applies | Route 1, with no new numbers. **Sect. 3.6.** The guard band of the relation now takes the place of the range and family guards, which here coincide with the extrapolated and new-family relations. The novelty guard is reported as a diagnostic, not applied, since most of its refusals would have been right. "A guard fires" is no longer among the reasons step 6 gives for a trial. **Sect. 3.5.** A guard now "flags" a design outside the calibration, where it used to return a trial. **Fig. 1 and the tables.** The step-6 box of Fig. 1 no longer has a guard step. It reads "interval for $q_p$ widened by the relation's guard band $g$, in place of the range and family guards", and a fired guard is no longer among its reasons for a trial. Table 5 ("Deciding a single design") says the same. The note to Table A4 adds "no applicability guard is applied". **Sect. 5.7.** The guard sentence calls the guards diagnostics. It says that the range guard refuses exactly the extrapolated designs (84 of the 126 new-setting cases), and it gives the requirement distance of its shares, 10 floors from the truth (`D_CHECK` in `guard.py`). Table A4, Fig. 4 and Sect. 5.7 thus describe the procedure that Sect. 3.6 specifies, and the new-family sentence of Sect. 5.7 holds as worded. | Sect. 3.5 p. 9, l. 391; Sect. 3.6 p. 10, l. 437; p. 10, l. 439; Fig. 1, step 6; Table 5; note to Table A4; Sect. 5.7 p. 17, l. 780 |
| **C3** Attribute the new-setting split to its rules | **Sect. 6.1.** It now reads "8.2 for a new setting (the force trend; by stratum the nearest setting needed 4.7 interpolated and 4.9 extrapolated to 500 kN, the force trend 8.9 to 100 kN, where the nearest setting needed 11)". **The conclusions.** They read "8.2 for a new process setting (the force trend; the nearest setting 4.7 interpolated and 4.9 extrapolated to 500 kN, the force trend 8.9 to 100 kN, with a stroke-speed change)". **Table 5.** The row "New process setting" names the rule of each figure and adds the nearest setting's 11 floors at 100 kN. **The abstract** keeps "the best rules needed 4.7 floors interpolating, 4.9 extrapolating to 500 kN and 8.9 to 100 kN". The plural says that the best rule differs by stratum, and it credits no figure to a rule. The abstract is at the journal's limit of 250 words, so naming the rules there would have cost other content. | Sect. 6.1 p. 19, l. 869; Sect. 7 p. 23, l. 1042; Table 5; abstract |
| **C4** Restore the index of the release-level statement | The abstract and the conclusions now read "Requirements at a performance index of 1.33 lay inside every decisive distance except a near-replicate's", as your letter proposes. To keep the abstract within 250 words, three phrases were shortened without changing their content: the strata now read "(near-replicates 0.85, resolvable siblings 4.9)", the draw-in floor stands in parentheses, and a semicolon replaces ", and" before the coverage clause. | Abstract; Sect. 7 p. 23, l. 1046 |
| **C5** Label the pooled gradient in Section 6.4 | "The growth of the decisive distance, pooled over strata, from about 3 to 8 and over 30 floors …" | Sect. 6.4 p. 21, l. 957 |
| **C6** Withdraw the untested short-series claim | **Sect. 5.6.** It reads "rules can be calibrated on short runs, but the floors and the held-out truths came from the full series, and whether truths from short runs suffice to qualify the rules was not tested". **Sect. 6.5.** It reads "here rules calibrated on about 50 parts per variant scored within 1.5 floors of those calibrated on full series, against truths and floors from the full series". **Withdrawn.** Neither "only the floor needs a run long enough to show the drift" nor "only the floor needed long runs" remains. | Sect. 5.6 p. 16, l. 735; Sect. 6.5 p. 22, l. 984 |
| **C7** Give the refit intervals of the safe distances | **Table A2.** It has a second refit row, "Refit, δs", from `rob_refit.csv` (`safe_lo`, `safe_hi`). With a sibling, the intervals are 0.15–1.4 floors for M2 and 0.75–3.0 for M5; these are the intervals at whose edge Sect. 5.9 places the point estimates. **The note** reads "95 % intervals of the decisive and safe distances". | Table A2 and its note; Sect. 5.9 p. 19, l. 854 |

---

## Part 2. Editorial corrections

| No. | Correction | Where |
|---|---|---|
| 1 | The caption of Fig. 4 adds "new family in the produced family's floor". | Fig. 4 caption |
| 2 | "the 47 distances of the requirement grid" | Sect. 3.6 p. 9, l. 408 |
| 3 | The reference prior "is a reference for requirements set from a few to some tens of floors from the true 95th percentile, denser where verdicts are hardest, which a team replaces by the distribution of its own requirements". | Sect. 3.6 p. 9, l. 413 |
| 4 | "the nearest setting decided at up to about 5 floors" | Sect. 5.4 p. 15, l. 673 |
| 5 | The note to Table A2 reads "a new family in its own floor (in the produced family's floor in Table 4)". Sect. 5.6 reads "for a new family by at most 4 in its own floor". | Note to Table A2; Sect. 5.6 p. 16, l. 733 |
| 6 | "M5, M5n and M3n predicted as well as the nearest produced setting with a produced sibling" | Sect. 6.1 p. 20, l. 906 |
| 7 | "A3 holds for repeatability and measurement resolution" | Sect. 5.1 p. 12, l. 539 |
| 8 | "the difference that drift and scatter of production and measurement produce between two batches of one design within a run" | Sect. 1 p. 2, l. 71 |

---

## Part 3. Recommended and optional points

**Recommended.**

1. **The ±3-grid bands. Done.** Sect. 5.7 (p. 17, l. 774) adds "(8.0, 5.0 and 14.75 within ±3)" to the bands under the near-truth prior. The worked example already gave the 5.0 floors.
2. **A licence for the deposit. Done.** The deposit is released under **[licence to be named by the author]**, which `LICENSE`, `.zenodo.json` and `CITATION.cff` state. The README and `RELEASE_NOTES.md` give the attribution that CC BY 4.0 requires for the feature tables and result files derived from RDDAC and DDACS: the creators, the licence and the changes made.
3. **`CITATION.cff`. Done.** It gives the DOI and version 4.

**Optional.**

- **The cap on g. Done.** Sect. 3.6 (p. 9, l. 410) searches g "in steps of 0.25 floors up to 20, beyond which the rules send most designs within the prior's range to trial". Under the reference prior, eight combinations of rule and relation in `panel_guard_priors.csv` qualify only beyond the cap. For those eight, the uncapped bands send 89–100 % of the verdicts at 10 floors from the truth to trial, and 77–99 % of those at 20 floors (`panel_guard_priors.csv`, new columns `trial_10_uncapped` and `trial_20_uncapped`).
- **Intervals in Table 4. Done.** Table 4 has interval rows for M1 and M1sn. They include the force trend's 8.2 floors for a new setting (6.7–9.0) and the bias correction's 33 floors for a new family (31–36).
- **The cost ranking for a new setting. Done.** Sect. 5.8 (p. 19, l. 835) reads "the force trend at every trial cost, by three false rejects of the nearest setting among 108 decisions".
- **Not done, for lack of space:**
  - the interpolated coverage in the conclusions; Sect. 5.5 gives it (M2n and M5n 93 %);
  - the protocol of a production part approval study as the protocol of the floor it supplies;
  - the 1.67 criterion in Sect. 3.1; Sect. 5.8 gives where the limits lie at indices of 1.67 and 2.0.

---

## Part 4. Corrections of the second-round response

| The second-round response said | Correction |
|---|---|
| The DOI would be minted "before resubmission", and the manuscript would not be resubmitted without it (preamble; Part 1, S6; Part 3; Part 8). | That undertaking was not kept: the second revision was resubmitted citing "[DOI pending]". The archive is now deposited, and the paper cites its DOI (C1). |
| "The text says why the prior represents the requirements a team faces" (Part 1, S2(a)). | The text said what the prior covers. It now presents the prior as a reference that a team replaces by the distribution of its own requirement distances (editorial correction 3). |
| The truths and floors are those of the full series "(Sect. 5.6, Sect. 6.5, note to Table A2)" (Part 1, S5). | Sect. 6.5 did not say so; it said that "only the floor needed long runs". It now says that the rules were scored "against truths and floors from the full series" (C6). |
| The narrowed short-series sentences (Part 4, A-m2; Part 6, C-N1). | They were quoted without their final clauses. These were "and only the floor needs a run long enough to show the drift" (Sect. 5.6) and "only the floor needed long runs" (Sect. 6.5). Nor did the response say that the second-round caveat "how many long runs a floor needs was not tested" had been deleted. Both clauses are now withdrawn, and Sect. 5.6 states what was not tested (C6). |
| "Wherever it is quoted as a headline, the nearest setting's strata are given" (Part 1, S4). | They were not given in the new sentence of Sect. 6.4, which now says that its gradient is pooled over strata (C5). |
| "Its measurement resolution, 0.38 floors (Sect. 4.3), is small against the example's margin of 6.2 floors" (Part 6, C-m7). | The resolution of 0.38 floors is in Sect. 4.3, but the comparison with the example's margin is not in the manuscript. The response made it, and it is withdrawn as a statement about the manuscript. |
| The uncapped bands send "94–100 %" of the verdicts at 10 floors from the truth to trial, and "82–100 %" at 20 floors (Part 5, B-N1). | For the bands that response named (M2 and M5 extrapolated; M2, M3 and M5 for a new family), the shares are 96.9–100 % at 10 floors and 82–99 % at 20 floors. They are now stored in `panel_guard_priors.csv` (`trial_10_uncapped`, `trial_20_uncapped`). |

---

## Part 5. Provenance of the new numbers, and the changed result file

| New in this version | Where | Result file (script) |
|---|---|---|
| Refit intervals of the safe distances | Table A2, row "Refit, δs" | `rob_refit.csv`: `safe_lo`, `safe_hi` (`robustness.py`; `make_tables.py`) |
| Intervals of M1 and M1sn | Table 4 | `dec_resolution.csv`: `resolution_lo`, `resolution_hi`; for a new family, in the produced family's floor, `panel_source_floor.csv` (`decisions.py`, `panel.py`; `make_tables.py`) |
| Guard bands under the grid within ±3 floors | Sect. 5.7 | `panel_guard_priors.csv` (`panel.py`) |
| Trial shares at the uncapped bands | Sect. 3.6 (the cap) | `panel_guard_priors.csv`: `trial_10_uncapped`, `trial_20_uncapped`, new (`panel.py`) |
| The range guard refuses exactly the extrapolated designs (84 of 126); right refusals at 10 floors | Sect. 5.7 | `dec_guard.csv`: `cases_guarded`, `false_alarm_rate` (`guard.py`) |
| Three false rejects of the nearest setting among 108 new-setting decisions, none of the force trend | Sect. 5.8 | `scen_scores.csv` (`scenarios.py`) |
| The nearest setting at 11 floors at 100 kN | Sect. 6.1; Table 5 | `panel_force_levels.csv` (`panel.py`) |

**The changed file.** `panel_guard_priors.csv` gained the two columns above. The other five columns are unchanged: without the two new columns the file is byte-identical to the one you checked. `RELEASE_NOTES.md` gives the one-line check and both checksums. The other six files your letter names (`dec_intervals.csv`, `dec_q95_reps.npy`, `dec_resolution.csv`, `panel_source_floor.csv`, `panel_step6.csv` and `rob_refit.csv`) and every other result file are byte-identical to the third-round version. Table A5 now maps Sect. 3.6 to this file as well.

---

## Part 6. Other changes

**For length.** To keep the main text on 23 pages, the following were cut. No result on which a conclusion rests was removed.

- **Sect. 3.6:** "If the distances are too large for the requirements of coming designs, another variant is produced." Fig. 1 keeps this loop in step 5.
- **Sect. 5.6:** the sentence on why the distances shrink with the budget when averaged over all subsets (the share of subsets that contain a sibling).
- **Sect. 5.2:** the parenthesis "(42 with a bootstrap probability of at least 0.95)".
- **Sect. 5.3:** "or 1.3° of wall angle".
- **Sect. 3.3:** the clause "that rescales a simulated trend of the wrong size".
- **Sect. 6.4:** its opening sentence, "The results give constructs of design research a production-referenced measure."
- **Other shortenings:** the definition of the verdicts in the introduction, the caption of Fig. 2, and the refit sentence of Sect. 4.4 ("not sampling uncertainty").

**In the abstract**, "A framework is proposed whose unit" now reads "The proposed framework's unit", and "The framework gives" now reads "This gives", to make room for the index of C4.

**For production.** The `lineno` option will be removed once the paper is accepted.

Yours sincerely,

Hüseyin Tayyer Canseven
