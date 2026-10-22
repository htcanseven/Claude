# Editorial decision, first round

**Manuscript:** "Evaluating AI-based manufacturability decisions against the resolution of production", by Hüseyin Tayyer Canseven (LUT University)

**Journal:** Journal of Intelligent Manufacturing (Springer)

**Version considered:** first submission: the 30-page line-numbered PDF and its LaTeX source, the cover letter, and version 1 of the released code (`scripts/`), result files (`results/*.csv`) and archive metadata (`.zenodo.json`, `CITATION.cff`, `RELEASE_NOTES.md`)

**Reports considered:** Reviewer 1 (machine learning for manufacturing quality), Reviewer 2 (sheet-metal forming and quality engineering) and Reviewer 3 (intelligent manufacturing and decision support), all dated 22 October 2026; all three recommend major revision

**Date:** 22 October 2026

*Written by an AI agent in the persona of a fictional handling editor of a simulated review panel; it does not come from the journal or speak for any real person.*

---

## Part 1. Decision letter to the author

Dear Hüseyin Tayyer Canseven,

Thank you for submitting your manuscript to the Journal of Intelligent Manufacturing. Three reviewers have reported on it. Their fields are machine learning for manufacturing quality, sheet-metal forming and quality engineering, and industrial decision support. I have read the manuscript, the three reports and your cover letter. I have also checked the reviewers' central claims, read-only, against your released code and result files.

### 1. Decision

**Major revision.** I will reconsider the manuscript after a substantial revision that meets the twelve required changes in Section 3 of this letter. This is a heavy major revision. It asks for:

- a narrower framing;
- a rewritten abstract and results section;
- a fair test of the learned rules;
- several new analyses, all inexpensive, on the data you already have.

The revised version will go back to all three reviewers. Acceptance is not assured. If the claims about AI-based support are not brought into line with what the study shows, the next decision may be a rejection.

### 2. Synthesis of the reports and of my checks

**What the paper offers.** The question matters to this journal's readers: when can a design-stage prediction replace a physical trial? Your answer is an evaluation framework rather than another predictor. It has four parts: a unit set by production, two distances on the operating characteristic, qualification by evidence relation, and a guard band.

The paper's best-supported finding is that, within a design family, the nearest produced setting or a straight line in force was at least as decisive as every simulation-based or learned rule evaluated. Any evaluation of AI-based manufacturability support therefore needs a production-record baseline. All three reviewers accept this finding, and my checks support it.

The work is unusually candid (Sections 4.5 and 6.6). It is also reproducible:

- all 127 checksums in `SHA256SUMS` verify;
- Tables 3, 4, A2, A3 and A4 regenerate identically from the archived result files.

**Where the reviewers agree.**

- *Strengths.* All three value the question, the production-record baseline, the comparisons of each rule with and without the simulation, and the grouped evaluation by relation.
- *Density.* All three find the text too dense for this journal. The abstract is made of numbers and undefined terms, there are fourteen similarly named rules, and many results paragraphs carry fifteen to twenty-five numbers.
- *Claims.* All three find that the title, the "evaluation standard" and the contribution "including classifiers and language-model checks" promise more than the evidence can carry. That evidence is one laboratory process, two geometries, two family transfers and one run per alternative.
- *Selection.* All three note that rules, strata, the guard band and its prior were partly chosen after results had been seen, and that several headline numbers are minima over rules and strata.
- *Pooling.* All three find that pooling seven characteristics hides where rules succeed and fail.
- *Archive.* All three ask for a licence and a DOI for the code archive.

**Where they differ.** Each reviewer locates the main weakness in their own field, and each is right about it.

- Reviewer 1: the learned rules reduce to the baselines, and the uncertainty quantification reflects an imposed variance bound.
- Reviewer 2: the unit, the measurement and the simulation it judges are not physically grounded, and the decisions modelled are only loosely tied to tryout.
- Reviewer 3: the guard band, the part a factory would deploy, departs from the stated procedure and is not validated, and costs and trials are missing.

Their ratings also differ. Reviewer 2 rates originality as strong and the support for the claims as adequate. Reviewers 1 and 3 rate both lower. Their remedies differ in cost: Reviewer 1 asks for a broad set of new learners, Reviewer 2 for new simulations and data from the dataset providers, and Reviewer 3 for a user study and a monitoring scheme. I have not made all of these requirements; Section 5 says where and why.

**My checks.** Every reviewer claim on which this decision rests holds up; Section 6 gives the evidence. In particular:

- The near-replicate stratum is defined from the held-out alternative's own production. With strata a team could form at decision time, the nearest setting needs 1.60 and 4.40 floors, not 0.85 and 4.9.
- For a new setting, the Gaussian process without the simulation (M5n) predicts the mean of the calibration alternatives. With a sibling, its centre lies a fraction of a floor from the nearest setting.
- The 85–86 % coverage has a cluster-bootstrap interval of about 0.76–0.94.
- The guard bands differ between the two geometries. The convex extrapolation bands of M2 and M5, applied to the concave cup, give only 83–84 % correct decided verdicts.
- The code documents scanner biases of tens of floors that the paper omits.
- The simulation grid does not reach the measured draw-in at most settings, and every within-family friction calibration of Mc ends at the edge of the grid.

A few details in the reports are overstated (Section 5), but none changes the decision.

**Why major revision rather than rejection.** The checks confirm four substantive problems:

1. The answer to RQ3 on learning rests on fits that reduce to the baselines.
2. The answer on simulation rests on a grid that does not contain the produced process.
3. One headline number uses information that is unavailable when the decision is made.
4. The guard band is estimated in-sample, pooled over families and characteristics, and under a prior chosen for convenience.

None of these invalidates the framework. Each can be fixed with the existing data, inexpensive analyses at the level of the alternatives, and a narrower and clearer account. That is why I am not rejecting the paper. It is also why the revision is substantial.

### 3. Required changes

For each item I state the problem briefly, what will satisfy it, and whether it needs new analysis or rewording. Line numbers refer to the submitted PDF.

**R1. Reframe the title, abstract, contributions and conclusions around what was shown.** *Rewording.* (All reviewers.)

The following passages promise an evaluation standard for AI-based manufacturability decisions, including classifiers and language-model checks:

- the title;
- the closing sentence of the abstract (ll. 038–040);
- the contributions (ll. 093–098);
- the conclusions (ll. 1064–1067).

What was actually evaluated is narrower: fourteen rules for process-setting changes and two die-family transfers, on one laboratory process, with one run per alternative and an uncalibrated simulation dataset. The decisions are one-sided upper limits on the 95th percentile of dimensional characteristics.

Satisfied when:

- the title says what was done, for example a production-referenced evaluation of design-stage decision rules in a deep-drawing case study (better wording is yours to find);
- the abstract is rewritten so that it:
  - defines floor, evidence relation and the decisive and safe distances where they first appear;
  - carries at most five numbers;
  - states the exploratory status, the single laboratory process, the single run per alternative and the uncalibrated simulation dataset;
  - ends with a finding rather than the claim of a standard;
- "evaluation standard" is removed throughout; classifiers and language-model checks are presented as an untested proposal (Section 6.5 and Table 6); and the six-item list becomes a "proposed reporting checklist";
- Sections 3.1 and 6.6 state three limits of scope: the demonstration uses one-sided upper limits; its verdicts are per characteristic (marginal); and attribute outcomes such as splits and wrinkles are not covered;
- the block "Observed on this dataset" in Table 5 is worded so that it cannot be read as general guidance.

**R2. Define the sibling strata from information available when the decision is made.** *New analysis (small).* (Reviewer 2.)

Section 5.4 (ll. 643–679) classifies a held-out alternative by whether its own centre differs resolvably from its siblings. The code does this in `panel.sibling_strata`, using the held-out alternative's own lubrication contrasts in `alt_effects.csv`. That is the alternative's production outcome, which a design team does not have. It also selects near-replicates for small errors of the nearest setting. The resulting 0.85 floors appears in the abstract, Table 5, Section 6.1 and the conclusions.

Reviewer 2 proposed a decision-time stratum instead: whether the two produced siblings differ resolvably from each other. With that stratum I find, as Reviewer 2 did:

| Rule | Siblings not resolvable (75 cases) | Siblings resolvable (51 cases) |
|---|---|---|
| Nearest setting (NN) | 1.60 floors | 4.40 floors |
| Force trend (M1sn) | 3.05 floors | 4.20 floors |

Satisfied when:

- decision-time strata replace the outcome strata in the abstract, Table 5, Sections 5.4, 5.8 and 6.1, and the conclusions, with case counts and the alternatives behind them;
- the outcome strata remain only as a labelled diagnostic of the pooled 3.4 floors;
- the release-level statement ("inside every decisive distance except a near-replicate's", ll. 035–036 and 831–833) is recomputed. The capability-anchored limits lie a median of 1.7 floors from the truth, against the nearest setting's 1.60 floors, so the exception now survives by only 0.1 floor. The comparison is marginal and should be reported as such.

**R3. Give the learned rules a fair test, or confine what is said about learning.** *New analysis and rewording.* (Reviewers 1 and 3.)

The design is 3 × 3 with six to nine calibration alternatives. In it, the Gaussian processes fitted by maximum marginal likelihood without hyperpriors reduce to the baselines:

- For a new setting, the median force length scale sits at its lower bound, and the noise variance sits at its bound in every fit.
- The M5n centre lies within 0.01 floor of the calibration mean in 94 % of new-setting cases. At 300 kN it equals NN and M1sn exactly.
- With a sibling, the M5n centre lies a median of 0.28 floor from NN.
- The noise bound is the pooled variance between lubrication series. It therefore contains the lubrication effect that the GP also models, and it exceeds the variance of the targets in about a fifth of the M5n fits.
- The archive's own learner study (`tuning.py`) finds no boosting or ridge setting closer than 11.2 floors with a sibling (NN: 3.4) or 13.1 floors for a new setting (NN: 8.5). The paper does not report this study.

"Learning adds intervals rather than accuracy" (l. 718) and "learned 90 % intervals" (abstract; ll. 1059–1060) are therefore findings about this fitting procedure in this design. They are not findings about learning in general.

Satisfied when:

- (a) an appendix table gives, by relation, the fitted hyperparameters, the noise relative to its bound, and the distance of each GP centre from the calibration mean, NN and M1sn;
- (b) at least one learner specified for this data regime is added and scored like the other rules. Two possibilities:
  - a GP with an explicit linear (or monotone) mean in force, whose coefficient uncertainty is propagated into the predictive variance, with weakly informative priors on length scales and noise in place of hard bounds;
  - a Bayesian linear or hierarchical model in force and lubrication.

  In either case, its noise term must not absorb effects that the model also represents;
- (c) prediction is separated from uncertainty. Cross the predictors (NN, M1sn, the GP mean, boosting) with one interval construction calibrated for each relation, for example leave-one-force-out residuals, borrowed across the two families if necessary. Credit for intervals then goes to whichever component earns it;
- (d) the tuning study is summarised in two or three sentences and mapped in Table A5;
- (e) RQ3, Sections 5.5 and 6.3, the abstract and the conclusions are phrased in terms of the model classes, fitting procedures and data regime evaluated, and "learned intervals" no longer includes M2 and M2n, which involve no learning.

**R4. Present the simulation as what it is.** *Mostly rewording, plus two small tables.* (Reviewers 1 and 2.)

The DDACS grid was not set up for this process. At the nominal thickness:

- the simulated mid-side draw-in exceeds the measured centre at 100 kN for every friction coefficient, still by 1.5–1.7 mm at μ = 0.15;
- at 300 kN it reaches the measured centre only at the edge of the grid on the concave cup, and not at all on the convex cup;
- at 500 kN it reaches the measured centre at μ ≈ 0.105 (concave) and 0.116 (convex);
- the simulated corner draw-in exceeds the measured value at every force, by 2.6–3.5 mm at μ = 0.10.

As a result, every within-family friction calibration of Mc ends at the grid maximum of 0.15 (72 of 72). The sentence "calibrating the friction coefficient did not repair it" (ll. 941–943) therefore tests the grid, not friction calibration.

Three further points need correcting:

- *Labels.* M1s contains only the scale term of a multi-fidelity model (ll. 296–297). Mc is a least-squares grid search without a discrepancy model (your code says so), yet it is cited to Kennedy and O'Hagan (2001) (l. 308).
- *Cup-depth offset.* The explanation at ll. 585–588 (scanned surface against shell mid-surface) cannot be right. Depth is measured as a height difference between flange and bottom, both seen from the same side of the sheet, so a half-thickness offset cancels.
- *Oil-film mapping.* Lines 476–479 say Mc depends on the mapping from oil film to friction. In the code it does not; M3 and the matched simulations do.

Satisfied when:

- a validation table gives measured and simulated values per characteristic, geometry and force, at nominal friction and at the best-fitting grid value, in physical units. It should include the extraction noise already in `meas_sim.csv`: the x–y differences of the simulated wall angle have a standard deviation of 1.8–2.3 floors, and the roughness of the dome is 2.4–9.8 floors;
- the abstract, Section 5.5, Table 5 and the conclusions state three things: the simulation is an uncalibrated generic dataset that does not contain the produced process at all settings; the Mc calibration is censored at the edge of the grid; and the RQ3 findings on simulation concern this dataset. Lines 941–943 are restricted accordingly;
- M1s and Mc are described as what they are (a scale-only correction; a least-squares friction fit without discrepancy), with citations that do not imply more. Adding a proper autoregressive multi-fidelity model and a calibration with a discrepancy term is recommended, not required;
- the cup-depth offset is either traced to a mechanism checked against the data (stroke or bottom dead centre, flange inclination, a DDACS convention) or reported as unexplained, with M0 with and without the offset shown only as a sensitivity;
- the mapping from oil film to friction is tested against the observed within-run and between-pattern slopes, and the result is reported, with the caveat given in Section 5, point 5.

**R5. Report the measurement and say what the floor contains.** *Mostly rewording; the numbers are already in your files.* (Reviewer 2; also Reviewer 1.)

Every result is expressed in a within-run unit of batch centres. These come from a single-sided range imager that the paper neither names nor specifies. The code documents direction-dependent systematic errors that the paper omits; the paper reports only the 4- to 18-fold scatter of the flange width along the scan lines (ll. 488–491). According to `meas_scan.csv` and the feature table:

- the flange width in y reads 2.3–3.5 mm larger than in x;
- the two flange diagonals differ by 1.6–2.2 mm;
- the north wall reads 0.9–1.6° low on the convex cups;
- the shadowed south wall is 7–10° off;
- on the cut convex parts, the north wall reads several degrees steeper than the east wall.

Three further facts bear on the unit:

- The mid-side draw-in is quantised in steps of 0.019 mm (0.38 floors). A series takes only 6–21 distinct values, and the bootstrap error of the truth is zero for five alternatives.
- The floors of single runs range from 0.21 to 2.16 times the pooled floor of their geometry.
- The alternative-cluster interval in `alt_floor.csv` is wider than the interval in Table 3.

Satisfied when:

- a measurement subsection covers:
  - the instrument and its principle;
  - its resolution;
  - the scan geometry relative to the part;
  - the operation at which each characteristic is measured (OP10 or OP20), with a justification for using OP10 values for the wall angle and the depth;
  - what the dataset documentation says about scan order and timing;
- a table defines each characteristic (operation, region, directions used, resolution, known biases and their magnitudes), with the redundancy analysis given in full in the appendix or supplementary material;
- the paper states that absolute values are uncalibrated, unless verification data exist, and limits absolute comparisons with the simulation accordingly;
- evidence on process drift against measurement drift is reported from features fixed by the tooling (Reviewer 2, comment 1(b)), together with a plain statement of what remains untestable;
- Table 3 adds the alternative-cluster interval, the range of per-run floors, and the floor without the warm-up;
- the unit is called a production-and-measurement floor wherever the two are not separated (or is renamed), and is distinguished from the shop-floor meaning of "production floor";
- the Gaussian process's "noise floor" is renamed, for example to "noise-variance bound".

**R6. Treat single-run truths and the uncertainty of the distances honestly.** *New analysis (a sensitivity analysis) and rewording.* (Reviewers 1 and 2.)

Several features of the design limit what the uncertainty statements can show:

- each truth is the 95th percentile of a single run;
- the floor leaves out variation between runs, which the paper bounds at 1.2–9.8 floors;
- the main intervals hold the fits fixed and resample only 18 clusters;
- 22 rule pairs and 27 variants are compared without control for multiplicity.

The coverage figures are also over-read. A cluster bootstrap over alternatives gives 0.76–0.94 for M5's 0.86 with a sibling, and 0.93–0.98 for M3's 0.96. So 85–86 % does not demonstrate under-coverage, while M3's intervals look conservative.

Satisfied when:

- a sensitivity analysis perturbs each truth by a between-run component, ranging from near-replicate reproducibility (about 1–1.5 floors) up to the between-series bound, and shows how the distances, the ranking of rules and the guard bands change;
- coverage is reported with cluster-robust intervals, per characteristic and per decision-time stratum, with the guaranteed or nominal level stated for each interval rule;
- each type of interval says what it represents; paired intervals are labelled as descriptive (or adjusted for multiplicity); and the smallest difference between rules that the design can resolve is stated;
- distances below about one floor are reported as "< 1", as Section 5.1 itself implies.

**R7. Estimate the guard band as the procedure prescribes, and validate it.** *New analysis, using the stored intervals.* (Reviewer 3; also Reviewer 1.)

Step 5 defines the guard band per design family (ll. 403–410). Table A4 instead pools both families and all seven characteristics, and estimates the band in-sample under a prior chosen for convenience. My checks show what this hides:

- *Per geometry.* The nearest setting needs 1.5 floors on one cup and 2.5 on the other when interpolating, and 9.5 against 5.75 when extrapolating. M2 and M5 qualify for extrapolation on the convex cup only.
- *Per characteristic.* With a sibling and its band of 0.25 floors, the nearest setting is right in 89 % of decided verdicts on the dome but 98.5 % on the waviness.
- *Under a release-like prior* within ±5 floors, the nearest setting with its band decides only 63 %, 32 % and 2 % of feasible verdicts (with a sibling, interpolating and extrapolating).
- *Out of sample.* Leave-one-alternative-out estimation under the reference prior keeps the share of correct decided verdicts at 0.945–0.99, which is reassuring and worth reporting. Leaving out a whole force cell, however, gives only 0.83 for M2 and 0.81 for M5 when extrapolating.

Satisfied when:

- the band is estimated per family, or pooling is justified and reconciled with the new-family relation;
- out-of-sample estimates of the share correct and the trial rate are reported with intervals, leaving out one alternative and, for new settings, one force cell;
- the band and the trial rate are shown as functions of the width of the prior, with a release-like prior reported next to the current reference;
- the share correct is reported per characteristic or per class of characteristic, or the text says plainly that the 95 % is an average over characteristics;
- a compact version of Table A4 moves into the main text.

**R8. Separate the pre-specified from the post hoc, and stop quoting best-of minima as results.** *Rewording and an inexpensive cross-fit.* (Reviewer 1; also Reviewers 2 and 3.)

Section 4.5 records that the following came after results had been seen: NN, M1sn, M2n, M5n, the grouped schemes, the GP noise bound, the jackknife+ intervals, and the guard bands with their prior. Several headline numbers are also minima taken over rules and strata:

- "4.9 extrapolating to 500 kN and 8.9 to 100 kN" combines NN at 500 kN (4.85) with M1sn at 100 kN (8.85). A team that had committed in advance to one rule would face 9.45 floors (NN) or 8.85 (M1sn).
- "Safe at 16–17 floors" for a new family combines M3 in the produced family's floor (17.1) with M2 in the new family's own floor (15.8).

Satisfied when:

- Tables 2, 4 and A4 mark which rules were pre-specified and which were added post hoc;
- the abstract and the conclusions quote, per relation, the distance of a rule that a team would commit to in advance. For a new family they quote one rule, in the produced family's floor, which is the floor that step 6 prescribes;
- the abstract and the conclusions state the exploratory status;
- the selection of rules and bands is cross-fitted between the geometries (selected on one, evaluated on the other). The per-geometry distances suggest the within-family ranking will survive: with a sibling, NN needs 1.95 and 3.55 floors against M5's 6.45 and 8.50;
- the variance decomposition (ll. 687–694) is either restricted to a pre-specified set of rules or dropped.

**R9. Report results per characteristic and in physical units.** *Reporting from existing files.* (Reviewers 1 and 3.)

For a rule that always decides, the decisive distance is about the 90th percentile of the absolute error, pooled over seven characteristics. The worst one or two characteristics therefore set it. The archive holds the per-characteristic results (`dec_resolution.csv`, `panel_physical_units.csv`), and they differ widely:

- For a new setting, the nearest setting needs 1.85 pooled floors on the wall angle but 14.6 on the waviness.
- When extrapolating, the scaled simulation beats the force trend on the mid-side draw-in (3.95 against 5.70 floors) but fails on the cup depth (165 against 9.85 floors). The cup depth is where the 164-floor false accept of l. 630 comes from.

Satisfied when:

- an appendix table gives, per characteristic (or per group: process indicators, drawn geometry, cut and springback), the decisive and safe distances in floors and in physical units, with case counts;
- key distances in the main text are also given in physical units, and relative to σ_LT or as an equivalent Ppk;
- the statement that the simulation "helped only across families" is made consistent with the per-characteristic results.

**R10. Connect the distances to costs, trials and the decisions actually modelled.** *Rewording and a moderate new analysis.* (Reviewers 2 and 3.)

The two distances fix one implicit cost ratio and treat a trial as free and error-free. The expected-cost formula exists only in `scenarios.py`. The ISO 2768-1 scenario of Section 5.8 cannot discriminate within a family, because there the cheapest rules have zero expected cost at every cost ratio.

With a sibling, M5 and M5n have smaller safe distances than NN (paired differences of −2.6 and −2.8 floors). That extra safety is bought with trials, which the narrative does not price.

The decisions modelled are the release, change or trial of a new setting on a fixed tool, against a one-sided limit on q95. They fit process planning and the approval of process changes better than they fit tryout.

Satisfied when:

- Section 3 introduces the loss (the costs of a false accept, a false reject and a trial);
- expected cost and trial rate are reported alongside the two distances for the main rules, over a range of trial costs relative to a false accept, preferably specific to each relation (for example as a decision-curve-style figure). As an indication: as the trial cost falls from 0.5 to 0.02 of a false accept, the cost-minimising band of the nearest setting runs from 0 to 4.5 floors with a sibling, and from 0 to about 15 floors when extrapolating;
- the main table gives the distance on the false-accept side;
- the trial appears as a reference row, with its within-run error as a lower bound, and the text states that variation between runs adds to that error. The first 20 and 50 parts reproduce the full-run q95 to within 1.30 and 0.86 floors in 90 % of cases;
- the decision set is framed explicitly (process planning, approval of process changes in series production, qualification of AI tools), and the worked example is placed in that frame.

**R11. Rewrite for this journal's readers, and position the work in the intelligent-manufacturing literature.** *Rewording and restructuring.* (All reviewers.)

Satisfied when:

- an early schematic shows κ(δ) and ω(δ) for one rule, with δd, δs and the guard band marked;
- the worked example moves to Section 3 and is carried through steps 1–6;
- the main text keeps six or seven rules with descriptive names, for example M0, M1s, M2, M5, NN, M1sn and the learner of R3. The remaining rules, M6 and most of Section 5.9 move to the appendix or supplementary material, and each relation gets one compact table;
- two new figures show:
  - the cups, the cut part and where each characteristic is measured;
  - batch centres over one run, illustrating the floor;
- terms are used consistently: sibling and new variant; NN and nearest setting; M3n and M4; q_p and q95;
- the dense paragraphs (ll. 403–446 and Section 5.8) are split, and the sentence at l. 1009 is completed or deleted;
- Section 2 and Table 1 engage with the closest lines of work and say what is adopted and what is new. These are:
  - the reliance and global-similarity indices of automatic virtual metrology (the work of F.-T. Cheng and co-workers that Reviewers 1 and 3 cite);
  - regression with a reject option;
  - transfer learning and domain adaptation across products and processes in manufacturing;
  - uncertainty quantification in predictive quality;
  - the validation and calibration of forming simulation (friction models, springback modelling, tool deflection), and machine learning in sheet forming;
  - the global consumer's and producer's risks of conformity assessment (JCGM 106:2012);
- the main text does not grow overall; material moves to supplementary material instead.

**R12. Make the archive reusable and the declarations unambiguous.** *Administrative.* (All reviewers.)

Satisfied when:

- the code carries a licence. `RELEASE_NOTES.md` refers to a `LICENSE` file that is not in the release, and neither `.zenodo.json` nor `CITATION.cff` states a licence;
- the Zenodo DOI is reserved or minted and cited in the paper and in `CITATION.cff`, and the reviewers can access the deposited version;
- `requirements.txt` lists `tabulate`, which `DataFrame.to_markdown` needs in 13 scripts, and pins `pyarrow` and `remotezip`;
- Table A5 maps `tuning.py` with `tune_decisions.csv`, and `measurement.py` with `meas_sim.csv`;
- the statement "as the repository history records" (ll. 522–523) is either backed by a timestamped snapshot in the deposit or removed;
- the statement on generative AI says unambiguously what the language model did. That includes stating that the internal reviews were simulated with it, and which rules and analyses they caused to be added. The statement should follow the publisher's policy;
- two references are checked:
  - confirm the cited editions of ISO 5725-2 and ISO 22514-2 (two reviewers know them as the 2019 and 2017 editions);
  - state the PPAP criterion correctly: for initial process studies, an index above 1.67 is acceptable and 1.33–1.67 needs customer approval, while 1.33 is the usual criterion for ongoing capability.

### 4. Recommended changes

These would strengthen the paper, but I will not make the decision depend on them. Please say in your response which you adopted.

- *Few-shot transfer to a new family* (Reviewer 1). Use one to three produced alternatives of the target geometry, with and without the other family's record. Compare NN within the target family against a multi-task GP with a free correlation between families, or against a hierarchical model.
- *Multi-fidelity modelling and calibration with discrepancy* (Reviewer 1). This means an autoregressive multi-fidelity GP with a fitted scale and a GP discrepancy, and a calibration with a discrepancy term in the line of Kennedy and O'Hagan (2001) and Higdon et al. (2004, *SIAM Journal on Scientific Computing*). Brynjarsdóttir and O'Hagan (2014, *Inverse Problems*) explain why calibration without a discrepancy term misleads.
- *Interval methods* (Reviewer 1):
  - conformalised quantile regression on the parts (Romano, Patterson and Candès, 2019); the quantile-loss boosting in `tuning.py` is a start;
  - an interval score for interval quality (Gneiting and Raftery, 2007, *Journal of the American Statistical Association*);
  - a short discussion of what M6's guarantee costs in decisiveness.
- *A design-level verdict* in which a design meets only if all its characteristics meet (Reviewers 1 and 3). If you do not add it, Section 6.6 should say that the verdicts are marginal.
- *Lower or two-sided limits*, for example the 5th percentile with a change of sign, and a window for the draw-in (Reviewers 1 and 2).
- *Attribute outcomes.* A short paragraph on how a requirement on a rate (splits, wrinkles) would be scored (all reviewers).
- *Data from the RDDAC providers* (Reviewer 2). Request the production and scanning log and any verification data (a reference artefact, repeated scans, a CMM comparison), and report the outcome. Also consider sub-pixel edge estimation for the flange width.
- *Simulation inputs* (Reviewer 2):
  - an envelope taken over the measured incoming variation;
  - the flow-curve scaling factor, if DDACS offers it near the RDDAC conditions;
  - if feasible, new simulations with friction set per pressure level.
- *Capability and short runs* (Reviewer 2). A variant whose decided statistic is a capability index under a normal or time-dependent model, and qualification with truths taken from the first 20–50 parts.
- *An actual AI tool* (Reviewer 3). Score one representative tool: a language-model check with the full protocol of Reviewer 3's comment 6, or a learned model pre-trained on the DDACS geometries.
- *A reusable checklist* (Reviewer 3). Present it as a table modelled on model cards (Mitchell et al., 2019) and TRIPOD+AI (Collins et al., 2024, *BMJ*), and release the scoring as a small documented function separate from the pipeline.
- *Deployment* (Reviewer 3). Describe the planned user study, the interface for a step-6 verdict, and a step for monitoring and re-qualification.
- *Pre-registration* (Reviewers 1 and 3). Deposit the frozen procedure now, so that the confirmatory test of Section 7 is genuinely prospective.
- *Minor comments.* Please answer every minor comment in the three reports; most are quick.

### 5. Where I overrule or qualify the reviewers

1. **The breadth of new learners (Reviewer 1, comments 1–3).** Reviewer 1 lists:
   - an autoregressive multi-fidelity GP;
   - calibration with discrepancy;
   - few-shot transfer;
   - relation-matched and non-exchangeable conformal methods;
   - conformalised quantile regression;
   - an interval score.

   I require only one well-specified small-data learner, the crossing of predictors with a relation-matched interval, and honest labels (R3, R4). The rest is recommended. With six to nine alternatives per family, each added learner deepens the selection and multiplicity problem that Reviewer 1 rightly raises in comment 4. The paper's contribution is the evaluation, not a new learner, and its claims can be narrowed instead.

2. **Details of Reviewer 1's account of the GP collapse.** The substance is right, and the problem is if anything broader than stated. Three details need correcting:
   - *Noise at its bound.* "The noise at its bound in every fit" holds for the new-setting and new-family fits only. With a sibling the share is 97–99 %, as the paper says, and in the pooled scopes 84–91 %. Reviewer 3's "every other fit" has the same slip.
   - *Mechanism.* The collapse to the calibration mean does not need a force length scale at its lower bound. In the concave 100 kN wall-angle fit, the force length scale goes to its upper bound and the GP still predicts the calibration mean to within 0.007°, because the noise bound absorbs the trend.
   - *The "GP linear" variant.* In my nine refits, the linear amplitude went to its lower bound in six fits rather than eight. The reviewer may have refitted other cases. The conclusion stands either way: the variant leaves M5n at 17.2/6.1 floors.

   Finally, the significantly smaller safe distances of M5 and M5n with a sibling are bought with trials. I do not ask you to credit the GPs with that safety before the trials are priced, which is why R10 is required.

3. **The short trial (Reviewer 2, comment 5(b)).** The numbers reproduce, but the comparison is not like-for-like. The first parts and the truth come from the same run, so the trial's error leaves out variation between runs, whereas the rules' errors include it. The data therefore do not establish that a short trial is more decisive than every design-stage rule except the nearest setting. R10 asks for the trial as a lower-bound reference, not as a result.

4. **What the paper reports about the scanner (Reviewer 2, comment 3).** The paper does report the 4- to 18-fold scatter of the flange width and the choice of directions (ll. 488–491). What it omits are the instrument and the magnitudes of the biases. In series medians, the north wall of the cut convex parts reads 3.3–5.6° steeper than the east wall, a little less than the 5–7° quoted from the code's docstring. Neither point changes R5.

5. **Simulation grid and oil film (Reviewer 2, comment 4).**
   - *Grid.* At 300 kN, the simulated mid-side draw-in of the concave cup comes within 0.01 mm of the measured centre at μ = 0.15. "Exceeds ... for every friction coefficient" is therefore marginal there. The conclusion stands, and it is stronger than stated, since every Mc calibration ends at μ = 0.15.
   - *Oil film.* The mapping implies a sensitivity of 0.8–3.1 mm of mid-side draw-in per g/m². That is 20–80 times the within-run slope (0.038 mm per g/m²), but only a few to some tens of times the slopes between lubrication patterns (−0.26 to +0.38 mm per g/m²). Noise in the oil readings also attenuates the within-run slope. The mapping should be tested and reported (R4) with that caveat, rather than declared wrong by an order of magnitude.

6. **Data from the providers and new simulations (Reviewer 2).** These are recommended, not required, because both lie outside your control. What is required is that the paper says what is unknown and limits its claims accordingly (R4, R5).

7. **Moving guard bands between geometries (Reviewer 3, comment 2).** The 83–84 % is correct. But step 5 does not transfer a band from one family to another. Under per-family estimation, M2 and M5 would not qualify at all for an extrapolated setting on the concave cup. The check therefore supports per-family estimation and out-of-sample validation (R7), not a different procedure. Reviewer 3's own leave-one-alternative-out result also shows that the in-sample optimism is modest under the reference prior. The larger issues are the choice of prior and the differences between characteristics.

8. **Deployment (Reviewer 3, comments 4(c), 6 and 8).** A user study, an interface design, a monitoring step and the scoring of an actual AI tool would all add value. The paper, however, claims structural validity only. I recommend these additions; I require instead that the claims of usefulness and of a standard be removed (R1).

9. **Fit to the journal.** I considered whether the paper, once its claims are narrowed, belongs in this journal rather than in an engineering-design or quality-engineering journal. An evaluation methodology for AI-supported manufacturing decisions, with a strong production baseline and real production data, is within the journal's scope. That holds on two conditions: the learned rules get a fair test (R3), and the paper speaks to the people who build and deploy such tools (R11). A revision that only narrows the claims, without R3, would leave a weak case for publication here.

### 6. What I checked and what I found

All checks were read-only. I did not rerun the pipeline. I imported the released functions in memory, with the package versions of `requirements.txt` installed, and wrote nothing to the repository. The only refits were nine M5n fits and nine fits of the "GP linear" variant, made with the released `m5_fit`.

| Claim (reviewer) | How I checked | Finding |
|---|---|---|
| The near-replicate stratum is defined from the held-out outcome; decision-time strata give about 1.5 floors (Reviewer 2) | Read `panel.sibling_strata`. Recomputed the strata from `dec_intervals.csv` and `alt_effects.csv` with the exact estimator of `decisions.py`. | **Confirmed.** The stratum uses the held-out alternative's own lubrication contrasts. The outcome strata reproduce 0.85, 2.45 and 4.85 floors (58, 34 and 34 cases). Decision-time strata: when the siblings are not resolvable from each other, NN needs 1.60 floors (75 cases; 90th percentile of absolute error 1.54); when they are, 4.40 floors (51 cases; 4.36). M1sn needs 3.05 and 4.20; M5 needs 6.15 and 8.90. |
| The force length scale of the GPs sits at its lower bound for a new setting, so the GP predicts the calibration mean (Reviewer 1) | Read `dec_gp.csv` and the per-fit hyperparameters in `dec_intervals.csv`. Refitted nine M5n fits in memory with `m5_fit`. | **Confirmed.** The median force length scale is 0.100 (at the bound in 57 % of M5 and 71 % of M5n new-setting fits). The noise is at its bound in all new-setting and new-family fits, in 97–99 % of fits with a sibling, and in 84–91 % of pooled fits. The M5n centre lies within 0.01 floor of the calibration mean in 94 % of new-setting cases (maximum 0.08). Eight of the nine refits equal the calibration mean to four decimals; for example, 14.8333 mm against a force-trend value of 14.9487 mm (concave cup, 100 kN, mid-side draw-in). At 300 kN, M5n = NN = M1sn exactly. With a sibling, the M5n centre lies a median of 0.28 floor from NN (90th percentile 1.19). |
| A clustered interval for the 85–86 % coverage (Reviewer 1) | Cluster bootstrap over the 18 alternatives (4,000 resamples) on `dec_intervals.csv`. | **Confirmed.** M5: 0.857 (interval 0.76–0.94). M5n: 0.849 (0.76–0.93). M3: 0.960 (0.93–0.98). Per characteristic, M5 covers 0.83–0.89. |
| Guard bands per geometry, and accuracy when bands move between geometries (Reviewer 3) | Reproduced 21 bands of Table A4 exactly with `panel.guard_band` on the stored intervals in the produced family's floor, then split them by geometry, applied them across geometries and estimated them out of sample. | **Confirmed.** NN needs 1.5 and 2.5 floors interpolating, 9.5 and 5.75 extrapolating (concave and convex). When extrapolating, M5 has no band on the concave cup and 5.0 on the convex; M2 has none and 6.25. Convex bands applied to concave cases give 84.2 % (M2) and 83.4 % (M5) correct decided verdicts. Leave one alternative out: 0.945–0.99 under the reference prior; under ±5 floors, 0.925 (NN) and 0.911 (M5n) when extrapolating. Leave one force cell out: 0.83 (M2) and 0.81 (M5) when extrapolating. NN with a sibling at 0.25 floors is right in 0.892 of decided verdicts on the dome and 0.985 on the waviness. Under ±5 floors, NN decides 63 %, 32 % and 2 % of feasible verdicts. |
| Scanner biases are documented in the code but missing from the paper (Reviewer 2) | Read the `qc.py` docstring, `meas_scan.csv` and the part feature table; searched `main.tex`. | **Confirmed, with a small overstatement.** The y flange width reads +2.29 to +3.47 mm more than the x width, with 3.7–17.7 times its standard deviation. The diagonals differ by 1.64–2.17 mm. The north wall reads 0.92–1.64° low on the convex cups, and the south wall is 6.7–10.0° off. On the cut convex parts, the north wall reads 3.3–5.6° steeper than the east wall (series medians). The paper reports only the scatter ratio. |
| The simulation grid fails to reproduce the measured draw-in (Reviewer 2) | Compared `features_ddacs_rddac.csv` at 0.99 mm with the measured centres. Recomputed the Mc friction fits in memory. | **Confirmed.** Mid-side draw-in, simulated minus measured at μ = 0.15: +1.49 and +1.73 mm at 100 kN; +0.01 and +0.40 mm at 300 kN (concave and convex). At 500 kN the measured value is reached at μ ≈ 0.105 and 0.116. Corner draw-in: +2.6 to +3.5 mm at μ = 0.10, and +1.3 to +3.3 mm at μ = 0.15. All 72 within-family Mc calibrations end at μ = 0.15. |
| The cup-depth offset is not a surface effect (Reviewer 2) | Read `dec_alternatives.csv` and the depth definitions in `features_rddac.py` and `features_ddacs.py`. | **Confirmed.** Measured depth is 28.28–28.82 mm; the nominal simulation gives 29.24–29.88 mm. Both define depth as a height below the bottom plane measured on the same side of the sheet, so a half-thickness offset cancels. |
| The mapping from oil film to friction is too sensitive (Reviewer 2) | Multiplied the simulated sensitivity to friction by the slope of the mapping; compared with `alt_mrc.csv` and `panel_runs.csv`. | **Confirmed, with the caveat in Section 5.** The mapping implies 0.77–3.13 mm per g/m². The observed within-run slope is 0.038 mm per g/m², and the slopes between patterns range from −0.26 to +0.38. |
| Per-run floors, cluster interval, quantisation and simulation noise (Reviewer 2) | `alternatives.floor_from` applied to each run; `alt_floor.csv`; `panel_resolution_steps.csv`; `meas_sim.csv`. | **Confirmed.** Per-run floors are 0.21–2.16 times the pooled floor (0.36–1.62 for the mid-side draw-in). The cluster interval for the waviness floor is 0.0021–0.0050 mm. The draw-in step is 0.38 floors, with 6–21 values per series and five zero standard errors. The simulated wall angle's x–y differences have a standard deviation of 1.8–2.3 floors (maximum 10.5–12.5), and the dome roughness is 2.4–9.8 floors. |
| A short trial reproduces q95 to about one floor (Reviewer 2) | Computed q95 of the first n parts against the full series for all 126 cases. | **Reproduced.** At the 90th percentile: 1.30 floors for 20 parts and 0.86 for 50 parts. This is within-run only (Section 5, point 3). |
| The tuning study changes no ranking against NN (Reviewer 1) | `tune_decisions.csv`. | **Confirmed.** The best learner needs 11.2 floors with a sibling (NN: 3.35) and 13.1 for a new setting (NN: 8.45). |
| Per-characteristic heterogeneity, and best-of headline numbers (Reviewers 1 and 3) | `dec_resolution.csv`, `panel_physical_units.csv`, `panel_force_levels.csv`, `panel_source_floor.csv`. | **Confirmed.** The figures are those quoted in R8 and R9. |
| Costs (Reviewer 3) | `scen_cost_map.csv`; cost-minimising NN band computed from the stored intervals. | **Confirmed.** Within a family, the cheapest rules have zero expected cost. NN's cost-minimising band is 0–4.5 floors with a sibling and 0–14.75 floors when extrapolating. |
| State of the archive (all reviewers) | `sha256sum -c SHA256SUMS`; the table functions of `make_tables.py` run in memory; the metadata files. | **Confirmed.** All 127 checksums verify. Tables 3, 4, A2, A3 and A4 regenerate identically. There is no `LICENSE` file and no licence field; `tabulate` is missing from `requirements.txt`, and two packages are unpinned. |

### 7. Next steps

- Please submit the revision by **20 January 2027** (90 days). If the new analyses, or a reply from the dataset providers, need longer, ask for an extension before that date.
- Please submit four things:
  - the revised manuscript;
  - a version with the changes marked;
  - a response letter. It should first take R1–R12 in turn, saying what you changed and where (with line numbers) and giving your evidence wherever you disagree. It should then answer every comment of the three reviewers, major and minor, point by point;
  - version 2 of the archive, with the licence, the DOI, updated checksums and the scripts that produce the new analyses, all mapped in Table A5.
- Where numbers change (decision-time strata, per-family guard bands, the new learner), carry them consistently through the abstract, the tables, Table 5 and the conclusions, and generate them from the archive as you do now.
- Keep the main text at about its current length, and move material to supplementary material.
- I will send the revision to the same three reviewers and will check the required changes myself against the new archive.
- If you think any required change is mistaken, say so in your response, with evidence, and I will weigh it.

Yours sincerely,

Handling editor (a fictional persona in a simulated review panel), Journal of Intelligent Manufacturing

---

## Part 2. Confidential note to the Editor-in-Chief

**Recommendation: major revision (substantial).** All three reviewers recommend major revision, and my read-only checks of the archive confirm their central claims:

- the learned rules reduce to the baselines in this design;
- the simulation grid does not contain the produced process, and every within-family friction calibration ends at the edge of the grid;
- one headline number comes from strata defined by the outcome;
- the guard band is estimated in-sample and pooled over families and characteristics.

None of this is a question of integrity. The archive is exemplary: all 127 checksums verify and every generated table regenerates identically. The post hoc additions are disclosed in the manuscript itself. The core idea is sound and useful to our readers, and the fixes are within reach with the existing data. I therefore prefer a demanding major revision to rejection with an invitation to resubmit. I have consolidated three long, overlapping reports into twelve required changes, so that the second round can be judged against a clear list.

**Risks.**

1. *Fit to the journal.* Once the AI claims are narrowed to what was shown, the AI content is modest: Gaussian processes and gradient boosting fitted to six to nine alternatives. I have therefore required a fair test with at least one properly specified small-data learner. If the revision only narrows its claims, the paper would sit better in an engineering-design or quality-engineering journal, and I would say so at the second round.
2. *Use of a language model.* A language model assisted with code, analysis and drafting. Internal reviews simulated with it led to rules and analyses being added after results were seen. This is disclosed in Section 4.5 and in the declarations, and appears consistent with Springer Nature's policy as I understand it: no AI authorship, and the use documented in the manuscript. Its extent is unusual, however. I have asked for unambiguous wording; you may wish to confirm that the journal has no further requirement.
3. *The archive.* It needs a licence and a minted DOI before acceptance.
4. *Generality.* The evidence comes from a single laboratory process. A revised version that still generalises from it would need firm handling.

If the uncertainty analysis changes substantially in revision, I may also consult a statistician on the bootstrap designs.
