# Design-stage decisions scored against production

Adequate: at least 95% of the parts conform. Conformal coverage 90%. Nominal simulation: t = 0.98 mm, friction 0.1. Requirements at d = -500 to 500 production floors from the true q95.

## Offset between parts and matched simulations (median over alternatives)

| qc            |   concave |   convex |
|:--------------|----------:|---------:|
| arm_op20      |    -3.486 |    0.041 |
| depth_op10    |    -0.953 |   -0.897 |
| dome_op20     |    -0.038 |    0.063 |
| drawin_corner |    -2.959 |   -3.32  |
| drawin_mid    |    -1.424 |   -1.758 |
| wall_op10     |     1.252 |    0.626 |
| waviness      |     0.032 |   -0.007 |

## Decision rates over all characteristics

| scope    | method   |   correct |   false_accept |   false_reject |   abstain |   error_when_decided |
|:---------|:---------|----------:|---------------:|---------------:|----------:|---------------------:|
| pooled   | M0       |     0.702 |          0.079 |          0.22  |     0     |                0.298 |
| pooled   | M1       |     0.779 |          0.099 |          0.122 |     0     |                0.221 |
| pooled   | M2       |     0.505 |          0     |          0.001 |     0.494 |                0.002 |
| pooled   | M3       |     0.531 |          0     |          0.005 |     0.464 |                0.009 |
| pooled   | M4       |     0.709 |          0.001 |          0.003 |     0.287 |                0.005 |
| pooled   | M5       |     0.859 |          0.003 |          0.007 |     0.131 |                0.011 |
| transfer | M0       |     0.702 |          0.079 |          0.22  |     0     |                0.298 |
| transfer | M1       |     0.744 |          0.12  |          0.136 |     0     |                0.256 |
| transfer | M2       |     0.644 |          0.045 |          0.061 |     0.25  |                0.141 |
| transfer | M3       |     0.661 |          0.052 |          0.075 |     0.211 |                0.162 |
| transfer | M4       |     0.63  |          0.149 |          0.149 |     0.072 |                0.321 |
| transfer | M5       |     0.766 |          0.094 |          0.112 |     0.027 |                0.212 |
| within   | M0       |     0.702 |          0.079 |          0.22  |     0     |                0.298 |
| within   | M1       |     0.84  |          0.081 |          0.078 |     0     |                0.16  |
| within   | M2       |     0.618 |          0.001 |          0.002 |     0.379 |                0.005 |
| within   | M3       |     0.571 |          0.001 |          0.003 |     0.425 |                0.007 |
| within   | M4       |     0.783 |          0.002 |          0.005 |     0.21  |                0.009 |
| within   | M5       |     0.881 |          0.006 |          0.01  |     0.103 |                0.018 |

## Distances over all characteristics with bootstrap intervals over design cases (1000 resamples)

| scope    | method   | decisive (95 % CI)   | safe (95 % CI)   |
|:---------|:---------|:---------------------|:-----------------|
| pooled   | M0       | 150 (100-150)        | 150 (100-150)    |
| pooled   | M1       | 30 (25-40)           | 30 (25-40)       |
| pooled   | M2       | 50 (40-75)           | 0 (0-0)          |
| pooled   | M3       | 25 (25-30)           | 0 (0-0.5)        |
| pooled   | M4       | 25 (15-30)           | 0.5 (0-1.5)      |
| pooled   | M5       | 12 (9.975-15)        | 1 (0.5-2.5)      |
| transfer | M0       | 150 (100-150)        | 150 (100-150)    |
| transfer | M1       | 40 (40-40)           | 40 (40-40)       |
| transfer | M2       | 75 (75-75)           | 20 (12-25)       |
| transfer | M3       | 50 (50-50)           | 20 (20-25)       |
| transfer | M4       | 150 (150-200)        | 150 (150-200)    |
| transfer | M5       | 40 (40-40)           | 30 (25-40)       |
| within   | M0       | 150 (100-150)        | 150 (100-150)    |
| within   | M1       | 15 (12-20)           | 15 (12-20)       |
| within   | M2       | 25 (25-30)           | 0.5 (0-1)        |
| within   | M3       | 20 (20-25)           | 0 (0-0.5)        |
| within   | M4       | 12 (10-12)           | 1 (0-2)          |
| within   | M5       | 7 (6.5-8)            | 2 (0.5-4.5)      |

## Decisive distance (production floors): beyond it at least 95 % of verdicts are correct

| qc            |   ('pooled', 'M0') |   ('pooled', 'M1') |   ('pooled', 'M2') |   ('pooled', 'M3') |   ('pooled', 'M4') |   ('pooled', 'M5') |   ('transfer', 'M0') |   ('transfer', 'M1') |   ('transfer', 'M2') |   ('transfer', 'M3') |   ('transfer', 'M4') |   ('transfer', 'M5') |   ('within', 'M0') |   ('within', 'M1') |   ('within', 'M2') |   ('within', 'M3') |   ('within', 'M4') |   ('within', 'M5') |
|:--------------|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|---------------------:|---------------------:|---------------------:|---------------------:|---------------------:|---------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|
| all           |                150 |                 30 |               50   |               25   |               25   |               12   |                  150 |                   40 |                 75   |                 50   |                  150 |                 40   |                150 |                 15 |               25   |                 20 |               12   |                7   |
| arm_op20      |                 40 |                 40 |               75   |               25   |               12   |                5.5 |                   40 |                   40 |                 75   |                 50   |                   50 |                 40   |                 40 |                 40 |               75   |                 20 |                9   |                6.5 |
| depth_op10    |                150 |                 25 |               30   |               30   |               12   |                4   |                  150 |                   25 |                 30   |                 40   |                   75 |                 20   |                150 |                 20 |               30   |                 20 |               12   |                5   |
| dome_op20     |                 40 |                 50 |               75   |               40   |               40   |               15   |                   40 |                   75 |                 75   |                 75   |                   75 |                 75   |                 40 |                 12 |               15   |                 30 |               20   |               15   |
| drawin_corner |                150 |                 15 |                9.5 |                6   |                8.5 |                3.5 |                  150 |                   15 |                  9.5 |                 25   |                  200 |                  7   |                150 |                 15 |                6.5 |                 15 |               10   |                2.5 |
| drawin_mid    |                 30 |                 15 |               15   |                8.5 |                7.5 |                3   |                   30 |                   12 |                 12   |                  6.5 |                   20 |                  3.5 |                 30 |                 15 |               15   |                 15 |                7.5 |                4.5 |
| wall_op10     |                 30 |                 20 |               20   |               25   |                5.5 |                2.5 |                   30 |                   25 |                 20   |                 50   |                  150 |                 12   |                 30 |                 15 |               12   |                 30 |                4.5 |                2.5 |
| waviness      |                 20 |                 15 |               40   |               20   |                4   |                2   |                   20 |                   20 |                 75   |                 50   |                   15 |                 25   |                 20 |                  8 |               25   |                 20 |                4   |                1.5 |

## Safe distance (production floors): beyond it at most 5 % of verdicts are wrong

| qc            |   ('pooled', 'M0') |   ('pooled', 'M1') |   ('pooled', 'M2') |   ('pooled', 'M3') |   ('pooled', 'M4') |   ('pooled', 'M5') |   ('transfer', 'M0') |   ('transfer', 'M1') |   ('transfer', 'M2') |   ('transfer', 'M3') |   ('transfer', 'M4') |   ('transfer', 'M5') |   ('within', 'M0') |   ('within', 'M1') |   ('within', 'M2') |   ('within', 'M3') |   ('within', 'M4') |   ('within', 'M5') |
|:--------------|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|---------------------:|---------------------:|---------------------:|---------------------:|---------------------:|---------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|
| all           |                150 |                 30 |                0   |                0   |                0.5 |                1   |                  150 |                   40 |                 20   |                 20   |                  150 |                   30 |                150 |                 15 |                0.5 |                0   |                1   |                2   |
| arm_op20      |                 40 |                 40 |                0.5 |                0.5 |                2   |                2   |                   40 |                   40 |                 30   |                 40   |                   50 |                   40 |                 40 |                 40 |                0.5 |                0.5 |                1.5 |                2.5 |
| depth_op10    |                150 |                 25 |                0   |                0   |                0.5 |                0.5 |                  150 |                   25 |                  8.5 |                 20   |                   50 |                   20 |                150 |                 20 |                0   |                0   |                1   |                3.5 |
| dome_op20     |                 40 |                 50 |                0   |                1.5 |                0.5 |                5   |                   40 |                   75 |                 25   |                 25   |                    9 |                   40 |                 40 |                 12 |                1   |                0.5 |                4   |                9.5 |
| drawin_corner |                150 |                 15 |                0   |                0.5 |                0.5 |                1.5 |                  150 |                   15 |                  2.5 |                  7.5 |                  200 |                    6 |                150 |                 15 |                0   |                0   |                0   |                0.5 |
| drawin_mid    |                 30 |                 15 |                0.5 |                0.5 |                0.5 |                0.5 |                   30 |                   12 |                  0.5 |                  2.5 |                   12 |                    1 |                 30 |                 15 |                0.5 |                0.5 |                2   |                1   |
| wall_op10     |                 30 |                 20 |                0   |                0.5 |                0.5 |                1   |                   30 |                   25 |                  7   |                  8.5 |                  150 |                   12 |                 30 |                 15 |                0.5 |                0   |                1.5 |                0.5 |
| waviness      |                 20 |                 15 |                0   |                0   |                0.5 |                0.5 |                   20 |                   20 |                 12   |                 20   |                    9 |                   20 |                 20 |                  8 |                0.5 |                0.5 |                0.5 |                0.5 |

## Decision rates per characteristic

| calibration     | qc            | method   |   correct |   false_accept |   false_reject |   abstain |   error_when_decided |
|:----------------|:--------------|:---------|----------:|---------------:|---------------:|----------:|---------------------:|
| concave->convex | arm_op20      | M0       |     0.909 |          0.04  |          0.051 |     0     |                0.091 |
| concave->convex | arm_op20      | M1       |     0.629 |          0.371 |          0     |     0     |                0.371 |
| concave->convex | arm_op20      | M2       |     0.597 |          0.154 |          0     |     0.249 |                0.205 |
| concave->convex | arm_op20      | M3       |     0.614 |          0.214 |          0     |     0.172 |                0.259 |
| concave->convex | arm_op20      | M4       |     0.615 |          0.383 |          0     |     0.002 |                0.384 |
| concave->convex | arm_op20      | M5       |     0.657 |          0.317 |          0     |     0.027 |                0.325 |
| concave->convex | depth_op10    | M0       |     0.577 |          0     |          0.423 |     0     |                0.423 |
| concave->convex | depth_op10    | M1       |     0.778 |          0.149 |          0.073 |     0     |                0.222 |
| concave->convex | depth_op10    | M2       |     0.511 |          0     |          0     |     0.489 |                0     |
| concave->convex | depth_op10    | M3       |     0.624 |          0.048 |          0.045 |     0.284 |                0.13  |
| concave->convex | depth_op10    | M4       |     0.627 |          0.357 |          0     |     0.017 |                0.363 |
| concave->convex | depth_op10    | M5       |     0.796 |          0.022 |          0.182 |     0     |                0.204 |
| concave->convex | dome_op20     | M0       |     0.771 |          0.229 |          0     |     0     |                0.229 |
| concave->convex | dome_op20     | M1       |     0.663 |          0.337 |          0     |     0     |                0.337 |
| concave->convex | dome_op20     | M2       |     0.673 |          0.267 |          0     |     0.06  |                0.284 |
| concave->convex | dome_op20     | M3       |     0.667 |          0.149 |          0     |     0.184 |                0.183 |
| concave->convex | dome_op20     | M4       |     0.723 |          0.159 |          0     |     0.118 |                0.18  |
| concave->convex | dome_op20     | M5       |     0.675 |          0.294 |          0     |     0.032 |                0.303 |
| concave->convex | drawin_corner | M0       |     0.557 |          0     |          0.443 |     0     |                0.443 |
| concave->convex | drawin_corner | M1       |     0.776 |          0.075 |          0.149 |     0     |                0.224 |
| concave->convex | drawin_corner | M2       |     0.741 |          0     |          0.022 |     0.237 |                0.028 |
| concave->convex | drawin_corner | M3       |     0.604 |          0     |          0.061 |     0.335 |                0.092 |
| concave->convex | drawin_corner | M4       |     0.552 |          0.448 |          0     |     0     |                0.448 |
| concave->convex | drawin_corner | M5       |     0.861 |          0     |          0.108 |     0.032 |                0.111 |
| concave->convex | drawin_mid    | M0       |     0.673 |          0     |          0.327 |     0     |                0.327 |
| concave->convex | drawin_mid    | M1       |     0.824 |          0.051 |          0.124 |     0     |                0.176 |
| concave->convex | drawin_mid    | M2       |     0.624 |          0     |          0     |     0.376 |                0     |
| concave->convex | drawin_mid    | M3       |     0.778 |          0     |          0     |     0.222 |                0     |
| concave->convex | drawin_mid    | M4       |     0.685 |          0.234 |          0     |     0.081 |                0.255 |
| concave->convex | drawin_mid    | M5       |     0.894 |          0     |          0     |     0.106 |                0     |
| concave->convex | wall_op10     | M0       |     0.826 |          0.174 |          0     |     0     |                0.174 |
| concave->convex | wall_op10     | M1       |     0.716 |          0     |          0.284 |     0     |                0.284 |
| concave->convex | wall_op10     | M2       |     0.687 |          0     |          0.1   |     0.214 |                0.127 |
| concave->convex | wall_op10     | M3       |     0.512 |          0     |          0.058 |     0.43  |                0.102 |
| concave->convex | wall_op10     | M4       |     0.552 |          0     |          0.448 |     0     |                0.448 |
| concave->convex | wall_op10     | M5       |     0.76  |          0     |          0.224 |     0.017 |                0.228 |
| concave->convex | waviness      | M0       |     0.869 |          0.109 |          0.022 |     0     |                0.131 |
| concave->convex | waviness      | M1       |     0.703 |          0     |          0.297 |     0     |                0.297 |
| concave->convex | waviness      | M2       |     0.567 |          0     |          0.111 |     0.322 |                0.164 |
| concave->convex | waviness      | M3       |     0.572 |          0     |          0.161 |     0.267 |                0.219 |
| concave->convex | waviness      | M4       |     0.794 |          0.02  |          0.103 |     0.083 |                0.134 |
| concave->convex | waviness      | M5       |     0.658 |          0     |          0.337 |     0.005 |                0.338 |
| convex->concave | arm_op20      | M0       |     0.735 |          0.01  |          0.255 |     0     |                0.265 |
| convex->concave | arm_op20      | M1       |     0.733 |          0.007 |          0.26  |     0     |                0.267 |
| convex->concave | arm_op20      | M2       |     0.637 |          0     |          0.275 |     0.088 |                0.302 |
| convex->concave | arm_op20      | M3       |     0.604 |          0     |          0.249 |     0.148 |                0.292 |
| convex->concave | arm_op20      | M4       |     0.602 |          0     |          0.383 |     0.015 |                0.389 |
| convex->concave | arm_op20      | M5       |     0.657 |          0     |          0.315 |     0.028 |                0.324 |
| convex->concave | depth_op10    | M0       |     0.552 |          0     |          0.448 |     0     |                0.448 |
| convex->concave | depth_op10    | M1       |     0.824 |          0     |          0.176 |     0     |                0.176 |
| convex->concave | depth_op10    | M2       |     0.546 |          0.065 |          0     |     0.39  |                0.106 |
| convex->concave | depth_op10    | M3       |     0.637 |          0.071 |          0.201 |     0.091 |                0.299 |
| convex->concave | depth_op10    | M4       |     0.592 |          0     |          0.393 |     0.015 |                0.399 |
| convex->concave | depth_op10    | M5       |     0.765 |          0.199 |          0.035 |     0.002 |                0.234 |
| convex->concave | dome_op20     | M0       |     0.633 |          0     |          0.367 |     0     |                0.367 |
| convex->concave | dome_op20     | M1       |     0.597 |          0     |          0.403 |     0     |                0.403 |
| convex->concave | dome_op20     | M2       |     0.584 |          0     |          0.34  |     0.076 |                0.368 |
| convex->concave | dome_op20     | M3       |     0.527 |          0     |          0.254 |     0.219 |                0.325 |
| convex->concave | dome_op20     | M4       |     0.425 |          0     |          0.013 |     0.562 |                0.03  |
| convex->concave | dome_op20     | M5       |     0.594 |          0     |          0.362 |     0.045 |                0.378 |
| convex->concave | drawin_corner | M0       |     0.587 |          0     |          0.413 |     0     |                0.413 |
| convex->concave | drawin_corner | M1       |     0.842 |          0.124 |          0.033 |     0     |                0.158 |
| convex->concave | drawin_corner | M2       |     0.864 |          0.013 |          0     |     0.123 |                0.015 |
| convex->concave | drawin_corner | M3       |     0.824 |          0.036 |          0     |     0.139 |                0.042 |
| convex->concave | drawin_corner | M4       |     0.566 |          0     |          0.433 |     0.002 |                0.434 |
| convex->concave | drawin_corner | M5       |     0.94  |          0.058 |          0     |     0.002 |                0.058 |
| convex->concave | drawin_mid    | M0       |     0.673 |          0     |          0.327 |     0     |                0.327 |
| convex->concave | drawin_mid    | M1       |     0.776 |          0.121 |          0.103 |     0     |                0.224 |
| convex->concave | drawin_mid    | M2       |     0.655 |          0     |          0.008 |     0.337 |                0.012 |
| convex->concave | drawin_mid    | M3       |     0.852 |          0.023 |          0     |     0.124 |                0.027 |
| convex->concave | drawin_mid    | M4       |     0.658 |          0     |          0.29  |     0.051 |                0.306 |
| convex->concave | drawin_mid    | M5       |     0.949 |          0.003 |          0.007 |     0.041 |                0.01  |
| convex->concave | wall_op10     | M0       |     0.673 |          0.327 |          0     |     0     |                0.327 |
| convex->concave | wall_op10     | M1       |     0.731 |          0.269 |          0     |     0     |                0.269 |
| convex->concave | wall_op10     | M2       |     0.685 |          0.028 |          0     |     0.287 |                0.04  |
| convex->concave | wall_op10     | M3       |     0.779 |          0.096 |          0.022 |     0.103 |                0.131 |
| convex->concave | wall_op10     | M4       |     0.567 |          0.433 |          0     |     0     |                0.433 |
| convex->concave | wall_op10     | M5       |     0.791 |          0.176 |          0     |     0.033 |                0.182 |
| convex->concave | waviness      | M0       |     0.788 |          0.212 |          0     |     0     |                0.212 |
| convex->concave | waviness      | M1       |     0.818 |          0.181 |          0.002 |     0     |                0.182 |
| convex->concave | waviness      | M2       |     0.652 |          0.101 |          0     |     0.247 |                0.134 |
| convex->concave | waviness      | M3       |     0.662 |          0.096 |          0     |     0.242 |                0.127 |
| convex->concave | waviness      | M4       |     0.866 |          0.058 |          0.02  |     0.056 |                0.083 |
| convex->concave | waviness      | M5       |     0.733 |          0.254 |          0     |     0.013 |                0.257 |
| pooled          | arm_op20      | M0       |     0.822 |          0.025 |          0.153 |     0     |                0.178 |
| pooled          | arm_op20      | M1       |     0.788 |          0.064 |          0.148 |     0     |                0.212 |
| pooled          | arm_op20      | M2       |     0.353 |          0     |          0.001 |     0.646 |                0.002 |
| pooled          | arm_op20      | M3       |     0.386 |          0     |          0.01  |     0.604 |                0.025 |
| pooled          | arm_op20      | M4       |     0.632 |          0.002 |          0.004 |     0.362 |                0.01  |
| pooled          | arm_op20      | M5       |     0.829 |          0.002 |          0.008 |     0.16  |                0.013 |
| pooled          | depth_op10    | M0       |     0.565 |          0     |          0.435 |     0     |                0.435 |
| pooled          | depth_op10    | M1       |     0.818 |          0.083 |          0.099 |     0     |                0.182 |
| pooled          | depth_op10    | M2       |     0.473 |          0     |          0     |     0.527 |                0     |
| pooled          | depth_op10    | M3       |     0.371 |          0     |          0     |     0.629 |                0     |
| pooled          | depth_op10    | M4       |     0.714 |          0     |          0.001 |     0.285 |                0.001 |
| pooled          | depth_op10    | M5       |     0.891 |          0     |          0.004 |     0.105 |                0.005 |
| pooled          | dome_op20     | M0       |     0.702 |          0.114 |          0.183 |     0     |                0.298 |
| pooled          | dome_op20     | M1       |     0.644 |          0.162 |          0.194 |     0     |                0.356 |
| pooled          | dome_op20     | M2       |     0.352 |          0.002 |          0     |     0.647 |                0.005 |
| pooled          | dome_op20     | M3       |     0.468 |          0.002 |          0.006 |     0.524 |                0.016 |
| pooled          | dome_op20     | M4       |     0.417 |          0     |          0.008 |     0.575 |                0.019 |
| pooled          | dome_op20     | M5       |     0.572 |          0.012 |          0.022 |     0.395 |                0.055 |
| pooled          | drawin_corner | M0       |     0.572 |          0     |          0.428 |     0     |                0.428 |
| pooled          | drawin_corner | M1       |     0.801 |          0.109 |          0.09  |     0     |                0.199 |
| pooled          | drawin_corner | M2       |     0.71  |          0     |          0     |     0.29  |                0     |
| pooled          | drawin_corner | M3       |     0.823 |          0     |          0.001 |     0.176 |                0.001 |
| pooled          | drawin_corner | M4       |     0.765 |          0.003 |          0.001 |     0.231 |                0.005 |
| pooled          | drawin_corner | M5       |     0.92  |          0.003 |          0.007 |     0.07  |                0.012 |
| pooled          | drawin_mid    | M0       |     0.673 |          0     |          0.327 |     0     |                0.327 |
| pooled          | drawin_mid    | M1       |     0.793 |          0.09  |          0.118 |     0     |                0.207 |
| pooled          | drawin_mid    | M2       |     0.592 |          0     |          0.004 |     0.404 |                0.007 |
| pooled          | drawin_mid    | M3       |     0.762 |          0     |          0.002 |     0.236 |                0.002 |
| pooled          | drawin_mid    | M4       |     0.759 |          0     |          0.003 |     0.238 |                0.004 |
| pooled          | drawin_mid    | M5       |     0.908 |          0     |          0.005 |     0.087 |                0.005 |
| pooled          | wall_op10     | M0       |     0.75  |          0.25  |          0     |     0     |                0.25  |
| pooled          | wall_op10     | M1       |     0.813 |          0.083 |          0.104 |     0     |                0.187 |
| pooled          | wall_op10     | M2       |     0.566 |          0     |          0     |     0.434 |                0     |
| pooled          | wall_op10     | M3       |     0.372 |          0     |          0.015 |     0.613 |                0.039 |
| pooled          | wall_op10     | M4       |     0.805 |          0     |          0.002 |     0.192 |                0.003 |
| pooled          | wall_op10     | M5       |     0.942 |          0.001 |          0.004 |     0.053 |                0.005 |
| pooled          | waviness      | M0       |     0.828 |          0.161 |          0.011 |     0     |                0.172 |
| pooled          | waviness      | M1       |     0.794 |          0.105 |          0.101 |     0     |                0.206 |
| pooled          | waviness      | M2       |     0.489 |          0     |          0     |     0.511 |                0     |
| pooled          | waviness      | M3       |     0.536 |          0     |          0     |     0.464 |                0     |
| pooled          | waviness      | M4       |     0.871 |          0     |          0.001 |     0.129 |                0.001 |
| pooled          | waviness      | M5       |     0.954 |          0     |          0.001 |     0.045 |                0.001 |
| within          | arm_op20      | M0       |     0.822 |          0.025 |          0.153 |     0     |                0.178 |
| within          | arm_op20      | M1       |     0.852 |          0.08  |          0.068 |     0     |                0.148 |
| within          | arm_op20      | M2       |     0.559 |          0     |          0.001 |     0.44  |                0.001 |
| within          | arm_op20      | M3       |     0.48  |          0     |          0.001 |     0.519 |                0.002 |
| within          | arm_op20      | M4       |     0.774 |          0.001 |          0.009 |     0.216 |                0.013 |
| within          | arm_op20      | M5       |     0.858 |          0.004 |          0.012 |     0.125 |                0.019 |
| within          | depth_op10    | M0       |     0.565 |          0     |          0.435 |     0     |                0.435 |
| within          | depth_op10    | M1       |     0.818 |          0.075 |          0.108 |     0     |                0.182 |
| within          | depth_op10    | M2       |     0.515 |          0.002 |          0     |     0.483 |                0.003 |
| within          | depth_op10    | M3       |     0.544 |          0.006 |          0     |     0.45  |                0.011 |
| within          | depth_op10    | M4       |     0.74  |          0.001 |          0.007 |     0.253 |                0.01  |
| within          | depth_op10    | M5       |     0.871 |          0.005 |          0.016 |     0.109 |                0.023 |
| within          | dome_op20     | M0       |     0.702 |          0.114 |          0.183 |     0     |                0.298 |
| within          | dome_op20     | M1       |     0.844 |          0.084 |          0.072 |     0     |                0.156 |
| within          | dome_op20     | M2       |     0.6   |          0.001 |          0.003 |     0.396 |                0.007 |
| within          | dome_op20     | M3       |     0.474 |          0     |          0.012 |     0.514 |                0.024 |
| within          | dome_op20     | M4       |     0.588 |          0.011 |          0.007 |     0.394 |                0.03  |
| within          | dome_op20     | M5       |     0.685 |          0.03  |          0.027 |     0.258 |                0.077 |
| within          | drawin_corner | M0       |     0.572 |          0     |          0.428 |     0     |                0.428 |
| within          | drawin_corner | M1       |     0.825 |          0.104 |          0.071 |     0     |                0.175 |
| within          | drawin_corner | M2       |     0.821 |          0.003 |          0     |     0.176 |                0.004 |
| within          | drawin_corner | M3       |     0.682 |          0.002 |          0     |     0.315 |                0.004 |
| within          | drawin_corner | M4       |     0.787 |          0.003 |          0     |     0.21  |                0.004 |
| within          | drawin_corner | M5       |     0.937 |          0.003 |          0.002 |     0.058 |                0.005 |
| within          | drawin_mid    | M0       |     0.673 |          0     |          0.327 |     0     |                0.327 |
| within          | drawin_mid    | M1       |     0.812 |          0.079 |          0.109 |     0     |                0.188 |
| within          | drawin_mid    | M2       |     0.639 |          0     |          0.006 |     0.355 |                0.009 |
| within          | drawin_mid    | M3       |     0.741 |          0     |          0.002 |     0.256 |                0.003 |
| within          | drawin_mid    | M4       |     0.803 |          0     |          0.007 |     0.191 |                0.008 |
| within          | drawin_mid    | M5       |     0.911 |          0.001 |          0.005 |     0.083 |                0.006 |
| within          | wall_op10     | M0       |     0.75  |          0.25  |          0     |     0     |                0.25  |
| within          | wall_op10     | M1       |     0.857 |          0.089 |          0.055 |     0     |                0.143 |
| within          | wall_op10     | M2       |     0.711 |          0     |          0.003 |     0.285 |                0.005 |
| within          | wall_op10     | M3       |     0.536 |          0     |          0     |     0.464 |                0     |
| within          | wall_op10     | M4       |     0.87  |          0.002 |          0.003 |     0.125 |                0.006 |
| within          | wall_op10     | M5       |     0.944 |          0     |          0.004 |     0.051 |                0.004 |
| within          | waviness      | M0       |     0.828 |          0.161 |          0.011 |     0     |                0.172 |
| within          | waviness      | M1       |     0.874 |          0.061 |          0.066 |     0     |                0.126 |
| within          | waviness      | M2       |     0.483 |          0     |          0.002 |     0.515 |                0.003 |
| within          | waviness      | M3       |     0.536 |          0     |          0.006 |     0.458 |                0.011 |
| within          | waviness      | M4       |     0.919 |          0     |          0.001 |     0.08  |                0.001 |
| within          | waviness      | M5       |     0.96  |          0     |          0.002 |     0.038 |                0.002 |
