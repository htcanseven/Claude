# Response to the four external reviews (E.1 to E.4)

Revision of 29 October 2026 for Mechanical Systems and Signal Processing. The four reports are referred to as E.1
(positive, minor to moderate revision), E.2 (major revision; statistics and positioning), E.3 (major revision;
framing, comparability, selection) and E.4 (major revision; POD/LoD/EOV positioning, normalisation, scope). Every
comment is listed with the action taken and where the manuscript changed. New analyses are in
`scripts/revision_round3.py` and their tables in `results/tables/R3_*.csv`; new displays were built with the
same generators as before. The manuscript grew from 31 to 38 pages because the reviewers asked for new evidence
(three tables, two figures) and for the prose to be split into shorter sentences; every table and figure
remains in the main text.

## Changes that answer several reviewers at once

| Change | Answers |
|---|---|
| Novelty reframed around a drift-calibrated framework for detectability assessment and sensor selection in seeded-fault campaigns; the SDR placed in the POD, limit-of-detection and EOV-novelty-detection family with a positioning table (new Table 1) and the mathematical equivalence stated (SDR >= 1 is a threshold at the empirical healthy quantile); comparators (per-feature AUC against the null and against the healthy trials, Cohen's d on the drift scale, a Gaussian-scale rule) computed on the same trials (Section 5.4) | E.2 M1; E.3 M2; E.4 M1 |
| Power at the required extent made the primary endpoint: e90 and e90/95 defined (Section 3.3) and tabulated per suite (Table 5), the decision table (Table 6) evaluated with the share at the level e_req maps to, the pooled variant and the tap-pair resampling unit in Table 7, a POD figure (Fig. 7) of the share per level with intervals | E.2 M4; E.3 M6; E.4 M1 |
| Scope stated up front: seeded faults of known extent, stationary operating points, abrupt-onset detectability, one machine per type; title, abstract, Section 1, Section 3.5 and the conclusions reworded to "three generator--drive systems"; the PMSG--SCIG pair named the controlled comparison and the WFSG an extension with a different evidential status, marked unscreened in Fig. 5 and Tables 6--7 | E.2 M5, M6; E.3 M1; E.4 M2, M4, M5 |
| Interval, null and reference conventions tested and tabulated (Table 10): fault interval after relay pick-up, the WFSG interval geometry on the common bench, a per-speed null, the between-trial reference; leakage of the negative-sequence estimate checked on a synthetic signal | E.2 M2, M6; E.3 M3, M6, minor 9; E.4 M5, M6, M10, 11 |
| Terminal impedance per speed (Table 9) with the regulator-gain reading and the inductance-ratio hypothesis stated as untested | E.4 M7 |
| Prose rewritten in short sentences in the abstract, introduction, background, method and discussion; "alternative" replaced by "candidate" (method) and "machine" (demonstration); an SDR illustration figure added (Fig. 1); GBDT choice justified | E.1 M1, M2, M4; E.2 writing; E.3 minor 1; E.4 presentation |
| Field use of the null: reference horizon, per-operating-region null, accumulation rule and the 7 s per-decision rate, in Section 6.2 | E.1 M3; E.3 minor 5; E.4 M5 |

## Reviewer E.1

**Major 1, readability.** Done. The abstract, introduction, Section 2, Section 3 and Section 6.1 were rewritten in short sentences (the abstract's longest sentence is now 32 words); results sentences that chained several numbers were split.

**Major 2, visualising the SDR.** Done. Fig. 1 shows one PMSG inter-turn trial: the per-window deviation of the voltage and current negative-sequence ratios from their R2 mean, the bars for the healthy change and the change under fault, and the null quantile, so that the SDR is read off as the ratio of the bar to the dashed line.

**Major 3, the null in the field.** Done. Section 6.2 now has a paragraph on the three field choices: the reference horizon (rolling against frozen, with the measured cost of a session-old baseline), the per-operating-region null (as the per-speed null of Table 10, or regression of the operating point as in EOV novelty detection), and the accumulation rule that turns the per-decision rate into a tolerated alarm rate.

**Major 4, why GBDT.** Done. Section 4.4 states the reason (features of different scales and shapes without tuning, no linearity assumption) and that a logistic regression is run beside it as the linear comparator.

**Minor.** Keywords replaced by condition monitoring, probability of detection, stator winding fault, negative sequence, wind-turbine generators, sensor selection. MMF and FOC are defined at first use (Section 5.1; Section 4.1 and Table 2). Figures 5--7 use marker shapes beside colour. MSSP review is single-anonymised, so the self-citation stays. The "e % of a winding" sentence stays.

## Reviewer E.2

**Major 1, contribution versus established threshold calibration.** Accepted. Section 2 states the equivalence (for a fixed feature, SDR >= 1 is a threshold on the change statistic at the empirical healthy quantile, so any normalisation with the same calibrated threshold takes the same decisions) and lists what the SDR adds (a null from every trial's own reference, a common scale, the screen and the calibrated oracle, the POD quantities). Table 1 compares the measures on what they need and yield. Section 5.4 tests the equivalences on the same trials: the per-feature AUC and Cohen's d rank the 33 features with Spearman correlations of 0.82 to 0.99 against the median SDR, while a Gaussian-scale threshold gives the same MDE for only 11 to 18 of 33 features per machine and class, because the quantile exceeds 1.96 sigma by a factor of 1.6 to 1.9 for the residuals. The abstract no longer claims that existing measures necessarily need a model or a detector; it says the SDR needs neither and is calibrated without a separate healthy campaign, and the introduction says what it needs instead (seeded faults).

**Major 2, false-alarm calibration.** Partly done, with the limits stated. The per-speed exceedance rates were already reported; a per-speed null is now evaluated (Table 10; it changes two of twelve MDEs and no decision verdict), and the stricter interval start and the WFSG geometry are evaluated as conventions. The screen's power statement is kept and the limitations now give the one-sided bound the reviewer asks for (zero false alarms in nine trials leave a 95 % upper bound of 28 %). Held-out calibration on independent healthy records beyond the nine trials is not possible with these datasets; the WFSG adequacy is labelled provisional (unscreened) in the figure and table notes.

**Major 3, selection and evaluation on the same data.** Partly done. The nested selection (fixed feature chosen on the other tap pairs) is now quantified at five cycles: it changes the pooled shares by at most one point (Table 5 note; Section 5.5). The decision table re-selects the feature in every resample. A fully independent held-out assessment is not available with 36 trials per level, and the limitations say so; the bootstrap fractions are now called resampling support, not probabilities, and the note says that a cell of 1.00 means that no resample failed.

**Major 4, MDE versus a high-probability requirement.** Done. Section 3.3 defines three quantities: the MDE (median crossing, about 50 % detection), e90 (share >= 0.9 at the level) and e90/95 (with support >= 0.95); the decision table uses the share at the level e_req maps to; Table 5 gives e90/95 per suite; Table 7 lists the seven cells that change under the pooled definition; Fig. 7 gives the share per level. Step 1 now asks whether the power is required on average over the envelope or at every operating point, and Section 5.7 reports the share at the lowest speed.

**Major 5, three case studies, not a ranking of types.** Done. The title reads "three wind-turbine generator--drive systems", the abstract, Sections 1, 4.1, 6.3 and 7 say "machines" or "generator--drive systems" where topology attribution is not supported, the PMSG--SCIG pair is named the controlled comparison, and the implications are conditional on the tested machines, the cost ordering and the requirement.

**Major 6, known onset and transients.** Done. The scope paragraph of Section 1 and Section 3.5 state abrupt-onset detectability at the outset. Table 10 gives the ablation: a fault interval starting after the relay pick-up raises the medians by 6 to 8 % and changes no MDE, the WFSG geometry lowers them by up to 36 %, and the between-trial reference moves several MDEs up one level. Section 4.4 names the three deployment scenarios of the referencing rules (no target data; a commissioning record; the immediately preceding healthy interval).

**Major 7, the calibrated oracle and feature fusion.** Done. The claim is narrowed to the tested calibrated maximum statistic (Section 5.5), and the window-level detectors of Section 5.6 are named as the multivariate comparator of the paper.

**Major 8, cost ordering.** Done. Section 4.3 states whose ordering is used, step 1 asks for it, Section 6.2 reads the decision table for a converter manufacturer and for a third-party retrofit, and the phrase "least-cost adequate suite among the specified candidates under the stated ordering" is used.

**Specific comments.** "Studentised" replaced by "standardised by an empirical quantile"; the 1.96 sigma statement is now explicitly for a scalar Gaussian null and the residual nulls are shown not to be Gaussian; near-zero reference values: the screen's null-quantile rule is stated as the numerical safeguard, the residual normalisation is explained, and the absolute-change variant is reported (ranking correlation 0.92--0.99, residual SDRs changed by 2 to 56 %); code availability: the author has chosen not to publish the pipeline with the manuscript, so the abstract says the data are open and the data availability paragraph names the datasets; literature: Currie 1968, MIL-HDBK-1823A, Sohn 2007, Cross et al. 2011, Farrar and Worden 2013, Bull et al. 2021, Gardner et al. 2020 and 2021 added; figures: Fig. 6 now shows the current pair as well, Fig. 7 added; a heatmap of verdicts was not added because Table 6 is already a verdict grid.

## Reviewer E.3

**Major 1, claims beyond the design.** Done; see E.2 major 5. The findings paragraph of the introduction states the scope before the findings.

**Major 2, novelty positioning.** Done; see E.2 major 1 and Table 1. The subsection the reviewer asks for is Section 2's second paragraph plus the comparator paragraph of Section 5.4.

**Major 3, comparability across the three machines.** Done. Table 10 recomputes the common-bench SDRs with the WFSG's interval geometry (150 ms fault, 190 ms reference halves): the medians fall by up to 36 %, two MDEs move up one level, and the ordering of the two machines is unchanged; the WFSG's shorter intervals therefore penalise it rather than favour it. The pooling of the WFSG over impedances is shown to lower its inter-turn medians and raise its inter-winding ones relative to the matching-impedance subset. Section 4.1 and the limitations name the PMSG--SCIG pair as the controlled comparison.

**Major 4, selection bias.** Done; see E.2 major 3. The nested shares are in the Table 5 note and in Section 5.5, and the limitations say the point estimates are chosen on the evaluation trials.

**Major 5, the transfer negatives.** Option (a) taken: the transfer results are stated as abrupt-onset detection against a stationary healthy background (Sections 5.6 and 6.3), the negatives are described (contactor operation and release transient, no load change, speed ramp or grid disturbance), and the TPR of 0.54 in one direction is called not field-ready.

**Major 6, pooled null and per-speed rates.** Done. A per-speed null is evaluated (Table 10, Section 5.7); step 1 asks whether the power is required at every operating point; the share at the lowest speed is reported; Section 6.2 discusses the per-operating-region null in the field.

**Major 7, severity axis.** Done. The axis is demoted to a covariate that exposes the design-extent against physical-severity distinction (Sections 3.1, 5.1), with the MMF argument kept for its ordering within a machine and the magnetising-current confound stated for comparisons across machines.

**Minor.** Abstract split into short sentences with the findings named; near-zero rule stated in Section 3.2; the features with heavy-tailed nulls named (excess kurtosis 3 to 7.5 for the residuals, 0.2 to 1.9 for the ripples); where the null-quantile uncertainty enters is stated in Section 3.2 and in the table notes (every bootstrap resamples the null); the 7 s false-alarm rate is in Section 6.2; the inheritance superscript is explained with an example in the Table 6 note; Fig. 5 keeps the SDR = 1 line and the caption states that the WFSG pooling is over impedances with the direction of the bias in Section 5.7; Fig. 6 shows the current pair again; the contactor pick-up effect is quantified (6 to 8 % on the medians); GBDT settings stay in Section 4.4 and the logistic results stay in the text of Section 5.6; the SNR analogy is acknowledged in Section 3.2; the MDE bracket notation is explained in the Table 4 note.

## Reviewer E.4

**Major 1, POD, LoD and EOV positioning.** Done; see E.2 major 1 and Table 1. The a90/95 correspondence is named in Sections 2 and 3.3, the share per level is plotted as a POD curve (Fig. 7), and the per-feature AUC and Cohen's d are computed on the same trials (Section 5.4).

**Major 2, what the method requires.** Done. The introduction and Section 3.5 state that the SDR is the statistic of a seeded-fault campaign, as POD is, and that the seeded-fault precondition is the price of needing no model.

**Major 3, normalisation and notation.** Done. Section 4.3 explains that the feature label names the ratio to the positive sequence and that the relative changes divide by the inherent asymmetry, so the SDR of a residual divides a change of the negative sequence by a quantile of its healthy changes, both relative to the same quantity; Section 5.7 reports the absolute-change variant (rank correlation 0.92--0.99, residual SDRs changed by 2 to 56 %); the near-zero rule is stated in Section 3.2.

**Major 4, the WFSG leg.** Done; see E.2 major 5. The WFSG is marked unscreened in Fig. 5 and in the notes of Tables 6 and 7, Section 4.1 names its different evidential status, and the abstract no longer puts its finding on an equal footing.

**Major 5, abrupt-onset detectability.** Done. Scope stated in the introduction and Section 3.5; the reference horizon is reported for the two ages the data allow (the preceding half second and the session; Table 10 and Section 5.7) with the MDE under each. The data give no intermediate ages, so the sweep the reviewer suggests is not possible.

**Major 6, pooled null and per-speed rates.** Done; see E.3 major 6. The 59.6 Hz hypothesis is kept as a candidate cause with the measured 1.7-fold wider null at 1800 rpm.

**Major 7, impedance mechanism.** Partly done. Table 9 gives the impedance per machine, class and speed: it is flat within 5 % over 80--120 Hz, which rules out a leakage-reactance reading and is consistent with a proportional-gain-dominated output impedance; the Kp-ratio reading is stated as a hypothesis that the undocumented inductances and gains leave untested.

**Major 8, severity axis.** Done; see E.3 major 7. Rated-current normalisation was not adopted because the ratio to the stator current is what the sensors see; the covariate role is stated.

**Major 9, transfer claim and placement.** Done. The ranking of the rules is named as the result of interest, the TPR caveat is stated, the features the GBDT sees are named (all features of Table 3 that a machine provides), the recovery windows are justified as carrying the release transient, and the section was shortened.

**Major 10, negative-sequence estimation at three cycles.** Done. On a synthetic three-phase signal with the PMSG's inherent asymmetry a three-cycle Hann window recovers I2/I1 within 0.2 %, and within 1.6 % with a 1 % error in the electrical frequency (Section 5.7).

**Major 11, statistical details.** Done: the interval effect is quantified (Table 10); the bootstrap fractions are called resampling support over at most 36 trials per level; the nested check is in the Table 5 note; the null shape is reported by feature (kurtosis and the quantile-to-Gaussian ratio). A histogram figure was not added for length.

**Major 12, reproducibility.** The author has chosen not to publish the pipeline with the manuscript; seeds and settings are in Section 4.4.

**Minor and technical.** Table 2 was checked against the processed WFSG records (438 variable-speed records at 4 kHz with 1.3 s length); Fig. 3 panels reordered to PMSG, SCIG, WFSG; "drift" defined at first use; the Gaussian 5 % test reworded as conditional; bold verdicts verified in the PDF; the abstract carries the power and the middle-level result; keywords changed; Section 3.5 labelled as outlook; the extrapolation to 10 Hz is tied to the flat impedance.

## Not done, and why

* Independent held-out healthy records for calibration (E.2 major 2) and a held-out assessment of the suite selection (E.2 major 3): the datasets hold nine healthy trials per machine and 36 trials per level; the limitations state the consequence.
* A reference-age sweep (E.4 major 5): the records carry no timing between trials; two ages are reported.
* Code publication (E.2, E.4): the author's decision for this submission.
* A verdict heatmap (E.2): Table 6 already presents the verdicts as a grid.
* Title with "laboratory" (E.4): the title now names the three generator--drive systems; the abstract names the bench data.
