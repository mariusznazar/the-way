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

Entries are written according to `template.md`; `examples.md` will hold verbatim copies of real
entries once this repository has a map of its own.

`skill/` holds `update-part-map`, a Claude Code skill that writes the entries of a product's map.
A product uses the skill from the commit of the-way it pins (WAY-34), linked into the product's
`.claude/skills/` from the pinned copy. For work on the-way itself, link its directory into the
user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\update-part-map" -Target "<the-way>\elements\part-map\skill"
```
