# Three alternatives: PMSG, SCIG, WFSG (3-cycle windows, common features)

Recordings: {'PMSG': 225, 'SCIG': 225, 'WFSG': 618}; WFSG at all fault impedances (coverage: {('PHASE', 11.32): 72, ('PHASE', 33.96): 108, ('TURNS', 1.0): 63, ('TURNS', 2.83): 117, ('WINDINGS', 2.83): 81, ('WINDINGS', 5.66): 36, ('WINDINGS', 11.32): 141}).

## Null (95th percentile of |no-fault relative change|)

| feature | PMSG | SCIG | WFSG |
|---|---|---|---|
| V2_V1 | 0.095 | 0.037 | 0.036 |
| I2_I1 | 0.160 | 0.036 | 0.080 |
| Id_2fe | 0.444 | 0.015 | 0.158 |
| Vqconv_2fe | 0.166 | 0.038 | 0.085 |
| If_2fe |  |  | 0.339 |

## Fault current per tap pair (median over recordings)

| ('case', '') | ('ftype', '') | ('sev_pct', '') | ('Ifault_A', 'PMSG') | ('Ifault_A', 'SCIG') | ('Ifault_A', 'WFSG') | ('Ifault_over_I1', 'PMSG') | ('Ifault_over_I1', 'SCIG') | ('Ifault_over_I1', 'WFSG') |
|---|---|---|---|---|---|---|---|---|
| PHASE_D02_D09 | PHASE | 27.290 |  |  | 2.693 |  |  | 0.603 |
| PHASE_D02_D10 | PHASE | 30.090 |  |  | 2.894 |  |  | 0.649 |
| PHASE_D03_D09 | PHASE | 19.600 |  |  | 2.968 |  |  | 0.663 |
| PHASE_D03_D10 | PHASE | 22.400 |  |  | 3.136 |  |  | 0.703 |
| PHASE_D05_D23 | PHASE | 79.200 |  |  | 3.430 |  |  | 0.786 |
| PHASE_D05_D24 | PHASE | 82.000 |  |  | 3.529 |  |  | 0.794 |
| PHASE_D08_D23 | PHASE | 67.100 |  |  | 3.618 |  |  | 0.815 |
| PHASE_D08_D24 | PHASE | 69.900 |  |  | 3.667 |  |  | 0.834 |
| PHASE_D11_D17 | PHASE | 20.300 |  |  | 3.140 |  |  | 0.717 |
| PHASE_D11_D20 | PHASE | 31.900 |  |  | 3.461 |  |  | 0.790 |
| PHASE_D12_D17 | PHASE | 17.600 |  |  | 3.142 |  |  | 0.714 |
| PHASE_D12_D20 | PHASE | 29.200 |  |  | 3.491 |  |  | 0.782 |
| PHASE_D14_D21 | PHASE | 26.300 |  |  | 3.805 |  |  | 0.869 |
| PHASE_D14_D22 | PHASE | 30.100 |  |  | 3.915 |  |  | 0.889 |
| PHASE_D15_D21 | PHASE | 18.900 |  |  | 3.996 |  |  | 0.908 |
| PHASE_D15_D22 | PHASE | 22.700 |  |  | 3.985 |  |  | 0.908 |
| TURNS_D01_D04 | TURNS | 12.040 | 5.850 | 5.159 | 4.575 | 1.630 | 0.708 | 0.878 |
| TURNS_D02_D03 | TURNS | 7.690 | 3.683 | 3.370 | 3.209 | 1.028 | 0.460 | 0.713 |
| TURNS_D05_D08 | TURNS | 12.100 | 5.928 | 5.598 | 3.971 | 1.655 | 0.740 | 0.856 |
| TURNS_D06_D07 | TURNS | 7.400 | 3.673 | 3.330 | 3.275 | 1.020 | 0.450 | 0.662 |
| TURNS_D09_D10 | TURNS | 2.800 | 1.398 | 1.123 | 1.280 | 0.377 | 0.152 | 0.258 |
| TURNS_D11_D12 | TURNS | 2.700 | 1.409 | 1.131 | 1.277 | 0.388 | 0.152 | 0.258 |
| TURNS_D13_D16 | TURNS | 11.600 | 5.872 | 5.522 | 3.898 | 1.633 | 0.747 | 0.835 |
| TURNS_D14_D15 | TURNS | 7.400 | 3.698 | 3.286 | 4.128 | 1.030 | 0.441 | 0.930 |
| TURNS_D17_D20 | TURNS | 11.600 | 5.904 | 5.546 | 3.879 | 1.653 | 0.746 | 0.834 |
| TURNS_D18_D19 | TURNS | 7.400 | 3.674 | 3.307 | 3.211 | 1.017 | 0.445 | 0.729 |
| TURNS_D21_D22 | TURNS | 3.800 | 1.414 | 1.087 | 1.298 | 0.391 | 0.144 | 0.258 |
| TURNS_D23_D24 | TURNS | 2.800 | 1.406 | 1.087 | 1.282 | 0.393 | 0.143 | 0.257 |
| WINDINGS_D01_D06 | WINDINGS | 14.340 | 7.113 | 6.478 | 3.330 | 2.002 | 0.872 | 0.747 |
| WINDINGS_D01_D07 | WINDINGS | 21.740 | 10.352 | 9.469 | 4.734 | 2.874 | 1.275 | 1.071 |
| WINDINGS_D04_D06 | WINDINGS | 2.300 | 2.003 | 1.908 | 2.394 | 0.550 | 0.256 | 0.689 |
| WINDINGS_D04_D07 | WINDINGS | 9.700 | 4.699 | 4.507 | 4.197 | 1.287 | 0.605 | 0.917 |
| WINDINGS_D09_D23 | WINDINGS | 62.500 |  |  | 4.991 |  |  | 1.139 |
| WINDINGS_D09_D24 | WINDINGS | 65.300 |  |  | 5.195 |  |  | 1.188 |
| WINDINGS_D10_D23 | WINDINGS | 59.700 |  |  | 4.923 |  |  | 1.125 |
| WINDINGS_D10_D24 | WINDINGS | 62.500 |  |  | 4.965 |  |  | 1.100 |
| WINDINGS_D11_D21 | WINDINGS | 36.400 | 16.010 | 14.225 | 3.114 | 4.366 | 1.894 | 0.702 |
| WINDINGS_D11_D22 | WINDINGS | 40.200 | 17.111 | 14.910 | 3.340 | 4.706 | 2.007 | 0.750 |
| WINDINGS_D12_D21 | WINDINGS | 33.700 | 15.158 | 13.373 | 2.888 | 4.191 | 1.804 | 0.650 |
| WINDINGS_D12_D22 | WINDINGS | 37.500 | 16.190 | 14.179 | 3.114 | 4.511 | 1.912 | 0.699 |
| WINDINGS_D13_D18 | WINDINGS | 14.800 | 6.828 | 6.279 | 2.573 | 1.878 | 0.844 | 0.592 |
| WINDINGS_D13_D19 | WINDINGS | 22.200 | 9.812 | 8.928 | 3.833 | 2.714 | 1.210 | 0.875 |
| WINDINGS_D16_D18 | WINDINGS | 3.200 | 2.096 | 1.902 | 1.997 | 0.582 | 0.256 | 0.524 |
| WINDINGS_D16_D19 | WINDINGS | 10.600 | 4.884 | 4.422 | 2.912 | 1.333 | 0.591 | 0.773 |

## Per-feature SDR (top 6 per machine and fault type)

| machine | ftype | feature | group | n | median_sdr | frac_detectable | healthy_false_alarm |
|---|---|---|---|---|---|---|---|
| SCIG | WINDINGS | Id_2fe | dq / control | 108 | 73.008 | 1.000 | 0.222 |
| SCIG | WINDINGS | Vdconv_2fe | dq / control | 108 | 57.302 | 1.000 | 0.111 |
| PMSG | WINDINGS | V2_V1 | dq / control | 108 | 51.480 | 0.917 | 0.222 |
| SCIG | WINDINGS | D2_D1 | dq / control | 108 | 50.729 | 1.000 | 0.333 |
| SCIG | WINDINGS | I2_I1 | stator current | 108 | 49.515 | 0.981 | 0.000 |
| SCIG | WINDINGS | V2_V1 | dq / control | 108 | 40.673 | 1.000 | 0.222 |
| SCIG | WINDINGS | Vd_2fe | dq / control | 108 | 37.398 | 1.000 | 0.000 |
| WFSG | WINDINGS | Iq_2fe | dq / control | 258 | 32.990 | 1.000 |  |
| WFSG | WINDINGS | Vqconv_2fe | dq / control | 258 | 31.928 | 1.000 |  |
| PMSG | WINDINGS | D2_D1 | dq / control | 108 | 28.714 | 0.907 | 0.000 |
| WFSG | WINDINGS | D2_D1 | dq / control | 258 | 26.949 | 1.000 |  |
| WFSG | WINDINGS | Iq_std | dq / control | 258 | 24.261 | 0.953 |  |
| WFSG | WINDINGS | Ia_h3 | stator current | 258 | 21.842 | 0.996 |  |
| WFSG | WINDINGS | Vd_2fe | dq / control | 258 | 20.586 | 0.996 |  |
| PMSG | WINDINGS | Vq_2fe | dq / control | 108 | 19.760 | 0.889 | 0.000 |
| PMSG | WINDINGS | I2_I1 | stator current | 108 | 11.539 | 0.833 | 0.000 |
| WFSG | TURNS | V2_V1 | dq / control | 176 | 9.450 | 0.795 |  |
| WFSG | TURNS | Iq_2fe | dq / control | 176 | 7.272 | 0.824 |  |
| WFSG | TURNS | Vqconv_2fe | dq / control | 176 | 7.072 | 0.824 |  |
| SCIG | TURNS | Id_2fe | dq / control | 108 | 6.525 | 0.778 | 0.222 |
| WFSG | TURNS | I_unbal_rms | stator current | 176 | 5.605 | 0.801 |  |
| PMSG | WINDINGS | Vd_2fe | dq / control | 108 | 5.566 | 0.713 | 0.000 |
| SCIG | TURNS | Vdconv_2fe | dq / control | 108 | 5.538 | 0.731 | 0.111 |
| SCIG | TURNS | D2_D1 | dq / control | 108 | 5.482 | 0.778 | 0.333 |
| WFSG | TURNS | Vq_2fe | dq / control | 176 | 4.884 | 0.812 |  |
| PMSG | WINDINGS | Vqconv_2fe | dq / control | 108 | 4.762 | 0.759 | 0.000 |
| WFSG | TURNS | Ia_h3 | stator current | 176 | 4.720 | 0.824 |  |
| SCIG | TURNS | I2_I1 | stator current | 108 | 3.990 | 0.704 | 0.000 |
| SCIG | TURNS | Vqconv_2fe | dq / control | 108 | 3.574 | 0.657 | 0.222 |
| SCIG | TURNS | V2_V1 | dq / control | 108 | 3.134 | 0.694 | 0.222 |
| PMSG | TURNS | V2_V1 | dq / control | 108 | 2.495 | 0.731 | 0.222 |
| PMSG | TURNS | D2_D1 | dq / control | 108 | 2.370 | 0.648 | 0.000 |
| PMSG | TURNS | I2_I1 | stator current | 108 | 1.384 | 0.574 | 0.000 |
| PMSG | TURNS | Vq_2fe | dq / control | 108 | 1.174 | 0.546 | 0.000 |
| PMSG | TURNS | Vqconv_2fe | dq / control | 108 | 1.141 | 0.546 | 0.000 |
| PMSG | TURNS | Iq_2fe | dq / control | 108 | 0.907 | 0.463 | 0.000 |

## Sensor suites

| suite | machine | ftype | best_feature | n_trials | fixed_median_sdr | fixed_share_detectable | fixed_min_detectable_pct | smallest_extent_tested_pct | oracle_share_detectable | oracle_min_detectable_pct |
|---|---|---|---|---|---|---|---|---|---|---|
| drive-internal | PMSG | TURNS | D2_D1 | 108 | 2.370 | 0.648 | 7.400 | 2.700 | 0.806 | 2.700 |
| 3 CT | PMSG | TURNS | I2_I1 | 108 | 1.384 | 0.574 | 7.400 | 2.700 | 0.787 | 2.800 |
| 3 CT + 3 VT | PMSG | TURNS | I2_I1 | 108 | 1.384 | 0.574 | 7.400 | 2.700 | 0.787 | 2.800 |
| 3 CT + 3 VT + drive | PMSG | TURNS | D2_D1 | 108 | 2.370 | 0.648 | 7.400 | 2.700 | 0.917 | 2.700 |
| drive-internal | PMSG | WINDINGS | D2_D1 | 108 | 28.714 | 0.907 | 2.300 | 2.300 | 0.981 | 2.300 |
| 3 CT | PMSG | WINDINGS | I2_I1 | 108 | 11.539 | 0.833 | 9.700 | 2.300 | 0.991 | 2.300 |
| 3 CT + 3 VT | PMSG | WINDINGS | I2_I1 | 108 | 11.539 | 0.833 | 9.700 | 2.300 | 0.991 | 2.300 |
| 3 CT + 3 VT + drive | PMSG | WINDINGS | D2_D1 | 108 | 28.714 | 0.907 | 2.300 | 2.300 | 1.000 | 2.300 |
| drive-internal | SCIG | TURNS | Vdconv_2fe | 108 | 5.538 | 0.731 | 7.400 | 2.700 | 0.870 | 2.700 |
| 3 CT | SCIG | TURNS | I2_I1 | 108 | 3.990 | 0.704 | 7.400 | 2.700 | 0.815 | 2.800 |
| 3 CT + 3 VT | SCIG | TURNS | I2_I1 | 108 | 3.990 | 0.704 | 7.400 | 2.700 | 0.815 | 2.800 |
| 3 CT + 3 VT + drive | SCIG | TURNS | Vdconv_2fe | 108 | 5.538 | 0.731 | 7.400 | 2.700 | 0.944 | 2.700 |
| drive-internal | SCIG | WINDINGS | Vdconv_2fe | 108 | 57.302 | 1.000 | 2.300 | 2.300 | 1.000 | 2.300 |
| 3 CT | SCIG | WINDINGS | I2_I1 | 108 | 49.515 | 0.981 | 2.300 | 2.300 | 0.981 | 2.300 |
| 3 CT + 3 VT | SCIG | WINDINGS | I2_I1 | 108 | 49.515 | 0.981 | 2.300 | 2.300 | 0.981 | 2.300 |
| 3 CT + 3 VT + drive | SCIG | WINDINGS | Vdconv_2fe | 108 | 57.302 | 1.000 | 2.300 | 2.300 | 1.000 | 2.300 |
| drive-internal | WFSG | TURNS | Iq_2fe | 180 | 7.272 | 0.806 | 11.600 | 11.600 | 0.967 | 11.600 |
| 3 CT | WFSG | TURNS | I_unbal_rms | 180 | 5.605 | 0.783 | 11.600 | 11.600 | 0.944 | 11.600 |
| 3 CT + 3 VT | WFSG | TURNS | V2_V1 | 180 | 9.450 | 0.778 | 11.600 | 11.600 | 0.950 | 11.600 |
| 3 CT + 3 VT + drive | WFSG | TURNS | V2_V1 | 180 | 9.450 | 0.778 | 11.600 | 11.600 | 0.978 | 11.600 |
| excitation (WFSG only) | WFSG | TURNS | If_2fe | 180 | 3.649 | 0.700 | 11.600 | 11.600 | 0.761 | 11.600 |
| drive-internal | WFSG | WINDINGS | Iq_2fe | 258 | 32.990 | 1.000 | 2.300 | 2.300 | 1.000 | 2.300 |
| 3 CT | WFSG | WINDINGS | Ia_h3 | 258 | 21.842 | 0.996 | 2.300 | 2.300 | 1.000 | 2.300 |
| 3 CT + 3 VT | WFSG | WINDINGS | Ia_h3 | 258 | 21.842 | 0.996 | 2.300 | 2.300 | 1.000 | 2.300 |
| 3 CT + 3 VT + drive | WFSG | WINDINGS | Iq_2fe | 258 | 32.990 | 1.000 | 2.300 | 2.300 | 1.000 | 2.300 |
| excitation (WFSG only) | WFSG | WINDINGS | If_2fe | 258 | 14.238 | 1.000 | 2.300 | 2.300 | 1.000 | 2.300 |

## Transfer (self-ref |z|, GBDT; 73601 windows, 8685 positives)

| train | test | auc | tpr_at_1pct_fpr |
|---|---|---|---|
| PMSG | PMSG | 0.875 | 0.646 |
| SCIG | SCIG | 0.921 | 0.773 |
| WFSG | WFSG | 0.989 | 0.957 |
| PMSG | SCIG | 0.895 | 0.592 |
| PMSG | WFSG | 0.983 | 0.942 |
| SCIG | PMSG | 0.810 | 0.336 |
| SCIG | WFSG | 0.971 | 0.915 |
| WFSG | PMSG | 0.858 | 0.559 |
| WFSG | SCIG | 0.914 | 0.676 |
| SCIG+WFSG | PMSG | 0.842 | 0.417 |
| PMSG+WFSG | SCIG | 0.900 | 0.626 |
| PMSG+SCIG | WFSG | 0.982 | 0.936 |

![G1](figures/G_sdr_by_feature_3alt.png)
![G2](figures/G_sdr_vs_severity_3alt.png)
![G3](figures/G_sensor_suites_3alt.png)
![G4](figures/G_transfer_3alt.png)
