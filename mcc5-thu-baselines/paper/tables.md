# Generated tables

Source: 4 result file(s), 76 rows.

## T1. Protocol x model (plain features)

| protocol | model | accuracy | macro_f1 | folds | seeds |
| --- | --- | --- | --- | --- | --- |
| leaky_random | cnn | 0.939 | 0.939 | 1 | 1 |
| leaky_random | svm | 0.964 | 0.965 | 1 | 1 |
| in_condition | cnn | 0.913 | 0.911 | 1 | 1 |
| in_condition | svm | 0.955 | 0.954 | 1 | 1 |
| unknown_condition | cnn | 0.883 ± 0.051 | 0.861 ± 0.056 | 3 | 1 |
| unknown_condition | svm | 0.947 ± 0.027 | 0.942 ± 0.034 | 12 | 1 |
| cross_profile | cnn | 0.810 ± 0.134 | 0.811 ± 0.127 | 2 | 1 |
| cross_profile | svm | 0.874 ± 0.114 | 0.882 ± 0.102 | 2 | 1 |
| single_source | cnn | 0.363 | 0.352 | 1 | 1 |
| single_source | svm | 0.365 ± 0.211 | 0.410 ± 0.194 | 12 | 1 |
| steady_to_transitional | svm | 0.885 | 0.846 | 1 | 1 |
| compositional_control | rf | 0.900 ± 0.000 | 0.933 ± 0.000 | 1 | 2 |
| leave_combination_out | rf | 0.003 ± 0.004 | 0.077 ± 0.034 | 3 | 2 |
| compositional_zeroshot | rf | 0.000 ± 0.000 | 0.015 ± 0.003 | 1 | 2 |

## T2. Physics-feature ablation: plain vs plain+order

| protocol | model | plain | plain+order | delta |
| --- | --- | --- | --- | --- |
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
| single_source | 0.363 | 0.207 | 0.354 | 0.364 |

## T4. Compound-fault protocols, multi-label metrics

| protocol | model | features | exact_match | micro_f1 | any_found | all_zero | topk_exact | topk_recall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional_control | rf | plain | 0.900 ± 0.000 | 0.936 ± 0.000 | 0.901 ± 0.001 | 0.076 ± 0.002 | 0.902 ± 0.001 | 0.902 ± 0.001 |
| compositional_control | rf | plain+order | 0.903 | 0.938 | 0.904 | 0.074 | 0.906 | 0.906 |
| leave_combination_out | rf | plain | 0.003 ± 0.004 | 0.222 ± 0.067 | 0.329 ± 0.098 | 0.246 ± 0.116 | 0.003 ± 0.004 | 0.166 ± 0.050 |
| leave_combination_out | rf | plain+order | 0.005 ± 0.009 | 0.446 ± 0.066 | 0.628 ± 0.085 | 0.286 ± 0.039 | 0.005 ± 0.009 | 0.317 ± 0.045 |
| compositional_zeroshot | rf | plain | 0.000 ± 0.000 | 0.062 ± 0.013 | 0.069 ± 0.016 | 0.786 ± 0.036 | 0.000 ± 0.000 | 0.035 ± 0.008 |
| compositional_zeroshot | rf | plain+order | 0.000 | 0.228 | 0.268 | 0.652 | 0.000 | 0.134 |

## T5. Per-condition detail (random forest, plain features)

*(no data yet — stage still running or not scheduled)*
