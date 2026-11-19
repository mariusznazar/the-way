# Handoff - the fix of the Minor findings of the review of the whole change (stage: make-change, the fix of a review's findings)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never ask the
human; a question goes back to the orchestrator in your report, with the ways open and what each costs. Never label an
answer as the human's approval.

## Where you work

- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Your base, the head that was reviewed: `d0a861d9ca22cb2a1cb364d8224bc01f3cd65a44`.
  Your range runs from there.
- Your directory for working copies: `.runs/fixer/` of the worktree. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/fixer-report.md`.
- `cycle.md` and the other files of the record directory are not yours to read, except those this handoff names.

## Method and variant

- Method: `task-cycle/change/SKILL.md` of the worktree (`make-change`). Variant: "the fix of a review's findings". Read the
  `SKILL.md` whole; read a file it names only when the step or variant that names it comes.
- The findings file, which you fix: `.runs/task-cycles/code-order-formatter-linter-size/reports/fix-findings.md` - the
  Minor findings of the whole-change review within the task, in the reviewer's words (findings 1, 3, 4, 5, 6, 7, 8, 9
  and 10 of its report; finding 2 has no code to change, finding 11 is outside the task). The frozen task is
  `.runs/task-cycles/code-order-formatter-linter-size/task.md`; the plan, which you read only where a finding points to it:
  `.runs/task-cycles/code-order-formatter-linter-size/plan.md`.
- Boundary: you fix these findings and nothing else, in commits by path (`git add <path> ...`, never `git add -A`, `.` or
  `commit -a`), with English messages. Make the commits so that finding 7 (the move of the shared base of the audit's
  modules) stands in the last commit alone, apart from the others: the orchestrator reverts the fix in whole where the
  review of the fix finds a new Critical or Important finding in it.
- Do NOT run the full gate: never `python -B gate/run_tests.py` without a directory argument. Focused runs of one
  directory you may make and must make for the files you change, each with its command and exit code in your report; wait for
  every run to finish before you return.
- `<ruff>` is `the Ruff of the quality environment of the main checkout`; every `.py` file you change is laid out by
  `<ruff> format --config ruff.toml <file>` and passes `<ruff> check --config ruff.toml --ignore-noqa <file>`.
- Trust boundaries: files named in the part map (`process-audit/audit_count.py`, `task-cycle/gate_times.py`, and others)
  must give the same verdict, exit code and message for the same input after your change as before it; where a finding
  touches one, show that on crafted input (as the earlier slices did).

## What the orchestrator settles for you, per finding

1. **Finding 1** (`yapf:` comments): widen the pattern of the formatter's test to the comments `# yapf: disable` and
   `# yapf: enable` as well as the three `fmt:` comments, found among the comments as the test finds them now, and bring the
   words of WAY-382 (its second paragraph) and of the invariant `formatter-layout` to the same list, as the reviewer says,
   editing the decision in place (WAY-07). Read `elements/decisions/skill/SKILL.md` and
   `elements/invariants/skill/SKILL.md`, as `task-cycle/skill/foundation_step.md` (read whole) gives for an entry; mark the
   two entries `the cycle's` in your report with one sentence of each in English and one in Polish, since they widen what
   the task's row 5 settled - the request puts them before the human. The test is seen failing once for a `# yapf: disable`
   comment added for a moment (WAY-08), outputs kept in `reports/`. Run `python -B elements/common/foundation_check.py`;
   it must exit 0 (name the tests that hold a sentence you reword, WAY-03).
2. **Findings 3, 4, 5**: as the reviewer writes. For 4 use the name `run`; for 5 a name that says the line is a nested list
   item under the first sub-item, e.g. `test_a_nested_list_item_under_the_first_sub_item_is_no_sub_item_of_the_list` (keep
   the lines `decision:` and `invariant:` of that test as they are).
3. **Finding 6**: extend `guidelines/coding-shared-module.md` as the reviewer says (its *Applies to* and *Where in code*),
   following `elements/../product-guidelines` practice: read the `SKILL.md` whose frontmatter `name:` is
   `maintain-coding-guidelines` (a search of the files named `SKILL.md` for that line finds it) and the file you edit,
   and write only what the finding states; where a status or an exemplar of a file needs a judgment of that skill (copy or
   not), do not invent it: return `questions`.
4. **Findings 8, 9, 10**: as the reviewer writes. For 8 bring the sentence of the invariant `audit-series-script-paths`
   (`foundations/invariants.md`) and the first sentence of the docstring of `process-audit/test_audit_series_scripts.py` to
   say where the history is read now, without changing what they require; run the foundation check (the invariant's
   test is changed by you: name it). For 9 take both file names from the constants in all the places of `audit_report.py`.
   For 10 say in `process-audit/audit_count.py:76` and `process-audit/price_list.md:21` that `task-cycle/stage_transcripts.py`,
   which `task-cycle/cycle_stages.py` imports, folds the cache writes into *Input*; change nothing else of the output of
   the command (a before/after run on a crafted input shows it).
5. **Finding 7** (the last commit, alone): move the shared base (`AuditCountError`, `Git`, `GitError`, `table_cells`,
   `is_separator`, `THE_WAY`, `MAX_BYTES`, and what only they use) from `process-audit/record_reading.py` into a module of
   its own in `process-audit/` that imports nothing of the audit's other modules and runs nothing on import (the rule of
   the kind `shared-module`), and make `record_reading.py`, `problem_register.py`, `version_analysis.py`,
   `audit_report.py` and `audit_count.py` import from it where they use it. No change of behaviour, exit codes, messages
   or output bytes; the tests change only in the module their imports name for a moved name (no expected value, no assertion;
   WAY-233). Show before/after on the crafted input as slice 16 did, run `python -B gate/run_tests.py process-audit`
   and `elements/part-map`, check the sizes with the size test (no function over 110, no file over 1200), and decide with
   the reason (WAY-48) whether the new module is a trust-boundary file of the part map (it holds a wrapper of git and the
   parsing of table text); change `foundations/part_map.md` only if you decide yes, and name the decision in the report.
   Where this finding proves to need more than a move (a cycle of imports, a change of a test's assertion), stop and return
   `questions` with what you found, leaving the earlier commits.

## The foundation entries and the plan's other settlements

The entries of the plan's *Foundation entries* (F1-F9) stand in `foundations/`; the task's settlements stay as they are
except where finding 1 widens WAY-382 and `formatter-layout`.

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

Your directory is `.runs/fixer/`.

## Your return

Return: status (`done`, `done with concerns`, `questions`, `blocked`), your commits, a one-line check result naming what
failed or did not run, and the report's path. The report holds, for each finding, what you changed and the evidence
(commands with exit codes), the entries marked `the cycle's`, the tests altered that hold a decision or an invariant
(WAY-03), the own-work check `make-change` gives (WAY-164), your **Unread material**, **Searches not found or unclear**,
reaches beyond this handoff, and your working copies with their removal.
