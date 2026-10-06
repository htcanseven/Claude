"""House style for the figures of *High-Speed Electrical Machines and Drives*.

Every figure in the book is drawn through this module, so the rules in
House_Style.md are enforced by code rather than remembered:

* every figure is made at exactly the text-block width, ``W_CM``, and placed in
  the manuscript at 100 %, so that what is drawn at 11 pt prints at 11 pt;
* every piece of text is Times New Roman at the body size, 11 pt;
* line weights, tick marks, colours and their paired line styles are fixed
  here, once;
* ``check(fig)`` refuses a figure whose text strays from the house font or
  size, and ``save()`` runs it before anything is written.

When Wiley confirms the trim size, change ``W_CM`` and regenerate: because
every figure is built at the same width, they all rescale together and stay
identical to one another.

Typical use::

    import hsbook_style as hs
    hs.setup()
    fig, ax = hs.figure(8.5)                  # a graph, full width, 8.5 cm tall
    ax.plot(x, y, label='...')
    ax.set_xlabel(hs.label('Rotational speed', 'n', 'r/min'))
    hs.save(fig, 'figures/ch1/fig_1_03')      # .png (600 dpi), .pdf, .svg

    fig, ax = hs.canvas(14.0)                 # an illustration; 1 unit = 1 cm
"""
from __future__ import annotations

import os
import re
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from cycler import cycler

# ───────────────────────────────────────────────────────────── geometry
W_CM = 15.92                    # text-block width of the manuscript (A4, 2.54 cm margins)
W_IN = W_CM / 2.54
CM = 1 / 2.54                   # inches per centimetre

# ───────────────────────────────────────────────────────────── typography
FONT = 'Times New Roman'        # the body font of the manuscript
SIZE = 11.0                     # pt, the body size; every text in every figure
# Metric-compatible substitutes, used only where Times New Roman is not installed.
# Liberation Serif and Nimbus Roman have identical advance widths, so a label
# laid out with them occupies exactly the space it will occupy in Times.
_FALLBACKS = ['Liberation Serif', 'Nimbus Roman', 'TeX Gyre Termes']

# ───────────────────────────────────────────────────────────── lines (pt, at final size)
LW_DATA = 1.2                   # curves in graphs
LW_OUTLINE = 1.0                # outlines of parts in illustrations
LW_AXES = 0.6                   # axes frame and ticks
LW_THIN = 0.5                   # leader lines, centre lines, dimension lines
LW_GRID = 0.4
LW_HATCH = 0.4

# ───────────────────────────────────────────────────────────── colour
# Colour is never the only carrier of meaning: each colour in the cycle is paired
# with its own line style, so every graph still reads in greyscale print.
INK = '#1a1a1a'
BLUE = '#1f4e79'
RUST = '#a6350f'
GREEN = '#4a7c1f'
GREY = '#6e6e6e'
CYCLE_COLOURS = [BLUE, RUST, GREEN, INK]
CYCLE_STYLES = ['-', '--', '-.', ':']

# Fills for illustrations: flat and light, so labels stay legible on them. No
# hatching and no gradients: a cut is shown by the darker 'section' tone, a
# laminated stack by thin lines across it (laminated()).
FILL = dict(
    housing='#f2f2ef',          # housings and casings seen from outside
    section='#dcdcd6',          # housing walls where a section or cut-away cuts them
    steel='#cfcfcf',            # shafts, discs and other solid steel parts
    rotor='#a6a6a6',            # rotor active parts drawn as one body
    lamination='#ffffff',       # laminated cores, with thin lines across the stack
    copper='#c9a227',           # windings and end windings
    coolant='#d7e4f0',          # cooling jackets and coolant
    oil='#f4e6d8',              # oil and lubrication equipment
    ground='#f5f5f5',           # floors, foundations
    bearing='#ffffff',          # bearings and bearing stators
)

LEADER = dict(arrowstyle='-', lw=LW_THIN, color=GREY, shrinkA=1, shrinkB=1)


def _house_font() -> str:
    names = {f.name for f in font_manager.fontManager.ttflist}
    for name in [FONT] + _FALLBACKS:
        if name in names:
            return name
    raise RuntimeError('No Times-compatible font installed; install Liberation Serif.')


RENDER_FONT = None


def setup() -> str:
    """Put matplotlib into house style; returns the font actually used for rendering."""
    global RENDER_FONT
    RENDER_FONT = _house_font()
    plt.rcParams.update({
        # text
        'font.family': 'serif', 'font.serif': [RENDER_FONT],
        'font.size': SIZE, 'axes.labelsize': SIZE, 'axes.titlesize': SIZE,
        'xtick.labelsize': SIZE, 'ytick.labelsize': SIZE, 'legend.fontsize': SIZE,
        'figure.titlesize': SIZE, 'legend.title_fontsize': SIZE,
        'mathtext.fontset': 'custom', 'mathtext.rm': RENDER_FONT,
        'mathtext.it': f'{RENDER_FONT}:italic', 'mathtext.bf': f'{RENDER_FONT}:bold',
        'mathtext.cal': f'{RENDER_FONT}:italic', 'mathtext.sf': RENDER_FONT,
        'mathtext.tt': RENDER_FONT,
        'mathtext.fallback': 'stix', 'axes.unicode_minus': True,
        # axes: full box, ticks inward on all four sides, light grid behind data
        'axes.linewidth': LW_AXES, 'axes.edgecolor': INK, 'axes.labelcolor': INK,
        'axes.grid': True, 'axes.axisbelow': True,
        'grid.color': '#d9d9d9', 'grid.linewidth': LW_GRID, 'grid.linestyle': '-',
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.major.size': 3.5, 'ytick.major.size': 3.5,
        'xtick.minor.size': 2.0, 'ytick.minor.size': 2.0,
        'xtick.major.width': LW_AXES, 'ytick.major.width': LW_AXES,
        'xtick.minor.width': LW_GRID, 'ytick.minor.width': LW_GRID,
        'xtick.color': INK, 'ytick.color': INK,
        'axes.labelpad': 4.0, 'xtick.major.pad': 4.0, 'ytick.major.pad': 4.0,
        # data
        'lines.linewidth': LW_DATA, 'lines.markersize': 6.0,
        'axes.prop_cycle': cycler(color=CYCLE_COLOURS, linestyle=CYCLE_STYLES),
        'hatch.linewidth': LW_HATCH, 'hatch.color': INK,
        # legend: no frame; direct labels on the curves are preferred where they fit
        'legend.frameon': False, 'legend.handlelength': 2.6, 'legend.borderaxespad': 0.6,
        'legend.labelspacing': 0.35,
        # output: never 'tight' — it would change the width the figure was built at
        'figure.dpi': 100, 'savefig.dpi': 600, 'savefig.bbox': None,
        'savefig.pad_inches': 0, 'savefig.facecolor': 'white',
        'svg.fonttype': 'none', 'pdf.fonttype': 42, 'ps.fonttype': 42,
        'svg.hashsalt': 'hsbook',     # stable ids: an unchanged figure rewrites identically
        'figure.constrained_layout.use': False,
    })
    return RENDER_FONT


# ───────────────────────────────────────────────────────────── building figures
def figure(height_cm: float, nrows: int = 1, ncols: int = 1, **kw):
    """A graph at the full text width. Constrained layout keeps every label inside."""
    fig, ax = plt.subplots(nrows, ncols, figsize=(W_IN, height_cm * CM),
                           layout='constrained', **kw)
    fig.get_layout_engine().set(w_pad=2 / 72, h_pad=2 / 72, wspace=0.06, hspace=0.06)
    return fig, ax


def canvas(height_cm: float):
    """An illustration at the full text width, drawn in centimetres of the printed page.

    One data unit is one centimetre on paper, so the designer knows that an 11 pt
    label is about 0.39 cm tall and can lay out parts and text without guessing.
    """
    fig = plt.figure(figsize=(W_IN, height_cm * CM))
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, W_CM); ax.set_ylim(0, height_cm)
    ax.set_aspect('equal'); ax.set_axis_off()
    # Illustrations draw in solid ink unless told otherwise; the colour/line-style
    # cycle is for distinguishing data series in graphs, not for drawing parts.
    ax.set_prop_cycle(cycler(color=[INK], linestyle=['-']))
    return fig, ax


def label(name: str, symbol: str | None = None, unit: str | None = None) -> str:
    """Axis label in the house form: 'Name *s* (unit)'.

    The symbol is set in italic; anything after an underscore is an upright
    descriptor subscript, as in the text: label('Speed', 'v_tip', 'm/s').
    """
    s = name
    if symbol:
        if '_' in symbol:
            base, sub = symbol.split('_', 1)
            s += rf' ${base}_{{\mathrm{{{sub}}}}}$'
        else:
            s += f' ${symbol}$'
    if unit:
        s += f' ({unit})'
    return s


def panel_label(ax, text: str, y: float = -0.16):
    """'(a) Short title', centred below a graph panel, at body size."""
    ax.text(0.5, y, text, transform=ax.transAxes, ha='center', va='top', fontsize=SIZE)


def leader(ax, text: str, xy, xytext, dot: bool = False, **kw):
    """A label joined to the part it names by a thin grey line without an arrowhead.

    A leader that ends inside a part, rather than on its outline, ends in a dot.
    """
    opts = dict(fontsize=SIZE, color=INK, ha='center', va='center',
                arrowprops=dict(LEADER), zorder=20)
    opts.update(kw)
    if dot:
        ax.plot(*xy, 'o', ms=2.6, mfc=GREY, mec='none', zorder=21)
    return ax.annotate(text, xy=xy, xytext=xytext, **opts)


def laminated(ax, x0, x1, y0, y1, pitch: float = 0.12, z: float = 4, lw: float = LW_OUTLINE):
    """A laminated stack seen from the side: white, with thin lines across it.

    Coordinates are those of a canvas (cm); the lines run across the stack,
    perpendicular to the shaft, one every `pitch` cm.
    """
    from matplotlib.patches import Rectangle
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc=FILL['lamination'], ec='none',
                           zorder=z))
    n = max(1, int(round((x1 - x0) / pitch)))
    for x in x0 + (x1 - x0) * (0.5 + np.arange(n)) / n:
        ax.plot([x, x], [y0, y1], color=GREY, lw=LW_THIN * 0.8, zorder=z + 0.1,
                solid_capstyle='butt')
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc='none', ec=INK, lw=lw,
                           zorder=z + 0.2))


NNBSP = '\u202f'                # narrow no-break space, the thousands separator


def number(v: float) -> str:
    """A tick number in the house form: 0.5, 1, 1500, 30 000 (grouped from five digits),
    with a true minus sign."""
    if v == 0:
        return '0'
    if abs(v) >= 1e4 and float(v).is_integer():
        s = f'{int(round(v)):,}'.replace(',', NNBSP)
    else:
        s = f'{v:g}'
    return s.replace('-', '\u2212')


def plain_log(axis, ticks=None):
    """Label a logarithmic axis with plain numbers (0.1, 1, 10, 100 000), not powers of ten."""
    from matplotlib.ticker import FuncFormatter, FixedLocator, NullFormatter
    if ticks is not None:
        axis.set_major_locator(FixedLocator(ticks))
    axis.set_major_formatter(FuncFormatter(lambda v, _: number(v)))
    axis.set_minor_formatter(NullFormatter())


# ───────────────────────────────────────────────────────────── enforcement
def check(fig) -> list[str]:
    """Every visible text must be the house font at the house size."""
    bad = []
    for t in fig.findobj(matplotlib.text.Text):
        if not t.get_visible() or not t.get_text().strip():
            continue
        size = t.get_fontsize()
        fam = t.get_fontname()
        if abs(size - SIZE) > 0.05:
            bad.append(f'{t.get_text()[:40]!r}: {size:g} pt')
        if fam not in (RENDER_FONT, FONT):
            bad.append(f'{t.get_text()[:40]!r}: font {fam}')
        if t.get_fontweight() not in ('normal', 400):
            bad.append(f'{t.get_text()[:40]!r}: weight {t.get_fontweight()}')
    return bad


def save(fig, stem: str) -> str:
    """Write .png (600 dpi, exact width), .pdf and .svg; refuse an off-style figure."""
    bad = check(fig)
    if bad:
        raise ValueError(f'{stem}: text off house style:\n  ' + '\n  '.join(bad))
    w, h = fig.get_size_inches()
    if abs(w - W_IN) > 1e-6:
        raise ValueError(f'{stem}: width {w * 2.54:.2f} cm, house width is {W_CM} cm')
    os.makedirs(os.path.dirname(stem) or '.', exist_ok=True)
    no_date = {'png': None, 'pdf': {'CreationDate': None}, 'svg': {'Date': None}}
    for ext in ('png', 'pdf', 'svg'):
        fig.savefig(f'{stem}.{ext}', metadata=no_date[ext])
    # In the SVG the labels stay text; name the house font first so the file opens
    # in Times New Roman, with the substitute it was laid out in as fallback.
    svg = open(f'{stem}.svg', encoding='utf-8').read()
    svg = re.sub(r"font-family:\s*'?" + re.escape(RENDER_FONT) + r"'?",
                 f"font-family:'{FONT}', '{RENDER_FONT}', serif", svg)
    open(f'{stem}.svg', 'w', encoding='utf-8').write(svg)
    plt.close(fig)
    return f'{stem}.png'
