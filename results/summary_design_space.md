# Design space from the DDACS corners

Simulations used: 396 (material scaling 1.0; thickness [0.98, 0.99]).

## Sensitivities and minimum resolvable change

| geometry   | qc            | factor                | unit       |   sim_sensitivity |   sim_sens_sd |   real_sensitivity |   floor |   resolvable_steps_real |   n_pairs |   mrc_real_floor |   mrc_sim_floor |   mrc_sim_floor_plus_margin |
|:-----------|:--------------|:----------------------|:-----------|------------------:|--------------:|-------------------:|--------:|------------------------:|----------:|-----------------:|----------------:|----------------------------:|
| concave    | drawin_mid    | geometry low->tool    | step       |           -2.5861 |        0.8419 |           nan      |  0.0497 |                 52.0219 |        66 |         nan      |        nan      |                    nan      |
| concave    | drawin_mid    | geometry tool->high   | step       |           -3.7156 |        0.06   |           nan      |  0.0497 |                 74.7429 |        66 |         nan      |        nan      |                    nan      |
| concave    | drawin_mid    | bhf_kN                | per 100 kN |           -0.5336 |      nan      |            -0.1038 |  0.0497 |                nan      |       nan |           0.4787 |          0.0932 |                      1.1085 |
| concave    | drawin_mid    | friction_coefficient  | per 0.01   |           -0.1686 |      nan      |            -0.0015 |  0.0497 |                nan      |       nan |          32.3258 |          0.2948 |                      3.5076 |
| concave    | drawin_mid    | sheet_metal_thickness | per 10 um  |            0.0185 |      nan      |            -0.0158 |  0.0497 |                nan      |       nan |           3.1442 |          2.6937 |                     32.0514 |
| concave    | drawin_corner | geometry low->tool    | step       |           -1.0174 |        0.3755 |           nan      |  0.0527 |                 19.3161 |        66 |         nan      |        nan      |                    nan      |
| concave    | drawin_corner | geometry tool->high   | step       |           -1.4166 |        0.0459 |           nan      |  0.0527 |                 26.8957 |        66 |         nan      |        nan      |                    nan      |
| concave    | drawin_corner | bhf_kN                | per 100 kN |           -0.3213 |      nan      |            -0.0854 |  0.0527 |                nan      |       nan |           0.6164 |          0.1639 |                      0.747  |
| concave    | drawin_corner | friction_coefficient  | per 0.01   |           -0.1085 |      nan      |            -0.0022 |  0.0527 |                nan      |       nan |          23.7962 |          0.4855 |                      2.2122 |
| concave    | drawin_corner | sheet_metal_thickness | per 10 um  |            0.0107 |      nan      |             0.0125 |  0.0527 |                nan      |       nan |           4.2094 |          4.9289 |                     22.459  |
| concave    | waviness      | geometry low->tool    | step       |            0.0168 |        0.0188 |           nan      |  0.0037 |                  4.5881 |        66 |         nan      |        nan      |                    nan      |
| concave    | waviness      | geometry tool->high   | step       |            0.0152 |        0.039  |           nan      |  0.0037 |                  4.1564 |        66 |         nan      |        nan      |                    nan      |
| concave    | waviness      | bhf_kN                | per 100 kN |           -0.0081 |      nan      |            -0.0126 |  0.0037 |                nan      |       nan |           0.2902 |          0.4538 |                      5.1192 |
| concave    | waviness      | friction_coefficient  | per 0.01   |            0.0007 |      nan      |            -0      |  0.0037 |                nan      |       nan |          80.9705 |          5.5749 |                     62.8864 |
| concave    | waviness      | sheet_metal_thickness | per 10 um  |            0.0005 |      nan      |             0.0012 |  0.0037 |                nan      |       nan |           3.0981 |          7.0357 |                     79.3651 |
| concave    | wall_op10     | geometry low->tool    | step       |            9.8701 |        0.6764 |           nan      |  0.0805 |                122.592  |        66 |         nan      |        nan      |                    nan      |
| concave    | wall_op10     | geometry tool->high   | step       |           10.1325 |        0.9413 |           nan      |  0.0805 |                125.851  |        66 |         nan      |        nan      |                    nan      |
| concave    | wall_op10     | bhf_kN                | per 100 kN |           -0.0949 |      nan      |            -0.0108 |  0.0805 |                nan      |       nan |           7.4258 |          0.8486 |                      5.5132 |
| concave    | wall_op10     | friction_coefficient  | per 0.01   |           -0.0239 |      nan      |            -0.0048 |  0.0805 |                nan      |       nan |          16.814  |          3.374  |                     21.921  |
| concave    | wall_op10     | sheet_metal_thickness | per 10 um  |            0.0278 |      nan      |             0.0127 |  0.0805 |                nan      |       nan |           6.3346 |          2.8937 |                     18.8005 |
| concave    | arm_op20      | geometry low->tool    | step       |           -1.5541 |        1.2242 |           nan      |  0.116  |                 13.3933 |        66 |         nan      |        nan      |                    nan      |
| concave    | arm_op20      | geometry tool->high   | step       |           -0.6574 |        1.3441 |           nan      |  0.116  |                  5.6654 |        66 |         nan      |        nan      |                    nan      |
| concave    | arm_op20      | bhf_kN                | per 100 kN |           -0.8848 |      nan      |            -0.1175 |  0.116  |                nan      |       nan |           0.9872 |          0.1311 |                      3.8576 |
| concave    | arm_op20      | friction_coefficient  | per 0.01   |           -0.1312 |      nan      |            -0.0014 |  0.116  |                nan      |       nan |          82.3445 |          0.8844 |                     26.0146 |
| concave    | arm_op20      | sheet_metal_thickness | per 10 um  |            0.2741 |      nan      |             0.0248 |  0.116  |                nan      |       nan |           4.674  |          0.4233 |                     12.4508 |
| concave    | depth_op10    | geometry low->tool    | step       |            0.0137 |        0.0892 |           nan      |  0.0087 |                  1.5711 |        66 |         nan      |        nan      |                    nan      |
| concave    | depth_op10    | geometry tool->high   | step       |           -0.1383 |        0.1415 |           nan      |  0.0087 |                 15.8351 |        66 |         nan      |        nan      |                    nan      |
| concave    | depth_op10    | bhf_kN                | per 100 kN |           -0.0409 |      nan      |            -0.0378 |  0.0087 |                nan      |       nan |           0.2314 |          0.2135 |                      3.2138 |
| concave    | depth_op10    | friction_coefficient  | per 0.01   |           -0.0114 |      nan      |             0.0003 |  0.0087 |                nan      |       nan |          30.1069 |          0.7658 |                     11.5282 |
| concave    | depth_op10    | sheet_metal_thickness | per 10 um  |            0.0078 |      nan      |             0.0069 |  0.0087 |                nan      |       nan |           1.2668 |          1.1262 |                     16.9535 |
| concave    | dome_op20     | geometry low->tool    | step       |            0.0283 |        0.0889 |           nan      |  0.0034 |                  8.212  |        66 |         nan      |        nan      |                    nan      |
| concave    | dome_op20     | geometry tool->high   | step       |           -0.022  |        0.0703 |           nan      |  0.0034 |                  6.3897 |        66 |         nan      |        nan      |                    nan      |
| concave    | dome_op20     | bhf_kN                | per 100 kN |            0.0005 |      nan      |             0.0033 |  0.0034 |                nan      |       nan |           1.0285 |          7.0172 |                    287.855  |
| concave    | dome_op20     | friction_coefficient  | per 0.01   |           -0.0063 |      nan      |             0      |  0.0034 |                nan      |       nan |         342.123  |          0.5433 |                     22.2867 |
| concave    | dome_op20     | sheet_metal_thickness | per 10 um  |            0.0038 |      nan      |             0.0038 |  0.0034 |                nan      |       nan |           0.9083 |          0.8951 |                     36.7164 |
| convex     | drawin_mid    | geometry low->tool    | step       |            0.4203 |        1.1124 |           nan      |  0.0521 |                  8.065  |        66 |         nan      |        nan      |                    nan      |
| convex     | drawin_mid    | geometry tool->high   | step       |           -5.9676 |        0.648  |           nan      |  0.0521 |                114.508  |        66 |         nan      |        nan      |                    nan      |
| convex     | drawin_mid    | bhf_kN                | per 100 kN |           -0.518  |      nan      |            -0.1044 |  0.0521 |                nan      |       nan |           0.4992 |          0.1006 |                      1.1465 |
| convex     | drawin_mid    | friction_coefficient  | per 0.01   |           -0.1522 |      nan      |            -0.0036 |  0.0521 |                nan      |       nan |          14.6341 |          0.3424 |                      3.9021 |
| convex     | drawin_mid    | sheet_metal_thickness | per 10 um  |            0.0129 |      nan      |            -0.0108 |  0.0521 |                nan      |       nan |           4.8454 |          4.0487 |                     46.1386 |
| convex     | drawin_corner | geometry low->tool    | step       |           -1.952  |        0.851  |           nan      |  0.0299 |                 65.2362 |        66 |         nan      |        nan      |                    nan      |
| convex     | drawin_corner | geometry tool->high   | step       |           -4.5474 |        0.4468 |           nan      |  0.0299 |                151.975  |        66 |         nan      |        nan      |                    nan      |
| convex     | drawin_corner | bhf_kN                | per 100 kN |           -0.2528 |      nan      |            -0.0838 |  0.0299 |                nan      |       nan |           0.3573 |          0.1184 |                      0.8594 |
| convex     | drawin_corner | friction_coefficient  | per 0.01   |           -0.0973 |      nan      |            -0.0005 |  0.0299 |                nan      |       nan |          54.6849 |          0.3076 |                      2.2336 |
| convex     | drawin_corner | sheet_metal_thickness | per 10 um  |            0.0082 |      nan      |             0.008  |  0.0299 |                nan      |       nan |           3.7444 |          3.6278 |                     26.3397 |
| convex     | waviness      | geometry low->tool    | step       |           -0.0117 |        0.0275 |           nan      |  0.0021 |                  5.4848 |        66 |         nan      |        nan      |                    nan      |
| convex     | waviness      | geometry tool->high   | step       |            0.0807 |        0.0352 |           nan      |  0.0021 |                 37.8913 |        66 |         nan      |        nan      |                    nan      |
| convex     | waviness      | bhf_kN                | per 100 kN |            0.0025 |      nan      |            -0.0043 |  0.0021 |                nan      |       nan |           0.4938 |          0.848  |                     15.8166 |
| convex     | waviness      | friction_coefficient  | per 0.01   |            0.0021 |      nan      |             0      |  0.0021 |                nan      |       nan |          99.8812 |          1.0275 |                     19.1645 |
| convex     | waviness      | sheet_metal_thickness | per 10 um  |           -0.0014 |      nan      |             0.0003 |  0.0021 |                nan      |       nan |           6.3443 |          1.5156 |                     28.268  |
| convex     | wall_op10     | geometry low->tool    | step       |            0.7217 |        0.5023 |           nan      |  0.0777 |                  9.2896 |        66 |         nan      |        nan      |                    nan      |
| convex     | wall_op10     | geometry tool->high   | step       |           19.8406 |        0.787  |           nan      |  0.0777 |                255.394  |        66 |         nan      |        nan      |                    nan      |
| convex     | wall_op10     | bhf_kN                | per 100 kN |            0.0469 |      nan      |             0.0136 |  0.0777 |                nan      |       nan |           5.6962 |          1.6573 |                     11.099  |
| convex     | wall_op10     | friction_coefficient  | per 0.01   |            0.0614 |      nan      |             0.0015 |  0.0777 |                nan      |       nan |          53.2597 |          1.265  |                      8.4718 |
| convex     | wall_op10     | sheet_metal_thickness | per 10 um  |            0.0329 |      nan      |             0.0057 |  0.0777 |                nan      |       nan |          13.5243 |          2.3637 |                     15.8298 |
| convex     | arm_op20      | geometry low->tool    | step       |           -3.718  |        0.644  |           nan      |  0.0999 |                 37.2126 |        66 |         nan      |        nan      |                    nan      |
| convex     | arm_op20      | geometry tool->high   | step       |            5.0517 |        0.8292 |           nan      |  0.0999 |                 50.5609 |        66 |         nan      |        nan      |                    nan      |
| convex     | arm_op20      | bhf_kN                | per 100 kN |           -0.0286 |      nan      |            -0.0975 |  0.0999 |                nan      |       nan |           1.0245 |          3.4929 |                    118.766  |
| convex     | arm_op20      | friction_coefficient  | per 0.01   |            0.0777 |      nan      |             0.0043 |  0.0999 |                nan      |       nan |          23.3081 |          1.286  |                     43.7272 |
| convex     | arm_op20      | sheet_metal_thickness | per 10 um  |            0.1487 |      nan      |            -0.0221 |  0.0999 |                nan      |       nan |           4.5196 |          0.6721 |                     22.8539 |
| convex     | depth_op10    | geometry low->tool    | step       |            0.2087 |        0.1263 |           nan      |  0.0123 |                 16.9466 |        66 |         nan      |        nan      |                    nan      |
| convex     | depth_op10    | geometry tool->high   | step       |           -0.5499 |        0.1917 |           nan      |  0.0123 |                 44.655  |        66 |         nan      |        nan      |                    nan      |
| convex     | depth_op10    | bhf_kN                | per 100 kN |           -0.1203 |      nan      |            -0.0403 |  0.0123 |                nan      |       nan |           0.3054 |          0.1024 |                      1.123  |
| convex     | depth_op10    | friction_coefficient  | per 0.01   |           -0.0265 |      nan      |            -0.0004 |  0.0123 |                nan      |       nan |          32.2848 |          0.4651 |                      5.1022 |
| convex     | depth_op10    | sheet_metal_thickness | per 10 um  |            0.0272 |      nan      |             0.0037 |  0.0123 |                nan      |       nan |           3.3268 |          0.452  |                      4.9582 |
| convex     | dome_op20     | geometry low->tool    | step       |           -0.0055 |        0.0448 |           nan      |  0.0082 |                  0.6657 |        66 |         nan      |        nan      |                    nan      |
| convex     | dome_op20     | geometry tool->high   | step       |            0.005  |        0.0384 |           nan      |  0.0082 |                  0.604  |        66 |         nan      |        nan      |                    nan      |
| convex     | dome_op20     | bhf_kN                | per 100 kN |           -0.0019 |      nan      |            -0.0056 |  0.0082 |                nan      |       nan |           1.4711 |          4.3345 |                     76.7835 |
| convex     | dome_op20     | friction_coefficient  | per 0.01   |            0.0011 |      nan      |             0.0001 |  0.0082 |                nan      |       nan |         162.523  |          7.7288 |                    136.912  |
| convex     | dome_op20     | sheet_metal_thickness | per 10 um  |           -0.0047 |      nan      |             0.0013 |  0.0082 |                nan      |       nan |           6.541  |          1.7644 |                     31.2557 |

## Gaussian-process surrogate, leave-one-out error over process conditions

| geometry   | qc            |   rmse_loo |   n |   floor |   rmse_over_floor |
|:-----------|:--------------|-----------:|----:|--------:|------------------:|
| concave    | drawin_mid    |     0.0031 |  66 |  0.0497 |            0.0631 |
| concave    | drawin_corner |     0.0022 |  66 |  0.0527 |            0.0418 |
| concave    | waviness      |     0.0028 |  66 |  0.0037 |            0.7576 |
| concave    | wall_op10     |     0.0559 |  66 |  0.0805 |            0.6947 |
| concave    | arm_op20      |     0.104  |  66 |  0.116  |            0.8964 |
| concave    | depth_op10    |     0.0074 |  66 |  0.0087 |            0.8469 |
| concave    | dome_op20     |     0.0387 |  66 |  0.0034 |           11.2331 |
| convex     | drawin_mid    |     0.0033 |  66 |  0.0521 |            0.0631 |
| convex     | drawin_corner |     0.0034 |  66 |  0.0299 |            0.115  |
| convex     | waviness      |     0.0118 |  66 |  0.0021 |            5.5531 |
| convex     | wall_op10     |     0.1414 |  66 |  0.0777 |            1.8199 |
| convex     | arm_op20      |     0.1781 |  66 |  0.0999 |            1.7826 |
| convex     | depth_op10    |     0.0141 |  66 |  0.0123 |            1.1484 |
| convex     | dome_op20     |     0.0137 |  66 |  0.0082 |            1.6682 |
