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
    """The text of §1.6.1 drawn literally. The three domains sit at the corners, each
    marked by a small drawing of what it governs: the sleeved rotor, the electrical
    frequency, the heat sink. The sides of the triangle are the directed cycle of
    remedies, each creating the next problem. Inside lies the feasible window, which the
    power-electronic interface splits into the two paradigms; their colours are those of
    Figure 1.6, rust for silicon and green for SiC and GaN, and the gatekeeper is drawn
    in the blue of the pulse-ratio lines there. Drawn in centimetres of the page."""
    H = 11.25
    f, ax = hs.canvas(H)
    A, B, C = np.array([7.96, 10.30]), np.array([1.60, 2.10]), np.array([14.32, 2.10])
    RN = 0.78                                    # radius of the corner discs
    tri = Polygon([A, B, C], closed=True, fc='#f7f7f5', ec='none', zorder=1)
    ax.add_patch(tri)

    # the feasible window, split by the gatekeeper into the two paradigms
    wx, wy, wa, wb = 7.96, 4.80, 3.25, 2.20      # centre and semi-axes of the window
    gy, gh = 4.80, 0.25                          # the gatekeeper band: centre, half-height
    win = Ellipse((wx, wy), 2 * wa, 2 * wb, fc='white', ec='none', zorder=2)
    ax.add_patch(win)
    for y0, y1, tint in ((gy, wy + wb, '#f3e5e0'), (wy - wb, gy, '#e8eee2')):
        zone = Rectangle((wx - wa, y0), 2 * wa, y1 - y0, fc=tint, ec='none', zorder=2.1)
        ax.add_patch(zone)
        zone.set_clip_path(win)
    ax.add_patch(Ellipse((wx, wy), 2 * wa, 2 * wb, fc='none', ec=INK, lw=hs.LW_OUTLINE,
                         zorder=2.5))
    band = Rectangle((0, gy - gh), hs.W_CM, 2 * gh, fc='#e2e8ee', ec='none', zorder=3)
    ax.add_patch(band)
    band.set_clip_path(tri)
    for y in (gy - gh, gy + gh):
        ln, = ax.plot([0, hs.W_CM], [y, y], color=BLUE, lw=hs.LW_OUTLINE, zorder=3.1)
        ln.set_clip_path(tri)
    ax.text(wx, gy, 'power electronics: the gatekeeper', color=BLUE, ha='center',
            va='center', zorder=6)
    ax.text(wx, 5.54, 'low-pole industrial topology\nreachable with silicon IGBT', color=RUST,
            ha='center', va='center', linespacing=1.1, zorder=6)
    ax.text(wx, 4.06, 'high-pole mobile topology\nfeasible only with SiC or GaN', color=GREEN,
            ha='center', va='center', linespacing=1.1, zorder=6)
    ax.text(wx, wy + wb + 0.34, 'feasible design window', ha='center', va='center', zorder=6)

    # the sides: each remedy creates the next problem
    for p, q in ((A, B), (B, C), (C, A)):
        u = (q - p) / np.linalg.norm(q - p)
        ax.add_patch(FancyArrowPatch(p + (RN + 0.10) * u, q - (RN + 0.10) * u, arrowstyle='-|>',
                                     mutation_scale=13, lw=1.3, color=INK, shrinkA=0,
                                     shrinkB=0, zorder=4))
    ax.text(4.38, 6.50, 'thicker sleeve\n→ larger air gap', ha='right', va='center',
            linespacing=1.15)
    ax.text(11.54, 6.50, 'cooling channels\n→ lower stiffness', ha='left', va='center',
            linespacing=1.15)
    ax.text(7.96, 1.47, 'more poles, higher frequency\n→ more loss in less volume',
            ha='center', va='center', linespacing=1.15)

    # the corners, each with a drawing of what it governs
    for c in (A, B, C):
        ax.add_patch(plt.Circle(c, RN, fc='white', ec=INK, lw=hs.LW_OUTLINE * 1.2, zorder=6))
    ax.add_patch(plt.Circle(A, 0.47, fc=GREY, ec=INK, lw=hs.LW_THIN, zorder=7))      # sleeve
    ax.add_patch(plt.Circle(A, 0.38, fc=FILL['rotor'], ec=INK, lw=hs.LW_THIN, zorder=7.1))
    for k in range(6):                                                              # magnets
        t = np.pi / 6 + k * np.pi / 3
        ax.plot(A[0] + np.array([0.15, 0.38]) * np.cos(t), A[1] + np.array([0.15, 0.38]) * np.sin(t),
                color=INK, lw=hs.LW_THIN, zorder=7.2)
    ax.add_patch(plt.Circle(A, 0.15, fc=FILL['steel'], ec=INK, lw=hs.LW_THIN, zorder=7.3))
    xs = np.linspace(-0.50, 0.50, 200)                                              # frequency
    ax.plot(B[0] + xs[[0, -1]], [B[1]] * 2, color=GREY, lw=hs.LW_THIN, zorder=7)
    ax.plot(B[0] + xs, B[1] + 0.30 * np.sin(2 * np.pi * 2.5 * (xs + 0.50)), color=INK,
            lw=1.3, zorder=7.1)
    ax.add_patch(Rectangle((C[0] - 0.45, C[1] - 0.34), 0.90, 0.15, fc=FILL['steel'], ec=INK,
                           lw=hs.LW_THIN, zorder=7))                                # heat sink
    for k in range(5):
        ax.add_patch(Rectangle((C[0] - 0.41 + k * 0.19, C[1] - 0.19), 0.08, 0.50,
                               fc=FILL['steel'], ec=INK, lw=hs.LW_THIN, zorder=7))
    ax.text(A[0] + RN + 0.22, A[1], 'Mechanical integrity', ha='left', va='center')
    ax.text(B[0], B[1] - RN - 0.14, 'Electromagnetic\nefficiency', ha='center', va='top',
            linespacing=1.1)
    ax.text(C[0], C[1] - RN - 0.14, 'Thermal\nmanagement', ha='center', va='top',
            linespacing=1.1)
    return f


# ───────────────────────────────────────────────────────────────── Fig. 1.2
@fig('1.2')
def geared_vs_directdrive():
    """The geared train and the integrated direct drive, drawn to scale.

    Every part is dimensioned in metres for a compressor unit of about 300 kW at
    30 000 r/min, taken from catalogue sizes, and (a) and (b) are drawn at one scale,
    so that the sizes compare directly. (c) repeats the motor of (b) at twice that
    scale, with the upper half in section, so that its parts stay legible.

    (a) Elevation. A four-pole 315 kW motor in IEC frame 355: 1.56 m long over the
    shaft end, 1.01 m high over the terminal box, shaft height 0.355 m, shaft end
    0.10 m. A step-up gearbox of ratio 20 in a closed casing, two-stage because one
    parallel-shaft stage stops at a ratio of about 11; no gearing is drawn, so none can
    face the wrong way. A coupling on each side, sized for 1.9 kN m and for 95 N m. A
    single-stage compressor with its bearing housing, a volute 0.56 m across for an
    impeller of about 0.28 m, an axial inlet and a discharge. Below the floor the
    lubrication skid: a tank of about 160 l, a pump and a plate oil cooler.
    (b) The same compressor flanged onto a high-speed motor 0.79 m long and 0.33 m
    across; the gearbox, the couplings and the oil system are gone.
    (c) That motor in half section: a rotor 0.12 m in diameter and 0.24 m long in a
    stator 0.25 m across, the cooling jacket, the radial and axial AMBs, a touchdown
    bearing at each end, and the impeller overhung on the shaft end.
    Drawn in centimetres of the printed page; the dimensions are in metres."""
    H = 16.75                                # canvas height (cm)
    f, ax = hs.canvas(H)
    OL = dict(ec=INK, lw=hs.LW_OUTLINE)
    S, BP = 3.50, 0.18                       # cm per metre in (a) and (b); baseplate height (m)

    def rect(x0, x1, y0, y1, fc, z=3, **kw):
        o = dict(OL); o.update(kw)
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=fc, zorder=z, **o))

    def rrect(x0, x1, y0, y1, fc, r=0.15, z=3, **kw):
        o = dict(OL); o.update(kw)
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, fc=fc, zorder=z,
                                    boxstyle=f'round,pad=0,rounding_size={r}', **o))

    def view(x0, y0, s):
        """A drawing view: metres along and above its datum, to centimetres of the page."""
        X = lambda x: x0 + s * x
        Y = lambda y: y0 + s * y

        def part(xa, xb, ya, yb, fc, z=3, r=None, **kw):
            if r:
                rrect(X(xa), X(xb), Y(ya), Y(yb), fc, r=s * r, z=z, **kw)
            else:
                rect(X(xa), X(xb), Y(ya), Y(yb), fc, z=z, **kw)
        return X, Y, part

    def floor(X0, X1, Y, depth, label_x):
        """The machine floor: a heavy line with the light band of the room below it."""
        rect(X0, X1, Y(-depth), Y(0), FILL['ground'], z=0, ec='none')
        ax.plot([X0, X1], [Y(0), Y(0)], color=INK, lw=hs.LW_OUTLINE * 1.3, zorder=1)
        ax.text(label_x, Y(0) - 0.32, 'machine floor', ha='right', va='center')

    def compressor(X, Y, part, yc):
        """Volute, discharge and axial inlet, identical in (a) and (b)."""
        part(3.22, 3.40, BP, yc - 0.27, FILL['housing'])                      # support
        part(3.18, 3.44, yc - 0.28, yc + 0.28, FILL['housing'], z=4, r=0.09)  # volute
        part(3.235, 3.385, yc + 0.25, yc + 0.43, FILL['housing'], z=3.9)      # discharge
        part(3.20, 3.42, yc + 0.43, yc + 0.455, FILL['housing'], z=4)
        part(3.44, 3.84, yc - 0.11, yc + 0.11, FILL['housing'], z=4)          # inlet pipe
        part(3.84, 3.865, yc - 0.165, yc + 0.165, FILL['housing'], z=4)       # inlet flange
        ax.add_patch(FancyArrowPatch((X(4.22), Y(yc)), (X(3.91), Y(yc)), arrowstyle='-|>',
                                     mutation_scale=12, lw=1.2, color=INK, zorder=5))

    # ═══════════════════════════════════ (a) geared train, elevation ═══════════
    X, Y, part = view(0.95, 11.05, S)        # datum: the motor's fan cowl, on the floor
    floor(0.15, 15.77, Y, 0.98, 15.60)
    part(-0.04, 3.62, 0, BP, FILL['steel'], z=2)                              # baseplate
    ym, yo = BP + 0.355, BP + 0.655                                           # shaft lines

    # motor, IEC 355: finned frame, fan cowl, terminal box, drive-end shield, shaft end
    for x0 in (0.30, 0.98):
        part(x0, x0 + 0.22, BP, BP + 0.06, FILL['housing'])                   # feet
    part(0.00, 0.17, BP + 0.07, BP + 0.64, FILL['housing'], r=0.04)
    part(0.15, 1.30, BP + 0.03, BP + 0.68, FILL['housing'])
    for y in np.arange(0.09, 0.64, 0.05):                                     # cooling fins
        ax.plot([X(0.19), X(1.26)], [Y(BP + y)] * 2, color=GREY, lw=hs.LW_THIN, zorder=4)
    part(0.58, 0.98, BP + 0.68, BP + 1.01, FILL['housing'])
    part(1.30, 1.35, ym - 0.22, ym + 0.22, FILL['housing'], r=0.02)
    part(1.35, 1.555, ym - 0.05, ym + 0.05, FILL['steel'], z=4)
    # low-speed coupling; gearbox input shaft
    for x0 in (1.47, 1.565):
        part(x0, x0 + 0.085, ym - 0.13, ym + 0.13, '#9c9c9c', z=5)
    part(1.565, 1.78, ym - 0.045, ym + 0.045, FILL['steel'], z=4)
    # gearbox: closed casing in elevation, input low and output high
    for x0 in (1.84, 2.18):
        part(x0, x0 + 0.18, BP, BP + 0.05, FILL['housing'])
    part(1.75, 1.80, ym - 0.11, ym + 0.11, FILL['housing'], z=4)              # bearing caps
    part(2.40, 2.45, yo - 0.08, yo + 0.08, FILL['housing'], z=4)
    part(1.80, 2.40, BP + 0.04, BP + 0.84, FILL['housing'])
    for x0 in (1.93, 2.08, 2.23):                                             # ribs
        part(x0, x0 + 0.035, BP + 0.10, BP + 0.78, FILL['section'], z=4, lw=hs.LW_THIN)
    part(1.92, 2.28, BP + 0.84, BP + 0.88, FILL['housing'])                   # inspection cover
    for x in (1.97, 2.23):
        ax.add_patch(plt.Circle((X(x), Y(BP + 0.86)), 0.04, fc=INK, ec='none', zorder=5))
    part(2.145, 2.16, BP + 0.88, BP + 0.94, INK, z=4, lw=0)                   # breather
    part(2.125, 2.18, BP + 0.94, BP + 0.97, FILL['housing'], r=0.01)
    part(2.45, 2.53, yo - 0.025, yo + 0.025, FILL['steel'], z=4)
    # high-speed coupling with its spacer; compressor shaft
    for x0 in (2.49, 2.71):
        part(x0, x0 + 0.06, yo - 0.055, yo + 0.055, '#9c9c9c', z=5)
    part(2.55, 2.71, yo - 0.035, yo + 0.035, '#9c9c9c', z=4.5)
    part(2.74, 2.84, yo - 0.025, yo + 0.025, FILL['steel'], z=4)
    # compressor: bearing housing on its pedestal, then the parts shared with (b)
    part(2.90, 3.12, BP, yo - 0.15, FILL['housing'])
    part(2.84, 3.18, yo - 0.15, yo + 0.15, FILL['housing'], z=4)
    compressor(X, Y, part, yo)

    # lubrication skid below the floor: tank -> pump -> cooler -> gearbox -> tank
    def pipe(xs, ys, ls='-'):
        ax.plot([X(x) for x in xs], [Y(y) for y in ys], color=RUST, lw=1.0, ls=ls, zorder=2,
                solid_capstyle='butt')
    part(1.55, 2.35, -0.72, -0.36, FILL['oil'], z=3, ec='none')               # tank, oil in it
    ax.plot([X(1.55), X(2.35)], [Y(-0.36)] * 2, color=INK, lw=hs.LW_THIN, zorder=4)
    part(1.55, 2.35, -0.72, -0.27, 'none', z=4)
    ax.add_patch(plt.Circle((X(2.62), Y(-0.50)), S * 0.12, fc='white', ec=INK,
                            lw=hs.LW_OUTLINE, zorder=4))                      # pump
    ax.add_patch(Polygon([(X(2.565), Y(-0.565)), (X(2.565), Y(-0.435)), (X(2.695), Y(-0.50))],
                         closed=True, fc='none', ec=INK, lw=hs.LW_THIN, zorder=5))
    part(2.86, 3.32, -0.67, -0.33, 'white')                                   # plate cooler
    for x in np.arange(2.895, 3.30, 0.035):
        ax.plot([X(x)] * 2, [Y(-0.635), Y(-0.365)], color=GREY, lw=hs.LW_THIN, zorder=4)
    pipe([2.35, 2.50], [-0.50, -0.50])
    pipe([2.74, 2.86], [-0.50, -0.50])
    pipe([3.09, 3.09, 2.05, 2.05], [-0.33, -0.10, -0.10, BP + 0.04])         # feed
    pipe([1.95, 1.95], [BP + 0.04, -0.27], ls=(0, (4, 2)))                    # return
    for x, y0, y1 in ((2.05, 0.02, 0.12), (1.95, 0.10, 0.00)):
        ax.add_patch(FancyArrowPatch((X(x), Y(y0)), (X(x), Y(y1)), arrowstyle='-|>',
                                     mutation_scale=9, lw=0, color=RUST, zorder=6))
    ax.text(X(1.86), Y(0) - 0.32, 'oil feed and return', ha='right', va='center')
    for x, t in ((1.95, 'oil tank'), (2.62, 'pump'), (3.09, 'oil cooler')):
        ax.text(X(x), Y(-0.86), t, ha='center', va='center')

    # scale bar for (a) and (b), in the empty floor band under the motor
    def scale_bar(X, Y, length, y, marks):
        for x0, fc in ((0, INK), (length / 2, 'white')):
            rect(X(x0), X(x0 + length / 2), Y(y), Y(y) + 0.13, fc, z=4, lw=hs.LW_THIN)
        for x, t in marks:
            ax.text(X(x), Y(y) - 0.30, t, ha='center', va='center')
    scale_bar(X, Y, 1.0, -0.62, ((0, '0'), (0.5, '0.5'), (1.0, '1 m')))

    # names, speeds, couplings
    for x, t in ((0.65, 'motor\n1500 r/min'), (2.10, 'gearbox\nstep-up ×20'),
                 (3.31, 'compressor\n30 000 r/min')):
        ax.text(X(x), Y(1.36), t, ha='center', va='bottom', linespacing=1.1)
    hs.leader(ax, 'coupling', xy=(X(1.56), Y(ym + 0.14)), xytext=(X(1.56), Y(1.13)))
    hs.leader(ax, 'coupling', xy=(X(2.62), Y(yo + 0.06)), xytext=(X(2.62), Y(1.13)))
    ax.text(7.96, Y(-0.98) - 0.42, '(a) Geared train', ha='center', va='center')

    # ═══════════════════════════════════ (b) integrated direct drive ═══════════
    # The compressor of (a), unchanged and in the same place, flanged straight onto
    # the high-speed motor; drawn to the same scale, so that what is left is seen
    # at its true size. Nothing is left below the floor.
    X, Y, part = view(0.95, 1.92, S)
    floor(X(2.29), 15.77, Y, 0.30, 15.60)
    part(2.33, 3.62, 0, BP, FILL['steel'], z=2)                               # baseplate
    yb = BP + 0.40                                                            # shaft line
    for x0 in (2.47, 2.97):
        part(x0, x0 + 0.13, BP, yb - 0.165, FILL['housing'])                  # motor feet
    part(2.39, 3.18, yb - 0.165, yb + 0.165, FILL['housing'], z=3.5)          # motor housing
    for x in (2.415, 2.66, 3.015, 3.155):                                     # cover joints
        ax.plot([X(x)] * 2, [Y(yb - 0.165), Y(yb + 0.165)], color=INK, lw=hs.LW_THIN,
                zorder=3.6)
    part(2.68, 2.84, yb + 0.165, yb + 0.225, FILL['housing'])                 # terminal box
    compressor(X, Y, part, yb)
    ax.text(X(2.66), Y(yb + 0.29), 'high-speed motor\n30 000 r/min', ha='center',
            va='bottom', linespacing=1.1)
    ax.text(X(3.37), Y(yb + 0.52), 'compressor\n30 000 r/min', ha='center', va='bottom',
            linespacing=1.1)
    ax.text(X(3.08), 0.40, '(b) Integrated direct drive', ha='center', va='center')

    # ═══════════════════════════════════ (c) the motor of (b), half section ════
    # Twice the scale of (b). Upper half cut, lower half seen from outside, as a
    # drafter draws a half section. Datum: the motor's non-drive end, on the shaft line.
    SC = 2 * S
    X, Y, part = view(2.25, 3.10, SC)
    R, T, L = 0.165, 0.012, 0.79                                              # housing

    def fill(pts, fc, z, edges=None):
        """A filled outline in (x, radius) whose ink edge leaves out the shaft line."""
        ax.add_patch(Polygon([(X(x), Y(r)) for x, r in pts], closed=True, fc=fc, ec='none',
                             zorder=z))
        for run in edges if edges is not None else [pts]:
            ax.plot([X(x) for x, r in run], [Y(r) for x, r in run], color=INK,
                    lw=hs.LW_OUTLINE, zorder=z + 0.05, solid_joinstyle='miter')

    def half(x0, x1, r0, r1, fc, z):
        """A rectangle standing on the shaft line (r0 = 0) or hanging from it (r1 = 0)."""
        on = r0 if r1 == 0 else r1
        fill([(x0, r0), (x0, r1), (x1, r1), (x1, r0)], fc, z,
             [[(x0, 0), (x0, on), (x1, on), (x1, 0)]])

    # the impeller: back plate, blade tip, shroud and eye, in (x, r)
    imp = [(0.800, 0.0275), (0.800, 0.140), (0.812, 0.140), (0.815, 0.125), (0.823, 0.110),
           (0.837, 0.097), (0.855, 0.089), (0.878, 0.084), (0.900, 0.082), (0.900, 0.0275)]

    # lower half, from outside: housing with its cover joints, shaft end, impeller
    half(0, L, -R, 0, FILL['housing'], 3)
    for x in (0.025, 0.27, 0.625, 0.765):
        ax.plot([X(x)] * 2, [Y(-R), Y(0)], color=INK, lw=hs.LW_THIN, zorder=3.5)
    half(L, 0.905, -0.0275, 0, FILL['steel'], 3)
    low = [(x, -r) for x, r in imp]
    fill(low, FILL['steel'], 3.2, [low])

    # upper half, cut: housing wall and end covers in the section tone, cavity inside
    fill([(0, 0), (0, R), (L, R), (L, 0)], FILL['section'], 3)
    cav = [(0.025, 0), (0.025, R - T), (0.765, R - T), (0.765, 0.035), (L, 0.035)]
    fill(cav + [(L, 0)], 'white', 3.2, [cav])
    for xa, xb in ((0.025, 0.27), (0.625, 0.765)):                            # AMB carriers
        part(xa, xb, 0.100, R - T, FILL['section'], z=4)
    for xa in (0.040, 0.728):                                                 # touchdown seats
        part(xa, xa + 0.022, 0.052, 0.100, FILL['section'], z=4)
    half(0.035, 0.905, 0, 0.0275, FILL['steel'], 4.6)                         # shaft
    for xa in (0.040, 0.728):                                                 # touchdown bearings
        part(xa, xa + 0.022, 0.031, 0.052, FILL['bearing'], z=5)
        ax.add_patch(plt.Circle((X(xa + 0.011), Y(0.0415)), SC * 0.0065, fc='white', ec=INK,
                                lw=hs.LW_THIN, zorder=5.2))
    for xa in (0.075, 0.131):                                                 # axial AMB stators
        part(xa, xa + 0.035, 0.036, 0.100, FILL['bearing'], z=5)
        part(xa + 0.008, xa + 0.027, 0.055, 0.082, FILL['copper'], z=5.3, lw=hs.LW_THIN)
    part(0.111, 0.130, 0.0275, 0.096, FILL['steel'], z=5)                     # thrust disc
    for xa in (0.190, 0.645):                                                 # radial AMBs
        hs.laminated(ax, X(xa), X(xa + 0.055), Y(0.043), Y(0.100), pitch=0.08, z=5)
        for xc in (xa - 0.009, xa + 0.055):
            part(xc, xc + 0.009, 0.052, 0.085, FILL['copper'], z=5.4, lw=hs.LW_THIN)
        hs.laminated(ax, X(xa - 0.004), X(xa + 0.059), Y(0.0275), Y(0.041), pitch=0.08, z=5)
    part(0.300, 0.600, 0.125, R - T, FILL['coolant'], z=4.2, lw=hs.LW_THIN)   # cooling jacket
    for x in np.linspace(0.300, 0.600, 9)[1:-1]:
        ax.plot([X(x)] * 2, [Y(0.125), Y(R - T)], color=INK, lw=hs.LW_THIN, zorder=4.3)
    hs.laminated(ax, X(0.330), X(0.570), Y(0.064), Y(0.125), pitch=0.10, z=5)  # stator core
    for xa in (0.285, 0.570):                                                 # end windings
        part(xa, xa + 0.045, 0.072, 0.115, FILL['copper'], z=5.3, r=0.012, lw=hs.LW_THIN)
    half(0.330, 0.570, 0, 0.061, FILL['rotor'], 5)                            # rotor
    ax.text(X(0.45), Y(0.031), 'rotor', ha='center', va='center', zorder=8)
    fill(imp, FILL['steel'], 5.5, [imp + [imp[0]]])                           # impeller, cut
    hub = [(0.900, 0.036), (0.870, 0.041), (0.845, 0.051), (0.826, 0.068), (0.813, 0.095),
           (0.806, 0.135)]
    ax.plot([X(x) for x, r in hub], [Y(r) for x, r in hub], color=INK, lw=hs.LW_THIN,
            zorder=5.6)
    half(0.900, 0.912, 0, 0.022, FILL['steel'], 5.7)                          # impeller nut
    ax.plot([X(-0.03), X(0.95)], [Y(0)] * 2, color=GREY, lw=hs.LW_THIN,
            ls=(0, (9, 2.5, 1.5, 2.5)), zorder=15)

    # labels: the parts inside, by leaders
    yt = Y(R) + 0.55
    hs.leader(ax, 'axial AMB', xy=(X(0.092), Y(0.092)), xytext=(X(-0.05), Y(0.125)), dot=True,
              ha='right')
    hs.leader(ax, 'touchdown\nbearing', xy=(X(0.051), Y(0.045)), xytext=(X(-0.05), Y(-0.02)),
              dot=True, ha='right', linespacing=1.1)
    hs.leader(ax, 'radial AMB', xy=(X(0.217), Y(0.090)), xytext=(X(0.19), yt), dot=True)
    hs.leader(ax, 'stator', xy=(X(0.45), Y(0.110)), xytext=(X(0.45), yt), dot=True)
    hs.leader(ax, 'radial AMB', xy=(X(0.672), Y(0.090)), xytext=(X(0.70), yt), dot=True)
    hs.leader(ax, 'impeller, on the\nmotor shaft', xy=(X(0.86), Y(-0.06)),
              xytext=(X(0.70), Y(-R) - 0.62), dot=True, linespacing=1.1)
    scale_bar(X, Y, 0.2, -R - 0.075, ((0, '0'), (0.2, '0.2 m')))
    ax.text(X(0.45), 0.40, '(c) The motor of (b), in half section', ha='center', va='center')
    return f


if __name__ == '__main__':
    want = sys.argv[1:] or list(FIGS)
    for num in want:
        png = hs.save(FIGS[num](), OUT + num.replace('1.', '1_0') if len(num) == 3 else OUT + num)
        print(f'Figure {num}: {png}')
