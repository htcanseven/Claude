"""Round-2 additions: the decision table with the share at the required level and with tap-pair resampling within
a level (both units), the incremental negative-sequence impedance per speed, and the operating-envelope table of
the fixed features (median SDR and detectable share by speed). Writes results/tables/R_decision_table*.csv,
R_z2_by_speed.csv and R_envelope_fixed.csv. Run after revision.py (uses the same caches)."""
import numpy as np
import pandas as pd

import compare as C
import compare3 as C3
import revision as R

TAB = C.TAB


def z2_by_speed(win, machines=("PMSG", "SCIG")):
    """Median |dV2c/dI2c| per machine, class and speed (five-cycle windows), with interquartile ranges."""
    w, pre_e, pre_l, flt = C.interval_means(win, ["I2r_I1", "V2r_V1", "I1", "V1"])
    meta = w.groupby("rid")[["machine", "ftype", "speed_rpm"]].first()
    di = ((flt.I2c_re + 1j * flt.I2c_im) - (pre_l.I2c_re + 1j * pre_l.I2c_im)) * pre_l.I1
    dv = ((flt.V2c_re + 1j * flt.V2c_im) - (pre_l.V2c_re + 1j * pre_l.V2c_im)) * pre_l.V1
    z = dv / di
    out = meta.join(pd.DataFrame({"dI2c_A": di.abs() / np.sqrt(2), "dV2c_V": dv.abs() / np.sqrt(2), "Z2_ohm": z.abs()}))
    rows = []
    for m in machines:
        for ft in ["TURNS", "WINDINGS"]:
            for sp, s in out[(out.machine == m) & (out.ftype == ft)].groupby("speed_rpm"):
                rows.append(dict(machine=m, ftype=ft, speed_rpm=int(sp), n=len(s), fe_hz=None,
                                 dI2c_A_rms=s.dI2c_A.median(), dV2c_V_rms=s.dV2c_V.median(),
                                 Z2_ohm=s.Z2_ohm.median(), Z2_q25=s.Z2_ohm.quantile(.25), Z2_q75=s.Z2_ohm.quantile(.75)))
    return pd.DataFrame(rows)


def envelope_fixed(sdr_path=TAB / "sdr_per_recording.csv"):
    """Median SDR and detectable share of the fixed inter-turn and inter-winding features of Table 4 by speed
    and by torque (five-cycle windows)."""
    d = pd.read_csv(sdr_path)
    fixed = {"PMSG": {"TURNS": ["V2r_V1", "I2r_I1", "D2r_D1"], "WINDINGS": ["V2r_V1", "I2r_I1", "D2r_D1"]},
             "SCIG": {"TURNS": ["I2r_I1", "D2r_D1", "V2r_V1"], "WINDINGS": ["I2r_I1", "PId_2fe", "V2r_V1"]}}
    rows = []
    for m, fts in fixed.items():
        for ft, feats in fts.items():
            s = d[(d.machine == m) & (d.ftype == ft)]
            for f in feats:
                col = f"{f}__sdr"
                r = dict(machine=m, ftype=ft, feature=f)
                for sp, g in s.groupby("speed_rpm"):
                    r[f"median_{int(sp)}"] = g[col].median()
                    r[f"share_{int(sp)}"] = float((g[col] >= 1).mean())
                tq = s.groupby(["speed_rpm", "torque_Nm"])[col].median()
                r["torque_factor_max"] = max(tq.loc[v].max() / tq.loc[v].min() for v in s.speed_rpm.unique())
                rows.append(r)
    return pd.DataFrame(rows)


def main():
    env = envelope_fixed()
    env.to_csv(TAB / "R_envelope_fixed.csv", index=False)
    print(env.round(2).to_string(index=False))

    files5, win5 = C.load()
    zs = z2_by_speed(win5)
    zs.to_csv(TAB / "R_z2_by_speed.csv", index=False)
    print(zs.round(2).to_string(index=False))

    for unit, suffix in [("trials", ""), ("pairs", "_pairs")]:
        dec5, sel5 = R.decision_table(win5, C.ALL_FEATS, machines=["PMSG", "SCIG"], unit=unit, suites=R.SUITES5)
        dec5.to_csv(TAB / f"R_decision_table_5c{suffix}.csv", index=False)
        sel5.to_csv(TAB / f"R_decision_cheapest_5c{suffix}.csv", index=False)
        print(unit, "5c done")
    files, win = C3.load3()
    feats = [f for f in C3.FEATS3 if f in win.columns or f in C.RESID]
    for unit, suffix in [("trials", ""), ("pairs", "_pairs")]:
        dec, sel = R.decision_table(win, feats, unit=unit)
        dec.to_csv(TAB / f"R_decision_table{suffix}.csv", index=False)
        sel.to_csv(TAB / f"R_decision_cheapest{suffix}.csv", index=False)
        print(unit, "3c done")


if __name__ == "__main__":
    main()
