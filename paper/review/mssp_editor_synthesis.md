# Editor-style synthesis of the three simulated MSSP reviews

Date: 23 October 2026. Manuscript: `paper/main.pdf` at commit c92fdbc (43 pages, elsarticle preprint).
Reports: `mssp_review_1_machines_signal_processing.md`, `mssp_review_2_statistics_fdi.md`,
`mssp_review_3_wind_phm_practice.md`. The reviewers did not see each other's reports or the earlier
RED reports.

## Verdict

All three recommend **major revision** with high confidence; Reviewer 3 adds that without a reframing
toward an experimental study with bench-bounded claims, rejection would be appropriate. The reports
converge on four points: (1) the inter-turn extent axis is confounded with the faulted phase and the
tested extents form three physical levels, not twelve, so the headline "3.8 % versus 7.4 %" claim does
not hold; (2) the inferential layer (fixed null, 50 %-power MDE, nine-trial screen, Wilson intervals,
in-sample feature selection in the decision table) claims more precision than it has; (3) abstract,
highlights and title claim more than Sections 5.7 and 6.4 admit; (4) the paper is about a third longer
than its content needs. The data, the openness and the controlled two-machine comparison are praised by
all three. The manuscript should not be submitted as it stands.

## Reviewer claims verified against the released tables

Every item below was checked with read-only queries of `results/tables/*.csv` or the built PDF.

| # | Claim | Result |
|---|---|---|
| 1 | Inter-turn SDR follows the faulted phase (R1 major 1) | **Confirmed.** Median inter-turn SDR of V2/V1 by faulted phase A/B/C: PMSG 1.6/2.8/25.3, SCIG 1.3/7.4/26.5; I2/I1: PMSG 0.8/1.7/5.6, SCIG 1.4/6.1/20.3. All four pairs at 2.7–3.8 % are phase A; the two 11.6 % pairs D13–D16 (phase A) and D17–D20 (phase C) carry the same fault current (6.01 vs 6.04 A) but V2/V1 SDR 4.2 vs 21.3 on the PMSG and 2.3 vs 33.0 on the SCIG. |
| 2 | Extent levels are three physical clusters (R1 major 2) | **Confirmed.** Fault current by case: 2.7/2.8/2.8/3.8 % all 1.41–1.44 A (PMSG) and 1.12–1.16 A (SCIG); 7.4/7.4/7.4/7.7 % all 3.74–3.77 A; 11.6–12.1 % all 6.0 A. The PMSG's "3.8 %" MDE rests on one pair (D21–D22, median SDR 1.45); the other three pairs of the same cluster give 0.26–1.17, and the 7.4 % pair D06–D07 is undetected on V2/V1 (0.51). |
| 3 | Decision table verdicts are non-monotone and the "(suite)?" notation hides probabilities (R3 major 2) | **Confirmed.** PMSG, inter-winding, e_req 12 %, alpha 0.95: 3 CT meets (p 0.965), 3 CT + 3 VT uncertain (0.872). PMSG, inter-turn, 5 %: drive-internal p 0.35 and 3 CT + 3 VT p 0.942 both print as uncertain, the table shows "(drive)?". |
| 4 | Quoted transfer ranges include within-machine entries (R2 major 7f, R3 minor 3) | **Confirmed.** Cross-machine AUC: self-referenced 0.82–0.92 (text: 0.82–0.95), commissioning baseline 0.62–0.86 (text: 0.62–0.90). Cross-machine TPR at 1 % FPR: 0.43–0.75 self-referenced, 0.02–0.54 under the baseline rule. |
| 5 | "78–98 %" WFSG inter-turn shares mix two analyses (R3 minor 2) | **Confirmed.** All-impedance fixed shares are 70–79 %; the matching-impedance shares of Table A.1 are 86–98 %. |
| 6 | D2/D1 on the SCIG fails the screen yet anchors the "no sensor" argument in Table 4 and Section 5.2 (R1 major 3, R3 minor 9) | **Confirmed.** D2/D1 fails on the SCIG at 3, 5 and 8 cycles (3, 4 and 5 false alarms of 9). The "nine times quieter controller output" sentence must go. |
| 7 | Wilson intervals understate the uncertainty (R1 major 2, R2 major 5a) | **Confirmed.** PMSG inter-turn V2/V1 share 76 %: tap-pair cluster bootstrap [55, 94] against Wilson [67, 83]; the text quotes Wilson. |
| 8 | Table 4 and Table 5 give different SCIG/PMSG ratios (R2 major 5b) | **Confirmed.** Table 4 reports the ratio of full-sample medians (1.40 for inter-turn V2/V1), Table 5 the median of the bootstrap ratio (1.10). |
| 9 | "The nested selection changes no share by more than five points" (R2 major 5c, R3 minor 1) | **Confirmed false** for the WFSG: 3 CT 98 to 86, drive-internal 91 to 87. |
| 10 | Section 5.7 misquotes Table A.2 (R2 minor 2) | **Confirmed.** Alpha 0.99 lowers shares by 0–8 points (text: 3–9) and moves one inter-winding MDE (PMSG V2/V1, 2.3 to 9.7 %) and one inter-turn MDE (PMSG Vq 2fe, 7.4 to 7.7 %), not "two inter-winding MDEs up one level". |
| 11 | Oracle false-alarm range misquoted (R2 minor 3) | **Confirmed.** Largest suites: 67 % (PMSG) and 89 % (SCIG); the text's 44–78 % are the drive-internal values. |
| 12 | Stale table notes (R1 minor 1, R3 minor 4) | **Confirmed.** Table 5 and A.1 define a dash that does not occur with that meaning; Table 7 defines "exc" and omits "+ torque"; Table A.2 carries an unused superscript note. |
| 13 | Fig. 1 box 2 overflows into box 5 (R3 minor 5) | **Confirmed** on the rendered page (the 11 pt lettering of the Elsevier version). |
| 14 | Stray "2026b" in reference 36 (R1 minor 10, R3 minor 10) | **Confirmed; fixed in this commit** (the suffix was left over from the author-year style). |
| 15 | Healthy WFSG records exist in the dataset (R1 major 5) | **Not confirmed.** The variable-speed inventory used here holds 198 fault records at 2.83 ohm and 438 at all impedances, none healthy; the title of the data paper covers the fixed-speed machine as well. Worth one sentence in Section 4.1. |
| 16 | Absolute-unit decomposition (R1 major 3, R3 major 7) | **Largely confirmed** from the healthy levels in `R_baselines_z2.csv`: the inter-turn changes of V2/V1 and I2/I1 are equal in absolute terms on the two machines (about 2.5e-4 and 1.2e-3), the SCIG's absolute nulls are 1.2 and 3.3 times quieter, not 2.6 and 4.8; the "factor 35" for the d-axis ripple is a relative-normalisation effect. The qualitative conclusion (quieter null, equal signature) survives; its magnitude does not. |

## What survives

- The signature location per machine type: V2/V1 is the strongest PMSG feature and the d-axis ripple the
  strongest SCIG feature in every faulted phase, so the relocation finding is not a phase artefact.
- The inter-winding result (all pairs in phase A): voltage transducers take the PMSG from 9.7 % (I2/I1) to
  2.3 % (V2/V1) at five cycles and add nothing for the SCIG. The inter-turn version of that claim does
  not survive at the cluster level: both machines detect the 7.5 % cluster in most pairs and neither
  detects the 3 % cluster.
- The SCIG's advantage on current and controller features is a quieter null with an equal signature,
  qualitatively; the factor is 1.2 to 6, not up to 35.
- Self-referenced detectors transfer best (cross-machine AUC 0.82–0.92 against 0.62–0.86), but "only" is
  wrong and the TPR at 1 % FPR into the PMSG (0.35–0.52) must be shown.
- Reproducibility: every number the reviewers queried reproduced from the CSVs.

## Where the author can push back

- "The SDR is Cohen's d divided by 1.96" (R2, R3): the paper says so itself; the reply is to position the
  statistic explicitly against d', Fisher score and per-feature ROC (one paragraph in 2.1 and Table 1) and
  to present the calibration, the selection step and the three-machine comparison as the contribution.
- Drive gains, bandwidths and observer structure (R1 major 4): not documented in the data papers; the
  manuscript can only state this and bound the relocation argument accordingly.
- "Known-onset detection is not condition monitoring" (R1 major 6, R3 major 6): Sections 3.2 and 6.4
  already say the quantities characterise a short-horizon change detector; the fix is to move that
  qualification into the abstract and beside every MDE, and to define the self-referencing rule in
  operation (sliding reference, horizon, reset).
- Retitling to "laboratory benches" (R3 major 4) is the author's call; the abstract and highlights must in
  any case carry the bench qualification.
- The missing references the reviewers name (Arkan 2001, Cruz and Cardoso 2001, Tallam 2007, Zafarani 2018,
  Shah, Nandi and Neti 2009, Yang 2010, Cheng, Zhang and Habetler 2011, Hang 2015, Henao 2014) are
  plausible and well known, but each must be verified against its DOI before it is added.

## Revision plan by tier

**Tier A: text, tables and figures, no re-analysis (about half a day).** Items 3 (print p_meets and
state the monotonicity rule), 4, 5, 6, 7 (cluster-bootstrap intervals in Table 5, available in
`H_bootstrap.csv`), 8 (one ratio estimator in both tables), 9, 10, 11, 12, 13, 15; re-scope the
abstract, highlights, Sections 5.3, 5.5, 6.1, 6.2 and the conclusions: the inter-turn voltage-transducer
claim becomes an inter-winding claim, "identical faults" becomes "the same tapped short-circuits",
"detector-free" becomes "requires no trained detector", "needs no dedicated healthy recordings" is
deleted, "transfers only" becomes "transfers best"; disclose the phase confound and the three physical
extent levels as a limitation; add the limitations Reviewer 3 lists (thermal state, nuisance transients,
per-speed false-alarm rates, 50 %-power MDE, nine healthy trials, WFSG windows, no AUC uncertainty);
drop the duplicate AI sentence in 4.4; cut Sections 2.3, 3.5 and 6.3 and Fig. 2 to approach 30 pages.

**Tier B: re-analysis from the released per-trial tables (about a day, possible in this repository
now).** Inter-turn results by tap pair and phase (a new table or a panel of Fig. 5); MDE and detectable
share at the three physical levels (3, 7.5, 12 %) with tap-pair bootstrap; a decision table with the
feature selection nested in the bootstrap, verdicts monotone over nested suites and a stated power
condition (for example DS at least 0.9 for e at or above e_req); the Table 4 decomposition repeated in
absolute units for the features whose healthy levels are stored.

**Tier C: needs the raw data (about 5 GB to download) and a new feature extraction (a day or two).**
Phasor-residual sequence features (magnitude of the complex negative-sequence increment, which removes
the phase confound at its root); resampling of the null quantile inside every bootstrap; a
per-operating-point commissioning baseline for the transfer experiment; cluster-bootstrap intervals for
AUC and TPR; Westfall-Young calibration of the oracle; a five-cycle decision table for the PMSG and SCIG;
window assignment by end time. This tier answers Reviewer 1's central objection fully; without it the
inter-turn claims must be re-scoped as in Tier A.

**Tier D: out of reach with these data.** Drive controller parameters, a DFIG, replicated machines,
reactance-limited faults.

## Recommendation

Do Tiers A and B before any submission; they remove every verified error and overclaim and leave an
honest experimental paper whose inter-turn conclusions are stated at the resolution the data support.
Tier C is what would turn "major revision" into a likely accept at MSSP, because it replaces the
confounded features rather than disclosing the confound.
