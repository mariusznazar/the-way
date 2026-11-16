# Handoff to the one author — the return step

The change is accepted by its reviews (the review of correction 1 passed at `47a47fe`, after the review of
the whole change and its fix). The return step now runs, as the human's remarks (item 2) and
`task-cycle/skill/blocked_finding.md` require. Same worktree and branch, head `47a47fe`; the target branch
has not moved. Your directory for working copies: `.runs/author-return/`. Your report:
`docs/task-cycles/audit-answers-contradiction-after-code/reports/author-return-report.md`.
Delegation as before: ask the human nothing, do not run the product's full gate.

- The method: `task-cycle/skill/return_step.md` — read it whole, and `task-cycle/skill/foundation_step.md`
  and the `SKILL.md` of an element, at the path the foundation step gives, when you write an entry of that
  element. The route of the cycle: one author without a plan; you are the author.
- What to compare with the code at `47a47fe` (range `aba5ee92a0734c2e775cc69662af669bf6455795..47a47fe`,
  the frozen task `docs/task-cycles/audit-answers-contradiction-after-code/task.md`): the entries the change
  wrote or changed — WAY-403, WAY-404, WAY-337 (the new paragraph), WAY-344 (the narrowing) and the line added
  to the part map's *Trust boundary* of `process-audit` — the entries of the task's *Decisions in play*
  (WAY-337, WAY-339, WAY-135, WAY-263), the entries the search of the foundation found, and the part map of
  the touched parts. Two corrections after your first turn changed code and instruction texts after the
  entries were written: the reading of *Discarded attempt* now reads a list of entries only where the first
  one stands at the entries' indent and no plain line stands at their indent or less (otherwise it reads the
  whole item as one attempt or gives `unknown`), and the four places that write a second discarded attempt say
  the earlier attempt is rewritten as an entry too. Check each sentence of WAY-404 and WAY-403 and of the
  narrowing of WAY-344 against this final code, and the record template's two items against it; correct what
  no longer matches in the same change, with no code change unless a mismatch is a defect of the code, which
  you return to the orchestrator instead of fixing.
- The human's answer accepts the narrowing of WAY-344 (item 5) as written; do not change its meaning. Do not
  fix the Minor findings of the reviews of the correction (M-1, M-2, M-3, O-1 of
  `reports/review-correction-report.md`): the cycle carries them to the request.
- Where the return step changes nothing, say so in the report with what you compared. Run the focused checks
  your changes need (a changed foundation entry: `python -B elements/common/foundation_check.py` without
  `--skip-test-citations`), each with command and exit code. Commit by path, messages in English.

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

The return step's report as `return_step.md` gives it (the fields of the record's *Return step*), with
**Unread material**, **Searches not found or unclear**, and the commits you made. Return status, commits, a
one-line check result and the report's path.
