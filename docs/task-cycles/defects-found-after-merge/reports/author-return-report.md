# Author return report — defects-found-after-merge

Status: `done` (nothing needed a correction). Commits made in this step: none. Head: `6d3298b`.

## Foundation compared with code

Compared with the files of the tree at `6d3298b`, each whole where it is an entry and by the passages
the entry speaks of where it is a file:

- WAY-353 against `project-level/task/template.md` (the paragraph under *What each section carries*'s
  header text) and `correction.md`/`record_template.md` (the kind test, which cite it by reference): the
  criterion (defect against the earlier task or foundation, or a regression; new need, change of mind,
  gap, maintenance excluded) reads the same in all. Matches.
- WAY-354 against `template.md` (the line `Defect introduced by:` under `Project relation:`, values
  `none` / addresses joined by ` · ` / commit address / `unknown — <why>`, filled by the refining agent,
  a missing line = not assessed), `project-level/task/skill/draft.md` and
  `process-audit/problem_register.md` (class `defect-found-after-merge`). Matches.
- WAY-355 against `task-cycle/record_template.md` (the item before the process remarks, one line per
  correction, the file in `reports/`) and `task-cycle/skill/correction.md` (the file
  `reports/correction-<n>-remarks.md`, word for word, also for conversation and target-branch-only
  corrections). Matches.
- WAY-356 against `record_template.md`, `correction.md` and `request_template.md` kind 17: the sources
  `item <n>` (kind number, not item number) / `remark` / `target-branch`, the kinds `defect` /
  `not-required` / `none` only with `target-branch`, the pairs shown in one sentence. Matches.
- WAY-357 against `problem_register.md`: the two classes with Added `start`, the bullet for
  `item · defect` to `known-problem-left`, *Record* and *Stages* sentences for both rows. Matches.
- WAY-287 (changed in place) against `request_template.md` kind 17 in *You accept by merging* and the
  correction row of the variants table: the group holds the pairs' sentence after a correction. Matches.
- The entries the task names under *Decisions in play*: WAY-330, 333, 339, 296, 289, 335 compared with
  the register template, the record template and the request template. WAY-296: the new item stands
  before the process remarks, which stay last (tests in `task-cycle/test_remarks_check.py` and
  `process-audit/test_audit_count.py`). WAY-339: new classes in the template's starting list change the
  list of classes, which already starts a new series in the user's register on its date; no text to
  change. WAY-289: the item 8 reference in `correction.md` reads "below" and item 8 is named below it.
  WAY-330 and WAY-333 hold for a register template with a starting list the user widens. WAY-335: the
  row after the merge names in *Record* the cycle that introduced the defect, which the decision counts
  under that cycle's version. All match.
- Part map entries `project-level`, `task-cycle` and `process-audit`: responsibilities (task refinement,
  the steps of a task, the register template and the audit) cover the changed files; `Files:` globs
  (`project-level/**`, `task-cycle/**`, `process-audit/**`) cover every file the change touched; no
  surface, trust boundary or dependency is changed. Matches; no part-map change.
- Search for what no longer matches: `grep -rn "WAY-35[3-7]"` across the tree outside `.runs/` finds
  references only in the files above, each to the entry whose meaning it carries; no other file of the
  tree names the record's items, the kinds of request items or the register's classes in a way the
  change leaves stale (the kinds are named only in `correction.md` and `request_template.md`, the
  register classes only in the template).

What no longer matched and its correction: none.

## Decisions written or changed

none in this step (written in the foundation step: WAY-353, 354, 355, 356, 357; changed in place:
WAY-287).

## Invariants written or changed

none

## Environment facts

none (no source outside the product that the foundation does not hold).

## Glossary terms

none: "defect", "correction" and "fixing task" keep their ordinary meanings; no term is used against
its entry.

## Part-map changes

none

## Projected entries written whole or in part

none (the task is independent and carries no projected entry).

## Rows of *Settlements to record* written

All eleven rows are written, none missing:

| Row | Entry |
|---|---|
| 1 | WAY-354 |
| 2 | WAY-353 |
| 3 | WAY-354 |
| 4 | WAY-355 |
| 5 | WAY-356 |
| 6 | WAY-357 |
| 7 | WAY-354 |
| 8 | WAY-354 |
| 9 | WAY-355 |
| 10 | WAY-356 |
| 11 | WAY-357 |

WAY-287 carries the change the task names under *Decisions in play* and is no row.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py --skip-test-citations .` — exit 0 ("0 errors").
- `git status --short` — clean; `git log --oneline -1` — `6d3298b`.
- No test run: nothing changed in this step. Not run: the full gate (the orchestrator's).

## Unread material

none. (Return step files, the handoff, the five new entries and WAY-287 as written, and the touched
templates and skills were read in this session; the part map entries read earlier, lines 77-125.)

## Searches not found or unclear

none
