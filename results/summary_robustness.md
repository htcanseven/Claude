# Robustness

## Floors and effect-to-scatter shares, reference against temperature-adjusted

| variant              | qc            |   floor |   floor_concave |   floor_convex |   share_bhf |   share_geometry |   share_lubrication |   mrc_bhf_kN |
|:---------------------|:--------------|--------:|----------------:|---------------:|------------:|-----------------:|--------------------:|-------------:|
| reference            | drawin_mid    |  0.085  |          0.0788 |         0.0938 |      0.8889 |                1 |              0.3889 |      90.1277 |
| reference            | drawin_corner |  0.0464 |          0.0527 |         0.0299 |      1      |                1 |              0.3889 |      54.825  |
| reference            | waviness      |  0.0028 |          0.0037 |         0.0021 |      0.8333 |                1 |              0.1667 |      32.6025 |
| reference            | wall_op10     |  0.0814 |          0.0885 |         0.0752 |      0.3889 |                1 |              0.5    |     345.653  |
| reference            | arm_op20      |  0.1085 |          0.116  |         0.0999 |      0.9444 |                1 |              0.5    |     100.923  |
| reference            | depth_op10    |  0.0109 |          0.0087 |         0.0123 |      1      |                1 |              0.3889 |      27.8867 |
| reference            | dome_op20     |  0.007  |          0.0034 |         0.0082 |      0.8333 |                1 |              0.6111 |     623.121  |
| temperature-adjusted | drawin_mid    |  0.0841 |          0.0789 |         0.0935 |      0.8889 |                1 |              0.3889 |      89.2297 |
| temperature-adjusted | drawin_corner |  0.0457 |          0.0531 |         0.0298 |      1      |                1 |              0.3889 |      54.041  |
| temperature-adjusted | waviness      |  0.0026 |          0.0037 |         0.0021 |      0.8333 |                1 |              0.2222 |      30.1617 |
| temperature-adjusted | wall_op10     |  0.0794 |          0.0877 |         0.0745 |      0.3889 |                1 |              0.5    |     337.31   |
| temperature-adjusted | arm_op20      |  0.1076 |          0.116  |         0.0995 |      0.9444 |                1 |              0.5    |     100.063  |
| temperature-adjusted | depth_op10    |  0.0094 |          0.0079 |         0.0111 |      1      |                1 |              0.4444 |      24.0591 |
| temperature-adjusted | dome_op20     |  0.0066 |          0.0041 |         0.0076 |      0.8889 |                1 |              0.6667 |     588.806  |

## Blank-holder force pairs: 100->300 kN (stroke speed changes) against 300->500 kN (same speed)

| qc            | pair     |   share_resolvable |   median_esr |   slope_per_100kN |   mrc_kN |
|:--------------|:---------|-------------------:|-------------:|------------------:|---------:|
| arm_op20      | 100->300 |              1     |        3.006 |            -0.225 |   48.214 |
| arm_op20      | 100->500 |              1     |        4.128 |            -0.108 |  100.923 |
| arm_op20      | 300->500 |              0.833 |        2.41  |             0.01  | 1082.55  |
| depth_op10    | 100->300 |              1     |       10.156 |            -0.053 |   20.706 |
| depth_op10    | 100->500 |              1     |       14.546 |            -0.039 |   27.887 |
| depth_op10    | 300->500 |              1     |        4.168 |            -0.025 |   42.693 |
| dome_op20     | 100->300 |              0.833 |        2.183 |            -0.001 |  542.744 |
| dome_op20     | 100->500 |              0.833 |        2.61  |            -0.001 |  623.121 |
| dome_op20     | 300->500 |              0.833 |        2.964 |            -0.001 |  731.442 |
| drawin_corner | 100->300 |              1     |        2.952 |            -0.07  |   66.59  |
| drawin_corner | 100->500 |              1     |        6.999 |            -0.085 |   54.825 |
| drawin_corner | 300->500 |              1     |        4.267 |            -0.1   |   46.593 |
| drawin_mid    | 100->300 |              0.833 |        3.241 |            -0.113 |   75.435 |
| drawin_mid    | 100->500 |              1     |        4.65  |            -0.094 |   90.128 |
| drawin_mid    | 300->500 |              0.833 |        1.907 |            -0.076 |  111.928 |
| wall_op10     | 100->300 |              0.333 |        0.75  |            -0.032 |  253.38  |
| wall_op10     | 100->500 |              0.5   |        1.014 |            -0.024 |  345.653 |
| wall_op10     | 300->500 |              0.333 |        0.481 |            -0.015 |  543.627 |
| waviness      | 100->300 |              1     |        9.348 |            -0.013 |   20.591 |
| waviness      | 100->500 |              1     |       11.903 |            -0.008 |   32.602 |
| waviness      | 300->500 |              0.5   |        2.633 |            -0.004 |   78.24  |

## Decision distances (floors) under the variants

|                                                         |   ('decisive', 'pooled') |   ('decisive', 'transfer') |   ('decisive', 'within') |   ('safe', 'pooled') |   ('safe', 'transfer') |   ('safe', 'within') |
|:--------------------------------------------------------|-------------------------:|---------------------------:|-------------------------:|---------------------:|-----------------------:|---------------------:|
| ("M3, friction of the pattern's median oil film", 'M3') |                    nan   |                        nan |                     40   |                nan   |                  nan   |                  3   |
| ('M6 conformalised GP', 'M6')                           |                     75   |                         75 |                     75   |                  0.5 |                   25   |                  0.5 |
| ('conformal level 0.80', 'M2')                          |                     50   |                         75 |                     25   |                  1   |                   20   |                  0.5 |
| ('conformal level 0.80', 'M5')                          |                      9   |                         40 |                      6   |                  1.5 |                   30   |                  2.5 |
| ('conformal level 0.95', 'M2')                          |                     50   |                         75 |                     25   |                  0   |                   20   |                  0.5 |
| ('conformal level 0.95', 'M5')                          |                     15   |                         40 |                      7.5 |                  1   |                   30   |                  1.5 |
| ('reference', 'M1')                                     |                     30   |                         40 |                     15   |                 30   |                   40   |                 15   |
| ('reference', 'M2')                                     |                     50   |                         75 |                     25   |                  0   |                   20   |                  0.5 |
| ('reference', 'M5')                                     |                     12   |                         40 |                      7   |                  1   |                   30   |                  2   |
| ('resolution target 0.90', 'M0')                        |                     75   |                         75 |                     75   |                 75   |                   75   |                 75   |
| ('resolution target 0.90', 'M1')                        |                     20   |                         25 |                     10   |                 20   |                   25   |                 10   |
| ('resolution target 0.90', 'M2')                        |                     40   |                         40 |                     20   |                  0   |                    8.5 |                  0   |
| ('resolution target 0.90', 'M3')                        |                     25   |                         40 |                     20   |                  0   |                   12   |                  0   |
| ('resolution target 0.90', 'M4')                        |                     12   |                        150 |                      8   |                  0   |                  150   |                  0   |
| ('resolution target 0.90', 'M5')                        |                      5.5 |                         25 |                      5   |                  0.5 |                   20   |                  0.5 |
| ('resolution target 0.99', 'M0')                        |                    150   |                        150 |                    150   |                150   |                  150   |                150   |
| ('resolution target 0.99', 'M1')                        |                     50   |                         75 |                     30   |                 50   |                   75   |                 30   |
| ('resolution target 0.99', 'M2')                        |                     75   |                         75 |                     50   |                  0.5 |                   30   |                  1.5 |
| ('resolution target 0.99', 'M3')                        |                     30   |                         75 |                     30   |                  3.5 |                   40   |                  3.5 |
| ('resolution target 0.99', 'M4')                        |                     30   |                        200 |                     15   |                  2.5 |                  200   |                  4   |
| ('resolution target 0.99', 'M5')                        |                     15   |                         75 |                     12   |                  5   |                   40   |                  5.5 |
| ('temperature-adjusted', 'M1')                          |                     25   |                         40 |                     15   |                 25   |                   40   |                 15   |
| ('temperature-adjusted', 'M2')                          |                     50   |                         75 |                     30   |                  0   |                   15   |                  0.5 |
| ('temperature-adjusted', 'M5')                          |                     10   |                         40 |                      7   |                  1   |                   30   |                  2.5 |
