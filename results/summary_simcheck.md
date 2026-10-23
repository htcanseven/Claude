# The simulation against the produced process, and the measurement

Mc friction fits at the upper edge of the grid (0.15): within the family 72 of 72.

## sim_validation

| qc            | unit   | geometry   |   bhf_kN |   measured_centre |   measured_min_series |   measured_max_series |   sim_nominal |   sim_minus_measured |   sim_minus_measured_floors |   sim_min_over_friction |   sim_max_over_friction | measured_inside_friction_range   |   closest_mu |   sim_at_closest_mu |   residual_at_closest_floors |   sim_xy_sd_floors |   sim_roughness_sd_floors |
|:--------------|:-------|:-----------|---------:|------------------:|----------------------:|----------------------:|--------------:|---------------------:|----------------------------:|------------------------:|------------------------:|:---------------------------------|-------------:|--------------------:|-----------------------------:|-------------------:|--------------------------:|
| drawin_mid    | mm     | concave    |      100 |           15.144  |               15.1043 |               15.1831 |       16.9815 |               1.8375 |                     36.9633 |                 16.6344 |                 17.3405 | False                            |         0.15 |             16.6344 |                      29.9823 |             0.0699 |                    0.0716 |
| drawin_corner | mm     | concave    |      100 |            4.9617 |                4.9429 |                4.9764 |        8.385  |               3.4233 |                     64.9942 |                  8.2401 |                  8.525  | False                            |         0.15 |              8.2401 |                      62.2443 |           nan      |                    0.0762 |
| waviness      | mm     | concave    |      100 |            0.1028 |                0.1012 |                0.1045 |        0.0821 |              -0.0207 |                     -5.6623 |                  0.0597 |                  0.0961 | False                            |         0.05 |              0.0961 |                      -1.8409 |           nan      |                    0.4173 |
| wall_op10     | deg    | concave    |      100 |           21.5989 |               21.5144 |               21.6653 |       20.9182 |              -0.6807 |                     -8.4542 |                 19.7747 |                 21.1012 | False                            |         0.07 |             21.1012 |                      -6.1813 |             2.324  |                    3.0515 |
| arm_op20      | deg    | concave    |      100 |            0.7594 |                0.6223 |                0.8729 |       -0.4379 |              -1.1973 |                    -10.3183 |                 -1.1032 |                  0.1517 | False                            |         0.05 |              0.1517 |                      -5.2372 |             0.4504 |                    0.8714 |
| depth_op10    | mm     | concave    |      100 |           28.437  |               28.4032 |               28.4562 |       29.3484 |               0.9114 |                    104.331  |                 29.3484 |                 29.376  | False                            |         0.1  |             29.3484 |                     104.331  |           nan      |                    0.7629 |
| dome_op20     | mm     | concave    |      100 |            0.0297 |                0.0195 |                0.0413 |        0.1336 |               0.1039 |                     30.1789 |                  0.0124 |                  0.1336 | True                             |         0.15 |              0.0304 |                       0.2032 |           nan      |                    9.758  |
| drawin_mid    | mm     | concave    |      300 |           14.8224 |               14.7604 |               14.8812 |       15.6632 |               0.8407 |                     16.9125 |                 14.8335 |                 16.6711 | False                            |         0.15 |             14.8335 |                       0.2236 |             0.0699 |                    0.0716 |
| drawin_corner | mm     | concave    |      300 |            4.8106 |                4.7651 |                4.8383 |        7.9711 |               3.1605 |                     60.0062 |                  7.5169 |                  8.3282 | False                            |         0.15 |              7.5169 |                      51.3829 |           nan      |                    0.0762 |
| waviness      | mm     | concave    |      300 |            0.0665 |                0.0654 |                0.0672 |        0.0144 |              -0.0522 |                    -14.2583 |                  0.013  |                  0.0513 | False                            |         0.05 |              0.0513 |                      -4.1737 |           nan      |                    0.4173 |
| wall_op10     | deg    | concave    |      300 |           21.5421 |               21.5139 |               21.5636 |       20.3195 |              -1.2226 |                    -15.1852 |                 19.4421 |                 20.6125 | False                            |         0.11 |             20.6125 |                     -11.5461 |             2.324  |                    3.0515 |
| arm_op20      | deg    | concave    |      300 |            0.4757 |                0.4237 |                0.5334 |       -3.7021 |              -4.1778 |                    -36.0038 |                 -4.3634 |                 -1.1418 | False                            |         0.05 |             -1.1418 |                     -13.9398 |             0.4504 |                    0.8714 |
| depth_op10    | mm     | concave    |      300 |           28.3281 |               28.3277 |               28.3287 |       29.3405 |               1.0124 |                    115.895  |                 29.3077 |                 29.3578 | False                            |         0.06 |             29.3077 |                     112.136  |           nan      |                    0.7629 |
| dome_op20     | mm     | concave    |      300 |            0.036  |                0.0343 |                0.0377 |        0.1387 |               0.1028 |                     29.8612 |                  0.0324 |                  0.1753 | True                             |         0.15 |              0.0324 |                      -1.0319 |           nan      |                    9.758  |
| drawin_mid    | mm     | concave    |      500 |           14.7286 |               14.6673 |               14.7785 |       14.8507 |               0.1221 |                      2.4569 |                 13.592  |                 16.143  | True                             |         0.11 |             14.6091 |                      -2.4038 |             0.0699 |                    0.0716 |
| drawin_corner | mm     | concave    |      500 |            4.6199 |                4.5673 |                4.6523 |        7.2104 |               2.5905 |                     49.1832 |                  5.8755 |                  8.0458 | False                            |         0.15 |              5.8755 |                      23.8382 |           nan      |                    0.0762 |
| waviness      | mm     | concave    |      500 |            0.0524 |                0.0506 |                0.0546 |        0.0394 |              -0.013  |                     -3.5582 |                  0.0108 |                  0.0777 | True                             |         0.12 |              0.0558 |                       0.9246 |           nan      |                    0.4173 |
| wall_op10     | deg    | concave    |      500 |           21.5555 |               21.5132 |               21.5887 |       19.4185 |              -2.137  |                    -26.5423 |                 19.3274 |                 20.9151 | False                            |         0.15 |             20.9151 |                      -7.9548 |             2.324  |                    3.0515 |
| arm_op20      | deg    | concave    |      500 |            0.2892 |                0.2494 |                0.3211 |       -4.3493 |              -4.6385 |                    -39.9743 |                 -4.4514 |                 -2.9284 | False                            |         0.05 |             -2.9284 |                     -27.7293 |             0.4504 |                    0.8714 |
| depth_op10    | mm     | concave    |      500 |           28.286  |               28.2805 |               28.2898 |       29.2418 |               0.9558 |                    109.414  |                 29.0046 |                 29.3256 | False                            |         0.15 |             29.0046 |                      82.2633 |           nan      |                    0.7629 |
| dome_op20     | mm     | concave    |      500 |            0.0431 |                0.0394 |                0.046  |        0.0829 |               0.0398 |                     11.5535 |                 -0.0048 |                  0.1545 | True                             |         0.08 |              0.0502 |                       2.0757 |           nan      |                    9.758  |
| drawin_mid    | mm     | convex     |      100 |           16.08   |               16.0675 |               16.0875 |       18.0855 |               2.0055 |                     38.4821 |                 17.8069 |                 18.4079 | False                            |         0.15 |             17.8069 |                      33.1374 |             0.1665 |                    0.0749 |
| drawin_corner | mm     | convex     |      100 |           10.0035 |                9.9975 |               10.0109 |       13.4795 |               3.476  |                    116.168  |                 13.3095 |                 13.6522 | False                            |         0.15 |             13.3095 |                     110.489  |           nan      |                    0.1963 |
| waviness      | mm     | convex     |      100 |            0.0784 |                0.0776 |                0.0788 |        0.066  |              -0.0123 |                     -5.7828 |                  0.0526 |                  0.0665 | False                            |         0.14 |              0.0665 |                      -5.5763 |           nan      |                    3.9659 |
| wall_op10     | deg    | convex     |      100 |           11.4479 |               11.4316 |               11.4664 |       10.7366 |              -0.7113 |                     -9.156  |                 10.0147 |                 10.9137 | False                            |         0.11 |             10.9137 |                      -6.8768 |             1.8166 |                    1.6562 |
| arm_op20      | deg    | convex     |      100 |           -4.3299 |               -4.3764 |               -4.2532 |       -4.4434 |              -0.1134 |                     -1.1354 |                 -4.6874 |                 -3.1038 | True                             |         0.11 |             -4.2928 |                       0.3711 |             1.0902 |                    0.8714 |
| depth_op10    | mm     | convex     |      100 |           28.8177 |               28.817  |               28.8189 |       29.8799 |               1.0621 |                     86.2535 |                 29.8121 |                 29.8799 | False                            |         0.05 |             29.8121 |                      80.7515 |           nan      |                    0.7393 |
| dome_op20     | mm     | convex     |      100 |            0.1162 |                0.1042 |                0.1269 |        0.0495 |              -0.0667 |                     -8.087  |                 -0.0021 |                  0.0666 | False                            |         0.12 |              0.0666 |                      -6.0122 |           nan      |                    2.4356 |
| drawin_mid    | mm     | convex     |      300 |           15.762  |               15.7064 |               15.8378 |       16.9062 |               1.1442 |                     21.9556 |                 16.1655 |                 17.7104 | False                            |         0.15 |             16.1655 |                       7.7427 |             0.1665 |                    0.0749 |
| drawin_corner | mm     | convex     |      300 |            9.876  |                9.8572 |                9.8993 |       13.1436 |               3.2676 |                    109.203  |                 12.7578 |                 13.4714 | False                            |         0.15 |             12.7578 |                      96.3089 |           nan      |                    0.1963 |
| waviness      | mm     | convex     |      300 |            0.0611 |                0.0608 |                0.0613 |        0.0596 |              -0.0014 |                     -0.6679 |                  0.0569 |                  0.0899 | True                             |         0.1  |              0.0596 |                      -0.6679 |           nan      |                    3.9659 |
| wall_op10     | deg    | convex     |      300 |           11.43   |               11.4276 |               11.4348 |       10.2997 |              -1.1303 |                    -14.5501 |                 10.2969 |                 10.8475 | False                            |         0.05 |             10.8475 |                      -7.4981 |             1.8166 |                    1.6562 |
| arm_op20      | deg    | convex     |      300 |           -4.9466 |               -5.1308 |               -4.622  |       -5.5032 |              -0.5565 |                     -5.5703 |                 -5.5032 |                 -4.2457 | True                             |         0.06 |             -4.9492 |                      -0.0256 |             1.0902 |                    0.8714 |
| depth_op10    | mm     | convex     |      300 |           28.7163 |               28.7053 |               28.7341 |       29.6353 |               0.919  |                     74.6268 |                 29.4742 |                 29.8028 | False                            |         0.15 |             29.4742 |                      61.5469 |           nan      |                    0.7393 |
| dome_op20     | mm     | convex     |      300 |            0.1047 |                0.0571 |                0.1318 |        0.0177 |              -0.0871 |                    -10.5628 |                  0.0019 |                  0.0887 | False                            |         0.12 |              0.0887 |                      -1.9423 |           nan      |                    2.4356 |
| drawin_mid    | mm     | convex     |      500 |           15.6624 |               15.6331 |               15.6875 |       16.0515 |               0.3891 |                      7.4661 |                 14.7825 |                 17.225  | True                             |         0.12 |             15.5733 |                      -1.7095 |             0.1665 |                    0.0749 |
| drawin_corner | mm     | convex     |      500 |            9.6685 |                9.5729 |                9.7603 |       12.5839 |               2.9154 |                     97.4343 |                 11.3756 |                 13.267  | False                            |         0.15 |             11.3756 |                      57.0526 |           nan      |                    0.1963 |
| waviness      | mm     | convex     |      500 |            0.0611 |                0.0597 |                0.0627 |        0.0724 |               0.0113 |                      5.2977 |                  0.0573 |                  0.1112 | True                             |         0.07 |              0.0641 |                       1.415  |           nan      |                    3.9659 |
| wall_op10     | deg    | convex     |      500 |           11.5025 |               11.3765 |               11.6653 |       11.1289 |              -0.3736 |                     -4.8087 |                 10.3135 |                 11.1972 | False                            |         0.14 |             11.1972 |                      -3.9298 |             1.8166 |                    1.6562 |
| arm_op20      | deg    | convex     |      500 |           -4.72   |               -4.9088 |               -4.5275 |       -4.2957 |               0.4243 |                      4.2467 |                 -5.5857 |                 -2.3006 | True                             |         0.08 |             -4.7204 |                      -0.0035 |             1.0902 |                    0.8714 |
| depth_op10    | mm     | convex     |      500 |           28.6565 |               28.6279 |               28.6794 |       29.3657 |               0.7092 |                     57.5951 |                 29.1233 |                 29.6448 | False                            |         0.15 |             29.1233 |                      37.9099 |           nan      |                    0.7393 |
| dome_op20     | mm     | convex     |      500 |            0.0938 |                0.0694 |                0.1134 |        0.0275 |              -0.0662 |                     -8.035  |                 -0.0008 |                  0.0818 | False                            |         0.11 |              0.0818 |                      -1.4557 |           nan      |                    2.4356 |

## sim_mc_friction

| scope   | target             | lubrication   |   mu | at_upper_edge   | at_lower_edge   |
|:--------|:-------------------|:--------------|-----:|:----------------|:----------------|
| within  | concave/100/coarse | coarse        | 0.15 | True            | False           |
| within  | concave/100/coarse | medium        | 0.15 | True            | False           |
| within  | concave/100/coarse | fine          | 0.15 | True            | False           |
| within  | concave/100/fine   | coarse        | 0.15 | True            | False           |
| within  | concave/100/fine   | medium        | 0.15 | True            | False           |
| within  | concave/100/fine   | fine          | 0.15 | True            | False           |
| within  | concave/100/medium | coarse        | 0.15 | True            | False           |
| within  | concave/100/medium | medium        | 0.15 | True            | False           |
| within  | concave/100/medium | fine          | 0.15 | True            | False           |
| within  | concave/300/coarse | coarse        | 0.15 | True            | False           |
| within  | concave/300/coarse | medium        | 0.15 | True            | False           |
| within  | concave/300/coarse | fine          | 0.15 | True            | False           |
| within  | concave/300/fine   | coarse        | 0.15 | True            | False           |
| within  | concave/300/fine   | medium        | 0.15 | True            | False           |
| within  | concave/300/fine   | fine          | 0.15 | True            | False           |
| within  | concave/300/medium | coarse        | 0.15 | True            | False           |
| within  | concave/300/medium | medium        | 0.15 | True            | False           |
| within  | concave/300/medium | fine          | 0.15 | True            | False           |
| within  | concave/500/coarse | coarse        | 0.15 | True            | False           |
| within  | concave/500/coarse | medium        | 0.15 | True            | False           |
| within  | concave/500/coarse | fine          | 0.15 | True            | False           |
| within  | concave/500/fine   | coarse        | 0.15 | True            | False           |
| within  | concave/500/fine   | medium        | 0.15 | True            | False           |
| within  | concave/500/fine   | fine          | 0.15 | True            | False           |
| within  | concave/500/medium | coarse        | 0.15 | True            | False           |
| within  | concave/500/medium | medium        | 0.15 | True            | False           |
| within  | concave/500/medium | fine          | 0.15 | True            | False           |
| within  | convex/100/coarse  | coarse        | 0.15 | True            | False           |
| within  | convex/100/coarse  | medium        | 0.15 | True            | False           |
| within  | convex/100/coarse  | fine          | 0.15 | True            | False           |
| within  | convex/100/fine    | coarse        | 0.15 | True            | False           |
| within  | convex/100/fine    | medium        | 0.15 | True            | False           |
| within  | convex/100/fine    | fine          | 0.15 | True            | False           |
| within  | convex/100/medium  | coarse        | 0.15 | True            | False           |
| within  | convex/100/medium  | medium        | 0.15 | True            | False           |
| within  | convex/100/medium  | fine          | 0.15 | True            | False           |
| within  | convex/300/coarse  | coarse        | 0.15 | True            | False           |
| within  | convex/300/coarse  | medium        | 0.15 | True            | False           |
| within  | convex/300/coarse  | fine          | 0.15 | True            | False           |
| within  | convex/300/fine    | coarse        | 0.15 | True            | False           |
| within  | convex/300/fine    | medium        | 0.15 | True            | False           |
| within  | convex/300/fine    | fine          | 0.15 | True            | False           |
| within  | convex/300/medium  | coarse        | 0.15 | True            | False           |
| within  | convex/300/medium  | medium        | 0.15 | True            | False           |
| within  | convex/300/medium  | fine          | 0.15 | True            | False           |
| within  | convex/500/coarse  | coarse        | 0.15 | True            | False           |
| within  | convex/500/coarse  | medium        | 0.15 | True            | False           |
| within  | convex/500/coarse  | fine          | 0.15 | True            | False           |
| within  | convex/500/fine    | coarse        | 0.15 | True            | False           |
| within  | convex/500/fine    | medium        | 0.15 | True            | False           |
| within  | convex/500/fine    | fine          | 0.15 | True            | False           |
| within  | convex/500/medium  | coarse        | 0.15 | True            | False           |
| within  | convex/500/medium  | medium        | 0.15 | True            | False           |
| within  | convex/500/medium  | fine          | 0.15 | True            | False           |
| setting | concave/100        | coarse        | 0.15 | True            | False           |
| setting | concave/100        | medium        | 0.15 | True            | False           |
| setting | concave/100        | fine          | 0.15 | True            | False           |
| setting | concave/300        | coarse        | 0.15 | True            | False           |
| setting | concave/300        | medium        | 0.15 | True            | False           |
| setting | concave/300        | fine          | 0.15 | True            | False           |
| setting | concave/500        | coarse        | 0.15 | True            | False           |
| setting | concave/500        | medium        | 0.15 | True            | False           |
| setting | concave/500        | fine          | 0.15 | True            | False           |
| setting | convex/100         | coarse        | 0.15 | True            | False           |
| setting | convex/100         | medium        | 0.15 | True            | False           |
| setting | convex/100         | fine          | 0.15 | True            | False           |
| setting | convex/300         | coarse        | 0.15 | True            | False           |
| setting | convex/300         | medium        | 0.15 | True            | False           |
| setting | convex/300         | fine          | 0.15 | True            | False           |
| setting | convex/500         | coarse        | 0.15 | True            | False           |
| setting | convex/500         | medium        | 0.15 | True            | False           |
| setting | convex/500         | fine          | 0.15 | True            | False           |

## sim_depth_offset

| geometry   |   bhf_kN |   depth_measured |   depth_sim |   depth_sim_minus_measured |   flange_angle_measured_deg |   flange_angle_sim_deg |   flange_rise_measured |   flange_rise_sim |   rise_difference |   wall_r15_measured |   wall_r15_sim |   wall_r15_measured_minus_sim |   press_bdc_median_mm |   press_bdc_sd_mm |
|:-----------|---------:|-----------------:|------------:|---------------------------:|----------------------------:|-----------------------:|-----------------------:|------------------:|------------------:|--------------------:|---------------:|------------------------------:|----------------------:|------------------:|
| concave    |      100 |          28.449  |     29.3484 |                     0.8994 |                      1.1144 |                 0.8983 |                 0.2991 |            0.2352 |           -0.0638 |             64.3891 |        62.3425 |                        2.0466 |               448.66  |            0.0077 |
| concave    |      300 |          28.3283 |     29.3405 |                     1.0122 |                      0.6302 |                -0.3156 |                 0.1735 |           -0.0881 |           -0.2616 |             64.3385 |        62.14   |                        2.1984 |               448.678 |            0.0197 |
| concave    |      500 |          28.2865 |     29.2418 |                     0.9552 |                      0.5747 |                -0.9253 |                 0.1556 |           -0.2907 |           -0.4463 |             64.3405 |        62.3254 |                        2.0151 |               448.574 |            0.0388 |
| convex     |      100 |          28.8175 |     29.8799 |                     1.0624 |                      1.3724 |                 1.0696 |                 0.1483 |            0.0934 |           -0.0549 |             74.9686 |        72.8135 |                        2.1551 |               448.666 |            0.0058 |
| convex     |      300 |          28.7114 |     29.6353 |                     0.9239 |                      1.0181 |                 0.2337 |                 0.1194 |            0.0286 |           -0.0909 |             74.9633 |        72.8836 |                        2.0797 |               448.678 |            0.0528 |
| convex     |      500 |          28.6623 |     29.3657 |                     0.7034 |                      1.162  |                 0.327  |                 0.136  |            0.0457 |           -0.0904 |             74.9825 |        72.925  |                        2.0576 |               448.72  |            0.0057 |

## sim_oil_mapping

| geometry   |   bhf_kN | qc            |   sim_mm_per_mu |   implied_mm_per_gm2 |   within_run_mm_per_gm2 |   between_patterns_min |   between_patterns_max |   between_patterns_median |   oil_traverse_sd_median |   oil_between_parts_sd |
|:-----------|---------:|:--------------|----------------:|---------------------:|------------------------:|-----------------------:|-----------------------:|--------------------------:|-------------------------:|-----------------------:|
| concave    |      100 | drawin_mid    |         -7.0832 |               0.8854 |                 -0.0076 |                -0.3748 |                 1.9959 |                   -0.1678 |                   0.2889 |                 0.1388 |
| concave    |      100 | drawin_corner |         -2.8608 |               0.3576 |                  0.0347 |                 0.1144 |                 0.4863 |                    0.1469 |                   0.2889 |                 0.1388 |
| concave    |      300 | drawin_mid    |        -18.3616 |               2.2952 |                  0.091  |                 0.2469 |                 0.5977 |                    0.3612 |                   0.278  |                 0.0993 |
| concave    |      300 | drawin_corner |         -7.9614 |               0.9952 |                  0.0089 |                -0.0443 |                 0.672  |                    0.1891 |                   0.278  |                 0.0993 |
| concave    |      500 | drawin_mid    |        -25.028  |               3.1285 |                  0.0519 |                 0.192  |                 0.3359 |                    0.2668 |                   0.2932 |                 0.1054 |
| concave    |      500 | drawin_corner |        -21.4888 |               2.6861 |                  0.0505 |                 0.0602 |                 0.3365 |                    0.2038 |                   0.2932 |                 0.1054 |
| convex     |      100 | drawin_mid    |         -6.1248 |               0.7656 |                  0.029  |                 0.0191 |                 0.068  |                    0.0502 |                   0.1378 |                 0.0645 |
| convex     |      100 | drawin_corner |         -3.4391 |               0.4299 |                 -0.0178 |                -0.0525 |                 0.0314 |                   -0.022  |                   0.1378 |                 0.0645 |
| convex     |      300 | drawin_mid    |        -15.4584 |               1.9323 |                  0.0688 |                 0.3538 |                 0.5261 |                    0.388  |                   0.1522 |                 0.0934 |
| convex     |      300 | drawin_corner |         -7.1587 |               0.8948 |                  0.0118 |                 0.1019 |                 0.2159 |                    0.1245 |                   0.1522 |                 0.0934 |
| convex     |      500 | drawin_mid    |        -23.9577 |               2.9947 |                  0.0229 |                -0.0838 |                 0.2301 |                    0.0689 |                   0.2662 |                 0.1038 |
| convex     |      500 | drawin_corner |        -18.2951 |               2.2869 |                  0.0105 |                 0.3533 |                 0.4201 |                    0.3858 |                   0.2662 |                 0.1038 |

## sim_envelope_variant

| envelope                    | scope                 | method   |   resolution_floors |   safe_floors |   median_width_floors |
|:----------------------------|:----------------------|:---------|--------------------:|--------------:|----------------------:|
| DDACS grid (reference)      | setting/extrapolation | M0w      |              118.75 |         77.45 |               24.03   |
| DDACS grid (reference)      | setting/extrapolation | M2       |               17.5  |          9.9  |                9.6317 |
| DDACS grid (reference)      | setting/extrapolation | M5       |               18.5  |          8.9  |                9.1032 |
| DDACS grid (reference)      | setting/interpolation | M0w      |              118.6  |         94.25 |               22.5813 |
| DDACS grid (reference)      | setting/interpolation | M2       |               17.75 |          2.7  |               11.4546 |
| DDACS grid (reference)      | setting/interpolation | M5       |               19.05 |          2.8  |               12.8387 |
| DDACS grid (reference)      | transfer              | M0w      |              117.4  |         79.3  |               23.2631 |
| DDACS grid (reference)      | transfer              | M2       |               40.75 |         26.4  |               15.1897 |
| DDACS grid (reference)      | transfer              | M5       |               35.2  |         31.3  |                4.661  |
| DDACS grid (reference)      | within                | M0w      |              118.7  |         94.25 |               23.5267 |
| DDACS grid (reference)      | within                | M2       |               22.65 |          0.15 |               15.1647 |
| DDACS grid (reference)      | within                | M5       |                7.15 |          0.75 |                4.3789 |
| measured incoming variation | setting/extrapolation | M0w      |              112.2  |        100.85 |               12.4013 |
| measured incoming variation | setting/extrapolation | M2       |               33.6  |          7.7  |               14.0847 |
| measured incoming variation | setting/extrapolation | M5       |               39.85 |          7.05 |               13.9502 |
| measured incoming variation | setting/interpolation | M0w      |              116.6  |        104.8  |                9.6784 |
| measured incoming variation | setting/interpolation | M2       |               34.6  |          1.7  |               17.6032 |
| measured incoming variation | setting/interpolation | M5       |               40.6  |          3.35 |               17.805  |
| measured incoming variation | transfer              | M0w      |              111.05 |         88.6  |               13.8055 |
| measured incoming variation | transfer              | M2       |               42.65 |         30.05 |               22.9072 |
| measured incoming variation | transfer              | M5       |               36.2  |         31.9  |               12.2967 |
| measured incoming variation | within                | M0w      |              113.55 |        101.05 |               11.8984 |
| measured incoming variation | within                | M2       |               34.75 |          1.25 |               21.784  |
| measured incoming variation | within                | M5       |               24.15 |          1.25 |               12.8247 |

## sim_envelope_ranges

| alternative        | env_thickness   | env_friction   |
|:-------------------|:----------------|:---------------|
| concave/100/coarse | 0.98-1.00       | 0.07-0.13      |
| concave/100/fine   | 0.97-1.00       | 0.05-0.13      |
| concave/100/medium | 0.98-1.00       | 0.10-0.15      |
| concave/300/coarse | 0.98-1.00       | 0.07-0.12      |
| concave/300/fine   | 0.98-1.00       | 0.12-0.15      |
| concave/300/medium | 0.98-1.00       | 0.10-0.15      |
| concave/500/coarse | 0.98-1.00       | 0.05-0.10      |
| concave/500/fine   | 0.98-1.00       | 0.10-0.15      |
| concave/500/medium | 0.98-1.00       | 0.07-0.13      |
| convex/100/coarse  | 0.97-1.00       | 0.06-0.10      |
| convex/100/fine    | 0.97-1.00       | 0.11-0.15      |
| convex/100/medium  | 0.97-1.00       | 0.08-0.12      |
| convex/300/coarse  | 0.98-1.00       | 0.06-0.11      |
| convex/300/fine    | 0.98-0.99       | 0.11-0.14      |
| convex/300/medium  | 0.98-0.99       | 0.08-0.14      |
| convex/500/coarse  | 0.98-1.00       | 0.05-0.09      |
| convex/500/fine    | 0.98-1.00       | 0.10-0.14      |
| convex/500/medium  | 0.98-1.00       | 0.07-0.12      |

## meas_characteristics

| qc            | unit   | operation   | region                          | directions                            |   resolution_step |   step_over_floor | distinct_per_series   |   zero_se_alternatives | known_biases                                                                                                                     |
|:--------------|:-------|:------------|:--------------------------------|:--------------------------------------|------------------:|------------------:|:----------------------|-----------------------:|:---------------------------------------------------------------------------------------------------------------------------------|
| drawin_mid    | mm     | OP10        | flange, mid-sides               | x widths only, (210 - Wx)/2           |            0.0192 |            0.3777 | 6-21                  |                      5 | Wy - Wx 2.29 to 3.47 mm; sd(Wy)/sd(Wx) 3.73 to 17.65                                                                             |
| drawin_corner | mm     | OP10        | flange, corner tips             | mean of the two diagonals             |            0.0001 |            0.0033 | 491-500               |                      0 | diagonals differ by 1.64 to 2.17 mm                                                                                              |
| waviness      | mm     | OP10        | flange                          | residual sd about a quadratic surface |            0      |            0.0035 | 469-494               |                      0 | -                                                                                                                                |
| wall_op10     | deg    | OP10        | side walls at mid-depth         | mean of east and west walls           |            0.0004 |            0.0049 | 497-500               |                      0 | north wall -1.64 to -0.92 deg against E/W on the convex cups (-0.05 to 0.39 concave); south wall shadowed, 6.73 to 10.00 deg off |
| arm_op20      | deg    | OP20        | cut arms, centre lines          | mean of the four arms                 |            0.0005 |            0.0045 | 496-500               |                      0 | -                                                                                                                                |
| depth_op10    | mm     | OP10        | flange against the bottom plane | median over the flange                |            0      |            0.0033 | 486-497               |                      0 | the flange plane is cut away at OP20                                                                                             |
| dome_op20     | mm     | OP20        | cup bottom, sag at r = 40 mm    | paraboloid fit                        |            0      |            0.0035 | 474-497               |                      0 | -                                                                                                                                |

## meas_cut_walls

| cut_wall_north_minus_east_convex   | cut_wall_west_minus_east_convex   |
|:-----------------------------------|:----------------------------------|
| 3.34 to 5.60                       | -0.32 to 7.24                     |

## meas_run_floors

| qc            |   floor | batch_interval    | cluster_interval   |   run_floor_min |   run_floor_median |   run_floor_max |   floor_without_warm_up |   warm_up_ratio |
|:--------------|--------:|:------------------|:-------------------|----------------:|-------------------:|----------------:|------------------------:|----------------:|
| drawin_mid    |  0.0505 | 0.04471-0.06058   | 0.04187-0.06106    |          0.3598 |             0.7273 |          1.6181 |                  0.05   |          0.9886 |
| drawin_corner |  0.0464 | 0.03451-0.05232   | 0.03236-0.05275    |          0.2673 |             0.7869 |          1.6176 |                  0.0442 |          0.9535 |
| waviness      |  0.0028 | 0.002412-0.003115 | 0.002053-0.00503   |          0.2137 |             0.7646 |          2.0806 |                  0.0025 |          0.8926 |
| wall_op10     |  0.0785 | 0.06617-0.1012    | 0.05377-0.1032     |          0.3039 |             0.4814 |          1.7381 |                  0.0629 |          0.8017 |
| arm_op20      |  0.1085 | 0.09422-0.1215    | 0.08861-0.1525     |          0.3976 |             0.7868 |          2.155  |                  0.1088 |          1.0021 |
| depth_op10    |  0.0109 | 0.009623-0.01236  | 0.008981-0.01244   |          0.3937 |             0.8609 |          1.4514 |                  0.0081 |          0.7456 |
| dome_op20     |  0.007  | 0.006072-0.008053 | 0.005151-0.008446  |          0.4249 |             0.8242 |          1.6119 |                  0.0065 |          0.9298 |

## meas_tooling_reference

| geometry   |   r_wx_cupwidth |   floor_cup_width_mm |   floor_wx_mm |   floor_depth_mm |   cup_width_mm |   wx_mm |   lateral_scale_drift_bound |
|:-----------|----------------:|---------------------:|--------------:|-----------------:|---------------:|--------:|----------------------------:|
| concave    |         -0.2726 |               0.0625 |        0.0994 |           0.0087 |        128.709 | 180.308 |                      0.0005 |
| convex     |          0.2663 |               0.0667 |        0.1042 |           0.0123 |        149.949 | 178.462 |                      0.0004 |

