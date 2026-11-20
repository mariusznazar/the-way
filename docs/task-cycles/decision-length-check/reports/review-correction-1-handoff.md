# Handoff — the review of correction 1 and the reading of six decisions

You are a fresh reviewer (agent type `the-way-stage`, on the strongest class) that did not make the
change and did not write any earlier review of it. The person who requested this cycle delegated
intermediate choices to the orchestrator; no answer here is that person's approval.

## Where you work

- Worktree: the task's worktree, branch `task/decision-length-check`. Read-only: you change no tracked
  file and make no commit. Work from the worktree's root; the-way is the worktree itself.
- Your directory for working copies: `.runs/review-correction-1/`; remove it before you return.
- Your report: `.runs/task-cycles/decision-length-check/reports/review-correction-1-report.md`, its first
  line `PASS <sha>` or `FAIL <sha>` (or `questions`). That file is the input of the cycle's scripts
  (`task-cycle/remarks_check.py` reads it). Where the harness refuses the write, return the report whole.
- The record's other files are not yours to read, except those this handoff names.

## Method

Read `task-cycle/review/SKILL.md` whole and `task-cycle/review/fix.md` (the review of a correction made for
the human's remarks, which the method names). The remarks stand in place of a findings file:
`.runs/task-cycles/decision-length-check/reports/correction-1-remarks.md`. The author's report of the
correction: `.runs/task-cycles/decision-length-check/reports/author-correction-1-report.md`; its claims are
to be verified, not taken as evidence.

## Two jobs

1. **The correction's range**: from `2ffff547` to `35796540` (`git diff 2ffff547..35796540`,
   `git log 2ffff547..35796540`; confirm `git rev-parse HEAD` is `35796540`). Remark 1 asks for
   `elements-common` in *Applies to* and `elements/common/` in *Where in code* of
   `guidelines/coding-shared-module.md`, and nothing else of that file. Judge whether the range meets the
   remark and no more, with the file's form against the guidelines and the tests that read it.
2. **The reading of remark 2**: read each of these six decisions of `foundations/decisions.md` **whole** —
   binding sentences, fields, *Rationale* and *Rejected*, as an entry read whole is the range of lines from its
   heading to the next heading — against the new rule of WAY-05 (the paragraph limits of three sentences
   and 300 words, the error for a decision a change adds or whose binding sentences it alters, a different
   division into paragraphs included, and the list for any other) and against the new check that carries it
   (`check_length`, `excess` and `base_paragraphs` in `elements/common/foundation_check.py`, with
   `elements/common/foundation_text.py` beside it), and report any collision of any of the six with them as a
   finding, graded by `review-change`:
   WAY-344, WAY-134, WAY-18, WAY-19, WAY-150 and WAY-321. The reason the human gives: the next task in the
   queue changes WAY-344, WAY-134 and WAY-150, and WAY-19 gives the rule of a paragraph for a part of
   another question, on which the paragraph limit stands. WAY-05 and the code are the change of the whole
   task (range `1b6fe1c1..35796540`), reviewed earlier: read them as the reference of this reading and as
   far as it needs, and judge a collision, not the whole change again. A finding of this reading is a finding
   of the request like any other; say for each decision what you read whole and whether you found a
   collision.

The twelve entries over the limit today (WAY-134 among them) are shortened by another task and are not
a finding of this reading; a collision of an entry's *content* with the new rule is.

## Your report

As your method gives it: its first line; graded findings (each Critical, Important or Minor; Minor
within or outside the task's scope), the mark `Contradiction: yes` on a blocking finding that contradicts the
settlements, the checks you ran with command and exit code (the focused runs of single directories and the
check of the foundation are allowed; **not** the product's full gate), **Unread material** with, for the
six decisions, each read whole or not and what stayed unread, **Searches not found or unclear**, and your
working copies. The task is `.runs/task-cycles/decision-length-check/task.md` for what the change must not
break.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.
