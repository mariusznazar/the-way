# Handoff — review of the whole change, `review-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. The cycle has one ordinary human contact, the request.

## Where you work

- The worktree: `the task's worktree` (branch `task/ai-review-fixes-from-24-11`, target branch `foundations`). Work from its root; the-way is this worktree (no product, no `.the-way` pin). You are read-only on the change.
- Your directory for working copies: `.runs/review-whole/` (directly under `.runs/` of the worktree).
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-report.md`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); the rule that a subagent may not write a file whose name starts with `report` does not apply to it. If the write is refused all the same, return the report whole as your answer. Its first line is `PASS <sha>` or `FAIL <sha>`.
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read unless this handoff names them.

## Your stage

The review of the whole change, as the one reviewer that made none of it. Read `task-cycle/review/SKILL.md` whole and follow it; it sends you to `task-cycle/review/whole_change.md` for the whole change, which you read when it says so. Read a file either names only when the step that names it comes. You select your own foundation and guidelines as the method gives.

- Range: base `07aa55df565d5f10428176c89d20d2c6420a6dfd` to head `225bf1c5` (one commit by the one author, no plan, no slice).
- The frozen task: `.runs/task-cycles/ai-review-fixes-from-24-11/task.md` (read whole). No spec, no plan.
- The author's report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-report.md`.
- Answers of the start: trust boundary **no** (no file of the change is one the part map names as a boundary; the check adds no read of outside data); irreversible operation **no**; no open design choice, no reserved choice; one author without a plan, class `same`. No decision was renumbered and the target branch has no commit the branch lacks (`origin/foundations` at `07aa55df`).
- The checks failing on the base: none (the base is a merge commit with the tree of its second parent; the list comes from the merged request's final gate, which was green).
- The author's own checks (named in its report) include all the focused tests of the directories touched, exit 0, and `python -B elements/common/foundation_check.py` with `0 errors` and no `listed:` line; the full gate is not run by any agent (CI is the final gate).
- Carry to your judgment these gaps the author's report names as unread: WAY-14, 33, 150, 02, 379, 382, 385 not read whole as entries; the part map's entries for `elements-common`, `invariants`, `decisions`, `task-cycle`, the glossary and the invariants whose *Part* is `elements-common` or `every` not read. You select your own reading, so read what bears on the change, which the author's gaps do not excuse.
- Points the orchestrator asks you to judge besides the method's own: (1) the author added to WAY-30's *Verification* a pair of examples (one complies, two violates) that row 1 of *Settlements to record* does not give, and edited the *Rationale* and *Rejected* of WAY-12 and WAY-30 — judge whether each addition stays within the settlements and the task's *Questions to settle* and what WAY-12, WAY-30 and WAY-05 say of such fields; (2) the author also edited the root `README.md` (the paragraph on what `foundation_check.py` reports), `elements/decisions/template.md` and `elements/invariants/template.md`, beyond the files the five items name — judge whether each is a required correction under WAY-33 or a widening of scope; (3) the check's rule against item 3 and Questions 1–4 word by word, and the fifteen links of item 4 against the invariants' *Derives from*.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way` populated, and the dependencies those checks need installed as the product's own rules give, before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and command of a probe that shows a finding among them, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.

## What to return

Your report at the path above, as `task-cycle/review/SKILL.md` gives it (first line `PASS <sha>` or `FAIL <sha>`; graded findings, each with its slice or none, its mark of contradiction with the settlements where one applies, and the reviewer's own scope judgment), with its **Unread material**, **Searches not found or unclear**, the number of decisions you read whole, and each check you ran with its command and exit code. Do not run the product's full gate. Return the report's first line, a one-line check result, the changed files with line counts and the report's path.
