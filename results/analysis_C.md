# Analysis C — Deployment-realistic evaluation

Features: 84 (full set, 6 channels) · windows: 32328 · 2 s / 50% · 100 Hz · seed 0

## Accuracy by protocol (mean ± std over folds)

| Protocol | folds | RF | KNN | SVM |
|---|---|---|---|---|
| RANDOM (leaky) | 5 | 100.00 ± 0.00 | 100.00 ± 0.00 | 100.00 ± 0.01 |
| GROUP (recording-holdout) | 6 | 47.60 ± 7.87 | 63.26 ± 11.84 | 53.23 ± 12.21 |
| CROSS-SPEED (LOSpeedO) | 3 | 49.40 ± 11.20 | 48.24 ± 9.09 | 49.67 ± 12.93 |
| CROSS-LOAD (LOLoadO) | 2 | 50.13 ± 4.75 | 40.26 ± 0.88 | 40.10 ± 2.04 |

## Optimism gap  (RANDOM − GROUP), accuracy points

| Model | RANDOM | GROUP | gap |
|---|---|---|---|
| RF | 100.00 | 47.60 | **+52.40** |
| KNN | 100.00 | 63.26 | **+36.74** |
| SVM | 100.00 | 53.23 | **+46.77** |

## Macro-F1 by protocol (mean over folds)

| Protocol | RF | KNN | SVM |
|---|---|---|---|
| RANDOM (leaky) | 100.00 | 100.00 | 100.00 |
| GROUP (recording-holdout) | 39.09 | 58.64 | 46.84 |
| CROSS-SPEED (LOSpeedO) | 41.02 | 41.92 | 44.03 |
| CROSS-LOAD (LOLoadO) | 45.69 | 40.11 | 40.57 |

