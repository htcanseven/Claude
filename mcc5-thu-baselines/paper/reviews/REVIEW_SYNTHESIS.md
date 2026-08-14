# Simulated pre-submission review — synthesis and action plan

Two independent reviewer agents read the complete manuscript source. Both
returned **Major Revision**, for largely convergent reasons — which is the
useful outcome: the convergent items are near-certain to arise in the real
review, so fixing them now is cheap insurance. Full reports:
`reviewer1_domain_expert.md`, `reviewer2_methodology.md`.

- **Reviewer 1** (condition monitoring / signal processing): 10 major,
  14 minor comments, 7 questions.
- **Reviewer 2** (ML evaluation methodology / statistics): 9 major,
  12 minor comments, 10 questions. Independently verified the
  trivial-baseline arithmetic and cross-checked every abstract number
  against the tables.

Both credited the same strengths: the prevalence floors, the session-confound
honesty, the leakage hygiene, and the appendix saturation result. Neither
questioned the paper's central message; both said the revision is fixable.

---

## Convergent majors (both reviewers — treat as certain to arise)

| # | Issue | Status |
|---|---|---|
| C1 | **Floor comparisons cherry-pick the weaker constant predictor.** Recall 0.630–0.694 vs the 0.667 three-constituent floor (exceeded only under recombination); R_all floor is 0.333 not 0.111; EM 0.083–0.157 does not clearly beat the 0.111 floor in most cells. Abstract, Contribution 2, and Conclusion all affected. | **FIXED tonight** — reworded to per-metric maximum floors and a joint-dominance claim (higher micro-F1 at comparable-or-lower FA); the cells where exceedance genuinely holds are now named. |
| C2 | **The 39% → 0.2% winding-suppression claim in Related Work is unsubstantiated in-paper.** | **FIXED tonight** — the modality-dissociation experiment (which used the appendix's own generic pipeline) is now reported in Appendix A and cross-referenced from Related Work. |
| C3 | **Code "on reasonable request" is inadequate for this paper**; R2 calls a public deposit *necessary for acceptance*; the timestamp metadata is load-bearing and currently behind the same barrier. | **DECISION NEEDED (you + Evin)** — the complete suite is ready; a GitHub+Zenodo deposit is ~an hour of work. My strong recommendation: do it. |
| C4 | **Crossed-split construction not reproducible from the text** (fold algebra, models fitted, unseen-condition cell definition, cardinalities per cell). | **EVIN** — needs pseudocode or a train/test cardinality table from her pipeline. |
| C5 | **Closed-set control underspecified** (classifier, features, window- vs run-level accuracy for the 0.913 headline; reconcile with the appendix's 0.939). | **EVIN** (her experiment) + I added the reconciling sentence to the appendix. |

## Reviewer 1's distinctive majors (physics)

| # | Issue | Status |
|---|---|---|
| R1-2 | Envelope/order processing chain ambiguous: envelope before or after 256/rev angle resampling; demodulation band policy; anti-aliasing. | **EVIN** — only she knows the code path; one methods paragraph. |
| R1-3 | Fixed ±0.12-order bands too narrow at second harmonics under roller slip (±1.1% at 2×BPFI). | **EVIN** — widen proportionally or show peak-location histograms. |
| R1-4 | Broken-bar features (o_e±1, o_e±2) are physically eccentricity/torque-oscillation signatures; proper (1±2s)f_e bands are computable from the key-phase channel. High broken-bar recall may rest on eccentricity-type evidence. | **EVIN** — sensitivity analysis or explicit confound discussion; also state pole count and line- vs inverter-fed. |
| R1-5 | Dataset/rig essentially undescribed (24 states, severities, seeding method, sensors, supply). | **SHARED** — I can draft the table from the dataset descriptor; Evin verifies. |
| R1-9/10 | AUC per-comparison n (~12 vs 12) should be stated; per-constituent precision/recall table missing; constructive current-only re-test of the reversal. | **EVIN** — outputs exist in her pipeline. |
| R1-7 | Contribution 5 promised documentation not in the paper. | **FIXED tonight** — contribution reworded to what the paper contains. |

## Reviewer 2's distinctive majors (inference)

| # | Issue | Status |
|---|---|---|
| R2-2 | **Cluster-level fragility**: 108 runs ≈ 9 compositions × 12 conditions, 7 recording dates; run-level clustering likely understates uncertainty; the headline interaction CI [0.0088, 0.0731] may not survive composition- or date-level bootstrap. | **EVIN** — the single most important robustness check before submission; if it fails, the abstract must be tempered. |
| R2-3 | No multiplicity control over the ~12-test contrast/interaction family; "prespecified/locked" carries no evidence. | **EVIN + BOTH** — designate primary metric/contrast, document when locked, FDR the rest. |
| R2-4 | Deprivation regimes confounded with training-set size. | **EVIN** — report per-cell training sizes; size-matched control or explicit acknowledgment. |
| R2-5 | **Session caveat applied asymmetrically**: the *positive* transfer AUCs and the closed-set 0.913 get no session hedge, only the reversal does. | **SHARED** — one symmetric-hedge sentence in Results (Evin's section) + I flagged it in the appendix reconciliation. |

## Minor items (both lists)

Applied tonight where they touch my sections: "every metric" softened in the
abstract; the interaction contrast identified (recombination vs two-sided);
cross-modal claim softened per R1-minor-2. Remaining for Evin/joint pass:
FA/row naming, ε values, threshold grid step, CI on directional recalls,
notation clash (𝒞 for composition and condition set), figure caption fixes
(Figs. 1, 3, 4, 5), bib in-press markers, MSCA foundational references
(Thomson & Fenger; Nandi–Toliyat–Li; Bellini; Randall & Antoni).

---

## Bottom line

Nothing in either review threatens the paper's central claim — both
reviewers explicitly said so. The work now splits three ways:

1. **Done tonight** (my sections): C1, C2, R1-7, abstract precision items.
2. **Evin's pipeline** (~2–4 days): the cluster-robustness check (R2-2, the
   single highest-priority item), split pseudocode + cardinalities (C4,
   R2-4), closed-set specification (C5), envelope-chain paragraph (R1-2),
   band-width or peak-histogram check (R1-3), slip-sideband sensitivity
   (R1-4), per-constituent table + current-only reversal re-test (R1-9/10),
   symmetric session hedge (R2-5).
3. **Joint decision**: public code deposit (C3) — both reviewers demand it;
   one calls it a condition of acceptance.
