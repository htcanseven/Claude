"""Apply the house style to Chapter 1 (House_Style.md).

Reads the authors' final chapter and writes Chapter_1_house_style.docx, changing
presentation only:

* figures 1.1-1.3 and 1.5-1.9 are replaced by the house-style drawings of
  src/ch1_figures.py, each placed at exactly the text width so that its 11 pt
  text prints at 11 pt; Figure 1.4, the authors' MATLAB plot, is left in place;
* every caption gets one paragraph style, Caption: Times New Roman 11 pt,
  justified like the body, with the label "Figure 1.x." or "Table 1.x." in bold;
  figure captions below the figure, table captions above the table;
* every table gets one style: full text width, horizontal rules only (1 pt above
  and below the table, 0.5 pt under the header), Times New Roman 11 pt throughout,
  text columns left and numeric columns centred, header in bold and repeated on a
  new page, sentence case;
* the alternative text of each figure is set to its caption.

Text is touched in five places only, each listed in the change log printed at
the end: missing full stops after three table numbers, sentence case in two
tables, "4x" written as "4×", "Left/Right" in the Figure 1.2 caption made
"(a)/(b)" to match the stacked panels, and one sentence added to the Figure 1.5
caption saying its loss values are illustrative.

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
NEW_FIG = {1: '01', 2: '02', 3: '03', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09'}
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
    head = HEADER[num]
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
            align = {'L': 'left', 'C': 'center'}[COLS[num][min(col, len(COLS[num]) - 1)]]
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
                    if num == 3 and t is not None and t.text and re.search(r'\dx\b', t.text):
                        t.text = re.sub(r'(\d)x\b', '\\1×', t.text)
                        LOG.append('Table 1.3: "4x", "8x" written as "4×", "8×"') \
                            if not any('4×' in l for l in LOG) else None
            if num in SENTENCE_CASE:
                cased |= sentence_case(tc)
            col += span
    if cased:
        LOG.append(f'Table 1.{num}: headings and entries set in sentence case, as in Table 1.4')
    if unbold[0]:
        LOG.append(f'Table 1.{num}: bold removed from the body rows; only the header is bold')


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
        if num == 5:
            append_sentence(cap, ' The loss values are illustrative (copper 2.8 %, iron 1.0 % and '
                                 'windage 0.4 % of rated output at rated speed); the efficiency '
                                 'maximum lies where the tangent from the origin touches the '
                                 'total loss.')
            LOG.append('Figure 1.5 caption: one sentence added stating that its loss values '
                       'are illustrative and how the efficiency maximum is found')
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

    # write
    out = {'word/document.xml': ET.tostring(doc, xml_declaration=True, encoding='UTF-8',
                                             standalone=True),
           'word/styles.xml': ET.tostring(styles, xml_declaration=True, encoding='UTF-8',
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
