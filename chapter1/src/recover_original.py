"""Recover the original draft's paragraph text from an existing redline.

Reject-all on a redline reproduces the source document exactly (verified by
verify_redline.py), so the redline is a lossless record of the draft. The
result is cached in the repository so the pipeline no longer depends on the
uploaded .docx being present.
"""
import zipfile, json, re
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def reject_all(path):
    root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    out = []
    for p in root.iter(W + 'p'):
        pPr = p.find(W + 'pPr')
        if pPr is not None:
            rPr = pPr.find(W + 'rPr')
            if rPr is not None and rPr.find(W + 'ins') is not None:
                continue                      # inserted paragraph -> not in original
        buf = []
        for child in p:
            if child.tag == W + 'ins':
                continue                      # insertions rejected
            if child.tag == W + 'del':
                buf += [t.text or '' for t in child.iter(W + 'delText')]
            elif child.tag == W + 'r':
                buf += [t.text or '' for t in child.iter(W + 't')]
        s = re.sub(r'\s+', ' ', ''.join(buf)).strip()
        if s:
            out.append(s)
    return out


if __name__ == '__main__':
    a = reject_all('Chapter_1_Redline_MINIMAL.docx')
    b = reject_all('Chapter_1_Redline_FULL.docx')
    # the banner text sits at the head of each redline and is not part of the draft
    def strip_banner(xs):
        for i, s in enumerate(xs):
            if s.startswith('1.1 Introduction'):
                return xs[i:]
        return xs
    a, b = strip_banner(a), strip_banner(b)
    assert a == b, f'redlines disagree: {len(a)} vs {len(b)} paragraphs'
    json.dump(a, open('original_draft_text.json', 'w'), ensure_ascii=False, indent=1)
    print(f'recovered {len(a)} paragraphs, identical from both redlines')
    print('first:', a[0][:70])
    print('last :', a[-1][:70])
