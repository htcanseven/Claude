# Response to the simulated MSSP reviews

Revision of 25 October 2026. Every comment of the three reports (`mssp_review_1_machines_signal_processing.md`,
`mssp_review_2_statistics_fdi.md`, `mssp_review_3_wind_phm_practice.md`) is listed with the action taken and where
the manuscript changed. The raw data were re-acquired, the feature caches re-extracted with the new phasor-residual
features, and every table and figure regenerated; numbers quoted below are those of the revised manuscript.
Table and figure numbers refer to the revised manuscript: Tables 1 (positioning), 2 (alternatives), 3 (suites),
4 (decomposition), 5 (per-phase results), 6 (MDE), 7 (suites), 8 (decision table), 9 (transfer), A.1 (three
alternatives), A.2 (sensitivity), A.3 (between-trial null), A.4 (null quantile), A.5 (three-way transfer);
Figs. 1 (procedure), 2 (generator systems), 3 (faults), 4 (SDR by feature), 5 (per tap pair and phase), 6 (SDR
against extent and severity).

## Changes that answer several reviewers at once

| Change | Answers |
|---|---|
| Phasor-residual sequence features (magnitude of the complex change of the phase-referenced negative-sequence ratio) added for currents, voltages and duty cycles; the magnitude ratios are kept for comparison, and a new subsection, a table and a figure report the inter-turn results per faulted phase and per tap pair | R1 major 1; R3 major 7 |
| Physical extent levels defined from the measured fault current (tap pairs with equal currents short the same turns); MDE evaluated on the levels and reported as a bracket; bootstrap over tap pairs for shares and medians, with the null quantile re-estimated in every resample | R1 major 2; R2 majors 1, 2, 5a; R3 major 2 |
| Decision table rebuilt: probabilities printed, verdict on the joint event (MDE within the requirement and detectable share at least 0.9 above it), fixed feature re-selected inside every resample, verdicts monotone over nested suites, requirements evaluated at the tested levels with untestable cells marked, PMSG and SCIG at five-cycle windows, WFSG at three | R2 major 3; R3 major 2 |
| Decomposition of the SCIG/PMSG ratio repeated in absolute units; the duty-cycle "no sensor" argument withdrawn; "entirely a quieter null" restricted to the stator current | R1 major 3; R3 major 7 |
| Oracle reported at a calibrated threshold (null of the maximum statistic); empirical false-alarm counts with Wilson intervals for every fixed feature; the screen's size and power stated; alpha translated into false alarms per unit time | R2 major 4; R3 major 3 |
| Transfer experiment: per-operating-point commissioning baseline added as a fourth referencing rule, TPR at 1 % FPR reported beside the AUC, cluster-bootstrap intervals over trials, "only" withdrawn, the self-referenced rule described as an abrupt-onset detector | R1 major 6; R2 major 7; R3 major 6 |
| Abstract, highlights, Sections 5 and 6 and the conclusions rewritten from the new tables; the voltage-transducer claim restricted to inter-winding faults at the smallest level; the WFSG presented as a third case at matched extents with its differences listed; claims bounded to the benches | R1 majors 2, 5; R2 major 6; R3 majors 4, 8; all minors on wording |
| Literature: Cruz and Cardoso 2001, Arkan et al. 2001, Tallam et al. 2007, Zafarani et al. 2018, Shah, Nandi and Neti 2009, Henao et al. 2014, Cheng, Zhang and Habetler 2011, Hang et al. 2015, Yang et al. 2010 and Hanley and McNeil 1982 added (each verified against its DOI); the DFIG assertion rewritten | R1 major 7; R2 major 1; R3 major 1 |
| Length: Section 6.3 removed, Sections 2.3 and 3.5 shortened, duplicate AI sentence removed, stale table notes removed, Fig. 1 layout fixed | R1 presentation; R3 major 8, minors 4, 5, 10 |

## Reviewer 1 (electrical machines and drives)

**Major 1, magnitude sequence features and the faulted phase.** Accepted. The phasor residuals were added to the
feature set and the window cache (Section 4.3, Appendix A.1), the inter-turn results are reported per faulted phase
and per tap pair (new Section 5.3, Table 5, Fig. 5), and the residual features replace the magnitude ratios in the
MDE table (Table 6), the suite and decision tables (Tables 7 and 8) and Fig. 6. Result: within a physical level the
magnitude ratios spread by a factor 2.7 to 14 (V2/V1) and 1.3 to 7 (I2/I1) between tap pairs, the residuals by 1.1
to 1.8; on the residuals the two machines are indistinguishable through the terminal voltage (SCIG/PMSG ratio of
median SDR 1.01 [0.68, 1.29]) and differ through the stator current (3.7 [2.1, 5.1]). The 2fe ripple of the dq
currents is the same negative-sequence current in the rotating frame; the dq features are kept as controller
observables because they are what the drive sees (Section 5.2).

**Major 2, extent levels and the headline MDE.** Accepted. Section 4.2 now defines physical extent levels from the
fault current (three inter-turn and six inter-winding levels), the MDE is a bracket on those levels (Section 3.3,
Tables 6 and 7), the shares carry tap-pair cluster-bootstrap intervals instead of Wilson intervals, and the
abstract, highlights and Section 6 no longer claim a 3.8 % inter-turn MDE. Result: through the voltage residual the
PMSG detects the smallest inter-turn level (2.7 to 3.8 %; share 88 % [74, 98]) and the SCIG the levels from 7.4 %
up; through the current residual the roles reverse; for inter-winding faults both machines detect the smallest
level through the voltage residual and the PMSG only from 9.7 % through the current residual.

**Major 3, decomposition as an artefact of the relative normalisation.** Accepted in part. Table 4 now gives the
decomposition in the relative form and in absolute units side by side; the text reports both and withdraws the
"factor 35" and the duty-cycle "involves no sensor" argument (the duty-cycle magnitude ratio fails the screen on
the SCIG; the duty-cycle residual, which passes it, is kept). Result: for the voltage residual the ratio is 1.01
relative and 0.93 absolute; for the current residual 3.7 and 4.7 with numerator ratios 0.71 and 0.78, so the SCIG
wins there by a null 5 to 6 times quieter; for the d-axis ripple 16 and 13.5 with a numerator ratio of 0.37 in the
relative form but 1.9 in amperes (null 45 and 7.0 times quieter), so for the controller quantities the "only by
silence" reading was an artefact of the relative normalisation, which the manuscript now says (Sections 5.2, 6.1).

**Major 4, the incremental negative-sequence impedance and the missing drive parameters.** Accepted in part. The
impedance is now computed from the complex phasor residuals of each trial (Section 5.2: 12.7 and 12.2 ohm on the
PMSG, 7.3 and 7.4 ohm on the SCIG, 0.60 and 0.35 per unit on the 2.5 kVA, 230 V base, at angles near 0 and 65
degrees), stated to be of the order of a passive machine's leakage reactance or above it, and the regulator's
contribution is declared inseparable without the drive parameters; the current-loop gains, bandwidths, switching
frequencies and the observer structure are not given in the data papers, which the manuscript now states (Table 2
note, Section 6.3), and the 10 Hz direct-drive statement is marked as a mechanism rather than a prediction
(Section 6.2).

**Major 5, the WFSG and "identical faults".** Accepted. "Identical faults" is replaced by "the same tapped
short-circuits" with the bench differences (resistance, duration, converter, sampling, voltage sensing) listed
where the WFSG is introduced; its inter-turn shares are reported at the matching impedance only and compared with
the PMSG/SCIG shares at the same extents; the variable-speed dataset holds no healthy records (confirmed from the
inventory), which Section 4.1 now says explicitly; in the decision table its cells outside the tested range are
marked not testable instead of failed.

**Major 6, known-onset self-referenced detection and the transfer claim.** Accepted in part. The commissioning
baseline numbers are now given beside every self-referenced one (Section 5.7, Table 9; the between-trial null in
Section 5.8, Table A.3), the TPR at 1 % FPR is reported with intervals, the self-referencing rule is defined in
operation and named an abrupt-onset detector (Sections 3.2, 4.4, 6.1), and "transfers only" is withdrawn: all
three healthy-referenced rules recover most of the AUC (0.87 to 0.89 across machines against 0.61 to 0.79 in
physical units), the self-referenced rule is best on AUC in both directions (0.93 and 0.89) and on TPR in one, and
the linear detector transfers in both directions only when self-referenced.

**Major 7, suites, severity axis and literature.** (i) The extended Park's vector approach is cited for the
angle-free I2/I1 (Section 4.3). (ii) The zero-sequence voltage under FOC and the stray flux are cited in Sections
2.2 and 6.2 as routes the datasets cannot populate. (iii) The references named are added (all DOIs verified); the
DFIG sentence is rewritten around Shah, Nandi and Neti. (iv) The physical severity axis is kept as the measured
fault current relative to the stator current, with the remark that the MMF asymmetry scales with the current times
the shorted fraction, so the axis orders resistor-limited faults of equal turns correctly and is not a general
severity measure (Section 5.1). (v) The IEA scaling rule is stated as the data paper gives it (speed ratio, torque
"analogously") in Section 4.2 and in the limitations.

**Minors.** 1: the stale notes are removed and the suite ordering completed. 2: the sentence quotes the shares of
the features it names. 3: the identification with Cohen's d is withdrawn (Section 3.2). 4: the relative form is
used for every feature; the sentence on an absolute variant for noise-floor features is removed and the absolute
variant is reported as the robustness check it is (Section 5.8). 5: windows are assigned to R1 by end time and to
R2 by start time (Appendix A.1). 6: the R >= 2|F| rule and the demonstration's 0.68/0.36 s are reconciled in Section
4.4 (the rule is stated as a recommendation that the benches miss by 6 %). 7: the screen's size and power and the
Wilson interval of the false-alarm count are stated (Sections 3.2 and 5.8, Appendix A.2). 8: the 1800 rpm null
exceedance of the current residual on the SCIG is noted with the near-coincidence of 59.6 Hz and the 60 Hz grid as
a possible cause (Section 5.5). 9: the parameters the data papers give are in Table 2; those they do not give are
listed as unknown. 10: the stray label is removed and every reference was re-checked against Crossref.

## Reviewer 2 (change detection and FDI statistics)

**Major 1, statistical identification of the SDR.** Accepted. Section 3.2 now describes the SDR as a mean-shift
statistic studentised by an empirical quantile of its own drift null, relates it to d', to the fault-to-noise ratio
of model-based FDI and to the per-feature AUC, withdraws "Cohen's d divided by 1.96", reports q95/1.96 sigma (0.95
to 1.12 for the scalar features) and the excess kurtosis of the null (0.2 to 7.1; Table A.4), and the null quantile
is resampled in every bootstrap (its own 95 % interval spans a factor 1.3 to 1.5; Appendix A.2).

**Major 2, MDE on the coarse grid.** Accepted. The MDE is evaluated on physical levels and reported as a bracket;
tap pairs are the resampling unit of the shares and medians; the dependence on tap-pair location within a level is
shown in Fig. 5 and Table 5 (per-phase table). The regression alternative is noted in the limitations (Section 6.3).

**Major 3, decision-table semantics and the headline claim.** Accepted. The verdict is now the bootstrap
probability of the joint event with a stated power (DS >= 0.9 above the requirement), the fixed feature is
re-selected inside the bootstrap, the null is resampled, probabilities are printed (Table 8), verdicts are monotone
over nested suites, requirements are evaluated at the tested levels (a requirement outside a machine's tested range
is marked not testable), and the abstract follows the table. Result at alpha = 0.95: no suite meets the smallest
inter-turn level on either machine (PMSG voltage suite 0.27, SCIG drive-internal suite 0.82, both uncertain); every
suite meets the middle level on both machines; the PMSG needs voltage transducers at the smallest inter-winding
level (drive-internal 0.93, current-only 0.00) and meets with every suite from 9.7 %; the SCIG and the WFSG meet
every tested inter-winding level with every suite.

**Major 4, reliability screen and false-alarm claims.** Accepted. The screen's size and power are stated, the
false-alarm count of every fixed feature appears in Tables 7, 8 (note) and A.1 with Wilson intervals in the text,
the oracle is calibrated on the null of the maximum (Section 3.2; it exceeds the fixed feature's share in one
suite only), and the sentence on the number of screened features notes the chance expectation (0.3 per machine).

**Major 5, intervals and verified inconsistencies.** (a) Table 6 carries the cluster-bootstrap intervals. (b)
Table 4 and Table 6 use the same estimator, the ratio of full-sample medians, with the bootstrap interval. (c) The
nested selection sentence is corrected from the table (no share moves by more than six points).

**Major 6, overclaims.** Accepted. "Detector-free" became "requires no model and no trained detector"; "needs no
dedicated healthy recordings" is withdrawn (the screen needs them); the decomposition and the between-trial null are
summarised beside the MDEs; the WFSG's unscreened status and missing healthy trials are stated in every table that
contains it.

**Major 7, transfer experiment.** (a) Cluster-bootstrap intervals over trials for AUC and TPR (Tables 9 and A.5).
(b) The share of hard negatives is stated with the metrics. (c) TPR at 1 % FPR is reported throughout and the
transfer claim tempered. (d) The per-operating-point commissioning baseline is the fourth referencing rule. (e)
Step 6 is described as the operational form of the SDR's referencing assumption, with the slowly growing fault as
the stated limitation. (f) The ranges quote cross-machine entries only. Result (GBDT, out-of-reference windows,
PMSG to SCIG / SCIG to PMSG): physical units 0.79 / 0.61; all-healthy baseline 0.88 / 0.88; per-operating-point
baseline 0.87 / 0.88; self-referenced 0.93 / 0.89, with TPR at 1 % FPR 0.81 / 0.54 against 0.71 / 0.62 for the
per-operating-point baseline (overlapping intervals in the second direction); logistic regression 0.93 / 0.91
self-referenced against 0.78 / 0.64 and 0.81 / 0.50 under the two baselines.

**Minors.** 1: fixed. 2: the Table A.2 sentences are rewritten from the table. 3: the oracle false-alarm range is
quoted for the suites it refers to. 4: R1 and R2 no longer overlap. 5: the composition of the null pool is stated.
6: MDE endpoints are tested levels. 7: Fig. 4 and Fig. 6 captions name the WFSG pooling; the impedance markers are
in the legend. 8: the range is corrected; "trial" is used throughout.

## Reviewer 3 (wind-turbine condition monitoring and PHM practice)

**Major 1, novelty.** Accepted in part. Section 2.1 and Table 1 position the SDR against d', the Fisher score and
the per-feature AUC, and the introduction presents the calibration, the derived quantities, the selection step and
the three-machine comparison as the contribution; the per-feature AUC of the window features is reported as a
threshold-free companion in the transfer tables rather than as a second ranking.

**Major 2, the decision table.** Accepted: (a) stated power; (b) probabilities printed; (c) monotone over nested
suites; (d) five-cycle windows for the PMSG and SCIG, three for the WFSG; (e) WFSG cells evaluated at its matching
impedance, marked not testable outside its tested range, with its lack of healthy trials stated in the note.

**Major 3, the false-alarm side.** Accepted: false-alarm counts in the suite tables, the size and power of the
screen stated, alpha translated into false alarms per unit time, every MDE labelled a bench quantity (Section 3.6).

**Major 4, relevance to multi-megawatt generators.** Accepted in part. Section 6.3 states the resistor-limited
signature law, the absence of turn counts in the data papers, the exact scaling rule the data paper gives and the
unmatched frequency and bandwidth ratio; the abstract and highlights carry the bench qualification; the title is
kept because the three generator types are what was compared, with "laboratory-bench data" stated in the abstract.

**Major 5, cost ordering and availability of drive quantities.** Accepted in part. Section 4.3 states the two
scenarios (OEM-integrated monitor and third-party retrofit) and the limitations say which suite is cheapest in each;
the table prints all suites with their probabilities, so the reader can apply either cost model.

**Major 6, the transfer result.** As for Reviewer 2 major 7: TPR with intervals, the per-operating-point baseline,
the abrupt-onset label, "only" withdrawn.

**Major 7, signature versus silence.** As for Reviewer 1 major 3: absolute-unit decomposition, "not the controller"
withdrawn, "only by silence" restricted to the stator current, the three-physical-events finding stated as a
property of resistor-limited emulation.

**Major 8, length and scope.** Section 6.3 removed, Sections 2.3 and 3.5 shortened; Fig. 1 and the list in 3.4 are
both kept because the figure carries the data flow and the list the default rules; Fig. 2 is kept at the author's
request; Table 9 collapsed to the out-of-reference metrics; the appendix tables kept as the evidence the reviewers
ask for.

**Major 9, limitations.** Added to Section 6.3: fixed thermal state, absent nuisance transients, per-speed
false-alarm rates, the 50 %-power MDE and the required share, nine healthy trials, the WFSG trials with few windows,
the between-trial null as the realistic one; the AUCs now carry intervals.

**Minors.** 1 to 3: corrected from the tables. 4: stale notes removed. 5: Fig. 1 fixed; Fig. 6 legend carries the
impedance markers and the SDR = 1 line is labelled in the caption. 6: the group is renamed "mechanical / DC link".
7: highlights and abstract rewritten. 8: Section 5.5 names the fixed features. 9: the two 0.95 values are
distinguished (null quantile alpha, bootstrap confidence); the duty-cycle sentence is removed; the suite-versus-MDE
comparison is reworded. 10: the duplicate AI sentence is removed; the stray label fixed; the two self-citations
are kept only where they support the statement that learned detectors are developed per machine. 11: the licence
is named and the tagged commit given in the data availability statement.

## Addendum, 25 October 2026: the shortened manuscript (31 pages)

The author then asked for the manuscript to be brought to about 30 pages without supplementary material. The
55-page revision described above was shortened to 31 pages (elsarticle `preprint`, 12 pt, line numbers) by
cutting text and redundant displays; nothing was moved to a supplement and no analysis changed, so the result
tables in `results/tables/` are those of the revision. What changed relative to the revision described above:

* Body text cut from about 13,800 to 7,950 words: the background is one section; method, demonstration and
  results tightened; the operating-envelope subsection folded into the robustness subsection (now 5.7);
  Discussion and Conclusions condensed; the appendix reduced to the feature definitions and the computation
  details that the text refers to.
* Tables removed, with every number the text relies on kept in the text: the positioning table (old Table 1),
  the per-phase table (old Table 5; the per-pair spread factors and per-phase medians are in Section 5.3), the
  decomposition table (old Table 4; the SCIG/PMSG numerator, denominator and SDR ratios of the four key
  features are in Section 5.2 in the relative and the absolute form) and the appendix tables A.1–A.5
  (three-alternative suites, window and quantile sensitivity, between-trial null, null-quantile intervals,
  three-way transfer; their results are quoted in Sections 5.5–5.7 with the intervals).
* Figures: the feature-ranking figure (Fig. 4) redrawn compact; the per-tap-pair figure (Fig. 5) reduced to the
  voltage pair (magnitude ratio against phasor residual), the current pair's spread factors staying in the text;
  the severity figure (old Fig. 6) removed, its physical-severity-axis comparison stated in Section 5.4.
* References set in the size the class uses for its journal layouts; all 37 references kept.
* New numbering: Tables 1 (alternatives), 2 (suites and features), 3 (MDE), 4 (suites versus detection),
  5 (decision table), 6 (transfer); Figs. 1 (procedure), 2 (generator systems), 3 (faults), 4 (SDR by feature),
  5 (per tap pair and phase). Sections: 1 Introduction, 2 Background, 3.1–3.5 Method, 4.1–4.4 Demonstration,
  5.1–5.7 Results, 6.1–6.3 Discussion, 7 Conclusions, Appendix A.1–A.2.
