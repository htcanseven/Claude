# A3 - recording-level statistics (GROUP, RF-200, 10 seeds)

| configuration | accuracy (%) | macro-F1 (%) |
|---|---|---|
| Baseline (100 Hz, 6 ch, 2 s) | 53.9 +/- 12.5 | 49.1 |
| 25 Hz, 6 ch, 2 s | 63.2 +/- 11.6 | 59.2 |
| Frugal (25 Hz, 3 raw ch, 4 s) | 75.0 +/- 11.4 | 71.1 |

Intervals are 95% clustered on recording (n=36).

## Paired permutation tests on per-recording differences

- frugal_vs_baseline: +21.1 points, p = 0.0198 (n = 36)
- fs25_vs_baseline: +9.4 points, p = 0.2577 (n = 36)
