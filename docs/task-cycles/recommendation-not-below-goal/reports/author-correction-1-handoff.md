# Handoff — correction 1 for the human's remarks (`make-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. The remarks below are the human's own (given through the person's day adviser, in the human's name); they bind. No other answer or go-ahead here is the human's approval.

## Where and what

- You are the one author, resumed. Worktree and branch: `the task's worktree`, `task/recommendation-not-below-goal`; head `e5a69f85` (the code is that of `3130f1d9`; the two commits after it only add and remove the record's copy). The target branch has not moved since the base `301e4eae`, so nothing is merged or renumbered.
- Method: `task-cycle/change/SKILL.md`, variant **a correction for the human's remarks**. Read `task-cycle/skill/foundation_step.md` again for the sentence on a precedence between two decisions.
- The remarks: `.runs/task-cycles/recommendation-not-below-goal/reports/correction-1-remarks.md` — read it whole. They answer the question of the request (item 1 of *Needed from you*, which is the collision of the new paragraph of WAY-113 with WAY-166 that you returned twice) with way **a**, in a wording of the relation they give: WAY-166 is not an exception to the new rule but the answer accepted in advance to the question whether to change the goal, which the new rule asks anyway where no way reaches the goal; in the technology step, where the goal is an agent's check of the running product and no option gives it, the goal is openly narrowed to the human's check — the one sentence WAY-166 already requires — and only against the goal so narrowed does the question recommend the cheapest option. They accept items 3 and 4 of the request (the place of the new paragraph and the eleven added words). Item 2 (the return step and the reconciliation) is the orchestrator's.
- The frozen task, the reviews and your earlier reports are as before: `.runs/task-cycles/recommendation-not-below-goal/task.md`, `reports/review-whole-2-report.md`, `reports/author-fix-2-report.md`. You read no other file of the record directory.

## What to do

1. Record the precedence as the remarks word it and as WAY-25 and `foundation_step.md` give it: in the decision that prevails or narrows (the remarks speak of WAY-166 and of its relation to the new rule; you choose the form: `narrows WAY-113` in WAY-166's *Relations*, its binding sentences stating the area in the remarks' words, its *Verification*, *Rationale* and *Rejected* aligned — the line of *Rejected* that calls the refusal "an exception to WAY-113" no longer says what the remarks say). Mark the entry `the cycle's`, and keep in your report, quoted, the passages of the remarks that give the outcome (WAY-25).
2. Check each place that restates WAY-166 or the new paragraph for a mismatch with that wording and correct only what no longer matches — `project-level/technology/settle.md`, `project-level/definition_template.md`, the new paragraph of WAY-113 and the bullet of `elements/common/way_of_working.md` — in the same change (WAY-33); add nothing the remarks do not give, and no new step for a choice with no recommended option (that was way c's). The remarks say way a costs one relation and a sentence; if you find that the wording needs more than that, say what and why in the report instead of widening it.
3. Keep every paragraph of every binding sentence you touch within three sentences and 300 words, and the binding part within 600 words; run `python -B elements/common/foundation_check.py` and the other checks your change reaches (`python -B gate/run_tests.py elements/common`, `python -B instruction-files/check_instructions.py .`), each with command and exit code, and keep each line you add at 100 columns or fewer.
4. Commit by path, in English. Do not make the return step now: the orchestrator dispatches it after the review of this correction.

## Report

Write the report to `.runs/task-cycles/recommendation-not-below-goal/reports/author-correction-1-report.md`; return its status, your commits, a one-line check result and its path. The report holds **Unread material** and **Searches not found or unclear** (each `none` where nothing), your own-work check, the meaning sentences of each entry you changed or wrote, in English and in Polish, marked `row 1`, `projected` or `the cycle's`, and the passages quoted that WAY-25 asks for. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py`); if the write is refused all the same, return the report whole as your answer.

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

Your directory for working copies: `.runs/author/` (the same as before).
