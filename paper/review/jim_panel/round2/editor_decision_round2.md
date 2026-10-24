# Editorial decision, second round

**Manuscript:** "When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing", by Hüseyin Tayyer Canseven (LUT University)

**Journal:** Journal of Intelligent Manufacturing (Springer)

**Version considered:** the revised 31-page line-numbered manuscript (`paper/review/jim_panel/round2/main_reviewed.pdf` and its source), the response letter (`paper/review/jim_panel/round1/response_round1.md`) and version 2 of the archive (`scripts/`, `results/`, `README.md`, `RELEASE_NOTES.md`, `requirements.txt`, `.zenodo.json`, `CITATION.cff`)

**Reports considered:** Reviewer 1 (machine learning for manufacturing quality), Reviewer 2 (sheet-metal forming and quality engineering) and Reviewer 3 (industrial decision support), second-round reports dated 24 October 2026; all three recommend minor revision

**Date:** 24 October 2026

*Written by an AI agent in the persona of a fictional handling editor of a simulated review panel; it does not come from the journal or speak for any real person.*

---

## Decision

**Minor revision.**

Dear Hüseyin Tayyer Canseven,

Thank you for a thorough and candid revision. I have read it, your response letter and the three reports. I have also checked the reviewers' central claims, read-only, against version 2 of the archive.

**What the revision achieved.** The paper now says what it shows: an exploratory evaluation on one laboratory process, with alternatives produced once and an uncalibrated simulation dataset. Specifically:

- the sibling strata use decision-time information;
- the learned rules get a fair test (M7n, M7, Mcd, relation-matched intervals, few-shot transfer);
- the measurement and the simulation are described as what they are;
- costs, trials and per-characteristic results are reported;
- the paper reads as a paper for this journal, so my first-round concern about fit is resolved.

The archive is exemplary. All 180 checksums verify, the scoring function reproduces the stored distances, and every number the reviewers and I checked reproduces. The central finding stands and is better supported: within a family, no simulation-based or learned rule decided closer than the nearest produced setting.

**What remains.** None of it needs new data:

- **RQ3 attribution and labels (C1–C3).** The safety credited to "not learning" comes from borrowing the other family's errors, and the relation-matched intervals carry no guarantee.
- **The part a factory would deploy (C4, C5).** Table 7 and the worked example use information a team does not have when it decides.
- **Messages to practitioners (C6–C8).** The statements on simulation levels, release-level decisions, trials and costs need tightening.
- **Reporting, the Online Resource and details (C9–C11).**

Three small new analyses are needed, all from stored results with the released code: a prior sensitivity for M7n, the trial under between-run variation, and decision-time guard bands. Everything else is rewording or reporting from existing files.

---

## Required changes

Page and line numbers refer to the revised PDF.

**C1. Credit the safety for new settings to the evidence that earned it.** *Rewording; reporting from existing files.* (Reviewer 1, major 1, minor 3.)

*Where:* abstract, ll. 037–039; Section 5.4, ll. 889–896; Section 6.1, ll. 1050–1051; conclusions, ll. 1199–1201.

*Why:* "Not learning" compares NN+RM, which borrows the other family's errors, with learners that see only their own family. The like-for-like comparisons in the archive show three things:

- A trend GP pooled over both families is safe at 2.75 floors for a new setting, against 5.15 for M7n alone and <1 for NN+RM.
- With the same relation-matched interval, the M7n and M1sn centres decide closer than the NN centre when extrapolating (17.6 and 17.8 floors, against 20.1).
- The interval does not make simulation-based centres safe: M1s+RM and M7+RM falsely accept up to 151–155 floors from the limit.

*Satisfied when:*

- the claim speaks of evidence borrowed from the other family on the same relation (using it needed no learning, and a pooled GP got part of the way);
- Section 5.4 states the three results above;
- the crossing of the eight predictors with the interval, plus the pooled trend GP, is an Online Resource table;
- the interval-score sentence (ll. 894–896) is limited to the production-record and trend centres (around M1s and M7 the scores are 76–155).

**C2. State that the relation-matched intervals carry no coverage guarantee.** *Rewording; reporting from existing files.* (Reviewer 1, major 2, minor 1.)

*Where:* Section 3.3, ll. 302–308; Table 2; Section 5.4, ll. 892–899.

*Why:* A family's calibration cases come from one or two fits (new setting) or nine overlapping fits (sibling). They are therefore not exchangeable with the other family's cases, and a single calibration family gives no distribution-free guarantee. The data agree: the borrowed NN quantile is 4.36 floors in one direction and 1.98 in the other, and NN+RM covers 0.95 and 0.73 in the two families with a sibling, and 0.61 on the dome.

*Satisfied when:*

- the text says that no guarantee is available, and that 88 and 93 % are the results of two family swaps;
- Table 2 labels the level as nominal;
- the cases behind each quantile are given (21, 42 or 63, all from one family);
- coverage per family, characteristic and stratum is in the Online Resource, with its range in the text;
- the jackknife+ guarantee (l. 899) is cited (Barber et al., 2021).

**C3. Explain the trend GP's intervals, test its priors and report M7's failure.** *Rewording; one small new analysis.* (Reviewer 1, major 3, minor 7.)

*Where:* Section 5.4, ll. 862–871; Fig. 1; Section 5.3, ll. 777–779; Section 6.1, ll. 1051–1053; Section 3.3, ll. 282 and 309.

*Why:* M7n answers R3(b) and illustrates Fig. 1. But its force length scale is the one set by its prior, and its intervals cover only 52–56 % for a new setting (17–33 % for the mid-side draw-in, none for the waviness). Their width is learned from variation between lubrication patterns at produced forces.

*Satisfied when:*

- Section 5.4 explains this;
- δd, δs and coverage of M7n by relation are reported with each of the four prior medians halved and doubled, one at a time (Online Resource; one sentence in the text on whether any conclusion changes);
- M7 is described as it behaves here: with two calibration forces its scale acts as a force slope, so it extrapolates like M1s;
- M7's false accepts, up to 118 floors on the cup depth, are reported next to M1s's 165;
- M7 is counted among the rules.

**C4. Give the guard band a team could have when deciding, validated by the matching scheme.** *Small new analysis from the stored intervals; rewording.* (Reviewer 3, major 1, minors 7, 13; Reviewer 1, major 4, minor 10.)

*Where:* Table 7; Section 3.6, ll. 442–450; Section 5.5, ll. 910–933; Tables 8 and 9; l. 1176.

*Why:* Table 7 shows in-sample bands pooled over the families (NN: 0.25, 2.0 and 7.0 floors), not the per-family bands that step 5 prescribes. For a new setting, neither is available when deciding:

- a family produced at two forces has no interpolation case, so its interpolation band rests on the cell being decided (the problem R2 removed from the strata);
- leaving one alternative out within the family keeps its siblings in the same cell, which have the same calibration set and, for NN, the same prediction.

*Satisfied when:*

- Table 7 gives the band available at decision time: per family with a sibling (or pooled, with a stated reason), and borrowed from the other family for a new setting;
- the share correct is validated by the matching scheme (one alternative left out within its family; the other family's band applied to the held-out family), under both priors, with cluster intervals, trial rates and the number of decided verdicts;
- step 5 says what happens when a family's production cannot exercise a relation (borrow, with the caveat of l. 307, or trial), and Tables 8 and 9 match;
- Section 5.5 reports:
  - the release-like failures with a force cell left out (NN 0.72 and NN+RM 0.74 extrapolating; M5 0.88 and M7n 0.87 interpolating);
  - the worst characteristics under the band (83–86 %);
  - that the bands are within-run (with τ = 3 floors, NN's grow to 2.9, 4.0 and 8.9);
- band and trial rate against the prior's width go into the Online Resource (within ±3 floors, NN with a sibling needs 8 floors and sends 99 % of verdicts to trial).

My own check suggests the reference-prior conclusions survive. Bands borrowed strictly from the other family keep NN at 0.951 correct interpolating and 0.952 extrapolating. Under the release-like prior they give 0.75 extrapolating.

**C5. Rework the worked example with what the planner knows.** *Rewording; small recomputation.* (Reviewer 2, major 4; Reviewer 3, major 1(b).)

*Where:* Section 3.7, ll. 455–471.

*Why:* Only 100 and 500 kN have been produced on the concave cup. Yet the example uses the nine-series floor, distances, shares and a band that include the 300 kN cell being decided, resolvable force changes from the 300 kN data, and a trial cost it never uses.

*Satisfied when* the example uses:

- the floor of the six produced series (0.041 mm, not 0.050);
- the resolvable force change from the two produced levels (about 40 kN);
- the convex family's interpolation distance and band (5.3 and 2.5 floors), stating that this family was produced and giving the exchangeability caveat;
- the trial cost as C8 defines it, or no trial cost at all;
- a sentence on the quantisation of the mid-side draw-in (0.38 floors; three values hold a median 89 % of a series).

The release survives, with a margin of 7.4 floors.

**C6. Make the simulated-versus-measured levels conditional on what is assumed.** *Rewording.* (Reviewer 2, major 1, minors 3–5.)

*Where:* Section 4.1, ll. 478–479; Sections 4.2–4.3; Section 5.2, ll. 724–753; Section 6.3, ll. 1077–1081.

*Why:* The measured draw-in is (210 − Wx)/2, but the 210 mm comes from the DDACS mesh (`common.BLANK_MM`), not from the produced blanks. One millimetre of blank width moves the mid-side draw-in by 0.5 mm (10 floors), and a 1 % lateral scale error by 0.9 mm.

*Satisfied when:*

- Section 4.1 says that the blank width is assumed and gives these sensitivities;
- "does not contain the produced process" rests first on the comparisons that depend on neither blank nor scale: a force effect 2.7–5.1 times too large, a concave wall angle that falls by 1.5° in simulation but not in production, concave arms that bend the other way, and a reversed dome ranking. The level comparisons (11 of 42, the draw-in gaps, the censored Mc) are presented as conditional;
- "partly fitted to the simulation" (l. 524) is explained, with the characteristics that depend on it;
- the depth-offset sentence (ll. 750–752) is corrected. A drawing depth 1 mm shorter moves the wall at 15 mm depth by only 0.2–0.4 mm. A scale error would give an offset proportional to the radius, whereas the offset is 2.0–2.2 mm at both radii. A different tool geometry fits best but is unconfirmed;
- Section 4.2 gives the extraction noise of the simulated characteristics, as R4 asked;
- l. 728 ("reaches": 0.012 mm remain at μ = 0.15), ll. 729–730 (the corner gap holds at μ = 0.10) and l. 1078 ("calibrated") are corrected.

**C7. Align the release-level and trial messages with capability and between-run variation.** *Rewording; one small new analysis.* (Reviewer 2, major 3, minor 8.)

*Where:* Section 5.6, ll. 947–957; Section 5.7; Table 8; Section 6.2, ll. 1061–1066; conclusions, ll. 1193–1194; l. 1169.

*Why:*

- *Release is a capability decision.* A release asks whether Ppk ≥ 1.33, which is a decision on m̄ + 4σ, and your own variant scores it. NN needs 3.35 floors with a sibling and 10.55 extrapolating. It therefore confirms Ppk ≥ 1.33 only for designs whose true within-run Ppk is about 2.1–3.2 with a sibling, and 3.8–7.3 extrapolating.
- *The trial rows escape the between-run component.* Perturbed as the rules' truths are, a 20-part trial decides at about 2.1, 3.6 and 5.1 floors for τ = 1, 2 and 3. NN with a sibling decides at 3.45, 4.45 and 5.75.

*Satisfied when:*

- Section 5.6 states the release question in these terms;
- the trial rows join the between-run sensitivity analysis;
- Table 8 ("otherwise by trial") and Section 6.2 say that near release level a short trial does not decide either, once runs differ by a floor or more, so the evidence must come from replicated runs;
- Section 6.2 gives the release-like figures next to the reference ones, and either drops or supports "the few close ones";
- "bounds its effect" (l. 1169) becomes "explores".

**C8. Use the costs consistently in the procedure, and label what is in-sample.** *Rewording; reporting from existing files.* (Reviewer 3, major 2, minors 10, 12.)

*Where:* Fig. 2 and Section 3.6; Section 3.7; Section 5.6, ll. 937–949; Fig. 6.

*Why:* Costs are inputs to step 1 and choose the rule in Table 8, yet step 5 sets g by the 95 % target alone. Fig. 6's cost-minimising bands are chosen in-sample, pooled over the families, under one prior and one c_FR, and some statements depend on that:

- with c_FR = 0.25 c_FA, the cheapest rule for a new family is M3 at c_T = 0.1 and M0 without a band at 0.2 and 0.5 (false-accept rate 0.145 per verdict at 0.5);
- under the release-like prior at c_T = 0.05, four GP-based rules undercut NN with a sibling by at most 0.003 c_FA.

*Satisfied when:*

- step 5 says how stated costs set the band (for example, the 95 % band by default, or the cost-minimising band under a cap on the false-accept rate), and the worked example follows it;
- Section 5.6 says that the cost bands are in-sample and pooled, and either estimates them out of sample (C4's schemes or a cross-fit) or keeps only the statements that hold under both priors and all three c_FR values. The new-family statement is qualified, and differences of thousandths of c_FA are called unresolved;
- Fig. 6 says that trials are priced as error-free and that its band search runs to 40 floors, beyond step 5's cap of 20. The text gives the 20-part trial's own error cost: 0.017 c_FA per verdict, or 0.037 under the release-like prior, against NN's whole 0.018 with a sibling at c_T = 0.05;
- the text states that both priors put 47 % of verdicts on failing designs, and l. 946 gives a source or calls its claim an assumption.

**C9. Report the selection completely and word it accurately.** *Rewording; reporting from existing files.* (Reviewer 1, major 4; Reviewer 3, minors 1, 5.)

*Where:* abstract, ll. 034–035; l. 633; Section 5.7, ll. 965–994; l. 1042; ll. 1178–1179; l. 1191.

*Satisfied when:*

- "committed to in advance" becomes "a single rule applied to every relation", since NN was added after the first results;
- "the cross-fitting bounds" becomes "estimates", because two folds cannot correct for rules designed after both geometries had been seen;
- both cross-fits are reported:
  - by safe distance: the selected rule is safe on the other geometry only at up to 18.2 floors interpolating and 11.5 extrapolating;
  - of step 6: share correct 0.92–0.97 within a family, below 0.95 in four of six cases, and 0.73 for a new family.

**C10. Restore a compact Online Resource and make the archive readable.** *Reporting from existing files.* (All reviewers.)

- The content is as set out in my ruling below.
- The main text must not grow.
- The archive gets a data dictionary: column names, scopes and code names in the paper's terms (for example `within` = sibling, `transfer` = new family, M4 = M3n, `resolution_floors` = δd), and the floor that each file uses.
- `findings.md` separates the current numbers from the superseded history.

**C11. Corrections of detail.** *Rewording; each one verified.*

- ll. 897–898: the cluster intervals span 0.72–0.94, and M3's is 0.94–0.98 (Reviewer 1).
- ll. 1003–1005: without the held-out series, M0 moves by 3.75 floors (Reviewer 1).
- ll. 1062–1064: an out-of-sample share of 0.954 (0.937–0.971) means about 92–95 of 98; recompute with the band of C4 (Reviewers 1, 3).
- ll. 902–906 and 1155: the few-shot distances use the new family's nine-run floor, which a team with one to three alternatives does not have (Reviewer 1).
- Table 6 note: the bracketed values are distances computed in the unit, not floors times the pooled floor (corner with a sibling: 0.13 against 0.21 mm) (Reviewer 2).
- ll. 664–666: A3 fails for the resolution of the mid-side draw-in (Reviewer 2).
- ll. 674–678: the 0.05 % drift bound is about 0.9 floor (Reviewer 2).
- Table 5: add Mcd, whose 30 floors the abstract quotes (Reviewer 3).
- ll. 1186–1188: say that the band was validated for an assumed prior (Reviewer 3).
- `qual_coverage.csv`: flag the degenerate cluster intervals that the response letter says are absent (Reviewer 1).
- Cite Friedman (2001) for gradient boosting (Reviewer 1).

---

## Recommended changes

These are optional. Please say in one line each whether you adopted them.

- **Reviewer 1:**
  - marginalise M7n's hyperparameters;
  - use a normalised nonconformity score;
  - restore the paragraph on finite-sample limits (a 5 % miss rate needs 19 alternatives per relation);
  - cite conformal risk control and "learn then test".
- **Reviewer 2:**
  - add an m̄ + 5σ variant and report the north-wall check;
  - send the request to the providers (blank dimensions, tool drawing) and report the answer;
  - discuss the saturation of the draw-in between 300 and 500 kN, and use the OP10-to-OP20 change of wall angle as a scale-free validation target;
  - state what a confirmatory dataset needs from the measurement, frame the new-family relation as the pre-tryout question (with the PPAP caveat), and mark the warm-up in Fig. 4.
- **Reviewer 3:**
  - estimate the cost bands out of sample, if C8 is met by restricting the statements;
  - consider rarer failing designs;
  - plot Fig. 6 relative to NN, and add the decided share to Fig. 1b;
  - in Section 6.5, address one-sided monitoring (about 150 decided verdicts to detect a rise from 5 to 10 %) and name planners and quality engineers as participants;
  - add the suggested items to Table 9;
  - add checks to `opchar.py`;
  - add a forward reference in Section 3.7.
- **Length:**
  - use the Online Resource to thin out ll. 889–906 and Section 5.7 (Reviewers 1, 3);
  - add a validation figure to Section 5.2 only if it replaces text (Reviewer 2).

---

## My checks of the reports

All checks were read-only. I imported the released functions in memory without writing bytecode, ran no pipeline script, and left `git status` clean.

| Claim | Reviewer | File or method | Verdict |
|---|---|---|---|
| 180 checksums verify; the scoring function reproduces the stored distances | all | `sha256sum -c`; `opchar.selfcheck` | Confirmed |
| Pooled trend GP: safe at 2.75 (1.30/3.05) floors; coverage 0.86/0.79; interval score 20.9 extrapolating | 1 | `learn_resolution.csv`; recomputed from `learn_intervals.csv` | Confirmed; "most of the way" qualified (Q1) |
| Same interval, other centres: 17.55/17.80 against 20.10; paired −2.55 (−2.85 to −0.25) | 1 | `learn_resolution.csv`, `learn_paired.csv` | Confirmed; interpolating, NN+RM is closer |
| M1s+RM and M7+RM false accepts at 151–155 floors; M7 at 118 on the cup depth | 1 | `learn_resolution.csv`, `qual_per_characteristic.csv` | Confirmed |
| NN+RM coverage by family, characteristic and stratum; quantiles 4.36/1.98; 21–63 cases | 1 | `learn_intervals.csv` (`rm_quantile_floors`, `rm_n`) | Confirmed |
| No guarantee with one calibration family | 1 | one effective draw gives coverage ½ | Confirmed |
| M7n coverage 52/56 %, mid-side 17/33 %, waviness 0 %; force length scale at the prior | 1 | `learn_intervals.csv`, `learn_gp_diagnostics.csv` | Confirmed; the archive has no prior sensitivity |
| M7's simulation term acts as a force slope | 1 | `learners.m7_design` | Confirmed |
| Cross-fits by safety (18.2/11.5) and of step 6 (0.92–0.97; 0.73) | 1, 3 | `qual_crossfit.csv` | Confirmed |
| Interval-score sentence too broad | 1 | `qual_coverage.csv` | Confirmed (M5n+RM scores 29.2 extrapolating) |
| Minor figures: interval bounds, degenerate intervals, M0's 3.75, 0.954, few-shot floor | 1 | `qual_coverage.csv`, `qual_floor_loao.csv`, `qual_guard_oos.csv`, `learners.fewshot` | Confirmed |
| Table 7 pooled; NN per family 0/0.5, 1.5/2.5, 9.5/5.75 | 3, 1 | `qual_guard_family.csv`; `qualify.guard_per_family` | Confirmed |
| The example's band comes from the cell decided; one-alternative-out is near in-sample | 3, 2 | code of `guard_per_family`, `guard_out_of_sample` | Confirmed |
| Force cell out, release-like: NN 0.718 (0.683–0.784), NN+RM 0.735, M5 0.875, M7n 0.867 | 3, 1 | `qual_guard_oos.csv` | Confirmed |
| Bands borrowed from the other family | mine | `qualify` functions on the stored intervals | NN 0.951/0.952 (reference), 0.934/0.748 (release-like) |
| Worst characteristics; τ = 3 bands; ±3 prior | 3 | `qual_guard_characteristic.csv`, `qual_between_run.csv`, `qual_guard_prior_width.csv` | Confirmed |
| Cost bands in-sample and pooled; NN at c_T = 0.05: 4.5 floors, 40 % trials; cheapest rule under other c_FR and priors | 3, 2 | `qualify.costs`, `qual_costs.csv` | Confirmed |
| Trial error cost 0.017/0.037; 47 % failing designs | 3 | `opchar.step6` on the trial cases | Confirmed |
| About 150 verdicts to detect 5 → 10 % | 3 | normal-approximation sample size | Confirmed (149) |
| The 210 mm blank comes from the DDACS mesh | 2 | `common.py`; `note_to_dataset_authors.md` | Confirmed |
| Invariant comparisons | 2 | `panel_force_effect.csv`, `sim_validation.csv`, `panel_arm_sign.csv` | Confirmed |
| Depth and radius offsets | 2 | `sim_depth_offset.csv` (a proportional offset predicts 2.44 mm at the convex radius) | Confirmed; inference qualified (Q3) |
| North wall 0.2–0.4 mm larger, against 0.8–1.4 mm under a y-scale error | 2 | per-side radii in `features_rddac.csv` | Confirmed (0.18–0.43 against 0.85–1.58); inference qualified |
| Six-series floor 0.041 mm, margin 7.4; quantisation 89 %; secant 48.5 kN | 2 | `alternatives.floor_from` on `features_rddac.csv`; `alt_mrc.csv` | Confirmed (0.0413, 7.41, 0.89); secant qualified (39.8–47.9 kN) |
| Trial under between-run variation | 2 | reimplemented with `between_run`'s draws | Confirmed within 0.05 floor |
| Capability reformulation | 2 | `qual_variants.csv`, `panel_floor_protocol.csv` | Confirmed |
| Table 6 note; "reaches"; corner gap | 2 | `qualify.per_characteristic`, `sim_validation.csv` | Confirmed |
| "Partly fitted to the simulation"; ISO editions | 2 | scales come from the dataset's `calibration.json` | Not checked |

---

## Qualifications of the reports

1. **The pooled trend GP (Reviewer 1).** It closes about half the gap in safe distance (5.15 → 2.75 floors, against NN+RM's <1). When extrapolating, its coverage is 79 % against NN+RM's 93 %, although its interval score is better. C1 corrects the attribution. It must not reverse the finding that NN+RM was the safest rule for new settings.
2. **Placement (Reviewers 1, 2).** The crossing and the validation tables belong in the Online Resource. They can enter the main text only if they replace text. Section 5.2 already states the validation's conclusions; it needs the conditional wording of C6, not a table.

   The M7n prior sensitivity is required because the paper itself says that a prior fixes a hyperparameter. Marginalisation and normalised scores are recommended only.
3. **The offsets (Reviewer 2).** The arithmetic rules out "could each produce", but the tool geometry remains an inference. The north-wall check argues against a y-scale error. It cannot, however, separate a non-square blank from an edge-detection bias in the direction of motion, so I only recommend it.
4. **The worked example (Reviewer 2).** I ask for no change of characteristic and no sub-pixel edges: the draw-in sets the force, and its quantisation is already in its distances. The 48.5 kN is the archive's pooled slope; the planner's own value is about 40 kN.
5. **The extrapolation scheme (Reviewers 1, 3).** Leaving the force cell out still uses the family's other extrapolated cell, whose calibration contains the cell being decided. Strictly, only the other family's band is available. Under the reference prior both give similar shares, so either is acceptable if it is labelled.
6. **Costs (Reviewer 3).** I require consistency and labels, not a particular cost procedure. Out-of-sample cost bands are one way to meet C8; other shares of failing designs are optional. A within-run statement with the τ = 3 figures replaces the requested between-run column in Table 7.
7. **"Committed to in advance".** The phrase echoes my R8, which asked for one rule fixed across relations rather than the best rule per relation. The reviewers are right that it reads as "pre-specified".
8. **Generative AI (Reviewer 3).** The declaration is explicit and appears consistent with Springer Nature's policy as I understand it. The journal office will confirm; nothing more is asked of you.

---

## Length, the archive and supplementary material

You removed the appendix and the drafted Online Resource to stay at 31 pages. You said so openly and offered to restore the tables, and the archive is complete. The reviewers nevertheless all ask for a compact Online Resource, and I agree:

- The answer to RQ3, the simulation finding and the deployable band now rest on CSV files with internal names and no captions.
- The archive has no DOI or licence yet, so it cannot be cited.
- `findings.md` mixes current and superseded numbers.
- An Online Resource is reviewed and published with the article but does not lengthen it. The length argument applies to an appendix, not to supplementary material.

**Ruling.**

- **Online Resource 1.** Restore it as an Online Resource, not an appendix. Limit it to tables that carry claims of the paper or that R1–R12 or this decision require. Caption them in the paper's terms (the relation and rule names of Table 2, with units and floors), and cite each one where the text now says "in the archived results". I expect about ten tables:
  1. all rules by relation, Mcd included;
  2. GP diagnostics, with the M7n prior sensitivity;
  3. the crossing, with the pooled trend GP;
  4. coverage by relation, family, characteristic and stratum;
  5. decisive and safe distances per characteristic (R9);
  6. the simulation against the measurement, with the extraction noise (R4);
  7. scan redundancy per series (R5);
  8. decision-time guard bands by scheme and prior, against the prior's width and per characteristic;
  9. costs by prior, c_FR and c_T;
  10. the between-run sensitivity with the trial rows, and the cross-fits.

  The robustness variants, few-shot details, paired differences and the oil-film and tooling checks may stay in the archive. Most of these tables existed in your first draft.
- **Main text.** I accept its growth to page 27, which is mostly material that R1–R12 asked to see there (Figs. 1, 3, 4 and 6; Tables 3, 6 and 7). It must not grow further. Pay for C1–C9 by moving numbers to the Online Resource, notably from ll. 889–906 and Section 5.7.
- **Archive.** It remains the machine-readable source, with the data dictionary of C10.

---

## Conditions for acceptance

- **Licence:** a licence file for the code, and the licence fields in `.zenodo.json` and `CITATION.cff`. The data-derived files stay under CC BY 4.0.
- **DOI:** a minted DOI, cited in the paper and in `CITATION.cff`. The deposited version must match the checksums of the revision, and I must be able to open it.
- **Registration:** `paper/notes/frozen_procedure.md` deposited with a timestamp and cited, since the conclusions name "a confirmatory test of the frozen procedure". Otherwise, the word "frozen" goes.
- **Data dictionary:** the dictionary of C10, in the deposit.

## What happens next

Please submit by **23 November 2026** (30 days), or ask for an extension before then: the revised manuscript, a marked-up version, Online Resource 1, the updated archive, and a short response that takes C1–C11 in turn with their locations and answers each recommendation in one line.

The revision will not go to a full new round. I will check C1–C11 and the conditions myself against the archive. I will also ask two reviewers to comment, within ten days, on selected parts:

- Reviewer 3: Table 7, Sections 3.6–3.7 and Sections 5.5–5.6;
- Reviewer 2: Section 5.2, the worked example and the validation table.

Reviewer 1 does not need to see the revision again.

If these checks hold and the conditions are met, I expect to recommend acceptance. If Table 7 still shows bands that a team could not have when deciding, the paper will need another round.

Yours sincerely,

Handling editor (a fictional persona in a simulated review panel), Journal of Intelligent Manufacturing
