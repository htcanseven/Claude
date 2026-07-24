# Analysis B — Sensor / signal characterization

## Effective resolution (quantisation LSB)

| channel | gX | gY | gZ | gUserX | gUserY | gUserZ |
|---|---|---|---|---|---|---|
| LSB (milli-g) | 0.015 | 0.015 | 0.015 | 0.001 | 0.001 | 0.001 |

Noise-floor PSD (gX, median >30 Hz): 8.23e-08 g²/Hz (-70.8 dB).

## Raw vs gravity-compensated equivalence (Pearson r of AC content)

| pair | gX~gUserX | gY~gUserY | gZ~gUserZ |
|---|---|---|---|
| r | 0.5785 | 0.4569 | 0.4571 |

> The raw and gravity-compensated triads are only **moderately correlated** (r ≈ 0.46–0.58), so iOS `userAcceleration` does more than remove DC — its complementary gravity filter also removes low-frequency content. Consistently, the **raw channels are more diagnostically informative** (higher MI) than the compensated ones, i.e. compensation discards useful low-frequency fault information. The two triads are complementary, not redundant — a concrete sensor-signal finding specific to smartphone-based acquisition.

## Per-channel diagnostic informativeness (mean MI)

| channel | gX | gY | gZ | gUserX | gUserY | gUserZ |
|---|---|---|---|---|---|---|
| mean MI | 0.748 | 0.684 | 0.648 | 0.571 | 0.471 | 0.457 |
