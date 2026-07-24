# DRAFT — IEEE TIM manuscript prose

> Working draft to accelerate writing. Citations as `[n]`, floats as `[Fig. X]/
> [Table Y]`. Numbers are from `results/`. Sections IV–VI depend on completed
> analyses; the trade-off/results wording is finalized once Analysis D lands.

## Title
Deployment-Realistic Condition Monitoring of Induction Motors With a Low-Cost
MEMS Accelerometer: Accuracy–Resource Trade-offs for Edge/IoT Sensing

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

## I. Introduction (draft)
Induction motors dominate industrial drives, and unplanned failures are costly,
motivating continuous CM [1–3]. Classical vibration CM relies on industrial
accelerometers sampled at tens of kHz to resolve bearing defect frequencies via
spectral/envelope analysis. Such instrumentation is accurate but expensive,
intrusive, and hard to scale to the many small motors in a plant — precisely the
population that an inexpensive, wireless, MEMS-based node could cover.

Consumer MEMS inertial sensors (as in smartphones) make ultra-low-cost
acquisition possible, but at low, software-capped sampling rates (here 100 Hz)
that violate the assumptions of classical high-frequency diagnosis. Two questions
follow, both of measurement character: (i) *what fault information is actually
recoverable* from such a constrained sensor, and (ii) *how should it be
evaluated and deployed* so that reported performance transfers to the field.

This paper addresses both. We deliberately separate genuine diagnostic capability
from evaluation optimism, characterize the sensor as an instrument, and quantify
the sensing/communication trade-offs that govern an edge deployment. Our
contributions are:
1. A **leakage-free evaluation methodology** (group-aware + cross-speed +
   cross-load) for windowed low-rate vibration CM, and a quantification of the
   optimism induced by the prevailing random-split practice.
2. A **measurement characterization** of the smartphone MEMS CM channel:
   effective resolution, noise floor, usable band, and raw vs
   gravity-compensated content.
3. An **accuracy–resource trade-off characterization** with a communication
   link budget and edge-model footprint, yielding deployable operating points.
All code and configurations are released for reproducibility.

## II. Related Work (draft skeleton)
- Signal-based CM of induction motors; bearing/rotor/electrical fault signatures
  [1–3]. High-rate accelerometer datasets [4–8] (contrast in [Table 1] of the
  data article: 8–200 kHz vs our 100 Hz).
- Low-cost / MEMS / smartphone vibration sensing [9]; low-sampling-rate CM
  feasibility [10–13].
- ML for fault diagnosis and **evaluation pitfalls**: window overlap and
  subject/recording leakage inflate accuracy; group-aware validation. *(position
  our methodological contribution here.)*
- Edge/IoT CM and TinyML; communication constraints (LoRaWAN duty cycle, etc.).

## III. Dataset and Measurement Setup (draft)
We use the public smartphone-MEMS dataset of [data article] (Mendeley
`10.17632/rs4vz8n3t5`). A 1.1 kW three-phase squirrel-cage motor, driven by a
V/f inverter and loaded by a DC generator, was recorded with an iPhone 15 Pro Max
(Sensor Play app) rigidly taped to the terminal box. Six channels are provided —
raw triaxial acceleration (gX,gY,gZ) and gravity-compensated linear acceleration
(gUserX,gUserY,gUserZ) — at 100 Hz for 15 min per condition. Six health states
(healthy H; insufficient/severe-insufficient lubrication B1/B2; cracked outer
ring B3; voltage imbalance V; broken rotor bar R) were recorded at 30/40/50 Hz
supply under loaded/unloaded operation: 6×2×3 = 36 recordings. We verified all 36
files contain exactly 89,999 samples with no missing values [validation.md].

## IV. Sensor and Signal Characterization (draft)
Treating the phone as an instrument under test, we estimate an effective
resolution (smallest quantization step) of ~0.015 mg on the raw channels and a
noise-floor PSD of −70.8 dB (g²/Hz) above 30 Hz [analysis_B]. The usable band is
hard-capped at 50 Hz (Nyquist); nonetheless diagnostic structure is present
within it — the rotational fundamental (~24 Hz at 50 Hz supply) and low harmonics
for R and V, and a broadband lift for bearing faults, against a healthy baseline
~10× lower in power [Fig. psd]. High-frequency bearing tones (BPFO/BPFI/BSF) lie
beyond the band, bounding what is recoverable.

A measurement subtlety specific to smartphone acquisition: the raw and
gravity-compensated triads are only moderately correlated (r ≈ 0.46–0.58), and
the **raw channels carry more label information** (mean MI 0.65–0.75) than the
compensated ones (0.46–0.57) [Fig. mi]. The on-device complementary filter that
produces `userAcceleration` therefore removes diagnostically useful
low-frequency content; raw channels are preferable for CM.

## V. Methodology (draft)
**Windowing/features.** Each recording is split into 2 s windows at 50% overlap
(32,328 windows total, matching the data article), and 14 time-domain features
per channel (RMS, STD, variance, peak-to-peak, max-abs, skewness, kurtosis,
crest/shape/impulse/clearance factors, zero-crossing rate, amplitude entropy).

**Evaluation protocols.** We contrast four protocols on identical features:
*RANDOM* (stratified split over all windows — the prevailing practice), *GROUP*
(whole-recording holdout via StratifiedGroupKFold; leakage-free), *CROSS-SPEED*
(leave-one-supply-frequency-out), and *CROSS-LOAD* (leave-one-load-out). We report
accuracy and macro-F1 with dispersion across folds. Classifiers: Random Forest,
KNN, and an RBF-approximate SVM; simple linear/tree models are added for the
footprint study.

## VI. Results (to finalize with Analysis D)
- VI-A Optimism gap [Table C, Fig. optimism_gap, Fig. confusion].
- VI-B Accuracy–resource trade-offs [Analysis D, Fig. tradeoffs_*].
- VI-C Link budget & edge footprint [Table E].

## VII. Discussion / Limitations
Single 1.1 kW motor, laboratory-induced discrete faults, qualitative B1/B2
severity; energy figures emulated not measured; results are a *lower-bound,
honest* baseline rather than a field claim. Cross-dataset validation
(downsampled industrial benchmark) is identified as the key generalization test.

## VIII. Conclusion
Low-rate smartphone-MEMS CM is viable for coarse fault states and edge/IoT
deployment, but only under leakage-free evaluation; we provide the methodology,
the sensor characterization, and the trade-off map to do so reproducibly.
