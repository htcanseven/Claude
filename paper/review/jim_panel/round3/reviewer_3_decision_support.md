# Referee report, third round: Reviewer 3

**Manuscript:** When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing
**Journal:** Journal of Intelligent Manufacturing
**Round:** Third round (second revision)
**Reviewer focus:** Industrial decision support: decisions under uncertainty, cost-aware decisions, human–AI collaboration and trust, and the deployment of AI tools in factories
**Date:** 24 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The author has done what I asked in the parts I said I wanted to see.

- **Table 7** (p. 20) now gives the guard band a team has when it decides, under both priors. With a sibling it is the family's own band, validated leaving one alternative out; for a new setting it is the other family's band.
- **Step 5** says when a band is borrowed and how stated costs widen it (L436–449).
- **The worked example** uses only what the planner knows (L452–473).
- **Section 5.6** labels the cost bands as in-sample and pooled, prices the trial's own errors and states the 47 % of failing designs.
- **Online Resource 1** (Tables S10–S13) holds the evidence for the deployed part.

The archive verifies. All 190 checksums hold, and `opchar.py --selfcheck` reproduces the distances, the 40 new-setting bands and the example's cost band. Four reporting errors remain. None needs new data.

## 2. My second-round points

**Major 1 (Table 7 and the worked example): resolved.** The following are in place:

- decision-time bands (Table 7; L914–917);
- borrowing (L437–440) and the convex band in the example (L463–467);
- the scheme and the verdict counts (S10);
- shares per characteristic (L921–923; S11);
- the within-run caveat (L923–926) and the band against the prior's width (S12).

Two descriptions are wrong (must-fix 1, 3).

**Major 2 (costs inside the procedure): partly resolved.** Costs now set the band (L440–441, L448–449), and the example follows (5.0 floors). The paper reports both priors and all cost ratios (S13), the trial's error cost (L950–955) and the 47 % (L955). But Fig. 6 and S13 are not computed under step 5's rule, and one restricted statement fails (must-fix 2). Declining out-of-sample cost bands and rarer failing designs is acceptable under C8.

**Major 3 (Online Resource): resolved** (S10–S13).

| Minor | Status | Where |
|---|---|---|
| 1 "committed to in advance" | Resolved | L034, L1023–1024, L1185 |
| 2 Mcd in Table 5 | Resolved | p. 18, L796 |
| 3 "93 of 98" | Resolved | L1041–1043; dome 89 % at L921–922 |
| 4 assumed prior | Resolved | L1181 |
| 5 cross-fitted step 6 | Resolved | L1000–1002; S15 |
| 6 monitoring, participants | Resolved | L1140–1154 (optional 4) |
| 7 Table 9 items | Partly; accepted | guard-band row only (p. 25) |
| 8 `opchar.py` checks | Partly; accepted | bands and cost band; no grouped validation |
| 9 density | Partly; accepted | L868–910 and L992–1012 still about 25 numbers each |
| 10 figures | Partly; accepted | Fig. 6 caption (L985–986) |
| 11 forward reference | Resolved | L453 |
| 12 trial-cost claim | Resolved | L949 |
| 13 threats | Resolved | L1169–1171 |

## 3. The editor's required changes in my area

- **C4: met in substance.** What is in place:
  - Table 7 is the decision-time band, validated by the matching scheme under both priors, with trial rates and verdict counts (S10).
  - Step 5 and Tables 8 and 9 agree with it.
  - Section 5.5 reports the release-like failures, the worst characteristics and the within-run caveat; S12 gives the band against the prior's width.

  Two things are missing: for a new setting the share is pooled over the families and has no interval (must-fix 1), and the force-cell scheme is mis-described (must-fix 3).
- **C5: met.** The floor of 0.041 mm, the 40 kN, the convex 5.3/2.5 floors with the caveat, the cost band, the quantisation and the margin of 7.4 floors all reproduce from `qual_worked_example.csv`.
- **C8: partly met.** The labels, the error cost of 0.017/0.037, the 47 % and the assumption are in place. Consistency with step 5 is not, and one statement fails (must-fix 2).
- **C9: met** (L034, L631, L999–1002, L1173). I checked 18.15/11.45 and 0.92–0.97 against `qual_crossfit.csv`.
- **C10: met.** Online Resource 1 is restored, the main text still ends on p. 27 of 31, and the archive has the data dictionary and a separate `findings_history.md`.
- **C11 (my items): met** (L1041–1043, Table 5, L1181).

## 4. New issues

### Must fix

1. **For a new setting, Table 7's "Correct" is pooled over the two families, and for most rules one family falls below 95 %** (p. 20; L917–918, "in each relation"). The bands are per family, but each share is summed over both families.
   - Under the reference prior, the borrowed bands give:
     - NN: 97 % on the concave cup and 93 % on the convex cup interpolating, and 92/100 % extrapolating;
     - M7n: 99/92 and 98/93 %;
     - M5 interpolating: 91/99 %.

     Sources: `qual_guard_family.csv` (`correct_*_with_other_band`), reproduced with `qualify.verdict_outcomes`.
   - A team on the convex cup that borrows 1.5 floors therefore gets 93 %. That is the 0.92–0.94 that Section 5.7 already reports for the cross-fitted step 6.

   *Fix:* give these shares as concave/convex pairs, as for g, and replace "in each relation" (L918) with "pooled over the families". In the S10 note, say that each share rests on one held-out cell per family (interpolated) or two (extrapolated), which is why it has no interval.

2. **The costs are not computed under step 5's rule, and L938–941 is wrong as stated** (p. 21; Fig. 6; S13).
   - Step 5 lets costs only widen the 95 % band (L440–441), but `qualify.costs` searches bands of 0–40 floors without that floor.
   - From a trial cost of about 0.1, the cheapest NN and M1sn bands fall below their 95 % bands, to none at 0.3–0.5. Extrapolating at c_T = 0.5, that means false accepts on 10–20 % of verdicts. Rules without any 95 % band, such as M0, are ranked as well (`qual_costs.csv`).
   - Hence, under the release-like prior at c_T = 0.2 and c_FR = 0.25, M0 is the cheapest option for an extrapolated setting (0.163 against M1sn's 0.174), as S13 itself prints. That contradicts "the nearest setting or the force trend is the cheapest rule at every trial cost".
   - Recomputed in memory with every band held at or above its 95 % band:
     - with a sibling, NN is cheapest from c_T = 0.1;
     - for a new setting, NN or M1sn is cheapest at every trial cost;
     - for a new family, no rule qualifies.

   *Fix:* recompute Fig. 6 and S13 under step 5's rule, which also shortens L943–946. Otherwise, label both as unconstrained and add the M0 exception at L941, paid for by shortening L945–946.

3. **The "force cell out" scheme is mis-described**, at L929–931, in the S10 note, in Section 5 of Online Resource 1 and in the `scheme` entry of `DATA_DICTIONARY.md`.
   - `qualify.guard_out_of_sample` removes the held-out geometry–force cell from the cases of both families.
   - Interpolating, this leaves only the other family's cell. M5's 0.88 and M7n's 0.87 are therefore Table 7's own values (0.875 and 0.867 in both files).
   - Extrapolating, the band pools three cells, two of them from the other family.
   - NN+RM is 0.7345, i.e. 0.73 as S10 prints, not 0.74.

   *Fix (same length):* "a band pooled over the other three extrapolated cells gives the nearest setting and NN+RM 0.72 and 0.73; interpolating, the borrowed bands give M5 and M7n 0.88 and 0.87".

4. **Section 6.2 gives the release-like trial rates without the share correct** (p. 23, L1043–1044). Of 100 extrapolated verdicts under the release-like prior, 8 are decided, and only about 6 of those are right (`qual_guard_decision.csv`: 7.9 % decided, 0.748 correct). A planner would read "92 to trial" as the price of a 95 % band.

   *Fix:* add "and only 6 of the other 8 are right", paid for by deleting the trial rates that L928 repeats from Table 7.

### Optional

1. L923–926: say that 0.25, 2.0 and 7.0 are in-sample bands pooled over the families (S14), not Table 7's.
2. Fig. 1 caption: g = 3.25 is M7n's pooled in-sample band (S12), not Table 7's 4.75/2.75; say so.
3. L438 and the step-5 box of Fig. 2: write "a new setting", not "interpolation", since Table 7 also borrows the extrapolation bands.
4. L1141–1144: a chart that sees false accepts only tracks their share among accepted designs, not "wrong decided verdicts"; the 150 is one-sided (185 two-sided).
5. L458: replace "a short press run" with the false-reject cost behind the 5.0-floor band (half a false accept; `qualify.worked_example`).

## 5. Checks I ran against the archive

All checks were read-only (`python3 -B`, scripts outside the repository, no pipeline script; `git status` left clean).

| Claim | File or method | Verdict |
|---|---|---|
| Integrity; scoring function | `sha256sum -c SHA256SUMS` (190), release-note hashes; `opchar.py --selfcheck` | All verify; distances, 40 bands, cost band reproduced |
| Table 7, both priors | `qual_guard_decision.csv` | Reproduced; "Correct" pooled |
| Per-family shares, borrowed bands | `qual_guard_family.csv`; `qualify` in memory | 0.92–0.94 in one family (must-fix 1) |
| Sibling band strictly at decision time | NN without the decided alternative in its siblings' predictions | 0.955/0.952 correct, trials 2.6/52 % (stored 1.7/41 %): confirmed |
| Force cell out | `guard_out_of_sample`; `qual_guard_oos.csv` | 0.718, 0.7345, 0.875, 0.867; pooled (must-fix 3) |
| Worst characteristics; τ = 3 | `qual_guard_decision.csv`, `qual_between_run.csv` | 0.888/0.883/0.853; 2.875/4.0/8.875 (pooled): confirmed |
| Worked example | `qual_worked_example.csv` | All numbers; 0.970 on the concave cup: confirmed |
| Cheapest rules | `qual_cost_cheapest.csv`, `qual_costs.csv` | M0 exception; bands below 95 % (must-fix 2) |
| Cheapest under step 5's rule | `qualify.verdict_outcomes`, bands ≥ 95 % band | Sibling and new-setting statements survive |
| Thousandths; trial cost; failing share | `qual_costs.csv`, `qual_trial_cost.csv` | 0.0034; 0.0171/0.0374; 0.474: confirmed |
| Release on m̄ + 4σ; trial under τ; cross-fits | `qual_release_capability.csv`, `qual_between_run_trial.csv`, `qual_crossfit.csv` | 3.35/10.55; 2.10/3.55/5.10; 0.92–0.97: confirmed |
| Section 6.2; 150 verdicts | `qual_guard_decision.csv`; normal approximation | 0.954 (0.936–0.971), 58, 41/92; 149: confirmed; 0.748 omitted |
| Licence, DOI | repository, `CITATION.cff`, `.zenodo.json` | Absent (the author's action) |

## 6. Recommendation

**Accept subject to the conditions.**

Table 7 now shows bands a team could have when deciding, which was the condition for avoiding another round. Step 5, the worked example and Tables 8 and 9 are consistent with it.

The first condition is the four must-fix items. They are reporting errors in Table 7 and Sections 5.5, 5.6 and 6.2. Each can be corrected from existing files or by relabelling, and none changes a finding: under step 5's rule the cost conclusions survive. The editor can check the corrections against the files named above without another review.

The other conditions are the author's own actions outside the manuscript:

- a licence for the code, with the licence fields in the deposit metadata;
- a minted DOI, cited in the paper;
- a timestamped deposit of the procedure.

## 7. Confidential comments to the editor

The revision answers my second round in substance. Must-fix items 1 and 2 matter most for practitioners.

- A "95 %" that is 97 % on one family and 93 % on the other hides the uncertainty of borrowing from a single family.
- Cost rankings built on bands that step 5 forbids describe a different procedure from the one the paper recommends.

Both are corrections, not new analyses: the per-family shares are in a version-2 file, and the cost conclusions hold under step 5's rule.

The mis-described scheme partly echoes C4 and my own round-2 wording, which listed the interpolating values under "force cell left out".

The licence, the DOI and the registration remain prerequisites for acceptance.
