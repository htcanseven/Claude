"""The two schematic figures that cannot be generated from an equation:
geared versus direct-drive architecture, and rotor bending modes."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Polygon, Circle

plt.rcParams.update({'font.family': 'serif', 'font.serif': ['DejaVu Serif'], 'font.size': 9,
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


# ─────────────────────────────────── (a) geared legacy  /  (b) direct drive
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.7))

ax1.set_axis_off(); ax1.set_xlim(0, 1); ax1.set_ylim(-.44, .56)
ax1.add_patch(Rectangle((0, -.44), 1, .44, fc='0.962', ec='none', zorder=0))
ax1.axhline(0, color='0.5', lw=1.1)
ax1.text(.012, .022, 'machine floor', fontsize=6.6, color='0.45', style='italic')
ax1.text(.012, -.415, 'basement', fontsize=6.6, color='0.45', style='italic')
ax1.text(.012, .520, '(a)   Geared arrangement', fontsize=9.2, fontweight='bold', color=INK)
ax1.text(.012, .455, '2\u20135 % gear loss  \u00b7  seals and oil changes  \u00b7  two storeys',
         fontsize=7.0, color=ACC2)

box(ax1, .050, .105, .205, .160, 'Induction motor', '4-pole,  1500 r/min')
box(ax1, .335, .105, .160, .160, 'Gearbox', 'step-up \u2248 \u00d720')
box(ax1, .580, .105, .190, .160, 'Compressor', '30 000 r/min')
for x0, x1 in ((.255, .335), (.495, .580)):
    ax1.plot([x0, x1], [.185, .185], color=INK, lw=2.4, solid_capstyle='butt', zorder=2)
    ax1.plot([(x0 + x1) / 2], [.185], marker='|', ms=9, color='0.4', mew=1.4, zorder=3)
impeller(ax1, .790, .185)

box(ax1, .310, -.345, .240, .160, 'Lubrication plant', 'tank,  pump,  cooler', fc=OIL)
for x in (.390, .452):
    ax1.plot([x, x], [-.185, .105], color=ACC2, lw=1.1, ls='--', zorder=1)
ax1.text(.575, -.105, 'oil feed and return', fontsize=6.6, color=ACC2, style='italic', va='center')

ax1.annotate('', xy=(.050, .350), xytext=(.770, .350),
             arrowprops=dict(arrowstyle='<->', lw=.9, color='0.35'))
ax1.text(.410, .372, 'footprint', ha='center', fontsize=6.8, color='0.35')

ax2.set_axis_off(); ax2.set_xlim(0, 1); ax2.set_ylim(-.44, .56)
ax2.add_patch(Rectangle((0, -.44), 1, .44, fc='0.962', ec='none', zorder=0))
ax2.axhline(0, color='0.5', lw=1.1)
ax2.text(.012, .022, 'machine floor', fontsize=6.6, color='0.45', style='italic')
ax2.text(.012, .520, '(b)   Integrated direct drive', fontsize=9.2, fontweight='bold', color=INK)
ax2.text(.012, .455, 'no gearbox  \u00b7  no oil system  \u00b7  no basement',
         fontsize=7.0, color=ACC3)

ax2.add_patch(FancyBboxPatch((.050, .062), .525, .228,
                             boxstyle='round,pad=0.006,rounding_size=0.014',
                             fc='none', ec=ACC3, lw=1.6, ls='--', zorder=2))
box(ax2, .150, .115, .250, .130, 'High-speed machine', '2-pole,  30 000 r/min', fs=7.2)
ax2.plot([.078, .490], [.180, .180], color=INK, lw=2.4, solid_capstyle='butt', zorder=2)
for x in (.108, .432):
    ax2.add_patch(Circle((x, .180), .021, fc='white', ec=ACC2, lw=1.5, zorder=5))
    ax2.plot([x], [.180], marker='o', ms=2.4, color=ACC2, zorder=6)
    ax2.text(x, .098, 'AMB', ha='center', fontsize=6.3, color=ACC2)
impeller(ax2, .512, .180)
ax2.text(.512, .098, 'impeller', ha='center', fontsize=6.3, color='0.35', style='italic')

ax2.annotate('', xy=(.050, .360), xytext=(.575, .360),
             arrowprops=dict(arrowstyle='<->', lw=.9, color='0.35'))
ax2.text(.3125, .382, 'footprint', ha='center', fontsize=6.8, color='0.35')
ax2.text(.625, .272, 'One hermetically sealed unit.', fontsize=7.4,
         color=ACC3, va='top', fontweight='bold')
ax2.text(.625, .212, 'Gearbox, couplings and oil system\nare deleted; the burden moves to\nthe rotor and to the converter.',
         fontsize=7.2, color=ACC3, va='top', linespacing=1.5)
ax2.text(.290, -.185, 'the two-storey layout disappears', ha='center',
         fontsize=7.2, color='0.45', style='italic')

fig.savefig(F + 'fig_geared_vs_directdrive.png'); plt.close(fig)

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
