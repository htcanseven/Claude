# Paper outline — IEEE Transactions on Instrumentation and Measurement (TIM)

**Title:**
*Deployment-Realistic IoT-Based Condition Monitoring of Induction Motors Using
Low-Cost MEMS Sensing*

**One-line thesis:** Ultra-low-bandwidth (100 Hz) smartphone-grade MEMS vibration
sensing can support reliable motor condition monitoring on constrained IoT/edge
nodes — *provided* it is evaluated under deployment-realistic protocols and
operated at the right accuracy–resource point, both of which this paper
establishes as a measurement methodology.

**Why TIM (not IEEE Sensors):** the contribution is a *measurement methodology*
and a *rigorous evaluation/characterization* on existing data — not a new sensor
or new measurements. TIM rewards exactly this: measurement-chain analysis,
evaluation rigor, uncertainty, and low-cost instrumentation trade-offs.

---

## Contributions (what we claim)

1. **A deployment-realistic evaluation methodology** for low-rate vibration CM
   that exposes and corrects the optimistic bias of overlapping-window random
   splits (group-aware + cross-speed + cross-load protocols), and quantifies the
   "optimism gap" with statistical rigor.
2. **A systematic accuracy–resource trade-off characterization** across the
   sensing/communication knobs — sampling rate, channel count, window length,
   feature set, quantization, packet loss — yielding Pareto operating points.
3. **A measurement-instrument characterization** of the smartphone MEMS
   accelerometer as a CM sensor: noise floor, effective resolution, usable
   bandwidth, and raw vs gravity-compensated channel value.
4. **An emulated edge-node + communication-feasibility analysis** (link budget +
   deterministic footprint + cycle-accurate MCU latency) showing which
   configurations fit which IoT links/hardware — with no physical hardware.
5. *(Optional)* **Cross-dataset validation** against a public industrial-grade
   accelerometer benchmark downsampled to 100 Hz (low-cost vs reference sensor).

---

## Section structure

- **Abstract** — problem, method, headline numbers (optimism gap; honest
  accuracy; recommended operating point + footprint).
- **Index Terms** — condition monitoring, fault diagnosis, MEMS accelerometer,
  induction motor, edge computing, IoT, low-cost sensing, evaluation methodology,
  measurement uncertainty.
- **I. Introduction** — motivation (low-cost/IoT CM); the two gaps (low-rate MEMS
  feasibility + optimistic evaluation in the literature); contributions.
- **II. Related Work** — (a) vibration-based CM & motor fault diagnosis;
  (b) low-cost/MEMS & smartphone sensing; (c) ML for fault diagnosis and its
  evaluation pitfalls (data leakage from overlapping windows); (d) edge/IoT CM.
- **III. Dataset and Measurement Setup** — the smartphone-MEMS dataset (cite Data
  in Brief + Mendeley DOI): motor, fault set, operating matrix, channels, format.
- **IV. Sensor and Signal Characterization** — noise floor / effective
  resolution; usable-band spectral analysis (the <50 Hz Nyquist wall);
  raw vs gravity-compensated channels; per-channel informativeness. *(Analysis B)*
- **V. Methodology** — measurement pipeline (windowing, feature set, models) and
  the **evaluation protocols** (random vs group-aware vs cross-condition) + the
  statistical-testing plan. *(Analysis A + protocol definitions)*
- **VI. Deployment-Realistic Evaluation Results** — the optimism gap, honest
  accuracies, cross-speed/cross-load generalization, with CIs. *(Analysis C)*
- **VII. Accuracy–Resource Trade-off Characterization** — sampling rate,
  channels, window length, feature set, quantization, packet loss, coupling
  robustness → Pareto fronts + recommended points. *(Analysis D)*
- **VIII. Edge-Node and Communication Feasibility** — link budget (BLE/Zigbee/
  LoRaWAN/NB-IoT), model/feature footprint, emulated Cortex-M latency, energy
  estimate. *(Analysis E)*
- **IX. Cross-Dataset Validation** *(optional)* — downsampled industrial-grade
  benchmark. *(Analysis F)*
- **X. Discussion** — recommended operating points per link class; practical
  guidance; threats to validity; limitations (single motor, discrete faults,
  emulated—not measured—energy).
- **XI. Conclusion & Future Work.**
- **Reproducibility** — released code + fixed seeds + configs.

---

## Target figures/tables (reviewer-facing evidence)

- F1. Measurement pipeline / sensor-to-decision block diagram.
- F2. Sensor characterization: noise floor + PSD usable band.
- F3. Raw vs gravity-compensated diagnostic-value comparison.
- F4. **Optimism gap:** random vs group-aware vs cross-condition accuracy (bars + CI).
- F5. Confusion matrices under the honest protocol.
- F6. **Pareto:** accuracy vs data-rate (sampling), vs bandwidth (channels), vs
  latency (window).
- F7. Quantization + packet-loss robustness curves.
- F8. Coupling/orientation robustness (rotation-augmentation) curves.
- T1. Link-budget table (payload regimes × IoT links).
- T2. Edge footprint table (model size, RAM, emulated latency, energy estimate).
- T3. Recommended operating point per link/hardware class.
