"""Produce the version of the annotated table of contents that goes to contributors.

The working copy carries a Status column ("expected", "suggested", "to be invited")
that records where each approach stands. That is internal: nobody should learn from an
attachment that a colleague is still a maybe. This strips it, and softens the header
line that marks the document as an internal draft.

Names are kept. Listing proposed contributors is normal in a book proposal; it is only
the state of each conversation that has to stay in-house.

usage: python3 src/make_circulation_toc.py
"""
import re

SRC = 'Annotated_TOC.md'
OUT = 'Annotated_TOC_for_contributors.md'


def strip_status_column(text):
    """Drop the last column from the contributor table only."""
    lines = text.split('\n')
    out, in_table = [], False
    for line in lines:
        if line.startswith('| Contributor | Affiliation |'):
            in_table = True
        elif in_table and not line.startswith('|'):
            in_table = False
        if in_table and line.startswith('|'):
            cells = line.split('|')
            # cells[0] and cells[-1] are the empty strings outside the outer pipes
            line = '|'.join(cells[:-2]) + '|'
        out.append(line)
    return '\n'.join(out)


def main():
    t = open(SRC, encoding='utf-8').read()
    t = strip_status_column(t)
    t = t.replace(
        '**Annotated table of contents for the Wiley proposal** — draft for discussion among the authors',
        '**Annotated table of contents for the Wiley proposal**')
    # the alternative-title deliberation is an authors' matter
    t = re.sub(r'^Alternative titles for discussion:.*\n\n', '', t, flags=re.M)
    open(OUT, 'w', encoding='utf-8').write(t)

    # The check is on the contributor table only. Chapter abstracts may honestly say that
    # a role is still open ("an aerospace contributor to be invited"); what must not
    # survive is a named person carried with the state of their conversation.
    rows = [r for r in t.split('\n') if r.startswith('| ') and r.count('|') > 2]
    table = [r for r in rows if re.match(r'^\| [A-Z][a-zé]+ ', r) and 'Chapters' not in r]
    for r in table:
        for status in ('agreed in principle', 'to be invited', 'suggested', 'expected',
                       'to be named', 'open'):
            assert status not in r, f'status {status!r} survives in: {r}'
    assert table, 'contributor table not found'
    print(f'wrote {OUT}: contributor table carries {len(table)} names, no Status column')


if __name__ == '__main__':
    main()
