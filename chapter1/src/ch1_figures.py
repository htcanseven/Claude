"""Every figure of Chapter 1, drawn in the house style (src/hsbook_style.py).

Each figure is built at the full text width with all text at the body size, so
it is inserted in the manuscript at 100 % and prints exactly as drawn.

usage:  python3 src/ch1_figures.py [1.1 1.3 ...]      (run from chapter1/)
Writes figures/ch1/fig_1_NN.{png,pdf,svg}.  Figure 1.4 plots the mode shapes in
data/fig_1_04_modes.csv, traced from the authors' MATLAB figure by
src/trace_fig_1_04.py until the model's own output replaces them.
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyBboxPatch, Ellipse, FancyArrowPatch

sys.path.insert(0, 'src')
import hsbook_style as hs
from hsbook_style import INK, BLUE, RUST, GREEN, GREY, FILL, SIZE

hs.setup()
OUT = 'figures/ch1/fig_'
FIGS = {}


def fig(num):
    def reg(fn):
        FIGS[num] = fn
        return fn
    return reg


# ───────────────────────────────────────────────────────────────── Fig. 1.1
@fig('1.1')
def classification_map():
    f, ax = hs.figure(9.0)
    P = np.logspace(-1, 4, 400)
    ax.loglog(P, 1e5 / np.sqrt(P), color=BLUE, ls='-', label=r'$n\sqrt{P} = 100\,000$')
    ax.loglog(P, 60 * 1.8e5 / (3 * P), color=RUST, ls='--',
              label=r'$f_1P = 180\,000$ kW/s at $p = 3$')
    for p in (1, 6):                                     # the same fP threshold, other pole pairs
        ax.loglog(P, 60 * 1.8e5 / (p * P), color=RUST, ls=':', lw=hs.LW_THIN,
                  label=r'the same $f_1P$ at $p = 1$ and $p = 6$' if p == 1 else None)
    ax.plot(120, 30000, 'o', ms=7, mfc='white', mec=INK, mew=1.2, zorder=6)
    hs.leader(ax, 'machine of Table 1.1', xy=(120, 30000), xytext=(330, 1.5e5), ha='left')
    ax.text(1.25e3, 60 * 1.8e5 / 1.25e3 * 1.15, r'$p = 1$', color=RUST, ha='left', va='bottom')
    ax.text(22, 60 * 1.8e5 / (6 * 22) * 0.72, r'$p = 6$', color=RUST, ha='right', va='top')
    ax.legend(loc='lower left')
    ax.set_xlim(0.1, 1e4); ax.set_ylim(1e3, 5e5)
    hs.plain_log(ax.xaxis); hs.plain_log(ax.yaxis)
    ax.set_xlabel(hs.label('Rated power', 'P', 'kW'))
    ax.set_ylabel(hs.label('Rated speed', 'n', 'r/min'))
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.3
@fig('1.3')
def stress_vs_tipspeed():
    f, ax = hs.figure(8.6)
    v = np.linspace(0, 350, 400); rho, nu = 7650., 0.3
    ring, = ax.plot(v, rho * v ** 2 / 1e6, color=GREEN, ls='-.', label='thin ring (sleeve)')
    bore, = ax.plot(v, (3 + nu) / 4 * rho * v ** 2 / 1e6, color=RUST, ls='--',
                    label='disc with central bore')
    solid, = ax.plot(v, (3 + nu) / 8 * rho * v ** 2 / 1e6, color=BLUE, ls='-', label='solid disc')
    ax.legend(handles=[ring, bore, solid], loc='upper left')
    for y, t in [(450, r'high-strength electrical steel, $R_{\mathrm{p0.2}}$'),
                 (300, 'design limit at safety factor 1.5')]:
        ax.axhline(y, color=GREY, lw=hs.LW_THIN, ls=(0, (2, 2)))
        ax.text(6, y + 9, t, color=INK, va='bottom')
    ax.axvline(150, color=GREY, lw=hs.LW_THIN)
    ax.text(154, 655, r'$v_{\mathrm{tip}} = 150$ m/s', color=INK, va='top', ha='left')
    ax.set_xlim(0, 350); ax.set_ylim(0, 700)
    ax.set_xlabel(hs.label('Peripheral speed', 'v_tip', 'm/s'))
    ax.set_ylabel(hs.label('Maximum tangential stress', None, 'MPa'))
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.4
# The rotor of the authors' model as the original MATLAB figure draws it, read
# off that figure at its own scale (z along the rotor from the NDE, r radius, m).
R_SHAFT = [(0.000, 0.103, 0.031), (0.103, 0.155, 0.057), (0.155, 0.172, 0.065),
           (0.172, 0.191, 0.069), (0.191, 0.331, 0.070), (0.331, 0.369, 0.085),
           (0.369, 0.409, 0.088), (0.409, 0.430, 0.121), (0.430, 0.993, 0.043),
           (0.993, 1.014, 0.121), (1.014, 1.053, 0.088), (1.053, 1.092, 0.085),
           (1.092, 1.437, 0.070), (1.437, 1.508, 0.057), (1.508, 1.516, 0.040),
           (1.516, 1.565, 0.057), (1.565, 1.582, 0.064), (1.598, 1.618, 0.061),
           (1.618, 1.661, 0.057), (1.661, 1.678, 0.0236), (1.678, 1.765, 0.0195),
           (1.765, 1.781, 0.0227), (1.781, 1.796, 0.085), (1.796, 2.041, 0.067),
           (2.041, 2.111, 0.057), (2.111, 2.141, 0.035)]
R_AMB = [(0.191, 0.331, 0.085), (1.092, 1.412, 0.085), (1.796, 2.008, 0.085)]  # laminated sleeves
R_ACTIVE = (0.430, 0.993, 0.128)
R_DISCS = [(0.000, 0.103, 0.044), (0.054, 0.066, 0.090), (0.102, 0.112, 0.067),
           (0.172, 0.191, 0.087), (1.412, 1.432, 0.087), (1.582, 1.598, 0.084),
           (2.008, 2.030, 0.087), (2.112, 2.132, 0.150)]
Z_ACTUATOR = (0.290, 1.313, 1.930)          # radial AMB actuator planes in the model
MODE_FREQ = (55.9, 293, 590.1, 905.8)       # Hz


@fig('1.4')
def rotor_modes():
    """The rotor drawn to scale above its first four bending mode shapes, which
    share its axial scale, so each deflection sits under the part it belongs to.
    The curves were traced from the original MATLAB figure (src/trace_fig_1_04.py)."""
    data = np.genfromtxt('data/fig_1_04_modes.csv', delimiter=',', skip_header=3, names=True)
    H, L, R = 9.15, 1.30, 0.25                  # canvas height; graph margins (cm)
    zmin, zmax = -0.03, 2.17
    S = (hs.W_CM - L - R) / (zmax - zmin)       # cm per metre, both drawing and graph
    gb, gh = 1.30, 4.55                          # graph bottom and height (cm)
    ya = gb + gh + 0.32 + 0.150 * S              # rotor axis
    f, ax = hs.canvas(H)
    X = lambda z: L + (z - zmin) * S

    def body(z0, z1, r, fc, z=3, lw=hs.LW_OUTLINE):
        ax.add_patch(Rectangle((X(z0), ya - r * S), (z1 - z0) * S, 2 * r * S, fc=fc, ec=INK,
                               lw=lw, zorder=z))

    for z0, z1, r in R_SHAFT:
        body(z0, z1, r, FILL['steel'])
    for z0, z1, r in R_DISCS:
        body(z0, z1, r, FILL['steel'], z=4, lw=hs.LW_THIN * 1.4)
    for z0, z1, r in R_AMB:
        hs.laminated(ax, X(z0), X(z1), ya - r * S, ya + r * S, pitch=0.11, z=4)
    body(*R_ACTIVE, FILL['rotor'], z=4)
    ax.plot([X(-0.02), X(2.16)], [ya, ya], color=GREY, lw=hs.LW_THIN,
            ls=(0, (9, 2.5, 1.5, 2.5)), zorder=6)

    yl = ya + 0.150 * S + 0.55                   # the row of labels
    for z, dx in zip(Z_ACTUATOR, (0, 0, -0.70)):    # the DE label kept clear of 'DE'
        hs.leader(ax, 'radial AMB', xy=(X(z), ya + 0.085 * S), xytext=(X(z) + dx, yl))
    hs.leader(ax, 'active part', xy=(X(0.71), ya + 0.128 * S), xytext=(X(0.71), yl))
    ax.text(X(0.0), yl, 'NDE', ha='center', va='center')
    ax.text(X(2.122), yl, 'DE', ha='center', va='center')

    g = f.add_axes((L / hs.W_CM, gb / H, (hs.W_CM - L - R) / hs.W_CM, gh / H))
    for z in Z_ACTUATOR:                         # bearing planes, from the AMB down
        g.axvline(z, color=GREY, lw=hs.LW_THIN, zorder=1)
        ax.plot([X(z), X(z)], [gb + gh, ya - 0.085 * S], color=GREY, lw=hs.LW_THIN, zorder=2)
    g.axhline(0, color=INK, lw=hs.LW_THIN, zorder=1)
    for k, (col, ls) in enumerate(zip(hs.CYCLE_COLOURS, hs.CYCLE_STYLES)):
        g.plot(data['z_m'], data[f'mode{k + 1}'], color=col, ls=ls,
               label=f'mode {k + 1}, $f$ = {MODE_FREQ[k]:g} Hz')
    g.legend(loc='lower center', ncols=2, bbox_to_anchor=(0.41, 0.0), columnspacing=1.6)
    g.set_xlim(zmin, zmax); g.set_ylim(-1.18, 1.18)
    g.set_xticks([0, 0.5, 1, 1.5, 2]); g.set_yticks([-1, -0.5, 0, 0.5, 1])
    g.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    g.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: hs.number(v)))
    g.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: hs.number(v)))
    g.set_xlabel(hs.label('Axial position', 'z', 'm'))
    g.set_ylabel('Normalised deflection')
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.5
@fig('1.5')
def loss_scaling():
    """Loss components at fixed geometry, from the scaling laws stated in the caption.

    Losses in per cent of rated output at rated speed (illustrative):
    copper 2.8 (constant), iron 1.0 (∝ n²), windage 0.4 (∝ n³). Output grows
    linearly with speed at constant torque, so efficiency peaks where the
    tangent from the origin touches the total-loss curve: beyond that point the
    loss grows faster than the output.
    """
    f, ax = hs.figure(9.0)
    n = np.linspace(0, 3, 400)
    cu, fe, wi = 2.8 + 0 * n, 1.0 * n ** 2, 0.4 * n ** 3
    tot = cu + fe + wi
    ax.plot(n, cu, color=BLUE, ls='-')
    ax.plot(n, fe, color=RUST, ls='--')
    ax.plot(n, wi, color=GREEN, ls='-.')
    ax.plot(n, tot, color=INK, ls='-', lw=hs.LW_DATA * 1.4)
    # efficiency maximum: minimum of loss/output, i.e. the tangent from the origin
    k = np.argmin(tot[1:] / n[1:]) + 1
    ns, ls_ = n[k], tot[k]
    ax.plot([0, 1.95], [0, 1.95 * ls_ / ns], color=GREY, lw=hs.LW_THIN, ls=(0, (2, 2)))
    ax.plot(ns, ls_, 'o', ms=6.5, mfc='white', mec=INK, mew=1.2, zorder=6)
    hs.leader(ax, 'efficiency maximum:\nbeyond it, loss grows\nfaster than output',
              xy=(ns, ls_), xytext=(0.62, 13.3), ha='center', linespacing=1.15)
    ax.text(2.97, 2.8 - 0.45, r'copper, $\approx$ constant', color=BLUE, ha='right', va='top')
    ax.text(2.97, 5.0, r'iron, $\propto n^2$', color=RUST, ha='right', va='top')
    ax.text(2.62, 0.4 * 2.62 ** 3 + 0.5, r'windage, $\propto n^3$', color=GREEN, ha='right', va='bottom')
    ax.text(2.40, tot[np.searchsorted(n, 2.40)] + 0.5, 'total', color=INK, ha='right', va='bottom')
    ax.set_xlim(0, 3); ax.set_ylim(0, 24)
    ax.set_xlabel(r'Speed relative to rated $n/n_{\mathrm{N}}$')
    ax.set_ylabel('Loss (% of rated output)')
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.6
@fig('1.6')
def converter_gate():
    f, ax = hs.figure(9.0)
    f1 = np.logspace(np.log10(30), np.log10(5e3), 400)
    ax.fill_between(f1, 2e3, 16e3, color=RUST, alpha=0.13, lw=0)
    ax.fill_between(f1, 16e3, 120e3, color=GREEN, alpha=0.13, lw=0)
    ax.loglog(f1, 21 * f1, color=BLUE, ls='-')
    ax.loglog(f1, 10 * f1, color=BLUE, ls=':')
    ax.text(4700, 2.4e3, 'silicon IGBT,\npractical range', color=RUST, ha='right', va='bottom',
            linespacing=1.1)
    ax.text(36, 1.0e5, 'SiC and GaN, practical range', color=GREEN, va='top')
    ax.text(330, 21 * 330 * 1.22, r'$m_{\mathrm{f}} = 21$', color=BLUE, ha='right', va='bottom',
            rotation=0)
    ax.text(700, 10 * 700 * 0.80, r'$m_{\mathrm{f}} = 10$', color=BLUE, ha='left', va='top')
    ax.plot(1500, 31500, 'o', ms=7, mfc='white', mec=INK, mew=1.2, zorder=6)
    hs.leader(ax, 'machine of Table 1.1:\n$f_1 = 1500$ Hz needs\n$f_{\\mathrm{sw}} = 31.5$ kHz',
              xy=(1500, 31500), xytext=(330, 4.6e4), ha='center', linespacing=1.15)
    ax.set_xlim(30, 5e3); ax.set_ylim(1e3, 2e5)
    hs.plain_log(ax.xaxis, [30, 100, 300, 1000, 3000]); hs.plain_log(ax.yaxis)
    ax.set_xlabel(hs.label('Fundamental frequency', 'f_1', 'Hz').replace(r'\mathrm{1}', '1'))
    ax.set_ylabel(hs.label('Switching frequency', 'f_sw', 'Hz'))
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.7
@fig('1.7')
def scaling_paths():
    f, ax = hs.figure(9.5)
    groups = ['active\nvolume', 'centrifugal\nstress', 'iron\nloss', 'windage\nloss',
              r'$l/D$' + '\nratio', r'$n_{\mathrm{op}}/n_{\mathrm{cr}}$']
    a = [2.00, 4.00, 4.00, 8.00, 1.00, 2.00]
    b = [0.50, 1.00, 2.00, 1.00, 4.00, 16.00]
    c = [0.58, 1.33, 2.00, 1.33, 2.60, 7.79]
    x = np.arange(len(groups)); w = 0.26
    series = [(a, RUST, '', '(a) fixed geometry, overspeed'),
              (b, BLUE, '////', '(b) tip-speed limited, $P$ constant'),
              (c, GREEN, '....', '(c) length capped by rotordynamics')]
    for i, (vals, col, hatch, lab) in enumerate(series):
        ax.bar(x + (i - 1) * w, vals, w, color=col, hatch=hatch, edgecolor='white', lw=0,
               label=lab)
        for xi, vi in zip(x + (i - 1) * w, vals):
            txt = f'{vi:.2f}'.rstrip('0').rstrip('.')
            ax.text(xi, vi * 1.10, txt, ha='center', va='bottom', rotation=90)
    ax.axhline(1, color=INK, lw=hs.LW_THIN, ls=(0, (3, 2)))
    ax.set_yscale('log'); ax.set_ylim(0.3, 60)
    hs.plain_log(ax.yaxis, [0.5, 1, 2, 4, 8, 16, 32])
    ax.set_xticks(x); ax.set_xticklabels(groups)
    ax.tick_params(axis='x', which='both', length=0)
    ax.grid(axis='x', visible=False)
    ax.set_xlim(-0.6, len(groups) - 0.4)
    ax.set_ylabel('Factor on doubling the speed')
    ax.legend(loc='upper left', handlelength=1.6)
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.8
@fig('1.8')
def critical_speed_divergence():
    f, ax = hs.figure(8.6)
    k = np.linspace(1, 3, 300)
    ax.fill_between(k, k ** -3.0, k, color=BLUE, alpha=0.07, lw=0)
    ax.plot(k, k, color=BLUE, ls='-')
    ax.plot(k, k ** -3.0, color=RUST, ls='--')
    ax.plot(k, k ** 4.0, color=GREEN, ls='-.')
    ax.text(2.97, 3 * 1.18, r'operating speed, $\propto \Omega$', color=BLUE, ha='right', va='bottom')
    ax.text(2.97, 0.135, r'first critical speed, $\propto \Omega^{-3}$', color=RUST,
            ha='right', va='bottom')
    ax.text(2.55, 2.55 ** 4 * 0.70, r'ratio $n_{\mathrm{op}}/n_{\mathrm{cr}}$, $\propto \Omega^{4}$',
            color=GREEN, ha='left', va='top')
    ax.plot(2, 16, 'o', ms=7, mfc='white', mec=INK, mew=1.2, zorder=6)
    hs.leader(ax, r'speed $\times 2$ $\Rightarrow$ margin $\times 16$', xy=(2, 16),
              xytext=(1.42, 45), ha='center')
    ax.set_yscale('log'); ax.set_xlim(1, 3); ax.set_ylim(0.02, 120)
    hs.plain_log(ax.yaxis, [0.03, 0.1, 0.3, 1, 3, 10, 30, 100])
    ax.set_xlabel('Speed multiplier along the tip-speed-limited path')
    ax.set_ylabel('Normalised value')
    return f



# ───────────────────────────────────────────────────────────────── Fig. 1.9
@fig('1.9')
def trilemma():
    """The text of §1.6.1 drawn literally: a directed cycle of three remedies, each
    creating the next problem, around a feasible window that the power-electronic
    interface splits into the two paradigms. Drawn in centimetres of the page."""
    H = 10.95
    f, ax = hs.canvas(H)
    A, B, C = np.array([7.96, 9.95]), np.array([1.55, 1.75]), np.array([14.37, 1.75])
    ax.add_patch(Polygon([A, B, C], closed=True, fc='#f7f7f5', ec=INK, lw=hs.LW_OUTLINE * 1.3,
                         zorder=1))

    def hw(y):                                   # half-width of the triangle at height y
        return (A[1] - y) / (A[1] - B[1]) * (C[0] - B[0]) / 2

    # vertices
    ax.text(A[0], A[1] + 0.45, 'Mechanical integrity', ha='center', va='bottom')
    ax.text(B[0] - 0.15, B[1] - 0.35, 'Electromagnetic\nefficiency', ha='center', va='top',
            linespacing=1.1)
    ax.text(C[0] + 0.15, C[1] - 0.35, 'Thermal\nmanagement', ha='center', va='top',
            linespacing=1.1)

    # the directed cycle: each remedy creates the next problem
    def edge_arrow(p, q, f0, f1, off):
        d = q - p; n = np.array([d[1], -d[0]]) / np.linalg.norm(d)
        ax.add_patch(FancyArrowPatch(p + f0 * d + off * n, p + f1 * d + off * n,
                                     arrowstyle='-|>', mutation_scale=13, lw=1.4, color=RUST,
                                     connectionstyle='arc3,rad=0.12', zorder=4))
    edge_arrow(A, B, 0.22, 0.80, 0.42)
    edge_arrow(B, C, 0.30, 0.70, 0.40)
    edge_arrow(C, A, 0.20, 0.78, 0.42)
    ax.text(2.25, 6.55, 'thicker sleeve\n→ larger air gap', ha='center', va='center',
            linespacing=1.15)
    ax.text(13.67, 6.55, 'cooling channels\n→ lower stiffness', ha='center', va='center',
            linespacing=1.15)
    ax.text(7.96, 0.62, 'more poles, higher frequency → more loss in less volume',
            ha='center', va='center')

    # the feasible window, split by the gatekeeper
    ax.text(7.96, 7.55, 'feasible design\nwindow', ha='center', va='center', linespacing=1.1)
    yu, gy, yl = 5.75, 4.45, 3.05
    ax.add_patch(Ellipse((7.96, yu), 2 * hw(yu) - 0.7, 1.25, fc='#dbe6f0', ec=BLUE,
                         lw=hs.LW_OUTLINE, zorder=2))
    ax.text(7.96, yu, 'low-pole industrial topology\nreachable with silicon IGBT',
            ha='center', va='center', linespacing=1.1, zorder=6)
    ax.add_patch(Ellipse((7.96, yl), 2 * hw(yl) - 1.6, 1.25, fc='#f3e1d8', ec=RUST,
                         lw=hs.LW_OUTLINE, zorder=2))
    ax.text(7.96, yl, 'high-pole mobile topology\nfeasible only with SiC or GaN',
            ha='center', va='center', linespacing=1.1, zorder=6)
    g = hw(gy) - 0.25
    ax.plot([7.96 - g, 7.96 + g], [gy, gy], color=GREEN, lw=1.6, zorder=5)
    for x in (7.96 - g, 7.96 + g):
        ax.plot([x, x], [gy - 0.18, gy + 0.18], color=GREEN, lw=1.6, zorder=5)
    ax.text(7.96, gy, 'power-electronic interface: the gatekeeper', ha='center', va='center',
            zorder=7, bbox=dict(boxstyle='square,pad=0.15', fc='#f7f7f5', ec='none'))
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.2
@fig('1.2')
def geared_vs_directdrive():
    """(a) The geared train in elevation: finned motor, a closed gearbox (no gearing
    shown, so nothing can be drawn facing the wrong way), a compressor with bearing
    pedestal, volute, axial inlet and discharge, and below the floor the lubrication
    skid with tank, pump and oil cooler. (b) The same compressor flanged onto a
    high-speed motor, drawn in the same manner with the upper half in section: the
    AMBs, the motor and the impeller on the motor shaft are seen inside, and the
    floor below is empty. Drawn in centimetres of the printed page."""
    H, DA = 17.0, 0.30                       # canvas height; lift of panel (a)
    f, ax = hs.canvas(H)
    OL = dict(ec=INK, lw=hs.LW_OUTLINE)

    def rect(x0, x1, y0, y1, fc, z=3, **kw):
        o = dict(OL); o.update(kw)
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, zorder=z, **o))

    def rrect(x0, x1, y0, y1, fc, r=0.15, z=3, **kw):
        o = dict(OL); o.update(kw)
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, fc=fc, zorder=z,
                                    boxstyle=f'round,pad=0,rounding_size={r}', **o))

    def pipe(xs, ys, ls='-'):
        ax.plot(xs, ys, color=RUST, lw=1.0, ls=ls, zorder=2, solid_capstyle='butt')

    # ═══════════════════════════════════ (a) geared train, elevation ═══════════
    a = lambda y: y + DA
    FL = a(11.30)                                         # machine floor
    ym, yc = a(13.15), a(13.95)                           # motor and compressor shaft lines
    rect(0.15, 15.77, a(8.75), FL, FILL['ground'], z=0, ec='none')
    ax.plot([0.15, 15.77], [FL, FL], color=INK, lw=hs.LW_OUTLINE * 1.3, zorder=1)
    rect(0.35, 15.55, FL, a(11.62), FILL['steel'], z=2)               # common baseplate
    ax.text(15.60, FL - 0.32, 'machine floor', ha='right', va='center')

    # motor: finned frame, end shields, terminal box, feet, shaft end
    for x0 in (0.85, 3.65):
        rect(x0, x0 + 0.60, a(11.62), a(11.92), FILL['housing'])
    rrect(0.30, 0.68, a(12.20), a(14.10), FILL['housing'], r=0.12)    # fan cowl (NDE)
    rect(0.65, 4.45, a(11.92), a(14.38), FILL['housing'])
    for y in np.arange(12.17, 14.25, 0.24):
        ax.plot([0.80, 4.30], [a(y), a(y)], color=GREY, lw=hs.LW_THIN, zorder=4)
    rrect(4.45, 4.72, a(12.38), a(13.92), FILL['housing'], r=0.08)    # drive-end shield
    rect(1.85, 2.95, a(14.38), a(14.95), FILL['housing'])             # terminal box
    rect(4.72, 5.05, ym - 0.13, ym + 0.13, FILL['steel'], z=4)
    # coupling 1
    for x0 in (5.05, 5.31):
        rect(x0, x0 + 0.20, ym - 0.34, ym + 0.34, '#9c9c9c', z=4)
    # gearbox: closed casing in elevation
    rect(5.51, 5.74, ym - 0.13, ym + 0.13, FILL['steel'], z=4)
    rect(5.74, 5.92, ym - 0.42, ym + 0.42, FILL['housing'], z=4)      # input bearing cap
    for x0 in (6.00, 8.30):
        rect(x0, x0 + 0.50, a(11.62), a(11.92), FILL['housing'])
    rect(5.92, 8.90, a(11.92), a(14.75), FILL['housing'])
    for x0 in (6.55, 7.35, 8.15):                                     # stiffening ribs
        rect(x0, x0 + 0.13, a(12.10), a(14.55), '#dcdcd6', z=4, lw=hs.LW_THIN)
    rect(6.45, 8.35, a(14.75), a(14.98), FILL['housing'])             # inspection cover
    for x in (6.62, 8.18):
        ax.add_patch(plt.Circle((x, a(14.865)), 0.05, fc=INK, ec='none', zorder=5))
    rect(7.80, 7.86, a(14.98), a(15.18), INK, z=4, lw=0)              # breather
    rrect(7.68, 7.98, a(15.18), a(15.30), FILL['housing'], r=0.05)
    rect(8.90, 9.08, yc - 0.42, yc + 0.42, FILL['housing'], z=4)      # output bearing cap
    rect(9.08, 9.28, yc - 0.13, yc + 0.13, FILL['steel'], z=4)
    # coupling 2
    for x0 in (9.28, 9.54):
        rect(x0, x0 + 0.20, yc - 0.34, yc + 0.34, '#9c9c9c', z=4)
    # compressor: bearing pedestal, volute, discharge, axial inlet
    rect(9.74, 9.97, yc - 0.13, yc + 0.13, FILL['steel'], z=4)
    rect(10.25, 11.05, a(11.62), yc - 0.60, FILL['housing'])          # pedestal support
    rect(9.97, 11.37, yc - 0.60, yc + 0.60, FILL['housing'], z=4)     # bearing housing
    rect(11.55, 12.55, a(11.62), a(12.30), FILL['housing'])           # volute support
    rrect(11.37, 12.77, yc - 1.70, yc + 1.70, FILL['housing'], r=0.55, z=4)   # volute
    rect(11.62, 12.52, yc + 1.62, yc + 2.05, FILL['housing'], z=4)    # discharge
    rect(11.47, 12.67, yc + 2.05, yc + 2.20, FILL['housing'], z=4)    # discharge flange
    rect(12.77, 14.10, yc - 0.55, yc + 0.55, FILL['housing'], z=4)    # inlet pipe
    rect(14.10, 14.27, yc - 0.78, yc + 0.78, FILL['housing'], z=4)    # inlet flange
    ax.add_patch(FancyArrowPatch((15.55, yc), (14.45, yc), arrowstyle='-|>',
                                 mutation_scale=12, lw=1.2, color=INK, zorder=5))

    # lubrication skid below the floor: tank -> pump -> cooler -> gearbox -> tank
    rect(5.60, 7.70, a(9.40), a(10.85), 'white')                      # oil tank
    rect(5.60, 7.70, a(9.40), a(10.45), FILL['oil'], z=3, ec='none')
    ax.plot([5.60, 7.70], [a(10.45), a(10.45)], color=INK, lw=hs.LW_THIN, zorder=4)
    rect(5.60, 7.70, a(9.40), a(10.85), 'none', z=4)
    ax.add_patch(plt.Circle((8.55, a(9.95)), 0.38, fc='white', ec=INK, lw=hs.LW_OUTLINE, zorder=4))
    ax.add_patch(Polygon([(8.36, a(9.70)), (8.36, a(10.20)), (8.86, a(9.95))], closed=True,
                         fc='none', ec=INK, lw=hs.LW_THIN, zorder=5))  # pump
    rect(9.55, 11.25, a(9.45), a(10.75), 'white')                     # oil cooler
    for x in np.arange(9.70, 11.15, 0.14):
        ax.plot([x, x], [a(9.58), a(10.62)], color=GREY, lw=hs.LW_THIN, zorder=4)
    pipe([7.70, 8.17], [a(9.95), a(9.95)])                            # tank -> pump
    pipe([8.93, 9.55], [a(9.95), a(9.95)])                            # pump -> cooler
    pipe([10.40, 10.40, 7.00, 7.00], [a(10.75), a(11.05), a(11.05), a(11.92)])   # feed
    pipe([6.72, 6.72], [a(11.92), a(10.85)], ls=(0, (4, 2)))                    # return
    for x, y0, y1 in ((7.00, 11.40, 11.75), (6.72, 11.55, 11.20)):
        ax.add_patch(FancyArrowPatch((x, a(y0)), (x, a(y1)), arrowstyle='-|>',
                                     mutation_scale=9, lw=0, color=RUST, zorder=6))
    ax.text(6.38, FL - 0.32, 'oil feed and return', ha='right', va='center')
    for x, t in ((6.65, 'oil tank'), (8.55, 'pump'), (10.40, 'oil cooler')):
        ax.text(x, a(9.05), t, ha='center', va='center')

    # names, speeds, couplings
    for x, t in ((2.55, 'motor\n1500 r/min'), (7.41, 'gearbox\nstep-up ×20'),
                 (13.90, 'compressor\n30 000 r/min')):
        ax.text(x, a(15.62), t, ha='center', va='bottom', linespacing=1.1)
    hs.leader(ax, 'coupling', xy=(5.28, ym + 0.36), xytext=(5.28, a(15.85)))
    hs.leader(ax, 'coupling', xy=(9.51, yc + 0.36), xytext=(9.51, a(15.85)))
    ax.text(7.96, a(8.40), '(a) Geared train', ha='center', va='center')

    # ═══════════════════════════════════ (b) integrated direct drive ═══════════
    # The compressor of (a), unchanged, now flanged straight onto a high-speed motor.
    # Upper half in section, lower half seen from outside, as a drafter draws a
    # half section; below the floor nothing is left, because the oil system is gone.
    FB, yb = 1.95, 4.25                                   # floor and shaft line of (b)
    u = lambda r: yb + r                                  # height of radius r above the shaft line
    X0, XD, R, T = 6.42, 11.25, 1.15, 0.12                # motor: NDE face, DE flange, radius, wall
    rect(0.15, 15.77, 0.85, FB, FILL['ground'], z=0, ec='none')
    ax.plot([0.15, 15.77], [FB, FB], color=INK, lw=hs.LW_OUTLINE * 1.3, zorder=1)
    rect(6.05, 14.60, FB, FB + 0.32, FILL['steel'], z=2)              # baseplate
    ax.text(15.60, FB - 0.32, 'machine floor', ha='right', va='center')

    def fill(pts, fc, z, edges=None):
        """A filled outline in (x, radius) whose ink edge leaves out the shaft line."""
        ax.add_patch(Polygon([(x, u(r)) for x, r in pts], closed=True, fc=fc, ec='none',
                             zorder=z))
        for run in edges if edges is not None else [pts]:
            ax.plot([x for x, r in run], [u(r) for x, r in run], color=INK,
                    lw=hs.LW_OUTLINE, zorder=z + 0.05, solid_joinstyle='miter')

    def half(x0, x1, r0, r1, fc, z):
        """A rectangle standing on the shaft line (r0 = 0) or hanging from it (r1 = 0)."""
        on = r0 if r1 == 0 else r1
        fill([(x0, r0), (x0, r1), (x1, r1), (x1, r0)], fc, z,
             [[(x0, 0), (x0, on), (x1, on), (x1, 0)]])

    # motor, lower half from outside: housing with its end-shield joints, DE flange, feet
    for x0 in (6.80, 10.20):
        rect(x0, x0 + 0.70, FB + 0.32, u(-R) + 0.02, FILL['housing'], z=2)
    half(X0, XD, -R, 0, FILL['housing'], 3)
    half(XD, 11.37, -1.30, 0, FILL['housing'], 3)
    for x in (8.10, 10.20):
        ax.plot([x, x], [u(-R), yb], color=INK, lw=hs.LW_THIN, zorder=3.5)

    # motor, upper half in section: housing and end shields cut, the parts inside
    fill([(X0, 0), (X0, R), (XD, R), (XD, 1.30), (11.37, 1.30), (11.37, 0)], FILL['section'], 3)
    cav = [(X0 + 0.14, 0), (X0 + 0.14, R - T), (11.08, R - T), (11.08, 0.20), (11.37, 0.20)]
    fill(cav + [(11.37, 0)], 'white', 3.2, [cav])
    rect(X0 + 0.14, 8.10, u(0.80), u(R - T), FILL['section'], z=4)    # end shields
    rect(10.20, 11.08, u(0.80), u(R - T), FILL['section'], z=4)
    rect(6.62, 6.82, u(0.34), u(0.80), FILL['section'], z=4)          # touchdown bearing seats
    rect(10.84, 11.08, u(0.34), u(0.80), FILL['section'], z=4)
    half(6.58, 12.02, 0, 0.16, FILL['steel'], 4.6)                    # shaft
    for x0 in (6.64, 10.88):                                          # touchdown bearings
        rect(x0, x0 + 0.16, u(0.16), u(0.34), FILL['bearing'], z=5)
        ax.add_patch(plt.Circle((x0 + 0.08, u(0.25)), 0.055, fc='white', ec=INK,
                                lw=hs.LW_THIN, zorder=5.2))
    for x0 in (6.88, 7.28):                                           # axial AMB stators
        rect(x0, x0 + 0.22, u(0.24), u(0.80), FILL['bearing'], z=5)
    for x0 in (6.98, 7.28):
        rect(x0, x0 + 0.12, u(0.40), u(0.62), FILL['copper'], z=5.3, lw=hs.LW_THIN)
    rect(7.14, 7.24, u(0.16), u(0.72), FILL['steel'], z=5)            # thrust disc
    for xa in (7.62, 10.30):                                          # radial AMBs
        hs.laminated(ax, xa, xa + 0.40, u(0.27), u(0.80), pitch=0.08, z=5)
        for xc in (xa - 0.06, xa + 0.40):
            rect(xc, xc + 0.06, u(0.36), u(0.66), FILL['copper'], z=5.4, lw=hs.LW_THIN)
        hs.laminated(ax, xa - 0.04, xa + 0.44, u(0.16), u(0.23), pitch=0.08, z=5)
    rect(8.18, 10.12, u(0.90), u(R - T), FILL['coolant'], z=4.2, lw=hs.LW_THIN)
    for x in np.linspace(8.18, 10.12, 8)[1:-1]:                       # cooling channels
        ax.plot([x, x], [u(0.90), u(R - T)], color=INK, lw=hs.LW_THIN, zorder=4.3)
    hs.laminated(ax, 8.40, 9.90, u(0.52), u(0.90), pitch=0.10, z=5)   # stator core
    for x0 in (8.12, 9.90):                                           # end windings
        rrect(x0, x0 + 0.28, u(0.56), u(0.84), FILL['copper'], r=0.08, z=5.3, lw=hs.LW_THIN)
    half(8.35, 9.95, 0, 0.47, FILL['rotor'], 5)                       # rotor
    ax.text(9.15, u(0.235), 'rotor', ha='center', va='center', zorder=8)

    # compressor, the same as in (a): support, volute, discharge, inlet
    rect(11.55, 12.55, FB + 0.32, u(-1.65), FILL['housing'])          # volute support
    for fc, y0, h in ((FILL['housing'], 0, yb), (FILL['section'], yb, 10)):
        v = FancyBboxPatch((11.37, u(-1.70)), 1.40, 3.40, fc=fc, ec=INK, lw=hs.LW_OUTLINE,
                           zorder=4, boxstyle='round,pad=0,rounding_size=0.55')
        ax.add_patch(v)
        v.set_clip_path(Rectangle((0, y0), hs.W_CM, h, transform=ax.transData))
    rect(11.62, 12.52, u(1.62), u(2.05), FILL['housing'], z=4)        # discharge
    rect(11.47, 12.67, u(2.05), u(2.20), FILL['housing'], z=4)
    half(12.77, 14.10, -0.55, 0, FILL['housing'], 4)                  # inlet pipe and flange
    half(14.10, 14.27, -0.78, 0, FILL['housing'], 4)
    half(12.77, 14.10, 0, 0.55, FILL['section'], 4)
    half(14.10, 14.27, 0, 0.78, FILL['section'], 4)
    ax.add_patch(FancyArrowPatch((15.55, yb), (14.45, yb), arrowstyle='-|>',
                                 mutation_scale=12, lw=1.2, color=INK, zorder=5))
    # inside the volute: scroll, diffuser, the cavity round the impeller, the inlet
    sx, sr, so = 11.82, 1.28, 0.30                                    # scroll centre and radius
    ax.add_patch(plt.Circle((sx, u(sr)), so, fc='white', ec=INK, lw=hs.LW_OUTLINE, zorder=5))
    gap = [(11.50, 0.19), (11.50, 0.90), (11.60, 0.90)]
    shroud = [(11.74, 0.90), (11.74, 0.80), (11.78, 0.69), (11.86, 0.61), (11.95, 0.575),
              (12.08, 0.565), (12.40, 0.53), (12.77, 0.47), (14.27, 0.47)]
    fill(gap + shroud + [(14.27, 0), (11.37, 0), (11.37, 0.19)], 'white', 5, [gap, shroud])
    meet = lambda x: sr - np.sqrt(so ** 2 - (x - sx) ** 2)            # diffuser wall meets scroll
    fill([(11.60, 0.86), (11.60, 1.12), (11.74, 1.12), (11.74, 0.86)], 'white', 5.1,
         [[(11.60, 0.90), (11.60, meet(11.60))], [(11.74, 0.90), (11.74, meet(11.74))]])
    half(11.37, 12.05, 0, 0.16, FILL['steel'], 5.2)                   # shaft end
    imp = [(11.56, 0.16), (11.56, 0.86), (11.68, 0.86), (11.70, 0.76), (11.75, 0.66),
           (11.83, 0.58), (11.93, 0.535), (12.05, 0.52), (12.05, 0.16)]
    fill(imp, FILL['steel'], 5.5, [imp + [imp[0]]])
    ax.plot([12.05, 11.90, 11.76, 11.66, 11.605, 11.59],
            [u(0.22), u(0.25), u(0.33), u(0.47), u(0.66), u(0.86)], color=INK,
            lw=hs.LW_THIN, zorder=5.6)                                # hub line under the blades
    half(12.05, 12.15, 0, 0.13, FILL['steel'], 5.5)                   # impeller nut
    ax.plot([6.07, 14.45], [yb, yb], color=GREY, lw=hs.LW_THIN, ls=(0, (9, 2.5, 1.5, 2.5)),
            zorder=15)

    # labels: names and speeds above, as in (a); the parts inside by leaders
    yr, yn = u(2.55), u(2.95)
    hs.leader(ax, 'radial AMB', xy=(7.82, u(0.66)), xytext=(7.40, yr), dot=True)
    hs.leader(ax, 'stator', xy=(9.15, u(0.74)), xytext=(9.15, yr), dot=True)
    hs.leader(ax, 'radial AMB', xy=(10.50, u(0.66)), xytext=(10.90, yr), dot=True)
    hs.leader(ax, 'axial AMB', xy=(6.99, u(0.70)), xytext=(5.45, u(1.30)), dot=True, ha='right')
    hs.leader(ax, 'touchdown bearing', xy=(6.66, u(0.30)), xytext=(5.45, u(0.30)), dot=True,
              ha='right')
    hs.leader(ax, 'impeller, on the\nmotor shaft', xy=(11.86, u(0.56)), xytext=(14.40, u(1.40)),
              dot=True, linespacing=1.1)
    ax.text(8.90, yn, 'high-speed motor\n30 000 r/min', ha='center', va='bottom', linespacing=1.1)
    ax.text(13.90, yn, 'compressor\n30 000 r/min', ha='center', va='bottom', linespacing=1.1)
    ax.text(7.96, 0.45, '(b) Integrated direct drive', ha='center', va='center')
    return f

if __name__ == '__main__':
    want = sys.argv[1:] or list(FIGS)
    for num in want:
        png = hs.save(FIGS[num](), OUT + num.replace('1.', '1_0') if len(num) == 3 else OUT + num)
        print(f'Figure {num}: {png}')
