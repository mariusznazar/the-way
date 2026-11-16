# Handoff to the one author — the fix of the review of the whole change

## What this is

The review of the whole change returned `FAIL ab2c8c801b2ba9170a00ed6056b8b7c56b062868`
(`reports/review-whole-report.md`). The findings to fix — one blocking, two Minor within the task —
stand in `reports/review-whole-findings.md`, in the reviewer's words. Method: `task-cycle/change/SKILL.md`,
variant "the fix of a review's findings". Same worktree and branch as before; head to fix from:
`ab2c8c801b2ba9170a00ed6056b8b7c56b062868`. Your directory for working copies: `.runs/author-fix/`.
Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-fix-report.md`.
You are the one author and work on your own class; the delegation is as in your first handoff:
ask the human nothing, and do not run the product's full gate.

## What to do about each finding

- **I-1 (blocking, WAY-344).** The orchestrator has weighed the finding and the author's own
  concern 1: the reading is probably the right one, and the decision's text lacks the case. The route
  that WAY-30 gives for a contradiction that shows during implementation, and the reviewer
  recommends, is: **propose on the task branch a narrowing of WAY-344** — edited in place in
  `foundations/decisions.md`, as the decisions' skill gives — that names the items of a cycle record
  that the command that counts the audit reads as of an earlier form where they are missing: at least
  *Discarded attempt* and *Review rounds*, and every other item of `cycle.md` the command reads
  (*Process pin*, *Plan*, *Slices returned too large*, *Process remarks on the-way*; take the list
  from the code, not from this sentence), giving the values that need them as unknown with a reason
  that names the item, with no line `Error:` and no change of the exit code. Its *Verification*
  names the tests that hold it. Write the narrowing as `the cycle's` entry change as
  `task-cycle/skill/foundation_step.md` gives, with its two sentences of meaning in your report, so
  that the request puts it before the human, who accepts it by merging (WAY-30, WAY-114). Do not
  change the code to give `Error:` and exit 1 for a missing item: WAY-344's own rationale argues
  against it. If you hold that the narrowing is a meaning beyond what you may write, or that the
  finding is wrong, say so in the report with the evidence and return `blocked` or answer the
  finding; do not leave the contradiction unhandled. Search the foundation once for entries the
  narrowing touches (WAY-33) and make the tests that hold the reading cite it as the decisions'
  skill gives for a test that holds a sentence.
- **M-1 (Minor, within the task).** Give the record template a form for a cycle that discards two
  attempts, and let the count read `yes` where any marker is `open design choice`; where a form of
  two markers cannot be read, give it a reason of its own, never the false reason "holds no marker of
  its reason". Make the two places of `task-cycle/skill/SKILL.md` and `task-cycle/skill/reserved_return.md`
  and `task-cycle/skill/correction.md` write it, and add the tests. The task's *To do* 6 gives three
  markers and one place; keep them, and write the smallest form that holds two discards, naming the
  choice in your report. WAY-405 follows the form where it states it.
- **M-2 (Minor, within the task).** Reword the sentence of WAY-405 as the finding gives it ("an item
  that reads neither `none` nor a marker").

## Checks

Run the affected focused checks again — the directories you changed and
`python -B elements/common/foundation_check.py` without `--skip-test-citations` — and give each
with its command and exit code, the exit code of a command that goes through a pipe included. Answer
with evidence a finding you hold wrong. Commit by path, messages in English.

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

## The report

As `make-change` gives it for a fix, with **Unread material** and **Searches not found or
unclear**, the own-work check and the fix's range from `ab2c8c801b2ba9170a00ed6056b8b7c56b062868`.
Return its status, commits, a one-line check result and the report's path.
