# Handoff — reviewer of the return step

The person who requested this cycle delegated intermediate choices to the orchestrator; nothing here is that person's approval. You review the commit of the return step as an agent that did not make it.

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. You change nothing in it.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant **a later change to an open request / the return step's range**; read it whole and a file it names when the step names it.
- Range: `f0482d0..3cf54a5` (one commit, `3cf54a5`: an edit of the *Verification* of WAY-385 in `foundations/decisions.md` and one `decision:` line in `agent-instructions/test_size_invariant.py`). The return step's report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/return-step-report.md` (what it compared and why it wrote only this); its handoff: `reports/return-step-handoff.md`; the foundation step it follows: `task-cycle/skill/foundation_step.md`; return step rules: `task-cycle/skill/return_step.md`.
- Judge it against the task (`.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`) and the entries the return step writes or corrects (WAY-385 and, by reading, the entries it compared). Trust boundary: yes for the change as a whole; this range touches no boundary file. Irreversible operation: no.
- Your directory for working copies: `.runs/review-return/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/review-return-report.md`, first line `PASS <sha>` or `FAIL <sha>`. Do not run the full gate; `python -B elements/common/foundation_check.py` and the focused run of `agent-instructions` are yours.

## Working copies (word for word from the orchestrator's skill)

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




## What you return

First line, graded findings as the method gives, checks with command and exit code, **Unread material**, **Searches not found or unclear**, the working-copies line, and a short return: status, report path, changed files with line counts, one-line check result.
