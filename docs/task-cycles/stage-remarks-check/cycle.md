# Cycle record — the script that checks the stage reports' "Searches not found or unclear" items against the cycle record's process remarks

- Task source: C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_pozne_etapy_w_uwagach_rekordu.md — settlements accepted 2026-11-05; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: C:\Storage\repos\the-way (the-way itself; worktree `.runs/worktrees/stage-remarks-check`)
- Process pin: not applicable — the-way is the product; the process is the worktree's own `task-cycle/`
- Target branch and base: `foundations` (origin/foundations), `b96cfff`. The session's main checkout stood at `61c72fb`, five commits behind; the task branch starts from the current `origin/foundations`, and this skill was read again from the worktree, since PR #72 changed `task-cycle/skill/SKILL.md` and `task-cycle/record_template.md`.
- Task branch: `task/stage-remarks-check`
- Status: request open

## Two questions at start

- Trust boundary: no — the part map gives `task-cycle` the trust boundary `none`; the script reads only the cycle's own record directory.
- Irreversible operation: no.

## Spec and execution route

- Open design choice at start: none — the three settlement rows fix the check (every item other than `none`, from both forms of the section, reported when missing from the remarks, re-run until clean), the order of the check before each archive commit, the rule for a report the orchestrator holds wrong, and the single form of the remarks block. How the script parses and matches is a choice of how to make what the task settles; the author makes it and names it.
- Reserved choice: none — the language and tooling are settled (WAY-38, WAY-89: Python 3.14, standard library only).
- Execution route and reason: one author without a plan. The change is one script with its tests, edits to three process files (`task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`, `task-cycle/record_template.md`) and the foundation entries of rows 1–3; one agent holds it.
- Author: one author with `make-change`, class `same` (Sonnet 5.5, harness model `sonnet`) — not `cheaper`: the author writes decision entries and parses report forms found in real archives, so the judgment is not ordinary implementation. Resumptions: for the return step (2026-11-06).
- Plan: none on the one-author route.
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: harness completion notification of a foreground or background `Agent` call; no limit beyond the harness's.
- Whole-change review: fresh reviewer (`review-change`, Sonnet 5.5, class `same`), range `b96cfff..5e90498`; `PASS 5e90498`, report reports/02-whole-review-report.md; 9 files changed (+953/-9: remarks_check.py 354, test_remarks_check.py 428, decisions.md 95, SKILL.md 50, record_template.md 15, request_template.md 10, blocked_finding.md 3, reserved_return.md 3, correction.md 4); every task item, the three settlement rows and both acceptance criteria covered; source fidelity checked against the digest script and the three loop2 archives; blocking 0, Minor 3, out of scope 0
- Review rounds: none — no review blocked, no fix; the return step made no commit, so it needed no review
- Weakest-point checks: author — every item of real reports in the forms agents write: independent count on 4 `loop2` extracts, found a BOM gap, fixed with a test (reports/01-author-report.md); reviewer repeated the idea on all 3+38+41 reports (reports/02-whole-review-report.md)

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used on the one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-05 | start | orchestrator, Sonnet 5.5 | task.md | cycle.md | worktree and branch from `b96cfff`; base gate started in `.runs/base-check-stage-remarks` (separate checkout of the base commit), output `base-gate.txt` |
| 2026-11-05 | one author | author, Sonnet 5.5 (class same), background Agent | reports/01-author-handoff.md, `make-change` whole change, frozen task | reports/01-author-report.md | done: commits `2a4847e`, `5e90498`; worktree clean; range non-empty; changed files match the task (script, tests, 3 process files + 3 more that commit a record, decisions.md); checks with commands and exit codes, own-work check and searches section present; base gate at `b96cfff`: 667 tests, exit 0 |
| 2026-11-06 | whole-change review | reviewer, Sonnet 5.5 (class same), fresh | reports/02-whole-review-handoff.md, `review-change`, range `b96cfff..5e90498` | reports/02-whole-review-report.md | dispatched; full gate on `5e90498` started in the task worktree in parallel |
| 2026-11-06 | whole-change review result | reviewer | — | reports/02-whole-review-report.md | `PASS 5e90498`; blocking 0, Minor 3 (M1 substring match, M2 request state for a listing held wrong, M3 escaped non-printable characters), out of scope 0; goes to the request's lists |
| 2026-11-06 | return step | author resumed (SendMessage), Sonnet 5.5 class same | reports/03-return-step-handoff.md, `return_step.md` | reports/03-return-step-report.md | dispatched; full gate on `5e90498` running in the task worktree (`gate-1.txt`) |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The main checkout's `foundations` was five commits behind origin (PR #72 touched the cycle's skill and record template). Source: `git log 61c72fb..origin/foundations`. | Base the task branch on `origin/foundations` and read the skill from the worktree. | `git diff 61c72fb origin/foundations` over `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` | Base on the stale local `foundations`: the script and template edits would conflict at merge with PR #72. | A merge conflict in the same two files. | branch |
| Q2 | Class of the one author. Source: SKILL step 4 (default `cheaper`). | `same` | see Author | `cheaper` (Haiku): the change writes decision entries and must read free-form report forms. | A fix round and a rewrite of the entries. | step 9 |
| Q3 | Which files of `reports/` are stage reports? Source: author's choice. | `reports/*report.md`. | author's report (reports/01-author-report.md) | Every `.md` in `reports/`: handoffs quote the section name as an instruction and give false items. | A report whose name does not end in `report` is not read; the cycle names its reports so. | script |
| Q4 | What is one item of the section? Source: author's choice. | A list item with continuation lines and sub-items joined into one line, or a paragraph where the section is no list; text after a bold label on its line is the first paragraph. | author's report (reports/01-author-report.md) | Printing the original lines. | Appended text differs from the original only in whitespace, which the match ignores. | script |
| Q5 | When does an item read `none`? Source: task's "other than `none`". | After stripping `*`, `_`, backticks, spaces and full stops it is `none` in any case; `none found` and `None unresolved. …` are items. | author's report (reports/01-author-report.md) | A looser reading that drops `none found`. | Noise in the nightly review, named in the task. | script |
| Q6 | Where does the match look? Source: author's choice, from the task's "inside the block the digest cuts". | Only inside the remarks blocks cut as `cycle_remarks_digest.py` cuts them (a port of its two functions), whitespace collapsed, exact words and case. | author's report (reports/01-author-report.md) | Matching anywhere in `cycle.md`. | The port must follow the digest; a change of the digest's rules is not seen here. | script |
| Q7 | Is an item that two reports give listed twice? Source: WAY-260 ("without combining repeated items"). | Yes, until the block holds it as many times as the reports give it. | author's report (reports/01-author-report.md) | Treating repeats as one item. | A repeat the orchestrator rightly wrote once is listed again. | script, WAY-294 |
| Q8 | Where does a bold-label section end that is no list item? Source: author's choice. | At the next heading, rule, or non-list line that starts with bold text. | author's report (reports/01-author-report.md) | Reading to the end of the file. | A section whose paragraphs start with bold text outside a list ends early; the real archives hold none. | script |
| Q10 | Where is the last run of the remarks check recorded? Source: author's choice. | Under *Verification* of the record, not in a new field of *Request handoff*. | author's report (reports/01-author-report.md) | A new field in the template. | None beyond one more field avoided. | SKILL.md, record template |
| Q11 | Where in step 12 does the check run? Source: author's choice. | Right after `cycle_stages.py`, before the description is written, and again before the commit if a report or remark changed. | author's report (reports/01-author-report.md) | After the description. | A listing held wrong would not reach the description. | SKILL.md |
| Q12 | What does the script do with no `reports/` directory or no `cycle.md`? Source: author's choice. | No `reports/`: no listing, exit 0. No `cycle.md`: exit 2. | author's report (reports/01-author-report.md) | Exit 1 for both. | A record with no reports reads as clean. | script |
| Q13 | Which files beyond the three the task names carry the call? Source: handoff ("the blocked variants"). | `blocked_finding.md` and `reserved_return.md` commit a record, so each got the call; `request_template.md` got item 10, a *Checks* mention and a variant row. | author's report (reports/01-author-report.md) | Leaving the blocked variants without the call. | A blocked request would archive a record unchecked. | SKILL.md, templates |
| Q9 | What is the request's state when a listing is held wrong? Source: row 2 of the task ("as with `request_check.py`"). | Unchanged: the state the request has for its other causes; the case stands in the remarks, in *For you to decide* and in *Checks*. | author's report (reports/01-author-report.md) | Draft state as for the form check (WAY-291). | A request marked ready carries a decision item; its first line says whether anything waits below. | SKILL.md, request_template.md; human decision item 1 |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/stage-remarks-check/task.md` | orchestrator | n/a |
| Code and process text | `2a4847e` | one author | `PASS 5e90498` |
| Foundation entries WAY-294 to WAY-296 | `5e90498` | one author | `PASS 5e90498` |
| Reports | `reports/01-author-report.md`, `02-whole-review-report.md`, `03-return-step-report.md` | author, reviewer, author | n/a |
| Stages | `stages.md` | orchestrator | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (base) | orchestrator, `b96cfff`, checkout `.runs/base-check-stage-remarks` | exit 0, 667 tests in 8 directories (`base-gate.txt`) | none failed; no check failing on the base |
| `python -B gate/run_tests.py` (change) | orchestrator, `5e90498` (the final tree: the return step made no commit, `origin/foundations` unmoved at `b96cfff`), task worktree | exit 0, 712 tests in 8 directories (`gate-1.txt`) | none failed; 5 tests skipped by themselves in `instruction-files`, as on the base |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/stage-remarks-check` | orchestrator, task worktree | first run exit 1 (10 items listed, all appended), last run exit 0, `checked: 3 reports, 10 items other than none, 0 not in the process remarks` | none |
| `python -B elements/common/foundation_check.py` | author and reviewer, `5e90498` | exit 0, `0 errors` | none |
| `python -B gate/run_tests.py task-cycle` | author, reviewer and return step, `5e90498` | exit 0, 137 tests | none |

## Return step

- Foundation compared with code: WAY-294 to WAY-296 (written), WAY-260, WAY-148, WAY-38, WAY-89, WAY-290, WAY-291 and the part map of `task-cycle` and `decisions`, each compared with the script, the process text and the template: nothing no longer matched, no correction (reports/03-return-step-report.md)
- Decisions written or changed: none in this step (WAY-294, WAY-295, WAY-296 written at the foundation step)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 as WAY-294, row 2 as WAY-295, row 3 as WAY-296

The return step made no commit; head stays `5e90498`, so it needed no review.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/73 — draft at opening, marked ready for review after the record's link is in the description
- Description: written and checked after this commit (`request.md` beside this record, by `task-cycle/skill/request_template.md`); the form check's last run is named in the description under *Checks*
- Writes to the task's backlog entry: the request link `[url::https://github.com/mariusznazar/the-way/pull/73]` added to its line in `_tasks_active.md`; the state `[/]` left as it was
- Process remarks on the-way:
  - one author (make-change, whole change), docs/task-cycles/stage-remarks-check/reports/01-author-report.md: A test guideline for the-way's own scripts (WAY-215): not found, as the handoff says; I followed the existing tests of `task-cycle/` (unittest, fixtures written in the test file, expected values written out).
  - one author (make-change, whole change), docs/task-cycles/stage-remarks-check/reports/01-author-report.md: The stage name for a report cannot be read from a path (a report path such as `37-reconciliation-report.md` does not give it reliably), so the script prints only the report path and the orchestrator takes the stage name from the Events; unclear whether the task wanted the script to print a stage name too.
  - one author (make-change, whole change), docs/task-cycles/stage-remarks-check/reports/01-author-report.md: The task says `reset-hasla` 37 and 38 hold two items each; the script finds three each. Unclear where the count of two came from (a count of only the unclear items, or of the items other than `none found`).
  - one author (make-change, whole change), docs/task-cycles/stage-remarks-check/reports/01-author-report.md: Whether a report with no recognised section (a form I did not see) should be listed: the task asks only for items, so the script lists nothing for it. A report that lacks the section is repaired by the orchestrator at the report's arrival (WAY-260), not by this script.
  - one author (make-change, whole change), docs/task-cycles/stage-remarks-check/reports/01-author-report.md: Whether the "critique before collective review" step applies to three entries already accepted as rows of a task document: not run (no subagents for me).
  - whole-change review (review-change), docs/task-cycles/stage-remarks-check/reports/02-whole-review-report.md: A guideline for the-way's own scripts and tests (WAY-215): not found, as the handoff says (no `guidelines/` directory); I judged the tests against the existing tests of `task-cycle/`.
  - whole-change review (review-change), docs/task-cycles/stage-remarks-check/reports/02-whole-review-report.md: Where the task's count "two items each" for `reset-hasla` reports 37 and 38 comes from: unclear; the script finds three each, and all three of each are real, unheld bullets.
  - whole-change review (review-change), docs/task-cycles/stage-remarks-check/reports/02-whole-review-report.md: Whether "as with `request_check.py`" in row 2 was meant to include the draft state of WAY-291: unclear from the task (M2).
  - whole-change review (review-change), docs/task-cycles/stage-remarks-check/reports/02-whole-review-report.md: A way to check the script's port against the live digest inside the repository's own tests: not found (the digest lies outside the repository); I compared them by hand once, as above.
  - return step (make-change), docs/task-cycles/stage-remarks-check/reports/03-return-step-report.md: Whether `task-cycle/record_template.md` should name `cycle_remarks_digest.py`, a script of the author's private notes outside the repository: I wrote that name at the first stage, to say why the block has the form it has. Unclear whether a file of the-way may name it. The comparison finds no foundation entry against it, so I left it.
  - the orchestrator: the project skill entry point `the-way-implement-task` reads the process from the checkout the session started in; the main checkout's `foundations` was five commits behind `origin/foundations`, so the skill first read was out of date and the cycle read it again from the task worktree.
