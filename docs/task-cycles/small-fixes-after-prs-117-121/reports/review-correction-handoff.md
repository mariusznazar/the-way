# Handoff — review of a correction for the human's remarks (task slug `small-fixes-after-prs-117-121`)

You reviewed the whole change, its fix and the return step of this task; you are resumed to review
a correction made after the human's remarks on the open request. The orchestrator dispatches you;
nothing here is the human's approval beyond the remarks, which bind; ask the human nothing.

- Worktree: `the task's worktree`, branch `task/small-fixes-after-prs-117-121`. Range: base `aefe984`, head `5cb2e1f` (confirm `git rev-parse HEAD`); one commit by the one author, five files.
- Method: `task-cycle/review/SKILL.md`; read `task-cycle/review/fix.md` as it says for a correction made for the human's remarks. The remarks stand in place of a findings file: `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-remarks.md` (the day advisor's answer in the human's name, which binds; finding o1 of your whole-change review and findings r1 and r2 of the return step's review are its subject).
- The author's report (claims to verify): `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-report.md`. The reports you know: `reports/review-whole-report.md`, `reports/review-return-report.md`.
- Judge: that each of the three remarks is made as the human asked and no wider (the rule on the added pair in `task-cycle/skill/request_template.md` limited to an entry that is `the cycle's` by an added pair; the two descriptions of the listing against `elements/common/foundation_check.py`); that the clause the author added to `task-cycle/skill/foundation_step.md` does what the template rule needs; and, with special care, the change in place of WAY-114 (`foundations/decisions.md`, the binding sentence, *Verification* and *Rejected*): the author holds it a clarification of what the request's description shows that the remark asks, not a change of the decision's meaning (WAY-114's rule of what an approved decision may change in the cycle, `agent-instructions/README.md` "Make the change"); say whether you hold it so, and whether the binding sentence still reads well after the insert (a line now longer than its neighbours).
- Entries by identifier, each whole: WAY-114 and the decisions its *Rejected* or *Verification* name that bear on the insert. Guidelines: none apply to this range (no code or test file changes).
- No full gate (the orchestrator's). You may run `python -B elements/common/foundation_check.py` and focused checks in your own working copy.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-correction-report.md`, first line `PASS <sha>` or `FAIL <sha>`. Your directory for working copies: `.runs/review-correction/`.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
