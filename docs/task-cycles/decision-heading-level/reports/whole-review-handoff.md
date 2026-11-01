# Handoff — review of the whole change, task `decision-heading-level`

**Delegation.** The person who requested this cycle has delegated intermediate choices to the
orchestrator. Send questions to the orchestrator; never to the human.

**Worktree.** `C:\Storage\repos\the-way\.runs\worktrees\decision-heading-level`. Read-only: change
no tracked file and commit nothing. Every path below is relative to it.

**Method.** Read `task-cycle/review/SKILL.md` whole; it lies in this worktree. Read a file it names,
one beside it included, only when the step or variant that names the file comes.

**Stage and boundary.** The review of the whole change, as an agent that made none of it. Return at
the end of the review; start no fix and no later stage. Do not run the full gate
`gate/run_tests.py` with no argument: its run is the orchestrator's.

**Range.** `2f51e6c..168b055`, base `2f51e6c` on `foundations`, branch
`task/decision-heading-level`. Route: one author without a plan; no spec, no slices.

**Frozen task.** `.runs/task-cycles/decision-heading-level/task.md`, read whole.

**Author's report.** `.runs/task-cycles/decision-heading-level/reports/author.md`.

**Answers of step 4.** Trust boundary: no. Irreversible operation: no. Open design choice: none, as
the task gives both insertions word for word. Foundation entries written: none.

**Foundation and guidelines.** You select your own, by the parts of the change. This repository has
no `guidelines/` directory.

**Report path.** `.runs/task-cycles/decision-heading-level/reports/whole-review.md`, its first line
`PASS <sha>`, `FAIL <sha>` or `questions`. Return that first line, a one-line check result naming
what failed or did not run, and the report's path.
