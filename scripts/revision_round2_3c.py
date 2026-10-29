"""Re-run only the three-cycle decision tables (both resampling units) after the at-level rule was mapped to the
lowest tested level at or above the requirement (the WFSG's inter-winding levels are its own extents)."""
import compare as C
import compare3 as C3
import revision as R

files, win = C3.load3()
feats = [f for f in C3.FEATS3 if f in win.columns or f in C.RESID]
for unit, suffix in [("trials", ""), ("pairs", "_pairs")]:
    dec, sel = R.decision_table(win, feats, unit=unit)
    dec.to_csv(C.TAB / f"R_decision_table{suffix}.csv", index=False)
    sel.to_csv(C.TAB / f"R_decision_cheapest{suffix}.csv", index=False)
    print(unit, "3c done", flush=True)
