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

`format_guard.py` checks a product's map against the list "What the checker checks" in
`template.md`, reading from the template the fields of each kind of entry, the titles of the
lists and the values their columns allow. Files are matched to parts by git itself, through the
patterns a part records. From the product's repository root, in CI with its main branch:

```
python <the-way>/elements/part-map/format_guard.py --base origin/main
```

Without `--base`, the list of known violations is not compared with the one on the main branch.
What the script cannot see it reports as unchecked, never as agreement (WAY-38): a flow whose
test leaves no coverage file, the change path of a promise level declared in the code, and new
or stale violations, which wait for the command a product declares for its dependency graph. Its
tests: `python -B -m unittest discover -s elements/part-map -p "test_*.py"`.

`skill/` holds `update-part-map`, a Claude Code skill that writes the entries of a product's map.
A product uses the skill from the commit of the-way it pins (WAY-34), linked into the product's
`.claude/skills/` from the pinned copy. For work on the-way itself, link its directory into the
user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\update-part-map" -Target "<the-way>\elements\part-map\skill"
```
