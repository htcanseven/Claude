# Reviewer 2 (signal-based FDI, change detection, statistics, ML/PHM)

## Recommendation: Major revision

The SDR/MDE/DS framework is a sensible, well-motivated design-stage detectability measure, the demonstration is unusually careful about calibration, screening, sensitivity and code release, and the design message suits RED. But (i) the implemented MDE does not follow its own definition, and under the stated definition the headline inter-turn MDE difference between PMSG and SCIG on current-signature features disappears; (ii) the reliability screen (n = 9) removes the headline feature at three-cycle windows, so an appendix table contradicts the main text; (iii) the transfer experiment's dominant negatives are normalised in-sample under the winning rule; (iv) the text misstates what the code does in two places and several text/table numbers disagree. All of this is fixable by re-running the released pipeline and rewriting, provided the claims are scaled to one machine per alternative.

## Summary

The paper makes diagnosability a criterion in architecture selection. Per (alternative, feature, trial) it divides the relative change of an interval-mean feature between a healthy reference and a faulted interval by the 95th percentile of the analogous no-fault change pooled over all trials of the alternative (the signal-to-drift ratio); SDR >= 1 is read as "detectable at about 5 % per-trial false alarm". From it follow a minimum detectable extent (smallest extent whose median SDR over operating points reaches one), a detectable share, a signature-location statistic and a reliability screen on healthy trials, inside a six-step co-selection procedure with a transfer test. The demonstration uses three open benchmark generators (PMSG, SCIG, WFSG) under identical tapped winding faults, five observation suites and 31 features, with window-length/quantile sensitivity, trial-level bootstrap intervals and GBDT/logistic transfer experiments under three feature-referencing rules; its headline is that the cheapest adequate suite is architecture-specific and that detectors transfer only when self-referenced.

## Major comments

**M1. The MDE implementation deviates from its definition, and the headline changes when fixed.** Sec. 3.3 defines MDE through the median SDR over operating points at extent e, but `compare3.min_detectable` groups by the raw floating-point `sev_pct` (a difference of tap positions), so extents the paper treats as identical (2.8/2.8, 7.4/7.4/7.4, 11.6/11.6 %) become separate levels: `C_min_detectable_severity.csv` has 11 "levels" for 8 distinct inter-turn extents, i.e. the MDE is a per-tap-pair minimum over 9 trials. Re-grouping by extent rounded to 0.1 % (my check on `sdr_per_recording.csv`), the SCIG inter-turn MDE through I2/I1 becomes 7.4 %, identical to the PMSG's, and the PMSG V2/V1 MDE becomes 3.8 %. The SDR is also non-monotone across levels (SCIG inter-turn V2/V1 and PId 2fe: 2.7 % detectable, 2.8 and 3.8 % not), so "min over e" rewards one lucky tap pair. The Discussion's "7.4 % on the PMSG and 2.8 % on the SCIG" rests on this. Fix: pool equal extents; define MDE as the smallest extent above which every tested level is detectable (limit-of-detection convention) or report both; re-derive the MDE tables and abstract, and let the SDR ratios and shares, which survive, carry the message.
Addressable: re-analysis of existing data

**M2. The reliability screen is fragile and silently removes the headline feature at three cycles.** With tau = 0.2 and 9 healthy trials, 1/9 passes and 2/9 fails; a feature at the nominal 5 % rate fails with probability 7 %, one at a true 20 % passes with probability 44 %. V2/V1 fires on 1/9 healthy PMSG trials at five cycles (`B_sdr_by_feature.csv`) and 2/9 at three (`summary3.md`), so Table [tab:suites3] shows the PMSG "3 CT + 3 VT" suite with I2/I1 at 7.4/9.7 %, contradicting Table [tab:suites] (V2/V1, 2.8/2.3 %) and the abstract. Sec. 5.7 claims robustness to window length from Table [tab:sens], which does not apply the screen. Fix: state the flip; report the healthy false-alarm count with a binomial interval instead of a hard exclusion, or apply the screen consistently in the sensitivity analysis.
Addressable: re-analysis of existing data

**M3. The "about 5 % per-trial false alarm" reading needs qualification.** (a) Eq. (1) references the mean over R; the code references R2 only (`delta = (flt - pre_l)/|pre_l|`), the better-matched choice, but it must be stated. (b) The pooled null is a mixture over operating points: exceedance of q95 by speed is 0–16 % in my check (SCIG I2/I1: 0/0/16 % at 1200/1500/1800 rpm; PMSG I2/I1: 1/13/1 %), so 5 % holds only on average, which matters because Sec. 5.4 reads the speed dependence as fault physics. (c) The PMSG/SCIG faulted interval starts 30 ms after the command and so contains about 60 ms of pre-fault data plus the transient (relay delay 85–90 ms), whereas the WFSG interval starts at the measured onset; this favours the WFSG. Fix: correct (a); report exceedance per operating point or use per-speed quantiles; start F at the measured onset everywhere (`t_onset` exists); report the healthy-trial false-alarm count (0–2 of 9 for the key features) with its interval.
Addressable: re-analysis of existing data

**M4. Position the SDR against standard statistics.** With a roughly Gaussian null, q95(|delta0|) ~ 1.96 sigma, so SDR >= 1 is a two-sided level-5 % test on the shift of interval means with known change time: the fixed-sample (Shewhart-type) mean-shift test, the known-onset special case of the GLR in Basseville and Nikiforov (1993, Ch. 2). The SDR is a trial-level standardised effect size (Cohen's d on interval means over 1.96), DS is empirical power, and DS at alpha is one ROC point. Saying so justifies SDR >= 1, makes explicit that the SDR assumes an oracle onset and full-interval averaging (the Introduction's "how early?" is never answered), and resolves the contradiction between Sec. 3.2 ("upper-bounds what a threshold detector can do") and Sec. 3.5 ("a detector that pools many windows can detect below SDR = 1").
Addressable: text

**M5. The transfer negatives are normalised in-sample under the winning rule.** Under "self-ref" every window is |z| against the mean/std of its own trial's PRE windows (`compare.calibrate`), and those PRE windows are the bulk of the test negatives (positives are 12 % of 73,601 windows). They are half-normal by construction and trivially separable, so the rule wins partly by construction; the WFSG (no healthy trials, F from measured onset) is the extreme case (AUC 0.99). TPR at 1 % FPR is interpolated on the test ROC, an oracle threshold set mostly by these easy negatives. A machine's healthy trials also form one GroupKFold group (`case|machine`), so four folds test without contactor-transient negatives and the fifth trains without them. Fix: normalise on the first half of PRE and evaluate on the second half, POST and healthy-FLT windows; report AUC/TPR and the FPR at the chosen threshold on healthy-FLT windows; spread healthy trials across folds; state the hyperparameters and set `random_state` (HGB's default early stopping uses an ungrouped random split, so results are not bit-reproducible).
Addressable: re-analysis of existing data

**M6. "Trials used" for the WFSG is inconsistent.** Table [tab:alternatives] and Sec. 4.2 say 198 trials at 2.83 Ohm; Table [tab:null] uses N = 618 (all impedances; `sdr_from_windows` pools every loaded record); Fig. [fig:features], Table [tab:topfeat] and the DS column of Table [tab:suites3] use 180/258 trials at all impedances, while the MDE column uses the 2.83 Ohm subset, which covers only 8 of 24 tap pairs (inter-turn >= 11.6 %, inter-winding <= 10.6 %). The WFSG inter-turn DS of 78–82 % therefore includes 1 Ohm trials at 2.7–7.7 %. Fix: one table of tap pairs and trial counts per impedance and class; state per table/figure which set is used.
Addressable: text

**M7. The relative change is ill-conditioned for near-zero features.** SCIG torque-transducer nulls are q95 = 7–21 (a 700–2100 % "healthy" change, `sdr_null_q95.csv`), and the oracle median SDR of the SCIG "+ torque" suite doubles (8.8 to 13.7, 92 to 175, `F_sensor_suites.csv`) although each torque feature's own median SDR is below 0.15: heavy tails, not signal. The relative change is also asymmetric (decreases bounded by -1). Fix: use |ln(phi_F/phi_R)| or a floored denominator; flag features with null q95 > 1 as uninformative; screen oracle statistics too.
Addressable: re-analysis of existing data

**M8. Multiplicity in the oracle variant.** The oracle takes the maximum SDR over up to 27 features per trial; under independence the null exceedance of the maximum is 1 - 0.95^k (about 70 % for k = 24), so oracle DS is neither at 5 % false alarm nor a calibrated upper bound. Fix: calibrate on the max statistic or report the oracle false-alarm rate on healthy trials beside it.
Addressable: re-analysis of existing data

**M9. Bootstrap units.** 108 trials are resampled as exchangeable, but they are 12 tap pairs x 9 operating points; a cluster bootstrap over tap pairs is the right unit for fault-class statements, and the SCIG/PMSG ratio should resample matched pairs. q95 is held fixed inside the bootstrap though estimated from the same trials; re-estimate it per resample. Percentile intervals for 100 % shares are [100, 100]; use Wilson or Clopper–Pearson (108/108 gives [96.6, 100]). MDE intervals such as 7.4 [2.7, 7.4] overlap completely between machines and must be stated wherever MDEs are compared.
Addressable: re-analysis of existing data

**M10. Claims exceed n = 1.** Sec. 6.4 is honest that the differences are between three machines with different sensing chains and sampling rates and that impedance and extent are confounded on the WFSG; the abstract, Sec. 6.2 and Conclusions nevertheless state topology-level properties ("decisive for the PMSG and superfluous for the SCIG"). Scale the wording to the units tested; the sensitivity analysis covers the tuning constants but not the screen (M2) or the F-interval definition (M3c).
Addressable: text (a population-level ranking is Not addressable without new experiments)

## Minor comments

m1. `\label{tab:suites}` is defined twice (demo.tex and tab_suites.tex); Secs. 4.3 and 5.5 resolve to one table. Addressable: text
m2. V2/V1 (external VTs per Table [tab:suites]) is grouped under "dq/controller" (`GROUP_OF`), so "controller group strongest in 75/90 % of PMSG trials" is misleading; V_dc std is labelled "mechanical". Addressable: re-analysis of existing data
m3. Sec. 5.7 "raises the median SDR by 10–20 %": the CSV gives -25 % (PMSG I_d 2fe) to +50 % (SCIG V2/V1 inter-turn); "at most nine percentage points" holds only relative to the baseline (full spread 13 points). Addressable: text
m4. Sec. 5.3 "monotonically (Spearman 0.69–0.95)": the CSV includes 0.51 (PMSG inter-turn PId 2fe), and Spearman < 1 is not monotone. Addressable: text
m5. Table [tab:null] caption (N = 618) contradicts Sec. 4.4 ("198 records"); see M6. Addressable: text
m6. Appendix A claims std, 1fe and 2fe for all synchronous-frame quantities; the code computes std only for currents/PI/torques, 1fe only for currents/torques, 2fe only for voltages. State which WFSG channels are measured versus commanded (`Va_conv_gen` serves as terminal voltage; T_e is P/omega). Addressable: text
m7. Unstated constants: WFSG onset threshold max(0.3 A, 6 sigma over 0.05–0.40 s) on a 10 ms RMS, off at first RMS below threshold after t_on + 0.05 s; POST offsets (0.30/0.15 s); PMSG/SCIG onset threshold 0.5 A; bootstrap seed; per-window f_e fallback outside 0.5–1.5 f_e0; windows per interval at the lowest WFSG speed. Addressable: text
m8. Sec. 5.6 gives 0.65–0.71 and 0.83–0.91 for the current-only suite; Table [tab:suitetransfer] has 0.72/0.65 and 0.92/0.83. Addressable: text
m9. PMSG inter-turn I2/I1 DS is 57 % in Sec. 5.2 and 56 % in Tables [tab:mde]/[tab:suites] (0.565). Addressable: text
m10. Healthy-z logistic S->P AUC 0.39 (below chance) deserves a sentence: target-scaling can be actively harmful. Addressable: text
m11. Cosine similarity of logistic weights (-0.04) is scale-dependent (machine-specific z units, C = 0.3); compare feature rankings by median SDR instead. Addressable: re-analysis of existing data
m12. Citing Lei et al. (2020), a review, for the GBDT is odd; cite Friedman (2001) or scikit-learn. Addressable: text
m13. Table [tab:alternatives]: "2.5 kVA" (PMSG) versus "2.5 kW" (SCIG); the text says 2.5 kVA for both. Addressable: text
m14. Sec. 5.2 points to Table [tab:topfeat] for the field-current result, which is in Table [tab:suites3]; PIq 2fe (median SDR 1.8, 63 %) outranks V_q 2fe for PMSG inter-turn faults but is omitted. Addressable: text
m15. WFSG inter-turn n is 176 in Table [tab:topfeat] and 180 in Table [tab:suites3] (NaN SDRs dropped versus counted undetectable). Addressable: re-analysis of existing data

## Numerical consistency check

Passed: Tables [tab:null], [tab:mde], [tab:boot], [tab:transfer], [tab:transfer3], [tab:groups], [tab:suites3], [tab:opgrid] against their CSVs (every cell); the SDRs, shares, ratios and AUCs quoted in Secs. 5.2–5.6; "four of nine" healthy firings; nine excluded features; fault-current ratios 1.86/0.80, 1.05/0.78, 0.85/0.73; the "quarter" reduction at alpha = 0.99.

Inconsistencies:
1. WFSG trial count: 198 (Table [tab:alternatives], Sec. 4.4) vs 618 (Table [tab:null], code) vs 180/258 (Table [tab:suites3] DS, Table [tab:topfeat]).
2. Eq. (1) reference R vs code reference R2 (`pre_l`).
3. Sec. 5.7 "10–20 %" vs -25 % to +50 % in `H_sensitivity_window.csv`.
4. Sec. 5.7 "at most nine percentage points" vs a 13-point spread (PMSG inter-turn I2/I1, 0.519–0.648).
5. Sec. 5.3 Spearman "0.69–0.95" vs 0.51 in `C_min_detectable_severity.csv`.
6. 57 % (text) vs 56 % (tables) for PMSG inter-turn I2/I1 DS.
7. Sec. 5.6 "0.65–0.71" / "0.83–0.91" vs Table [tab:suitetransfer] 0.72/0.65 and 0.92/0.83.
8. Table [tab:suites3] (3 c) PMSG 3 CT + 3 VT: I2/I1, 7.4/9.7 % vs Table [tab:suites] (5 c): V2/V1, 2.8/2.3 % (screen flip, unexplained).
9. Table [tab:groups] "mechanical" group represented by V_dc std.
10. Table [tab:alternatives] kVA/kW.
11. Duplicate label `tab:suites`.
12. Sec. 5.7 names two moving inter-turn MDEs; SCIG inter-winding V_q 2fe also moves (9.7/2.3/9.7 %).
