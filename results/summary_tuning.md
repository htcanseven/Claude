# Sensitivity of M3 and M4 to the learner and its settings

Settings: reference: {'max_depth': 3, 'max_iter': 200, 'learning_rate': 0.08, 'random_state': 0}; regularised: {'max_depth': 2, 'max_iter': 100, 'learning_rate': 0.05, 'l2_regularization': 1.0, 'random_state': 0}; flexible: {'max_depth': 6, 'max_iter': 400, 'learning_rate': 0.1, 'min_samples_leaf': 10, 'random_state': 0}; ridge: ridge (alpha 1); quantile: {'max_depth': 3, 'max_iter': 200, 'learning_rate': 0.08, 'random_state': 0, 'loss': 'quantile', 'quantile': 0.95}; selected: the boosting setting with the smallest mean absolute leave-one-out error over the calibration alternatives.

Reference setting reproduces the stored intervals: True (756 cases).

## Decisive and safe distances over all characteristics (floors)

| scope                 | rule   | setting     |   resolution_floors |   safe_floors |   resolution_failing |   safe_failing |
|:----------------------|:-------|:------------|--------------------:|--------------:|---------------------:|---------------:|
| setting               | M3     | flexible    |               35.7  |         13.35 |                22.85 |          11.95 |
| setting               | M3     | quantile    |               30.3  |         15.35 |                29.95 |          18.4  |
| setting               | M3     | reference   |               30.7  |         16    |                22.2  |          12.6  |
| setting               | M3     | regularised |               26.8  |         13.65 |                23.45 |          10.35 |
| setting               | M3     | ridge       |               36.75 |          7.75 |                36.45 |           4.6  |
| setting               | M3     | selected    |               28.4  |         16.75 |                22.15 |          12.95 |
| setting               | M4     | flexible    |               13.5  |          7.6  |                12.2  |           9.15 |
| setting               | M4     | quantile    |               14.6  |          8.5  |                13.05 |           9.1  |
| setting               | M4     | reference   |               13.3  |          7.4  |                12.65 |           9.15 |
| setting               | M4     | regularised |               13.4  |          7.65 |                13.05 |           9.15 |
| setting               | M4     | ridge       |               16.15 |          4.95 |                14    |           5.6  |
| setting               | M4     | selected    |               13.05 |          7.75 |                12.35 |           9.15 |
| setting/extrapolation | M3     | flexible    |               39.75 |         14.25 |                22.85 |          11.8  |
| setting/extrapolation | M3     | quantile    |               30.45 |         17.3  |                25.95 |          19.2  |
| setting/extrapolation | M3     | reference   |               32.85 |         16.95 |                22.15 |          12.6  |
| setting/extrapolation | M3     | regularised |               27.3  |         14.85 |                23.15 |          11.35 |
| setting/extrapolation | M3     | ridge       |               37    |         11.5  |                38.45 |           7.75 |
| setting/extrapolation | M3     | selected    |               28.2  |         17.05 |                21.95 |          12.95 |
| setting/extrapolation | M4     | flexible    |               12.85 |          7.6  |                13.9  |           9.95 |
| setting/extrapolation | M4     | quantile    |               14.9  |          8.4  |                13.05 |           9.9  |
| setting/extrapolation | M4     | reference   |               13.05 |          7.8  |                13.6  |           9.85 |
| setting/extrapolation | M4     | regularised |               14    |          7.9  |                13.4  |           9.85 |
| setting/extrapolation | M4     | ridge       |               19.25 |          5.55 |                15.95 |           6.45 |
| setting/extrapolation | M4     | selected    |               13.05 |          7.9  |                13.3  |           9.85 |
| setting/interpolation | M3     | flexible    |               33.65 |         13.35 |                22.15 |          13.15 |
| setting/interpolation | M3     | quantile    |               28    |          9.6  |                30.3  |          15.35 |
| setting/interpolation | M3     | reference   |               29.05 |         13.35 |                22.6  |          13.2  |
| setting/interpolation | M3     | regularised |               26    |          9.2  |                26    |           9.2  |
| setting/interpolation | M3     | ridge       |               28.8  |          1.65 |                26.2  |           0.95 |
| setting/interpolation | M3     | selected    |               29.05 |         13.35 |                22.6  |          13.2  |
| setting/interpolation | M4     | flexible    |               13.8  |          7.5  |                10.1  |           0    |
| setting/interpolation | M4     | quantile    |               14.6  |          8.55 |                13.05 |           0    |
| setting/interpolation | M4     | reference   |               14.7  |          7    |                10.35 |           0    |
| setting/interpolation | M4     | regularised |               13.25 |          7    |                10.6  |           0    |
| setting/interpolation | M4     | ridge       |               10.65 |          2.55 |                11.55 |           2.2  |
| setting/interpolation | M4     | selected    |               13.6  |          7.5  |                10.4  |           0    |
| transfer              | M3     | flexible    |               48.7  |         25.75 |                47.9  |          19.9  |
| transfer              | M3     | quantile    |               50.4  |         27.15 |                48.6  |          31.8  |
| transfer              | M3     | reference   |               48.75 |         20.5  |                47.7  |          19.9  |
| transfer              | M3     | regularised |               49.3  |         26.3  |                47.9  |          23    |
| transfer              | M3     | ridge       |               51.2  |         20.6  |                47.9  |           8.9  |
| transfer              | M3     | selected    |               48.6  |         25.75 |                47.7  |          19.9  |
| transfer              | M4     | flexible    |              133.1  |        128.65 |               171.3  |         165.9  |
| transfer              | M4     | quantile    |              133.1  |        128.9  |               171.25 |         166    |
| transfer              | M4     | reference   |              133.1  |        128.45 |               170.9  |         163.95 |
| transfer              | M4     | regularised |              132.9  |        128.45 |               170.55 |         165.5  |
| transfer              | M4     | ridge       |              132.85 |        127.85 |               172.3  |         166.35 |
| transfer              | M4     | selected    |              133.1  |        128.65 |               170.55 |         165.5  |
| within                | M3     | flexible    |               27.4  |          0.05 |                20.2  |           0    |
| within                | M3     | quantile    |               26.1  |          0    |                27.85 |           0    |
| within                | M3     | reference   |               23.05 |          0    |                16.15 |           0    |
| within                | M3     | regularised |               22.95 |          0.3  |                21.35 |           0.3  |
| within                | M3     | ridge       |               32.3  |          0.35 |                30.85 |           0.35 |
| within                | M3     | selected    |               19.85 |          0.05 |                16.4  |           0    |
| within                | M4     | flexible    |               11.15 |          0.1  |                11.15 |           0    |
| within                | M4     | quantile    |               11.85 |          0.15 |                11.05 |           0    |
| within                | M4     | reference   |               11.3  |          0.05 |                11.3  |           0    |
| within                | M4     | regularised |               12.6  |          0.05 |                13.3  |           0    |
| within                | M4     | ridge       |               12.7  |          0    |                16.15 |           0    |
| within                | M4     | selected    |               11.75 |          0.05 |                12.35 |           0    |

## Settings chosen by the inner leave-one-out (design cases)

|                    |   flexible |   reference |   regularised |
|:-------------------|-----------:|------------:|--------------:|
| ('setting', 'M3')  |         78 |          33 |            15 |
| ('setting', 'M4')  |         51 |          21 |            54 |
| ('transfer', 'M3') |         72 |          45 |             9 |
| ('transfer', 'M4') |         54 |          36 |            36 |
| ('within', 'M3')   |         47 |          43 |            36 |
| ('within', 'M4')   |         48 |          36 |            42 |
