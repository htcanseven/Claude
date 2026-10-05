# Requirement scenarios from general tolerances

Number of the 18 alternatives whose 95th percentile meets the limit:

| qc        |   H |   K |   L |   c |   f/m |   v |
|:----------|----:|----:|----:|----:|------:|----:|
| arm_op20  | nan | nan | nan |   9 |     3 |   9 |
| dome_op20 |  11 |  18 |  18 | nan |   nan | nan |
| wall_op10 | nan | nan | nan |   0 |     0 |  18 |

## Verdicts over all scenarios (correct / false accept / false reject / uncertain)

| method   |   pooled |   transfer |   within |
|:---------|---------:|-----------:|---------:|
| M0       |    0.66  |      0.66  |    0.66  |
| M1       |    0.735 |      0.66  |    0.87  |
| M2       |    0.389 |      0.438 |    0.716 |
| M3       |    0.463 |      0.506 |    0.63  |
| M4       |    0.71  |      0.426 |    0.84  |
| M5       |    0.883 |      0.648 |    0.889 |

| scope    | method   |   correct |   false_accept |   false_reject |   uncertain |
|:---------|:---------|----------:|---------------:|---------------:|------------:|
| pooled   | M0       |     0.66  |          0.191 |          0.148 |       0     |
| pooled   | M1       |     0.735 |          0.099 |          0.167 |       0     |
| pooled   | M2       |     0.389 |          0     |          0     |       0.611 |
| pooled   | M3       |     0.463 |          0     |          0.012 |       0.525 |
| pooled   | M4       |     0.71  |          0     |          0.006 |       0.284 |
| pooled   | M5       |     0.883 |          0.006 |          0.006 |       0.105 |
| transfer | M0       |     0.66  |          0.191 |          0.148 |       0     |
| transfer | M1       |     0.66  |          0.136 |          0.204 |       0     |
| transfer | M2       |     0.438 |          0.043 |          0.13  |       0.389 |
| transfer | M3       |     0.506 |          0.049 |          0.13  |       0.315 |
| transfer | M4       |     0.426 |          0.253 |          0.185 |       0.136 |
| transfer | M5       |     0.648 |          0.099 |          0.191 |       0.062 |
| within   | M0       |     0.66  |          0.191 |          0.148 |       0     |
| within   | M1       |     0.87  |          0.068 |          0.062 |       0     |
| within   | M2       |     0.716 |          0     |          0     |       0.284 |
| within   | M3       |     0.63  |          0     |          0.006 |       0.364 |
| within   | M4       |     0.84  |          0     |          0.006 |       0.154 |
| within   | M5       |     0.889 |          0     |          0.012 |       0.099 |

## Per characteristic and class, within the family

| scope   | method   | qc        | tol_class   |   correct |   false_accept |   false_reject |   uncertain |
|:--------|:---------|:----------|:------------|----------:|---------------:|---------------:|------------:|
| within  | M0       | arm_op20  | c           |     0.667 |          0     |          0.333 |       0     |
| within  | M0       | arm_op20  | f/m         |     0.833 |          0     |          0.167 |       0     |
| within  | M0       | arm_op20  | v           |     0.667 |          0     |          0.333 |       0     |
| within  | M0       | dome_op20 | H           |     0.111 |          0.389 |          0.5   |       0     |
| within  | M0       | dome_op20 | K           |     1     |          0     |          0     |       0     |
| within  | M0       | dome_op20 | L           |     1     |          0     |          0     |       0     |
| within  | M0       | wall_op10 | c           |     0.167 |          0.833 |          0     |       0     |
| within  | M0       | wall_op10 | f/m         |     0.5   |          0.5   |          0     |       0     |
| within  | M0       | wall_op10 | v           |     1     |          0     |          0     |       0     |
| within  | M1       | arm_op20  | c           |     0.833 |          0     |          0.167 |       0     |
| within  | M1       | arm_op20  | f/m         |     0.667 |          0.167 |          0.167 |       0     |
| within  | M1       | arm_op20  | v           |     1     |          0     |          0     |       0     |
| within  | M1       | dome_op20 | H           |     0.833 |          0.111 |          0.056 |       0     |
| within  | M1       | dome_op20 | K           |     1     |          0     |          0     |       0     |
| within  | M1       | dome_op20 | L           |     1     |          0     |          0     |       0     |
| within  | M1       | wall_op10 | c           |     0.667 |          0.333 |          0     |       0     |
| within  | M1       | wall_op10 | f/m         |     1     |          0     |          0     |       0     |
| within  | M1       | wall_op10 | v           |     0.833 |          0     |          0.167 |       0     |
| within  | M2       | arm_op20  | c           |     0.667 |          0     |          0     |       0.333 |
| within  | M2       | arm_op20  | f/m         |     0.5   |          0     |          0     |       0.5   |
| within  | M2       | arm_op20  | v           |     0.667 |          0     |          0     |       0.333 |
| within  | M2       | dome_op20 | H           |     0.5   |          0     |          0     |       0.5   |
| within  | M2       | dome_op20 | K           |     0.944 |          0     |          0     |       0.056 |
| within  | M2       | dome_op20 | L           |     1     |          0     |          0     |       0     |
| within  | M2       | wall_op10 | c           |     0.667 |          0     |          0     |       0.333 |
| within  | M2       | wall_op10 | f/m         |     1     |          0     |          0     |       0     |
| within  | M2       | wall_op10 | v           |     0.5   |          0     |          0     |       0.5   |
| within  | M3       | arm_op20  | c           |     0.5   |          0     |          0     |       0.5   |
| within  | M3       | arm_op20  | f/m         |     0.556 |          0     |          0     |       0.444 |
| within  | M3       | arm_op20  | v           |     0.722 |          0     |          0     |       0.278 |
| within  | M3       | dome_op20 | H           |     0.389 |          0     |          0.056 |       0.556 |
| within  | M3       | dome_op20 | K           |     0.833 |          0     |          0     |       0.167 |
| within  | M3       | dome_op20 | L           |     1     |          0     |          0     |       0     |
| within  | M3       | wall_op10 | c           |     0.278 |          0     |          0     |       0.722 |
| within  | M3       | wall_op10 | f/m         |     0.889 |          0     |          0     |       0.111 |
| within  | M3       | wall_op10 | v           |     0.5   |          0     |          0     |       0.5   |
| within  | M4       | arm_op20  | c           |     0.833 |          0     |          0     |       0.167 |
| within  | M4       | arm_op20  | f/m         |     0.667 |          0     |          0     |       0.333 |
| within  | M4       | arm_op20  | v           |     1     |          0     |          0     |       0     |
| within  | M4       | dome_op20 | H           |     0.5   |          0     |          0.056 |       0.444 |
| within  | M4       | dome_op20 | K           |     0.833 |          0     |          0     |       0.167 |
| within  | M4       | dome_op20 | L           |     1     |          0     |          0     |       0     |
| within  | M4       | wall_op10 | c           |     1     |          0     |          0     |       0     |
| within  | M4       | wall_op10 | f/m         |     1     |          0     |          0     |       0     |
| within  | M4       | wall_op10 | v           |     0.722 |          0     |          0     |       0.278 |
| within  | M5       | arm_op20  | c           |     0.889 |          0     |          0.056 |       0.056 |
| within  | M5       | arm_op20  | f/m         |     0.667 |          0     |          0     |       0.333 |
| within  | M5       | arm_op20  | v           |     1     |          0     |          0     |       0     |
| within  | M5       | dome_op20 | H           |     0.556 |          0     |          0.056 |       0.389 |
| within  | M5       | dome_op20 | K           |     0.944 |          0     |          0     |       0.056 |
| within  | M5       | dome_op20 | L           |     1     |          0     |          0     |       0     |
| within  | M5       | wall_op10 | c           |     1     |          0     |          0     |       0     |
| within  | M5       | wall_op10 | f/m         |     1     |          0     |          0     |       0     |
| within  | M5       | wall_op10 | v           |     0.944 |          0     |          0     |       0.056 |
