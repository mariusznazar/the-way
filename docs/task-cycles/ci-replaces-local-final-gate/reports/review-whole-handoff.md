# Handoff — review of the whole change

You are a reviewer (agent type `the-way-stage`) in a task cycle of the-way; you did not make this change. The person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that person's approval.

- Worktree (read-only for you): `the task's worktree`, branch `task/ci-replaces-local-final-gate`.
- Method: read `task-cycle/review/SKILL.md` whole; your variant is the review of the whole change, so read `task-cycle/review/whole_change.md` and follow it; read each other file the method names only when its step comes. You select your own foundation and guidelines.
- Range: base `8f0c1c3e89c8e8151f64cf82a3b8bf07d004b999` .. head `b64608400f4fb55bb5508f71e2c4c2aadbcd6a60` (three commits: `b2f3f82`, `1c65f5f`, `b646084`). Compute the diff yourself.
- Frozen task (read whole): `docs/task-cycles/ci-replaces-local-final-gate/task.md`. No spec, no plan (one author without a plan); no slice reviews happened, so you judge everything.
- The author's report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-report.md` (claims to verify, not evidence). Note what it says it did not read: `foundations/part_map.md` was not opened, not every decision of the touched parts was read whole — your own selection covers them. It also names open points to judge: no WAY-365 move out of `process-audit/audit_count.py` (3317 lines), the rule for "CI runs on a request" written in step 10 (the task gives none), two separate jobs `tests` and `tests-windows`, the stale environment fact `foundations-branch-ruleset` after the human action.
- Answers of step 4: trust boundary **yes** — `process-audit/audit_count.py` is the trust boundary of the part `process-audit` and the change edits it; check crafted input there (a record copy with a missing, empty or odd `gate_times.md`, hostile text). Irreversible operation: **no**; the change must only prepare the human action (the required check `tests-windows` in the ruleset `foundations_tests`, set by the human at the request) and touch no GitHub setting.
- Task items to cover: To do 1–5, the acceptance criterion (the CI run on the Windows must execute the 32 Windows-only tests; you cannot run GitHub — say how the job is built and what stays unchecked), *Settlements to record* rows 1–6 (each went to where its row says), *Decisions in play* WAY-160, WAY-16, WAY-261, WAY-350 (WAY-261's exception and WAY-350's sentence must stay unchanged). Check source fidelity: no sentence of the changed decisions goes beyond what the task and its sources settle.
- You do not run the product's full gate (the orchestrator's alone, WAY-160). You may run the tests of single directories with `python -B gate/run_tests.py <directory>` and `python -B elements/common/foundation_check.py`; a check you run carries its command and exit code.
- Report: write it to `docs/task-cycles/ci-replaces-local-final-gate/reports/review-whole-report.md`, first line `PASS <sha>` or `FAIL <sha>` (or `questions`), then as the method gives, with **Unread material** and **Searches not found or unclear**, the count of decisions read whole, and the working copies line. Return the report's first line, the report's path and a one-line check result.
- Your directory for working copies: `.runs/review-whole/`.


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
