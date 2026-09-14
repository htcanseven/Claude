# IEEE TEC rejection — analysis and revision plan

Working analysis of the reviewer feedback on *"Physics-Informed Diagnosis of Rotor Winding
Inter-turn Short-Circuit Faults in Synchronous Generators Using Stray Magnetic Field
Signals"* (Canseven & Şahin Sadık), rejected by IEEE Transactions on Energy Conversion.

## The short version

Twenty-five comments across the editor and three reviewers reduce to **four structural
problems**. Three are real, one is a self-inflicted formatting error.

1. **The benchmark is saturated.** Every model lands between 0.963 and 0.995 macro-F1 —
   an ℓ2 logistic regression ties a dual-head CNN. And the 607 files are really only
   **28 independent physical conditions** (7 operating points × 4 severities), resampled as
   20–30 near-identical 10-second recordings each. The experiment cannot resolve the
   difference it was built to measure, which is why both R1 and R2 said the novelty was not
   demonstrated. The paper half-concedes this already ("limited power of the paired test at
   near-saturated error rates").
2. **The physics is asserted, never measured.** The whole "physics-informed" claim rests on
   Eq. (4), `V(k·f_m) ≈ γ·K_k·I_f`, and on P18 failing *because* excitation current is low.
   **The field current is never reported for any operating point** — and it is not in the
   source dataset either (the 220 V / 3.5 A figures are nameplate ratings; the data report
   tabulates only apparent power and power factor). The central causal claim is unverified.
3. **The contribution is a known negative result.** "Physics-informed features beat raw
   deep learning" — R2 is right that this is already established. The severity calibration
   only lifts the CNN to a level three classical models already reached without it.
4. **Table IV / Fig. 6 silently switch denominators** — and this is what made R1 openly
   doubt the results.

### Problem 4 is fully resolved

R1 asked how 48 errors could beat 22, while 12 and 4 errors tie. **The numbers are correct;
the presentation is not.** Classical rows are over n = 607 files, CNN rows over
n = 1821 = 607 × 3 seeds:

- 48/1821 = **2.64 %** vs. 22/607 = **3.62 %** → the CNN really is better.
- 12/1821 = 4/607 = **0.659 %** *exactly* → identical rates, identical macro-F1.

Run `python3 tools/error_rate_check.py` for the corrected single-denominator table.

### Good news

- **Reviewer 3 recommended acceptance.** All of R3's points are editorial, about a day's work.
- A large share of the remaining comments is answerable **from the public dataset, with no
  new experiments** — tap wiring (J/J1/J2/J3), sensor photos (reusable under CC BY 4.0),
  the two-generator question, the P15–P21 numbering, and the full per-operating-point file
  inventory (which sums to exactly the 607 files used). See `analysis/05_dataset_reference.md`.

### The hard constraint

You have no physical access to the bench — the machine is at UFSC in Brazil. The two
requests that most directly drive the editor's "general applicability" objection cannot be
met from the released data at all: the finest tap is 20 % of one pole, and **all seven
operating points sit at 7.0 kVA**, so the loading axis is never explored.

## Recommendations

- **Do not appeal.** The editor's three grounds are each independently defensible, and R1's
  Fig. 6 question — which looks like reviewer error — is actually caused by the manuscript.
- **Email the UFSC/GRUCAD authors today.** R2 already told you to. It is the long-pole item
  and the only route to the per-operating-point field current that Problem 2 needs.
- **Reframe around the physics, not the benchmark.** The strongest available contribution:
  derive an *excitation–severity confounding index* from Eq. (4), compute it per operating
  point **before** training anything, and show it predicts which operating points fail. You
  already predicted P18 correctly — present that as a prediction rather than an observation.
- **Make the task harder** so the benchmark regains resolving power: sweep the number of
  source operating points (k = 1…6), sweep record length, add sensor perturbations. All
  free with data in hand.
- **Realistic horizon:** ~4 months for a strong TIE/TIA submission without new
  measurements; 6–8 months for a TEC-grade resubmission including FEM or new data.

## Contents

| File | What it is |
|---|---|
| `analysis/01_comment_triage.md` | All 25 comments, each with a verdict, concrete fix and effort estimate |
| `analysis/02_root_cause.md` | The four structural problems, with the fix for each |
| `analysis/03_revision_plan.md` | Strategy, venue options, work packages WP0–WP7, sequencing, go/no-go checks |
| `analysis/04_response_draft.md` | Draft point-by-point response text for resubmission |
| `analysis/05_dataset_reference.md` | Verified facts about source dataset [11], with citations |
| `tools/error_rate_check.py` | Reproduces the Fig. 6 resolution and the corrected table |

Two reviewer claims are **factually incorrect** and are handled without dispute in the
draft responses: R1-9 (the numbers are right, the presentation caused it) and R3-2b
(Table III *is* cited twice — but the underlying "needs more discussion" concern is fair).
