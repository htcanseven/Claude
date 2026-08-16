import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
plt.rcParams.update({
    'font.family':'serif','font.serif':['DejaVu Serif'],'font.size':9,
    'axes.linewidth':0.8,'axes.grid':True,'grid.alpha':0.25,'grid.linewidth':0.5,
    'legend.frameon':True,'legend.framealpha':0.95,'legend.edgecolor':'0.7',
    'figure.dpi':300,'savefig.dpi':300,'savefig.bbox':'tight','savefig.pad_inches':0.03,
})
INK, ACC, ACC2, ACC3 = '#1a1a1a', '#1f4e79', '#a6350f', '#4a7c1f'
F = 'figures/'

# ---------------------------------------------------------------- Fig 1.2
# Classification map: n vs P with iso-lines of n*sqrt(P) and fP
fig, ax = plt.subplots(figsize=(5.5,4.0))
P = np.logspace(-1, 4, 400)
for c in [1e5]:
    ax.loglog(P, c/np.sqrt(P), color=ACC, lw=1.8, label=r'$n\sqrt{P}=100\,000$')
for c, ls in [(1e5,':'), (1e6,'-.')]:
    ax.loglog(P, c/np.sqrt(P), color=ACC, lw=0.8, ls=ls, alpha=0.5)
for fp, ls in [(1.8e5,'--')]:
    ax.loglog(P, 60*fp/(3*P), color=ACC2, lw=1.8, ls=ls,
              label=r'$f_1P=180\,000$ kW/s  ($p=3$)')
for fp in [1.8e4, 1.8e6]:
    ax.loglog(P, 60*fp/(3*P), color=ACC2, lw=0.8, ls=':', alpha=0.5)
ax.plot(120, 30000, 'o', ms=8, mfc='white', mec=INK, mew=1.6, zorder=6)
ax.annotate('worked example\n120 kW, 30 000 r/min', xy=(120,30000), xytext=(330,62000),
            fontsize=7.5, ha='left', arrowprops=dict(arrowstyle='->', lw=0.7, color=INK))
ax.set_xlabel('Rated power  $P$  (kW)'); ax.set_ylabel('Rated speed  $n$  (r/min)')
ax.set_xlim(0.1,1e4); ax.set_ylim(1e3,5e5)
ax.legend(loc='upper right', fontsize=7.5)
ax.set_title('Two speed criteria in the power–speed plane', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_02_classification_map.png'); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.3
# Centrifugal stress vs tip speed
fig, ax = plt.subplots(figsize=(5.5,3.8))
v = np.linspace(0,350,400); rho, nu = 7650., 0.3
ax.plot(v, (3+nu)/8*rho*v**2/1e6,  color=ACC,  lw=1.8, label='solid disc')
ax.plot(v, (3+nu)/4*rho*v**2/1e6,  color=ACC2, lw=1.8, ls='--', label='disc with central bore')
ax.plot(v, rho*v**2/1e6,           color=ACC3, lw=1.8, ls='-.', label='thin ring (sleeve)')
for y, t in [(450,'high-strength electrical steel, $R_{p0.2}$'),
             (300,'design limit at safety factor 1.5')]:
    ax.axhline(y, color='0.45', lw=0.8, ls=':')
    ax.text(6, y+11, t, fontsize=7, color='0.3')
ax.axvline(150, color='0.6', lw=0.7)
ax.text(152, 620, r'$v_{\mathrm{tip}}=150$ m/s', fontsize=7, color='0.35', rotation=90, va='top')
ax.set_xlabel(r'Peripheral speed  $v_{\mathrm{tip}}$  (m/s)')
ax.set_ylabel('Maximum tangential stress (MPa)')
ax.set_xlim(0,350); ax.set_ylim(0,700); ax.legend(loc='upper left', fontsize=8)
ax.set_title('Centrifugal stress depends only on tip speed, not on r/min', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_03_stress_vs_tipspeed.png'); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.6
# Three scaling paths, grouped bars
fig, ax = plt.subplots(figsize=(6.2,3.9))
labels = ['active\nvolume','centrifugal\nstress','iron\nloss','windage\nloss','$l/D$\nratio',r'$n_{\rm op}/n_{\rm cr}$']
a = [2.00, 4.00, 4.00, 8.00, 1.00,  2.00]
b = [0.50, 1.00, 2.00, 1.00, 4.00, 16.00]
c = [0.58, 1.33, 2.00, 1.33, 2.60,  7.79]
x = np.arange(len(labels)); w = 0.26
ax.bar(x-w, a, w, color=ACC2, label='(a) fixed geometry, overspeed', edgecolor='white', lw=0.5)
ax.bar(x,   b, w, color=ACC,  label='(b) tip-speed limited, $P$ const', edgecolor='white', lw=0.5)
ax.bar(x+w, c, w, color=ACC3, label='(c) length capped by rotordynamics', edgecolor='white', lw=0.5)
for xi, vi in zip(np.r_[x-w,x,x+w], a+b+c):
    ax.text(xi, vi*1.09, f'{vi:.2f}', ha='center', fontsize=6.4, color='0.25')
ax.axhline(1, color='0.4', lw=0.8, ls='--')
ax.set_yscale('log'); ax.set_ylim(0.3, 40); ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7.5)
ax.set_ylabel('Factor change when speed is doubled')
ax.legend(loc='upper left', fontsize=7.5); ax.grid(axis='x', visible=False)
ax.set_title('The same speed doubling, three different design paths', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_06_scaling_paths.png'); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.7
# Critical speed divergence
fig, ax = plt.subplots(figsize=(5.5,3.8))
k = np.linspace(1,3,300)
ax.plot(k, k,        color=ACC,  lw=1.9, label=r'operating speed  $\propto\ \omega$')
ax.plot(k, k**-3.0,  color=ACC2, lw=1.9, ls='--', label=r'1st critical speed  $\propto\ \omega^{-3}$')
ax.plot(k, k**4.0,   color=ACC3, lw=1.9, ls='-.', label=r'ratio $n_{\rm op}/n_{\rm cr}\ \propto\ \omega^{4}$')
ax.fill_between(k, k**-3.0, k, color=ACC, alpha=0.06)
ax.plot(2, 16, 'o', ms=7, mfc='white', mec=INK, mew=1.5, zorder=6)
ax.annotate(r'speed $\times 2$  $\Rightarrow$  margin $\times 16$', xy=(2,16), xytext=(1.16,30),
            fontsize=8, arrowprops=dict(arrowstyle='->', lw=0.7, color=INK))
ax.set_yscale('log'); ax.set_xlim(1,3); ax.set_ylim(0.02,90)
ax.set_xlabel(r'Speed multiplier along the tip-speed-limited path')
ax.set_ylabel('Normalised value')
ax.legend(loc='lower left', fontsize=8)
ax.set_title('Why rotordynamics becomes binding before material strength', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_07_critical_speed_divergence.png'); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.9
# mf map: fundamental vs switching frequency
fig, ax = plt.subplots(figsize=(5.6,4.0))
f1 = np.logspace(1.5, 3.7, 400)
ax.fill_between(f1, 2e3, 16e3, color=ACC2, alpha=0.13, label='Si IGBT practical range')
ax.fill_between(f1, 16e3, 120e3, color=ACC3, alpha=0.13, label='SiC / GaN practical range')
ax.loglog(f1, 21*f1, color=ACC, lw=1.9, label=r'$m_f = 21$  (synchronous-PWM threshold)')
ax.loglog(f1, 10*f1, color=ACC, lw=0.9, ls=':', label=r'$m_f = 10$  (control stability floor)')
ax.plot(1500, 31500, 'o', ms=8, mfc='white', mec=INK, mew=1.6, zorder=6)
ax.annotate('worked example\n$f_1$=1500 Hz $\\Rightarrow$ $f_{sw}$=31.5 kHz\nSi cannot reach it',
            xy=(1500,31500), xytext=(140,60000), fontsize=7.5,
            arrowprops=dict(arrowstyle='->', lw=0.7, color=INK))
ax.set_xlabel('Fundamental frequency  $f_1$  (Hz)')
ax.set_ylabel('Required switching frequency  $f_{sw}$  (Hz)')
ax.set_xlim(30,5e3); ax.set_ylim(1e3,2e5); ax.legend(loc='lower right', fontsize=7)
ax.set_title('The converter gate: where silicon stops being an option', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_09_converter_gate.png'); plt.close(fig)

# ---------------------------------------------------------------- Fig 1.11
# Design space: triangle of constraints + converter gate
fig, ax = plt.subplots(figsize=(5.4,4.6)); ax.set_axis_off()
V = np.array([[0.5,0.95],[0.055,0.12],[0.945,0.12]])
ax.add_patch(Polygon(V, closed=True, fc='none', ec=INK, lw=1.6))
inner = 0.5 + (V-0.5)*0.60
ax.add_patch(Polygon(inner, closed=True, fc=ACC, alpha=0.11, ec=ACC, lw=1.1, ls='--'))
ax.text(0.5,0.45,'feasible\ndesigns', ha='center', va='center', fontsize=8.5, color=ACC, style='italic')
for (x,y),(t,s),va in zip(V,
        [('MECHANICAL',r'$v_{\rm tip}$ limit, retention, fatigue'),
         ('ELECTROMAGNETIC',r'pole count, $f_1$, core and AC losses'),
         ('THERMAL',r'loss density, cooling path, magnet temp.')],
        ['bottom','top','top']):
    dy = 0.035 if va=='bottom' else -0.045
    ax.text(x, y+dy, t, ha='center', va=va, fontsize=9, fontweight='bold', color=INK)
    ax.text(x, y+dy+(0.035 if va=='bottom' else -0.042), s, ha='center', va=va, fontsize=6.8, color='0.35')
for a_, b_, lab in [(0,1,'sleeve thickness\nvs. air gap'),(0,2,'frequency\nvs. loss density'),
                    (1,2,'cooling geometry\nvs. stiffness')]:
    m = (V[a_]+V[b_])/2
    off = (m-np.array([0.5,0.42])); off = off/np.linalg.norm(off)*0.085
    ax.text(*(m+off), lab, ha='center', va='center', fontsize=6.6, color='0.4', style='italic')
gx = np.linspace(0.02,0.98,2)
ax.plot(gx, 0.30+0*gx, color=ACC2, lw=2.0, ls='--')
ax.fill_between(gx, 0.02, 0.30, color=ACC2, alpha=0.10)
ax.text(0.5, 0.215, 'CONVERTER GATE', ha='center', fontsize=8, fontweight='bold', color=ACC2)
ax.text(0.5, 0.165, 'switching capability admits only part of the space;\nSiC raises the gate, it does not remove it',
        ha='center', fontsize=6.8, color=ACC2, style='italic')
ax.set_xlim(0,1); ax.set_ylim(0.03,1.06)
ax.set_title('The high-speed design space: three constraints and a gate', fontsize=9.5, pad=4)
fig.savefig(F+'fig_1_11_design_space.png'); plt.close(fig)
print("generated:")
import os
for f in sorted(os.listdir('figures')): print('  ', f, f"{os.path.getsize('figures/'+f)/1024:.0f} kB")
