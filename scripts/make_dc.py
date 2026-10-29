"""Derive the double-column manuscript (paper/main_dc.tex, Elsevier CAS class cas-dc) from the single-column
review manuscript paper/main.tex. The body text, tables and figures are carried over verbatim; only the preamble
and the front matter are rewritten for the CAS class, the CRediT statement is printed by the class, and the
floats that are wider than one column (listed in WIDE) are set across both columns.

    python3 scripts/make_dc.py           # writes paper/main_dc.tex
"""
import re
import sys
from pathlib import Path

MAIN = Path("paper/main.tex")
OUT = Path("paper/main_dc.tex")
HIGHLIGHTS = Path("paper/highlights.tex")

# Floats set across both columns (label -> True). Everything else stays within one column.
WIDE = {"tab:positioning", "fig:method", "tab:alternatives", "fig:alternatives", "tab:suitedef", "fig:features",
        "fig:pairs", "tab:suites", "tab:decision", "tab:cells", "tab:envelope", "tab:conventions", "fig:pod",
        "fig:faults", "tab:mde", "tab:transfer"}
# Overrides from the command line: --narrow fig:faults,tab:mde  --wide ...
args = sys.argv[1:]
for flag, action in (("--narrow", WIDE.discard), ("--wide", WIDE.add)):
    if flag in args:
        for lab in args[args.index(flag) + 1].split(","):
            action(lab)

PREAMBLE = r"""%% Mechanical Systems and Signal Processing -- Elsevier CAS double-column class (els-cas-templates on CTAN),
%% numbered references. Derived from main.tex by scripts/make_dc.py; edit main.tex, not this file.
\documentclass[a4paper,fleqn]{cas-dc}

\usepackage[numbers,sort&compress]{natbib}
\usepackage{threeparttable}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,decorations.pathreplacing,decorations.pathmorphing}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black,
            pdftitle={__TITLE__},
            pdfauthor={Hüseyin Tayyer Canseven}}
\usepackage{xurl}      % URLs and DOIs may break at any character (loaded after hyperref)
\urlstyle{same}
\graphicspath{{figures/}}

%% References print the DOI as a resolvable link (Elsevier style) instead of the bst's `doi:' prefix.
\providecommand{\DOIprefix}{}
\newcommand{\doi}[1]{\href{https://doi.org/#1}{\nolinkurl{https://doi.org/#1}}}

%% Float placement: allow figures and tables to share pages with text and with each other.
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.7}
\renewcommand{\textfraction}{0.07}
\renewcommand{\floatpagefraction}{0.8}
\renewcommand{\dbltopfraction}{0.9}
\renewcommand{\dblfloatpagefraction}{0.8}
\setcounter{topnumber}{3}
\setcounter{dbltopnumber}{3}
\setcounter{totalnumber}{4}
%% Table body size (the class sets captions and references at 8 pt).
\newcommand{\tabsize}{\fontsize{8}{10}\selectfont}
%% Reference list at the class's 8 pt on a slightly tighter leading (the class sets 8/10 at begin-document).
\AtBeginDocument{\gdef\bibfont{\fontsize{8}{9.5}\selectfont}}
\setlength{\emergencystretch}{1.5em}
%% The class prints an `ORCID(s):' footnote even when no ORCID is given; none is given here.
\makeatletter
\AtBeginDocument{\RenewDocumentCommand\printorcid{}{}}
\makeatother

\begin{document}
\let\WriteBookmarks\relax
\shorttitle{A signal-to-drift ratio for winding-fault detectability and sensor selection}
\shortauthors{H.~T. Canseven}

\title[mode=title]{__TITLE__}

\author[1]{H\"useyin Tayyer Canseven}
\ead{huseyin.canseven@lut.fi}
\credit{__CREDIT__}
\affiliation[1]{organization={Department of Electrical Engineering, LUT School of Energy Systems, LUT University},
                city={Lappeenranta},
                postcode={53850},
                country={Finland}}

__ABSTRACT__

\begin{highlights}
__HIGHLIGHTS__
\end{highlights}

\begin{keywords}
__KEYWORDS__
\end{keywords}

\maketitle
"""


def between(text, start, end):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j + len(end)]


def main():
    src = MAIN.read_text()
    title = re.search(r"\\title\{(.+?)\}\n", src).group(1)
    abstract = between(src, "\\begin{abstract}", "\\end{abstract}")
    keywords = between(src, "\\begin{keyword}", "\\end{keyword}")
    keywords = keywords.replace("\\begin{keyword}\n", "").replace("\n\\end{keyword}", "").strip()
    credit = re.search(r"\\section\*\{CRediT authorship contribution statement\}\n\\textbf\{[^}]+\}\s*(.+?)\.\n", src).group(1)
    hl = HIGHLIGHTS.read_text()
    items = re.findall(r"^\s*\\item (.+)$", hl, flags=re.M)
    highlights = "\n".join(f"\\item {it.strip()}" for it in items)

    pre = (PREAMBLE.replace("__TITLE__", title).replace("__ABSTRACT__", abstract).replace("__KEYWORDS__", keywords)
           .replace("__CREDIT__", credit).replace("__HIGHLIGHTS__", highlights))

    # Body: from the first section to the CRediT statement; declarations after the CRediT statement.
    body_start = src.index("\\section{Introduction}")
    credit_start = src.index("\\section*{CRediT")
    decl_start = src.index("\\section*{", credit_start + 10)
    bib_start = src.index("\\bibliographystyle")
    body = src[body_start:credit_start]
    decl = src[decl_start:bib_start]

    # Star the wide floats.
    def star(m):
        block = m.group(0)
        kind = m.group(1)
        lab = re.search(r"\\label\{((?:tab|fig):[^}]+)\}", block)
        if lab and lab.group(1) in WIDE:
            block = block.replace(f"\\begin{{{kind}}}[htbp]", f"\\begin{{{kind}*}}[htbp]", 1)
            block = block.replace(f"\\end{{{kind}}}", f"\\end{{{kind}*}}", 1)
        else:
            block = block.replace("width=\\textwidth", "width=\\columnwidth")
        # The CAS class sets every table caption at the float's full width; inside a threeparttable, whose
        # width is the tabular's, that produces a spurious overfull box, so the caption moves above it.
        cap = re.search(r"\\caption\{.*\}\\label\{tab:[^}]+\}\n", block)
        if cap and "\\begin{threeparttable}" in block:
            block = block.replace(cap.group(0), "")
            block = block.replace("\\begin{threeparttable}\n", cap.group(0) + "\\begin{threeparttable}\n", 1)
        return block
    body = re.sub(r"\\begin\{(figure|table)\}\[htbp\].*?\\end\{\1\}", star, body, flags=re.S)

    out = (pre + "\n" + body.rstrip() + "\n\n\\printcredits\n\n" + decl.rstrip() + "\n\n"
           + "\\bibliographystyle{elsarticle-num-names}\n\\bibliography{refs}\n\n\\end{document}\n")
    OUT.write_text(out)
    n_star = out.count("\\begin{table*}") + out.count("\\begin{figure*}")
    print(f"wrote {OUT}: {n_star} two-column floats, {len(items)} highlights")


if __name__ == "__main__":
    main()
