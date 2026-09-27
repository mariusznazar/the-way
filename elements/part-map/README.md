# Part map

The part map holds the parts of a product and what joins them: which part may depend on which,
which flows run across several parts, and what crosses the edge to the world outside. It says
what is allowed, not what the code happens to contain today — what the code contains is computed
from it and checked against the map.

Each part carries its responsibility, a rule for assigning files to it, the dependencies it is
allowed, the failure modes it can suffer — from which its criticality is computed — and the
files where it takes in what it does not trust. Beside the parts stand the critical flows, the
external context, and the surfaces someone outside the product relies on, with one path of
change for each level of promise.

Entries are written according to `template.md`; `examples.md` holds verbatim copies of entries
from this repository's own map, `foundations/part_map.md`.

`format_guard.py` checks a product's map against the list "What the format guard checks" in
`template.md`, reading from the template the fields of each kind of entry, the titles of the lists
and the values their columns allow. Files are matched to parts by git itself, through the patterns a
part records. From the product's repository root:

```
python <the-way>/elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl
python <the-way>/elements/part-map/format_guard.py foundations/part_map.md --base <commit> --record .runs/part-map-base.jsonl
```

`--base` names the commit the task branch left the main branch from; only with it is the list of
known violations compared with the one on that commit. `none` in place of that commit is what the
gate fills in where it does not exist: the check that needs it is recorded as `unchecked`, a note
says so, and the run gives no error; a commit that is not `none` and does not exist stays an error.
`--record` names a JSON Lines file in a folder git ignores, created or overwritten, which receives
the-way's own record of the run: a verdict for each invariant cited by a check the run's options
select — the check against the base with `--base`, the checks of the map alone without it — and a
line for each failure that belongs to no invariant. The report for a person holds every check,
whichever options are given. A `TODO` in any field of an entry is an error on every run, since the
template gives `TODO` to no field. Exit code: 0 without errors, 1 with errors, 2 when the map or the
template cannot be read or the record cannot be written.

What the script cannot see it reports as unchecked, never as agreement (WAY-38): a flow whose
test leaves no coverage file, the promise levels declared in the code, and new or stale
violations, which wait for the command a product declares for its dependency graph. A call to git
that fails, the map standing outside a git repository included, is an error of the run. Its tests,
from the root of the-way: `python -B gate/run_tests.py elements/part-map --record
.runs/part-map-tests.jsonl`.

`skill/` holds `update-part-map`, a Claude Code skill that writes the entries of a product's map.
A product uses the skill from the commit of the-way it pins (WAY-34), linked into the product's
`.claude/skills/` from the pinned copy. For work on the-way itself, link its directory into the
user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\update-part-map" -Target "<the-way>\elements\part-map\skill"
```
