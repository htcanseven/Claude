# Measurement (Elsevier) — what changed overnight

## Deliverables
| file | what it is |
|---|---|
| `paper/Measurement (Elsevier)/manuscript.pdf` | submission-ready, 41 pp in Elsevier `review` format (double-spaced, line-numbered) |
| `.../manuscript.tex` + 8 section files + `refs.bib` | sources |
| `.../highlights.txt` | 5 highlights, all ≤85 characters |
| `.../graphical_abstract.png` | 1328×531, the leakage-decomposition result |
| `.../cover_letter.md` | written against Measurement's stated scope conditions |
| `results/*.json`, `*.md` | all new experimental output |

## Why MST rejected it, and what was done
The letter named one criterion: "provide a comprehensive overview of related
research through the reference list". The submitted list had **29 entries**, four
of them Data-in-Brief data descriptors. Measurement's own guide encodes the same
requirement as a scope condition ("critical review of the state-of-the-art …
showing how the research presented advances it") and additionally warns that
fault-diagnosis papers "with little or no elements of measurement science" are
out of scope.

**References: 29 → 70.** All 41 new entries were pulled from the Crossref API
with authoritative BibTeX and **every DOI was verified against the Crossref
registry** — nothing was written from memory. Section 2 was rewritten as a real
critical review in six subsections, now covering MEMS metrology (calibration,
thermal drift, cross-axis sensitivity, mounting), documented smartphone sensor
errors, selection bias, operating-condition shift, and uncertainty evaluation
for learned models.

## Three new experiments, and what they changed

**1. The leakage mechanism was wrong.** A ladder of partitionings tested each
suspected cause:

| partitioning | accuracy |
|---|---|
| RANDOM, 50 % overlap | 100.0 % |
| RANDOM, no overlap | 100.0 % |
| BLOCKED within recording | 100.0 % |
| GROUP (recording held out) | 52.8 % |

Window overlap contributes **0.0 points**, temporal proximity **0.0**, recording
identity **+46.7** — the entire gap. The previous text blamed overlapping windows
sharing samples; that is disproved. The practical consequence is sharper than the
old claim: enforcing non-overlapping windows, the usual precaution, offers no
protection at all on this class of data.

**2. The 25 Hz result had a real contradiction, now resolved.** Shaft frequencies
span 13.1–24.9 Hz; at 25 Hz sampling (Nyquist 12.5 Hz) proper decimation removes
all of them, yet accuracy improved. Holding frequency content fixed while varying
rate:

| condition | accuracy |
|---|---|
| 100 Hz unmodified | 52.8 % |
| 100 Hz low-passed to 12.5 Hz | 50.1 % |
| 25 Hz, anti-alias decimation | 62.9 % |
| 25 Hz, no anti-alias filter | 38.0 % |

Band-limiting alone **costs** 2.7 points; the whole +12.8 gain comes from the
reduced sample count per window; aliasing costs 24.9. So the time-domain feature
set is not invariant to sampling rate, and any rate sweep with fixed time-domain
features measures band and feature sensitivity together. The practical advice
survives; the explanation changes.

**3. Statistics rebuilt on the recording as the sampling unit.** Scores are now
computed per held-out recording, with clustered intervals and paired permutation
tests:

- Frugal vs baseline: **+21.1 points, p = 0.020** — holds.
- 25 Hz vs baseline alone: **+9.4 points, p = 0.26 — not significant.**

The old seed-level test reported these as p = 0.0001 and p = 0.003. Intervals are
about **three times wider** (±12 rather than ±4) because recording-to-recording
variation dominates. Per-fold accuracy genuinely ranges 54.5 %–98.2 %.

**4. Nested cross-validation** separates selection from estimation. Nested
estimate **71.0 %** vs 76.9 % when selection and scoring share folds — a **6.0
point selection bias**. Encouragingly, a blind inner selector still chose the
frugal configuration in **13 of 18** folds, so the recommendation is reproduced
independently; only the number attached to it changes.

## Decisions taken without you
1. **Code kept private**, per your instruction. Worth knowing: all three AI
   reviews *and* the earlier referee agent named this as a top criticism. The
   paper now claims only a fully specified method, and the limitations say
   plainly that the implementation is not distributed.
2. **GUM/Type A language withdrawn** for classification results. Measurement is a
   metrology journal; calling five seed re-runs a Type A evaluation would be
   challenged there. It is now called a reproducibility interval, with the
   unquantified influence quantities listed qualitatively.
3. **Contributions kept in paragraph form** (your earlier preference) despite one
   review recommending bullets.
4. **No stationary-phone noise measurement** — a different handset/session is a
   different instrument and would not characterise this dataset's sensor.

## Before you submit
- **Test-rig photo is 166 dpi** (needs ≥300). This is the one thing I cannot fix
  — please re-export from the original camera file at ≥1800 px wide.
- Fill in the **date** in the cover letter and confirm the **funding** statement
  ("no specific funding").
- Suggested reviewers if the portal asks — I did not invent names.
- Measurement is single-anonymous, so the manuscript is **de-anonymised** (author,
  affiliation, email restored).

## Residual risk
The single-machine, single-specimen scope remains the paper's main exposure, and
no amount of re-analysis fixes it. It is now stated in the abstract, introduction
and limitations rather than buried. If a reviewer presses on reproducibility,
releasing the evaluation-protocol code alone (fold assignment plus the four
partitioners, a few hundred lines, no dataset) would be the cheapest concession.
