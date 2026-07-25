# DRAFT — IEEE TIM manuscript prose

> **Index of the finalized manuscript.** All sections are complete as passive-voice
> LaTeX under `paper/`, assembled by `main.tex` (abstract + keywords live there).
> This file now serves as a section map, not a draft.

## Title
Deployment-Realistic IoT-Based Condition Monitoring of Induction Motors Using
Low-Cost MEMS Sensing

## Abstract (draft)
Vibration-based condition monitoring (CM) of induction motors is increasingly
attractive on low-cost, consumer-grade MEMS sensors that could be embedded in
inexpensive wireless nodes. Using a public smartphone-acquired vibration dataset
(six health states, three supply frequencies, two load levels, 100 Hz), we make
three measurement-oriented contributions. First, we show that the near-perfect
accuracies commonly reported for such data are largely a **methodological
artifact**: random splitting of overlapping analysis windows leaks
recording-specific information, inflating accuracy by 35–52 points relative to a
leakage-free, whole-recording (group-aware) protocol. Second, we **characterize
the smartphone MEMS channel as a measurement instrument** — effective resolution,
noise floor, the 50 Hz usable band, and the (non-obvious) finding that on-device
gravity compensation discards diagnostically useful low-frequency content.
Third, we map the **accuracy–resource trade-off** across sampling rate, channel
count, window length, quantization, packet loss and mounting orientation, and
combine it with a communication link budget and edge-model footprint to identify
deployable operating points for BLE/Zigbee/NB-IoT/LoRaWAN nodes. [headline D
number], [footprint number]. The study offers a reproducible, deployment-honest
baseline for low-cost IoT-based motor CM.

## I. Introduction
**Finalized in `paper/intro.tex`** (passive voice, top-journal style: motivation →
three-gap framing (recoverability, evaluation leakage, IoT trade-off) → four
explicit contributions → paper organization). Uses `\IEEEPARstart`.

## II. Related Work
**Finalized in `paper/related_work.tex`** (five subsections + positioning table;
citations resolve against `paper/refs.bib`).

## III. Dataset and Measurement Setup
**Finalized in `paper/dataset.tex`** (passive voice; specifications, fault-emulation
and measured-speed tables, test-rig figure placeholder, and the original
representative-signals figure `results/fig_example_signals.png`).

## IV. Sensor and Signal Characterization
**Finalized in `paper/characterization.tex`** (passive voice; effective
resolution/noise floor, usable-band PSD, raw-vs-gravity-compensated channels;
figures `results/fig_psd_usable_band.png`, `results/fig_channel_mi.png`).

## V. Methodology
**Finalized in `paper/methodology.tex`** (passive voice; pipeline figure,
segmentation/windowing, feature-definition table, classifiers, and the four
evaluation protocols with the leakage rationale; multi-seed statistics).

## VI. Results
**Finalized in `paper/results.tex`** (report-focused; optimism-gap table,
trade-off sweeps + frugal recipe, link budget + footprint; figures gap/confusion/
tradeoffs/recipe). VI-A optimism table reconciling to 5-seed values.

## VII. Discussion and Limitations
**Finalized in `paper/discussion.tex`** (evaluation-methodology implication,
ultra-low-bandwidth-as-asset, model complexity/edge feasibility, sensor guidance,
scope; then limitations: single motor, 36 recordings/wide CIs, qualitative B1/B2,
energy indirect, cross-machine generalization as future work).

## VIII. Conclusion
*(TODO)* Low-rate smartphone-MEMS CM is viable for coarse fault states and
edge/IoT deployment, but only under leakage-free evaluation; the paper provides
the methodology, the sensor characterization, and the trade-off map reproducibly.
