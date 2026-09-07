"""The two schematic figures that cannot be generated from an equation:
geared versus direct-drive architecture, and rotor bending modes."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle

plt.rcParams.update({'font.family': 'serif', 'font.serif': ['DejaVu Serif'], 'font.size': 9,
                     'svg.fonttype': 'none', 'pdf.fonttype': 42, 'ps.fonttype': 42,
                     'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
                     'savefig.pad_inches': 0.04})
INK, ACC, ACC2, ACC3 = '#1a1a1a', '#1f4e79', '#a6350f', '#4a7c1f'
STEEL, OIL = '#dde5ee', '#f4e6d8'
F = 'figures/'


def box(ax, x, y, w, h, label, sub=None, fc=STEEL, fs=7.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.006,rounding_size=0.012',
                                fc=fc, ec=INK, lw=1.1, zorder=3))
    ax.text(x + w / 2, y + h / 2 + (0.020 if sub else 0), label, ha='center', va='center',
            fontsize=fs, zorder=4, fontweight='bold')
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.030, sub, ha='center', va='center',
                fontsize=fs - 1.4, color='0.3', zorder=4)


def impeller(ax, x, y, s=0.026):
    for a in np.linspace(0, 2 * np.pi, 9)[:-1]:
        ax.add_patch(Polygon([[x, y],
                              [x + s * np.cos(a), y + s * np.sin(a) * 1.6],
                              [x + s * .7 * np.cos(a + .45), y + s * .7 * np.sin(a + .45) * 1.6]],
                             fc=ACC, ec=ACC, lw=.5, alpha=.85, zorder=4))


# ─────────────────────────────────── (a) geared train  /  (b) direct drive
# Drawn as an engineering elevation and an axial section rather than as a block
# diagram: shaft centre lines, section hatching on cut material, end shields.
matplotlib.rcParams['hatch.linewidth'] = 0.45
CL = dict(color='0.25', lw=0.7, ls=(0, (11, 3, 1.6, 3)), zorder=1)   # dash-dot centre line
OUT = dict(ec=INK, lw=1.15, zorder=4)
THIN = dict(color=INK, lw=0.7, zorder=4)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.6, 6.6))


def mirror(ax, fn):
    """Draw a part above and below the centre line."""
    fn(ax, +1); fn(ax, -1)


def rect(ax, x0, x1, y0, y1, sgn=1, fc='white', hatch=None, ec=INK, lw=1.15, z=4, alpha=1):
    ax.add_patch(Rectangle((x0, sgn * y0 if sgn > 0 else sgn * y1),
                           x1 - x0, y1 - y0, fc=fc, ec=ec, lw=lw, hatch=hatch,
                           zorder=z, alpha=alpha))


# ── (a) geared train, axial section ────────────────────────────────────────
ax1.set_axis_off(); ax1.set_xlim(0, 1); ax1.set_ylim(-.70, .52)
ax1.text(.010, .462, '(a)   Geared train,  axial section',
         fontsize=9.4, fontweight='bold', color=INK)

YM, YC = -.055, .050            # motor centre line, compressor centre line


def housing(ax, x0, x1, yc, h, wall=.024, fc='#f4f4f1'):
    for sgn in (1, -1):
        ax.add_patch(Polygon([[x0, yc + sgn * .030], [x0, yc + sgn * h],
                              [x1, yc + sgn * h], [x1, yc + sgn * .030],
                              [x1 - wall, yc + sgn * .030], [x1 - wall, yc + sgn * (h - wall)],
                              [x0 + wall, yc + sgn * (h - wall)], [x0 + wall, yc + sgn * .030]],
                             closed=True, fc=fc, hatch='xx', ec=INK, lw=1.1, zorder=3))


def band(ax, x0, x1, yc, r0, r1, **kw):
    for sgn in (1, -1):
        lo = yc + sgn * r0 if sgn > 0 else yc - r1
        ax.add_patch(Rectangle((x0, lo), x1 - x0, r1 - r0, zorder=5, **kw))


def bearing(ax, xc, yc, r0=.020, r1=.050, w=.020):
    for sgn in (1, -1):
        lo = yc + sgn * r0 if sgn > 0 else yc - r1
        ax.add_patch(Rectangle((xc - w / 2, lo), w, r1 - r0, fc='white', hatch='\\\\\\',
                               ec=INK, lw=1.0, zorder=6))


# motor, sectioned
ax1.plot([.030, .360], [YM, YM], **CL)
housing(ax1, .062, .286, YM, .172)
band(ax1, .028, .352, YM, 0, .016, fc='0.80', ec=INK, lw=1.1)
band(ax1, .112, .232, YM, .026, .076, fc='0.86', ec=INK, lw=1.1)
band(ax1, .106, .238, YM, .086, .146, fc='white', hatch='///', ec=INK, lw=1.1)
for xw in (.080, .238):
    for sgn in (1, -1):
        ax1.add_patch(FancyBboxPatch((xw, YM + .094 if sgn > 0 else YM - .140), .026, .046,
                                     boxstyle='round,pad=0.002,rounding_size=0.008',
                                     fc='#c9a227', ec=INK, lw=.8, zorder=5))
bearing(ax1, .098, YM); bearing(ax1, .250, YM)
ax1.text(.174, .356, 'motor', ha='center', fontsize=7.6, fontweight='bold', zorder=7)
ax1.text(.174, .316, '1500 r/min', ha='center', fontsize=6.4, color='0.3', zorder=7)

for dx in (-.014, .006):        # coupling flanges
    ax1.add_patch(Rectangle((.312 + dx, YM - .046), .009, .092, fc='0.62', ec=INK, lw=.8, zorder=6))

# gearbox: the casing is sectioned, the inside is not drawn.  The input and
# output shafts leave at different heights, which is what makes it a step-up.
ax1.add_patch(Polygon([[.352, -.238], [.352, .232], [.536, .232], [.536, -.238]],
                      closed=True, fc='none', ec=INK, lw=1.2, zorder=4))
for poly in ([[.352, -.238], [.352, .232], [.376, .232], [.376, -.238]],
             [[.512, -.238], [.512, .232], [.536, .232], [.536, -.238]],
             [[.352, .208], [.352, .232], [.536, .232], [.536, .208]],
             [[.352, -.238], [.352, -.214], [.536, -.214], [.536, -.238]]):
    ax1.add_patch(Polygon(poly, closed=True, fc='#f0efe9', hatch='xx', ec=INK, lw=1.1, zorder=4))
ax1.text(.444, .356, 'gearbox', ha='center', fontsize=7.6, fontweight='bold', zorder=7)
ax1.text(.444, .316, 'step-up  × 20', ha='center', fontsize=6.4, color='0.3', zorder=7)
ax1.text(.444, .010, 'sealed\ncasing', ha='center', va='center', fontsize=6.2,
         color='0.5', style='italic', zorder=7, linespacing=1.5)

# compressor, sectioned, on the raised output centre line
ax1.plot([.520, .900], [YC, YC], **CL)
band(ax1, .524, .884, YC, 0, .016, fc='0.80', ec=INK, lw=1.1)
for dx in (-.014, .006):
    ax1.add_patch(Rectangle((.556 + dx, YC - .046), .009, .092, fc='0.62', ec=INK, lw=.8, zorder=6))
housing(ax1, .596, .784, YC, .150)
bearing(ax1, .634, YC); bearing(ax1, .746, YC)
ax1.text(.690, .356, 'compressor', ha='center', fontsize=7.6, fontweight='bold', zorder=7)
ax1.text(.690, .316, '30 000 r/min', ha='center', fontsize=6.4, color='0.3', zorder=7)
for sgn in (1, -1):
    ax1.add_patch(Polygon([[.822, YC + sgn * .016], [.884, YC + sgn * .132],
                           [.900, YC + sgn * .108], [.842, YC + sgn * .012]],
                          fc=ACC, ec=INK, lw=.8, zorder=6))
    ax1.add_patch(Polygon([[.820, YC + sgn * .010], [.868, YC + sgn * .070],
                           [.884, YC + sgn * .046], [.834, YC + sgn * .007]],
                          fc=ACC, ec=INK, lw=.8, alpha=.75, zorder=6))

LBL1 = dict(fontsize=6.2, color='0.28', ha='center', zorder=8,
            arrowprops=dict(arrowstyle='-', lw=.6, color='0.5', shrinkA=0, shrinkB=2))
ax1.annotate('coupling', xy=(.312, YM + .046), xytext=(.312, .196), **LBL1)
ax1.annotate('coupling', xy=(.556, YC + .046), xytext=(.560, .238), **LBL1)
ax1.annotate('rolling bearings', xy=(.098, YM + .050), xytext=(.106, .196), **LBL1)

ax1.add_patch(Rectangle((.050, -.300), .845, .034, fc='0.87', ec=INK, lw=1.0, zorder=3))
ax1.text(.470, -.283, 'common baseplate', ha='center', va='center', fontsize=6.2,
         color='0.3', style='italic', zorder=6)
ax1.plot([0, 1], [-.336, -.336], color='0.5', lw=1.0)
ax1.add_patch(Rectangle((0, -.70), 1, .364, fc='0.965', ec='none', zorder=0))
ax1.text(.012, -.364, 'machine floor', fontsize=6.4, color='0.45', style='italic')
ax1.add_patch(Rectangle((.340, -.570), .230, .118, fc=OIL, ec=INK, lw=1.0, zorder=4))
ax1.text(.455, -.494, 'lubrication skid', ha='center', fontsize=6.9, fontweight='bold', zorder=6)
ax1.text(.455, -.538, 'tank  ·  pump  ·  cooler', ha='center', fontsize=6.1, color='0.35', zorder=6)
for x in (.396, .514):
    ax1.plot([x, x], [-.452, -.300], color=ACC2, lw=.9, ls='--', zorder=1)
ax1.text(.596, -.366, 'oil feed and return', fontsize=6.4, color=ACC2, style='italic', va='top')
ax1.text(.012, -.652, '2–5 % gear loss  ·  seals and oil changes  ·  a second storey below the floor',
         fontsize=6.9, color=ACC2)
ax1.text(.012, -.608, 'the gearbox casing is sealed; its input and output shafts leave at different heights',
         fontsize=6.4, color='0.45', style='italic')


# ── (b) integrated direct drive: axial section ─────────────────────────────
ax2.set_axis_off(); ax2.set_xlim(0, 1); ax2.set_ylim(-.46, .40)
ax2.text(.010, .348, '(b)   Integrated direct drive,  axial section',
         fontsize=9.4, fontweight='bold', color=INK)

ax2.plot([.055, .905], [0, 0], **CL)
HOUS_X0, HOUS_X1 = .128, .742
for sgn in (1, -1):
    ax2.add_patch(Polygon([[HOUS_X0, sgn * .034], [HOUS_X0, sgn * .245],
                           [HOUS_X1, sgn * .245], [HOUS_X1, sgn * .034],
                           [HOUS_X1 - .026, sgn * .034], [HOUS_X1 - .026, sgn * .219],
                           [HOUS_X0 + .026, sgn * .219], [HOUS_X0 + .026, sgn * .034]],
                          closed=True, fc='#f4f4f1', hatch='xx', ec=INK, lw=1.15, zorder=3))
    rect(ax2, .318, .566, .196, .219, sgn=sgn, fc='#d7e4f0', lw=.8, z=4)
    rect(ax2, .095, .862, 0, .030, sgn=sgn, fc='0.80', lw=1.15, z=5)
    rect(ax2, .336, .548, .030, .112, sgn=sgn, fc='0.66', lw=1.15, z=5)
    rect(ax2, .330, .554, .124, .196, sgn=sgn, fc='white', hatch='///', lw=1.15, z=5)
    for xw in (.300, .554):
        ax2.add_patch(FancyBboxPatch((xw, .134 if sgn > 0 else -.186), .030, .052,
                                     boxstyle='round,pad=0.002,rounding_size=0.010',
                                     fc='#c9a227', ec=INK, lw=.8, zorder=5))
ax2.plot([.095, .862], [0, 0], **CL)
ax2.text(.442, .071, 'solid rotor', ha='center', va='center', fontsize=6.6, color='white',
         fontweight='bold', zorder=7)
ax2.text(.442, .160, 'stator core', ha='center', va='center', fontsize=6.4, zorder=7)

for x0, x1 in ((.176, .268), (.612, .704)):
    for sgn in (1, -1):
        rect(ax2, x0 + .006, x1 - .006, .030, .074, sgn=sgn, fc='0.88', lw=1.0, z=5)
        rect(ax2, x0, x1, .086, .168, sgn=sgn, fc='white', hatch='\\\\\\', lw=1.15, z=5)
for x in (.146, .724):
    for sgn in (1, -1):
        rect(ax2, x - .010, x + .010, .032, .056, sgn=sgn, fc=ACC2, lw=.7, z=6, alpha=.55)
for sgn in (1, -1):
    ax2.add_patch(Polygon([[.800, sgn * .030], [.874, sgn * .162], [.890, sgn * .136],
                           [.826, sgn * .026]], fc=ACC, ec=INK, lw=.8, zorder=6))
    ax2.add_patch(Polygon([[.798, sgn * .022], [.856, sgn * .090], [.872, sgn * .064],
                           [.818, sgn * .018]], fc=ACC, ec=INK, lw=.8, alpha=.75, zorder=6))

LBL = dict(fontsize=6.2, color='0.28', ha='center', zorder=8,
           arrowprops=dict(arrowstyle='-', lw=.6, color='0.5', shrinkA=0, shrinkB=2))
ax2.annotate('cooling jacket', xy=(.470, .219), xytext=(.500, .282), **LBL)
ax2.annotate('end winding', xy=(.312, .176), xytext=(.226, .282), **LBL)
ax2.annotate('impeller, overhung on\nthe shaft end, outboard\nof the drive-end bearing',
             xy=(.856, .120), xytext=(.845, .282), linespacing=1.4, **LBL)
ax2.annotate('touchdown bearing', xy=(.146, -.056), xytext=(.088, -.322),
             fontsize=6.2, color='0.28', ha='center', zorder=8,
             arrowprops=dict(arrowstyle='-', lw=.6, color='0.5', shrinkA=0, shrinkB=2))
for xc in (.222, .658):
    ax2.annotate('radial AMB', xy=(xc, -.168), xytext=(xc, -.290), fontsize=6.4, color=ACC2,
                 ha='center', zorder=8,
                 arrowprops=dict(arrowstyle='-', lw=.7, color=ACC2, shrinkA=0, shrinkB=2))
ax2.annotate('', xy=(HOUS_X0, -.360), xytext=(.892, -.360),
             arrowprops=dict(arrowstyle='<->', lw=.8, color='0.4'))
ax2.text(.510, -.428, 'one machine: no gearbox, no couplings, no oil system',
         ha='center', fontsize=7.0, color=ACC3, fontweight='bold')

for _ext in ('png', 'svg', 'pdf'):
    fig.savefig(F + 'fig_geared_vs_directdrive.' + _ext)
plt.close(fig)

# The SVG keeps its text as text (svg.fonttype='none'), so labels stay editable.
# Point the font stack at Times New Roman first so the drawing opens in the same
# face as the manuscript; DejaVu Serif remains the fallback the layout was set in.
_svg = F + 'fig_geared_vs_directdrive.svg'
_s = open(_svg, encoding='utf-8').read()
_s = _s.replace("'DejaVu Serif', serif", "'Times New Roman', 'DejaVu Serif', serif")
open(_svg, 'w', encoding='utf-8').write(_s)

# ────────────────────────────────────────────────────────── bending modes
fig, axes = plt.subplots(2, 1, figsize=(5.9, 4.1))
L, sup = 1.0, (.13, .87)
span = sup[1] - sup[0]
x = np.linspace(0, L, 500)
xi = np.clip((x - sup[0]) / span, 0, 1)

for ax, (n, name, col) in zip(axes, [(1, 'First bending mode', ACC),
                                     (2, 'Second bending mode', ACC2)]):
    ax.set_axis_off(); ax.set_xlim(-.06, 1.06); ax.set_ylim(-.44, .44)
    ax.plot([0, L], [0, 0], color='0.55', lw=1.0, ls=(0, (5, 4)), zorder=1)
    y = np.sin(n * np.pi * xi) * .245
    y[(x < sup[0]) | (x > sup[1])] = 0
    ax.plot(x, y, color=col, lw=2.3, zorder=3)
    ax.plot(x, -y, color=col, lw=1.0, alpha=.30, ls='--', zorder=2)
    for xs in (0.0, L - .075):
        ax.add_patch(Rectangle((xs, -.046), .075, .092, fc='0.84', ec=INK, lw=.8, zorder=4))
    for s in sup:
        ax.add_patch(Polygon([[s - .028, -.118], [s + .028, -.118], [s, -.020]],
                             fc='0.72', ec=INK, lw=.9, zorder=5))
        ax.plot([s - .042, s + .042], [-.128, -.128], color=INK, lw=1.3, zorder=5)
        ax.text(s, -.205, 'bearing', ha='center', fontsize=6.4, color='0.4')
    for k in range(1, n):
        xn = sup[0] + span * k / n
        ax.plot([xn], [0], marker='o', ms=5.5, mfc='white', mec=col, mew=1.6, zorder=6)
        ax.text(xn, .055, 'node', ha='center', fontsize=6.4, color=col, style='italic')
    ax.text(-.045, .335, name, fontsize=8.8, fontweight='bold', color=INK)

axes[0].text(.5, .335, 'undeflected axis dashed', ha='center', fontsize=6.6,
             color='0.45', style='italic')
axes[1].annotate('', xy=(sup[0], -.335), xytext=(sup[1], -.335),
                 arrowprops=dict(arrowstyle='<->', lw=.9, color='0.35'))
axes[1].text(.5, -.322, 'bearing span  $l$', ha='center', va='bottom',
             fontsize=7.2, color='0.35')
fig.suptitle('Bending modes of a slender rotor:  '
             r'$n_{\mathrm{cr}}\propto r_r/l^{2}$', fontsize=9.5, y=.972)
fig.savefig(F + 'fig_bending_modes.png'); plt.close(fig)
print('generated fig_geared_vs_directdrive.png and fig_bending_modes.png')

# ──────────────────────────────────── Taylor–Couette flow in the air gap
fig, axes = plt.subplots(1, 2, figsize=(6.3, 3.2))
GAPY = (0.0, 1.0)

for ax, (title, vortex) in zip(axes, [('(a)  Laminar Couette flow\nlow Taylor number', False),
                                      ('(b)  Taylor vortices\nabove the critical Taylor number', True)]):
    ax.set_axis_off(); ax.set_xlim(-.22, 1.02); ax.set_ylim(-.60, 1.30)
    # stator (top) and rotor (bottom) walls of the developed annulus
    ax.add_patch(Rectangle((0, 1.0), 1.0, .17, fc='0.86', ec=INK, lw=1.0, zorder=4))
    ax.add_patch(Rectangle((0, -.17), 1.0, .17, fc=STEEL, ec=INK, lw=1.0, zorder=4))
    ax.text(.5, 1.085, 'stator bore', ha='center', va='center', fontsize=7.0, zorder=5)
    ax.text(.5, -.085, 'rotor surface', ha='center', va='center', fontsize=7.0, zorder=5)
    ax.annotate('', xy=(-.075, 0), xytext=(-.075, 1.0),
                arrowprops=dict(arrowstyle='<->', lw=.9, color='0.4'))
    ax.text(-.105, .5, 'gap  $\\delta$', ha='right', va='center', fontsize=7.2, color='0.4')
    ax.annotate('', xy=(.34, -.285), xytext=(.06, -.285),
                arrowprops=dict(arrowstyle='->', lw=1.4, color=ACC))
    ax.text(.37, -.285, '$v_{\\mathrm{tip}}$', va='center', fontsize=7.6, color=ACC)

    if not vortex:
        for y in np.linspace(.10, .90, 7):
            ax.plot([.04, .96], [y, y], color=ACC, lw=1.0, alpha=.75, zorder=3)
            ax.annotate('', xy=(.62 + .30 * (1 - y), y), xytext=(.58 + .30 * (1 - y), y),
                        arrowprops=dict(arrowstyle='->', lw=.9, color=ACC, alpha=.8))
        ax.text(.5, 1.235, 'velocity varies smoothly across the gap;\ndrag is modest',
                ha='center', fontsize=6.8, color='0.35', style='italic')
    else:
        n_cell = 5
        for k in range(n_cell):
            xc = (k + .5) / n_cell
            sgn = 1 if k % 2 == 0 else -1
            for r in (.30, .62, .94):
                th = np.linspace(0, 2 * np.pi, 200)
                ax.plot(xc + r * np.cos(th) * .088, .5 + r * np.sin(th) * .43,
                        color=ACC2, lw=.95, alpha=.85, zorder=3)
            ax.annotate('', xy=(xc + sgn * .052, .60), xytext=(xc + sgn * .052, .40),
                        arrowprops=dict(arrowstyle='->', lw=1.1, color=ACC2))
        ax.text(.5, 1.235, 'counter-rotating toroidal cells;\ndrag and rotor heating rise sharply',
                ha='center', fontsize=6.8, color='0.35', style='italic')
    ax.text(.5, -.475, title, ha='center', va='center', fontsize=8.0, fontweight='bold', color=INK)

fig.suptitle('Flow regimes in the air gap', fontsize=9.5, y=1.045)
fig.savefig(F + 'fig_taylor_vortices.png'); plt.close(fig)
print('generated fig_taylor_vortices.png')
