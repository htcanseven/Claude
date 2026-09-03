"""Apply tracked-change edits directly to the author's Chapter 1 .docx.

Works on the unpacked, run-merged copy in work/unpacked/.  Every edit is a
genuine Word revision (w:ins / w:del, tracked paragraph marks, tracked table
rows) authored under AUTHOR, so the author can step through, accept or reject
each one in Word's Review pane.  Nothing outside the listed edits is touched:
the author's images, equations, styles, footers and rsids stay exactly as
they were.

Run from work/:  python3 ../src/build_tracked.py
"""
import copy, re, sys, os, shutil
from lxml import etree
from PIL import Image

AUTHOR = 'Claude'
DATE = '2026-09-02T12:00:00Z'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
M = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS = {'w': W, 'm': M, 'r': R}
FIGDIR = '../figures/'
IMG_WIDTH_EMU = 5731510            # the width the author used for all four figures

_id = [10000]
def nid():
    _id[0] += 1
    return str(_id[0])

def q(tag):
    p, t = tag.split(':')
    return '{%s}%s' % (NS[p], t)

# ───────────────────────────────────────────── symbol/equation text extraction
_LOW = 'αβχδεφγηιϕκλμνοπθρστυϖωξψζ'; _UPP = 'ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖ'
SYM = {0xF061 + i: c for i, c in enumerate(_LOW)}
SYM.update({0xF041 + i: c for i, c in enumerate(_UPP)})
SYM.update({0xF0B4: '×', 0xF0B1: '±', 0xF0A3: '≤', 0xF0B3: '≥', 0xF0B9: '≠', 0xF0BB: '≈',
            0xF0D7: '·', 0xF0B7: '·', 0xF0AE: '→', 0xF0B5: '∝', 0xF0D6: '√'})

def ptext(p):
    out = []
    for n in p.iter():
        if n.tag == q('w:t'):
            out.append(n.text or '')
        elif n.tag == q('w:sym'):
            try: out.append(SYM.get(int(n.get(q('w:char')), 16), ''))
            except (TypeError, ValueError): pass
        elif n.tag == q('w:tab'):
            out.append(' ')
        elif n.tag == q('m:oMath'):
            out.append(''.join(t.text or '' for t in n.iter(q('m:t'))))
        elif n.tag == q('w:drawing'):
            out.append('[FIGURE]')
    return re.sub(r'\s+', ' ', ''.join(out)).strip()

# ───────────────────────────────────────────────────────────── XML builders
def rpr(b=False, i=False, sub=False, sup=False, noproof=False):
    e = etree.Element(q('w:rPr'))
    f = etree.SubElement(e, q('w:rFonts'))
    for a in ('ascii', 'hAnsi', 'cs'):
        f.set(q('w:' + a), 'Times New Roman')
    if b:
        etree.SubElement(e, q('w:b')); etree.SubElement(e, q('w:bCs'))
    if i:
        etree.SubElement(e, q('w:i')); etree.SubElement(e, q('w:iCs'))
    if noproof:
        etree.SubElement(e, q('w:noProof'))
    if sub or sup:
        etree.SubElement(e, q('w:vertAlign')).set(q('w:val'), 'subscript' if sub else 'superscript')
    etree.SubElement(e, q('w:lang')).set(q('w:val'), 'en-GB')
    return e

def track(tag):
    e = etree.Element(q(tag))
    e.set(q('w:id'), nid()); e.set(q('w:author'), AUTHOR); e.set(q('w:date'), DATE)
    return e

def run(text, **fmt):
    r = etree.Element(q('w:r'))
    r.append(rpr(**fmt))
    t = etree.SubElement(r, q('w:t')); t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return r

def ins_runs(markup, base=None):
    """Parse a light markup into inserted runs.
    _italic_  *bold*  ~subscript~  ^superscript^  (toggles; may nest)."""
    base = dict(base or {})
    state = dict(b=base.get('b', False), i=base.get('i', False), sub=False, sup=False)
    out, buf = [], ''
    def flush():
        nonlocal buf
        if buf:
            w = track('w:ins'); w.append(run(buf, **state)); out.append(w); buf = ''
    for ch in markup:
        if ch == '_':   flush(); state['i'] = not state['i']
        elif ch == '*': flush(); state['b'] = not state['b']
        elif ch == '~': flush(); state['sub'] = not state['sub']
        elif ch == '^': flush(); state['sup'] = not state['sup']
        else: buf += ch
    flush()
    return out

def para(markup='', style=None, bold=False, indent=None, jc=None, spacing_after=None):
    """A new paragraph whose mark is tracked as inserted."""
    p = etree.Element(q('w:p'))
    ppr = etree.SubElement(p, q('w:pPr'))
    if style:
        etree.SubElement(ppr, q('w:pStyle')).set(q('w:val'), style)
    if spacing_after is not None:
        etree.SubElement(ppr, q('w:spacing')).set(q('w:after'), str(spacing_after))
    if indent:
        etree.SubElement(ppr, q('w:ind')).set(q('w:firstLine'), str(indent))
    if jc:
        etree.SubElement(ppr, q('w:jc')).set(q('w:val'), jc)
    mark = rpr(b=bold)
    mark.insert(0, track('w:ins'))            # tracked paragraph mark, first in rPr
    ppr.append(mark)
    for r in ins_runs(markup, base=dict(b=bold)):
        p.append(r)
    return p

def equation(markup):
    return para(markup, indent=1304)          # same first-line indent the author uses

# ───────────────────────────────────────────────────────── figure insertion
_rid = [100]
_docpr = [900000000]
def figure(png, rels, media_dir):
    """A new paragraph containing a tracked-inserted picture, sized to the
    author's figure width.  Registers the image relationship and copies the file."""
    _rid[0] += 1; _docpr[0] += 1
    rid = 'rId%d' % _rid[0]
    n = len([f for f in os.listdir(media_dir) if f.startswith('image')]) + 1
    target = 'media/image%d.png' % n
    shutil.copy(FIGDIR + png, os.path.join(media_dir, 'image%d.png' % n))
    rel = etree.SubElement(rels, '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship')
    rel.set('Id', rid); rel.set('Target', target)
    rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
    w, h = Image.open(FIGDIR + png).size
    cx, cy = IMG_WIDTH_EMU, int(IMG_WIDTH_EMU * h / w)
    pid = str(_docpr[0])
    drawing = etree.fromstring(f'''
<w:drawing xmlns:w="{W}" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
  xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
  xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" xmlns:r="{R}">
 <wp:inline distT="0" distB="0" distL="0" distR="0">
  <wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>
  <wp:docPr id="{pid}" name="Picture {pid}"/>
  <wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>
  <a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
   <pic:pic><pic:nvPicPr><pic:cNvPr id="{pid}" name="{png}"/><pic:cNvPicPr/></pic:nvPicPr>
    <pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
    <pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
     <a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
   </pic:pic></a:graphicData></a:graphic>
 </wp:inline></w:drawing>''')
    p = para()
    w_ins = track('w:ins')
    r = etree.SubElement(w_ins, q('w:r')); r.append(rpr(noproof=True)); r.append(drawing)
    p.append(w_ins)
    return p

# ───────────────────────────────────────────────────────── table insertion
def table(rows, widths=(3005, 2519, 3492)):
    """A tracked-inserted table in the author's table style (TabloKlavuzu = Table Grid).
    Every row, cell paragraph mark and run is marked inserted."""
    t = etree.Element(q('w:tbl'))
    tp = etree.SubElement(t, q('w:tblPr'))
    etree.SubElement(tp, q('w:tblStyle')).set(q('w:val'), 'TabloKlavuzu')
    tw = etree.SubElement(tp, q('w:tblW')); tw.set(q('w:w'), '0'); tw.set(q('w:type'), 'auto')
    lk = etree.SubElement(tp, q('w:tblLook'))
    for k, v in [('val', '04A0'), ('firstRow', '1'), ('lastRow', '0'), ('firstColumn', '1'),
                 ('lastColumn', '0'), ('noHBand', '0'), ('noVBand', '1')]:
        lk.set(q('w:' + k), v)
    g = etree.SubElement(t, q('w:tblGrid'))
    for wd in widths:
        etree.SubElement(g, q('w:gridCol')).set(q('w:w'), str(wd))
    for ri, cells in enumerate(rows):
        tr = etree.SubElement(t, q('w:tr'))
        trpr = etree.SubElement(tr, q('w:trPr')); trpr.append(track('w:ins'))
        for ci, txt in enumerate(cells):
            tc = etree.SubElement(tr, q('w:tc'))
            tcpr = etree.SubElement(tc, q('w:tcPr'))
            cw = etree.SubElement(tcpr, q('w:tcW')); cw.set(q('w:w'), str(widths[ci])); cw.set(q('w:type'), 'dxa')
            tc.append(para(txt, bold=(ri == 0 or ci == 0)))
    return t

# ───────────────────────────────────────────── in-place tracked text editing
def text_runs(p):
    """Direct-child runs that are plain single-w:t runs, with their text; other
    children yield (elem, None) so a span crossing them is refused."""
    items = []
    for c in p:
        if c.tag == q('w:r'):
            kids = [k for k in c if k.tag != q('w:rPr')]
            if len(kids) == 1 and kids[0].tag == q('w:t'):
                items.append((c, kids[0].text or ''))
                continue
        if c.tag != q('w:pPr'):
            items.append((c, None))
    return items

def split_run(r, k):
    """Split run r at character k; returns (left, right), both in the tree."""
    t = r.find(q('w:t')); s = t.text or ''
    left = copy.deepcopy(r); left.find(q('w:t')).text = s[:k]
    right = copy.deepcopy(r); right.find(q('w:t')).text = s[k:]
    for e in (left.find(q('w:t')), right.find(q('w:t'))):
        e.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    r.addprevious(left); r.addnext(right); r.getparent().remove(r)
    return left, right

def _charmap(p):
    """Concatenated text of the paragraph's direct children, with each plain
    text run mapped to its character range; any other child (symbol, equation,
    picture, mixed run) occupies one '\\x00' so a span may not cross it."""
    buf, spans = '', []
    for c in p:
        if c.tag in ZERO_WIDTH:
            continue
        if c.tag == q('w:r'):
            kids = [k for k in c if k.tag not in (q('w:rPr'), q('w:lastRenderedPageBreak'))]
            if len(kids) == 1 and kids[0].tag == q('w:t'):
                s = kids[0].text or ''
                spans.append((c, len(buf), len(buf) + len(s))); buf += s
                continue
        spans.append((c, len(buf), len(buf) + 1)); buf += '\x00'
    return buf, spans

# paragraph children that carry no content: spell-check markers and bookmarks
ZERO_WIDTH = {q('w:pPr'), q('w:proofErr'), q('w:bookmarkStart'), q('w:bookmarkEnd')}

def _scrub(p):
    """Prepare a paragraph for span editing without changing its content:
    drop transient markup Word regenerates anyway (spell-check flags, last
    rendered page breaks), and split any run holding several content children
    (text on both sides of a symbol, say) into one run per child, each with a
    copy of the original run properties."""
    for e in list(p.iter(q('w:proofErr'))) + list(p.iter(q('w:lastRenderedPageBreak'))):
        e.getparent().remove(e)
    for r in list(p):
        if r.tag != q('w:r'):
            continue
        rp = r.find(q('w:rPr'))
        kids = [k for k in r if k.tag != q('w:rPr')]
        if len(kids) <= 1:
            continue
        for k in kids:
            nr = etree.Element(q('w:r'))
            if rp is not None:
                nr.append(copy.deepcopy(rp))
            nr.append(k)
            r.addprevious(nr)
        r.getparent().remove(r)

def _locate(p, idx):
    for c, s, e in _charmap(p)[1]:
        if s <= idx < e:
            return c, idx - s
    raise IndexError(idx)

def delete_span(p, old, replacement=None):
    """Tracked deletion of `old` inside paragraph p (must lie within plain text
    runs); optionally followed by a tracked insertion of `replacement` carrying
    the same formatting as the deleted text."""
    _scrub(p)
    buf, _ = _charmap(p)
    k = buf.find(old)
    if k < 0 or '\x00' in buf[k:k + len(old)]:
        sys.exit(f'delete_span: span not found in plain runs: {old[:60]!r}\n  para: {ptext(p)[:120]!r}')
    end = k + len(old)
    # cut the boundary runs so that the span is a whole number of runs
    c, off = _locate(p, k)
    if off > 0:
        split_run(c, off)
    c, off = _locate(p, end - 1)
    if off + 1 < len(c.find(q('w:t')).text or ''):
        split_run(c, off + 1)
    start_run, _ = _locate(p, k)
    end_run, _ = _locate(p, end - 1)
    span, on = [], False
    for c in list(p):
        if c is start_run: on = True
        if on: span.append(c)
        if c is end_run: break
    fmt_src = copy.deepcopy(span[0].find(q('w:rPr')))
    d = track('w:del'); span[0].addprevious(d)
    for r in span:
        t = r.find(q('w:t')); t.tag = q('w:delText')
        d.append(r)
    if replacement is not None:
        w_ins = track('w:ins'); rr = etree.SubElement(w_ins, q('w:r'))
        if fmt_src is not None: rr.append(fmt_src)
        tt = etree.SubElement(rr, q('w:t')); tt.text = replacement
        tt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        d.addnext(w_ins)

def delete_para(p):
    """Tracked deletion of a whole paragraph (mark and every run)."""
    ppr = p.find(q('w:pPr'))
    if ppr is None:
        ppr = etree.Element(q('w:pPr')); p.insert(0, ppr)
    prpr = ppr.find(q('w:rPr'))
    if prpr is None:
        prpr = etree.SubElement(ppr, q('w:rPr'))
    prpr.insert(0, track('w:del'))
    for c in list(p):
        if c.tag == q('w:pPr'): continue
        d = track('w:del'); c.addprevious(d); d.append(c)
        for t in c.iter(q('w:t')): t.tag = q('w:delText')

# ────────────────────────────────────────────────────────────── the edits
def main():
    doc_path = 'unpacked/word/document.xml'
    tree = etree.parse(doc_path); root = tree.getroot()
    body = root.find(q('w:body'))
    rels = etree.parse('unpacked/word/_rels/document.xml.rels').getroot()
    media = 'unpacked/word/media'
    paras = [p for p in body.iter(q('w:p'))]
    top = [c for c in body if c.tag in (q('w:p'), q('w:tbl'))]

    def P(prefix):
        for p in paras:
            if ptext(p).startswith(prefix): return p
        sys.exit(f'anchor not found: {prefix!r}')

    def after(anchor, *elems):
        cur = anchor
        for e in elems:
            cur.addnext(e); cur = e
        return cur

    log = []

    # 1 ── planning outline at the head of the draft: tracked deletion of the 40 lines
    body_start = P('1.1 Introduction: The High-Speed Landscape')
    n = 0
    for c in top:
        if c is body_start: break
        if c.tag == q('w:p') and ptext(c):
            delete_para(c); n += 1
    log.append(f'deleted the {n}-line planning outline at the head of the chapter (tracked; reject to keep)')

    # 2 ── small copy-edits
    edits = [
        ('The speed of a high-speed machine is not merely a mechanical', 'mechanical rpm value', 'mechanical r/min value'),
        ('The Switching Frequency Wall', '10, rather to 20 times', '10 to 20 times'),
        ('In EU financed Voltcar project', 'In EU financed Voltcar project', 'In the EU-financed Voltcar project'),
        ('Large Air Gaps', '2–5… mm', '2–5 mm'),
        ('The distribution of mechanical stress is heavily dependent', 'stress in in inner radius', 'stress at the inner radius'),
        ('Conversely, solid rotors', 'a high airgap', 'a large air gap'),
        ('The fundamental power equation', 'the airgap magnetic-flux density', 'the air-gap magnetic-flux density'),
        ('In conventional 50/60 Hz industrial drives', 'rises the switching frequency', 'raises the switching frequency'),
        ('In conventional 50/60 Hz industrial drives', 'If only possible', 'Wherever possible,'),
        ('In conventional 50/60 Hz industrial drives', 'should be followed to get', 'should be maintained to get'),
    ]
    for anchor, old, new in edits:
        delete_span(P(anchor), old, new); log.append(f'copy-edit: "{old}" → "{new}"')

    # 3 ── the fP passage: drafting artefacts
    delete_para(P('The fP product is discussed in the context of classifying'))
    log.append('deleted the sentence apologising for its own missing citation ("without external resources provided")')
    p58 = P('In summary, the definitions for high-speed machines remain varied')
    tail = ptext(p58)[ptext(p58).index(' Literature is still evolving'):]
    delete_span(p58, tail)
    log.append('trimmed "...Literature is still evolving ... in the current context" from the closing sentence')

    # 4 ── qualify the fP threshold; add Figure 1.1
    anc = P('If we consider that the two first definitions fulfil the definition')
    after(anc,
        para('Two qualifications should be attached to this figure. The value is proposed here from a single design point, and the Voltcar machine is itself marginal by the tip-speed criterion, at 150.8 m/s against a 150 m/s threshold, so it is a weak anchor for a classification boundary. At this stage the _fP_ product is therefore best read as a descriptive figure of merit for converter burden rather than as a validated threshold; its calibration against a population of published machines is carried out later in this book.'),
        para('What the _fP_ product does capture, and what neither _v_~tip~ nor _n_√_P_ can, is the pole number. The same 120 kW rotor wound as a two-pole machine would have an identical tip speed and an identical _n_√_P_, while its fundamental frequency, and with it the _fP_ product, would fall by a factor of three. Figure 1.1 shows how the two criteria sit relative to one another in the power–speed plane.'),
        figure('fig_classification_map.png', rels, media),
        para('Figure 1.1. The _n_√_P_ and _fP_ criteria in the power–speed plane. The _fP_ contour is drawn for _p_ = 3; changing the pole-pair number translates it vertically, which is the dependence that _n_√_P_ cannot express. The marked point is the machine of Table 1.1.'))
    log.append('added two paragraphs qualifying the 180 000 kW/s threshold, and Figure 1.1 (classification map)')

    # 5 ── captions for the author's four existing figures
    caps = [
        ('Figure 2. Caption', 'Figure 1.2. Traditional geared and integrated direct-drive architectures. Left: a mains-frequency motor drives the impeller through a step-up gearbox and its lubrication system. Right: the impeller is mounted directly on the high-speed motor shaft, optionally carried on active magnetic bearings, and the gearbox, couplings and oil system disappear.'),
        ('Fig. 3 Caption', 'Figure 1.4. Computed lateral bending mode shapes of a high-speed rotor between its non-drive end (NDE) and drive end (DE), with the first four natural frequencies. A rotor operated above its first bending mode must pass through resonance on every run-up and coast-down. [machine and source to be stated]'),
        ('Fig 4 Caption', 'Figure 1.5. Loss components against rotational speed at fixed machine geometry: copper loss approximately constant, iron loss rising roughly with the square of speed and windage with its cube. The onset of efficiency decay marks where loss growth overtakes the linear growth of output power. Section 1.5.5 shows how this picture changes when the machine is redesigned for the higher speed rather than overspeed.'),
        ('Fig. 5 Caption', 'Figure 1.9. The high-speed trilemma and its gatekeeper. Each remedy at one vertex creates the problem at the next: mechanical reinforcement widens the effective air gap, the pole count and frequency chosen for power density raise the iron and windage losses, and the cooling geometry needed to remove them erodes stiffness and lengthens the rotor. The design space therefore closes on itself, and feasible machines occupy the window at its centre. The power electronic interface decides which part of that window can be reached: silicon IGBT converters admit the low-pole industrial topology, while the high-pole mobile topology is feasible only with SiC or GaN switching.'),
    ]
    for old, new in caps:
        p = P(old) if not old.startswith('Fig. 3') else None
        if p is None:                          # "Fig. 3 Caption" shares its paragraph with the picture
            for c in paras:
                if ptext(c).endswith('Fig. 3 Caption'): p = c; break
        delete_span(p, old, new)
    log.append('wrote captions for the four existing figures and numbered all figures sequentially (1.1–1.9)')

    # 6 ── quantify the centrifugal stress; add Figure 1.3
    anc = P('Conversely, solid rotors, often found in high-performance induction')
    after(anc,
        para('The factor of two is exact for a thin disc. For a solid rotating disc of density _ρ_ and Poisson ratio _ν_ the maximum tangential stress occurs at the centre and is'),
        equation('_σ_~max~ = [(3 + _ν_)/8] _ρ_ _v_~tip~^2^'),
        para('while introducing a small central bore moves the maximum to the bore and doubles it:'),
        equation('_σ_~max~ = [(3 + _ν_)/4] _ρ_ _v_~tip~^2^'),
        para('Figure 1.3 evaluates both for electrical steel, taking _ρ_ = 7650 kg/m^3^ and _ν_ = 0.3. A bored lamination reaches about 252 MPa at 200 m/s and about 395 MPa at 250 m/s. Against a high-strength grade with a proof stress near 450 MPa and a safety factor of 1.5, the 250 m/s design is already outside the allowable envelope while the 200 m/s design is inside it. This is the quantitative form of the advantage that solid rotors hold over laminated ones.'),
        figure('fig_stress_vs_tipspeed.png', rels, media),
        para('Figure 1.3. Maximum tangential stress against peripheral speed for a solid disc, a disc with a central bore and a thin ring, for electrical steel (_ρ_ = 7650 kg/m^3^, _ν_ = 0.3). The central bore doubles the stress, which is the penalty paid by any shaft-mounted lamination stack.'))
    log.append('added the algebraic form of the centrifugal stress with worked MPa values, and Figure 1.3')

    # 7 ── the converter requirement as a number; add Figure 1.6
    anc = P('This conflict is the primary reason why high-speed design requires a holistic')
    after(anc,
        para('It is worth putting a number on this conflict for the machine of Table 1.1. At a fundamental frequency of 1500 Hz, maintaining _m_~f~ = 21 requires a switching frequency of 31.5 kHz. A silicon IGBT stage of this rating operates practically at 8 to 16 kHz; at 16 kHz the modulation ratio would be 10.7, which is at the control-stability floor identified above and far below the synchronous-PWM threshold. This machine therefore cannot be supplied acceptably from a silicon converter, and the shortfall cannot be recovered at the machine end without changing the pole number. Figure 1.6 shows where the boundary falls.'),
        figure('fig_converter_gate.png', rels, media),
        para('Figure 1.6. Required switching frequency against fundamental frequency for two modulation ratios, with the practical ranges of silicon IGBT and wide-bandgap devices indicated. The machine of Table 1.1 falls outside the silicon region.'))
    log.append('added the worked converter requirement (31.5 kHz at m_f = 21) and Figure 1.6')

    # 8 ── square–cube qualification
    anc = P('As we scale a machine down to reach higher speeds, the ratio of Loss/Surface Area')
    after(anc,
        para('One qualification is worth adding here. The square–cube argument assumes that the machine is scaled isotropically, with every dimension changing in proportion. High-speed machines are not scaled that way. The tip-speed limit caps the diameter, so the rotor shrinks radially while growing axially in order to recover the rating, and along that path the rotor lateral surface area, which is proportional to _D_~r~_l_, is very nearly preserved. What does degrade is the loss density inside the stator, and the length of the conduction path out of the rotor, which is thermally isolated by an air gap whose conductance is poor and largely independent of the cooling effort spent on the stator.'))
    log.append('added a qualification to the square–cube argument')

    # 9 ── new §1.5.5 and Table 1.4; new §1.5.6
    anc = P('By understanding these scaling laws, the designer can identify the sweet spot')
    rows = [['Quantity', 'Scaling on the tip-speed-limited path', 'Factor on doubling Ω'],
            ['Rotor diameter _D_~r~', '∝ Ω^−1^', '0.50'],
            ['Active length _l_', '∝ Ω', '2.00'],
            ['_l_/_D_~r~ ratio', '∝ Ω^2^', '4.00'],
            ['Active volume', '∝ Ω^−1^', '0.50'],
            ['Centrifugal stress _σ_~mec~', 'constant', '1.00'],
            ['Iron loss _P_~Fe~', '∝ Ω', '2.00'],
            ['Windage loss _P_~wnd~', 'constant', '1.00'],
            ['Rotor surface area', 'constant', '1.00'],
            ['First critical speed _n_~cr~', '∝ Ω^−3^', '0.125']]
    after(anc,
        para('1.5.5 Reading the scaling table: which path is being followed', style='Balk3'),
        para('Table 1.3 is best read one row at a time, because the rows are not all evaluated under the same condition. The power and stress rows state their condition explicitly, namely constant power as the diameter is reduced and constant stress as the tip speed is held fixed. The iron-loss and windage rows, by contrast, are evaluated at fixed rotor geometry, which is the overspeed case rather than the design case. The distinction matters, because a designer moving to a higher speed does not hold the geometry fixed: the tip-speed limit forces the diameter down, and the rating is then recovered by increasing the active length.'),
        para('It is therefore useful to tabulate the same speed doubling along the path that a design actually follows, with rated power and peripheral speed both held constant, so that the rotor radius scales as Ω^−1^ and the active length as Ω. Table 1.4 gives the result, and Figure 1.7 compares it with the fixed-geometry case of Table 1.3.'),
        para('Table 1.4 The same doubling of speed evaluated along the tip-speed-limited design path, at constant rated power'),
        table(rows),
        para('', spacing_after=0),
        para('Two entries deserve comment. Windage is unchanged rather than increased eightfold, because windage power is the product of a shear stress set by the tip speed, which is fixed by definition along this path, and a rotor surface area proportional to _D_~r~_l_, which is preserved because the diameter reduction and the length increase cancel. Iron loss doubles rather than quadruples, because the loss per unit mass rises as _f_^2^ while the iron mass falls with the halving active volume. The fourfold and eightfold figures of Table 1.3 are correct for overspeeding an existing machine; it is only their application to a redesign that would mislead. Figure 1.7 also shows an intermediate case in which the active length is allowed to grow only 1.5-fold, as rotordynamics will usually demand; every quantity then lands between the two extremes.'),
        figure('fig_scaling_paths.png', rels, media),
        para('Figure 1.7. The same doubling of speed evaluated along three design paths: fixed geometry, tip-speed limited at constant power, and tip-speed limited with the active length capped by rotordynamics.'),
        para('1.5.6 Rotordynamic scaling: where the returns actually stop', style='Balk3'),
        para('The last row of Table 1.4 deserves a section of its own, because it identifies the constraint that in practice terminates the pursuit of higher speed.'),
        para('Section 1.3.2 established that high-speed rotors become long and thin. Treating the rotor as a uniform beam, the first bending critical speed scales as'),
        equation('_n_~cr~ ∝ _r_~r~ / _l_^2^'),
        para('Substituting the tip-speed-limited path used for Table 1.4, with _r_~r~ ∝ Ω^−1^ and _l_ ∝ Ω,'),
        equation('_n_~cr~ ∝ Ω^−1^ / Ω^2^ = Ω^−3^'),
        para('so that the first critical speed falls as the cube of the design speed while the operating speed rises linearly with it. The ratio of the two therefore scales as'),
        equation('_n_~op~ / _n_~cr~ ∝ Ω^4^'),
        para('A doubling of the design speed degrades the rotordynamic margin by a factor of sixteen, as Figure 1.8 shows. This is why so many high-speed machines must be operated supercritically. It is not a design preference: along the only path that respects the material limit, the critical speed collapses far faster than the operating speed rises.'),
        para('These exponents are idealised. A real rotor is not a uniform beam, the bearing span exceeds the active length, shaft extensions and couplings add mass outboard of the bearings, and a shrink-fitted sleeve or a solid rotor body stiffens the assembly, as the mode shapes of Figure 1.4 illustrate. They should be read as indicating the severity of the trend rather than as design values. The trend is nevertheless what governs practice, and it is the reason that the rotor’s mechanical and rotordynamic design cannot be left until the electromagnetic design is complete.'),
        figure('fig_critical_speed_divergence.png', rels, media),
        para('Figure 1.8. Divergence of the operating speed and the first bending critical speed along the tip-speed-limited design path. The rotordynamic margin degrades as the fourth power of the speed multiplier.'))
    log.append('added §1.5.5 with Table 1.4 and Figure 1.7, and §1.5.6 with the rotordynamic scaling result and Figure 1.8')

    # 9a ── §1.6.2 roadmap: the draft describes 19 chapters in six parts; the
    #       proposal now offers 12 chapters in four parts.  Tracked replacement of
    #       the roadmap body; the author's closing sentence is kept.
    first = P('This book is structured as a comprehensive journey')
    last = P('This roadmap ensures that whether the reader')
    doomed, on = [], False
    for p in paras:
        if p is first: on = True
        if p is last: break
        if on: doomed.append(p)
    for p in doomed:
        delete_para(p)
    after(doomed[-1],
        para('This book is structured as a journey through the multidisciplinary landscape of high-speed engineering, and its order follows the design sequence described in this chapter rather than the conventional one: the constraints that bind first are treated before the electromagnetic design that must fit within them. Two machines are carried through every design chapter and assembled into complete, measured designs at the end, a two-pole gearless industrial compressor drive and the six-pole traction machine of Table 1.1, so that each of the two paradigms has a worked example running through the whole book. Following this introduction, the text is organised into four parts.'),
        para('Part I: The High-Speed Design Space', bold=True),
        para('Chapter 2 surveys the applications, from gearless industrial compression through electric traction to aerospace propulsion and electrically assisted turbocharging, and calibrates the classification criteria of Section 1.1.1 against a population of built machines. Chapter 3 compares the candidate topologies, namely solid-rotor and laminated induction machines, synchronous and permanent-magnet-assisted reluctance machines, and surface- and interior-magnet synchronous machines, together with the choice of winding at high fundamental frequency; switched reluctance is treated briefly, because its converter falls outside the drive-interface thread that runs through the book.'),
        para('Part II: The Constraints that Bind First', bold=True),
        para('Chapter 4 addresses the _r_Ω^2^ wall directly: rotor stress analysis, magnet retention by carbon-fibre and metallic sleeves against interior-magnet bridge designs, and fatigue life and overspeed margin. Chapter 5 covers rotordynamics, with Campbell diagrams, gyroscopic effects, balancing and supercritical operation, together with the vibration and acoustic behaviour that follows. Chapter 6 treats the tribology of the support system: bearing selection from high-precision rolling elements through air foil systems to active magnetic bearings, lubrication and bearing losses at high speed, seals, and the damage mechanisms of wear, fretting and bearing currents.'),
        para('Part III: Electromagnetic Design within the Constraints', bold=True),
        para('Chapter 7 develops the sizing procedure, working from the mechanical and rotordynamic limits inward to the electromagnetic design, with worked examples for both the industrial and the mobile paradigm and a section on optimisation-based multiphysics sizing. Chapter 8 addresses AC copper losses, comparing Litz wire and form-wound conductors to mitigate skin and proximity effects. Chapter 9 treats the losses and the thermal budget in the kilohertz range: core losses with the soft magnetic materials and manufacturing effects behind them, eddy currents in sleeves and magnets and magnet segmentation, aerodynamic and windage losses including Taylor–Couette flow in the air gap, and the cooling architectures that set the loss budget the design must meet.'),
        para('Part IV: Delivery, the Drive and the Applications', bold=True),
        para('Chapter 10 treats the drive as the gatekeeper it is: the converter interface, the role of SiC and GaN devices, insulation stress under fast switching, bearing currents, and control at high fundamental frequency including sensorless operation at low pulse ratios. Chapters 11 and 12 present complete design case studies, industrial and mobile respectively, each carried from specification to measured validation, with the test methods, the loss segregation at high speed, and the overspeed and endurance qualification that the applicable standards require.'))
    log.append('rewrote the §1.6.2 roadmap for the 12-chapter, four-part structure (tracked; the closing sentence is kept)')

    # 9b ── Figure 1.9: replace the author's trilemma picture with the one that
    #       follows the text of §1.6.1 (a tracked replacement: the old picture is
    #       marked deleted, the new one inserted, so Reject restores the original)
    if os.path.exists(FIGDIR + 'fig_trilemma.png'):
        old = None
        for p in paras:
            for d in p.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
                if d.get('{%s}embed' % R) == 'rId11':
                    old = p
        if old is None:
            sys.exit('Figure 1.9 picture (rId11) not found')
        for r in list(old):
            if r.tag == q('w:r') and r.find(q('w:drawing')) is not None:
                d = track('w:del'); r.addprevious(d); d.append(r)
        newfig = figure('fig_trilemma.png', rels, media)
        for w_ins in newfig.findall(q('w:ins')):
            old.append(w_ins)
        log.append('replaced the Figure 1.9 picture with one drawn to the text of §1.6.1 (tracked; reject to restore the original)')

    tree.write(doc_path, xml_declaration=True, encoding='UTF-8', standalone=True)
    etree.ElementTree(rels).write('unpacked/word/_rels/document.xml.rels', xml_declaration=True, encoding='UTF-8', standalone=True)

    # 10 ── switch Track Changes on for the author's further edits
    sp = 'unpacked/word/settings.xml'
    st = etree.parse(sp); sroot = st.getroot()
    if sroot.find(q('w:trackRevisions')) is None:
        order = ['writeProtection','view','zoom','removePersonalInformation','removeDateAndTime','doNotDisplayPageBoundaries',
                 'displayBackgroundShape','printPostScriptOverText','printFractionalCharacterWidth','printFormsData',
                 'embedTrueTypeFonts','embedSystemFonts','saveSubsetFonts','saveFormsData','mirrorMargins',
                 'alignBordersAndEdges','bordersDoNotSurroundHeader','bordersDoNotSurroundFooter','gutterAtTop',
                 'hideSpellingErrors','hideGrammaticalErrors','activeWritingStyle','proofState','formsDesign',
                 'attachedTemplate','linkStyles','stylePaneFormatFilter','stylePaneSortMethod','documentType',
                 'mailMerge','revisionView','trackRevisions']
        before = {q('w:' + n) for n in order}
        idx = 0
        for i, c in enumerate(sroot):
            if c.tag in before: idx = i + 1
        sroot.insert(idx, etree.Element(q('w:trackRevisions')))
        st.write(sp, xml_declaration=True, encoding='UTF-8', standalone=True)
    log.append('switched Track Changes on in the document settings')

    print('\n'.join(f'  - {l}' for l in log))
    print(f'\n  tracked revisions written: {_id[0] - 10000}')

if __name__ == '__main__':
    main()
