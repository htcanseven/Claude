"""Write the response to the panel with page and line numbers of the revised manuscript.

Reads response_to_panel.src.md, compiles a line-numbered copy of paper/main.tex (a single file with no supplementary
material) in a temporary directory and replaces every {{loc:phrase}} by "p. N, l. L" of the first place where the
phrase occurs in the compiled PDF, {{mainpages}} by the page on which the conclusions end and {{totalpages}} by the
page count. Writes response_to_panel.md and lists phrases that could not be found.

Usage: python paper/review/cfp_panel/resolve_locations.py
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parents[1]
SRC, OUT = HERE / "response_to_panel.src.md", HERE / "response_to_panel.md"
END_OF_CONCLUSIONS = "The released code, which reproduces every result"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)                     # LaTeX commands in a phrase
    return re.sub(r"[^0-9a-z]", "", s.lower())


def compile_numbered(tmp: Path) -> Path:
    for f in ["main.tex", "sn-jnl.cls", "sn-basic.bst", "refs.bib", "fig_procedure.tex", "main.bbl"]:
        shutil.copy(PAPER / f, tmp / f)
    shutil.copytree(PAPER / "figures", tmp / "figures")
    tex = (tmp / "main.tex").read_text()
    tex = re.sub(r"\\documentclass\[([^\]]*)\]\{sn-jnl\}",
                 lambda m: "\\documentclass[" + (m.group(1) if "lineno" in m.group(1) else m.group(1) + ",lineno") + "]{sn-jnl}",
                 tex, count=1)
    (tmp / "main.tex").write_text(tex)
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=tmp, capture_output=True)
    return tmp / "main.pdf"


def page_lines(pdf: Path) -> list[list[tuple[int, str]]]:
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                                        text=True).stdout).group(1))
    pages = []
    for p in range(1, n + 1):
        txt = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", str(pdf), "-"],
                             capture_output=True, text=True).stdout
        raw_lines = txt.splitlines()
        trail = re.compile(r"^(.*\S)\s{2,}(\d{1,4})\s*$")
        lead = re.compile(r"^\s*(\d{1,4})\s+(\S.*)$")
        # the class's line numbers stand right of the text on odd pages and left of it on even pages
        left = sum(bool(lead.match(r)) for r in raw_lines) > sum(bool(trail.match(r)) for r in raw_lines)
        lines, last, pending = [], 0, None
        for raw in raw_lines:
            if re.fullmatch(r"\s*\d{1,4}\s*", raw):          # a line number on a line of its own labels the next line
                pending = int(raw)
                continue
            m = (lead if left else trail).match(raw)
            if m:
                num, text = (m.group(1), m.group(2)) if left else (m.group(2), m.group(1))
                last = int(num)
            else:
                text, last = raw, (pending if pending is not None else last)
            pending = None
            if text.strip():
                lines.append((last, text))
        pages.append(lines)
    return pages


def locate(pages, phrase: str):
    key = norm(phrase)
    for p, lines in enumerate(pages, 1):
        joined, owner = "", []
        for num, text in lines:
            t = norm(text)
            joined += t
            owner += [num] * len(t)
        i = joined.find(key)
        if i >= 0:
            return p, owner[i]
    return None


def main() -> None:
    src = SRC.read_text()
    with tempfile.TemporaryDirectory() as d:
        pdf = compile_numbered(Path(d))
        pages = page_lines(pdf)
    total = len(pages)
    concl = locate(pages, END_OF_CONCLUSIONS)
    if concl is None:
        sys.exit(f"end of the conclusions not found: {END_OF_CONCLUSIONS!r}")
    main_pages = concl[0]
    missing = []

    def rep(m):
        hit = locate(pages, m.group(1))
        if hit is None:
            missing.append(m.group(1))
            return "(location not found)"
        return f"p. {hit[0]}, l. {hit[1]}"

    out = re.sub(r"\{\{loc:(.*?)\}\}", rep, src)
    unknown = re.findall(r"\{\{[^}]*\}\}", out.replace("{{mainpages}}", "").replace("{{totalpages}}", ""))
    missing += [f"unknown placeholder {x}" for x in unknown]
    out = out.replace("{{mainpages}}", str(main_pages)).replace("{{totalpages}}", str(total))
    OUT.write_text(out)
    print(f"{OUT.name}: {total} pages, main text {main_pages}")
    if missing:
        print("not found:\n  " + "\n  ".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
