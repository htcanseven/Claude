import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
plt.rcParams.update({
    'font.family':'serif','font.serif':['DejaVu Serif'],'font.size':9,
    'axes.linewidth':0.8,'axes.grid':True,'grid.alpha':0.25,'grid.linewidth':0.5,
    'legend.frameon':True,'legend.framealpha':0.95,'legend.edgecolor':'0.7',
    'figure.dpi':300,'savefig.dpi':300,'savefig.bbox':'tight','savefig.pad_inches':0.03,
})
INK, ACC, ACC2, ACC3 = '#1a1a1a', '#1f4e79', '#a6350f', '#4a7c1f'
F='figures/'

# ------- Fig 1.6 : staggered labels, no collision
fig, ax = plt.subplots(figsize=(6.4,3.9))
labels = ['active\nvolume','centrifugal\nstress','iron\nloss','windage\nloss','$l/D$\nratio',r'$n_{\rm op}/n_{\rm cr}$']
series = [('(a) fixed geometry, overspeed', [2.00,4.00,4.00,8.00,1.00,2.00], ACC2),
          ('(b) tip-speed limited, $P$ const', [0.50,1.00,2.00,1.00,4.00,16.00], ACC),
          ('(c) length capped by rotordynamics', [0.58,1.33,2.00,1.33,2.60,7.79], ACC3)]
x = np.arange(len(labels)); w = 0.26
for i,(lab,vals,col) in enumerate(series):
    off = (i-1)*w
    ax.bar(x+off, vals, w, color=col, label=lab, edgecolor='white', lw=0.5)
    for xi, vi in zip(x+off, vals):
        ax.text(xi, vi*1.10, f'{vi:.2f}', ha='center', fontsize=6.3, color='0.25', rotation=90)
ax.axhline(1, color='0.4', lw=0.8, ls='--')
ax.set_yscale('log'); ax.set_ylim(0.3, 90)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7.5)
ax.set_ylabel('Factor change when speed is doubled')
ax.legend(loc='upper left', fontsize=7.3, ncol=1); ax.grid(axis='x', visible=False)
ax.set_title('The same speed doubling, three different design paths', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_06_scaling_paths.png'); plt.close(fig)

# ------- Fig 1.11 : gate clipped to triangle, labels inside
fig, ax = plt.subplots(figsize=(5.6,4.8)); ax.set_axis_off()
apex, bl, br = np.array([0.5,0.93]), np.array([0.07,0.20]), np.array([0.93,0.20])
V = np.array([apex,bl,br])
tri = Polygon(V, closed=True, fc='none', ec=INK, lw=1.7); ax.add_patch(tri)
inner = 0.5 + (V-np.array([0.5,0.44]))*0.58 + np.array([0,0.02])
ax.add_patch(Polygon(inner, closed=True, fc=ACC, alpha=0.12, ec=ACC, lw=1.0, ls='--'))
ax.text(0.5,0.50,'feasible\ndesigns', ha='center', va='center', fontsize=9, color=ACC, style='italic')

# converter gate, clipped to the triangle
ygate = 0.335
xl = np.interp(ygate,[bl[1],apex[1]],[bl[0],apex[0]])
xr = np.interp(ygate,[br[1],apex[1]],[br[0],apex[0]])
band = Polygon([[xl,ygate],[xr,ygate],[br[0],bl[1]],[bl[0],bl[1]]], closed=True,
               fc=ACC2, alpha=0.13, ec='none'); ax.add_patch(band)
ax.plot([xl,xr],[ygate,ygate], color=ACC2, lw=2.0, ls='--')
ax.text(0.5, 0.285, 'CONVERTER GATE', ha='center', fontsize=8.3, fontweight='bold', color=ACC2)
ax.text(0.5, 0.242, 'not reachable with the available\nswitching capability', ha='center',
        fontsize=6.9, color=ACC2, style='italic')

for (x,y),(t,s),va,dy in zip(V,
        [('MECHANICAL',r'$v_{\rm tip}$ limit, retention, fatigue'),
         ('ELECTROMAGNETIC',r'pole count, $f_1$, core and AC loss'),
         ('THERMAL','loss density, cooling, magnet temp.')],
        ['bottom','top','top'], [0.030,-0.035,-0.035]):
    ax.text(x, y+dy, t, ha='center', va=va, fontsize=8.8, fontweight='bold', color=INK)
    ax.text(x, y+dy+(0.036 if va=='bottom' else -0.040), s, ha='center', va=va, fontsize=6.7, color='0.35')

for a_,b_,lab,dx,dy in [(0,1,'sleeve thickness\nvs. air gap',0.085,0.02),
                        (0,2,'frequency\nvs. loss density',-0.085,0.02),
                        (1,2,'cooling geometry\nvs. rotor stiffness',0.0,0.055)]:
    m = (V[a_]+V[b_])/2
    ax.text(m[0]+dx, m[1]+dy, lab, ha='center', va='center', fontsize=6.6,
            color='0.42', style='italic')
ax.text(0.5, 0.085, 'SiC and GaN raise the gate; they do not remove it.',
        ha='center', fontsize=7.4, color='0.3', style='italic')
ax.set_xlim(0,1); ax.set_ylim(0.05,1.02)
ax.set_title('The high-speed design space: three constraints and a gate', fontsize=9.5, pad=4)
fig.savefig(F+'fig_1_11_design_space.png'); plt.close(fig)
print("fixed 2 figures")
