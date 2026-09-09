import sys, zipfile, re, difflib
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def txt(p): return re.sub(r'\s+',' ',''.join(t.text or '' for t in p.iter(W+'t'))).strip()
def read(f):
    root=ET.fromstring(zipfile.ZipFile(f).read('word/document.xml'))
    out=[]
    for el in root.find(W+'body'):
        if el.tag==W+'p':
            s=txt(el)
            if s: out.append(s)
        elif el.tag==W+'tbl':
            for row in el.iter(W+'tr'):
                cells=[' '.join(filter(None,(txt(p) for p in c.iter(W+'p')))).strip() for c in row.findall(W+'tc')]
                line=' | '.join(x for x in cells if x)
                if line: out.append('ROW: '+line)
    return out

def worddiff(a, b):
    aw, bw = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, aw, bw, autojunk=False)
    frag=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal':
            seg = aw[i1:i2]
            if len(seg) > 8: frag.append('… ' + ' '.join(seg[:4]) + ' … ' + ' '.join(seg[-4:]) + ' …')
            else: frag.append(' '.join(seg))
        elif op=='delete': frag.append('[[-' + ' '.join(aw[i1:i2]) + '-]]')
        elif op=='insert': frag.append('[[+' + ' '.join(bw[j1:j2]) + '+]]')
        else: frag.append('[[-' + ' '.join(aw[i1:i2]) + '-]][[+' + ' '.join(bw[j1:j2]) + '+]]')
    return ' '.join(frag)

a,b = read(sys.argv[1]), read(sys.argv[2])
print(f'old {len(a)} paragraphs, new {len(b)}\n')
n=0
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op=='equal': continue
    old, new = a[i1:i2], b[j1:j2]
    used=set()
    for o in old:
        best, bi = 0.0, None
        for k,x in enumerate(new):
            if k in used: continue
            r = difflib.SequenceMatcher(None,o,x).quick_ratio()
            if r>best: best, bi = r, k
        if bi is not None and best>0.55:
            used.add(bi); n+=1
            print(f'--- [{n}] edited'); print('   ', worddiff(o,new[bi])); print()
        else:
            n+=1; print(f'--- [{n}] DELETED'); print('   ', o[:400]); print()
    for k,x in enumerate(new):
        if k not in used:
            n+=1; print(f'--- [{n}] ADDED'); print('   ', x[:400]); print()
