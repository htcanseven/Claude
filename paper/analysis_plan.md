# Analysis plan

Every analysis below runs **in software on the existing dataset** (plus, for F,
other *public* datasets). No new hardware, no new measurements. Each item is
tagged with the paper section it feeds.

## A. Pipeline & reproducibility backbone  → §V
- **A1** Loader for the 36 `.csv`/`.mat` files; parse `Class_Load_Speed` metadata.
- **A2** Windowing: 2 s / 50% overlap (baseline parity) + configurable length/overlap.
- **A3** Time-domain feature set per channel: RMS, STD, peak-to-peak, kurtosis,
  skewness, crest factor (baseline parity) **+** mean, variance, shape/impulse/
  margin/clearance factors, zero-crossing rate, signal entropy.
- **A4** Config-driven experiment runner, fixed seeds, released code.

## B. Sensor / signal characterization (the "instrument" angle)  → §IV
- **B1** Noise floor & effective resolution from quiet healthy segments; estimate
  quantization step / dynamic range of the MEMS stream.
- **B2** Usable bandwidth: PSD per class; show the hard <50 Hz Nyquist wall and
  where each fault's discriminative energy actually sits.
- **B3** Raw (`g*`) vs gravity-compensated (`guser*`) channels: which carries more
  diagnostic value, per fault class.
- **B4** Per-channel / per-axis informativeness ranking (mutual information).

## C. Deployment-realistic evaluation methodology (headline)  → §VI
- **C1** Reproduce the leaky baseline: random split over overlapping windows →
  the optimistic ~98% (sanity check vs the data article).
- **C2** **Group-aware split** (hold out whole recordings) → the honest number;
  report the *optimism gap* (C1 − C2).
- **C3** **Cross-speed** generalization: train {30,40} → test 50 Hz, etc.
- **C4** **Cross-load** generalization: train loaded → test unloaded (and reverse).
- **C5** Statistical rigor: CIs across folds/seeds; McNemar tests between
  protocols and between models.
- Models: RF, KNN, SVM (baseline parity) + a compact 1D-CNN and a small MLP for
  the edge story.

## D. Accuracy–resource trade-off characterization (systems core)  → §VII
- **D1** Sampling-rate sweep by decimation: 100 → 50 → 25 → 12.5 → 10 Hz →
  accuracy vs data rate.
- **D2** Channel-count sweep: 6 → 3 → 1 → accuracy vs bandwidth/energy.
- **D3** Window-length sweep: 4 / 2 / 1 / 0.5 s → accuracy vs detection latency.
- **D4** Feature-set ablation: full vs minimal subset → compute cost vs accuracy.
- **D5** Quantization: float32 → int16 → int8 → accuracy vs memory.
- **D6** Packet-loss / missing-sample robustness: 0–20% loss + simple concealment.
- **D7** Mounting/coupling robustness via **software augmentation**: 3-D rotation
  of the tri-axial data (emulates orientation) + gain/noise (emulates tape
  coupling) → accuracy under sensor-placement variability.
- Synthesis: Pareto fronts + recommended operating points.

## E. Edge-node & communication feasibility (emulated IoT)  → §VIII
- **E1** Link budget: raw vs feature vs decision payloads mapped to BLE, Zigbee,
  **LoRaWAN (with 1% duty-cycle limit)**, NB-IoT — which links carry which stream.
- **E2** Footprint (deterministic, no hardware): model size + RAM via
  `emlearn`/`micromlgen` (classical) and TFLite-Micro tensor arena (1D-CNN).
- **E3** Latency via **cycle-accurate MCU emulation** (Renode / QEMU, Cortex-M4
  class) → ms at a stated clock; energy as a datasheet-based estimate with
  explicit assumptions (labeled *estimated*, not measured).

## F. Cross-dataset validation (optional, strengthener)  → §IX
- Downsample a public *industrial-accelerometer* dataset (CWRU / Paderborn /
  MFPT) to 100 Hz; test transfer and quantify low-cost vs reference-grade loss.
  Existing public data — still no new measurement.

---

### Credibility gradient (state honestly in the paper)
- **Deterministic / solid:** feature cost, model size, RAM, link-budget payloads,
  all accuracy sweeps.
- **Defensible via emulation:** MCU latency (cycle-accurate).
- **Estimate only:** energy per inference (datasheet-based; assumptions stated).

### Build order (proposed)
1. A (backbone) → 2. C (honest evaluation, the headline) → 3. D (trade-offs) →
4. B (sensor characterization) → 5. E (edge/link) → 6. F (optional).
