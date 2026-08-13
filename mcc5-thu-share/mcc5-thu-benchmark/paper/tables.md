# Generated tables

Source: 7 result file(s), 264 rows.

In T1 the `folds` column matters: models were not all run over the same number of condition folds, and folds differ in difficulty by up to 0.35 accuracy (T5). Compare models using T1b, which intersects the fold sets first.

## T1. Protocol x model (plain features)

| protocol | model | accuracy | macro_f1 | folds | seeds |
| --- | --- | --- | --- | --- | --- |
| leaky_random | cnn | 0.939 | 0.939 | 1 | 1 |
| leaky_random | rf | 0.975 ± 0.000 | 0.976 ± 0.000 | 1 | 3 |
| leaky_random | svm | 0.964 | 0.965 | 1 | 1 |
| in_condition | cnn | 0.913 | 0.911 | 1 | 1 |
| in_condition | rf | 0.965 ± 0.000 | 0.964 ± 0.000 | 1 | 3 |
| in_condition | svm | 0.955 | 0.954 | 1 | 1 |
| unknown_condition | cnn | 0.883 ± 0.051 | 0.861 ± 0.056 | 3 | 1 |
| unknown_condition | rf | 0.939 ± 0.024 | 0.931 ± 0.033 | 12 | 3 |
| unknown_condition | svm | 0.947 ± 0.027 | 0.942 ± 0.034 | 12 | 1 |
| cross_profile | cnn | 0.810 ± 0.134 | 0.811 ± 0.127 | 2 | 1 |
| cross_profile | rf | 0.839 ± 0.115 | 0.843 ± 0.110 | 2 | 3 |
| cross_profile | svm | 0.874 ± 0.114 | 0.882 ± 0.102 | 2 | 1 |
| single_source | cnn | 0.500 ± 0.118 | 0.498 ± 0.126 | 3 | 1 |
| single_source | rf | 0.333 ± 0.104 | 0.361 ± 0.114 | 12 | 3 |
| single_source | svm | 0.365 ± 0.211 | 0.410 ± 0.194 | 12 | 1 |
| steady_to_transitional | cnn | 0.829 | 0.797 | 1 | 1 |
| steady_to_transitional | rf | 0.766 ± 0.001 | 0.753 ± 0.002 | 1 | 3 |
| steady_to_transitional | svm | 0.885 | 0.846 | 1 | 1 |
| compositional_control | cnn | 0.824 | 0.910 | 1 | 1 |
| compositional_control | rf | 0.900 ± 0.000 | 0.933 ± 0.000 | 1 | 2 |
| leave_combination_out | cnn | 0.000 ± 0.000 | 0.104 ± 0.021 | 3 | 1 |
| leave_combination_out | rf | 0.003 ± 0.004 | 0.077 ± 0.034 | 3 | 2 |
| compositional_zeroshot | cnn | 0.000 | 0.038 | 1 | 1 |
| compositional_zeroshot | rf | 0.000 ± 0.000 | 0.015 ± 0.003 | 1 | 2 |

## T1b. Cross-model comparison on common folds only

| protocol | common_folds | cnn | rf | svm |
| --- | --- | --- | --- | --- |
| leaky_random | 1 | 0.939 | 0.975 ± 0.000 | 0.964 |
| in_condition | 1 | 0.913 | 0.965 ± 0.000 | 0.955 |
| unknown_condition | 3 | 0.883 ± 0.051 | 0.928 ± 0.017 | 0.936 ± 0.023 |
| cross_profile | 2 | 0.810 ± 0.134 | 0.839 ± 0.115 | 0.874 ± 0.114 |
| single_source | 3 | 0.500 ± 0.118 | 0.386 ± 0.107 | 0.546 ± 0.291 |
| steady_to_transitional | 1 | 0.829 | 0.766 ± 0.001 | 0.885 |
| compositional_control | 1 | 0.824 | 0.900 ± 0.000 |  |
| leave_combination_out | 3 | 0.000 ± 0.000 | 0.003 ± 0.004 |  |
| compositional_zeroshot | 1 | 0.000 | 0.000 ± 0.000 |  |

## T2. Physics-feature ablation: plain vs plain+order

| protocol | model | plain | plain+order | delta |
| --- | --- | --- | --- | --- |
| in_condition | rf | 0.965 ± 0.000 | 0.966 ± 0.001 | +0.002 |
| unknown_condition | rf | 0.939 ± 0.024 | 0.940 ± 0.020 | +0.001 |
| cross_profile | rf | 0.839 ± 0.115 | 0.856 ± 0.083 | +0.017 |
| single_source | rf | 0.333 ± 0.104 | 0.379 ± 0.116 | +0.047 |
| steady_to_transitional | rf | 0.766 ± 0.001 | 0.799 ± 0.002 | +0.034 |
| compositional_control | rf | 0.900 ± 0.000 | 0.903 | +0.004 |
| leave_combination_out | rf | 0.003 ± 0.004 | 0.005 ± 0.009 | +0.002 |
| compositional_zeroshot | rf | 0.000 ± 0.000 | 0.000 | +0.000 |

## T3. Test-time noise robustness (CNN)

| protocol | clean | 0 dB | 10 dB | 20 dB |
| --- | --- | --- | --- | --- |
| leaky_random | 0.939 | 0.198 | 0.675 | 0.925 |
| in_condition | 0.913 | 0.219 | 0.703 | 0.900 |
| unknown_condition | 0.883 ± 0.051 | 0.158 ± 0.103 | 0.567 ± 0.251 | 0.822 ± 0.130 |
| cross_profile | 0.810 ± 0.134 | 0.232 ± 0.001 | 0.625 ± 0.099 | 0.810 ± 0.140 |
| single_source | 0.500 ± 0.118 | 0.221 ± 0.021 | 0.452 ± 0.086 | 0.498 ± 0.116 |
| steady_to_transitional | 0.829 | 0.190 | 0.490 | 0.817 |
| compositional_control | 0.824 |  |  |  |
| leave_combination_out | 0.000 ± 0.000 |  |  |  |
| compositional_zeroshot | 0.000 |  |  |  |

## T4. Compound-fault protocols, multi-label metrics

| protocol | model | features | exact_match | micro_f1 | any_found | all_zero | topk_exact | topk_recall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional_control | cnn | plain | 0.824 | 0.904 | 0.896 | 0.090 | 0.903 | 0.903 |
| compositional_control | rf | plain | 0.900 ± 0.000 | 0.936 ± 0.000 | 0.901 ± 0.001 | 0.076 ± 0.002 | 0.902 ± 0.001 | 0.902 ± 0.001 |
| compositional_control | rf | plain+order | 0.903 | 0.938 | 0.904 | 0.074 | 0.906 | 0.906 |
| leave_combination_out | cnn | plain | 0.000 ± 0.000 | 0.393 ± 0.042 | 0.619 ± 0.089 | 0.204 ± 0.099 | 0.012 ± 0.018 | 0.477 ± 0.022 |
| leave_combination_out | rf | plain | 0.003 ± 0.004 | 0.222 ± 0.067 | 0.329 ± 0.098 | 0.246 ± 0.116 | 0.003 ± 0.004 | 0.166 ± 0.050 |
| leave_combination_out | rf | plain+order | 0.005 ± 0.009 | 0.446 ± 0.066 | 0.628 ± 0.085 | 0.286 ± 0.039 | 0.005 ± 0.009 | 0.317 ± 0.045 |
| compositional_zeroshot | cnn | plain | 0.000 | 0.122 | 0.149 | 0.551 | 0.079 | 0.333 |
| compositional_zeroshot | rf | plain | 0.000 ± 0.000 | 0.062 ± 0.013 | 0.069 ± 0.016 | 0.786 ± 0.036 | 0.000 ± 0.000 | 0.035 ± 0.008 |
| compositional_zeroshot | rf | plain+order | 0.000 | 0.228 | 0.268 | 0.652 | 0.000 | 0.134 |

## T5. Per-condition detail (random forest, plain features)

| condition | single_source | unknown_condition |
| --- | --- | --- |
| speed_circulation_20Nm_1000rpm | 0.244 ± 0.009 | 0.929 ± 0.001 |
| speed_circulation_20Nm_2000rpm | 0.450 ± 0.010 | 0.947 ± 0.002 |
| speed_circulation_20Nm_3000rpm | 0.466 ± 0.004 | 0.908 ± 0.003 |
| speed_circulation_40Nm_1000rpm | 0.190 ± 0.013 | 0.920 ± 0.002 |
| speed_circulation_40Nm_2000rpm | 0.356 ± 0.004 | 0.945 ± 0.000 |
| speed_circulation_40Nm_3000rpm | 0.535 ± 0.006 | 0.944 ± 0.001 |
| torque_circulation_20Nm_1000rpm | 0.217 ± 0.005 | 0.959 ± 0.001 |
| torque_circulation_20Nm_2000rpm | 0.338 ± 0.005 | 0.963 ± 0.002 |
| torque_circulation_20Nm_3000rpm | 0.294 ± 0.009 | 0.886 ± 0.002 |
| torque_circulation_40Nm_1000rpm | 0.238 ± 0.002 | 0.944 ± 0.000 |
| torque_circulation_40Nm_2000rpm | 0.354 ± 0.006 | 0.964 ± 0.001 |
| torque_circulation_40Nm_3000rpm | 0.314 ± 0.005 | 0.959 ± 0.000 |
