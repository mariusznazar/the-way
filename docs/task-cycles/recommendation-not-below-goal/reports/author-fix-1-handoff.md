# Handoff — the fix of the review's findings (`make-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead here is that person's approval.

## Where and what

- You are the one author, resumed. Worktree and branch as before: `the task's worktree`, `task/recommendation-not-below-goal`; reviewed head `7c2502a73f8360d9e47af85863c522392ec6c192`.
- Method: `task-cycle/change/SKILL.md`, variant **the fix of a review's findings**; read the part of it that variant names, and `task-cycle/skill/foundation_step.md` again for the sentence on a collision with a current entry.
- Findings file: `reports/review-whole-findings.md` (that is, `.runs/task-cycles/recommendation-not-below-goal/reports/review-whole-findings.md`): two blocking findings (I1, I2) and one Minor finding within the task (M1), in the reviewer's words. The full review is `reports/review-whole-report.md`; read it whole too.
- Your fix range runs from the reviewed head. Commit by path, in English.

## What to do with each finding

- **I2** and **M1**: fix them. For I2 name the question in the second paragraph ("the question against that choice") or move the new paragraph — your choice, say which and why; the same words must not be restated differently in a way that changes a binding sentence (WAY-263).
- **I1**: the reviewer holds that the new paragraph and WAY-166 (with `project-level/technology/settle.md` and `project-level/definition_template.md`) give opposite outcomes where the material's goal is an agent's check of the running product, and that nothing the human accepted gives the outcome. First judge that against what the human accepted — the frozen task (`.runs/task-cycles/recommendation-not-below-goal/task.md`: *Questions to settle* with their sources, the *Settlements to record* rows) and WAY-25. If a passage of it gives the outcome, write the precedence in the decision that prevails as `foundation_step.md` says, quote the passages in your report, and mark the entry `the cycle's`. If none does, make no choice between the reviewer's three ways: the orchestrator does not settle it either (it is a collision with a current entry other than as the task commands). Then leave the wording of I1 as it is, return the status `blocked` with the question for the human — the ways, what each costs, the cost of undoing each, and your recommendation with its weak point, as "How a skill asks" gives it (WAY-113) — and say in the report that I2 and M1 are fixed and committed and that only I1 waits.
- Run the checks the fix reaches again (`python -B elements/common/foundation_check.py` and the others you ran before that the fix touches), each with command and exit code, and answer with evidence any finding you hold wrong. Your own-work check as before.

## Report

Write the report to `.runs/task-cycles/recommendation-not-below-goal/reports/author-fix-1-report.md`; return its status, your commits, a one-line check result and its path. The report holds **Unread material** and **Searches not found or unclear** (each `none` where there is nothing) and, for every entry you changed, the meaning sentences as before. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py`); if the write is refused all the same, return the report whole as your answer.

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
