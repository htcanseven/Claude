# Response to the simulated MSSP reviews

Revision of 24 October 2026. Every comment of the three reports (`mssp_review_1_machines_signal_processing.md`,
`mssp_review_2_statistics_fdi.md`, `mssp_review_3_wind_phm_practice.md`) is listed with the action taken and where
the manuscript changed. The raw data were re-acquired, the feature caches re-extracted with the new phasor-residual
features, and every table and figure regenerated; numbers quoted below are those of the revised manuscript.

## Changes that answer several reviewers at once

| Change | Answers |
|---|---|
| Phasor-residual sequence features (magnitude of the complex change of the phase-referenced negative-sequence ratio) added for currents, voltages and duty cycles; the magnitude ratios are kept for comparison, and a new subsection and table report the inter-turn results per faulted phase | R1 major 1; R3 major 7 |
| Physical extent levels defined from the measured fault current (tap pairs with equal currents short the same turns); MDE evaluated on the levels and reported as a bracket; bootstrap over tap pairs for shares and medians, with the null quantile re-estimated in every resample | R1 major 2; R2 majors 1, 2, 5a; R3 major 2 |
| Decision table rebuilt: probabilities printed, verdict on the joint event (MDE within the requirement and detectable share at least 0.9 above it), fixed feature re-selected inside every resample, verdicts monotone over nested suites, PMSG and SCIG at five-cycle windows, WFSG at three | R2 major 3; R3 major 2 |
| Decomposition of the SCIG/PMSG ratio repeated in absolute units; the duty-cycle "no sensor" argument withdrawn | R1 major 3; R3 major 7 |
| Oracle reported at a calibrated threshold (null of the maximum statistic); empirical false-alarm counts with Wilson intervals for every fixed feature; the screen's power stated; alpha translated into false alarms per unit time | R2 major 4; R3 major 3 |
| Transfer experiment: per-operating-point commissioning baseline added as a fourth referencing rule, TPR at 1 % FPR reported beside the AUC, cluster-bootstrap intervals over trials, "only" withdrawn, the self-referenced rule described as an abrupt-onset detector | R1 major 6; R2 major 7; R3 major 6 |
| Abstract, highlights, Sections 5 and 6 and the conclusions rewritten from the new tables; the voltage-transducer claim restricted to inter-winding faults; the WFSG presented as a third case at matched extents with its differences listed; claims bounded to the benches | R1 majors 2, 5; R2 major 6; R3 majors 4, 8; all minors on wording |
| Literature: Cruz and Cardoso 2001, Arkan et al. 2001, Tallam et al. 2007, Zafarani et al. 2018, Shah, Nandi and Neti 2009, Henao et al. 2014, Cheng, Zhang and Habetler 2011, Hang et al. 2015, Yang et al. 2010 and Hanley and McNeil 1982 added (each verified against its DOI); the DFIG assertion rewritten | R1 major 7; R2 major 1; R3 major 1 |
| Length: Section 6.3 removed, Sections 2.3 and 3.5 shortened, duplicate AI sentence removed, stale table notes removed, Fig. 1 layout fixed | R1 presentation; R3 major 8, minors 4, 5, 10 |

## Reviewer 1 (electrical machines and drives)

**Major 1, magnitude sequence features and the faulted phase.** Accepted. The phasor residuals were added to the
feature set and the window cache (Section 4.3, Appendix A.1), the inter-turn results are reported per faulted phase
(new Section 5.3, Table 5, Fig. 6), and the residual features replace the magnitude ratios in the MDE table, the
decision table and Fig. 5. The 2fe ripple of the dq currents is stated to be the same negative-sequence current in
the rotating frame (Section 5.2). RESULT-PHASE

**Major 2, extent levels and the headline MDE.** Accepted. Section 4.2 now defines physical extent levels from the
fault current (three inter-turn and five inter-winding levels), the MDE is a bracket on those levels (Section 3.3,
Tables 5 and 6), the shares carry tap-pair cluster-bootstrap intervals instead of Wilson intervals, and the
abstract, highlights and Section 6 no longer claim a 3.8 % inter-turn MDE. RESULT-MDE

**Major 3, decomposition as an artefact of the relative normalisation.** Accepted in part. Table 4 now gives the
decomposition in the relative form and in absolute units side by side; the text reports both and withdraws the
"factor 35" and the duty-cycle "involves no sensor" argument (D2/D1 fails the screen on the SCIG and is dropped
from the decomposition). The qualitative conclusion is kept where the absolute form supports it. RESULT-DECOMP

**Major 4, the incremental negative-sequence impedance and the missing drive parameters.** Accepted in part. The
impedance is now computed from the complex phasor residuals (Appendix table, Section 5.2) and compared with the
passive negative-sequence impedance in per unit; the current-loop gains, bandwidths, switching frequencies and the
observer structure are not given in the data papers, which the manuscript now states (Table 2 note, Section 6.4),
and the 10 Hz direct-drive statement is marked as a mechanism rather than a prediction (Section 6.2).

**Major 5, the WFSG and "identical faults".** Accepted. "Identical faults" is replaced by "the same tapped
short-circuits" with the bench differences (resistance, duration, converter, sampling, voltage sensing) listed
where the WFSG is introduced; its inter-turn shares are reported at the matching impedance only and compared with
the PMSG/SCIG shares at the same extents; the variable-speed dataset holds no healthy records (confirmed from the
inventory), which Section 4.1 now says explicitly.

**Major 6, known-onset self-referenced detection and the transfer claim.** Accepted in part. The commissioning
baseline numbers are now given beside every self-referenced one (Section 5.8, Table A.3, Table 8), the TPR at 1 %
FPR is reported with intervals, the self-referencing rule is defined in operation and named an abrupt-onset
detector (Section 3.2, Section 6.1), and "transfers only" is withdrawn.

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
4.4 (the rule is stated as a recommendation that the benches miss by 6 %). 7: the screen's power and the Wilson
interval of the false-alarm count are stated (Sections 3.2 and 5.8). 8: the 1800 rpm null exceedance of I2/I1 on the
SCIG is noted with the near-coincidence of 59.6 Hz and the 60 Hz grid as a possible cause (Section 5.5). 9: the
parameters the data papers give are in Table 2; those they do not give are listed as unknown. 10: the stray label
is removed and every reference was re-checked against Crossref.

## Reviewer 2 (change detection and FDI statistics)

**Major 1, statistical identification of the SDR.** Accepted. Section 3.2 now describes the SDR as a mean-shift
statistic studentised by an empirical quantile of its own drift null, relates it to d', to the fault-to-noise ratio
of model-based FDI and to the per-feature AUC, withdraws "Cohen's d divided by 1.96", reports q95/1.96 sigma and
the excess kurtosis of the null (Table A.5), and the null quantile is resampled in every bootstrap (Appendix A.2).
RESULT-NULLQ

**Major 2, MDE on the coarse grid.** Accepted. The MDE is evaluated on physical levels and reported as a bracket;
tap pairs are the resampling unit of the shares and medians; the dependence on tap-pair location within a level is
shown in Fig. 6 and Table 5 (per-phase table). The regression alternative is noted as future work (Section 6.4).

**Major 3, decision-table semantics and the headline claim.** Accepted. The verdict is now the bootstrap
probability of the joint event with a stated power (DS >= 0.9 above the requirement), the fixed feature is
re-selected inside the bootstrap, the null is resampled, probabilities are printed (Table 7), verdicts are monotone
over nested suites, and the abstract follows the table. RESULT-DECISION

**Major 4, reliability screen and false-alarm claims.** Accepted. The screen's size and power are stated, the
false-alarm count of every fixed feature appears in Tables 6, 7 (note) and A.1 with Wilson intervals in the text,
the oracle is calibrated on the null of the maximum (Section 3.2), and the sentence on the number of screened
features notes the chance expectation.

**Major 5, intervals and verified inconsistencies.** (a) Table 5 carries the cluster-bootstrap intervals. (b) Table
4 and Table 5 use the same estimator, the ratio of full-sample medians, with the bootstrap interval. (c) The nested
selection sentence is corrected from the table.

**Major 6, overclaims.** Accepted. "Detector-free" became "requires no model and no trained detector"; "needs no
dedicated healthy recordings" is withdrawn (the screen needs them); the decomposition and the between-trial null are
summarised in the abstract and beside the MDEs; the WFSG rows are marked provisional in the tables and the
figure captions.

**Major 7, transfer experiment.** (a) Cluster-bootstrap intervals over trials for AUC and TPR (Tables 8 and A.4).
(b) The share of hard negatives is stated with the metrics. (c) TPR at 1 % FPR is reported throughout and the
transfer claim tempered. (d) The per-operating-point commissioning baseline is the fourth referencing rule. (e)
Step 6 is described as the operational form of the SDR's referencing assumption, with the slowly growing fault as
the stated limitation. (f) The ranges quote cross-machine entries only. RESULT-TRANSFER

**Minors.** 1: fixed. 2: the Table A.2 sentences are rewritten from the table. 3: the oracle false-alarm range is
quoted for the suites it refers to. 4: R1 and R2 no longer overlap. 5: the composition of the null pool is stated.
6: MDE endpoints are tested levels. 7: Fig. 4 and Fig. 5 captions name the WFSG pooling; the impedance markers are
in the legend. 8: the range is corrected; "trial" is used throughout.

## Reviewer 3 (wind-turbine condition monitoring and PHM practice)

**Major 1, novelty.** Accepted in part. Section 2.1 and Table 1 position the SDR against d', the Fisher score and
the per-feature AUC, and the introduction presents the calibration, the derived quantities, the selection step and
the three-machine comparison as the contribution; the per-feature AUC of the window features is reported as a
threshold-free companion in the transfer tables rather than as a second ranking.

**Major 2, the decision table.** Accepted: (a) stated power; (b) probabilities printed; (c) monotone over nested
suites; (d) five-cycle windows for the PMSG and SCIG, three for the WFSG; (e) WFSG cells marked as unscreened.

**Major 3, the false-alarm side.** Accepted: false-alarm counts in the suite tables, the power of the screen stated,
alpha translated into false alarms per unit time, every MDE labelled a bench quantity (Section 3.6).

**Major 4, relevance to multi-megawatt generators.** Accepted in part. Section 6.4 states the resistor-limited
signature law, the absence of turn counts in the data papers, the exact scaling rule the data paper gives and the
unmatched frequency and bandwidth ratio; the abstract and highlights carry the bench qualification; the title is
kept because the three generator types are what was compared, with "laboratory benches" stated in the abstract.

**Major 5, cost ordering and availability of drive quantities.** Accepted in part. Section 4.3 states the two
scenarios (OEM-integrated monitor and third-party retrofit) and the limitations say which suite is cheapest in each;
the table prints all suites with their probabilities, so the reader can apply either cost model.

**Major 6, the transfer result.** As for Reviewer 2 major 7: TPR with intervals, the per-operating-point baseline,
the abrupt-onset label, "only" withdrawn.

**Major 7, signature versus silence.** As for Reviewer 1 major 3: absolute-unit decomposition, "not the controller"
withdrawn, the three-physical-events finding stated as a property of resistor-limited emulation.

**Major 8, length and scope.** Section 6.3 removed, Sections 2.3 and 3.5 shortened; Fig. 1 and the list in 3.4 are
both kept because the figure carries the data flow and the list the default rules; Fig. 2 is kept at the author's
request; Table 8 collapsed to the out-of-reference metrics; the appendix tables kept as the evidence the reviewers
ask for.

**Major 9, limitations.** Added to Section 6.4: fixed thermal state, absent nuisance transients, per-speed
false-alarm rates, the 50 %-power MDE, nine healthy trials, the WFSG trials with few windows, the between-trial
null as the realistic one; the AUCs now carry intervals.

**Minors.** 1 to 3: corrected from the tables. 4: stale notes removed. 5: Fig. 1 fixed; Fig. 5 legend carries the
impedance markers and the SDR = 1 line is labelled in the caption. 6: the group is renamed "mechanical / DC link".
7: highlights and abstract rewritten. 8: Section 5.5 names the fixed features. 9: the two 0.95 values are
distinguished (null quantile alpha, bootstrap confidence); the duty-cycle sentence is removed; the suite-versus-MDE
comparison is reworded. 10: the duplicate AI sentence is removed; the stray label fixed; the two self-citations
are kept only where they support the statement that learned detectors are developed per machine. 11: the licence
is named and the tagged commit given in the data availability statement.
