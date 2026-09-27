# Environment facts

This element holds a product's environment facts: the platform, licences, law, browser
behaviour. Each fact has a method of checking it. A fact does not describe the behaviour of the
product itself — that is an invariant.

This description grows into the element's template as the element goes through its steps.

`format_guard.py` checks a product's environment facts file against the list "What the format
guard checks" in `template.md`, reading from the template the fields of an entry and the words each
may hold, the list of withdrawn identifiers, the file and row of human verdicts and the words
*Holds for* may not read. It reads the invariants, the part map and the decision log beside the
file with their own guards' parsers, checks the rows naming a fact in `human_verdicts.md` beside
it, scans the files git tracks for the `fact:` lines of checks, and asks git which paths it
ignores. From the product's repository root:

```
python <the-way>/elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl
python <the-way>/elements/environment-facts/format_guard.py foundations/environment_facts.md --base <commit> --record .runs/environment-facts-base.jsonl
python <the-way>/elements/environment-facts/format_guard.py foundations/environment_facts.md --merge-onto <commit> --record .runs/environment-facts-merge-onto.jsonl
```

`--base` names the commit the task branch left the main branch from; only with it are identifiers
and versions compared with that commit (WAY-75, WAY-79). `--merge-onto` names the commit of the
main branch a merge is made onto; only with it is a `TODO` outside *Method* an error, every
fingerprint a decision's *Based on* carries for a fact compared with the fact after that merge, and
a fact that no invariant's *Rests on* and no decision's *Based on* names an error rather than a
warning (WAY-71, WAY-88, WAY-90). `none` in place of either commit records the checks that need it
as `unchecked`; a commit that is not `none` and does not exist stays an error. `--record` names a
JSON Lines file in a folder git ignores, which receives a verdict for each invariant cited by a
check the run's options select, and a line for each failure that belongs to no invariant. Exit
code: 0 without errors, 1 with errors, 2 when the file or the template cannot be read or the record
cannot be written.

The guard checks the form of a source, not what it says (WAY-80), and reports a declared correction
as "correction declared, confirmation not checked", never as agreeing (WAY-79). A fact is named in
a decision's *Based on* as `<identifier>@<fingerprint>`; an identifier of the file standing there
as a word of its own, outside quoted text, an address or a path, is reported as a fact named
without its fingerprint, as is one written `<identifier>/<version>` or `<identifier>@` followed by
anything but hex digits. Its tests, from the root of the-way:
`python -B gate/run_tests.py elements/environment-facts --record .runs/environment-facts-tests.jsonl`.

`skill/` holds `record-environment-fact`, a Claude Code skill that writes the entries of a
product's environment facts file. A product uses the skill from the commit of the-way it pins
(WAY-34), linked into the product's `.claude/skills/` from the pinned copy. For work on the-way
itself, link its directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-environment-fact" -Target "<the-way>\elements\environment-facts\skill"
```
