# Second demonstration: build orientation in powder bed fusion of PA12

Specimens: 111 (anchors excluded); orientation classes of 30 deg; characteristics: 8.

## Floor (batch = class within a build)

| qc                        |   floor |   n_batches |   sd_within | measurement_note              |
|:--------------------------|--------:|------------:|------------:|:------------------------------|
| Cylindricity_Cyl_24mm_Pos |  0.057  |          18 |      0.049  | mean of three CMM repetitions |
| Diameter_Cyl_24mm_Neg     |  0.0772 |          18 |      0.0643 | mean of three CMM repetitions |
| Diameter_Cyl_24mm_Pos     |  0.0722 |          18 |      0.0786 | mean of three CMM repetitions |
| Diameter_Cyl_8mm_Neg      |  0.0702 |          18 |      0.0798 | mean of three CMM repetitions |
| Diameter_Cyl_8mm_Pos      |  0.1311 |          18 |      0.125  | mean of three CMM repetitions |
| Dist_HX1_1-4              |  0.0511 |          18 |      0.0708 | mean of three CMM repetitions |
| Flatness_Base_Plate       |  0.0719 |          18 |      0.0729 | mean of three CMM repetitions |
| Position_Cyl_24mm_Pos     |  0.3142 |          18 |      0.3209 | mean of three CMM repetitions |

## Orientation-class pairs with ESR >= 1

| qc                        |   sum |   size |
|:--------------------------|------:|-------:|
| Cylindricity_Cyl_24mm_Pos |     5 |     15 |
| Diameter_Cyl_24mm_Neg     |     0 |     15 |
| Diameter_Cyl_24mm_Pos     |     3 |     15 |
| Diameter_Cyl_8mm_Neg      |     2 |     15 |
| Diameter_Cyl_8mm_Pos      |     1 |     15 |
| Dist_HX1_1-4              |     6 |     15 |
| Flatness_Base_Plate       |     0 |     15 |
| Position_Cyl_24mm_Pos     |     1 |     15 |

## Decisive / safe distances (floors), held-out class, within

| scope   | method   | qc   |   resolution_floors |   safe_floors |   resolution_lo |   resolution_hi |   safe_lo |   safe_hi |
|:--------|:---------|:-----|--------------------:|--------------:|----------------:|----------------:|----------:|----------:|
| within  | M0       | all  |                 5.5 |           5.5 |             4.5 |             6   |       4.5 |         6 |
| within  | M1       | all  |                 2   |           2   |             1.5 |             2   |       1.5 |         2 |
| within  | M2       | all  |                 4   |           1   |             4   |             4.5 |       0   |         1 |
| within  | M5       | all  |                 3.5 |           1   |             3.5 |             4   |       0.5 |         1 |

| qc                        |   ('resolution_floors', 'M0') |   ('resolution_floors', 'M1') |   ('resolution_floors', 'M2') |   ('resolution_floors', 'M5') |   ('safe_floors', 'M0') |   ('safe_floors', 'M1') |   ('safe_floors', 'M2') |   ('safe_floors', 'M5') |
|:--------------------------|------------------------------:|------------------------------:|------------------------------:|------------------------------:|------------------------:|------------------------:|------------------------:|------------------------:|
| Cylindricity_Cyl_24mm_Pos |                           6   |                           2   |                           3   |                           2.5 |                     6   |                     2   |                     1   |                     0.5 |
| Diameter_Cyl_24mm_Neg     |                           4   |                           2   |                           2.5 |                           2   |                     4   |                     2   |                     1   |                     1   |
| Diameter_Cyl_24mm_Pos     |                           4   |                           1.5 |                           3   |                           1   |                     4   |                     1.5 |                     0.5 |                     1   |
| Diameter_Cyl_8mm_Neg      |                           4.5 |                           1   |                           1.5 |                           1.5 |                     4.5 |                     1   |                     0.5 |                     1   |
| Diameter_Cyl_8mm_Pos      |                           4   |                           1   |                           1.5 |                           2   |                     4   |                     1   |                     0.5 |                     0   |
| Dist_HX1_1-4              |                           6.5 |                           3   |                           4.5 |                           4   |                     6.5 |                     3   |                     1.5 |                     1   |
| Flatness_Base_Plate       |                           6   |                           1.5 |                           2.5 |                           2   |                     6   |                     1.5 |                     0.5 |                     0.5 |
| Position_Cyl_24mm_Pos     |                           4.5 |                           2   |                           3.5 |                           3   |                     4.5 |                     2   |                     1   |                     2.5 |
| all                       |                           5.5 |                           2   |                           4   |                           3.5 |                     5.5 |                     2   |                     1   |                     1   |

## Calibration budget

|   k | method   |   resolution_floors |   safe_floors |   wrong_at_10 |   uncertain_at_10 |
|----:|:---------|--------------------:|--------------:|--------------:|------------------:|
|   1 | M0       |                 5.5 |           5.5 |             0 |                 0 |
|   1 | M1       |                 2   |           2   |             0 |                 0 |
|   1 | M2       |                 2   |           2   |             0 |                 0 |
|   2 | M0       |                 5.5 |           5.5 |             0 |                 0 |
|   2 | M1       |                 2   |           2   |             0 |                 0 |
|   2 | M2       |                 2.5 |           1.5 |             0 |                 0 |
|   2 | M5       |                 3   |           1.5 |             0 |                 0 |
|   3 | M0       |                 5.5 |           5.5 |             0 |                 0 |
|   3 | M1       |                 2   |           2   |             0 |                 0 |
|   3 | M2       |                 3.5 |           1   |             0 |                 0 |
|   3 | M5       |                 3   |           1   |             0 |                 0 |
|   4 | M0       |                 5.5 |           5.5 |             0 |                 0 |
|   4 | M1       |                 2   |           2   |             0 |                 0 |
|   4 | M2       |                 3.5 |           1   |             0 |                 0 |
|   4 | M5       |                 3   |           1   |             0 |                 0 |
|   5 | M0       |                 5.5 |           5.5 |             0 |                 0 |
|   5 | M1       |                 2   |           2   |             0 |                 0 |
|   5 | M2       |                 4   |           1   |             0 |                 0 |
|   5 | M5       |                 3.5 |           1   |             0 |                 0 |
