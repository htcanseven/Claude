# A2 - band-limiting vs sampling rate (GROUP protocol, RF-200, 5 seeds)

| condition | windows | accuracy (%) | macro-F1 (%) |
|---|---|---|---|
| 100 Hz, unmodified | 32328 | 52.8 +/- 13.2 | 48.4 |
| 100 Hz, low-pass 12.5 Hz | 32328 | 50.1 +/- 13.5 | 45.1 |
| 25 Hz, anti-alias decimation | 32364 | 62.9 +/- 12.3 | 58.6 |
| 25 Hz, no anti-alias filter | 32364 | 38.0 +/- 13.1 | 32.2 |

## Decomposition

- band-limiting alone (a->b): -2.7 points
- rate/sample-count (b->c):   +12.8 points
- aliasing (c->d):            -24.9 points
- total (a->c):               +10.1 points
