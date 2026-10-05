# Findings

Design-stage manufacturability decisions qualified with production evidence. Deep drawing and cutting of
DP600 cups: 18 design–process alternatives (2 geometries × 3 blank-holder forces × 3 lubrication patterns),
500 consecutive parts each (RDDAC), against the matching finite-element simulations (DDACS).

Every number below comes from the CSV named in brackets, written by `bash scripts/run_all.sh` (19.5 min on
4 cores from the cached feature tables). Distances and floors are in the units of each quality
characteristic unless stated; "floors" means multiples of that characteristic's production floor.

## Headline

1. **Production resolves geometry and, mostly, blank-holder force, but rarely the lubrication pattern.** All
   63 geometry contrasts, 106 of 126 blank-holder force contrasts and 53 of 126 lubrication contrasts exceed
   the production floor [alt_effects.csv].
2. **The nominal simulation is not decision-grade.** Its median offset from production reaches 108 floors
   (16 floors or more for six of seven characteristics on the concave cup) and varies by 10.5 to 38 floors
   between alternatives of one geometry; it needs requirements 150 floors from the truth before 95 % of its
   verdicts are right [dec_alternatives.csv, dec_resolution.csv].
3. **Calibrated on the other alternatives of the family, a Gaussian-process discrepancy model (M5) decides
   correctly beyond 7 floors (bootstrap 95 % CI 6.5–8) and errs in at most 5 % of verdicts beyond 2 floors
   (0.5–4.5).** The conformal envelope (M2) is safer (0.5 floors) but needs 25 floors to decide; learning the
   characteristic from production data alone (M4) needs 12; the intervals of M5, M4, M1 and M2 do not overlap
   [dec_resolution.csv].
4. **Across geometries no rule is safe closer than 20 floors, and machine learning without the simulation
   fails outright** (150 floors). The simulation is what carries a decision into a new geometry, but its
   calibration does not transfer reliably [dec_resolution.csv].
5. **Production evidence buys safety first, and which variants are produced matters.** With 4 to 5 produced
   alternatives of the family the calibrated rules err in under 1 % of verdicts at 10 floors; more alternatives
   make M5 more decisive (20 to 7 floors) but M2 less so (12 to 25) [budget_resolution.csv]. Calibration sets
   whose blank-holder forces bracket the new design make M2 error-free and M5 nearly so at 10 floors from two
   alternatives on; extrapolating sets err in 4.6–7.9 % [budget_design.csv].
6. **The press-force record cannot stand in for the scan.** It explains at most 17 % of the part-to-part and
   11 % of the batch-to-batch variation of any characteristic [inline_lod.csv, inline_drift.csv].
7. **Against general tolerances (ISO 2768) the best rule decides 89 % of 162 design questions correctly, with no
   false accept** (within the family); the nominal simulation is right in 66 % and accepts 19 % that fail
   [scen_scores.csv].
8. **An applicability guard makes the transfer safe by sending it to trial.** For 90.5 % of the cases on a new
   geometry the simulated q95 lies outside the calibration range; the rest are decided with at most 2.4 % wrong
   verdicts [dec_guard.csv].

## 0 Data and characteristics

- 9,000 parts read without failure, 500 per alternative; 10 parts carry no scan in the archive, so the
  characteristics rest on 8,990 parts [features_rddac.csv].
- 396 simulations matched to the experiments (6 sheet thicknesses × 11 friction coefficients per geometry
  and force) and 264 over the DDACS design corners [features_ddacs_rddac.csv, features_ddacs_corners.csv].
- Seven quality characteristics, defined once in `scripts/qc.py` and measured identically on scans and
  simulated nodes about the cup-bottom plane: draw-in at the mid-sides and at the corners, flange waviness,
  wall angle after drawing, arm angle after cutting, cup depth, bottom dome after cutting.
- Centres of batches, alternatives and cells are 10 % trimmed means: edge positions on the scans are
  quantised by the pixel grid, and medians of quantised values jump between grid levels (Section 1).

## 1 Production floor

The floor F is the 95 % quantile of the difference between the centres of two batches of 50 consecutive
parts of one alternative, pooled over alternatives [alt_floor.csv, sens_drift.csv].

| Characteristic | Floor (95 % CI) | Concave | Convex | Part SD | Floor / scatter floor |
|---|---|---|---|---|---|
| Draw-in, mid-side (mm) | 0.085 (0.076–0.095) | 0.079 | 0.094 | 0.131 | 1.40 |
| Draw-in, corner (mm) | 0.046 (0.035–0.052) | 0.053 | 0.030 | 0.027 | 4.49 |
| Flange waviness (mm) | 0.0028 (0.0024–0.0031) | 0.0037 | 0.0021 | 0.0020 | 2.53 |
| Wall angle (°) | 0.081 (0.071–0.092) | 0.089 | 0.075 | 0.130 | 1.47 |
| Arm angle, cut (°) | 0.109 (0.094–0.122) | 0.116 | 0.100 | 0.091 | 2.56 |
| Cup depth (mm) | 0.011 (0.010–0.012) | 0.009 | 0.012 | 0.007 | 3.93 |
| Bottom dome, cut (mm) | 0.0070 (0.0061–0.0081) | 0.0034 | 0.0082 | 0.0036 | 3.86 |

- **Drift, not scatter, sets the floor.** After the parts of each alternative are permuted (time order
  removed), the floor shrinks by a factor of 1.4 (mid-side draw-in, wall angle) to 4.5 (corner draw-in)
  [sens_drift.csv]. Batches of one design drift apart by more than independent parts would.
- **Robust to the analysis constants.** Over batch sizes 25 to 100 and quantiles 0.90 to 0.99 the floor moves
  by a factor of 0.64 to 2.2; the share of resolvable contrasts stays at 0.97–1.00 for geometry, 0.75–0.88
  for blank-holder force and 0.26–0.50 for lubrication [sens_floor.csv, sens_esr.csv].
- **Median against trimmed mean.** Batch medians inflate the floor of mid-side draw-in by 38 % and of the wall
  angle by 31 % (pixel-grid quantisation); the other five change by at most 5 % [sens_floor.csv].

## 2 Which design and process differences production resolves

Effect-to-scatter ratio ESR = |difference of two alternatives' centres| / F, for alternatives that differ in
one factor [alt_effects.csv].

| Factor | Contrasts with ESR ≥ 1 | Median ESR per characteristic | Bootstrap P(ESR ≥ 1) ≥ 0.95 |
|---|---|---|---|
| Geometry | 63 of 63 | 2.8 (waviness) to 130 (wall angle) | 63 of 63 |
| Blank-holder force | 106 of 126 | 0.9 (wall angle) to 10.2 (depth) | 102 of 126 |
| Lubrication pattern | 53 of 126 | 0.5 to 1.6 | 43 of 126 (61 at ≤ 0.05) |

- The wall angle is the one characteristic that does not respond to blank-holder force (39 % of contrasts).
- **Minimum resolvable change of blank-holder force** (F / sensitivity of the cell centres): cup depth 28 kN
  (95 % CI 25–32), waviness 33 kN, corner draw-in 55 kN, mid-side draw-in 90 kN, arm angle 101 kN, wall angle
  346 kN, dome 623 kN, the last two beyond the tested 100–500 kN [alt_mrc.csv].
- **Incoming conditions are too stable to matter.** Shifting a characteristic by one floor would take 19 to
  147 µm of sheet thickness against a within-series SD of 2.9 µm, and 14 to 162 K of punch temperature against
  a drift of 1.1 to 6.4 K per series [alt_mrc.csv, features_rddac.csv].

## 3 Simulation against production

Offset between the parts' 95th percentile and the nominal simulation (t = 0.98 mm, μ = 0.10), median over the
alternatives of a geometry, in floors (concave / convex) [dec_alternatives.csv]:

| Characteristic | Offset (floors) | Offset of the matched simulation (units) |
|---|---|---|
| Cup depth | −106 / −72 | −0.95 / −0.90 mm |
| Draw-in, corner | −59 / −108 | −3.0 / −3.3 mm |
| Arm angle, cut | −30 / +0.7 | −3.5 / +0.04° |
| Bottom dome, cut | −28 / +8 | −0.04 / +0.06 mm |
| Draw-in, mid-side | −17 / −16 | −1.4 / −1.8 mm |
| Wall angle | +16 / +6 | +1.3 / +0.6° |
| Waviness | +9 / +3 | +0.03 / −0.01 mm |

Within one geometry the offset itself varies by 10.5 to 38 floors between alternatives, so a constant bias
correction cannot get below that.

## 4 Design-stage decisions

Each alternative in turn is treated as a new design and judged from simulation, calibrated on other
alternatives: *within* the family (8 alternatives of the same geometry), *pooled* (17, both geometries) or
*transfer* (9 of the other geometry). Requirements are placed d floors from the true 95th percentile.
Decisive distance: beyond it ≥ 95 % of verdicts are correct. Safe distance: beyond it ≤ 5 % are wrong
[dec_resolution.csv; Figure F3].

| Rule | Within: decisive / safe | Pooled | Transfer |
|---|---|---|---|
| M0 nominal simulation | 150 / 150 | 150 / 150 | 150 / 150 |
| M1 bias-corrected | 15 / 15 | 30 / 30 | 40 / 40 |
| M2 envelope + conformal margin | 25 / 0.5 | 50 / 0 | 75 / 20 |
| M3 simulation + ML discrepancy | 20 / 0 | 25 / 0 | 50 / 20 |
| M4 ML only (no simulation) | 12 / 1 | 25 / 0.5 | 150 / 150 |
| M5 Gaussian-process calibration | **7 / 2** | **12 / 1** | 40 / 30 |

At a requirement 10 floors from the truth [dec_curve.csv]:

| Rule | Within: correct / wrong / uncertain | Transfer: correct / wrong / uncertain |
|---|---|---|
| M0 | 69 % / 31 % / 0 | 69 % / 31 % / 0 |
| M1 | 91 % / 9 % / 0 | 71 % / 29 % / 0 |
| M2 | 67 % / 0 / 33 % | 65 % / 9 % / 26 % |
| M3 | 65 % / 0 / 35 % | 66 % / 11 % / 23 % |
| M4 | 94 % / 0 / 6 % | 56 % / 31 % / 14 % |
| M5 | 97 % / 0 / 3 % | 77 % / 21 % / 3 % |

- **M5 per characteristic, within the family** (decisive / safe, floors): waviness 1.5 / 0.5, wall angle
  2.5 / 0.5, corner draw-in 2.5 / 0.5, mid-side draw-in 4.5 / 1.0, depth 5 / 3.5, arm angle 6.5 / 2.5,
  dome 15 / 9.5. In units: 0.004 mm, 0.20°, 0.12 mm, 0.38 mm, 0.054 mm, 0.71° and 0.11 mm
  [dec_resolution.csv, alt_floor.csv].
- **What the simulation adds** (M3 against M4): within a family nothing; ML on the produced alternatives alone
  is more decisive (12 against 20 floors). Across geometries everything: without the simulation the model
  cannot leave the geometry it was trained on (150 floors), with it the rule decides at 50.
- **Where the AI helps and where it does not.** The Gaussian-process discrepancy is the most decisive rule
  within the family and pooled, and ties with bias correction across geometries, but in transfer it is
  over-confident: it abstains in 3 % of verdicts while being wrong in 21 % at 10 floors. The conformal
  envelope knows better what it does not know (26 % uncertain, 9 % wrong).

## 5 Calibration budget

Within-family calibration on every subset of k produced alternatives [budget_resolution.csv; Figure F4]:

| k | M1 decisive | M2 decisive / safe | M5 decisive / safe | Error at 10 floors (M2, M5) |
|---|---|---|---|---|
| 1 | 20 | 12 / 12 | – | 8.1 %, – |
| 2 | 20 | 15 / 8 | 20 / 7.5 | 3.4 %, 3.0 % |
| 3 | 20 | 25 / 4 | 20 / 5 | 1.5 %, 1.8 % |
| 4 | 20 | 25 / 2.5 | 15 / 3.5 | 0.8 %, 0.9 % |
| 5 | 20 | 25 / 1.5 | 10 / 2.5 | 0.4 %, 0.4 % |
| 8 | 15 | 25 / 0.5 | 7 / 2 | 0 %, 0 % |

Bias correction (M1) never gets safe below 15 floors. With a conformal margin, more evidence only makes the
rule safer; with the Gaussian process it also makes it more decisive. Four to five produced alternatives of a
family are the point where both calibrated rules become reliable.

## 6 Design space

Simulated against measured sensitivity [ds_sensitivity.csv; Figure F2]:

- **Blank-holder force:** the simulation overstates the effect on draw-in 3 to 7 times and on the concave
  wall and arm angle 4 to 8 times, understates it on the dome 3 to 7 times, reproduces cup depth on the
  concave cup (1.1) and gets the sign of the convex wall angle and the convex waviness wrong.
- **Sheet thickness:** reproduced for cup depth (1.1) and dome (1.0) on the concave cup and for corner
  draw-in on both (0.85–1.03); wrong in sign for mid-side draw-in.
- **Friction:** 5 to 630 times the effect inferred from the measured oil film, 4 of 14 with the opposite
  sign. This points to the dataset's linear oil-to-friction mapping rather than to the solver.
- **Minimum resolvable change of blank-holder force with simulation as the only evidence** (floor plus the
  calibrated margin over the simulated sensitivity): 75 to 139 kN for draw-in against 36 to 124 kN in
  production; for depth 112 to 321 kN against 23 to 31 kN.
- **Design steps between the DDACS corners**, in floors: the steps move the wall angle by 10 to 264 and the
  corner draw-in by 19 to 152, while the convex steps move the dome by 0.6 to 0.7 floors, below what
  production can resolve.
- **Gaussian-process surrogate of the simulations** (leave-one-out over process conditions): error 0.04 to
  0.12 floors for draw-in, 0.6 to 1.9 for wall angle, arm angle and depth, 5.6 for the convex waviness and 11
  for the concave dome; a surrogate stands in for the simulation only for the smooth characteristics
  [ds_surrogate.csv].

## 7 In-line verifiability

- Part level: from the force record, sheet thickness and oil film, out-of-fold R² is at most 0.17 (cup depth)
  and at most 0.03 for five of seven characteristics; the limit of detection is 3.1 to 3.3 within-alternative
  SDs, i.e. no better than knowing nothing [inline_lod.csv].
- Batch level: the drift between batch centres is explained to at most 11 % (R² out of fold, folds by
  alternative); removing it lowers the floor by at most 16 % (depth) [inline_drift.csv].
- The scan stays the evidence; force monitoring does not tighten the floor.

## 8 Threats to validity

- **One material, one press, two geometries.** The procedure is general, the numbers are not.
- **The floor is short-term.** Each alternative was produced once, as 500 consecutive strokes; days, coils and
  tool states are not covered, so the floor is a lower bound of series-production variation.
- **Blank-holder force and stroke speed are confounded:** 46.8 mm/s at 100 kN against 78.6 mm/s at 300 and
  500 kN [features_rddac.csv]. Force effects include the speed effect.
- **Punch temperature drifts** by 1.1 to 6.4 K within a series (median 4.3 K) and cell medians differ by up to
  5.3 K [features_rddac.csv]; part of every between-alternative effect can be thermal, although the
  temperature sensitivities in Section 2 make it a fraction of a floor.
- **Lubrication is a pattern, not a friction coefficient.** Pattern medians of the oil film are 1.32 (coarse),
  1.11 (medium) and 0.97 g/m² (fine) with a within-series SD of 0.10 g/m²; the simulations are matched through
  a linear oil-to-friction mapping that Section 6 calls into question.
- **Scan measurement.** Edge positions are quantised by the pixel grid (handled by trimmed means, Section 1);
  absolute offsets between scans and simulations carry the scanner calibration uncertainty, floors and
  effects do not.
- **Conformal margins on few alternatives.** With 8 to 17 calibration alternatives the 90 % margin equals the
  largest calibration residual; the guarantee is marginal and assumes exchangeable alternatives, which the
  transfer violates by design.
- **Synthetic requirements.** Requirements are placed at known distances from the truth to score the rules;
  no specification of the real part is used.
- **Design corners co-vary.** DDACS moves curvature radius, bottom radius and wall angle together between two
  corners per base shape, so single geometric effects are not identifiable.

## 9 What this means for the paper

- The object of study is the design-stage decision, not the predictor: which rule, with how much production
  evidence, gives a verdict that production confirms.
- Contributions that survive the data: the production floor as the unit of design decisions; safe and
  decisive distances as decision-level detection limits; the calibration budget; and a clear map of where
  machine learning helps (within a family, where the Gaussian-process calibration halves the decisive
  distance of the best physics-only rule) and where it does not (across geometries, where only the
  simulation carries the decision and no calibration is safe below 20 floors).
- Open items before writing: a realistic requirement scenario taken from the part's function, a procedure
  figure and positioning table, and the simulated three-referee review of the playbook.

## 10 Additions after the publishability review

### 10.1 Calibration design [budget_design.csv]

| Rule | Calibration set | Safe distance k = 2 / 3 / 4 / 5 | Wrong at 10 floors k = 2 / 3 / 4 / 5 |
|---|---|---|---|
| M2 | brackets the new design's force | 3 / 1.5 / 1.5 / 1 | 0 / 0 / 0 / 0 % |
| M2 | extrapolates | 12 / 12 / 12 / 12 | 7.9 / 5.8 / 5.6 / 5.2 % |
| M5 | brackets | 2.5 / 3 / 2.5 / 2 | 0.1 / 0.6 / 0.2 / 0.1 % |
| M5 | extrapolates | 12 / 12 / 10 / 10 | 6.7 / 5.4 / 4.6 / 4.7 % |

### 10.2 Applicability guards [dec_guard.csv]

Across geometries the novelty guard (simulated q95 of the new design outside the range of the calibration
alternatives) fires in 90.5 % of the cases and the family guard in all; the remaining cases are decided with 0 %
(M2) and 2.4 % (M5) wrong verdicts at 10 floors. Within a family neither guard fires.

### 10.3 Requirements from general tolerances [scen_truth.csv, scen_scores.csv]

ISO 2768-1 angular classes (f/m 0.5°, c 1°, v 2°, legs 10–50 mm) on the wall angle (about the tool's design
angle) and the arm angle (about flat), ISO 2768-2 flatness classes (H 0.1, K 0.2, L 0.4 mm, 30–100 mm) on the
bottom dome; values checked against the standards' text (paper/notes/tolerance_sources.md). 162 decisions per
rule and scope. Within the family: M5 89 % right, 0 % false accepts, 1.2 % false rejects, 10 % trial; M1 87 %
right with 6.8 % false accepts; M2 72 % right, no wrong verdicts, 28 % trial; M0 66 % right, 19 % false accepts.
Transfer: M5 65 % right with 9.9 % false accepts; M2 44 % right, 4.3 % false accepts, 39 % trial.

### 10.4 Robustness [rob_floor.csv, rob_bhf_pairs.csv, rob_decisions.csv]

- Punch-temperature correction lowers floors by 1–14 %; M5 within 7/2.5 floors (reference 7/2), pooled 10/1.
- Conformal level 0.80 / 0.95: M2 within unchanged (25/0.5); M5 decisive 6 / 7.5.
- Resolution target 0.90 / 0.99: M5 5 / 12, M4 8 / 15, M1 10 / 30 floors (ranking unchanged).
- Force effects at equal stroke speed (300→500 kN): corner draw-in and depth resolved in 6/6 contrasts, mid-side
  draw-in, arm angle and dome in 5/6, waviness 3/6, wall angle 2/6.
- Oil film replaced by the pattern median for M3: decisive 40 floors (reference 20), safe 3.
- Conformalised GP (M6): safe 0.5 floors, decisive 75 everywhere (negative result).

### 10.5 Related work found

The dataset authors' descriptor paper (Baum et al. 2026, Trans Indian Inst Met, doi:10.1007/s12666-026-03870-5)
decomposes the simulation-to-reality deviation (geometry 77–92 % of its variance) and predicts it with gradient
boosting from process measurements (R² 81–92 %). This paper's question is complementary (design-stage decisions
without process measurements of the new alternative); their R² is mostly between-alternative variation, which
the within-alternative in-line analysis removes.
