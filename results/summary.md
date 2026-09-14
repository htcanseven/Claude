# PMSG vs SCIG under identical winding short-circuits — first comparison

Recordings: 225 per machine (24 fault cases + healthy, × 3 speeds × 3 torques). Windows of 5 electrical cycles, hop 1 cycle. PRE-early = 0.30–0.62 s, PRE-late = 0.62–0.98 s, FLT = relay-on + 30 ms to relay-off − 10 ms. Features use only stator-side / controller signals; `Ifault` and `Fault_relay` are ground truth.

**Detectability statistic.** Signal-to-drift ratio SDR = |relative change of a feature between PRE-late and FLT| ÷ 95th percentile of |relative change between PRE-early and PRE-late| over all 225 recordings of that machine. SDR ≥ 1 means the change under fault exceeds what ordinary within-recording drift produces in 95 % of healthy segments, i.e. detectable at ≈5 % per-recording false alarm. It is scale-free and directly comparable across features, operating points and topologies.

**Caveat on every number:** one physical machine per topology, no repeated tests. Differences between the two columns are differences between *these two machines*; attributing them to topology needs the simulation populations planned for the paper.

## A. Same tap pair ≠ same physical severity

Mean fault current over the 24 cases: PMSG 6.64 A, SCIG 5.97 A (SCIG/PMSG median 0.91, range 0.78–0.96). In per-unit of rated current: PMSG 1.05, SCIG 0.78. Relative to the pre-fault stator current I1: PMSG 2.63, SCIG 1.13 — the SCIG's magnetising current makes the same fault a much smaller fraction of what the stator sensors see.

| case | sev_pct | phases | Ifault_A_PMSG | Ifault_A_SCIG | ratio_SCIG_over_PMSG | Ifault_over_I1_PMSG | Ifault_over_I1_SCIG |
|---|---|---|---|---|---|---|---|
| TURNS_D11_D12 | 2.700 | AA | 1.428 | 1.161 | 0.813 | 0.560 | 0.219 |
| TURNS_D09_D10 | 2.800 | AA | 1.415 | 1.161 | 0.821 | 0.557 | 0.220 |
| TURNS_D23_D24 | 2.800 | AA | 1.425 | 1.134 | 0.796 | 0.564 | 0.214 |
| TURNS_D21_D22 | 3.800 | AA | 1.436 | 1.125 | 0.783 | 0.569 | 0.212 |
| TURNS_D06_D07 | 7.400 | AA | 3.755 | 3.426 | 0.913 | 1.492 | 0.645 |
| TURNS_D14_D15 | 7.400 | BB | 3.758 | 3.399 | 0.905 | 1.494 | 0.641 |
| TURNS_D18_D19 | 7.400 | AA | 3.744 | 3.383 | 0.904 | 1.484 | 0.637 |
| TURNS_D02_D03 | 7.700 | BB | 3.772 | 3.444 | 0.913 | 1.498 | 0.650 |
| TURNS_D13_D16 | 11.600 | AA | 6.011 | 5.664 | 0.942 | 2.397 | 1.069 |
| TURNS_D17_D20 | 11.600 | CC | 6.040 | 5.654 | 0.936 | 2.409 | 1.067 |
| TURNS_D01_D04 | 12.000 | AA | 6.016 | 5.328 | 0.886 | 2.415 | 1.006 |
| TURNS_D05_D08 | 12.100 | CC | 6.016 | 5.716 | 0.950 | 2.394 | 1.077 |
| WINDINGS_D04_D06 | 2.300 | AA | 2.062 | 1.941 | 0.941 | 0.818 | 0.365 |
| WINDINGS_D16_D18 | 3.200 | AA | 2.140 | 1.933 | 0.903 | 0.836 | 0.364 |
| WINDINGS_D04_D07 | 9.700 | AA | 4.816 | 4.620 | 0.959 | 1.880 | 0.870 |
| WINDINGS_D16_D19 | 10.600 | AA | 4.956 | 4.548 | 0.918 | 1.933 | 0.855 |
| WINDINGS_D01_D06 | 14.300 | AA | 7.268 | 6.667 | 0.917 | 2.898 | 1.258 |
| WINDINGS_D13_D18 | 14.800 | AA | 6.934 | 6.367 | 0.918 | 2.741 | 1.202 |
| WINDINGS_D01_D07 | 21.700 | AA | 10.535 | 9.590 | 0.910 | 4.181 | 1.812 |
| WINDINGS_D13_D19 | 22.200 | AA | 10.010 | 9.158 | 0.915 | 3.967 | 1.727 |
| WINDINGS_D12_D21 | 33.700 | AA | 15.388 | 13.722 | 0.892 | 6.082 | 2.590 |
| WINDINGS_D11_D21 | 36.400 | AA | 16.350 | 14.466 | 0.885 | 6.414 | 2.731 |
| WINDINGS_D12_D22 | 37.500 | AA | 16.558 | 14.521 | 0.877 | 6.503 | 2.741 |
| WINDINGS_D11_D22 | 40.200 | AA | 17.558 | 15.215 | 0.867 | 6.937 | 2.873 |

![A](figures/A_fault_current_by_case.png)

## B. Where the signature shows up, per topology

Null (95th percentile of |no-fault relative change|) per machine, selected features:

| feature | PMSG | SCIG |
|---|---|---|
| I2_I1 | 0.162 | 0.034 |
| V2_V1 | 0.086 | 0.033 |
| Id_2fe | 0.563 | 0.016 |
| Iq_2fe | 0.184 | 0.060 |
| PIq_2fe | 0.100 | 0.053 |
| Vq_2fe | 0.165 | 0.060 |
| Ia_h3 | 0.216 | 0.035 |
| Te_2fe | 0.649 | 0.625 |
| Vdc_std | 0.003 | 0.004 |

Top-6 features by median SDR per machine and fault type (`median_delta` = median relative change, sign = direction):

| machine | ftype | feature | group | median_sdr | frac_detectable | healthy_false_alarm | median_delta |
|---|---|---|---|---|---|---|---|
| SCIG | WINDINGS | D2_D1 | dq / control | 84.887 | 1.000 | 0.444 | 0.854 |
| SCIG | WINDINGS | PId_2fe | dq / control | 74.013 | 1.000 | 0.111 | 1.188 |
| SCIG | WINDINGS | Id_2fe | dq / control | 73.971 | 1.000 | 0.111 | 1.188 |
| SCIG | WINDINGS | Vdconv_2fe | dq / control | 63.019 | 1.000 | 0.111 | 1.203 |
| PMSG | WINDINGS | V2_V1 | terminal voltage | 61.898 | 0.944 | 0.111 | 5.318 |
| SCIG | WINDINGS | I2_I1 | stator current | 55.608 | 1.000 | 0.111 | 1.869 |
| SCIG | WINDINGS | V2_V1 | terminal voltage | 48.192 | 1.000 | 0.000 | 1.569 |
| PMSG | WINDINGS | D2_D1 | dq / control | 32.629 | 0.898 | 0.000 | 2.942 |
| PMSG | WINDINGS | Vq_2fe | terminal voltage | 22.398 | 0.898 | 0.000 | 3.688 |
| PMSG | WINDINGS | I2_I1 | stator current | 11.316 | 0.815 | 0.000 | 1.833 |
| SCIG | TURNS | D2_D1 | dq / control | 11.062 | 0.815 | 0.444 | 0.017 |
| PMSG | WINDINGS | PIq_2fe | dq / control | 8.002 | 0.833 | 0.111 | 0.636 |
| SCIG | TURNS | PId_2fe | dq / control | 6.685 | 0.778 | 0.111 | 0.015 |
| SCIG | TURNS | Id_2fe | dq / control | 6.682 | 0.787 | 0.111 | 0.015 |
| SCIG | TURNS | Vdconv_2fe | dq / control | 5.960 | 0.769 | 0.111 | 0.013 |
| PMSG | WINDINGS | Vqconv_2fe | dq / control | 5.232 | 0.769 | 0.222 | 0.669 |
| SCIG | TURNS | I2_I1 | stator current | 4.525 | 0.750 | 0.111 | 0.042 |
| SCIG | TURNS | V2_V1 | terminal voltage | 4.171 | 0.731 | 0.000 | 0.026 |
| PMSG | TURNS | V2_V1 | terminal voltage | 2.990 | 0.759 | 0.111 | 0.003 |
| PMSG | TURNS | D2_D1 | dq / control | 2.779 | 0.639 | 0.000 | 0.010 |
| PMSG | TURNS | PIq_2fe | dq / control | 1.802 | 0.630 | 0.111 | -0.028 |
| PMSG | TURNS | I2_I1 | stator current | 1.471 | 0.565 | 0.000 | -0.003 |
| PMSG | TURNS | Vq_2fe | terminal voltage | 1.346 | 0.574 | 0.000 | 0.020 |
| PMSG | TURNS | Vqconv_2fe | dq / control | 1.221 | 0.565 | 0.222 | -0.014 |

Share of fault recordings in which each signal group holds the strongest signature:

| machine | ftype | group | representative_feature | share_of_recordings_where_group_is_strongest |
|---|---|---|---|---|
| PMSG | TURNS | stator current | I2_I1 | 0.083 |
| PMSG | TURNS | terminal voltage | V2_V1 | 0.667 |
| PMSG | TURNS | dq / control | D2_D1 | 0.167 |
| PMSG | TURNS | mechanical | Vdc_std | 0.083 |
| PMSG | WINDINGS | stator current | I2_I1 | 0.056 |
| PMSG | WINDINGS | terminal voltage | V2_V1 | 0.880 |
| PMSG | WINDINGS | dq / control | D2_D1 | 0.037 |
| PMSG | WINDINGS | mechanical | Vdc_std | 0.028 |
| SCIG | TURNS | stator current | I2_I1 | 0.278 |
| SCIG | TURNS | terminal voltage | V2_V1 | 0.130 |
| SCIG | TURNS | dq / control | PId_2fe | 0.556 |
| SCIG | TURNS | mechanical | Vdc_std | 0.037 |
| SCIG | WINDINGS | stator current | I2_I1 | 0.333 |
| SCIG | WINDINGS | terminal voltage | V2_V1 | 0.000 |
| SCIG | WINDINGS | dq / control | PId_2fe | 0.667 |
| SCIG | WINDINGS | mechanical | Spd_std | 0.000 |

![B](figures/B_sdr_by_feature.png)

## C. Minimum detectable fault extent

Features with the highest pooled median SDR (both machines): V2_V1, Vq_2fe, I2_I1, PId_2fe. Smallest tap-pair severity level whose median SDR is ≥ 1:

| machine | ftype | feature | min_detectable_sev_pct | min_detectable_first_pct | n_sev_levels | n_levels_detectable | spearman_sdr_vs_sev |
|---|---|---|---|---|---|---|---|
| PMSG | TURNS | V2_V1 | 3.800 | 3.800 | 8 | 6 | 0.790 |
| PMSG | TURNS | Vq_2fe | 7.400 | 7.400 | 8 | 5 | 0.775 |
| PMSG | TURNS | I2_I1 | 7.400 | 7.400 | 8 | 5 | 0.704 |
| PMSG | TURNS | PId_2fe | 12.100 | 11.600 | 8 | 2 | 0.512 |
| PMSG | WINDINGS | V2_V1 | 2.300 | 2.300 | 12 | 12 | 0.925 |
| PMSG | WINDINGS | Vq_2fe | 9.700 | 2.300 | 12 | 11 | 0.910 |
| PMSG | WINDINGS | I2_I1 | 9.700 | 9.700 | 12 | 10 | 0.919 |
| PMSG | WINDINGS | PId_2fe | 21.700 | 10.600 | 12 | 8 | 0.867 |
| SCIG | TURNS | V2_V1 | 7.400 | 2.700 | 8 | 6 | 0.832 |
| SCIG | TURNS | Vq_2fe | 7.400 | 7.400 | 8 | 5 | 0.794 |
| SCIG | TURNS | I2_I1 | 7.400 | 7.400 | 8 | 5 | 0.769 |
| SCIG | TURNS | PId_2fe | 7.400 | 2.700 | 8 | 6 | 0.805 |
| SCIG | WINDINGS | V2_V1 | 2.300 | 2.300 | 12 | 12 | 0.947 |
| SCIG | WINDINGS | Vq_2fe | 9.700 | 2.300 | 12 | 11 | 0.952 |
| SCIG | WINDINGS | I2_I1 | 2.300 | 2.300 | 12 | 12 | 0.868 |
| SCIG | WINDINGS | PId_2fe | 2.300 | 2.300 | 12 | 12 | 0.935 |

![C](figures/C_sdr_vs_severity.png)

## D. Operating-point dependence

| machine | speed_rpm | torque_Nm | median_best_sdr | frac_detectable |
|---|---|---|---|---|
| PMSG | 1200 | 5.200 | 7.896 | 0.833 |
| PMSG | 1200 | 6.400 | 9.006 | 0.833 |
| PMSG | 1200 | 8.000 | 5.301 | 0.792 |
| PMSG | 1500 | 5.200 | 12.826 | 0.958 |
| PMSG | 1500 | 6.400 | 11.252 | 0.958 |
| PMSG | 1500 | 8.000 | 9.580 | 0.917 |
| PMSG | 1800 | 5.200 | 20.477 | 0.917 |
| PMSG | 1800 | 6.400 | 18.200 | 0.958 |
| PMSG | 1800 | 8.000 | 15.458 | 0.917 |
| SCIG | 1200 | 5.200 | 18.149 | 0.917 |
| SCIG | 1200 | 6.400 | 16.580 | 0.917 |
| SCIG | 1200 | 8.000 | 16.052 | 0.958 |
| SCIG | 1500 | 5.200 | 26.429 | 0.917 |
| SCIG | 1500 | 6.400 | 23.491 | 0.917 |
| SCIG | 1500 | 8.000 | 23.812 | 0.917 |
| SCIG | 1800 | 5.200 | 51.011 | 1.000 |
| SCIG | 1800 | 6.400 | 47.169 | 1.000 |
| SCIG | 1800 | 8.000 | 44.012 | 0.958 |

![D](figures/D_operating_point_grid.png)

## E. Cross-topology transfer

Window-level detector (1 = fault window of a fault recording; 0 = pre-fault windows of all recordings and fault-time windows of healthy recordings). n windows = 46030; positives = 5882. Within-topology rows use 5-fold GroupKFold over fault cases (unseen tap pairs).

| calibration | model | train | test | setting | auc | tpr_at_1pct_fpr | n_test |
|---|---|---|---|---|---|---|---|
| raw | logistic | PMSG | PMSG | within (unseen cases) | 0.775 | 0.549 | 23204 |
| raw | logistic | SCIG | SCIG | within (unseen cases) | 0.794 | 0.577 | 22826 |
| raw | logistic | PMSG | SCIG | cross-topology | 0.713 | 0.409 | 22826 |
| raw | logistic | SCIG | PMSG | cross-topology | 0.592 | 0.254 | 23204 |
| raw | gbdt | PMSG | PMSG | within (unseen cases) | 0.876 | 0.604 | 23204 |
| raw | gbdt | SCIG | SCIG | within (unseen cases) | 0.903 | 0.627 | 22826 |
| raw | gbdt | PMSG | SCIG | cross-topology | 0.783 | 0.466 | 22826 |
| raw | gbdt | SCIG | PMSG | cross-topology | 0.551 | 0.236 | 23204 |
| healthy-z | logistic | PMSG | PMSG | within (unseen cases) | 0.775 | 0.549 | 23204 |
| healthy-z | logistic | SCIG | SCIG | within (unseen cases) | 0.794 | 0.577 | 22826 |
| healthy-z | logistic | PMSG | SCIG | cross-topology | 0.707 | 0.424 | 22826 |
| healthy-z | logistic | SCIG | PMSG | cross-topology | 0.443 | 0.085 | 23204 |
| healthy-z | gbdt | PMSG | PMSG | within (unseen cases) | 0.876 | 0.604 | 23204 |
| healthy-z | gbdt | SCIG | SCIG | within (unseen cases) | 0.903 | 0.627 | 22826 |
| healthy-z | gbdt | PMSG | SCIG | cross-topology | 0.815 | 0.207 | 22826 |
| healthy-z | gbdt | SCIG | PMSG | cross-topology | 0.745 | 0.302 | 23204 |
| self-ref | logistic | PMSG | PMSG | within (unseen cases) | 0.902 | 0.709 | 23204 |
| self-ref | logistic | SCIG | SCIG | within (unseen cases) | 0.938 | 0.801 | 22826 |
| self-ref | logistic | PMSG | SCIG | cross-topology | 0.896 | 0.666 | 22826 |
| self-ref | logistic | SCIG | PMSG | cross-topology | 0.881 | 0.602 | 23204 |
| self-ref | gbdt | PMSG | PMSG | within (unseen cases) | 0.918 | 0.737 | 23204 |
| self-ref | gbdt | SCIG | SCIG | within (unseen cases) | 0.945 | 0.811 | 22826 |
| self-ref | gbdt | PMSG | SCIG | cross-topology | 0.918 | 0.739 | 22826 |
| self-ref | gbdt | SCIG | PMSG | cross-topology | 0.857 | 0.433 | 23204 |

Cosine similarity of the two logistic weight vectors (healthy-z features), PMSG vs SCIG: **0.02** (1 = identical feature weighting).

Largest-weight features (healthy-z logistic):

| feature | PMSG | SCIG | abs_mean |
|---|---|---|---|
| V2_V1 | 7.254 | -1.119 | 4.187 |
| I2_I1 | 1.305 | 5.871 | 3.588 |
| PIq_2fe | -3.447 | 2.209 | 2.828 |
| Ia_h3 | 3.347 | 1.183 | 2.265 |
| Vd_2fe | 2.234 | 0.744 | 1.489 |
| Iq_2fe | 1.747 | 0.993 | 1.370 |
| Iq_std | -0.482 | -2.232 | 1.357 |
| Vdconv_2fe | -2.111 | 0.478 | 1.295 |
| I_unbal_rms | -1.737 | -0.795 | 1.266 |
| Vqconv_2fe | -0.790 | 1.557 | 1.173 |
| D2_D1 | 1.787 | 0.530 | 1.158 |
| Vq_2fe | 2.045 | -0.048 | 1.046 |

![E](figures/E_transfer.png)
