"""Fetch authoritative BibTeX for the selected DOIs via Crossref content
negotiation, so author lists, volumes and pages come from the registry rather
than being retyped. Selection was made by reading the candidate titles."""
from __future__ import annotations
import json, re, time, urllib.request, unicodedata

SELECT = [
    # MEMS metrology: what a real metrological characterisation delivers
    ("mems_metrology", 4), ("mems_metrology", 6), ("mems_metrology", 7),
    ("mems_metrology", 8), ("mems_metrology", 0), ("mems_metrology", 2),
    # low-cost MEMS as vibration instruments (mounting, cross-sensitivity)
    ("mems_lowcost", 3), ("mems_lowcost", 13), ("mems_lowcost", 6), ("mems_lowcost", 2),
    # smartphone sensing
    ("smartphone", 2), ("smartphone", 1), ("smartphone", 11), ("smartphone", 13), ("smartphone", 5),
    # induction machine / bearing condition monitoring
    ("cm_induction", 4), ("cm_induction", 0), ("cm_induction", 2), ("cm_induction", 1),
    ("cm_bearing", 0), ("cm_bearing", 2),
    # evaluation methodology, leakage, selection bias, benchmark critique
    ("leakage", 1), ("leakage", 2), ("cv_eval", 2), ("cv_eval", 0), ("benchmark", 0),
    # operating-condition shift
    ("domain_shift", 1), ("domain_shift", 10), ("domain_shift", 13), ("domain_shift", 4),
    # IoT / edge / TinyML / wireless nodes
    ("iot_edge", 0), ("tinyml", 10), ("tinyml", 1), ("wireless", 1), ("wireless", 5),
    # uncertainty and GUM practice
    ("uncertainty", 3), ("uncertainty", 4), ("uncertainty", 1), ("uncertainty", 8), ("uncertainty", 10),
    # sampling / decimation
    ("sampling", 0),
]


def bibtex_for(doi):
    req = urllib.request.Request(
        "https://doi.org/" + doi,
        headers={"Accept": "application/x-bibtex; charset=utf-8",
                 "User-Agent": "refs-builder (mailto:research@example.org)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def latexify(s):
    """Replace non-ASCII with LaTeX escapes so 8-bit BibTeX cannot mangle them."""
    repl = {"–": "--", "—": "---", "’": "'", "‘": "'", "“": "``", "”": "''",
            "é": r"{\'e}", "è": r"{\`e}", "ü": r'{\"u}', "ö": r'{\"o}', "ä": r'{\"a}',
            "ç": r"{\c{c}}", "ñ": r"{\~n}", "á": r"{\'a}", "í": r"{\'i}", "ó": r"{\'o}",
            "ú": r"{\'u}", "Á": r"{\'A}", "É": r"{\'E}", "ø": r"{\o}", "å": r"{\aa}",
            "ł": r"{\l}", "ś": r"{\'s}", "ż": r"{\.z}", "ź": r"{\'z}", "č": r"{\v{c}}",
            "š": r"{\v{s}}", "ž": r"{\v{z}}", "ğ": r"{\u{g}}", "ı": r"{\i}",
            "Ş": r"{\c{S}}", "ş": r"{\c{s}}", "İ": r"{\.I}", "°": r"$^\circ$",
            "×": r"$\times$", "≈": r"$\approx$", " ": " ", "&": r"\&",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    # anything still non-ASCII: strip accents, else drop
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        else:
            d = unicodedata.normalize("NFKD", ch)
            out.append("".join(c for c in d if ord(c) < 128))
    return "".join(out)


def main():
    cand = json.load(open("../results/ref_candidates.json"))
    entries, meta = [], []
    for tag, i in SELECT:
        try:
            it = cand[tag][i]
        except (KeyError, IndexError):
            print(f"  !! missing {tag}:{i}"); continue
        doi = it["doi"]
        try:
            bt = bibtex_for(doi)
        except Exception as e:
            print(f"  !! {doi}: {e}"); continue
        # rewrite the citation key to something readable and stable
        first = (it["authors"][0].split(",")[0] if it["authors"] else "anon").lower()
        first = re.sub(r"[^a-z]", "", first) or "anon"
        key = f"{first}{it['year']}{tag.split('_')[0]}"
        n, k = 2, key
        while any(f"@{'{'}{k}," in e or ("{" + k + ",") in e for e in entries):
            k = f"{key}{n}"; n += 1
        bt = re.sub(r"^@(\w+)\{[^,]+,", lambda m: f"@{m.group(1)}{{{k},", bt.strip(), count=1)
        entries.append(latexify(bt))
        meta.append(dict(key=k, doi=doi, tag=tag, title=it["title"],
                         journal=it["journal"], year=it["year"]))
        print(f"  ok {k:28s} {it['year']} {it['journal'][:34]}")
        time.sleep(0.6)
    open("../results/new_refs.bib", "w").write("\n\n".join(entries) + "\n")
    json.dump(meta, open("../results/new_refs.json", "w"), indent=2)
    print(f"\nwrote {len(entries)} entries to results/new_refs.bib")


if __name__ == "__main__":
    main()
