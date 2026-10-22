# Referee report: Reviewer 2

**Manuscript:** Evaluating AI-based manufacturability decisions against the resolution of production
**Journal:** Journal of Intelligent Manufacturing
**Round:** First submission
**Reviewer focus:** Sheet-metal forming practice (deep drawing, die tryout, finite-element process simulation) and quality engineering (statistical process control, process capability, measurement systems analysis)
**Date:** 22 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary of the submission

The manuscript proposes a framework for judging whether a design-stage prediction (from simulation, machine learning or production records) is fit to decide whether a new design–process alternative will meet a requirement. Its unit, the "production floor", is the 95 % quantile of the difference between the trimmed-mean centres of two 50-part batches of one alternative within a run. A rule that returns meets, fails or trial is characterised by a decisive distance and a safe distance in floors, separately for three relations of the new design to what has been produced (sibling, new process setting, new family), and a procedure turns these into guard bands for single verdicts. The demonstration uses the open RDDAC data (two cup geometries × three blank-holder forces × three lubrication patterns, 500 scanned DP600 parts each) and the matched DDACS LS-DYNA simulations, and scores fourteen rules on seven characteristics. Within a family, the nearest produced setting or a linear force trend decides as well as or better than every simulation-based or learned rule (3.4 floors with a sibling, 4.7–8.9 for a new setting), while the simulation helps only in the transfer between the two geometries, where no rule is safe closer than 16–17 floors.

## 2. Assessment

- **Originality: strong.** Scoring design-stage decision rules in a production-defined unit, by evidence relation and against a production-record baseline with and without the simulation, is new for manufacturability support, although its building blocks (precision limits, operating characteristics, conformity-assessment guard bands) are established.
- **Significance for intelligent manufacturing: adequate.** It addresses a real gap and delivers a sobering, useful baseline result, but its practical weight is limited until the unit is shown to be a production quantity and the method has been applied to multi-run industrial data and to decisions that tryout engineers actually make.
- **Technical soundness: adequate.** The statistics are careful, transparent and reproducible, but the physical meaning of the unit (production or measurement drift, single-run truths) and the set-up of the simulation it is used to judge are not established.
- **AI/ML methodology, baselines and evaluation protocol: adequate.** Grouped evaluation by relation, paired bootstraps and the strong no-learning baseline are exemplary, but the learners are minimal (Gaussian processes and gradient boosting on six to nine alternatives), the effective sample is 18 runs and two transfers, and several rules were added after results had been seen, as the authors report.
- **Evidence supports the claims: adequate.** The dataset-specific results are supported and mostly hedged, but one headline number rests on strata defined from the outcome, the conclusions about simulation rest on a simulation dataset that does not contain the produced process, and the claim of an evaluation standard rests on one laboratory process.
- **Clarity, organisation and length: weak.** The text is very dense: fourteen similarly named rules, numbers in nearly every sentence, a unit whose name clashes with the everyday meaning of "production floor", and no figure of the parts, the cut operation or the measurement.
- **Positioning and references: adequate.** Coverage of design theory, V&V, conformal prediction and SPC/MSA is broad, but the paper barely engages with how forming simulation is validated and calibrated in practice or with how machine learning is used in sheet forming.
- **Fit to JIM's scope: adequate.** An evaluation methodology for AI-supported manufacturing decisions belongs in JIM, but the AI content is modest, and the value to practitioners has to be made explicit for JIM's readership.

## 3. Major comments

The comments below are offered against real strengths. The paper asks the right question, uses 9,000 real parts rather than synthetic data, and compares every learned or simulated rule with a production-record baseline and with its own version without the simulation. It states its assumptions (A1–A3) and limitations, and it records which analyses were added after results had been seen. I checked the deposit: every file in `SHA256SUMS` verifies, and the values of Tables 3 and 4 and the numbers of Sections 5.1, 5.2 and 5.8 that I spot-checked agree with `results/*.csv`. Where I quote my own numbers below, they come from small read-only computations on the authors' feature tables using their own functions. They are offered as checks the authors can reproduce and extend, not as final values.

### 1. What the production floor contains: production drift, measurement drift, or both

*Problem.* The floor is named and interpreted as a property of production (Sections 3.2, 5.1, 5.2), and it is set by drift within the run (drift factor 2.1–4.5, Table 3). Nothing in the manuscript, however, attributes that drift to the process:

- the documentation does not say whether parts were scanned in production order (ll. 464–465);
- the stability of the scanner cannot be checked (ll. 550–551);
- none of the recorded process signals explains the drift (out-of-fold R² from −0.23 to 0.20, ll. 551–567);
- the scanner has strong direction-dependent artefacts (comment 3).

To a tryout engineer, a draw-in that wanders by 0.05 mm over a 500-part run with no corresponding change in punch force, sheet thickness or oil film is as likely to come from the measuring chain, or from unmeasured blank dimensions, as from the process.

*Why it matters.* The floor is the unit of every result. If an appreciable share of it is measurement drift, then:

- Section 5.2 ("what production resolves") describes what this scanner resolves;
- A3 is not established;
- the split into near-replicate and resolvable siblings (Section 5.4) moves with it.

The name also invites confusion, because in manufacturing "production floor" means the shop floor.

*What would resolve it.*

- (a) Ask the dataset providers for the production and scanning log: dates and order of the series, coil or blank batch, whether scanning was in-line and in production order, and the delay and part temperature at scanning. The series start temperatures of 20.5–29.6 °C (`panel_runs.csv`) already suggest that several series followed others directly.
- (b) Use features set by the tooling as in-run references. Dimensions largely fixed by punch and die should not drift with friction or blank-holder conditions. A quick check with the authors' feature table: the batch-centre deviations of the flange width Wx and of the cup width at 15 mm depth (the sum of the east and west wall positions) are uncorrelated (r ≈ 0.03). That argues against a common lateral scale drift of the scanner. Evidence of this kind belongs in Section 5.1, with a plain statement of what remains untestable: edge detection at the flange boundary, and drift in z.
- (c) Discuss the physical candidates a forming engineer would list for within-run drift:
  - tool warm-up and its effect on lubricant viscosity;
  - build-up and redistribution of lubricant on die and blank holder over consecutive strokes;
  - variation of material properties along the blank stack;
  - variation in blank size. This one enters the draw-in one to one, because the draw-in is computed against a nominal 210 mm blank edge taken from the DDACS mesh (`common.py`, `BLANK_MM`) rather than against measured blanks.
- (d) Rename the unit (for example "within-run resolution" or "production noise floor"), or at least define it against the shop-floor meaning. Call it a production-and-measurement floor wherever the evidence does not separate the two, as ll. 274–276 already concede.

### 2. One run per alternative: heterogeneity of the unit, variation between runs, and the link to capability

*Problem.*

- (i) **The pooled floor hides heterogeneity between runs.** The 95 % batch-pair difference within each run ranges from about 0.2 to 2.2 times the pooled floor of its geometry (0.36–1.62 for the mid-side draw-in; my computation with `alternatives.batch_centres`). Assumption A2 is therefore not supported uniformly. The 95 % interval in Table 3 comes from resampling batches, which ignores the serial dependence the authors document. Their own alternative-cluster interval in `alt_floor.csv` is wider, for example 0.0021–0.0050 mm against 0.0024–0.0031 mm for the waviness.
- (ii) **Every truth is the q95 of a single run.** Variation between runs, coils and tool states is unmeasured and bounded only at 1.2–9.8 floors (ll. 567–570, 1031–1034). In series stamping, coil-to-coil variation of material properties is commonly a major source of variation in springback-related characteristics. Safe distances of 0 to 0.75 floors therefore say nothing about future production (Table 4, with a sibling: M2 0.15, M5 0.75, M2n 0, M3 0). The authors say as much for distances below about one floor (ll. 572–573), yet Table 4 and Fig. 2 report these values without qualification.
- (iii) **The link to capability is left to the reader.** One floor is 0.7–1.7 long-term standard deviations (l. 543). By the authors' own mapping in Section 5.8, a limit 3.4 floors above the 95th percentile corresponds to a performance index of about 2. In a quality engineer's terms, the best design-stage rule with a produced sibling confirms conformance only where the alternative would have a capability of about Ppk ≈ 2 at the requirement. This is arguably the paper's most practice-relevant message, and it is hidden in floors.

*Why it matters.* Quality engineers will read every distance as a statement about series production. Without the heterogeneity between runs and the variation between runs, the distances, guard bands and trial rates are optimistic in a way the reader cannot judge.

*What would resolve it.*

- Report the floor of each run, or a random-effects summary of within-run drift across runs, and put the cluster interval in Table 3.
- Add a sensitivity analysis that perturbs each truth by a between-run component. Its size should span the near-replicate reproducibility of q95 (about 1–1.5 floors; see comment 6) and the between-series bound. Show how distances, guard bands and the ranking of rules change.
- Report distances below about one floor as "< 1".
- Give the key distances also in σ_LT, or as the equivalent Ppk of the requirement.
- Consider a variant whose decided statistic is a capability index under a normal or ISO 22514-2 time-dependent model. Parametric tails are routine in capability studies, whereas ll. 243–246 read as if they were not an option.

### 3. The quality characteristics and their measurement uncertainty

*Problem.* Section 4.3 (ll. 483–495) gives the characteristics thirteen lines. The information needed to judge them is in the code, not in the paper.

- **Instrument.** The scanner is a single-sided range imager with pixels of 0.077 × 0.158 mm and height steps of 7.75 µm (`common.py`). The paper names neither the scanner nor its specification, the fixturing, the scan orientation, or when the parts were scanned.
- **Systematic errors.** The four-side redundancy (`qc.py` docstring, `meas_scan.csv`) reveals systematic, direction-dependent errors that the paper omits:
  - the flange width in y reads 2.3–3.5 mm larger than in x and scatters 4–18 times as much, uncorrelated with x;
  - the two flange diagonals differ by 1.6–2.2 mm in every series;
  - the north wall reads 0.9–1.6° low on the convex cups;
  - the shadowed south wall reads 7–10° off;
  - on the cut parts, walls facing the camera read 5–7° steeper, which is why the wall angle after cutting was dropped.

  The authors sensibly avoid the worst directions. These findings nevertheless show an instrument with direction-dependent systematic errors of tens of floors. The residual bias in the directions that were kept is unknown. It does not enter the floor, which is a within-alternative quantity, but it does enter every absolute comparison with the simulation: M0, the offsets, the force-effect ratio, the sign of the arm angle and the "definitional" depth offset.
- **Quantisation of the headline characteristic.** The mid-side draw-in (abstract; worked example) is quantised in steps of 0.019 mm (0.38 floors). A 500-part series takes a median of only 10 distinct values (range 6–21), and for five alternatives the bootstrap standard error of the true q95 is zero (`panel_resolution_steps.csv`). The truth for this characteristic sits on the grid.
- **Operation measured.** The wall angle and the cup depth are measured after drawing (OP10), whereas a drawing specifies the finished, cut part. The paper does not say so; l. 486 calls them characteristics "a drawing would carry".
- **Scope of the A3 checks.** The checks offered for A3 (a white-floor share of 15–33 %, and the resolution) address repeatability only. They do not address bias, linearity or stability, which are the parts of a measurement systems analysis that matter here.

*Why it matters.* Two questions in my brief are whether the characteristics are measured well enough to carry a unit of 0.05 mm or 0.08°, and whether the simulation is judged against a sound measurement. As written, a reader cannot assess either.

*What would resolve it.*

- Add a measurement subsection: the instrument and its principle, and the scan geometry (image axes against the direction of motion; "along/across the scan lines" at ll. 489–491 is ambiguous).
- Add a table of characteristic definitions giving the operation, region, directions used, resolution, and known biases with magnitudes. Report the redundancy analysis in full.
- Ask the dataset providers for any verification data: a reference artefact, repeated scans of one part, or a comparison with a coordinate measuring machine. If none exists, state that absolute values are uncalibrated and limit absolute comparisons accordingly.
- Use sub-pixel edge estimation for the flange width, for example the mean of the edge positions over the band rows instead of the median of integer pixel widths.
- State, and justify, the use of OP10 values for the wall angle and the depth.

### 4. The simulation set-up, and whether the simulation is represented fairly

*Problem.* The simulations are a generic dataset that was neither set up for nor validated against the produced process. Several findings follow from that rather than from what simulation can contribute.

- **(a) The simulation grid does not contain the produced process.** At the nominal thickness, the simulated mid-side draw-in exceeds the measured centre at 100 and 300 kN for every friction coefficient up to the grid maximum of 0.15. It reaches the measured value only at 500 kN (μ ≈ 0.105 for the concave cup, 0.116 for the convex). The simulated corner draw-in exceeds the measured value at every force: by 2.6–3.5 mm at μ = 0.10, and still at μ = 0.15. (These are my checks of `features_ddacs_rddac.csv` against `features_rddac.csv`.) The calibration of Mc is therefore censored at the edge of the grid. "Calibrating the friction coefficient did not repair it" (ll. 941–943) thus tests the grid, not friction calibration.
- **(b) The oil-film-to-friction mapping is contradicted by the data.** M3 and every matched simulation rest on this mapping (ll. 476–479). Combined with the simulated sensitivity to friction, it implies a change in mid-side draw-in of 0.8–3.2 mm per g/m² of oil. The observed within-run slope is 0.038 mm per g/m², and the slopes between lubrication patterns are roughly 0.05–0.4 mm per g/m², one of them negative. The mapping is thus too large by an order of magnitude or more. This fits what is commonly observed in forming tribology: above a modest film weight, contact pressure, sliding speed and temperature matter more than the amount of oil. The mapping should be tested and reported, not only flagged as an assumption.
- **(c) The envelope does not reflect measured incoming variation.** The envelope rules (M2, M5, M0w) take the envelope over the whole DDACS grid, 0.95–1.00 mm and μ 0.05–0.15 (`decisions.py`). The measured variation is much narrower: series median thicknesses are 0.986–0.993 mm (l. 463). A friction range of 0.05–0.15 is a reasonable prior for an unknown process, but far wider than the variation within one process. "Plausible incoming conditions" (ll. 298–301) is not what a process engineer's robustness simulation would use, and M0w's 119/94 floors probably reflect this in part.
- **(d) The numerical noise of the simulated characteristics is measured but not reported** (`meas_sim.csv`).
  - The x–y difference of the simulated wall angle has an SD of 1.8–2.3 floors, with a maximum of 10–12.
  - For the dome, the roughness along the friction grid has an SD of 2.4–9.8 floors, with a maximum of up to 35, and the top of the envelope exceeds a smooth response surface by 10–18 floors.

  Floors of 2–12 µm (dome, depth, waviness) are below what a shell model with a 1 mm mesh resolves in springback. On these characteristics the simulation is therefore partly scored on its numerical noise. The response-surface variant in Table A2 addresses part of this. The noise itself should be reported, and the simulation comparison given per characteristic or restricted to characteristics the model can resolve.
- **(e) The cup-depth offset is not explained.** Ll. 585–588 attribute it to the scanned surface against the shell mid-surface. That cannot be the cause in a single-sided scan: the bottom and the flange are seen on the same side of the sheet, so a t/2 offset cancels in their vertical distance. The offset is close to one sheet thickness (measured 28.3–28.8 mm, simulated 29.2–29.8 mm). That points instead to one of:
  - a difference in effective drawing depth (stroke or bottom dead centre, deflection of press or tool);
  - a different flange inclination;
  - a modelling convention in DDACS.

  Each of these is a set-up mismatch, not a definitional difference. Removing the offset moves M0 from 108 to 65 floors, so the mechanism has to be established.
- **(f) Several discrepancies are diagnostic, and the paper should say so.**
  - The sign error in the arm angle is confined to the concave cups. The convex arm angles agree with the simulation within about 0.6° (`panel_arm_sign.csv` and the feature tables). That points to springback modelling rather than a sign convention.
  - The simulation also under-predicts the opening of the wall angle by about 0.6–1.4°, although without reference data this cannot be separated from the wall biases of comment 3.
  - Both are consistent with known limitations of isotropic hardening and a constant elastic modulus for dual-phase steels: the Bauschinger effect, and the decrease of the unloading modulus with plastic strain (see, for example, Wagoner, Lim and Lee, 2013, *International Journal of Plasticity* 45:3–20).
  - Likewise, a constant Coulomb law cannot reproduce a weak sensitivity to blank-holder force if friction falls with contact pressure (Hol et al., 2012, already cited in Section 2.3).
  - If, as is usual, the tools are modelled as rigid, the elastic deflection of die, blank holder and press at 100–500 kN is ignored. That deflection redistributes the blank-holder pressure and is a recognised cause of draw-in discrepancies that tryout compensates by die spotting.

*Why it matters.* Forming practitioners will read RQ3 as a statement about process simulation, and so too the abstract's finding that "the simulation as used, offset or rescaled, helped only across families". In tryout, no one would use a simulation for decisions within a family without first calibrating it to the first tryout parts.

*What would resolve it.*

- Add a validation table: measured against simulated values per characteristic, geometry and force, at nominal and at best-fitting friction, in physical units.
- State in the abstract, Section 5.5, Table 5 and the conclusions that:
  - the simulation is an uncalibrated generic dataset that does not contain the produced process at two of the three forces;
  - RQ3 therefore measures that dataset;
  - a process-calibrated simulation might contribute more within a family.
- If new simulations are feasible, add a calibration of the kind tryout would make: μ per pressure level, or a pressure-dependent law.
- Take the envelope over measured incoming variation, and resolve the depth offset.

### 5. Do the decisions modelled reflect tryout and process development, and would the findings help a tryout engineer?

*Problem.*

- **(a) The decisions modelled are not the decisions of tryout.** In tryout the simulation is used as a target and a guide: die and blank-holder settings are adjusted until the simulated draw-in line is reproduced. The tool changes between loops (spotting, draw beads), and nothing is released without a few strokes. The decisions modelled here are release, change or trial of a new setting at a fixed tool state, judged on a one-sided limit on q95. They fit process planning and change management better than tryout. Draw-in in particular is specified as a window, not as a one-sided limit. The worked example (ll. 813–826) asks whether a new blank-holder force on an existing tool can be released without a trial, which the paper itself calls "a short press run" (ll. 928–929).
- **(b) The trial verdict is never scored.** An engineer chooses between a prediction and a trial of n parts, and both belong on the same operating characteristic. A quick check with the authors' data: within a run, the first 20 parts reproduce the full-run q95 to within 1.3 floors in 90 % of the 126 cases, and the first 50 parts to within about 0.9 floors. A short trial is thus more decisive than every design-stage rule except the nearest setting for near-replicates, and variation between runs would add to its error. Scoring the trial would turn the argument of Section 6.2 into a result.
- **(c) The procedure assumes long runs.** It needs 500-part runs for floors and truths (steps 2 and 5), whereas tryout produces short runs on a changing tool. Section 5.6 shows that rules can be calibrated on 50 parts, but the truths and floors still came from full series (ll. 765–767).
- **(d) The costs are too narrow.** The text reports a single cost ratio (ll. 843–849), although `scen_cost_map.csv` covers c_fr from 0.25 to 2 and c_trial from 0.02 to 0.5. In practice the cost of a trial differs by orders of magnitude between relations: minutes of press time for a new force, a new die for a new family. A false accept found at tryout or at start of production costs far more than a trial.

*Why it matters.* Whether the findings would help a tryout or process engineer is part of my brief. Several results would, but the paper does not put its weight on them:

- the minimum resolvable change of blank-holder force of 21–67 kN between 100 and 300 kN (none for the wall angle) tells an engineer which force steps can be confirmed within a run;
- the transfer of the produced family's springback offset of the wall angle to the new family (1.9 floors, ll. 710–712) mirrors the empirical springback allowances that experienced tryout engineers use.

*What would resolve it.*

- Frame the decision set explicitly:
  - process planning;
  - approval of a process change, for example a change of lubricant or force in series production, which change management under production part approval already has to decide;
  - qualification of AI tools.
- Score the trial as a rule, including the start-up of the run and the variation between runs.
- Test qualification with truths taken from the first 20–50 parts.
- Use trial costs specific to each relation over a wider range, and make the distance on the false-accept side the primary measure of safety.
- Replace the worked example with a decision closer to practice, for example a draw-in window, or a drawing tolerance on wall angle or depth.
- Bring forward the findings that serve tryout.

### 6. The sibling strata are defined by the held-out outcome

*Problem.* Section 5.4 (ll. 643–679) splits the sibling relation by whether the held-out alternative differs resolvably from its siblings. The stratum is computed from the held-out alternative's own production (`panel.py`, `sibling_strata`), which a team does not have at the design stage. The near-replicate stratum is, moreover, selected for small differences between the held-out alternative and its siblings, which mechanically favours the nearest setting. The resulting 0.85 and 4.9 floors appear as guidance in the abstract (p. 1, ll. 31–32), Table 5 and the conclusions.

*Why it matters.* Guidance has to rest on information available when the decision is made.

*What would resolve it.*

- Stratify by information available beforehand, for example whether the two produced siblings differ resolvably from each other. My computation from `dec_intervals.csv` and `alt_effects.csv` gives 90 % absolute errors for the nearest setting of about 1.5 floors when they do not (75 cases) and 4.4 floors when they do (51 cases). For a point rule this is close to the decisive distance (ll. 376–377). The qualitative message survives; the figure of 0.85 does not.
- Report decision-time strata in the abstract, Table 5 and the conclusions. Keep the outcome strata as a diagnostic of the pooled 3.4.

### 7. Scope, generalisability and the claims made

*Problem.* The evidence is narrow:

- one material grade and thickness, one press and one tool set;
- laboratory runs, each alternative produced once;
- within a family, a 3 × 3 factorial in which lubrication is mostly not resolved;
- across families, two transfers between geometries that differ in three features at once.

The "new family" is a mild novelty (same blank, material, press and nominal depth) compared with an industrial new part. The characteristics are dimensional. The questions that dominate deep-drawing feasibility (splits, wrinkles, excessive thinning) are outside the framework (ll. 997–998), and three of the seven characteristics (the two draw-ins and the flange waviness) are process indicators. Yet the title, the abstract's last sentence (p. 1, ll. 38–39) and the conclusions (ll. 1064–1067) speak of AI-based manufacturability decisions and an evaluation standard.

*Why it matters.* Practitioners will want to know whether the findings carry over to:

- other grades (higher-strength steels, aluminium);
- deeper draws near the forming limit;
- industrial presses with controllable die cushions;
- series produced across coils.

The evidence says nothing about any of these.

*What would resolve it.*

- Narrow the title and abstract to design-stage conformance decisions on dimensional characteristics.
- State in the abstract that the demonstration covers one laboratory deep-drawing process with an uncalibrated simulation dataset.
- Spell out what a confirmatory dataset needs:
  - several runs per setting across days and coils;
  - documented production and scan order;
  - a reference artefact scanned through the series;
  - more than two geometries;
  - ideally, an industrial process.
- Say briefly how attribute outcomes such as splits would be scored, for example through operating characteristics for a rate.

### 8. Presentation and positioning for JIM's readership

*Problem.* The manuscript is hard to use.

- There are fourteen rules with similar names (M1, M1s, M1n, M1sn, M2n, …), two floors, and guard bands under several priors.
- Numbers appear in almost every sentence, and the abstract is mostly numbers.
- Neither the process nor the scan is ever shown: the cup geometries, the tool dimensions, the press and die cushion, how the lubrication patterns were applied, and the OP20 cut and its "arms".
- Fig. 2 has twelve small panels on a symmetric logarithmic axis.

The positioning against forming practice is also thin. The paper barely engages with:

- simulation validation and calibration (friction models, springback modelling, tool deflection);
- robustness analysis of forming processes;
- in-line measurement of draw-in and closed-loop control of the blank holder;
- machine learning for sheet forming.

JIM readers will place the work against exactly these lines.

*What would resolve it.*

- Add a figure of the two cups and the cut part, showing where the characteristics are measured and the scan.
- Add a figure of batch centres over one run that illustrates the floor.
- Keep six or seven rules in the main text (M0, M1 or M1s, M2, M5, NN, M1sn, possibly M3) and move the rest to the appendix.
- Rewrite the abstract around the question, the framework and three findings.
- Add a table of key distances in physical units per characteristic.
- Harmonise rule names between code and paper (M3n/M4, Table 2 footnote).
- Extend Section 2 to cover the lines of forming work listed above.

## 4. Minor comments

1. **Abstract, p. 1, ll. 28–29.** "95 % conformance" is ambiguous for quality engineers, for whom conformance usually means parts within tolerance. "A requirement on the 95th percentile" is clearer.
2. **Section 2.5, ll. 179–181; Section 3.1, ll. 243–244.** Under production part approval, the acceptance criterion for initial process studies is a performance index above 1.67, with 1.33–1.67 subject to customer review; 1.33 is the usual criterion for ongoing capability. Please reflect this. Section 5.8 already reports 1.67.
3. **Section 3.2, ll. 263–265.** The reference protocol includes the warm-up of the first ~150 parts (ll. 462–463). Justify including a start-up transient in a unit meant for series decisions, and report the floor without warm-up in Table 3; Table A2 gives only its effect on the distances.
4. **Section 3.3, ll. 298–301.**
   - Give the ranges actually used for the envelope (comment 4c).
   - DDACS appears to vary a flow-curve scaling factor in its wider design space; the corner selection in `features_ddacs.py` fixes it at 1.0. If simulations at other factors exist near the RDDAC conditions, including them would bring the envelope closer to a practitioner's robustness simulation, in which material scatter is usually the leading input.
5. **Section 3.4, ll. 376–377.** For point rules the decisive distance is essentially the 90 % quantile of the absolute error in floors. Saying so early, in plain words, would help readers.
6. **Section 4.1, ll. 452–460.** Please give:
   - the material data available: grade designation, coil or coils, yield and tensile strength, r-values;
   - the tool dimensions: punch, die radius, drawing depth;
   - the press and die-cushion type;
   - how the lubrication patterns were applied;
   - what "coarse/medium/fine" denote, given the overlapping oil-film ranges.
7. **Section 4.1, ll. 463–464.** Make the stroke-speed confound concrete. Strain-rate effects in DP600 are small between 47 and 79 mm/s, whereas the behaviour of the lubricant film and tool heating depend on sliding speed and stroke rate.
8. **Section 4.2, ll. 468–480.** Report:
   - the element type and the number of integration points through the thickness;
   - whether contact accounts for shell thickness;
   - whether the tools are rigid or elastic;
   - how the blank-holder force is applied, and the stroke;
   - the springback procedure and the OP20 trimming.

   State which of these the DDACS documentation leaves open.
9. **Section 4.2, ll. 479–480.** Report M0 also at the best-fitting friction coefficient. μ = 0.10 is the middle of the grid, not a calibrated value.
10. **Section 4.4, ll. 509–511.** State the block length of the truth bootstrap: 50 parts, non-overlapping (`decisions.py`).
11. **Table 3.** Give the alternative-cluster interval (or both intervals), the range of per-run floors, and the floor without warm-up.
12. **Section 5.1, ll. 567–569.** "Differ by up to 1.2 … to 9.8 floors" describes 95 % quantiles of differences between series that include lubrication effects. They are not maxima.
13. **Section 5.2, ll. 584–585.** Add that the convex arm angles agree with the simulation (comment 4f).
14. **Table 4.** M1s for a new setting has δs = 19 but a distance of 164 floors on the false-accept side. Pooling both sides can hide a dangerous false-accept tail behind a moderate overall safe distance. False accepts are the costlier error in forming, so consider making the false-accept-side distance the primary measure of safety in the main tables.
15. **Fig. 2.** Enlarge the panels, show fewer rules, and make the δd and δs markers easier to tell apart.
16. **Section 5.7, ll. 800–808.**
    - The guard band of the nearest setting with a sibling ranges from 0.25 to 8.0 floors across the priors shown. Illustrate how a team would derive its prior from history, for example the margins between drawing limits and achieved 95th percentiles on past parts.
    - State the requirement grid of ±20 floors in physical units per characteristic: about ±1 mm of draw-in, ±1.6° of wall angle, ±0.2 mm of depth and ±0.07–0.16 mm of dome.
17. **Section 5.8, ll. 840–843.** State which characteristics and which tolerance class the ISO 2768-1 scenario uses.
18. **Section 6.5, ll. 990–998.** In deep drawing, splits and wrinkles are the first manufacturability question. Even a short paragraph on scoring a requirement on a rate would help.
19. **Table A5.** Map `meas_sim.csv` (the numerical noise of the simulated characteristics), and bring the full content of `meas_scan.csv`, including the biases, into the paper (comments 3 and 4).
20. **Reproducibility and references.**
    - The archive DOI is still pending (reference Canseven, 2026).
    - `pyarrow` and `remotezip` are unpinned in `requirements.txt`.
    - Please confirm the editions cited for ISO 5725-2 (2025) and ISO 22514-2 (2026); most readers will know the 2019 and 2017 editions.

## 5. Recommendation

**Major revision.** The manuscript asks a question that matters to anyone who deploys simulation or machine learning in process development: can a prediction be relied on to decide, and how close to the requirement? It answers with an evaluation design that is careful, transparent and reproducible. Its central empirical message is valuable and well supported on this dataset: within a family, a well-indexed production record is the baseline that any learned or simulated manufacturability check must beat. From a forming and quality-engineering standpoint, however, several problems remain:

- The unit on which everything rests has not been shown to be a production quantity rather than partly a measurement one.
- That unit is built from single runs, and neither the heterogeneity between runs nor the variation between runs is propagated.
- The measurement biases visible in the authors' own files are not reported.
- The simulation the unit is used to judge is an uncalibrated dataset that does not contain the produced process at two of three forces. The conclusions about what simulation contributes are therefore not yet fair to simulation as practitioners use it.
- One headline number rests on strata defined from the outcome.
- The decisions and costs modelled are only loosely tied to tryout practice.

Most of this can be addressed with the existing data, metadata from the dataset providers, and a clearer, more modest framing. I would be glad to see a revised version.

## 6. Confidential comments to the editor

This is a serious and unusually transparent piece of work. The deposited files verify against their checksums, and the numbers I spot-checked match the result files. My concerns are with the physical grounding (measurement and simulation) and the framing, not with integrity, and a major revision can address them. The manuscript is very dense for JIM's readership. A reviewer with machine-learning expertise should assess the conformal and Gaussian-process parts in more depth than I have. The authors disclose extensive assistance by a large language model (Section 4.5), including internal reviews simulated with it that shaped which rules and analyses were added. The disclosure appears adequate, but the editor may wish to confirm that it is consistent with the publisher's policy.
