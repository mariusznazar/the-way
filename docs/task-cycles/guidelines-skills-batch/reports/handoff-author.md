# Handoff — the one author (`make-change`, "the whole change as the one author")

You are the one author of this change, with no plan and no slices. You work from the root of this
worktree: `.` (branch
`task/guidelines-skills-batch`, base `05534d381b95a4e2692875263dd0d8875097b89d`). Write only there.

## Delegation

The human who requested this cycle delegated intermediate choices to the orchestrator. The cycle
has no human contact before the request. Do not ask the human anything. Send a question to the
orchestrator (return `questions`) only for a fact no source gives; a choice of how to make what the
task and the foundation settle is yours to make and to name in your report.

## Method

Your method is the project skill `make-change`: read `task-cycle/change/SKILL.md`
whole, and any file it names only when the step or variant that names it comes. Your variant is
"the whole change as the one author". Your report path is
`docs/task-cycles/guidelines-skills-batch/reports/author-report.md`.

The foundation step (writing the entries the task carries) is part of your work: read
`task-cycle/skill/foundation_step.md` whole when you reach it, and the skill of an element when
you write an entry of that element (`elements/decisions/skill/SKILL.md` for `foundations/decisions.md`; the
glossary, invariants, part map and environment-facts elements likewise if you touch them). Do not
run the product's full gate (`python -B gate/run_tests.py`): that run is the orchestrator's.
Run the focused tests of the directories you change (`python -B gate/run_tests.py <directory>`),
`python -B elements/common/foundation_check.py` as its README gives, and, for instruction-files
and skill files, `instruction-files/check_instructions.py` as its skill gives; report each with its
command and exit code.

## The task

Frozen task, read in full:
`docs/task-cycles/guidelines-skills-batch/task.md`

Its `Status` is `ready for cycle`; `Project relation: independent`; *Questions carried to cycle*
and *Human actions*: none. Its *To do* has 20 items; its *Questions to settle* are answered by the
human; its *Settlements to record* has 5 rows you write into the foundation (WAY-134, WAY-135).

Line numbers in the task are of the state it was refined on (`foundations` `f447bb6`); the
decision log has grown since, so find every place by its content. Since that commit only
`product-guidelines/{coding,styleguide,testing}/SKILL.md` changed (the paragraph that says where
the skills named in the files beside a skill lie); no item of the task is touched by it.

## Answers of the orchestrator's step 4

- Trust boundary: no. Irreversible operation: no. Open design choice: none. Reserved choice: none.
- Route: one author without a plan, class `same`.
- The repository has no `guidelines/` directory of its own (task, question 4): do not wait for
  coding or testing guidelines of the-way.
- Source discipline: the task is the only authority. Where an item's text leaves a detail open, say
  so in the report rather than closing it with an invented rule; where you need wording, take the
  words of the decision or the standing text the item names.

## What to read (selected by "Reading the foundation", WAY-150)

Parts touched: `product-guidelines` (skills and templates of `coding/`, `testing/`, `styleguide/`,
and `audit_end.md`, `reading.md`), `project-level` (`project-level/task/skill/guideline_findings.md`),
`instruction-files` (`judging.md`), and `decisions` (`foundations/decisions.md`, the settlements).

Foundation entries to read whole, by identifier, in `foundations/decisions.md` (heading
`### WAY-NN`): the task's *Decisions in play* — WAY-95, 168, 171, 172, 204, 215, 216, 240, 242,
247, 251, 256, 272, 274, 276, 278, 282 — and, for the instruction-files item and the
settlements, WAY-257 (the judging table), WAY-201, WAY-202, WAY-217, WAY-273, WAY-275 and WAY-25
(precedence between decisions). Read the glossary (`foundations/glossary.md`) whole and the part
map (`foundations/part_map.md`) whole. Read further wherever the foundation step's search finds
an entry; name each such reach (a decision or file you read that this handoff did not name) in
your report.

Guideline files of the parts are the skills and templates you edit; read each whole before you
edit it. There are no product guidelines of the-way to read.

## Boundary

Make the whole change: the 20 items, the 5 settlements as entries of the foundation, the return
step's comparison is not yours (the orchestrator dispatches it later). Commit with explicit paths
(`git add <paths>`; never `git add -A`), messages in English. Where an item proves impossible as
written, or two items collide, return `returned` or `questions` as your method gives, with no
guess. Weakest-point check: for each item name the requirement, the check you made that the
changed text really says it, and what it showed.

Return: status, commits, one-line check result naming what failed or did not run, the report path,
and in the report the sections your method gives, including **Searches not found or unclear**
(each thing looked for and not found or unclear, or `none`) and your own-work check.
