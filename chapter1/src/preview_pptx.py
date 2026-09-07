"""Read a .pptx back and draw what is actually in it.

LibreOffice cannot open a file in this environment, so the only honest way to
check the PowerPoint version of Figure 1.2 is to parse the shapes out of the
saved file and re-plot them.  What this renders is what PowerPoint will show:
geometry, stacking order, fills, hatch patterns and label positions all come
from the .pptx, not from the matplotlib figure it was built from.

usage:  python3 src/preview_pptx.py figures/editable/Figure_1_2.pptx out.png
"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyBboxPatch
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.oxml.ns import qn

EMU = 914400.0
PAT = {'ltUpDiag': '///', 'ltDnDiag': '\\\\\\', 'diagCross': 'xx'}
DASH = {'dashDot': (0, (9, 3, 1.5, 3)), 'dash': (0, (5, 3)), 'sysDot': (0, (1, 2))}


def _fill(spPr):
    """→ (facecolor, hatch) for the shape's fill."""
    if spPr is None or spPr.find(qn('a:noFill')) is not None:
        return 'none', None
    solid = spPr.find(qn('a:solidFill'))
    if solid is not None:
        return _clr(solid), None
    patt = spPr.find(qn('a:pattFill'))
    if patt is not None:
        bg = patt.find(qn('a:bgClr'))
        return (_clr(bg) if bg is not None else 'white'), PAT.get(patt.get('prst'), '//')
    return 'none', None


def _clr(node, default='#000000'):
    c = node.find(qn('a:srgbClr'))
    if c is None:
        return default
    a = c.find(qn('a:alpha'))
    hexv = '#' + c.get('val')
    if a is not None:
        return matplotlib.colors.to_rgba(hexv, int(a.get('val')) / 100000.0)
    return hexv


def _line(spPr):
    """→ (edgecolor, linewidth in points, dash) for the shape's outline."""
    ln = None if spPr is None else spPr.find(qn('a:ln'))
    if ln is None or ln.find(qn('a:noFill')) is not None:
        return 'none', 0, None
    sf = ln.find(qn('a:solidFill'))
    w = int(ln.get('w') or 12700) / 12700.0
    d = ln.find(qn('a:prstDash'))
    return (_clr(sf) if sf is not None else '#000000'), w, DASH.get(d.get('val') if d is not None else None)


def walk(shapes):
    """Flatten the groups; chOff == off, so child offsets are already slide EMU."""
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def render(path, out):
    prs = Presentation(path)
    W, H = prs.slide_width / EMU, prs.slide_height / EMU
    fig, ax = plt.subplots(figsize=(W, H))
    fig.subplots_adjust(0, 0, 1, 1)
    ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.set_axis_off()
    matplotlib.rcParams['hatch.linewidth'] = 0.45
    n = 0

    for sh in walk(prs.slides[0].shapes):
        el = sh._element
        spPr = el.find(qn('p:spPr'))
        x, y = sh.left / EMU, sh.top / EMU
        w, h = (sh.width or 0) / EMU, (sh.height or 0) / EMU
        fc, hatch = _fill(spPr)
        ec, lw, dash = _line(spPr)
        n += 1

        cust = None if spPr is None else spPr.find(qn('a:custGeom'))
        prst = None if spPr is None else spPr.find(qn('a:prstGeom'))

        if cust is not None:
            p = cust.find(qn('a:pathLst')).find(qn('a:path'))
            pts, closed = [], False
            for node in p:
                if node.tag in (qn('a:moveTo'), qn('a:lnTo')):
                    pt = node.find(qn('a:pt'))
                    pts.append((x + int(pt.get('x')) / EMU, y + int(pt.get('y')) / EMU))
                elif node.tag == qn('a:close'):
                    closed = True
            if closed:
                ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=ec, lw=lw, hatch=hatch))
            else:
                ax.plot(*zip(*pts), color=ec, lw=lw, ls=dash or '-')
        elif el.tag == qn('p:cxnSp'):
            xf = spPr.find(qn('a:xfrm'))
            flipH = xf.get('flipH') == '1'; flipV = xf.get('flipV') == '1'
            x0, x1 = (x + w, x) if flipH else (x, x + w)
            y0, y1 = (y + h, y) if flipV else (y, y + h)
            ax.plot([x0, x1], [y0, y1], color=ec, lw=lw, ls=dash or '-')
        elif prst is not None and prst.get('prst') == 'roundRect':
            ax.add_patch(FancyBboxPatch((x + h * .12, y + h * .12), w - h * .24, h - h * .24,
                                        boxstyle=f'round,pad={h * .12:.4f}',
                                        fc=fc, ec=ec, lw=lw, hatch=hatch))
        elif prst is not None:
            ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, hatch=hatch))

        if sh.has_text_frame and sh.text_frame.text.strip():
            tf = sh.text_frame
            anch = (tf._txBody.find(qn('a:bodyPr')).get('anchor') or 't')
            paras = [p for p in tf.paragraphs]
            r0 = paras[0].runs[0]
            fs = r0.font.size.pt if r0.font.size else 10
            ha = {None: 'left', 1: 'center', 2: 'right', 3: 'left'}.get(
                paras[0].alignment and paras[0].alignment.value or None, 'left')
            va = {'t': 'top', 'ctr': 'center', 'b': 'bottom'}[anch]
            tx = {'left': x, 'center': x + w / 2, 'right': x + w}[ha]
            ty = {'top': y, 'center': y + h / 2, 'bottom': y + h}[va]
            ax.text(tx, ty, '\n'.join(p.text for p in paras), fontsize=fs,
                    ha=ha, va={'top': 'top', 'center': 'center', 'bottom': 'bottom'}[va],
                    color=str(r0.font.color.rgb) and '#' + str(r0.font.color.rgb),
                    fontweight='bold' if r0.font.bold else 'normal',
                    style='italic' if r0.font.italic else 'normal',
                    family='serif',
                    linespacing=(paras[0].line_spacing.pt / fs
                                 if hasattr(paras[0].line_spacing, 'pt') else 1.2))

    fig.savefig(out, dpi=150)
    print(f'{out}: rendered {n} shapes read back from {path}')


if __name__ == '__main__':
    render(sys.argv[1] if len(sys.argv) > 1 else 'figures/editable/Figure_1_2.pptx',
           sys.argv[2] if len(sys.argv) > 2 else '/tmp/pptx_preview.png')
