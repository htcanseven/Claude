"""Numerical verification of the scaling relations used in Chapter 1.

Three design paths are compared, all starting from the same baseline machine:
  (a) FIXED GEOMETRY  : overspeed an existing design (D, l fixed)
  (b) TIP-SPEED PATH  : hold P and v_tip constant, let D shrink and l grow
  (c) ROTORDYNAMIC    : as (b) but with l capped at 1.5x baseline
"""
import numpy as np

# ---- baseline machine (Voltcar-like) -------------------------------------
D0, l0, n0, P0, p = 0.096, 0.130, 30000.0, 120.0, 3      # m, m, r/min, kW, pole pairs
w0 = 2*np.pi*n0/60
vtip0 = np.pi*D0*n0/60
f0 = p*n0/60
print(f"BASELINE: D={D0*1000:.0f} mm  l={l0*1000:.0f} mm  n={n0:.0f} r/min")
print(f"          v_tip={vtip0:.1f} m/s   f1={f0:.0f} Hz   l/D={l0/D0:.2f}")
print(f"          n*sqrt(P) = {n0*np.sqrt(P0):,.0f}    fP = {f0*P0:,.0f} kW/s\n")

k = 2.0   # speed multiplier

def report(name, D, l, w):
    """All losses normalised to the baseline."""
    vtip = w*D/2
    # P propto D^2 l w  (B, A held constant)
    P    = (D/D0)**2 * (l/l0) * (w/w0)
    # sigma propto v_tip^2
    sig  = (vtip/vtip0)**2
    # windage propto D^4 l w^3
    wind = (D/D0)**4 * (l/l0) * (w/w0)**3
    # iron loss propto f^2 * iron mass;  mass propto D^2 l
    fe   = (w/w0)**2 * (D/D0)**2 * (l/l0)
    # DC copper propto J^2 * Vcu ; Vcu propto D*l at constant A, J
    cu   = (D/D0)*(l/l0)
    # rotor lateral surface propto D*l
    surf = (D/D0)*(l/l0)
    # 1st bending critical: f_c propto r / l^2  (uniform beam)
    fc   = (D/D0)/(l/l0)**2
    print(f"{name}")
    print(f"  D={D/D0:5.2f}x  l={l/l0:5.2f}x  l/D={(l/D)/(l0/D0):5.2f}x  v_tip={vtip:6.1f} m/s ({sig:4.2f}x stress)")
    print(f"  P={P:5.2f}x | P_Cu={cu:5.2f}x  P_Fe={fe:5.2f}x  P_wind={wind:5.2f}x | surface={surf:5.2f}x")
    print(f"  n_crit={fc:5.3f}x   ->  n_op/n_crit = {(w/w0)/fc:6.2f}x\n")

# (a) fixed geometry
report("(a) FIXED GEOMETRY, speed x2", D0, l0, k*w0)

# (b) tip-speed-limited, constant power:  D propto 1/w, l propto w
report("(b) TIP-SPEED LIMITED, P const, speed x2", D0/k, l0*k, k*w0)

# (c) rotordynamically capped length (l can only grow 1.5x);
#     D then set to recover power:  D^2 = P0/(l*w) -> D propto 1/sqrt(l*w)
lc = 1.5*l0
Dc = D0*np.sqrt((l0/lc)*(w0/(k*w0)))
report("(c) l CAPPED at 1.5x, P const, speed x2", Dc, lc, k*w0)

print("="*66)
print("ANALYTIC EXPONENTS on path (b), quantity propto w^x :")
for q, x in [("rotor radius r",-1),("active length l",1),("l/D ratio",2),
             ("active volume",-1),("power density",1),("rotor surface",0),
             ("centrifugal stress",0),("fundamental freq",1),("DC copper loss",0),
             ("iron loss (a=2)",1),("windage loss",0),("1st critical speed",-3),
             ("n_op / n_crit",4)]:
    print(f"   {q:24s} w^{x:<3d}   doubling speed -> x{2.0**x:.2f}")
