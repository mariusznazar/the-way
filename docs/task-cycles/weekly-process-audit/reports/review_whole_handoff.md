# Handoff — reviewer of the whole change (`review-change`: the whole change)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Nothing here is that person's approval. You review as an
agent that made none of this change; grade and scope are yours. Your questions go to the orchestrator.

## What you review

- Worktree (read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`.
- Method: `task-cycle/review/SKILL.md`, whole, and `task-cycle/review/whole_change.md`, whole (you select your own foundation and guidelines by
  "Reading the foundation" in `elements/common/way_of_working.md`; the-way has no guidelines of its own — WAY-328 holds its code and tests to none).
- Head to review: `git rev-parse HEAD` must be `a5ebc88` (confirm; on a mismatch ask the orchestrator).
- The cycle's base is `e3825a82386a61930a86f8517fc0c5f422fc2833` (`foundations` at the start). While the cycle ran, `origin/foundations` moved to
  `52f8164` and was merged into the branch by commit `5f2c155`. **What the request will change in `foundations` is `git diff 52f8164..HEAD`: review that
  diff**; the rest of `git diff e3825a8..HEAD` came in from the target branch and is not this task's. Judge in that diff the files of the task: the
  twelve decisions and the changes of WAY-09, WAY-38, WAY-89, WAY-320 and WAY-328's scope; the part map; `process-audit/`; `task-cycle/cycle_stages.py`,
  `task-cycle/test_cycle_stages.py`, `task-cycle/record_template.md` and the one sentence in `task-cycle/skill/SKILL.md`; `README.md`; the generated entry
  points of the skills under `.claude/skills/` and `.agents/skills/`.
- Report path: `docs/task-cycles/weekly-process-audit/reports\review_whole_report.md`.

## Inputs

- The frozen task, whole: `.runs/task-cycles/weekly-process-audit/task.md` (items of *To do* 1–8, the five answers of *Questions to settle*, the twelve rows
  of *Settlements to record*, *Human actions*, *Out of scope*).
- The plan, whole: `.runs/task-cycles/weekly-process-audit/plan.md`. It was written before the target branch took WAY-327 and WAY-328: the audit's
  decisions are WAY-329…WAY-340 now (the plan's "row n" = WAY-(328+n); where the plan says "WAY-3xx" for the audit's rows, add two).
- Route: planned slices; no spec. Slices and ranges (base..head), and whether each had a review of its own:
  - Foundation entries `e3825a8..1adca16` — no review of its own (judge it here); its report `reports/foundation_entries_report.md`. Renumbered by
    `62f81a3` (the audit's decisions +2) and merged by `5f2c155` (also adds `process-audit` to the Scope of WAY-328, which the target branch's new rule
    asks of a change that adds a part).
  - Slice 1 `1adca16..4443973` — no review of its own; `reports/slice1_report.md`.
  - Slice 2 `4443973..876710c` — no review of its own; `reports/slice2_report.md`.
  - Slice 3 `876710c..9285a74`, fix `116f319` — reviewed (`reports/review_slice3_report.md`; fix `reports/review_slice3_fix_report.md`).
  - Slice 4 `116f319..269d7be`, fix `9392230` — reviewed (`reports/review_slice4_report.md`, `reports/review_slice4_fix_report.md`); a blocking finding
    remained, and the human decided (below).
  - Correction for the human's decision `5f2c155..9cf2633` — reviewed (`reports/review_correction_report.md`, `PASS`).
  - Slice 5 `9cf2633..c2a0169`, fix `7bb25c3` — reviewed (`reports/review_slice5_report.md`, `reports/review_slice5_fix_report.md`).
  - Slice 6 `7bb25c3..2e7168c` — reviewed (`reports/review_slice6_report.md`, `PASS`).
  - Slice 7 `2e7168c..a5ebc88` — no review of its own; `reports/slice7_report.md`. The mechanical check found no mismatch in any slice.
- The Minor and out-of-scope findings of the slice reviews, for you to grade as findings of this review (list each Minor finding with its place and
  words; say where one lies outside the task): in the review reports above (sections "Minor findings", "Out of scope", "Declined to judge").
- The human's decision on the request that blocked at slice 4 (their words): "a co do tego 0.0% zgadzam się z propozycją, ale nie rozumiem idei żeby to
  zrobić osobnym zadaniem — jak wiemy co jest do zrobienia, to trzeba to zrobić, a nie wydzielać". Made by the correction (`reports/correction_handoff.md`,
  `reports/correction_report.md`).

## Risk and answers of the start

- Trust boundary: **yes** — `process-audit/audit_count.py` reads from outside the repository the cycle records and `stages.md` of the repositories the user
  names (through git history), the user's locations file, the register of problems, the price list and the results place; `task-cycle/cycle_stages.py` reads
  session transcripts and now the text of the messages that start a turn. The slices 3–6 had reviews against crafted input; check once more hostile input at
  the whole, in particular across slices (a register row, a record and a stage report that disagree; a result cell built from several sources; the order of
  work and the size of output on large input).
- Irreversible operation: no. Scheduling the counting and adding the weekly task to the backlog are human actions the task places in the cycle
  (WAY-140); check that nothing in the change performs them.
- **Orchestrator's choices you are to judge, not accept:** (1) `cycle_stages.py` is not marked a trust boundary in the part map (the part map gives
  `task-cycle` none; the slice-3 review put it as out of scope); (2) the binding choices of slice 3 (repositories named by keys of the locations file and
  their entry `repository`; entries `problem_register` and `audit_results` under `the-way`; `--locations`; a cycle of the-way's own history is given the
  commit named in its *Target branch and base* line as its version); (3) a findings file must be named by at least two turns before the share of fix
  rounds counts (the correction's added rule); (4) the conservative series rule (any change of the paths of the stage-report methods and
  `cycle_stages.py` splits a series), which on the-way's own history gives 20 series for 53 versions; (5) the prices of the price list were read by a
  fetching agent from the providers' pages on 2026-11-11 (`reports/prices_fetched.md`): you cannot check the pages — say so.
- Gaps the orchestrator carries to you from the slice reports' **Unread material**: slice 2 read WAY-148 at old line numbers (its last lines stayed
  unread); the writer of the foundation entries read WAY-140, WAY-134, WAY-135 and WAY-161 in part; the executor of slice 7 did not read
  `process-audit/audit_count.py` between lines 600 and 1560 (it wrote the skill from the docstring and runs) — judge whether the skill states what the
  command does.

## Also check

- Coverage of every item of *To do* (1–8), every row of *Settlements to record* (rows 1–12) and *Human actions*; fidelity to the task's sources (the
  task's wording of the three questions per version, the series rule, the classes and weights); the task's *Out of scope* untouched.
- That the target branch's new rules and this change hold together: `task-cycle/skill/request_template.md` and `task-cycle/skill/SKILL.md` came in from
  the target branch while the cycle's correction edited `task-cycle/record_template.md` and one sentence of `task-cycle/skill/SKILL.md`; WAY-327 and
  WAY-328 (new) against the audit's decisions and the Scope of WAY-328.
- The foundation: the decisions of the touched parts you select, the glossary words the change introduces ("issue" / sprawa, "series"; the return step
  decides about entries, but report a sentence that a reader would read wrongly for lack of one), the invariants of `process-audit` and every part.
- Whether the change adds anything nobody asked for.

## Report

Write the full report to the report path, first line `PASS <head sha>` or `FAIL <head sha>`; for each blocking finding the slice it comes from (number and
commit) or that it spans slices or comes from none. Include **Declined to judge**, each check you ran as command and exit code (focused checks only: the full
suite is the cycle's own run; `python -B gate/run_tests.py process-audit` takes about a minute and the `task-cycle` directory about a minute — run long
commands in the background and wait in stretches under four minutes), each reach beyond the dispatch, **Unread material** opening with the counts of decisions you
read whole and by title only, and **Searches not found or unclear**. Return only the first line, the counts of blocking, Minor and out-of-scope findings, a one-line
check result and the report path.
