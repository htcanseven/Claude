# Response to the second round of external reviews (E.1–E.4)

Manuscript: *A signal-to-drift ratio for winding-fault detectability and sensor selection in three wind-turbine
generator–drive systems*. Single-column review version `paper/main.pdf` (42 pages, line-numbered), double-column
CAS version `paper/main_dc.pdf`. New analyses: `scripts/revision_round4.py`, outputs `results/tables/R4_*.csv` and
`results/summary_round4.md`. Table and figure numbers below are those of the revised manuscript (Table 2 is the new
quantities table, Table 8 the held-out table, Fig. 8 the null histograms; later tables are renumbered by +1 or +2).

## Summary of the changes

| Change | Raised by |
|---|---|
| `e90/95` renamed `e90^B` (bootstrap-supported extent) and separated from the POD bound `a90/95` in Section 3.3, Table 2, Tables 6 and 7 and the procedure figure; resampling support called an empirical decision-stability measure; the binomial argument stated | E.2 §2, E.3 minor 1, E.4 inconsistency 2 |
| Held-out run of the complete procedure (null quantile, screen, fixed feature frozen on the development tap pairs), Table 8, with a false-alarm count of the frozen procedure | E.2 §3 |
| Requirement-specific selection rule run inside the bootstrap; the fixed-feature rule kept and its scope stated in Section 3.2 | E.2 §4 |
| Conditional sentence on the false-alarm validation in step 5; "no separate healthy campaign" narrowed to the threshold in the abstract, introduction and Section 2; WFSG columns headed "exploratory, unscreened" | E.2 §5 |
| Operating-point mixture stated; `e90` defined at the level and every higher tested level; step 5 and Section 3.3 made to coincide | E.2 §6A, E.4 point 4 |
| Table 2, the quantities of the method (statistic, empirical performance, stability) | E.2 §6E |
| Comparator interpretation sentence; AUC construction and degrees of freedom stated | E.2 §6C, E.3 minor 6 |
| Highlights 4 and 5 reworded | E.2 §6D, E.3 minor 5, E.4 |
| Rayleigh reference for the residuals, folded normal for the scalars; Section 3.2 and 5.4 rewritten; Fig. 8 null histograms; kurtosis by speed | E.4 point 1, E.4 status 11 |
| Primary decision table at 10 000 resamples; borderline marker; tap-pair values quoted | E.4 point 2 |
| Table 1 AUC and Cohen's d rows footnoted | E.4 point 3 |
| Fig. 2 boxes 4 and 5 and the requirement box rewritten | E.4 point 4 |
| Log-logistic POD model on the six inter-winding levels (Section 6.3) | E.4 point 5 |
| Conclusions and Section 6.2 corrected for the SCIG's current-only suite | E.4 inconsistency 1 |
| "alternatives" removed from Fig. 2, Table 3 and Fig. 3; "candidates" in the method, "machines" in the demonstration | E.4 inconsistency 3 |
| Introduction names `e90`; abstract carries the impedance ratio and the AUC range | E.4 inconsistencies 4 and 8 |
| Absolute-change variant: no MDE or `e90` moves (Section 5.7) | E.4 status 3 |
| Grid-frequency hypothesis tested on the raw healthy records and not supported (Section 5.7) | E.4 status 6 |
| Fault current in per unit of the nameplate current (Section 4.2, Table 3) | E.4 status 8 |
| MMF defined; Fig. 1 caption names the trial and the pooled null; Table 6 note says "at this window length"; MDE–`e90` pairing sentence | E.1, E.3 minors 2–4 |

## Reviewer E.1

**Double-blind compliance.** MSSP uses single-blind review, so the author block stays in the manuscript. The
self-citation (reference 41) is cited in the third person, as the whole paper is.

**MMF.** Defined at first use in Section 5.1: "the magnetomotive force (MMF) asymmetry".

**Fig. 1 placement.** Fig. 1 is placed in Section 3.2 directly after the equations; the float parameters keep it on
the page of the definition.

## Reviewer E.2

**§2, `e90/95` is not a POD confidence bound.** Option B taken. The quantity is renamed `e90^B`, the
*bootstrap-supported 90 %-detection extent*, and Section 3.3 now states that it is not the `a90/95` bound: the
resampling fraction measures how stable the decision is under the procedure, with the feature re-selected and the
null re-estimated, not the frequentist coverage of a detection probability; the binomial example is given (36 of 36
detections leave a one-sided 95 % lower bound of 0.92, 18 of 18 one of 0.85). `e90` is called the `a90` read on the
tested grid. Table 7's heading reads "bootstrap support for meeting the empirical requirement", its caption says
"empirical requirement", and the note calls the cell an empirical stability measure of the decision, not a posterior
probability and not a confidence level. The new Table 2 separates statistic, empirical performance and stability
quantities, which is where the reviewer's distinction is now visible at a glance.

**§3, out-of-sample assessment of the complete procedure.** Done as the reviewer specifies (Section 5.5 and
Table 8): for each tap pair in turn the pooled null quantile, the screen and the fixed feature of every suite are
fitted on the records of the other tap pairs and the healthy trials, frozen, and applied to the held-out pair,
whose trials keep their own pre-fault reference; the held-out detections are aggregated by physical level. Result:
the held-out `e90` equals the in-sample one for all sixteen suite–class pairs, the held-out share at the smallest
level differs from the in-sample one in two cells by at most six points, and the folds choose the in-sample feature
or an equivalent one. The false-alarm side was also held out (each healthy trial out of the null and the selection
in turn): 0 of 9 on the PMSG and 1 to 3 of 9 on the SCIG against 0 and 1 to 2 in sample; the text says that the 3 of
9, the d-axis ripple of the SCIG's drive-internal inter-winding suite, is a count the screen would reject and marks
that cell as the least secure. Section 6.3 no longer says the fixed feature is chosen on the trials it is evaluated
on; it cites the held-out run.

**§4, selection objective.** Option 2 (fixed-rule assessment) is kept and stated in Section 3.2: the rule selects
on the median-crossing extent, so adequacy is adequacy under this prescribed univariate selection. The
requirement-specific rule was also run inside every resample (largest share at the level the requirement maps to):
it changes one cell, the PMSG's drive-internal suite at 9.7–10.6 % inter-winding, from uncertain (0.88) to meets
(1.00), and no other verdict (Section 5.5).

**§5, false-alarm limitations in the decision claims.** The sentence the reviewer proposes is in step 5, almost
verbatim. The WFSG columns of Table 7 are headed "WFSG (exploratory, unscreened)". The "no separate healthy
campaign" message is narrowed in the abstract ("its threshold needs no separate healthy campaign, though validating
the false-alarm rate does"), the introduction and Section 2.

**§6A, operating-point population.** Section 3.3: "The share is assessed over the empirical mixture of operating
points represented at each tested level, equal weights per trial, which is not a turbine duty cycle." `e90` is
defined at the level and at every higher tested level; step 5 evaluates the event at the level the requirement
maps to, and Section 3.3 states that `e90^B ≤ e_req` is the same event as the step-5 condition, which it is on these
data because no suite meets a level and fails a higher one (Table 7 is monotone in every row).

**§6B, code.** Not done; the author's decision from the previous round stands. The response can only note that
every number in the paper is reproducible from the released data with the scripts in the repository.

**§6C, comparator interpretation.** Section 5.4 ends with the reviewer's sentence: the added value is the
calibrated interpretation and the decision organisation, not a different ranking of the informative features.

**§6D, highlight.** "Healthy referencing improves cross-system transfer in the tested machines."

**§6E, definition table.** Table 2.

## Reviewer E.3

1. Table 7 header changed as requested.
2. Table 6 note: "at this window length", with a pointer to Table 8.
3. Section 3.3 now says the MDE and `e90` are reported as a pair because the gap between them is the slope of the
   POD curve, with a pointer to Fig. 7.
4. Fig. 1 caption names the trial (7.4 %, 1500 rpm, 6.4 N m) and says the dashed line is the machine's pooled
   `q0.95`.
5. Highlight 4: "A decision table picks the cheapest suite with detection power 0.9 at a given extent".
6. Section 5.4 states that there is one AUC per feature, from all trials of a class against all healthy changes of
   the machine, and that each Spearman correlation is over the 33 features of one machine and class.

## Reviewer E.4

**Point 1, Rayleigh reference.** The reviewer is right, and the correction changes the message. With a Rayleigh
reference for the residual magnitudes and a folded normal for the scalar features, the empirical quantile lies
within 3 to 11 % of the parametric one for the fixed features, and the parametric rule gives the same MDE as the
empirical quantile for 29 to 32 of the 30 to 33 features per machine and class and for every residual feature.
Section 3.2 and 5.4 were rewritten: the empirical quantile is kept because it needs no shape choice per feature and
because the tails are heavier than the references (excess kurtosis of the residual magnitudes 1 to 7.5 against
0.25 for a Rayleigh variable), unevenly across speeds (0 to 10.5 by speed for the PMSG's voltage residual), as a
scale mixture over operating points would produce. Fig. 8 shows the null histograms with both references; the
kurtosis by speed is in `R4_kurtosis_by_speed.csv`. The "11 to 18 of 33" count is gone.

**Point 2, borderline verdicts.** The primary decision table (PMSG and SCIG, α = 0.95) was re-run at 10 000
resamples; Table 7 and the e90 columns derive from it. The two SCIG cells nearest the boundary read 0.036 and 0.049
at 1000 resamples, 0.040 at 10 000 and 0.002 under tap-pair resampling; no cell lies within two Monte-Carlo
standard errors of a boundary at 10 000 resamples (a marker and note are in place should one). Section 5.5 says
so and quotes the tap-pair values.

**Point 3, Table 1 fairness.** The AUC and Cohen's d rows now read "usual" under "separate healthy campaign" with
a footnote: as usually applied; both can be formed on the within-trial drift null, as Section 5.4 does, and then
differ from the SDR only in the threshold.

**Point 4, definitions.** Section 3.3 states that adequacy, `e90^B ≤ e_req`, is the same event as the step-5
condition; Fig. 2's requirement box reads "power ≥ 0.9 at e_req with support ≥ 0.95, false-alarm rate ≤ 1 − α" and
box 4 lists the share at each level, `e90` and `e90^B`.

**Point 5, interpolation.** Section 6.3: on the six inter-winding levels a log-logistic POD model puts `a90` at
3.2 % (bootstrap 95th percentile 3.7) for the PMSG's duty-cycle residual, 4.5 (4.8) for its current residual and
2.5 (3.1) for the SCIG's; the other fixed features detect every trial at every level, so the model is degenerate for
them. No supplementary figure (the paper has none).

**Inconsistencies.** (1) Conclusions and Section 6.2 corrected: the smallest inter-winding level is met on the
induction machine by every suite except the current transducers alone, which are uncertain there. (2) Table 7
header. (3) "alternatives" removed from Fig. 2, Table 3 and Fig. 3; the method says "candidates", the demonstration
"machines". (4) The introduction names `e90`. (5) Highlight 4 reworded. (6) Code: not done (above). (7) Reference 41
is kept, cited neutrally. (8) The abstract carries the impedance ratio (factor 1.7) and the transfer AUC range
(0.85 to 0.98) within 250 words.

**Status 3, absolute-change variant.** Section 5.7: the variant changes no MDE and no `e90` of the sixteen
suite–class pairs and no fixed feature except one, where two equivalent magnitude ratios swap.

**Status 6, the 59.6/60 Hz hypothesis.** Tested on the raw healthy records (Section 5.7): a joint least-squares
fit of the stator current to the fundamental and a grid-frequency component finds a second tone of 2 to 4 % of the
fundamental at 1800 rpm, but a tone 0.25 to 0.6 Hz from the fundamental fits 1 to 4 % at 1200 and 1500 rpm as well,
where a 60 Hz component itself is below 0.1 %. The tone is a slow modulation of the fundamental present at every
speed, so the hypothesis is not supported and the wider SCIG null at 1800 rpm is reported as unexplained.

**Status 7, impedance mechanism.** The data papers give the nameplate ratings (now in Table 3, rated currents
6.3 and 7.7 A) but no inductances or loop gains; the hypothesis stays stated as untested.

**Status 8, severity covariate.** Section 4.2 gives the fault current in per unit of the nameplate current per
level (inter-turn 0.23, 0.60, 0.96 for the PMSG and 0.15, 0.44, 0.73 for the SCIG; inter-winding 0.33 to 2.8 and
0.25 to 2.0), with the remark that this scale compares the machines but not the fault physics.

**Status 11, null histogram.** Fig. 8.

**Status 12, code.** Not done (above).

## Not done, and why

* Code repository: the author's decision; no code-availability statement is made.
* A coverage study of the bootstrap (E.2 Option A): not attempted; Option B was taken and the terminology
  narrowed accordingly.
* A new healthy campaign to validate the false-alarm rate: not possible on the released data; the claims are
  stated as conditional on the available screen.
* Supplementary POD figure (E.4 point 5): the paper carries no supplement; the fitted values are in the text.
