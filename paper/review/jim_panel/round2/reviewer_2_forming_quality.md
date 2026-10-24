# Referee report, second round: Reviewer 2

**Manuscript:** When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing
**Journal:** Journal of Intelligent Manufacturing
**Round:** Second round (first revision)
**Reviewer focus:** Sheet-metal forming practice (deep drawing, die tryout, finite-element process simulation) and quality engineering (statistical process control, process capability, measurement systems analysis)
**Date:** 24 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary of the revision

The revision is thorough and, in my areas, candid. The title and abstract now state the scope: one laboratory process, alternatives produced once and an uncalibrated simulation dataset. The unit is renamed the within-run floor. It is related to the repeatability and intermediate-precision limits of ISO 5725 and called a production-and-measurement floor where the two cannot be separated. Table 4 characterises it with a cluster interval, single-run floors, the floor without warm-up and F/σLT. A measurement subsection and Table 3 report the scanner, its scales, the operation measured, the quantisation of the mid-side draw-in and the direction-dependent biases. Section 5.2 now states that the simulation dataset does not contain the produced process: both friction calibrations end at an edge of the grid, the oil-film mapping is an order of magnitude too sensitive, and the depth offset is unexplained. The decisions are framed as process planning, approval of process changes and qualification of AI tools; tryout is excluded. Further additions are trial reference rows, decision-time strata, a between-run sensitivity, costs, a worked example (Section 3.7) and figures of the parts and of batch centres over a run. The validation of the simulation and the per-series scan redundancy exist only as archive CSV files. The central findings are unchanged and better supported. Four things remain: how far the absolute comparison with the simulation holds, the release-level and trial messages, the worked example, and where the evidence tables live.

## 2. Assessment of the response to my first-round comments

**Major 1, what the floor contains: Resolved.** The unit is renamed, distinguished from the shop floor and called a production-and-measurement floor (p. 6, ll. 269–273). The physical candidates, the tooling check and what remains untestable are reported (p. 15, ll. 667–678). Only the wording of the tooling bound needs work (minor 1).

**Major 2, one run per alternative: Resolved, with one gap.** Table 4 reports the cluster interval, the single-run floors and the floor without warm-up. The between-run sensitivity and "<1" are added (p. 13, ll. 587–590; p. 21, ll. 960–964; p. 8, ll. 361–363), and capability is linked through Table 4, Table 6 and the m̄ + 4σ variant (p. 22, ll. 999–1001). The trial is left out of the sensitivity analysis, and the release-level conclusion ignores the capability variant (major 3).

**Major 3, characteristics and measurement: Partly resolved.** Section 4.3 and Table 3 are what I asked for, OP10 is justified and A3 is narrowed (p. 12, ll. 519–539; p. 15, ll. 664–666). But "absolute values are therefore uncalibrated" (p. 12, ll. 525–527) is not carried into Section 5.2, "partly fitted to the simulation" (l. 524) is unexplained, and sub-pixel edges were declined although the worked example uses the quantised characteristic (majors 1 and 4).

**Major 4, the simulation set-up: Partly resolved.** The rewording is good: grid, censoring, oil-mapping test, labels, DDACS settings, convex arm angles and depth offset as unexplained (p. 7, ll. 284–313; pp. 11–12, ll. 502–515; pp. 16–17, ll. 724–753). There is, however, no validation table in the paper, the extraction noise of the simulated characteristics is never mentioned, and the depth-offset paragraph draws an inference that does not hold (majors 1 and 2).

**Major 5, the decisions modelled: Resolved.** The decision set, the trial rows, the short runs, the costs over c_T/c_FA = 0.01–0.5, the false-accept side and the findings for tryout are all in (p. 2, ll. 78–82; Table 5; Fig. 6; p. 18, ll. 822–824). The worked example's choice of decision is acceptable; its execution is not (major 4).

**Major 6, outcome-defined strata: Resolved.** Decision-time strata are used throughout (p. 9, ll. 393–395; p. 17, ll. 762–766; Table 8), and the numbers reproduce.

**Major 7, scope: Resolved.** The title, the abstract (p. 1, ll. 31–33), the threats (p. 26, ll. 1164–1180) and the paragraph on rates (p. 25, ll. 1130–1133) meet the request; minor 8 adds one sentence.

**Major 8, presentation and positioning: Resolved.** Figs. 3 and 4 are clear and useful, eight rules remain, Section 2.2 covers forming validation and in-line draw-in control, and Table 6 gives physical units.

| Round-1 minor | Status | Note |
|---|---|---|
| 1–5, 7, 8, 10–18 | Resolved | e.g. PPAP p. 4, ll. 165–167; warm-up p. 15, l. 663; stroke speed p. 11, ll. 489–491; ISO 2768-1 scenario removed |
| 6 material, tools, press, lubrication | Resolved as far as documented | p. 11, ll. 483–495 |
| 9 M0 at best-fitting friction | Partly | archive only (`sim_validation.csv`) |
| 19 `meas_sim`, `meas_scan` | Partly | mapped in the archive; extraction noise absent from the paper |
| 20 archive and editions | Partly | pins fixed; DOI and licence pending; ISO editions not verified by me |

## 3. The editor's required changes that concern my expertise

- **R4: partly met.** The rewording, the censoring, the oil-mapping test and the unexplained depth offset are met. The validation table "including the extraction noise" is not in the paper.
- **R5: largely met.** The subsection, Table 3, the statement on uncalibrated values, the tooling evidence, the additions to Table 4 and the renaming are met. The redundancy analysis "in full in the appendix or supplementary material" is only a CSV file.
- **R6, R10, R12 (PPAP): met.** One exception: the trial is not perturbed in the between-run sensitivity.
- **R9: met** by Table 6, apart from its footnote (minor 6).
- **R11, my part:** the figures and the positioning against forming work are met. The main text grew, from p. 23 to p. 27, although R11 asked that it not grow.

**Where the tables went.**
- *Acceptable.* Versioned, checksummed result files are fine for tables whose content the paper reports in words: the further rules, every rule per characteristic, guard bands per prior, and robustness variants.
- *Not acceptable.* They do not suffice for the evidence behind claims in the abstract and the conclusions, which forming and quality readers must see to judge. A CSV file has no caption or definitions. `results/findings.md` mixes current and superseded sections ("supersede Section Q where they differ"). Neither passes through the journal's review and archive as an Online Resource would.
- *Length.* Electronic supplementary material does not count against length, so the length argument does not force this route (major 2).

## 4. New or remaining issues

### Major

**1. The level comparison with the simulation rests on two undocumented inputs (p. 11, ll. 478–479; p. 12, ll. 522–527; pp. 16–17, ll. 724–753; p. 24, ll. 1077–1081).**

The measured draw-in is (210 − Wx)/2, and it depends on two inputs the paper does not document:
- The 210 mm blank is taken from the DDACS mesh (`common.py`, `BLANK_MM`), but the paper states it as a property of the produced blanks; the drafted request to the providers asks for the blank size. One millimetre of blank width moves the mid-side draw-in by 0.5 mm (10 floors).
- A lateral scale error of 1 % moves the mid-side draw-in by about 0.9 mm (18 floors) and the corner draw-in by about 1.4 mm. Nothing in the data pins the scale or the blank down to this level. Wy − Wx is 1.3–1.9 % of the width on a nominally square blank. The wall position at 15 mm depth and the depth differ from the simulation by 2.8–3.5 % and 2.5–3.7 %. Whatever their causes ((d), (e)), the levels carry uncertainties of about a millimetre.

The level comparisons therefore cannot by themselves establish that "the simulation dataset does not contain the produced process". These are the 11 of 42 combinations inside the friction range, the draw-in gaps of 1.8–2.0 and 2.6–3.5 mm, and the Mc edge. The comparisons that are invariant to these inputs do establish it:
- the simulated force effect on draw-in is 2.7–5.1 times the measured one;
- on the concave cup, the simulated wall angle falls by 1.5° from 100 to 500 kN, whereas the measured one does not change (21.60, 21.54, 21.56°);
- the concave arms bend the other way;
- the bottom dome ranks the geometries in reverse order (measured 0.03–0.04 mm concave against 0.09–0.12 mm convex; simulated 0.08–0.14 against 0.02–0.05 mm).

Please:
- (a) state that the blank width is assumed, and give the sensitivity of the levels to it and to the scale;
- (b) rest the conclusion on the invariant comparisons and present the levels as conditional;
- (c) explain "partly fitted to the simulation", and which characteristics depend on that fit;
- (d) correct the depth-offset paragraph (p. 17, ll. 750–752). The three candidates cannot "each" produce both offsets:
  - a drawing depth 1 mm shorter moves the wall at 15 mm depth outward by only tan θ × 1 mm, which is 0.4 mm on the concave cup and 0.2 mm on the convex cup;
  - a lateral scale error fitted to the concave radius (62 mm) predicts about 2.4 mm at the convex radius (73 mm), whereas both read 2.0–2.2 mm;
  - the scanned outer surface against the shell mid-surface explains only 0.3–0.4 mm.

  The data favour an additive cause, a tool about 2 mm larger in radius than in DDACS, which would be a mismatch of set-up, not of measurement;
- (e) report an internal check: the tooling-fixed wall radius at 15 mm depth reads only 0.2–0.4 mm larger on the north side than on the east and west sides (south is shadowed). A y-scale error of 1.3–1.9 % would make that 0.8–1.4 mm. Most of Wy − Wx is therefore probably not a scale error, which points again to the blank. Ask the providers for the blank dimensions and the tool drawing.

**2. The validation and the scan redundancy belong in the paper or an Online Resource (Section 5.2; Table 3; response, "Length").**
- Give a compact validation table or figure in the main text, per characteristic and geometry: the measured centre, nominal simulation minus measurement, the range over the friction grid, the closest grid friction with its residual, and the extraction noise. The text never mentions the discrepancies in wall angle, waviness and dome.
- Put the per-series redundancy analysis (R5) in a short Online Resource. Whether the GP diagnostics (R3a) join it is for the editor and Reviewer 1.
- Keep the CSV files as the machine-readable source, and give readers a `findings.md` that holds only the current numbers.

**3. Release-level and trial messages need the capability statistic and the between-run variation (p. 21, ll. 947–957; Table 8; p. 24, ll. 1061–1066; p. 26, ll. 1193–1194).**

- (a) *Release is a capability decision.* Section 5.6 asks whether a rule confirms q95 ≤ R when R sits where the design has Ppk = 1.33. A release instead asks whether Ppk ≥ 1.33 (≥ 1.67 in an initial study), a decision on m̄ + 4σ or m̄ + 5σ. Your own variant answers this (`qual_variants.csv`): NN needs 3.35 floors with a sibling and 10.55 when extrapolating. In capability terms, NN with a sibling confirms Ppk ≥ 1.33 only for designs whose true Ppk is about 1.33 + 1.12 F/σLT, that is 2.1–3.2; when extrapolating, the true Ppk must be about 3.8–7.3. Please report it this way and add m̄ + 5σ. Note that σLT is a within-run quantity, so these are within-run performance indices.
- (b) *The trial escapes the between-run component.* The trial rows are not given the between-run component that the rules face. I perturbed the truths as `qualify.between_run` does. For τ = 1, 2 and 3, a 20-part trial then decides at 2.05, 3.55 and 5.05 floors and a 50-part trial at 1.90, 3.45 and 5.03, against 3.45, 4.45 and 5.75 for NN with a sibling. For τ ≥ 1, a short trial thus does not decide at the 1.75 floors of a limit at Ppk 1.33 either: near release level the evidence must come from replicated runs. Please add the trial to the sensitivity analysis and revise "otherwise by trial" (Table 8) and Section 6.2.
- (c) *Which prior applies.* Section 6.2 quotes only the reference prior ("93 of the other 98 right"). A requirement 20 floors above q95 corresponds to Ppk ≈ 0.55 + 20 F/(3σLT), about 5–12, which is trivially met. For change approval in series production the release-like prior applies, under which NN decides only 63, 32 and 2 % of verdicts. Tie the prior to the decision class, and qualify "the few close ones" (l. 1066): for drawing tolerances on a capable process, close decisions are the common case.

**4. The worked example uses information the planner would not have (pp. 10–11, ll. 455–471).**

Only 100 and 500 kN have been produced, yet the example uses information from the 300 kN production it is meant to predict:
- the floor of 0.050 mm comes from all nine series; the six produced series give 0.041 mm (my computation);
- the 4.7 floors and the 95 % out-of-sample share come from the held-out 300 kN cells, including the one being predicted, and the 1.5-floor band from that cell alone; two produced levels cannot qualify interpolation within this family;
- "21–67 kN" uses 300 kN data and several characteristics, whereas the secant for the mid-side draw-in is 48.5 kN;
- the stated trial cost (1/20) is never used, although at that cost the cost-minimising band is 4.5 floors, not 2.0.

Please:
- redo the example with the six-series floor, the interpolation band borrowed from the convex family (2.5 floors, with the exchangeability caveat of l. 307) and the cost-optimal band;
- state in step 5 what happens when a family's production cannot exercise a relation.

The release probably survives, with a margin of about 7.4 floors. The example also uses the one characteristic for which A3 fails: its step is 0.38 floors, and three values hold a median 89 % of a series. Switch characteristics or implement sub-pixel edges.

### Minor

1. **p. 15, ll. 674–678.** State the drift bound in floors: 0.05 % of Wx is 0.045 mm, about 0.9 floor of draw-in, so the correlation carries the argument. On the convex cup, r = +0.27 allows a common lateral component of up to about a fifth of the variance of the Wx batch centres (my estimate).
2. **p. 15, ll. 664–666.** "A3 holds for repeatability and resolution" contradicts the clause before it; add "except the resolution of the mid-side draw-in".
3. **p. 16, ll. 728–730.**
   - At μ = 0.15 the concave mid-side draw-in stays 0.012 mm (0.24 floor) above the measurement, so "reaches" overstates.
   - The corner gap of 2.6–3.5 mm holds at μ = 0.10; at 0.15 it is still 1.3–3.3 mm.
4. **p. 16, ll. 734–736; p. 24, ll. 1077–1083.**
   - Mcd's μ = 0.05 is low for oiled DP600 and lies on the grid edge: Mcd compensates for a structural error, so its 30 floors for a new family do not show a successful calibration. Replace "calibrated" (l. 1078) by "friction-fitted (censored)".
   - Add to Section 6.3 that the measured draw-in saturates between 300 and 500 kN (−0.10 against −0.32 mm per 200 kN; local minimum resolvable change 105 kN). This fits friction falling with pressure, or a blank-holder force that does not fully reach the flange (distance blocks, cushion transmission). Ask the providers which.
5. **Section 4.2.** Report the extraction noise of the simulated characteristics: x–y standard deviation of the wall angle 1.8–2.3 floors, dome roughness 2.4–9.8 floors.
6. **Table 6, footnote.** The values in brackets are distances evaluated in the unit, not floors times the pooled floor. For example, the corner with a sibling shows 0.13 mm, whereas 4.5 × 0.046 = 0.21 mm. Reword.
7. **p. 12, ll. 531–533.** OP10 wall angles are pre-trim. On the cut parts, the east wall (the reference direction) differs from OP10 by +0.5 to +1.2° on the concave cups and −0.9 to −1.3° on the convex cups (6–17 floors), against simulated +0.8 to +3.6° and +2.8 to +3.8°. Say so. Read on one instrument, this change is also a validation target that does not depend on the scale.
8. **p. 26, ll. 1168–1170; p. 27, ll. 1202–1205.**
   - The sensitivity "explores" rather than "bounds": τ = 3 is the largest difference between series in one campaign, not across coils and tool states.
   - List what a confirmatory dataset needs from the measurement: documented scan order, a reference artefact scanned through each series, and repeated scans with re-fixturing.
9. **p. 2, ll. 78–82.**
   - The new-family relation is the pre-tryout feasibility question for a new die; say so, and that the results agree with practice (p. 21, ll. 928–929).
   - Under PPAP, a change of force or lubricant usually means customer notification and a resubmission run; say that the framework informs the evidence only where the customer leaves room.
10. **Fig. 4.** Mark the 150-part warm-up and add the punch temperature on a second axis.

## 5. Checks I ran against the archive

All checks were read-only: pandas reads of the result files plus small reimplementations; no pipeline run.

| Check | File(s) | Result |
|---|---|---|
| Checksums | `SHA256SUMS` | Confirmed: 180 of 180 |
| Table 5, every cell | `dec_resolution`, `learn_resolution`, `panel_source_floor`, `learn_source_floor` | Confirmed |
| Table 4; drift factor 2.1–4.5; white share 15–33 %; lag profile | `alt_floor`, `meas_run_floors`, `sens_drift`, `meas_floor`, `panel_variogram` | Confirmed; the lag figures are averages over the geometries |
| Tooling reference: r = −0.27 / +0.27; bound 0.05 % | `meas_tooling_reference`; recomputed from `features_rddac` | Confirmed; the bound is about 0.9 floor |
| Validation of the simulation | `sim_validation`, `panel_force_effect`, `sim_mc_friction`, `learn_mcd_posterior`, `sim_oil_mapping`, `sim_envelope_variant` | Confirmed: 11 of 42; force ratio 2.67–5.13; Mc 72 of 72 at 0.15; Mcd mass 0.73–0.93 at 0.05; oil slopes; 24.15 against 7.15. Wording issues in minor 3 |
| Depth offset 0.70–1.06 mm; wall radius offset 2.02–2.20 mm | `sim_depth_offset` | Confirmed; the radial offset is equal at both radii (major 1d) |
| Blank width of 210 mm | `common.py` | Taken from the DDACS mesh |
| Strata 1.60 / 4.40 floors (75 / 51 cases) | `qual_strata` | Confirmed |
| Tables 6 and 7 | `qual_per_characteristic`, `qual_guard_oos` | Confirmed; footnote issue in minor 6 |
| Trial reference 1.35 / 0.90 floors | `qual_trial`; recomputed from `features_rddac` | Reproduced exactly; 2.05–5.05 floors at τ = 1–3 (mine) |
| τ = 3: NN 5.75 / 10.28; M5 9.30 / 20.18; band 2.88; m̄ + 4σ variant; Ppk limits 1.03–3.14 | `qual_between_run`, `qual_variants`, `panel_capability` | Confirmed |
| Worked example | `dec_intervals`, `learn_intervals`, `qual_costs` | Confirmed: NN 14.994 mm and margin 6.2; M7n 4.5; M0 15.66 mm; truth 8.4 floors. Six-series floor 0.041 mm; cost-optimal band 4.5 |
| Quantisation 6–21 values; minimum resolvable change 21–67 kN | `panel_resolution_steps`, `rob_bhf_pairs` | Confirmed |
| "Partly fitted to the simulation"; ISO editions | `common.py`, sample HDF5 files | Cannot verify |

## 6. Recommendation

**Minor revision.** The revision deals with my first-round concerns in substance:
- the unit is described honestly and characterised;
- the measurement is reported;
- the simulation is presented as what it is;
- the decisions are framed;
- the strata problem is gone;
- every number I checked reproduces.

The central findings stand: within a family the production record is the baseline, the learners reduce to it, and the generic simulation dataset does not represent the process. None of the four remaining issues needs new data. Majors 1 and 2 are mostly rewording and table placement; majors 3 and 4 are small reanalyses the archive already supports. They do change what the paper tells quality engineers about release-level decisions and trials, so they should be settled before acceptance.

## 7. Confidential comments to the editor

This is a careful and transparent revision with an exemplary archive: every checksum and number I checked matches. My one point of principle is the replacement of required appendix tables by CSV files. I would require the validation of the simulation as a compact table or figure in the main text, and the scan redundancy in a short Online Resource, which does not count towards length. The main text grew by four pages despite R11, but the new figures earn their place. The release-level and trial points change the advice to practitioners, not the core findings. I do not need to see the manuscript again if you confirm the four major items, though I would like to see the validation table. The licence, the DOI, the request to the providers and the registration of the frozen procedure remain author actions.
