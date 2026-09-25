# Decisions

A decision is an active constraint, with its rationale and the options it rejected. Decisions
also carry what the product is for and who it is for, the principles for resolving trade-offs,
and what the product deliberately does not do.

Entries are written according to `template.md`; `examples.md` holds verbatim copies of real
entries.

`format_guard.py` checks a product's log against the list "What the format guard checks" in
`template.md`, reading the fields and kinds from the template. From the product's repository
root, with the commit the task branch left the main branch from:

```
python <the-way>/elements/decisions/format_guard.py --base <commit>
```

Without `--base`, the checks against that commit are skipped. Its tests, from the root of the-way:
`python -B gate/run_tests.py elements/decisions --record .runs/decisions-tests.jsonl`.

`skill/` holds `record-decision`, a Claude Code skill that turns a decision into an entry of a
product's log. A product uses the skill from the commit of the-way it pins (WAY-34), linked into
the product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its
directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-decision" -Target "<the-way>\elements\decisions\skill"
```
