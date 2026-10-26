"""Apply the house style to Chapter 1 (House_Style.md).

Reads the authors' final chapter and writes Chapter_1_house_style.docx, changing
presentation only:

* every figure is replaced by its house-style drawing from src/ch1_figures.py,
  placed at exactly the text width so that its 11 pt text prints at 11 pt;
* every caption gets one paragraph style, Caption: Times New Roman 11 pt,
  justified like the body, with the label "Figure 1.x." or "Table 1.x." in bold;
  figure captions below the figure, table captions above the table;
* every table gets one style: full text width, horizontal rules only (1 pt above
  and below the table, 0.5 pt under the header), Times New Roman 11 pt throughout,
  text columns left and numeric columns centred, header in bold and repeated on a
  new page, sentence case;
* the alternative text of each figure is set to its caption.

Text is touched in a few places only, each listed in the change log printed at
the end: missing full stops after three table numbers, sentence case in two
tables, "4x" written as "4×", and the captions of Figures 1.2, 1.4 and 1.5,
which are brought into line with the redrawn figures. After those, the wording
agreed with the authors (fix_text): headings in sentence case as in the table of
contents, a heading for §1.2, "rpm" made r/min, the in-text citations in one
form, and the reference list that the open comments asked for, after which the
comments are marked resolved.

usage:  python3 src/apply_house_style.py      (run from chapter1/)
"""
import copy
import io
import re
import sys
import zipfile

from lxml import etree as ET
from PIL import Image

SRC = 'incoming/Chapter_1_final.docx'
DST = 'Chapter_1_house_style.docx'
NEW_FIG = {n: f'{n:02d}' for n in range(1, 10)}
TEXT_EMU = 5731510               # 9026 twips: the text-block width of the manuscript
TEXT_TWIPS = 9026

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
PIC = 'http://schemas.openxmlformats.org/drawingml/2006/picture'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
XML = 'http://www.w3.org/XML/1998/namespace'


def q(tag, ns=W):
    return f'{{{ns}}}{tag}'


LOG = []

# ───────────────────────────────────────────── schema order of child elements
ORDER = {
    'pPr': ['pStyle', 'keepNext', 'keepLines', 'pageBreakBefore', 'framePr', 'widowControl',
            'numPr', 'suppressLineNumbers', 'pBdr', 'shd', 'tabs', 'suppressAutoHyphens',
            'kinsoku', 'wordWrap', 'overflowPunct', 'topLinePunct', 'autoSpaceDE', 'autoSpaceDN',
            'bidi', 'adjustRightInd', 'snapToGrid', 'spacing', 'ind', 'contextualSpacing',
            'mirrorIndents', 'suppressOverlap', 'jc', 'textDirection', 'textAlignment',
            'textboxTightWrap', 'outlineLvl', 'divId', 'cnfStyle', 'rPr', 'sectPr', 'pPrChange'],
    'rPr': ['rStyle', 'rFonts', 'b', 'bCs', 'i', 'iCs', 'caps', 'smallCaps', 'strike', 'dstrike',
            'outline', 'shadow', 'emboss', 'imprint', 'noProof', 'snapToGrid', 'vanish',
            'webHidden', 'color', 'spacing', 'w', 'kern', 'position', 'sz', 'szCs', 'highlight',
            'u', 'effect', 'bdr', 'shd', 'fitText', 'vertAlign', 'rtl', 'cs', 'em', 'lang',
            'eastAsianLayout', 'specVanish', 'oMath'],
    'tcPr': ['cnfStyle', 'tcW', 'gridSpan', 'hMerge', 'vMerge', 'tcBorders', 'shd', 'noWrap',
             'tcMar', 'textDirection', 'tcFitText', 'vAlign', 'hideMark', 'headers', 'cellIns',
             'cellDel', 'cellMerge', 'tcPrChange'],
    'trPr': ['cnfStyle', 'divId', 'gridBefore', 'gridAfter', 'wBefore', 'wAfter', 'cantSplit',
             'trHeight', 'tblHeader', 'tblCellSpacing', 'jc', 'hidden', 'ins', 'del',
             'trPrChange'],
}


def child(parent, tag, attrs=None, replace=True):
    """Get or create parent/tag at its schema position; set attributes."""
    order = ORDER[ET.QName(parent).localname]
    old = parent.find(q(tag))
    if old is not None and replace:
        parent.remove(old)
        old = None
    if old is None:
        el = ET.Element(q(tag))
        pos = order.index(tag)
        idx = len(parent)
        for i, c in enumerate(parent):
            name = ET.QName(c).localname
            if name in order and order.index(name) > pos:
                idx = i
                break
        parent.insert(idx, el)
    else:
        el = old
    for k, v in (attrs or {}).items():
        el.set(q(k), v)
    return el


def ppr(p):
    pp = p.find(q('pPr'))
    if pp is None:
        pp = ET.Element(q('pPr'))
        p.insert(0, pp)
    return pp


def rpr(r):
    rp = r.find(q('rPr'))
    if rp is None:
        rp = ET.Element(q('rPr'))
        r.insert(0, rp)
    return rp


def text(el):
    return ''.join(t.text or '' for t in el.iter(q('t')))


def runs(p):
    return [r for r in p.iter(q('r')) if r.find(q('t')) is not None]


def times(rp):
    child(rp, 'rFonts', {'ascii': 'Times New Roman', 'hAnsi': 'Times New Roman',
                         'cs': 'Times New Roman'})


# ───────────────────────────────────────────── styles.xml
CAPTION_STYLE = f'''<w:style xmlns:w="{W}" w:type="paragraph" w:styleId="Caption">
  <w:name w:val="caption"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
  <w:uiPriority w:val="35"/><w:unhideWhenUsed/><w:qFormat/>
  <w:pPr><w:spacing w:before="120" w:after="240" w:line="259" w:lineRule="auto"/>
    <w:jc w:val="both"/></w:pPr>
  <w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
    <w:i w:val="0"/><w:iCs w:val="0"/><w:color w:val="000000"/>
    <w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>
</w:style>'''

TABLE_STYLE = f'''<w:style xmlns:w="{W}" w:type="table" w:customStyle="1" w:styleId="HSBookTable">
  <w:name w:val="HS Book Table"/><w:basedOn w:val="TableNormal"/><w:uiPriority w:val="40"/>
  <w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>
  <w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
    <w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>
  <w:tblPr>
    <w:tblBorders>
      <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>
      <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>
    </w:tblBorders>
    <w:tblCellMar><w:top w:w="45" w:type="dxa"/><w:left w:w="85" w:type="dxa"/>
      <w:bottom w:w="45" w:type="dxa"/><w:right w:w="85" w:type="dxa"/></w:tblCellMar>
  </w:tblPr>
  <w:tblStylePr w:type="firstRow">
    <w:rPr><w:b/><w:bCs/></w:rPr>
    <w:tcPr><w:tcBorders><w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    </w:tcBorders></w:tcPr>
  </w:tblStylePr>
</w:style>'''


def add_styles(styles):
    for sid, xml in (('Caption', CAPTION_STYLE), ('HSBookTable', TABLE_STYLE)):
        for s in styles.findall(q('style')):
            if s.get(q('styleId')) == sid:
                styles.remove(s)
        styles.append(ET.fromstring(xml))


# ───────────────────────────────────────────── captions
def split_run(r, at):
    """Split run r at character offset `at`; returns (left, right)."""
    t = r.find(q('t'))
    s = t.text or ''
    right = copy.deepcopy(r)
    t.text = s[:at]
    right.find(q('t')).text = s[at:]
    for x in (t, right.find(q('t'))):
        x.set(f'{{{XML}}}space', 'preserve')
    r.addnext(right)
    return r, right


def bold_label(p, label):
    """Make the caption label bold, splitting the run where the label ends."""
    n, done = len(label), 0
    for r in runs(p):
        s = text(r)
        if done >= n:
            break
        if done + len(s) > n:
            r, _ = split_run(r, n - done)
            s = text(r)
        child(rpr(r), 'b'); child(rpr(r), 'bCs')
        done += len(s)


def insert_text(p, at, s):
    """Insert string s at character offset `at` of the paragraph text."""
    done = 0
    for r in runs(p):
        t = r.find(q('t'))
        L = len(t.text or '')
        if done + L >= at:
            k = at - done
            t.text = (t.text or '')[:k] + s + (t.text or '')[k:]
            t.set(f'{{{XML}}}space', 'preserve')
            return
        done += L
    raise ValueError('offset beyond paragraph')


def replace_text(p, old, new):
    for t in p.iter(q('t')):
        if t.text and old in t.text:
            t.text = t.text.replace(old, new, 1)
            return True
    raise ValueError(f'{old!r} not found in a single run')


def append_sentence(p, s):
    last = runs(p)[-1]
    r = copy.deepcopy(last)
    rp = r.find(q('rPr'))
    if rp is not None:
        for tag in ('b', 'bCs', 'i', 'iCs', 'vertAlign'):
            for el in rp.findall(q(tag)):
                rp.remove(el)
    r.find(q('t')).text = s
    r.find(q('t')).set(f'{{{XML}}}space', 'preserve')
    for t in r.findall(q('t'))[1:]:
        r.remove(t)
    last.addnext(r)


def style_caption(p, kind, num):
    pp = ppr(p)
    child(pp, 'pStyle', {'val': 'Caption'})
    for el in pp.findall(q('ind')):          # captions run the full text width
        pp.remove(el)
    if kind == 'Table':
        child(pp, 'keepNext')
        child(pp, 'spacing', {'before': '240', 'after': '120', 'line': '259', 'lineRule': 'auto'})
    else:
        child(pp, 'spacing', {'before': '120', 'after': '240', 'line': '259', 'lineRule': 'auto'})
    child(pp, 'jc', {'val': 'both'})
    head = f'{kind} 1.{num}'
    s = text(p)
    assert s.startswith(head), (s[:30], head)
    if not s.startswith(head + '.'):
        insert_text(p, len(head), '.')
        LOG.append(f'{head}: full stop added after the number ("{head}." as in every other caption)')
    for r in runs(p):
        times(rpr(r))
    bold_label(p, head + '.')


# ───────────────────────────────────────────── tables
COLS = {1: 'LLL', 2: 'LLL', 3: 'LCL', 4: 'LCC'}       # alignment by logical column
HEADER = {1: False, 2: True, 3: True, 4: True}
SENTENCE_CASE = {2, 3}
KEEP_CAPS = {'Inconel', 'Converteam', 'Voltcar'}


def sentence_case(cell):
    """Lower the initial capital of every word but the first, except symbols
    (italic or sub/superscript runs), acronyms and proper names."""
    first = True
    changed = False
    for r in runs(cell):
        rp = r.find(q('rPr'))
        is_symbol = rp is not None and (rp.find(q('vertAlign')) is not None or
                                         rp.find(q('i')) is not None)
        t = r.find(q('t'))
        s = t.text or ''

        def fix(m):
            nonlocal first, changed
            w = m.group(0)
            if first:
                first = False
                return w
            if is_symbol or w in KEEP_CAPS or not re.fullmatch(r'[A-Z][a-z]+', w):
                return w
            changed = True
            return w[0].lower() + w[1:]
        t.text = re.sub(r'[A-Za-z]+', fix, s)
    return changed


def style_table(tbl, num):
    house_table(tbl, COLS[num], HEADER[num], num in SENTENCE_CASE, num == 3, f'Table 1.{num}')


def house_table(tbl, aligns, head=True, sentence=False, factor_x=False, label='table'):
    """Put one table into the house style. `aligns` gives L or C per logical column."""
    # table properties, rebuilt in schema order
    tp = tbl.find(q('tblPr'))
    keep = [c for c in tp if ET.QName(c).localname in ('tblCaption', 'tblDescription')]
    for c in list(tp):
        tp.remove(c)
    E = lambda tag, **a: ET.SubElement(tp, q(tag), {q(k): v for k, v in a.items()})
    E('tblStyle', val='HSBookTable')
    E('tblW', w='5000', type='pct')
    E('jc', val='center')
    b = E('tblBorders')
    for side, sz in (('top', '8'), ('left', None), ('bottom', '8'), ('right', None),
                     ('insideH', None), ('insideV', None)):
        ET.SubElement(b, q(side), {q('val'): 'single' if sz else 'nil',
                                   **({q('sz'): sz, q('space'): '0', q('color'): '000000'}
                                      if sz else {})})
    E('tblLayout', type='fixed')
    m = E('tblCellMar')
    for side, w in (('top', '45'), ('left', '85'), ('bottom', '45'), ('right', '85')):
        ET.SubElement(m, q(side), {q('w'): w, q('type'): 'dxa'})
    E('tblLook', val='0420' if head else '0400', firstRow='1' if head else '0', lastRow='0',
      firstColumn='0', lastColumn='0', noHBand='1', noVBand='1')
    for c in keep:
        tp.append(c)

    # grid scaled to the full text width, author's proportions kept
    grid = tbl.find(q('tblGrid'))
    cols = [int(g.get(q('w'))) for g in grid.findall(q('gridCol'))]
    scale = TEXT_TWIPS / sum(cols)
    cols = [round(c * scale) for c in cols]
    cols[-1] += TEXT_TWIPS - sum(cols)
    for g, w in zip(grid.findall(q('gridCol')), cols):
        g.set(q('w'), str(w))

    cased = False
    unbold = [False]
    for ri, tr in enumerate(tbl.findall(q('tr'))):
        trp = tr.find(q('trPr'))
        if trp is None:
            trp = ET.Element(q('trPr'))
            tr.insert(0 if tr.find(q('tblPrEx')) is None else 1, trp)
        child(trp, 'cantSplit')
        if head and ri == 0:
            child(trp, 'tblHeader')
        col = 0
        for tc in tr.findall(q('tc')):
            tcp = tc.find(q('tcPr'))
            if tcp is None:
                tcp = ET.Element(q('tcPr'))
                tc.insert(0, tcp)
            span = int(tcp.find(q('gridSpan')).get(q('val'))) if tcp.find(q('gridSpan')) is not None else 1
            child(tcp, 'tcW', {'w': str(sum(cols[col:col + span])), 'type': 'dxa'})
            for tag in ('tcBorders', 'shd'):
                for el in tcp.findall(q(tag)):
                    tcp.remove(el)
            if head and ri == 0:
                bd = child(tcp, 'tcBorders')
                ET.SubElement(bd, q('bottom'), {q('val'): 'single', q('sz'): '4',
                                                 q('space'): '0', q('color'): '000000'})
            child(tcp, 'vAlign', {'val': 'center'})
            align = {'L': 'left', 'C': 'center'}[aligns[min(col, len(aligns) - 1)]]
            for p in tc.findall(q('p')):
                pp = ppr(p)
                child(pp, 'spacing', {'before': '0', 'after': '0', 'line': '240',
                                      'lineRule': 'auto'})
                child(pp, 'jc', {'val': align})
                for r in p.iter(q('r')):
                    rp = rpr(r)
                    times(rp)
                    child(rp, 'sz', {'val': '22'}); child(rp, 'szCs', {'val': '22'})
                    if head and ri == 0:
                        child(rp, 'b'); child(rp, 'bCs')
                    else:                              # only the header row is bold
                        for tag in ('b', 'bCs'):
                            for el in rp.findall(q(tag)):
                                rp.remove(el)
                                unbold[0] = True
                    t = r.find(q('t'))
                    if factor_x and t is not None and t.text and re.search(r'\dx\b', t.text):
                        t.text = re.sub(r'(\d)x\b', '\\1×', t.text)
                        LOG.append(f'{label}: "4x", "8x" written as "4×", "8×"') \
                            if not any('4×' in l for l in LOG) else None
            if sentence:
                cased |= sentence_case(tc)
            col += span
    if cased:
        LOG.append(f'{label}: headings and entries set in sentence case, as in Table 1.4')
    if unbold[0]:
        LOG.append(f'{label}: bold removed from the body rows; only the header is bold')


# ───────────────────────────────────────────── figures
def style_figure(p, num, caption, zf, rels, new_media):
    pp = ppr(p)
    for el in pp.findall(q('ind')):
        pp.remove(el)
    child(pp, 'keepNext')
    child(pp, 'spacing', {'before': '240', 'after': '0', 'line': '240', 'lineRule': 'auto'})
    child(pp, 'jc', {'val': 'center'})
    inline = p.find('.//' + q('inline', WP))
    doc_pr = inline.find(q('docPr', WP))
    doc_pr.set('descr', re.sub(r'^Figure 1\.\d+\.\s*', '', caption))
    if num not in NEW_FIG:
        return
    png = f'figures/ch1/fig_1_{NEW_FIG[num]}.png'
    data = open(png, 'rb').read()
    w, h = Image.open(io.BytesIO(data)).size
    cx, cy = TEXT_EMU, round(TEXT_EMU * h / w)
    inline.find(q('extent', WP)).set('cx', str(cx)); inline.find(q('extent', WP)).set('cy', str(cy))
    ext = inline.find('.//' + q('xfrm', A) + '/' + q('ext', A))
    ext.set('cx', str(cx)); ext.set('cy', str(cy))
    eff = inline.find(q('effectExtent', WP))
    if eff is not None:
        for k in ('l', 't', 'r', 'b'):
            eff.set(k, '0')
    # A crop applied in Word to the old picture would cut into the new one.
    for src in inline.iter(q('srcRect', A)):
        src.getparent().remove(src)
        LOG.append(f'Figure 1.{num}: Word crop of the old picture removed '
                   f'(the new drawing has no title or margin to trim)')
    rid = inline.find('.//' + q('blip', A)).get(q('embed', R))
    new_media['word/' + rels[rid]] = data


def split_figure_paragraph(p):
    """An image sharing its paragraph with its caption is split in two, so that every
    figure is an image paragraph followed by a caption paragraph."""
    kids = list(p)
    k = next(i for i, c in enumerate(kids) if c.find('.//' + q('drawing')) is not None)
    tail = [c for c in kids[k + 1:] if ET.QName(c).localname != 'pPr']
    if not ''.join(text(c) for c in tail).strip():
        return None
    cap = ET.Element(q('p'))
    pp = p.find(q('pPr'))
    if pp is not None:
        cap.append(copy.deepcopy(pp))
    for c in tail:
        cap.append(c)                       # moves the element
    p.addnext(cap)
    t = cap.find('.//' + q('t'))            # the caption must not start with a space
    if t is not None and t.text:
        t.text = t.text.lstrip()
    return cap


# ───────────────────────────────────────────── text
# Headings in sentence case, as in the table of contents, and without the stray full
# stops after "1.4" and "1.5". Each entry: the start of the heading, then the changes.
HEADINGS = [
    ('1.1 Introduction', [('The High-Speed Landscape', 'the high-speed landscape')]),
    ('Defining "High Speed"', [('"High Speed"', '"high speed"')]),
    ('1.1.2 Historical Context', [('Historical Context and the Direct-Drive Revolution',
                                   'Historical context and the direct-drive revolution')]),
    ('1.2.1 Industrial', [('Industrial High-Speed Machines: The Stationary Approach',
                           'Industrial high-speed machines: the stationary approach')]),
    ('1.2.2 High-Specific-Power', [('High-Specific-Power HS Machines: The Mobile Approach',
                                    'High-specific-power HS machines: the mobile approach')]),
    ('1.3 Fundamental', [('Fundamental Physical Constraints', 'Fundamental physical constraints')]),
    ('1.3.1 Mechanical Limits', [('Mechanical Limits: The ', 'Mechanical limits: the '),
                                 (' Wall', ' wall')]),
    ('1.3.2 Rotordynamics', [('Rotordynamics and Critical Speeds',
                              'Rotordynamics and critical speeds')]),
    ('1.4. The role', [('1.4. ', '1.4 ')]),
    ('1.5. Scaling', [('1.5. ', '1.5 ')]),
    ('1.5.2 Mechanical stress', [('scaling: The ', 'scaling: the ')]),
    ('1.5.3 Loss scaling', [('The efficiency', 'the efficiency')]),
    ('1.5.4 Thermal scaling', [('The square-cube', 'the square-cube')]),
    ('1.6 Summary', [('Framing the Design Challenges Ahead', 'framing the design challenges ahead')]),
    ('1.6.2 Roadmap', [('Roadmap of the Following Book Chapters',
                        'Roadmap of the following book chapters')]),
]
# The unnumbered headings below the numbered ones: bold paragraphs of their own.
RUN_IN = {
    'The Limitations of the Geared Legacy': 'The limitations of the geared legacy',
    'The Integrated High-Speed Unit: A Leap in Performance':
        'The integrated high-speed unit: a leap in performance',
    'Challenges and Trade-offs': 'Challenges and trade-offs',
    'The Divergent Evolution: Direct-Drive Industrial vs. Geared Traction':
        'The divergent evolution: direct-drive industrial vs. geared traction',
    'The Industrial Paradigm: The "Gearless" Hermetic Unit':
        'The industrial paradigm: the "gearless" hermetic unit',
    'The Traction Paradigm: The Geared High-Speed Optimum':
        'The traction paradigm: the geared high-speed optimum',
    'The Economic Paradox: Why "More Parts" Can Be Cheaper':
        'The economic paradox: why "more parts" can be cheaper',
    'Applications: The Drivers of Direct-Drive': 'Applications: the drivers of direct drive',
    'Topology: The Logic of Low Pole Counts': 'Topology: the logic of low pole counts',
    'Two-Pole Induction Machines (IM)': 'Two-pole induction machines (IM)',
    '2/4-Pole Rotor-Surface-Magnet PMSMs': '2/4-pole rotor-surface-magnet PMSMs',
    'Strategy: Mechanical Robustness and Sleeve Technology':
        'Strategy: mechanical robustness and sleeve technology',
    'Power Electronics: The IGBT Compatibility': 'Power electronics: the IGBT compatibility',
    'Conclusion: The Stationary Philosophy': 'Conclusion: the stationary philosophy',
    'Applications: The Pursuit of Power Density': 'Applications: the pursuit of power density',
    'Topology: Multi-pole IPM and Reluctance Torque':
        'Topology: multi-pole IPM and reluctance torque',
    'Strategy: Mass Minimization through Frequency':
        'Strategy: mass minimization through frequency',
    'Power Electronics: The Necessity of Wide Bandgap (SiC/GaN)':
        'Power electronics: the necessity of wide bandgap (SiC/GaN)',
    'Conclusion: The High-Frequency High-Density Frontier':
        'Conclusion: the high-frequency high-density frontier',
    'Centrifugal Stress Distribution: Solid vs. Laminated Rotors':
        'Centrifugal stress distribution: solid vs. laminated rotors',
    'Material Fatigue and the Retention System': 'Material fatigue and the retention system',
    ' Ratio Challenge: Why HS Machines are Long and Thin?':
        ' ratio challenge: why HS machines are long and thin?',
    'Bearing Technologies: From Ball Bearings to AMBs':
        'Bearing technologies: from ball bearings to AMBs',
    'Framing the Comparison': 'Framing the comparison',
}
# Two headings of §1.1.1 were set as Heading 3 beside the numbered ones; they become
# bold paragraphs like the other headings at that depth.
DEMOTE = {'The r/min fallacy: Why speed is a relative term.':
              'The r/min fallacy: why speed is a relative term',
          'Different definitions of high speed': 'Different definitions of high speed'}
SECTION_1_2 = '1.2 The two paradigms: industrial and mobile'
# In-text citations brought to one form, "(Author et al., year)".
CITATIONS = [('Armengaud et al, 2025', 'Armengaud et al., 2025'),
             ('Canseven et. al., 2024', 'Canseven et al., 2024'),
             ('Lipo, T.A., 2017', 'Lipo, 2017'),
             ('Pyrhönen et. al., 2013', 'Pyrhönen et al., 2013')]
# The reference list. The authors' comments gave the six references in full; the
# author lists and identifiers of El Hajji et al. and Armengaud et al. are completed
# from the publishers' records. Each entry is a list of (text, italic) pieces.
REFERENCES = [
    [('Armengaud, E., Ratz, F., Muñiz, Á., Poza, J., Garramiola, F., Almandoz, G., … '
      'Montonen, J. (2025). European initiatives addressing high efficiency and low-cost '
      'electric motors for circularity and low use of rare resources. ', False),
     ('SAE International Journal of Advances and Current Practices in Mobility, 7', True),
     ('(6), 2781–2794. https://doi.org/10.4271/2025-01-8806', False)],
    [('Canseven, H. T., Petrov, I., Martikainen, I., & Pyrhönen, J. (2024). Eddy-current '
      'losses in slitted rotor cores of PMSMs—Development of a novel method. ', False),
     ('IEEE Transactions on Energy Conversion, 40', True), ('(2), 1339–1349.', False)],
    [('El Hajji, T., Hemeida, A., Lehikoinen, A., Martin, F., & Belahcen, A. (2024). Optimal '
      'design of high specific power electric machines for fully electric regional aircraft: '
      'A case study of 1 MW S-PMSM. ', False),
     ('Aerospace, 11', True), ('(10), 820. https://doi.org/10.3390/aerospace11100820', False)],
    [('Lipo, T. A. (2017). ', False), ('Analysis of synchronous machines', True),
     ('. CRC Press.', False)],
    [('Pyrhönen, J., Jokinen, T., & Hrabovcová, V. (2013). ', False),
     ('Design of rotating electrical machines', True), (' (2nd ed.). John Wiley & Sons.', False)],
    [('Scherman, E., Parviainen, M., Nutakor, C., Petrov, I., Pyrhönen, J., & Sopanen, J. '
      '(2026). Impact of rotor topology on dynamic behavior and manufacturing in a high-speed '
      'electric machine. In J. Sopanen, E. Kurvinen, R. Viitala, T. Holopainen, & '
      'T. Choudhury (Eds.), ', False),
     ('Proceedings of the 12th IFToMM International Conference on Rotordynamics', True),
     (' (Mechanisms and Machine Science, Vol. 211). Springer, Cham.', False)],
]


def replace_across(p, old, new):
    """Replace the first `old` in the paragraph text, even where it runs across several
    runs; the new text takes the formatting of the run in which `old` begins."""
    ts = list(p.iter(q('t')))
    s = ''.join(t.text or '' for t in ts)
    at = s.find(old)
    if at < 0:
        raise ValueError(f'{old!r} not found in {s[:60]!r}')
    end, done, placed = at + len(old), 0, False
    for t in ts:
        a = done
        done += len(t.text or '')
        if done <= at or a >= end:
            continue
        lo, hi = max(at, a) - a, min(end, done) - a
        t.text = t.text[:lo] + ('' if placed else new) + t.text[hi:]
        t.set(f'{{{XML}}}space', 'preserve')
        placed = True


def body_run(s, italic=False, bold=False):
    """A run in the body font, Times New Roman, British English, as the chapter's own."""
    r = ET.Element(q('r'))
    rp = ET.SubElement(r, q('rPr'))
    times(rp)
    if bold:
        child(rp, 'b'); child(rp, 'bCs')
    if italic:
        child(rp, 'i'); child(rp, 'iCs')
    child(rp, 'lang', {'val': 'en-GB'})
    t = ET.SubElement(r, q('t'))
    t.text = s
    t.set(f'{{{XML}}}space', 'preserve')
    return r


def heading(level, s):
    p = ET.Element(q('p'))
    pp = ppr(p)
    child(pp, 'pStyle', {'val': f'Heading{level}'})
    child(pp, 'jc', {'val': 'both'})
    p.append(body_run(s))
    return p


def fix_text(body):
    """The wording changes agreed for the circulated chapter, each one logged."""
    paras = [el for el in body if el.tag == q('p')]
    style = lambda p: (p.find(q('pPr') + '/' + q('pStyle')).get(q('val'))
                       if p.find(q('pPr') + '/' + q('pStyle')) is not None else '')
    for start, changes in HEADINGS:
        p = next(p for p in paras if style(p).startswith('Heading') and text(p).startswith(start))
        for old, new in changes:
            replace_across(p, old, new)
    LOG.append(f'Headings: {len(HEADINGS)} set in sentence case as in the table of contents, '
               'and the full stops after "1.4" and "1.5" removed')
    n = 0
    for p in paras:
        for old, new in RUN_IN.items():
            if old in text(p) and not style(p):
                replace_across(p, old, new)
                child(ppr(p), 'keepNext')           # never last on a page
                n += 1
    assert n == len(RUN_IN), (n, len(RUN_IN))
    LOG.append(f'Unnumbered headings: {n} bold headings within the sections set in sentence case '
               'and kept with the paragraph that follows')
    for p in paras:
        if text(p) in DEMOTE and style(p) == 'Heading3':
            new = DEMOTE[text(p)]
            pp = ppr(p)
            for tag in ('pStyle', 'numPr'):
                for el in pp.findall(q(tag)):
                    pp.remove(el)
            child(pp, 'keepNext')
            replace_across(p, text(p), new)
            for rp in [rpr(r) for r in runs(p)] + [child(pp, 'rPr', replace=False)]:
                child(rp, 'b'); child(rp, 'bCs')
            LOG.append(f'"{new}": was a Heading 3 without a number beside the numbered ones; '
                       'now a bold heading within §1.1.1, like the other headings at that depth')
    first = next(p for p in paras if style(p) == 'Heading3' and text(p).startswith('1.2.1'))
    first.addprevious(heading(2, SECTION_1_2))
    LOG.append(f'§1.2 heading added: "{SECTION_1_2}" (the chapter ran from §1.1.2 into §1.2.1)')
    p = next(p for p in paras if 'mechanical rpm value' in text(p))
    replace_across(p, 'not merely a mechanical rpm value', 'not merely a mechanical value in r/min')
    LOG.append('§1.1.1: "a mechanical rpm value" made "a mechanical value in r/min"')
    for old, new in CITATIONS:
        p = next(p for p in paras if old in text(p))
        replace_across(p, old, new)
    LOG.append('Citations: four brought to the form "(Author et al., year)"')

    # the reference list, after the last paragraph of the chapter
    last = [p for p in paras if text(p).strip()][-1]
    at = last
    for el in [heading(2, 'References')] + [ET.Element(q('p')) for _ in REFERENCES]:
        at.addnext(el)
        at = el
    refs = list(body)[list(body).index(last) + 2:][:len(REFERENCES)]
    for p, pieces in zip(refs, REFERENCES):
        pp = ppr(p)
        child(pp, 'spacing', {'after': '80', 'line': '259', 'lineRule': 'auto'})
        child(pp, 'ind', {'left': '360', 'hanging': '360'})
        child(pp, 'jc', {'val': 'left'})
        for s, it in pieces:
            p.append(body_run(s, italic=it))
    LOG.append(f'References: a list of the {len(REFERENCES)} works cited, from the authors\' '
               'comments, added at the end of the chapter')


def resolve_comments(ext):
    """Mark every comment resolved: the six still open each held a reference, and every
    reference is now in the list at the end of the chapter."""
    W15 = 'http://schemas.microsoft.com/office/word/2012/wordml'
    n = 0
    for e in ext.findall(q('commentEx', W15)):
        if e.get(q('done', W15)) != '1':
            e.set(q('done', W15), '1')
            n += 1
    LOG.append(f'Comments: the {n} still open, each holding a full reference, marked resolved')


# ───────────────────────────────────────────── main
def main():
    zin = zipfile.ZipFile(SRC)
    doc = ET.fromstring(zin.read('word/document.xml'))
    styles = ET.fromstring(zin.read('word/styles.xml'))
    rels = {r.get('Id'): r.get('Target')
            for r in ET.fromstring(zin.read('word/_rels/document.xml.rels'))}
    add_styles(styles)

    body = doc.find(q('body'))
    for el in list(body):
        if el.tag == q('p') and el.find('.//' + q('drawing')) is not None:
            if split_figure_paragraph(el) is not None:
                LOG.append('Figure 1.4: image and caption separated into two paragraphs, '
                           'as for every other figure')
    els = list(body)
    new_media = {}

    # figures and their captions
    figs = [i for i, el in enumerate(els)
            if el.tag == q('p') and el.find('.//' + q('drawing')) is not None]
    assert len(figs) == 9, len(figs)
    for num, i in enumerate(figs, 1):
        cap = next(el for el in els[i + 1:i + 4] if el.tag == q('p') and text(el).strip())
        assert text(cap).startswith(f'Figure 1.{num}.'), text(cap)[:40]
        if num == 2:
            replace_text(cap, 'Left:', '(a)')
            replace_text(cap, 'Right:', '(b)')
            LOG.append('Figure 1.2 caption: "Left:" and "Right:" made "(a)" and "(b)", '
                       'since the panels are stacked')
            replace_text(cap, 'active magnetic bearings,', 'active magnetic bearings (AMBs),')
            append_sentence(cap, ' The units are drawn to scale for a compressor of about 300\u00a0kW: '
                                 '(a) and (b) at one scale, so that their sizes compare directly, '
                                 'and (c), the motor of (b) with its upper half in section, at '
                                 'twice that scale. The dimensions are representative of '
                                 'catalogue equipment, not those of a particular machine.')
            LOG.append('Figure 1.2 caption: "(AMBs)" added, the abbreviation the drawing uses, '
                       'and two sentences on the common scale of (a) and (b) and on (c)')
        if num == 4:
            append_sentence(cap, ' The rotor is drawn to scale above the mode shapes, on the '
                                 'same axial scale; the vertical lines mark its radial AMBs.')
            LOG.append('Figure 1.4 caption: one sentence added explaining the rotor drawing '
                       'above the mode shapes and the lines marking the radial AMBs')
        if num == 5:
            append_sentence(cap, ' The loss values are illustrative (copper 2.8 %, iron 1.0 % and '
                                 'windage 0.4 % of rated output at rated speed); the efficiency '
                                 'maximum lies where the tangent from the origin touches the '
                                 'total loss.')
            LOG.append('Figure 1.5 caption: one sentence added stating that its loss values '
                       'are illustrative and how the efficiency maximum is found')
        if num == 9:
            replace_across(cap, 'along every edge of the triangle',
                           'around the cycle, each remedy creating the next problem')
            replace_across(cap, 'window at its centre', 'window at the centre')
            append_sentence(cap, ' Within the window the power electronics stands as a gate between '
                                 'the two paradigms, shown at 30\u00a0000\u00a0r/min: above it the two-pole '
                                 'industrial machine at 500\u00a0Hz, which silicon IGBTs can supply, and '
                                 'below it the six-pole mobile machine at 1500\u00a0Hz, which needs SiC or '
                                 'GaN.')
            LOG.append('Figure 1.9 caption: the triangle\'s edges become the cycle the figure now '
                       'draws, and one sentence explains the gate and the two machines in the window')
        style_figure(els[i], num, text(cap), zin, rels, new_media)
        style_caption(cap, 'Figure', num)

    # tables and their captions
    tbls = [i for i, el in enumerate(els) if el.tag == q('tbl')]
    assert len(tbls) == 4, len(tbls)
    for num, i in enumerate(tbls, 1):
        cap = next(el for el in reversed(els[max(0, i - 3):i])
                   if el.tag == q('p') and text(el).strip())
        assert text(cap).startswith(f'Table 1.{num}'), text(cap)[:40]
        style_caption(cap, 'Table', num)
        style_table(els[i], num)

    # the wording agreed after the house-style pass, and the open comments
    fix_text(body)
    ext = ET.fromstring(zin.read('word/commentsExtended.xml'))
    resolve_comments(ext)

    # write
    out = {'word/document.xml': ET.tostring(doc, xml_declaration=True, encoding='UTF-8',
                                             standalone=True),
           'word/styles.xml': ET.tostring(styles, xml_declaration=True, encoding='UTF-8',
                                          standalone=True),
           'word/commentsExtended.xml': ET.tostring(ext, xml_declaration=True, encoding='UTF-8',
                                                    standalone=True)}
    out.update(new_media)
    with zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            zout.writestr(item, out.get(item.filename, zin.read(item.filename)))
    print(f'wrote {DST}: {len(new_media)} figures replaced, 9 figure and 4 table captions, '
          f'4 tables restyled')
    print('text changes:')
    for l in dict.fromkeys(LOG):
        print('  -', l)


if __name__ == '__main__':
    main()
