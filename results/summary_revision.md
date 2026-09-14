# Revision re-analyses

## R9 null exceedance by speed (pooled q95, 5-cycle windows)

| machine | speed_rpm | V2_V1 | I2_I1 | Id_2fe | PId_2fe | Vq_2fe | n |
|---|---|---|---|---|---|---|---|
| PMSG | 1200 | 0.040 | 0.013 | 0.027 | 0.027 | 0.013 | 75 |
| PMSG | 1500 | 0.053 | 0.133 | 0.067 | 0.067 | 0.107 | 75 |
| PMSG | 1800 | 0.067 | 0.013 | 0.067 | 0.067 | 0.040 | 75 |
| SCIG | 1200 | 0.120 | 0.000 | 0.093 | 0.093 | 0.107 | 75 |
| SCIG | 1500 | 0.040 | 0.000 | 0.067 | 0.067 | 0.053 | 75 |
| SCIG | 1800 | 0.000 | 0.160 | 0.000 | 0.000 | 0.000 | 75 |

## R10 PMSG vs SCIG feature-ranking similarity (5-cycle windows)

| ftype | n_features | spearman | top5_PMSG | top5_SCIG |
|---|---|---|---|---|
| TURNS | 30 | 0.697 | V2_V1, D2_D1, PIq_2fe, I2_I1, Vq_2fe | D2_D1, PId_2fe, Id_2fe, Vdconv_2fe, I2_I1 |
| WINDINGS | 30 | 0.887 | V2_V1, D2_D1, Vq_2fe, I2_I1, PIq_2fe | D2_D1, PId_2fe, Id_2fe, Vdconv_2fe, I2_I1 |

## R11 WFSG fault windows per trial (3-cycle windows)

| speed_rpm | n_trials | fe0_Hz | n_flt_median | n_flt_min | trials_without_fault_window | trials_below_3_windows |
|---|---|---|---|---|---|---|
| 716.000 | 46.000 | 23.870 | 3.000 | 0.000 | 3.000 | 3.000 |
| 955.000 | 46.000 | 31.830 | 5.000 | 0.000 | 1.000 | 1.000 |
| 1432.000 | 46.000 | 47.750 | 4.000 | 2.000 | 0.000 | 1.000 |
| 1671.000 | 50.000 | 55.700 | 2.000 | 2.000 | 0.000 | 50.000 |
| 1800.000 | 206.000 | 60.000 | 3.000 | 2.000 | 0.000 | 26.000 |
| 1910.000 | 44.000 | 63.660 | 3.000 | 3.000 | 0.000 | 0.000 |
## R6 healthy baselines and incremental negative-sequence impedance dV2/dI2 (RMS units)

| machine | ftype | n | I2_I1_pre | V2_V1_pre | D2_D1_pre | I1_pre_A_rms | I2_pre_A_rms | dI2_A_rms | dV2_V_rms | dV2_dI2_ohm | dV2_dI2_q25 | dV2_dI2_q75 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PMSG | TURNS | 108 | 0.005 | 0.001 | 0.001 | 2.567 | 0.015 | -0.000 | -0.000 | 7.925 | -2.073 | 16.544 |
| PMSG | WINDINGS | 108 | 0.005 | 0.001 | 0.001 | 2.571 | 0.015 | 0.020 | 0.455 | 15.400 | 10.895 | 18.029 |
| SCIG | TURNS | 108 | 0.008 | 0.002 | 0.004 | 5.253 | 0.043 | 0.001 | 0.006 | 6.687 | 3.997 | 7.898 |
| SCIG | WINDINGS | 108 | 0.008 | 0.002 | 0.004 | 5.253 | 0.041 | 0.059 | 0.397 | 7.040 | 6.588 | 7.535 |
| WFSG | TURNS | 117 | 0.015 | 0.007 | 0.004 | 2.158 | 0.043 | 0.003 | -0.069 | 17.328 | 11.832 | 64.161 |
| WFSG | WINDINGS | 81 | 0.015 | 0.007 | 0.004 | 2.172 | 0.045 | 0.027 | 0.296 | 10.626 | 9.661 | 12.848 |

## R7 within-trial vs commissioning-baseline (between-trial) null, PMSG/SCIG, 5-cycle windows

| machine | ftype | feature | q95_within | q95_between | median_sdr_within | ds_within | median_sdr_between | ds_between |
|---|---|---|---|---|---|---|---|---|
| PMSG | TURNS | V2_V1 | 0.086 | 0.315 | 2.990 | 0.759 | 1.052 | 0.500 |
| PMSG | TURNS | I2_I1 | 0.162 | 0.268 | 1.471 | 0.565 | 0.978 | 0.481 |
| PMSG | TURNS | Id_2fe | 0.563 | 0.876 | 0.516 | 0.296 | 0.441 | 0.204 |
| PMSG | TURNS | PId_2fe | 0.557 | 0.870 | 0.518 | 0.306 | 0.441 | 0.204 |
| PMSG | TURNS | Vq_2fe | 0.165 | 0.277 | 1.346 | 0.574 | 0.872 | 0.444 |
| PMSG | TURNS | D2_D1 | 0.090 | 0.211 | 2.779 | 0.639 | 1.109 | 0.519 |
| PMSG | WINDINGS | V2_V1 | 0.086 | 0.315 | 61.898 | 0.944 | 12.508 | 0.833 |
| PMSG | WINDINGS | I2_I1 | 0.162 | 0.268 | 11.316 | 0.815 | 6.343 | 0.750 |
| PMSG | WINDINGS | Id_2fe | 0.563 | 0.876 | 4.143 | 0.722 | 2.398 | 0.667 |
| PMSG | WINDINGS | PId_2fe | 0.557 | 0.870 | 4.206 | 0.722 | 2.404 | 0.667 |
| PMSG | WINDINGS | Vq_2fe | 0.165 | 0.277 | 22.398 | 0.898 | 10.742 | 0.815 |
| PMSG | WINDINGS | D2_D1 | 0.090 | 0.211 | 32.629 | 0.898 | 11.904 | 0.852 |
| SCIG | TURNS | V2_V1 | 0.033 | 0.111 | 4.171 | 0.731 | 1.448 | 0.593 |
| SCIG | TURNS | I2_I1 | 0.034 | 0.130 | 4.525 | 0.750 | 1.148 | 0.537 |
| SCIG | TURNS | Id_2fe | 0.016 | 0.078 | 6.682 | 0.787 | 1.290 | 0.528 |
| SCIG | TURNS | PId_2fe | 0.016 | 0.078 | 6.685 | 0.778 | 1.290 | 0.528 |
| SCIG | TURNS | Vq_2fe | 0.060 | 0.131 | 2.577 | 0.602 | 1.536 | 0.583 |
| SCIG | TURNS | D2_D1 | 0.010 | 0.068 | 11.062 | 0.815 | 1.565 | 0.519 |
| SCIG | WINDINGS | V2_V1 | 0.033 | 0.111 | 48.192 | 1.000 | 16.081 | 0.944 |
| SCIG | WINDINGS | I2_I1 | 0.034 | 0.130 | 55.608 | 1.000 | 12.869 | 0.861 |
| SCIG | WINDINGS | Id_2fe | 0.016 | 0.078 | 73.971 | 1.000 | 15.968 | 0.880 |
| SCIG | WINDINGS | PId_2fe | 0.016 | 0.078 | 74.013 | 1.000 | 15.978 | 0.880 |
| SCIG | WINDINGS | Vq_2fe | 0.060 | 0.131 | 24.800 | 0.917 | 11.202 | 0.861 |
| SCIG | WINDINGS | D2_D1 | 0.010 | 0.068 | 84.887 | 1.000 | 12.177 | 0.824 |

## R8 relative vs absolute change: feature ranking

| machine | ftype | spearman_rank_corr | top3_relative | top3_absolute | ds_top_relative | ds_top_absolute |
|---|---|---|---|---|---|---|
| PMSG | TURNS | 0.920 | V2_V1, D2_D1, PIq_2fe | V2_V1, D2_D1, PIq_2fe | 0.759 | 0.769 |
| PMSG | WINDINGS | 0.981 | V2_V1, D2_D1, Vq_2fe | V2_V1, D2_D1, Vq_2fe | 0.944 | 0.926 |
| SCIG | TURNS | 0.970 | D2_D1, PId_2fe, Id_2fe | D2_D1, PId_2fe, Id_2fe | 0.815 | 0.806 |
| SCIG | WINDINGS | 0.978 | D2_D1, PId_2fe, Id_2fe | D2_D1, Id_2fe, PId_2fe | 1.000 | 1.000 |
## R1 cheapest suite per requirement (bootstrap verdicts: meets P>=0.95, fails P<=0.05)

| alpha | e_req_pct | machine | ftype | cheapest_meets | cheapest_meets_feature | cheapest_not_failing | n_uncertain |
|---|---|---|---|---|---|---|---|
| 0.900 | 3 | PMSG | TURNS | none |  | 3 CT + 3 VT | 2 |
| 0.900 | 3 | PMSG | WINDINGS | none |  | drive-internal | 3 |
| 0.900 | 3 | SCIG | TURNS | none |  | none | 0 |
| 0.900 | 3 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.900 | 3 | WFSG | TURNS | none |  | none | 0 |
| 0.900 | 3 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 5 | PMSG | TURNS | 3 CT + 3 VT | V2_V1 | drive-internal | 1 |
| 0.900 | 5 | PMSG | WINDINGS | none |  | drive-internal | 4 |
| 0.900 | 5 | SCIG | TURNS | none |  | none | 0 |
| 0.900 | 5 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.900 | 5 | WFSG | TURNS | none |  | none | 0 |
| 0.900 | 5 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 8 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 1 |
| 0.900 | 8 | PMSG | WINDINGS | none |  | drive-internal | 4 |
| 0.900 | 8 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.900 | 8 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.900 | 8 | WFSG | TURNS | none |  | none | 0 |
| 0.900 | 8 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 12 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 0 |
| 0.900 | 12 | PMSG | WINDINGS | 3 CT | I2_I1 | drive-internal | 1 |
| 0.900 | 12 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.900 | 12 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.900 | 12 | WFSG | TURNS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 12 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 3 | PMSG | TURNS | none |  | 3 CT + 3 VT | 1 |
| 0.950 | 3 | PMSG | WINDINGS | none |  | drive-internal | 3 |
| 0.950 | 3 | SCIG | TURNS | none |  | none | 0 |
| 0.950 | 3 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.950 | 3 | WFSG | TURNS | none |  | none | 0 |
| 0.950 | 3 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 5 | PMSG | TURNS | none |  | drive-internal | 3 |
| 0.950 | 5 | PMSG | WINDINGS | none |  | drive-internal | 3 |
| 0.950 | 5 | SCIG | TURNS | none |  | none | 0 |
| 0.950 | 5 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.950 | 5 | WFSG | TURNS | none |  | none | 0 |
| 0.950 | 5 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 8 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 1 |
| 0.950 | 8 | PMSG | WINDINGS | none |  | drive-internal | 3 |
| 0.950 | 8 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.950 | 8 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.950 | 8 | WFSG | TURNS | none |  | none | 0 |
| 0.950 | 8 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 12 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 0 |
| 0.950 | 12 | PMSG | WINDINGS | 3 CT | I2_I1 | drive-internal | 3 |
| 0.950 | 12 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.950 | 12 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.950 | 12 | WFSG | TURNS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 12 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.990 | 3 | PMSG | TURNS | none |  | none | 0 |
| 0.990 | 3 | PMSG | WINDINGS | none |  | none | 0 |
| 0.990 | 3 | SCIG | TURNS | none |  | none | 0 |
| 0.990 | 3 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 2 |
| 0.990 | 3 | WFSG | TURNS | none |  | none | 0 |
| 0.990 | 3 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.990 | 5 | PMSG | TURNS | none |  | 3 CT + 3 VT | 2 |
| 0.990 | 5 | PMSG | WINDINGS | none |  | none | 0 |
| 0.990 | 5 | SCIG | TURNS | none |  | none | 0 |
| 0.990 | 5 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 5 | WFSG | TURNS | none |  | none | 0 |
| 0.990 | 5 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.990 | 8 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 3 |
| 0.990 | 8 | PMSG | WINDINGS | none |  | none | 0 |
| 0.990 | 8 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 8 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 8 | WFSG | TURNS | none |  | none | 0 |
| 0.990 | 8 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.990 | 12 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 0 |
| 0.990 | 12 | PMSG | WINDINGS | none |  | drive-internal | 4 |
| 0.990 | 12 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 12 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 12 | WFSG | TURNS | drive-internal | Vqconv_2fe | drive-internal | 0 |
| 0.990 | 12 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |

## R1 full decision table (alpha = 0.95)

| e_req_pct | machine | ftype | suite | cost_rank | fixed_feature | mde_monotone_pct | mde_ci_lo | mde_ci_hi | p_meets | verdict | ds_conditional | ds_all | smallest_extent_tested_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.700 | 0.000 | fails | 0.815 | 0.648 | 2.700 |
| 5 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.700 | 0.350 | uncertain | 0.861 | 0.648 | 2.700 |
| 8 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.700 | 1.000 | meets | 0.972 | 0.648 | 2.700 |
| 12 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.700 | 1.000 | meets | 1.000 | 0.648 | 2.700 |
| 3 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.000 | fails | 0.728 | 0.574 | 2.700 |
| 5 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.001 | fails | 0.806 | 0.574 | 2.700 |
| 8 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.932 | uncertain | 0.889 | 0.574 | 2.700 |
| 12 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.962 | meets | 0.889 | 0.574 | 2.700 |
| 3 | PMSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 3.800 | 2.800 | 11.600 | 0.051 | uncertain | 0.877 | 0.731 | 2.700 |
| 5 | PMSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 3.800 | 2.800 | 11.600 | 0.942 | uncertain | 0.889 | 0.731 | 2.700 |
| 8 | PMSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 3.800 | 2.800 | 11.600 | 0.970 | meets | 0.972 | 0.731 | 2.700 |
| 12 | PMSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 3.800 | 2.800 | 11.600 | 1.000 | meets | 1.000 | 0.731 | 2.700 |
| 3 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 3.800 | 2.800 | 11.600 | 0.037 | fails | 0.877 | 0.731 | 2.700 |
| 5 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 3.800 | 2.800 | 11.600 | 0.939 | uncertain | 0.889 | 0.731 | 2.700 |
| 8 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 3.800 | 2.800 | 11.600 | 0.973 | meets | 0.972 | 0.731 | 2.700 |
| 12 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 3.800 | 2.800 | 11.600 | 1.000 | meets | 1.000 | 0.731 | 2.700 |
| 3 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.300 | 2.300 | 14.300 | 0.123 | uncertain | 0.909 | 0.907 | 2.300 |
| 5 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.300 | 2.300 | 14.300 | 0.123 | uncertain | 0.933 | 0.907 | 2.300 |
| 8 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.300 | 2.300 | 14.300 | 0.123 | uncertain | 0.933 | 0.907 | 2.300 |
| 12 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.300 | 2.300 | 14.300 | 0.137 | uncertain | 1.000 | 0.907 | 2.300 |
| 3 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.300 | 0.000 | fails | 0.889 | 0.833 | 2.300 |
| 5 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.300 | 0.029 | fails | 0.956 | 0.833 | 2.300 |
| 8 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.300 | 0.029 | fails | 0.956 | 0.833 | 2.300 |
| 12 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.300 | 0.965 | meets | 0.986 | 0.833 | 2.300 |
| 3 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.109 | uncertain | 0.909 | 0.917 | 2.300 |
| 5 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.109 | uncertain | 0.967 | 0.917 | 2.300 |
| 8 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.109 | uncertain | 0.967 | 0.917 | 2.300 |
| 12 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.872 | uncertain | 1.000 | 0.917 | 2.300 |
| 3 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.128 | uncertain | 0.909 | 0.917 | 2.300 |
| 5 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.128 | uncertain | 0.967 | 0.917 | 2.300 |
| 8 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.128 | uncertain | 0.967 | 0.917 | 2.300 |
| 12 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | V2_V1 | 9.700 | 2.300 | 14.300 | 0.870 | uncertain | 1.000 | 0.917 | 2.300 |
| 3 | SCIG | TURNS | drive-internal | 0 | Id_2fe | 7.400 | 3.800 | 7.400 | 0.005 | fails | 0.889 | 0.778 | 2.700 |
| 5 | SCIG | TURNS | drive-internal | 0 | Id_2fe | 7.400 | 3.800 | 7.400 | 0.034 | fails | 0.972 | 0.778 | 2.700 |
| 8 | SCIG | TURNS | drive-internal | 0 | Id_2fe | 7.400 | 3.800 | 7.400 | 1.000 | meets | 0.972 | 0.778 | 2.700 |
| 12 | SCIG | TURNS | drive-internal | 0 | Id_2fe | 7.400 | 3.800 | 7.400 | 1.000 | meets | 1.000 | 0.778 | 2.700 |
| 3 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 7.400 | 0.000 | fails | 0.815 | 0.704 | 2.700 |
| 5 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 7.400 | 0.000 | fails | 0.917 | 0.704 | 2.700 |
| 8 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 7.400 | 1.000 | meets | 0.944 | 0.704 | 2.700 |
| 12 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 7.400 | 1.000 | meets | 1.000 | 0.704 | 2.700 |
| 3 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 7.400 | 0.000 | fails | 0.815 | 0.704 | 2.700 |
| 5 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 7.400 | 0.000 | fails | 0.917 | 0.704 | 2.700 |
| 8 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 7.400 | 1.000 | meets | 0.944 | 0.704 | 2.700 |
| 12 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 7.400 | 1.000 | meets | 1.000 | 0.704 | 2.700 |
| 3 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Id_2fe | 7.400 | 3.800 | 7.400 | 0.007 | fails | 0.889 | 0.778 | 2.700 |
| 5 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Id_2fe | 7.400 | 3.800 | 7.400 | 0.026 | fails | 0.972 | 0.778 | 2.700 |
| 8 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Id_2fe | 7.400 | 3.800 | 7.400 | 1.000 | meets | 0.972 | 0.778 | 2.700 |
| 12 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Id_2fe | 7.400 | 3.800 | 7.400 | 1.000 | meets | 1.000 | 0.778 | 2.700 |
| 3 | SCIG | WINDINGS | drive-internal | 0 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | SCIG | WINDINGS | drive-internal | 0 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | SCIG | WINDINGS | drive-internal | 0 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | SCIG | WINDINGS | drive-internal | 0 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 3 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 0.972 | meets | 1.000 | 0.981 | 2.300 |
| 5 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 8 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 12 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 3 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 2.322 | 0.975 | meets | 1.000 | 0.981 | 2.300 |
| 5 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 2.322 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 8 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 2.322 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 12 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 2.322 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 3 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Id_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 3 | WFSG | TURNS | drive-internal | 0 | Iq_2fe | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.906 | 0.906 | 11.600 |
| 5 | WFSG | TURNS | drive-internal | 0 | Iq_2fe | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.906 | 0.906 | 11.600 |
| 8 | WFSG | TURNS | drive-internal | 0 | Iq_2fe | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.906 | 0.906 | 11.600 |
| 12 | WFSG | TURNS | drive-internal | 0 | Iq_2fe | 11.600 | 11.600 | 11.600 | 1.000 | meets | 0.921 | 0.906 | 11.600 |
| 3 | WFSG | TURNS | 3 CT | 1 | Ia_h3 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 5 | WFSG | TURNS | 3 CT | 1 | Ia_h3 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 8 | WFSG | TURNS | 3 CT | 1 | Ia_h3 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 12 | WFSG | TURNS | 3 CT | 1 | Ia_h3 | 11.600 | 11.600 | 11.600 | 1.000 | meets | 0.968 | 0.983 | 11.600 |
| 3 | WFSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 5 | WFSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 8 | WFSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 12 | WFSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 11.600 | 11.600 | 11.600 | 1.000 | meets | 0.968 | 0.983 | 11.600 |
| 3 | WFSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 5 | WFSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 8 | WFSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.983 | 0.983 | 11.600 |
| 12 | WFSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 11.600 | 11.600 | 11.600 | 1.000 | meets | 0.968 | 0.983 | 11.600 |
| 3 | WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.863 | 0.863 | 11.600 |
| 5 | WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.863 | 0.863 | 11.600 |
| 8 | WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 11.600 | 11.600 | 11.600 | 0.000 | fails | 0.863 | 0.863 | 11.600 |
| 12 | WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 11.600 | 11.600 | 11.600 | 1.000 | meets | 0.857 | 0.863 | 11.600 |
| 3 | WFSG | WINDINGS | drive-internal | 0 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | WFSG | WINDINGS | drive-internal | 0 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | WFSG | WINDINGS | drive-internal | 0 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | WFSG | WINDINGS | drive-internal | 0 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets |  | 1.000 | 2.300 |
| 3 | WFSG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | WFSG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | WFSG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | WFSG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 2.300 | 1.000 | meets |  | 1.000 | 2.300 |
| 3 | WFSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | WFSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | WFSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | WFSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 2.300 | 2.300 | 2.300 | 1.000 | meets |  | 1.000 | 2.300 |
| 3 | WFSG | WINDINGS | 3 CT + 3 VT + drive | 3 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | WFSG | WINDINGS | 3 CT + 3 VT + drive | 3 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | WFSG | WINDINGS | 3 CT + 3 VT + drive | 3 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | WFSG | WINDINGS | 3 CT + 3 VT + drive | 3 | Iq_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets |  | 1.000 | 2.300 |
| 3 | WFSG | WINDINGS | excitation (WFSG only) | 0 | If_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | WFSG | WINDINGS | excitation (WFSG only) | 0 | If_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | WFSG | WINDINGS | excitation (WFSG only) | 0 | If_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | WFSG | WINDINGS | excitation (WFSG only) | 0 | If_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets |  | 1.000 | 2.300 |

## R2 requirement-writable quantities (alpha = 0.95, 3-cycle windows)

| machine | ftype | suite | cost_rank | fixed_feature | n_candidates | mde_first_pct | mde_monotone_pct | ds_all | ds_ge_5pct | ds_ge_8pct | ds_nested | smallest_extent_tested_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PMSG | TURNS | drive-internal | 0 | D2_D1 | 14 | 7.400 | 7.400 | 0.648 | 0.861 | 0.972 | 0.648 | 2.700 |
| PMSG | TURNS | 3 CT | 1 | I2_I1 | 6 | 7.400 | 7.400 | 0.574 | 0.806 | 0.889 | 0.574 | 2.700 |
| PMSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 7 | 3.800 | 3.800 | 0.731 | 0.889 | 0.972 | 0.731 | 2.700 |
| PMSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 23 | 3.800 | 3.800 | 0.731 | 0.889 | 0.972 | 0.676 | 2.700 |
| PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14 | 14.300 | 14.300 | 0.907 | 0.933 | 0.933 | 0.907 | 2.300 |
| PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 6 | 9.700 | 9.700 | 0.833 | 0.956 | 0.956 | 0.833 | 2.300 |
| PMSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 7 | 9.700 | 9.700 | 0.917 | 0.967 | 0.967 | 0.917 | 2.300 |
| PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | V2_V1 | 23 | 9.700 | 9.700 | 0.917 | 0.967 | 0.967 | 0.917 | 2.300 |
| SCIG | TURNS | drive-internal | 0 | Id_2fe | 13 | 7.400 | 7.400 | 0.778 | 0.972 | 0.972 | 0.778 | 2.700 |
| SCIG | TURNS | 3 CT | 1 | I2_I1 | 6 | 7.400 | 7.400 | 0.704 | 0.917 | 0.944 | 0.704 | 2.700 |
| SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7 | 7.400 | 7.400 | 0.704 | 0.917 | 0.944 | 0.704 | 2.700 |
| SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Id_2fe | 22 | 7.400 | 7.400 | 0.778 | 0.972 | 0.972 | 0.778 | 2.700 |
| SCIG | WINDINGS | drive-internal | 0 | Id_2fe | 13 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 6 | 2.300 | 2.300 | 0.981 | 1.000 | 1.000 | 0.981 | 2.300 |
| SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 7 | 2.300 | 2.300 | 0.981 | 1.000 | 1.000 | 0.981 | 2.300 |
| SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Id_2fe | 22 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | TURNS | drive-internal | 0 | Iq_2fe | 13 | 11.600 | 11.600 | 0.906 | 0.906 | 0.906 | 0.872 | 11.600 |
| WFSG | TURNS | 3 CT | 1 | Ia_h3 | 6 | 11.600 | 11.600 | 0.983 | 0.983 | 0.983 | 0.863 | 11.600 |
| WFSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 7 | 11.600 | 11.600 | 0.983 | 0.983 | 0.983 | 0.983 | 11.600 |
| WFSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 22 | 11.600 | 11.600 | 0.983 | 0.983 | 0.983 | 0.983 | 11.600 |
| WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 2 | 11.600 | 11.600 | 0.863 | 0.863 | 0.863 | 0.863 | 11.600 |
| WFSG | WINDINGS | drive-internal | 0 | Iq_2fe | 13 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | 3 CT | 1 | I2_I1 | 6 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 7 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | 3 CT + 3 VT + drive | 3 | Iq_2fe | 22 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | excitation (WFSG only) | 0 | If_2fe | 2 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |

## R3 SCIG / PMSG ratio decomposition (5-cycle windows)

| ftype | feature | abs_delta_median_PMSG | q95_PMSG | sdr_median_PMSG | abs_delta_median_SCIG | q95_SCIG | sdr_median_SCIG | ratio_sdr | ratio_numerator | ratio_denominator |
|---|---|---|---|---|---|---|---|---|---|---|
| TURNS | V2_V1 | 0.257 | 0.086 | 2.990 | 0.136 | 0.033 | 4.171 | 1.395 | 0.529 | 2.639 |
| TURNS | I2_I1 | 0.238 | 0.162 | 1.471 | 0.152 | 0.034 | 4.525 | 3.075 | 0.638 | 4.820 |
| TURNS | Id_2fe | 0.291 | 0.564 | 0.516 | 0.107 | 0.016 | 6.682 | 12.946 | 0.369 | 35.092 |
| TURNS | PId_2fe | 0.289 | 0.557 | 0.518 | 0.107 | 0.016 | 6.685 | 12.909 | 0.372 | 34.708 |
| TURNS | Vq_2fe | 0.222 | 0.165 | 1.346 | 0.155 | 0.060 | 2.577 | 1.914 | 0.701 | 2.732 |
| TURNS | Vqconv_2fe | 0.197 | 0.162 | 1.221 | 0.139 | 0.039 | 3.592 | 2.943 | 0.706 | 4.167 |
| TURNS | D2_D1 | 0.251 | 0.090 | 2.779 | 0.111 | 0.010 | 11.062 | 3.981 | 0.444 | 8.958 |
| WINDINGS | V2_V1 | 5.318 | 0.086 | 61.898 | 1.569 | 0.033 | 48.192 | 0.779 | 0.295 | 2.639 |
| WINDINGS | I2_I1 | 1.833 | 0.162 | 11.316 | 1.869 | 0.034 | 55.608 | 4.914 | 1.020 | 4.820 |
| WINDINGS | Id_2fe | 2.335 | 0.564 | 4.143 | 1.188 | 0.016 | 73.971 | 17.853 | 0.509 | 35.092 |
| WINDINGS | PId_2fe | 2.344 | 0.557 | 4.206 | 1.188 | 0.016 | 74.013 | 17.599 | 0.507 | 34.708 |
| WINDINGS | Vq_2fe | 3.688 | 0.165 | 22.398 | 1.495 | 0.060 | 24.800 | 1.107 | 0.405 | 2.732 |
| WINDINGS | Vqconv_2fe | 0.845 | 0.162 | 5.232 | 1.184 | 0.039 | 30.536 | 5.836 | 1.401 | 4.167 |
| WINDINGS | D2_D1 | 2.942 | 0.090 | 32.630 | 0.854 | 0.010 | 84.887 | 2.602 | 0.290 | 8.958 |

## R4 transfer, three alternatives (self-ref, GBDT): all negatives vs out-of-reference negatives

| train | test | auc_all | tpr_all | auc_oor | tpr_oor | fpr_healthy_flt_at_1pct | n_healthy_flt |
|---|---|---|---|---|---|---|---|
| PMSG | PMSG | 0.861 | 0.630 | 0.853 | 0.623 | 0.028 | 141 |
| SCIG | SCIG | 0.915 | 0.765 | 0.907 | 0.762 | 0.007 | 140 |
| WFSG | WFSG | 0.974 | 0.929 | 0.973 | 0.927 |  | 0 |
| PMSG | SCIG | 0.883 | 0.618 | 0.877 | 0.600 | 0.000 | 140 |
| PMSG | WFSG | 0.974 | 0.903 | 0.976 | 0.894 |  | 0 |
| SCIG | PMSG | 0.813 | 0.363 | 0.800 | 0.346 | 0.000 | 141 |
| SCIG | WFSG | 0.951 | 0.869 | 0.956 | 0.862 |  | 0 |
| WFSG | PMSG | 0.858 | 0.533 | 0.844 | 0.519 | 0.007 | 141 |
| WFSG | SCIG | 0.909 | 0.621 | 0.895 | 0.612 | 0.000 | 140 |
| SCIG+WFSG | PMSG | 0.842 | 0.431 | 0.828 | 0.414 | 0.000 | 141 |
| PMSG+WFSG | SCIG | 0.886 | 0.629 | 0.878 | 0.615 | 0.000 | 140 |
| PMSG+SCIG | WFSG | 0.971 | 0.893 | 0.974 | 0.883 |  | 0 |


| machine | n_windows | n_pos | n_oor | n_healthy_flt |
|---|---|---|---|---|
| PMSG | 24554 | 3391 | 20804 | 141 |
| SCIG | 24176 | 3355 | 20501 | 140 |
| WFSG | 17668 | 1362 | 11978 | 0 |

## R4 transfer, PMSG/SCIG (5-cycle windows)

| calibration | model | train | test | auc_all | tpr_all | auc_oor | tpr_oor | fpr_healthy_flt_at_1pct | n_healthy_flt |
|---|---|---|---|---|---|---|---|---|---|
| raw | logistic | PMSG | PMSG | 0.775 | 0.549 | 0.776 | 0.546 | 0.000 | 123 |
| raw | logistic | SCIG | SCIG | 0.794 | 0.577 | 0.797 | 0.576 | 0.000 | 122 |
| raw | logistic | PMSG | SCIG | 0.713 | 0.409 | 0.711 | 0.405 | 0.000 | 122 |
| raw | logistic | SCIG | PMSG | 0.592 | 0.254 | 0.594 | 0.255 | 0.000 | 123 |
| raw | gbdt | PMSG | PMSG | 0.876 | 0.604 | 0.873 | 0.602 | 0.000 | 123 |
| raw | gbdt | SCIG | SCIG | 0.903 | 0.627 | 0.906 | 0.628 | 0.000 | 122 |
| raw | gbdt | PMSG | SCIG | 0.783 | 0.466 | 0.783 | 0.466 | 0.000 | 122 |
| raw | gbdt | SCIG | PMSG | 0.551 | 0.236 | 0.552 | 0.234 | 0.000 | 123 |
| healthy-z | logistic | PMSG | PMSG | 0.775 | 0.549 | 0.776 | 0.546 | 0.000 | 123 |
| healthy-z | logistic | SCIG | SCIG | 0.794 | 0.577 | 0.797 | 0.576 | 0.000 | 122 |
| healthy-z | logistic | PMSG | SCIG | 0.707 | 0.424 | 0.706 | 0.424 | 0.000 | 122 |
| healthy-z | logistic | SCIG | PMSG | 0.443 | 0.085 | 0.447 | 0.086 | 0.000 | 123 |
| healthy-z | gbdt | PMSG | PMSG | 0.876 | 0.604 | 0.873 | 0.602 | 0.000 | 123 |
| healthy-z | gbdt | SCIG | SCIG | 0.903 | 0.627 | 0.906 | 0.628 | 0.000 | 122 |
| healthy-z | gbdt | PMSG | SCIG | 0.815 | 0.207 | 0.815 | 0.207 | 0.000 | 122 |
| healthy-z | gbdt | SCIG | PMSG | 0.745 | 0.302 | 0.746 | 0.304 | 0.016 | 123 |
| self-ref | logistic | PMSG | PMSG | 0.902 | 0.709 | 0.894 | 0.705 | 0.000 | 123 |
| self-ref | logistic | SCIG | SCIG | 0.938 | 0.801 | 0.932 | 0.799 | 0.000 | 122 |
| self-ref | logistic | PMSG | SCIG | 0.896 | 0.666 | 0.892 | 0.657 | 0.000 | 122 |
| self-ref | logistic | SCIG | PMSG | 0.881 | 0.602 | 0.871 | 0.592 | 0.000 | 123 |
| self-ref | gbdt | PMSG | PMSG | 0.918 | 0.737 | 0.910 | 0.728 | 0.033 | 123 |
| self-ref | gbdt | SCIG | SCIG | 0.945 | 0.811 | 0.939 | 0.809 | 0.016 | 122 |
| self-ref | gbdt | PMSG | SCIG | 0.918 | 0.739 | 0.910 | 0.725 | 0.000 | 122 |
| self-ref | gbdt | SCIG | PMSG | 0.857 | 0.433 | 0.840 | 0.418 | 0.000 | 123 |

## R5 features failing the reliability screen (> 1 of 9 healthy trials)

| window_cycles | machine | feature | healthy_false_alarm | n_false |
|---|---|---|---|---|
| 3 | SCIG | D2_D1 | 0.333 | 3 |
| 5 | PMSG | Id_1fe | 0.333 | 3 |
| 5 | PMSG | Spd_std | 0.444 | 4 |
| 5 | SCIG | Ia_h7 | 0.333 | 3 |
| 5 | SCIG | D2_D1 | 0.444 | 4 |
| 8 | PMSG | PId_std | 0.333 | 3 |
| 8 | PMSG | Spd_std | 0.444 | 4 |
| 8 | SCIG | Iq_2fe | 0.444 | 4 |
| 8 | SCIG | D2_D1 | 0.556 | 5 |
| 8 | SCIG | Vdc_std | 0.444 | 4 |