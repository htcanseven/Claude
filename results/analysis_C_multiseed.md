# Analysis C (multi-seed) — optimism gap

Seeds [0, 1, 2, 3, 4]; means pooled over seeds x folds. 100 Hz, 6 ch, 2 s, full features.

## Accuracy (%)

| Protocol | RF | KNN | SVM |
|---|---|---|---|
| RANDOM | 100.0 ± 0.0 | 100.0 ± 0.0 | 100.0 ± 0.0 |
| GROUP | 54.3 ± 12.3 | 61.1 ± 11.7 | 57.6 ± 14.1 |
| CROSS-SPEED | 50.0 ± 11.3 | 48.2 ± 9.1 | 50.1 ± 12.6 |
| CROSS-LOAD | 49.3 ± 5.3 | 40.3 ± 0.9 | 40.1 ± 1.9 |

## Macro-F1 (%)

| Protocol | RF | KNN | SVM |
|---|---|---|---|
| RANDOM | 100.0 | 100.0 | 100.0 |
| GROUP | 48.1 | 55.8 | 51.6 |
| CROSS-SPEED | 41.6 | 41.9 | 44.3 |
| CROSS-LOAD | 44.4 | 40.1 | 40.4 |

## Optimism gap (RANDOM − GROUP), accuracy points

- RF: 100.0 → 54.3  (**+45.7**)
- KNN: 100.0 → 61.1  (**+38.9**)
- SVM: 100.0 → 57.6  (**+42.4**)
