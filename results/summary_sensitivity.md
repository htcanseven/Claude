# Sensitivity and uncertainty (PMSG vs SCIG)

## (a) Null quantile in the SDR denominator

| machine | ftype | feature | median_sdr | share_detectable | min_detectable_pct | healthy_false_alarms | screened | null_quantile |
|---|---|---|---|---|---|---|---|---|
| PMSG | TURNS | V2_V1 | 3.665 | 0.796 | 3.800 | 1 | False | 0.900 |
| PMSG | TURNS | I2_I1 | 2.005 | 0.648 | 7.400 | 2 | False | 0.900 |
| PMSG | TURNS | Id_2fe | 0.596 | 0.333 | 12.100 | 2 | False | 0.900 |
| PMSG | TURNS | PId_2fe | 0.593 | 0.333 | 12.100 | 2 | False | 0.900 |
| PMSG | TURNS | Vq_2fe | 1.601 | 0.648 | 7.400 | 1 | False | 0.900 |
| PMSG | WINDINGS | V2_V1 | 75.873 | 0.944 | 2.300 | 1 | False | 0.900 |
| PMSG | WINDINGS | I2_I1 | 15.424 | 0.870 | 3.200 | 2 | False | 0.900 |
| PMSG | WINDINGS | Id_2fe | 4.787 | 0.741 | 21.700 | 2 | False | 0.900 |
| PMSG | WINDINGS | PId_2fe | 4.816 | 0.741 | 21.700 | 2 | False | 0.900 |
| PMSG | WINDINGS | Vq_2fe | 26.635 | 0.907 | 9.700 | 1 | False | 0.900 |
| SCIG | TURNS | V2_V1 | 5.108 | 0.759 | 7.400 | 1 | False | 0.900 |
| SCIG | TURNS | I2_I1 | 5.831 | 0.787 | 7.400 | 1 | False | 0.900 |
| SCIG | TURNS | Id_2fe | 8.131 | 0.843 | 7.400 | 2 | False | 0.900 |
| SCIG | TURNS | PId_2fe | 8.161 | 0.843 | 7.400 | 2 | False | 0.900 |
| SCIG | TURNS | Vq_2fe | 3.158 | 0.639 | 7.400 | 2 | False | 0.900 |
| SCIG | WINDINGS | V2_V1 | 59.021 | 1.000 | 2.300 | 1 | False | 0.900 |
| SCIG | WINDINGS | I2_I1 | 71.658 | 1.000 | 2.300 | 1 | False | 0.900 |
| SCIG | WINDINGS | Id_2fe | 90.010 | 1.000 | 2.300 | 2 | False | 0.900 |
| SCIG | WINDINGS | PId_2fe | 90.350 | 1.000 | 2.300 | 2 | False | 0.900 |
| SCIG | WINDINGS | Vq_2fe | 30.395 | 0.954 | 9.700 | 2 | False | 0.900 |
| PMSG | TURNS | V2_V1 | 2.990 | 0.759 | 3.800 | 1 | False | 0.950 |
| PMSG | TURNS | I2_I1 | 1.471 | 0.565 | 7.400 | 0 | False | 0.950 |
| PMSG | TURNS | Id_2fe | 0.516 | 0.296 | 12.100 | 1 | False | 0.950 |
| PMSG | TURNS | PId_2fe | 0.518 | 0.306 | 12.100 | 1 | False | 0.950 |
| PMSG | TURNS | Vq_2fe | 1.346 | 0.574 | 7.400 | 0 | False | 0.950 |
| PMSG | WINDINGS | V2_V1 | 61.898 | 0.944 | 2.300 | 1 | False | 0.950 |
| PMSG | WINDINGS | I2_I1 | 11.316 | 0.815 | 9.700 | 0 | False | 0.950 |
| PMSG | WINDINGS | Id_2fe | 4.143 | 0.722 | 21.700 | 1 | False | 0.950 |
| PMSG | WINDINGS | PId_2fe | 4.206 | 0.722 | 21.700 | 1 | False | 0.950 |
| PMSG | WINDINGS | Vq_2fe | 22.398 | 0.898 | 9.700 | 0 | False | 0.950 |
| SCIG | TURNS | V2_V1 | 4.171 | 0.731 | 7.400 | 0 | False | 0.950 |
| SCIG | TURNS | I2_I1 | 4.525 | 0.750 | 7.400 | 1 | False | 0.950 |
| SCIG | TURNS | Id_2fe | 6.682 | 0.787 | 7.400 | 1 | False | 0.950 |
| SCIG | TURNS | PId_2fe | 6.685 | 0.778 | 7.400 | 1 | False | 0.950 |
| SCIG | TURNS | Vq_2fe | 2.577 | 0.602 | 7.400 | 1 | False | 0.950 |
| SCIG | WINDINGS | V2_V1 | 48.192 | 1.000 | 2.300 | 0 | False | 0.950 |
| SCIG | WINDINGS | I2_I1 | 55.608 | 1.000 | 2.300 | 1 | False | 0.950 |
| SCIG | WINDINGS | Id_2fe | 73.971 | 1.000 | 2.300 | 1 | False | 0.950 |
| SCIG | WINDINGS | PId_2fe | 74.013 | 1.000 | 2.300 | 1 | False | 0.950 |
| SCIG | WINDINGS | Vq_2fe | 24.800 | 0.917 | 9.700 | 1 | False | 0.950 |
| PMSG | TURNS | V2_V1 | 2.344 | 0.685 | 3.800 | 0 | False | 0.990 |
| PMSG | TURNS | I2_I1 | 1.206 | 0.519 | 7.400 | 0 | False | 0.990 |
| PMSG | TURNS | Id_2fe | 0.361 | 0.241 | 12.100 | 0 | False | 0.990 |
| PMSG | TURNS | PId_2fe | 0.356 | 0.241 | 12.100 | 0 | False | 0.990 |
| PMSG | TURNS | Vq_2fe | 1.004 | 0.500 | 7.700 | 0 | False | 0.990 |
| PMSG | WINDINGS | V2_V1 | 48.539 | 0.907 | 9.700 | 0 | False | 0.990 |
| PMSG | WINDINGS | I2_I1 | 9.277 | 0.787 | 9.700 | 0 | False | 0.990 |
| PMSG | WINDINGS | Id_2fe | 2.895 | 0.685 | 21.700 | 0 | False | 0.990 |
| PMSG | WINDINGS | PId_2fe | 2.891 | 0.685 | 21.700 | 0 | False | 0.990 |
| PMSG | WINDINGS | Vq_2fe | 16.711 | 0.861 | 9.700 | 0 | False | 0.990 |
| SCIG | TURNS | V2_V1 | 3.164 | 0.648 | 7.400 | 0 | False | 0.990 |
| SCIG | TURNS | I2_I1 | 3.406 | 0.676 | 7.400 | 0 | False | 0.990 |
| SCIG | TURNS | Id_2fe | 5.394 | 0.722 | 7.400 | 1 | False | 0.990 |
| SCIG | TURNS | PId_2fe | 5.403 | 0.722 | 7.400 | 1 | False | 0.990 |
| SCIG | TURNS | Vq_2fe | 1.792 | 0.593 | 7.400 | 1 | False | 0.990 |
| SCIG | WINDINGS | V2_V1 | 36.556 | 1.000 | 2.300 | 0 | False | 0.990 |
| SCIG | WINDINGS | I2_I1 | 41.860 | 0.972 | 2.300 | 0 | False | 0.990 |
| SCIG | WINDINGS | Id_2fe | 59.713 | 1.000 | 2.300 | 1 | False | 0.990 |
| SCIG | WINDINGS | PId_2fe | 59.814 | 1.000 | 2.300 | 1 | False | 0.990 |
| SCIG | WINDINGS | Vq_2fe | 17.250 | 0.843 | 9.700 | 1 | False | 0.990 |

## (b) Window length

| machine | ftype | feature | median_sdr | share_detectable | min_detectable_pct | healthy_false_alarms | screened | window_cycles |
|---|---|---|---|---|---|---|---|---|
| PMSG | TURNS | V2_V1 | 2.495 | 0.731 | 3.800 | 2 | False | 3 |
| PMSG | TURNS | I2_I1 | 1.384 | 0.574 | 7.400 | 0 | False | 3 |
| PMSG | TURNS | Id_2fe | 0.571 | 0.287 | 12.100 | 0 | False | 3 |
| PMSG | TURNS | PId_2fe | 0.565 | 0.296 | 12.100 | 0 | False | 3 |
| PMSG | TURNS | Vq_2fe | 1.174 | 0.546 | 7.400 | 0 | False | 3 |
| PMSG | WINDINGS | V2_V1 | 51.480 | 0.917 | 9.700 | 2 | False | 3 |
| PMSG | WINDINGS | I2_I1 | 11.539 | 0.833 | 9.700 | 0 | False | 3 |
| PMSG | WINDINGS | Id_2fe | 4.587 | 0.713 | 21.700 | 0 | False | 3 |
| PMSG | WINDINGS | PId_2fe | 4.575 | 0.713 | 21.700 | 0 | False | 3 |
| PMSG | WINDINGS | Vq_2fe | 19.760 | 0.889 | 9.700 | 0 | False | 3 |
| SCIG | TURNS | V2_V1 | 3.134 | 0.694 | 7.400 | 2 | False | 3 |
| SCIG | TURNS | I2_I1 | 3.990 | 0.704 | 7.400 | 0 | False | 3 |
| SCIG | TURNS | Id_2fe | 6.525 | 0.778 | 7.400 | 2 | False | 3 |
| SCIG | TURNS | PId_2fe | 6.577 | 0.778 | 7.400 | 2 | False | 3 |
| SCIG | TURNS | Vq_2fe | 2.420 | 0.611 | 7.400 | 1 | False | 3 |
| SCIG | WINDINGS | V2_V1 | 40.673 | 1.000 | 2.300 | 2 | False | 3 |
| SCIG | WINDINGS | I2_I1 | 49.515 | 0.981 | 2.300 | 0 | False | 3 |
| SCIG | WINDINGS | Id_2fe | 73.008 | 1.000 | 2.300 | 2 | False | 3 |
| SCIG | WINDINGS | PId_2fe | 73.568 | 1.000 | 2.300 | 2 | False | 3 |
| SCIG | WINDINGS | Vq_2fe | 22.990 | 0.880 | 9.700 | 1 | False | 3 |
| PMSG | TURNS | V2_V1 | 2.990 | 0.759 | 3.800 | 1 | False | 5 |
| PMSG | TURNS | I2_I1 | 1.471 | 0.565 | 7.400 | 0 | False | 5 |
| PMSG | TURNS | Id_2fe | 0.516 | 0.296 | 12.100 | 1 | False | 5 |
| PMSG | TURNS | PId_2fe | 0.518 | 0.306 | 12.100 | 1 | False | 5 |
| PMSG | TURNS | Vq_2fe | 1.346 | 0.574 | 7.400 | 0 | False | 5 |
| PMSG | WINDINGS | V2_V1 | 61.898 | 0.944 | 2.300 | 1 | False | 5 |
| PMSG | WINDINGS | I2_I1 | 11.316 | 0.815 | 9.700 | 0 | False | 5 |
| PMSG | WINDINGS | Id_2fe | 4.143 | 0.722 | 21.700 | 1 | False | 5 |
| PMSG | WINDINGS | PId_2fe | 4.206 | 0.722 | 21.700 | 1 | False | 5 |
| PMSG | WINDINGS | Vq_2fe | 22.398 | 0.898 | 9.700 | 0 | False | 5 |
| SCIG | TURNS | V2_V1 | 4.171 | 0.731 | 7.400 | 0 | False | 5 |
| SCIG | TURNS | I2_I1 | 4.525 | 0.750 | 7.400 | 1 | False | 5 |
| SCIG | TURNS | Id_2fe | 6.682 | 0.787 | 7.400 | 1 | False | 5 |
| SCIG | TURNS | PId_2fe | 6.685 | 0.778 | 7.400 | 1 | False | 5 |
| SCIG | TURNS | Vq_2fe | 2.577 | 0.602 | 7.400 | 1 | False | 5 |
| SCIG | WINDINGS | V2_V1 | 48.192 | 1.000 | 2.300 | 0 | False | 5 |
| SCIG | WINDINGS | I2_I1 | 55.608 | 1.000 | 2.300 | 1 | False | 5 |
| SCIG | WINDINGS | Id_2fe | 73.971 | 1.000 | 2.300 | 1 | False | 5 |
| SCIG | WINDINGS | PId_2fe | 74.013 | 1.000 | 2.300 | 1 | False | 5 |
| SCIG | WINDINGS | Vq_2fe | 24.800 | 0.917 | 9.700 | 1 | False | 5 |
| PMSG | TURNS | V2_V1 | 3.219 | 0.731 | 3.800 | 1 | False | 8 |
| PMSG | TURNS | I2_I1 | 1.576 | 0.583 | 7.400 | 0 | False | 8 |
| PMSG | TURNS | Id_2fe | 0.437 | 0.278 | 12.100 | 1 | False | 8 |
| PMSG | TURNS | PId_2fe | 0.434 | 0.278 | 12.100 | 1 | False | 8 |
| PMSG | TURNS | Vq_2fe | 1.325 | 0.602 | 7.400 | 0 | False | 8 |
| PMSG | WINDINGS | V2_V1 | 66.037 | 0.935 | 2.300 | 1 | False | 8 |
| PMSG | WINDINGS | I2_I1 | 12.134 | 0.824 | 9.700 | 0 | False | 8 |
| PMSG | WINDINGS | Id_2fe | 3.430 | 0.694 | 21.700 | 1 | False | 8 |
| PMSG | WINDINGS | PId_2fe | 3.393 | 0.704 | 21.700 | 1 | False | 8 |
| PMSG | WINDINGS | Vq_2fe | 23.450 | 0.907 | 9.700 | 0 | False | 8 |
| SCIG | TURNS | V2_V1 | 4.688 | 0.750 | 7.400 | 0 | False | 8 |
| SCIG | TURNS | I2_I1 | 4.678 | 0.750 | 7.400 | 1 | False | 8 |
| SCIG | TURNS | Id_2fe | 7.604 | 0.833 | 7.400 | 1 | False | 8 |
| SCIG | TURNS | PId_2fe | 7.627 | 0.833 | 7.400 | 1 | False | 8 |
| SCIG | TURNS | Vq_2fe | 2.568 | 0.620 | 7.400 | 1 | False | 8 |
| SCIG | WINDINGS | V2_V1 | 51.279 | 1.000 | 2.300 | 0 | False | 8 |
| SCIG | WINDINGS | I2_I1 | 57.689 | 1.000 | 2.300 | 1 | False | 8 |
| SCIG | WINDINGS | Id_2fe | 81.701 | 1.000 | 2.300 | 1 | False | 8 |
| SCIG | WINDINGS | PId_2fe | 81.927 | 1.000 | 2.300 | 1 | False | 8 |
| SCIG | WINDINGS | Vq_2fe | 23.955 | 0.880 | 9.700 | 1 | False | 8 |

## (c) Bootstrap over recordings (2000 resamples, 95 % percentile intervals)

| ftype | feature | machine | median_sdr | median_sdr_ci_lo | median_sdr_ci_hi | share | share_ci_lo | share_ci_hi | share_wilson_lo | share_wilson_hi | mde | mde_ci_lo | mde_ci_hi | mde_undetectable_frac |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TURNS | V2_V1 | PMSG | 2.990 | 1.215 | 12.543 | 0.759 | 0.546 | 0.935 | 0.671 | 0.830 | 3.800 | 2.800 | 3.800 | 0.000 |
| TURNS | V2_V1 | SCIG | 4.171 | 0.949 | 15.505 | 0.731 | 0.491 | 0.926 | 0.641 | 0.806 | 7.400 | 7.400 | 7.400 | 0.000 |
| TURNS | V2_V1 | SCIG/PMSG ratio of medians | 1.104 | 0.378 | 4.560 | -0.030 | -0.278 | 0.167 |  |  |  |  |  |  |
| TURNS | I2_I1 | PMSG | 1.471 | 0.601 | 2.364 | 0.565 | 0.361 | 0.741 | 0.471 | 0.655 | 7.400 | 7.400 | 12.100 | 0.000 |
| TURNS | I2_I1 | SCIG | 4.525 | 1.113 | 11.658 | 0.750 | 0.546 | 0.907 | 0.661 | 0.822 | 7.400 | 7.400 | 7.400 | 0.000 |
| TURNS | I2_I1 | SCIG/PMSG ratio of medians | 3.068 | 1.336 | 5.633 | 0.184 | 0.083 | 0.287 |  |  |  |  |  |  |
| TURNS | Id_2fe | PMSG | 0.516 | 0.390 | 1.094 | 0.296 | 0.111 | 0.509 | 0.218 | 0.388 | 12.100 | 11.600 | 12.100 | 0.002 |
| TURNS | Id_2fe | SCIG | 6.682 | 1.302 | 18.252 | 0.787 | 0.602 | 0.935 | 0.701 | 0.854 | 7.400 | 3.800 | 7.400 | 0.000 |
| TURNS | Id_2fe | SCIG/PMSG ratio of medians | 11.954 | 2.629 | 29.610 | 0.488 | 0.287 | 0.676 |  |  |  |  |  |  |
| TURNS | PId_2fe | PMSG | 0.518 | 0.389 | 1.109 | 0.306 | 0.111 | 0.528 | 0.227 | 0.398 | 12.100 | 11.600 | 12.100 | 0.002 |
| TURNS | PId_2fe | SCIG | 6.685 | 1.304 | 18.258 | 0.778 | 0.583 | 0.926 | 0.691 | 0.846 | 7.400 | 3.800 | 7.400 | 0.000 |
| TURNS | PId_2fe | SCIG/PMSG ratio of medians | 11.759 | 2.587 | 28.839 | 0.470 | 0.269 | 0.667 |  |  |  |  |  |  |
| TURNS | Vq_2fe | PMSG | 1.346 | 0.791 | 4.578 | 0.574 | 0.361 | 0.769 | 0.480 | 0.663 | 7.400 | 7.400 | 11.600 | 0.000 |
| TURNS | Vq_2fe | SCIG | 2.577 | 0.516 | 5.330 | 0.602 | 0.343 | 0.843 | 0.508 | 0.689 | 7.400 | 7.400 | 7.700 | 0.000 |
| TURNS | Vq_2fe | SCIG/PMSG ratio of medians | 1.489 | 0.464 | 3.206 | 0.027 | -0.167 | 0.213 |  |  |  |  |  |  |
| WINDINGS | V2_V1 | PMSG | 61.898 | 9.243 | 181.107 | 0.944 | 0.870 | 1.000 | 0.884 | 0.974 | 2.300 | 2.300 | 14.300 | 0.000 |
| WINDINGS | V2_V1 | SCIG | 48.192 | 15.277 | 187.698 | 1.000 | 1.000 | 1.000 | 0.966 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | V2_V1 | SCIG/PMSG ratio of medians | 0.974 | 0.696 | 1.684 | 0.056 | 0.000 | 0.130 |  |  |  |  |  |  |
| WINDINGS | I2_I1 | PMSG | 11.316 | 1.978 | 64.261 | 0.815 | 0.639 | 0.944 | 0.731 | 0.877 | 9.700 | 9.538 | 21.700 | 0.000 |
| WINDINGS | I2_I1 | SCIG | 55.608 | 12.502 | 117.001 | 1.000 | 1.000 | 1.000 | 0.966 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | I2_I1 | SCIG/PMSG ratio of medians | 5.494 | 1.751 | 13.129 | 0.187 | 0.056 | 0.361 |  |  |  |  |  |  |
| WINDINGS | Id_2fe | PMSG | 4.143 | 1.164 | 12.718 | 0.722 | 0.528 | 0.907 | 0.631 | 0.798 | 21.700 | 9.700 | 21.700 | 0.000 |
| WINDINGS | Id_2fe | SCIG | 73.971 | 22.924 | 245.222 | 1.000 | 1.000 | 1.000 | 0.966 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | Id_2fe | SCIG/PMSG ratio of medians | 18.508 | 12.425 | 27.525 | 0.281 | 0.093 | 0.472 |  |  |  |  |  |  |
| WINDINGS | PId_2fe | PMSG | 4.206 | 1.179 | 12.997 | 0.722 | 0.528 | 0.907 | 0.631 | 0.798 | 21.700 | 9.700 | 21.700 | 0.000 |
| WINDINGS | PId_2fe | SCIG | 74.013 | 22.938 | 245.459 | 1.000 | 1.000 | 1.000 | 0.966 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | PId_2fe | SCIG/PMSG ratio of medians | 18.243 | 12.272 | 27.223 | 0.281 | 0.093 | 0.472 |  |  |  |  |  |  |
| WINDINGS | Vq_2fe | PMSG | 22.398 | 3.243 | 61.975 | 0.898 | 0.787 | 0.981 | 0.827 | 0.942 | 9.700 | 2.300 | 14.300 | 0.000 |
| WINDINGS | Vq_2fe | SCIG | 24.800 | 7.043 | 78.594 | 0.917 | 0.805 | 1.000 | 0.849 | 0.956 | 9.700 | 2.300 | 9.700 | 0.000 |
| WINDINGS | Vq_2fe | SCIG/PMSG ratio of medians | 1.130 | 0.831 | 1.897 | 0.020 | -0.019 | 0.065 |  |  |  |  |  |  |