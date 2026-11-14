# Handoff — reviewer of the whole change

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: put every question to the orchestrator in your report. Never label an answer as the human's approval. You are read-only except for your report.

## Worktree, range and method

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. Review the whole change: base `ac753401de0bfaae0b9b8175c10c17387736f8d8`, head `39d702a61fce67962c5788dbac8636dc5c6e67ae` — confirm it with `git rev-parse HEAD` first (on a mismatch ask the orchestrator which range to review); `git diff <base>..<head>` and `git log <base>..<head>` are yours to compute.
- Method: read whole `task-cycle/review/SKILL.md` of the worktree (`review-change`) and then `task-cycle/review/whole_change.md`, and follow them: you select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md` (the-way has no `guidelines/` directory); count how many decisions you read whole and how many by title only. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: do not run it. Focused checks are yours to run where a finding needs one (for example `python -B elements/common/foundation_check.py`, or the tests of one directory); give each with its command and exit code.
- The first line of your report is `PASS <sha>` or `FAIL <sha>`; grade and scope are yours (Critical, Important, Minor; and what is outside the task's scope).

## What the change is

- Frozen task (read whole): `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`; its 12 accepted rows of *Settlements to record*, six answered questions and three *Questions carried to cycle* are the requirement. Reviewed spec (read whole): `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` (D1–D9, Constraints; the spec before its one revision is `spec-reviewed.md`). Plan: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`.
- Answers of the cycle's two questions at its start: the change touches no trust boundary (the files of the parts it edits are none of those the part map names as one; `elements/common/foundation_check.py` is a surface, `foundation-check-command`, not a boundary — check that its path, argument and exit codes are as promised), and holds no operation that cannot be undone.
- Autonomous choices of the orchestrator that bind the work (they are the cycle's, not the human's; judge whether each is followed and whether a wrong one would break the change): the switch `--skip-test-citations` skips only the report WAY-321 names and WAY-321 is unchanged; "a decision the change changes" means a change of its binding sentences, whitespace-normalised; rows 11 and 12 are attached paragraphs of WAY-12 and WAY-03; the line for an unknown base is written only where the working tree's log holds a decision; a base lacking `foundations/decisions.md` or `foundations/invariants.md` is unknown for that file; the pair-then-trim rule stands in step 3 of `elements/decisions/skill/SKILL.md` and in `task-cycle/skill/return_step.md`; `task-cycle/record_template.md` is edited for the item that names a row's place.

## The slices (none had a review of its own: you judge every one)

| Slice | Range (base..head) | Executor class | What |
|---|---|---|---|
| Foundation entries | `ac75340..d629ed8` | same | 13 decisions of `foundations/decisions.md` edited in place, two attached paragraphs (WAY-12, WAY-03); report `reports/foundation-entries-report.md` |
| 1 | `d629ed8..6440ca9` | cheaper | the line `decision:` read by the check; `reports/slice-1-report.md` |
| 2 | `6440ca9..269fecc` | same | the base and the `listed:` lines; `rules.md`; `reports/slice-2-report.md` |
| 3 | `269fecc..ea2d186` | same | decisions that nothing holds; `reports/slice-3-report.md` |
| 4 | `ea2d186..12286a5` | cheaper | the invariant whose sentence changed; both READMEs; `reports/slice-4-report.md` |
| 5 | `12286a5..c8dcc56` | same | `elements/decisions/template.md`; `reports/slice-5-report.md` |
| 6 | `c8dcc56..64cd4ad` | cheaper | `elements/decisions/skill/SKILL.md`, `decide_entry.md`, `task-cycle/skill/return_step.md`, `task-cycle/record_template.md`; `reports/slice-6-report.md` |
| 7 | `64cd4ad..f20a62c` | cheaper | the column *Goes to*: `project-level/task/template.md`, `elements/common/skill/task_variant.md`, `build_table.md`, `task-cycle/skill/foundation_step.md`; `reports/slice-7-report.md` |
| 8 | `f20a62c..5c4db42` | cheaper | `product-guidelines/template.md`; `reports/slice-8-report.md` |
| 9 | `5c4db42..39d702a` | cheaper | `task-cycle/skill/request_template.md`; `reports/slice-9-report.md` |

The reports are the executors' claims, to be verified, not evidence. The slices' mechanical checks passed (clean worktree, non-empty range, changed files within each slice's *Change*, commands and exit codes in each report). No Minor or out-of-scope findings of earlier reviews exist.

## Gaps and open points the orchestrator carries to you

- Unread by the authors, to judge where they bear: WAY-113, WAY-24, WAY-268, WAY-61, WAY-38, WAY-321, WAY-344, WAY-315, WAY-14, WAY-25, WAY-287 (foundation entries agent); WAY-61, 65, 321, 344, 38 and the invariants and part-map ranges (slice 1); WAY-12, WAY-22, WAY-33 whole and WAY-268 in part (slice 6); WAY-115, 113, 114, 126, 124, 315, 11, 33 and WAY-134 after its start (slice 7); the invariants' ranges, glossary and part map (slices 3, 7); spec D1, D5–D7 and WAY-12 (slice 4); WAY-26 and WAY-293 only in part (slice 5).
- Executors 3 and 4 said the base of this checkout is unknown (no `main` or `master`, `origin/HEAD` not set); the orchestrator's run shows `refs/remotes/origin/HEAD` set to `refs/remotes/origin/foundations` and the script printing no unknown-base line. Check how the script finds the base here and that the-way's own foundation passes with each of the 13 edited decisions held.
- Slice 2's choice: a remote HEAD that shares no history with HEAD makes the base unknown; the script does not fall back to `main`.
- Slice 5 also changed the non-goal sentence of "Trade-off principles and non-goals" in `elements/decisions/template.md` (not named by its slice): judge whether it is needed and right.
- The slice-1 and slice-4 executors report tests that passed before their code (they check what the old script already did), and slice 4 notes that the set of citing files at the base is redundant with no test failing on its removal.
- Slice 8 left the word "and" alone on a line of the opening paragraph of `product-guidelines/template.md` (cosmetic); slice 9's kind 7 says "without the switch" where `--skip-test-citations` is the switch it means.
- The foundation step wrote the entries before slice 1, so the entries and the code were made apart: check that each entry says what the code and the templates now do (the return step compares them too, but judge it from the diff), that the quoted sentence starts in the tests' `decision:` lines stand in the entries, and that no template, skill or request file copies the five questions (WAY-35).
- `origin/foundations` has moved since the base (PR #116 changed the decisions template and the log); the orchestrator merges it in step 12, not now.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/whole-review-report.md` as the method gives it: first line `PASS <sha>` or `FAIL <sha>`; each finding graded, with its place, its slice (or none) and the way to settle it; the coverage of every item of *To do* 1–9, each row of *Settlements to record* and each carried question, and source fidelity; the sections **Unread material** and **Searches not found or unclear**; the count of decisions read whole and by title. Return the first line and the path.
