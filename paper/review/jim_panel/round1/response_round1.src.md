# Response to the editor and the reviewers, first round

**Manuscript:** "When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing" (submitted as "Evaluating AI-based manufacturability decisions against the resolution of production"), by Hüseyin Tayyer Canseven
**Journal:** Journal of Intelligent Manufacturing
**Answers:** the decision of 22 October 2026 (major revision, required changes R1–R12) and the reports of Reviewers 1, 2 and 3
**Revision of:** the version considered in the first round (frozen as `paper/review/jim_panel/round1/main_reviewed.tex`)

> **Note on this document.** The decision letter and the three reports it answers were written by AI agents acting as a simulated review panel; they do not come from the journal, its editors or its reviewers. The response is written as it would be to a real editor. Items that only the author can complete before a real submission (the licence and the DOI of the archive, the registration of the frozen procedure, the request to the dataset providers) are marked **[author]**.

**Locations.** Page and line numbers refer to the revised manuscript, `paper/main.pdf`, compiled with line numbers. Tables, captions and figures carry no line numbers and are named. The new Online Resource 1 (`paper/supplement.pdf`) holds Tables S1–S20 and Figures S1–S4; its Section 1 specifies every rule and analysis added in this revision. The version marked up against the reviewed manuscript is `paper/review/jim_panel/round1/main_diff.pdf`; latexdiff shows the regenerated tables in their new form; the new title (R1) and the new figures are not marked. The revised paper has {{totalpages}} pages; the main text ends on page {{mainpages}} (page 23 before). The running text of the main body grew by about 5 % (from about 9,100 to 9,600 words); the rest of the growth is the four figures and two tables that the decision asked for (the schematic, the parts, the batch centres, the costs, the characteristics and the guard bands) and 21 references. Everything else that was added went to the appendix and to Online Resource 1.

**Archive.** Version 2 of the archive holds every script and result file of this revision. `RELEASE_NOTES.md` lists what was added and the checksums of the main new result files; `SHA256SUMS` covers every script and result file. Every result file of version 1 is unchanged, except one figure. Licence and DOI: **[author]**.

Dear Editor,

Thank you for consolidating three long reports into twelve required changes, and for checking the reviewers' central claims against the archive yourself. Your checks and the reviewers' were right on every point that the decision rests on, and the revision follows R1–R12. In brief:

- **Claims.** The paper is retitled, the abstract rewritten (five numbers, 249 words, ending with a finding), "evaluation standard" removed, and the reuse for classifiers and language-model checks presented as an untested proposal (R1).
- **Strata.** The sibling strata are now defined from decision-time information (R2); the release-level comparison is reported as marginal (0.15 floor).
- **Learning.** The GP diagnostics are tabulated; a learner specified for the small-data regime (the trend GP M7n), an autoregressive multi-fidelity model (M7) and a friction calibration with a discrepancy term (Mcd) are added; prediction is separated from uncertainty by crossing predictors with relation-matched intervals; the tuning study is reported (R3). The finding does not change: within a family the learners reduce to the production record, and intervals calibrated on the relation, not learning, make it safe for new settings.
- **Simulation and measurement.** The simulation dataset is presented as uncalibrated and not containing the produced process, with a validation table, the censored friction calibration, the oil-film test and the unexplained depth offset (R4). A measurement subsection and a table of characteristics report the instrument, its resolution and its direction-dependent biases (R5).
- **Uncertainty and guard bands.** A between-run sensitivity, cluster intervals of coverage, interval scores and the smallest resolvable difference are added (R6). Guard bands are estimated per family, validated out of sample, shown against the width of the prior and per characteristic, and moved into the main text (R7).
- **Selection, characteristics, costs.** Pre-specified and post hoc rules are marked, the abstract and conclusions quote a rule committed to in advance, the selection is cross-fitted between the geometries (R8); results per characteristic, in physical units and as performance indices are reported (R9); the loss, costs, trial rates, the false-accept and false-reject sides and the trial as a reference rule are added (R10).
- **Presentation and archive.** The paper is restructured for this journal (R11), and the archive and declarations are fixed (R12).

All new numbers are generated from the archive by the same scripts as before. Part 1 takes R1–R12 in turn, Part 2 the recommended changes and Part 3 your qualifications of the reports; Parts 4–6 answer every comment of the three reviewers.

---

## Part 1. Required changes R1–R12

### R1. Title, abstract, contributions and conclusions

- **Title.** "When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing". It says what was done and keeps the question that the editor and the reviewers saw as the paper's strength.
- **Abstract.** Rewritten. It defines the floor, the evidence relations (by their three cases) and the decisive and safe distances where they first appear; it carries five numbers (95 %, 5 %, 3.4, 8.5 and 30 floors); it states the exploratory status, the single laboratory process, that every alternative was produced once and that the simulation dataset is uncalibrated; and it ends with a finding: "Within a family, a production record indexed by its relation to the coming design is the baseline a learned manufacturability check has to beat."
- **"Evaluation standard"** no longer appears. The contributions end with "a proposed reporting checklist with an open scoring function" {{loc:a proposed reporting checklist with an open scoring function}}; the study is called exploratory in the introduction {{loc:The study is exploratory}}, in Section 4.5 {{loc:The comparison of rules is therefore exploratory}} and in the conclusions {{loc:In an exploratory application to one laboratory deep-drawing process}}.
- **Classifiers and language-model checks** are an untested proposal: Section 6.4 is titled "a proposal" and opens its extensions with "The extensions below are untested" {{loc:The extensions below are untested}}. Table 6 of the first version (the mapping onto other processes) is removed; the checklist is Table 8, "Proposed reporting checklist".
- **Three limits of scope** are stated in Section 3.1 {{loc:Three limits of scope apply}} (one-sided upper limits, marginal verdicts with a design-level verdict as an extension, attribute outcomes not covered) and again among the threats to validity {{loc:attribute outcomes such as splits and wrinkles are not covered}}.
- **Table 7** (the former Table 5) heads its second block "Observed in this study (one process, 18 alternatives produced once, 2 geometries; not general)" and gives the basis of each row in alternatives, force cells and transfers.

### R2. Decision-time sibling strata

- **Definition.** A new variant is now classed by whether its two produced siblings differ resolvably from each other, which a team knows before deciding {{loc:so the sibling relation is stratified by this decision-time information}}. The function is `qualify.decision_time_strata`.
- **Results.** The nearest setting needs 1.60 floors when the siblings do not differ resolvably (75 cases on 17 alternatives) and 4.40 when they do (51 cases on 16); the force trend 3.05 and 4.20; M5 6.15 and 8.90 {{loc:Stratified by what a team knows when deciding}}. These are your figures. Table S3 gives them for every main rule with the 90th percentile of the absolute error, and keeps the outcome strata of the first version (0.85, 2.45 and 4.85 floors; 58, 34 and 34 cases) only as a labelled diagnostic.
- **Carried through.** Section 6.1 {{loc:1.6 when the two produced siblings did not differ resolvably}}, Table 7 ("New variant with a produced sibling") and the conclusions now use the decision-time strata; the abstract no longer quotes strata at all.
- **Release-level statement.** Recomputed and reported as marginal: a limit at a performance index of 1.33 lies a median 1.75 floors from the truth, inside every attainable distance except the nearest setting's 1.60 with non-resolvable siblings, "which it exceeds by only 0.15 floor" {{loc:which it exceeds by only 0.15 floor}}. The conclusions say that release-level requirements "needed a trial unless a near-replicate sibling had been produced".

### R3. A fair test of the learned rules

- **(a) GP diagnostics.** Table A3 gives, by relation, the fitted force length scale and the share of fits at its bound, the noise relative to its bound (M5, M5n) or the nugget relative to the sampling error (M7n), and the distance of each centre from the calibration mean, NN and M1sn. Section 5.4 reports them {{loc:reduce to the baselines in this design}}: for a new setting M5n's force length scale is at its lower bound in 68–79 % of the fits, its noise at its bound in every fit, and its centre within 0.01 floor of the calibration mean in 93–95 % of the cases; with a sibling it lies a median 0.28 floor from the nearest setting.
- **(b) A learner specified for this regime.** The trend GP M7n has an explicit linear mean in force and lubrication whose coefficients are integrated out (universal kriging, restricted likelihood), weakly informative log-normal priors on length scales and noise instead of hard bounds, and a noise term made of the known sampling variance of each truth plus an estimated between-run nugget that absorbs no modelled effect {{loc:The trend GP (M7n) is a learner specified}}; its priors are in the appendix {{loc:M7n and M7 work in pooled floors}} and Online Resource 1, Section 1. It is scored like every other rule. It reduces to the force trend: its centre lies a median 0.33–0.36 floor from M1sn for a new setting, its force length scale stays near the prior's 200 kN, and its nugget is three to four times the sampling error {{loc:The trend GP, specified for this regime, reduces to the force trend instead}}. It is more decisive than M5n for a new setting (14.5 against 17.2 floors; paired difference −2.7, interval −5.6 to −1.1) and as safe, but less decisive than the nearest setting in every relation.
- **(c) Prediction separated from uncertainty.** P+RM puts around the prediction of a rule P a relation-matched interval: the 90 % split-conformal quantile of P's absolute errors over the cases of the same relation in the other family, a group-conditional construction, guaranteed only if the families' errors are exchangeable {{loc:Finally, intervals are separated from predictors}}. Table A4 crosses eight predictors (NN, M1sn, M1s, M5n, M5, M3n, M7n, M7) with it. With it the nearest setting is safe for a new setting (safe distance below one floor, against 6.8 for M5 and 5.2 for M7n) at the decisive distance of the learned intervals, covers 88 % of the truths interpolating and 93 % extrapolating, and has the best interval score {{loc:Prediction and interval separate}}. Credit for intervals thus goes to the calibration on the relation, not to the learner.
- **(d) Tuning study.** Summarised {{loc:The archive's study of part-level boosting}} (no setting closer than 11.2 floors with a sibling and 13.1 for a new setting) and mapped in Table A7 (`tuning.py`: `tune_decisions`).
- **(e) Phrasing.** RQ3 now names the data regime and model classes {{loc:And, with six to nine produced alternatives, what do a generic simulation dataset}}; so do Section 6.1 {{loc:For this simulation dataset and for Gaussian processes and boosting fitted to six to nine alternatives}}, the abstract ("a Gaussian process specified for small data reduced to a force trend") and the conclusions {{loc:Gaussian processes and boosting fitted to six to nine alternatives reproduced the production record}}. "Learned intervals" now refers only to model-based intervals; M2 and M2n are called "the rules' own intervals" or "largest residual".

### R4. The simulation as what it is

- **Validation table.** Table A6 summarises, per characteristic over the six geometry–force cells, the measured centres, the simulation at the nominal thickness and friction minus the measurement in the unit and in floors, the cells inside the friction range, the closest grid friction and the extraction noise (x–y differences 1.8–2.3 floors for the wall angle, roughness 2.4–9.8 floors for the dome). Table S18 gives every cell, with the simulation at nominal friction, the range over the grid, the closest grid friction and the residual there.
- **Text.** Section 5.2 opens with "The simulation dataset does not contain the produced process" {{loc:The simulation dataset does not contain the produced process}}: the measured centre lies within the simulated friction range in 11 of 42 combinations, the mid-side draw-in is not reached at 100 kN for any friction, and so on. The friction calibration is censored: "all 72 within-family least-squares calibrations of Mc end at its upper edge (0.15)" {{loc:all 72 within-family least-squares calibrations of Mc end at its upper edge}}. The abstract ("an uncalibrated simulation dataset"), Section 6.1 ("For this simulation dataset"), Section 6.3 {{loc:the simulation here is a generic dataset that does not contain the produced process}}, the threats {{loc:so the findings on simulation concern this dataset}} and the conclusions ("a generic simulation dataset") restrict the findings to this dataset. The sentence "calibrating the friction coefficient did not repair it" is replaced by one that names the grid as the limit.
- **Labels.** M1s is "the scale term of a multi-fidelity correction without its discrepancy" {{loc:the scale term of a multi-fidelity correction without its discrepancy}}; Mc is "friction per pattern fitted to the draw-ins, least squares, plus offset" (Table A2) and "without a discrepancy" in the computation details {{loc:Mc calibrates, per lubrication pattern, the friction coefficient}}, with no citation of Kennedy and O'Hagan (2001).
- **Recommended additions, adopted.** An autoregressive multi-fidelity model M7 with a fitted scale on the simulation and a GP discrepancy {{loc:Its counterpart with the simulation (M7) is the autoregressive multi-fidelity model}}, and a friction calibration with a GP discrepancy, Mcd (Online Resource 1, Section 1). M7 is worse than M7n for a new setting (28 floors), because the simulated force trend enters it; Mcd's posterior piles at the lower edge of the grid (0.05), where the simulated force effect is weakest {{loc:with a discrepancy term the posterior of Mcd piles at the lower edge}}, and Mcd is the most decisive rule for a new family (30 floors).
- **Cup-depth offset.** Reported as unexplained, with the checks: bottom and flange are seen from the same side of the sheet, so a half-thickness offset cancels; the flange inclination would make the measured depth larger, not smaller; the wall position at 15 mm depth also differs (2.0–2.2 mm in radius); a shorter effective drawing depth, a different tool geometry or a scanner scale error could each produce the offsets, which the data cannot separate {{loc:The depth offset is not definitional}}. M0 without the offset (65 instead of 108 floors) is given only as a sensitivity. The press position at bottom dead centre varies by at most 0.053 mm within a series (Table S19).
- **Oil-film mapping.** Tested against the within-run and between-pattern slopes {{loc:The dataset's mapping from oil film to friction implies}}: the mapping implies 0.8–3.1 mm of mid-side draw-in per g/m², against within-run slopes of −0.01 to +0.09 mm and median slopes between the patterns of −0.17 to +0.39 mm per g/m². With your caveat, the text says that noise in the oil readings attenuates the within-run slope, and that the mapping is nevertheless too sensitive by an order of magnitude. Section 4.2 now says that M3, M3n and the matched simulations depend on the mapping {{loc:an assumption of the dataset's authors on which M3, M3n and the matched simulations depend}}, and that Mc and Mcd calibrate the friction instead.

### R5. The measurement and what the floor contains

- **Measurement subsection.** Section 4.3 names the instrument (a single-sided laser line scanner recording height and luminescence images), its resolution and the scan geometry relative to the part (0.077 mm along the laser line, 0.158 mm between lines in the direction of motion, 7.75 µm height steps, cup bottom facing the scanner) {{loc:The parts were measured with a single-sided laser line scanner}}, the origin of the scales and the nominal repeatability, the operation at which each characteristic is measured with the reason for OP10 for the wall angle and the depth {{loc:measured after drawing because the cut removes the flange that defines the depth}}, and, in Section 4.1, what the documentation says and does not say about the order of production and scanning {{loc:the documentation states neither the order of the blocks}}.
- **Table of characteristics.** Table 3 gives each characteristic's operation, region and definition, the directions used, its measurement step relative to the floor, the number of distinct values per series and the direction-dependent differences with their magnitudes. Table S20 gives the redundancy analysis per series. The first version described the flange-width scatter as "along the scan lines"; the correct statement is that the width in the direction of motion reads 2.3–3.5 mm larger and scatters 3.7–17.6 times more than the width along the laser line, which the mid-side draw-in uses.
- **Uncalibrated absolute values.** "Absolute values are therefore uncalibrated, which limits every absolute comparison with the simulation … but not the floor" {{loc:Absolute values are therefore uncalibrated}}.
- **Process against measurement drift.** Section 5.1 reports the tooling reference that Reviewer 2 proposed {{loc:the batch centres of the flange width and of the cup width at 15}}: the batch centres of flange width and cup width at 15 mm depth correlate at r = −0.27 and +0.27 within the runs of the two geometries (pooled over both geometries, as in Reviewer 2's quick check, r = 0.03), which argues against a common lateral scale drift; the cup width varies by 0.06–0.07 mm between batches and so bounds such a drift only below 0.05 %; "drift in height and of the edge detection remain untestable" {{loc:drift in height and of the edge detection remain untestable}}. The physical candidates for drift are listed {{loc:Physical candidates for the drift are}}.
- **Table 4.** Adds the alternative-cluster interval, the range of single-run floors (0.21–2.16 of the pooled floor of the geometry) and the floor without the warm-up (0.75–1.00); the batch interval, which ignores the serial dependence, is left to the archive.
- **Naming.** The unit is renamed the within-run floor throughout, and Section 3.2 says that without a reference artefact it is a production-and-measurement floor and not the shop floor {{loc:it is a production-and-measurement floor, and not the shop floor}}. The GP's bound is the "noise-variance bound" {{loc:(the noise-variance bound)}}.

### R6. Single-run truths and the uncertainty of the distances

- **Between-run sensitivity.** Every truth is perturbed by a between-run component of standard deviation τ = 0, 0.5, 1, 1.5, 2 and 3 floors and, as a bound, by each characteristic's variation between series {{loc:a sensitivity analysis adds to every truth a between-run component}}. With τ = 3 floors the nearest setting needs 5.8 floors with a sibling and 10 extrapolating, M5 9.3 and 20; a production-record rule stays the most decisive within the family in each of 200 draws; the nearest setting's band with a sibling grows from 0.25 to 2.9 floors {{loc:A between-run component added to every truth lengthens the distances but keeps their order}}; Table S12.
- **Coverage.** Reported with cluster-bootstrap intervals over alternatives, with each rule's guaranteed or nominal level (Table S4) and per characteristic and decision-time stratum (Table S5). With a sibling M5 covers 86 % (0.76–0.94), M5n 85 % (0.76–0.93) and M3 96 % (0.93–0.98) against a guarantee of 0.78 {{loc:With a sibling the model-based intervals}}. For a new setting and a new family the alternatives of one held-out cell or family share their calibration set and are near-replicates, so a cluster bootstrap over alternatives would understate the uncertainty; Table S4 says so and gives no interval there.
- **What each interval represents.** Section 4.4 describes the three kinds {{loc:The uncertainty of the distances is described in three ways}}; the paired intervals are labelled "descriptive and not adjusted for the many comparisons"; the smallest difference the design resolves is stated: "Paired intervals between point rules span about ±2 floors with a sibling and when extrapolating" {{loc:Paired intervals between point rules span about}} (median half-widths 2.11, 0.39 and 2.24 floors; Table S17).
- **"<1".** Distances below one floor are reported as "<1" in every distance table, with the reason in Section 3.4 {{loc:Distances below about one floor are reported as}}.

### R7. The guard band as the procedure prescribes, validated

- **Per family.** The band is estimated per family {{loc:The band is estimated per family and validated out of sample}}. The bands differ between the geometries (the nearest setting 1.5 and 2.5 floors interpolating, 9.5 and 5.75 extrapolating), M2 and M5 qualify for an extrapolated setting on the convex cup only, and moved to the concave cup their bands give 84 and 83 % correct decided verdicts {{loc:Estimated per family, as step 5 prescribes}}; Table S7.
- **Out of sample, with intervals.** Leaving one alternative out keeps the share of correct decided verdicts at 0.94–0.99 for every rule and relation; leaving one force cell out at 0.93–0.95 for the nearest setting and the force trend, but at 0.83 and 0.81 for M2 and M5 when extrapolating {{loc:Out of sample the bands hold}}. Table S8 gives the shares with 95 % cluster intervals and the trial rates, under both priors.
- **Width of the prior.** Band and trial rate are given for priors within ±3, ±5, ±10, ±20 and ±50 floors (Table S9); the release-like prior is reported next to the reference {{loc:The bands belong to the prior as much as to the rules}}: the nearest setting's band grows to 2.0, 4.25 and 14.25 floors, and it decides only 63, 32 and 2 % of the verdicts.
- **Per characteristic.** "The 95 % is an average over characteristics" {{loc:The 95\,\% is an average over characteristics}}, with the dome (89 %) and the waviness (98.5 %) named; Table S10 gives the share per characteristic and bands per class of characteristic.
- **Main text.** Table 6 is the compact version of the former Table A4, with the band under both priors, the out-of-sample share correct and the trial rate.

### R8. Pre-specified and post hoc rules; no best-of minima

- **Marks.** Tables 2, 5 and A2 mark the rules added after the first results (†) and in this revision (‡); M0–M5 and M3n are pre-specified.
- **Quoted distances.** The abstract and the conclusions quote, per relation, the nearest setting, a rule committed to in advance: 3.4 floors with a sibling and 8.5 for a new setting, in the conclusions {{loc:decided at 3.4 floors with a produced sibling and 8.5}}. The best-of figures "4.9 extrapolating to 500 kN and 8.9 to 100 kN" are gone; Section 6.1 gives the nearest setting at 4.7 interpolating and 9.5 extrapolating. For a new family the abstract states a bound ("none closer than 30 floors") rather than a rule's achievement, and the conclusions add the pre-specified M5 at 35 floors, all in the produced family's floor {{loc:(the pre-specified M5 at 35)}}. The safe distance "16–17 floors" for a new family, which mixed two floors, is gone.
- **Exploratory status.** In the abstract and the conclusions (R1).
- **Cross-fitting.** The selection of rules and bands is cross-fitted between the geometries {{loc:The selection of rules and bands is cross-fitted between the geometries}}. Selected on one geometry and evaluated on the other, the most decisive rule is the nearest setting with a sibling (2.0 and 3.6 floors), the force trend or the median interpolating (4.2–5.8) and the force trend or the nearest setting extrapolating (8.9–11) {{loc:Selected on one geometry and evaluated on the other}}; Table S13 gives the step-6 selection with its band, share correct and trial rate on the other geometry. The ranking survives, as you expected.
- **Decomposition.** Restricted to the pre-specified rules M1–M5 (Table S17): within the family the rule accounts for 60 % of the variance of the decisive distances and the relation for 16 %, which supports "within a family the choice of rule mattered more than the relation, also among the pre-specified rules" {{loc:also among the pre-specified rules (RQ2)}}.
- **Development record.** Section 4.5 now lists everything added after the first results and says which additions followed reviews of earlier versions simulated with a language model {{loc:The rules were not fixed in advance}}.

### R9. Per characteristic and in physical units

- **Table A5** gives the decisive distance per characteristic in floors and in the unit, for the nearest setting in all three within-family relations, M1sn and M1s extrapolating and M5 for a new family, with case counts and the performance index of a requirement at the nearest setting's distance. Table S15 gives decisive and safe distances per characteristic for every main rule and relation. The tail statistic is no longer the only view: the 165-floor false accept of the scaled simulation is attributed to the cup depth {{loc:on the cup depth, while on the mid-side draw-in}}.
- **In the text.** Physical units {{loc:In physical units the nearest setting is right beyond}}; the floor in long-term standard deviations (Table 4, last column) and the requirement grid in physical units {{loc:floors are about}}; the performance index in Table A5 and Section 5.6.
- **Consistency.** "The simulation helped only across families" is replaced by "the simulation contributed little within a family, helping single characteristics when extrapolating in force, and mattered across families, for the characteristics it models directly" {{loc:the simulation contributed little within a family}}, which Table A5 and Section 6.3 bear out (the draw-ins and the arm angle when extrapolating).

### R10. Costs, trials and the decisions modelled

- **Loss.** Section 3.1 introduces the costs of a false accept, a false reject and a trial and the expected cost per verdict, Eq. (2) {{loc:so a rule's expected cost per verdict is}}.
- **Expected cost and trial rate.** Fig. 6, a decision-curve-style figure, shows the expected cost per verdict with the cost-minimising band, and that band, against the cost of a trial for each relation; Table S11 gives the cheapest rule for three ratios of false reject to false accept and five trial costs. Section 5.6 reports them {{loc:Pricing the verdicts by Eq.}}: as the trial cost falls from 0.5 to 0.01 of a false accept, the cost-minimising band of the nearest setting rises from 0 to 5 floors with a sibling and from 0 to 15 extrapolating (your figures: 0–4.5 and about 15); the 95 % bands correspond to trials costing a tenth to a quarter of a false accept. The trial rates are in Table 6.
- **False-accept side.** Table 5 gives the safe distances on the false-accept and the false-reject side for every rule and relation.
- **The trial as a reference.** Table 5 has two trial rows (the first 20 and 50 parts of the design's own run), and Section 5.6 states that this is a within-run lower bound and that a trial on another day also carries the variation between runs {{loc:A trial is not error-free either}}. Scored by the distances, the trials decide at 1.35 and 0.90 floors (your check gave 1.30 and 0.86 as 90th percentiles of the absolute error, the quantity the decisive distance approximates).
- **Decision set.** The introduction names it: process planning, the approval of process changes in series production and the qualification of AI-based tools, but not the tryout of a new die {{loc:The decisions in scope are those of process planning}}; the worked example is a process planner's decision {{loc:A process planner has to decide}}.

### R11. Writing for this journal's readers

- **Schematic.** Fig. 1 shows the verdict shares of one rule against the requirement distance with δd and δs marked, and the share correct among decided verdicts against the margin with g marked; Section 3.4 leads with the reading of the decisive distance as about the 90th percentile of the absolute error {{loc:In plain terms, for a rule that always decides}}.
- **Worked example** in Section 3.7, carried through steps 1–6 {{loc:Step 1 frames the decision}}.
- **Fewer rules.** The main text keeps eight rules with descriptive names (Table 2): M0 nominal simulation, M1s scaled simulation, M2 envelope, M5 GP-corrected envelope, NN nearest produced setting, M1sn force trend, M7n trend GP and NN+RM. The other rules are defined in Table A2 and Online Resource 1; M6 and the former Section 5.9 moved to Online Resource 1 (Tables S1, S2, S4). Each relation has one column block in Table 5.
- **Two new figures.** Fig. 3 shows the cups after drawing and cutting with the regions and directions of the characteristics, and Fig. 4 the batch centres over one run with the floor.
- **Terms.** "Sibling" names the relation and "new variant" the design; "nearest setting" is NN and "force trend" M1sn throughout; M3n is explained as M4 in the code (Tables A2, A7); $q_p$ is used throughout, with $p = 0.95$.
- **Dense paragraphs.** The guard-band paragraph is split into three (Section 3.6), with pseudocode for steps 5 and 6 {{loc:In pseudocode, step 5 is}}; the former Section 5.8 is split into guard bands (5.5) and costs, trials and release-level requirements (5.6); the incomplete sentence of l. 1009 is deleted.
- **Positioning.** Section 2 and Table 1 now engage with the reliance and global-similarity indices of automatic virtual metrology {{loc:Automatic virtual metrology goes further}} (a row in Table 1), regression with a reject option {{loc:as does regression with a reject option}}, transfer learning and domain adaptation {{loc:Models are carried across products and processes by transfer learning}}, uncertainty quantification in predictive quality {{loc:their uncertainty is quantified by Bayesian, ensemble and conformal methods}}, the validation and calibration of forming simulation (friction, springback, tool deflection, robustness, in-line draw-in control) and machine learning in sheet forming {{loc:In sheet forming, the friction law}}, and the global consumer's and producer's risks of JCGM 106 {{loc:the global consumer's and producer's risks follow from a prior distribution}}. The last paragraph of Section 2 says what is adopted and what is new {{loc:is the production-defined unit in which every rule}}.
- **Length.** See "Locations" above: the running text grew by about 5 %, and everything else moved to the appendix or Online Resource 1.

### R12. Archive and declarations

- **Licence. [author]** The code carries no licence yet. `RELEASE_NOTES.md` no longer refers to a missing `LICENSE` file; it states that the author adds the licence file and the licence field of the deposit metadata before the deposit is published. The choice of licence is the author's.
- **DOI. [author]** To be reserved or minted with the deposit of version 2 and inserted in `refs.bib` (`canseven2026archive`) and `CITATION.cff`; `paper/submission/make_zip.sh` warns while it is pending.
- **requirements.txt** now pins every package, including `tabulate` (0.10.0), `pyarrow` (25.0.1), `remotezip` (0.12.6) and `threadpoolctl` (3.7.0).
- **Table A7** maps `tuning.py` with `tune_decisions` (Section 5.4) and `measurement.py` with `meas_sim` (Section 4.2), and every script and result file added in this revision.
- **"As the repository history records"** is removed. Section 4.5 says that the constants were set before the decision results were seen, "which the archive cannot verify, as no timestamped snapshot was deposited at the time" {{loc:which the archive cannot verify, as no timestamped snapshot was deposited at the time}}.
- **Generative AI.** The declaration now says that the language model was used to write and debug code, retrieve and check literature, run analyses and draft text, and to simulate reviews of earlier versions in five rounds as referees and editor; that most rules and analyses added after the first results were added in response to these simulated reviews, naming them; and that none of these reviews is a review by a journal {{loc:It was also used to simulate reviews of earlier versions of the manuscript}}. Section 4.5 gives the same account with the full list. To our understanding of Springer Nature's policy (no AI authorship, use documented in the manuscript), the statement complies; the journal may have further requirements, which we will follow.
- **ISO editions.** The cited editions are correct and current, and the reviewers know their predecessors: according to ISO's open-data deliverables metadata, ISO 5725-2:2025 (edition 3) was published on 18 December 2025 and replaces ISO 5725-2:2019, and ISO 22514-2:2026 (edition 3) was published on 6 February 2026 and replaces ISO 22514-2:2017. `refs.bib` records this next to each entry. The repeatability limit is now cited to ISO 5725-6 as well, which gives the computation of the limits.
- **PPAP.** Corrected in Section 2.4 {{loc:in an initial process study an index above 1.67 meets the acceptance criteria}} and Section 5.6: for an initial process study, an index above 1.67 meets the acceptance criteria and one between 1.33 and 1.67 may be acceptable after a review by the customer (the PPAP manual, 4th edition, calls for a review by the customer's authorised representative rather than approval); 1.33 is cited as a recommended minimum for existing processes (Montgomery), since the PPAP manual itself does not state the criterion for ongoing capability.

---

## Part 2. Recommended changes

| Recommendation | Adopted? | What and where |
|---|---|---|
| Few-shot transfer to a new family | Yes | One to three produced alternatives of the target family, with and without the other family's record: the nearest setting within the target family, the other family's record shifted by the median offset, and a two-task GP with a free inter-family correlation (with and without the simulation) {{loc:With one produced alternative of the new family}}; Table S16. One produced alternative of the new family brings its decisive distance from 28 to 9 floors in its own floor; the two-task GP is safe at 1.3–1.6 floors but decides only at 13–17. |
| Multi-fidelity modelling and calibration with discrepancy | Yes | M7 (autoregressive, fitted scale and GP discrepancy) and Mcd (Kennedy and O'Hagan 2001 with Higdon et al. 2004 and Brynjarsdóttir and O'Hagan 2014 cited for the need of a discrepancy term); see R4. |
| Interval methods | Partly | Interval score (Gneiting and Raftery 2007) for every interval rule (Table S4); M6's guarantee and its cost in decisiveness discussed {{loc:computed on sibling-type residuals, covers 93}}. Conformalised quantile regression on the parts is not added: calibrated within the calibration set, its residuals would again be sibling-type, which is the mismatch that the relation-matched intervals address; it is named as a next candidate {{loc:conformalised quantile regression on the parts}}. |
| Design-level verdict | Yes | A design meets only if all seven characteristics meet {{loc:Requiring all seven characteristics of a design to meet}}; Table S14. The production-record rules lose at most 1.8 floors within a family, M5 up to 16. |
| Lower or two-sided limits | Lower limits | Lower limits on the 5th percentile of the draw-ins, the wall angle and the depth (Table S2): the nearest setting stays within 0.4 floor of its reference distance with a sibling. A draw-in window is the conjunction of an upper and a lower verdict and is scored like the design level; it is not added as a separate analysis. |
| Attribute outcomes | Yes | A paragraph on scoring a requirement on a rate {{loc:A requirement on a rate, such as the share of split or wrinkled parts}}. |
| Data from the RDDAC providers | Prepared **[author]** | A request for the production and scanning log, verification data, tooling and material data and the open simulation settings is drafted (`paper/submission/note_to_dataset_authors.md`) for the author to send. The paper states what the documentation leaves open {{loc:and gives no material certificate, coil record, tool drawing}}. Sub-pixel edge estimation of the flange width is not added: it needs a re-extraction of all 9,000 scans, which streams the raw data again; the quantisation it would remove is reported (0.38 floors, 6–21 values per series). |
| Simulation inputs | Partly | The envelope over the measured incoming variation is scored (M5 with a sibling 24 instead of 7.2 floors) {{loc:An envelope over the measured incoming variation}}; Table S2. The flow-curve factor cannot be added: the dataset varies it only for other tool geometries, and all 396 simulations of the RDDAC tools use the nominal flow curve {{loc:all with the nominal flow curve}}. New simulations with friction per pressure level are outside this work. |
| Capability and short runs | Yes | The decided statistic m̄ + 4σ (a performance index of 1.33 at the limit) and calibration and truths from the first 20 or 50 parts (Table S2): the nearest setting stays within 0.4 floor with a sibling and 1.2 extrapolating. |
| An actual AI tool | No | Scoring a language-model check or a model pre-trained on the DDACS geometries would need a protocol of its own (Section 6.4) and would add a second exploratory selection to this one; the paper presents it as a proposal and the frozen procedure leaves room for it as a secondary rule. |
| A reusable checklist and scoring function | Yes | Table 8, modelled on model cards and TRIPOD+AI, with item, why it matters and where this paper reports it, including the five items Reviewer 3 listed; `scripts/opchar.py` is the scoring function on its own, with a self-check that reproduces `dec_resolution.csv` {{loc:the scoring is released as a small documented function}}. |
| Deployment | Yes | Section 6.5: the interface of a step-6 verdict, monitoring by a control chart of decision outcomes with re-qualification criteria, the cost of the evidence, and the planned user study {{loc:In use, a step-6 verdict would be shown}}. |
| Pre-registration | Prepared **[author]** | The frozen procedure, with the data a confirmatory set needs, the fixed constants and rules, six hypotheses and the analysis plan, is drafted in `paper/notes/frozen_procedure.md` for the author to register before any confirmatory data are analysed. |
| Minor comments | Yes | Parts 4–6. |

---

## Part 3. Your qualifications of the reports

1. **Breadth of new learners.** Understood. We added the required learner (M7n) and the crossing, and of the recommended ones only those that needed no new data (M7, Mcd, few-shot transfer, interval score); each is marked as added in this revision, and the cross-fitting covers the larger rule set.
2. **Details of the GP collapse.** Agreed. Section 5.4 states "at its bound in every fit" only for the new setting; with a sibling the share is 97–99 % (`dec_gp.csv`), and Table A3 gives the median ratio of the fitted noise to its bound by relation. The mechanism you describe (the noise bound absorbing the trend, whatever the length scale) is why M7n replaces the hard bound by an estimated nugget.
3. **The short trial.** Agreed: the trial appears only as a within-run lower bound, with the statement that variation between runs adds to its error.
4. **What the paper reported about the scanner.** Agreed. Table 3 gives the cut-wall difference as the series medians you computed (3.3–5.6°).
5. **Grid and oil film.** Both corrections are in the text: at 300 kN the concave mid-side draw-in is reached "only at the edge of the grid", and the oil-film result carries the attenuation caveat and compares with the between-pattern slopes rather than only the within-run slope.
6. **Data from the providers and new simulations.** The paper says what is unknown (R4, R5), and the request is prepared.
7. **Moving bands between geometries.** Agreed; the 83–84 % is reported as a check of per-family estimation, not as a procedure.
8. **Deployment.** The claims of usefulness and of a standard are removed; Section 6.5 describes deployment as future work.
9. **Fit to the journal.** R3 and R11 are addressed in that spirit: the learned rules get a fair test with a well-specified small-data learner, multi-fidelity and discrepancy models and relation-matched intervals, and the paper now speaks to developers of AI-based manufacturability tools {{loc:For a developer of an AI-based manufacturability tool the lesson is methodological}}.

---

## Part 4. Reviewer 1

Thank you for the careful report, and for the in-memory refits that pinned down the GP collapse.

**Major 1. The learners reduce to the baselines.** Agreed, and now shown and tested.
- (a) Table A3 shows the hyperparameters and the centre equivalences by relation (R3a).
- (b) M7n is the GP with an explicit linear mean whose coefficient uncertainty is propagated, weakly informative priors tied to the design spacing and an estimated nugget (R3b). It reduces to the force trend, as a well-specified model must with two or three force levels, and Section 6.3 says why {{loc:The learners failed for a reason the framework exposes}}.
- (c) Prediction and interval are crossed (Table A4; R3c). An interval can be put around NN without any learning, and NN+RM is now a main rule.
- (d) The tuning study is reported (R3d).
- (e) RQ3 is phrased in terms of model classes and the data regime (R3e). The remark that NN is a nearest-neighbour regressor and M1sn ordinary least squares is taken: the paper now calls them production-record rules, not rules without learning.
- On safety: the smaller safe distances of M5 and M5n with a sibling are now priced (Fig. 6, Table S11). The cost analysis shows them buying safety with trials: with a sibling the nearest setting is the cheapest rule once a trial costs a tenth of a false accept or more.

**Major 2. Multi-fidelity, calibration, transfer, physics-informed.**
- (i) M7, an AR(1) multi-fidelity GP with a fitted scale and a GP discrepancy, is added (R4); Le Gratiet and Garnier (2014) and Perdikaris et al. (2017) are cited.
- (ii) Mcd, a calibration with a discrepancy term in the line of Kennedy and O'Hagan (2001) and Higdon et al. (2004), is added; Mc is described as a least-squares fit without the citation.
- (iii) The few-shot experiment with k = 1–3 compares the nearest setting within the target family with an intrinsic-coregionalisation GP with a free inter-family correlation (Bonilla et al. 2008) and family intercepts with shared slopes, with and without the other family's record and the simulation (Table S16).
- Physics-informed learning (Karniadakis et al. 2021) and sim-to-real transfer in manufacturing (Tercan et al. 2018) are discussed {{loc:also from simulation to real parts}}; shape constraints are not tested, but the result that a well-specified model becomes the linear force trend bounds what monotonicity could add with two or three force levels.

**Major 3. Uncertainty quantification.**
- (i) M7n estimates the noise from the known sampling variance of each truth plus a between-run nugget under a prior, not a hard bound, and reports the nugget relative to the sampling error (Table A3). M5 and M5n keep the bound, which is now named and reported relative to the fitted noise.
- (ii) Cluster-robust coverage per characteristic and per decision-time stratum (Tables S4, S5; R6).
- (iii) Relation-matched, group-conditional split-conformal intervals borrowed across the two families (Vovk et al. 2005 cited), with the statement that their guarantee needs exchangeability of the two families' errors, which the data cannot establish (Barber et al. 2023 cited) {{loc:which the data cannot establish}}.
- (iv) The interval score is added (Table S4).
- (v) Conformalised quantile regression is not added; see Part 2.
- (vi) M6 is discussed: its margin costs about ten floors of decisiveness with a sibling (17 against 7.2) and covers 93 % there, but only 61 % extrapolating, because its residuals are sibling-type.

**Major 4. Selection on the evaluation data.**
- (a) The exploratory status is in the abstract and the conclusions.
- (b) Tables 2, 5 and A2 mark the post hoc rules.
- (c) The selection is cross-fitted; the ranking survives (R8).
- (d) The band is estimated leaving one alternative out (and one force cell out), with intervals and trial rates (Table S8).
- (e) The abstract quotes the nearest setting, a rule committed to in advance (R8).
- (f) The frozen procedure is drafted for registration **[author]** (Part 2).

**Major 5. Pooling seven characteristics.** Per-characteristic distances (Tables A5, S15) and per-characteristic guard-band accuracy (Table S10) are reported, with bands per class of characteristic (process indicators, drawn geometry, cut part); the design-level analysis is added (Table S14). The δ-dependent composition of the failing side is now handled by reporting the safe distances on the false-accept and the false-reject side separately for every rule (Table 5) {{loc:the safe distances on the false-accept and the false-reject side are therefore reported as well}}. Step 5 can qualify per characteristic, as Table 7 ("Qualifying a rule") now says.

**Major 6. Uncertainty of the distances.**
- The refitting bootstrap, the between-run sensitivity and the fixed-fit resampling are each described with what they represent (R6). A hierarchical model of the exclusion distances is not fitted: with 18 alternatives in two families it would rest on its priors.
- The between-run component is added as a sensitivity (R6).
- The minimum difference the design resolves is stated (about ±2 floors between point rules with a sibling and extrapolating; Table S17).
- Paired intervals are labelled descriptive. Bates, Hastie and Tibshirani (2024) is cited {{loc:like any cross-validated estimate, the distances describe the fitting procedure}}.

**Major 7. Title, contributions and scope.** Retitled; classifiers and language-model checks are a proposal; lower limits are added (Table S2); attribute outcomes have a paragraph; the guidance block of Table 7 is worded as observations of this study (R1).

**Major 8. Presentation.** The abstract is rewritten with five numbers; Fig. 1 is the conceptual figure you asked for; the main text keeps eight rules; Table 5 is one compact table with a column block per relation; the GP bound is renamed; M3n is explained as M4 in the code (R11). A new family is now scored in the produced family's floor in the main tables and in its own floor only in Table S1.

**Minor comments.**
1. Every characteristic is scored in the floor of its own geometry; the pooled floor serves only to convert distances to physical units {{loc:and the pooled floor serves only to convert distances to physical units}}.
2. Leakage of the floors. Recomputed: with every case scored in the floor of its geometry computed without its own alternative's series, the floors change by factors of 0.70–1.08, and the distances of the nearest setting and the force trend move by at most 0.25 floors and those of the other main rules by at most 1.4 {{loc:floors recomputed without the held-out alternative's own series}}; Table S2 (`qual_floor_loao.csv`). The nominal thickness is the grid value nearest the median thickness of all parts; since the grid steps are 0.01 mm and the series medians span 0.986–0.993 mm, leaving one series out cannot change it.
3. The number of calibration alternatives per relation (8, 6 and 9) is given in the note to Table 2, with the guaranteed level of each interval rule in Table S4.
4. Both one-sided distances are in Table 5 (FA/FR), and Section 3.4 explains the δ-dependent weight of the failing side.
5. Section 4.4 now says that the jointly held-out alternatives of a new setting are resampled individually and that each resample draws a block-bootstrap replicate of every truth (non-overlapping blocks of 50 parts) {{loc:those held out together for a new setting individually}}. Nine alternatives per geometry allow 24,310 distinct resamples per geometry.
6. The pooled columns moved to Table S1, whose description says that M1n, M2n and M1sn have no family term there.
7. The coincidence at 300 kN is stated {{loc:the centre of M5n coincide by construction}}.
8. The 165-floor false accept is attributed to the cup depth (R9).
9. The decomposition is restricted to the pre-specified rules and presented as descriptive (Table S17).
10. The sentence is replaced; the coincidence of the M5 and M5n centres with NN is stated (R3).
11. Table S4 gives cluster intervals, the coverage of M6 and the interval score.
12. The sentence is deleted.
13. Virtual metrology, regression with a reject option, predictive quality and transfer learning are now in Section 2 and Table 1 (R11).
14. (a)–(b) Licence and DOI **[author]** (R12). (c) `requirements.txt` fixed. (d) Table A7 maps `tuning.py`. (e) The statement is removed (R12).
15. The new Fig. 5 shows three rules in larger panels, with tick labels at ±10 and ±100 and the near-replicate strata in Table S3.
16. Fig. S4 gives the curves behind the bands, for the rules of the main text, and marks each band with a larger marker. The number of decided verdicts behind each point is not printed; the uncertainty of the share correct at each band is quantified by the out-of-sample intervals of Table S8.
17. The cost model is Eq. (2), Fig. 6 and Table S11.
18. ISO 5725-6, which gives the computation of the repeatability and reproducibility limits, is now cited with ISO 5725-2 for the repeatability limit; we give no clause numbers, which we could not check against the current editions.
19. "Proposed reporting checklist" (Table 8).

---

## Part 5. Reviewer 2

Thank you for a report that grounded the unit, the measurement and the simulation in forming and quality practice, and for the checks you ran on the feature tables.

**Major 1. What the floor contains.**
- (a) The request to the providers is drafted **[author]**; the paper states what the documentation leaves open.
- (b) The tooling reference is reported (R5), with a plain statement of what remains untestable.
- (c) The physical candidates are discussed, blank size included {{loc:which enters the draw-in one to one because it is computed against the nominal 210}}. The series start temperatures are in Section 4.1.
- (d) The unit is renamed the within-run floor and called a production-and-measurement floor where the two are not separated (R5).

**Major 2. One run per alternative.**
- (i) The single-run floors and the cluster interval are in Table 4; A2 is no longer stated without this qualification.
- (ii) The between-run sensitivity spans near-replicate reproducibility to the between-series bound (R6); distances below one floor are reported as "<1".
- (iii) The link to capability is made: the floor in long-term standard deviations (Table 4), the performance index of a requirement at the decisive distance (Table A5) and the capability-anchored limits of Section 5.6. Pooled, your reading holds: an index of 2.0 lies a median 3.14 floors above the 95th percentile, about the nearest setting's 3.4 floors with a sibling; per characteristic, the index at its decisive distance ranges from 0.9 (waviness) to 4.0 (dome).
- A variant with a capability statistic is added (m̄ + 4σ, a performance index of 1.33 at the limit; Table S2).

**Major 3. Characteristics and measurement uncertainty.**
- The measurement subsection and the table of characteristics are added (R5). "Along/across the scan lines" is replaced by "along the laser line" and "in the direction of motion".
- The systematic errors are reported with their magnitudes (Table 3, Table S20); the residual bias of the directions kept is unknown, and the paper limits absolute comparisons with the simulation accordingly.
- The quantisation of the mid-side draw-in (0.019 mm, 0.38 floors, 6–21 values per series, five zero standard errors) is reported {{loc:The mid-side draw-in is quantised in steps of 0.019}}; sub-pixel edge estimation is not added (Part 2).
- The operation measured is stated and justified (R5); the wall angle and depth are no longer called characteristics "a drawing would carry".
- A3 is now stated as holding "for repeatability and resolution, while bias, linearity and stability remain untested" {{loc:while bias, linearity and stability remain untested}}.

**Major 4. The simulation set-up.**
- (a) The grid's failure to contain the process and the censoring of Mc are reported (R4), with your numbers and the editor's correction at 300 kN.
- (b) The oil-film mapping is tested (R4).
- (c) The envelope over measured incoming variation is scored (Part 2). It halves the envelope's width but makes M5 less decisive, because through the mapping it then varies with the lubrication pattern more than production does.
- (d) The extraction noise is reported (Table A6) and the simulation comparison given per characteristic (Tables A5, S15).
- (e) The depth offset is reported as unexplained with the mechanisms checked (R4).
- (f) The diagnostic discrepancies are stated: the convex arm angles agree within 0.6° {{loc:whereas the convex arm angles agree within 0.6}}; Section 6.3 names pressure-dependent friction, a hardening model fit for springback (Wagoner et al. 2013) and elastic tools (Pilthammar et al. 2018), and Section 4.2 lists what the DDACS documentation gives (rigid tools, shell elements with seven integration points, constant Coulomb friction) and leaves open.
- The abstract, Sections 5.2 and 6.3, Table 7 and the conclusions state that the simulation is an uncalibrated generic dataset and that a process-calibrated simulation might contribute more within a family {{loc:might contribute more; the per-characteristic results show where it already helps}}.

**Major 5. The decisions modelled.**
- (a) The decision set is framed (R10); tryout is excluded.
- (b) The trial is scored as a rule, as a within-run lower bound (R10; your 1.3 and 0.9 floors reproduce).
- (c) Truths and calibration from the first 20 or 50 parts are tested (Table S2): the nearest setting with a sibling moves by less than half a floor. The floor itself still needs ten batches, as Section 6.4 says {{loc:here nine produced alternatives per family and 500-part series gave ten batches}}.
- (d) Trial costs from 0.01 to 0.5 of a false accept for every relation, three ratios of false reject to false accept, and the false-accept side reported separately (R10). Section 5.6 notes that the 95 % bands correspond to trials costing more than a new force on an existing tool costs.
- The worked example is kept as a release of a new blank-holder force, now framed as a process-planning decision; a draw-in window would add a lower limit, which the framework scores by a change of sign (Table S2).
- The findings that serve tryout are brought forward: the minimum resolvable force change (Section 5.2 and step 3 of the worked example) and the transfer of the produced family's wall-angle deviation (1.9 floors) {{loc:Production knowledge still carries over where a drawing nominal transfers}}.

**Major 6. Sibling strata.** Replaced by decision-time strata, with your figures (R2).

**Major 7. Scope.** The title and abstract are narrowed (R1); the abstract states the single laboratory process and the uncalibrated simulation dataset; the frozen procedure lists what a confirmatory dataset needs (several runs across days and coils, documented production and scan order, a reference artefact, more than two geometries); attribute outcomes have a paragraph.

**Major 8. Presentation and positioning.** Figures of the cups, the cut part and the measured regions (Fig. 3) and of batch centres over a run (Fig. 4); eight rules in the main text; the abstract rewritten; physical units per characteristic (Table A5); the M3n/M4 naming explained; Section 2 extended to forming validation, robustness analysis, in-line draw-in control and machine learning in sheet forming (R11).

**Minor comments.**
1. "95 % conformance" is gone; the abstract speaks of verdicts and distances, Section 3.1 of the 95th percentile.
2. The PPAP criterion is corrected (R12).
3. The warm-up is kept, "because series production starts up after every break" {{loc:keeps the warm-up because series production starts up}}; Table 4 gives the floor without it.
4. The envelope's ranges are stated (the dataset's thicknesses 0.95–1.00 mm and friction 0.05–0.15) and the flow-curve factor is not available at the RDDAC geometries (Part 2).
5. Section 3.4 says so in plain words (R11).
6. The material data, tool dimensions, press and cushion and the application of the lubrication patterns are not in the documentation, which Section 4.1 now says; the request asks for them. The oil-film medians of the three patterns are given.
7. The stroke speed is made concrete: the 100 kN series ran at 47 mm/s against 78–79 mm/s, "so the extrapolation to 100 kN also changes the sliding speed and stroke rate on which the lubricant film depends" {{loc:so the extrapolation to 100}}.
8. Section 4.2 reports what the DDACS documentation gives and what it leaves open {{loc:Its documentation gives rigid tools}}.
9. The simulation at the closest grid friction is in Table S18, with the residual there.
10. The block length is stated (non-overlapping blocks of 50 parts).
11. Table 4 (R5).
12. Worded as 95th percentiles of the centre differences, lubrication effects included {{loc:at the 95th percentile of their centre differences, lubrication effects included}}.
13. Added (Section 5.2).
14. The false-accept-side distance is in Table 5 for every rule; the M1s false-accept tail is in Section 5.3 and Section 6.1 {{loc:Qualification by relation also exposed a dangerous extrapolation}}.
15. Fig. 5 shows three rules in larger panels with distinct line styles for δd and δs.
16. The derivation of a team's prior from history is illustrated, and the grid of ±20 floors is given in physical units per characteristic {{loc:floors are about}}.
17. The ISO 2768-1 scenario is removed from the paper: it could not discriminate within a family (R10) and is replaced by the cost analysis; it remains in the archive (`scenarios.py`).
18. A paragraph on scoring a rate (Section 6.4).
19. Table A7 maps `meas_sim`; the content of `meas_scan` is in Table S20.
20. DOI **[author]**; pins fixed; ISO editions confirmed (R12).

---

## Part 6. Reviewer 3

Thank you for the report, and for checking the guard band out of sample, per geometry and per characteristic; those checks shaped R7.

**Major 1. The message is hard to reach.**
- (a) The schematic is Fig. 1.
- (b) The worked example is in Section 3.7 and runs through steps 1–6.
- (c) Section 3.4 leads with the 90th-percentile reading (R11).
- (d) Eight rules remain in the main text; M6, the surrogate details, the variance decomposition, the former Table 6 and most of the former Section 5.9 moved to Online Resource 1 or the archive.
- (e) The abstract has five numbers and ends with a finding.
- (f) Section 6.2 is "Implications for practice" {{loc:For a process planner or quality engineer the results say three things}}.
- The coined terms are introduced where they are used, the six terms of the former l. 075–083 no longer share one paragraph, the 40-line guard-band paragraph is split, and the names are harmonised (R11).

**Major 2. The guard band.**
- (a) Estimated per family (R7).
- (b) Validated out of sample, leaving one alternative and one force cell out, with intervals and trial rates (Table S8). Your figures reproduce: 0.945–0.99 leaving one alternative out under the reference prior; 0.83 and 0.81 for M2 and M5 leaving a force cell out.
- (c) The share correct per characteristic and per class of characteristic, and "the 95 % is an average over characteristics" in the text (R7).
- (d) The prior: band and trial rate against the width of the prior (Table S9), the release-like prior next to the reference, and the illustration of a prior from past drawing limits. We kept ±20 floors as the reference because a requirement set a few to some tens of floors from the 95th percentile is the common case far from release level; the release-like prior is reported throughout as the alternative for requirements near capability limits.
- (e) The former Table A4 is in the main text as Table 6. A curve of the band against the number of produced alternatives is not added: the subsets of k alternatives give few decided verdicts per relation for most k, and Fig. S3 already shows the distances against k.

**Major 3. Costs, trial rates and part-level verdicts.**
- The loss is introduced next to Eq. (1) (R10).
- Expected cost and trial rate are reported with the distances (Fig. 6, Tables 6, S11).
- A decision-curve-style figure (Fig. 6), for c_T/c_FA from 0.01 to 0.5 and c_FR/c_FA of 0.25, 0.5 and 1 (Table S11).
- One-sided distances in the main table (Table 5).
- A part-level (design-level) verdict is defined and scored (Table S14).
- The trial's own error is treated as a within-run lower bound (Table 5 and Section 5.6); the test-fidelity models of Thomke and Bell and of Salado and Kannan remain in Section 2.4 as the frame for a fuller treatment.
- The economic message has a number: "of 100 verdicts on new variants with a sibling the nearest setting with its band sends 2 to trial and gets at least 93 of the other 98 right; of 100 on extrapolated settings it sends 55 to trial" {{loc:of 100 verdicts on new variants with a sibling}}.

**Major 4. Claims and scope.**
- (a) Retitled and reframed (R1).
- (b) The abstract ends with a finding.
- (c) Section 6.4 is called a proposal; no AI tool is scored (Part 2).
- (d) The procedure is frozen in a draft for registration **[author]**, which states the protocol of the confirmatory test; the abstract states the exploratory status.
- On the sibling relation as a near-replicate test: the decision-time strata now separate near-replicate siblings (1.6 floors) from resolvable ones (4.4 floors), and the definition of the relation now says that the nominal simulation does not represent the factor that separates siblings {{loc:which the nominal simulation does not represent}}.

**Major 5. The unit.**
- Physical units and σ_LT (R9); the performance index of a requirement at the decisive distance (Table A5).
- Per-characteristic results in the appendix and Online Resource 1 (Tables A5, S15).
- The requirement grid in physical units (R9).
- Section 3.2 states that the within-run floor is a lower bound of the variation of series production {{loc:which makes it a lower bound of the variation of series production}}, and the between-run sensitivity says what it implies for future series.
- The floor between series is a robustness variant (Table S2), with the caveat that it is partly circular.

**Major 6. Reuse and checklist.**
- (i) The limitation for classifiers is stated: binning by the true margin needs a continuous, production-referenced outcome for every test design, which CAD-based datasets usually lack {{loc:which needs a continuous, production-referenced outcome for every test design}}.
- (ii) The language-model protocol now includes the model and version, the query date, decoding settings, prompt paraphrases, refusals and hedged answers as trials, monotonicity and a contamination test {{loc:reporting model and version, query date, decoding settings and prompt paraphrases}}.
- (iii) The incomplete sentence is deleted.
- (iv) Table 8 is a table modelled on model cards and TRIPOD+AI, with item, why it matters and where this paper reports it, and includes decision thresholds and costs, out-of-sample estimation of the band, per-characteristic results, case counts with the alternative as the unit of replication, and the development record.
- The scoring is released as `scripts/opchar.py`, which takes intervals, truths and floors and returns the distances, the guard band, the step-6 shares and the expected cost.

**Major 7. Positioning.** Virtual metrology with reliance indices (a row in Table 1), the global risks of JCGM 106 (Section 2.3, with the link to the prior-dependent band), domain shift and transfer learning, human–AI decision-making with uncertainty displays (Zhang, Liao and Bellamy 2020) and cost-sensitive evaluation (Elkan 2001; Vickers and Elkin 2006) are in Section 2 {{loc:Cost-sensitive evaluation}}; the last paragraph of Section 2 says what is adopted and what is new (R11).

**Major 8. Human–AI collaboration and deployment.** Section 6.5 specifies the interface of a step-6 verdict, a monitoring step with a control chart of decision outcomes and criteria for re-qualification (wrong decided verdicts above 5 % beyond chance, new runs' floors outside the range of the single-run floors, a reworked die), the cost of the evidence against the trials it saves, and the planned user study with cases of known outcome, outcome measures and the comparison of verdicts with and without the band {{loc:A qualification has to be maintained}}.

**Minor comments.**
1. "Learned 90 % intervals" is gone (R3e).
2. "Decision support" and "selective prediction" are added to the keywords; "conformity assessment" is not, because the six keywords allowed are taken.
3. The sentence is rewritten.
4. Each interval rule's guaranteed or nominal level is given (Table 2, Table S4).
5. The FA and FR sides are reported separately, and Section 3.4 explains the drift of the failing side's weight.
6. Section 3.4: "with 126 cases, some 240 verdicts, the 95 % threshold rests on about a dozen" {{loc:the 95\,\% threshold rests on about a dozen}}.
7. Split, with pseudocode (R11).
8. Fig. 2 (the procedure) has dashed input boxes for the produced alternatives, the simulations and the prior with the costs, and its text no longer runs into the borders.
9. Section 4.4 states that the units of replication are the 18 alternatives {{loc:but the units of replication are the 18 alternatives}}, and the Basis column of Table 7 gives alternatives, force cells and transfers.
10. The development record states that the reviews were simulated with a language model and which additions they caused, and the declaration says the same (R12).
11. Fig. 5 is a new, larger figure with three rules.
12. The scaled simulation's false accepts are in Sections 5.3 and 6.1; the abstract's limit of five numbers leaves no room for it there.
13. The decomposition is restricted to the pre-specified rules (Table S17).
14. The noise at its bound is stated where the coverage is discussed {{loc:its noise variance at its bound in every fit}}.
15. The tuning study is summarised and mapped (R3d).
16. Section 6.4 states the series length and number of alternatives used, and that one sibling sufficed and short runs reproduced the distance with a sibling.
17. Split into Sections 5.5 and 5.6, with Eq. (2), Fig. 6 and Table S11; the ISO 2768-1 scenario is removed.
18. Fig. S4 marks each band.
19. The Basis column gives alternatives and transfers, and the prescriptive rows mention costs ("by expected cost at the team's trial cost").
20. Section 6.2 makes the transparency of the nearest setting an explicit criterion {{loc:The nearest setting is also the most transparent rule}}.
21. Deleted.
22. Section 6.4 states what the PA12 data would have needed {{loc:a floor within a build would need at least ten replicated anchors}}.
23. The threats now include the guard band's pooling over characteristics, its reference prior, the marginal verdicts and the assumed costs {{loc:The guard band was estimated pooled over characteristics}}.
24. DOI **[author]**; ISO editions confirmed (R12).
25. Licence **[author]**; `RELEASE_NOTES.md` no longer refers to a missing file; pins fixed (R12).

---

Yours sincerely,

Hüseyin Tayyer Canseven
