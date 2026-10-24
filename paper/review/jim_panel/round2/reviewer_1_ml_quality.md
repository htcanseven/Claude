# Referee report, second round: Reviewer 1

**Manuscript:** When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing
**Journal:** Journal of Intelligent Manufacturing
**Round:** Second round (first revision)
**Reviewer focus:** Machine learning for manufacturing quality: predictive quality and virtual metrology, learned manufacturability assessment, uncertainty quantification and conformal prediction, small-data and transfer learning
**Date:** 24 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary of the revision

The paper is retitled and reframed as an exploratory, production-referenced evaluation on one laboratory deep-drawing process. It has a plain abstract, eight main rules, a schematic (Fig. 1) and a worked example. In my area the revision adds the following:

- the GP diagnostics (Section 5.4);
- a trend GP for small data (M7n: universal kriging, log-normal priors, an estimated nugget);
- an autoregressive multi-fidelity model (M7) and a friction calibration with a GP discrepancy (Mcd);
- point predictors crossed with relation-matched split-conformal intervals borrowed from the other family (P+RM);
- interval scores, cluster-bootstrap coverage and a discussion of M6;
- few-shot transfer to a new family;
- decision-time strata, per-characteristic distances (Table 6) and a design-level verdict;
- cross-fitted selection, per-family and out-of-sample guard bands, and a between-run sensitivity analysis;
- a stand-alone scoring function (`scripts/opchar.py`).

The central finding stands and is now better supported: within a family the learners reproduce production-record rules, and no simulation-based or learned rule decides closer than the nearest produced setting. The tables an appendix would have held are now result files in version 2 of the archive. Every number I checked reproduces (Section 5).

## 2. Assessment of the response to my first-round comments

| Round-1 major comment | Status | Reason (revised PDF) |
|---|---|---|
| 1. Learners reduce to the baselines | Partly resolved | Four of five requests are met: (a) the diagnostics are in the text (p. 19, ll. 858–866); (b) M7n is added (p. 7, ll. 295–299; p. 14, ll. 641–643); (d) the tuning study is reported (p. 19, ll. 871–873); (e) RQ3 is rephrased (p. 2, ll. 69–71). For (c), the crossing is computed for eight predictors, but the paper reports NN+RM only (p. 20, ll. 889–893). See Major 1. |
| 2. Multi-fidelity, discrepancy, transfer, physics-informed | Resolved | M7, Mcd and the few-shot transfer are added and scored. M1s and Mc are labelled correctly (p. 7, ll. 284, 311–313). The untested families of models are named (p. 24, ll. 1088–1092). Points on M7 are in Major 3. |
| 3. Uncertainty quantification | Partly resolved | Added: the estimated nugget, relation-matched intervals, the interval score and M6 (p. 20, ll. 899–901). Declining conformalised quantile regression is reasoned. However, the conformal guarantee is misstated, and coverage per characteristic and per stratum is only in the archive (Major 2). |
| 4. Selection on the evaluation data | Partly resolved | The exploratory status, the †/‡ marks, cross-fitting (p. 21–22, ll. 965–992) and out-of-sample bands (Table 7) are all added. Remaining: the cross-fit is reported for one criterion only; "committed to in advance" describes a post hoc rule; the frozen procedure is not deposited (Major 4). |
| 5. Pooling over characteristics | Resolved | Added: Table 6, the FA/FR sides (Table 5; p. 8, ll. 363–367), the design-level verdict (p. 22, ll. 995–998) and per-characteristic accuracy of the band (p. 21, ll. 921–923). The statement on the simulation is now consistent (p. 23, ll. 1047–1050). |
| 6. Uncertainty of the distances | Resolved | The three kinds of interval are described (p. 13, ll. 579–593). The between-run sensitivity (p. 21, ll. 960–964) and the resolvable difference (p. 22, ll. 992–994) are given, and the paired intervals are labelled descriptive. |
| 7. Title and scope | Resolved | New title; Section 6.4 is a proposal; lower limits are tested (p. 22, ll. 998–1002); attribute outcomes are discussed (p. 25, ll. 1130–1133). |
| 8. Presentation | Resolved | Plain abstract, Fig. 1, eight named rules, one compact Table 5, the renamed bound, and the M3n/M4 naming explained (p. 27, l. 1226). One dense paragraph remains (Minor 11). |

| Round-1 minor | Status | Where |
|---|---|---|
| 1 Floors per geometry | Resolved | p. 6, ll. 260–261 |
| 2 Floor leakage | Resolved | p. 22, ll. 1003–1005 (see Minor 6) |
| 3 n per relation | Resolved | Table 2 note |
| 4 One-sided distances | Resolved | Table 5 |
| 5 Resampling details | Resolved | p. 13, ll. 579–583 |
| 6 Pooled columns | Resolved | removed |
| 7 300 kN coincidence | Resolved | p. 17, ll. 775–777 |
| 8 Cup-depth false accept | Resolved | p. 17, ll. 777–779 |
| 9 Variance shares | Resolved | restricted to the pre-specified rules |
| 10 Lead sentence | Resolved | p. 19, ll. 858–866 |
| 11 Coverage table additions | Resolved | archive; p. 20 |
| 12 Sentence at old l. 1009 | Resolved | deleted |
| 13 Positioning | Resolved | p. 3, ll. 106–113; Table 1 |
| 14 Archive | Partly resolved | licence and DOI pending (p. 28, l. 1277) |
| 15 Fig. 2 | Resolved | new Fig. 5 |
| 16 Verdict counts in Fig. 4 | Partly resolved | out-of-sample intervals in the archive only |
| 17 Cost model | Resolved | Eq. (2), Fig. 6 |
| 18 ISO clauses | Partly resolved | ISO 5725-6 added; acceptable |
| 19 "Proposed reporting checklist" | Resolved | Table 9 |

## 3. The editor's required changes that concern my expertise

- **R1:** met, apart from two phrases (Majors 1 and 4).
- **R3:**
  - (a) Not met as specified. There is no table in the paper; Section 5.4 summarises the diagnostics and the table is `learn_gp_diagnostics.csv`.
  - (b) Met.
  - (c) Partly met: the crossing exists, but the paper reports NN+RM only.
  - (d) and (e) Met.
- **R4** (labels, and the recommended M7 and Mcd): met.
- **R6:** largely met. Coverage per characteristic and per decision-time stratum is only in the archive, and the archive contradicts the response letter on intervals for new settings (Minor 5).
- **R7** (validation): met in substance. For new settings, Table 7 shows the leave-one-alternative-out (LOAO) share instead of the leave-one-force-cell-out share, and the bands under the release-like prior are not validated in the paper (Major 4).
- **R8:** met; the cross-fit is reported for decisiveness only.
- **R9:** met.
- **R11** (positioning): met. The main text grew from 23 to 27 pages, and nothing moved to supplementary material (Major 5).
- **R12:** requirements, mapping, the declaration on generative AI and the history statement are met. The licence and the DOI are not.

## 4. New or remaining issues

### Major

**1. The answer to RQ3 on intervals rests on a comparison that is not like-for-like, and the crossing is reported for one predictor only** (p. 1, ll. 37–39; p. 20, ll. 889–896; p. 23, ll. 1050–1051; p. 27, ll. 1198–1201). "Intervals calibrated on the same relation in the other family, not learning, made the production record safe" compares two rules that use different information:

- NN+RM borrows the other family's errors on the same relation.
- M7n, as reported, sees only the six to nine alternatives of its own family.

The archive contains the like-for-like comparison:

- *Pooled trend GP.* M7n calibrated on both families (pooled-setting scope, with a family intercept) is safe at 2.75 floors for a new setting (1.30 interpolating, 3.05 extrapolating). It covers 86 % interpolating and 79 % extrapolating. Its extrapolation interval score is 20.9, inside the 19–24 that the paper credits to the relation-matched intervals. Its decisive distances are 11.3 and 15.3 floors, against 9.55 and 20.1 for NN+RM (`learn_resolution.csv`, `learn_intervals.csv`).
- *Same interval, different centres.* With the same relation-matched interval, the M7n and M1sn centres are more decisive than NN when extrapolating: 17.6 and 17.8 against 20.1 floors. The paired difference for M7n+RM − NN+RM is −2.55 (−2.85 to −0.25) (`learn_paired.csv`).
- *Simulation-based centres.* The relation-matched interval does not make these safe. M1s+RM and M7+RM falsely accept failing alternatives up to 151–155 floors from the limit for a new setting.

The decisiveness conclusion is robust, because an interval rule can never decide closer than its own centre used as a point rule, and the GP centres reduce to NN or M1sn. The safety conclusion is not about learning against calibration. It is about whether the rule uses evidence from the other family on how predictions fail at a new force.

*Request:*
- Report the crossing in a compact main-text table: eight predictors × relation-matched interval, giving δd/δs, the FA-side distance, coverage and interval score per relation. It would replace many of the numbers in ll. 889–906.
- Add the pooled trend GP as the learned way of borrowing across families.
- Reword the abstract, Section 6.1 and the conclusions, for example "borrowing the other family's errors on the same relation". Restrict "what made rules safe" to the production-record and trend centres.

**2. The relation-matched interval: its guarantee is misstated, and its coverage averages over characteristics and two family swaps** (p. 7, ll. 302–308; Table 2; p. 20, ll. 892–893).

- *The guarantee.* The text says the intervals "guarantee coverage only if the two families' errors are exchangeable". That condition is not sufficient. The 21–63 calibration cases of one family are strongly dependent: they come from one or two fits for a new setting or a new family, and from nine heavily overlapping fits with a sibling. They are therefore not exchangeable with a test case from the other family. In the limit of perfect dependence within a family, coverage falls to one half whatever the nominal level. With one calibration family, no distribution-free 90 % guarantee is available.
- *Per family.* The realised coverage of NN+RM is 0.95 (concave) against 0.73 (convex) with a sibling, 1.00 against 0.76 interpolating, and 0.86 against 1.00 extrapolating.
- *Per characteristic.* It is 0.61 for the dome with a sibling, 0.67 for the arm angle and the waviness when interpolating, and 0.75 for the waviness and the depth when extrapolating.
- *Per stratum.* It is 0.69 (0.52–0.88) with resolvable siblings.
- *Exchangeability.* The borrowed quantiles differ between the two directions: 4.36 against 1.98 floors for NN with a sibling, and 30.4 against 12.3 for M1s interpolating. This is direct evidence that the families' errors are not exchangeable.

*Request:*
- State plainly that no guarantee is available, and that 88 % and 93 % are empirical results of two swaps. Label the level of NN+RM as nominal in Table 2.
- Give the number of cases, alternatives and fits behind each quantile.
- Report the coverage per family, per characteristic and per stratum in the text.
- Consider a normalised nonconformity score (absolute error over a per-characteristic scale estimated in the other family), so that one quantile can serve heterogeneous characteristics.

**3. The trend GP's intervals are not diagnosed, and the multi-fidelity model's main failure is not reported** (p. 19, ll. 863–871; p. 20, l. 893; Fig. 1).

*M7n.* Its intervals cover 52 % interpolating and 56 % extrapolating. For the mid-side draw-in, the characteristic that sets the blank-holder force, coverage is 17 % and 33 %; for the waviness it is 0 % in both. The reason is visible in the archive:

- its median half-width is 2.0–2.8 floors, against 90th-percentile absolute errors of 4.6–8.8 floors for the force trend it reproduces;
- its GP amplitude (1.2–1.5 floors) is identified only from variation between lubrication patterns at produced forces, which is sibling-type information;
- its force length scale is the prior's;
- its hyperparameters are plug-in MAP estimates.

This is the relation mismatch of round 1, now inside a Bayesian model. M7n is the paper's answer to R3(b) and the illustrative rule of Fig. 1, so readers need to know which of its results (14.5/5.2 floors, 52–56 % coverage) belong to the learner and which to the prior medians fixed in this revision.

*Request:* explain the mechanism in Section 5.4 or 6.3, and add a sensitivity analysis of δd, δs and coverage to the prior medians of the length scale and the GP standard deviation (halved and doubled). Marginalising the four hyperparameters would also be cheap with six to nine points.

*M7.* It uses only the nominal simulation as its low-fidelity input. With two calibration forces that input takes two values, so the scale ρ cannot be separated from a force slope, and M7's mean extrapolates as M1s does. Its GP discrepancy did not prevent false accepts up to 118 floors from the limit on the cup depth when extrapolating (FA-side safe distance 117.7 floors; `learn_resolution.csv`, `qual_per_characteristic.csv`).

*Request:* describe M7 accordingly and report this failure next to M1s's 165 floors (p. 17, ll. 777–779; p. 23, ll. 1051–1053). It is the most useful lesson about multi-fidelity correction for this journal's readers.

**4. The reporting of selection and validation is incomplete** (p. 14, ll. 631–634; p. 21–22, ll. 965–994; Table 7; p. 21, ll. 924–927; p. 26, ll. 1178–1179).

- *Cross-fit by safety.* `qual_crossfit.csv` also selects rules by safe distance. That selection picks M1s+RM, M1sn+RM or M4+RM, and on the other geometry the selected rule is safe only at up to 18.2 floors interpolating and 11.5 extrapolating.
- *Cross-fit of step 6.* With the rule and band chosen on one geometry, the share of correct decided verdicts on the other is 0.92–0.94 extrapolating, 0.93–0.97 interpolating and 0.73 for a new family.

  Please report both cross-fits.
- *"Bounds".* The cross-fit estimates, from two folds, the optimism of the final choice among the reported rules. It cannot correct for rules designed after results on both geometries were seen. Please replace "bounds" with "estimates".
- *Table 7.* For interpolation and extrapolation the three alternatives of a cell share one fit, so leaving one force cell out is the relevant scheme. Show that share in Table 7, with its cluster interval.
- *Release-like bands.* With a force cell left out, the release-like bands give 0.72 (NN) and 0.74 (NN+RM) extrapolating, and 0.87–0.88 (M7n, M5) interpolating. Only NN's figure appears in the text.
- *"Committed to in advance"* (p. 1, ll. 34–35; p. 26, l. 1191). NN was added after the first results (†). Please write "a single rule for every relation", or similar.

**5. Where the tables went.** The archive is a sensible home for the robustness variants, the scan redundancy and the protocol checks. It is not adequate as the only home of the evidence on which the answer to RQ3 rests, nor of the tables the editor required:

- the GP diagnostics (R3a);
- the crossing (R3c);
- coverage per characteristic, stratum and family (R6);
- the simulation validation table (R4).

At present these exist only as CSV files with code names and no column dictionary. For example, `resolution_floors` stands for δd, and the `transfer` rows of `learn_resolution.csv` are in the new family's own floor, whereas Table 5 uses `learn_source_floor.csv`. The deposit has neither a DOI nor a licence. An Online Resource does not count toward the article's length, so keeping the paper at 31 pages does not require dropping the supplement, which the author has already drafted.

*Request:*
- a short Online Resource (a few pages) with these tables, captioned in the paper's terms;
- a data dictionary in `findings.md`;
- a minted DOI and a licence before acceptance.

### Minor

1. Restore the paragraph on finite-sample guarantees deleted from Section 3.3 (round 1, ll. 315–322). It gave the largest-residual and jackknife+ levels and the 1/(n+1) limit: a 5 % miss rate needs at least 19 produced alternatives in a relation. Also cite Barber et al. (2021) for the jackknife+ "guarantee of 0.78" (p. 7, l. 316; p. 20, l. 899) and Friedman (2001) for boosting. Both are in `refs.bib` but no longer cited.
2. The guard band is a selective-risk threshold chosen on the evaluation data. Cite conformal risk control (Angelopoulos et al., 2024, dropped from the text) and the "learn then test" framework of Angelopoulos, Bates, Candès, Jordan and Lei, and say why finite-sample risk control is out of reach here.
3. The interval-score sentence (p. 20, ll. 894–896) holds for the relation-matched intervals around NN, M1sn, M5n and M7n. Around M1s and M7 they score 76–155. M2n's own interval scores 14.2 when interpolating. The response letter's claim that NN+RM has "the best interval score" fails when extrapolating (24.3 against 19.1 for M1sn+RM).
4. In the archive the cluster intervals for coverage with a sibling span 0.72–0.94, not 0.71–0.94, and the interval for M3 is 0.94–0.98, not 0.93–0.98 (p. 20, ll. 897–898).
5. `qual_coverage.csv` gives cluster intervals for the interpolated, extrapolated and new-family relations, several degenerate (0.714–0.714, 0.929–0.929), although the response letter (R6) says it gives none there. Please blank or flag them.
6. Recomputing the floors without the held-out series moves M0, a main rule, by 3.75 floors, not "at most 1.4" (p. 22, ll. 1003–1005).
7. M7 is counted neither among the eight main rules nor among the "ten further rules" (p. 7, ll. 282, 309).
8. The few-shot distances (p. 20, ll. 902–906; p. 26, l. 1155) are in the new family's floor computed from all nine of its runs, which a team does not have at k = 1–3. Single-run floors range from 0.21 to 2.16 times the pooled floor. Please state this.
9. "Gets at least 93 of the other 98 right" (p. 24, ll. 1062–1064): the out-of-sample share is 0.954 (0.937–0.971), that is 92–95 of 98.
10. Table 7 shows bands pooled over the families, but step 5 prescribes per-family bands, which the worked example uses (p. 11, l. 464). Show the per-family bands or explain why the pooled ones are shown.
11. The paragraph at p. 20, ll. 889–906 holds about forty numbers. The table requested in Major 1 would absorb most of them.

## 5. Checks I ran against the archive

All checks were read-only. I did not run the pipeline. I imported only the stand-alone `opchar.py`. Nothing was written to the repository; `git status` was clean afterwards.

| Check | File(s) | Result |
|---|---|---|
| Checksums, and version 1 against version 2 | `SHA256SUMS`; round-1 list via `git show` | Confirmed: all 180 verify; only the documented files changed; the 14 checksums in the release notes match |
| Self-check of the scoring function | `opchar.py --selfcheck` | Confirmed: reproduces `dec_resolution.csv` |
| `opchar.distances` on the new rules | `learn_intervals.csv` against `learn_resolution.csv` | Confirmed: 67 of 67 rows (δd, δs, FA, FR) |
| `opchar.guard_band` and `step6` | against Table 7 | Confirmed: g, g5 and trial rate in all 18 cells |
| Table 5, all cells and intervals | `dec_resolution`, `learn_resolution`, `panel_source_floor`, `learn_source_floor`, `qual_trial` | Confirmed |
| Table 6 | `qual_per_characteristic.csv` | Confirmed |
| GP diagnostics and paired differences (Section 5.4) | `learn_gp_diagnostics`, `dec_gp`, `learn_paired` | Confirmed |
| Coverage, interval scores, M6, tuning | `qual_coverage`, `qual_m6_coverage`, `tune_decisions` | Confirmed, with Minors 3–5 |
| Mcd posterior | `learn_mcd_posterior.csv` | Confirmed: maximum at 0.05 in all 50 calibration sets |
| Coverage of P+RM and M7n per family, characteristic and stratum | `learn_intervals.csv`, `qual_coverage.csv` | New, not reported: Majors 2 and 3 |
| Crossing; pooled trend GP; M7 false accepts | `learn_resolution`, `learn_paired`, `qual_per_characteristic` | New, not reported: Majors 1 and 3 |
| Cross-fit and out-of-sample bands | `qual_crossfit`, `qual_guard_oos` | Text numbers confirmed; safety and step-6 cross-fits and the release-like force-cell shares are unreported (Major 4) |
| Strata, between-run, design level, decomposition, few-shot | `qual_strata`, `qual_between_run`, `qual_design_level`, `qual_decomposition`, `learn_fewshot` | Confirmed |
| Floors without the held-out series | `qual_floor_loao.csv` | Confirmed, except M0 (Minor 6) |
| Environment | `requirements.txt` | Pins match an installed environment; no licence or DOI |

## 6. Recommendation

**Minor revision.** The revision answers the central problem of round 1: the learned rules now get a fair test. The GP collapse is shown, and the models a reader would expect (a well-specified small-data GP, multi-fidelity, calibration with discrepancy, few-shot transfer, relation-matched conformal intervals) are scored by relation against the production record. Everything I checked reproduces.

What remains is reporting, wording and one inexpensive sensitivity analysis. Most of the evidence is already in the archive, but the paper must:

- report the crossing and the pooled trend GP, and reword the "not learning" claim;
- state the conformal guarantee correctly, and report coverage per family and per characteristic;
- diagnose M7n's intervals and report M7's false accepts;
- complete the reporting of the cross-fit;
- move the key tables into an Online Resource.

The DOI and the licence are conditions for acceptance.

## 7. Confidential comments to the editor

The author has done what the decision asked, and the archive is exemplary: the stand-alone scoring function reproduces every distance and band I tested. My remaining concern is interpretive, not one of integrity. The paper's sharpest AI claim, "intervals ... not learning", is weaker than written: the archive's own pooled trend GP gets most of the way to the same safety. The paper should say so. On the tables, I would not accept a CSV-only archive as the home of the GP diagnostics, the crossing and the coverage detail. A short Online Resource costs no pages, and the author already drafted one.

The main text has grown to 27 pages; Section 5.7 could move to that supplement. The rules added in response to the simulated first round (M7n, M7, Mcd, P+RM) are themselves post hoc. Only the promised confirmatory test can remove that, so the frozen procedure should be registered before acceptance. I need not see the paper again if the editor verifies these items; most can be checked directly against the archive.
