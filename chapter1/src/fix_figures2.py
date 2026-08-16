import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
plt.rcParams.update({'font.family':'serif','font.serif':['DejaVu Serif'],'font.size':9,
    'axes.linewidth':0.8,'axes.grid':True,'grid.alpha':0.25,'grid.linewidth':0.5,
    'legend.frameon':True,'legend.framealpha':0.95,'legend.edgecolor':'0.7',
    'figure.dpi':300,'savefig.dpi':300,'savefig.bbox':'tight','savefig.pad_inches':0.03})
INK, ACC, ACC2, ACC3 = '#1a1a1a', '#1f4e79', '#a6350f', '#4a7c1f'; F='figures/'

# ---- Fig 1.2 cleaned: only the two labelled criteria
fig, ax = plt.subplots(figsize=(5.6,4.0))
P = np.logspace(-1,4,400)
ax.loglog(P, 1e5/np.sqrt(P), color=ACC, lw=2.0, label=r'$n\sqrt{P}=100\,000$  (machine criterion)')
ax.loglog(P, 60*1.8e5/(3*P), color=ACC2, lw=2.0, ls='--',
          label=r'$f_1P=180\,000$ kW/s  (drive criterion, $p=3$)')
ax.fill_between(P, 1e5/np.sqrt(P), 5e5, color=ACC, alpha=0.06)
ax.plot(120,30000,'o',ms=8,mfc='white',mec=INK,mew=1.7,zorder=6)
ax.annotate('worked example\n120 kW, 30 000 r/min', xy=(120,30000), xytext=(4.2,4.2e3),
            fontsize=7.5, ha='left', arrowprops=dict(arrowstyle='->',lw=0.7,color=INK))
ax.text(0.16, 1.4e5, 'high-speed region\n(by $n\\sqrt{P}$)', fontsize=7.2, color=ACC, style='italic')
ax.set_xlabel('Rated power  $P$  (kW)'); ax.set_ylabel('Rated speed  $n$  (r/min)')
ax.set_xlim(0.1,1e4); ax.set_ylim(1e3,5e5); ax.legend(loc='upper right', fontsize=7.2)
ax.set_title('Two speed criteria in the power$-$speed plane', fontsize=9.5, pad=7)
fig.savefig(F+'fig_1_02_classification_map.png'); plt.close(fig)

# ---- Fig 1.11 : no overlaps
fig, ax = plt.subplots(figsize=(5.6,4.8)); ax.set_axis_off()
apex,bl,br = np.array([0.5,0.93]), np.array([0.07,0.20]), np.array([0.93,0.20])
V = np.array([apex,bl,br])
ax.add_patch(Polygon(V, closed=True, fc='none', ec=INK, lw=1.7))
inner = 0.5 + (V-np.array([0.5,0.44]))*0.56 + np.array([0,0.045])
ax.add_patch(Polygon(inner, closed=True, fc=ACC, alpha=0.13, ec=ACC, lw=1.0, ls='--'))
ax.text(0.5,0.56,'feasible\ndesigns', ha='center', va='center', fontsize=9, color=ACC, style='italic')
ygate = 0.29
xl = np.interp(ygate,[bl[1],apex[1]],[bl[0],apex[0]]); xr = np.interp(ygate,[br[1],apex[1]],[br[0],apex[0]])
ax.add_patch(Polygon([[xl,ygate],[xr,ygate],[br[0],bl[1]],[bl[0],bl[1]]], closed=True, fc=ACC2, alpha=0.13, ec='none'))
ax.plot([xl,xr],[ygate,ygate], color=ACC2, lw=2.0, ls='--')
ax.text(0.5,0.248,'CONVERTER GATE', ha='center', fontsize=8.3, fontweight='bold', color=ACC2)
ax.text(0.5,0.213,'switching capability not available', ha='center', fontsize=6.8, color=ACC2, style='italic')
for (x,y),(t,s),va,dy in zip(V,
        [('MECHANICAL',r'$v_{\rm tip}$ limit, retention, fatigue'),
         ('ELECTROMAGNETIC',r'pole count, $f_1$, core and AC loss'),
         ('THERMAL','loss density, cooling, magnet temp.')],
        ['bottom','top','top'],[0.030,-0.035,-0.035]):
    ax.text(x,y+dy,t,ha='center',va=va,fontsize=8.8,fontweight='bold',color=INK)
    ax.text(x,y+dy+(0.036 if va=='bottom' else -0.040),s,ha='center',va=va,fontsize=6.7,color='0.35')
ax.text(0.235,0.60,'sleeve thickness\nvs. air gap',ha='center',fontsize=6.6,color='0.42',style='italic')
ax.text(0.765,0.60,'frequency\nvs. loss density',ha='center',fontsize=6.6,color='0.42',style='italic')
ax.text(0.5,0.345,'cooling geometry vs. rotor stiffness',ha='center',fontsize=6.6,color='0.42',style='italic')
ax.text(0.5,0.075,'SiC and GaN raise the gate; they do not remove it.',ha='center',fontsize=7.4,color='0.3',style='italic')
ax.set_xlim(0,1); ax.set_ylim(0.04,1.02)
ax.set_title('The high-speed design space: three constraints and a gate', fontsize=9.5, pad=4)
fig.savefig(F+'fig_1_11_design_space.png'); plt.close(fig)
print("ok")
