# Handoff — the review of the whole change, second dispatch (`review-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead in this handoff is that person's approval. The human reviews the
request, not the steps. You did not make this change; grade and scope of every finding are yours.

## Where and what

- Worktree (your working directory, the process root): `the task's worktree`, branch `task/recommendation-not-below-goal`. The process is the-way itself: there is no `.the-way` submodule and the task moved no pin. Read only; never write in the main checkout `the main checkout of the repository`.
- Method: `task-cycle/review/SKILL.md` in the worktree. Read it whole, and a file it names, one beside it included, only when the step or variant that names the file comes. Variant: the review of the whole change (it names `whole_change.md`).
- Range: base `301e4eae1111310ccd80e466f62ea01838b9ff88` to head `42298f2a81d8d4600b7a3769ab5ab6795510f0f6` (two commits: the author's change `7c2502a7` and a fix `42298f2a` of an earlier review's findings; one author, no plan, no slices, so no slice had a review of its own: you judge the whole, the fix included). Compute the diff yourself and confirm `git rev-parse HEAD`.
- Frozen task: `.runs/task-cycles/recommendation-not-below-goal/task.md` — read it whole. No spec, no plan. Cover every item of its *To do* (1–3), each answered question (1–4), both rows of *Settlements to record* and *Out of scope*.
- Reports of the author, sets of claims to verify, not evidence: `.runs/task-cycles/recommendation-not-below-goal/reports/author-report.md` (the change) and `.runs/task-cycles/recommendation-not-below-goal/reports/author-fix-1-report.md` (a fix of an earlier review's findings; it also puts one question to the human, which the author could not settle from what the human accepted, and left standing). You are a fresh reviewer: you read no earlier review's report.
- Answers of the start: trust boundary no; irreversible operation no; open design choice none; execution route one author without a plan.
- You select your own foundation and guidelines (`elements/common/way_of_working.md` "Reading the foundation", `product-guidelines/reading.md`) and state in your report how many decisions you read whole. The orchestrator's selection, which you are free to widen: WAY-113 (the entry the change alters, whole, with *Rejected*), WAY-166 (judge yourself whether it collides with the new rule, and the case where the material's goal is an agent's check of the running product), WAY-120, WAY-35, WAY-33, WAY-123 and the derived decisions that name WAY-113.
- `cycle.md` and the other files of `.runs/task-cycles/recommendation-not-below-goal/` are not yours to read, save the frozen task, the author's report and this handoff.
- You run no gate (WAY-160). Run the foundation check (`python -B elements/common/foundation_check.py`) and anything you need to judge a claim, and record each with its command and exit code.

## Report

Write the report in full to `.runs/task-cycles/recommendation-not-below-goal/reports/review-whole-2-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`. Return that first line, your checks with their commands and exit codes, and the report's path. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), so the harness's refusal of a file whose name starts with `report`, `summary`, `findings` or `analysis` does not apply to this name; if the write is refused all the same, return the report whole as your answer. It holds **Unread material** (what this handoff names, or what you selected, that stayed unread or read in part, or `none`) and **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), and the number of decisions you read whole.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/review-whole-2/`.
