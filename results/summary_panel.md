# Analyses requested in review

## decomposition

| distance          | relations         |   rules |   share_relation |   share_rule |   share_interaction | best_rule_range    |
|:------------------|:------------------|--------:|-----------------:|-------------:|--------------------:|:-------------------|
| resolution_floors | all relations     |      11 |            0.686 |        0.06  |               0.254 | [8.45, 35.3, 3.35] |
| resolution_floors | within the family |      11 |            0.148 |        0.681 |               0.17  | [8.45, 3.35]       |
| safe_floors       | all relations     |      11 |            0.658 |        0.153 |               0.189 |                    |
| safe_floors       | within the family |      11 |            0.353 |        0.517 |               0.13  |                    |

## sibling_strata

|   resolved_siblings | method   |   cases |   resolution_floors |   safe_floors |   resolution_adequate |   safe_adequate |   resolution_failing |   safe_failing |   abs_error_p90 |
|--------------------:|:---------|--------:|--------------------:|--------------:|----------------------:|----------------:|---------------------:|---------------:|----------------:|
|                   0 | M0       |      58 |              115.1  |        115.1  |                115.15 |          115.15 |                26.95 |          26.95 |         110.955 |
|                   0 | M1       |      58 |               14.6  |         14.6  |                 17.85 |           17.85 |                13.8  |          13.8  |          17.355 |
|                   0 | M1n      |      58 |                9.2  |          9.2  |                  4.55 |            4.55 |                 9.4  |           9.4  |           9.06  |
|                   0 | M1s      |      58 |                6.85 |          6.85 |                  7.65 |            7.65 |                 6.85 |           6.85 |           6.149 |
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
|      500 | extrapolation | M2       |      42 |               18.65 |          9.95 |                 26.85 |           10.75 |                17.9  |           8.3  |
|      500 | extrapolation | M2n      |      42 |               17.65 |          3.6  |                 19.6  |            5.85 |                 7.6  |           0    |
|      500 | extrapolation | M3       |      42 |               24.75 |         15.15 |                 25.35 |           10.25 |                22.2  |          15.15 |
|      500 | extrapolation | M4       |      42 |               12.2  |          3.15 |                 11.45 |            4.45 |                12.65 |           0    |
|      500 | extrapolation | M5       |      42 |               19.6  |          9.65 |                 33.9  |            9.8  |                18.8  |           6.8  |
|      500 | extrapolation | M5n      |      42 |               18.45 |          2.35 |                 22.5  |            3.95 |                 7.7  |           0    |
|      500 | extrapolation | NN       |      42 |                4.85 |          4.85 |                  6.65 |            6.65 |                 2.3  |           2.3  |

## source_floor

| method   | floor         |   resolution_floors |   safe_floors |   resolution_adequate |   safe_adequate |   resolution_failing |   safe_failing |
|:---------|:--------------|--------------------:|--------------:|----------------------:|----------------:|---------------------:|---------------:|
| M0       | target family |              108.35 |        108.35 |                109.4  |          109.4  |                17    |          17    |
| M0       | source family |              103.75 |        103.75 |                105.45 |          105.45 |                27.9  |          27.9  |
| M1       | target family |               35.3  |         35.3  |                 35.65 |           35.65 |                32.6  |          32.6  |
| M1       | source family |               32.9  |         32.9  |                 24    |           24    |                35.2  |          35.2  |
| M1n      | target family |              130.7  |        130.7  |                128.5  |          128.5  |               172.65 |         172.65 |
| M1n      | source family |              130.5  |        130.5  |                165.25 |          165.25 |               129    |         129    |
| M1s      | target family |              122.3  |        122.3  |                122.45 |          122.45 |               122.2  |         122.2  |
| M1s      | source family |              120.65 |        120.65 |                118.15 |          118.15 |               124.65 |         124.65 |
| M2       | target family |               50.65 |         15.8  |                 51.55 |           23.2  |                48.6  |          11.05 |
| M2       | source family |               40.75 |         26.4  |                 29.5  |            9.7  |                41.85 |          26.85 |
| M2n      | target family |              132.35 |        129.05 |                130.15 |          126.85 |               180.7  |         164.55 |
| M2n      | source family |              133.15 |        127.85 |                175.1  |          155.4  |               131.6  |         126.35 |
| M3       | target family |               48.75 |         20.5  |                 49.95 |           20.6  |                47.7  |          19.9  |
| M3       | source family |               40.15 |         17.1  |                 35.05 |           15.5  |                40.65 |          17.5  |
| M4       | target family |              133.1  |        128.45 |                130.75 |          125.6  |               170.9  |         163.95 |
| M4       | source family |              134.85 |        125.95 |                173.9  |          161.05 |               133.15 |         124.25 |
| M5       | target family |               38.4  |         27.5  |                 44    |           27.05 |                35.4  |          31.75 |
| M5       | source family |               35.2  |         31.3  |                 25.85 |           14.95 |                35.2  |          33.3  |
| M5n      | target family |              132.15 |        129.55 |                129.9  |          127.3  |               171.4  |         167.15 |
| M5n      | source family |              132.5  |        128.1  |                171.75 |          164.95 |               131.1  |         126.7  |
| NN       | target family |              130.5  |        130.5  |                128.4  |          128.4  |               169.15 |         169.15 |
| NN       | source family |              130.4  |        130.4  |                168.05 |          168.05 |               128.85 |         128.85 |

## physical_units

| scope    | method   | qc            |   resolution_floors |   safe_floors |
|:---------|:---------|:--------------|--------------------:|--------------:|
| setting  | M0       | arm_op20      |                4    |          4    |
| setting  | M0       | depth_op10    |                1.05 |          1.05 |
| setting  | M0       | dome_op20     |                0.15 |          0.15 |
| setting  | M0       | drawin_corner |                3.45 |          3.45 |
| setting  | M0       | drawin_mid    |                2    |          2    |
| setting  | M0       | wall_op10     |                2.25 |          2.25 |
| setting  | M0       | waviness      |                0.1  |          0.1  |
| setting  | M1       | arm_op20      |                2.6  |          2.6  |
| setting  | M1       | depth_op10    |                0.3  |          0.3  |
| setting  | M1       | dome_op20     |                0.05 |          0.05 |
| setting  | M1       | drawin_corner |                0.75 |          0.75 |
| setting  | M1       | drawin_mid    |                1.4  |          1.4  |
| setting  | M1       | wall_op10     |                1.15 |          1.15 |
| setting  | M1       | waviness      |                0.05 |          0.05 |
| setting  | M1s      | arm_op20      |                3.05 |          3.05 |
| setting  | M1s      | depth_op10    |                1.45 |          1.45 |
| setting  | M1s      | dome_op20     |                0.1  |          0.1  |
| setting  | M1s      | drawin_corner |                0.1  |          0.1  |
| setting  | M1s      | drawin_mid    |                0.2  |          0.2  |
| setting  | M1s      | wall_op10     |                0.2  |          0.2  |
| setting  | M1s      | waviness      |                0.1  |          0.1  |
| setting  | M2       | arm_op20      |                3.2  |          0.95 |
| setting  | M2       | depth_op10    |                0.15 |          0.15 |
| setting  | M2       | dome_op20     |                0.2  |          0.05 |
| setting  | M2       | drawin_corner |                0.25 |          0.1  |
| setting  | M2       | drawin_mid    |                0.95 |          0.45 |
| setting  | M2       | wall_op10     |                0.65 |          0.25 |
| setting  | M2       | waviness      |                0.05 |          0.05 |
| setting  | M3       | arm_op20      |                4.75 |          2.25 |
| setting  | M3       | depth_op10    |                0.3  |          0.2  |
| setting  | M3       | dome_op20     |                0.2  |          0.05 |
| setting  | M3       | drawin_corner |                1.05 |          0.5  |
| setting  | M3       | drawin_mid    |                1.75 |          0.95 |
| setting  | M3       | wall_op10     |                1.85 |          0.65 |
| setting  | M3       | waviness      |                0.1  |          0.1  |
| setting  | M4       | arm_op20      |                1.3  |          0.3  |
| setting  | M4       | depth_op10    |                0.2  |          0.15 |
| setting  | M4       | dome_op20     |                0.15 |          0.05 |
| setting  | M4       | drawin_corner |                0.35 |          0.2  |
| setting  | M4       | drawin_mid    |                0.55 |          0.3  |
| setting  | M4       | wall_op10     |                0.4  |          0.2  |
| setting  | M4       | waviness      |                0.05 |          0.05 |
| setting  | M5       | arm_op20      |                4    |          0.95 |
| setting  | M5       | depth_op10    |                0.2  |          0.15 |
| setting  | M5       | dome_op20     |                0.15 |          0.05 |
| setting  | M5       | drawin_corner |                0.25 |          0.1  |
| setting  | M5       | drawin_mid    |                1    |          0.35 |
| setting  | M5       | wall_op10     |                0.65 |          0.25 |
| setting  | M5       | waviness      |                0.1  |          0.05 |
| setting  | M5n      | arm_op20      |                0.95 |          0.3  |
| setting  | M5n      | depth_op10    |                0.25 |          0.15 |
| setting  | M5n      | dome_op20     |                0.1  |          0.05 |
| setting  | M5n      | drawin_corner |                0.45 |          0.2  |
| setting  | M5n      | drawin_mid    |                0.55 |          0.25 |
| setting  | M5n      | wall_op10     |                0.25 |          0.1  |
| setting  | M5n      | waviness      |                0.1  |          0.05 |
| setting  | NN       | arm_op20      |                0.6  |          0.6  |
| setting  | NN       | depth_op10    |                0.15 |          0.15 |
| setting  | NN       | dome_op20     |                0.05 |          0.05 |
| setting  | NN       | drawin_corner |                0.25 |          0.25 |
| setting  | NN       | drawin_mid    |                0.35 |          0.35 |
| setting  | NN       | wall_op10     |                0.15 |          0.15 |
| setting  | NN       | waviness      |                0.05 |          0.05 |
| transfer | M0       | arm_op20      |                4    |          4    |
| transfer | M0       | depth_op10    |                1.05 |          1.05 |
| transfer | M0       | dome_op20     |                0.15 |          0.15 |
| transfer | M0       | drawin_corner |                3.45 |          3.45 |
| transfer | M0       | drawin_mid    |                2    |          2    |
| transfer | M0       | wall_op10     |                2.25 |          2.25 |
| transfer | M0       | waviness      |                0.1  |          0.1  |
| transfer | M1       | arm_op20      |                4.1  |          4.1  |
| transfer | M1       | depth_op10    |                0.3  |          0.3  |
| transfer | M1       | dome_op20     |                0.2  |          0.2  |
| transfer | M1       | drawin_corner |                0.75 |          0.75 |
| transfer | M1       | drawin_mid    |                1.2  |          1.2  |
| transfer | M1       | wall_op10     |                1.35 |          1.35 |
| transfer | M1       | waviness      |                0.1  |          0.1  |
| transfer | M1s      | arm_op20      |                4.95 |          4.95 |
| transfer | M1s      | depth_op10    |                0.35 |          0.35 |
| transfer | M1s      | dome_op20     |                0.15 |          0.15 |
| transfer | M1s      | drawin_corner |                3.7  |          3.7  |
| transfer | M1s      | drawin_mid    |                0.75 |          0.75 |
| transfer | M1s      | wall_op10     |                9.75 |          9.75 |
| transfer | M1s      | waviness      |                0.05 |          0.05 |
| transfer | M2       | arm_op20      |                5.3  |          3.4  |
| transfer | M2       | depth_op10    |                0.3  |          0.1  |
| transfer | M2       | dome_op20     |                0.25 |          0.15 |
| transfer | M2       | drawin_corner |                0.35 |          0.15 |
| transfer | M2       | drawin_mid    |                1    |          0.1  |
| transfer | M2       | wall_op10     |                0.8  |          0.05 |
| transfer | M2       | waviness      |                0.15 |          0.05 |
| transfer | M3       | arm_op20      |                5.8  |          4.05 |
| transfer | M3       | depth_op10    |                0.3  |          0.2  |
| transfer | M3       | dome_op20     |                0.3  |          0.1  |
| transfer | M3       | drawin_corner |                0.7  |          0.3  |
| transfer | M3       | drawin_mid    |                0.85 |          0.2  |
| transfer | M3       | wall_op10     |                2.55 |          0.45 |
| transfer | M3       | waviness      |                0.1  |          0.05 |
| transfer | M4       | arm_op20      |                5.35 |          4.45 |
| transfer | M4       | depth_op10    |                0.5  |          0.4  |
| transfer | M4       | dome_op20     |                0.2  |          0.1  |
| transfer | M4       | drawin_corner |                5.25 |          4.95 |
| transfer | M4       | drawin_mid    |                1.1  |          0.85 |
| transfer | M4       | wall_op10     |               10.5  |          9.9  |
| transfer | M4       | waviness      |                0.05 |          0.05 |
| transfer | M5       | arm_op20      |                3.95 |          3.5  |
| transfer | M5       | depth_op10    |                0.2  |          0.15 |
| transfer | M5       | dome_op20     |                0.25 |          0.15 |
| transfer | M5       | drawin_corner |                0.35 |          0.15 |
| transfer | M5       | drawin_mid    |                0.3  |          0.15 |
| transfer | M5       | wall_op10     |                0.6  |          0.25 |
| transfer | M5       | waviness      |                0.05 |          0.05 |
| transfer | M5n      | arm_op20      |                4.9  |          4.45 |
| transfer | M5n      | depth_op10    |                0.45 |          0.4  |
| transfer | M5n      | dome_op20     |                0.15 |          0.1  |
| transfer | M5n      | drawin_corner |                5.2  |          5.05 |
| transfer | M5n      | drawin_mid    |                1.1  |          0.9  |
| transfer | M5n      | wall_op10     |               10.3  |          9.95 |
| transfer | M5n      | waviness      |                0.05 |          0.05 |
| transfer | NN       | arm_op20      |                4.65 |          4.65 |
| transfer | NN       | depth_op10    |                0.45 |          0.45 |
| transfer | NN       | dome_op20     |                0.1  |          0.1  |
| transfer | NN       | drawin_corner |                5.1  |          5.1  |
| transfer | NN       | drawin_mid    |                1.05 |          1.05 |
| transfer | NN       | wall_op10     |               10.15 |         10.15 |
| transfer | NN       | waviness      |                0.05 |          0.05 |
| within   | M0       | arm_op20      |                4    |          4    |
| within   | M0       | depth_op10    |                1.05 |          1.05 |
| within   | M0       | dome_op20     |                0.15 |          0.15 |
| within   | M0       | drawin_corner |                3.45 |          3.45 |
| within   | M0       | drawin_mid    |                2    |          2    |
| within   | M0       | wall_op10     |                2.25 |          2.25 |
| within   | M0       | waviness      |                0.1  |          0.1  |
| within   | M1       | arm_op20      |                0.95 |          0.95 |
| within   | M1       | depth_op10    |                0.25 |          0.25 |
| within   | M1       | dome_op20     |                0.05 |          0.05 |
| within   | M1       | drawin_corner |                0.65 |          0.65 |
| within   | M1       | drawin_mid    |                1.05 |          1.05 |
| within   | M1       | wall_op10     |                0.95 |          0.95 |
| within   | M1       | waviness      |                0.05 |          0.05 |
| within   | M1s      | arm_op20      |                0.45 |          0.45 |
| within   | M1s      | depth_op10    |                0.1  |          0.1  |
| within   | M1s      | dome_op20     |                0.05 |          0.05 |
| within   | M1s      | drawin_corner |                0.15 |          0.15 |
| within   | M1s      | drawin_mid    |                0.15 |          0.15 |
| within   | M1s      | wall_op10     |                0.25 |          0.25 |
| within   | M1s      | waviness      |                0.05 |          0.05 |
| within   | M2       | arm_op20      |                3.2  |          0.05 |
| within   | M2       | depth_op10    |                0.25 |          0    |
| within   | M2       | dome_op20     |                0.15 |          0.05 |
| within   | M2       | drawin_corner |                0.3  |          0    |
| within   | M2       | drawin_mid    |                1.05 |          0    |
| within   | M2       | wall_op10     |                0.75 |          0.05 |
| within   | M2       | waviness      |                0.1  |          0.05 |
| within   | M3       | arm_op20      |                2.95 |          0.05 |
| within   | M3       | depth_op10    |                0.35 |          0    |
| within   | M3       | dome_op20     |                0.15 |          0.05 |
| within   | M3       | drawin_corner |                0.7  |          0    |
| within   | M3       | drawin_mid    |                1.4  |          0    |
| within   | M3       | wall_op10     |                4.15 |          0.05 |
| within   | M3       | waviness      |                0.1  |          0    |
| within   | M4       | arm_op20      |                1.15 |          0.15 |
| within   | M4       | depth_op10    |                0.1  |          0.05 |
| within   | M4       | dome_op20     |                0.15 |          0.05 |
| within   | M4       | drawin_corner |                0.35 |          0.05 |
| within   | M4       | drawin_mid    |                0.25 |          0.05 |
| within   | M4       | wall_op10     |                0.5  |          0    |
| within   | M4       | waviness      |                0.05 |          0.05 |
| within   | M5       | arm_op20      |                0.75 |          0.15 |
| within   | M5       | depth_op10    |                0.1  |          0.05 |
| within   | M5       | dome_op20     |                0.1  |          0.05 |
| within   | M5       | drawin_corner |                0.2  |          0.05 |
| within   | M5       | drawin_mid    |                0.2  |          0.05 |
| within   | M5       | wall_op10     |                0.4  |          0.15 |
| within   | M5       | waviness      |                0.05 |          0    |
| within   | M5n      | arm_op20      |                0.75 |          0.15 |
| within   | M5n      | depth_op10    |                0.1  |          0.05 |
| within   | M5n      | dome_op20     |                0.1  |          0.05 |
| within   | M5n      | drawin_corner |                0.2  |          0.05 |
| within   | M5n      | drawin_mid    |                0.2  |          0.05 |
| within   | M5n      | wall_op10     |                0.3  |          0.1  |
| within   | M5n      | waviness      |                0.05 |          0    |
| within   | NN       | arm_op20      |                0.3  |          0.3  |
| within   | NN       | depth_op10    |                0.05 |          0.05 |
| within   | NN       | dome_op20     |                0.05 |          0.05 |
| within   | NN       | drawin_corner |                0.15 |          0.15 |
| within   | NN       | drawin_mid    |                0.1  |          0.1  |
| within   | NN       | wall_op10     |                0.3  |          0.3  |
| within   | NN       | waviness      |                0.05 |          0.05 |

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
| setting/interpolation | M2       |         0.75 |            17.75 |         2.7  |            0.75  |            0     |            0.25  |            0.958 |            0     |            0.042 |            18.5  |         1.95 |            0.688 |            0     |            0.312 |            0.958 |                0 |            0.042 |
| setting/interpolation | M2n      |         0    |            13.3  |         0    |            0.812 |            0     |            0.188 |            1     |            0     |            0     |            13.3  |         0    |            0.812 |            0     |            0.188 |            1     |                0 |            0     |
| setting/interpolation | M3       |        17.75 |            29.05 |        13.35 |            0.525 |            0.088 |            0.388 |            0.819 |            0     |            0.181 |            46.8  |         0    |            0.062 |            0     |            0.938 |            0.306 |                0 |            0.694 |
| setting/interpolation | M4       |         6    |            14.7  |         7    |            0.75  |            0.012 |            0.238 |            0.986 |            0     |            0.014 |            20.7  |         1    |            0.45  |            0     |            0.55  |            0.944 |                0 |            0.056 |
| setting/interpolation | M5       |         0.5  |            19.05 |         2.8  |            0.612 |            0     |            0.388 |            0.958 |            0     |            0.042 |            19.55 |         2.3  |            0.6   |            0     |            0.4   |            0.958 |                0 |            0.042 |
| setting/interpolation | M5n      |         0    |            15.6  |         0    |            0.75  |            0     |            0.25  |            1     |            0     |            0     |            15.6  |         0    |            0.75  |            0     |            0.25  |            1     |                0 |            0     |
| setting/interpolation | NN       |         2    |             4.65 |         4.65 |            1     |            0     |            0     |            1     |            0     |            0     |             6.65 |         2.65 |            1     |            0     |            0     |            1     |                0 |            0     |
| transfer              | M0       |       inf    |           108.35 |       108.35 |            0.653 |            0.347 |            0     |            0.731 |            0.269 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1       |       inf    |            35.3  |        35.3  |            0.72  |            0.28  |            0     |            0.858 |            0.142 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1n      |       inf    |           130.7  |       130.7  |            0.556 |            0.444 |            0     |            0.598 |            0.402 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M1s      |       inf    |           122.3  |       122.3  |            0.565 |            0.435 |            0     |            0.662 |            0.338 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M2       |       inf    |            50.65 |        15.8  |            0.649 |            0.096 |            0.255 |            0.836 |            0.041 |            0.123 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M2n      |       inf    |           132.35 |       129.05 |            0.473 |            0.36  |            0.167 |            0.521 |            0.306 |            0.174 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M3       |       inf    |            48.75 |        20.5  |            0.594 |            0.113 |            0.293 |            0.767 |            0.055 |            0.178 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M4       |       inf    |           133.1  |       128.45 |            0.523 |            0.377 |            0.1   |            0.589 |            0.329 |            0.082 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M5       |       inf    |            38.4  |        27.5  |            0.774 |            0.184 |            0.042 |            0.881 |            0.082 |            0.037 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | M5n      |       inf    |           132.15 |       129.55 |            0.548 |            0.389 |            0.063 |            0.589 |            0.329 |            0.082 |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| transfer              | NN       |       inf    |           130.5  |       130.5  |            0.556 |            0.444 |            0     |            0.639 |            0.361 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| within                | M0       |       inf    |           108.35 |       108.35 |            0.653 |            0.347 |            0     |            0.731 |            0.269 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| within                | M1       |       inf    |            15.2  |        15.2  |            0.879 |            0.121 |            0     |            0.991 |            0.009 |            0     |           nan    |       nan    |          nan     |          nan     |          nan     |          nan     |              nan |          nan     |
| within                | M1n      |         5.25 |             9.05 |         9.05 |            0.971 |            0.029 |            0     |            1     |            0     |            0     |            14.45 |         3.8  |            0.879 |            0     |            0.121 |            0.991 |                0 |            0.009 |
| within                | M1s      |         2    |             4.85 |         4.85 |            1     |            0     |            0     |            1     |            0     |            0     |             6.85 |         2.85 |            0.992 |            0     |            0.008 |            1     |                0 |            0     |
| within                | M2       |         0    |            22.65 |         0.15 |            0.669 |            0     |            0.331 |            0.922 |            0     |            0.078 |            22.65 |         0.15 |            0.669 |            0     |            0.331 |            0.922 |                0 |            0.078 |
| within                | M2n      |         0    |            18.75 |         0    |            0.766 |            0     |            0.234 |            0.968 |            0     |            0.032 |            18.75 |         0    |            0.766 |            0     |            0.234 |            0.968 |                0 |            0.032 |
| within                | M3       |         0    |            23.05 |         0    |            0.548 |            0     |            0.452 |            0.936 |            0     |            0.064 |            23.05 |         0    |            0.548 |            0     |            0.452 |            0.936 |                0 |            0.064 |
| within                | M4       |         0    |            11.3  |         0.05 |            0.912 |            0     |            0.088 |            1     |            0     |            0     |            11.3  |         0.05 |            0.912 |            0     |            0.088 |            1     |                0 |            0     |
| within                | M5       |         0    |             7.15 |         0.75 |            0.987 |            0     |            0.013 |            1     |            0     |            0     |             7.15 |         0.75 |            0.987 |            0     |            0.013 |            1     |                0 |            0     |
| within                | M5n      |         0    |             7.15 |         0.55 |            0.996 |            0     |            0.004 |            1     |            0     |            0     |             7.15 |         0.55 |            0.996 |            0     |            0.004 |            1     |                0 |            0     |
| within                | NN       |         0.25 |             3.35 |         3.35 |            1     |            0     |            0     |            1     |            0     |            0     |             3.6  |         3.1  |            1     |            0     |            0     |            1     |                0 |            0     |

## capability

|   ppk | scope    | method   |   median_d |   right |   false_reject |   trial |   adequate |
|------:|:---------|:---------|-----------:|--------:|---------------:|--------:|-----------:|
|  1    | setting  | M0       |      1.032 |   0.429 |          0.571 |   0     |          1 |
|  1    | setting  | M1       |      1.032 |   0.508 |          0.492 |   0     |          1 |
|  1    | setting  | M1n      |      1.032 |   0.556 |          0.444 |   0     |          1 |
|  1    | setting  | M1s      |      1.032 |   0.73  |          0.27  |   0     |          1 |
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
| nominal + offset |      18 |                1.95 |          1.95 |              0.326 |           1.754 |
| M0               |      18 |               27.5  |         27.5  |             13.977 |          27.075 |
| M1               |      18 |               16.35 |         16.35 |              5.336 |          15.942 |
| M1s              |      18 |              123.2  |        123.2  |            121.147 |         122.969 |
| Mc               |      18 |               18.9  |         18.9  |             15.257 |          18.29  |
| M2               |      18 |                9.95 |          0.05 |              1.015 |           4.487 |
| M5               |      18 |                7.3  |          3.15 |              3.601 |           4.592 |
| M1n              |      18 |              129.1  |        129.1  |            126.024 |         129.041 |
| NN               |      18 |              129.95 |        129.95 |            125.907 |         129.762 |

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

| qc            | geometry   |   floor |   sigma_lt |   sigma_st |   sigma_within_batch |   sigma_between_batch |   floor_over_sigma_lt |   floor_over_sigma_st |   normal_model_floor |
|:--------------|:-----------|--------:|-----------:|-----------:|---------------------:|----------------------:|----------------------:|----------------------:|---------------------:|
| drawin_mid    | concave    |   0.05  |      0.041 |      0.038 |                0.045 |                 0.016 |                 1.211 |                 1.303 |                0.048 |
| drawin_mid    | convex     |   0.052 |      0.034 |      0.027 |                0.034 |                 0.018 |                 1.526 |                 1.937 |                0.051 |
| drawin_corner | concave    |   0.053 |      0.031 |      0.023 |                0.034 |                 0.016 |                 1.691 |                 2.266 |                0.047 |
| drawin_corner | convex     |   0.03  |      0.023 |      0.02  |                0.023 |                 0.01  |                 1.311 |                 1.472 |                0.03  |
| waviness      | concave    |   0.004 |      0.002 |      0.001 |                0.002 |                 0.001 |                 2.148 |                 3.072 |                0.003 |
| waviness      | convex     |   0.002 |      0.003 |      0.003 |                0.003 |                 0.001 |                 0.794 |                 0.799 |                0.002 |
| wall_op10     | concave    |   0.081 |      0.05  |      0.046 |                0.055 |                 0.025 |                 1.596 |                 1.75  |                0.074 |
| wall_op10     | convex     |   0.078 |      0.117 |      0.115 |                0.108 |                 0.02  |                 0.662 |                 0.676 |                0.07  |
| arm_op20      | concave    |   0.116 |      0.061 |      0.048 |                0.054 |                 0.042 |                 1.89  |                 2.436 |                0.118 |
| arm_op20      | convex     |   0.1   |      0.107 |      0.093 |                0.122 |                 0.031 |                 0.934 |                 1.069 |                0.098 |
| depth_op10    | concave    |   0.009 |      0.004 |      0.003 |                0.006 |                 0.003 |                 2.223 |                 3.021 |                0.008 |
| depth_op10    | convex     |   0.012 |      0.007 |      0.005 |                0.006 |                 0.004 |                 1.672 |                 2.424 |                0.012 |
| dome_op20     | concave    |   0.003 |      0.002 |      0.002 |                0.003 |                 0.001 |                 1.439 |                 1.857 |                0.003 |
| dome_op20     | convex     |   0.008 |      0.005 |      0.004 |                0.004 |                 0.003 |                 1.537 |                 1.966 |                0.008 |

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

## sibling strata: cases

|   resolved_siblings |   cases |
|--------------------:|--------:|
|                   0 |      58 |
|                   1 |      34 |
|                   2 |      34 |
