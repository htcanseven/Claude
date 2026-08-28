"""Accept-all must reproduce the revised chapter; reject-all must reproduce the draft."""
import zipfile, sys, re
from xml.etree import ElementTree as ET
sys.path.insert(0, 'src')
import make_redline as R

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def resolve(path, mode):
    """mode 'accept' or 'reject' -> list of paragraph strings."""
    root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    out = []
    for p in root.iter(W + 'p'):
        pPr = p.find(W + 'pPr')
        mark = None
        if pPr is not None:
            rPr = pPr.find(W + 'rPr')
            if rPr is not None:
                if rPr.find(W + 'ins') is not None:
                    mark = 'ins'
                elif rPr.find(W + 'del') is not None:
                    mark = 'del'
        if mode == 'accept' and mark == 'del':
            continue
        if mode == 'reject' and mark == 'ins':
            continue
        buf = []
        for child in p:
            if child.tag == W + 'ins':
                if mode == 'accept':
                    buf += [t.text or '' for t in child.iter(W + 't')]
            elif child.tag == W + 'del':
                if mode == 'reject':
                    buf += [t.text or '' for t in child.iter(W + 'delText')]
            elif child.tag == W + 'r':
                buf += [t.text or '' for t in child.iter(W + 't')]
        s = re.sub(r'\s+', ' ', ''.join(buf)).strip()
        if s:
            out.append(s)
    return out


def norm(xs):
    return [re.sub(r'\s+', ' ', x).strip() for x in xs if x.strip()]


orig = norm([t for _, t in R.extract_original()])
ok = True
for docf, md in [('Chapter_1_Redline_FULL.docx', 'ch1_full.md'),
                 ('Chapter_1_Redline_MINIMAL.docx', 'ch1_minimal.md')]:
    new = norm([t for _, t in R.extract_markdown(md)])
    acc = norm(resolve(docf, 'accept'))
    rej = norm(resolve(docf, 'reject'))
    # the banner block sits at the head of the redline; skip it on both sides
    def tail(xs, ref):
        return xs[len(xs) - len(ref):] if len(xs) >= len(ref) else xs
    a_ok = tail(acc, new) == new
    r_ok = tail(rej, orig) == orig
    print(f'{docf}')
    print(f'   accept-all reproduces revised chapter : {a_ok}  ({len(tail(acc,new))} vs {len(new)} paragraphs)')
    print(f'   reject-all reproduces original draft  : {r_ok}  ({len(tail(rej,orig))} vs {len(orig)} paragraphs)')
    if not a_ok:
        d = [(x, y) for x, y in zip(tail(acc, new), new) if x != y][:2]
        for x, y in d:
            print(f'      GOT {x[:90]}\n      EXP {y[:90]}')
    if not r_ok:
        d = [(x, y) for x, y in zip(tail(rej, orig), orig) if x != y][:2]
        for x, y in d:
            print(f'      GOT {x[:90]}\n      EXP {y[:90]}')
    ok = ok and a_ok and r_ok
print('\nRESULT:', 'PASS' if ok else 'FAIL')
