# Handoff to the reviewer of the return step — task `walkthrough-in-running-product`

You review one range of a task cycle of the-way as an agent that did not make it, with `review-change`
(read `task-cycle/review/SKILL.md` whole; the return step's commits are reviewed as its section 2 gives,
against the task and the foundation entries the return step writes or corrects). Read-only; return
PASS or FAIL with graded findings and the checks you ran. No full gate, no next stage, no question to
the human.

- Worktree `the task's worktree`, branch
  `task/walkthrough-in-running-product`. Range: `cdbde3d2..83aa64db` (confirm `git rev-parse HEAD` is
  `83aa64db...`); compute the diff and log yourself. One commit, two files:
  `foundations/decisions.md`, `task-cycle/skill/request_template.md`.
- What the return step is (its method, to judge the range against):
  `task-cycle/skill/return_step.md`, read whole. The author's report, a set of claims to verify:
  `.runs/task-cycles/walkthrough-in-running-product/reports/author-return-report.md` — it says it
  changed the title and one sentence of kind 8 of the request template, the question of WAY-408 and
  re-flowed lines of the log, and wrote no invariant, environment fact, glossary term or part-map change.
  Verify: that the re-flow changed no word (compare the text with words joined, before and after), that
  the title/question/"its author or executor" changes agree with WAY-408 (read whole), WAY-287 and the
  task, that `python -B elements/common/foundation_check.py` is clean, and that nothing the task or the
  foundation requires of the return step was missed (an entry for a source outside the product, a
  glossary term for a word in a changed meaning, a row of *Settlements to record*; judge by the task's
  rows 1-11 and `return_step.md`).
- Frozen task, read whole: `.runs/task-cycles/walkthrough-in-running-product/task.md`. Earlier rounds:
  the whole change passed after one fix (`PASS cdbde3d2`, range `9cffc9ba..cdbde3d2`); you review only
  the return step's commit, but a mismatch of the change with the entries that you find while judging
  the commit is yours to report.
- Trust boundary: no. You select the foundation you need for this range yourself by "Reading the
  foundation" in `elements/common/way_of_working.md` (the decisions WAY-406, WAY-407, WAY-408, WAY-121,
  WAY-319, WAY-287, WAY-289, WAY-25 read whole as far as the range touches them).
- Report: `.runs/task-cycles/walkthrough-in-running-product/reports/review-return-report.md`, first line
  `PASS <sha>` or `FAIL <sha>`, then findings graded as the method gives (a blocking finding with
  `Contradiction: yes|no` against the task's settlements or the foundation), checks with command and exit
  code, **Unread material**, **Searches not found or unclear**, working copies. Return the first line,
  the changed files with line counts, the checks and the path.
- Your directory for working copies: `.runs/review-return/`.
- The files of the cycle's record directory other than the three this handoff names (the task, the
  author's return report, your own report), `cycle.md` among them, are not yours to read.

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
