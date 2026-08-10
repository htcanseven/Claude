# Significance & measurement-uncertainty (RF, 200 trees)

Seeds [0, 1, 2, 3, 4]; fixed recording-level 6-fold partition; Type A uncertainty from seed-level repeats (n=5, k=t_{0.975,4}).

## GROUP accuracy with expanded uncertainty

| Config | Accuracy (%) | U95 | reproducibility s (%) |
|---|---|---|---|
| baseline | 52.8 | ±4.4 | 3.5 |
| fs25 | 62.9 | ±2.5 | 2.1 |
| optimal | 75.9 | ±2.8 | 2.2 |

## Paired comparisons (difference over common (seed,fold) test folds)

- **optimal_vs_baseline**: Δ = +23.1 pts (paired t p=8.39e-06, Wilcoxon p=2.08e-05, n=30)
- **fs25_vs_fs100**: Δ = +10.1 pts (paired t p=0.0152, Wilcoxon p=0.0093, n=30)
