# Handoff — the fix of a review's findings (task cycle of the-way)

The same delegation and place as `reports/author-handoff.md` (you are the same author, resumed on
the same branch and worktree; nobody else writes in it).

- Method: `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**. Re-read the
  part of that `SKILL.md` the variant names.
- Findings file, read whole: `reports/review-whole-findings.md` (under
  `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/`), the reviewer's words: two
  blocking findings (I-1, I-2), each marked `Contradiction: yes`, and after them four Minor
  findings (M-1 to M-4) of the review of the whole change within the task. Fix all six in this one
  fix. A finding you hold wrong you answer with evidence in your report instead of changing it.
- The reviewed head is `60561fba`; your fix's range runs from it.
- The frozen task stays the source of what the settlements say (`task.md`, same directory): I-1 and
  I-2 are findings that the change departs from it, so narrow to its words; widen nothing (its
  *Not chosen* and *Out of scope* still bind). Where you correct WAY-229 or WAY-136, keep the limits
  of the foundation check and carry the change into every place the finding names and every other
  place that restates the same words (search once, as before).
- Run the affected checks again (the foundation check, the instruction check, the tests of the
  directories you touch) with commands and exit codes; not the product's gate.
- Report path: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/author-fix-1-report.md`
  (it is the input of `task-cycle/remarks_check.py`; write it there). Its first line is yours. It
  holds, as before: status, commits, the own-work check, each check with command and exit code,
  for each finding what you did or why you hold it wrong, **Unread material** and **Searches not
  found or unclear** (each `none` where so).
- The files of the record directory other than the two named above are not yours to read.

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

Your directory for working copies: `.runs/author/` (as before).
