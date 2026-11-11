# Handoff — review of the whole change

Delegation: the person who requested this cycle delegated intermediate choices to the orchestrator;
your questions go to the orchestrator. Nothing here is the human's approval.

Worktree (work only here, read-only): `the task's worktree (the repository's root)`
Branch `task/scripts-fail-on-missing-fields`.

Method and variant: read `task-cycle/review/SKILL.md` of this worktree whole (entry point
`.claude/skills/the-way-review-change/SKILL.md`). Your variant is "the whole change". Read a file
the method names (`whole_change.md` and others) only when the step or variant that names it comes.
Also read `agent-instructions/README.md` — the-way's own rules of a change.

Range: base `e9a0f926dc9758f6554e8c0a30925d3e4d68cfed`, head `4905a56` (full SHA by
`git rev-parse HEAD`; confirm it). One commit, one file: `foundations/decisions.md`, +79 lines,
the new entry WAY-330. The route is one author without a plan: no spec, no plan, no slices.

Task (frozen, read whole): `docs/task-cycles/scripts-fail-on-missing-fields/task_frozen.md` — the
document proper starts at the line `# Skrypty the way sprawdzają dane wejściowe…`; the part above is
the author's private backlog note. Judge coverage of every item of *To do* and every row of
*Settlements to record* (1–4), and fidelity to the task as the source: the decision may state only
what the task and its *Questions to settle* settle, and the *Not chosen* ways belong in *Rejected*
with their costs. *Out of scope* is the review and repair of existing scripts.

Author's report (a set of claims to verify, not evidence):
`docs/task-cycles/scripts-fail-on-missing-fields/reports/author_report.md`. It carries three
concerns and two things its writer added on its own: the *Verification* example pair and the last
sentence of *Rationale* about WAY-12. Judge whether each is acceptable, and grade as you see fit; the
orchestrator does not tell you the grade.

Answers of step 4: trust boundary — no (one entry of `foundations/decisions.md`, part `decisions`,
*Trust boundary* none); irreversible operation — no. Reserved choice — none. Mechanical check of
the author's range by the orchestrator: clean worktree, non-empty range, the one file, no mismatch.
The author's **Unread material** (WAY-03; `task-cycle/request_check.py` after line 120; the rest of
`decisions.md` and `invariants.md`) — the orchestrator passes it to you: read WAY-03 yourself if you
judge the form against it.

You select your own foundation and guidelines by "Reading the foundation"
(`elements/common/way_of_working.md`) — the parts the change touches are the 16 of the new entry's
*Scope* through `decisions`; state in the report how many decisions you read whole and how many by
title. Product guidelines: the-way has none (WAY-328); no guideline file to read. Run
`python -B elements/common/foundation_check.py` as a check of your own and report its command and exit
code. Do not run the product's gate (`gate/run_tests.py`); it is the orchestrator's.

Report: write it to
`docs/task-cycles/scripts-fail-on-missing-fields/reports/review_whole_report.md`
as the method gives it; first line `PASS <sha>` or `FAIL <sha>` or `questions`; for each blocking
finding the slice it comes from — here none, since there is no plan, say `none`; list Minor findings
within the task apart from those outside the task's scope; include **Unread material** and
**Searches not found or unclear** (each `none` where empty). Return the status, the first line, the
checks with command and exit code, the report path, questions and concerns.
