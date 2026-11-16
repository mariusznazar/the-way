# Return step — readiness-approval-rename

**Status:** done. **Commits:** none (the comparison found nothing that no longer matches).

## Foundation compared with code

Head `cef14df7`. Compared: the decisions the change edits (WAY-27, WAY-107, WAY-114, WAY-118, WAY-121, WAY-126, WAY-140,
WAY-145, WAY-227, WAY-280, WAY-320, WAY-330, WAY-344 and the decisions whose text the old words stood in), the invariant
`project-readiness-check` and its neighbour `project-definition-form`, the glossary entries `gate` and `projected entry`,
the part map, and the files of the directories the task lists, with the scripts and tests.

- **Old names** (`readiness gate`, `gate record`, `ready for gate`, `project-readiness-gate`, `readiness_gate`, also across a
  line break) searched in every tracked file but the generated entry points: the only hits are `foundations/decisions.md:8366`
  ("the script that runs the gate records", the test command split by a line break, WAY-350) and the two new tests of the old
  heading and the old status in `project-level/test_readiness_check.py`, which hold the old words as input. The entry points
  under `.claude/skills/` and `.agents/skills/` equal what `skill_entry_points.py --write` writes (the entry-point test is in
  the `agent-instructions` run of the fix).
- **`entry` in the locations-file or backlog-line meaning**: searched `foundations/`, `elements/`, `project-level/`,
  `task-cycle/`, `process-audit/`, `foundation-review/`, `guidelines/`, `product-guidelines/`, `installation/`,
  `instruction-files/`, `agent-instructions/`, `AGENTS.md`, `README.md`: none left; what stays is the foundation entry, the
  record's entries (list items) and the Python names `entry_path`, `REGISTER_ENTRY`, `RESULTS_ENTRY`, `REPOSITORY_ENTRY`, and
  the local `entries` of `entry_path`.
- **Part map** (`foundations/part_map.md`): names no file renamed (no `readiness_gate.md`); the `project-level` responsibility
  says "its readiness approval"; the trust-boundary table says "the places its keys name" and "the registry of running gates"
  (the test command). Nothing to change.
- **WAY-342**: confirmed. It stands only as the row `| WAY-342 | its rule, the answer to "Which keys of the locations file does
  the audit of the process read?" …` under `## Withdrawn identifiers` (decisions.md:11188), which reads "keys". The decision
  `### WAY-376` holds no use of `entry` in that meaning or of `gate` (the task's phrase "cited in WAY-376" does not match the
  file: the row is in the table of withdrawn identifiers, not under WAY-376; nothing to change).
- **Entries written or changed carry no history**: no "formerly" or date of an event in `gate`, `projected entry`, the changed
  sentences of WAY-27, 107, 118, 126, 140, 320, 330. The old words stand only in the two tests as input data.

## Decisions written or changed

none by this step (the change's decisions were edited in the change itself: WAY-27, WAY-107, WAY-114, WAY-118, WAY-121,
WAY-126, WAY-140, WAY-145, WAY-227, WAY-280, WAY-320, WAY-330, WAY-344, the row WAY-342, and every decision holding the old
words, with no change of meaning).

## Invariants

none written. `project-readiness-gate` is `project-readiness-check` (heading, WAY-118's *Verification*, every `invariant:` line);
the two new tests cite `project-definition-form`, which holds their rule.

## Environment facts

none.

## Glossary terms

`gate` (Not: the human's approval of a project definition — "readiness approval") and `projected entry` (new), written in the
change; no further term. `entry` unchanged, `read off` unchanged.

## Part-map changes

none.

## Projected entries written whole or in part

none (the task's sources hold no projected entry).

## Rows of *Settlements to record*

1. glossary term — entry `gate`, field *Not*, `foundations/glossary.md`.
2. glossary term — new entry `projected entry`, `foundations/glossary.md`.
3. data or code — `project-level/definition_template.md` (status table, form) and `project-level/readiness_check.py`
   (`STATUS`), with `plan_check.py`, the tests and the three tests of plan state.
4. invariant — identifier `project-readiness-check` in `foundations/invariants.md`.
5. sentence of WAY-320 — "keys by name", "names its key", "the key `tasks` under `the-way`" (also WAY-107, WAY-27, WAY-330).
6. sentence of WAY-140 — "the task's line in the backlog the product names".

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- No directory I touch in this step (I changed no file); the focused runs of the change and of the fix stand in their reports.

## Unread material

- `task-cycle/skill/return_step.md` and `foundation_step.md`: read whole. The record's *Return step* field was not read
  (not named for me); the places of the rows follow the task's *Settlements to record*.

## Searches not found or unclear

- The task's "cited question WAY-342 in WAY-376": WAY-342 is a row under *Withdrawn identifiers*, not a part of WAY-376 (see above).

## Working copies

none made; `.runs/author-return/` was not created.
