# Referee report

**Manuscript:** Qualifying design-stage manufacturability decisions with production evidence
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Referee 3:** sheet-metal forming and process simulation; manufacturing metrology

**Basis of review.** I read the PDF (`main_v1.pdf`, 28 pp.), the LaTeX source and the released scripts and result tables. Where I doubted a statement, I recomputed it from the released feature tables (`results/features_rddac.csv`, `features_ddacs_rddac.csv`, `features_ddacs_corners.csv`, `dec_alternatives.csv`, `dec_intervals.csv`, `scen_truth.csv`) and the cached PA12 files, using the author's own functions where possible. All numbers below can be reproduced from those files. My re-implementation of M5 reproduces Table 7 exactly (7 / 2 floors within the family, 12 / 1 pooled, 40 / 30 transfer), so the additional numbers rest on the same basis as the paper's.

## Summary

The paper proposes a unit for design-stage manufacturability decisions, the "production floor": the 95 % quantile of the difference between the centres of two 50-part batches of one design. A decision rule (meets / fails / trial) is characterised by two distances: the decisive distance, beyond which at least 95 % of its verdicts are correct, and the safe distance, beyond which at most 5 % are wrong.

Six rules are scored on the open RDDAC dataset with matched DDACS finite-element simulations: the nominal simulation, a bias correction, a conformal envelope, a Gaussian-process (GP) discrepancy, and gradient boosting with and without the simulation. RDDAC holds 9,000 deep-drawn DP600 cups, produced as 18 series of 500 parts (geometry × blank-holder force × lubrication) and scanned in 3D. Each series is held out in turn and calibrated within its geometry, pooled over both geometries, or on the other geometry only. A calibration budget, an applicability guard, requirement scenarios based on ISO 2768 and a second case on PA12 powder bed fusion complete the study.

The headline results are:
- the nominal simulation needs requirements about 150 floors away before it decides reliably;
- a GP-calibrated envelope decides correctly beyond 7 floors within a family;
- four to five "bracketing" alternatives make the calibrated rules reliable;
- nothing transfers safely across geometries;
- the PA12 build orientations are nearly indistinguishable in production.

## Assessment of contribution and fit

The question is important and fits the collection well: how close to a requirement can a design-stage verdict be trusted, and how much production evidence does that take? Scoring rules by their decision outcomes, with explicit abstention, rather than by prediction error or interval coverage, is a genuinely useful idea, and Table 1 positions it fairly. The open, reproducible pipeline over two public datasets is exemplary; it is what made the checks below possible. The author is also candid about several limitations: the stroke-speed confound, the failure of transfer across geometries, and conformal margins computed from few calibration points.

My concerns are with the evidence underneath the unit and the verdicts, which is where my expertise lies.

1. **Measurement.** The floor is computed from scans whose measurement capability is never assessed. The data show that, for two of the seven characteristics, the part-to-part variation is largely measurement noise, and that the scans contain systematic errors of 1–10° in wall angles and 2–4 mm in flange dimensions.
2. **Simulation extraction.** The simulated characteristics carry extraction noise of several floors that comes from the 1 mm mesh.
3. **Discrepancy interpretation.** The differences between simulation and parts are interpreted without the forming-physics candidates (friction law, blank-holder contact, material model), and the absolute-value transform hides a sign error.
4. **Statistical grounding of the floor.** The floor is not related to statistical process control, process capability or short- versus long-term variation, and it rests on one series per alternative.
5. **Role of the simulation.** Within a family, a GP fitted to the production record alone, without the simulation, does at least as well as the paper's best rule. The "where machine learning helps" message is therefore not supported as stated, and the calibration-design result mostly reflects near-twin alternatives.
6. **Requirement scenarios.** The ISO 2768 scenarios are not realistic requirements for this part and are dominated by easy decisions.
7. **Second case.** The PA12 case violates the paper's own definition of a batch.

Most of these can be repaired with the data at hand, but the repairs will change numbers and probably some conclusions.

## Major comments

### 1. No measurement-system analysis: the floor contains gauge variation, and for two characteristics it is largely a measurement floor

**What is wrong.** Apart from pixel quantisation, the scanner is treated as exact (Sec. 3.2, 6.5). No repeatability, reproducibility or stability figure is reported, and no floor is compared with a measurement uncertainty. Yet several floors are tiny relative to the height quantum of 0.00775 mm:

| Characteristic | Floor | In height quanta |
|---|---|---|
| Cup depth | 0.011 mm | 1.4 |
| Bottom dome | 0.007 mm | 0.9 |
| Flange waviness | 0.0028 mm | 0.36 |

The released feature table shows that measurement noise dominates the part-level variation of two characteristics.

- **Mid-side draw-in** is computed as (420 − Wx − Wy)/4 from the flange widths Wx and Wy.
  - In every series the standard deviation (SD) of Wy is 0.27–0.92 mm, 4–18 times the SD of Wx (0.05–0.15 mm).
  - Wx and Wy are uncorrelated from part to part (r = −0.21 to +0.20). Physical draw-in variation (friction, blank-holder pressure, material) would make the two widths of the same part covary.
  - Wy shows no appreciable serial correlation (lag-1 autocorrelation −0.25 to 0.14). For comparison, Wx reaches 0.66 and the depth 0.76.
  - √(0.08² + 0.5²)/4 ≈ 0.13 mm reproduces the "part SD" of Table 4. If y behaved like x, the part SD would be about 0.03 mm.
  - White noise of 0.13 mm on its own produces a batch-difference floor of about 0.05 mm (1.96·√2·0.13/√50). That is most of the permutation ("scatter") floor of 0.061 mm and more than half of the floor of 0.085 mm.
- **Wall angle** is the mean of the E, W and N walls.
  - The N wall has a part SD of 0.31–0.38° in every series, two to eight times the E/W values on the concave cups.
  - The N wall is uncorrelated with the E wall (r = −0.07 to 0.11) and with its own value on the previous part.
  - Its contribution of about 0.11° to the three-wall mean explains the part SD of 0.13°, and about 0.045° of the 0.081° floor.

Sec. 5.1 says that, for these two characteristics, "their parts scatter widely but their batches stay close". That sentence describes the gauge, not production.

For depth, dome and waviness, the floors can be reached statistically by averaging. Whether a triangulation scanner is stable to that level over a 500-part series is unknown. A z-gain drift of 0.04 % changes a 28.4 mm depth by one floor. The drift factors of 3.9 for depth and dome (Table 4) therefore cannot be attributed to the process unless a reference artefact is scanned through the series.

**Why it matters.**
- The floor is the unit of every result. Gauge variance enlarges F, and therefore makes every rule look better when expressed in floors: the unit rewards a poor gauge.
- The effect-to-scatter ratios (ESRs), the minimum resolvable changes, the safe and decisive distances, and the conclusion that "production has a resolution, and it is set by drift" (Sec. 6.1) all inherit this gauge variance.
- The "true" q95 is inflated too, by roughly 1.645·(0.13 − 0.03) ≈ 0.16 mm for the mid-side draw-in and ≈ 0.14° for the wall angle. That is about 2 floors each, the same size as the safe distances being reported.

**What would fix it.**
- (a) Run a gauge study:
  - repeated scans of a sample of parts with re-fixturing (type-1 and type-2 studies per AIAG MSA or VDA 5);
  - scans of a calibrated artefact at the start, middle and end of a series, to separate scanner drift from process drift.

  If the RDDAC authors cannot supply repeats, estimate the measurement variance from the redundancy in the data: x versus y widths, E versus W walls, and residual noise on the flat bottom.
- (b) Report %GRR relative to each floor, and the number of distinct categories.
- (c) Decompose the floor into measurement and process parts with a nested variance-component model. Define the production floor on the process part, or report both.
- (d) Rewrite Sec. 5.1 and 6.1 accordingly.

### 2. Systematic scan errors make the absolute offsets, and the claim of "identical" measurement, unreliable

**What is wrong.**

- **The south wall is not missing data.** Sec. 4.3 says this wall is shadowed by the scanner and excluded. In fact the pipeline returns valid-looking values that are wrong by 7–10°:
  - 12.3–14.9° on the concave cups, where E and W read about 21.3–21.8°;
  - 19.1–21.5° on the convex cups, where E and W read about 11.2–12.0°.

  Only two convex series are mostly NaN (`op10_wall_angle_S_deg`).
- **The wall angle after cutting was dropped without mention.** The docstring of `qc.py` notes that "on the cut convex parts the north and, in some parts, the west wall read 5–7 degrees steeper than the east wall" (scan artefacts on walls facing the camera). For that reason the code drops the wall angle after cutting, a decision the manuscript does not mention.
- **The N wall disagrees after drawing too.** The same docstring states that all three walls "agree after drawing". They do not. On all nine convex series, the N wall reads 0.9–1.9° lower than the mean of E and W. This moves the three-wall mean by 0.3–0.6°, i.e. 4–8 floors.
- **Wy is systematically larger than Wx.**
  - Wy exceeds Wx by 2.1–3.7 mm in every series. The simulation gives Wx − Wy = 0.065 mm, and the scanned walls at 15 mm depth agree within 0.3 mm between x (E, W) and y (N).
  - The two flange diagonals differ by 1.6–2.2 mm in every series (`op10_Ld1_mm` versus `op10_Ld2_mm`). This is consistent with a non-orthogonality of about 0.4° between the scan axes, or with non-square blanks.
  - Blank dimensions are not reported, and draw-in is referred to the nominal 210 mm.
- **The scanned wall is about 2 mm outboard of the simulated one.** At 15 mm depth the scanned wall lies 2.0–2.5 mm outboard of the simulated mid-surface:
  - concave: 64.3–64.6 mm versus 62.3 mm;
  - convex: 74.9–75.4 mm versus 72.9 mm.

  Half the thickness of the die-side surface explains about 0.5 mm. The remainder, about 3 % of the radius, is either a difference in tool geometry between DDACS and the physical tool, or an in-plane scale error.
- **Mid-surface versus scanned surface.** Shell nodes lie on the mid-surface; the scanner sees the die-side surface. No correction is applied for this.
  - The bottom-to-flange depth then differs by (t_bottom − t_flange)/2. The flange thickens (DDACS shows up to +16 % in the corners), so this is tens of µm, i.e. several depth floors.
  - The wall angle shifts with the thickness gradient along the wall: of order 0.1°, about one floor.

**Why it matters.**
- Three results mix simulation error with measurement bias, blank size and surface-definition differences: the M0 headline (150 floors), Table 6, and statements such as "the simulation overestimates the corner draw-in by about 3 mm".
- The excess (Wy − Wx)/4 alone accounts for 0.5–0.9 mm of the −1.4 to −1.8 mm mid-side offset.
- The N-wall bias is as large as the margins (2.1–5.1 floors) that decide the class-c truth for the convex wall angle in Table 9.

**What would fix it.**
- Validate the scan geometry against a traceable reference:
  - CMM measurements of a few parts per geometry;
  - a ball bar, step gauge or flat scanned in the same fixture;
  - acceptance testing as in VDI/VDE 2634 Part 2 or ISO 10360-8, depending on the sensor type.
- State the scanner type, the fixture, the specified error limits, and how `calibration.json` was obtained.
- Report Wx and Wy, L1 and L2, and the per-side angles.
- Base the wall angle on the E/W pair, which is symmetric and cancels tilt, or justify the use of N.
- Obtain the blank dimensions.
- Offset the shell mid-surface by half the local thickness before comparing.
- Replace "measured identically" with an explicit list of the differences that remain.

### 3. Extraction on the 1 mm simulation mesh adds noise of several floors, and the envelope maximum amplifies it

**What is wrong.**

- **Asymmetry in a symmetric model.** The quarter model is symmetric about its diagonal (Wx − Wy = 0.065 mm), so its x-arm and y-arm wall angles should agree. Across the 396 RDDAC simulations they differ by more than 0.1° in 13 % and by more than 0.3° in 8.3 %, with a maximum of 1.0°.
- **A staircase over the input grid.** Over the friction–thickness grid, the simulated wall angle forms a staircase.
  - Example (concave, 100 kN, friction 0.05): 19.54, 19.54, 19.55, 20.23, 20.25 and 20.26° for thicknesses from 0.95 to 1.00 mm.
  - The step of about 0.7° runs diagonally through the grid. This is the signature of a level crossing jumping between 1 mm radial bins, not of mechanics.
- **Roughness in floors.** I used, as a roughness measure, the residual of each simulated value from the mean of its two neighbours along the friction grid. Its SD, in floors:

  | Characteristic | Roughness SD (floors) | Maximum (floors) |
  |---|---|---|
  | Wall angle | 2.1–3.4 | 6–12 |
  | Bottom dome | 3.0–12 | 12–35 |
  | Waviness, convex | 4.9 | 24 |
  | Arm angle, cup depth | about 1 | 3–3.6 |
  | Both draw-ins | below 0.25 | 1.0 |

- **The envelope maximum.** M2 and M5 use the maximum over the 66 simulations of a geometry × force cell (`sim_env_hi`), the statistic most sensitive to such outliers.
  - Within a family, the simulation enters M1, M2 and M5 through a single number per force level, identical for the three lubrication patterns.
  - For wall angle and dome, this number is partly extraction noise.
- **The definitions are not identical between scans and simulations.**
  - Scan waviness excludes a 3 mm edge zone and uses an iteratively trimmed fit; the simulation does neither.
  - 0.5 mm versus 1 mm bins, and a 0.31 mm block grid versus a 1 mm mesh, give different spatial bandwidths.
  - The dome is fitted on a distance-transform core of the scanned plateau, but on a disc of nodes within 0.5 mm of the top in the simulation.

**Why it matters.**
- The decisive distances of M5 per characteristic (1.5–6.5 floors) are of the same order as this extraction noise.
- A.2 concludes that "a surrogate can stand in for the simulation only for its smooth outputs". That conclusion is partly an artefact of the extraction.
- The wall-angle ratios in Table A3 (4.1, −2.0, 2.2, 2.8, 5.5, −83) look like noise.

**What would fix it.**
- Extract from the interpolated shell surface (shape functions), or fit lines or planes to the wall over the evaluated height, instead of taking medians of binned nodes.
- Quantify the extraction noise: x versus y arms, jittered bin edges, and a few runs on a refined mesh.
- Replace the raw envelope maximum with the maximum of a smooth response surface over the plausible input range, or with a high quantile.
- Make the scan and simulation definitions genuinely identical, and list what remains different.

### 4. The interpretation of the simulation discrepancies is under-developed and partly wrong

**(a) A sign error is hidden by absolute values.** For arm angle and dome, both parts and simulations pass through |·| (`decisions.transform`).
- Every scanned concave part has a positive arm angle (0.08–1.09°).
- 89–100 % of the concave simulations are negative, with cell medians of −0.8°, −4.0° and −4.3° at 100, 300 and 500 kN.
- As a result, the concave 100 kN alternatives look well predicted in Table 6 and for M0/M1 (|nominal| 0.74° against q95 0.71–0.97°), even though the simulation bends the arms the other way.

With symmetric limits the verdicts are unaffected. An assessment of simulation credibility (Table 6, Table A3), however, must use signed values.

**(b) Blank-holder force.**
- Measured mid-side draw-in falls by 0.094 mm per 100 kN. The simulation at 0.99 mm and μ = 0.10 falls by about 0.5 mm per 100 kN.
- The measured cups at 100 kN show roughly the draw-in, or less, that the simulation predicts for 500 kN.
- The usual causes of such a mismatch lie in the friction law and the boundary conditions, not in "the solver":
  - constant Coulomb friction, where in reality friction decreases with contact pressure (e.g. Hol et al. 2012, Wear 286–287);
  - a rigid blank holder bearing on the thickened corners (does shell thickening enter the contact?);
  - spacers or a cushion-pin layout that limit the effective pressure;
  - elasticity of the press and the tools.
- The data also show an asymmetry that a quarter-symmetric model cannot represent:
  - the load-cell imbalance at 20 mm stroke is 0.09–0.37 (`imbalance20`);
  - the flange is off-centre relative to the cup by 0.3–3.9 mm in x: the E–W extent difference is 0.6–7.8 mm, while the walls at mid-depth are symmetric within 0.3 mm about the same centre;
  - the offset is roughly 2–4.5 mm in y;
  - both offsets vary from series to series.

**(c) The friction ratios of "5 to 630 times".** These ratios use within-series slopes on the friction equivalent of the measured oil film. Such slopes are unreliable for four reasons:
- they are attenuated by measurement error in the film (errors-in-variables);
- they are estimated over a narrow range (within-series SD of 0.06–0.21 g/m²);
- they are distorted by the clamping of the mapping: up to 30 % of a series lies below 0.8 g/m² and up to 20 % above 1.6 g/m², and up to 46 % of the matched simulations sit at an end of the friction grid;
- the traverse measures a line across the blank, not the film in the die-radius contact.

A ratio of 630 with mixed signs indicates a near-zero denominator. It cannot single out "the oil-to-friction mapping rather than the solver". The same caveat applies to the sheet-thickness slopes (within-series SD of 2.3–4.9 µm in 17 of 18 series) and to the thickness MRCs of 19–147 µm.

**(d) Cup depth.** The offset of 0.9 mm is almost the same for both geometries and all settings. Meanwhile, the recorded bottom-dead-centre position (`pos_bdc_mm`) is constant within 0.22 mm over the 18 series. This points to a difference in drawing depth or reference between DDACS and the experiment, rather than to forming physics.

**(e) Springback.** Wall angle, arm angle and dome are dominated by springback and depend on the material model. The Bauschinger effect, kinematic hardening, and the decrease of the unloading modulus with plastic strain are first-order effects for DP600 (cf. Wagoner et al. 2013, cited by the author; Yoshida and Uemori 2002). The manuscript states neither the DDACS material, hardening, friction and contact models, nor whether the RDDAC coil was characterised.

**(f) The bottom may be bistable.**
- The convex dome jumps between series: 0.057 mm for convex/300/coarse against 0.125–0.132 mm for the other two oil patterns.
- The simulated concave dome jumps by up to 35 floors between neighbouring friction steps.

A thin, nearly flat bottom may snap between two states after trimming. A floor and a q95 computed from a two-state mixture are not meaningful.

**Why it matters.** The "where machine learning helps" discussion treats the simulation as biased but informative. If the bias has identifiable physical causes, the appropriate baseline is a physically calibrated simulation (Kennedy–O'Hagan with calibration parameters, which the paper cites but does not use), and the GP discrepancy partly absorbs known model-form errors.

**What would fix it.**
- Use signed offsets.
- Calibrate friction (or a pressure-dependent friction law) and an effective blank-holder force at one force level, and test at the other levels.
- Add a rule with a calibration parameter in the Kennedy–O'Hagan sense.
- Treat the within-series slopes for errors-in-variables, or remove the friction column of Table A3.
- Document the DDACS models and the drawing depth.
- Discuss the asymmetry and the possible bistability of the bottom.

### 5. The floor is not related to statistical process control, process capability, or short- versus long-term variation

**(a) The statistic and special causes.**
- F is the 95 % quantile of 45 dependent pairwise differences between the ten batch means of a series, pooled over series.
- Under a trend, the largest differences are first versus last batch, so F grows with the length of the series.
- F is not a variance component, and its relation to the short-term and long-term standard deviations (σ_ST, σ_LT) is not given.
- The batch trajectories show three different mechanisms:
  - **warm-up:** in five series the first one or two batches have a depth 8–9 µm low;
  - **steps:** in several series, mid-series steps coincide with dips of the punch temperature around batches 4–7, probably interruptions;
  - **opposite trends:** for the corner draw-in, concave/100/coarse runs from +31 to −29 µm while concave/300/coarse runs from −25 to +26 µm.
- These series are not in statistical control, and a floor driven by such special causes describes how the trial was run.
- The author's own sensitivity analysis moves F by a factor of 0.64–2.2 for batch sizes B = 25–100 and quantiles α = 0.90–0.99.

**(b) A mean-based unit for a tail-based requirement.**
- F is defined on batch means, whereas adequacy is defined on the q95 of single parts.
- Where the part SD exceeds F, the uncertainty of q95 is governed by within-batch scatter, not by F.
- A floor defined on q95 (|q95_i − q95_j| between batches) would match the requirement.

**(c) One series per alternative.**
- The "truth" is the q95 of a single series; the variation between series of the same setting is unknown, and the 500 parts are pseudo-replicates of a single setup.
- The data show setup differences between series:
  - bottom dead centre at 448.57–448.79 mm;
  - flange offsets that differ by several millimetres;
  - punch temperature at the start of a series of 21.2–30.2 °C;
  - oil film of 0.85–1.13 g/m² for one and the same "pattern" (fine);
  - sheet-thickness medians of 986 µm with an SD of 4.8 µm (convex/100) against 990–993 µm elsewhere, which suggests different coils.
- Safe distances of 0.5–2 floors are smaller than the plausible uncertainty of the truth itself.

**(d) The adequacy share.** p = 0.95 means up to 5 % nonconforming parts. That is far from production acceptance: Cpk ≥ 1.33 corresponds to about 63 ppm, and Ppk ≥ 1.67 is common at launch. A rule that is safe at q95 need not be safe in the tail.

**(e) Engineering relevance.**
- Decisive distances of 1.5 floors of waviness (about 4 µm) or 5 floors of depth (about 50 µm) lie far below any tolerance a drawing of this part would carry.
- M0's 150 floors are driven by characteristics whose floors are only 9–53 µm.

**What would fix it.**
- Fit a nested random-effects model (alternative / batch / part) with REML variance components.
- Report σ_ST from rational subgroups of 3–5 consecutive parts, σ_LT, and the corresponding capability indices (ISO 22514-2).
- Identify interruptions from time stamps or the temperature record, and report floors with and without them.
- Add a floor defined on q95.
- Show how all distances depend on B, α and series length (for example, floors computed from the first 250 parts only).
- Use the three oil-pattern series of each geometry × force cell, which the paper finds mostly indistinguishable, as quasi-replicates to estimate between-series variation.
- Test adequacy at p = 0.99 and p = 0.99865, with a parametric tail.
- Give the distances also in physical units, relative to realistic tolerance widths.

### 6. Within a family the simulation contributes nothing measurable: a Gaussian process without the simulation does as well as M5

**What is wrong.** Two central claims rest on comparing M5 with M4:
- "the best rule combines the simulation envelope with a Gaussian-process correction" (Sec. 5.4);
- "machine learning helps where it corrects a physical model with the production record" (Sec. 6.3).

M5 is a GP on the q95 offsets of whole alternatives. M4 is gradient boosting on single parts, with resampled residuals and a nested offset and margin. Moving from M4 to M5 therefore changes the model class and the level of modelling at the same time as adding the simulation.

The obvious control is missing: the same GP, with the same descriptors and settings, fitted to q95 directly without the simulation baseline. I ran it with the author's functions (`decisions.descriptors`, `verdicts`, `distance_table`; same kernel, normalisation, restarts and 90 % level; 300 bootstrap resamples for the intervals). My M5 reproduces Table 7 exactly.

| Scope | M5 (paper): decisive / safe (floors) | Same GP without simulation: decisive / safe | At \|d\| = 10, M5: right / trial / wrong | At \|d\| = 10, without simulation: right / trial / wrong |
|---|---|---|---|---|
| Within family | 7 / 2 (bootstrap 6.5–8 / 0.5–4.5) | 6 / 1.5 (5.5–7 / 0.5–3) | 97.2 / 2.8 / 0 % | 99.2 / 0.8 / 0 % |
| Pooled | 12 / 1 | 9 / 1 | 93.7 / 6.3 / 0 % | 96.8 / 3.2 / 0 % |
| Transfer | 40 / 30 | 150 / 150 | 76.6 / 2.8 / 20.6 % | 57.9 / 5.2 / 36.9 % |

Per characteristic within the family, the GP without the simulation compares with M5 as follows (decisive distance in floors):

| Characteristic | GP without simulation | M5 | Without simulation is |
|---|---|---|---|
| Waviness | 1.5 | 1.5 | equal |
| Corner draw-in | 2.5 | 2.5 | equal |
| Arm angle | 6.5 | 6.5 | equal |
| Bottom dome | 12 | 15 | better |
| Wall angle | 3.5 | 2.5 | slightly worse |
| Mid-side draw-in | 5.5 | 4.5 | slightly worse |
| Cup depth | 5.5 | 5 | slightly worse |

**Why it matters.**
- Within a family and pooled, the decisive ingredient is GP interpolation of the produced alternatives' q95 over blank-holder force and oil-pattern rank.
- The simulation helps only across geometries, and there no rule is safe below 30 floors without the guard.
- This reverses the emphasis of the abstract, Sec. 6.3 and Table 12.

**What would fix it.**
- Add this control, and, if feasible, a part-level M4 with the same GP model class.
- State plainly that, in this demonstration, the value of the simulation is confined to transfer across geometries.
- Revise the abstract, Sec. 6.3 and Table 12 accordingly.

### 7. Scope: the within-family "design" decisions are process settings on an existing tool, calibrated on near-twins

**What is wrong.**

- **These are process-window decisions.** Within a family, the held-out alternative differs from its calibration alternatives only in blank-holder force and/or oil pattern, on the same tool. Eight produced variants of one tool describe tryout or process-window selection, not a design-stage product decision.
- **The one geometry change in the data is drastic.** Concave ↔ convex changes four things at once: the base shape, the wall angle (20° ↔ 10°), the curvature radius (100 ↔ 150 mm) and the bottom radius (7.5 ↔ 10 mm). Here the novelty guard sends 90.5 % of the verdicts to trial, and correct verdicts at 10 floors drop to 5–8 % (`dec_guard.csv`). The demonstration therefore delivers no reliable verdict for a new design.
- **"Brackets" mostly means "a same-force sibling exists".** The calibration-design result has the same limitation.
  - `budget.py` classifies a calibration subset as "brackets" when min ≤ force ≤ max over its alternatives. This includes every subset that contains an alternative at the same force as the target.
  - For targets at 100 or 500 kN, bracketing therefore simply means that a same-force sibling exists.
  - Enumerating the subsets: 81 % (k = 2) to 96 % (k = 5) of the bracketing subsets contain a same-force sibling, for which M1, M2 and M5 use identical simulation values. True interpolation (100 and 500 kN → 300 kN) accounts for only 4–19 %.
  - "Four to five produced alternatives that bracket the new design's process settings" therefore largely means "the same tool at the same force with another oil pattern has been produced". Since the oil pattern cannot be resolved for most characteristics, that is a near-replicate.
- **Force brackets speed too.** The 100 kN level carries the change of stroke speed, so "bracketing the force" also brackets the speed.

**What would fix it.**
- Reframe the within-family scope as process-window decisions after tooling, or argue why it is a design decision.
- Split Table 8 into three classes: same-force sibling, true interpolation, and extrapolation.
- Report the guarded transfer results as "no verdict".
- Revise the abstract and conclusions accordingly.

### 8. The ISO 2768 scenarios are not realistic requirements for this part, and the 89 % is dominated by easy decisions

**(a) Which standards apply.**
- ISO 2768-2 was withdrawn in 2021 and replaced by ISO 22081:2021. The new standard specifies general geometrical specifications as a profile tolerance relative to a datum system, without class tables.
- Deep-drawn parts are usually specified with ISO 1101 surface-profile and position tolerances to a datum system, plus trim-line tolerances.
- DIN 6930-2, which the code considers, has no flatness tolerance.
- None of this is discussed in the paper.

**(b) The flatness row.**
- The flatness row depends on the size of the toleranced feature; the author's own notes cite clause 5.1.1 (the longer lateral length of the surface).
- By my estimate from `wall_r15` and the wall angle, the flat bottom is about 105–130 mm across between the punch-radius tangents.
- So the 100–300 mm row applies (H 0.2, K 0.4, L 0.8 mm), not the 30–100 mm row that the paper selects via an 80 mm evaluation circle.
- With the correct row, all 18 alternatives meet class H (the largest q95 is 0.138 mm), and flatness no longer discriminates between alternatives.

**(c) The dome is not a flatness value.** The sag of a rotationally symmetric paraboloid fitted with free tilt ignores saddle and twist components. Flatness is a minimum-zone value over the whole face (ISO 12781).

**(d) Tolerances apply to features, not to averages.** A drawing tolerance applies to each wall and each arm, but the scenarios use averages that hide per-side differences:
- the four arms of one part differ by up to 0.7° (concave, E–W) and by 1.5–1.7° (convex, N–S);
- for concave/100/fine, the median north-arm angle is 1.10°, above the class-c limit of 1°, while the four-arm mean "meets" (q95 0.94°).

**(e) Most decisions are easy.**
- Seven of the nine tolerance classes have the same truth for every alternative of a family: wall f/m, c and v; flatness K and L; and arm c and v, which split exactly by geometry.
- Only arm f/m on the concave cups and flatness H on the convex cups discriminate within a family.
- Of the 162 decisions, 57 % lie more than 10 floors from the limit and 34 % more than 20. Only 42 (26 %) lie within 5 floors.
- I recomputed the verdicts from `dec_intervals.csv` with the logic of `scenarios.py`. Within the family:
  - M5 is right in 60 % of the 42 near-limit decisions (36 % trial, 5 % false reject), and in 96–100 % of the decisions beyond 5 floors;
  - M1 is right in 62 % near the limit, with 19 % false accepts.
- "89 % correct without a false accept" is therefore mostly a statement about decisions far from the limit.

**(f) Acceptance.** Requiring q95 ≤ R, i.e. accepting up to 5 % nonconforming parts, is not how a drawing tolerance is judged.

**What would fix it.**
- Derive the requirement scenarios from the part's function, or from realistic per-feature profile and position tolerances (e.g. an arm profile of ±0.5 mm relative to the bottom datum and the cup axes, and a trim-line position).
- Use an acceptance criterion consistent with process capability.
- Report the results stratified by margin.
- Drop ISO 2768-2, or use the correct row together with a minimum-zone flatness.

### 9. The DDACS design corners are announced but not used, and the stated limitation is inaccurate

**What is wrong.**
- **No corner result is reported.** Sec. 4.2 says that 264 corner simulations "are used for the design-space analysis (Appendix A)", but no corner result appears in the manuscript. A.2 reports only surrogates and sensitivities over process conditions at the tool geometry. The corner-step sensitivities exist only in the repository's `findings.md`.
- **The limitation is stated incorrectly.** Sec. 6.5 states that "three geometric parameters change together, so single geometric effects are not identifiable". For the convex family, however, the step from the tool to the upper corner changes only the wall angle (`design_space.py`, `features_ddacs_corners.csv`):
  - tool: curvature radius 150 mm, bottom radius 10 mm, wall angle 10°;
  - upper corner: curvature radius 150 mm, bottom radius 10 mm, wall angle 30°.
- **The corners cannot test a decision rule.** They are far apart (by the author's own numbers, the steps move the wall angle by 10–264 floors) and have no production counterpart.

**What would fix it.** Either present a design-space analysis a designer can use, or remove the corners from the paper and correct the limitation statement. A usable analysis would give:
- per-step sensitivities in floors;
- the convex wall-angle step as a clean single-factor case;
- what a minimum resolvable geometric change would be, and with what credibility.

### 10. The PA12 case violates the paper's own definitions, and its conclusion is an artefact of an inflated floor

**(a) A batch here is not one design.**
- A "batch" is one 30° orientation class within one build: six or seven different orientations at randomised positions, not consecutive parts of one design.
- The spread of orientation means within a class (SD 0.034–0.16 mm across characteristics) is as large as the spread between class means (0.009–0.12 mm), and it goes into the batch noise.

**(b) Builds are blocks, which biases the ESR low.**
- Builds are common to all classes: each orientation appears once per build, in a randomised layout.
- The build effect cancels in class contrasts, because all class centres average the same three builds. It does not cancel in the floor, so the ESR is biased low.
- Three builds give three batch means per class and 18 pairwise differences per characteristic. The 95 % quantile of 18 differences is essentially their maximum.
- The class q95 is the 95 % quantile of 18–21 specimens, i.e. close to their maximum.

**(c) With build as a block, the orientation effect is clearly resolved.** I fitted a two-way fixed-effects model on the signed deviations, with build as a block.
- The orientation-class effect is significant at 5 % for seven of eight characteristics:
  - p < 0.001 for cylindricity, the 24 mm pin and the hexagon;
  - p = 0.003–0.033 for the 8 mm pin, both holes and position;
  - flatness: p = 0.90.
- The range of build means (0.019–0.036 mm) is far below the floors (0.051–0.31 mm).
- Two statements in the paper are therefore artefacts of the floor definition: that "production barely separates the orientations", and that "the record of one orientation decides for the others within 2 floors".

**(d) The data needed for a proper floor are present but discarded.**
- The dataset contains eight identical anchor specimens per build (24 in all), which `case2_pa12.py` discards.
- Their within-build SD (0.04–0.29 mm) exceeds the SD of their build means (0.007–0.10 mm): position in the build volume matters more than the build.
- The z level is significant for the hexagon (p ≈ 10⁻⁴), yet position is ignored.
- The CMM repeatability (SD of the three repeats, 0.003–0.012 mm) is available but not reported.

**(e) The nominal predictor is a straw man.** M0, the nominal geometry, ignores the scaling and offset compensation that every PBF process applies.

**What would fix it.** Either redo the case properly or drop it.
- **Redo:**
  - use individual orientations (or narrow classes) as alternatives;
  - treat builds as blocks and position as a covariate;
  - base the floor on the anchor specimens, or on the residual of an orientation + build + position model;
  - accept that three specimens per orientation cannot support an empirical q95 without a parametric model.
- **Drop:** remove the case and temper the generality claims (abstract, Sec. 6.4).

## Minor comments

1. **Sec. 1 (p. 2) and Sec. 3.2 (p. 6).** The paper argues that "a difference between two alternatives smaller than the floor cannot be resolved in production, so no design-stage decision needs to be finer". Conformity concerns one alternative's q95 relative to a limit, and the q95 can lie arbitrarily close to that limit; whether two alternatives can be told apart is a different question. Rephrase, or justify the claim through the uncertainty of q95.
2. **Eq. (2), p. 6.**
   - State that all pairs i < j within an alternative are pooled (per geometry in the decision analysis).
   - State that the pairs are dependent, and how this affects the bootstrap interval.
   - Note that the decision analysis uses the per-geometry floors, not the floors quoted in the abstract.
3. **Sec. 3.2 (p. 6) and A.1 (p. 22).** Wx lies on a 0.038 mm half-pixel grid and Wy on a 0.079 mm grid, both small against the part SDs of the widths. The 38 % larger median-based floor of the mid-side draw-in (repository findings) is therefore more plausibly the heavy-tailed y-edge noise of Major comment 1 than quantisation.
4. **Sec. 4.1 (pp. 8–9).** "On one tool set in two geometries" is unclear. Please give:
   - the tool data (punch and die radii, clearance, drawing depth);
   - the blank-holder system (cushion, springs, spacers);
   - how the blanks were cut, and to what tolerance;
   - the rolling direction relative to the scan axes;
   - the scanner type and fixture, and whether scans were taken in-line or later;
   - the order and dates of the 18 series.
5. **Sec. 4.2 (p. 9).** The nominal simulation (0.98 mm) is 0.01 mm below the measured median thickness (0.990 mm; series medians 0.986–0.993 mm). Most parts are matched to 0.99 mm, and up to 25 % of a series to the grid end at 1.00 mm. Use 0.99 mm or justify 0.98 mm.
6. **Sec. 4.1 (p. 9) and Sec. 6.5 (p. 20).**
   - The lubrication "patterns" differ systematically in oil amount: series medians of 1.15–1.48 g/m² (coarse), 0.92–1.23 g/m² (medium) and 0.85–1.13 g/m² (fine).
   - The range between series of one pattern is as large as the range between patterns.
   - State what was actually controlled. "Pattern, not a friction coefficient" understates this.
7. **Table 3 (p. 10).**
   - List the differences that remain between scan and simulation extraction (Major comments 2 and 3).
   - The scan wall mean weights x and y by 2/3 and 1/3 (E, W, N), whereas the simulation weights them 1/2 and 1/2.
   - Give the sign conventions for arm angle and dome.
8. **Table 3, wall angle (p. 10).** The radial coordinate is taken in the scanner frame, and the depth is a vertical distance to the fitted plane. With the residual tilt of 0.07–0.09° (`op10_bottom_tilt_deg`), opposite walls shift by about ± one floor. E and W cancel each other; the unpaired N wall does not.
9. **Sec. 5.2 (p. 11).** The paper says that "variation of the incoming material within a series is too small to matter". Only thickness and oil were measured, not strength, hardening or anisotropy, and the thickness slope is attenuated by gauge noise over a ±3 µm range. Restrict the statement to thickness.
10. **Table 5 (p. 11).** The minimum resolvable force change comes from a linear slope over 100–500 kN. The sensitivity changes strongly between the two intervals (Table A4): 48 versus 1083 kN for the arm angle, 21 versus 78 kN for the waviness. The 100 kN level also includes the speed change (about 47 versus 79 mm/s). Report per interval in the main text.
11. **Sec. 5.3 (p. 11) and Table 6 (p. 13).** Say which entries are signed. The "Matched, units" entries for arm angle and dome are differences of absolute values (Major comment 4a).
12. **Sec. 5.4 (p. 13).**
    - The text says that "the intervals in Table A1 do not overlap between M5, M4, M1 and M2"; in fact M4 (10–12) and M1 (12–20) touch at 12.
    - The bootstrap resamples nine alternatives per family and treats the floors and fitted hyperparameters as fixed. Say so.
13. **Sec. 5.5 (p. 14).** Next to "90.5 % go to trial", give the share of correct verdicts with the guard (5–8 %).
14. **Sec. 5.6 (p. 15) and Table 9 (p. 17).**
    - Give the leg lengths used for ISO 2768-1. The flat segment used for the convex arms is only about 7.5 mm (median `op20_seg`, after the 1 mm margins; concave about 18 mm).
    - For a shorter leg of at most 10 mm, the limits are ±1°, ±1°30′ and ±3°, not those used.
    - State whether the "design angle of its tool" (DDACS `wall_angle`) refers to the punch or the die, and how it compares with the scanned die-side surface.
15. **Sec. 5.7 (p. 16).**
    - The temperature correction uses the within-series slope, which is confounded with any monotone trend in time.
    - Differences between series are not corrected: start temperatures range from 21.2 to 30.2 °C, and series means differ by up to about 5 K.
    - A reduction of 1–14 % shows that temperature does not set the floor; please say what does.
16. **Sec. 5.7 (p. 17).** Replacing each part's oil film with the pattern median also changes every matched simulation through the steep mapping. The deterioration of M3 (from 20 to 40 floors) may therefore reflect the mapping rather than information in the film. Test this by changing only the model input (M4).
17. **Sec. 6.5 (p. 20).**
    - The paper says that absolute offsets "carry the scanner calibration uncertainty, which floors and effects do not". In fact floors carry gauge repeatability, and effects carry scale errors.
    - Add the missing threats to validity: no MSA, view-dependent wall artefacts, blank offset versus quarter symmetry, the material model, the unknown run order, and production interruptions.
18. **Sec. 4.4 (p. 10).** "All constants were fixed before the analysis": cite a dated record, e.g. a tagged commit. Several constants materially affect the results: B, α, the trimming, the 40 mm dome radius, the 10–20 mm wall band, and the 80 mm flatness circle.
19. **Eq. (1) (p. 6) and Table 2 (p. 7).**
    - For two-sided characteristics the interval is on the q95 of |c|. Say explicitly that the sign information is discarded.
    - The text discusses the rules in the order M0, M1, M2, M5, M3, M4, and an M6 appears later. Consider renumbering.
20. **A.1 (p. 22).** The scan's corner tip (the mean of outline points within 0.3 mm of the extreme diagonal projection) depends on the blank corner condition (radius, burr), whereas the simulation uses the exact corner node. Mention this.
21. **Figures.**
    - Fig. 2 (p. 12): the page number overlaps the caption. Per-geometry floor bars would be more informative than the pooled floor.
    - Fig. 3 (p. 15): the symmetric-log tick labels are hard to read. Give the number of cases per panel.
22. **References.** Add:
    - VDI/VDE 2634 Part 2 or ISO 10360-8 (acceptance testing of optical 3D measuring systems);
    - VDA 5 or ISO 22514-7 (capability of measurement processes);
    - ISO 22514-2 (process capability);
    - ISO 22081:2021, ISO 1101 and ISO 12781 (flatness);
    - work on pressure-dependent friction and on springback modelling of DP steels (e.g. Hol et al. 2012; Yoshida and Uemori 2002).

## Recommendation: major revision

Scoring design-stage decision rules against production by safe and decisive distances, with explicit abstention and a calibration budget, is a worthwhile contribution that fits the collection. The open, reproducible pipeline makes exactly this kind of scrutiny possible.

In its current form, however, the quantities that carry the conclusions are not validated:
- the unit contains unquantified gauge variance, which is dominant for two characteristics;
- systematic scan errors of 1–10° in wall angles and 2–4 mm in flange dimensions affect the absolute offsets and the scenario truths;
- the simulated characteristics carry extraction noise of several floors;
- the discrepancy analysis misses the forming-physics explanations and hides a sign error;
- the floor is not tied to statistical process control or capability, and rests on one series per alternative;
- a simple control shows that, within a family, the simulation adds nothing, which reverses the main "where machine learning helps" message;
- the calibration-design result mostly reflects near-twin alternatives;
- the ISO 2768 scenarios are unrealistic and dominated by easy decisions;
- the PA12 case contradicts the paper's own definitions.

None of this is fatal to the idea, and most of it can be addressed with the data at hand:
- redundancy-based gauge estimates, or repeat scans;
- per-side reporting;
- cleaner extraction from the simulations;
- the missing controls;
- realistic requirements, with results stratified by margin;
- a redesigned or removed PA12 case.

The revision will change numbers and probably some conclusions, so I recommend major rather than minor revision. If measurement validity cannot be established, through repeat scans or a traceable reference, I would regard the floor-based claims as unsupported.
