"""Build candidate references from the Crossref REST API.

Every entry comes back from Crossref with a real DOI; nothing is written from
memory. Results are filtered to journals that matter for this paper's audience
and deduplicated against the existing refs.bib.
"""
from __future__ import annotations
import json, re, sys, time, urllib.parse, urllib.request

MAILTO = "research@example.org"          # polite-pool identifier only
BASE = "https://api.crossref.org/works"

# venue -> weight. Anything not listed is kept only if the query is niche.
PREFERRED = [
    "measurement", "mechanical systems and signal processing",
    "ieee transactions on instrumentation and measurement",
    "ieee transactions on industrial electronics",
    "ieee transactions on industrial informatics",
    "measurement science and technology", "isa transactions",
    "ieee sensors journal", "sensors", "expert systems with applications",
    "reliability engineering", "ieee access", "metrology and measurement systems",
    "structural health monitoring", "journal of sound and vibration",
    "applied acoustics", "engineering applications of artificial intelligence",
    "ieee transactions on energy conversion", "ieee industrial electronics magazine",
    "measurement: sensors", "nature machine intelligence", "patterns",
    "ieee instrumentation & measurement magazine", "advanced engineering informatics",
]

QUERIES = [
    ("cm_induction",  "vibration condition monitoring induction motor fault diagnosis", 2020),
    ("cm_bearing",    "rolling element bearing fault diagnosis vibration signal", 2021),
    ("mems_metrology","MEMS accelerometer calibration metrological characterization uncertainty", 2019),
    ("mems_lowcost",  "low-cost MEMS accelerometer vibration measurement machine monitoring", 2021),
    ("smartphone",    "smartphone accelerometer vibration measurement machinery", 2019),
    ("leakage",       "data leakage machine learning evaluation generalization pitfalls", 2020),
    ("cv_eval",       "cross-validation bias model selection performance estimation", 2019),
    ("domain_shift",  "domain shift working condition transfer fault diagnosis bearing", 2021),
    ("iot_edge",      "industrial internet of things edge computing machine condition monitoring", 2021),
    ("tinyml",        "TinyML microcontroller embedded machine learning inference sensor", 2021),
    ("uncertainty",   "measurement uncertainty evaluation GUM Type A Type B instrumentation", 2018),
    ("wireless",      "wireless sensor node vibration monitoring LoRa energy consumption", 2020),
    ("benchmark",     "public bearing dataset benchmark evaluation fault diagnosis comparison", 2021),
    ("sampling",      "sampling rate downsampling aliasing vibration diagnosis feature", 2019),
]


def fetch(query, from_year, rows=40):
    params = {
        "query.bibliographic": query,
        "filter": f"from-pub-date:{from_year}-01-01,type:journal-article",
        "rows": str(rows),
        "select": "DOI,title,container-title,issued,author,volume,issue,page,ISSN",
        "sort": "relevance",
        "mailto": MAILTO,
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": f"refs-builder (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())["message"]["items"]


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def main():
    existing = set()
    try:
        bib = open("../paper/refs.bib").read()
        existing = {d.lower() for d in re.findall(r"DOI=\{([^}]+)\}", bib)}
        existing |= {d.lower() for d in re.findall(r"doi\s*=\s*\{([^}]+)\}", bib, re.I)}
    except FileNotFoundError:
        pass
    print(f"{len(existing)} DOIs already cited")

    out, seen = {}, set(existing)
    for tag, q, yr in QUERIES:
        try:
            items = fetch(q, yr)
        except Exception as e:
            print(f"  {tag}: FAILED {e}"); continue
        keep = []
        for it in items:
            doi = norm(it.get("DOI"))
            ct = norm((it.get("container-title") or [""])[0])
            if not doi or doi in seen:
                continue
            if not any(p in ct for p in PREFERRED):
                continue
            title = (it.get("title") or [""])[0]
            if not title or len(title) < 12:
                continue
            seen.add(doi)
            keep.append(dict(doi=it["DOI"], title=title,
                             journal=(it.get("container-title") or [""])[0],
                             year=(it.get("issued", {}).get("date-parts", [[None]])[0][0]),
                             volume=it.get("volume"), page=it.get("page"),
                             authors=[f"{a.get('family','')}, {a.get('given','')}"
                                      for a in it.get("author", [])[:8] if a.get("family")]))
        out[tag] = keep
        print(f"  {tag}: {len(keep)} candidates")
        time.sleep(1)
    json.dump(out, open("../results/ref_candidates.json", "w"), indent=2)
    total = sum(len(v) for v in out.values())
    print(f"total {total} candidate references")


if __name__ == "__main__":
    main()
