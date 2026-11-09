# Cycle record — the way: places outside the repository in ~/.the-way/locations.json instead of paths in repository files

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, accepted 2026-11-08; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: the-way (public repository; target branch `foundations`)
- Process pin: this checkout (the-way itself), base commit `17b83bf145653be0beeb43f5fa8175a4197a3700`
- Target branch and base: `foundations` at `17b83bf145653be0beeb43f5fa8175a4197a3700` (fetched 2026-11-09; local equals origin)
- Task branch: `task/locations-file` in worktree `.runs/worktrees/locations-file`
- Status: request open

## Two questions at start

- Trust boundary: no — the touched files (root `AGENTS.md`, the new test in `gate/`, skill and template files of `project-level`, `foundation-review`, `product-guidelines`, tests of `installation`, entries of `foundations/`) belong to parts whose *Trust boundary* is `none` in the part map.
- Irreversible operation: no — the change adds a test and edits text and tests; the only effect outside the repository, the file `~/.the-way/locations.json`, is a human action already done before the cycle.

## Spec and execution route

- Open design choice at start: none — rows 1–3 of *Settlements to record* and questions 1–5 settle the file, its place, the test, its exclusion list and the wording of `## Backlog`. The one choice carried to the cycle (how the foundation records the new check, within row 3) is the author's, recorded as an autonomous choice; WAY-61 and row 3 bound it.
- Reserved choice: none
- Execution route and reason: one author without a plan — one agent can hold it: one new test, edits of about fifteen small text files, three foundation entries.
- Author: one author, class `same` as the orchestrator (`sonnet`), because the change spans many parts (agent-instructions, gate, project-level, foundation-review, product-guidelines, installation, decisions, invariants); resumed for the fix and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code — a background agent reports by completion notification; the turn yields while it runs.
- Whole-change review: reviewer opus (agent `af3e0bffecacaca21`), `review-change`, range `17b83bf..973ee64`, first line `FAIL 973ee64`, `reports/review-whole-report.md`; 12 files, +282/−38 (AGENTS.md 6/5, foundation-review/SKILL.md 5/5, foundations/decisions.md 77/14, foundations/invariants.md 11/1, project-level/backlog_place.md 38/0, project-level/definition_template.md 5/3, project-level/lead/skill/SKILL.md 2/1, project-level/skill/first_write.md 2/2, project-level/task/skill/final_review.md 1/1, project-level/task/skill/read_sources.md 5/5, task-cycle/skill/SKILL.md 2/1, task-cycle/test_tracked_files_private_paths.py 128/0); coverage: all five *To do* items and rows 1–3 met, the two autonomous choices of the author accepted, source fidelity checked against the task's questions 1, 2 and 4.
- Review rounds: (1) whole change `17b83bf..973ee64`, `FAIL`: I-1 (Important) the new decision omitted the exemption of four files that row 3 and the new invariant carry; I-2 (Important) a sentence of the new shared skill file forbade a cycle to write outside the repository, contradicting WAY-140; Minor within the task M-1, M-2. Fix `973ee64..ba36539` by the resumed author (`reports/fix-1-report.md`): I-1, I-2, M-2 fixed, M-1 left unchanged (the finding allows either). Review of the fix by the same reviewer (`reports/review-fix-1-report.md`): `PASS ba36539`; M-1 remains, accepted, Minor. (2) Return step `ba36539..2984b5f`, fresh reviewer opus (agent `a029f21d2a7eba3bc`, `reports/review-return-report.md`): `PASS 2984b5f`, no findings. No blocking finding remained. No revert.
- Weakest-point checks: author — requirement named: *To do* 3 (every skill that finds the backlog); check: grep of tracked files for `## Backlog`, `backlog`, `WAY-107`, each hit read; showed six readers, now pointing to the shared file; `reports/author-report.md`. Whole-change reviewer repeated it with wider terms (`task area`, `project place`) and found no reader missed. Fix — requirement: WAY-320 stays faithful to question 2 of the task; check: word-by-word comparison and `foundation_check.py`; `reports/fix-1-report.md`.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

None — one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-09 | Start | orchestrator, sonnet | entry point `the-way-implement-task`, task path given as argument | frozen `task.md`; worktree `.runs/worktrees/locations-file` from `17b83bf`; base check in `.runs/base-check-locations-file` (detached `17b83bf`), log `.runs/base-check-locations-file.log` | task `ready for cycle`, human action done (`locations.json` exists); route chosen; dispatch author |
| 2026-11-09 | Author (one author) | agent `a728e52735006da67`, sonnet (class `same`) | `reports/handoff-author.md`; `the-way-make-change`, variant the whole change as the one author; frozen `task.md` | `reports/author-report.md` | dispatched in background at base `17b83bf`; wait by completion notification |
| 2026-11-09 | Author result | agent `a728e52735006da67`, sonnet | — | `reports/author-report.md` (saved by the orchestrator from the author's returned text: its Write tool refused a report file) | `done with concerns` (concern: only the missing file); commit `973ee64`, 12 files +282/−38; mechanical check: worktree clean, range `17b83bf..973ee64` non-empty, changed files match *To do*, every check with command and exit code, **Searches** and own-work check present; next: whole-change review |
| 2026-11-09 | Whole-change review | fresh reviewer, opus (no class cheaper than the orchestrator's) | `reports/handoff-review-whole.md`; `the-way-review-change`, whole change, range `17b83bf..973ee64`, frozen task, author's report | `reports/review-whole-report.md` | dispatched in background |
| 2026-11-09 | Whole-change review result | reviewer opus (agent `af3e0bffecacaca21`) | — | `reports/review-whole-report.md` | `FAIL 973ee64`: 2 blocking (I-1 WAY-320 lacks the exemption of row 3; I-2 `backlog_place.md` WAY-140 sentence contradicts WAY-140), 2 Minor within the task (M-1, M-2), 0 outside scope; 12 files +282/−38; checks exit 0 (task-cycle, foundation_check, elements/common, agent-instructions, project-level); next: one fix by the resumed author with `reports/findings-whole-1.md`  |
| 2026-11-09 | Fix (resumed author) | agent `a728e52735006da67`, sonnet (class `same`, the one author's class) | message with `reports/findings-whole-1.md`; `the-way-make-change`, fix of a review's findings | `reports/fix-1-report.md` (saved from returned text; Write refused again) | `done`; commit `ba36539`; I-1, I-2, M-2 fixed, M-1 left as operational reading (finding allows either); checks exit 0 with commands; mechanical check: worktree clean, range `973ee64..ba36539` non-empty; next: review of the fix by the same reviewer |
| 2026-11-09 | Review of the fix | reviewer opus (agent `af3e0bffecacaca21`, resumed) | message: range `973ee64..ba36539`, `findings-whole-1.md`, `fix-1-report.md` | `reports/review-fix-1-report.md` | `PASS ba36539`: I-1, I-2, M-2 fixed; M-1 remains (accepted, Minor, goes to the request's list); checks exit 0 |
| 2026-11-09 | Gate (step 10) | orchestrator | `python -B gate/run_tests.py` in separate checkout `.runs/gate-check-locations-file` at `ba36539`, log `.runs/gate-check-locations-file.log` | exit 0, 826 tests in 9 directories on `ba36539`; rerun on `2984b5f` after the return step: exit 0, 826 tests | the return step changed the tree, so the gate ran again on the final tree |
| 2026-11-09 | Return step | agent `a728e52735006da67`, sonnet (resumed author) | `reports/handoff-return-step.md` | `reports/return-step-report.md`  | dispatched |
| 2026-11-09 | Return step result | agent `a728e52735006da67` (resumed author) | — | `reports/return-step-report.md` (saved from returned text) | `done`; commit `2984b5f`: WAY-309 *Verification* now names `tracked-file-private-paths` (1 field, +2/−1); checks exit 0 with commands; tree differs from the gate run on `ba36539`, so the gate reruns on the final tree (step 12) |
| 2026-11-09 | Review of the return step | fresh reviewer, opus (agent `a029f21d2a7eba3bc`) | `reports/handoff-review-return.md`; range `ba36539..2984b5f` | `reports/review-return-report.md` | dispatched |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the task leave an open design choice that calls for a spec? Task *Questions carried to cycle* | No: how to record the new check is bounded by row 3 and WAY-61 and is the author's autonomous choice | task rows 1–3; WAY-61 | write a spec for one entry's wording | an extra spec stage for a wording choice | route |
| Q2 | How does the foundation record the new check (task *Questions carried to cycle*; WAY-61)? | A new invariant `tracked-file-private-paths` with method `test`; `outbound-link-reach` stays `review`, loses its exception | WAY-61 (a test must check what the sentence is about; the test checks paths and note links, not unreachable repositories); `reports/author-report.md`; accepted by `reports/review-whole-report.md` | turn `outbound-link-reach` to `test`; split it in two (withdrawn identifier, rewritten references) | merging two entries and the *Derives from* of one | author |
| Q3 | Where does the test stand (task: run by `gate/run_tests.py`)? | in `task-cycle/`, discovered by the gate runner | part map: `gate` depends on none, so it cannot import `task-cycle/private_paths_check.py` (invariant `cross-part-imports`); accepted by the whole-change review | `gate/` with a copy of the pattern (a second pattern) | someone looks in `gate/`; moving it means a new dependency or a copy | author |
| Q4 | One shared file for the rule of finding a backlog place, or the rule in each skill? | one file `project-level/backlog_place.md`, six pointers | author's report | six copies of the rule | a skill that reads only its own file misses the pointer; each pointer names the file | author |
| Q5 | What does an agent do when the entry exists but its path does not exist? Not in the task | counts as a missing place: ask and offer to record | author's report; whole-change review M-1 (Minor, remains, accepted) | treat only a missing file or entry as missing | an agent asks where a placed path moved, or silently fails | author |
| Q6 | May a task cycle create or change the locations file? Not in the task | no: it names the missing entry in its report (WAY-140: a human's effect outside the repository) | WAY-140; narrowed from "writes nothing outside the repository" by fix 1 (I-2) | cycle creates the file | a cycle writing to the user's disk outside the repository | author, fix |
| Q7 | Is the gate to run on the final tree after the return step committed? | yes: separate checkout of `2984b5f` | `SKILL.md` step 12 | trust the run on `ba36539` | a failure the one-field edit caused goes unseen | orchestrator |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/locations-file/task.md` | orchestrator | n/a |
| Code and foundation commits | `973ee64` (change), `ba36539` (fix of findings), `2984b5f` (return step) on `task/locations-file`, base `17b83bf` | one author (sonnet) | `FAIL`, then `PASS ba36539`, then `PASS 2984b5f` |
| Reports | `reports/author-report.md`, `fix-1-report.md`, `return-step-report.md`, `review-whole-report.md`, `review-fix-1-report.md`, `review-return-report.md`; handoffs `handoff-*.md`; `findings-whole-1.md` | agents; saved by the orchestrator where the agent could not write the file | — |
| Stages table | `stages.md` | orchestrator (`task-cycle/cycle_stages.py`) | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the base (separate checkout `.runs/base-check-locations-file`) | orchestrator, `17b83bf`, Windows | exit 0; 817 tests in 9 directories, every directory passed; no check failing on the base | none |
| `python -B gate/run_tests.py task-cycle` before `AGENTS.md` was changed (new test only) | author, `973ee64` working tree, Windows | exit 1; one failure listing `AGENTS.md:20` and `AGENTS.md:25` | none |
| `python -B gate/run_tests.py task-cycle` after the change | author | exit 0, 209 tests | none |
| `python -B gate/run_tests.py` on the reviewed change (separate checkout `.runs/gate-check-locations-file` at `ba36539`, log `.runs/gate-check-ba36539.log`) | orchestrator, `ba36539` | exit 0; 826 tests in 9 directories, every directory passed | none |
| `python -B gate/run_tests.py` on the final tree (same checkout at `2984b5f`, log `.runs/gate-check-2984b5f.log`) | orchestrator, `2984b5f` | exit 0; 826 tests in 9 directories, every directory passed | none |
| `python -B elements/common/foundation_check.py` | author, fix, return step; reviewers | exit 0, 0 errors | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | merges: 14, threshold: 30, `reminder: no` | none |
| reconciliation with the target branch: `git fetch`; `origin/foundations` = base `17b83bf`, an ancestor of the head | orchestrator | no merge needed, so no review of a merge | none |
| `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/locations-file/stages.md` | orchestrator | exit 0, no warnings | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/locations-file` | orchestrator, original record | first run exit 0 with `0 reports` (reports not named `*report.md`; renamed), then exit 1 listing 8 items, then exit 0 after they were appended; 3 runs | none |

## Return step

- Foundation compared with code: WAY-27, WAY-107, WAY-320, WAY-308, WAY-309, WAY-140, WAY-61 and the invariants `outbound-link-reach`, `tracked-file-private-paths`, and the part map of `project-level`, `task-cycle`, `foundation-review`, `product-guidelines`, `agent-instructions` compared with the files; one mismatch: WAY-309 did not name the invariant that derives from it; corrected in `2984b5f` (`reports/return-step-report.md`); reviewed `PASS 2984b5f`
- Decisions written or changed: WAY-320 (new, row 2); WAY-27 and WAY-107 (edited, row 1); WAY-309 (*Verification* names the new invariant, return step)
- Invariants written or changed: `tracked-file-private-paths` (new, test; set by row 3); `outbound-link-reach` (exception removed; set by row 3)
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 (WAY-27, WAY-107); row 2 (WAY-320); row 3 (`tracked-file-private-paths`, `outbound-link-reach`)

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/92 — opened as a draft, then marked ready after the record's commit
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/locations-file/request.md --task .runs/task-cycles/locations-file/task.md` exit 0, private-paths check on it exit 0; the record's link and the checks on the copy are added after the record's commit (written and checked again after this commit)
- Writes to the task's backlog entry: the request link added to the task's line in the author's backlog (`[url::...pull/92]`); its state left as it was, Ready
- Process remarks on the-way:
  - Author, .runs/task-cycles/locations-file/reports/author-report.md: I read WAY-27, 107, 308, 309, 61, 140 and 16 whole. WAY-07, 25, 33, 114 and 134 I read through the templates and the foundation step that carry their rules, not entry by entry.
  - Author, .runs/task-cycles/locations-file/reports/author-report.md: The task does not say whether a product's key in the locations file is its directory name or the name given in its `## Backlog` line. I made the line name it, so nothing is inferred.
  - Author, .runs/task-cycles/locations-file/reports/author-report.md: The task does not say what to do when the entry exists but its path does not. `backlog_place.md` treats that as a missing place (see the weakest point).
  - Author, .runs/task-cycles/locations-file/reports/author-report.md: The hint "about 15 files name `## Backlog`" matched 15 hits in 12 files. Six find a place (changed), four are installation test fixtures, and two only name the section.
  - Author, .runs/task-cycles/locations-file/reports/author-report.md: `guidelines/` is absent, as the handoff says.
  - Whole-change review, .runs/task-cycles/locations-file/reports/review-whole-report.md: I did not read every decision whose *Scope* names `project-level`, `task-cycle` or `agent-instructions` (step 2 of "Reading the foundation" selects several hundred); I read the decisions the task's *Decisions in play* names, those the change writes or changes, and those they link to or a grade needed.
  - Whole-change review, .runs/task-cycles/locations-file/reports/review-whole-report.md: The task does not say which repository name a product uses as its key in the locations file; the change leaves it to the `## Backlog` line, which names it — no finding.
  - Whole-change review, .runs/task-cycles/locations-file/reports/review-whole-report.md: `the-way` has no `guidelines/`, as the handoff says, so no guideline rule was compared.
  - orchestrator: the harness refused every subagent a Write of a report file ("Subagents should return findings as text, not write report files"), three times for the author and the return step; the method has each agent write its report to its report path, so the orchestrator saved each returned text as the report, with a header saying so. A the-way method that expects an agent to write a file does not say what to do when the harness refuses it.
  - orchestrator: `task-cycle/remarks_check.py` reads only files named `*report.md`, which no handoff, skill or template says; the first run of the check on this record read 0 reports because the orchestrator had named the reports `report-<stage>.md`, and it listed nothing until they were renamed.
