"""Figure 1.9 — the high-speed trilemma as the text of §1.6.1 actually states it:
a directed cycle of three remedies that each create the next problem, a feasible
design window in the middle, and the power-electronic interface as the gatekeeper
that decides which of two topologies can be reached at all."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse, FancyArrowPatch

plt.rcParams.update({'font.family': 'serif', 'font.serif': ['DejaVu Serif'], 'font.size': 9,
                     'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
                     'savefig.pad_inches': 0.05})
INK, ACC, ACC2, ACC3, GREY = '#1a1a1a', '#1f4e79', '#a6350f', '#4a7c1f', '#555555'

fig, ax = plt.subplots(figsize=(6.8, 6.0))
ax.set_axis_off(); ax.set_xlim(-0.30, 1.30); ax.set_ylim(-0.27, 1.04)

# ── the triangle -------------------------------------------------------------
A, B, C = np.array([0.50, 0.90]), np.array([0.02, 0.20]), np.array([0.98, 0.20])
ax.add_patch(Polygon([A, B, C], closed=True, fc='#f7f7f5', ec=INK, lw=1.7, zorder=1))

def halfwidth(y):                       # triangle half-width at height y
    return (A[1] - y) / (A[1] - B[1]) * (C[0] - B[0]) / 2

# vertices
ax.text(0.50, 0.995, 'MECHANICAL INTEGRITY', ha='center', va='center', fontsize=8.8,
        fontweight='bold', color=INK)
ax.text(0.50, 0.940, 'survive the $r\\Omega^2$ wall:  slender rotor, reinforcement, sleeve',
        ha='center', va='center', fontsize=6.6, color=GREY, style='italic')
ax.text(0.02, 0.125, 'ELECTROMAGNETIC\nEFFICIENCY', ha='center', va='center', fontsize=8.8,
        fontweight='bold', color=INK, linespacing=1.15)
ax.text(-0.29, 0.040, 'power density and low mass:\nhigh pole count, high $f_1$, thin yoke',
        ha='left', va='center', fontsize=6.6, color=GREY, style='italic', linespacing=1.35)
ax.text(0.98, 0.125, 'THERMAL\nMANAGEMENT', ha='center', va='center', fontsize=8.8,
        fontweight='bold', color=INK, linespacing=1.15)
ax.text(1.29, 0.040, 'remove concentrated losses:\naggressive cooling, channels, jackets',
        ha='right', va='center', fontsize=6.6, color=GREY, style='italic', linespacing=1.35)

# ── the directed cycle: each remedy creates the next problem -------------------
def edge_arrow(p, q, offset, rad, f0=0.15, f1=0.85):
    """Arrow from fraction f0 to f1 along edge p->q, displaced outward by `offset`."""
    d = q - p; n = np.array([d[1], -d[0]]) / np.linalg.norm(d)   # outward normal for ccw order
    s, e = p + f0 * d + offset * n, p + f1 * d + offset * n
    ax.add_patch(FancyArrowPatch(s, e, arrowstyle='-|>', mutation_scale=16, lw=1.9,
                                 color=ACC2, connectionstyle=f'arc3,rad={rad}', zorder=4))

def note(x, y, text):
    ax.text(x, y, text, ha='center', va='center', fontsize=6.6, color=ACC2, zorder=6,
            linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.35', fc='white', ec=ACC2, lw=0.7))

edge_arrow(A, B, 0.055, 0.18, 0.20, 0.85)        # mechanical -> electromagnetic (left edge, down)
note(-0.06, 0.60, 'thick carbon-fibre sleeve\n→ larger effective air gap\n→ electromagnetic\n    performance suffers')
edge_arrow(B, C, 0.060, 0.18, 0.23, 0.77)        # electromagnetic -> thermal (base, rightward)
note(0.50, -0.075, 'more poles, higher frequency\n→ iron and windage losses\n→ heat in a volume that cannot shed it')
edge_arrow(C, A, 0.055, 0.18, 0.15, 0.80)        # thermal -> mechanical (right edge, up)
note(1.06, 0.60, 'cooling channels, jacket geometry\n→ lower stator stiffness, higher $l/D$\n→ rotordynamic trouble')

# ── the feasible window, split by the gatekeeper --------------------------------
ax.text(0.50, 0.745, 'feasible high-speed\ndesign window', ha='center', va='center',
        fontsize=6.7, color=GREY, style='italic', zorder=6, linespacing=1.25)
ax.annotate('', xy=(0.50, 0.640), xytext=(0.50, 0.700),
            arrowprops=dict(arrowstyle='-|>', lw=0.8, color=GREY, mutation_scale=9))

yu, yl, gy = 0.548, 0.325, 0.437
ax.add_patch(Ellipse((0.50, yu), 2 * halfwidth(yu) - 0.09, 0.150, fc='#dbe6f0', ec=ACC, lw=1.1, zorder=2))
ax.text(0.50, yu + 0.027, 'low-pole industrial topology', ha='center', va='center', fontsize=6.5,
        fontweight='bold', color=ACC, zorder=6)
ax.text(0.50, yu - 0.022, 'robust rotor, $f_1$ below ~1 kHz\nreachable with silicon IGBT converters',
        ha='center', va='center', fontsize=5.6, color=ACC, zorder=6, linespacing=1.3)

ax.add_patch(Ellipse((0.50, yl), 2 * halfwidth(yl) - 0.16, 0.150, fc='#f6e3da', ec=ACC2, lw=1.1, zorder=2))
ax.text(0.50, yl + 0.027, 'high-pole mobile topology', ha='center', va='center', fontsize=6.8,
        fontweight='bold', color=ACC2, zorder=6)
ax.text(0.50, yl - 0.022, 'mass-minimised, $f_1$ in the kilohertz range\nfeasible only with SiC / GaN switching',
        ha='center', va='center', fontsize=5.8, color=ACC2, zorder=6, linespacing=1.3)

hw = halfwidth(gy) - 0.03
ax.plot([0.5 - hw, 0.5 + hw], [gy, gy], color=ACC3, lw=2.0, ls=(0, (6, 3)), zorder=5)
for x in (0.5 - hw, 0.5 + hw):
    ax.plot([x, x], [gy - 0.022, gy + 0.022], color=ACC3, lw=2.0, zorder=5)
ax.text(0.50, gy, 'POWER ELECTRONIC INTERFACE\nthe gatekeeper', ha='center', va='center',
        fontsize=6.3, fontweight='bold', color=ACC3, zorder=7, linespacing=1.15,
        bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='none'))

ax.text(0.50, -0.215, 'Each remedy at one vertex creates the problem at the next, so the design space '
        'closes on itself;\nthe converter technology then decides which part of the window a machine can occupy.',
        ha='center', va='center', fontsize=6.6, color=GREY, style='italic', linespacing=1.4)

fig.savefig('figures/fig_trilemma.png'); plt.close(fig)
print('generated figures/fig_trilemma.png')
