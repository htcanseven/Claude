# Analysis D — Accuracy-resource trade-offs (GROUP protocol, RF)

Baseline (100 Hz, 6ch, 2 s, full features): **46.4 ± 10.9%** GROUP accuracy.

## D1 · Sampling rate

| fs (Hz) | raw kbps | acc | ±std | F1 |
|---|---|---|---|---|
| 100 | 9.6 | 46.4 | 10.9 | 38.3 |
| 50 | 4.8 | 43.7 | 8.0 | 39.2 |
| 25 | 2.4 | 66.7 | 19.0 | 62.5 |
| 20 | 1.9 | 62.7 | 22.0 | 58.7 |
| 12.5 | 1.2 | 56.4 | 6.0 | 49.9 |
| 10 | 1.0 | 59.5 | 16.7 | 53.5 |

## D2 · Channel subset

| subset | #ch | raw kbps | acc | ±std |
|---|---|---|---|---|
| all6 | 6 | 9.6 | 46.4 | 10.9 |
| raw3 | 3 | 4.8 | 56.7 | 7.4 |
| user3 | 3 | 4.8 | 41.3 | 12.5 |
| gUserZ | 1 | 1.6 | 37.2 | 15.3 |
| gUserX | 1 | 1.6 | 29.3 | 10.8 |
| gUserY | 1 | 1.6 | 23.7 | 13.5 |

## D3 · Window length

| window (s) | latency (s) | acc | ±std |
|---|---|---|---|
| 4.0 | 4.0 | 63.3 | 11.0 |
| 2.0 | 2.0 | 46.4 | 10.9 |
| 1.0 | 1.0 | 52.0 | 8.3 |
| 0.5 | 0.5 | 49.7 | 7.1 |

## D4 · Feature set

| set | #feat | acc | ±std |
|---|---|---|---|
| full | 84 | 46.4 | 10.9 |
| paper6 | 36 | 45.3 | 11.0 |

## D5 · Quantization

| bits | acc | ±std |
|---|---|---|
| 32 | 46.4 | 10.9 |
| 8 | 50.0 | 10.2 |
| 6 | 48.0 | 10.8 |
| 4 | 44.7 | 8.0 |

## D6 · Packet loss

| loss | acc | ±std |
|---|---|---|
| 0% | 46.4 | 10.9 |
| 5% | 46.8 | 11.0 |
| 10% | 47.0 | 11.9 |
| 20% | 46.5 | 10.6 |

## D7 · Mounting/coupling robustness (train 0°, test rotated)

| rotation (deg) | acc | ±std |
|---|---|---|
| 0 | 46.4 | 10.9 |
| 5 | 45.3 | 13.0 |
| 10 | 37.9 | 8.7 |
| 20 | 33.8 | 12.0 |
| 30 | 31.4 | 13.2 |
