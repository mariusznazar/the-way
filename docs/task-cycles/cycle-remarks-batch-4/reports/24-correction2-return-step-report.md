# Return step report, after the second correction — cycle `cycle-remarks-batch-4`

**Status:** `done` — nothing no longer matches; **no commit** made. Head compared: `1c1e8c8`
(range `e3825a8..1c1e8c8`).

## Return step (fields of the record)

- **Foundation compared with code:** compared WAY-160, WAY-71 and WAY-287 (as the two corrections left
  them), WAY-27, WAY-17, WAY-163, WAY-294, WAY-58, the glossary entries `gate` and `return step` and the
  part-map entries `decisions`, `task-cycle` and `elements-common` with the files of the repository on
  this head and with the human's remarks (`reports/11-correction-remarks.md`,
  `reports/18-correction2-remarks.md`). Result: all match.
  - WAY-71's binding sentence and `elements/common/rules.md` carry the same clause for a mixed value (the
    second correction checked it by a whitespace-collapsed comparison); both element templates, the
    docstring and `known_part`/`todo_item` of `foundation_check.py`, its tests, WAY-287's example and
    item 15 of `request_template.md` say the same: the known items stay named and checked, the first
    `TODO` item with what follows is one description, a bare `TODO` item is an error, and a mixed value
    is one gap shown with the missing part alone.
  - WAY-71's *Verification*: the *violates* case "a whole-value `TODO — …` with the known fact in its
    description" is a case for the agent comparing a change, not for the script (the script accepts a
    whole-value `TODO`), as the human's route 1 intends; it reads true.
  - WAY-71's *Rationale* names no file or script (WAY-05); WAY-287's three places agree on the three
    fields.
  - WAY-160 (gate once on the tree the return step and its review leave; *violates* example of the
    unmatched fix range), WAY-27, WAY-17, WAY-163, WAY-294 and WAY-58: unchanged by the second
    correction and still matching, as in the earlier return steps.
  - Glossary `gate` and `return step`: used in their meaning. Part map: no file added, removed or moved
    and no responsibility changed; the three entries need no edit.
  - The-way's foundation holds no `TODO` in the five fields (`foundation_check.py .`: 0 errors).
- **Decisions written or changed:** none in this step.
- **Invariants:** none.
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries:** none carried.
- **Rows of *Settlements to record*:** none.

## For the human, not changed here

- N-1 of the review of the second correction: a bare `TODO` after a comma or a line break instead of
  ` · ` passes silently, and a described one after a comma gives a misleading error ("is no identifier
  of a fact"). The rule and the templates speak of ` · ` only.
- Earlier left to the human, still open: the *Relations* link from WAY-287 to WAY-71 (the remaining part
  of M-5); the WAY-287 line over 100 columns (cosmetic) — it was in the binding sentence's tail and the
  second correction did not touch it.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors").
- No commit, so no other check run.

## Unread material

none read in part beyond the compare: handoff, `return_step.md` and `foundation_step.md` read whole;
WAY-71 read whole (current text) and the second correction's diffs of `rules.md`, both templates and
`request_template.md` read; WAY-287, WAY-160, WAY-27, WAY-17, WAY-163, WAY-294, WAY-58, the glossary
entries and the part-map entries were not re-read in this step (unchanged since the first and second
return steps except WAY-287's *Verification* example, read in the second correction).

## Searches not found or unclear

none
