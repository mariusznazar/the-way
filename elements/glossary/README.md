# Glossary

The glossary gives the words a product's rules stand on one meaning each, where they need one, so
that the same word does not mean one thing in a decision, another in an invariant and a third in the code. The glossary of
the-way holds the words of the process; a product's glossary holds the words of its domain and takes
the words of the process from the-way at the commit it pins (WAY-92).

An entry holds its term, one definition and two fields: *Avoid*, other words for what the term names,
and *Not*, other meanings the word carries in the foundation (WAY-94). Nothing cites a term by an
identifier or a fingerprint: a sentence depends on a term by using its word (WAY-94), and a changed
definition goes through a review of the term's uses (WAY-97).

`template.md` holds the rules of an entry. `format_guard.py` checks a glossary against them, from
the root of the product's repository:

```
python -B <the-way>/elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl
python -B <the-way>/elements/glossary/format_guard.py foundations/glossary.md --base <fork-point> --record .runs/glossary-base.jsonl
python -B <the-way>/elements/glossary/format_guard.py foundations/glossary.md --merge-onto <main> --record .runs/glossary-merge-onto.jsonl
python -B <the-way>/elements/glossary/format_guard.py foundations/glossary.md --uses <word>
```

The first three are the runs the *Method* of the glossary's invariants names: the file alone, the
file against the commit the branch left the main branch from, and the file as a merge onto the main
branch leaves it. The last lists the uses of a word, as the template's section on uses bounds them,
and checks nothing.

`skill/` holds `record-glossary-term`, a Claude Code skill that writes the entries of a product's
glossary. A product uses the skill from the commit of the-way it pins (WAY-34), linked into the
product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its directory into
the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-glossary-term" -Target "<the-way>\elements\glossary\skill"
```
