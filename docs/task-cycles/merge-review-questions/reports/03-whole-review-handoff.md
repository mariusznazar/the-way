# Handoff — the review of the whole change (`review-change`)

Delegation: the person who requested this cycle delegated intermediate choices to the orchestrator;
nothing here is that person's approval.

Worktree (work from its root; read-only for you):
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions`, branch `task/merge-review-questions`.

Method: `task-cycle/review/SKILL.md` of this worktree, the variant for the review of the whole change.
Read it whole; read a file it names only when the step or variant that names it comes. You select your
own foundation and guidelines by the parts of the change.

Range to review: base `52889bc700123b50258c4201835034f0529351df` to head `3601aba` (two commits:
`5932216` the two decisions WAY-306 and WAY-307 in `foundations/decisions.md`, `3601aba` the wording
in five skill files).

Frozen task (read whole):
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\task.md`
(Polish; the replacement sentences of *To do* 1–4 are English, and the change must carry them word for
word, wrapping aside). The task's *To do* line numbers are from `dfd50e5`; the step-12 sentence is now
at `task-cycle/skill/SKILL.md:415-420`. No spec, no plan (one author without a plan). The task's
*Questions to settle* answers and *Context* are binding; `task-cycle/review/SKILL.md` must stay
unchanged (*Out of scope*).

Both rows of *Settlements to record* are carried by the new decisions WAY-306 (row 1) and WAY-307
(row 2); check coverage of every *To do* item and both rows, and source fidelity.

Author's report: `.runs\task-cycles\merge-review-questions\reports\02-author-report.md` in the worktree
(absolute path: `C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\reports\02-author-report.md`).

Answers of step 4: touches a trust boundary — no; holds an irreversible operation — no.
The task did not move a pin. No Minor or out-of-scope findings of earlier reviews exist.

You alone grade and scope your findings. The orchestrator runs the product's gate; do not run it
(run focused checks only, e.g. `python -B elements/common/foundation_check.py`).

The report: write it in full to
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\reports\04-whole-review-report.md`
as your method gives it, with each check's command and exit code and the section **Searches not found
or unclear** (`none` is an answer). Return the report's first line (`PASS <sha>` / `FAIL <sha>` /
`questions`), changed files with line counts, and the report path.
