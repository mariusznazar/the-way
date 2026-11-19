# Handoff - the return step (stage: return step, written as the foundation step writes)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never ask the
human; a question goes back to the orchestrator in your report. Never label an answer as the human's approval.

## Where you work

- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Your base, the head of the finished change: `2e066ab4f6f7a0b30b29ed09bbafbaf61b6fea38`.
- Your directory for working copies: `.runs/return-step/` of the worktree. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/return-step-report.md`.
- `cycle.md` and other files of the record directory are not yours to read, except those this handoff names.

## Your method and stage

- Method: `task-cycle/change/SKILL.md` of the worktree (`make-change`), read whole, and `task-cycle/skill/return_step.md`
  and `task-cycle/skill/foundation_step.md`, each read whole - the return step writes as the foundation step writes. Read
  the `SKILL.md` of an element (`elements/decisions/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`,
  `elements/glossary/skill/SKILL.md`, `elements/part-map/skill/SKILL.md`, `elements/environment-facts/skill/SKILL.md`) only
  when you write an entry of that element, with the element's `template.md`, `elements/common/rules.md` and
  `elements/common/way_of_working.md`.
- Boundary: you compare and correct foundation entries and the part map against the code; you write no code except where
  a correction of an entry requires a one-line change of a test line `decision:` that quotes it. Commit only what you
  correct, by path (`git add <path> ...`, never `git add -A`, `.` or `commit -a`), with English messages. Where nothing
  no longer matches, commit nothing and say so with the evidence. Do NOT run the full gate; focused runs of one directory
  you may make.

## What you compare with the code

The change, base `d69fb20b` to head `2e066ab4f6f7a0b30b29ed09bbafbaf61b6fea38` (read `git log` and `git diff` of the range; the reformatting commit
`015ce05c` is formatter output only), made these entries and files: decisions WAY-382, WAY-385, WAY-379 (its
*Verification*), WAY-145, WAY-350, WAY-339, WAY-09 (its *Verification*); invariants `formatter-layout` and
`own-foundation-check-report` (new), `ruff-blocking-rules` and `function-and-file-size` (now `Violated: no`),
`gate-times-refuses-impossible-entry` and `audit-series-script-paths` (reworded); the part map (`repository` gained
`/.git-blame-ignore-revs`; `task-cycle` gained `task-cycle/stage_transcripts.py` and `process-audit` gained
`process-audit/record_reading.py`, `problem_register.py` and `audit_shared.py` among its *Trust boundary* files);
`guidelines/coding.md` (`### Formatter`), `guidelines/coding-shared-module.md`, `README.md`,
`installation/README.md`. The task (`.runs/task-cycles/code-order-formatter-linter-size/task.md`, read whole) names these
decisions in play: WAY-382, WAY-385, WAY-379, WAY-205, WAY-51, WAY-380, WAY-381, WAY-16, WAY-08, WAY-03, WAY-233, WAY-95,
WAY-145, WAY-350. The plan, for what it says the return step should compare (`.runs/task-cycles/code-order-formatter-linter-size/plan.md`,
read the *Foundation entries* section and the *Choices*) and the planner's concern 7: nine `.md` files mention
`task-cycle/cycle_stages.py` as the script that measures the cost, and the description of
`process-audit/test_audit_series_scripts.py`.

Compare, as `return_step.md` gives, each entry above, the entries the task names, and the part map of every touched part
(every part that holds Python code, `repository`, `decisions`, `invariants`) with the files of the repository: that the
files each *Files* line names exist, that the *Depends on* lines match the imports of the new modules
(`process-audit/audit_shared.py`, `record_reading.py`, `problem_register.py`, `version_analysis.py`, `audit_report.py`,
`task-cycle/stage_transcripts.py`; the test of the invariant `cross-part-imports` holds this), that no sentence of an entry
still says a number or a state that the change altered (thresholds 80/1000, "violated", "no formatter", "none - WAY-382", an
old name of a moved function), and that the `.md` files that name `task-cycle/cycle_stages.py` as the script that measures
the cost say that the cost script spans `task-cycle/stage_transcripts.py` as well, where WAY-339 means the cost series - leave
the places that name it as the writer of `stages.md`. Search the foundation and the guidelines for the old phrases ("80
lines", "1000 lines", "known violation", "expected failure", "none - WAY-382", "settings of the linter") and for the
meaning of the word `entry` where this change renamed it. Write no entry for behaviour merely because no invariant covers
it, no glossary entry (WAY-95: the word "entry" in its ordinary meaning gets none), and no environment fact unless the change
rests on a source outside the product that the foundation does not hold (the formatter's behaviour on `fmt:` and `yapf:`
comments and on `except` clauses of Python 3.14 would be one such source: the foundation holds `ruff-default-rules` and
`ruff-required-version`; decide whether a fact for the formatter's documentation is needed, with the reason, as
`elements/environment-facts/skill/SKILL.md` gives, and write it only if the change rests on it). A choice of this cycle
that binds after the merge goes to the log only where the questions of the decisions template give it that place; the
cycle's own choices are rows of the record and need nothing from you.

Run `python -B elements/common/foundation_check.py` after every correction (exit 0 required). The tests that hold a sentence
you reword are named in your report (WAY-03).

## Working copies (word for word)

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

Your directory is `.runs/return-step/`.

## Your return

Return: status (`done`, `done with concerns`, `questions`, `blocked`), your commits (or none), a one-line check result
naming what failed or did not run, and the report's path. The report holds the record's *Return step* items the template
gives (foundation compared with code: the entries and files compared and what no longer matched with its correction or
none; decisions, invariants, environment facts, glossary terms and part-map changes written or changed, or none; projected
entries and rows of *Settlements to record* written, or none), the own-work check `make-change` gives (WAY-164), your
**Unread material**, **Searches not found or unclear**, reaches beyond this handoff, and your working copies with their
removal.
