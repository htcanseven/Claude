# Sensitivity of M3 and M4 to the learner and its settings

Settings: reference: {'max_depth': 3, 'max_iter': 200, 'learning_rate': 0.08, 'random_state': 0}; regularised: {'max_depth': 2, 'max_iter': 100, 'learning_rate': 0.05, 'l2_regularization': 1.0, 'random_state': 0}; flexible: {'max_depth': 6, 'max_iter': 400, 'learning_rate': 0.1, 'min_samples_leaf': 10, 'random_state': 0}; ridge: ridge (alpha 1); quantile: {'max_depth': 3, 'max_iter': 200, 'learning_rate': 0.08, 'random_state': 0, 'loss': 'quantile', 'quantile': 0.95}; selected: the boosting setting with the smallest mean absolute leave-one-out error over the calibration alternatives.

Reference setting reproduces the stored intervals: True (756 cases).

## Decisive and safe distances over all characteristics (floors)

| scope                 | rule   | setting     |   resolution_floors |   safe_floors |   resolution_failing |   safe_failing |
|:----------------------|:-------|:------------|--------------------:|--------------:|---------------------:|---------------:|
| setting               | M3     | flexible    |               35.5  |         14.2  |                23.25 |          12.65 |
| setting               | M3     | quantile    |               29.5  |         17.5  |                29    |          18.6  |
| setting               | M3     | reference   |               31.5  |         15.8  |                21.5  |          12.4  |
| setting               | M3     | regularised |               26.15 |         14.6  |                23    |          11.25 |
| setting               | M3     | ridge       |               33.3  |          9.6  |                29.25 |           6.65 |
| setting               | M3     | selected    |               26.4  |         17.15 |                20.4  |          13.7  |
| setting               | M4     | flexible    |               13.55 |          7.75 |                12.15 |           9.05 |
| setting               | M4     | quantile    |               14.6  |          8.5  |                13.15 |           9.15 |
| setting               | M4     | reference   |               13.35 |          7.9  |                12.4  |           9.05 |
| setting               | M4     | regularised |               12.95 |          7.7  |                12.2  |           9.05 |
| setting               | M4     | ridge       |               14.75 |          4.9  |                13.85 |           6.55 |
| setting               | M4     | selected    |               13.1  |          8.2  |                12.2  |           9.05 |
| setting/extrapolation | M3     | flexible    |               37    |         14.05 |                31.7  |          12.65 |
| setting/extrapolation | M3     | quantile    |               29.65 |         17.6  |                25.15 |          18.9  |
| setting/extrapolation | M3     | reference   |               31.5  |         16.1  |                20.7  |          12.4  |
| setting/extrapolation | M3     | regularised |               26.45 |         14.8  |                23    |          11.25 |
| setting/extrapolation | M3     | ridge       |               33.3  |         12.05 |                31    |           9.4  |
| setting/extrapolation | M3     | selected    |               25.25 |         17.25 |                20.4  |          13.7  |
| setting/extrapolation | M4     | flexible    |               12.8  |          7.6  |                14.55 |           9.9  |
| setting/extrapolation | M4     | quantile    |               14.8  |          8.35 |                13.5  |           9.9  |
| setting/extrapolation | M4     | reference   |               12.55 |          7.55 |                14.7  |           9.85 |
| setting/extrapolation | M4     | regularised |               12.5  |          7.75 |                12.5  |           9.8  |
| setting/extrapolation | M4     | ridge       |               15.8  |          5.8  |                14.25 |           7.95 |
| setting/extrapolation | M4     | selected    |               12.55 |          7.7  |                14.55 |           9.8  |
| setting/interpolation | M3     | flexible    |               34.2  |         15.6  |                19.05 |          13.8  |
| setting/interpolation | M3     | quantile    |               25.35 |         12.2  |                30    |          17.6  |
| setting/interpolation | M3     | reference   |               30.6  |         14.75 |                21.85 |          14.3  |
| setting/interpolation | M3     | regularised |               25.5  |         14.15 |                22.3  |          13.2  |
| setting/interpolation | M3     | ridge       |               30.5  |          0.25 |                20.5  |           0    |
| setting/interpolation | M3     | selected    |               30.6  |         15.6  |                18.6  |          14.3  |
| setting/interpolation | M4     | flexible    |               13.9  |          8.9  |                10.05 |           0    |
| setting/interpolation | M4     | quantile    |               14.6  |          8.55 |                13.15 |           0    |
| setting/interpolation | M4     | reference   |               14.75 |          8.45 |                10.15 |           0    |
| setting/interpolation | M4     | regularised |               13.35 |          6.8  |                10.6  |           0    |
| setting/interpolation | M4     | ridge       |                9.95 |          2.25 |                10.2  |           1.45 |
| setting/interpolation | M4     | selected    |               13.5  |          8.9  |                10.6  |           0    |
| transfer              | M3     | flexible    |               46.95 |         26.15 |                46.85 |          17.2  |
| transfer              | M3     | quantile    |               50.4  |         26.6  |                48.6  |          27.55 |
| transfer              | M3     | reference   |               48.3  |         21.95 |                46.95 |          17.7  |
| transfer              | M3     | regularised |               50.4  |         26.55 |                47.6  |          21.35 |
| transfer              | M3     | ridge       |               50.4  |         21.2  |                47.9  |           9.9  |
| transfer              | M3     | selected    |               47.2  |         26    |                46.95 |          17.7  |
| transfer              | M4     | flexible    |              133.05 |        128.55 |               170.8  |         166.6  |
| transfer              | M4     | quantile    |              133.05 |        128.85 |               171.25 |         165.95 |
| transfer              | M4     | reference   |              133    |        128.35 |               170.9  |         164.65 |
| transfer              | M4     | regularised |              133    |        128.5  |               170.75 |         166    |
| transfer              | M4     | ridge       |              132.6  |        127.65 |               172.1  |         166.2  |
| transfer              | M4     | selected    |              133.05 |        128.55 |               170.75 |         166    |
| within                | M3     | flexible    |               23.15 |          0    |                21.45 |           0    |
| within                | M3     | quantile    |               18.4  |          0    |                17.45 |           0    |
| within                | M3     | reference   |               17.45 |          0    |                16.4  |           0    |
| within                | M3     | regularised |               19.75 |          0.25 |                19.2  |           0.25 |
| within                | M3     | ridge       |               27.75 |          0.4  |                25.35 |           0.15 |
| within                | M3     | selected    |               16.2  |          0.25 |                16.2  |           0.15 |
| within                | M4     | flexible    |               10.85 |          0.6  |                10.85 |           0.2  |
| within                | M4     | quantile    |               11.2  |          0.5  |                10.65 |           0.3  |
| within                | M4     | reference   |               11.25 |          0.6  |                11.25 |           0.45 |
| within                | M4     | regularised |               11.25 |          0.4  |                12.05 |           0    |
| within                | M4     | ridge       |               12.05 |          0.25 |                13.75 |           0    |
| within                | M4     | selected    |               11    |          0.6  |                11    |           0.45 |

## Settings chosen by the inner leave-one-out (design cases)

|                    |   flexible |   reference |   regularised |
|:-------------------|-----------:|------------:|--------------:|
| ('setting', 'M3')  |         78 |          33 |            15 |
| ('setting', 'M4')  |         51 |          21 |            54 |
| ('transfer', 'M3') |         72 |          45 |             9 |
| ('transfer', 'M4') |         54 |          36 |            36 |
| ('within', 'M3')   |         47 |          43 |            36 |
| ('within', 'M4')   |         48 |          36 |            42 |
