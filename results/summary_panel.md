# Analyses requested in review

## decomposition

| rule_set                | distance          | relations         |   rules |   share_relation |   share_rule |   share_interaction | best_rule_range    | new_family_floor        |
|:------------------------|:------------------|:------------------|--------:|-----------------:|-------------:|--------------------:|:-------------------|:------------------------|
| eleven calibrated rules | resolution_floors | all relations     |      11 |            0.686 |        0.06  |               0.254 | [8.45, 35.3, 3.35] | new family's floor      |
| eleven calibrated rules | resolution_floors | within the family |      11 |            0.148 |        0.681 |               0.17  | [8.45, 3.35]       | new family's floor      |
| eleven calibrated rules | safe_floors       | all relations     |      11 |            0.658 |        0.153 |               0.189 |                    | new family's floor      |
| eleven calibrated rules | safe_floors       | within the family |      11 |            0.353 |        0.517 |               0.13  |                    | new family's floor      |
| with M1sn               | resolution_floors | all relations     |      12 |            0.696 |        0.063 |               0.241 | [8.15, 35.3, 3.35] | new family's floor      |
| with M1sn               | resolution_floors | within the family |      12 |            0.147 |        0.712 |               0.141 | [8.15, 3.35]       | new family's floor      |
| with M1sn               | safe_floors       | all relations     |      12 |            0.678 |        0.143 |               0.18  |                    | new family's floor      |
| with M1sn               | safe_floors       | within the family |      12 |            0.352 |        0.513 |               0.135 |                    | new family's floor      |
| eleven calibrated rules | resolution_floors | all relations     |      11 |            0.665 |        0.062 |               0.273 | [8.45, 32.9, 3.35] | produced family's floor |
| eleven calibrated rules | resolution_floors | within the family |      11 |            0.148 |        0.681 |               0.17  | [8.45, 3.35]       | produced family's floor |
| eleven calibrated rules | safe_floors       | all relations     |      11 |            0.673 |        0.144 |               0.182 |                    | produced family's floor |
| eleven calibrated rules | safe_floors       | within the family |      11 |            0.353 |        0.517 |               0.13  |                    | produced family's floor |
| with M1sn               | resolution_floors | all relations     |      12 |            0.678 |        0.064 |               0.257 | [8.15, 32.9, 3.35] | produced family's floor |
| with M1sn               | resolution_floors | within the family |      12 |            0.147 |        0.712 |               0.141 | [8.15, 3.35]       | produced family's floor |
| with M1sn               | safe_floors       | all relations     |      12 |            0.691 |        0.135 |               0.174 |                    | produced family's floor |
| with M1sn               | safe_floors       | within the family |      12 |            0.352 |        0.513 |               0.135 |                    | produced family's floor |

## sibling_strata

|   resolved_siblings | method   |   cases |   resolution_floors |   safe_floors |   resolution_adequate |   safe_adequate |   resolution_failing |   safe_failing |   abs_error_p90 |
|--------------------:|:---------|--------:|--------------------:|--------------:|----------------------:|----------------:|---------------------:|---------------:|----------------:|
|                   0 | M0       |      58 |              115.1  |        115.1  |                115.15 |          115.15 |                26.95 |          26.95 |         110.955 |
|                   0 | M1       |      58 |               14.6  |         14.6  |                 17.85 |           17.85 |                13.8  |          13.8  |          17.355 |
|                   0 | M1n      |      58 |                9.2  |          9.2  |                  4.55 |            4.55 |                 9.4  |           9.4  |           9.06  |
|                   0 | M1s      |      58 |                6.85 |          6.85 |                  7.65 |            7.65 |                 6.85 |           6.85 |           6.149 |
|                   0 | M1sn     |      58 |                3.05 |          3.05 |                  3.3  |            3.3  |                 2.25 |           2.25 |           2.928 |
|                   0 | M2       |      58 |               22.45 |          0    |                 26.85 |            0    |                15.45 |           0    |           7.723 |
|                   0 | M2n      |      58 |               18.75 |          0    |                 19.6  |            0    |                18.75 |           0    |           9.06  |
|                   0 | M3       |      58 |               26.95 |          0    |                 35.75 |            0    |                14.6  |           0    |          11.438 |
|                   0 | M4       |      58 |                8.1  |          0    |                  7.4  |            0    |                 9.45 |           0    |           1.113 |
|                   0 | M5       |      58 |                6.05 |          0    |                  6.45 |            0    |                 5.8  |           0    |           1.39  |
|                   0 | M5n      |      58 |                5.15 |          0    |                  4.8  |            0    |                 5.9  |           0    |           0.91  |
|                   0 | NN       |      58 |                0.85 |          0.85 |                  0.9  |            0.9  |                 0.75 |           0.75 |           0.788 |
|                   1 | M0       |      34 |               74.8  |         74.8  |                101    |          101    |                13.85 |          13.85 |          69.813 |
|                   1 | M1       |      34 |               15.6  |         15.6  |                 19.95 |           19.95 |                15.6  |          15.6  |          18.863 |
|                   1 | M1n      |      34 |               10.25 |         10.25 |                  3.65 |            3.65 |                14.85 |          14.85 |           9.374 |
|                   1 | M1s      |      34 |                5    |          5    |                  4.85 |            4.85 |                 9    |           9    |           4.933 |
|                   1 | M1sn     |      34 |                3.8  |          3.8  |                  2.6  |            2.6  |                 4.55 |           4.55 |           3.687 |
|                   1 | M2       |      34 |               24.95 |          0.3  |                 24.95 |            0.05 |                27.65 |           0.5  |          13.026 |
|                   1 | M2n      |      34 |               21.3  |          0.3  |                 14    |            0    |                29.95 |           0.55 |           9.374 |
|                   1 | M3       |      34 |               18.25 |          0    |                 21.65 |            0    |                17    |           0    |           7.57  |
|                   1 | M4       |      34 |               11.3  |          0    |                  6.85 |            0    |                14.05 |           0    |           3.363 |
|                   1 | M5       |      34 |                6.1  |          0    |                  4.55 |            0    |                 8.3  |           0.2  |           2.451 |
|                   1 | M5n      |      34 |                7.15 |          0.2  |                  5.7  |            0    |                 7.85 |           0.35 |           2.867 |
|                   1 | NN       |      34 |                2.45 |          2.45 |                  1.4  |            1.4  |                 3.4  |           3.4  |           2.298 |
|                   2 | M0       |      34 |               95.85 |         95.85 |                 99.1  |           99.1  |                10.15 |          10.15 |          86.837 |
|                   2 | M1       |      34 |               15.9  |         15.9  |                  7.9  |            7.9  |                18.5  |          18.5  |          15.685 |
|                   2 | M1n      |      34 |                6.95 |          6.95 |                  7.25 |            7.25 |                 3.4  |           3.4  |           6.785 |
|                   2 | M1s      |      34 |                4.6  |          4.6  |                  4.8  |            4.8  |                 4.3  |           4.3  |           4.547 |
|                   2 | M1sn     |      34 |                4.45 |          4.45 |                  4.9  |            4.9  |                 3.5  |           3.5  |           4.298 |
|                   2 | M2       |      34 |               14.75 |          1.35 |                 13.6  |            1.35 |                18.85 |           1.4  |           7.875 |
|                   2 | M2n      |      34 |               17.1  |          1.05 |                 17.1  |            2.15 |                11.8  |           0    |           6.785 |
|                   2 | M3       |      34 |               17    |          0.05 |                 17.5  |            1.35 |                15.1  |           0    |           8.19  |
|                   2 | M4       |      34 |               13.2  |          2.95 |                 13.2  |            3.45 |                14.6  |           1.1  |           5.994 |
|                   2 | M5       |      34 |                9.65 |          2.25 |                 11.05 |            3.6  |                 9.65 |           2.25 |           4.795 |
|                   2 | M5n      |      34 |                8.7  |          2.9  |                  9.8  |            3.05 |                 8.35 |           1.55 |           4.82  |
|                   2 | NN       |      34 |                4.85 |          4.85 |                  5.1  |            5.1  |                 4.45 |           4.45 |           4.775 |

## force_levels

|   bhf_kN | relation      | method   |   cases |   resolution_floors |   safe_floors |   resolution_adequate |   safe_adequate |   resolution_failing |   safe_failing |
|---------:|:--------------|:---------|--------:|--------------------:|--------------:|----------------------:|----------------:|---------------------:|---------------:|
|      100 | extrapolation | M0       |      42 |              105.55 |        105.55 |                114.65 |          114.65 |                11.55 |          11.55 |
|      100 | extrapolation | M1       |      42 |               24.6  |         24.6  |                 26.6  |           26.6  |                11    |          11    |
|      100 | extrapolation | M1n      |      42 |               12.6  |         12.6  |                  3.75 |            3.75 |                17.1  |          17.1  |
|      100 | extrapolation | M1s      |      42 |               14.7  |         14.7  |                  5.65 |            5.65 |                21.05 |          21.05 |
|      100 | extrapolation | M1sn     |      42 |                8.85 |          8.85 |                  7.35 |            7.35 |                 9.85 |           9.85 |
|      100 | extrapolation | M2       |      42 |               16.75 |          8.1  |                 16.75 |            6.7  |                14.85 |          12.95 |
|      100 | extrapolation | M2n      |      42 |               15.5  |          9.9  |                  7.2  |            0.75 |                20.35 |          13.8  |
|      100 | extrapolation | M3       |      42 |               40.05 |         18.2  |                 40.4  |           18.5  |                22.15 |           3    |
|      100 | extrapolation | M4       |      42 |               13.3  |          9.85 |                 11.9  |            1.6  |                15.95 |          13.8  |
|      100 | extrapolation | M5       |      42 |               17.5  |          8.1  |                 18.5  |            5.45 |                15.85 |          13.25 |
|      100 | extrapolation | M5n      |      42 |               16    |          9.7  |                  7.7  |            1.25 |                21.45 |          13.15 |
|      100 | extrapolation | NN       |      42 |               11    |         11    |                  5    |            5    |                14.8  |          14.8  |
|      300 | interpolation | M0       |      42 |              108.6  |        108.6  |                115.1  |          115.1  |                17    |          17    |
|      300 | interpolation | M1       |      42 |               11.25 |         11.25 |                 11.3  |           11.3  |                 9.2  |           9.2  |
|      300 | interpolation | M1n      |      42 |                4.8  |          4.8  |                  4.8  |            4.8  |                 5.8  |           5.8  |
|      300 | interpolation | M1s      |      42 |               19.25 |         19.25 |                 18.7  |           18.7  |                30.4  |          30.4  |
|      300 | interpolation | M1sn     |      42 |                4.65 |          4.65 |                  4.65 |            4.65 |                 3.1  |           3.1  |
|      300 | interpolation | M2       |      42 |               17.75 |          2.7  |                 24.95 |            2.4  |                15.45 |           3.65 |
|      300 | interpolation | M2n      |      42 |               13.3  |          0    |                 15.05 |            0    |                10    |           0    |
|      300 | interpolation | M3       |      42 |               29.05 |         13.35 |                 30.65 |           13.35 |                22.6  |          13.2  |
|      300 | interpolation | M4       |      42 |               14.7  |          7    |                 18.95 |            8.75 |                10.35 |           0    |
|      300 | interpolation | M5       |      42 |               19.05 |          2.8  |                 32.6  |            3.1  |                18.65 |           2.4  |
|      300 | interpolation | M5n      |      42 |               15.6  |          0    |                 19.45 |            0    |                11.1  |           0    |
|      300 | interpolation | NN       |      42 |                4.65 |          4.65 |                  4.65 |            4.65 |                 3.1  |           3.1  |
|      500 | extrapolation | M0       |      42 |               99.1  |         99.1  |                108.35 |          108.35 |                27.5  |          27.5  |
|      500 | extrapolation | M1       |      42 |               23.8  |         23.8  |                 21.75 |           21.75 |                25.35 |          25.35 |
|      500 | extrapolation | M1n      |      42 |                9.8  |          9.8  |                 10.85 |           10.85 |                 2.75 |           2.75 |
|      500 | extrapolation | M1s      |      42 |               19.15 |         19.15 |                 18.35 |           18.35 |               165.1  |         165.1  |
|      500 | extrapolation | M1sn     |      42 |                8.85 |          8.85 |                  6.3  |            6.3  |                 9    |           9    |
|      500 | extrapolation | M2       |      42 |               18.65 |          9.95 |                 26.85 |           10.75 |                17.9  |           8.3  |
|      500 | extrapolation | M2n      |      42 |               17.65 |          3.6  |                 19.6  |            5.85 |                 7.6  |           0    |
|      500 | extrapolation | M3       |      42 |               24.75 |         15.15 |                 25.35 |           10.25 |                22.2  |          15.15 |
|      500 | extrapolation | M4       |      42 |               12.2  |          3.15 |                 11.45 |            4.45 |                12.65 |           0    |
|      500 | extrapolation | M5       |      42 |               19.6  |          9.65 |                 33.9  |            9.8  |                18.8  |           6.8  |
|      500 | extrapolation | M5n      |      42 |               18.45 |          2.35 |                 22.5  |            3.95 |                 7.7  |           0    |
|      500 | extrapolation | NN       |      42 |                4.85 |          4.85 |                  6.65 |            6.65 |                 2.3  |           2.3  |

## source_floor

| scope    | method   | qc   |   n_cases |   resolution_floors |   safe_floors |   resolution_adequate |   safe_adequate |   resolution_failing |   safe_failing |   resolution_lo |   resolution_hi |   safe_lo |   safe_hi | floor         |
|:---------|:---------|:-----|----------:|--------------------:|--------------:|----------------------:|----------------:|---------------------:|---------------:|----------------:|----------------:|----------:|----------:|:--------------|
| transfer | M0       | all  |       126 |              108.35 |        108.35 |                109.4  |          109.4  |                17    |          17    |         101.35  |         114.65  |   101.35  |   114.65  | target family |
| transfer | M1       | all  |       126 |               35.3  |         35.3  |                 35.65 |           35.65 |                32.6  |          32.6  |          33.15  |          37     |    33.15  |    37     | target family |
| transfer | M1s      | all  |       126 |              122.3  |        122.3  |                122.45 |          122.45 |               122.2  |         122.2  |         121.25  |         122.75  |   121.25  |   122.75  | target family |
| transfer | M2       | all  |       126 |               50.65 |         15.8  |                 51.55 |           23.2  |                48.6  |          11.05 |          49.724 |          52.45  |    13.699 |    23.15  | target family |
| transfer | M5       | all  |       126 |               38.4  |         27.5  |                 44    |           27.05 |                35.4  |          31.75 |          35.4   |          38.8   |    24.5   |    31.25  | target family |
| transfer | M1n      | all  |       126 |              130.7  |        130.7  |                128.5  |          128.5  |               172.65 |         172.65 |         129     |         131     |   129     |   131     | target family |
| transfer | NN       | all  |       126 |              130.5  |        130.5  |                128.4  |          128.4  |               169.15 |         169.15 |         129.25  |         130.85  |   129.25  |   130.85  | target family |
| transfer | M2n      | all  |       126 |              132.35 |        129.05 |                130.15 |          126.85 |               180.7  |         164.55 |         130.6   |         132.65  |   127.35  |   129.4   | target family |
| transfer | M5n      | all  |       126 |              132.15 |        129.55 |                129.9  |          127.3  |               171.4  |         167.15 |         130.499 |         132.5   |   127.9   |   129.9   | target family |
| transfer | M3       | all  |       126 |               48.75 |         20.5  |                 49.95 |           20.6  |                47.7  |          19.9  |          45.25  |          52.65  |    16.15  |    28.4   | target family |
| transfer | M4       | all  |       126 |              133.1  |        128.45 |                130.75 |          125.6  |               170.9  |         163.95 |         131.45  |         133.45  |   126.45  |   128.8   | target family |
| transfer | M1sn     | all  |       126 |              130.35 |        130.35 |                128.7  |          128.7  |               169.55 |         169.55 |         129.35  |         130.7   |   129.35  |   130.7   | target family |
| transfer | M0       | all  |       126 |              103.75 |        103.75 |                105.45 |          105.45 |                27.9  |          27.9  |          84.45  |         112.4   |    84.45  |   112.4   | source family |
| transfer | M1       | all  |       126 |               32.9  |         32.9  |                 24    |           24    |                35.2  |          35.2  |          30.699 |          36.101 |    30.699 |    36.101 | source family |
| transfer | M1s      | all  |       126 |              120.65 |        120.65 |                118.15 |          118.15 |               124.65 |         124.65 |         118.6   |         120.95  |   118.6   |   120.95  | source family |
| transfer | M2       | all  |       126 |               40.75 |         26.4  |                 29.5  |            9.7  |                41.85 |          26.85 |          39.45  |          41.95  |     9.8   |    32     | source family |
| transfer | M5       | all  |       126 |               35.2  |         31.3  |                 25.85 |           14.95 |                35.2  |          33.3  |          31.4   |          38.6   |    27.5   |    32.05  | source family |
| transfer | M1n      | all  |       126 |              130.5  |        130.5  |                165.25 |          165.25 |               129    |         129    |         129.15  |         130.65  |   129.15  |   130.65  | source family |
| transfer | NN       | all  |       126 |              130.4  |        130.4  |                168.05 |          168.05 |               128.85 |         128.85 |         128.95  |         130.6   |   128.95  |   130.6   | source family |
| transfer | M2n      | all  |       126 |              133.15 |        127.85 |                175.1  |          155.4  |               131.6  |         126.35 |         131.75  |         133.3   |   126.5   |   128.001 | source family |
| transfer | M5n      | all  |       126 |              132.5  |        128.1  |                171.75 |          164.95 |               131.1  |         126.7  |         131.25  |         132.7   |   126.85  |   128.3   | source family |
| transfer | M3       | all  |       126 |               40.15 |         17.1  |                 35.05 |           15.5  |                40.65 |          17.5  |          36.15  |          45.15  |    14.75  |    19.45  | source family |
| transfer | M4       | all  |       126 |              134.85 |        125.95 |                173.9  |          161.05 |               133.15 |         124.25 |         133.5   |         135.2   |   124.599 |   126.3   | source family |
| transfer | M1sn     | all  |       126 |              130.5  |        130.5  |                167.8  |          167.8  |               128.85 |         128.85 |         128.85  |         130.651 |   128.85  |   130.651 | source family |

## source_floor_paired

| scope    | rule_a   | rule_b   |   resolution_diff |   resolution_diff_lo |   resolution_diff_hi |   resolution_share_a_smaller |   safe_diff |   safe_diff_lo |   safe_diff_hi |   safe_share_a_smaller | floor         |
|:---------|:---------|:---------|------------------:|---------------------:|---------------------:|-----------------------------:|------------:|---------------:|---------------:|-----------------------:|:--------------|
| transfer | M5       | M2       |            -12.25 |              -14.754 |              -11.25  |                        1     |       11.7  |          4.1   |         16.001 |                  0     | target family |
| transfer | M5       | M1       |              3.1  |               -0.15  |                5.25  |                        0.032 |       -7.8  |        -10.951 |         -4.199 |                  1     | target family |
| transfer | M5       | M4       |            -94.7  |              -97.201 |              -93.199 |                        1     |     -100.95 |       -103.552 |        -96.8   |                  1     | target family |
| transfer | M5       | M3       |            -10.35 |              -14.4   |               -8.55  |                        1     |        7    |         -0.604 |         11.504 |                  0.03  | target family |
| transfer | M3       | M4       |            -84.35 |              -87.551 |              -79.75  |                        1     |     -107.95 |       -112.252 |       -100.05  |                  1     | target family |
| transfer | M1       | M1n      |            -95.4  |              -96.551 |              -92.45  |                        1     |      -95.4  |        -96.551 |        -92.45  |                  1     | target family |
| transfer | M2       | M2n      |            -81.7  |              -82.503 |              -78.5   |                        1     |     -113.25 |       -115.451 |       -104.8   |                  1     | target family |
| transfer | M5       | M5n      |            -93.75 |              -95.8   |              -91.95  |                        1     |     -102.05 |       -104.651 |        -98     |                  1     | target family |
| transfer | M5       | NN       |            -92.1  |              -94.551 |              -91     |                        1     |     -103    |       -105.75  |        -99.15  |                  1     | target family |
| transfer | M5n      | NN       |              1.65 |                0.65  |                1.65  |                        0     |       -0.95 |         -1.9   |         -0.95  |                  1     | target family |
| transfer | Mc       | M1       |              2.35 |                0.9   |                9.1   |                        0.01  |        2.35 |          0.9   |          9.1   |                  0.01  | target family |
| transfer | M2       | M0w      |            -68.05 |              -69.751 |              -66.199 |                        1     |      -78.45 |        -84.301 |        -60.599 |                  1     | target family |
| transfer | M1s      | M1       |             87    |               85.15  |               89.251 |                        0     |       87    |         85.15  |         89.251 |                  0     | target family |
| transfer | M1s      | M1n      |             -8.4  |               -8.9   |               -6.699 |                        1     |       -8.4  |         -8.9   |         -6.699 |                  1     | target family |
| transfer | M1s      | NN       |             -8.2  |               -8.95  |               -7.2   |                        1     |       -8.2  |         -8.95  |         -7.2   |                  1     | target family |
| transfer | M2       | NN       |            -79.85 |              -81.101 |              -77.45  |                        1     |     -114.7  |       -116.901 |       -106.95  |                  1     | target family |
| transfer | M2n      | NN       |              1.85 |                0.75  |                1.85  |                        0     |       -1.45 |         -2.5   |         -1.45  |                  1     | target family |
| transfer | M1s      | M1sn     |             -8.05 |               -8.8   |               -7.2   |                        1     |       -8.05 |         -8.8   |         -7.2   |                  1     | target family |
| transfer | M1sn     | NN       |             -0.15 |               -0.15  |                0.251 |                        0.94  |       -0.15 |         -0.15  |          0.251 |                  0.94  | target family |
| transfer | M1sn     | M1n      |             -0.35 |               -0.35  |                0.7   |                        0.661 |       -0.35 |         -0.35  |          0.7   |                  0.661 | target family |
| transfer | M3       | M2       |             -1.9  |               -4.307 |                1.551 |                        0.923 |        4.7  |         -3.41  |          8.002 |                  0.245 | target family |
| transfer | M3       | M5       |             10.35 |                8.55  |               14.4   |                        0     |       -7    |        -11.504 |          0.604 |                  0.97  | target family |
| transfer | M5       | M2       |             -5.55 |               -9.151 |               -2.15  |                        1     |        4.9  |         -0.6   |         19.354 |                  0.041 | source family |
| transfer | M5       | M1       |              2.3  |               -0.2   |                5.65  |                        0.036 |       -1.6  |         -5.05  |         -0.449 |                  0.994 | source family |
| transfer | M5       | M4       |            -99.65 |             -103.55  |              -95.05  |                        1     |      -94.65 |        -98.401 |        -92.8   |                  1     | source family |
| transfer | M5       | M3       |             -4.95 |               -7.9   |               -0.499 |                        0.993 |       14.2  |         11.35  |         16.4   |                  0     | source family |
| transfer | M3       | M4       |            -94.7  |              -98.701 |              -89.7   |                        1     |     -108.85 |       -111.251 |       -106     |                  1     | source family |
| transfer | M1       | M1n      |            -97.6  |              -99.75  |              -93.9   |                        1     |      -97.6  |        -99.75  |        -93.9   |                  1     | source family |
| transfer | M2       | M2n      |            -92.4  |              -93.75  |              -90.249 |                        1     |     -101.45 |       -118     |        -94.85  |                  1     | source family |
| transfer | M5       | M5n      |            -97.3  |             -101.1   |              -92.849 |                        1     |      -96.8  |       -100.6   |        -95.05  |                  1     | source family |
| transfer | M5       | NN       |            -95.2  |              -99.05  |              -90.499 |                        1     |      -99.1  |       -102.9   |        -97.149 |                  1     | source family |
| transfer | M5n      | NN       |              2.1  |                2.05  |                2.35  |                        0     |       -2.3  |         -2.35  |         -2.05  |                  1     | source family |
| transfer | Mc       | M1       |              9.7  |                3.3   |               13.014 |                        0     |        9.7  |          3.3   |         13.014 |                  0     | source family |
| transfer | M2       | M0w      |            -76.65 |              -79.251 |              -73.449 |                        1     |      -52.9  |        -78.001 |        -42.645 |                  1     | source family |
| transfer | M1s      | M1       |             87.75 |               82.999 |               89.35  |                        0     |       87.75 |         82.999 |         89.35  |                  0     | source family |
| transfer | M1s      | M1n      |             -9.85 |              -11.9   |               -8.45  |                        1     |       -9.85 |        -11.9   |         -8.45  |                  1     | source family |
| transfer | M1s      | NN       |             -9.75 |              -11.85  |               -8.3   |                        1     |       -9.75 |        -11.85  |         -8.3   |                  1     | source family |
| transfer | M2       | NN       |            -89.65 |              -91.001 |              -87.5   |                        1     |     -104    |       -120.55  |        -97.349 |                  1     | source family |
| transfer | M2n      | NN       |              2.75 |                2.7   |                2.9   |                        0     |       -2.55 |         -2.6   |         -2.4   |                  1     | source family |
| transfer | M1s      | M1sn     |             -9.85 |              -11.9   |               -8.2   |                        1     |       -9.85 |        -11.9   |         -8.2   |                  1     | source family |
| transfer | M1sn     | NN       |              0.1  |               -0.15  |                0.1   |                        0.067 |        0.1  |         -0.15  |          0.1   |                  0.067 | source family |
| transfer | M1sn     | M1n      |              0    |               -0.3   |                0.05  |                        0.091 |        0    |         -0.3   |          0.05  |                  0.091 | source family |
| transfer | M3       | M2       |             -0.6  |               -3.55  |                3.7   |                        0.809 |       -9.3  |        -16.101 |          6.901 |                  0.833 | source family |
| transfer | M3       | M5       |              4.95 |                0.499 |                7.9   |                        0     |      -14.2  |        -16.4   |        -11.35  |                  1     | source family |

## physical_units

| scope    | method   | qc            |   pooled_floor |   resolution_units |   safe_units |   resolution_pooled_floors |   safe_pooled_floors |
|:---------|:---------|:--------------|---------------:|-------------------:|-------------:|---------------------------:|---------------------:|
| setting  | M0       | arm_op20      |          0.109 |              3.967 |        3.967 |                      36.55 |                36.55 |
| setting  | M0       | depth_op10    |          0.011 |              1.05  |        1.05  |                      96.45 |                96.45 |
| setting  | M0       | dome_op20     |          0.007 |              0.114 |        0.114 |                      16.2  |                16.2  |
| setting  | M0       | drawin_corner |          0.046 |              3.446 |        3.446 |                      74.3  |                74.3  |
| setting  | M0       | drawin_mid    |          0.051 |              1.971 |        1.971 |                      39    |                39    |
| setting  | M0       | wall_op10     |          0.078 |              2.213 |        2.213 |                      28.2  |                28.2  |
| setting  | M0       | waviness      |          0.003 |              0.055 |        0.055 |                      19.9  |                19.9  |
| setting  | M1       | arm_op20      |          0.109 |              2.583 |        2.583 |                      23.8  |                23.8  |
| setting  | M1       | depth_op10    |          0.011 |              0.292 |        0.292 |                      26.85 |                26.85 |
| setting  | M1       | dome_op20     |          0.007 |              0.048 |        0.048 |                       6.8  |                 6.8  |
| setting  | M1       | drawin_corner |          0.046 |              0.731 |        0.731 |                      15.75 |                15.75 |
| setting  | M1       | drawin_mid    |          0.051 |              1.359 |        1.359 |                      26.9  |                26.9  |
| setting  | M1       | wall_op10     |          0.078 |              1.146 |        1.146 |                      14.6  |                14.6  |
| setting  | M1       | waviness      |          0.003 |              0.034 |        0.034 |                      12.2  |                12.2  |
| setting  | M1s      | arm_op20      |          0.109 |              3.039 |        3.039 |                      28    |                28    |
| setting  | M1s      | depth_op10    |          0.011 |              1.439 |        1.439 |                     132.2  |               132.2  |
| setting  | M1s      | dome_op20     |          0.007 |              0.05  |        0.05  |                       7.15 |                 7.15 |
| setting  | M1s      | drawin_corner |          0.046 |              0.1   |        0.1   |                       2.15 |                 2.15 |
| setting  | M1s      | drawin_mid    |          0.051 |              0.197 |        0.197 |                       3.9  |                 3.9  |
| setting  | M1s      | wall_op10     |          0.078 |              0.157 |        0.157 |                       2    |                 2    |
| setting  | M1s      | waviness      |          0.003 |              0.077 |        0.077 |                      27.9  |                27.9  |
| setting  | M1sn     | arm_op20      |          0.109 |              0.884 |        0.884 |                       8.15 |                 8.15 |
| setting  | M1sn     | depth_op10    |          0.011 |              0.086 |        0.086 |                       7.9  |                 7.9  |
| setting  | M1sn     | dome_op20     |          0.007 |              0.025 |        0.025 |                       3.6  |                 3.6  |
| setting  | M1sn     | drawin_corner |          0.046 |              0.083 |        0.083 |                       1.8  |                 1.8  |
| setting  | M1sn     | drawin_mid    |          0.051 |              0.283 |        0.283 |                       5.6  |                 5.6  |
| setting  | M1sn     | wall_op10     |          0.078 |              0.137 |        0.137 |                       1.75 |                 1.75 |
| setting  | M1sn     | waviness      |          0.003 |              0.027 |        0.027 |                       9.65 |                 9.65 |
| setting  | M2       | arm_op20      |          0.109 |              3.169 |        0.939 |                      29.2  |                 8.65 |
| setting  | M2       | depth_op10    |          0.011 |              0.148 |        0.113 |                      13.6  |                10.4  |
| setting  | M2       | dome_op20     |          0.007 |              0.151 |        0.015 |                      21.55 |                 2.1  |
| setting  | M2       | drawin_corner |          0.046 |              0.213 |        0.09  |                       4.6  |                 1.95 |
| setting  | M2       | drawin_mid    |          0.051 |              0.912 |        0.412 |                      18.05 |                 8.15 |
| setting  | M2       | wall_op10     |          0.078 |              0.612 |        0.251 |                       7.8  |                 3.2  |
| setting  | M2       | waviness      |          0.003 |              0.044 |        0.04  |                      15.95 |                14.35 |
| setting  | M3       | arm_op20      |          0.109 |              4.705 |        2.252 |                      43.35 |                20.75 |
| setting  | M3       | depth_op10    |          0.011 |              0.26  |        0.161 |                      23.85 |                14.75 |
| setting  | M3       | dome_op20     |          0.007 |              0.178 |        0.031 |                      25.3  |                 4.45 |
| setting  | M3       | drawin_corner |          0.046 |              1.027 |        0.455 |                      22.15 |                 9.8  |
| setting  | M3       | drawin_mid    |          0.051 |              1.708 |        0.947 |                      33.8  |                18.75 |
| setting  | M3       | wall_op10     |          0.078 |              1.821 |        0.632 |                      23.2  |                 8.05 |
| setting  | M3       | waviness      |          0.003 |              0.09  |        0.058 |                      32.8  |                21.2  |
| setting  | M4       | arm_op20      |          0.109 |              1.264 |        0.298 |                      11.65 |                 2.75 |
| setting  | M4       | depth_op10    |          0.011 |              0.174 |        0.121 |                      16    |                11.1  |
| setting  | M4       | dome_op20     |          0.007 |              0.136 |        0.011 |                      19.35 |                 1.5  |
| setting  | M4       | drawin_corner |          0.046 |              0.32  |        0.162 |                       6.9  |                 3.5  |
| setting  | M4       | drawin_mid    |          0.051 |              0.546 |        0.288 |                      10.8  |                 5.7  |
| setting  | M4       | wall_op10     |          0.078 |              0.381 |        0.153 |                       4.85 |                 1.95 |
| setting  | M4       | waviness      |          0.003 |              0.043 |        0.037 |                      15.65 |                13.35 |
| setting  | M5       | arm_op20      |          0.109 |              3.988 |        0.939 |                      36.75 |                 8.65 |
| setting  | M5       | depth_op10    |          0.011 |              0.154 |        0.115 |                      14.15 |                10.6  |
| setting  | M5       | dome_op20     |          0.007 |              0.142 |        0.018 |                      20.15 |                 2.55 |
| setting  | M5       | drawin_corner |          0.046 |              0.216 |        0.079 |                       4.65 |                 1.7  |
| setting  | M5       | drawin_mid    |          0.051 |              0.975 |        0.339 |                      19.3  |                 6.7  |
| setting  | M5       | wall_op10     |          0.078 |              0.608 |        0.247 |                       7.75 |                 3.15 |
| setting  | M5       | waviness      |          0.003 |              0.055 |        0.039 |                      19.85 |                14.2  |
| setting  | M5n      | arm_op20      |          0.109 |              0.917 |        0.266 |                       8.45 |                 2.45 |
| setting  | M5n      | depth_op10    |          0.011 |              0.206 |        0.115 |                      18.9  |                10.55 |
| setting  | M5n      | dome_op20     |          0.007 |              0.077 |        0.012 |                      10.95 |                 1.65 |
| setting  | M5n      | drawin_corner |          0.046 |              0.438 |        0.176 |                       9.45 |                 3.8  |
| setting  | M5n      | drawin_mid    |          0.051 |              0.528 |        0.25  |                      10.45 |                 4.95 |
| setting  | M5n      | wall_op10     |          0.078 |              0.239 |        0.098 |                       3.05 |                 1.25 |
| setting  | M5n      | waviness      |          0.003 |              0.066 |        0.036 |                      23.95 |                12.9  |
| setting  | NN       | arm_op20      |          0.109 |              0.586 |        0.586 |                       5.4  |                 5.4  |
| setting  | NN       | depth_op10    |          0.011 |              0.13  |        0.13  |                      11.9  |                11.9  |
| setting  | NN       | dome_op20     |          0.007 |              0.035 |        0.035 |                       5    |                 5    |
| setting  | NN       | drawin_corner |          0.046 |              0.227 |        0.227 |                       4.9  |                 4.9  |
| setting  | NN       | drawin_mid    |          0.051 |              0.321 |        0.321 |                       6.35 |                 6.35 |
| setting  | NN       | wall_op10     |          0.078 |              0.145 |        0.145 |                       1.85 |                 1.85 |
| setting  | NN       | waviness      |          0.003 |              0.04  |        0.04  |                      14.55 |                14.55 |
| transfer | M0       | arm_op20      |          0.109 |              3.967 |        3.967 |                      36.55 |                36.55 |
| transfer | M0       | depth_op10    |          0.011 |              1.05  |        1.05  |                      96.45 |                96.45 |
| transfer | M0       | dome_op20     |          0.007 |              0.114 |        0.114 |                      16.2  |                16.2  |
| transfer | M0       | drawin_corner |          0.046 |              3.446 |        3.446 |                      74.3  |                74.3  |
| transfer | M0       | drawin_mid    |          0.051 |              1.971 |        1.971 |                      39    |                39    |
| transfer | M0       | wall_op10     |          0.078 |              2.213 |        2.213 |                      28.2  |                28.2  |
| transfer | M0       | waviness      |          0.003 |              0.055 |        0.055 |                      19.9  |                19.9  |
| transfer | M1       | arm_op20      |          0.109 |              4.097 |        4.097 |                      37.75 |                37.75 |
| transfer | M1       | depth_op10    |          0.011 |              0.258 |        0.258 |                      23.7  |                23.7  |
| transfer | M1       | dome_op20     |          0.007 |              0.188 |        0.188 |                      26.8  |                26.8  |
| transfer | M1       | drawin_corner |          0.046 |              0.703 |        0.703 |                      15.15 |                15.15 |
| transfer | M1       | drawin_mid    |          0.051 |              1.192 |        1.192 |                      23.6  |                23.6  |
| transfer | M1       | wall_op10     |          0.078 |              1.318 |        1.318 |                      16.8  |                16.8  |
| transfer | M1       | waviness      |          0.003 |              0.05  |        0.05  |                      18.3  |                18.3  |
| transfer | M1s      | arm_op20      |          0.109 |              4.922 |        4.922 |                      45.35 |                45.35 |
| transfer | M1s      | depth_op10    |          0.011 |              0.329 |        0.329 |                      30.25 |                30.25 |
| transfer | M1s      | dome_op20     |          0.007 |              0.135 |        0.135 |                      19.25 |                19.25 |
| transfer | M1s      | drawin_corner |          0.046 |              3.669 |        3.669 |                      79.1  |                79.1  |
| transfer | M1s      | drawin_mid    |          0.051 |              0.738 |        0.738 |                      14.6  |                14.6  |
| transfer | M1s      | wall_op10     |          0.078 |              9.743 |        9.743 |                     124.15 |               124.15 |
| transfer | M1s      | waviness      |          0.003 |              0.039 |        0.039 |                      14.1  |                14.1  |
| transfer | M1sn     | arm_op20      |          0.109 |              4.661 |        4.661 |                      42.95 |                42.95 |
| transfer | M1sn     | depth_op10    |          0.011 |              0.408 |        0.408 |                      37.5  |                37.5  |
| transfer | M1sn     | dome_op20     |          0.007 |              0.098 |        0.098 |                      13.95 |                13.95 |
| transfer | M1sn     | drawin_corner |          0.046 |              5.1   |        5.1   |                     109.95 |               109.95 |
| transfer | M1sn     | drawin_mid    |          0.051 |              1.006 |        1.006 |                      19.9  |                19.9  |
| transfer | M1sn     | wall_op10     |          0.078 |             10.127 |       10.127 |                     129.05 |               129.05 |
| transfer | M1sn     | waviness      |          0.003 |              0.028 |        0.028 |                      10.2  |                10.2  |
| transfer | M2       | arm_op20      |          0.109 |              5.296 |        3.353 |                      48.8  |                30.9  |
| transfer | M2       | depth_op10    |          0.011 |              0.256 |        0.072 |                      23.5  |                 6.6  |
| transfer | M2       | dome_op20     |          0.007 |              0.207 |        0.125 |                      29.45 |                17.75 |
| transfer | M2       | drawin_corner |          0.046 |              0.32  |        0.102 |                       6.9  |                 2.2  |
| transfer | M2       | drawin_mid    |          0.051 |              0.988 |        0.099 |                      19.55 |                 1.95 |
| transfer | M2       | wall_op10     |          0.078 |              0.8   |        0.004 |                      10.2  |                 0.05 |
| transfer | M2       | waviness      |          0.003 |              0.108 |        0.025 |                      39.1  |                 9    |
| transfer | M3       | arm_op20      |          0.109 |              5.801 |        4.037 |                      53.45 |                37.2  |
| transfer | M3       | depth_op10    |          0.011 |              0.299 |        0.179 |                      27.5  |                16.45 |
| transfer | M3       | dome_op20     |          0.007 |              0.296 |        0.067 |                      42.1  |                 9.5  |
| transfer | M3       | drawin_corner |          0.046 |              0.668 |        0.297 |                      14.4  |                 6.4  |
| transfer | M3       | drawin_mid    |          0.051 |              0.826 |        0.157 |                      16.35 |                 3.1  |
| transfer | M3       | wall_op10     |          0.078 |              2.531 |        0.412 |                      32.25 |                 5.25 |
| transfer | M3       | waviness      |          0.003 |              0.089 |        0.04  |                      32.4  |                14.5  |
| transfer | M4       | arm_op20      |          0.109 |              5.329 |        4.412 |                      49.1  |                40.65 |
| transfer | M4       | depth_op10    |          0.011 |              0.46  |        0.364 |                      42.25 |                33.4  |
| transfer | M4       | dome_op20     |          0.007 |              0.175 |        0.069 |                      24.9  |                 9.85 |
| transfer | M4       | drawin_corner |          0.046 |              5.25  |        4.928 |                     113.2  |               106.25 |
| transfer | M4       | drawin_mid    |          0.051 |              1.056 |        0.844 |                      20.9  |                16.7  |
| transfer | M4       | wall_op10     |          0.078 |             10.477 |        9.872 |                     133.5  |               125.8  |
| transfer | M4       | waviness      |          0.003 |              0.03  |        0.023 |                      10.7  |                 8.25 |
| transfer | M5       | arm_op20      |          0.109 |              3.934 |        3.467 |                      36.25 |                31.95 |
| transfer | M5       | depth_op10    |          0.011 |              0.198 |        0.131 |                      18.2  |                12    |
| transfer | M5       | dome_op20     |          0.007 |              0.213 |        0.129 |                      30.3  |                18.35 |
| transfer | M5       | drawin_corner |          0.046 |              0.306 |        0.135 |                       6.6  |                 2.9  |
| transfer | M5       | drawin_mid    |          0.051 |              0.27  |        0.106 |                       5.35 |                 2.1  |
| transfer | M5       | wall_op10     |          0.078 |              0.585 |        0.243 |                       7.45 |                 3.1  |
| transfer | M5       | waviness      |          0.003 |              0.047 |        0.044 |                      17.1  |                15.85 |
| transfer | M5n      | arm_op20      |          0.109 |              4.867 |        4.444 |                      44.85 |                40.95 |
| transfer | M5n      | depth_op10    |          0.011 |              0.434 |        0.372 |                      39.9  |                34.15 |
| transfer | M5n      | dome_op20     |          0.007 |              0.124 |        0.079 |                      17.65 |                11.2  |
| transfer | M5n      | drawin_corner |          0.046 |              5.172 |        5.005 |                     111.5  |               107.9  |
| transfer | M5n      | drawin_mid    |          0.051 |              1.079 |        0.899 |                      21.35 |                17.8  |
| transfer | M5n      | wall_op10     |          0.078 |             10.273 |        9.951 |                     130.9  |               126.8  |
| transfer | M5n      | waviness      |          0.003 |              0.027 |        0.024 |                       9.8  |                 8.55 |
| transfer | NN       | arm_op20      |          0.109 |              4.65  |        4.65  |                      42.85 |                42.85 |
| transfer | NN       | depth_op10    |          0.011 |              0.404 |        0.404 |                      37.15 |                37.15 |
| transfer | NN       | dome_op20     |          0.007 |              0.099 |        0.099 |                      14.05 |                14.05 |
| transfer | NN       | drawin_corner |          0.046 |              5.095 |        5.095 |                     109.85 |               109.85 |
| transfer | NN       | drawin_mid    |          0.051 |              1.013 |        1.013 |                      20.05 |                20.05 |
| transfer | NN       | wall_op10     |          0.078 |             10.131 |       10.131 |                     129.1  |               129.1  |
| transfer | NN       | waviness      |          0.003 |              0.025 |        0.025 |                       9    |                 9    |
| within   | M0       | arm_op20      |          0.109 |              3.967 |        3.967 |                      36.55 |                36.55 |
| within   | M0       | depth_op10    |          0.011 |              1.05  |        1.05  |                      96.45 |                96.45 |
| within   | M0       | dome_op20     |          0.007 |              0.114 |        0.114 |                      16.2  |                16.2  |
| within   | M0       | drawin_corner |          0.046 |              3.446 |        3.446 |                      74.3  |                74.3  |
| within   | M0       | drawin_mid    |          0.051 |              1.971 |        1.971 |                      39    |                39    |
| within   | M0       | wall_op10     |          0.078 |              2.213 |        2.213 |                      28.2  |                28.2  |
| within   | M0       | waviness      |          0.003 |              0.055 |        0.055 |                      19.9  |                19.9  |
| within   | M1       | arm_op20      |          0.109 |              0.939 |        0.939 |                       8.65 |                 8.65 |
| within   | M1       | depth_op10    |          0.011 |              0.228 |        0.228 |                      20.9  |                20.9  |
| within   | M1       | dome_op20     |          0.007 |              0.048 |        0.048 |                       6.8  |                 6.8  |
| within   | M1       | drawin_corner |          0.046 |              0.601 |        0.601 |                      12.95 |                12.95 |
| within   | M1       | drawin_mid    |          0.051 |              1.031 |        1.031 |                      20.4  |                20.4  |
| within   | M1       | wall_op10     |          0.078 |              0.91  |        0.91  |                      11.6  |                11.6  |
| within   | M1       | waviness      |          0.003 |              0.03  |        0.03  |                      10.7  |                10.7  |
| within   | M1s      | arm_op20      |          0.109 |              0.418 |        0.418 |                       3.85 |                 3.85 |
| within   | M1s      | depth_op10    |          0.011 |              0.078 |        0.078 |                       7.2  |                 7.2  |
| within   | M1s      | dome_op20     |          0.007 |              0.041 |        0.041 |                       5.85 |                 5.85 |
| within   | M1s      | drawin_corner |          0.046 |              0.128 |        0.128 |                       2.75 |                 2.75 |
| within   | M1s      | drawin_mid    |          0.051 |              0.111 |        0.111 |                       2.2  |                 2.2  |
| within   | M1s      | wall_op10     |          0.078 |              0.235 |        0.235 |                       3    |                 3    |
| within   | M1s      | waviness      |          0.003 |              0.022 |        0.022 |                       7.8  |                 7.8  |
| within   | M1sn     | arm_op20      |          0.109 |              0.45  |        0.45  |                       4.15 |                 4.15 |
| within   | M1sn     | depth_op10    |          0.011 |              0.037 |        0.037 |                       3.4  |                 3.4  |
| within   | M1sn     | dome_op20     |          0.007 |              0.033 |        0.033 |                       4.75 |                 4.75 |
| within   | M1sn     | drawin_corner |          0.046 |              0.107 |        0.107 |                       2.3  |                 2.3  |
| within   | M1sn     | drawin_mid    |          0.051 |              0.136 |        0.136 |                       2.7  |                 2.7  |
| within   | M1sn     | wall_op10     |          0.078 |              0.232 |        0.232 |                       2.95 |                 2.95 |
| within   | M1sn     | waviness      |          0.003 |              0.01  |        0.01  |                       3.55 |                 3.55 |
| within   | M2       | arm_op20      |          0.109 |              3.169 |        0.033 |                      29.2  |                 0.3  |
| within   | M2       | depth_op10    |          0.011 |              0.242 |        0.003 |                      22.2  |                 0.25 |
| within   | M2       | dome_op20     |          0.007 |              0.122 |        0.002 |                      17.3  |                 0.3  |
| within   | M2       | drawin_corner |          0.046 |              0.255 |        0.026 |                       5.5  |                 0.55 |
| within   | M2       | drawin_mid    |          0.051 |              1.013 |        0     |                      20.05 |                 0    |
| within   | M2       | wall_op10     |          0.078 |              0.722 |        0.012 |                       9.2  |                 0.15 |
| within   | M2       | waviness      |          0.003 |              0.083 |        0     |                      30.05 |                 0.05 |
| within   | M3       | arm_op20      |          0.109 |              2.941 |        0.005 |                      27.1  |                 0.05 |
| within   | M3       | depth_op10    |          0.011 |              0.318 |        0     |                      29.25 |                 0    |
| within   | M3       | dome_op20     |          0.007 |              0.123 |        0     |                      17.5  |                 0.05 |
| within   | M3       | drawin_corner |          0.046 |              0.7   |        0     |                      15.1  |                 0    |
| within   | M3       | drawin_mid    |          0.051 |              1.369 |        0     |                      27.1  |                 0    |
| within   | M3       | wall_op10     |          0.078 |              4.116 |        0.012 |                      52.45 |                 0.15 |
| within   | M3       | waviness      |          0.003 |              0.073 |        0     |                      26.3  |                 0    |
| within   | M4       | arm_op20      |          0.109 |              1.107 |        0.125 |                      10.2  |                 1.15 |
| within   | M4       | depth_op10    |          0.011 |              0.099 |        0.003 |                       9.05 |                 0.25 |
| within   | M4       | dome_op20     |          0.007 |              0.132 |        0.012 |                      18.75 |                 1.75 |
| within   | M4       | drawin_corner |          0.046 |              0.308 |        0.002 |                       6.65 |                 0.05 |
| within   | M4       | drawin_mid    |          0.051 |              0.217 |        0.03  |                       4.3  |                 0.6  |
| within   | M4       | wall_op10     |          0.078 |              0.49  |        0     |                       6.25 |                 0    |
| within   | M4       | waviness      |          0.003 |              0.01  |        0     |                       3.45 |                 0.05 |
| within   | M5       | arm_op20      |          0.109 |              0.716 |        0.141 |                       6.6  |                 1.3  |
| within   | M5       | depth_op10    |          0.011 |              0.063 |        0.009 |                       5.75 |                 0.85 |
| within   | M5       | dome_op20     |          0.007 |              0.096 |        0.018 |                      13.7  |                 2.6  |
| within   | M5       | drawin_corner |          0.046 |              0.172 |        0.044 |                       3.7  |                 0.95 |
| within   | M5       | drawin_mid    |          0.051 |              0.167 |        0.008 |                       3.3  |                 0.15 |
| within   | M5       | wall_op10     |          0.078 |              0.369 |        0.137 |                       4.7  |                 1.75 |
| within   | M5       | waviness      |          0.003 |              0.007 |        0.001 |                       2.45 |                 0.25 |
| within   | M5n      | arm_op20      |          0.109 |              0.722 |        0.141 |                       6.65 |                 1.3  |
| within   | M5n      | depth_op10    |          0.011 |              0.062 |        0.008 |                       5.7  |                 0.75 |
| within   | M5n      | dome_op20     |          0.007 |              0.081 |        0.017 |                      11.5  |                 2.4  |
| within   | M5n      | drawin_corner |          0.046 |              0.183 |        0.032 |                       3.95 |                 0.7  |
| within   | M5n      | drawin_mid    |          0.051 |              0.182 |        0.005 |                       3.6  |                 0.1  |
| within   | M5n      | wall_op10     |          0.078 |              0.279 |        0.051 |                       3.55 |                 0.65 |
| within   | M5n      | waviness      |          0.003 |              0.007 |        0.001 |                       2.4  |                 0.25 |
| within   | NN       | arm_op20      |          0.109 |              0.282 |        0.282 |                       2.6  |                 2.6  |
| within   | NN       | depth_op10    |          0.011 |              0.039 |        0.039 |                       3.55 |                 3.55 |
| within   | NN       | dome_op20     |          0.007 |              0.038 |        0.038 |                       5.4  |                 5.4  |
| within   | NN       | drawin_corner |          0.046 |              0.135 |        0.135 |                       2.9  |                 2.9  |
| within   | NN       | drawin_mid    |          0.051 |              0.099 |        0.099 |                       1.95 |                 1.95 |
| within   | NN       | wall_op10     |          0.078 |              0.259 |        0.259 |                       3.3  |                 3.3  |
| within   | NN       | waviness      |          0.003 |              0.003 |        0.003 |                       1.15 |                 1.15 |

## failing_weight

|   delta |   cases |   feasible_failing |   weight_failing |
|--------:|--------:|-------------------:|-----------------:|
|     1   |     126 |                126 |            0.5   |
|     3.4 |     126 |                124 |            0.496 |
|     8.5 |     126 |                115 |            0.477 |
|    16   |     126 |                 98 |            0.438 |
|    35   |     126 |                 84 |            0.4   |
|   108   |     126 |                 63 |            0.333 |

## step6

| scope                 | method   |   guard_band |   decisive_alone |   safe_alone |   right_10_alone |   wrong_10_alone |   trial_10_alone |   right_20_alone |   wrong_20_alone |   trial_20_alone |   decisive_step6 |   safe_step6 |   right_10_step6 |   wrong_10_step6 |   trial_10_step6 |   right_20_step6 |   wrong_20_step6 |   trial_20_step6 |
|:----------------------|:---------|-------------:|-----------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| setting               | M0       |       inf    |           108.35 |       108.35 |            0.653 |            0.347 |            0     |            0.731 |            0.269 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting               | M1       |       inf    |            23.75 |        23.75 |            0.787 |            0.213 |            0     |            0.918 |            0.082 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting               | M1n      |         8.75 |            10.3  |        10.3  |            0.946 |            0.054 |            0     |            1     |            0     |            0     |            19.15 |         1.4  |            0.603 |            0     |            0.397 |            0.963 |                0 |            0.037 |
| setting               | M1s      |       inf    |            19.15 |        19.15 |            0.887 |            0.113 |            0     |            0.959 |            0.041 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting               | M1sn     |         4.75 |             8.15 |         8.15 |            0.996 |            0.004 |            0     |            1     |            0     |            0     |            13.4  |         3.4  |            0.866 |            0     |            0.134 |            1     |                0 |            0     |
| setting               | M2       |       inf    |            17.5  |         8.1  |            0.728 |            0.025 |            0.247 |            0.973 |            0     |            0.027 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting               | M2n      |         6    |            15.25 |         5.85 |            0.808 |            0.008 |            0.184 |            0.986 |            0     |            0.014 |            21.3  |         0    |            0.485 |            0     |            0.515 |            0.904 |                0 |            0.096 |
| setting               | M3       |        17    |            30.7  |        16    |            0.515 |            0.113 |            0.372 |            0.772 |            0.005 |            0.224 |            47.7  |         0.05 |            0.134 |            0     |            0.866 |            0.311 |                0 |            0.689 |
| setting               | M4       |         6    |            13.3  |         7.4  |            0.778 |            0.017 |            0.205 |            0.995 |            0     |            0.005 |            19.05 |         1.4  |            0.527 |            0     |            0.473 |            0.968 |                0 |            0.032 |
| setting               | M5       |       inf    |            18.65 |         6.8  |            0.682 |            0.017 |            0.301 |            0.968 |            0     |            0.032 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting               | M5n      |         5.5  |            17.2  |         6.1  |            0.782 |            0.008 |            0.209 |            0.977 |            0     |            0.023 |            23.6  |         0.6  |            0.481 |            0     |            0.519 |            0.886 |                0 |            0.114 |
| setting               | NN       |         5    |             8.45 |         8.45 |            0.975 |            0.025 |            0     |            1     |            0     |            0     |            13.55 |         3.45 |            0.887 |            0.004 |            0.109 |            0.995 |                0 |            0.005 |
| setting/extrapolation | M0       |       inf    |           105.55 |       105.55 |            0.698 |            0.302 |            0     |            0.735 |            0.265 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/extrapolation | M1       |       inf    |            24.6  |        24.6  |            0.723 |            0.277 |            0     |            0.878 |            0.122 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/extrapolation | M1n      |         9.75 |            11.75 |        11.75 |            0.918 |            0.082 |            0     |            1     |            0     |            0     |            21.5  |         1.1  |            0.516 |            0     |            0.484 |            0.918 |                0 |            0.082 |
| setting/extrapolation | M1s      |       inf    |            19.1  |        19.1  |            0.906 |            0.094 |            0     |            0.959 |            0.041 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/extrapolation | M1sn     |         6    |             8.85 |         8.85 |            0.994 |            0.006 |            0     |            1     |            0     |            0     |            14.85 |         2.85 |            0.786 |            0     |            0.214 |            1     |                0 |            0     |
| setting/extrapolation | M2       |       inf    |            17.5  |         9.9  |            0.717 |            0.038 |            0.245 |            0.98  |            0     |            0.02  |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/extrapolation | M2n      |         7.25 |            15.5  |         9.1  |            0.805 |            0.013 |            0.182 |            0.98  |            0     |            0.02  |            22.75 |         1.85 |            0.497 |            0     |            0.503 |            0.844 |                0 |            0.156 |
| setting/extrapolation | M3       |        16.75 |            32.85 |        16.95 |            0.509 |            0.126 |            0.365 |            0.748 |            0.007 |            0.245 |            51.1  |         0.05 |            0.151 |            0     |            0.849 |            0.313 |                0 |            0.687 |
| setting/extrapolation | M4       |         6.5  |            13.05 |         7.8  |            0.792 |            0.019 |            0.189 |            1     |            0     |            0     |            18.8  |         1.3  |            0.528 |            0     |            0.472 |            0.973 |                0 |            0.027 |
| setting/extrapolation | M5       |       inf    |            18.5  |         8.9  |            0.717 |            0.025 |            0.258 |            0.973 |            0     |            0.027 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/extrapolation | M5n      |         6.75 |            18.1  |         8.6  |            0.799 |            0.013 |            0.189 |            0.966 |            0     |            0.034 |            24.85 |         1.85 |            0.522 |            0     |            0.478 |            0.85  |                0 |            0.15  |
| setting/extrapolation | NN       |         7    |             9.45 |         9.45 |            0.962 |            0.038 |            0     |            1     |            0     |            0     |            16.5  |         2.45 |            0.736 |            0     |            0.264 |            0.986 |                0 |            0.014 |
| setting/interpolation | M0       |       inf    |           108.6  |       108.6  |            0.562 |            0.438 |            0     |            0.722 |            0.278 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/interpolation | M1       |         8.75 |            11.25 |        11.25 |            0.912 |            0.088 |            0     |            1     |            0     |            0     |            20    |         2.1  |            0.562 |            0     |            0.438 |            0.958 |                0 |            0.042 |
| setting/interpolation | M1n      |         2    |             4.8  |         4.8  |            1     |            0     |            0     |            1     |            0     |            0     |             6.8  |         2.8  |            1     |            0     |            0     |            1     |                0 |            0     |
| setting/interpolation | M1s      |       inf    |            19.25 |        19.25 |            0.85  |            0.15  |            0     |            0.958 |            0.042 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| setting/interpolation | M1sn     |         2    |             4.65 |         4.65 |            1     |            0     |            0     |            1     |            0     |            0     |             6.65 |         2.65 |            1     |            0     |            0     |            1     |                0 |            0     |
| setting/interpolation | M2       |         0.75 |            17.75 |         2.7  |            0.75  |            0     |            0.25  |            0.958 |            0     |            0.042 |            18.5  |         1.95 |            0.688 |            0     |            0.312 |            0.958 |                0 |            0.042 |
| setting/interpolation | M2n      |         0    |            13.3  |         0    |            0.812 |            0     |            0.188 |            1     |            0     |            0     |            13.3  |         0    |            0.812 |            0     |            0.188 |            1     |                0 |            0     |
| setting/interpolation | M3       |        17.75 |            29.05 |        13.35 |            0.525 |            0.088 |            0.388 |            0.819 |            0     |            0.181 |            46.8  |         0    |            0.062 |            0     |            0.938 |            0.306 |                0 |            0.694 |
| setting/interpolation | M4       |         6    |            14.7  |         7    |            0.75  |            0.012 |            0.238 |            0.986 |            0     |            0.014 |            20.7  |         1    |            0.45  |            0     |            0.55  |            0.944 |                0 |            0.056 |
| setting/interpolation | M5       |         0.5  |            19.05 |         2.8  |            0.612 |            0     |            0.388 |            0.958 |            0     |            0.042 |            19.55 |         2.3  |            0.6   |            0     |            0.4   |            0.958 |                0 |            0.042 |
| setting/interpolation | M5n      |         0    |            15.6  |         0    |            0.75  |            0     |            0.25  |            1     |            0     |            0     |            15.6  |         0    |            0.75  |            0     |            0.25  |            1     |                0 |            0     |
| setting/interpolation | NN       |         2    |             4.65 |         4.65 |            1     |            0     |            0     |            1     |            0     |            0     |             6.65 |         2.65 |            1     |            0     |            0     |            1     |                0 |            0     |
| transfer              | M0       |       inf    |           103.75 |       103.75 |            0.624 |            0.376 |            0     |            0.724 |            0.276 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1       |       inf    |            32.9  |        32.9  |            0.744 |            0.256 |            0     |            0.816 |            0.184 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1n      |       inf    |           130.5  |       130.5  |            0.556 |            0.444 |            0     |            0.627 |            0.373 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1s      |       inf    |           120.65 |       120.65 |            0.547 |            0.453 |            0     |            0.706 |            0.294 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1sn     |       inf    |           130.5  |       130.5  |            0.564 |            0.436 |            0     |            0.654 |            0.346 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M2       |       inf    |            40.75 |        26.4  |            0.59  |            0.06  |            0.35  |            0.772 |            0.057 |            0.171 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M2n      |       inf    |           133.15 |       127.85 |            0.462 |            0.41  |            0.128 |            0.575 |            0.316 |            0.11  |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M3       |       inf    |            40.15 |        17.1  |            0.581 |            0.124 |            0.295 |            0.746 |            0.031 |            0.224 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M4       |       inf    |           134.85 |       125.95 |            0.526 |            0.419 |            0.056 |            0.601 |            0.325 |            0.075 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M5       |       inf    |            35.2  |        31.3  |            0.748 |            0.179 |            0.073 |            0.86  |            0.092 |            0.048 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M5n      |       inf    |           132.5  |       128.1  |            0.526 |            0.423 |            0.051 |            0.605 |            0.333 |            0.061 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | NN       |       inf    |           130.4  |       130.4  |            0.564 |            0.436 |            0     |            0.654 |            0.346 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| within                | M0       |       inf    |           108.35 |       108.35 |            0.653 |            0.347 |            0     |            0.731 |            0.269 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| within                | M1       |       inf    |            15.2  |        15.2  |            0.879 |            0.121 |            0     |            0.991 |            0.009 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| within                | M1n      |         5.25 |             9.05 |         9.05 |            0.971 |            0.029 |            0     |            1     |            0     |            0     |            14.45 |         3.8  |            0.879 |            0     |            0.121 |            0.991 |                0 |            0.009 |
| within                | M1s      |         2    |             4.85 |         4.85 |            1     |            0     |            0     |            1     |            0     |            0     |             6.85 |         2.85 |            0.992 |            0     |            0.008 |            1     |                0 |            0     |
| within                | M1sn     |         0.75 |             3.5  |         3.5  |            1     |            0     |            0     |            1     |            0     |            0     |             4.25 |         2.75 |            1     |            0     |            0     |            1     |                0 |            0     |
| within                | M2       |         0    |            22.65 |         0.15 |            0.669 |            0     |            0.331 |            0.922 |            0     |            0.078 |            22.65 |         0.15 |            0.669 |            0     |            0.331 |            0.922 |                0 |            0.078 |
| within                | M2n      |         0    |            18.75 |         0    |            0.766 |            0     |            0.234 |            0.968 |            0     |            0.032 |            18.75 |         0    |            0.766 |            0     |            0.234 |            0.968 |                0 |            0.032 |
| within                | M3       |         0    |            23.05 |         0    |            0.548 |            0     |            0.452 |            0.936 |            0     |            0.064 |            23.05 |         0    |            0.548 |            0     |            0.452 |            0.936 |                0 |            0.064 |
| within                | M4       |         0    |            11.3  |         0.05 |            0.912 |            0     |            0.088 |            1     |            0     |            0     |            11.3  |         0.05 |            0.912 |            0     |            0.088 |            1     |                0 |            0     |
| within                | M5       |         0    |             7.15 |         0.75 |            0.987 |            0     |            0.013 |            1     |            0     |            0     |             7.15 |         0.75 |            0.987 |            0     |            0.013 |            1     |                0 |            0     |
| within                | M5n      |         0    |             7.15 |         0.55 |            0.996 |            0     |            0.004 |            1     |            0     |            0     |             7.15 |         0.55 |            0.996 |            0     |            0.004 |            1     |                0 |            0     |
| within                | NN       |         0.25 |             3.35 |         3.35 |            1     |            0     |            0     |            1     |            0     |            0     |             3.6  |         3.1  |            1     |            0     |            0     |            1     |                0 |            0     |

## guard_priors

| scope                 | method   | prior                      |   guard_band |   guard_band_uncapped |
|:----------------------|:---------|:---------------------------|-------------:|----------------------:|
| setting/extrapolation | M0       | grid within 20 (reference) |       inf    |                inf    |
| setting/extrapolation | M0       | grid within 5              |       inf    |                inf    |
| setting/extrapolation | M0       | grid within 3              |       inf    |                inf    |
| setting/extrapolation | M0       | uniform within 20          |       inf    |                inf    |
| setting/extrapolation | M0       | uniform within 50          |       inf    |                inf    |
| setting/extrapolation | M1       | grid within 20 (reference) |       inf    |                 32    |
| setting/extrapolation | M1       | grid within 5              |       inf    |                 34.25 |
| setting/extrapolation | M1       | grid within 3              |       inf    |                 34.75 |
| setting/extrapolation | M1       | uniform within 20          |       inf    |                 24.5  |
| setting/extrapolation | M1       | uniform within 50          |        13.5  |                 13.5  |
| setting/extrapolation | M1s      | grid within 20 (reference) |       inf    |                inf    |
| setting/extrapolation | M1s      | grid within 5              |       inf    |                inf    |
| setting/extrapolation | M1s      | grid within 3              |       inf    |                inf    |
| setting/extrapolation | M1s      | uniform within 20          |       inf    |                inf    |
| setting/extrapolation | M1s      | uniform within 50          |         4.5  |                inf    |
| setting/extrapolation | M1sn     | grid within 20 (reference) |         6    |                  6    |
| setting/extrapolation | M1sn     | grid within 5              |         8.5  |                  8.5  |
| setting/extrapolation | M1sn     | grid within 3              |         9    |                  9    |
| setting/extrapolation | M1sn     | uniform within 20          |         3.5  |                  3.5  |
| setting/extrapolation | M1sn     | uniform within 50          |         0    |                  0    |
| setting/extrapolation | M2       | grid within 20 (reference) |       inf    |                 23.25 |
| setting/extrapolation | M2       | grid within 5              |       inf    |                 24.25 |
| setting/extrapolation | M2       | grid within 3              |       inf    |                 24.5  |
| setting/extrapolation | M2       | uniform within 20          |         6    |                  6    |
| setting/extrapolation | M2       | uniform within 50          |         0    |                  0    |
| setting/extrapolation | M3       | grid within 20 (reference) |        16.75 |                 16.75 |
| setting/extrapolation | M3       | grid within 5              |        19.25 |                 19.25 |
| setting/extrapolation | M3       | grid within 3              |        19.75 |                 19.75 |
| setting/extrapolation | M3       | uniform within 20          |        14.75 |                 14.75 |
| setting/extrapolation | M3       | uniform within 50          |         4    |                  4    |
| setting/extrapolation | M4       | grid within 20 (reference) |         6.5  |                  6.5  |
| setting/extrapolation | M4       | grid within 5              |        13.5  |                 13.5  |
| setting/extrapolation | M4       | grid within 3              |        13.5  |                 13.5  |
| setting/extrapolation | M4       | uniform within 20          |         1.5  |                  1.5  |
| setting/extrapolation | M4       | uniform within 50          |         0    |                  0    |
| setting/extrapolation | M5       | grid within 20 (reference) |       inf    |                 23    |
| setting/extrapolation | M5       | grid within 5              |       inf    |                 24    |
| setting/extrapolation | M5       | grid within 3              |       inf    |                 24.5  |
| setting/extrapolation | M5       | uniform within 20          |         5    |                  5    |
| setting/extrapolation | M5       | uniform within 50          |         0    |                  0    |
| setting/extrapolation | M5n      | grid within 20 (reference) |         6.75 |                  6.75 |
| setting/extrapolation | M5n      | grid within 5              |        12.5  |                 12.5  |
| setting/extrapolation | M5n      | grid within 3              |        13    |                 13    |
| setting/extrapolation | M5n      | uniform within 20          |         2.5  |                  2.5  |
| setting/extrapolation | M5n      | uniform within 50          |         0    |                  0    |
| setting/extrapolation | NN       | grid within 20 (reference) |         7    |                  7    |
| setting/extrapolation | NN       | grid within 5              |        14.25 |                 14.25 |
| setting/extrapolation | NN       | grid within 3              |        14.75 |                 14.75 |
| setting/extrapolation | NN       | uniform within 20          |         3.5  |                  3.5  |
| setting/extrapolation | NN       | uniform within 50          |         0    |                  0    |
| setting/interpolation | M0       | grid within 20 (reference) |       inf    |                inf    |
| setting/interpolation | M0       | grid within 5              |       inf    |                inf    |
| setting/interpolation | M0       | grid within 3              |       inf    |                inf    |
| setting/interpolation | M0       | uniform within 20          |       inf    |                inf    |
| setting/interpolation | M0       | uniform within 50          |       inf    |                inf    |
| setting/interpolation | M1       | grid within 20 (reference) |         8.75 |                  8.75 |
| setting/interpolation | M1       | grid within 5              |        11.25 |                 11.25 |
| setting/interpolation | M1       | grid within 3              |        11.5  |                 11.5  |
| setting/interpolation | M1       | uniform within 20          |         6    |                  6    |
| setting/interpolation | M1       | uniform within 50          |         1    |                  1    |
| setting/interpolation | M1s      | grid within 20 (reference) |       inf    |                 29.5  |
| setting/interpolation | M1s      | grid within 5              |       inf    |                 30    |
| setting/interpolation | M1s      | grid within 3              |       inf    |                 30.5  |
| setting/interpolation | M1s      | uniform within 20          |       inf    |                 27.5  |
| setting/interpolation | M1s      | uniform within 50          |         4.5  |                  4.5  |
| setting/interpolation | M1sn     | grid within 20 (reference) |         2    |                  2    |
| setting/interpolation | M1sn     | grid within 5              |         4.25 |                  4.25 |
| setting/interpolation | M1sn     | grid within 3              |         5    |                  5    |
| setting/interpolation | M1sn     | uniform within 20          |         0.25 |                  0.25 |
| setting/interpolation | M1sn     | uniform within 50          |         0    |                  0    |
| setting/interpolation | M2       | grid within 20 (reference) |         0.75 |                  0.75 |
| setting/interpolation | M2       | grid within 5              |         2.75 |                  2.75 |
| setting/interpolation | M2       | grid within 3              |         3.25 |                  3.25 |
| setting/interpolation | M2       | uniform within 20          |         0    |                  0    |
| setting/interpolation | M2       | uniform within 50          |         0    |                  0    |
| setting/interpolation | M3       | grid within 20 (reference) |        17.75 |                 17.75 |
| setting/interpolation | M3       | grid within 5              |        19    |                 19    |
| setting/interpolation | M3       | grid within 3              |        19.5  |                 19.5  |
| setting/interpolation | M3       | uniform within 20          |        12.75 |                 12.75 |
| setting/interpolation | M3       | uniform within 50          |         1.25 |                  1.25 |
| setting/interpolation | M4       | grid within 20 (reference) |         6    |                  6    |
| setting/interpolation | M4       | grid within 5              |         9.25 |                  9.25 |
| setting/interpolation | M4       | grid within 3              |        10.25 |                 10.25 |
| setting/interpolation | M4       | uniform within 20          |         3    |                  3    |
| setting/interpolation | M4       | uniform within 50          |         0    |                  0    |
| setting/interpolation | M5       | grid within 20 (reference) |         0.5  |                  0.5  |
| setting/interpolation | M5       | grid within 5              |         2.75 |                  2.75 |
| setting/interpolation | M5       | grid within 3              |         3.5  |                  3.5  |
| setting/interpolation | M5       | uniform within 20          |         0    |                  0    |
| setting/interpolation | M5       | uniform within 50          |         0    |                  0    |
| setting/interpolation | M5n      | grid within 20 (reference) |         0    |                  0    |
| setting/interpolation | M5n      | grid within 5              |         1    |                  1    |
| setting/interpolation | M5n      | grid within 3              |         1.5  |                  1.5  |
| setting/interpolation | M5n      | uniform within 20          |         0    |                  0    |
| setting/interpolation | M5n      | uniform within 50          |         0    |                  0    |
| setting/interpolation | NN       | grid within 20 (reference) |         2    |                  2    |
| setting/interpolation | NN       | grid within 5              |         4.25 |                  4.25 |
| setting/interpolation | NN       | grid within 3              |         5    |                  5    |
| setting/interpolation | NN       | uniform within 20          |         0.25 |                  0.25 |
| setting/interpolation | NN       | uniform within 50          |         0    |                  0    |
| transfer              | M0       | grid within 20 (reference) |       inf    |                inf    |
| transfer              | M0       | grid within 5              |       inf    |                inf    |
| transfer              | M0       | grid within 3              |       inf    |                inf    |
| transfer              | M0       | uniform within 20          |       inf    |                inf    |
| transfer              | M0       | uniform within 50          |       inf    |                inf    |
| transfer              | M1       | grid within 20 (reference) |       inf    |                inf    |
| transfer              | M1       | grid within 5              |       inf    |                inf    |
| transfer              | M1       | grid within 3              |       inf    |                inf    |
| transfer              | M1       | uniform within 20          |       inf    |                 59.75 |
| transfer              | M1       | uniform within 50          |       inf    |                 31.75 |
| transfer              | M1s      | grid within 20 (reference) |       inf    |                inf    |
| transfer              | M1s      | grid within 5              |       inf    |                inf    |
| transfer              | M1s      | grid within 3              |       inf    |                inf    |
| transfer              | M1s      | uniform within 20          |       inf    |                inf    |
| transfer              | M1s      | uniform within 50          |       inf    |                inf    |
| transfer              | M1sn     | grid within 20 (reference) |       inf    |                inf    |
| transfer              | M1sn     | grid within 5              |       inf    |                inf    |
| transfer              | M1sn     | grid within 3              |       inf    |                inf    |
| transfer              | M1sn     | uniform within 20          |       inf    |                inf    |
| transfer              | M1sn     | uniform within 50          |       inf    |                inf    |
| transfer              | M2       | grid within 20 (reference) |       inf    |                 41.75 |
| transfer              | M2       | grid within 5              |       inf    |                 42.75 |
| transfer              | M2       | grid within 3              |       inf    |                 43.25 |
| transfer              | M2       | uniform within 20          |       inf    |                 40.25 |
| transfer              | M2       | uniform within 50          |         6.25 |                  6.25 |
| transfer              | M3       | grid within 20 (reference) |       inf    |                 42.25 |
| transfer              | M3       | grid within 5              |       inf    |                 42.25 |
| transfer              | M3       | grid within 3              |       inf    |                 42.25 |
| transfer              | M3       | uniform within 20          |       inf    |                 41.5  |
| transfer              | M3       | uniform within 50          |         6.5  |                  6.5  |
| transfer              | M4       | grid within 20 (reference) |       inf    |                inf    |
| transfer              | M4       | grid within 5              |       inf    |                inf    |
| transfer              | M4       | grid within 3              |       inf    |                inf    |
| transfer              | M4       | uniform within 20          |       inf    |                inf    |
| transfer              | M4       | uniform within 50          |       inf    |                inf    |
| transfer              | M5       | grid within 20 (reference) |       inf    |                 42.25 |
| transfer              | M5       | grid within 5              |       inf    |                 44.25 |
| transfer              | M5       | grid within 3              |       inf    |                 44.75 |
| transfer              | M5       | uniform within 20          |       inf    |                 39.75 |
| transfer              | M5       | uniform within 50          |        15    |                 15    |
| transfer              | M5n      | grid within 20 (reference) |       inf    |                inf    |
| transfer              | M5n      | grid within 5              |       inf    |                inf    |
| transfer              | M5n      | grid within 3              |       inf    |                inf    |
| transfer              | M5n      | uniform within 20          |       inf    |                inf    |
| transfer              | M5n      | uniform within 50          |       inf    |                inf    |
| transfer              | NN       | grid within 20 (reference) |       inf    |                inf    |
| transfer              | NN       | grid within 5              |       inf    |                inf    |
| transfer              | NN       | grid within 3              |       inf    |                inf    |
| transfer              | NN       | uniform within 20          |       inf    |                inf    |
| transfer              | NN       | uniform within 50          |       inf    |                inf    |
| within                | M0       | grid within 20 (reference) |       inf    |                inf    |
| within                | M0       | grid within 5              |       inf    |                inf    |
| within                | M0       | grid within 3              |       inf    |                inf    |
| within                | M0       | uniform within 20          |       inf    |                inf    |
| within                | M0       | uniform within 50          |       inf    |                inf    |
| within                | M1       | grid within 20 (reference) |       inf    |                 29.5  |
| within                | M1       | grid within 5              |       inf    |                 31    |
| within                | M1       | grid within 3              |       inf    |                 31.25 |
| within                | M1       | uniform within 20          |        14.25 |                 14.25 |
| within                | M1       | uniform within 50          |         3.25 |                  3.25 |
| within                | M1s      | grid within 20 (reference) |         2    |                  2    |
| within                | M1s      | grid within 5              |         7.25 |                  7.25 |
| within                | M1s      | grid within 3              |         8.5  |                  8.5  |
| within                | M1s      | uniform within 20          |         0.5  |                  0.5  |
| within                | M1s      | uniform within 50          |         0    |                  0    |
| within                | M1sn     | grid within 20 (reference) |         0.75 |                  0.75 |
| within                | M1sn     | grid within 5              |         2.75 |                  2.75 |
| within                | M1sn     | grid within 3              |         4.5  |                  4.5  |
| within                | M1sn     | uniform within 20          |         0    |                  0    |
| within                | M1sn     | uniform within 50          |         0    |                  0    |
| within                | M2       | grid within 20 (reference) |         0    |                  0    |
| within                | M2       | grid within 5              |         0    |                  0    |
| within                | M2       | grid within 3              |         0.5  |                  0.5  |
| within                | M2       | uniform within 20          |         0    |                  0    |
| within                | M2       | uniform within 50          |         0    |                  0    |
| within                | M3       | grid within 20 (reference) |         0    |                  0    |
| within                | M3       | grid within 5              |         0    |                  0    |
| within                | M3       | grid within 3              |         4    |                  4    |
| within                | M3       | uniform within 20          |         0    |                  0    |
| within                | M3       | uniform within 50          |         0    |                  0    |
| within                | M4       | grid within 20 (reference) |         0    |                  0    |
| within                | M4       | grid within 5              |         0    |                  0    |
| within                | M4       | grid within 3              |         3.5  |                  3.5  |
| within                | M4       | uniform within 20          |         0    |                  0    |
| within                | M4       | uniform within 50          |         0    |                  0    |
| within                | M5       | grid within 20 (reference) |         0    |                  0    |
| within                | M5       | grid within 5              |         0    |                  0    |
| within                | M5       | grid within 3              |         6.5  |                  6.5  |
| within                | M5       | uniform within 20          |         0    |                  0    |
| within                | M5       | uniform within 50          |         0    |                  0    |
| within                | M5n      | grid within 20 (reference) |         0    |                  0    |
| within                | M5n      | grid within 5              |         0    |                  0    |
| within                | M5n      | grid within 3              |         4    |                  4    |
| within                | M5n      | uniform within 20          |         0    |                  0    |
| within                | M5n      | uniform within 50          |         0    |                  0    |
| within                | NN       | grid within 20 (reference) |         0.25 |                  0.25 |
| within                | NN       | grid within 5              |         2    |                  2    |
| within                | NN       | grid within 3              |         8    |                  8    |
| within                | NN       | uniform within 20          |         0    |                  0    |
| within                | NN       | uniform within 50          |         0    |                  0    |

## capability

|   ppk | scope    | method   |   median_d |   right |   false_reject |   trial |   adequate |
|------:|:---------|:---------|-----------:|--------:|---------------:|--------:|-----------:|
|  1    | setting  | M0       |      1.032 |   0.429 |          0.571 |   0     |          1 |
|  1    | setting  | M1       |      1.032 |   0.508 |          0.492 |   0     |          1 |
|  1    | setting  | M1n      |      1.032 |   0.556 |          0.444 |   0     |          1 |
|  1    | setting  | M1s      |      1.032 |   0.73  |          0.27  |   0     |          1 |
|  1    | setting  | M1sn     |      1.032 |   0.73  |          0.27  |   0     |          1 |
|  1    | setting  | M2       |      1.032 |   0.294 |          0.159 |   0.548 |          1 |
|  1    | setting  | M2n      |      1.032 |   0.262 |          0.127 |   0.611 |          1 |
|  1    | setting  | M3       |      1.032 |   0.254 |          0.325 |   0.421 |          1 |
|  1    | setting  | M4       |      1.032 |   0.262 |          0.302 |   0.437 |          1 |
|  1    | setting  | M5       |      1.032 |   0.294 |          0.175 |   0.532 |          1 |
|  1    | setting  | M5n      |      1.032 |   0.27  |          0.127 |   0.603 |          1 |
|  1    | setting  | NN       |      1.032 |   0.603 |          0.397 |   0     |          1 |
|  1    | transfer | M0       |      1.032 |   0.429 |          0.571 |   0     |          1 |
|  1    | transfer | M1       |      1.032 |   0.54  |          0.46  |   0     |          1 |
|  1    | transfer | M1n      |      1.032 |   0.508 |          0.492 |   0     |          1 |
|  1    | transfer | M1s      |      1.032 |   0.429 |          0.571 |   0     |          1 |
|  1    | transfer | M1sn     |      1.032 |   0.492 |          0.508 |   0     |          1 |
|  1    | transfer | M2       |      1.032 |   0.286 |          0.198 |   0.516 |          1 |
|  1    | transfer | M2n      |      1.032 |   0.452 |          0.429 |   0.119 |          1 |
|  1    | transfer | M3       |      1.032 |   0.349 |          0.278 |   0.373 |          1 |
|  1    | transfer | M4       |      1.032 |   0.5   |          0.413 |   0.087 |          1 |
|  1    | transfer | M5       |      1.032 |   0.476 |          0.349 |   0.175 |          1 |
|  1    | transfer | M5n      |      1.032 |   0.5   |          0.476 |   0.024 |          1 |
|  1    | transfer | NN       |      1.032 |   0.5   |          0.5   |   0     |          1 |
|  1    | within   | M0       |      1.032 |   0.429 |          0.571 |   0     |          1 |
|  1    | within   | M1       |      1.032 |   0.603 |          0.397 |   0     |          1 |
|  1    | within   | M1n      |      1.032 |   0.698 |          0.302 |   0     |          1 |
|  1    | within   | M1s      |      1.032 |   0.738 |          0.262 |   0     |          1 |
|  1    | within   | M1sn     |      1.032 |   0.762 |          0.238 |   0     |          1 |
|  1    | within   | M2       |      1.032 |   0.167 |          0.016 |   0.817 |          1 |
|  1    | within   | M2n      |      1.032 |   0.198 |          0.016 |   0.786 |          1 |
|  1    | within   | M3       |      1.032 |   0.016 |          0.024 |   0.96  |          1 |
|  1    | within   | M4       |      1.032 |   0.127 |          0.032 |   0.841 |          1 |
|  1    | within   | M5       |      1.032 |   0.262 |          0.048 |   0.69  |          1 |
|  1    | within   | M5n      |      1.032 |   0.27  |          0.048 |   0.683 |          1 |
|  1    | within   | NN       |      1.032 |   0.817 |          0.183 |   0     |          1 |
|  1.33 | setting  | M0       |      1.746 |   0.452 |          0.548 |   0     |          1 |
|  1.33 | setting  | M1       |      1.746 |   0.524 |          0.476 |   0     |          1 |
|  1.33 | setting  | M1n      |      1.746 |   0.595 |          0.405 |   0     |          1 |
|  1.33 | setting  | M1s      |      1.746 |   0.786 |          0.214 |   0     |          1 |
|  1.33 | setting  | M1sn     |      1.746 |   0.762 |          0.238 |   0     |          1 |
|  1.33 | setting  | M2       |      1.746 |   0.317 |          0.151 |   0.532 |          1 |
|  1.33 | setting  | M2n      |      1.746 |   0.341 |          0.095 |   0.563 |          1 |
|  1.33 | setting  | M3       |      1.746 |   0.262 |          0.278 |   0.46  |          1 |
|  1.33 | setting  | M4       |      1.746 |   0.325 |          0.238 |   0.437 |          1 |
|  1.33 | setting  | M5       |      1.746 |   0.317 |          0.159 |   0.524 |          1 |
|  1.33 | setting  | M5n      |      1.746 |   0.333 |          0.04  |   0.627 |          1 |
|  1.33 | setting  | NN       |      1.746 |   0.651 |          0.349 |   0     |          1 |
|  1.33 | transfer | M0       |      1.746 |   0.452 |          0.548 |   0     |          1 |
|  1.33 | transfer | M1       |      1.746 |   0.54  |          0.46  |   0     |          1 |
|  1.33 | transfer | M1n      |      1.746 |   0.532 |          0.468 |   0     |          1 |
|  1.33 | transfer | M1s      |      1.746 |   0.452 |          0.548 |   0     |          1 |
|  1.33 | transfer | M1sn     |      1.746 |   0.508 |          0.492 |   0     |          1 |
|  1.33 | transfer | M2       |      1.746 |   0.325 |          0.167 |   0.508 |          1 |
|  1.33 | transfer | M2n      |      1.746 |   0.452 |          0.429 |   0.119 |          1 |
|  1.33 | transfer | M3       |      1.746 |   0.365 |          0.27  |   0.365 |          1 |
|  1.33 | transfer | M4       |      1.746 |   0.5   |          0.397 |   0.103 |          1 |
|  1.33 | transfer | M5       |      1.746 |   0.492 |          0.294 |   0.214 |          1 |
|  1.33 | transfer | M5n      |      1.746 |   0.5   |          0.476 |   0.024 |          1 |
|  1.33 | transfer | NN       |      1.746 |   0.508 |          0.492 |   0     |          1 |
|  1.33 | within   | M0       |      1.746 |   0.452 |          0.548 |   0     |          1 |
|  1.33 | within   | M1       |      1.746 |   0.667 |          0.333 |   0     |          1 |
|  1.33 | within   | M1n      |      1.746 |   0.778 |          0.222 |   0     |          1 |
|  1.33 | within   | M1s      |      1.746 |   0.81  |          0.19  |   0     |          1 |
|  1.33 | within   | M1sn     |      1.746 |   0.817 |          0.183 |   0     |          1 |
|  1.33 | within   | M2       |      1.746 |   0.198 |          0.008 |   0.794 |          1 |
|  1.33 | within   | M2n      |      1.746 |   0.278 |          0.016 |   0.706 |          1 |
|  1.33 | within   | M3       |      1.746 |   0.048 |          0.016 |   0.937 |          1 |
|  1.33 | within   | M4       |      1.746 |   0.23  |          0.024 |   0.746 |          1 |
|  1.33 | within   | M5       |      1.746 |   0.444 |          0.024 |   0.532 |          1 |
|  1.33 | within   | M5n      |      1.746 |   0.405 |          0.032 |   0.563 |          1 |
|  1.33 | within   | NN       |      1.746 |   0.913 |          0.087 |   0     |          1 |
|  1.67 | setting  | M0       |      2.459 |   0.46  |          0.54  |   0     |          1 |
|  1.67 | setting  | M1       |      2.459 |   0.579 |          0.421 |   0     |          1 |
|  1.67 | setting  | M1n      |      2.459 |   0.683 |          0.317 |   0     |          1 |
|  1.67 | setting  | M1s      |      2.459 |   0.833 |          0.167 |   0     |          1 |
|  1.67 | setting  | M1sn     |      2.459 |   0.817 |          0.183 |   0     |          1 |
|  1.67 | setting  | M2       |      2.459 |   0.421 |          0.135 |   0.444 |          1 |
|  1.67 | setting  | M2n      |      2.459 |   0.405 |          0.056 |   0.54  |          1 |
|  1.67 | setting  | M3       |      2.459 |   0.286 |          0.262 |   0.452 |          1 |
|  1.67 | setting  | M4       |      2.459 |   0.365 |          0.206 |   0.429 |          1 |
|  1.67 | setting  | M5       |      2.459 |   0.373 |          0.151 |   0.476 |          1 |
|  1.67 | setting  | M5n      |      2.459 |   0.381 |          0.032 |   0.587 |          1 |
|  1.67 | setting  | NN       |      2.459 |   0.746 |          0.254 |   0     |          1 |
|  1.67 | transfer | M0       |      2.459 |   0.46  |          0.54  |   0     |          1 |
|  1.67 | transfer | M1       |      2.459 |   0.571 |          0.429 |   0     |          1 |
|  1.67 | transfer | M1n      |      2.459 |   0.548 |          0.452 |   0     |          1 |
|  1.67 | transfer | M1s      |      2.459 |   0.476 |          0.524 |   0     |          1 |
|  1.67 | transfer | M1sn     |      2.459 |   0.516 |          0.484 |   0     |          1 |
|  1.67 | transfer | M2       |      2.459 |   0.365 |          0.159 |   0.476 |          1 |
|  1.67 | transfer | M2n      |      2.459 |   0.452 |          0.429 |   0.119 |          1 |
|  1.67 | transfer | M3       |      2.459 |   0.397 |          0.254 |   0.349 |          1 |
|  1.67 | transfer | M4       |      2.459 |   0.5   |          0.389 |   0.111 |          1 |
|  1.67 | transfer | M5       |      2.459 |   0.524 |          0.278 |   0.198 |          1 |
|  1.67 | transfer | M5n      |      2.459 |   0.5   |          0.468 |   0.032 |          1 |
|  1.67 | transfer | NN       |      2.459 |   0.532 |          0.468 |   0     |          1 |
|  1.67 | within   | M0       |      2.459 |   0.46  |          0.54  |   0     |          1 |
|  1.67 | within   | M1       |      2.459 |   0.683 |          0.317 |   0     |          1 |
|  1.67 | within   | M1n      |      2.459 |   0.825 |          0.175 |   0     |          1 |
|  1.67 | within   | M1s      |      2.459 |   0.841 |          0.159 |   0     |          1 |
|  1.67 | within   | M1sn     |      2.459 |   0.881 |          0.119 |   0     |          1 |
|  1.67 | within   | M2       |      2.459 |   0.27  |          0     |   0.73  |          1 |
|  1.67 | within   | M2n      |      2.459 |   0.333 |          0     |   0.667 |          1 |
|  1.67 | within   | M3       |      2.459 |   0.071 |          0.016 |   0.913 |          1 |
|  1.67 | within   | M4       |      2.459 |   0.397 |          0.008 |   0.595 |          1 |
|  1.67 | within   | M5       |      2.459 |   0.563 |          0.008 |   0.429 |          1 |
|  1.67 | within   | M5n      |      2.459 |   0.548 |          0.008 |   0.444 |          1 |
|  1.67 | within   | NN       |      2.459 |   0.929 |          0.071 |   0     |          1 |
|  2    | setting  | M0       |      3.145 |   0.468 |          0.532 |   0     |          1 |
|  2    | setting  | M1       |      3.145 |   0.627 |          0.373 |   0     |          1 |
|  2    | setting  | M1n      |      3.145 |   0.714 |          0.286 |   0     |          1 |
|  2    | setting  | M1s      |      3.145 |   0.849 |          0.151 |   0     |          1 |
|  2    | setting  | M1sn     |      3.145 |   0.841 |          0.159 |   0     |          1 |
|  2    | setting  | M2       |      3.145 |   0.468 |          0.103 |   0.429 |          1 |
|  2    | setting  | M2n      |      3.145 |   0.444 |          0.056 |   0.5   |          1 |
|  2    | setting  | M3       |      3.145 |   0.302 |          0.246 |   0.452 |          1 |
|  2    | setting  | M4       |      3.145 |   0.389 |          0.183 |   0.429 |          1 |
|  2    | setting  | M5       |      3.145 |   0.389 |          0.111 |   0.5   |          1 |
|  2    | setting  | M5n      |      3.145 |   0.429 |          0.024 |   0.548 |          1 |
|  2    | setting  | NN       |      3.145 |   0.794 |          0.206 |   0     |          1 |
|  2    | transfer | M0       |      3.145 |   0.468 |          0.532 |   0     |          1 |
|  2    | transfer | M1       |      3.145 |   0.603 |          0.397 |   0     |          1 |
|  2    | transfer | M1n      |      3.145 |   0.556 |          0.444 |   0     |          1 |
|  2    | transfer | M1s      |      3.145 |   0.476 |          0.524 |   0     |          1 |
|  2    | transfer | M1sn     |      3.145 |   0.516 |          0.484 |   0     |          1 |
|  2    | transfer | M2       |      3.145 |   0.389 |          0.159 |   0.452 |          1 |
|  2    | transfer | M2n      |      3.145 |   0.452 |          0.421 |   0.127 |          1 |
|  2    | transfer | M3       |      3.145 |   0.405 |          0.222 |   0.373 |          1 |
|  2    | transfer | M4       |      3.145 |   0.5   |          0.389 |   0.111 |          1 |
|  2    | transfer | M5       |      3.145 |   0.548 |          0.27  |   0.183 |          1 |
|  2    | transfer | M5n      |      3.145 |   0.516 |          0.46  |   0.024 |          1 |
|  2    | transfer | NN       |      3.145 |   0.532 |          0.468 |   0     |          1 |
|  2    | within   | M0       |      3.145 |   0.468 |          0.532 |   0     |          1 |
|  2    | within   | M1       |      3.145 |   0.73  |          0.27  |   0     |          1 |
|  2    | within   | M1n      |      3.145 |   0.865 |          0.135 |   0     |          1 |
|  2    | within   | M1s      |      3.145 |   0.897 |          0.103 |   0     |          1 |
|  2    | within   | M1sn     |      3.145 |   0.913 |          0.087 |   0     |          1 |
|  2    | within   | M2       |      3.145 |   0.325 |          0     |   0.675 |          1 |
|  2    | within   | M2n      |      3.145 |   0.381 |          0     |   0.619 |          1 |
|  2    | within   | M3       |      3.145 |   0.143 |          0     |   0.857 |          1 |
|  2    | within   | M4       |      3.145 |   0.556 |          0.008 |   0.437 |          1 |
|  2    | within   | M5       |      3.145 |   0.667 |          0.008 |   0.325 |          1 |
|  2    | within   | M5n      |      3.145 |   0.675 |          0     |   0.325 |          1 |
|  2    | within   | NN       |      3.145 |   0.96  |          0.04  |   0     |          1 |

## m0_split

| variant                                        |   resolution_floors |   safe_floors |   resolution_adequate |   safe_adequate |   resolution_failing |   safe_failing |
|:-----------------------------------------------|--------------------:|--------------:|----------------------:|----------------:|---------------------:|---------------:|
| nominal simulation                             |              108.35 |        108.35 |                 109.4 |           109.4 |                17    |          17    |
| cup-depth reference offset removed (-0.936 mm) |               64.85 |         64.85 |                  99.1 |            99.1 |                19.85 |          19.85 |

## nominal_offset

| method           |   cases |   resolution_floors |   safe_floors |   median_abs_error |   abs_error_p90 |
|:-----------------|--------:|--------------------:|--------------:|-------------------:|----------------:|
| nominal + offset |      18 |                1.9  |          1.9  |              0.318 |           1.776 |
| M0               |      18 |               28.5  |         28.5  |             13.963 |          28.06  |
| M1               |      18 |               16.95 |         16.95 |              5.366 |          16.522 |
| M1s              |      18 |              125.4  |        125.4  |            122.153 |         125.165 |
| Mc               |      18 |               18.7  |         18.7  |             15.188 |          18.599 |
| M2               |      18 |               10.15 |          0.05 |              1.052 |           4.65  |
| M5               |      18 |                7.45 |          3.05 |              3.597 |           4.759 |
| M1n              |      18 |              130.15 |        130.15 |            127.094 |         129.438 |
| NN               |      18 |              130.1  |        130.1  |            126.829 |         129.305 |

## variogram

| qc            | geometry   |   lag_batches |   pairs |   q95_floors |
|:--------------|:-----------|--------------:|--------:|-------------:|
| drawin_mid    | concave    |             1 |      81 |        0.735 |
| drawin_mid    | concave    |             2 |      72 |        0.681 |
| drawin_mid    | concave    |             3 |      63 |        0.875 |
| drawin_mid    | concave    |             4 |      54 |        0.929 |
| drawin_mid    | concave    |             5 |      45 |        1     |
| drawin_mid    | concave    |             6 |      36 |        1.129 |
| drawin_mid    | concave    |             7 |      27 |        1.045 |
| drawin_mid    | concave    |             8 |      18 |        1.081 |
| drawin_mid    | concave    |             9 |       9 |        1.389 |
| drawin_mid    | convex     |             1 |      81 |        0.858 |
| drawin_mid    | convex     |             2 |      72 |        0.949 |
| drawin_mid    | convex     |             3 |      63 |        1.106 |
| drawin_mid    | convex     |             4 |      54 |        1.156 |
| drawin_mid    | convex     |             5 |      45 |        0.958 |
| drawin_mid    | convex     |             6 |      36 |        0.948 |
| drawin_mid    | convex     |             7 |      27 |        0.908 |
| drawin_mid    | convex     |             8 |      18 |        0.887 |
| drawin_mid    | convex     |             9 |       9 |        1.059 |
| drawin_corner | concave    |             1 |      81 |        0.439 |
| drawin_corner | concave    |             2 |      72 |        0.589 |
| drawin_corner | concave    |             3 |      63 |        0.839 |
| drawin_corner | concave    |             4 |      54 |        1.053 |
| drawin_corner | concave    |             5 |      45 |        0.944 |
| drawin_corner | concave    |             6 |      36 |        1.021 |
| drawin_corner | concave    |             7 |      27 |        1.042 |
| drawin_corner | concave    |             8 |      18 |        1.067 |
| drawin_corner | concave    |             9 |       9 |        1.068 |
| drawin_corner | convex     |             1 |      81 |        0.758 |
| drawin_corner | convex     |             2 |      72 |        0.95  |
| drawin_corner | convex     |             3 |      63 |        0.871 |
| drawin_corner | convex     |             4 |      54 |        0.894 |
| drawin_corner | convex     |             5 |      45 |        1.393 |
| drawin_corner | convex     |             6 |      36 |        1.565 |
| drawin_corner | convex     |             7 |      27 |        1.567 |
| drawin_corner | convex     |             8 |      18 |        1.19  |
| drawin_corner | convex     |             9 |       9 |        1.126 |
| waviness      | concave    |             1 |      81 |        0.413 |
| waviness      | concave    |             2 |      72 |        0.658 |
| waviness      | concave    |             3 |      63 |        0.889 |
| waviness      | concave    |             4 |      54 |        1.157 |
| waviness      | concave    |             5 |      45 |        1.395 |
| waviness      | concave    |             6 |      36 |        1.536 |
| waviness      | concave    |             7 |      27 |        1.726 |
| waviness      | concave    |             8 |      18 |        1.99  |
| waviness      | concave    |             9 |       9 |        1.664 |
| waviness      | convex     |             1 |      81 |        0.611 |
| waviness      | convex     |             2 |      72 |        0.931 |
| waviness      | convex     |             3 |      63 |        0.942 |
| waviness      | convex     |             4 |      54 |        0.839 |
| waviness      | convex     |             5 |      45 |        1.033 |
| waviness      | convex     |             6 |      36 |        0.991 |
| waviness      | convex     |             7 |      27 |        1.096 |
| waviness      | convex     |             8 |      18 |        1.261 |
| waviness      | convex     |             9 |       9 |        1.419 |
| wall_op10     | concave    |             1 |      81 |        0.505 |
| wall_op10     | concave    |             2 |      72 |        0.802 |
| wall_op10     | concave    |             3 |      63 |        0.922 |
| wall_op10     | concave    |             4 |      54 |        1.074 |
| wall_op10     | concave    |             5 |      45 |        1.042 |
| wall_op10     | concave    |             6 |      36 |        1.326 |
| wall_op10     | concave    |             7 |      27 |        1.193 |
| wall_op10     | concave    |             8 |      18 |        1.374 |
| wall_op10     | concave    |             9 |       9 |        1.331 |
| wall_op10     | convex     |             1 |      81 |        0.795 |
| wall_op10     | convex     |             2 |      72 |        0.936 |
| wall_op10     | convex     |             3 |      63 |        0.876 |
| wall_op10     | convex     |             4 |      54 |        0.93  |
| wall_op10     | convex     |             5 |      45 |        0.995 |
| wall_op10     | convex     |             6 |      36 |        1.115 |
| wall_op10     | convex     |             7 |      27 |        1.27  |
| wall_op10     | convex     |             8 |      18 |        1.217 |
| wall_op10     | convex     |             9 |       9 |        1.506 |
| arm_op20      | concave    |             1 |      81 |        0.598 |
| arm_op20      | concave    |             2 |      72 |        0.813 |
| arm_op20      | concave    |             3 |      63 |        0.939 |
| arm_op20      | concave    |             4 |      54 |        1.114 |
| arm_op20      | concave    |             5 |      45 |        1.334 |
| arm_op20      | concave    |             6 |      36 |        1.495 |
| arm_op20      | concave    |             7 |      27 |        1.739 |
| arm_op20      | concave    |             8 |      18 |        1.992 |
| arm_op20      | concave    |             9 |       9 |        1.629 |
| arm_op20      | convex     |             1 |      81 |        0.702 |
| arm_op20      | convex     |             2 |      72 |        0.973 |
| arm_op20      | convex     |             3 |      63 |        0.951 |
| arm_op20      | convex     |             4 |      54 |        0.999 |
| arm_op20      | convex     |             5 |      45 |        0.932 |
| arm_op20      | convex     |             6 |      36 |        1.053 |
| arm_op20      | convex     |             7 |      27 |        1.009 |
| arm_op20      | convex     |             8 |      18 |        1.033 |
| arm_op20      | convex     |             9 |       9 |        1.234 |
| depth_op10    | concave    |             1 |      81 |        0.484 |
| depth_op10    | concave    |             2 |      72 |        0.804 |
| depth_op10    | concave    |             3 |      63 |        0.78  |
| depth_op10    | concave    |             4 |      54 |        0.848 |
| depth_op10    | concave    |             5 |      45 |        1.047 |
| depth_op10    | concave    |             6 |      36 |        1.102 |
| depth_op10    | concave    |             7 |      27 |        1.204 |
| depth_op10    | concave    |             8 |      18 |        1.454 |
| depth_op10    | concave    |             9 |       9 |        1.564 |
| depth_op10    | convex     |             1 |      81 |        0.563 |
| depth_op10    | convex     |             2 |      72 |        0.768 |
| depth_op10    | convex     |             3 |      63 |        0.922 |
| depth_op10    | convex     |             4 |      54 |        0.87  |
| depth_op10    | convex     |             5 |      45 |        0.997 |
| depth_op10    | convex     |             6 |      36 |        1.088 |
| depth_op10    | convex     |             7 |      27 |        1.046 |
| depth_op10    | convex     |             8 |      18 |        1.114 |
| depth_op10    | convex     |             9 |       9 |        1.214 |
| dome_op20     | concave    |             1 |      81 |        0.639 |
| dome_op20     | concave    |             2 |      72 |        0.776 |
| dome_op20     | concave    |             3 |      63 |        0.886 |
| dome_op20     | concave    |             4 |      54 |        0.996 |
| dome_op20     | concave    |             5 |      45 |        1.19  |
| dome_op20     | concave    |             6 |      36 |        1.397 |
| dome_op20     | concave    |             7 |      27 |        1.364 |
| dome_op20     | concave    |             8 |      18 |        1.493 |
| dome_op20     | concave    |             9 |       9 |        1.386 |
| dome_op20     | convex     |             1 |      81 |        0.461 |
| dome_op20     | convex     |             2 |      72 |        0.596 |
| dome_op20     | convex     |             3 |      63 |        0.728 |
| dome_op20     | convex     |             4 |      54 |        0.884 |
| dome_op20     | convex     |             5 |      45 |        0.973 |
| dome_op20     | convex     |             6 |      36 |        1.078 |
| dome_op20     | convex     |             7 |      27 |        1.226 |
| dome_op20     | convex     |             8 |      18 |        1.413 |
| dome_op20     | convex     |             9 |       9 |        1.622 |

## floor_protocol

| qc            | geometry   |   floor |   sigma_lt |   sigma_st |   sigma_within_batch |   sigma_between_batch |   floor_over_sigma_lt |   floor_over_sigma_st |   normal_model_floor |   series_with_sigma_w_above_sigma_lt |   max_excess_sigma_w_over_sigma_lt |   sigma_lt_median_series |   model_floor_subgroups_of_5 |   subgroup5_over_batch50 |
|:--------------|:-----------|--------:|-----------:|-----------:|---------------------:|----------------------:|----------------------:|----------------------:|---------------------:|-------------------------------------:|-----------------------------------:|-------------------------:|-----------------------------:|-------------------------:|
| drawin_mid    | concave    |   0.05  |      0.048 |      0.045 |                0.045 |                 0.016 |                 1.039 |                 1.093 |                0.048 |                                    0 |                             -0.008 |                    0.041 |                        0.072 |                    1.498 |
| drawin_mid    | convex     |   0.052 |      0.038 |      0.029 |                0.034 |                 0.018 |                 1.359 |                 1.786 |                0.051 |                                    0 |                             -0.024 |                    0.034 |                        0.065 |                    1.276 |
| drawin_corner | concave    |   0.053 |      0.038 |      0.035 |                0.034 |                 0.016 |                 1.395 |                 1.524 |                0.047 |                                    0 |                             -0.016 |                    0.031 |                        0.062 |                    1.316 |
| drawin_corner | convex     |   0.03  |      0.025 |      0.021 |                0.023 |                 0.01  |                 1.2   |                 1.407 |                0.03  |                                    0 |                             -0.01  |                    0.023 |                        0.04  |                    1.343 |
| waviness      | concave    |   0.004 |      0.002 |      0.002 |                0.002 |                 0.001 |                 1.577 |                 2.004 |                0.003 |                                    0 |                             -0.005 |                    0.002 |                        0.004 |                    1.214 |
| waviness      | convex     |   0.002 |      0.003 |      0.003 |                0.003 |                 0.001 |                 0.744 |                 0.77  |                0.002 |                                    2 |                              0.002 |                    0.003 |                        0.004 |                    1.863 |
| wall_op10     | concave    |   0.081 |      0.06  |      0.052 |                0.055 |                 0.025 |                 1.339 |                 1.559 |                0.074 |                                    0 |                             -0.008 |                    0.051 |                        0.098 |                    1.33  |
| wall_op10     | convex     |   0.078 |      0.11  |      0.107 |                0.108 |                 0.02  |                 0.706 |                 0.727 |                0.07  |                                    3 |                              0.003 |                    0.117 |                        0.145 |                    2.072 |
| arm_op20      | concave    |   0.116 |      0.067 |      0.046 |                0.054 |                 0.042 |                 1.73  |                 2.524 |                0.118 |                                    0 |                             -0.045 |                    0.061 |                        0.134 |                    1.135 |
| arm_op20      | convex     |   0.1   |      0.125 |      0.118 |                0.122 |                 0.031 |                 0.797 |                 0.85  |                0.098 |                                    0 |                             -0.01  |                    0.107 |                        0.174 |                    1.775 |
| depth_op10    | concave    |   0.009 |      0.006 |      0.005 |                0.006 |                 0.003 |                 1.411 |                 1.705 |                0.008 |                                    0 |                             -0.03  |                    0.004 |                        0.01  |                    1.32  |
| depth_op10    | convex     |   0.012 |      0.008 |      0.005 |                0.006 |                 0.004 |                 1.64  |                 2.259 |                0.012 |                                    0 |                             -0.028 |                    0.007 |                        0.014 |                    1.187 |
| dome_op20     | concave    |   0.003 |      0.003 |      0.002 |                0.003 |                 0.001 |                 1.222 |                 1.505 |                0.003 |                                    0 |                             -0.001 |                    0.002 |                        0.004 |                    1.367 |
| dome_op20     | convex     |   0.008 |      0.005 |      0.004 |                0.004 |                 0.003 |                 1.554 |                 1.865 |                0.008 |                                    0 |                             -0.062 |                    0.005 |                        0.01  |                    1.181 |

## resolution_steps

| qc            |   median_step |   step_over_floor |   distinct_values_total |   distinct_per_series_median |   distinct_per_series_min |   distinct_per_series_max |   alternatives_with_zero_q95_se |
|:--------------|--------------:|------------------:|------------------------:|-----------------------------:|--------------------------:|--------------------------:|--------------------------------:|
| drawin_mid    |         0.019 |             0.378 |                      71 |                         10   |                         6 |                        21 |                               5 |
| drawin_corner |         0     |             0.003 |                    8905 |                        497.5 |                       491 |                       500 |                               0 |
| waviness      |         0     |             0.003 |                    7796 |                        480   |                       469 |                       494 |                               0 |
| wall_op10     |         0     |             0.005 |                    8937 |                        499   |                       497 |                       500 |                               0 |
| arm_op20      |         0     |             0.004 |                    8969 |                        500   |                       496 |                       500 |                               0 |
| depth_op10    |         0     |             0.003 |                    8748 |                        493   |                       486 |                       497 |                               0 |
| dome_op20     |         0     |             0.004 |                    8466 |                        490   |                       474 |                       497 |                               0 |

## runs

| alternative        |   start_temp_C |   rise_first_150_K |   rise_series_K |   sheet_median_um |   stroke_speed_mm_s |
|:-------------------|---------------:|-------------------:|----------------:|------------------:|--------------------:|
| concave/100/coarse |         20.456 |              4.572 |           6.661 |           991.226 |              46.985 |
| concave/100/fine   |         22.99  |              4.57  |           6.375 |           986.91  |              47.002 |
| concave/100/medium |         23.012 |              3.421 |           3.729 |           992.699 |              46.992 |
| concave/300/coarse |         23.598 |              4.288 |           5.722 |           992.006 |              79.005 |
| concave/300/fine   |         27.208 |              2.645 |           1.88  |           992.432 |              79.012 |
| concave/300/medium |         25.663 |              3.464 |           3.62  |           992.937 |              79.016 |
| concave/500/coarse |         22.601 |              4.951 |           6.079 |           991.845 |              78.925 |
| concave/500/fine   |         21.879 |              3.309 |           6.799 |           991.767 |              78.948 |
| concave/500/medium |         25.57  |              3.267 |           4.764 |           991.774 |              78.928 |
| convex/100/coarse  |         26.548 |              1.531 |           2.662 |           986.025 |              46.667 |
| convex/100/fine    |         28.082 |              1.124 |           1.465 |           986.717 |              46.688 |
| convex/100/medium  |         28.226 |              0.984 |           1.144 |           986.325 |              46.681 |
| convex/300/coarse  |         23.935 |              4.001 |           5.893 |           990.23  |              78.214 |
| convex/300/fine    |         26.908 |              1.748 |           2.576 |           985.631 |              78.095 |
| convex/300/medium  |         21.87  |              4.139 |           6.644 |           985.774 |              78.029 |
| convex/500/coarse  |         24.671 |              3.69  |           5.713 |           990.619 |              78.321 |
| convex/500/fine    |         29.646 |              1.492 |           1.966 |           990.299 |              78.298 |
| convex/500/medium  |         27.529 |              2.487 |           3.269 |           990.367 |              78.307 |

## force_effect

| qc            | geometry   |   real_effect |   sim_effect |   ratio |
|:--------------|:-----------|--------------:|-------------:|--------:|
| drawin_mid    | concave    |        -0.415 |       -2.131 |   5.13  |
| drawin_mid    | convex     |        -0.418 |       -2.034 |   4.871 |
| drawin_corner | concave    |        -0.342 |       -1.175 |   3.437 |
| drawin_corner | convex     |        -0.335 |       -0.896 |   2.673 |

## arm_sign

| geometry   |   bhf_kN |   simulations |   sims_downward |   parts |   parts_downward |
|:-----------|---------:|--------------:|----------------:|--------:|-----------------:|
| concave    |      100 |            66 |           0.894 |    1498 |                0 |
| concave    |      300 |            66 |           1     |    1500 |                0 |
| concave    |      500 |            66 |           1     |    1500 |                0 |
| convex     |      100 |            66 |           1     |    1500 |                1 |
| convex     |      300 |            66 |           1     |    1496 |                1 |
| convex     |      500 |            66 |           1     |    1496 |                1 |

## q95_unit

| scope    | method   |   resolution_floors |   safe_floors |
|:---------|:---------|--------------------:|--------------:|
| setting  | M0       |               76.2  |         76.2  |
| setting  | M1       |               17.5  |         17.5  |
| setting  | M1s      |               14.85 |         14.85 |
| setting  | M2       |               15.2  |          5.95 |
| setting  | M5       |               17.9  |          6.15 |
| setting  | M5n      |               16.5  |          5.05 |
| setting  | NN       |                6.85 |          6.85 |
| transfer | M0       |               76.2  |         76.2  |
| transfer | M1       |               30.4  |         30.4  |
| transfer | M1s      |              133.05 |        133.05 |
| transfer | M2       |               41.3  |         12.65 |
| transfer | M5       |               33.85 |         29.95 |
| transfer | M5n      |              140.4  |        136.8  |
| transfer | NN       |              138.55 |        138.55 |
| within   | M0       |               76.2  |         76.2  |
| within   | M1       |               12.35 |         12.35 |
| within   | M1s      |                5.3  |          5.3  |
| within   | M2       |               16.9  |          0.15 |
| within   | M5       |                6.85 |          0.4  |
| within   | M5n      |                6.65 |          0.6  |
| within   | NN       |                2.75 |          2.75 |

## sibling strata: cases

|   resolved_siblings |   cases |
|--------------------:|--------:|
|                   0 |      58 |
|                   1 |      34 |
|                   2 |      34 |
