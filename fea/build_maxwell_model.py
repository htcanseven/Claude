"""
PyAEDT builder for the Brno benchmark IPMSM (Zezula et al., IEEE TIE 73(1) 2026).

    !!  UNTESTED  !!
    Written without access to an AEDT installation. Treat as a structured starting
    point: the geometry logic and the matrix strategy are the substance, but every
    PyAEDT call needs checking against your installed version. API names moved when
    pyaedt was renamed to ansys-aedt-core in 2024.

Strategy
--------
Two designs, because they need different symmetry:

  calibration : 60-degree sector, ANTI-PERIODIC boundary.
                GCD(36,42)=6 -> 6 sectors of 6 slots / 7 poles; 7 is odd, so the
                field is anti-symmetric across the sector. Used to match
                lambda_pm, Ld, Lq, L0 against the published table. Cheap.

  faultmatrix : FULL 360 degrees, no symmetry.
                Exciting one turn breaks sector symmetry, so periodic boundaries
                are invalid here. Each of the 25 turns of one coil becomes its own
                winding; request the inductance matrix; solve ONCE. Every fault
                window is then a submatrix sum (see lf_from_matrix.py).

Machine data (published)
------------------------
  42 poles (PP=21), ns=6 coils/phase, 25 turns/coil -> 150 turns/phase
  Rs 727 mOhm, Rc 362 mOhm, Ld 3.29 mH, Lq 3.12 mH, L0 2.74 mH
  lambda_pm,1 18.4 mWb, lambda_pm,3 200 uWb
  Nominal 6.89 A, 3.78 Nm, 638 rpm, 253 W

Geometry is NOT published. Slot/pole is inferred as 36s/42p single-layer
(ns=6 -> 18 coils -> 36 slots single-layer; base unit 6s/7p, the 12s/14p family).
CONFIRM against Fig. 3 of the paper before trusting anything here.
Main dimensions follow from lambda_pm: D_bore * L_stk ~ 3.1e-3 m^2.
"""

try:
    from ansys.aedt.core import Maxwell2d          # 2024+
except ImportError:
    from pyaedt import Maxwell2d                   # legacy

import numpy as np

# ----------------------------------------------------------------------------
# Parameters. Tune the starred ones to hit the calibration targets.
# ----------------------------------------------------------------------------
P = dict(
    aedt_version = "2024.2",
    project      = "brno_ipmsm",

    n_slots      = 36,
    n_poles      = 42,
    n_turns      = 25,          # per coil segment

    # main dimensions: D_bore * L_stk ~ 3.1e-3 m^2 from lambda_pm
    r_bore       = 55.0,        # mm, stator inner radius
    l_stk        = 30.0,        # mm
    r_stator_out = 75.0,        # mm
    airgap       = 0.7,         # mm

    slot_depth   = 14.0,        # mm  * drives leakage -> L0
    slot_width   = 4.4,         # mm  * drives leakage -> L0
    slot_open    = 2.0,         # mm  * tooth tip opening
    tooth_tip_h  = 1.0,         # mm

    mag_depth    = 3.0,         # mm  * buried depth -> saliency (target Ld/Lq ~ 1.05)
    mag_thick    = 2.5,         # mm  * -> lambda_pm
    mag_width    = 6.0,         # mm  * -> lambda_pm
    bridge       = 0.6,         # mm  * -> leakage / saliency

    steel        = "M270-35A",  # substitute your library grade
    magnet       = "N38SH",

    i_probe      = 1.0,         # A, small probe current for linear L extraction
)

# Calibration targets from the published table
TARGETS = dict(Ld_mH=3.29, Lq_mH=3.12, L0_mH=2.74, lam_pm1_mWb=18.4, Rs_mOhm=727.0)


def turn_centres(P):
    """Radial centres of the 25 turns stacked through the slot depth.

    Index 0 = slot BOTTOM (deepest, largest leakage linkage), index 24 = opening.
    This ordering must match lf_from_matrix.py.
    """
    r_in  = P["r_bore"] + P["tooth_tip_h"]              # slot starts above the tip
    h     = P["slot_depth"]
    n     = P["n_turns"]
    # bottom = deepest = largest radius for an inner-rotor stator
    depths = (np.arange(n) + 0.5) * h / n               # 0 = opening side
    return r_in + h - depths                            # index 0 -> deepest


def build(design="faultmatrix"):
    """Build one of the two designs. Returns the Maxwell2d handle."""
    full = (design == "faultmatrix")

    m2d = Maxwell2d(project=P["project"], design=design,
                    solution_type="Magnetostatic",
                    version=P["aedt_version"], non_graphical=False)

    # --- design variables, so geometry stays parametric for calibration sweeps
    for k in ("r_bore", "r_stator_out", "slot_depth", "slot_width", "slot_open",
              "tooth_tip_h", "airgap", "mag_depth", "mag_thick", "mag_width",
              "bridge"):
        m2d[k] = f"{P[k]}mm"
    m2d["l_stk"] = f"{P['l_stk']}mm"

    # ------------------------------------------------------------------
    # VERIFY FROM HERE DOWN -- geometry construction is the part most likely
    # to need adaptation to your PyAEDT version and modelling preferences.
    # Sketch of the intended sequence:
    #
    #   1. stator yoke annulus            modeler.create_circle x2 + subtract
    #   2. one slot profile               create_polyline(..., cover_surface=True)
    #   3. duplicate_around_axis          n_slots (or 6 for the sector design)
    #   4. subtract slots from yoke
    #   5. rotor annulus + magnet pockets, duplicate_around_axis n_poles
    #   6. band / airgap objects
    #   7. region + vector potential A=0 on the outer edge
    #   8. sector design only: assign_master_slave(..., same_as_master=False)
    #      for ANTI-periodic symmetry
    # ------------------------------------------------------------------

    if full:
        _assign_turn_windings(m2d)
    return m2d


def _assign_turn_windings(m2d):
    """One winding per turn: + conductor in slot A, - conductor in slot B.

    A single-layer tooth coil wraps one tooth, so each turn has a go-conductor in
    the slot on one side and a return-conductor in the slot on the other. Turn k
    is therefore a 2-object winding with opposite polarities.
    """
    names = []
    for k in range(P["n_turns"]):
        w = f"turn_{k:02d}"
        m2d.assign_winding(assignment=None, winding_type="Current",
                           current=P["i_probe"], name=w)
        m2d.assign_coil(assignment=[f"cond_A_{k:02d}"], conductors_number=1,
                        polarity="Positive", name=f"{w}_A")
        m2d.assign_coil(assignment=[f"cond_B_{k:02d}"], conductors_number=1,
                        polarity="Negative", name=f"{w}_B")
        m2d.add_winding_coils(assignment=w, coils=[f"{w}_A", f"{w}_B"])
        names.append(w)

    # THE key step: one matrix -> every fault window by submatrix summation
    m2d.assign_matrix(assignment=names, matrix_name="TurnMatrix")
    return names


def solve_and_export(m2d, csv_out="turn_matrix.csv"):
    """Solve and write the 25x25 inductance matrix for lf_from_matrix.py.

    IMPORTANT: demagnetise the magnets (Br = 0) for inductance extraction, or use
    frozen permeability from an operating point. With magnets active the solution
    is not a pure inductance measurement.
    """
    setup = m2d.create_setup(name="MS")
    setup.props["MaximumPasses"]   = 12
    setup.props["PercentError"]    = 0.5
    setup.update()
    m2d.analyze_setup("MS")

    # Export route differs across versions -- check post.get_solution_data /
    # the Matrix report for "Matrix1.L(turn_i,turn_j)" style expressions.
    raise NotImplementedError(
        "Export the TurnMatrix inductance matrix as a 25x25 CSV, then run:\n"
        "    python fea/lf_from_matrix.py  (swap synthetic_slot_matrix for\n"
        "    load_maxwell_matrix('turn_matrix.csv'))")


if __name__ == "__main__":
    print(__doc__)
    print("Calibration targets:", TARGETS)
    print("\nTurn radial centres (mm), index 0 = slot bottom:")
    print(np.round(turn_centres(P), 2))
