# Revision re-analyses

## R1 cheapest suite per requirement (bootstrap verdicts: meets P>=0.95, fails P<=0.05)

| alpha | e_req_pct | machine | ftype | cheapest_meets | cheapest_meets_feature | cheapest_not_failing | n_uncertain |
|---|---|---|---|---|---|---|---|
| 0.900 | 3 | PMSG | TURNS | none |  | none | 0 |
| 0.900 | 3 | PMSG | WINDINGS | none |  | drive-internal | 2 |
| 0.900 | 3 | SCIG | TURNS | none |  | drive-internal | 2 |
| 0.900 | 3 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.900 | 3 | WFSG | TURNS | none |  | none | 0 |
| 0.900 | 3 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 5 | PMSG | TURNS | none |  | drive-internal | 2 |
| 0.900 | 5 | PMSG | WINDINGS | none |  | drive-internal | 4 |
| 0.900 | 5 | SCIG | TURNS | none |  | drive-internal | 2 |
| 0.900 | 5 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.900 | 5 | WFSG | TURNS | none |  | none | 0 |
| 0.900 | 5 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 8 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 0 |
| 0.900 | 8 | PMSG | WINDINGS | none |  | drive-internal | 4 |
| 0.900 | 8 | SCIG | TURNS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.900 | 8 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.900 | 8 | WFSG | TURNS | none |  | none | 0 |
| 0.900 | 8 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 12 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 0 |
| 0.900 | 12 | PMSG | WINDINGS | 3 CT | I_unbal_rms | drive-internal | 2 |
| 0.900 | 12 | SCIG | TURNS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.900 | 12 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.900 | 12 | WFSG | TURNS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.900 | 12 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 3 | PMSG | TURNS | none |  | none | 0 |
| 0.950 | 3 | PMSG | WINDINGS | none |  | drive-internal | 2 |
| 0.950 | 3 | SCIG | TURNS | none |  | none | 0 |
| 0.950 | 3 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.950 | 3 | WFSG | TURNS | none |  | none | 0 |
| 0.950 | 3 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 5 | PMSG | TURNS | none |  | drive-internal | 2 |
| 0.950 | 5 | PMSG | WINDINGS | none |  | drive-internal | 2 |
| 0.950 | 5 | SCIG | TURNS | none |  | drive-internal | 2 |
| 0.950 | 5 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.950 | 5 | WFSG | TURNS | none |  | none | 0 |
| 0.950 | 5 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 8 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 2 |
| 0.950 | 8 | PMSG | WINDINGS | none |  | drive-internal | 2 |
| 0.950 | 8 | SCIG | TURNS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.950 | 8 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.950 | 8 | WFSG | TURNS | none |  | none | 0 |
| 0.950 | 8 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |
| 0.950 | 12 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 0 |
| 0.950 | 12 | PMSG | WINDINGS | 3 CT | I2_I1 | drive-internal | 2 |
| 0.950 | 12 | SCIG | TURNS | drive-internal | Vdconv_2fe | drive-internal | 0 |
| 0.950 | 12 | SCIG | WINDINGS | drive-internal | Vdconv_2fe | drive-internal | 0 |
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
| 0.990 | 12 | PMSG | TURNS | drive-internal | D2_D1 | drive-internal | 1 |
| 0.990 | 12 | PMSG | WINDINGS | none |  | drive-internal | 4 |
| 0.990 | 12 | SCIG | TURNS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 12 | SCIG | WINDINGS | drive-internal | Id_2fe | drive-internal | 0 |
| 0.990 | 12 | WFSG | TURNS | drive-internal | Iq_2fe | drive-internal | 1 |
| 0.990 | 12 | WFSG | WINDINGS | drive-internal | Iq_2fe | drive-internal | 0 |

## R1 full decision table (alpha = 0.95)

| e_req_pct | machine | ftype | suite | cost_rank | fixed_feature | mde_monotone_pct | mde_ci_lo | mde_ci_hi | p_meets | verdict | ds_conditional | ds_all | smallest_extent_tested_pct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.690 | 0.000 | fails | 0.815 | 0.648 | 2.700 |
| 5 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.690 | 0.311 | uncertain | 0.861 | 0.648 | 2.700 |
| 8 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.690 | 1.000 | meets | 0.972 | 0.648 | 2.700 |
| 12 | PMSG | TURNS | drive-internal | 0 | D2_D1 | 7.400 | 3.800 | 7.690 | 1.000 | meets | 1.000 | 0.648 | 2.700 |
| 3 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.000 | fails | 0.728 | 0.574 | 2.700 |
| 5 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.001 | fails | 0.806 | 0.574 | 2.700 |
| 8 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.905 | uncertain | 0.889 | 0.574 | 2.700 |
| 12 | PMSG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.970 | meets | 0.889 | 0.574 | 2.700 |
| 3 | PMSG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.000 | fails | 0.728 | 0.574 | 2.700 |
| 5 | PMSG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.001 | fails | 0.806 | 0.574 | 2.700 |
| 8 | PMSG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.899 | uncertain | 0.889 | 0.574 | 2.700 |
| 12 | PMSG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.100 | 0.956 | meets | 0.889 | 0.574 | 2.700 |
| 3 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | D2_D1 | 7.400 | 3.800 | 7.690 | 0.000 | fails | 0.815 | 0.648 | 2.700 |
| 5 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | D2_D1 | 7.400 | 3.800 | 7.690 | 0.301 | uncertain | 0.861 | 0.648 | 2.700 |
| 8 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | D2_D1 | 7.400 | 3.800 | 7.690 | 0.999 | meets | 0.972 | 0.648 | 2.700 |
| 12 | PMSG | TURNS | 3 CT + 3 VT + drive | 3 | D2_D1 | 7.400 | 3.800 | 7.690 | 0.999 | meets | 1.000 | 0.648 | 2.700 |
| 3 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.123 | uncertain | 0.909 | 0.907 | 2.300 |
| 5 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.123 | uncertain | 0.933 | 0.907 | 2.300 |
| 8 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.123 | uncertain | 0.933 | 0.907 | 2.300 |
| 12 | PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.142 | uncertain | 1.000 | 0.907 | 2.300 |
| 3 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.002 | fails | 0.889 | 0.833 | 2.300 |
| 5 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.029 | fails | 0.956 | 0.833 | 2.300 |
| 8 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.029 | fails | 0.956 | 0.833 | 2.300 |
| 12 | PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.974 | meets | 0.986 | 0.833 | 2.300 |
| 3 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.000 | fails | 0.889 | 0.833 | 2.300 |
| 5 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.034 | fails | 0.956 | 0.833 | 2.300 |
| 8 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.034 | fails | 0.956 | 0.833 | 2.300 |
| 12 | PMSG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 9.700 | 3.200 | 14.340 | 0.972 | meets | 0.986 | 0.833 | 2.300 |
| 3 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.129 | uncertain | 0.909 | 0.907 | 2.300 |
| 5 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.129 | uncertain | 0.933 | 0.907 | 2.300 |
| 8 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.129 | uncertain | 0.933 | 0.907 | 2.300 |
| 12 | PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | D2_D1 | 14.340 | 2.300 | 14.340 | 0.148 | uncertain | 1.000 | 0.907 | 2.300 |
| 3 | SCIG | TURNS | drive-internal | 0 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.001 | fails | 0.864 | 0.731 | 2.700 |
| 5 | SCIG | TURNS | drive-internal | 0 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.131 | uncertain | 0.931 | 0.731 | 2.700 |
| 8 | SCIG | TURNS | drive-internal | 0 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.999 | meets | 0.972 | 0.731 | 2.700 |
| 12 | SCIG | TURNS | drive-internal | 0 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.999 | meets | 1.000 | 0.731 | 2.700 |
| 3 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.000 | fails | 0.815 | 0.704 | 2.700 |
| 5 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.000 | fails | 0.917 | 0.704 | 2.700 |
| 8 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.970 | meets | 0.944 | 0.704 | 2.700 |
| 12 | SCIG | TURNS | 3 CT | 1 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.970 | meets | 1.000 | 0.704 | 2.700 |
| 3 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.000 | fails | 0.815 | 0.704 | 2.700 |
| 5 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.000 | fails | 0.917 | 0.704 | 2.700 |
| 8 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.970 | meets | 0.944 | 0.704 | 2.700 |
| 12 | SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7.400 | 7.400 | 12.040 | 0.970 | meets | 1.000 | 0.704 | 2.700 |
| 3 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.003 | fails | 0.864 | 0.731 | 2.700 |
| 5 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.140 | uncertain | 0.931 | 0.731 | 2.700 |
| 8 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.997 | meets | 0.972 | 0.731 | 2.700 |
| 12 | SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 7.400 | 3.800 | 7.400 | 0.997 | meets | 1.000 | 0.731 | 2.700 |
| 3 | SCIG | WINDINGS | drive-internal | 0 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | SCIG | WINDINGS | drive-internal | 0 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | SCIG | WINDINGS | drive-internal | 0 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | SCIG | WINDINGS | drive-internal | 0 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 3 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 0.971 | meets | 1.000 | 0.981 | 2.300 |
| 5 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 8 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 12 | SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 3 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 3.200 | 0.974 | meets | 1.000 | 0.981 | 2.300 |
| 5 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 8 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 12 | SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 2.300 | 2.300 | 3.200 | 1.000 | meets | 1.000 | 0.981 | 2.300 |
| 3 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 5 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 8 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
| 12 | SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 2.300 | 2.300 | 2.300 | 1.000 | meets | 1.000 | 1.000 | 2.300 |
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
| 12 | WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 11.600 | 11.600 | 11.600 | 0.999 | meets | 0.857 | 0.863 | 11.600 |
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
| PMSG | TURNS | drive-internal | 0 | D2_D1 | 12 | 7.400 | 7.400 | 0.648 | 0.861 | 0.972 | 0.648 | 2.700 |
| PMSG | TURNS | 3 CT | 1 | I2_I1 | 7 | 7.400 | 7.400 | 0.574 | 0.806 | 0.889 | 0.574 | 2.700 |
| PMSG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 7 | 7.400 | 7.400 | 0.574 | 0.806 | 0.889 | 0.574 | 2.700 |
| PMSG | TURNS | 3 CT + 3 VT + drive | 3 | D2_D1 | 21 | 7.400 | 7.400 | 0.648 | 0.861 | 0.972 | 0.648 | 2.700 |
| PMSG | WINDINGS | drive-internal | 0 | D2_D1 | 12 | 2.300 | 14.340 | 0.907 | 0.933 | 0.933 | 0.907 | 2.300 |
| PMSG | WINDINGS | 3 CT | 1 | I2_I1 | 7 | 9.700 | 9.700 | 0.833 | 0.956 | 0.956 | 0.833 | 2.300 |
| PMSG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 7 | 9.700 | 9.700 | 0.833 | 0.956 | 0.956 | 0.833 | 2.300 |
| PMSG | WINDINGS | 3 CT + 3 VT + drive | 3 | D2_D1 | 21 | 2.300 | 14.340 | 0.907 | 0.933 | 0.933 | 0.907 | 2.300 |
| SCIG | TURNS | drive-internal | 0 | Vdconv_2fe | 9 | 7.400 | 7.400 | 0.731 | 0.931 | 0.972 | 0.731 | 2.700 |
| SCIG | TURNS | 3 CT | 1 | I2_I1 | 5 | 7.400 | 7.400 | 0.704 | 0.917 | 0.944 | 0.704 | 2.700 |
| SCIG | TURNS | 3 CT + 3 VT | 2 | I2_I1 | 5 | 7.400 | 7.400 | 0.704 | 0.917 | 0.944 | 0.704 | 2.700 |
| SCIG | TURNS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 16 | 7.400 | 7.400 | 0.731 | 0.931 | 0.972 | 0.731 | 2.700 |
| SCIG | WINDINGS | drive-internal | 0 | Vdconv_2fe | 9 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| SCIG | WINDINGS | 3 CT | 1 | I2_I1 | 5 | 2.300 | 2.300 | 0.981 | 1.000 | 1.000 | 0.981 | 2.300 |
| SCIG | WINDINGS | 3 CT + 3 VT | 2 | I2_I1 | 5 | 2.300 | 2.300 | 0.981 | 1.000 | 1.000 | 0.981 | 2.300 |
| SCIG | WINDINGS | 3 CT + 3 VT + drive | 3 | Vdconv_2fe | 16 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | TURNS | drive-internal | 0 | Iq_2fe | 14 | 11.600 | 11.600 | 0.906 | 0.906 | 0.906 | 0.872 | 11.600 |
| WFSG | TURNS | 3 CT | 1 | Ia_h3 | 7 | 11.600 | 11.600 | 0.983 | 0.983 | 0.983 | 0.863 | 11.600 |
| WFSG | TURNS | 3 CT + 3 VT | 2 | V2_V1 | 8 | 11.600 | 11.600 | 0.983 | 0.983 | 0.983 | 0.983 | 11.600 |
| WFSG | TURNS | 3 CT + 3 VT + drive | 3 | V2_V1 | 24 | 11.600 | 11.600 | 0.983 | 0.983 | 0.983 | 0.983 | 11.600 |
| WFSG | TURNS | excitation (WFSG only) | 0 | If_2fe | 2 | 11.600 | 11.600 | 0.863 | 0.863 | 0.863 | 0.863 | 11.600 |
| WFSG | WINDINGS | drive-internal | 0 | Iq_2fe | 14 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | 3 CT | 1 | I2_I1 | 7 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | 3 CT + 3 VT | 2 | V2_V1 | 8 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
| WFSG | WINDINGS | 3 CT + 3 VT + drive | 3 | Iq_2fe | 24 | 2.300 | 2.300 | 1.000 | 1.000 | 1.000 | 1.000 | 2.300 |
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

| train | test | auc_all | tpr_all | auc_oor | tpr_oor |
|---|---|---|---|---|---|
| PMSG | PMSG | 0.874 | 0.652 | 0.863 | 0.642 |
| SCIG | SCIG | 0.917 | 0.773 | 0.908 | 0.764 |
| WFSG | WFSG | 0.991 | 0.959 | 0.993 | 0.954 |
| PMSG | SCIG | 0.896 | 0.600 | 0.886 | 0.566 |
| PMSG | WFSG | 0.984 | 0.945 | 0.992 | 0.937 |
| SCIG | PMSG | 0.817 | 0.332 | 0.794 | 0.311 |
| SCIG | WFSG | 0.969 | 0.911 | 0.985 | 0.915 |
| WFSG | PMSG | 0.859 | 0.551 | 0.832 | 0.522 |
| WFSG | SCIG | 0.917 | 0.684 | 0.892 | 0.662 |
| SCIG+WFSG | PMSG | 0.841 | 0.422 | 0.818 | 0.392 |
| PMSG+WFSG | SCIG | 0.899 | 0.621 | 0.884 | 0.580 |
| PMSG+SCIG | WFSG | 0.983 | 0.942 | 0.994 | 0.938 |


| machine | n_windows | n_pos | n_oor |
|---|---|---|---|
| PMSG | 24554 | 3391 | 17411 |
| SCIG | 24176 | 3355 | 17201 |
| WFSG | 24871 | 1939 | 10727 |

## R4 transfer, PMSG/SCIG (5-cycle windows)

| calibration | model | train | test | auc_all | tpr_all | auc_oor | tpr_oor |
|---|---|---|---|---|---|---|---|
| raw | logistic | PMSG | PMSG | 0.797 | 0.561 | 0.798 | 0.557 |
| raw | logistic | SCIG | SCIG | 0.791 | 0.573 | 0.799 | 0.575 |
| raw | logistic | PMSG | SCIG | 0.705 | 0.407 | 0.703 | 0.392 |
| raw | logistic | SCIG | PMSG | 0.606 | 0.260 | 0.613 | 0.260 |
| raw | gbdt | PMSG | PMSG | 0.880 | 0.624 | 0.876 | 0.615 |
| raw | gbdt | SCIG | SCIG | 0.898 | 0.660 | 0.904 | 0.662 |
| raw | gbdt | PMSG | SCIG | 0.772 | 0.369 | 0.774 | 0.379 |
| raw | gbdt | SCIG | PMSG | 0.510 | 0.235 | 0.513 | 0.233 |
| healthy-z | logistic | PMSG | PMSG | 0.797 | 0.561 | 0.798 | 0.557 |
| healthy-z | logistic | SCIG | SCIG | 0.791 | 0.573 | 0.799 | 0.575 |
| healthy-z | logistic | PMSG | SCIG | 0.697 | 0.413 | 0.698 | 0.412 |
| healthy-z | logistic | SCIG | PMSG | 0.392 | 0.075 | 0.403 | 0.077 |
| healthy-z | gbdt | PMSG | PMSG | 0.884 | 0.615 | 0.880 | 0.609 |
| healthy-z | gbdt | SCIG | SCIG | 0.900 | 0.660 | 0.906 | 0.657 |
| healthy-z | gbdt | PMSG | SCIG | 0.820 | 0.092 | 0.821 | 0.083 |
| healthy-z | gbdt | SCIG | PMSG | 0.760 | 0.304 | 0.762 | 0.305 |
| self-ref | logistic | PMSG | PMSG | 0.905 | 0.713 | 0.895 | 0.704 |
| self-ref | logistic | SCIG | SCIG | 0.922 | 0.797 | 0.916 | 0.789 |
| self-ref | logistic | PMSG | SCIG | 0.912 | 0.700 | 0.908 | 0.663 |
| self-ref | logistic | SCIG | PMSG | 0.887 | 0.614 | 0.870 | 0.596 |
| self-ref | gbdt | PMSG | PMSG | 0.928 | 0.759 | 0.918 | 0.752 |
| self-ref | gbdt | SCIG | SCIG | 0.944 | 0.827 | 0.937 | 0.821 |
| self-ref | gbdt | PMSG | SCIG | 0.930 | 0.739 | 0.920 | 0.718 |
| self-ref | gbdt | SCIG | PMSG | 0.847 | 0.408 | 0.820 | 0.383 |

## R5 features failing the reliability screen (> 1 of 9 healthy trials)

| window_cycles | machine | feature | healthy_false_alarm | n_false |
|---|---|---|---|---|
| 3 | PMSG | Id_1fe | 0.222 | 2 |
| 3 | PMSG | PId_std | 0.222 | 2 |
| 3 | PMSG | V2_V1 | 0.222 | 2 |
| 3 | PMSG | Tm_1fe | 0.222 | 2 |
| 3 | PMSG | Spd_std | 0.222 | 2 |
| 3 | SCIG | Ia_h3 | 0.222 | 2 |
| 3 | SCIG | Ia_h7 | 0.222 | 2 |
| 3 | SCIG | Id_2fe | 0.222 | 2 |
| 3 | SCIG | Iq_2fe | 0.222 | 2 |
| 3 | SCIG | Vqconv_2fe | 0.222 | 2 |
| 3 | SCIG | PId_2fe | 0.222 | 2 |
| 3 | SCIG | D2_D1 | 0.333 | 3 |
| 3 | SCIG | V2_V1 | 0.222 | 2 |
| 3 | SCIG | Vdc_std | 0.222 | 2 |
| 5 | PMSG | Id_1fe | 0.333 | 3 |
| 5 | PMSG | Vqconv_2fe | 0.222 | 2 |
| 5 | PMSG | PId_std | 0.222 | 2 |
| 5 | PMSG | Spd_std | 0.444 | 4 |
| 5 | SCIG | Ia_h3 | 0.222 | 2 |
| 5 | SCIG | Ia_h7 | 0.333 | 3 |
| 5 | SCIG | Iq_2fe | 0.222 | 2 |
| 5 | SCIG | Vqconv_2fe | 0.222 | 2 |
| 5 | SCIG | D2_D1 | 0.444 | 4 |
| 5 | SCIG | Vdc_std | 0.222 | 2 |
| 8 | PMSG | Id_1fe | 0.222 | 2 |
| 8 | PMSG | Iq_std | 0.222 | 2 |
| 8 | PMSG | Vqconv_2fe | 0.222 | 2 |
| 8 | PMSG | PId_std | 0.333 | 3 |
| 8 | PMSG | Spd_std | 0.444 | 4 |
| 8 | SCIG | Ia_h3 | 0.222 | 2 |
| 8 | SCIG | Ia_h7 | 0.222 | 2 |
| 8 | SCIG | Iq_2fe | 0.444 | 4 |
| 8 | SCIG | Vqconv_2fe | 0.222 | 2 |
| 8 | SCIG | D2_D1 | 0.556 | 5 |
| 8 | SCIG | Vdc_std | 0.444 | 4 |