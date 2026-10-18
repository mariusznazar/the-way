# Foundation selection — foundation step, turn 1

Method: "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150).

## Revision

- Foundation read at `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` (`foundations` tip = task base), worktree
  `C:/Storage/repos/the-way-wt/agent-path-technology-step`, branch `task/agent-path-technology-step`.

## Touched parts

- `project-level` — the later code (definition template's Technology section, `settle-technology` skill)
  and the subject of WAY-121/122/123/165/166 (Scope `project-level, decisions`).
- `decisions` — `foundations/decisions.md` collects entries; by WAY-44 the parts a change touches follow
  from the entries it changes: WAY-121, WAY-122, WAY-123 (Scope `project-level, decisions`) and the new
  WAY-165/166 (same Scope).
- `invariants` file entry changed: `project-technology-record/1` (Part `project-level`; only its
  *Derives from* fingerprint renews).
- No prospective new part. Trust-boundary file `project-level/readiness_check.py` is not to change.

## Expected current *Scope* matches

Exhaustive scan of every current decision's *Scope* (wrapped values joined; 150 numbers, latest
version each, no repeals present) for `project-level` or `decisions`, by a throw-away script over
`foundations/decisions.md`. Matches (number — line at base):

WAY-01 (6), 02 (38), 04 (95), 05 (137), 07 (176), 09 (234), 10 (305), 11 (343), 12 (384), 14 (459),
17 (507), 18 (531), 19 (563), 20 (596), 21 (623), 22 (645), 24 (673), 25 (708), 26 (737), 27 (763),
28 (794), 29 (826), 30 (857), 31 (891), 32 (926), 33 (952), 34 (983), 35 (1012), 36 (1046), 37 (1075),
38 (1102), 52 (1464), 53 (1490), 54 (1513), 55 (1546), 60 (1697), 61 (1733), 65 (1895), 69 (1960),
71 (1996), 72 (2034), 73 (2060), 74 (2093), 84 (2377), 85 (2410), 86 (2442), 89 (2476), 90 (2505),
95 (2606), 97 (2686), 98 (2722), 99 (2756), 100 (2788), 101 (2814), 102 (2837), 103 (2864), 104 (2889),
106 (2992), 107 (3018), 108 (3044), 109 (3075), 110 (3098), 111 (3122), 112 (3151), 113 (3181),
114 (3217), 115 (3246), 116 (3277), 117 (3305), 118 (3334), 119 (3368), 120 (3395), 121 (3427),
122 (3464), 123 (3523), 124 (3562), 126 (3674), 127 (3721), 134 (3993), 137 (4172), 138 (4212),
139 (4262), 140 (4301), 142 (4380), 143 (4432), 144 (4470), 145 (4507), 146 (4553), 147 (4593),
150 (4712), 151 (4750), 152 (4787), 153 (4818), 154 (4860), 155 (4898), 156 (4933).

## Explicitly named by the task (*Decisions in play*)

WAY-121, 122, 123, 137, 138, 139, 140, 143, 100, 106, 04; invariant `project-technology-record`;
glossary term `surface`. All are inside the Scope set above except none (all matched), so no missing
match.

## Read whole vs discovered

- Read whole (all fields, *Rationale*, *Rejected*): WAY-01 to 05, 07 to 14, 16 to 22, 24 to 38,
  48, 49, 51 to 55, 60, 61 (first part through *Verification*), 65, 68, 69, 71 to 74, 84 to 86, 89, 90,
  95 to 156 (WAY-141 included), 164.
- Discovered by Scope and located, read through binding sentences and fields only: WAY-61 (remainder
  of *Rationale*), WAY-93 (glossary-only questions; not touched by the work).
- Invariants read whole: `project-technology-record`, `project-definition-form`,
  `project-readiness-gate`, `project-plan-form`, `project-plan-check`, `project-plan-state-evidence`,
  `project-plan-state-subprocesses`, `skill-entry-points`, `instruction-file-imports`,
  `root-claude-md-import`, `installation-claude-guidance`, `decision-guard-stale-reference`,
  `decision-fingerprint-input`, `log-reference-target`. The 45 invariants with Part `every` were
  inspected by identifier and *Derives from*; none derives from WAY-121/122/123/137/138/139.
- Incoming dependents of WAY-121 (`740c254e` at base): WAY-122, WAY-123 and invariant
  `project-technology-record/1` — the only three links (grep of the whole repository outside `.runs/`).
  Dependents of WAY-123 (`f3b45293`): WAY-137 (narrows), WAY-138 — unchanged binding, no renewal.
- Part map: read whole (`foundations/part_map.md`), including the `project-level` failure modes and
  trust boundary.
- Glossary: read whole (`foundations/glossary.md`, 31 terms); terms that matter: `surface` (not used
  for the interface), `preparatory task` (uses "running product" plainly), `part`, `result`, `entry`,
  `human action`.
- Environment facts: searched (see author report), no relevant entry; none named by a selected
  decision's *Based on* bears on the work.
- Templates, rules, examples read whole: `elements/decisions/template.md`, `elements/common/rules.md`,
  `elements/common/way_of_working.md`, `elements/decisions/examples.md` (WAY-03, read).

## Recheck

Selection made once at `77c8a8b`; the foundation did not change during the step. The second search
against the integration tip is a later cycle stage.
