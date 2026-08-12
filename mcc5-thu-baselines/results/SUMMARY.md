# MCC5-THU baseline and proposed-model results

`acc` is exact-match accuracy (for the multi-label compositional protocol, all components of a compound fault must be correct). Values are mean ± std over seeds and folds.

| protocol | model | features | acc | macro_f1 | micro_f1 | n_runs | folds |
| --- | --- | --- | --- | --- | --- | --- | --- |
| leaky_random | rf | plain | 0.975 | 0.975 |  | 1 | 1 |
| in_condition | rf | plain | 0.965 | 0.964 |  | 1 | 1 |
| unknown_condition | rf | plain | 0.939 ± 0.024 | 0.931 ± 0.033 |  | 12 | 12 |
| cross_profile | rf | plain | 0.839 ± 0.147 | 0.843 ± 0.141 |  | 2 | 2 |
| single_source | rf | plain | 0.333 ± 0.106 | 0.361 ± 0.116 |  | 12 | 12 |
| steady_to_transitional | rf | plain | 0.767 | 0.755 |  | 1 | 1 |
| compositional_zeroshot | rf | plain | 0.000 | 0.017 | 0.072 | 1 | 1 |

## Drop relative to the leaky random split

Reference (leaky_random, all models): **0.975**

| protocol | acc | drop |
| --- | --- | --- |
| in_condition | 0.965 | +0.010 |
| unknown_condition | 0.939 | +0.036 |
| cross_profile | 0.839 | +0.136 |
| single_source | 0.333 | +0.642 |
| steady_to_transitional | 0.767 | +0.208 |
| compositional_zeroshot | 0.000 | +0.975 |
