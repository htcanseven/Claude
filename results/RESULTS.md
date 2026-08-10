# Results synthesis — low-cost MEMS motor CM (IEEE TIM)

Reproducible analyses on the smartphone-MEMS dataset (Mendeley `rs4vz8n3t5`,
v1). All code in `src/`; per-analysis tables in `results/analysis_*.md`;
figures in `results/*.png`. Seed 0 throughout.

---

## A · Data validation  (`validation.md`)

- **36/36** recordings present; every file exactly **89,999 samples = 900 s @
  100 Hz**; **zero NaNs**; consecutive-duplicate rows negligible (no
  sample-and-hold artifact).
- Our 2 s / 50%-overlap windowing yields **32,328 windows** — reproducing the
  data article's count exactly (pipeline validated).

## B · Sensor / signal characterization  (`analysis_B.md`)

- **Effective resolution (LSB):** raw channels 0.015 mg, gravity-compensated
  0.001 mg. **Noise floor** (gX, >30 Hz): 8.2×10⁻⁸ g²/Hz (−70.8 dB).
- **Usable band 0–50 Hz** (Nyquist). Fault signatures *do* live in this band —
  rotational fundamental (~24 Hz at 50 Hz supply) and low harmonics for R and V,
  broadband lift for bearing faults — while a healthy motor sits ~10× lower
  (`fig_psd_usable_band.png`). High-frequency bearing defect tones (BPFO/BPFI/BSF)
  are absent, as expected.
- **Raw vs gravity-compensated:** only moderately correlated (r ≈ 0.46–0.58), and
  the **raw channels are more diagnostically informative** (mean MI 0.65–0.75)
  than the compensated ones (0.46–0.57). iOS `userAcceleration` discards useful
  low-frequency fault content — a smartphone-specific measurement finding
  (`fig_channel_mi.png`).

## C · Deployment-realistic evaluation — the headline  (`analysis_C.md`)

| Protocol | RF | KNN | SVM |
|---|---|---|---|
| **RANDOM** (leaky, overlapping-window split) | 100.0 | 100.0 | 100.0 |
| **GROUP** (whole-recording holdout) | 47.6 ± 7.9 | 63.3 ± 11.8 | 53.2 ± 12.2 |
| **CROSS-SPEED** (leave-one-speed-out) | 49.4 | 48.2 | 49.7 |
| **CROSS-LOAD** (leave-one-load-out) | 50.1 | 40.3 | 40.1 |

- **Optimism gap (RANDOM − GROUP): +52 / +37 / +47 points** for RF/KNN/SVM. The
  ~98–100% accuracies obtained under random splitting of overlapping windows are
  a **leakage artifact**: adjacent 50%-overlap windows are near-duplicates and
  each recording has characteristic statistics, so a random split lets the model
  recognize *which recording* a window came from rather than the fault itself.
- Under leakage-free evaluation the task is **real but much harder** (well above
  the 16.7% chance level, far below 98%). **Simpler models generalize better**
  (KNN > SVM > RF), a sign the forest overfits the ~30 training recordings.
- **Confusion (RF, GROUP, `fig_confusion_group.png`):** Healthy (0.82) and
  Broken-rotor R (0.64) are identifiable; the two lubrication severities **B1/B2
  blur together** (B2 recall 0.16) and bearing/electrical faults confuse —
  consistent with the missing high-frequency bearing information.

## D · Accuracy–resource trade-offs  (`analysis_D.md`, `analysis_harden.md`)

Leakage-free GROUP protocol; single-seed sweeps (`fig_tradeoffs_*.png`) plus
5-seed confirmation for the headline knobs.

- **Sampling rate (multi-seed):** 100 Hz → 53.7%, **25 Hz → 64.9% (best)**, 10 Hz
  → 59.7%. Every rate ≤ 25 Hz matches or beats 100 Hz — the anti-alias low-pass
  removes high-frequency content the model overfits. *100 Hz confers no benefit.*
- **Channels:** raw-3ch (56.7%) **beats** all-6ch (46.4%); the gravity-compensated
  triad and single axes are worse. Fewer, better-chosen channels win.
- **Window length:** 4 s (63.3%) > 2 s (46.4%) — longer windows generalize better
  (cost: detection latency).
- **Feature set:** the 6-feature "paper" subset (45.3%) ≈ full 14-feature set
  (46.4%) — a minimal, edge-cheap feature set suffices.
- **Quantization:** graceful — 8-bit 50%, 4-bit 45% (≈ float baseline).
- **Packet loss:** essentially flat to 20% loss (~47%) — robust for lossy wireless.
- **Mounting rotation:** degrades with orientation offset (30° → 31%), motivating
  careful mounting or orientation-invariant features.
- **Combined optimal (25 Hz + raw-3ch + 4 s), multi-seed:** **RF 74.2%** vs the
  naive baseline **53.7%** (`fig_recipe_stacking.png`). *The frugal, IoT-friendly
  choices stack into a ~20-point gain* while cutting raw data volume ~8×.

## E · Link budget & edge footprint  (`analysis_E.md`)

- **Telemetry:** raw 6-ch @100 Hz = **9.6 kbps** (int16); 84-feature stream =
  **2.69 kbps**; on-node **decision = 40 bps**.
- **LoRaWAN** (1% duty cycle, ~55 bps sustained) admits **only the decision
  stream** → classification *must* run on the node for LoRa-class links;
  BLE / Zigbee / NB-IoT can carry raw or feature streams.
- **Edge footprint vs honest accuracy:** a **4.7 KB logistic regression (52.2%)**
  matches/beats a **1.09 MB RF-200 (46.4%)**; RF-50-d8 = 51.2% @214 KB. Small,
  edge-deployable models are also the better *generalizers* here — a convenient
  alignment for low-cost IoT nodes. Feature extraction is O(W·C) time-domain
  statistics (no FFT), tractable on a Cortex-M-class MCU.
- *Next step (labelled):* cycle-accurate latency/energy via Renode + emlearn/TFLM
  C-array sizes.

---

### Headline takeaways for the paper
1. **Methodology contribution:** leakage-free (group-aware + cross-condition)
   evaluation is essential; the field's random-split accuracies overstate
   smartphone-MEMS CM performance by **35–52 points**.
2. **Feasibility bound:** at 100 Hz, coarse states (healthy / broken-rotor) are
   reliably separable; fine bearing-degradation staging is not (Nyquist-limited).
3. **Trade-off characterization:** the resource-*optimal* IoT configuration
   (25 Hz, raw-3ch, 4 s) **beats** the naive 100 Hz/6-channel baseline (74% vs
   54%); robust to quantization and packet loss, sensitive to mounting.
4. **Deployability:** tiny models + on-node decisions make LoRa-class IoT nodes
   viable, and small models *also generalize better* under honest evaluation.
