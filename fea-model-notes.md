# Building the FEA Model — Notes

*How to prepare the finite-element model for the EPEi conference paper, given that the
benchmark motor's geometry is not published. Companion to `conference-paper-idea.md`.*

## 1. Key derivation: this machine is leakage-dominated

From Zezula et al., TIE 73(1) 2026, Table II: Ld = 3.29 mH, Lq = 3.12 mH, L0 = 2.74 mH.

Zero-sequence inductance carries no fundamental magnetizing component, so it is
essentially the leakage inductance. With (Ld + Lq)/2 = 3.21 mH:

    L_leak ~ 2.74 mH        L_mag ~ 0.47 mH        => leakage is ~85% of total

Consistent with 42 poles + tooth-coil winding: small pole pitch weakens the magnetizing
path, slot/tooth leakage dominates. The near-zero saliency (Ld slightly ABOVE Lq)
is the same effect.

## 2. Why this de-risks the paper

Split the fault physics:

- **EMF driving the fault current** — comes from flux encircling the tooth. All turns of
  a tooth coil encircle the same tooth, so PM-induced EMF per turn is roughly
  position-independent. The r/N assumption is adequate here.
- **Fault-loop inductance L_f limiting that current** — built in their model by scaling
  terminal inductances with the turn ratio. But slot-leakage flux links turns very
  unevenly: flux crossing the slot at height h links only conductors below h. A turn at
  the slot bottom sits in a different leakage environment from one at the slot opening.

Position dependence therefore enters through **L_f** — and this machine is precisely the
one where leakage, hence L_f, dominates.

## 3. Falsifiable pre-FEA test (the week-1 gate)

Fault current is resistance-limited at high Rsc and inductance-limited at low Rsc. The
benchmark sweeps Rsc = 442 -> 47.0 -> 5.62 -> 1.74 mOhm, crossing that transition.

> **Prediction:** if L_f carries a turn-position error, the model residual
> (if_meas - if_new) should GROW as Rsc falls, and be small at 442 mOhm.

Testable immediately from `Data_diverse_FI/Rsc_changes_*.mat` with no FEA. Flat residual
across Rsc => L_f hypothesis dead, two days spent. Growing residual => paper confirmed,
and FEA only has to quantify a mechanism already demonstrated.

**This is the answer to the geometry problem.** The FEA does not PREDICT the effect, it
EXPLAINS an effect the data already shows. Explanation tolerates approximate geometry;
prediction does not. That is what defuses the "your geometry is guessed" review.

## 4. What is known / derivable about the machine

Table I/II values are mutually consistent — verified:
T = 1.5 * PP * lambda_pm * iq = 1.5*21*0.0184*6.52 = 3.78 Nm; P = 3.78 * 638 rpm = 253 W.

| Quantity | Value | Source |
|---|---|---|
| Poles | 42 (PP = 21) | Table II |
| Coils/phase, turns/coil | ns = 6, 25 turns -> 150 turns/phase | Table II + text |
| Likely slot/pole | **36 slots / 42 poles, single-layer tooth-coil** | ns = 6 => 18 coils => 36 slots single-layer; base unit 6s/7p, same family as 12s/14p, high winding factor. **CONFIRM against their Fig. 3** |
| Size constraint | D_bore * L_stk ~ 3.1e-3 m^2 | from lambda_pm,1 = 18.4 mWb, kw ~ 0.96, Bg1 ~ 0.85 T |
| Suggested split | D ~ 110 mm, L ~ 30 mm | ~7 kPa shear stress, normal for a small lab servo |
| Slot area | ~85 mm^2 for 25 turns | k_fill 0.4, J ~ 5 A/mm^2 |

**Calibration targets:** Rs = 727 mOhm, Ld = 3.29 mH, Lq = 3.12 mH, **L0 = 2.74 mH**,
lambda_pm,1 = 18.4 mWb, lambda_pm,3 = 200 uWb.

Weight L0 most heavily — it is the direct handle on leakage, the quantity the paper
turns on.

## 5. Build procedure

**Transient co-simulation is NOT required.** L_f as a function of which turns are
shorted is a magnetostatic quantity.

1. **Geometry.** 36s/42p single-layer; GCD(36,42) = 6 so solve one 60-degree sector with
   periodic boundaries. Interior magnets; tune magnet depth and bridge width until
   Ld/Lq ~ 1.05 and L0 ~ 2.74 mH.
2. **Turn-level conductors.** Model the 25 turns of one coil as 25 individually
   addressable regions stacked through the slot depth. The only non-standard step, and
   the core of the paper.
3. **Extract L_f(r, position).** Drive current in a chosen turn subset, solve
   magnetostatically, take flux linkage -> fault-loop self-inductance. Repeat for each
   contiguous r-turn window at each slot position, r = 3, 6, 10 to match their
   severities.
4. **Compare** with their formula
   Lf1 = (r/ns) * np(ns-1) * (Ld+Lq+L0)/3 + (1/3)(r/ns)L0 + (ns/r) Lwire.
   The ratio L_f,FEA / L_f,model versus turn position is the headline figure.
5. **Optional (load dependence).** Re-solve with stator current applied to capture local
   saturation — the 1 Nm vs 3 Nm axis, the backup contribution.

~50-100 magnetostatic solves on a 60-degree sector: minutes of compute. Maxwell 2D,
JMAG, MotorCAD FEA, or FEMM via pyFEMM (free, scriptable) all suffice. No transient
solver, no external circuit coupling needed.

## 6. Effort

| Task | Time |
|---|---|
| Residual analysis from shipped data (the gate) | 2 days |
| Geometry build + calibration to 5 targets | 3-4 days |
| Turn-level parametrisation + L_f sweep | 2-3 days |
| Figures + writing | 4-5 days |

~2 weeks total; the first 2 days decide whether the rest is worth doing.

## 7. Open items

- Confirm the 36s/42p single-layer inference against Fig. 3 of the TIE 2026 paper.
- Note Lwire = 3.81 uH (their FIU parasitic) scales as ns/r — it affects LOW shorted-turn
  counts most, i.e. the same direction as the position effect. Must be separated from
  the L_f error in the analysis, or it becomes a confound.
