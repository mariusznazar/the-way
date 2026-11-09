# Cycle record — the way: a product rule may read "test" while its test is written later in the same change, and an automatic check keeps it

- Task source: the task document `zadanie_the_way_metoda_niezmiennika.md` in the author's backlog (`_zadania\`), `Status: ready for cycle`; frozen copy `.runs/task-cycles/invariant-method-on-finished-change/task.md` (copied 2026-11-09)
- Task relation: independent
- Product repository: the-way (public repository; target branch `foundations`)
- Process pin: this checkout (the-way itself), base commit `46bba355e51bc671a4af604e11757d91574949b6`
- Target branch and base: `foundations` at `46bba355e51bc671a4af604e11757d91574949b6` (fetched 2026-11-09; local equals origin)
- Task branch: `task/invariant-method-on-finished-change` in worktree `.runs/worktrees/invariant-method-on-finished-change`
- Status: request open

## Two questions at start

- Trust boundary: no — the touched files (`foundations/decisions.md`, `foundations/invariants.md`, `elements/invariants/template.md`, `elements/common/foundation_check.py`, its test, `elements/common/way_of_working.md`) belong to the parts `decisions`, `invariants`, `elements-common`, whose *Trust boundary* is `none` in the part map.
- Irreversible operation: no — the change edits text, a check script and its tests; nothing is run outside the repository.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the four *To do* items, questions 1–4 and settlement rows 1–3 settle the wording, the place of the check, the switch's role and the invariant. Left to the author as how-to choices (recorded as autonomous choices): the name of the switch, whether the rejected way enters *Rejected* of WAY-61 (row 1's open point), whether row 2 is a decision of its own.
- Reserved choice: none
- Execution route and reason: one author without a plan — one agent can hold it: one script check with its tests, two small text edits (WAY-61, invariants template), a one-line edit of the way of working, three foundation entries.
- Author: one author, class `same` as the orchestrator (`sonnet`), because the change touches three parts (decisions, invariants, elements-common) and edits the wording of an approved decision and a script with its tests; resumed for the fix and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code — a background agent reports by completion notification; the turn yields while it runs.
- Whole-change review: reviewer opus (agent `aec99deb9a4e3d317`), `review-change`, range `46bba35..e3fcc20`, first line `PASS e3fcc2025fa436467400f3ba56711c60f47f9c91`, `reports/review-whole-report.md`; 8 files, +178/−26 (README.md 2/2, installation/README.md 4/2, elements/common/foundation_check.py 31/6, test_foundation_check.py 61/1, way_of_working.md 5/2, elements/invariants/template.md 6/3, foundations/decisions.md 59/10, foundations/invariants.md 10/0); coverage: To do 1–4 and rows 1–3 met, questions 1–4 not reopened, source fidelity checked; no plan.
- Review rounds: (1) whole change `46bba35..e3fcc20`, `PASS`, no blocking finding; Minor within the task M1, M2, M3 fixed in one fix `e3fcc20..7c3161a` by the resumed author (`reports/fix-1-report.md`); review of the fix by the same reviewer: `PASS 7c3161a` (`reports/review-fix-1-report.md`), no remaining or new finding. No revert. No blocking finding remained.
- Weakest-point checks: author — requirement named: the new check reports on tracked non-Markdown files only, like the existing citation check; check: tests for a Markdown citation, an untracked file and a tracked file (the first two failed before the code), plus a test that the switch skips no other error; showed all pass; `reports/author-report.md`. Whole-change reviewer repeated it with scratch runs (empty repository, another invariant's citing line deleted: exit 1 without the switch, exit 0 with it); `reports/review-whole-report.md`. Fix — requirement: invariant and WAY-61 name each other consistently; check: `foundation_check.py` exit 0; `reports/fix-1-report.md`.

## Slices

Not applicable: one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-09 09:02 | Setup | orchestrator, sonnet | worktree and branch from `46bba35` | — | `task/invariant-method-on-finished-change` created; base gate started in `.runs/base-check-invariant-method-on-finished-change` (first start was lost with its shell, no result; restarted) |
| 2026-11-09 | Author | one author, `make-change` whole change, sonnet | `reports/handoff-author.md`, frozen task | `reports/author-report.md` | `done`; commits `9d499d0`, `e3fcc20`; clean worktree, non-empty range `46bba35..e3fcc20`; report holds commands and exit codes, own-work check and Searches section; 8 files +178/-26; base gate known green; next: review of the whole change |
| 2026-11-09 | Whole-change review | reviewer, opus (`review-change`) | `reports/handoff-review-whole.md`, range `46bba35..e3fcc20` | `reports/review-whole-report.md` | `PASS e3fcc20`; 0 blocking, 3 Minor within the task (M1 rationale wording of WAY-61, M2 `test-method-citation` derives from WAY-321 only, M3 docstring line of 101 characters), 0 out of scope; 8 files +178/-26; next: one fix for the Minor findings (WAY-161) |
| 2026-11-09 | Fix of Minor findings | author resumed, sonnet (`make-change`, the fix of a review's findings) | `reports/findings-whole-1.md`, base `e3fcc20` | `reports/fix-1-report.md` | `done`; commit `7c3161a` (3 files +10/-9); M1, M2, M3 fixed; elements/common gate-focused run exit 0 (117 tests), foundation_check exit 0; Searches: none; clean worktree, non-empty range |
| 2026-11-09 | Review of the fix | same reviewer resumed, opus (`review-change`, fix) | range `e3fcc20..7c3161a`, `reports/fix-1-report.md` | `reports/review-fix-1-report.md` | `PASS 7c3161a`; no remaining or new findings; M1–M3 confirmed fixed; next: gate by the orchestrator, then the return step |
| 2026-11-09 | Gate | orchestrator | `python -B gate/run_tests.py` on `7c3161a` | `.runs/gate-7c3161a.log` | exit 0, 834 tests in 9 directories |
| 2026-11-09 | Return step | author resumed, sonnet (`make-change`, return step) | `reports/handoff-return-step.md`, `task-cycle/skill/return_step.md` | `reports/return-step-report.md` | dispatched |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Name of the switch that skips the new report (task question 2 leaves it to the author) | `--skip-test-citations` | `reports/author-report.md`, Choices | `--before-tests`, `--entry-mode` (name the situation, not the effect) | a rename of one flag and its mentions | author |
| Q2 | Does the way rejected at question 1 enter *Rejected* of WAY-61 (row 1's open point)? | yes, with its cost from question 1, no file names | `reports/author-report.md`; decisions template, WAY-134 | leaving it only in the task's history | one clause to delete | author |
| Q3 | Is row 2 a decision of its own or part of WAY-61? | a decision of its own, WAY-321 | `reports/author-report.md` | folded into WAY-61 | merge two entries | author |
| Q4 | What does `test-method-citation` derive from? | first WAY-321 only; after the review's M2 (accepted, the reviewer's suggestion) WAY-61 · WAY-321 and WAY-61's *Verification* names it | `reports/author-report.md`, `reports/review-whole-report.md` M2, `reports/fix-1-report.md` | WAY-321 only | one link and one line | author, fix |
| Q5 | Two one-clause edits of `README.md` and `installation/README.md`, outside the task's list | kept | `reports/author-report.md`; reviewer: within the reach of the change, would keep them | leaving the two descriptions untrue | revert two clauses | author |
| Q6 | Where does the error stand? | at the *Method* line of the invariant | `reports/author-report.md` | at the citation search | none | author |
| Q7 | Reading of the reviewer's M1 smaller point (the *Rejected* clause about `TODO`) | author left it unchanged, reviewer withdrew it | `reports/fix-1-report.md`, `reports/review-fix-1-report.md` | rewording the clause | one clause | fix |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Code and foundation commits | `46bba35..9d499d0..e3fcc20..7c3161a` on `task/invariant-method-on-finished-change` | one author (sonnet) | `PASS e3fcc20` (whole change), `PASS 7c3161a` (fix) |
| Full reports | `reports/author-report.md`, `reports/review-whole-report.md`, `reports/findings-whole-1.md`, `reports/fix-1-report.md`, `reports/review-fix-1-report.md`, `reports/return-step-report.md` | agents | see above |
| Stages | `stages.md` | orchestrator | — |
| Frozen task | `.runs/task-cycles/invariant-method-on-finished-change/task.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base, separate checkout `.runs/base-check-invariant-method-on-finished-change`) | orchestrator, `46bba35`, Windows | exit 0; `826 tests in 9 directories; every directory passed` (log `.runs/base-check-invariant-method-on-finished-change.log`) | none failed on the base |
| `python -B gate/run_tests.py` (reviewed change, worktree head `7c3161a`, Windows; log `.runs/gate-7c3161a.log` outside the record) | orchestrator | exit 0; `834 tests in 9 directories; every directory passed` | none failed, none unrun |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator, `46bba35` | exit 0; `merges: 15`, `threshold: 30`, `reminder: no` | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/invariant-method-on-finished-change/request.md --task .runs/task-cycles/invariant-method-on-finished-change/task.md` | orchestrator | exit 0, 1 run so far (before the record's link) | none |
| `python -B task-cycle/private_paths_check.py .runs/task-cycles/invariant-method-on-finished-change/request.md` | orchestrator | exit 0, 1 run so far | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/invariant-method-on-finished-change` (original) | orchestrator | first run exit 1 (2 items not in the remarks, appended), second run exit 0; 2 runs | none |

## Return step

- Foundation compared with code: WAY-61, WAY-321, `test-method-citation`, WAY-16, WAY-63, WAY-65, WAY-160, the invariants template and skills, `way_of_working.md`, `installation/README.md`, the install guidance and the part-map entries `decisions`, `invariants`, `elements-common`, `foundation-check-command`, `test-runner-command`, compared with the code: nothing no longer matched, no correction, no commit (`reports/return-step-report.md`); two open points reported, left unchanged (WAY-61 *Scope* without `task-cycle`; the planned-slice gap)
- Decisions written or changed: WAY-61 (edited, row 1), WAY-321 (new, row 2) — both by the foundation step; the return step wrote none
- Invariants written or changed: `test-method-citation` (new, set by row 3 of the task)
- Environment facts: none
- Glossary terms: none ("finished change" and "citing test" fail the WAY-95 test)
- Part-map changes: none
- Projected entries written whole or in part: none (independent task)
- Rows of *Settlements to record* written: row 1 WAY-61, row 2 WAY-321, row 3 `test-method-citation`

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/93 — draft at opening, marked ready after the record's link is in the description
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check last run exit 0, 1 run before the record's link; written and checked after this commit for the record's link and the checks on the copy
- Writes to the task's backlog entry: none (the cycle did not touch the author's private backlog)
- Process remarks on the-way:
  - Author, `.runs/task-cycles/invariant-method-on-finished-change/reports/author-report.md`: The handoff names `installation/README.md:71-74` among the files to read; no instruction says whether a product's description of its command must repeat the switch rule — I added a clause (see choices).
  - Author, `.runs/task-cycles/invariant-method-on-finished-change/reports/author-report.md`: No `guidelines/` directory in the-way (settled by the task's question 3), so no guideline to follow; the style of the neighbouring script and tests was followed.
  - Author, `.runs/task-cycles/invariant-method-on-finished-change/reports/author-report.md`: Unclear whether *Scope* of WAY-61 should gain `task-cycle`, since its new sentence now speaks of the cycle's slices; left unchanged (not in the task).
  - Author, `.runs/task-cycles/invariant-method-on-finished-change/reports/author-report.md`: The task says 16 `test` invariants at `a3206c1`; the base holds 18 and the tree 19 with the new one (`grep -c` of the `Method: test` lines). The check passes on all of them.
  - Whole-change review, `.runs/task-cycles/invariant-method-on-finished-change/reports/review-whole-report.md`: The handoff's point 4 speaks of "the task's return-step duty (entries true to the code)"; the task document holds no such phrase. I judged the README edits against the task and WAY-321 instead.
  - Whole-change review, `.runs/task-cycles/invariant-method-on-finished-change/reports/review-whole-report.md`: No `guidelines/` directory in the-way, so no guideline was compared (settled by the task's question 3).
  - Fix of Minor findings, `.runs/task-cycles/invariant-method-on-finished-change/reports/fix-1-report.md`: None. The findings file named exact places; all found by text.
  - Return step, `.runs/task-cycles/invariant-method-on-finished-change/reports/return-step-report.md`: None beyond the two open points above.
