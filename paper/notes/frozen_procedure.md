# Frozen procedure for a confirmatory test (draft for pre-registration)

**Status.** Draft prepared with the revision for the *Journal of Intelligent Manufacturing*. It is not yet
registered: the author deposits it, with a timestamp, in a public registry (for example OSF Registries, or Zenodo
with the archive) before any confirmatory data are analysed. Everything below is fixed by this document; any
deviation will be reported with its reason.

## 1. Purpose

To test, on production data not used to develop the framework, the observations of the exploratory study (one
laboratory deep-drawing process, each alternative produced once, a generic simulation dataset), stated as the
hypotheses of Section 4. The framework, its constants and the rules are those of the paper and of
`scripts/opchar.py` at the archived release that this document cites.

## 2. Data a confirmatory dataset needs

- A design family with at least nine produced design–process alternatives covering a sibling relation (alternatives
  that differ only in a factor varied at a fixed setting), at least three levels of one process setting, and, for
  the new-family relation, at least two families sharing material and process.
- Series of at least 500 consecutive parts per alternative (ten batches of 50) for the floor and the truths, and at
  least two series of some alternatives on different days or coils, to estimate the variation between runs.
- Documented production and measurement order, and a reference artefact measured through the series, so that the
  floor can be split into process and measurement drift.
- A design-stage prediction (simulation or learned model) for every alternative, made without access to its
  production, and characteristics defined identically for parts and predictions.

## 3. Fixed constants and definitions

- **Decided statistic and requirements.** The 95th percentile of the parts ($p = 0.95$); one-sided upper limits
  $R = q_p + d\,F$ on the evaluation grid of the paper ($0$, $\pm0.5$ to $\pm10$ in steps of 0.5, $\pm12$, $\pm15$,
  $\pm20$, $\pm25$, $\pm30$, $\pm40$, $\pm50$, $\pm75$, $\pm100$, $\pm150$, $\pm200$, $\pm300$, $\pm500$ floors);
  infeasible requirements (negative limits on non-negative characteristics) dropped.
- **Floor.** Batches of $B = 50$ consecutive parts, centre the 10 % trimmed mean, batches with fewer than 80 % valid
  values dropped, all pairs of batches within a series, $\alpha = 0.95$; per characteristic and family; a new family
  scored in the floor of the produced family.
- **Distances.** Decisive distance: smallest $\delta$ beyond which at least 95 % of the feasible verdicts at
  $|d| = \delta$ are correct; safe distance: smallest $\delta$ beyond which at most 5 % are wrong; both on a 0.05-floor
  grid, with the distances on the false-accept and false-reject sides.
- **Relations and schemes.** Sibling: the alternative alone held out. New setting: all alternatives of one setting
  level held out (interpolated inside the produced range, extrapolated outside). New family: one family calibrates
  the rules for the other.
- **Rules.** NN (mean $q_p$ of the produced alternatives at the nearest setting level); M1sn (least-squares line in
  the setting); M1s (least-squares $a + b\,s_0$ on the nominal prediction $s_0$); M2 (envelope top plus median offset,
  largest-residual margin); M5 (GP offset with the noise-variance bound); M7n (trend GP with the priors of the paper);
  NN+RM (NN with the 90 % split-conformal quantile of NN's absolute errors on the same relation in another family).
  A rule not on this list may be scored but is secondary.
- **Guard band.** Reference prior: the grid within $\pm20$ floors, equal weights; release-like prior: within $\pm5$.
  Band searched in steps of 0.25 floors up to 20; smallest band beyond which at least 95 % of decided verdicts are
  correct. With a sibling, estimated from the family's own sibling cases and validated leaving one alternative out
  within the family, the predictions behind the band refitted without it; for a new setting, which a family
  produced at two setting levels cannot exercise, the band of the same relation in another family, validated on
  this family (shares reported per family). Stated costs only widen the band (step 5).
- **Costs.** $c_\mathrm{FR} = 0.5\,c_\mathrm{FA}$; trial costs $c_\mathrm{T}/c_\mathrm{FA}$ from 0.01 to 0.5.

## 4. Hypotheses (from the exploratory study)

- **H1.** With a produced sibling, NN decides at a distance no larger than that of M5 and of M7n (paired
  difference of decisive distances $\le 0$).
- **H2.** For an interpolated setting, NN and M1sn decide at least as closely as every interval rule (M2, M5, M7n).
- **H3.** For an extrapolated setting, NN+RM is safe within one floor while M5's safe distance exceeds three floors.
- **H4.** Leaving one alternative out, the guard band of NN under the reference prior keeps at least 93 % of the
  decided verdicts correct with a sibling and interpolating.
- **H5.** For a new family, no rule qualifies for single verdicts under the reference prior (no band up to 20 floors).
- **H6.** The prediction of a well-specified small-data learner (M7n) lies within one floor of the force trend for a
  new setting in at least half of the cases.

## 5. Analysis

- Distances and bands computed with `scripts/opchar.py` of the cited release, unchanged.
- Uncertainty: cluster bootstrap over alternatives within family (2000 resamples); paired differences between rules
  on common resamples; a hypothesis on a difference holds when its 95 % interval lies on the predicted side.
- Variation between runs: where replicated series exist, the truths of one series are scored against rules
  calibrated on the others, and the floor between series is reported next to the within-run floor.
- Per-characteristic results are reported for every hypothesis; pooled results are primary.
- Every result is reported, whether or not it supports the hypotheses, and every deviation from this document is
  listed with its reason.
