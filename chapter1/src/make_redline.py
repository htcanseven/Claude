"""Build Word tracked-changes redlines: original draft -> revised chapter.

Produces genuine w:ins / w:del revision markup that Word's Review pane can
step through, accept and reject, and turns the Track Changes setting on.
"""
import re, zipfile, difflib, html
from xml.etree import ElementTree as ET
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import parse_xml

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"')

ORIG = '/root/.claude/uploads/09466ca9-86b9-587c-a1f5-70ef3088e8a8/98e68beb-The_first_Ch_of_HS_machines.docx'
AUTHOR, DATE = 'Chapter 1 revision', '2026-08-28T00:00:00Z'

# Adobe Symbol font -> Unicode (Word stores these as w:sym char="F0xx")
_LOW = 'αβχδεφγηιϕκλμνοπθρστυϖωξψζ'
_UPP = 'ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖ'
SYM = {}
for i, ch in enumerate(_LOW):
    SYM[0xF061 + i] = ch
for i, ch in enumerate(_UPP):
    SYM[0xF041 + i] = ch
SYM.update({0xF0B4: '×', 0xF0B1: '±', 0xF0A3: '≤', 0xF0B3: '≥', 0xF0B9: '≠',
            0xF0BB: '≈', 0xF0D7: '·', 0xF0B7: '·', 0xF0AE: '→', 0xF0B5: '∝',
            0xF0D6: '√', 0xF0A5: '∞', 0xF0B6: '∂', 0xF0F7: '÷'})


def _sym(node):
    try:
        return SYM.get(int(node.get(W + 'char'), 16), '')
    except (TypeError, ValueError):
        return ''


def _omml(node):
    """Linearise an OMML equation to readable text."""
    return ''.join(t.text or '' for t in node.iter(M + 't'))


def para_text(p):
    out = []
    for n in p.iter():
        if n.tag == W + 't':
            out.append(n.text or '')
        elif n.tag == W + 'delText':
            continue
        elif n.tag == W + 'sym':
            out.append(_sym(n))
        elif n.tag == W + 'tab':
            out.append(' ')
        elif n.tag == M + 'oMath':
            out.append(_omml(n))
        elif n.tag == W + 'drawing':
            out.append('[FIGURE]')
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def style_of(p):
    pPr = p.find(W + 'pPr')
    if pPr is None:
        return 'Normal'
    s = pPr.find(W + 'pStyle')
    v = (s.get(W + 'val') if s is not None else '') or ''
    if v.lower().startswith('heading'):
        return 'Heading ' + v[-1]
    return 'Normal'


def extract_original():
    """(style, text) pairs from the uploaded draft, OMML and symbols resolved."""
    z = zipfile.ZipFile(ORIG)
    root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(W + 'body')
    items = []
    for el in body:
        if el.tag == W + 'p':
            t = para_text(el)
            if t:
                items.append((style_of(el), t))
        elif el.tag == W + 'tbl':
            for row in el.iter(W + 'tr'):
                cells = [' '.join(para_text(p) for p in c.iter(W + 'p')).strip()
                         for c in row.findall(W + 'tc')]
                line = ' | '.join(c for c in cells if c)
                if line:
                    items.append(('Normal', line))
    return items


def extract_markdown(path):
    """(style, text) pairs from a revised chapter source."""
    items, lines = [], open(path, encoding='utf-8').read().split('\n')
    for ln in lines:
        s = ln.strip()
        if not s or s == '---':
            continue
        if s.startswith('#### '):
            items.append(('Heading 4', s[5:]))
        elif s.startswith('### '):
            items.append(('Heading 3', s[4:]))
        elif s.startswith('## '):
            items.append(('Heading 2', s[3:]))
        elif s.startswith('# '):
            items.append(('Heading 1', s[2:]))
        elif s.startswith('|'):
            cells = [c.strip() for c in s.strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                continue
            items.append(('Normal', ' | '.join(cells)))
        else:
            plain = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
            plain = re.sub(r'\*([^*]+?)\*', r'\1', plain)
            items.append(('Normal', re.sub(r'\s+', ' ', plain).strip()))
    return items


# ---------------------------------------------------------------- XML helpers
_uid = [1000]


def nid():
    _uid[0] += 1
    return _uid[0]


def esc(t):
    return html.escape(t, quote=False)


def run_xml(text, mode):
    """mode: None | 'ins' | 'del'"""
    if mode == 'del':
        return (f'<w:del {NS} w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}">'
                f'<w:r><w:delText xml:space="preserve">{esc(text)}</w:delText></w:r></w:del>')
    if mode == 'ins':
        return (f'<w:ins {NS} w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}">'
                f'<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:ins>')
    return f'<w:r {NS}><w:t xml:space="preserve">{esc(text)}</w:t></w:r>'


def add_para(doc, style, segments, mark=None):
    """segments: list of (mode, text). mark: 'ins'/'del' for the paragraph mark."""
    p = doc.add_paragraph()
    try:
        p.style = doc.styles[style]
    except KeyError:
        pass
    if mark:
        tag = 'w:ins' if mark == 'ins' else 'w:del'
        rPr = parse_xml(f'<w:rPr {NS}><{tag} w:id="{nid()}" w:author="{AUTHOR}" '
                        f'w:date="{DATE}"/></w:rPr>')
        p._p.get_or_add_pPr().append(rPr)
    for mode, text in segments:
        if text:
            p._p.append(parse_xml(run_xml(text, mode)))
    return p


def word_diff(a, b):
    """Word-level segments between two paragraphs."""
    aw, bw = a.split(' '), b.split(' ')
    segs, sm = [], difflib.SequenceMatcher(None, aw, bw, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            segs.append((None, ' '.join(aw[i1:i2]) + ' '))
        elif op == 'delete':
            segs.append(('del', ' '.join(aw[i1:i2]) + ' '))
        elif op == 'insert':
            segs.append(('ins', ' '.join(bw[j1:j2]) + ' '))
        else:
            segs.append(('del', ' '.join(aw[i1:i2]) + ' '))
            segs.append(('ins', ' '.join(bw[j1:j2]) + ' '))
    return segs


def enable_track_changes(doc):
    s = doc.settings.element
    s.append(parse_xml(f'<w:trackChanges {NS}/>'))


def banner(doc, title, summary):
    h = doc.add_paragraph()
    r = h.add_run(title)
    r.bold, r.font.size = True, Pt(15)
    p = doc.add_paragraph()
    r = p.add_run(
        'Word tracked-changes comparison of the original draft against the revised chapter. '
        'Open Review → Tracking and set the display to All Markup to step through every '
        'change; Accept or Reject works normally. Track Changes is left switched on, so any '
        'further edits are also recorded.')
    r.italic, r.font.size = True, Pt(9.5)
    r.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    p = doc.add_paragraph()
    r = p.add_run('Note: the original draft stored Greek letters as Symbol-font characters and '
                  'eight equations as Word equation objects. These have been resolved to plain '
                  'Unicode text on both sides so that they do not appear as spurious differences. '
                  'Figures and tables are compared as text.')
    r.italic, r.font.size = True, Pt(9.5)
    r.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    doc.add_paragraph()
    hp = doc.add_paragraph(); rr = hp.add_run('Summary of changes in this version'); rr.bold = True
    for i, line in enumerate(summary, 1):
        p = doc.add_paragraph(style='List Number')
        add = p.add_run(line); add.font.size = Pt(10)
    doc.add_page_break()


STOP = set('the a an of and or to in is are for on at as by it its this that with be '
           'from can we they which not but if then than these those'.split())


def bag(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP}


def sim(sa, sb):
    """Jaccard-style overlap on content words; cheap enough for full alignment."""
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / max(len(sa), len(sb))


def align(a, b, thresh=0.30, band=0.45):
    """Order-preserving alignment maximising total similarity.

    A diagonal band stops far-apart paragraphs from pairing. Without it the
    planning skeleton at the head of the draft matches headings deep in the
    revised text, and order-preservation then blocks every genuine body match.

    Returns a list of (i, j) with either index None for an unmatched paragraph.
    """
    A, B = [bag(x) for x in a], [bag(x) for x in b]
    n, m = len(a), len(b)

    def score(i, j):
        if abs(i / n - j / m) > band:
            return 0.0
        return 1.0 if a[i] == b[j] else sim(A[i], B[j])

    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        row, prev = S[i], S[i - 1]
        for j in range(1, m + 1):
            s = score(i - 1, j - 1)
            diag = prev[j - 1] + s if s >= thresh else -1.0
            row[j] = max(diag, prev[j], row[j - 1])
    # traceback
    out, i, j = [], n, m
    while i > 0 and j > 0:
        s = score(i - 1, j - 1)
        if s >= thresh and abs(S[i][j] - (S[i - 1][j - 1] + s)) < 1e-9:
            out.append((i - 1, j - 1)); i, j = i - 1, j - 1
        elif abs(S[i][j] - S[i - 1][j]) < 1e-9:
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    while i > 0:
        out.append((i - 1, None)); i -= 1
    while j > 0:
        out.append((None, j - 1)); j -= 1
    return list(reversed(out))


def build(new_md, out_path, title, summary):
    orig, new = extract_original(), extract_markdown(new_md)
    doc = Document()
    st = doc.styles['Normal']
    st.font.name, st.font.size = 'Cambria', Pt(11)
    st.paragraph_format.space_after = Pt(7)
    enable_track_changes(doc)
    banner(doc, title, summary)

    a, b = [t for _, t in orig], [t for _, t in new]
    stats = dict(equal=0, inserted=0, deleted=0, revised=0, rewritten=0)

    for i, j in align(a, b):
        if i is not None and j is not None:
            if a[i] == b[j]:
                add_para(doc, new[j][0], [(None, a[i])]); stats['equal'] += 1
            elif sim(bag(a[i]), bag(b[j])) >= 0.55:
                # close enough that an inline word-level redline stays readable
                add_para(doc, new[j][0], word_diff(a[i], b[j])); stats['revised'] += 1
            else:
                # substantially rewritten: show the old and the new as whole blocks,
                # which reads far better in Word than heavily interleaved markup
                add_para(doc, 'Normal', [('del', a[i])], mark='del')
                add_para(doc, new[j][0], [('ins', b[j])], mark='ins')
                stats['rewritten'] += 1
        elif i is not None:
            add_para(doc, 'Normal', [('del', a[i])], mark='del'); stats['deleted'] += 1
        else:
            add_para(doc, new[j][0], [('ins', b[j])], mark='ins'); stats['inserted'] += 1

    doc.core_properties.title = title
    doc.save(out_path)
    return stats


SUM_FULL = [
    "Scaling table corrected. The draft's table mixed a fixed-geometry path with a tip-speed-limited path in one set of rows. Along the tip-speed-limited constant-power path, windage loss is unchanged rather than 8x, and iron loss doubles rather than quadruples.",
    "Rotordynamic scaling added. The first bending critical speed falls as the cube of design speed while operating speed rises linearly, so the margin degrades as the fourth power: doubling the speed costs a factor of 16. This constraint was absent from the draft and is the one that actually limits attainable speed.",
    "Three design paths separated explicitly (fixed geometry, tip-speed limited, length capped), because a scaling exponent is undefined until one states what is held constant. Every column of the new table names its path.",
    "Square-cube thermal argument replaced. It assumes isotropic scaling, which high-speed machines do not follow: they shrink radially and grow axially, so rotor surface area is preserved.",
    "Centrifugal stress quantified. The draft's claim that a central bore doubles stress is now derived and worked through in MPa against a real proof stress.",
    "Two drafting artefacts removed from the fP passage ('without external resources provided...', '...in the current context'), which read as an AI tool commenting on its own retrieval limits.",
    "The 180 000 kW/s threshold withdrawn. It had been calibrated from a single machine that is itself marginal by tip speed. fP is now presented as a proposed drive-system figure of merit, with calibration deferred to the Chapter 2 survey.",
    "Fourfold repetition of the industrial-versus-mobile contrast consolidated into one section and one table.",
    "Trilemma recast as three constraints plus a converter gate, resolving the draft's own observation that power electronics sat outside the trilemma.",
    "Roadmap rewritten from 19 chapters in six parts to 12 chapters in four parts.",
    "Planning skeleton removed from the head of the chapter; it had drifted from the text below it.",
    "Worked example added: the Voltcar machine carried through all three classification criteria and on to the converter requirement (31.5 kHz at m_f = 21, which silicon cannot supply).",
    "Constraints moved ahead of the design paradigms, so the physics is established before the two families are explained as different responses to it.",
    "Direct-drive history rewritten as the lead-in to the paradigms section, where it explains why the two families diverge.",
    "Notation paragraph added, fixing symbol conventions for the book.",
    "Figure numbering corrected; the draft had Figures 2 to 5 with no Figure 1. Six analytical figures generated from the equations in the text.",
]

SUM_MIN = [
    "Scaling table corrected. The draft's table mixed a fixed-geometry path with a tip-speed-limited path in one set of rows. Along the tip-speed-limited constant-power path, windage loss is unchanged rather than 8x, and iron loss doubles rather than quadruples.",
    "Rotordynamic scaling added. The first bending critical speed falls as the cube of design speed while operating speed rises linearly, so the margin degrades as the fourth power: doubling the speed costs a factor of 16. This constraint was absent from the draft.",
    "Three design paths separated explicitly (fixed geometry, tip-speed limited, length capped). Every column of the new table names its path.",
    "Square-cube thermal argument replaced, since it assumes an isotropic scaling that high-speed machines do not follow.",
    "Centrifugal stress quantified, with the doubling caused by a central bore now derived rather than asserted.",
    "Two drafting artefacts removed from the fP passage ('without external resources provided...', '...in the current context').",
    "The 180 000 kW/s threshold withdrawn; fP presented as a proposed drive-system figure of merit with calibration deferred to Chapter 2.",
    "Fourfold repetition of the industrial-versus-mobile contrast consolidated into one section and one table.",
    "Trilemma recast as three constraints plus a converter gate.",
    "Roadmap rewritten from 19 chapters in six parts to 12 chapters in four parts.",
    "Planning skeleton removed from the head of the chapter.",
    "Worked example added: the Voltcar machine carried through all three criteria and on to the converter requirement.",
    "Figure numbering corrected and six analytical figures generated from the equations in the text.",
    "Original section structure and numbering retained throughout, so this version can be reviewed side by side with the draft.",
]

if __name__ == '__main__':
    for md, out, title, summ in [
        ('ch1_full.md', 'Chapter_1_Redline_FULL.docx',
         'Chapter 1 — Tracked Changes: original draft → FULL version', SUM_FULL),
        ('ch1_minimal.md', 'Chapter_1_Redline_MINIMAL.docx',
         'Chapter 1 — Tracked Changes: original draft → MINIMAL version', SUM_MIN),
    ]:
        s = build(md, out, title, summ)
        print(f"{out}\n   unchanged {s['equal']}   edited-inline {s['revised']}   "
              f"rewritten {s['rewritten']}   inserted {s['inserted']}   deleted {s['deleted']}")
