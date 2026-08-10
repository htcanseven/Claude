# Reconciled tables (fixed recording partition, RF200, 5 seeds, mean +/- U95)

## Table VI optimism
| Protocol | RF | KNN | SVM |
|---|---|---|---|
| RANDOM | 100.0 $\pm$ 0.0 | 100.0 $\pm$ 0.0 | 100.0 $\pm$ 0.0 |
| GROUP | 52.8 $\pm$ 4.4 | 59.0 $\pm$ 1.4 | 58.4 $\pm$ 3.6 |
| CROSS-SPEED | 49.9 $\pm$ 1.3 | 48.2 $\pm$ 0.0 | 50.1 $\pm$ 1.0 |
| CROSS-LOAD | 49.5 $\pm$ 2.7 | 40.3 $\pm$ 0.0 | 40.1 $\pm$ 0.5 |

## Table VII sampling (RF GROUP)
| Rate (Hz) | kbps | Accuracy |
|---|---|---|
| 100 | 9.6 | 52.8 $\pm$ 4.4 |
| 50 | 4.8 | 39.2 $\pm$ 3.5 |
| 25 | 2.4 | 62.9 $\pm$ 2.5 |
| 20 | 1.9 | 60.9 $\pm$ 6.0 |
| 12.5 | 1.2 | 60.9 $\pm$ 3.2 |
| 10 | 1.0 | 58.8 $\pm$ 0.9 |

## Table VIII recipe
| Configuration | RF | KNN | LogReg |
|---|---|---|---|
| Baseline (100 Hz, 6 ch, 2 s) | 52.8 $\pm$ 4.4 | 59.0 $\pm$ 1.4 | 59.6 $\pm$ 2.8 |
| + 25 Hz | 62.9 $\pm$ 2.5 | 46.5 $\pm$ 2.0 | 57.3 $\pm$ 1.7 |
| + raw 3 ch | 65.6 $\pm$ 1.8 | 51.4 $\pm$ 1.7 | 52.5 $\pm$ 2.3 |
| + 4 s window (optimal) | 75.9 $\pm$ 2.8 | 54.9 $\pm$ 2.7 | 60.3 $\pm$ 3.9 |
