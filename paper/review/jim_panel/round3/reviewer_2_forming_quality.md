# Referee report, third round: Reviewer 2

**Manuscript:** When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing
**Journal:** Journal of Intelligent Manufacturing
**Round:** Third round (second revision)
**Reviewer focus:** Sheet-metal forming practice (deep drawing, die tryout, finite-element process simulation) and quality engineering (statistical process control, process capability, measurement systems analysis)
**Date:** 24 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary of the revision

The author did what was asked, within the fixed length (31 pages, main text ending on p. 27):
- the worked example now uses only what a planner knows;
- the blank width is stated as assumed, with its sensitivity and that of the scale;
- the simulation finding leads with comparisons that depend on neither;
- release is treated as a capability decision, and the trial joins the between-run sensitivity analysis;
- Online Resource 1 holds the validation of the simulation (Table S3) and the scan redundancy per series (Table S4).

Every number I checked reproduces. Two rewordings remain, neither costing length:
- one scale-free comparison, which I proposed myself, holds only at the nominal friction;
- the trial message has lost its condition outside Section 5.6.

## 2. My second-round points

**Major 1, levels resting on two undocumented inputs: Resolved, with one correction of my own.**
- The blank is "taken as 210 mm wide", and the sensitivities to blank and scale are given (p. 11, ll. 481–483; p. 12, ll. 533–534).
- The finding rests first on scale-free comparisons, and the levels are conditional (p. 16, ll. 716–729).
- "Partly fitted" is explained (p. 12, ll. 530–532).
- The depth-offset inference is corrected (p. 17, ll. 744–746).
- The north-wall check was optional.

Must-fix 1 corrects my own list of comparisons.

**Major 2, validation and redundancy: Resolved.**
- Table S3 gives everything I asked for, per characteristic, geometry and force, extraction noise included.
- Table S4 gives the redundancy per series.
- `findings.md` holds only the current numbers.

**Major 3, release and trial: Partly resolved.**
- (a) Release is a decision on m̄ + 4σ, with within-run indices (p. 21, ll. 960–963).
- (b) The trial joins the sensitivity analysis (p. 21, ll. 963–966; Table S14), but its condition is lost further on.
- (c) The release-like trial rates stand next to the reference ones, and "the few close ones" is gone (p. 23, ll. 1041–1044). The release-like share correct is missing.

Both gaps are must-fix 2.

**Major 4, the worked example: Resolved** (pp. 10–11, ll. 453–473; see Section 3). Step 5 now says what happens when a relation cannot be exercised (p. 10, ll. 437–440).

| Minor | Status | Location |
|---|---|---|
| 1 drift bound in floors | Resolved | p. 15, ll. 678–679 |
| 2 A3 exception | Resolved | p. 15, l. 670 |
| 3 "reaches", corner gap | Resolved | p. 16, ll. 727–729 |
| 4 "calibrated"; saturation | Partly (saturation optional, declined) | p. 23, l. 1057; p. 16, ll. 730–732 |
| 5 extraction noise | Resolved | p. 12, ll. 518–520 |
| 6 Table 6 note | Resolved | p. 18, ll. 817–818 |
| 7 OP10 pre-trim angles | Not adopted (optional) | p. 12, ll. 539–541 give the reason |
| 8 "explores"; measurement needs | Resolved; re-fixtured repeat scans not named | p. 26, l. 1163; p. 27, ll. 1198–1199 |
| 9 pre-tryout; PPAP | Resolved | p. 2, ll. 78–83; p. 21, ll. 932–933 |
| 10 Fig. 4 | Warm-up shaded; no temperature axis | p. 16 |

**Where the tables went: Resolved.** Online Resource 1 carries the evidence behind the abstract and the conclusions. Each table names its result files, and the CSV files remain the machine-readable source.

## 3. The editor's required changes in my area

**C5: Met.** I checked each number against `qual_worked_example.csv` and recomputed it in memory from `features_rddac.csv`, `dec_alternatives.csv` and the stored intervals:

| Text (pp. 10–11) | Archive | Verdict |
|---|---|---|
| floor 0.041 mm (l. 459) | 0.04135 mm | ✓ |
| steps of 0.019 mm; 89 % in three values (ll. 459–461) | 0.0192 mm; 0.891 | ✓ (all 18 series; the six produced give 0.019 mm and 88 %) |
| about 40 kN (l. 462) | secant 39.8 kN (37–45 per pattern) | ✓ |
| convex family: 5.3 floors, band 2.5 (l. 466) | 5.3; 2.5 | ✓ |
| widened to 5.0 (l. 467) | 5.0 | ✓ at c_FR = 0.5 c_FA, which is not stated |
| NN 14.99 mm, margin 7.4 floors (l. 468) | 14.9936 mm; 7.41 | ✓ |
| trend GP margin 5.4 (ll. 469–470) | 5.36 | ✓ |
| M2, M5, M5n contain the limit (l. 470) | upper ends 15.37, 15.58 and 15.33 mm; lower ends below 15.30 | ✓ |
| M0 15.66 mm (ll. 471–472) | 15.663 mm | ✓ |
| truth 14.88 mm, 10.0 floors (l. 472) | 14.8846 mm; 10.05 | ✓ |

The text says that the convex family was produced at all three forces and gives the exchangeability caveat (l. 465). The release survives, with a margin of 7.4 floors.

**C6: Met** on every criterion (locations in Section 2). The criterion's list of comparisons came from my report and needs one correction (must-fix 1).

**C7: Partly met.**
- Met: release in capability terms; the trial rows (Table S14); "explores" (p. 26, l. 1163); "the few close ones" dropped.
- Not met: "once runs differ" appears in Section 5.6 (p. 21, l. 964) but not in Table 8, Section 6.2 or the conclusions.
- Not met: Section 6.2 omits the release-like share correct.

**C10 (validation, redundancy): Met.** Tables S3 and S4 are captioned in the paper's terms and cited at p. 12, l. 520; p. 16, l. 723; p. 6, l. 264; and the note to Table 4. Table S4 is not cited where the redundancy is discussed (optional 4).

**C11 (my items): Met.** The Table 6 note, A3 (p. 15, l. 670) and the 0.9 floor (p. 15, l. 679).

## 4. New issues

### Must fix

**1. The concave wall-angle trend does not hold across the friction grid (p. 16, ll. 718–720; Table S3 note).** The 1.5° fall from 100 to 500 kN holds only at the nominal friction.
- Over the grid's 66 friction–thickness combinations, the simulated change ranges from −1.9° to +1.7°.
- It falls by 1° or more only at μ = 0.10–0.11 (17 %), and 39 % of the combinations lie within 0.5° of the measured −0.04°.
- Source: `features_ddacs_rddac.csv` through `qc.sims_qc`; the nominal values match `sim_validation.csv`.
- The corner force-effect ratio also drops to 1.1–1.4 at μ = 0.05.

Three comparisons do hold over the whole grid:
- the mid-side force effect, 2.8–7.4 times the measured one at every friction and thickness;
- the concave arms, which bend downwards in 89–100 % of all simulations (`panel_arm_sign.csv`);
- the dome ranking, reversed in 76 % of the 198 combinations.

I proposed the wall-angle comparison in round 2 and withdraw it. The fix shortens the text:
- replace "the simulated force effect on the draw-in … the measured one not at all;" with "at every friction and thickness of the grid the simulated force effect on the mid-side draw-in is 2.8 to 7.4 times the measured one;";
- add "in three quarters of the simulations" after "in reverse";
- amend the Table S3 note to match.

**2. The trial message has lost its condition (Table 8, p. 24, ll. 1080–1081; p. 23, ll. 1043–1046; p. 26, ll. 1187–1189).**
- Within a run, the 20- and 50-part trials decide at 1.35 and 0.90 floors (`qual_trial.csv`). That is inside the 1.75 floors of a limit at Ppk 1.33.
- They move out only with τ ≥ 1 floor, to 2.1 and 1.9 floors (`qual_between_run_trial.csv`).
- This is a sensitivity result, not an observation on "18 alternatives".

Rewordings, none longer than the text they replace:
- *Table 8:* "once runs differed by a floor, neither a prediction nor a short trial confirmed the index".
- *Conclusions:* "and once runs differed by a floor, neither a prediction nor a short trial confirmed a performance index of 1.33".
- *Section 6.2, condition:* "once runs differ by a floor" in place of "which needed replicated runs".
- *Section 6.2, share correct:* add "getting 6 of the other 8 right" after "41 and 92". Under the release-like prior the extrapolated band keeps only 75 % correct (`qual_guard_decision.csv`; p. 21, ll. 928–929). Pay for it with ", the natural default where a learned rule shows no advantage" (l. 1052).

### Optional

1. Section 3.7: name c_FR = 0.5 c_FA. The cost band is 5.0 at c_FR = 0.25–0.5 but 5.5 at 1.0.
2. Section 3.7: the borrowed band was validated in nine-series floors but is applied in the six-series floor (0.21 against 0.25 mm). The release holds either way (6.2 nine-series floors).
3. p. 11, l. 482: "moves the mid-side draw-in by 0.5 mm and the corner draw-in by 0.7 mm".
4. Table 3: change 17.6 to 17.7 (`meas_scan.csv` gives 17.65; Table S4 prints 17.7), and cite Table S4 in its note.
5. Draft request to the providers, item 3: a different drawing depth cannot explain the radial offset (p. 17, ll. 744–746), so ask about the tool geometry.

## 5. Checks I ran against the archive

All checks were read-only: pandas reads and released functions imported in memory with `python3 -B`. I ran no pipeline script, and `git status` is unchanged apart from this report.

| Claim | File or method | Verdict |
|---|---|---|
| Checksums; release-note hashes | `sha256sum -c SHA256SUMS`; `RELEASE_NOTES.md` | 190 of 190; four hashes match |
| Worked example | `qual_worked_example.csv`; own floor code and `alternatives.floor_from`; `qualify` functions | Confirmed (Section 3) |
| Table S3, 42 rows; 11 of 42 inside the grid; extraction noise | `sim_validation.csv`, `meas_sim.csv` | Confirmed |
| Table S4; differences in Table 3 | `meas_scan.csv`, `panel_floor_protocol.csv`, `sens_drift.csv`, `meas_characteristics.csv` | Confirmed; 17.6 is a double rounding |
| Scale-free comparisons at nominal settings | `panel_force_effect.csv` (2.67–5.13), `sim_validation.csv` (−1.50°), `panel_arm_sign.csv` | Confirmed |
| The same over all 396 simulations | `features_ddacs_rddac.csv` via `qc.sims_qc` | Wall-angle trend fails (must-fix 1) |
| Offsets 0.70–1.06 and 2.0–2.2 mm; 0.2–0.4 mm from 1 mm of depth | `sim_depth_offset.csv`; tangent of the wall angles | Confirmed |
| 0.011 mm; corner 2.6–3.5/1.3–3.3 mm; Mc 72/72 at 0.15; Mcd at 0.05 | `sim_validation.csv`, `sim_mc_friction.csv`, `learn_mcd_posterior.csv` | Confirmed |
| Release on m̄ + 4σ: 3.35/10.55 floors; index 2.1–3.3/3.8–7.4 | `qual_release_capability.csv`; `qualify.release_capability` | Confirmed |
| Trial under τ; Table S14 | `qual_between_run_trial.csv`, `qual_between_run.csv`, `qual_trial.csv` | Confirmed |
| Table 7; Section 6.2 figures | `qual_guard_decision.csv` | Confirmed |
| Table 6 note | `qualify.per_characteristic`; `qual_per_characteristic.csv` (corner 0.1345 mm) | Confirmed |
| 9.8 floors per mm of blank; 0.9 mm per 1 % of scale; drift bound ≈ 0.9 floor | arithmetic on `common.BLANK_MM` and Table 4 | Confirmed |
| "Partly fitted to the simulation" | `common.py` (line spacing from the dataset's calibration), `qc.py` (directions used) | Directions consistent; the fit itself cannot be checked |

## 6. Recommendation

**Accept subject to the conditions.** In my area the revision meets C5, C6, C10 and C11 and most of C7. The worked example now shows a planner a decision they could actually take. The two must-fix items are rewordings that keep or shorten the length, and the editor can check them against the named files without another round. The central findings stand.

Outstanding, and the author's actions outside the manuscript: the licence, the DOI, a timestamped registration of the procedure, and the request to the dataset providers.

## 7. Confidential comments to the editor

A careful revision: every number I checked reproduced, and the response's page and line references are accurate. Must-fix 1 corrects my own round-2 suggestion, which C6 adopted: I took a nominal-friction trend for a friction-free one. The replacement is shorter and makes the argument stronger. Must-fix 2 restores the condition that C7 asked for. Without it, Table 8 presents a sensitivity result as an observation, and the within-run trial rows of Table 5 contradict it. I do not need to see the manuscript again.
