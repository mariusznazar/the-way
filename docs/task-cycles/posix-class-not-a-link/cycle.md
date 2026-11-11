# Cycle record — the way: the private-paths check does not list a POSIX character class in double brackets as a note link

- Task source: the task document in the author's private backlog (`zadanie_the_way_klasa_znakow_posix_nie_jest_linkiem.md`), `Status: ready for cycle`; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: https://github.com/mariusznazar/the-way (the-way itself)
- Process pin: n/a (the-way itself; checkout at base)
- Target branch and base: `foundations`, `e1726b78ad357791c5f84dd946f0edd26cdc3fe8`
- Task branch: `task/posix-class-not-a-link`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits `task-cycle/private_paths_check.py`, its test and one decision; the part map names no network, key, deployment or outside-file boundary for them (the script only reads files it is given and lists text).
- Irreversible operation: no

## Spec and execution route

- Open design choice at start: none — Q1 (twelve POSIX class names, `[ [:name:] ]` only) and Q2 (the shared pattern list, so every check that looks for a link) are settled by the task; the form of the exception inside `NOTE_LINK` is how to make what the task settles.
- Reserved choice: none
- Execution route and reason: one author without a plan — one regex change, one test class, one decision edited in place; fits one agent.
- Author: class `cheaper` (the default for ordinary implementation), model haiku; it also does the foundation step and the return step.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: native completion notification of the Agent tool
- Whole-change review: reviewer other than the author (sonnet), `review-change`; range `e1726b7..8fa6bac`, first line `PASS 8fa6bac2a7af84c73f54d7c8320c9077592f955b`, `reports/review_report.md`; `foundations/decisions.md` +26 −10, `task-cycle/private_paths_check.py` +14 −7, `task-cycle/test_private_paths_check.py` +29, `task-cycle/test_tracked_private_paths_check.py` +9; every task item, the answers of pytania 1 and 2 and settlement row 1 covered; 0 blocking, 2 Minor (1 within the task, fixed; 1 outside the task, `[ [[:space:] ]` still listed).
- Review rounds: none blocked. The Minor finding within the task (WAY-323 rationale clause) was fixed in `15c2062` (`reports/fix_findings.md`, `reports/fix_report.md`) and reviewed once by the same reviewer: `PASS 15c20628d005500efe761d174650edc80a0d42d1`, `reports/fix_review_report.md`, no new finding, nothing reverted.
- Weakest-point checks: author — the exception must hold in every check that looks for a link and a real link or path on the same line must stay listed; checked by a scratch record directory run through `private_paths_check.py` (exit 1, lists `[ [Notatka] ]` and the path, not `[[:alpha:]]`), `reports/author_report.md` own-work check.

## Slices

none (one author)

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-11 | start | orchestrator (sonnet 5.5) | task read; branch `task/posix-class-not-a-link` from `e1726b7`; base gate started in `.runs/base-check-posix-class-not-a-link` | `.runs/base-check-posix-class-not-a-link.log` | route: one author |
| 2026-11-11 | change | author (haiku, class cheaper) | `reports/author_handoff.md`, make-change one author | `reports/author_report.md`, commit `8fa6bac` | done; mechanical check passed (clean tree, non-empty range e1726b7..8fa6bac, 4 files); next: whole-change review |
| 2026-11-11 | whole-change review | reviewer (sonnet) | `reports/review_handoff.md`, review-change | `reports/review_report.md` | PASS 8fa6bac; 1 Minor within the task, 1 outside; next: fix of the Minor |
| 2026-11-11 | fix | author resumed (haiku) | `reports/fix_handoff.md`, `reports/fix_findings.md`, make-change fix | `reports/fix_report.md`, commit `15c2062` | done; next: review of the fix |
| 2026-11-11 | fix review | reviewer resumed (sonnet) | range `8fa6bac..15c2062` | `reports/fix_review_report.md` | PASS 15c2062, no new finding |
| 2026-11-11 | return step | author resumed (haiku) | `reports/return_handoff.md`, `task-cycle/skill/return_step.md` | `reports/return_report.md` | done, no commit; open point: WAY-323 *Based on* `none` |
| 2026-11-11 | gate | orchestrator | `python -B gate/run_tests.py` on `15c2062` | `reports/gate_final.log` | exit 0, 919 tests in 9 directories |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the exception cover a capital-letter name (`[ [:Space:] ]`) and a class without its closing colon (`[ [:alpha] ]`)? Source: task says exactly `[ [:nazwa:] ]` of twelve names | Neither: the exception is case-sensitive and needs the exact form | `reports/author_report.md` (Choices made); review probe lists `[ [:ALPHA:] ]` | exempt more forms — the task limited it to the twelve exact names (pytanie 1) | a false hit on a rare text, or a note titled so is listed (as intended) | author |
| Q2 | May WAY-323 *Based on* stay `none` for the twelve class names? Source: `reports/return_report.md` open point | Yes, `none`: the names are fixed by the list in the decision itself, taken from the task's settlement; no quotable local source of the POSIX list was found | `reports/return_report.md` | add an environment fact or a `TODO` — would need a source outside the product, not fetched | the decision rests on an unrecorded outside list; shows to a reader asking why these twelve | return step; request item |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/posix-class-not-a-link/task.md` | orchestrator | n/a |
| code and foundation entry | commit `8fa6bac` | author (haiku) | PASS (`reports/review_report.md`) |
| fix of a Minor finding | commit `15c2062` | author (haiku) | PASS (`reports/fix_review_report.md`) |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on base | orchestrator, `e1726b7`, separate checkout of the base | 0 — 913 tests in 9 directories, every directory passed; no check failing on the base | none |
| `python -B gate/run_tests.py` on the final tree | orchestrator, `15c2062` | 0 — 919 tests in 9 directories, every directory passed (913 + 6 new) | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0 — merges 22, threshold 30, `reminder: no` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/posix-class-not-a-link` | orchestrator, original record | 0 after 2 runs (first run exit 1 listed 6 items, appended to the process remarks) | none |
| `python -B task-cycle/private_paths_check.py docs/task-cycles/posix-class-not-a-link` | orchestrator, cleaned copy | 0 after 2 runs (first run exit 1 listed 56 places, cleaned by one rewriting) | none |
| `python -B task-cycle/image_files_check.py docs/task-cycles/posix-class-not-a-link` | orchestrator, cleaned copy | 0, 1 run | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/posix-class-not-a-link` | orchestrator, cleaned copy | 0, 1 run | none |
| `python -B task-cycle/request_check.py` and `private_paths_check.py` on the description | orchestrator | 0 and 0 (private-paths check: exit 1 first with 14 places, then 0 after 2 runs; form check 2 runs, 0) | none |

## Return step

- Foundation compared with code: WAY-323 (edited), WAY-328 (named by the task), WAY-309, WAY-320, WAY-324 and the invariant `tracked-file-private-paths` (found by the search), and the part map entry of `task-cycle`, each compared with the code; nothing no longer matched (`reports/return_report.md`)
- Decisions written or changed: WAY-323 (in place, row 1)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — WAY-323

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/101 — draft, to be marked ready after the record is committed
- Description: (to fill)
- Writes to the task's backlog entry: none
- Process remarks on the-way:
  - change (the one author), .runs/task-cycles/posix-class-not-a-link/reports/author_report.md: How the gate calls `foundation_check.py`: the handoff says "see how the gate calls it". `grep` for `foundation_check` in `gate/` finds no call; the form check is run by its own tests (`elements/common/test_foundation_check.py`) and by the decision skill's command. I did not find the gate's call and did not dig further; the gate was not run.
  - change (the one author), .runs/task-cycles/posix-class-not-a-link/reports/author_report.md: The first read of `task-cycle/change/SKILL.md` used a relative path from the reports directory; I re-read it by its absolute path from the worktree root, and the text matches the one that was read. Recorded because the first path resolved without an error and I did not establish why.
  - change (the one author), .runs/task-cycles/posix-class-not-a-link/reports/author_report.md: No glossary entry for note link or character class (grep, none found).
  - return step, .runs/task-cycles/posix-class-not-a-link/reports/return_report.md: A local source for the POSIX character class names with a quotable passage: not found (see the open point above).
  - whole-change review, .runs/task-cycles/posix-class-not-a-link/reports/review_report.md: The two files in `task-cycle/skill` the author said describe the rule (`request_template.md`, `SKILL.md`): I did not confirm by reading that nothing there restates the exception; the `grep` for the rule's prose found no match.
  - whole-change review, .runs/task-cycles/posix-class-not-a-link/reports/review_report.md: Whether the 12 hits of the source product were all `[[:space:]]`/`[[:alpha:]]` or also other of the twelve names: the task says "all that class"; unverified here (outside the repository).
