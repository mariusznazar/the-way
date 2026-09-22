# Invariants

An invariant is a rule the product has to keep. Each invariant carries its method of checking
and the current result of running it (WAY-08), and names the environment facts it rests on
(WAY-17).

This description grows into the element's template as the element goes through its steps.

`format_guard.py` checks a product's invariants file against the list "What the format guard
checks" in `template.md`, reading from the template the fields of an entry and the words each may
hold, the lists that close the file, the values the gate fills in and the words a sentence may not
use. It reads the decision log and the part map beside the file with their own guards' parsers,
and scans the files git tracks for the `invariant:` and `data:` lines of checks. From the
product's repository root, with the commit the task branch left the main branch from:

```
python <the-way>/elements/invariants/format_guard.py --base <commit>
```

Without `--base`, the identifiers, versions, corrections and the list of violated invariants are
not compared with that commit, and the guard reports them as unchecked, never as agreement
(WAY-38); so is a declared correction, whose confirmation has no home yet (WAY-57). In a repository
with no main branch there is no such commit, so these comparisons do not run at all. Its tests:
`python -B -m unittest discover -s elements/invariants -p "test_*.py"`.

`skill/` holds `record-invariant`, a Claude Code skill that writes the entries of a product's
invariants file. A product uses the skill from the commit of the-way it pins (WAY-34), linked into
the product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its
directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-invariant" -Target "<the-way>\elements\invariants\skill"
```
