# Applicability guards

Transfer across geometries; correct / wrong / uncertain shares at |d| = 10 floors.

| guard   | method   |   resolution_floors |   safe_floors |   correct |   wrong |   uncertain |   share_guarded |
|:--------|:---------|--------------------:|--------------:|----------:|--------:|------------:|----------------:|
| none    | M0       |                 150 |           150 |     0.687 |   0.313 |       0     |           0     |
| none    | M1       |                  40 |            40 |     0.706 |   0.294 |       0     |           0     |
| none    | M2       |                  75 |            20 |     0.651 |   0.091 |       0.258 |           0     |
| none    | M3       |                  50 |            20 |     0.659 |   0.111 |       0.23  |           0     |
| none    | M4       |                 150 |           150 |     0.556 |   0.306 |       0.139 |           0     |
| none    | M5       |                  40 |            30 |     0.766 |   0.206 |       0.028 |           0     |
| family  | M0       |                 inf |             0 |     0     |   0     |       1     |           1     |
| family  | M1       |                 inf |             0 |     0     |   0     |       1     |           1     |
| family  | M2       |                 inf |             0 |     0     |   0     |       1     |           1     |
| family  | M3       |                 inf |             0 |     0     |   0     |       1     |           1     |
| family  | M4       |                 inf |             0 |     0     |   0     |       1     |           1     |
| family  | M5       |                 inf |             0 |     0     |   0     |       1     |           1     |
| novelty | M0       |                 inf |             0 |     0.083 |   0.012 |       0.905 |           0.905 |
| novelty | M1       |                 inf |             0 |     0.079 |   0.016 |       0.905 |           0.905 |
| novelty | M2       |                 inf |             0 |     0.048 |   0     |       0.952 |           0.905 |
| novelty | M3       |                 inf |             0 |     0.079 |   0.012 |       0.909 |           0.905 |
| novelty | M4       |                 inf |             0 |     0.071 |   0.004 |       0.925 |           0.905 |
| novelty | M5       |                 inf |             0 |     0.071 |   0.024 |       0.905 |           0.905 |
