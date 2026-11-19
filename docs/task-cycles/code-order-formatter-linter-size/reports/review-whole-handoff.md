# Handoff - reviewer of the whole change (stage: review-change, the whole change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never ask
the human. You did not make the change; you review it and change nothing in the reviewed worktree (read-only). You
alone grade and scope your findings; for each blocking finding name the slice it comes from (by number and
commit) or say that it spans slices (name them) or comes from none (a gap of the plan, or the entries of the plan).

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole, and
  `task-cycle/review/whole_change.md`, read whole and followed: what you read and what you check besides section 2,
  including the structure of the code the change leaves (the numbers from your own runs).
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range of the whole change: base `d69fb20b` to head
  `d0a861d9`; compute the diff yourself (`git diff d69fb20b..d0a861d9`, `git log`). The change is large (95 files,
  about +19 900/-10 500, most of it the one reformatting commit `015ce05c`, which reviewer 2 compared by syntax tree);
  read the diff of every non-reformatting commit in full and, for the reformatting commit, check what it says.
- You select your own foundation and guidelines, as `elements/common/way_of_working.md` ("Reading the foundation")
  and `product-guidelines/reading.md` give, for the parts the change touches (every part of the-way that holds Python
  code, `repository`, `decisions`, `invariants`; the part map is `foundations/part_map.md`). Write the index of your
  selection of decisions with `elements/common/decision_index.py` into your directory `.runs/review-whole/` and
  state in your report how many decisions you read whole. Read each guideline file whole.
- Your directory for working copies (the worktrees the method asks for, scripts): `.runs/review-whole/`. Your
  report: `.runs/task-cycles/code-order-formatter-linter-size/reports/review-whole-report.md`; its first line is
  `PASS <sha>` or `FAIL <sha>` (the head you reviewed). It holds the graded findings (blocking, Minor, and
  outside the task's scope), the checks you ran each with command and exit code, **Unread material**,
  **Searches not found or unclear**, your reaches, and your working copies with their removal.
- `cycle.md` and other files of the record directory are not yours to read except those named below.
- Do not run the full gate (`python -B gate/run_tests.py` with no directory argument): its run is the orchestrator's
  or CI's. Focused runs of one directory (`python -B gate/run_tests.py <directory>`) you may make. `<ruff>` is
  `the Ruff of the quality environment of the main checkout` (the main checkout's quality environment;
  `ruff.toml` pins its version). Wait for your own runs to finish before you return.

## Answers of step 4 of the cycle

A trust boundary is touched: the part map names as trust boundaries `task-cycle/cycle_stages.py`,
`task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`,
`process-audit/record_items.py`, `installation/install.py`, `instruction-files/check_instructions.py`,
`project-level/readiness_check.py`, `project-level/plan_check.py`, `project-level/plan_state.py`, and the change
reformats, fixes, divides and moves code of them (new modules `task-cycle/stage_transcripts.py`,
`process-audit/record_reading.py`, `process-audit/problem_register.py` are named trust-boundary files in the part map by
slices 13 and 15). Check crafted input at the boundary files: the same input must give the same verdict, exit code and
message before and after. No operation that cannot be undone.

## What you are given

- The frozen task, read whole: `.runs/task-cycles/code-order-formatter-linter-size/task.md`; the plan, read whole:
  `.runs/task-cycles/code-order-formatter-linter-size/plan.md` (no spec was written: the cycle found no open design
  choice). The plan's *Foundation entries* (F1-F9) are written by commits `9c093516` and `00945f93`.
- The slices and their ranges (a review of its own = a review of the slice by an agent that did not make it; where
  there is none, you are the only review the slice gets, and you judge it as a slice, its executor's own-work check
  included):

| Unit | Range (base..head) | Review of its own |
|---|---|---|
| Foundation entries F1-F9 | `d69fb20b..00945f93` | none: yours; report `reports/foundation-entries-report.md` |
| Slice 1 formatter configuration | `00945f93..6c13454c` | none: report `reports/executor-1-report.md` |
| Slice 2 the one reformatting | `6c13454c..015ce05c` | `reports/review-2-report.md` PASS |
| Slice 3 formatter test, rule, documents | `015ce05c..037f6c93` | none: `reports/executor-3-report.md` |
| Slice 4 full check of the foundation in the gate | `037f6c93..2620dcc3` | none: `reports/executor-4-report.md` |
| Slice 5 linter faults at four boundaries | `2620dcc3..8fecce81` | `reports/review-5-report.md` PASS |
| Slice 6 linter faults in nine test files | `8fecce81..d6442f89` | none: `reports/executor-6-report.md` |
| Slice 7 linter faults, foundation check and migration | `d6442f89..c41a772d` | none: `reports/executor-7-report.md` |
| Slice 8 last linter fault, linter's mark cleared | `c41a772d..222c5a7b` | none: `reports/executor-8-report.md` |
| Slice 9 worktree test and git maintenance | `222c5a7b..0ccdc807` | none: `reports/executor-9-report.md` |
| Slice 10 the word "entry" | `0ccdc807..462add5d` | `reports/review-10-report.md` PASS |
| Slice 11 four long functions at boundaries | `462add5d..679112e3` | `reports/review-11-report.md` PASS |
| Slice 12 request check divided | `679112e3..d84a1fe9` | none: `reports/executor-12-report.md` (saved by the orchestrator from the text the executor returned) |
| Slice 13 transcripts module | `d84a1fe9..1f09e4d6` | `reports/review-13-report.md` PASS |
| Slice 14 audit copy test | `1f09e4d6..efc2f090` | none: `reports/executor-14-report.md` |
| Slice 15 register and record reading | `efc2f090..95316c25` | `reports/review-15-report.md` PASS |
| Slice 16 analysis and report modules | `95316c25..a30a04ff` | `reports/review-16-report.md` PASS |
| Slice 17 tests import new modules; cost script spans two files | `a30a04ff..6c748289` | `reports/review-17-report.md` PASS |
| Slice 18 transitional exports removed | `6c748289..4e5f95fb` | `reports/review-18-report.md` PASS |
| Slice 19 size test strict, mark cleared | `4e5f95fb..d0a861d9` | none: `reports/executor-19-report.md` |

  All the reports are in `.runs/task-cycles/code-order-formatter-linter-size/reports/`. Read the executor report of each
  slice that has no review of its own (and the report of the agent of the entries), with any mismatch the
  orchestrator's mechanical check passed on, below.
- Mismatches the orchestrator's mechanical check passed on: slice 3 changed one more file than its *Change*,
  `agent-instructions/test_script_invariants.py` (one name added to the list `NAMES`, so the test of the invariant
  that holds the files that are no script accepts `.git-blame-ignore-revs`); slice 17's *Change* was widened by the
  orchestrator to `process-audit/SKILL.md` (line 54), the docstring of `process-audit/audit_count.py` and the result
  text of `process-audit/audit_report.py`, after the first commit left the Goal's sentence unmet; slices 13, 15, 16 and
  17 depart from the plan's text in how the modules are cut (the executors' reports say where: `fill`,
  `read_repository`, `committed_date` and `read_prices` stay in `audit_count.py`; `count_rows`, `cost_rows` and `money`
  stand in `version_analysis.py`); slice 4 reworded the comment above `OWN_FINDINGS` in
  `elements/common/test_foundation_check.py`; slice 9 relies on git 2.31 or later (environment `GIT_CONFIG_COUNT`).
- The Minor and out-of-scope findings of the slice reviews (grade each as a finding of your review, as the method says):
  - Slice 10: Minor - fixture text "entries none" left at `process-audit/test_record_items.py:58` and `:128`; Minor - the
    test name `test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list` is less exact.
  - Slice 13: Minor, outside the task per the reviewer - `task-cycle/stage_transcripts.py` stands in no table of
    `guidelines/coding-shared-module.md` (the task carries this question to the cycle; plan *Choices* 12).
  - Slice 15: Minor - the shared base (`AuditCountError`, `Git`, `table_cells`, ...) stands in
    `process-audit/record_reading.py`, so the register module imports from the record reader; Minor - `read_prices`,
    `fill` and `read_repository` stayed in `process-audit/audit_count.py` (`record_reading.py` has 51 lines of room
    under 1200).
  - Slice 16: Minor - the comment over `__all__` of `audit_count.py` was wrong (slice 18 removed `__all__`; check it is
    gone); Minor - `foundations/invariants.md` (`audit-series-script-paths`) and the docstring of
    `process-audit/test_audit_series_scripts.py` still say `audit_count.py` reads the history of the series scripts,
    which now stands in `version_analysis.py`.
  - Slice 17: Minor - `process-audit/audit_report.py` takes the cost files from constants in one place and writes them
    as literals in others; Minor, outside the task - `process-audit/price_list.md:21` and
    `process-audit/audit_count.py:62,76` name `task-cycle/cycle_stages.py` alone as the script that folds the cache
    writes into *Input*, which now lives in `task-cycle/stage_transcripts.py`.
- Known notes for you to judge: the agent of slice 3 left `README.md` around line 106 reading "the settings of the
  linter" (now stale: the same Ruff formats); slice 19's note that `installation/install.py` `plan` stands at 109 lines
  against the limit of 110; the task's rows 1-5 of *Settlements to record* and every item of *To do* 1-8 and both
  acceptance criteria are yours to check as met by the commits; the formatter's own invariant `formatter-layout`
  and the invariant `own-foundation-check-report`, written by the entries, with their tests in slices 3 and 4.
- Foundation entries marked `the cycle's` by the agent of the entries, for the request to put before the human: F6, F7,
  F8 (the word "entry"), F9 (WAY-339 and `audit-series-script-paths` name both files of the cost script), also WAY-09's
  *Verification* gained `own-foundation-check-report` and WAY-382's *Scope* gained `repository`. Judge whether each
  follows from the task with no way left open.

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

Your directory is `.runs/review-whole/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts (the
non-reformatting ones, and the total), your count of decisions read whole, and the report's path. Name each Minor
finding within the task apart from those outside it, as the method says, so that the orchestrator can cut the Minor
findings within the task into the findings file of the fix.
