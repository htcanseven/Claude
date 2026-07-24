# Hardening — multi-seed + combined operating point

Seeds: [0, 1, 2, 3, 4] · GROUP protocol (StratifiedGroupKFold-6) · means pooled over seeds×folds.

## Incremental frugal recipe (does it stack?)

| configuration | RF | KNN | LogReg |
|---|---|---|---|
| baseline: 100Hz/6ch/2s | 53.7 ± 13.4 | 61.1 ± 11.7 | 57.0 ± 11.7 |
| + 25 Hz | 64.9 ± 15.7 | 46.7 ± 12.9 | 59.0 ± 13.9 |
| + raw-3ch | 65.1 ± 15.2 | 52.8 ± 15.5 | 55.1 ± 14.8 |
| + 4 s window (optimal) | 74.2 ± 16.6 | 55.0 ± 19.2 | 62.6 ± 16.4 |

## Sampling-rate sweep (multi-seed, RF)

| fs (Hz) | acc | ±std |
|---|---|---|
| 100 | 53.7 | 13.4 |
| 50 | 42.0 | 12.8 |
| 25 | 64.9 | 15.7 |
| 20 | 61.6 | 16.8 |
| 12.5 | 59.1 | 14.9 |
| 10 | 59.7 | 13.7 |
