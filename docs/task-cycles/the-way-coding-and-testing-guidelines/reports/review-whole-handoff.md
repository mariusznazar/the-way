# Handoff — reviewer of the whole change

The person who requested this cycle delegated intermediate choices to the orchestrator; nothing
here is that person's approval. You review the whole change as an agent that made none of it.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`. You change nothing in it.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant **the whole change** (it names `task-cycle/review/whole_change.md`; read that where the skill names it). Read it whole; a skill named by its name alone is the `SKILL.md` whose frontmatter `name:` is that name — read it as a file (you have no skill tool).
- Range: `2d593214e4ce11676880b1f3ac3aa75884e023ab..be9b44d` (base to head, 32 commits, 38 files, +2956 −221; `git diff --stat` lists them). Read the full diff.
- Frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` (20 items of *To do*, 26 answers, 34 settlement rows, the audit's causes 1–34). Plan: `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` (23 slices, 40 foundation entries E1–E40, its *Choices*, the orchestrator's additions at its end). No spec. Route: planned slices.
- **Trust boundary: yes.** The change edits `task-cycle/cycle_stages.py` and `task-cycle/cycle_measures.py` (files the part map names as boundaries) and adds citations of refusal invariants for six boundary files; check crafted input at those files and that the invariants cite tests that check the refusal. **Irreversible operation: no.**
- Your directory for working copies: `.runs/review-whole/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/review-whole-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`.
- Select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md`; the-way has its own guidelines now (`guidelines/coding.md`, `guidelines/testing.md`, `guidelines/coding-<kind>.md`), written by this change: read what applies to the change's parts and judge the change also against the sentences those guidelines now give. State in your report how many decisions you read whole.
- You never run the product's gate (`python -B gate/run_tests.py` with no directory): the orchestrator runs it once on the finished change, at the start signal of the day advisor. Run focused checks (`python -B gate/run_tests.py <directory>` or a file) as you need.
- `<ruff>` means `.runs/quality-venv/Scripts/ruff.exe` under the main checkout `<main checkout>` (the parent of the directory `git rev-parse --git-common-dir` prints).

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



## The identifiers of the entries the slice names

The plan names entries written by the foundation step by their row `E<n>`; here are the identifiers
the writer gave them (use these, not the plan's proposals):

| Entry of the plan | Kind | Identifier written | Row |
|---|---|---|---|
| E1 | decision | WAY-379 | row 1 |
| E2 | decision | WAY-380 | row 3 |
| E3 | decision | WAY-381 | row 4 |
| E4 | decision | WAY-382 | row 11 |
| E5 | decision | WAY-383 | row 12 |
| E6 | decision | WAY-384 | row 13 |
| E7 | decision | WAY-385 | row 14 |
| E8 | decision | WAY-386 | row 18 |
| E8 | decision | WAY-387 | row 18 |
| E8 | decision | WAY-388 | row 18 |
| E8 | decision | WAY-389 | row 18 |
| E8 | decision | WAY-390 | row 18 |
| E8 | decision | WAY-391 | row 18 |
| E9 | decision | WAY-392 | row 2 |
| E10 | decision | WAY-393 | row 20 |
| E11 | decision | WAY-394 | row 25 |
| E12 | decision | WAY-395 | row 26 |
| E13 | decision | WAY-396 | row 27 |
| E13 | decision | WAY-397 | row 27 |
| E13 | decision | WAY-398 | row 27 |
| E13 | decision | WAY-399 | row 27 |
| E13 | decision | WAY-400 | row 27 |
| E14 | decision | WAY-401 | row 28 |
| E15 | decision | WAY-402 | row 29 |
| E16 | change of a decision | WAY-09 | row 31 |
| E17 | withdrawal of a decision | WAY-328 | row 32 |
| E18 | change of a decision | WAY-344 | row 33 |
| E19 | change of a decision | WAY-363 | row 34 |
| E20 | change of a decision | WAY-38 | row 9 |
| E21 | change of an invariant | `script-subprocesses` | row 10 |
| E22 | invariant | `ruff-blocking-rules` | row 6 |
| E23 | invariant | `function-and-file-size` | row 15 |
| E24 | invariant | `generator-writes-only-with-write` | row 19 |
| E25 | invariant | `repository-changer-acts-only-when-told` | row 19 |
| E26 | invariant | `command-runner-passes-exit-code` | row 19 |
| E27 | invariant | `shared-module-import-runs-nothing` | row 19 |
| E28 | invariant | `readiness-check-refuses-non-utf-8` | row 30 |
| E29 | invariant | `cycle-stages-refuses-crafted-names` | row 30 |
| E30 | invariant | `cycle-measures-refuses-nested-line` | row 30 |
| E31 | invariant | `gate-times-refuses-impossible-entry` | row 30 |
| E32 | invariant | `audit-count-refuses-record-links` | row 30 |
| E33 | invariant | `check-instructions-refuses-outside-links` | row 30 |
| E34 | glossary term | `files test` | row 21 |
| E35 | glossary term | `git test` | row 22 |
| E36 | glossary term | `repository test` | row 23 |
| E37 | environment fact | `ruff-default-rules` | row 7 |
| E38 | environment fact | `ruff-required-version` | row 8 |
| E39 | part-map line | written by Slice 1 | — |
| E40 | part-map line | written by Slice 18 | — |

Deviations of the written entries from the plan that bear on you: the glossary terms are headed
`files test`, `git test` and `repository test` (not the bare `files`, `git`, `repository`); six
decisions WAY-386 to WAY-391 designate the exemplars of the six kinds (one each), and five decisions
WAY-396 to WAY-400 the exemplar of each level (one each); the entries name eleven parts with Python
code (`product-guidelines` is the eleventh).


## Slices: ranges, reviews and reports

| Slice | Head | Own review | Executor report (in `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/`) |
|---|---|---|---|
| Foundation entries | `e1586a4` (range `2d59321..e1586a4`) | none: judged here | `entries-report.md` |
| 1 | `162bff8` | none: judged here | `executor-1-report.md` |
| 2 | `d113238` | PASS `review-2-report.md` | `executor-2-report.md` |
| 3 | `43d7d9b` | none | `executor-3-report.md` |
| 4 | `ced0fd9`, fix `49be485` | FAIL then PASS of the fix: `review-4-report.md`, `slice-4-findings.md`, `review-4-fix-report.md` | `executor-4-report.md`, `executor-4-fix-report.md` |
| 5 | `5f19b1d`, `c07e286` | PASS `review-5-report.md` | `executor-5-report.md` |
| 6 | `0905337` | PASS `review-6-report.md` | `executor-6-report.md` |
| 7 | `8ef214d` | none | `executor-7-report.md` |
| 8 | `6cf3fa9` | PASS `review-8-report.md` | `executor-8-report.md` |
| 10 | `c1ab102`..`d84dc5b` | none | `executor-10-report.md` (with addendum) |
| 11 | `99340e9` | PASS `review-11-report.md` | `executor-11-report.md` |
| 12 | `c86b09b` | none | `executor-12-report.md` |
| 13 | `d389ff5` | none | `executor-13-report.md` |
| 14 | `878c88d` | none | `executor-14-report.md` |
| 15 | `8dce794` | none | `executor-15-report.md` |
| 16 | `fc9244f` | none | `executor-16-report.md` |
| 17 | `2b9914c` | none | `executor-17-report.md` |
| 9 (made after 17, see choice Q8) | `f16616c` | none | `executor-9-report.md` |
| 18 | `38c1ff8` | none | `executor-18-report.md` |
| 19 | `cb6c208` | none | `executor-19-report.md` |
| 20 | `f7c64a2`, `734798f`, `316a698` | none | `executor-20-report.md` (with addendum) |
| 21 | `39aaa1c`, `6fd60ef` | none | `executor-21-report.md` (with addendum) |
| 22 | `b47e1b2` | none | `executor-22-report.md` |
| 23 | `be9b44d` | none | `executor-23-report.md` |

Judge every slice that had no review of its own; name for each blocking finding the slice it comes from, or that it comes from none.

Minor and out-of-scope findings of the slice reviews (carried; the cycle keeps them in the request's list unless your report lists them as within the task):
- Slice 4 (`reports/review-4-report.md`, `reports/review-4-fix-report.md`): the docstring of `MissingFieldError` still says "Claude Code transcript" (`task-cycle/cycle_stages.py`); `required` and `required_count` stay under the heading `# Claude Code`; no Codex test accepts a count of `10**15-1`; a Codex line that is JSON but no object gives `AttributeError`.
- Slice 5 (`reports/review-5-report.md`): a time with `Z` in the separator position is read as naive UTC; a bare `2026-10-06Z` is refused.
- Slice 6 (`reports/review-6-report.md`): the cited test proves the deletion clause of its invariant and not the "counts for no run" clause.

## Choices of the cycle that you judge (autonomous, none is the human's approval)

- Q2: eleven parts with Python code, `product-guidelines` the eleventh (the task says ten; `product-guidelines/test_skill_references.py` exists at the base); the row of that part in the table of parts of `guidelines/testing.md` puts its complexity in computation: the orchestrator's proposal.
- Q3: slice 4 covers the Codex half of cause 3; the Claude Code half was corrected at the base; the other fields of the Codex rollout were then made required by the fix of the slice's review.
- Q4: the command-runner rule is tested on `task-cycle/gate_times.py` only. Q5: `## Rules` of the kinds `check` and `measuring-report` read `none — <decision>`. Q6: four new linter places (F541, TRY004, PYI034, PIE810) stay under the invariant marked violated.
- Q7: glossary terms headed `files test`, `git test`, `repository test` (the rows say `files`, `git`, `repository`); some binding sentences go beyond a row (WAY-379, WAY-392, WAY-382, WAY-383, WAY-393, WAY-388–391; the entries report lists them).
- Q8: slice 9 was made after slice 17; its filter keeps findings of two invariants by message text and does not keep a reference to a withdrawn part. Q9: `Name:` without `name:` ends `skill_entry_points.py` with exit 2. Q10: the report file of `migrate_foundation.py` under the ignored `.runs/` is no change of a tracked file or working directory (invariant of the repository changers). Q11: `elements/common/migrate_foundation.py` is `do not copy` in `guidelines/coding-repository-changer.md`.
- The test of slice 15 reads "input closed" as an open empty pipe whose read blocks; the sentence of the invariant `shared-module-import-runs-nothing` says "closed input". The part-map sentence of `agent-instructions` does not mention `guidelines/`.
- Entries E-writer's unread plan lines 652–999 (slices 17–23 and *Coverage*) when it wrote the entries: check that the entries and the guidelines agree with what the slices wrote.

## What you return

The report's first line, then graded findings as the method gives (every finding with `file:line`, a failure scenario, its grade and, for a blocking one, its slice); the coverage of every item of *To do*, every row of *Settlements to record* and each cause the task takes; source fidelity of the entries to the task; the checks you ran with command and exit code; **Unread material** and **Searches not found or unclear** (`none` is an answer); the working-copies line; and a short return: status, report path, changed files with line counts (top ones), one-line check result.
