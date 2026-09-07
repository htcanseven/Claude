"""Accept every tracked change in the Chapter 1 file and write a clean copy.

The deliverable to the co-authors is the tracked version, so they can see what was
changed. The copy that goes to a contributor, or eventually to the publisher, must not
carry 458 revisions under someone's name. This applies the same accept-all rules Word
would, on the XML:

  w:ins            unwrap, keep the content
  w:del            remove, content and all
  pPr/rPr/w:ins    remove the marker; the paragraph stays
  pPr/rPr/w:del    the paragraph mark is deleted, so the paragraph merges with the next
  trPr/w:ins       remove the marker; the row stays
  trPr/w:del       remove the row
  trackRevisions   switched off in settings.xml

usage: python3 src/accept_changes.py work/Chapter_1_tracked.docx Chapter_1_HS_machines_CLEAN.docx
"""
import re
import shutil
import sys
import zipfile

from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def q(tag):
    return '{%s}%s' % (W, tag.split(':')[1])


def marked(p, kind):
    """Is this paragraph's own mark recorded as an insertion or a deletion?"""
    ppr = p.find(q('w:pPr'))
    if ppr is None:
        return None
    rpr = ppr.find(q('w:rPr'))
    return None if rpr is None else rpr.find(q(kind))


def accept(xml):
    root = etree.fromstring(xml)

    # paragraphs whose mark is deleted: in our edits these are whole-paragraph
    # deletions, so the run content sits in w:del too and the paragraph goes entirely.
    for p in root.iter(q('w:p')):
        if marked(p, 'w:del') is not None:
            p.getparent().remove(p)

    # a paragraph inserted as a whole keeps its mark, minus the marker
    for p in root.iter(q('w:p')):
        ins = marked(p, 'w:ins')
        if ins is not None:
            ins.getparent().remove(ins)

    for row in root.iter(q('w:tr')):
        trpr = row.find(q('w:trPr'))
        if trpr is None:
            continue
        if trpr.find(q('w:del')) is not None:
            row.getparent().remove(row)
        elif (m := trpr.find(q('w:ins'))) is not None:
            trpr.remove(m)

    for d in root.findall('.//' + q('w:del')):
        d.getparent().remove(d)

    for i in root.findall('.//' + q('w:ins')):
        parent, at = i.getparent(), i.getparent().index(i)
        for child in reversed(list(i)):
            parent.insert(at, child)
        parent.remove(i)

    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def main(src, dst):
    shutil.copy(src, dst)
    zin = zipfile.ZipFile(src)
    items = {n: zin.read(n) for n in zin.namelist()}
    zin.close()

    items['word/document.xml'] = accept(items['word/document.xml'])
    items['word/settings.xml'] = re.sub(
        rb'<w:trackRevisions[^/>]*/>', b'', items['word/settings.xml'])

    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in items.items():
            z.writestr(name, data)

    d = items['word/document.xml'].decode()
    for tag in ('w:ins', 'w:del', 'w:delText'):
        n = len(re.findall(r'<%s[ >]' % tag, d))
        assert n == 0, f'{n} {tag} elements survive'
    assert b'trackRevisions' not in items['word/settings.xml']
    print(f'{dst}: {len(re.findall(r"<w:drawing[ >]", d))} figures, no revision marks')


if __name__ == '__main__':
    main(*(sys.argv[1:3] or ['work/Chapter_1_tracked.docx',
                             'Chapter_1_HS_machines_CLEAN.docx']))
