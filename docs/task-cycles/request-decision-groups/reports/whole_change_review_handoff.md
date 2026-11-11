# Handoff — review of the whole change

You review the whole change of one task of a the-way task cycle, as an agent that did not make it.
You are read-only: change no file of the worktree, make no commit. The person who requested the
cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- **Worktree:** `the repository's root (the task's worktree)`, branch `task/request-decision-groups`.
- **Method:** the project skill `the-way-review-change`, method file `task-cycle/review/SKILL.md` in the worktree; read it whole, and each file it names only when the step or variant that names it comes. Your variant: **the whole change**.
- **Range to review:** base `e3825a82386a61930a86f8517fc0c5f422fc2833` to head `ff7799473843608eb11cc2f4e162920d8f7681a7` (`git diff e3825a8..ff77994`): two commits, `9876bfe` (code, template, skill files) and `ff77994` (decisions). Changed files: `foundations/decisions.md` (166 lines), `task-cycle/request_check.py` (81), `task-cycle/skill/SKILL.md` (8), `task-cycle/skill/correction.md` (16), `task-cycle/skill/request_template.md` (318), `task-cycle/test_request_check.py` (177).
- **Frozen task (read it whole; it is the requirement):** `docs/task-cycles/request-decision-groups/task_frozen.md`. No spec and no plan exist: one author, no slices.
- **The author's report (read it):** `docs/task-cycles/request-decision-groups/reports/author_report.md`.
- **Your report path:** `docs/task-cycles/request-decision-groups/reports/whole_change_review.md`. Its first line is `PASS <sha>`, `FAIL <sha>` or `questions`, then the sections your method requires, including the counts of decisions read whole and by title, **Unread material** and **Searches not found or unclear**. Every check you name carries its command and exit code.

## Answers of the orchestrator at start

- Does the change touch a trust boundary? No (`task-cycle` and `decisions` carry the boundary `none` in the part map). Does it hold an irreversible operation? No. Check both anyway against the diff.
- The task moved no pin. Checks failing on the base: none (`python -B gate/run_tests.py` on `e3825a8`: exit 0, 864 tests in 9 directories).
- The orchestrator runs the product's gate after your review; do not run the whole gate. Focused tests are yours to run where your judgment needs them.

## What to check, beyond your method's criteria

- Every item of the frozen task's *To do* 1–8, and each of its *Settlements to record* rows 1–5, against the diff — coverage, and source fidelity: whether anything the diff says is not in the task or the foundation. The author's report lists choices of its own (Choices 1–9) and one edit outside the task (WAY-317); judge each.
- The author reports, as gaps in its reading, that WAY-162 and WAY-295 were read in part, that WAY-150, WAY-33, WAY-36 and WAY-07 were not opened as entries, and that `task-cycle/skill/SKILL.md` was read only in passages. You select your own foundation and read it by "Reading the foundation" in `elements/common/way_of_working.md`; read the decisions that bear on the section for the human's decisions whole, and say what you read.
- The template's own example of the decision section must pass `python -B task-cycle/request_check.py` as the author's test claims; the numbers of the kinds of items must point at the same kinds as at the base (`correction.md`, `SKILL.md` and the template's own references); and the Polish wording of the groups must be consistent with the task's *To do* 1.
- Whether the wording of the template is understandable to the human it is written for (the top part is written in plain words).

Return: status (the report's first line), no commits, a one-line check result naming what failed or did not run, the report's path, your questions and concerns, your **Unread material** and your **Searches not found or unclear**.
