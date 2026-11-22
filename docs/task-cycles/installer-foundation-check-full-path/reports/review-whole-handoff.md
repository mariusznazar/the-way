# Handoff — the reviewer of the whole change, `review-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. Do not stop for questions the sources settle.

## Where you work

- The worktree: `the task's worktree` (branch `task/installer-foundation-check-full-path`). the-way is this worktree; there is no product and no `.the-way` pin.
- Your directory for working copies: `.runs/review-whole/` (directly under `.runs/` of the worktree).
- Your report: `.runs/task-cycles/installer-foundation-check-full-path/reports/review-whole-report.md`. Its first line is `PASS <sha>` or `FAIL <sha>`, or `questions`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); the rule that a subagent may not write a file whose name starts with `report` does not apply to it. If the write is refused all the same, return the report whole as your answer.
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read, save the ones this handoff names.

## Your stage

Review the whole change with `review-change`. Read `task-cycle/review/SKILL.md` whole and follow it; for the whole change read `task-cycle/review/whole_change.md` as it says and follow it. You select your own foundation and guidelines (WAY-150, WAY-213) by "Reading the foundation" in `elements/common/way_of_working.md` and `product-guidelines/reading.md`, and count how many decisions of your index you read whole. You are read-only: you change no tracked file and make no commit. Run no full gate (`python -B gate/run_tests.py` with no argument): CI runs it.

- Range: base `fad52af301db6fd6b831850e9bf69f6a11559a4a` to head `1c222ce2` (confirm `git rev-parse HEAD` is the head's full SHA of `1c222ce2`); one commit; the route is one author without a plan, no spec, no slices.
- The frozen task: `.runs/task-cycles/installer-foundation-check-full-path/task.md` (read whole; *Settlements to record* rows 1 and 2, its two answered questions and its *Decisions in play* bind).
- The author's report: `.runs/task-cycles/installer-foundation-check-full-path/reports/author-report.md`; treat it as claims to verify.

## What the orchestrator tells you

- The task touches a trust boundary: the part map names `installation/install.py` as the trust boundary of the part `installation`; the change edits one literal of the block that file writes into a product's `AGENTS.md`. Check crafted input at that boundary as the method gives, and that the change adds no new read of outside data.
- The task holds no operation that cannot be undone.
- The decision WAY-418 binds the review of this change: a warning of the instruction check in a run on the head of the change is a finding Important within the task's scope, with no comparison with the base. Run the instruction check on the head as `task-cycle/review/whole_change.md` gives.
- The orchestrator's selection of what the author read is not binding for you. The author reports it did not open `guidelines/coding-repository-changer.md` (the installer is a script of that kind) for the reason that the change edits one literal of the text the installer writes; judge whether its row's *When to read* matches the change, and read the file whole if it does.
- The author asks the orchestrator whether WAY-418's *Verification* should name the new invariant; the orchestrator's choice: leave the decision unchanged, since no row of *Settlements to record* asks for the edit. Judge it as a finding only if you hold the foundation to require it.
- The author's test builds the product in the system's temporary directory by the existing `InstallTest` helper, as every test of that file does; the rule of working copies does not cover files a product's own tests make by themselves.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way` populated, and the dependencies those checks need installed as the product's own rules give, before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and command of a probe that shows a finding among them, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.

## What to return

The report as `task-cycle/review/SKILL.md` gives it, its first line `PASS <sha>` or `FAIL <sha>`, with every finding graded and scoped by you alone (blocking, Minor, outside the task's scope), the checks you ran each with its command and exit code, the number of decisions you read whole, the changed files with added and removed line counts, **Unread material** (what you selected or this handoff names that stayed unread or was read in part, or `none`) and **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`). Return the status, the report's first line, one line on the checks, and the report's path.
