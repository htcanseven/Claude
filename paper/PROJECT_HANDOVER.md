# Project handover — low-cost MEMS condition-monitoring paper

Written to let a fresh Claude Code session pick this up without re-deriving
context. Current branch `claude/motor-condition-monitoring-iot-111aqd`,
tip `6db334c`.

---

## 1. If the workspace looks empty, it is stale

This has happened once already: the container was reset to `dabe55f` (the PR #1
merge) while the branch on the remote was four commits ahead. Symptoms are
`paper/Measurement (Elsevier)/` missing, `paper/refs.bib` showing 29 entries
instead of 70, and `src/protocols_v2.py` absent.

```bash
git fetch origin claude/motor-condition-monitoring-iot-111aqd
git reset --hard origin/claude/motor-condition-monitoring-iot-111aqd
grep -c '^@' paper/refs.bib          # must print 70
ls "paper/Measurement (Elsevier)"    # must list manuscript.tex + 8 sections
```

The dataset is gitignored. If `data/raw/` is empty, re-download from Mendeley
DOI `10.17632/rs4vz8n3t5.1` (36 CSV recordings, ~200 MB) before running any
analysis script. `pip install pymupdf` is needed for PDF verification.

---

## 2. Story so far

A public smartphone-MEMS vibration dataset (Ertarğın et al., *Data in Brief*
67 (2026) 112916) of one 1.1 kW induction machine: 6 health states × 3 supply
frequencies × 2 loads = 36 recordings at 100 Hz. The paper is a measurement
study, not a new classifier.

| stage | outcome |
|---|---|
| IEEE TIM | desk rejected — **scope** |
| IOP MST (MST-138741) | desk rejected — **"comprehensive overview of related research through the reference list"** (29 references submitted) |
| Measurement (Elsevier) | current target, ready to submit |

Measurement's guide encodes both prior failure modes as scope conditions: it
requires a "critical review of the state-of-the-art … showing how the research
presented advances it", and excludes fault-diagnosis papers "with little or no
elements of measurement science or technology".

---

## 3. What the paper now claims

| quantity | value |
|---|---|
| Optimism gap, random vs recording-wise | 41–47 points |
| — from window overlap | **0.0** |
| — from temporal proximity | **0.0** |
| — from recording identity | **+46.7** |
| Band-limiting to 12.5 Hz at 100 Hz | −2.7 |
| Sample count at fixed band | **+12.8** |
| Aliasing (anti-alias filter removed) | −24.9 |
| Baseline (100 Hz, 6 ch, 2 s) | 53.9 ± 12.5 % |
| Frugal (25 Hz, 3 raw ch, 4 s) | 75.0 ± 11.4 % |
| Frugal − baseline | +21.1 pts, permutation **p = 0.020** |
| 25 Hz − baseline | +9.4 pts, **p = 0.26 (not significant)** |
| Nested-CV estimate | **71.0 %** (selection bias **+6.0** pts) |
| Macro-F1 at baseline | 51.1 %; per-class recall 0.87 (H) … 0.16 (B2) |

Intervals are 95 % clustered on the **recording** (n = 36), not on seeds. Seed
based intervals were about three times narrower and are no longer used.

**Two earlier claims were overturned by experiment, not by rewording:**
1. Window overlap was blamed for the leakage. It contributes nothing; recording
   identity contributes all of it. Enforcing non-overlapping windows — the usual
   precaution — offers no protection on this class of data.
2. The 25 Hz benefit was attributed to the information living at low frequency.
   Band-limiting alone is mildly *harmful*; the gain comes from the reduced
   sample count per window. Shaft frequencies (13.1–24.9 Hz) all sit above the
   12.5 Hz Nyquist limit of the 25 Hz stream, so the best configuration has
   removed them entirely.

---

## 4. Code map (`src/`)

| file | purpose |
|---|---|
| `protocols_v2.py` | shared: `build_custom` (pluggable resampler), `rs_polyphase` / `rs_lowpass_only` / `rs_naive_decimate`, `eval_group` / `eval_random` / `eval_blocked` / `eval_leave_one`, `clustered_ci`, `paired_permutation` |
| `run_leakage_decomposition.py` | → `results/leakage_decomposition.{md,json}` (~30 min) |
| `run_antialias.py` | → `results/antialias.{md,json}` (~25 min) |
| `run_stats_v2.py` | 10 seeds → `results/stats_v2.{md,json}` (~35 min) |
| `run_nested_cv.py` | → `results/nested_cv.{md,json}` (~45 min) |
| `make_graphical_abstract.py` | → `results/graphical_abstract.png` (1328×531) |
| `fetch_refs.py`, `build_bib.py` | Crossref search → verified BibTeX |
| `dataio.py`, `features.py`, `evaluation.py`, `viz.py` | original pipeline |

~5.5 s per RF-200 fit on 4 cores; a full re-run of all four experiments ≈ 2.5 h.
Every reported number traces to a JSON in `results/`.

**References were built from the Crossref API and every DOI was verified against
the registry.** If more are added, keep that rule — nothing written from memory.

---

## 5. Standing preferences (apply to all future edits)

- **Passive voice, third person. No "we", "our", "us" anywhere.**
- Contributions in **paragraph form**, never bulleted.
- Title keeps **IoT**; no double colon, no question mark.
- **Code is not released.** Every reviewer so far has raised this; the paper
  claims only a fully specified method and states in the limitations that the
  implementation is not distributed.
- No new measurements; this dataset only.
- Floats use `[t]`.

---

## 6. Open items

1. **Test-rig photo is 166 dpi**, needs ≥300 dpi. Requires the original camera
   file. Only item blocking submission.
2. Cover letter needs the **date** and a confirmed **funding** statement.
3. Optional: `[tbp]` instead of `[t]` if float placement drifts in the
   double-spaced review layout.
4. If rejected on single-machine scope, fallback venue is **Measurement: Sensors**.
5. If pressed on reproducibility, the cheap concession is releasing only the
   protocol code (fold assignment + the four partitioners, no dataset).

## 7. Residual risk

Single machine, one physical specimen per fault, no new measurements. No
re-analysis fixes this; it is now stated in the abstract, introduction and
limitations rather than buried. The methodological findings are what carry the
paper.

---

## 8. Rebuild

```bash
cd "paper/Measurement (Elsevier)"
tectonic -X compile manuscript.tex     # expect 41 pp, no "??", no errors
```
Elsewhere: `paper/` holds the superseded IOP/IEEE versions, and
`paper/Deployment-…(IOP MST)/` the MST submission. Do not edit those for the
Measurement submission — the live sources are in `paper/Measurement (Elsevier)/`.
`paper/MEASUREMENT_SUBMISSION_NOTES.md` records what changed overnight and why.
