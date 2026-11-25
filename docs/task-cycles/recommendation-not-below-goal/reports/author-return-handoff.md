# Handoff — the return step (`make-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead here is the human's approval.

## Where and what

- You are the one author, resumed. Worktree and branch: `the task's worktree`, `task/recommendation-not-below-goal`; head `e08834e4317de5961519bed739b02f49b7a89d0f`, reviewed `PASS` by the reviewer of the whole change (`reports/review-correction-1-report.md`; read it whole). The code is that of the task's base `301e4eae1111310ccd80e466f62ea01838b9ff88` plus your three commits `7c2502a7`, `42298f2a`, `3130f1d9` and the correction `e08834e4`; the commits `8f29f4f1` and `e5a69f85` only add and remove the record's copy.
- Stage: the **return step**. Read `task-cycle/skill/return_step.md` whole and, since the return step writes as the foundation step writes, `task-cycle/skill/foundation_step.md` whole, and the `SKILL.md` of an element at the path `foundation_step.md` gives when you write an entry of that element. The method is `task-cycle/change/SKILL.md`; no variant row applies to this stage.
- The frozen task: `.runs/task-cycles/recommendation-not-below-goal/task.md`. The human's remarks of correction 1: `.runs/task-cycles/recommendation-not-below-goal/reports/correction-1-remarks.md`. Your report of the correction: `.runs/task-cycles/recommendation-not-below-goal/reports/author-correction-1-report.md`.

## What the reviewer left for the return step

The review of the correction (PASS) lists two Minor findings within the task; the cycle does not fix a Minor finding of a review of a correction, but your return step compares the foundation entries and the files and corrects whatever no longer matches, so judge each by `return_step.md`: correct what the correction made false in a file that restates it, and only that; name what stays and why.

- N1: `project-level/technology/settle.md:34-38` and `project-level/definition_template.md:242-248` repeat the older decision's rule (WAY-166) without its new third sentence (where the material's goal is an agent's check of the running product, the one sentence narrows that goal openly to the human's check, and the recommendation goes against the narrowed goal). The reviewer holds that an agent following them still acts rightly, and that a reader of those files alone does not learn the narrowing.
- N2: outside the area of that decision, a technology choice where no option reaches the goal still gets a question with no recommendation, and `settle.md` has no step for the risk tests or for "you choose" in that case. The reviewer grades it Minor and notes that the human chose way a over way d, which left that step out. Do not write such a step: it is not in the human's remarks.

Report what you compared and what you corrected or left, by the sections `return_step.md` gives. Where the return step commits, a fresh reviewer reviews its range (the orchestrator dispatches it); where it commits nothing, say so.

## Checks

Run what your return step reaches, each with command and exit code (at least `python -B elements/common/foundation_check.py`, and `python -B gate/run_tests.py <directory>` for a directory a changed file is read by). Your own-work check as before.

## Report

Write the report to `.runs/task-cycles/recommendation-not-below-goal/reports/author-return-report.md`; return its status, your commits, a one-line check result and its path. It holds **Unread material** and **Searches not found or unclear** (each `none` where nothing) and the meaning sentences of each entry you changed. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py`); if the write is refused all the same, return the report whole as your answer.

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
