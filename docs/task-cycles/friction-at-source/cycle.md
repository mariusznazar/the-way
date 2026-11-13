# Cycle record — the way: steps "check it yourself" in the request, pointing at a place in a task by its heading, the foundation review asks about the end of a transitional state

- Task source: the task document of the author's private backlog, the task's note in the `_zadania` folder beside the file of the entry `tasks` under `the-way`; `Status: ready for cycle`, document updated 2026-11-12, settlements cut 2026-11-12; frozen copy `task.md` beside this record.
- Task relation: independent
- Product repository: the-way (remote mariusznazar/the-way)
- Process pin: not applicable — the cycle runs on the-way itself, which pins no other checkout.
- Target branch and base: `foundations`, 6814c6f6c9ff2b29d34612fa5cc86945ec3a2812 (equal to `origin/foundations` after a fetch; the checkout was clean and needed no fast-forward)
- Task branch: `task/friction-at-source`, in the worktree `.runs/worktrees/friction-at-source`
- Status: running

## Two questions at start

- Trust boundary: no — the change edits the template of a request's description (`task-cycle/skill/request_template.md`), the template of a task document and the skill that refines tasks (`project-level/`), the skill of the foundation review (`foundation-review/`), and entries of `foundations/decisions.md` and `foundations/glossary.md`. None of these files is a trust boundary of the part map: the boundary files are scripts of `task-cycle/`, `project-level/`, `process-audit/`, `installation/` and `instruction-files/` that the change does not touch.
- Irreversible operation: no — the change is text in tracked files; nothing is deleted, migrated or run against data outside the repository.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — each of the three points is settled by a question of the task (2, 3, 4) with its ways not chosen, and the four accepted rows of *Settlements to record* settle their entries. The task leaves open only the wording of the entries, the number of the new decisions (WAY-353 onward) and the form of the glossary entry, which are choices of how to make what is settled, not design choices (WAY-135). WAY-327 is changed in place (task question 4 says so); the two new decisions are rows 1 and 2.
- Reserved choice: none — no language, framework, library, store of data, way of logging in or place to run is involved.
- Execution route and reason: one author without a plan. The change is prose in about eight files of five parts (task-cycle, project-level, foundation-review, decisions, glossary), no script is written, and every entry is settled; one agent can hold it. Planning would add a plan stage for a change a single reading covers. Judged from the task document; repeated after no spec, since none was written.
- Author: one author with `make-change`, class `same` as the orchestrator's (not `cheaper`), model `sonnet`. Reason for the class: the change spans five parts, and writes three foundation entries and a glossary entry whose wording binds later work; a wording slip in a decision is paid for by every later cycle. Resumptions and replacements: none yet.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code; a foreground `Agent` call blocks, a background agent reports by completion notification, so the turn yields when only that result remains. No limit beyond the harness's.
- Whole-change review: reviewer other than the author (a fresh general-purpose agent on sonnet, `review-change`), range 6814c6f..e51d835, first line `PASS e51d835`, report `reports/review-whole-change-report.md`; changed files 10 (184 added, 23 removed); every task item, every settlement row (1–4) and every *Decisions in play* entry covered, source fidelity judged; 0 blocking, 7 Minor within the task, 0 outside; resumed once for repair (exit code of one check; ten decisions whose titles bore on the change read whole; 27 invariants of the touched parts), no grade changed; 32 decisions read whole and 175 by title of 207 selected; none named unread whose title bears on the change; no blocking finding, so no slice to name.
- Review rounds:
  - findings `reports/fix-findings.md`: the review of the whole change `PASS e51d835` listed seven Minor findings within the task, none outside its scope; the one author, resumed on its class, fixed all seven in `6e4669e` (range e51d835..6e4669e, report `reports/fix-author-report.md`); the same reviewer, resumed, reviewed the fix once, `PASS 6e4669e` (report `reports/review-fix-report.md`), 0 new findings, none of the seven remaining, one Minor note (the command rule is the author's reading and no decision states it), which goes to the request's list; no fix was reverted.
- Weakest-point checks: the author's own-work check (`reports/author-report.md`): the requirement that the form check and the skeleton stay as they are while a description carries the new fifth part; the new example item put into the three groups of a valid description and checked by the form check's reader, exit 0, `problems: []`; the skeleton test passes. The fix's author ran it again after the fix (`reports/fix-author-report.md`), exit 0.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: the one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-13 | start | orchestrator, sonnet 5.5 | `task-cycle/skill/SKILL.md`, task document read whole, `agent-instructions/README.md`, request template (item 4 of the kinds), `project-level/task/template.md`, part map | this record, `task.md` | `Status: ready for cycle`, *Human actions* `none`, `Project relation: independent`. Reconciled with sources: `foundations` moved from 2292f33 to 6814c6f (29 commits); the decisions that changed in that range are WAY-347 to WAY-352 (new) and a few reworded ones about the audit; none of the entries named under *Decisions in play* changed (WAY-327 compared word for word). The part map changed only in trust-boundary lines of `task-cycle` and the external-context table. No effect on the task. |
| 2026-11-13 | base | orchestrator | worktree `.runs/worktrees/friction-at-source` from 6814c6f; base checkout `.runs/base-check` | `.runs/base-check.log`, `gate_times.md` | Gate on the base started through `task-cycle/gate_times.py` in the background; result goes under *Verification*. |
| 2026-11-13 | author | author (general-purpose, sonnet), `make-change`: the whole change as the one author | `reports/author-handoff.md`; frozen task; entries named there | `reports/author-report.md`; commits ffeadc7, 32f9904, e51d835 | `done with concerns`: 3 commits, 10 files; checks passed (foundation_check 0 errors; `gate/run_tests.py task-cycle` 365 tests, `project-level` 275 tests; private-paths check on each file; own-work check). Concerns: (1) the handoff's `skill_entry_points.py --check` does not exist — the script has no such flag, the no-argument form (exit 0) checks; my error in the handoff, no effect on the change; (2) steps for the human vs WAY-286's no-file-names rule; (3) a reading of WAY-329 in WAY-354's rationale. Mechanical check: clean worktree, non-empty range, no slice rows to compare, each check with command and exit code, **Unread material** and **Searches not found or unclear** present, own-work check present. Unread material (some invariants by title, six files of `project-level/task/skill/` unread, `foundation-review/remarks.md` in part): autonomous choice Q3, below. Next: review of the whole change. |
| 2026-11-13 | whole-change review | reviewer (general-purpose, sonnet), `review-change`: the whole change | `reports/review-whole-change-handoff.md`; range 6814c6f..e51d835; frozen task; author report | `reports/review-whole-change-report.md` | `PASS e51d835`: 0 blocking, 7 Minor within the task, 0 outside; 32 decisions read whole and 175 by title (after repair). The first report lacked an exit code for `project-level` and left unopened decisions whose titles bear on the change (WAY-150); both returned to the reviewer for repair (same agent resumed, read-only), which gave exit 0, read the ten decisions whole and the 27 invariants by Part, and found no change of grade. Next: fix of the Minor findings (WAY-161). |
| 2026-11-13 | fix of the Minor findings | author resumed (sonnet), `make-change`: the fix of a review's findings | `reports/fix-handoff.md`; findings file `reports/fix-findings.md` | `reports/fix-author-report.md` | `done`: one commit 6e4669e, 5 files, all seven findings fixed, none contested; checks (foundation check, task-cycle 365, project-level 275, private-paths on 5 files, own-work check) all exit 0, each with its command; mechanical check: clean worktree, non-empty range, sections present. Next: review of the fix. |
| 2026-11-13 | review of the fix | reviewer resumed (sonnet), `review-change`: the fix of earlier findings | `reports/review-fix-handoff.md`; findings `reports/fix-findings.md`; range e51d835..6e4669e | `reports/review-fix-report.md` | `PASS 6e4669e`: seven findings fixed, no new finding; one Minor note outside the fix's reach: the rule "a step may give a command" in the request template is the author's reading and no decision states it (carried to the return step and to the request's judgment of unfixed findings). Checks each with exit 0. |
| 2026-11-13 | return step | author resumed (sonnet), `make-change` as the return step | `reports/return-step-handoff.md`; `task-cycle/skill/return_step.md` | `reports/return-step-author-report.md` | `done`: nothing needed correcting, no commit, working tree clean at 6e4669e; `foundation_check.py` exit 0; the command-in-a-step rule judged a choice of wording, not a decision (item 1 of *You accept by merging*). No commit, so no review of the return step. Report sections present. |
| 2026-11-13 | gate | orchestrator | `python -B task-cycle/gate_times.py --output .runs/task-cycles/friction-at-source/gate_times.md -- python -B gate/run_tests.py` on 6e4669e | `gate_times.md`, `.runs/gate-final.log` | exit 0, 1200 tests in 10 directories, 621.4 s. |
| 2026-11-13 | reconciliation | orchestrator | `git fetch origin`; `origin/foundations` equals the base 6814c6f | none | no merge needed; `review_reminder.py origin/foundations`: 29 merges, threshold 30, `reminder: no`. |
| 2026-11-13 | stages and measures | orchestrator | `task-cycle/cycle_stages.py` and `task-cycle/cycle_measures.py`, session of the orchestrator | `stages.md`, `mechanism_measures.md` | both exit 0. |
| 2026-11-13 | request | orchestrator | `task-cycle/skill/request_template.md` | `request.md` | form check exit 0, private-paths check exit 0 (1 run each before publishing); next: push, draft request, record copy. |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the cycle need the spec route for a change whose only open points are wording? Source: step 4, WAY-135 | No spec; one author | Task questions 2, 3, 4 answered with ways not chosen; settlements rows 1–4 accepted | Writing a spec for the wording | A wrong wording is fixed by the fix after the review, one round | route |
| Q3 | The author's report names material of its handoff left unread or read in part (invariants by title; six files of `project-level/task/skill/`; `remarks.md` in part). Source: step 4, "Where a report says that something its handoff names stayed unread" | Carried to the review of the whole change, which selects its own foundation and reads the diff; no resumption of the author | The six files the author did not read were searched by it for `line number`, `file:line`, `revision` only; the review reads the diff against the task, which names no part of them | Resuming the author to read them | A rule left in an unread file contradicts the new one: the reviewer's search or the return step finds it, one fix round | review |
| Q2 | Class of the one author. Source: step 4, WAY-229 | `same` (sonnet) | Change across five parts that writes entries binding later work | `cheaper` (haiku) | A weaker author's wording slip costs one fix round and its review | Author |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/friction-at-source/task.md` | orchestrator | — |
| Code commits | ffeadc7, 32f9904, e51d835 (the change); 6e4669e (fix of the Minor findings) | author | whole change `PASS e51d835`; fix `PASS 6e4669e` |
| Reports | `reports/author-report.md`, `reports/review-whole-change-report.md`, `reports/fix-author-report.md`, `reports/review-fix-report.md`, `reports/return-step-author-report.md` | author, reviewer | — |
| Handoffs and findings | `reports/author-handoff.md`, `reports/review-whole-change-handoff.md`, `reports/fix-handoff.md`, `reports/fix-findings.md`, `reports/review-fix-handoff.md`, `reports/return-step-handoff.md` | orchestrator | — |
| Request description | `request.md` | orchestrator | form check exit 0, private-paths check exit 0 |
| Stages, measures, gate times | `stages.md`, `mechanism_measures.md`, `gate_times.md` | scripts | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B task-cycle/gate_times.py --output ../task-cycles/friction-at-source/gate_times.md -- python -B gate/run_tests.py` (base) | orchestrator, 6814c6f, `.runs/base-check`, Windows, Python 3.14.3 | 0 — 1200 tests in 10 directories, every directory passed; 672.7 s in total (`gate_times.md`) | none: no check fails on the base |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/friction-at-source/gate_times.md -- python -B gate/run_tests.py` (final tree) | orchestrator, 6e4669e, the task worktree, Windows, Python 3.14.3 | 0 — 1200 tests in 10 directories, every directory passed; 621.4 s | none |
| `python -B elements/common/foundation_check.py` | author, reviewers, 6e4669e (and each of the first three commits by the reviewer, in copies outside the worktree) | 0, `0 errors` | none |
| `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py project-level` | author, fix author, reviewers | 0, 365 and 275 tests | none |
| `python -B task-cycle/private_paths_check.py <file>` on each changed file | author, fix author | 0 each | none |
| `python -B agent-instructions/skill_entry_points.py` | author, reviewer | 0, entry points current (the handoff named a flag `--check` that does not exist; the no-argument form checks) | none |
| `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/friction-at-source/stages.md <session>`; `python -B task-cycle/cycle_measures.py --output .runs/task-cycles/friction-at-source/mechanism_measures.md <session>` | orchestrator | 0 and 0 | none |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | `merges: 29`, `threshold: 30`, `reminder: no` | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/friction-at-source/request.md --task .runs/task-cycles/friction-at-source/task.md`; `python -B task-cycle/private_paths_check.py .runs/task-cycles/friction-at-source/request.md` | orchestrator | 0 and 0 (1 run each; the last runs after the record's link are added below) | none |

## Return step

- Foundation compared with code: the return step (author resumed, `reports/return-step-author-report.md`) compared WAY-327, WAY-353, WAY-354, the glossary word `transitional state`, the ten entries of the task's *Decisions in play* and the part map of the five touched parts with the files at 6e4669e (the fix included): nothing no longer matched; no correction, no commit
- Decisions written or changed: WAY-327 (changed in place, row 3), WAY-353 (row 1), WAY-354 (row 2), all by the foundation step with the code
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: `transitional state` (row 4), written by the foundation step; no term used against its entry
- Part-map changes: none (no file added or moved)
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — WAY-353; row 2 — WAY-354; row 3 — WAY-327; row 4 — glossary `transitional state`

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/108, draft until the record is committed and the description edited, then ready
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check last command `python -B task-cycle/request_check.py .runs/task-cycles/friction-at-source/request.md --task .runs/task-cycles/friction-at-source/task.md`, exit 0, 1 run; written and checked before the commit of the record's copy
- Writes to the task's backlog entry: pending
- Process remarks on the-way:
  - author, docs/task-cycles/friction-at-source/reports/author-report.md: `python -B agent-instructions/skill_entry_points.py --check`, named in the handoff, does not exist (error exit 2); the script takes `--write` or no argument (no argument checks). I used the no-argument form.
  - author, docs/task-cycles/friction-at-source/reports/author-report.md: The handoff names the next free number WAY-353; the log's last entry before the change was WAY-352 and no withdrawn number is 353 or 354 — confirmed.
  - author, docs/task-cycles/friction-at-source/reports/author-report.md: The task document's *Context* names WAY-329 as the reason a task outside a plan has no identifier an entry could name; WAY-329 derives only the identifier of a plan task's line, so WAY-354's Rationale says "an identifier that an entry could name exists only for a task of a project plan (WAY-329)" — a reading, not a quotation. A reviewer may want that sentence tightened.
  - author, docs/task-cycles/friction-at-source/reports/author-report.md: The task's row 1 says the rule covers "the template and the skill"; no single file of the skill is named, so I chose `draft.md` and `final_review.md` (choice 4).
  - fix of the Minor findings, docs/task-cycles/friction-at-source/reports/fix-author-report.md: None. (Finding 3's mention of WAY-297 and WAY-07 precedent is the reviewer's; I did not look it up, since the finding keeps the fix regardless.)
  - return step, docs/task-cycles/friction-at-source/reports/return-step-author-report.md: None. (The `git grep` for "four parts" found only `request_template.md` and the decision itself; the other hits, `audit_count.py` and `problem_register.md`, speak of another set of four.)
  - whole-change review, docs/task-cycles/friction-at-source/reports/review-whole-change-report.md: The handoff names `python -B agent-instructions/skill_entry_points.py --check`? It does not: the handoff names only the three focused checks. The author's report says its own handoff named `--check`, which does not exist. Nothing for me to do.
  - whole-change review, docs/task-cycles/friction-at-source/reports/review-whole-change-report.md: Which step of `foundation-review/SKILL.md` ends the review is unclear for a transitional-state decision where the human names a task (finding 1).
  - whole-change review, docs/task-cycles/friction-at-source/reports/review-whole-change-report.md: Where a step for a check by hand may name a command: not settled by WAY-286, WAY-327 or the template (finding 5).
  - whole-change review, docs/task-cycles/friction-at-source/reports/review-whole-change-report.md: No path to a data file of this review in a repository, so I could not check how a "task exists" answer is recorded beyond `proposals.md:55-60`.
