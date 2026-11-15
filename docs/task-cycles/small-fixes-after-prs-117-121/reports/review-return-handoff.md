# Handoff — review of the return step's commits (task slug `small-fixes-after-prs-117-121`)

You review the commits of the return step of one task of the-way as an agent that did not make
them. The orchestrator of the task cycle dispatches you; nothing here is the human's approval; ask
the human nothing.

- Worktree (read-only for you): `the task's worktree`, branch `task/small-fixes-after-prs-117-121`. Range: base `eaf815c` (the reviewed code head), head `4066ae5` (confirm `git rev-parse HEAD`); one commit, which changes `agent-instructions/README.md`, `elements/invariants/template.md`, `foundations/decisions.md` (WAY-344) and `foundations/part_map.md` (part `elements-common`).
- Method: `task-cycle/review/SKILL.md`, the review of the return step's commits (its section 2: against the task and the foundation entries the return step writes or corrects). Read `task-cycle/skill/return_step.md` for what the return step is and may do.
- The task (frozen, read the passages that bear on the range): `docs/task-cycles/small-fixes-after-prs-117-121/task.md`; items 8 and 9 (the listing of an invariant whose base copy lacks *Method* or *Part*; the sentence of WAY-344), its *Context* line on `agent-instructions/README.md`, and rows 1–9 of *Settlements to record*, row 3 above all.
- The return step's report (claims to verify): `docs/task-cycles/small-fixes-after-prs-117-121/reports/return-step-report.md`. The earlier reviews of the same change, for what was already judged: `reports/review-whole-report.md` (FAIL `e9aea95`) and `reports/review-fix-report.md` (PASS `eaf815c`, its Minor finding n1). The code you compare the corrected entries with is `elements/common/foundation_check.py` and its tests at `4066ae5`.
- Foundation entries by identifier, each whole: WAY-344, WAY-114, WAY-134 (what makes an entry `the cycle's` and what a row carries), WAY-17 not needed. Guidelines: none apply to this range (no code or test file changes).
- Judge in particular: that each corrected sentence is true of the code and no wider than the task's rows settle; that the removal of two clauses from WAY-344's pair of examples is right under the return step's rule (a pair is left only for a part no test holds; the test named by *Verification* `tests:`), so that WAY-344's mark goes back to `row 3`; that the part-map change keeps the part's responsibility and dependencies in agreement with the code (`elements/common/foundation_source.py`, a module of reading files and git, imported by `foundation_check.py`); and that the entry's meaning sentences in the report match.
- No full gate (the orchestrator's). You may run `python -B elements/common/foundation_check.py` and focused checks in your own working copy.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/review-return-report.md`, first line `PASS <sha>` or `FAIL <sha>`. Your directory for working copies: `.runs/review-return/`.

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
