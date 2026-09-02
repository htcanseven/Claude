"""Render a .docx to PDF with LibreOffice and rasterise selected pages with PyMuPDF.

usage: python3 render_pages.py file.docx outdir [dpi]
Prints the page count and writes outdir/page-NN.png for every page.
"""
import sys, os, subprocess, glob
import fitz  # pymupdf

docx, outdir = sys.argv[1], sys.argv[2]
dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 80
os.makedirs(outdir, exist_ok=True)
sk = glob.glob('/root/.claude/skills/synced/*/docx/scripts/office/soffice.py')[0]
subprocess.run([sys.executable, sk, '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx],
               check=True, capture_output=True, timeout=600)
pdf = os.path.join(outdir, os.path.splitext(os.path.basename(docx))[0] + '.pdf')
doc = fitz.open(pdf)
print(f'{pdf}: {doc.page_count} pages')
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=dpi)
    pix.save(os.path.join(outdir, f'page-{i + 1:02d}.png'))
print('rendered', doc.page_count, 'pages to', outdir)
