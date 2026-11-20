# Handoff — review of the whole change

You review the whole change of a task of the-way as an agent that did not make it (agent type
`the-way-stage`, on the strongest class). The person who requested this cycle delegated intermediate
choices to the orchestrator; no answer in this handoff is that person's approval.

## Where you work

- Worktree: the task's worktree, branch `task/decision-length-check`.
  Read-only: you change no tracked file and make no commit. Work from the worktree's root; the-way
  here is the worktree itself.
- Your directory for working copies: `.runs/review-whole/`.
- Your report goes to `.runs/task-cycles/decision-length-check/reports/review-whole-report.md`; its
  first line is `PASS <sha>` or `FAIL <sha>` (or `questions`). That file is the input of the cycle's
  scripts (`task-cycle/remarks_check.py` reads it). Where the harness refuses the write, return the
  report whole as your answer.
- The file `cycle.md` and other files of `.runs/task-cycles/decision-length-check/` are not yours to
  read, except those this handoff names: `task.md`, `reports/author-report.md`, and the file you
  write your selection's index to if you choose that directory.

## Method

Read `task-cycle/review/SKILL.md` whole, then `task-cycle/review/whole_change.md` as it directs. You
review **the whole change**.

- Range: base `1b6fe1c1` to head `e8b76178` (`git diff 1b6fe1c1..e8b76178`, `git log 1b6fe1c1..e8b76178`);
  confirm `git rev-parse HEAD` is `e8b76178`. Four commits: `0f738707` (a move of code with no change
  of behaviour), `58f9937d` (WAY-05), `9dc811af` (the check and its tests), `e8b76178` (template and
  READMEs).
- The frozen task: `.runs/task-cycles/decision-length-check/task.md`. Read it whole; it is what you
  review against: every item of *To do*, every answer of *Questions to settle* (rejected variants
  must not be restored), *Settlements to record* rows 1–2 and *Decisions in play* (the quoted sentence
  of WAY-05 and its five changes), and *Out of scope*.
- The author's report: `.runs/task-cycles/decision-length-check/reports/author-report.md`. Its claims
  are to be verified, not taken as evidence.
- No spec, no plan: one author made the change, with no slices. The change was not reviewed before
  now; there is no earlier Minor or out-of-scope finding to carry.
- Answers of the orchestrator at start: the change touches no trust boundary and holds no operation
  that cannot be undone. The author's choice to move the readers of an entry's text out of
  `foundation_check.py` into `elements/common/foundation_text.py` (to keep the file within the 1200
  lines of WAY-385), keeping the names importable from `foundation_check`, is the orchestrator's
  accepted reading of the task's carried question; judge whether it is sound, not whether it was
  asked.

## What to notice about what the author did not read

The author's report says it did not run the selection of "Reading the foundation" and read part of
`test_foundation_check.py` and WAY-12. You select your own foundation and guidelines (your method
says how), so that gap is yours to close: select by the parts the change touches — `decisions`,
`elements-common`, `agent-instructions` and the root `README.md` (see `foundations/part_map.md`) — and
read the guidelines of the-way's own code and tests that apply (`guidelines/coding.md`,
`guidelines/coding-check.md`, `guidelines/testing.md`, and `guidelines/coding-shared-module.md` for the
new module). The author also left unchanged three texts that say "one to three binding sentences"
(`product-guidelines/styleguide/template.md`, `product-guidelines/testing/template.md`, and a decision
in `foundations/decisions.md`) as still true; judge that, and whether another place that describes
what the check reports needs the new report (the task's point 3 names four).

## Your report

As your method gives it: its first line, graded findings (each Critical, Important or Minor; a
Minor finding within the task named as such, one outside the task's scope named as outside it), the
slice of each finding (none here), the mark `Contradiction: yes` on a blocking finding that
contradicts the settlements, the checks you ran each with command and exit code, how many decisions
of your index you read whole, **Unread material** (what you selected and left unread or read in part,
or `none`), **Searches not found or unclear** (each thing you looked for and did not find or found
unclear, or `none`), and your working copies. You do not run the product's full gate
(`python -B gate/run_tests.py` with no directory): its run is the orchestrator's or CI's (WAY-160);
you may run the focused runs of single directories and the check of the foundation.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.
