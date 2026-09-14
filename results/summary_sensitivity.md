# Sensitivity and uncertainty (PMSG vs SCIG)

## (a) Null quantile in the SDR denominator

| machine | ftype | feature | median_sdr | share_detectable | min_detectable_pct | null_quantile |
|---|---|---|---|---|---|---|
| PMSG | TURNS | V2_V1 | 3.665 | 0.796 | 2.800 | 0.900 |
| PMSG | TURNS | I2_I1 | 2.005 | 0.648 | 2.800 | 0.900 |
| PMSG | TURNS | Id_2fe | 0.596 | 0.333 | 11.600 | 0.900 |
| PMSG | TURNS | PId_2fe | 0.593 | 0.333 | 11.600 | 0.900 |
| PMSG | TURNS | Vq_2fe | 1.601 | 0.648 | 7.400 | 0.900 |
| PMSG | WINDINGS | V2_V1 | 75.873 | 0.944 | 2.300 | 0.900 |
| PMSG | WINDINGS | I2_I1 | 15.424 | 0.870 | 3.200 | 0.900 |
| PMSG | WINDINGS | Id_2fe | 4.787 | 0.741 | 10.600 | 0.900 |
| PMSG | WINDINGS | PId_2fe | 4.816 | 0.741 | 10.600 | 0.900 |
| PMSG | WINDINGS | Vq_2fe | 26.635 | 0.907 | 2.300 | 0.900 |
| SCIG | TURNS | V2_V1 | 5.108 | 0.759 | 2.700 | 0.900 |
| SCIG | TURNS | I2_I1 | 5.831 | 0.787 | 2.800 | 0.900 |
| SCIG | TURNS | Id_2fe | 8.131 | 0.843 | 2.700 | 0.900 |
| SCIG | TURNS | PId_2fe | 8.161 | 0.843 | 2.700 | 0.900 |
| SCIG | TURNS | Vq_2fe | 3.158 | 0.639 | 7.400 | 0.900 |
| SCIG | WINDINGS | V2_V1 | 59.021 | 1.000 | 2.300 | 0.900 |
| SCIG | WINDINGS | I2_I1 | 71.658 | 1.000 | 2.300 | 0.900 |
| SCIG | WINDINGS | Id_2fe | 90.010 | 1.000 | 2.300 | 0.900 |
| SCIG | WINDINGS | PId_2fe | 90.350 | 1.000 | 2.300 | 0.900 |
| SCIG | WINDINGS | Vq_2fe | 30.395 | 0.954 | 2.300 | 0.900 |
| PMSG | TURNS | V2_V1 | 2.990 | 0.759 | 2.800 | 0.950 |
| PMSG | TURNS | I2_I1 | 1.471 | 0.565 | 7.400 | 0.950 |
| PMSG | TURNS | Id_2fe | 0.516 | 0.296 | 11.600 | 0.950 |
| PMSG | TURNS | PId_2fe | 0.518 | 0.306 | 11.600 | 0.950 |
| PMSG | TURNS | Vq_2fe | 1.346 | 0.574 | 7.400 | 0.950 |
| PMSG | WINDINGS | V2_V1 | 61.898 | 0.944 | 2.300 | 0.950 |
| PMSG | WINDINGS | I2_I1 | 11.316 | 0.815 | 9.700 | 0.950 |
| PMSG | WINDINGS | Id_2fe | 4.143 | 0.722 | 10.600 | 0.950 |
| PMSG | WINDINGS | PId_2fe | 4.206 | 0.722 | 10.600 | 0.950 |
| PMSG | WINDINGS | Vq_2fe | 22.398 | 0.898 | 2.300 | 0.950 |
| SCIG | TURNS | V2_V1 | 4.171 | 0.731 | 2.700 | 0.950 |
| SCIG | TURNS | I2_I1 | 4.525 | 0.750 | 2.800 | 0.950 |
| SCIG | TURNS | Id_2fe | 6.682 | 0.787 | 2.700 | 0.950 |
| SCIG | TURNS | PId_2fe | 6.685 | 0.778 | 2.700 | 0.950 |
| SCIG | TURNS | Vq_2fe | 2.577 | 0.602 | 7.400 | 0.950 |
| SCIG | WINDINGS | V2_V1 | 48.192 | 1.000 | 2.300 | 0.950 |
| SCIG | WINDINGS | I2_I1 | 55.608 | 1.000 | 2.300 | 0.950 |
| SCIG | WINDINGS | Id_2fe | 73.971 | 1.000 | 2.300 | 0.950 |
| SCIG | WINDINGS | PId_2fe | 74.013 | 1.000 | 2.300 | 0.950 |
| SCIG | WINDINGS | Vq_2fe | 24.800 | 0.917 | 2.300 | 0.950 |
| PMSG | TURNS | V2_V1 | 2.344 | 0.685 | 3.800 | 0.990 |
| PMSG | TURNS | I2_I1 | 1.206 | 0.519 | 7.400 | 0.990 |
| PMSG | TURNS | Id_2fe | 0.361 | 0.241 | 11.600 | 0.990 |
| PMSG | TURNS | PId_2fe | 0.356 | 0.241 | 11.600 | 0.990 |
| PMSG | TURNS | Vq_2fe | 1.004 | 0.500 | 7.400 | 0.990 |
| PMSG | WINDINGS | V2_V1 | 48.539 | 0.907 | 2.300 | 0.990 |
| PMSG | WINDINGS | I2_I1 | 9.277 | 0.787 | 9.700 | 0.990 |
| PMSG | WINDINGS | Id_2fe | 2.895 | 0.685 | 14.340 | 0.990 |
| PMSG | WINDINGS | PId_2fe | 2.891 | 0.685 | 14.340 | 0.990 |
| PMSG | WINDINGS | Vq_2fe | 16.711 | 0.861 | 9.700 | 0.990 |
| SCIG | TURNS | V2_V1 | 3.164 | 0.648 | 7.400 | 0.990 |
| SCIG | TURNS | I2_I1 | 3.406 | 0.676 | 7.400 | 0.990 |
| SCIG | TURNS | Id_2fe | 5.394 | 0.722 | 7.400 | 0.990 |
| SCIG | TURNS | PId_2fe | 5.403 | 0.722 | 7.400 | 0.990 |
| SCIG | TURNS | Vq_2fe | 1.792 | 0.593 | 7.400 | 0.990 |
| SCIG | WINDINGS | V2_V1 | 36.556 | 1.000 | 2.300 | 0.990 |
| SCIG | WINDINGS | I2_I1 | 41.860 | 0.972 | 2.300 | 0.990 |
| SCIG | WINDINGS | Id_2fe | 59.713 | 1.000 | 2.300 | 0.990 |
| SCIG | WINDINGS | PId_2fe | 59.814 | 1.000 | 2.300 | 0.990 |
| SCIG | WINDINGS | Vq_2fe | 17.250 | 0.843 | 9.700 | 0.990 |

## (b) Window length

| machine | ftype | feature | median_sdr | share_detectable | min_detectable_pct | window_cycles |
|---|---|---|---|---|---|---|
| PMSG | TURNS | V2_V1 | 2.495 | 0.731 | 2.800 | 3 |
| PMSG | TURNS | I2_I1 | 1.384 | 0.574 | 7.400 | 3 |
| PMSG | TURNS | Id_2fe | 0.571 | 0.287 | 11.600 | 3 |
| PMSG | TURNS | PId_2fe | 0.565 | 0.296 | 11.600 | 3 |
| PMSG | TURNS | Vq_2fe | 1.174 | 0.546 | 7.400 | 3 |
| PMSG | WINDINGS | V2_V1 | 51.480 | 0.917 | 2.300 | 3 |
| PMSG | WINDINGS | I2_I1 | 11.539 | 0.833 | 9.700 | 3 |
| PMSG | WINDINGS | Id_2fe | 4.587 | 0.713 | 10.600 | 3 |
| PMSG | WINDINGS | PId_2fe | 4.575 | 0.713 | 10.600 | 3 |
| PMSG | WINDINGS | Vq_2fe | 19.760 | 0.889 | 2.300 | 3 |
| SCIG | TURNS | V2_V1 | 3.134 | 0.694 | 7.400 | 3 |
| SCIG | TURNS | I2_I1 | 3.990 | 0.704 | 7.400 | 3 |
| SCIG | TURNS | Id_2fe | 6.525 | 0.778 | 2.800 | 3 |
| SCIG | TURNS | PId_2fe | 6.577 | 0.778 | 2.800 | 3 |
| SCIG | TURNS | Vq_2fe | 2.420 | 0.611 | 7.400 | 3 |
| SCIG | WINDINGS | V2_V1 | 40.673 | 1.000 | 2.300 | 3 |
| SCIG | WINDINGS | I2_I1 | 49.515 | 0.981 | 2.300 | 3 |
| SCIG | WINDINGS | Id_2fe | 73.008 | 1.000 | 2.300 | 3 |
| SCIG | WINDINGS | PId_2fe | 73.568 | 1.000 | 2.300 | 3 |
| SCIG | WINDINGS | Vq_2fe | 22.990 | 0.880 | 9.700 | 3 |
| PMSG | TURNS | V2_V1 | 2.990 | 0.759 | 2.800 | 5 |
| PMSG | TURNS | I2_I1 | 1.471 | 0.565 | 7.400 | 5 |
| PMSG | TURNS | Id_2fe | 0.516 | 0.296 | 11.600 | 5 |
| PMSG | TURNS | PId_2fe | 0.518 | 0.306 | 11.600 | 5 |
| PMSG | TURNS | Vq_2fe | 1.346 | 0.574 | 7.400 | 5 |
| PMSG | WINDINGS | V2_V1 | 61.898 | 0.944 | 2.300 | 5 |
| PMSG | WINDINGS | I2_I1 | 11.316 | 0.815 | 9.700 | 5 |
| PMSG | WINDINGS | Id_2fe | 4.143 | 0.722 | 10.600 | 5 |
| PMSG | WINDINGS | PId_2fe | 4.206 | 0.722 | 10.600 | 5 |
| PMSG | WINDINGS | Vq_2fe | 22.398 | 0.898 | 2.300 | 5 |
| SCIG | TURNS | V2_V1 | 4.171 | 0.731 | 2.700 | 5 |
| SCIG | TURNS | I2_I1 | 4.525 | 0.750 | 2.800 | 5 |
| SCIG | TURNS | Id_2fe | 6.682 | 0.787 | 2.700 | 5 |
| SCIG | TURNS | PId_2fe | 6.685 | 0.778 | 2.700 | 5 |
| SCIG | TURNS | Vq_2fe | 2.577 | 0.602 | 7.400 | 5 |
| SCIG | WINDINGS | V2_V1 | 48.192 | 1.000 | 2.300 | 5 |
| SCIG | WINDINGS | I2_I1 | 55.608 | 1.000 | 2.300 | 5 |
| SCIG | WINDINGS | Id_2fe | 73.971 | 1.000 | 2.300 | 5 |
| SCIG | WINDINGS | PId_2fe | 74.013 | 1.000 | 2.300 | 5 |
| SCIG | WINDINGS | Vq_2fe | 24.800 | 0.917 | 2.300 | 5 |
| PMSG | TURNS | V2_V1 | 3.219 | 0.731 | 2.800 | 8 |
| PMSG | TURNS | I2_I1 | 1.576 | 0.583 | 7.400 | 8 |
| PMSG | TURNS | Id_2fe | 0.437 | 0.278 | 11.600 | 8 |
| PMSG | TURNS | PId_2fe | 0.434 | 0.278 | 11.600 | 8 |
| PMSG | TURNS | Vq_2fe | 1.325 | 0.602 | 7.400 | 8 |
| PMSG | WINDINGS | V2_V1 | 66.037 | 0.935 | 2.300 | 8 |
| PMSG | WINDINGS | I2_I1 | 12.134 | 0.824 | 9.700 | 8 |
| PMSG | WINDINGS | Id_2fe | 3.430 | 0.694 | 10.600 | 8 |
| PMSG | WINDINGS | PId_2fe | 3.393 | 0.704 | 10.600 | 8 |
| PMSG | WINDINGS | Vq_2fe | 23.450 | 0.907 | 2.300 | 8 |
| SCIG | TURNS | V2_V1 | 4.688 | 0.750 | 2.700 | 8 |
| SCIG | TURNS | I2_I1 | 4.678 | 0.750 | 2.800 | 8 |
| SCIG | TURNS | Id_2fe | 7.604 | 0.833 | 2.700 | 8 |
| SCIG | TURNS | PId_2fe | 7.627 | 0.833 | 2.700 | 8 |
| SCIG | TURNS | Vq_2fe | 2.568 | 0.620 | 7.400 | 8 |
| SCIG | WINDINGS | V2_V1 | 51.279 | 1.000 | 2.300 | 8 |
| SCIG | WINDINGS | I2_I1 | 57.689 | 1.000 | 2.300 | 8 |
| SCIG | WINDINGS | Id_2fe | 81.701 | 1.000 | 2.300 | 8 |
| SCIG | WINDINGS | PId_2fe | 81.927 | 1.000 | 2.300 | 8 |
| SCIG | WINDINGS | Vq_2fe | 23.955 | 0.880 | 9.700 | 8 |

## (c) Bootstrap over recordings (2000 resamples, 95 % percentile intervals)

| ftype | feature | machine | median_sdr | median_sdr_ci_lo | median_sdr_ci_hi | share | share_ci_lo | share_ci_hi | mde | mde_ci_lo | mde_ci_hi | mde_undetectable_frac |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TURNS | V2_V1 | PMSG | 2.990 | 1.621 | 5.144 | 0.759 | 0.676 | 0.843 | 2.800 | 2.700 | 3.800 | 0.000 |
| TURNS | V2_V1 | SCIG | 4.171 | 1.977 | 6.612 | 0.731 | 0.648 | 0.815 | 2.700 | 2.700 | 7.400 | 0.000 |
| TURNS | V2_V1 | SCIG/PMSG ratio of medians | 1.321 | 0.523 | 2.867 | -0.027 | -0.139 | 0.083 |  |  |  |  |
| TURNS | I2_I1 | PMSG | 1.471 | 0.917 | 1.779 | 0.565 | 0.463 | 0.657 | 7.400 | 2.700 | 7.400 | 0.000 |
| TURNS | I2_I1 | SCIG | 4.525 | 2.235 | 6.007 | 0.750 | 0.667 | 0.833 | 2.800 | 2.700 | 7.400 | 0.000 |
| TURNS | I2_I1 | SCIG/PMSG ratio of medians | 3.101 | 1.601 | 5.589 | 0.184 | 0.056 | 0.315 |  |  |  |  |
| TURNS | Id_2fe | PMSG | 0.516 | 0.416 | 0.651 | 0.296 | 0.213 | 0.380 | 11.600 | 3.800 | 11.600 | 0.000 |
| TURNS | Id_2fe | SCIG | 6.682 | 2.619 | 10.197 | 0.787 | 0.713 | 0.861 | 2.700 | 2.700 | 7.400 | 0.000 |
| TURNS | Id_2fe | SCIG/PMSG ratio of medians | 12.606 | 4.997 | 20.637 | 0.491 | 0.370 | 0.602 |  |  |  |  |
| TURNS | PId_2fe | PMSG | 0.518 | 0.420 | 0.666 | 0.306 | 0.222 | 0.398 | 11.600 | 3.800 | 11.600 | 0.000 |
| TURNS | PId_2fe | SCIG | 6.685 | 2.851 | 10.266 | 0.778 | 0.704 | 0.852 | 2.700 | 2.700 | 7.400 | 0.000 |
| TURNS | PId_2fe | SCIG/PMSG ratio of medians | 12.486 | 5.239 | 20.835 | 0.471 | 0.361 | 0.583 |  |  |  |  |
| TURNS | Vq_2fe | PMSG | 1.346 | 0.969 | 2.439 | 0.574 | 0.481 | 0.667 | 7.400 | 2.800 | 7.690 | 0.000 |
| TURNS | Vq_2fe | SCIG | 2.577 | 1.536 | 3.482 | 0.602 | 0.509 | 0.694 | 7.400 | 7.400 | 7.400 | 0.000 |
| TURNS | Vq_2fe | SCIG/PMSG ratio of medians | 2.015 | 0.907 | 3.182 | 0.029 | -0.111 | 0.157 |  |  |  |  |
| WINDINGS | V2_V1 | PMSG | 61.898 | 35.543 | 91.274 | 0.944 | 0.898 | 0.981 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | V2_V1 | SCIG | 48.192 | 29.430 | 89.066 | 1.000 | 1.000 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | V2_V1 | SCIG/PMSG ratio of medians | 0.829 | 0.430 | 1.959 | 0.056 | 0.019 | 0.102 |  |  |  |  |
| WINDINGS | I2_I1 | PMSG | 11.316 | 3.951 | 22.161 | 0.815 | 0.741 | 0.889 | 9.700 | 2.300 | 9.700 | 0.000 |
| WINDINGS | I2_I1 | SCIG | 55.608 | 36.175 | 93.454 | 1.000 | 1.000 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | I2_I1 | SCIG/PMSG ratio of medians | 5.378 | 2.406 | 16.586 | 0.185 | 0.111 | 0.259 |  |  |  |  |
| WINDINGS | Id_2fe | PMSG | 4.143 | 2.488 | 6.916 | 0.722 | 0.639 | 0.806 | 10.600 | 3.200 | 14.340 | 0.000 |
| WINDINGS | Id_2fe | SCIG | 73.971 | 45.527 | 127.879 | 1.000 | 1.000 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | Id_2fe | SCIG/PMSG ratio of medians | 18.001 | 9.663 | 36.972 | 0.277 | 0.194 | 0.361 |  |  |  |  |
| WINDINGS | PId_2fe | PMSG | 4.206 | 2.506 | 7.013 | 0.722 | 0.639 | 0.806 | 10.600 | 3.200 | 14.340 | 0.000 |
| WINDINGS | PId_2fe | SCIG | 74.013 | 45.546 | 127.954 | 1.000 | 1.000 | 1.000 | 2.300 | 2.300 | 2.300 | 0.000 |
| WINDINGS | PId_2fe | SCIG/PMSG ratio of medians | 17.779 | 9.409 | 36.220 | 0.277 | 0.194 | 0.361 |  |  |  |  |
| WINDINGS | Vq_2fe | PMSG | 22.398 | 10.673 | 35.856 | 0.898 | 0.833 | 0.954 | 2.300 | 2.300 | 9.700 | 0.000 |
| WINDINGS | Vq_2fe | SCIG | 24.800 | 13.752 | 36.401 | 0.917 | 0.861 | 0.972 | 2.300 | 2.300 | 9.700 | 0.000 |
| WINDINGS | Vq_2fe | SCIG/PMSG ratio of medians | 1.068 | 0.514 | 2.443 | 0.017 | -0.056 | 0.093 |  |  |  |  |