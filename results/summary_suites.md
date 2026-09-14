# Sensor-suite analysis — which monitoring architecture detects what, per topology

Suites, ordered by added hardware / integration:

- **drive-internal** — no added sensors; access to the converter controller (18 candidate features)
- **3 CT** — 3 current transducers at the terminals; no angle information (6 candidate features)
- **3 CT + 3 VT** — 3 current + 3 voltage transducers; no angle information (7 candidate features)
- **3 CT + 3 VT + drive** — external transducers plus controller access (dq transform of measured voltages) (27 candidate features)
- **+ torque transducer** — everything above plus a shaft torque transducer (30 candidate features)

Features that fire on more than one of the nine healthy recordings of a machine are excluded for that machine (`excluded` column). `fixed_*` = one feature per suite chosen once by median SDR; `oracle_*` = best feature per recording (upper bound for a multi-feature detector).

| suite | machine | ftype | n_features | best_feature | fixed_median_sdr | fixed_share_detectable | fixed_min_detectable_pct | oracle_share_detectable | oracle_min_detectable_pct | excluded |
|---|---|---|---|---|---|---|---|---|---|---|
| drive-internal | PMSG | TURNS | 16 | D2_D1 | 2.779 | 0.639 | 7.400 | 0.870 | 2.700 | Id_1fe,Spd_std |
| 3 CT | PMSG | TURNS | 6 | I2_I1 | 1.471 | 0.565 | 7.400 | 0.769 | 7.400 |  |
| 3 CT + 3 VT | PMSG | TURNS | 7 | V2_V1 | 2.990 | 0.759 | 3.800 | 0.880 | 2.800 |  |
| 3 CT + 3 VT + drive | PMSG | TURNS | 25 | V2_V1 | 2.990 | 0.759 | 3.800 | 0.954 | 2.700 | Id_1fe,Spd_std |
| + torque transducer | PMSG | TURNS | 28 | V2_V1 | 2.990 | 0.759 | 3.800 | 0.954 | 2.700 | Id_1fe,Spd_std |
| drive-internal | PMSG | WINDINGS | 16 | D2_D1 | 32.629 | 0.898 | 14.300 | 1.000 | 2.300 | Id_1fe,Spd_std |
| 3 CT | PMSG | WINDINGS | 6 | I2_I1 | 11.316 | 0.815 | 9.700 | 0.944 | 2.300 |  |
| 3 CT + 3 VT | PMSG | WINDINGS | 7 | V2_V1 | 61.898 | 0.944 | 2.300 | 0.972 | 2.300 |  |
| 3 CT + 3 VT + drive | PMSG | WINDINGS | 25 | V2_V1 | 61.898 | 0.944 | 2.300 | 1.000 | 2.300 | Id_1fe,Spd_std |
| + torque transducer | PMSG | WINDINGS | 28 | V2_V1 | 61.898 | 0.944 | 2.300 | 1.000 | 2.300 | Id_1fe,Spd_std |
| drive-internal | SCIG | TURNS | 17 | PId_2fe | 6.685 | 0.778 | 7.400 | 0.991 | 2.700 | D2_D1 |
| 3 CT | SCIG | TURNS | 5 | I2_I1 | 4.525 | 0.750 | 7.400 | 0.870 | 2.700 | Ia_h7 |
| 3 CT + 3 VT | SCIG | TURNS | 6 | I2_I1 | 4.525 | 0.750 | 7.400 | 0.898 | 2.700 | Ia_h7 |
| 3 CT + 3 VT + drive | SCIG | TURNS | 25 | PId_2fe | 6.685 | 0.778 | 7.400 | 0.991 | 2.700 | D2_D1,Ia_h7 |
| + torque transducer | SCIG | TURNS | 25 | PId_2fe | 6.685 | 0.778 | 7.400 | 0.991 | 2.700 | D2_D1,Ia_h7,Tm_1fe,Tm_2fe,Tm_std |
| drive-internal | SCIG | WINDINGS | 17 | PId_2fe | 74.013 | 1.000 | 2.300 | 1.000 | 2.300 | D2_D1 |
| 3 CT | SCIG | WINDINGS | 5 | I2_I1 | 55.608 | 1.000 | 2.300 | 1.000 | 2.300 | Ia_h7 |
| 3 CT + 3 VT | SCIG | WINDINGS | 6 | I2_I1 | 55.608 | 1.000 | 2.300 | 1.000 | 2.300 | Ia_h7 |
| 3 CT + 3 VT + drive | SCIG | WINDINGS | 25 | PId_2fe | 74.013 | 1.000 | 2.300 | 1.000 | 2.300 | D2_D1,Ia_h7 |
| + torque transducer | SCIG | WINDINGS | 25 | PId_2fe | 74.013 | 1.000 | 2.300 | 1.000 | 2.300 | D2_D1,Ia_h7,Tm_1fe,Tm_2fe,Tm_std |

## Transfer restricted to each suite (GBDT)

| suite | calibration | PMSG→PMSG | PMSG→SCIG | SCIG→PMSG | SCIG→SCIG |
|---|---|---|---|---|---|
| + torque transducer | healthy-z | 0.876 | 0.815 | 0.745 | 0.904 |
| + torque transducer | self-ref | 0.918 | 0.918 | 0.857 | 0.946 |
| 3 CT | healthy-z | 0.854 | 0.736 | 0.622 | 0.868 |
| 3 CT | self-ref | 0.863 | 0.911 | 0.815 | 0.897 |
| 3 CT + 3 VT | healthy-z | 0.836 | 0.859 | 0.703 | 0.891 |
| 3 CT + 3 VT | self-ref | 0.893 | 0.917 | 0.886 | 0.901 |
| 3 CT + 3 VT + drive | healthy-z | 0.880 | 0.813 | 0.750 | 0.904 |
| 3 CT + 3 VT + drive | self-ref | 0.919 | 0.917 | 0.859 | 0.946 |
| drive-internal | healthy-z | 0.870 | 0.727 | 0.740 | 0.870 |
| drive-internal | self-ref | 0.890 | 0.922 | 0.863 | 0.949 |

![F](figures/F_sensor_suites.png)
