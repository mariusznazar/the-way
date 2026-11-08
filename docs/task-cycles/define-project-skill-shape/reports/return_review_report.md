PASS 09b0dd0c7dafe1840c788f280f90e90fdd7944fa

# Review of the return step — define-project in the shape of WAY-256

Reviewed: the return step's commit, range `eeca32c..09b0dd0` (one commit, `09b0dd0` "Name
define-project's step 7 file readiness_gate.md, since the glossary's gate is the test command").
`git rev-parse HEAD` = `09b0dd0c7dafe1840c788f280f90e90fdd7944fa`, the head given.
Method: `task-cycle/review/SKILL.md`, read whole; against the frozen task
(`.runs/task-cycles/define-project-skill-shape/task.md`, To do 2–3 and the acceptance criteria on
pointers and on the change staying in `project-level/skill/`), `task-cycle/skill/return_step.md`
(read whole) and the glossary entry "gate" (`foundations/glossary.md:67-71`).

The diff: `project-level/skill/gate.md` renamed to `readiness_gate.md` at similarity 100% (content
unchanged); `SKILL.md:73-75` (step 6) and `:79-80` (step 7) and `existing_definition.md:11-12` name
the new file. Each pointer keeps its step, its condition ("Where the readiness check reports a
finding at this step…", "unless step 6 had you read it", "in a turn dispatched through a refinement
conversation path", "goes through step 7 … again") and its wording apart from the name and the line
break; no route is added or lost.

## Findings

### Critical

none

### Important

none

### Minor

- **M-1 (within the task, record only).** Place: `.runs/task-cycles/define-project-skill-shape/reports/fix_report.md:39-40, :58-77, :151-166`,
  and likewise `review_report.md`, `findings.md`, `review_fix_report.md`. These records name
  `gate.md` with no note that the file is now `readiness_gate.md`; `author_report.md:6-7` got such
  a note, `fix_report.md` was "left as written for `eeca32c`" (`return_report.md:118-119`). Why it
  matters: the request description is still pending (`cycle.md:98`); a passage carried from
  `fix_report.md` into it word for word would name a file that no longer exists. Nothing in the
  tree is affected. Evidence: `grep -rn "gate\.md" .runs/task-cycles/define-project-skill-shape/ | grep -v readiness_gate\.md`
  lists those lines; the request material itself (`word-counts.md`, `assessment.md`,
  `proposals.md`) holds no old name (below).

Blocking findings: 0. Minor: 1. Out of scope: 0 (one line under Declined to judge).

## What was checked and how

- **No pointer to the old name.** `git grep -n "gate\.md" 09b0dd0 | grep -v "readiness_gate\.md"`
  finds nothing in the whole tracked tree (exit 1 of grep = no match). Positive control:
  `git grep -n "readiness_gate\.md" 09b0dd0` finds exactly the three pointers of the diff.
  `installation/install.py:31` names only `project-level/skill/SKILL.md`; no installer list names a
  file beside it.
- **The change stays in `project-level/skill/`.** `git diff --name-only eeca32c..09b0dd0 -- ':!project-level/skill'`
  prints nothing; `git diff --name-only 2754675..09b0dd0 | grep -v "^project-level/skill/"` prints
  nothing (To do 3).
- **Files of the-way citing the skill's step numbers still point right.** `git grep` for
  "define-project step / step 7" outside the skill: `project-level/lead/skill/SKILL.md:208` ("step 7
  in delegated mode"), `project-level/plan/skill/existing_plan.md:9` ("step 7 again"),
  `project-level/technology/start.md:8` ("step 5"). Step headings 5, 6 and 7 ("The readiness gate")
  stand in `SKILL.md` at the same numbers; 7.1–7.5 are in `readiness_gate.md` unchanged (rename at
  100% similarity). None of these names a file of the skill. (Other "step 7" hits are of other
  skills: `plan/skill/assign_entries.md:15`, `technology/task_run.md:78`, `task-cycle/skill/SKILL.md`.)
- **The correction is one the return step may make.** `return_step.md:19`: "A term used against
  its entry takes the use corrected and no entry." The glossary's "gate" is "the one command that
  runs all of a product's tests"; a file named `gate.md` holding the readiness gate is a use against
  that entry, made by this change (the file is new in `c0a0f52`). The new name repeats the step's own
  heading "The readiness gate" (`SKILL.md:77`). No foundation entry is written, matching the report.
- **Report figures and route walks.** `word-counts.md` (8), `assessment.md` (12), `proposals.md` (4),
  `make_word_counts.py` (8), `make_assessment.py` (11), `check_pointers.py` (8) name
  `readiness_gate.md`; none names `gate.md`. `author_report.md` route walks name `gate.md` under the
  note at its top (`:6-7`). The return report's claim "the same figures as after the fix" holds:
  `verify_counts.py` compares 279 figures, 0 differ — a file name is one token, so no count moves.
- **Pointer acceptance criterion** (each pointer names its step in words a reader of `SKILL.md`
  recognises): unchanged by the rename; the step 6 and step 7 pointers sit under their headings.
- **Author's own-work check**: it names the weakest point (a pointer left on the old name, or a
  step sent to a missing file), and its check — grep plus `check_pointers.py` — would catch it; I
  reran both with the positive control above.
- The return report's "done with concerns" (moved uses of "the gate" meaning the readiness gate):
  see Declined to judge.

## Declined to judge

- The uses of "the gate" for the readiness gate that the change moved word for word from the base
  (`SKILL.md:26`, `:40`; `delegated_mode.md:1`, `:22-29`; `existing_definition.md:11`, `:15`;
  `first_write.md:9`): outside the task — To do 1/acceptance criterion 1 and the series' settlement
  ("the rebuild changes where rules stand, not their content") forbid rewording them here, the same
  words stand in WAY-118 and `project-level/definition_template.md` ("Gate record"), which To do 3
  keeps unchanged, and a word with two meanings is a renaming under WAY-99, which section 3 of the
  method leaves outside a glossary-term finding. The return report sends it to `assessment.md`
  proposal 4.

## Checks run

| Check | Command | Exit code / result |
|---|---|---|
| Range and head | `git rev-parse HEAD`; `git log --oneline eeca32c..09b0dd0`; `git diff -M eeca32c..09b0dd0` | 0; one commit; rename 100% + 3 pointer lines |
| Old name anywhere tracked | `git grep -n "gate\.md" 09b0dd0 \| grep -v "readiness_gate\.md"` | no match (grep exit 1); positive control 3 hits |
| Old name in the record | `grep -rn "gate\.md" .runs/task-cycles/define-project-skill-shape/ \| grep -v "readiness_gate\.md"` | hits only in historical reports (M-1) |
| Outside `project-level/skill/` | `git diff --name-only eeca32c..09b0dd0 -- ':!project-level/skill'`; same for `2754675..09b0dd0` | empty both |
| Pointers | `python -B <reports>/check_pointers.py` | 0, "10 files; 0 failures" |
| Sentences of the base | `python -B` on a copy of `<reports>/compare_sentences.py` in the scratchpad (so the record's `compare_sentences.txt` is not rewritten), then `diff` with the record's file | 0, "121 units; 8 missing; 0 unexpected"; diff exit 0 (identical) |
| Figures | `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/author_report.md <reports>/fix_report.md <reports>/return_report.md` | 0, "279 figures compared, 0 differ"; wc -w cross-check on 15 files, two locales |
| Focused tests | `python -B gate/run_tests.py project-level` | 0, 271 tests OK |
| Entry points | `python -B agent-instructions/skill_entry_points.py` | 0, "entry points are current" |
| Foundation | `python -B elements/common/foundation_check.py .` | 0, "0 errors" |
| Line length | `awk 'length>100' project-level/skill/*.md` | only `SKILL.md:3` (frontmatter description, unchanged) |
| Worktree untouched | `git status --short` | clean |

Not run: the full gate (the orchestrator's run); `gate/run_tests.py installation` (no installer
file names a file beside `SKILL.md`, shown by the grep above). No mutation check of
`check_pointers.py` against a missing file: it would need a changed tree; the author's report
records one for `eeca32c`, and the old-name grep covers the risk directly.

## Reaches beyond the dispatch

- `foundations/glossary.md:67-71`, the entry "gate" — the correction is made against it (named in
  the handoff, read whole).
- `installation/install.py:31` via `git grep` — whether the installer names the renamed file.
- `.runs/task-cycles/define-project-skill-shape/cycle.md:95-98` — whether the request description
  already exists (pending), for the weight of M-1.
- `reports/compare_sentences.py`, `check_pointers.py`, `verify_counts.py` (their write calls and
  paths) — to run them without changing the record.

## Searches not found or unclear

- Which reports the request description will draw from is not stated anywhere in the record
  (`cycle.md:98` "Description: pending"); M-1 is graded on the assumption that `fix_report.md` may be
  one of them.
