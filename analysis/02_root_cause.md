# Why this paper was rejected — the four problems underneath the 25 comments

The editor's three sentences are the decision. Everything the reviewers wrote maps onto
them:

> "the novelty and added value of the proposed approach are not sufficiently demonstrated"
> "the experimental validation is not sufficiently comprehensive"
> "important methodological details required for reproducibility remain insufficiently documented"

Individually, most of the 25 reviewer comments are answerable in a week. The rejection is
not the sum of those comments. It is four structural problems, three of which are real and
one of which is a self-inflicted presentation error. Fixing the 25 comments without fixing
these four would produce a cleaner paper that gets rejected again.

---

## Problem 1 — The benchmark is saturated, so it cannot support any comparative claim

This is the deepest problem and it is the reason R1 wrote "do not provide any significant
novelty" and R2 wrote "the novelty and added value are not entirely clear."

The paper's headline is a *comparison*: physics-informed features vs. raw deep learning,
classical learners vs. 1D-CNN. But look at the spread in Table IV:

| Model | Errors | Error rate | Macro-F1 |
|---|---|---|---|
| ExtraTrees | 3 / 607 | 0.49 % | 0.9951 |
| SVM-RBF | 4 / 607 | 0.66 % | 0.9935 |
| LR-L2 | 4 / 607 | 0.66 % | 0.9935 |
| SC-CNN | 12 / 1821 | 0.66 % | 0.9935 |
| Raw-CNN | 48 / 1821 | 2.64 % | 0.9737 |
| RF | 22 / 607 | 3.62 % | 0.9632 |

Every model of interest sits between 3 and 4 errors. **An ℓ2-regularised logistic
regression ties a dual-head CNN.** That is not a finding about representations or model
families; it is the signature of a task with no headroom left.

And the effective sample size is far smaller than 607. The dataset has **7 operating points
× 4 severity levels = 28 distinct physical conditions**. The 607 files are repeated 10-second
acquisitions of an *unchanged* machine state — 20 to 30 recordings per cell, minutes apart.
Those are not 607 independent samples. They are 28 conditions, resampled. The paper's own
statistics section already concedes the consequence:

> "this result reflects the limited power of the paired test at near-saturated error rates
> rather than demonstrated equivalence"

That sentence is correct, and it is also an admission that the central experiment cannot
answer the central question. A McNemar test on one discordant file (p = 1.000) carries no
information. Reporting "3 errors out of 607" implies a precision the design does not have.

Independent support: the contemporaneous ISIE 2026 study on the *same fault* (rotor ITSC
severity, eddy-current vibration sensing) reports **90.56 % accuracy with 87 % recall on
mild faults**. When this problem is posed with realistic difficulty retained, methods land
near 90 %. Landing at 99.5 % is evidence the task was made easy, not that the method is
strong.

**What this costs you:** the paper's stated contribution ("no deep-learning-superiority
conclusion is supported") is a *null result on an experiment with no resolving power*. A
null result is only publishable when the experiment could have detected the effect. Yours
could not, and R2 additionally points out that the expected direction of the result was
already known.

### The fix — restore resolving power (no new measurements required)

All of these use the data you already have:

1. **Vary the number of source operating points.** You currently train on 6 and test on 1.
   Train on *k* = 1, 2, 3, 4, 5, 6 operating points and test on the held-out ones. Report
   macro-F1 as a function of *k*. Methods that tie at *k* = 6 will separate at *k* = 1–2,
   and the physics-informed representations should separate *most* there — which is
   precisely the claim you want to make and currently cannot.
2. **Shorten the observation window.** You use 10 s at 125 kHz. Sweep record length
   (10 s → 1 s → 200 ms → 50 ms) and sampling rate. This simultaneously answers R2-2's
   request for time-to-diagnosis, and it is a realistic constraint for field deployment.
3. **Add measured-level perturbations.** Sensor gain mismatch, small angular misplacement,
   additive noise, grid-frequency drift. A representation that claims robustness to
   operating-point shift should be tested against sensor-mounting shift too — and that is
   *new*, nobody in your Table I does it.
4. **Report at the level of independent conditions.** Give per-cell (OP × severity)
   results for all 28 cells. Compute confidence intervals by resampling **conditions**, not
   files. If you keep file-level counts, state the correlation structure explicitly.
5. **Change the headline metric.** Instead of "macro-F1 at saturation," report something
   with dynamic range and operational meaning — e.g. *the minimum number of source
   operating points required to reach 95 % macro-F1 on unseen operating points*. That
   quantity is new, decision-relevant for commissioning a monitoring system, and it
   discriminates between representations.

---

## Problem 2 — The central physics claim is asserted, never measured

The title says "Physics-Informed." The physics is Eq. (4):

```
V(k·f_m) ≈ γ · K_k · I_f          V(f_e) ≈ K_e · I_f · (1 − γ/2p)
```

and the resulting narrative, quoted from Section II:

> "a deeply under-excited operating point (low I_f) can reproduce the weak fault harmonics
> of the fault at nominal excitation. This is precisely the boundary failure observed at
> the under-excited condition in Section V."

This is the most interesting idea in the paper: **severity γ and excitation I_f are
physically confounded in absolute amplitude, and normalising by the fundamental cancels
I_f to first order.** It explains *why* P18 fails and *why* normalised features work. It is
a genuine physics-informed insight.

**But the manuscript never reports I_f for a single operating point.** And it cannot be
recovered from the source: the data report tabulates only apparent power and power factor
for P15–P21; the 220 V / 3.5 A field values are the machine's *nameplate* rating (see
`05_dataset_reference.md`, §5).

So the causal chain is unverified end to end:
- `I_f` per operating point: not measured, not reported, not available.
- `V(k·f_m) ∝ γ·I_f`: never tested against the measured data.
- "P18 fails because `I_f` is low": asserted. Equally consistent with the presented
  evidence are (a) lower stray-field SNR at low leading power factor, (b) armature-reaction
  redistribution of the external field, (c) saturation changes in the magnetic circuit.
  You have not excluded any of them.

A reviewer who notices this concludes that "physics-informed" is a label on the feature
names rather than a validated model. That is exactly the editor's "novelty and added value
are not sufficiently demonstrated" *and* "methodological details insufficiently
documented," in one stroke.

Note also that Fig. 5(c) shows the normalised ratio "increases with γ across all operating
points" but with "visible residual spread" — and the spread is never quantified. The whole
argument for normalisation rests on a qualitative reading of one panel.

### The fix — measure it (high value, no new hardware)

1. **Obtain `I_f` per operating point.** Ask the UFSC/GRUCAD authors directly — R2 already
   told you to contact them, so this doubles as compliance with R2-5. If they cannot supply
   it, estimate it: for a salient-pole machine, compute the excitation emf from the
   measured terminal quantities and the d/q reactances, then map to `I_f` on the air-gap
   line. State the method and its uncertainty.
2. **Test Eq. (4) directly.** Plot measured `A(k·f_m)` against `γ·I_f` across all 28 cells.
   Fit it. Report R². If the first-order law holds, you have *validated a physical model on
   measured data* — that is a contribution, and it is the one thing in this paper that
   nobody in your Table I has done.
3. **Quantify the normalisation.** Report the between-operating-point variance of
   `R(k·f_m; f_e)` at fixed γ, before and after normalisation. One number — a variance
   reduction factor — replaces the qualitative reading of Fig. 5(b–c) and proves the claim.
4. **Turn the P18 observation into a prediction.** Derive an *excitation–severity
   confounding index* from Eq. (4) — how close the (γ, `I_f`) product for a mild fault at
   one operating point comes to that of a healthy machine at another. Compute it for all
   seven operating points **before running any classifier**. If the predicted difficulty
   ranking matches the measured per-operating-point error ranking, you have a predictive
   physical criterion for where cross-operating-point diagnosis will fail. That is novel,
   it is useful (it tells an engineer which operating points to commission on), and it
   reframes the paper from a benchmark into a physical result.

Item 4 is, in my assessment, the strongest available reframing of this work.

---

## Problem 3 — The contribution is framed as a negative result that is already known

R2 states it bluntly: *"The conclusions that physics-informed machine learning approaches
perform better than algorithms relying on raw data is already known."* This is correct, and
the paper's abstract leads with the negative framing: "the benchmark does not support a
simple deep-learning-superiority conclusion."

Two further framing problems:

- **The severity calibration rescues only your own CNN.** SC-CNN reaches 0.9935 — which
  ExtraTrees, SVM-RBF and logistic regression already reach *without* any calibration. So
  the demonstrated value of the calibration stage is repairing a deficiency of the raw CNN,
  not improving the state of the art. As presented it reads as a patch.
- **The feature set is acknowledged as not new.** R2: "The features, obtained from the raw
  signals, used to feed the networks are known and not new." Harmonic ratios, band-energy
  ratios and cross-channel differences are all established. Novelty cannot rest here.

### The fix — reframe, and generalise the calibration

- Lead with the physical result (Problem 2, item 4), not the benchmark. The benchmark
  becomes supporting evidence, not the headline.
- **Apply the ordinal severity calibration to the classical models too.** If a severity
  regressor + ordinal thresholds improves RF, SVM and LR as well, it is a general method
  and a real contribution. If it only helps the CNN, it is a patch — and you should say so
  and demote it. Either outcome is publishable; the current framing avoids the question.
- Drop "does not support a simple deep-learning-superiority conclusion" from the abstract.
  Under Problem 1 you cannot support that claim anyway, and it advertises a null result.

---

## Problem 4 — Table IV / Fig. 6 mixes two denominators, and it cost you a reviewer's trust

R1's last question:

> "How can 48 errors correspond to a Macro-F1 score higher than that obtained with 22
> errors, while 12 errors and 4 errors result in the same Macro-F1 score?"

**Your numbers are correct. Your presentation is not.** The classical rows are over
n = 607 files; the CNN rows are pooled over three seeds, n = 1821 = 607 × 3. Normalising:

- 48 / 1821 = **2.64 %** vs. 22 / 607 = **3.62 %** → the CNN really is better, hence the higher F1.
- 12 / 1821 = 4 / 607 = **0.659 %** *exactly* → identical error rates, hence identical F1 = 0.9935.

Both "paradoxes" dissolve. (Verify with `tools/error_rate_check.py`.)

The table footnote does say "CNN rows are pooled over three seeds," but an *error count*
column that silently switches denominator between rows — reproduced as bar labels in
Fig. 6 — is genuinely misleading. A careful reviewer read the figure, found it
self-contradictory, and reasonably concluded the results could not be verified. This one
formatting decision plausibly contributed as much to R1's overall negative assessment as
any substantive issue.

### The fix (30 minutes)

Report **error rate (%)** as the primary column, and give CNN results as **mean ± std
across the three seeds on the 607-file basis** (16.0 ± s.d. for raw, 4.0 ± s.d. for
calibrated). Then every row sits on n = 607 and the ordering is monotone in both error
count and F1:

| Model | Errors (n = 607 basis) | Error rate | Macro-F1 |
|---|---|---|---|
| ExtraTrees | 3 | 0.49 % | 0.9951 |
| SVM-RBF | 4 | 0.66 % | 0.9935 |
| LR-L2 | 4 | 0.66 % | 0.9935 |
| SC-CNN | 4.0 (mean of 3 seeds) | 0.66 % | 0.9935 |
| Raw-CNN | 16.0 (mean of 3 seeds) | 2.64 % | 0.9737 |
| RF | 22 | 3.62 % | 0.9632 |

Apply the same normalisation to Fig. 6 and to the Fig. 7 confusion matrices (which
currently report 36 *seed-level* P18 errors — i.e. 12 per seed).

---

## Summary of what actually has to change

| Problem | Severity | Fixable with data in hand? |
|---|---|---|
| 1. Saturated benchmark, no resolving power | **Fatal** | Yes — harder protocol, no new measurements |
| 2. Physics claim asserted, `I_f` never measured | **Fatal** | Mostly — needs `I_f` from dataset authors or estimation |
| 3. Contribution framed as a known negative result | **Fatal** | Yes — reframing + generalising the calibration |
| 4. Denominator error in Table IV / Fig. 6 | Serious, cosmetic cause | Yes — 30 minutes |

Problems 1–3 are what the editor means by "substantial additional methodological and
experimental work." They are largely addressable with the existing 21 GB of data plus one
email to the dataset authors — but they require re-running the experimental campaign under
a harder protocol, not editing the manuscript.
