# Cycle record — Skill do plików instrukcji podaje przy każdym werdykcie kryterium miejsca reguły i ocenia także skille

- Task source: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/zadanie_instruction_files_jako_router.md; `Status: ready for cycle`, last updated 2026-10-28; frozen in [task.md](task.md).
- Task relation: independent
- Product repository: C:/Storage/repos/the-way (the-way itself, top level; integration route of `agent-instructions/README.md`); worktree C:/Storage/repos/the-way-wt/instruction-files-router
- Process pin: none — the-way works on itself; skills read from this worktree at `0b8c1bd`
- Target branch and base: `foundations` at `0b8c1bd613b94bce290e49aad9eaf1d0b2587b02` (= origin/foundations, fetched 2026-10-28T00:00Z)
- Task branch: `task/instruction-files-router`, created with `--no-track`
- Status: request open

## Two questions at start

- Trust boundary: yes in letter — the part map names `instruction-files/check_instructions.py` as the trust boundary of `instruction-files`, and To do 9 changes its module docstring (line 3, the reference to section 6 of `principles.md`). Nothing else of that file changes. The review of the whole change is told so and checks that the change to that file is docstring-only and alters no handling of the files it reads.
- Irreversible operation: no. Text of the repository only; no human action, no effect outside the repository.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Rows 1–5 of *Settlements to record* settle the shape: the criterion and shared rules in `SKILL.md`, one file per kind of text read by the judging step, no repetition, no pointer from a kind file, a shared file named in the step only where shared rules outweigh; the second question of recognizability with its order (reword the condition first, whole rule only after a recorded miss); the criterion in every row of the judging table; instruction count as the reason. Rows 6–7 settle the facts and the task gives the source and its quotation. File names and the distribution of today's sections are choices of how to make what the task settles: the author makes them and names them.
- Execution route and reason: one author without a plan — one coherent restructuring of `instruction-files/` with its foundation entries; the reading is about 8 000 words of the part plus the selected entries, which one agent holds.
- Author: class `same` (Opus, as the orchestrator) — the change runs across five parts (`instruction-files`, `decisions`, `environment-facts`, `product-guidelines`, `agent-instructions`) and its distribution of the principles over new files is a judgment the rest of the skill rests on.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code background `Agent` with completion notification; no polling.
- Whole-change review: fresh reviewer (Opus) by `review-change`, range `0b8c1bd..634fa3b`, [review-report.md](reports/review-report.md), first line `PASS 634fa3b4e2fdb890dafbbdc5aa2ef0c69df9b931`; 12 files, +559 −390 (`principles.md` −316; `SKILL.md` +215 −55; `decisions.md` +131 −12; four new files +200). Coverage: every To do 1–9 and settlement row 1–7 met; answers under *Questions to settle* and *Out of scope* kept; `check_instructions.py` change docstring-only (trust boundary). 0 blocking, 6 Minor, 0 out of scope.
- Review rounds: none — no review returned `FAIL`. The return step's range `634fa3b..524d9b8` had its own review: [return-review-report.md](reports/return-review-report.md), `PASS 524d9b8838cc0dd285fbb46630bbf7831477a356`, 0 blocking, 4 Minor.
- Weakest-point checks: author — To do 1 / row 5 (no repetition between files, no pointer from a kind file): a script compared normalised sentences over 40 characters across the skill's files and listed `.md` names in kind files; no exact repeat, three restatements in other words found by reading and removed; no positive control ([author-report.md](reports/author-report.md)). The reviews later found restatements the check missed (whole-change Minor 2, corrected in the return step; return-step Minor 2, listed in the request).

## Slices

Not on the planned route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-10-28T00:01Z | Start | Orchestrator, Opus 5.5 | Frozen task, `task-cycle/skill/SKILL.md`, `agent-instructions/README.md`, part map, decision scopes of touched parts | Worktree, branch, base `0b8c1bd`; base checks below | Route: one author, `same` |
| 2026-10-28T00:10Z | Author dispatch | Orchestrator to author, Opus | [author-handoff.md](reports/author-handoff.md), `task-cycle/change/SKILL.md`, whole frozen task | reports/author-report.md (pending) | Make change with foundation step, return before review |
| 2026-10-28T00:31Z | Author return | Author, Opus | Same | [author-report.md](reports/author-report.md), commit `634fa3b` | `done with concerns`: added a fifth file `instruction-files/judging.md` beyond the handoff's list; passed to the review as information. Mechanical check: clean tree, range `0b8c1bd..634fa3b` one commit, each check with command and exit code. Focused tests ran before two last Markdown-only edits. |
| 2026-10-28T00:33Z | Whole-change review dispatch | Orchestrator to fresh reviewer, Opus | [review-handoff.md](reports/review-handoff.md), `task-cycle/review/SKILL.md`, range `0b8c1bd..634fa3b`, whole frozen task, author report | reports/review-report.md (pending) | Independent review |
| 2026-10-28T00:45Z | Whole-change review return | Reviewer, Opus | Same | [review-report.md](reports/review-report.md) | `PASS 634fa3b`; 0 blocking, 6 Minor, 0 out of scope; confirms `judging.md` as an application of WAY-256/WAY-258. Minor findings go to the request unfixed. |
| 2026-10-28T00:47Z | Return-step dispatch | Orchestrator to author (resumed), Opus | [return-handoff.md](reports/return-handoff.md), step 11 | reports/return-report.md (pending) | Compare entries with code |
| 2026-10-28T00:50Z | Return-step return | Author, Opus | Same | [return-report.md](reports/return-report.md), no commit | `done with concerns`: three mismatches of code with entries this change writes (WAY-256: Change/Place/Write reworded in `SKILL.md`; WAY-258: `kind_skill.md` repeats the one-level rule; `single-rule-compliance` stated more broadly in `SKILL.md`), left because the handoff said not to act on Minor findings. |
| 2026-10-28T00:52Z | Return-step correction of handoff | Orchestrator to author (resumed), Opus | Message: the handoff's "do not act on Minor findings" was too broad (C5) | reports/return-report.md (to be updated) | Correct the three mismatches as the return step's corrections (WAY-11) |
| 2026-10-28T00:57Z | Return-step return | Author, Opus | Same | [return-report.md](reports/return-report.md), commit `524d9b8` | `done`: Change/Place/Write moved to `changing.md`, `placing.md`, `writing.md`; one-level rule kept in `SKILL.md` alone; fact's qualifiers restored; a fourth mismatch (Place step 1 restating the add rule) pointed to its section. Mechanical: clean tree, one commit, checks with commands and exit codes. |
| 2026-10-28T00:58Z | Return-step review dispatch | Orchestrator to fresh reviewer, Opus | [return-review-handoff.md](reports/return-review-handoff.md), range `634fa3b..524d9b8` | reports/return-review-report.md (pending) | Review of the return step |
| 2026-10-28T01:03Z | Return-step review return | Reviewer, Opus | Same | [return-review-report.md](reports/return-review-report.md) | `PASS 524d9b8`; 0 blocking, 4 Minor, 0 out of scope; Minor findings go to the request |
| 2026-10-28T01:04Z | Target reconciliation | Orchestrator | `git fetch origin foundations`; `origin/foundations` = `0b8c1bd`, ancestor of HEAD | — | Already up to date; no merge, tree unchanged |
| 2026-10-28T01:16Z | Gate | Orchestrator | `python -B gate/run_tests.py` on `524d9b8` | [gate-524d9b8.log](reports/gate-524d9b8.log) | Exit 0, 613 tests |
| 2026-10-28T01:20Z | Stages and record | Orchestrator | `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/instruction-files-router/stages.md bbb978e3-af35-4972-aa8a-c437684d3df2` | [stages.md](stages.md), exit 0 | Record copied to `docs/task-cycles/instruction-files-router/`, committed, removal committed, pushed; request opened as draft, then marked ready |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Spec or plan needed? (step 4) | No spec, no plan; one author | Settlement rows 1–7 and To do 1–9 settle every meaning; layout is application | Spec of the file layout | Author returns `returned` with an open choice; one attempt discarded | Author |
| C2 | Does a docstring edit in a trust-boundary file count? (step 4) | Yes in letter; reviewer told to verify docstring-only | Part map `instruction-files` *Trust boundary* | Answer no | None beyond a narrower review | Reviewer |
| C3 | Guidelines selection (step 2, `product-guidelines/reading.md`) | Empty — the-way has no `guidelines/`; the task settles that it writes no code | Task's question on `product-guidelines/reading.md` | Wait for `wlasne_wytyczne_the_way.md` | None — the task settled it | Author, reviewer |
| C5 | Return step: correct mismatches that coincide with Minor review findings? | Yes — step 11 corrects in the same change whatever no longer matches the entries (WAY-11); the rule that Minor findings are not fixed governs review findings, not the return step's own comparison. The return handoff's "do not act on them" was the orchestrator's error, corrected. Minor 3 and 5 are no mismatch with an entry and stay unfixed for the request. | Return report; step 11; "The end of a code review" | Leave the three for the request | A rewording of process prose that a reviewer then checks; without it the first skill shaped by WAY-256/258 contradicts them | Author, return-step reviewer |
| C4 | Author's class (WAY-229) | `same` | Five parts touched | `cheaper` default | A cheaper author could misplace the split; cost is a review round | Author |
| C6 | Names of the kind files (author) | `kind_main_file.md`, `kind_skill.md`, `kind_path_rule.md` | author-report.md choice 1 | `skill.md` (clash with `SKILL.md` on case-insensitive filesystems), a `kinds/` subdirectory | Renames only | Author |
| C7 | A file for the judging mode beyond the handoff's list (author) | `judging.md`, named by the Judge step | WAY-256/WAY-258 as written; confirmed by the whole-change review | Keep judging in `SKILL.md` | Fold text back | Author, reviewer |
| C8 | Shared file for rules common to kinds? (author, row 5) | None — `SKILL.md` holds them; row 5's condition does not hold | author-report.md choice 3 | A shared file named by the step | One more file at each use | Author |
| C9 | Distribution of `principles.md` and its *Sources* list (author) | Sections over `SKILL.md`, kind files and `judging.md`; sources cited beside each principle | author-report.md choice 4 | Keep `principles.md` as a shared file read every time | Two tool-doc sources dropped (whole-change Minor 3, listed in the request) | Author |
| C10 | Split of rows 1–5 under WAY-19 (author) | WAY-256 (rows 1, 4), WAY-257 (row 3, asking part of row 2), WAY-258 (row 5), change to WAY-128 (rows 1, 2); row 1's number is WAY-256 | author-report.md choice 6 | One entry for rows 1–5; five entries | Renumbering before merge; the lesson map takes WAY-256 | Author, request |
| C11 | Row 2's evidence threshold in WAY-128 (author) | "once records of agents' work show they missed the reworded pointer"; WAY-130's "more than once" applies because putting a rule whole in the main file is adding a rule | author-report.md choice 7 | Write WAY-130's number into WAY-128 | A reader may take one miss as enough | Author |
| C12 | Change, Place and Write procedures under WAY-256 (return step) | Moved to `changing.md`, `placing.md`, `writing.md`, named by the table of modes | return-report.md; return-step review PASS | Keep short mode procedures in `SKILL.md` and name that reading | Three small files; return-step Minor 2 notes restatements to replace by pointers | Author, return-step reviewer |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | [task.md](task.md) | Human-approved source | Ready for cycle |
| Change and foundation entries | `634fa3b` | Author, Opus | `PASS 634fa3b` |
| Return step | `524d9b8` | Author, Opus | `PASS 524d9b8` |
| Handoffs and reports | [author-handoff](reports/author-handoff.md), [author-report](reports/author-report.md), [review-handoff](reports/review-handoff.md), [review-report](reports/review-report.md), [return-handoff](reports/return-handoff.md), [return-report](reports/return-report.md), [return-review-handoff](reports/return-review-handoff.md), [return-review-report](reports/return-review-report.md) | Orchestrator and agents | — |
| Gate logs | [gate-634fa3b.log](reports/gate-634fa3b.log), [gate-524d9b8.log](reports/gate-524d9b8.log) | Orchestrator | Exit 0 |
| Request text | [pr-body.md](reports/pr-body.md) | Orchestrator | — |
| Stages | [stages.md](stages.md) | `task-cycle/cycle_stages.py` | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B elements/common/foundation_check.py` | Orchestrator, base `0b8c1bd`, Windows | 0; 0 errors | — |
| `python -B agent-instructions/skill_entry_points.py` | Orchestrator, base `0b8c1bd` | 0; entry points are current | — |
| `python -B gate/run_tests.py instruction-files` | Orchestrator, base `0b8c1bd` | OK, 104 tests, 5 skipped (output line; exit code masked by a pipe to `tail`) | Full gate not run on the base; no known base failures |
| `python -B gate/run_tests.py` | Orchestrator, `634fa3b`, Windows, run while the review ran ([log](reports/gate-634fa3b.log)) | 0; 613 tests in 8 directories, every directory passed; 5 skips in `instruction-files` | — |
| Focused checks of author and reviewers | Author and reviewers, `634fa3b` and `524d9b8` | `foundation_check.py` 0; `skill_entry_points.py` 0; `run_tests.py instruction-files` 0 (104, 5 skipped); `run_tests.py agent-instructions` 0 (18); `check_instructions.py` on the skill's files 0 (0 errors, 5 dead-path warnings on example paths); `git diff --check` 0 | Author's focused tests ran before last Markdown-only edits, which no test reads |
| `python -B gate/run_tests.py` | Orchestrator, `524d9b8` (final tree), Windows ([log](reports/gate-524d9b8.log)) | 0; 613 tests in 8 directories, every directory passed | — |
| Manual: a fresh agent session using the rebuilt skill | — | not applicable | Not run: whether agents follow the new route is untested |

## Return step

- Foundation compared with code: WAY-128, WAY-256, WAY-257, WAY-258, `claude-skill-nested-references`, `instruction-density-accuracy`, the task's *Decisions in play*, the WAY-33 search's entries and the part map of the touched parts. Mismatches: Change/Place/Write reworded in `SKILL.md` against WAY-256; `kind_skill.md` restating the one-level rule against WAY-258; `single-rule-compliance` stated more broadly in `SKILL.md`; Place step 1 restating the add rule. All corrected in `524d9b8` (the first return left them under an over-broad handoff line, C5).
- Decisions written or changed: none in the return step (WAY-128, WAY-256, WAY-257, WAY-258 by the foundation step in `634fa3b`)
- Invariants written or changed: none
- Environment facts: none in the return step (`claude-skill-nested-references` new and `instruction-density-accuracy` changed in `634fa3b`)
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none (independent task)
- Rows of *Settlements to record* written: 1 → WAY-256 and WAY-128; 2 → WAY-128 and WAY-257; 3 → WAY-257; 4 → WAY-256; 5 → WAY-258; 6 → `claude-skill-nested-references`; 7 → `instruction-density-accuracy`

## Request handoff

- Request URL and status: see the request that links this record — ready for review
- Cycle and its reasons: no spec (the task settles every meaning); one author without a plan, class `same`, five parts; whole-change review PASS; the return step corrected four mismatches, its review PASS
- Process pin: none — the-way itself
- What this request settles: WAY-256, WAY-257, WAY-258 (new), WAY-128 (changed), `claude-skill-nested-references` (new fact), `instruction-density-accuracy` (changed fact), each with its Polish meaning sentence in [pr-body.md](reports/pr-body.md); no row tied to an entry already stated
- What the foundation puts in front of the human at the merge: none
- Checks: `python -B gate/run_tests.py` on `524d9b8`, exit 0; unchecked: no fresh session has used the rebuilt skill
- Human actions the request waits for: none
- Questions: none
- Review findings listed: whole-change Minor 3, 4, 5; return-step Minor 1–4; none outside scope
- Blocked by review: none
- Choices within the request: 12, in the questions table above
- Writes to the task's backlog entry: none
- Process remarks on the-way: (1) step 11 against "The end of a code review": when a return-step mismatch is also a Minor review finding, the skill does not say which rule wins; this cycle's orchestrator first wrote "do not act on them" and had to correct it (C5). (2) WAY-125's "reads … whole" against WAY-256's step files (whole-change Minor 4) decides whether rebuilding process skills saves anything.
