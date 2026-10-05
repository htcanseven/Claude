# Production floor and effects between alternatives

Parts per alternative: 500-500; batch size 50 (batches below 80% valid dropped); centres: 10 % trimmed means; alpha 0.95; bootstrap 2000 (seed 1).

## Floor per characteristic

| qc            | label                     | unit   |   floor |   floor_lo |   floor_hi |   floor_lo_alt |   floor_hi_alt |   floor_concave |   floor_convex |   sd_within |
|:--------------|:--------------------------|:-------|--------:|-----------:|-----------:|---------------:|---------------:|----------------:|---------------:|------------:|
| drawin_mid    | Draw-in at mid-sides      | mm     |  0.0505 |     0.0447 |     0.0606 |         0.0419 |         0.0611 |          0.0497 |         0.0521 |      0.0391 |
| drawin_corner | Draw-in at corners        | mm     |  0.0464 |     0.0345 |     0.0523 |         0.0324 |         0.0528 |          0.0527 |         0.0299 |      0.027  |
| waviness      | Flange waviness           | mm     |  0.0028 |     0.0024 |     0.0031 |         0.0021 |         0.005  |          0.0037 |         0.0021 |      0.002  |
| wall_op10     | Wall angle after drawing  | deg    |  0.0785 |     0.0662 |     0.1012 |         0.0538 |         0.1032 |          0.0805 |         0.0777 |      0.0833 |
| arm_op20      | Arm angle after cutting   | deg    |  0.1085 |     0.0942 |     0.1215 |         0.0886 |         0.1525 |          0.116  |         0.0999 |      0.0914 |
| depth_op10    | Cup depth                 | mm     |  0.0109 |     0.0096 |     0.0124 |         0.009  |         0.0124 |          0.0087 |         0.0123 |      0.0069 |
| dome_op20     | Bottom dome after cutting | mm     |  0.007  |     0.0061 |     0.0081 |         0.0052 |         0.0084 |          0.0034 |         0.0082 |      0.0036 |

## Share of single-factor contrasts with ESR >= 1

| qc            |   bhf |   geometry |   lubrication |
|:--------------|------:|-----------:|--------------:|
| arm_op20      |  0.94 |          1 |          0.5  |
| depth_op10    |  1    |          1 |          0.39 |
| dome_op20     |  0.83 |          1 |          0.61 |
| drawin_corner |  1    |          1 |          0.39 |
| drawin_mid    |  1    |          1 |          0.5  |
| wall_op10     |  0.22 |          1 |          0.28 |
| waviness      |  0.83 |          1 |          0.17 |

## Minimum resolvable change

| qc            | factor       |   slope |       mrc |    mrc_lo |      mrc_hi |
|:--------------|:-------------|--------:|----------:|----------:|------------:|
| drawin_mid    | bhf_kN       | -0.001  |   48.531  |   42.6154 |     58.107  |
| drawin_mid    | oil_gm2      |  0.0382 |    1.3241 |    1.0192 |      2.442  |
| drawin_mid    | sheet_um     | -0.0014 |   36.2724 |   29.9681 |     48.3953 |
| drawin_mid    | punch_temp_C | -0.0027 |   18.3861 |   10.4695 |     59.8058 |
| drawin_corner | bhf_kN       | -0.0008 |   54.825  |   40.5564 |     62.0586 |
| drawin_corner | oil_gm2      |  0.0266 |    1.7469 |    1.256  |      4.6557 |
| drawin_corner | sheet_um     |  0.0011 |   42.8237 |   33.052  |     52.6618 |
| drawin_corner | punch_temp_C | -0.0029 |   15.8547 |   10.1322 |     34.6431 |
| waviness      | bhf_kN       | -0.0001 |   32.6025 |   28.733  |     36.7854 |
| waviness      | oil_gm2      |  0.0006 |    4.3364 |    1.9493 |     82.2596 |
| waviness      | sheet_um     |  0.0001 |   31.8303 |   27.2076 |     39.5422 |
| waviness      | punch_temp_C | -0.0002 |   14.9544 |    9.1807 |     46.0719 |
| wall_op10     | bhf_kN       |  0      | 5613.46   | 2061.33   | 113670      |
| wall_op10     | oil_gm2      |  0.0274 |    2.8665 |    1.5506 |     30.8365 |
| wall_op10     | sheet_um     |  0.001  |   77.5545 |   48.9268 |    202.873  |
| wall_op10     | punch_temp_C | -0.0031 |   25.5389 |   13.523  |    235.902  |
| arm_op20      | bhf_kN       | -0.0011 |  100.923  |   87.5398 |    112.23   |
| arm_op20      | oil_gm2      | -0.0009 |  118.261  |    2.6524 |    225.835  |
| arm_op20      | sheet_um     |  0.0007 |  147.279  |   80.6522 |    853.066  |
| arm_op20      | punch_temp_C |  0.0007 |  162.387  |   21.6808 |   1444.74   |
| depth_op10    | bhf_kN       | -0.0004 |   27.8867 |   24.605  |     31.6537 |
| depth_op10    | oil_gm2      |  0.0006 |   19.6459 |    3.1839 |    185.637  |
| depth_op10    | sheet_um     |  0.0006 |   19.0722 |   16.1044 |     23.3517 |
| depth_op10    | punch_temp_C |  0.0008 |   13.7113 |    8.909  |     29.8403 |
| dome_op20     | bhf_kN       | -0      |  623.121  |  494.257  |    828.04   |
| dome_op20     | oil_gm2      |  0.0002 |   42.639  |    5.1502 |    274.529  |
| dome_op20     | sheet_um     |  0.0003 |   24.6726 |   20.5106 |     30.4856 |
| dome_op20     | punch_temp_C | -0.0004 |   16.8893 |   10.9225 |     30.681  |
