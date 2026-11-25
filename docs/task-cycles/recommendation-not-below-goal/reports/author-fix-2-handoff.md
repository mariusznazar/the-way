# Handoff — the second fix of the review's findings (`make-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead here is that person's approval.

## Where and what

- You are the one author, resumed. Worktree and branch as before: `the task's worktree`, `task/recommendation-not-below-goal`; reviewed head `42298f2a81d8d4600b7a3769ab5ab6795510f0f6`.
- Method: `task-cycle/change/SKILL.md`, variant **the fix of a review's findings**.
- Findings file: `reports/review-whole-2-findings.md` (`.runs/task-cycles/recommendation-not-below-goal/reports/review-whole-2-findings.md`): the one blocking finding (I1) and two Minor findings within the task (M1, M2), in the reviewer's words. The full review: `reports/review-whole-2-report.md`; read it whole too. It is a fresh reviewer's review of the whole change, made on the strongest class (the earlier review ran on a class lower than asked); its I1 is the finding you returned to the human in your first fix.
- Your fix range runs from the reviewed head. Commit by path, in English.

## What to do with each finding

- **I1**: it stands as in your first fix. You judged then that no accepted text gives the outcome, and the new reviewer agrees; it recommends another way than yours (the goal rule prevails only where the material's goal is itself an agent's check of the running product, recorded in WAY-113 as `narrows WAY-166`, with the same area in `settle.md` and `definition_template.md` and a step in `settle.md` for a choice with no recommendation; weak point and cost in its words). Change nothing for I1. Return `blocked` again with the question for the human: the ways (yours and the reviewer's among them, each with what happens once it is chosen, what it costs and what undoing costs), and say where your recommendation and the reviewer's differ and which you would give now and why, with its weak point (WAY-113). The orchestrator carries your question into the request.
- **M1** (`prepare.md` raggedness): fix it by re-wrapping, no word changed.
- **M2** (the question whether to change the goal, asked where no refinement is under way): the reviewer grades it Minor within the task, and the task's own words ("with the human in the same refinement") are its source. Fix it if a few words say where such a question goes inside a task's cycle by a route the foundation already gives (WAY-30, WAY-315, a blocked draft request) without a new rule and without changing what the task settles; if the fix would need a rule the task and the foundation do not give, do not write it: say so in the report with evidence, as a finding you hold wrong or beyond the task (the review of the fix will judge). Keep the paragraph within three sentences and 300 words, and `foundation_check.py` quiet.
- Run the checks the fix reaches again (`python -B elements/common/foundation_check.py` and the others that the fix touches), each with command and exit code. Your own-work check as before.

## Report

Write the report to `.runs/task-cycles/recommendation-not-below-goal/reports/author-fix-2-report.md`; return its status, your commits, a one-line check result and its path. The report holds **Unread material** and **Searches not found or unclear** (each `none` where nothing) and the meaning sentences of every entry you changed. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py`); if the write is refused all the same, return the report whole as your answer.

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
