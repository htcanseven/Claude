# In-line verifiability from the force record

Gradient boosting {'max_depth': 3, 'max_iter': 200, 'learning_rate': 0.08, 'random_state': 0}; ridge alpha 1.0; 5-fold GroupKFold over production batches of 50.

| qc            | label                     | unit   |    n |   r2_oof |   r2_oof_linear |   sd_within |   sd_error |    lod |   lod_over_sd |   recall_top5_at_fa5 |
|:--------------|:--------------------------|:-------|-----:|---------:|----------------:|------------:|-----------:|-------:|--------------:|---------------------:|
| drawin_mid    | Draw-in at mid-sides      | mm     | 8867 |   0.0651 |          0.0307 |      0.057  |     0.0366 | 0.1206 |        2.1143 |               0.1446 |
| drawin_corner | Draw-in at corners        | mm     | 8867 |   0.025  |          0.0296 |      0.0244 |     0.0242 | 0.0797 |        3.2645 |               0.1031 |
| waviness      | Flange waviness           | mm     | 8867 |   0.0187 |          0.0067 |      0.0019 |     0.0019 | 0.0061 |        3.2051 |               0.1883 |
| wall_op10     | Wall angle after drawing  | deg    | 8867 |  -0.0166 |         -0.0003 |      0.0693 |     0.0692 | 0.2276 |        3.2832 |               0.0583 |
| arm_op20      | Arm angle after cutting   | deg    | 8867 |   0.0012 |         -0.0135 |      0.0836 |     0.0821 | 0.2701 |        3.2325 |               0.1413 |
| depth_op10    | Cup depth                 | mm     | 8867 |   0.1727 |          0.1095 |      0.0056 |     0.0054 | 0.0178 |        3.1842 |               0.2242 |
| dome_op20     | Bottom dome after cutting | mm     | 8867 |   0.1012 |          0.0797 |      0.0033 |     0.0033 | 0.0108 |        3.2558 |               0.1659 |

## Batch level: drift explained by the signals (ridge alpha 10.0, folds by alternative)

| qc            |   n_batches |   r2_oof_batch |   floor |   floor_drift_removed |   floor_reduction |
|:--------------|------------:|---------------:|--------:|----------------------:|------------------:|
| drawin_mid    |         177 |         0.1967 |  0.051  |                0.0464 |            0.0889 |
| drawin_corner |         177 |         0.0652 |  0.0468 |                0.0448 |            0.0431 |
| waviness      |         177 |        -0.1537 |  0.0028 |                0.003  |           -0.0557 |
| wall_op10     |         177 |        -0.1196 |  0.0764 |                0.0858 |           -0.1234 |
| arm_op20      |         177 |        -0.2332 |  0.1088 |                0.1212 |           -0.114  |
| depth_op10    |         177 |         0.1114 |  0.0109 |                0.0092 |            0.1631 |
| dome_op20     |         177 |         0.1045 |  0.007  |                0.0063 |            0.1036 |
