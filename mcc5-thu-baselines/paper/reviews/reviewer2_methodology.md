# Reviewer 2 — ML evaluation methodology expert (simulated pre-submission review)
# Recommendation: MAJOR REVISION
# Note: reviewer verified the trivial-baseline arithmetic and cross-checked all abstract/conclusion numbers against the tables before writing.

## 1. Summary
Constituent-level evaluation of compound-fault recovery on MCC5-THU motor data (288 runs, 24 states, 12 conditions, 9 compounds): nine independent binary detectors over curated order-domain features, locked L2-logistic probe, training-only preprocessing, inner-CV threshold calibration; crossed protocol (recombination / one-sided / two-sided x seen/unseen conditions) on the same 108 compound runs; constant-predictor floors; difference-of-differences interaction (+0.040, CI [0.0088, 0.0731]); one Holm-supported score-orientation reversal, hedged given session separability (AUC 0.998); post-hoc threshold/severity/classifier-family analyses; appendix with a separate generic pipeline.

## 2. Strengths
1. Evaluation stance above the field's norm: run-level severity-aware splits, training-only calibration, explicit floors (arithmetic verified consistent), Holm over the 18 polarity tests.
2. Cross-modal compound setting is a real gap; positioning table honest.
3. AUC_dir / AUC_sep distinction exactly right; explicit that post-hoc inversion would require target labels.
4. Timestamp recovery and same-state nuisance control is the kind of self-undermining control most papers omit.
5. Post-hoc analyses clearly labeled, not used to re-select the locked model.
6. Appendix saturation result useful in its own right.

## 3. Major comments
**M1. Floor comparisons made against the weaker of the paper's own constants; several claims fail against the stronger one.** Against R_const floor 0.6667: probe recall exceeds only in the two recombination cells (0.6759, 0.6944), below in the other four (0.6296-0.6620). Against R_all floor 0.3333: two-sided unseen (0.3241) below, three cells barely above. EM (0.0833-0.1574) below-or-equal the 0.1111 floor in three of six cells, never stated. Sec 4.2 argues joint reading correctly; abstract, Contribution 2, Conclusion drop the qualification. Resolve: per-metric best-constant floors with bootstrap CIs on model-minus-floor differences; state EM indistinguishable from trivial in most cells (only F0.5/RF/MLP variants clearly exceed); reword to a dominance claim or restrict to cells where exceedance holds.

**M2. Bootstrap cluster choice (physical run) likely understates uncertainty; headline interaction fragile.** 108 runs = 9 compositions x 12 conditions, 7 recording dates; regime manipulations act at composition level; directional decomposition shows within-composition correlation. Effective n for composition-level effects ~9. Interaction CI [0.0088, 0.0731] barely excludes zero and could fail under composition- or date-level clustering. Resolve: sensitivity analysis at composition and date level; temper abstract/conclusion if not robust.

**M3. No multiplicity control over the contrast/interaction family; "prespecified/locked" unsubstantiated.** >=12 CI-based decisions besides the Holm-corrected polarity tests; several intervals marginal ([0.0000, 0.0509]; [0.0046, 0.1019]). Resolve: designate primary metric/contrast with evidence of when fixed; FDR the rest; label exploratory.

**M4. Context deprivation confounded with training-set size.** Two-sided removes far more data than recombination. Resolve: per-cell training sizes; size-matched control or explicit acknowledgment.

**M5. Session caveat asymmetric.** Positive transfer AUCs (median 0.905/0.884) and within-pair oracles (0.9167-1.000) face the same session confound in the favorable direction; closed-set 0.913 may partly be session identification. Resolve: symmetric hedge; one sentence on the closed-set figure.

**M6. Closed-set control underspecified for a headline number.** Classifier, features, window- vs run-level accuracy unstated; appendix 0.939 from a different pipeline sits confusingly close; reconcile.

**M7. Crossed splits not reproducible from the text.** Models fitted per what? Unseen-condition exclusion scope? Seen/unseen partition sizes? Pairing of the one-sided regime's two rows? The six scenario rows share test runs; needs fold algebra + one sentence on paired-only comparability.

**M8. "Code upon reasonable request" not acceptable for this paper.** Controls irreproducible without code; timestamp metadata load-bearing and behind the same barrier; authors' own source comment concedes the alternative. Public deposit necessary, not optional.

**M9. Unreferenced numbers in Related Work** (39% -> 0.2%). Report the experiment or remove.

## 4. Minor comments
1. Trivial table omits Active Macro-F1; "every metric" not literally true.
2. Abstract should identify the interaction contrast (recombination vs two-sided); R-O interaction unresolved for the same metrics, so "chiefly" is doing a lot of work.
3. FA/run misnomer in one-sided regime (216 rows); N reused for whatever subset.
4. Threshold grid step unstated.
5. Directional recalls without CIs.
6. "Resolved" nonstandard; define once.
7. Within-pair oracle training scheme belongs in Methods (only Results says "condition-held-out").
8. Bib: phme2025 key/year mismatch; gama2025/neuro2025 lack volumes (mark in press); verify song2025gzsl page field.
9. 0.843-0.731=0.112 reported as +0.111; make consistent.
10. Floors should be described as test-set-optimal constants (if they are — see Q5).
11. Equation numbering inconsistent with IEEE preference.
12. Remove (or act on) the Zenodo comment in main.tex.

## 5. Questions
1. What does "locked" mean procedurally; evidence (code history/protocol file)?
2. How many model fits; training cardinalities per cell?
3. Is the per-run one-sided value the mean of two directional rows; how is micro-F1 paired in the bootstrap?
4. Does the interaction survive composition- and date-level clustering?
5. Were the constants verified optimal over all 2^9 label sets per metric, or chosen by inspection?
6. Unseen-condition cells: held-out for all 24 states or only compounds; how many conditions per fold?
7. Closed-set 0.913: model, features, unit?
8. Polarity permutation: attainable minimum p before Holm; units of the "bootstrap interval below 0.5" criterion?
9. Were the 12 runs per composition acquired in a single session each?
10. Will code + timestamp metadata be deposited with a DOI?

## 6. Criteria
Technically sound: largely; inference-layer gaps (M2-M4). Methods valid: yes at high level; split construction and closed-set control not reproducible (M6, M7). Conclusions supported: mostly; floor-exceedance wording contradicted by the paper's own table in several cells (M1); interaction needs robustness (M2, M3); hedging on positive transfer and closed-set inadequate (M5). References: adequate. English: yes. Data: dataset yes; code/metadata no (M8).

## 7. Recommendation
**Major Revision.** Methodologically serious, framework a genuine contribution; reconcile headline claims with the paper's own baselines, show the interaction robust to clustering and multiplicity, make protocol and closed-set control reproducible, deposit the code — all fixable, none expected to overturn the central message.
