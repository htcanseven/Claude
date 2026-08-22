# A1 - decomposition of the optimism gap (RF-200, 5 seeds)

| partitioning | leakage sources retained | accuracy (%) | macro-F1 (%) |
|---|---|---|---|
| RANDOM, 50% overlap | shared samples, proximity, recording identity | 100.0 +/- 0.0 | 100.0 |
| RANDOM, no overlap | proximity, recording identity | 100.0 +/- 0.0 | 100.0 |
| BLOCKED within recording | recording identity | 100.0 +/- 0.0 | 100.0 |
| GROUP, no overlap | none | 53.3 +/- 13.2 | 49.1 |
| GROUP, 50% overlap | none | 52.8 +/- 13.2 | 48.4 |
| CROSS-SPEED | none, + speed shift | 49.9 +/- 15.5 | 41.5 |
| CROSS-LOAD | none, + load shift | 49.5 +/- 15.2 | 44.5 |

## Attribution (successive differences)

- window overlap (shared samples): +0.0 points
- temporal proximity:              +0.0 points
- recording identity:              +46.7 points
- total optimism gap:              +46.7 points
