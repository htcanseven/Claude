# Reviewer 1 — Condition-monitoring domain expert (simulated pre-submission review)
# Recommendation: MAJOR REVISION

## 1. Summary
The authors evaluate whether elementary mechanisms of compound induction-motor faults can be recovered when the exact combination, the compound context, and the operating condition are withheld from training, on the public MCC5-THU motor dataset (2.2 kW, 24 states, 9 bearing-plus-X compounds, 12 conditions, 288 runs), via nine independent binary constituent detectors over curated mechanism-specific feature families, a crossed protocol (recombination / one-sided / two-sided x seen/unseen conditions), run-level severity-aware splits, constant-predictor floors, run-clustered bootstrap, Holm-corrected permutation tests. Closed-set 0.913 coexists with EM 0.083-0.157; interaction +0.040 CI [0.009,0.073]; one Holm-supported score-orientation reversal, attribution deliberately open (same-state recordings separable at AUC 0.998).

## 2. Strengths
1. Central thesis (closed-set accuracy vs constituent decomposition are different abilities) is correct, timely, demonstrated rather than asserted.
2. Prior-aware evaluation (constant-predictor references) is a genuine methodological contribution.
3. Recording-sensitivity control and refusal to attribute the reversal to physics is unusually honest.
4. Leakage hygiene exemplary: run-level splits, severity-variant leakage closed, training-only calibration, clustered bootstrap, prespecified contrasts, Holm.
5. Appendix leave-one-condition-out saturation result is a valuable corrective.
6. Cross-modal suppression motivation physically sound; SKF 6205 orders correct; 2xBSF inclusion proper; normalized order-band ratios good practice.

## 3. Major comments
1. **Floor pairing inconsistent (Conclusion; Contribution 2).** Conclusion claims recall (0.630-0.694) and R_all (0.444) exceed floors "0.556 and 0.111" — but the three-constituent constant achieves R_const=0.6667 (straddled, not exceeded) and R_all=0.3333; EM 0.083-0.157 straddles the 0.111 floor. Sec 4.2 handles this correctly; Conclusion/Contribution cherry-pick. Required: per-metric maximum floors; state only micro-F1 (and R_all under recombination, marginally) clearly exceeds; superiority is a joint operating-point property.
2. **Vibration chain ambiguous.** Envelope before or after 256/rev angle resampling? If after, bandwidth is 128 orders and resonance carriers (2-8 kHz) are lost before demodulation. State order of operations, demodulation-band policy, anti-aliasing.
3. **Fixed +/-0.12-order bands do not scale with harmonic.** +/-3.3% at BPFO but +/-1.1% at 2xBPFI; roller slip is 1-2%. Widen proportionally or show peak-location histograms.
4. **Broken-bar "sideband proxies" are physically the wrong sidebands.** Classic signature is (1+/-2s)f_e (inside the carrier band); o_e+/-1, o_e+/-2 are eccentricity/torque-oscillation signatures. Slip is computable from key-phase + carrier. High broken-bar recall (0.979/0.896) may rest on eccentricity-type evidence; expected cross-fire on eccentricity constituents. Required: slip-parameterized sensitivity analysis or demonstrate what the proxies respond to; state pole count and line- vs inverter-fed.
5. **Dataset and rig essentially undescribed.** No enumeration of 24 states, severities, profiles, sensors, supply, fault seeding method; seeded-vs-natural realism unaddressed; outer-fold construction never operationally specified. Required: setup table + protocol pseudocode.
6. **Load-bearing claim only in Related Work (39% -> 0.2% winding suppression) corresponds to no experiment in the paper.** Report it (ideally as a curated-vs-concatenated ablation) or remove.
7. **Contribution 5 promises documentation the paper does not contain** ("label abbreviations", "release-level inconsistencies"). Add or delete.
8. **Code availability inconsistent with thesis.** Timestamp metadata needed to verify session controls is behind the same request barrier. Public deposit with DOI required (this reviewer).
9. **Small-sample fragility of AUC analyses.** ~12-vs-12 runs per directed comparison; 1.000/0.000 are coarse statistics. State n, add bootstrap intervals; constructive check: repeat the static-eccentricity transfer with current-only features.
10. **Per-constituent results missing.** Which constituents produce the 0.64-0.73 FA/run? Predict vu/winding cross-fire (shared sequence-ratio features; negative-sequence cannot separate supply unbalance from turn faults without voltage) and static/dynamic eccentricity confusion. Required: per-constituent precision/recall table + discussion.

## 4. Minor comments
1. Notation clash: calligraphic C for composition and condition set.
2. "Cross-modal in eight of nine" overstates eccentricity pairs (strong vibration expression at shaft orders); soften.
3. Fig. 1 node labels clipped/colliding.
4. Fig. 3 hatched vs plain empty cells unexplained.
5. Fig. 4 annotations 1-4 and diagonal undefined; x-axis nearly uninformative.
6. Fig. 5 y-axis names cryptic; state n behind 18.5%/31.4%.
7. epsilon values never given.
8. FA/run is per prediction row in one-sided regime; rename.
9. Closed-set experiment: specify features/classifier/unit (0.913 depends on it).
10. Which run lacks a timestamp (287/288), and handling?
11. Source of missing values requiring imputation?
12. Appendix "diversity > volume": single-source comparison confounds diversity with volume; only cross-profile supports diversity claim; soften.
13. Bib: missing volumes; year/key mismatches; verify song2025gzsl page field.
14. MCSA canon thin: add Thomson & Fenger; Nandi, Toliyat & Li; Bellini et al.; Randall & Antoni.

## 5. Questions
1. Line-fed or inverter-fed, pole count, open/closed loop?
2. Envelope before or after angle resampling; demodulation band?
3. Why not slip-parameterized (1+/-2s)f_e bands; what do o_e+/-k respond to on broken-bar vs eccentricity singles?
4. Which constituents dominate false additions; how often do vu and winding co-activate?
5. Why does withholding winding context halve recall while broken-bar barely matters? Winding severity metadata?
6. Unseen-condition cells: how many conditions withheld, for all classes or only compounds?
7. Does the reversal persist with current-only static-eccentricity features?

## 6. Criteria
Technically sound: largely; open issues Majors 1-4. Reproducible: not yet (Majors 5, 8). Conclusions supported: mostly; floor comparisons not as written (Major 1); one unsubstantiated claim (Major 6). References: ML lineage good; MCSA foundations underrepresented. English: very good. Data: dataset public; code/metadata not deposited.

## 7. Recommendation
**Major Revision.** Core contribution real and publishable; fix floor pairing, envelope/broken-bar physics questions, substantiate the unsupported claim, specify dataset and protocol reproducibly.
