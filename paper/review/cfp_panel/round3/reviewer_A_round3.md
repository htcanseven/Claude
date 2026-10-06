# Referee report, third round: Reviewer A

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design (Springer), special collection "AI in Design for Manufacturing"
**Round:** third (second revision)
**Reviewer focus:** design decision-making under uncertainty, design margins, verification and validation planning, evaluation of design support; at the editor's request, the required changes S1–S3 in particular depth

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The second revision answers the decision letter point by point and, for the three items the editor asked me to examine in depth, does what the letter required: the force trend M1sn is added as the paired counterpart of the scaled simulation and the claim that a rescaled simulation adds information within a family is withdrawn throughout (S1); the prior of the guard band is stated exactly, its influence is shown under four further priors, and the procedure's operating characteristics are tabulated by rule and relation in Table A4 (S2); and the new family is reported in the produced family's floor, with both floors and their intervals in the text (S3). I re-derived every S1–S3 figure quoted below from the released result files, and the paired bootstrap and the guard bands also with the author's own code; all of them reproduce, and the response describes them accurately. The other required changes within my remit are met, except that the archive DOI, which the editor made a condition of acceptance, is still pending. The new figures have also introduced two small inaccuracies into headline sentences of the abstract, Sect. 6.1 and the conclusions, and a few editorial points remain.

## 2. Status of my second-round points

All figures I cite as verified come from read-only checks on `results/*.csv`. They use the author's functions (`distance_pair` and `exclusion` in `decisions.py`; `guard_band` in `panel.py`), and no pipeline script was rerun.

### New issues

**N1. The rescaled simulation against a straight line in force: resolved.**

*Evidence in the manuscript.*
- **The rule is added.**
  - Table 2 (p. 8, l. 343): "M1sn force trend | a + b force, least squares | point".
  - Sect. 3.3 (p. 7, l. 304–307) gives the reason for the pairing: "within a geometry they are functions of the force alone: M1sn is the counterpart of M1s without the simulation".
  - The rule is paired in Sect. 4.4 (p. 11, l. 499) and appears below the line in Table 4.
- **The claim is withdrawn.**
  - Sect. 5.5 (p. 16, l. 697–702): "Rescaled, it does no better: … the straight line in force (M1sn) decides 1.4 floors closer than the scaled simulation with a sibling (+0.65 to +3.0) and 11 closer for a new setting (+5.3 to +13.8), in every resample and refit configuration; the 4.2 floors that the scaled simulation gains over the median of the produced alternatives with a sibling come from the force level."
  - Sect. 6.3 (p. 21, l. 933–934): "Within a design family the production record carried the decision, even against a rescaled simulation."
  - Sect. 6.1 (p. 20, l. 908–910), the abstract (l. 37) and the conclusions (p. 23, l. 1052–1053) say "offset or rescaled".
  - No sentence that credits the rescaled simulation within a family remains; I searched the LaTeX source.

*Verified.*
- **Distances.** `dec_resolution.csv` gives M1sn at:
  - 3.50 floors with a sibling;
  - 8.15 for a new setting;
  - 4.65 interpolated, identical to NN, as it must be by construction (the Table A4 rows of M1sn and NN are identical there too);
  - 8.85 extrapolated.
- **Paired differences with the fits fixed.** `dec_paired.csv` gives M1s − M1sn = +1.35 [0.65, 2.95] with a sibling and +11.00 [5.30, 13.80] for a new setting. I re-ran the resampling with the author's functions on `dec_intervals.csv` and `dec_q95_reps.npy`:
  - the intervals are identical;
  - the force trend is *strictly* more decisive in all 1,000 resamples, with smallest differences of 0.50 and 3.40 floors and no ties, so "in every resample" is exact.
- **Paired differences with refitting.** `rob_refit_paired.csv` gives +1.35 [1.35, 3.60] and +11.00 [8.80, 12.05], with M1s never the smaller.

*What remains.* Nothing on N1 itself. However, the new-setting split that the force trend's 8.2 floors now heads is attached to the wrong rule in Sect. 6.1 and the conclusions (Sect. 4.1 below).

**N2. New family: unit and selective reporting: resolved.**

*Evidence in the manuscript.*
- **Table 4.** The new-family columns are in the produced family's floor, and the note says so (p. 14, l. 624–625): "a new family rests on two transfers and is scored in the floor of the produced family". The table gives intervals for:
  - M2: 39–42/9.8–32;
  - M3: 36–45/15–19;
  - M5: 31–39/28–32;
  - M5n.
- **Sect. 5.3** (p. 13, l. 596 – p. 14, l. 636) gives both floors and adds M3. It no longer ranks the rules: "The best rule was thus safe at about 16–17 floors in either floor … but two transfers do not resolve which rule is safest: the safe distance of M3 minus that of M2 lies between −16 and +7 floors in the produced family's floor and between −3 and +8 in the new family's."
- **The unit is stated** in the abstract (l. 34–35, "in either family's floor"), the "New family" row of Table 5, the conclusions (p. 23, l. 1049–1050) and the caption of Fig. 2.
- "The envelope rule is the safest" no longer appears anywhere.

*Verified.*
- **Produced family's floor** (`panel_source_floor.csv`, δd/δs with intervals):
  - M1: 32.90;
  - M2: 40.75/26.40 [39.45–41.95/9.80–32.00];
  - M3: 40.15/17.10 [36.15–45.15/14.75–19.45];
  - M5: 35.20/31.30 [31.40–38.60/27.50–32.05];
  - Mc: 42.60.
- **New family's own floor** (safe distances): M2 15.80, M3 20.50, M5 27.50.
- **Paired difference** (`panel_source_floor_paired.csv`), safe distance of M3 − M2:
  - −9.30 [−16.10, +6.90] in the produced family's floor, with M3 the smaller in 83 % of resamples;
  - +4.70 [−3.41, +8.00] in the new family's floor, with M3 the smaller in 25 %.
- **Figures and tables.** Fig. 2, Fig. 4 and Table A3 take the new family from the produced-floor results (`figs.py`, `panel.step6`, `make_tables.py`).

*What remains.* Only Table A2 keeps the new family in its own floor (remaining point 6 below; editorial).

**N3. Step 6: the prior of the guard band, and the evaluation reported for one rule only: resolved; one clause recommended.**

*Evidence in the manuscript.*
- **The prior is stated exactly**, in three places:
  - Sect. 3.6 (p. 9, l. 408–411): "The reference prior weights the 47 distances of the evaluation grid within ±20 floors equally (0, ±0.5 to ±10 in steps of 0.5, ±12, ±15 and ±20; 87 % of the weight within ±10), drops infeasible requirements and searches g in steps of 0.25 floors up to 20";
  - the caption of Fig. 4 (p. 18, l. 797–799);
  - row *g* of Table A1.
- **Its status is stated:**
  - Sect. 3.6 (l. 406–408): "g depends on the distribution of requirement distances that the team expects, not on rule and relation alone";
  - Table A1: "not a property of rule and relation alone";
  - Table 5: "Derive the rule's guard band for the distribution of requirement distances the team expects".
- **Its influence is shown** in Sect. 5.7 (p. 17, l. 779 – p. 18, l. 803) under the grid within ±5 floors and uniform priors within ±20 and ±50 floors. The grid within ±3 floors appears in the worked example (l. 816).
- **The procedure's operating characteristics are reported:**
  - Table A4 gives g, δd/δs under step 6, and the trial shares at 10 and 20 floors (T10, T20) for M1, M1s, M2, M5, M5n, NN, M3, M3n and M1sn, with a sibling, interpolated and extrapolated. Its note covers M0, M0w, Mc and the new family.
  - Table A3 gives the coverage, half-width and centre of the interval rules.
  - The rules that never qualify are named (p. 17, l. 776–778).
  - Fig. 4 has separate panels with g marked.

*Verified.*
- The coded reference prior is exactly as stated: 47 points, 41 of them within ±10 floors.
- Every cell of Table A4 reproduces from `panel_step6.csv`.
- Every band quoted in Sect. 5.7 reproduces from `panel_guard_priors.csv`.
- "At most 79 %" for a new family reproduces from `panel_step6_curves.csv` (M2: 0.791).
- **The worked example** reproduces from `dec_intervals.csv`:
  - NN predicts 14.99 mm, a margin of 6.16 floors;
  - the widened intervals of M2, M5 and M5n are exactly as quoted;
  - at +8.5 floors, step 6 with NN is right in 42 of 42 interpolated cases.

*What remains.*
- **The reason for the prior.** The sentence meant to say why the reference prior represents the requirements a team faces (l. 410–412) describes the prior rather than justifies it. Now that its conditional status is explicit, this is acceptable.
- **The near-truth prior.** It is shown only as the ±5 grid. Under that grid the band of the nearest setting with a sibling is a quarter of its value under the ±3 grid that the worked example uses. This is recommended, not a condition (Sect. 4.3).

### New minor points of my second-round report

| # | Point | Status | Evidence; what remains |
|---|---|---|---|
| 1 | Traceability; archive | **Partly resolved** | Table A5 (p. 27) maps each section's quoted numbers to their script and file, and all 47 result files it names exist in `results/`. Sect. 4.5, the appendix and the availability statements cite the archive. **The DOI is still pending**: p. 28, l. 1267–1268, "Zenodo, version 3, [DOI pending]". Still needed: mint and cite it (Sect. 6). |
| 2 | Short series show calibration, not qualification | Resolved | Sect. 5.6 (p. 17, l. 761–763): "rules can be calibrated on short runs, here scored against the truths and floors of the full series"; the note to Table A2 says the same. The bounds of 1.5 and 4 floors reproduce (`rob_decisions.csv`). Editorial point: see Sect. 4.4. |
| 3 | "Within the family" in two senses | Resolved | "With a produced sibling" now denotes the sibling relation. "Within a family" is used only for both within-family relations (l. 683, 760, 851, 905, 1050). |
| 4 | Table 3 aggregates | Resolved | The note reads "classical statistics pooled over the series as root mean squares". σ_w is below σ_LT in all 14 rows. Series by series, σ_w exceeds σ_LT in 5 of 126 cases, by at most 0.27 % (`panel_floor_protocol.csv`). |
| 5 | A "definitional" finding that is empirical | Resolved | Sect. 6.1 (p. 19, l. 869–871): "its distribution-free intervals are guaranteed their level only where the calibration alternatives are exchangeable with the new design". |
| 6 | Table 5 basis; "Fixing a requirement" | Resolved | The block is labelled "From the framework (prescriptive; usefulness not evaluated)". The row is "Planning a requirement … As a heuristic". Sect. 6.2 (p. 20, l. 917–919): "the decision itself needs the guard band, because the safe distance is defined on the true margin". |
| 7 | Release-level requirements only with a sibling | Resolved | Sect. 5.8 (p. 19, l. 834–835) and Table 5. For the missing index qualifier in the abstract, see Sect. 4.2. |
| 8 | Surrogate statement | Resolved | Sect. 5.5 (p. 16, l. 707–711) scores the surrogate as a rule (109 against 108 floors; 15 against 15) and gives "leave-one-out root-mean-square error below 2 floors for 12 of the 14". Both reproduce (`ds_surrogate_rule.csv`, `ds_surrogate.csv`). |
| 9 | Worked example | Resolved | "Chosen for illustration" (l. 810–811); "its guard band was estimated on data that include it" (l. 820–821); the widened intervals of M2, M5 and M5n are given (l. 817–818) and reproduce. |
| 10 | Table 6; the black-box route | Resolved | The caption reads "(an untested proposal)". Comparability within a protocol is stated (p. 23, l. 1013–1016), and so is the binning estimator (p. 22, l. 993–996). The minimal report is a numbered checklist (l. 1005–1010). |
| 11 | Paired differences: name the relation | Resolved | p. 16, l. 693–697, including "M1 13.5 further out for a new setting". |
| 12 | The 3.4-floor headline | Resolved | 0.85 and 4.9 floors are given in the abstract (l. 30–32), Sect. 6.1 and the conclusions (l. 1046–1047). |
| 13 | Uncertainty of the headline distances | Resolved as specified | Table 4 gives the intervals. *Optional:* the revision has made two other figures headline best attainable distances, M1sn's 8.2 floors for a new setting [6.7, 9.0] (`dec_resolution.csv`) and M1's 33 for a new family [30.7, 36.1] (`panel_source_floor.csv`). Both intervals are in the files and could join Table 4. |
| 14 | Designer-study hypotheses | Resolved | Sect. 6.3 (p. 21, l. 947–952) gives two testable hypotheses with their measures. |
| 15 | The error of a tryout trial | Resolved | Sect. 3.4 (p. 9, l. 377–380) and Sect. 5.1 (p. 12, l. 550–551). |

### Remaining minor and editorial points of my second-round report

1. **"Two operating characteristics."** Resolved: p. 2, l. 76–77, "by two points on its operating characteristics".
2. **M6 in the table notes.** Resolved, in the notes to Tables 2 and 4.
3. **The factor that defines a sibling.** Resolved: p. 9, l. 386–387, "differs only in the factor varied at a fixed setting".
4. **The cost sentence.** Resolved: p. 19, l. 836–843, as a list (i)–(iii), with the coarseness and the six failing alternatives stated. `scen_cost_map.csv` reproduces it, including the three-way tie with a sibling.
5. **Fig. 4.** Resolved. Editorial point: see Sect. 4.4.
6. **The new-family robustness rows.** Resolved in substance: "the envelope rule the safest for a new family" is removed.
   - *Residual.* Table A2 keeps the new family in its own floor (note, p. 26, l. 1171–1172). Its reference row (M2 51/16, M5 38/28) therefore differs from Table 4 (41/26, 35/31), and "for a new family by at most 4" (Sect. 5.6, l. 761–762) is stated in the floor the procedure rules out.
   - The response's reason, that this floor "makes the variants comparable with each other", would hold in any common floor.
   - The choice is disclosed, so it is acceptable. One clause in the note pointing to Table 4 would prevent confusion.
7. **What the floor adds to the repeatability limit.** Resolved: p. 4, l. 179–181.
8. **PA12 builds.** Resolved: p. 23, l. 1016–1019.
9. **"Relying on".** Resolved.
10. **Transparency as an argument.** Resolved: p. 21, l. 924–926, "arguably".
11. **Editions; Montgomery.** Resolved, and I withdraw my query. ISO 5725-2:2025 and ISO 22514-2:2026 are current third editions (December 2025 and February 2026), as the response says. Montgomery's place of publication is given.
12. **Numbers repeating Table 4.** Resolved: Sect. 5.3 is shortened.
13. **The abstract's definitional sentence.** Resolved: it is split.

**Residuals of my first-round comments.**
- *A8 (positioning).* Resolved. Sect. 6.4 (p. 21, l. 956–966; p. 22, l. 979–983) now states what the results imply for capability databases, margins, overlapped development, set-based design and testing. Sect. 2.2 (p. 3, l. 118–120) says how the evidence relation differs from the design type.
- *A9 (density).* Partly resolved. Sects. 5.5 and 5.8 remain very dense. The editor made this a recommendation, and I do not press it.
- *A correction to my own report.* My uniform-prior band of 0.5 floors (nearest setting, interpolated) depended on the grid step; 0.25 floors at the 0.05-floor step, as reported, is right.

## 3. The required changes S1–S7 within my remit

**S1 (withdraw the rescaled-simulation claim): met.** Item by item against the letter:
- **The force trend** is in Table 2 and below the line in Table 4. Its paired interval is in Sect. 5.5, and its refit interval in Sect. 5.9 (p. 19, l. 856–857).
- **The text.** Sects. 5.5, 6.1 and 6.3 are rewritten. Table 5 names "nearest setting or force trend" for a new setting, and the abstract and the conclusions say "offset or rescaled".
- **Where the force trend is best**, it is reported without interpretation.
  - Sect. 5.3 (p. 13, l. 590–591): "the force trend and the nearest produced setting decide at 8.2 and 8.5 floors". Table 4 gives 8.9 against 9.5 floors extrapolated.
  - The paired difference is −0.30 [−2.00, +2.55] (`dec_paired.csv`). The paper does not quote it, and need not.
- **The decomposition** says whether it includes M1sn: "Over the eleven calibrated rules … (71 and 15 % with M1sn)" (p. 15, l. 680–684). It reproduces from `panel_decomposition.csv`:

  | Scope | Relation | Rule |
  |---|---|---|
  | All three relations, produced family's floor | 66.5 % | 6.2 % |
  | All three relations, new family's own floor | 68.6 % | 6.0 % |
  | Within a family | 14.8 % | 68.1 % |
  | Within a family, with M1sn | 14.7 % | 71.2 % |

- **The "one exception"** is withdrawn in Part 3 of the response.
- **Strata and force levels**, which bear on S1:
  - With two resolvable siblings, the force trend decides at 4.45 floors against NN's 4.85 (Sect. 5.4).
  - At 100 kN the force trend decides at 8.85 floors against NN's 11.0; at 500 kN, at 8.85 against 4.85 (`panel_force_levels.csv`). Both reproduce.

**S2 (the prior and the procedure's operating characteristics): met.**
- **(a)** The prior is stated exactly in Sect. 3.6, the caption of Fig. 4 and Table A1.
- **(b)** Its influence is shown under the ±5 grid and both uniform priors, with the ±3 grid in the worked example.
- **(c)** Its conditional status is stated in Sect. 3.6, Table 5 and Table A1.
- **(d)** Table A4 and Table A3 are added, the rules that never qualify are named, and guard performance has a sentence (p. 18, l. 805–807: 96 % and 72 %; this reproduces from `dec_guard.csv`).
- **(e)** "Every new-family design goes to trial" is presented as following "from the reference prior and the 20-floor cap" (p. 18, l. 803–804). The uniform prior within ±50 floors qualifies M2, M3 and M5 at 6.25, 6.5 and 15 floors.
- **(f)** Fig. 4 has separate panels, marks g, and its caption says that the share is taken over verdicts "with at least the given margin".
- **(g)** The worked example is qualified as the letter asked.

The response's explanation that the letter's 3.75 and 11.75 floors are the same bands in the new family's own floor is correct: I recomputed them with `guard_band`. One clause is recommended (Sect. 4.3).

**S3 (the new family in the prescribed floor): met.** See N2 above:
- both floors are given, with their intervals;
- no rule is named safest, and the paired difference of M3 and M2 is given in both floors;
- the unit is stated wherever 16–17 floors appear;
- M3 is added;
- Fig. 2, Fig. 4, Table A3 and step 6 all use the produced family's floor.

The only residual is editorial (Table A2).

**S4 (strata, split, labels): met for my items** (m3, m5, m6, m7 and m12). The index qualifier for release-level requirements is missing in the abstract and the conclusions (Sect. 4.2).

**S5 (methods and analyses): met for my items** (m2, m4, m8 and m15). The descriptions of the jackknife+ interval (p. 7, l. 312–316) and of the refit bootstrap (p. 11–12, l. 506–513), which were Reviewer B's points, are also in place.

**S6 (traceability and archive): partly met.**
- *Done:*
  - Table A5;
  - the numbers that carry claims are in the paper (Tables 4, A3 and A4);
  - the result files are corrected: `panel_physical_units.csv` is regenerated, and NN for the waviness with a sibling is now 0.0032 mm, or 1.15 floors.
- *Not done:* the DOI.

**S7 (reuse section): met for my item** (m10).

## 4. New issues arising from this revision

There are no major issues.

### 4.1 The new-setting split is attached to the wrong figure (minor; correction)

*Locations:* Sect. 6.1 (p. 19, l. 874 – p. 20, l. 904); the conclusions (p. 23, l. 1047–1048); the abstract (l. 32–34).

*The problem.*
- **The two sentences.**
  - Sect. 6.1 reads "8.2 for a new setting (4.7 interpolated; 4.9 and 8.9 extrapolated to 500 and 100 kN)".
  - The conclusions read "8.2 for a new process setting (4.7 interpolated; 4.9 extrapolated to 500 kN and 8.9 to 100 kN, with a stroke-speed change)".
- **Whose figures they are** (`panel_force_levels.csv`):
  - The 8.2 floors belong to the force trend, whose own split is 4.65, 8.85 and 8.85 floors.
  - The 4.9 floors at 500 kN belong to the nearest setting, whose own split is 4.65, 4.85 and 11.0 floors and which pools to 8.45.
- **The two readings.**
  - Read as a decomposition of the 8.2 floors, the parenthesis credits one rule with deciding at 4.9 floors when extrapolating to 500 kN and at 8.9 at 100 kN. No rule did.
  - Read as the best rule in each stratum, it picks the rule separately for each stratum, after the results were seen.

*Why it matters.* These are now the paper's headline figures for a new process setting, and this is where S1 and S4 meet.

*The fix.* Name the rules, as Table 5 already does ("nearest setting or force trend"), for example: "8.2 for a new setting (the force trend; by stratum, the nearest setting 4.7 interpolated and 4.9 extrapolated to 500 kN, the force trend 8.9 to 100 kN)". The abstract's "the best rules needed" is less open to misreading, but naming the rules there too would be better.

### 4.2 The release-level statement has lost its index (minor; correction)

*Locations:* the abstract (l. 35–36) and the conclusions (p. 23, l. 1050–1051), which both say "Release-level requirements lay inside every decisive distance except a near-replicate's".

*The problem.*
- The paper defines release criteria as "a performance index of 1.33 or more" (p. 6, l. 236–237).
- Sect. 5.8 rightly restricts the statement to indices "up to an index of 1.33" (p. 18, l. 826–828).
- At indices of 1.67 and 2.0, the limits lie a median 2.46 and 3.14 floors above the 95th percentile (`panel_capability.csv`). That is at or beyond the 2.45 floors at which the nearest setting decides with one resolvable sibling (Sect. 5.4).

*The fix.* Add "at an index of 1.33" in both places, as Table 5 does.

### 4.3 Recommended: show the ±3 band where the near-truth prior is discussed

*Location:* Sect. 5.7 (p. 17, l. 779–782).

*What the text says.* It takes the grid within ±5 floors as the prior "where release-level requirements lie" and reports bands for the nearest setting of 2.0, 4.25 and 14.25 floors.

*What the ±3 grid gives.* The grid within ±3 floors brackets the positions of Sect. 5.8 (medians of 1.0–3.1 floors) at least as closely. Under it (`panel_guard_priors.csv`):
- the nearest setting needs 8.0 floors with a sibling, 5.0 interpolated and 14.75 extrapolated;
- M5 needs 6.5 floors with a sibling, instead of 0.

The sibling band of the nearest setting thus moves by a factor of four between two near-truth priors. The paper does not show this; it uses the ±3 grid only in the worked example.

*Why it matters.* With a band of 8.0 floors, step 6 with the nearest setting releases almost nothing at release level, even with a sibling. I placed requirements 1.75 floors above each alternative's 95th percentile, the median position at an index of 1.33. Step 6 with the nearest setting then sends the following share of sibling cases to trial:
- 6 % with g = 0.25;
- 54 % with g = 2.0;
- 99 % with g = 8.0.

This strengthens the paper's own conclusion that release-level requirements need trials.

*The fix.* One clause would do, for example "(under the grid within ±3 floors, 8.0, 5.0 and 14.75)". The letter's minimum for S2(b) is already met, so this is not a condition.

### 4.4 Editorial

- **Fig. 4 caption.** Add "a new family in the produced family's floor", as the caption of Fig. 2 and the note to Table A3 do.
- **Sect. 3.6, l. 408.** "The 47 distances of the evaluation grid" should be "of the requirement grid", the term used in Sect. 4.5 (l. 517), in Sect. 6.5 and in the code. "Evaluation grid" invites confusion with "the 0.05-floor grid on which [the distances] are evaluated" (l. 369).
- **Sect. 5.4, l. 674–676.** "The nearest setting decided at about 5 floors whenever the new design differed resolvably": with one resolvable sibling it decided at 2.5 floors (l. 643). "At up to about 5 floors" is exact.
- **Sect. 6.5, l. 990–991.** "Scored as well as with full series" should be "within 1.5 floors of full series" (Sect. 5.6).
- **Table A2 note.** Point to Table 4 for the new family in the produced family's floor (remaining point 6).

## 5. Accuracy of the response

I checked every statement that concerns my points against the manuscript and the result files, in:
- Part 1 (S1–S3);
- Part 3;
- Part 4;
- Part 7.

Apart from the two statements and the one weak reason below, they are exact, and the page and line locations given in Part 1 are correct.

1. **The DOI.** The response says three times that the DOI would be in place before resubmission:
   - the preamble: it "is minted when the archive is deposited, before resubmission";
   - Part 3: "The manuscript will not be resubmitted without it";
   - Part 8: it "will replace the placeholder … before resubmission".

   Yet the resubmitted manuscript still cites "[DOI pending]" (p. 28, l. 1267–1268), and the response itself reads "[DOI to be inserted after deposit]". `.zenodo.json` is prepared for version 3 but, as expected before a deposit, carries no DOI. Unless the DOI has reached the editor separately, these statements are not accurate, and S6 is not yet met.
2. **The reason for the prior.** Part 1, S2(a), says: "The text says why the prior represents the requirements a team faces." The text (p. 9, l. 410–412) says what the prior covers ("requirements set from a few to some tens of floors from the true 95th percentile, denser where verdicts are hardest"), not why a team faces that distribution. Sect. 5.7 in fact says that release-level requirements lie nearer the truth. This is a small overstatement.
3. **Table A2.** Part 4, A-r6, justifies keeping Table A2 in the new family's floor by comparability between the variants. That holds in any common floor, so it is not a reason; it does not misstate the manuscript, however.

Where my second-round report was wrong, the response corrects it accurately: the ISO editions, and the grid-step dependence of one uniform-prior band.

## 6. Recommendation

**Accept, subject to the stated minor corrections.**

The three substantive problems of my second report are resolved. In each case the correction sharpens the paper's message rather than weakening it:
- within a family, the production record carries the decision even against a rescaled simulation;
- the guard band belongs to a rule, a relation and a requirement prior, and near-truth priors push release-level decisions towards trials;
- the new family is reported in the unit a team would have, and the paper claims no ranking that two transfers cannot support.

I reproduced every S1–S3 figure from the released files. For the paired bootstrap and the guard bands I also used the author's code, and nothing failed to reproduce. What remains is a condition the editor has already set (the DOI), two wording corrections to headline sentences, and editorial points. None needs new analysis or another review round, and I do not need to see the manuscript again.

*Corrections required before acceptance:*
1. **The DOI.** Mint the archive DOI and insert it in the reference list (p. 28, l. 1267–1268), which the availability statements cite. Confirm that the deposit holds the version-3 code and result files. This is the editor's condition under S6.
2. **The new-setting split.** Attribute it to its rules in Sect. 6.1 (p. 19, l. 874 – p. 20, l. 904) and the conclusions (p. 23, l. 1047–1048), and preferably in the abstract (l. 32–34); see Sect. 4.1.
3. **The release-level sentence.** Add "at an index of 1.33" in the abstract (l. 35–36) and the conclusions (p. 23, l. 1050–1051); see Sect. 4.2.

*Recommended:* the ±3-grid clause of Sect. 4.3.

*Editorial:* the points of Sect. 4.4 and, optionally, intervals for M1sn (new setting) and M1 (new family) in Table 4.

## 7. Confidential comments to the editor

I examined S1–S3 in the depth you asked for. All three are met, and the response describes them exactly. In particular:
- I re-ran the fixed-fit paired bootstrap of M1s against the force trend with the author's `distance_pair`. The intervals are identical, and the force trend is strictly more decisive in all 1,000 resamples.
- I recomputed the new-family bands with `guard_band`, which confirms the author's explanation of your 3.75 and 11.75 floors.
- Every cell of Table A4 and the new-family figures in both floors reproduce from the result files.

I have no integrity concern.

The one unmet condition is the DOI. The response says the manuscript would not be resubmitted without it, but it has been. I would accept once the DOI is in the paper and the deposit holds the result files named in Table A5. Comparing a few of them with the working copy would settle that, for example:
- `dec_intervals.csv`;
- `panel_source_floor.csv`;
- `panel_guard_priors.csv`;
- `panel_step6.csv`.

Corrections 2 and 3 are wording changes that you can check against this report without me.

My second-round query about the ISO editions was mistaken; the author was right. As before, I have not assessed the forming physics or the scan extraction in depth.
