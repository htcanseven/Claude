"""Check the tracked Chapter 1: reject-all must reproduce the author's original
text exactly, and accept-all must contain the expected new material.

usage: python3 src/verify_tracked.py work/Chapter_1_tracked.docx
"""
import sys, json, re, zipfile
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
_LOW = 'αβχδεφγηιϕκλμνοπθρστυϖωξψζ'; _UPP = 'ΑΒΧΔΕΦΓΗΙϑΚΛΜΝΟΠΘΡΣΤΥςΩΞΨΖ'
SYM = {0xF061 + i: c for i, c in enumerate(_LOW)}
SYM.update({0xF041 + i: c for i, c in enumerate(_UPP)})
SYM.update({0xF0B4: '×', 0xF0B1: '±', 0xF0A3: '≤', 0xF0B3: '≥', 0xF0B9: '≠', 0xF0BB: '≈',
            0xF0D7: '·', 0xF0B7: '·', 0xF0AE: '→', 0xF0B5: '∝', 0xF0D6: '√'})


def runtext(el, mode):
    out = []
    for n in el.iter():
        if n.tag == W + 't' and mode != 'deltext':
            out.append(n.text or '')
        elif n.tag == W + 'delText' and mode == 'deltext':
            out.append(n.text or '')
        elif n.tag == W + 'sym':
            try: out.append(SYM.get(int(n.get(W + 'char'), 16), ''))
            except (TypeError, ValueError): pass
        elif n.tag == W + 'tab':
            out.append(' ')
        elif n.tag == M + 'oMath':
            out.append(''.join(t.text or '' for t in n.iter(M + 't')))
        elif n.tag == W + 'drawing':
            out.append('[FIGURE]')
    return ''.join(out)


def resolve(path, mode):
    root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    body = root.find(W + 'body'); out = []

    def para(p):
        pPr = p.find(W + 'pPr'); mark = None
        if pPr is not None:
            r = pPr.find(W + 'rPr')
            if r is not None:
                if r.find(W + 'ins') is not None: mark = 'ins'
                elif r.find(W + 'del') is not None: mark = 'del'
        if (mode == 'accept' and mark == 'del') or (mode == 'reject' and mark == 'ins'):
            return None
        buf = []
        for c in p:
            if c.tag == W + 'ins':
                if mode == 'accept': buf.append(runtext(c, 't'))
            elif c.tag == W + 'del':
                if mode == 'reject': buf.append(runtext(c, 'deltext'))
            elif c.tag == W + 'pPr':
                continue
            else:
                buf.append(runtext(c, 't'))
        s = re.sub(r'\s+', ' ', ''.join(buf)).strip()
        return s or None

    for el in body:
        if el.tag == W + 'p':
            s = para(el)
            if s: out.append(s)
        elif el.tag == W + 'tbl':
            for row in el.iter(W + 'tr'):
                trPr = row.find(W + 'trPr'); rmark = None
                if trPr is not None:
                    if trPr.find(W + 'ins') is not None: rmark = 'ins'
                    elif trPr.find(W + 'del') is not None: rmark = 'del'
                if (mode == 'reject' and rmark == 'ins') or (mode == 'accept' and rmark == 'del'):
                    continue
                cells = [' '.join(filter(None, (para(p) for p in c.iter(W + 'p')))).strip()
                         for c in row.findall(W + 'tc')]
                line = ' | '.join(x for x in cells if x)
                if line: out.append(line)
    return out


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'work/Chapter_1_tracked.docx'
    orig = json.load(open('original_draft_text.json'))
    rej, acc = resolve(path, 'reject'), resolve(path, 'accept')
    ok = rej == orig
    print(f'reject-all == original draft : {ok}  ({len(rej)}/{len(orig)} paragraphs)')
    if not ok:
        import difflib
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, orig, rej, autojunk=False).get_opcodes():
            if op != 'equal':
                print(' ', op, 'orig', i1, i2, 'rej', j1, j2)
    d = zipfile.ZipFile(path).read('word/document.xml').decode()
    checks = {
        'artefact sentence gone': not any('without external resources' in p for p in acc),
        'planning outline gone': acc[0].startswith('1.1 Introduction'),
        'Figure 1.9 caption': any(p.startswith('Figure 1.9.') for p in acc),
        'Table 1.4 present': any(p.startswith('First critical speed') for p in acc),
        '§1.5.6 present': any(p.startswith('1.5.6') for p in acc),
        'roadmap: four parts': sum(1 for p in acc if p.startswith('Part ') and ':' in p) == 4,
        'roadmap: 12 chapters named': any('Chapters 11 and 12' in p for p in acc),
        'roadmap: 19-chapter text gone': not any('Chapter 19' in p or 'Part VI' in p for p in acc),
        'closing sentence kept': any(p.startswith('This roadmap ensures') for p in acc),
        'drawings (4 original + 6 inserted)': len(re.findall(r'<w:drawing[ >]', d)) == 10,
        'track revisions on': b'trackRevisions' in zipfile.ZipFile(path).read('word/settings.xml'),
    }
    for k, v in checks.items():
        print(f'  {"PASS" if v else "FAIL"}  {k}')
    print('RESULT:', 'PASS' if ok and all(checks.values()) else 'FAIL')
    sys.exit(0 if ok and all(checks.values()) else 1)
