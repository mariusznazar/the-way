# Invariants

An invariant is a rule the product has to keep. Each invariant carries its method of checking
and the current result of running it (WAY-08), and names the environment facts it rests on
(WAY-17).

This description grows into the element's template as the element goes through its steps.

`format_guard.py` checks a product's invariants file against the list "What the format guard
checks" in `template.md`, reading from the template the fields of an entry and the words each may
hold, the fields the main branch holds `TODO` in, the lists that close the file, the values the
gate fills in and the words a sentence may not use. It reads the decision log, the part map and
the environment facts beside the file with their own guards' parsers, checks the rows naming an
invariant in `human_verdicts.md` beside it, scans the files git tracks for the `invariant:` and
`data:` lines of checks, and asks git which paths it ignores. From the product's repository root:

```
python <the-way>/elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl
python <the-way>/elements/invariants/format_guard.py foundations/invariants.md --base <commit> --record .runs/invariants-base.jsonl
python <the-way>/elements/invariants/format_guard.py foundations/invariants.md --merge-onto <commit> --record .runs/invariants-merge-onto.jsonl
```

`--base` names the commit the task branch left the main branch from; only with it are the
identifiers, versions, corrections and the list of violated invariants compared with that commit.
`--merge-onto` names the commit of the main branch a merge is made onto; only with it is a `TODO` in
a field other than *Method* and *Rests on* an error — in *Rests on* too, once the environment facts
that merge leaves have entries — and every fingerprint in *Derives from* and *Rests on* compared
with the current wording in the decision log and the environment facts that merge leaves (WAY-66,
WAY-71). `none` in place of either commit is what the gate fills in where that commit does not
exist: the checks that need it are recorded as `unchecked`, a note says so, and the run gives no
error; a commit that is not `none` and does not exist stays an error. `--record` names a JSON Lines
file in a folder git ignores, created or overwritten, which receives the-way's own record of the
run: a verdict for each invariant cited by a check the run's options select — the checks against
the base with `--base`, the checks of a merge with `--merge-onto`, the checks of the file alone
with neither — and a line for each failure that belongs to no invariant. The report for a person
holds every check, whichever options are given. Exit code: 0 without errors, 1 with errors, 2 when
the file or the template cannot be read or the record cannot be written.

What the script cannot see it reports as unchecked in the report for a person, never as agreement
(WAY-38): a declared correction, whose confirmation has no entry yet, so the person reads
"correction declared, confirmation not checked" while the record gives `invariant-version-changed`
its verdict on the sentence as written, `pass` where the correction names both fingerprints
(WAY-57); and whether a quarantine names the invariant of a flow that names it in prose. A call to
git that fails, the file standing outside a git repository included, is an error of the run. Its
tests, from the root of the-way:
`python -B gate/run_tests.py elements/invariants --record .runs/invariants-tests.jsonl`.

`skill/` holds `record-invariant`, a Claude Code skill that writes the entries of a product's
invariants file. A product uses the skill from the commit of the-way it pins (WAY-34), linked into
the product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its
directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-invariant" -Target "<the-way>\elements\invariants\skill"
```
