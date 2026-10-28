# Editor-style synthesis of the round-2 simulated MSSP reviews

Date: 28 October 2026. Manuscript: the shortened revision (31 pages, elsarticle preprint, 12 pt; `paper/main.pdf`
after the corrections listed at the end). Reports: `mssp_review_round2_1.md` (electrical machines and drives),
`mssp_review_round2_2.md` (change detection and FDI statistics), `mssp_review_round2_3.md` (wind-turbine
condition monitoring and PHM practice). Each reviewer had their own round-1 report, the response document with
its shortening addendum, the manuscript text with line numbers and read-only access to `results/tables/`.

## Verdict

All three recommend **minor revision** (Reviewer 1: high confidence; Reviewer 2: high on the statistics, medium
on the machine-specific interpretation; Reviewer 3: high). All three say the round-1 objections were accepted
and answered by re-analysis, that every table entry they checked reproduces from the released CSVs, and that the
31-page version is readable and complete without a supplement. What they object to is a set of sentences that
replaced removed displays and no longer matched the data, one misstatement about the WFSG in the Discussion and
Conclusions, and three substantive points (the terminal impedance reading, the pooled detectable share, the
resampling unit within a level). None of them found a verdict of the decision table or a table entry wrong.

## Reviewer claims verified against the released tables

Every discrepancy the reports raise was re-checked here with read-only queries of `results/tables/*.csv` before
any text was changed.

| # | Claim | Result |
|---|---|---|
| 1 | WFSG fault-to-stator current ratios "1.20 and 1.03" are in no table (R1 major 3, R2 check 7, R3 check 7) | **Confirmed.** `G_fault_current_3alt.csv` at 2.83 ohm: inter-turn pairs 4.66-4.84 (median 4.73), inter-winding pairs 2.24-4.74 (median 3.10); stator current about 1.1 A. Text corrected to 4.7 and 3.1. |
| 2 | Per-level spread of V2/V1 "2.7 to 14" (R1, R2, R3) | **Confirmed.** `R_pair_table.csv`, five cycles: 3.84-14.26 for V2/V1, 1.28-6.91 for I2/I1, 1.13-1.75 for the residuals. Corrected to 3.8 to 14. |
| 3 | Operating-envelope sentence: PMSG current residual falls with speed, torque factor up to 1.6 on the PMSG (R1 major 4, R2 check 9, R3 check 9) | **Confirmed.** `sdr_per_recording.csv`: 1200 to 1800 rpm medians PMSG voltage residual 5.26 to 10.02, duty-cycle residual 2.75 to 5.58, current residual 1.80 to 1.40 (share 0.67 at both); SCIG current residual 3.79 to 16.59, duty-cycle residual 9.52 to 12.20; torque factor at fixed speed up to 1.64 (PMSG) and 1.21 (SCIG). Sentence rewritten with the features named. |
| 4 | "The three nearly coincide on the voltage residual" at equal fault-to-stator current ratio (R2 check 8) | **Confirmed false on the stated axis.** Binned by ratio, the SCIG's voltage residual is 4 to 10 times the PMSG's (e.g. 18.5 against 6.5 at a ratio of 1-1.5); binned by fault current in amperes the PMSG and SCIG coincide (6.5/6.6, 13.1/14.9, 20.9/18.8, 65.8/63.7) and the SCIG's current residual is 2 to 5 times the PMSG's. Sentence rewritten accordingly. |
| 5 | Sections 6.1 and 7 say the middle inter-turn level is met on all three machines; the WFSG cells are n.t. (R2 major 3, R3 check 10) | **Confirmed.** `R_decision_table.csv`: WFSG inter-turn at 3.0 and 7.5 % untested, at 11.8 % meets (field current alone 0.924). Both passages corrected. |
| 6 | At three cycles every SCIG inter-turn suite stops at the middle level, not "its two cheapest" (R1, R2, R3) | **Confirmed.** `G_sensor_suites_3alt.csv`: MDE 7.5 for all four suites. Corrected. |
| 7 | Drive-internal suite does not reach the current transducers' inter-winding bracket on the PMSG (R1 minor 8, R3 minor 6) | **Confirmed.** `F_sensor_suites.csv`: drive-internal MDE 2.8 (share 0.96) against 3 CT (2.8, 10.1]. Corrected: same bracket for inter-turn faults, smallest level for inter-winding faults. |
| 8 | Between-trial null factor 4.6 should be 4.5 (R1, R2, R3) | **Confirmed.** `R_between_trial_null.csv`: largest ratio of the key features 4.52 (SCIG d-axis ripple). Corrected in two places. |
| 9 | Logistic baseline 0.50 should be 0.49; two-on-one AUC 0.91 (SCIG) is the all-windows value (R1, R2) | **Confirmed.** `R_transfer2_oor.csv`: 0.4947; `R_transfer3_oor.csv`: auc_oor 0.905. Corrected. |
| 10 | Pooled detectable share: at the required level itself the shares are 0.64, 0.78, 0.78 against pooled 0.88, 0.93, 0.96 (R2 major 2, R3 major 1) | **Confirmed.** `sdr_per_recording.csv`: PMSG voltage residual at the 3.0 % level 23 of 36 trials (0.64), SCIG duty-cycle residual 0.78, PMSG duty-cycle residual at the 2.8 % inter-winding level 0.78; PMSG current and duty-cycle residuals at the smallest inter-turn level 0.11 and 0.25. The pooled definition is now stated in 3.3 and the per-level shares given for the uncertain cells and in 6.2. |
| 11 | "In most resamples" is wrong for the SCIG cell (R2 minor 8) | **Confirmed** (0.82 means the joint event fails in 18 % of resamples). Reworded. |
| 12 | At alpha 0.99 the PMSG current-only suite at the middle level drops to 0.53 (R1 minor 10) | **Confirmed.** `R_decision_table_5c.csv`. Added. |
| 13 | PMSG q-axis voltage ripple inter-turn MDE moves to the middle level at eight cycles (R1, R2, R3) | **Confirmed.** `H_sensitivity_window.csv`: 11.8 at 3 and 5 cycles, 7.5 at 8. Added. |
| 14 | "Shares within about +/-15 points" understates Table 3 (R1, R2) | **Confirmed** (half-widths 10 to 26). Sentence removed; Table 3 carries the intervals. |
| 15 | Resampling unit within a level changes the SCIG drive-internal cell from 0.85 (trials) to 0.97 (tap pairs) (R2 major 1) | **Plausible, not re-run here.** The note of Table 5 now states that trials are resampled within a level with the tap pairs treated as exchangeable; a pair-resampled probability for the uncertain cells is left for the next revision (below). |
| 16 | The terminal ratio dV2/dI2 is the current regulator's closed-loop output impedance, not a blend of machine and regulator (R1 major 1) | **Accepted on the argument** (converter connected directly to the stator, no output filter stated). Section 5.2 now reads the ratio as the regulator's output impedance at the negative-sequence frequency, tied to the machine through the inductance it is tuned to, with the tuning share unverifiable without the gains. The per-speed impedance table R1 asks for is left for the next revision. |
| 17 | SCIG level currents cluster "identically" (R2 minor 12) | **Confirmed** within 3 to 8 %. Corrected to "within 8 %". |
| 18 | Yang et al. 2010, said in the response to be added, is not in the reference list (R1 M7) | **Confirmed.** The response letter overstated; the reference was not added. Noted here, not fixed. |

## What was changed in the manuscript after round 2

The eighteen items above that are marked corrected, added or accepted were applied to the text, the table notes and
the highlights (details in the response document's second addendum), together with the restorations the reviewers
asked for that cost one clause each: the rotating-frame remark on the 2fe ripple, the window-assignment rule and
the shortfall against the twice-the-fault-duration rule in Appendix A.2, the 59.6 Hz candidate cause of the 16 %
exceedance, the Wilson interval of the two-of-nine false alarms, the hard-negative counts of the transfer
experiment, the window length of Fig. 4 in the text, and a retrofit reading of the decision table in Section 6.2.
To keep the manuscript at 31 pages, restatements of equal length were removed (introduction, scope, discussion and
conclusions sentences that repeated results; the WFSG bench sentence of Appendix A.1). The build is clean (no
warnings, no overfull boxes, captions within two lines) and the Overleaf zip test-compiles to 31 pages.

## What remains for the next revision (not done here)

These are substantive requests that change analyses or add displays, and should be decided by the author:

1. **Resampling unit of the decision table** (R2 major 1): report the tap-pair-resampled probability beside the
   trial-resampled one for the four uncertain cells, or switch the within-level bootstrap to tap pairs; one run
   of `scripts/revision.py` with the unit as an option.
2. **Power at the required level** (R2 major 2, R3 major 1): either redefine DS_req at the level e_req itself in
   step 5 and Table 5, or print both shares; the per-level shares are now in the text, the definition is unchanged.
3. **Per-speed terminal impedance** (R1 major 1): a six-row table of dV2/dI2 per machine and speed (2fe = 80, 100,
   120 Hz), which would turn the bandwidth mechanism of Section 6.2 into an observation; `R_z2_complex.csv` would
   need a speed column.
4. **Per-speed table of the fixed features** (R1 major 4, R2 major 4, R3 major 2): a compact table of median SDR
   and share by speed for the four fixed features, since nothing in the paper now shows the operating envelope;
   the numbers are in `sdr_per_recording.csv`.
5. **MDE interval in Table 3** (R1 major 2, R2 minor 5): add the operating-point interval of the MDE (or
   P(MDE <= e*) from the decision table) beside the bracket; the column exists in `H_bootstrap.csv`.
6. **Smaller items**: name the pipeline licence and give the release tag in the data statement (R3); add
   Yang et al. 2010 or remove the claim from the response letter (R1); state that the data papers give no turn
   counts (R3); consider "laboratory" or "bench" in the title (R3, left to the editor); Fig. 2 is called
   decorative by R1 and R3 and kept at the author's request.

## Where to push back

* R1's reading of the terminal ratio as the regulator's output impedance holds for a converter connected directly
  to the stator; if the benches carry an output filter the machine's leakage path re-enters, and the data papers do
  not say. The new wording states the assumption.
* R3's title objection: the abstract, Section 6.3 and the conclusions now bound every claim to the benches, and the
  title names the generator types, not a field result; the editor can decide.
* R2's hard-negative count (141 and 140 windows) is small because only nine healthy trials exist per machine; it is
  now stated, and it is the reason the "0 to 5 %" firing rate carries no interval.
