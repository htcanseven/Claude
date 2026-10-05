# Sensitivity of M3 and M4 to the learner and its settings

Settings: reference: {'max_depth': 3, 'max_iter': 200, 'learning_rate': 0.08, 'random_state': 0}; regularised: {'max_depth': 2, 'max_iter': 100, 'learning_rate': 0.05, 'l2_regularization': 1.0, 'random_state': 0}; flexible: {'max_depth': 6, 'max_iter': 400, 'learning_rate': 0.1, 'min_samples_leaf': 10, 'random_state': 0}; ridge: ridge (alpha 1); selected: the boosting setting with the smallest mean absolute leave-one-out error over the calibration alternatives.

Reference setting reproduces the stored distances: True.

## Decisive and safe distances over all characteristics (floors, bootstrap 95 % interval)

| scope    | rule   | setting     | decisive      | safe          |
|:---------|:-------|:------------|:--------------|:--------------|
| transfer | M3     | flexible    | 50 (50-50)    | 25 (20-30)    |
| transfer | M3     | reference   | 50 (50-50)    | 20 (20-25)    |
| transfer | M3     | regularised | 50 (50-75)    | 30 (20-30)    |
| transfer | M3     | ridge       | 50 (50-75)    | 20 (10-25)    |
| transfer | M3     | selected    | 50 (50-50)    | 25 (20-30)    |
| transfer | M4     | flexible    | 150 (150-200) | 150 (150-200) |
| transfer | M4     | reference   | 150 (150-200) | 150 (150-200) |
| transfer | M4     | regularised | 150 (150-200) | 150 (150-200) |
| transfer | M4     | ridge       | 150 (150-200) | 150 (150-200) |
| transfer | M4     | selected    | 150 (150-200) | 150 (150-200) |
| within   | M3     | flexible    | 25 (20-25)    | 0 (0-0.5)     |
| within   | M3     | reference   | 20 (20-25)    | 0 (0-0.5)     |
| within   | M3     | regularised | 25 (20-25)    | 0 (0-2)       |
| within   | M3     | ridge       | 30 (25-40)    | 0.5 (0-2.5)   |
| within   | M3     | selected    | 20 (20-25)    | 0.5 (0-0.5)   |
| within   | M4     | flexible    | 12 (9.5-12)   | 0.5 (0-2.5)   |
| within   | M4     | reference   | 12 (10-12)    | 1 (0-2)       |
| within   | M4     | regularised | 12 (10-15)    | 0.5 (0-2.5)   |
| within   | M4     | ridge       | 15 (12-15)    | 0.5 (0-1)     |
| within   | M4     | selected    | 12 (10-12)    | 0.5 (0-2.5)   |

## Settings chosen by the inner leave-one-out (design cases)

|                    |   flexible |   reference |   regularised |
|:-------------------|-----------:|------------:|--------------:|
| ('transfer', 'M3') |         63 |          36 |            27 |
| ('transfer', 'M4') |         45 |          36 |            45 |
| ('within', 'M3')   |         42 |          48 |            36 |
| ('within', 'M4')   |         51 |          27 |            48 |

## Decisive distance per characteristic

| qc            |   ('transfer', 'M3', 'flexible') |   ('transfer', 'M3', 'reference') |   ('transfer', 'M3', 'regularised') |   ('transfer', 'M3', 'ridge') |   ('transfer', 'M3', 'selected') |   ('transfer', 'M4', 'flexible') |   ('transfer', 'M4', 'reference') |   ('transfer', 'M4', 'regularised') |   ('transfer', 'M4', 'ridge') |   ('transfer', 'M4', 'selected') |   ('within', 'M3', 'flexible') |   ('within', 'M3', 'reference') |   ('within', 'M3', 'regularised') |   ('within', 'M3', 'ridge') |   ('within', 'M3', 'selected') |   ('within', 'M4', 'flexible') |   ('within', 'M4', 'reference') |   ('within', 'M4', 'regularised') |   ('within', 'M4', 'ridge') |   ('within', 'M4', 'selected') |
|:--------------|---------------------------------:|----------------------------------:|------------------------------------:|------------------------------:|---------------------------------:|---------------------------------:|----------------------------------:|------------------------------------:|------------------------------:|---------------------------------:|-------------------------------:|--------------------------------:|----------------------------------:|----------------------------:|-------------------------------:|-------------------------------:|--------------------------------:|----------------------------------:|----------------------------:|-------------------------------:|
| all           |                               50 |                              50   |                                  50 |                            50 |                               50 |                              150 |                               150 |                                 150 |                           150 |                              150 |                             25 |                              20 |                                25 |                          30 |                             20 |                           12   |                            12   |                              12   |                        15   |                           12   |
| arm_op20      |                               75 |                              50   |                                  75 |                            75 |                               75 |                               50 |                                50 |                                  50 |                            50 |                               50 |                             20 |                              20 |                                20 |                          30 |                             20 |                           12   |                             9   |                              12   |                        20   |                           12   |
| depth_op10    |                               40 |                              40   |                                  40 |                            50 |                               40 |                               75 |                                75 |                                  75 |                            75 |                               75 |                             25 |                              20 |                                25 |                          40 |                             20 |                           12   |                            12   |                              12   |                        15   |                           12   |
| dome_op20     |                               75 |                              75   |                                  75 |                            75 |                               75 |                               50 |                                75 |                                  50 |                            40 |                               50 |                             30 |                              30 |                                30 |                          40 |                             30 |                           20   |                            20   |                              20   |                        15   |                           20   |
| drawin_corner |                               30 |                              25   |                                  20 |                            30 |                               20 |                              200 |                               200 |                                 200 |                           200 |                              200 |                             20 |                              15 |                                15 |                          25 |                             15 |                           10   |                            10   |                               9   |                         8.5 |                           10   |
| drawin_mid    |                               12 |                               6.5 |                                   9 |                            20 |                                7 |                               20 |                                20 |                                  20 |                            20 |                               20 |                             20 |                              15 |                                15 |                          20 |                             15 |                            7.5 |                             7.5 |                               7.5 |                         5.5 |                            7.5 |
| wall_op10     |                               50 |                              50   |                                  40 |                            40 |                               40 |                              150 |                               150 |                                 150 |                           150 |                              150 |                             30 |                              30 |                                25 |                          25 |                             30 |                            5   |                             4.5 |                               5   |                         5   |                            4.5 |
| waviness      |                               50 |                              50   |                                  50 |                            50 |                               50 |                               12 |                                15 |                                  15 |                            20 |                               12 |                             20 |                              20 |                                20 |                          40 |                             20 |                            4   |                             4   |                               3.5 |                        12   |                            4   |
