# Cycle record — the way: skill przeglądu fundamentu i niezałatanych uwag z PR-ów, z przypomnieniem po 30 scaleniach

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_sprawdzic_czy_29_decyzji_the_way_nadal_stoi_na_pra.md`, `Status: ready for cycle`, document updated 2026-11-07; frozen copy `frozen_task.md` beside this record
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way itself; no pin)
- Process pin: none — the-way itself, processes read from the worktree
- Target branch and base: `foundations`, `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6`
- Task branch: `task/foundation-review-skill` (worktree `C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill`)
- Status: request open

## Two questions at start

- Trust boundary: no — the files the change touches (`task-cycle/**`, `elements/**`, `foundations/**`, `agent-instructions/**`, `.claude/skills/**`, `.agents/skills/**`) have `Trust boundary: none` in the part map; none of them is named by it as taking in network data, keys, deployment or outside files. A script that counts merges would read the output of local `git`, which the part map's external context lists as trusted.
- Irreversible operation: no — the cycle writes a skill and text; the tag `foundation-review/…` is put by the skill when a human runs it later, not by the cycle. The cycle creates no tag and no account or server effect.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. The task settles: the skill (working name `review-foundation`), its inputs and outputs (To do 1, questions 1–15), the tag convention and the two git commands (*Context*), the threshold 30 and the place of the reminder (the request's description), the change of WAY-24, and settlement rows 1–7. What it leaves is how to make these — which part holds the skill's files, how the skill's text is split, how the reminder's count is computed and tested, the wording of the new decisions. Each is a way of making what the task settles, not a choice that binds later work differently: the part-map line for a file the change adds is no choice (step 4), and the reminder's computation is fixed by the two commands the task gives.
- Reserved choice: none — language, store, framework and place to run are not in question; Python and git are already settled for the-way.
- Execution route and reason: one author without a plan. The change is a new skill (a few markdown files), a few edits to existing task-cycle text and to WAY-24 with the decisions of rows 1–7, the entry points the generator writes, a part-map line and, if the author finds it needed, one small script with its test. It touches several parts but is text-bound and one agent can hold it. Class `same`: the change reaches many parts (task-cycle, decisions, elements, entry points) and the skill's text must stay faithful to a long source.
- Author: one author, `make-change`, class `same` as mine (Sonnet 5.5, the harness's default for a subagent); reason for a class other than `cheaper`: the change crosses many parts and has to take decisions of its own about a skill's shape. Resumptions: none yet.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` call; a background agent reports by completion notification and I yield the turn on it; no limit applied beyond the harness's
- Whole-change review: fresh reviewer (Sonnet 5.5, `review-change`), range `86cc21e..02ca017`, report `reports/review_whole.md`, first line `FAIL 02ca017`: 1 Important, 7 Minor, 0 out of scope; 62 files changed, +911/-79 (including 44 generated entry-point files). Covers every item of *To do* 1–3, the questions the change carries, *Settlements to record* 1–7 (row 1 tied to the changed WAY-24, rows 2–7 are WAY-300..WAY-305) and the *Decisions in play*; source fidelity judged sound, the one widening of a stated rule is the first-review start of WAY-304; nothing private in the added lines. After the fix, the same reviewer, `reports/review_fix.md`, range `02ca017..34a206f`: `PASS 34a206f`.
- Review rounds: one. Whole change: `FAIL 02ca017`, blocking finding Important 1 (the tag message counted "entries and remarks" in `foundation-review/SKILL.md` step 7 and "entries" in WAY-301), fix `34a206f` by the same author (range `02ca017..34a206f`), reviewed once by the same reviewer: `PASS 34a206f`. No blocking finding remained. Return step: no commit, so no review of it.
- Weakest-point checks: author — requirement "every place that restates WAY-24 says the review is the skill's run, not a backlog task" (To do 3): search of the repository for the old wording, a sample description with the reminder through `request_check.py` (exit 0), the real count against the two git commands by hand; showed no leftover (`reports/author_report.md`, own-work check). Author's fix — requirement "WAY-301 and every text that restates the tag message agree": the search after the fix found no "entries checked" / "entries and remarks" left (`reports/author_fix_report.md`). Return step — see *Return step* (`reports/return_step_report.md`).

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: the one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-07 00:30 | start | orchestrator (Sonnet 5.5) | task document read whole; `agent-instructions/README.md`; `task-cycle/skill/SKILL.md` | — | `git fetch`: checkout equal to `origin/foundations` `86cc21e`; no fast-forward needed |
| 2026-11-07 00:33 | base | orchestrator | worktree `.runs/worktrees/foundation-review-skill`, branch `task/foundation-review-skill` from `86cc21e`; separate checkout `.runs/base-foundation-review-skill` at `86cc21e` for the base gate | `base_gate.txt` | gate on the base started in the separate checkout, so no tracked file of the worktree is touched while it runs |
| 2026-11-07 00:45 | author | one author, `make-change` (whole change), class same, Sonnet 5.5 | `reports/handoff_author.md`; frozen task; `reports/selected_decisions.txt` | `reports/author_report.md` | dispatched in the background |
| 2026-11-07 01:10 | author return | one author | report | `reports/author_report.md` | `done with concerns`; commits 46ae3b9, 45d294f, dcf04d2, 0ef44b0, 02ca017; worktree clean, range non-empty; every check has command and exit code (the test-first run's exit is not recorded, the author says so); Searches and own-work check present. Concerns: skill unexercised; squash/rebase products would never get the reminder; README of agent-instructions says nothing of the reminder |
| 2026-11-07 01:15 | whole-change review | fresh reviewer, `review-change`, class same (Sonnet 5.5) | `reports/handoff_review_whole.md`; range 86cc21e..02ca017 | `reports/review_whole.md` | dispatched |
| 2026-11-07 01:25 | whole-change review return | reviewer | `reports/handoff_review_whole.md` | `reports/review_whole.md` | `FAIL 02ca017`: 1 Important (tag message: SKILL.md step 7 vs WAY-301, WAY-263), 7 Minor, 0 out of scope; fix goes to the author, resumed |
| 2026-11-07 01:35 | fix | author resumed (same agent), `make-change` fix, class same | `reports/findings_whole.md` | `reports/author_fix_report.md` | `done`; commit 34a206f (WAY-301, skill step 7 and `weak_points.md` say "the number of items checked"); foundation_check, entry points, agent-instructions and elements/common pass; Searches `none` |
| 2026-11-07 01:40 | fix review | same reviewer resumed, `review-change` fix | range 02ca017..34a206f; findings file | `reports/review_fix.md` | dispatched |
| 2026-11-07 01:45 | fix review return | same reviewer | range 02ca017..34a206f | `reports/review_fix.md` | `PASS 34a206f`; no blocking finding remains |
| 2026-11-07 01:50 | return step | author resumed | `reports/handoff_return_step.md`, `task-cycle/skill/return_step.md` | `reports/return_step_report.md` | dispatched. Order note: the orchestrator runs the product's gate (step 10) once on the final tree after the return step, instead of before and again after, since the return step may change the tree and a second 16-minute run would add nothing |
| 2026-11-07 02:05 | return step return | author resumed | `reports/handoff_return_step.md` | `reports/return_step_report.md` | `done`, no commit; two open points (WAY-140 and a review session; reminder reaches only cycles) |
| 2026-11-07 02:10 | gate | orchestrator | `python -B gate/run_tests.py` on `34a206f` | `final_gate.txt` | exit 0, 765 tests in 9 directories |
| 2026-11-07 02:35 | reconciliation | orchestrator | `git fetch`; `origin/foundations` is `86cc21e`, an ancestor of the head | — | nothing to merge, so no review of a merge |
| 2026-11-07 02:40 | request | orchestrator | `request.md`, `stages.md` | https://github.com/mariusznazar/the-way/pull/80 | draft opened; record copied to `docs/task-cycles/foundation-review-skill/`, committed and removed; request marked ready after the link by SHA |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the task leave an open design choice? Step 4 | No (see *Spec and execution route*) | `frozen_task.md`: *To do*, questions 1–15, *Settlements to record* 1–7 | writing a spec for the part, the wording and the counting script | a spec would cost a stage and a review for choices the author names anyway | route |
| Q2 | Human action 2 (`mapa_artykulow.md` L7 "nośnik" moved to the new decision's number) is placed *in the cycle* | Not done by the cycle; it is the human's, at the merge, and the request lists it with the new decision's number | `frozen_task.md`, *Human actions* | the cycle edits a file outside the repository | WAY-140: an effect outside the repository is a human's | request |
| Q3 | Where does the review keep its list of remarks, and how does it make a task? Task says "one data file" only. Author choice 6, 7 | The product's task area, `foundation_review_<date>.md`; a task is a backlog entry plus a document with `Status: refining`, or the text handed to the human where the agent cannot write | `reports/author_report.md` choices 6, 7 | data file inside the repository (may be public); a task written fully refined | one move of the file; another form of task | skill `proposals.md`, `with_the_human.md` |
| Q4 | Does pushing the tag need its own yes, and when is it put? Author choice 8 | Push only on the human's yes; no tag until the human decided every proposal and group | `reports/author_report.md` choice 8 | tag pushed by the skill without asking; tag put for a half review | one more question at the end | skill step 7, WAY-301 |
| Q5 | Which commit does the tag mark? Author choice 9 | The remote tip read at step 1, so the tag marks what was read | `reports/author_report.md` choice 9 | tip at the end of the session | merges that arrive during the session count to the next review, which is right | skill steps 1 and 7 |
| Q6 | Where does the skill live? Author choice 1 | New part `foundation-review` with directory `foundation-review/`; WAY-09 and the part map follow | `reports/author_report.md` choice 1 | `task-cycle/`, `elements/common/` | one rename of a directory and a part | part map, WAY-09, installer |
| Q7 | Count as script or text? Author choice 2 | Script `task-cycle/review_reminder.py` with a test | `reports/author_report.md` choice 2 | text only for the orchestrator | a prefix change must touch the script and the skill | step 13 |
| Q8 | Where does the reminder stand in the description? Author choice 3 | End of *How to merge* | `reports/author_report.md` choice 3 | *For you to decide*, *What you will see* | the human reads it elsewhere | request template |
| Q9 | Names and split. Author choices 4, 5 | Skill `review-foundation`, entry point `the-way-review-foundation`; `SKILL.md` plus four files read at their steps | `reports/author_report.md` choices 4, 5 | one file | none large | skill |
| Q10 | First review of a repository whose neighbour was reviewed. Question 14 gives a date for one product. Author choice 11 | "The human names the request to start after" (WAY-304), no date in the skill | `reports/author_report.md` choice 11 | a date in the skill (history) | the one widening of a stated rule, judged sound by the reviewer | WAY-304 |
| Q11 | WAY-24 row 1 as a seventh decision? Author choice 10 | Tied to WAY-24, no second entry | `reports/author_report.md` choice 10 | a separate entry | the request has to name both | foundation step |
| Q12 | Tag message content (review Important 1). Fix by the author | "the number of items checked and no title of a task or of a private note" in WAY-301 and every text restating it | `reports/author_fix_report.md`; task *Context* "liczbę sprawdzonych pozycji" | "entries and remarks", "of a person" | a tag message | WAY-301, skill step 7, `weak_points.md` |
| Q13 | The request's state for the task's *Human actions* item 2 (placed *in the cycle*): blocked draft, or ready? Step 12 and the variants table say a request waiting for a human action in the cycle stays a draft marked blocked | Ready. The action is to move a pointer in a file outside the repository once the number of the decision is known, which only happens at the merge; nothing the cycle needs waits for it, and it is listed in *For you to decide* | `frozen_task.md` *Human actions*: "Mariusz, przy scaleniu requestu, gdy numer jest znany" | blocked draft: it would wait on an action the human can do only at the merge | one click to mark the request draft | request |
| Q14 | Reports of the reviewers are named `review_whole.md`, `review_fix.md`, not `*report.md` | `remarks_check.py` reads `reports/*report.md`, so it skips them; their **Searches** items were copied into the process remarks by hand, and the check passes for the rest | `task-cycle/remarks_check.py` docstring | rename the files | an item of a reviewer not copied | process remarks |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `docs/task-cycles/foundation-review-skill/frozen_task.md` (source document updated 2026-11-07) | orchestrator | — |
| author report | `reports/author_report.md`, commits `46ae3b9`, `45d294f`, `dcf04d2`, `0ef44b0`, `02ca017` | author (Sonnet 5.5) | `FAIL 02ca017` (one Important) |
| whole-change review | `reports/review_whole.md`; findings file `reports/findings_whole.md` | reviewer | `FAIL`, then fixed |
| fix | `reports/author_fix_report.md`, commit `34a206f` | author resumed | `reports/review_fix.md`: `PASS 34a206f` |
| return step | `reports/return_step_report.md`, no commit | author resumed | not reviewed (no commit) |
| stages | `stages.md` | `cycle_stages.py` | — |
| handoffs | `reports/handoff_author.md`, `handoff_review_whole.md`, `handoff_return_step.md` | orchestrator | — |
| gate on the base, gate on the final tree | `base_gate.txt`, `final_gate.txt` | orchestrator | exit 0, exit 0 |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the base, in `.runs/base-foundation-review-skill` | orchestrator, `86cc21e`, Windows 11, Python 3.14 | exit 0; 756 tests in 9 directories, every directory passed | none: no check failed on the base |
| `python -B gate/run_tests.py` on the final tree | orchestrator, `34a206f` (target `86cc21e` is its ancestor, nothing to reconcile), Windows 11, Python 3.14 | exit 0; 765 tests in 9 directories, every directory passed (9 new, in `task-cycle`) | none |
| `python -B gate/run_tests.py installation`, first run of the author | author, `0ef44b0`+ | exit 1; 3 failures, stale expected count of entry points (40, now 42) | fixed in `02ca017`; second run exit 0, 44 tests; the final gate passes it |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator, `34a206f` | exit 0; `tag: foundation-review/2026-11-06`, `merges: 1`, `threshold: 30`, `reminder: no` | none; no reminder in this request |
| `python -B task-cycle/cycle_stages.py 9857b0fd-30ff-4c03-b364-adc89a8451eb --output docs/task-cycles/foundation-review-skill/stages.md` | orchestrator | exit 0; no warnings | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/foundation-review-skill` | orchestrator | exit 1 on the first run (11 items listed, copied into the process remarks), exit 0 on the second and every later one; reports named `review_*.md` are not read by the script, their items were added by hand | none |

## Return step

Author resumed, `reports/return_step_report.md`, status `done`, no commit (head stays `34a206f`).

- Foundation compared with code: WAY-24, WAY-09, WAY-82, WAY-300 to WAY-305, the facts template sentence, the task's *Decisions in play*, WAY-286 and WAY-287, and the part-map entries of `foundation-review`, `task-cycle`, `installation`, `decisions`, `part-map`, `environment-facts`, `agent-instructions` against the files at `34a206f`: all match, nothing corrected.
- Decisions written or changed: WAY-300 to WAY-305 written; WAY-24, WAY-09 and WAY-82 changed (foundation step, `45d294f`; WAY-301 and the texts that restate it reworded in `34a206f`)
- Invariants written or changed: none — no row or decision of the task sets a rule a commit could make false
- Environment facts: none — no decision of the change cites an outside source in *Based on*
- Glossary terms: none
- Part-map changes: new part `foundation-review`; `installation` gains it in *Depends on* (`45d294f`)
- Projected entries written whole or in part: none (the task is independent)
- Rows of *Settlements to record* written: row 1 tied to WAY-24 (no second entry); row 2 WAY-300; row 3 WAY-301; row 4 WAY-302; row 5 WAY-303; row 6 WAY-304; row 7 WAY-305

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/80, draft at opening; marked ready after the record's commit is linked
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check: last run exit 0 (`form holds`), 3 runs
- Writes to the task's backlog entry: request link `[url::https://github.com/mariusznazar/the-way/pull/80]` added to the task's line in `_tasks_active.md`; state left at Ready, [/]
- Process remarks on the-way:
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The task does not say where the data file of a review lives or what it is called; I chose the product's task area and `foundation_review_<date>.md` (choice 6).
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The task does not say how the skill creates a task in a backlog the agent may not write to, nor in what form; I chose the entry plus a `Status: refining` document, or the text for the human (choice 7).
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The task does not say whether pushing the tag needs its own yes, nor when the skill puts the tag if the human stops halfway; I chose a yes for the push and no tag until every decision is made (choice 8).
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The count by `git rev-list --merges --first-parent` reads 0 for a product whose merges are squashed or rebased (no merge commit); the task's *Context* fixes the two commands, and the request template already notes this limitation for the merge. The skill tells such a product's review to read the host's list of merged requests, but the reminder in that product would never fire. Unclear whether any product squashes; this is a gap in the task, not filled.
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The agent-instructions README (`agent-instructions/README.md`), which tells the agent leading a change to the-way before `main` how to write the description, says nothing of the reminder, and WAY-300 binds the orchestrator of a cycle only; so a change to the-way made without a cycle gets no reminder. I did not widen WAY-300 or the README beyond the row's words.
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: Row 5 of the task says the review raises a remark the request asked about "when no answer is written"; I could not tell from the task how a *comment of the human* that answers by silence (a thumbs-up, a merge) counts. The skill says the merge is no answer and a written decision is.
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The skill has not been run on a repository: its form (data file columns, the order of the human contact) follows the task's text and the two private files read for form only. A first real run will probably find steps to tighten.
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: The decision number for the human's action 2 (the "nośnik" of row L7 in `mapa_artykulow.md`): the decision that carries the reminder is **WAY-300**; the decision that carries the tag is WAY-301.
  - author (make-change, whole change), `docs/task-cycles/foundation-review-skill/reports/author_report.md`: `elements/common/migrate_foundation.py:436` still says "the task of the periodic review of the foundation" in a message of the old-form migration; I left it (see the foundation search above).
  - whole-change review (review-change), `docs/task-cycles/foundation-review-skill/reports/review_whole.md`: Not found: a rule saying whether a tag message may count remarks, or only entries (Important 1): the task says "pozycji" and no decision settles it beyond WAY-301's own "entries".
  - whole-change review (review-change), `docs/task-cycles/foundation-review-skill/reports/review_whole.md`: Not found: any text in the-way that defines "the daily scan" (Minor 4).
  - whole-change review (review-change), `docs/task-cycles/foundation-review-skill/reports/review_whole.md`: Unclear: whether question 14's first-review rule (given for one product, by date) was meant to be general; the change generalises it as "after the request the human names" (WAY-304). I read it as sound but it is the one widening of a stated rule.
  - whole-change review (review-change), `docs/task-cycles/foundation-review-skill/reports/review_whole.md`: Unclear: whether the task wanted the reminder in changes to the-way made without a cycle (Declined to judge).
  - whole-change review (review-change), `docs/task-cycles/foundation-review-skill/reports/review_whole.md`: Not found: the author's sample description for `request_check.py`; I did not re-run that check.
  - return step (author resumed), `docs/task-cycles/foundation-review-skill/reports/return_step_report.md`: Whether WAY-140 reaches the agent's writes of backlog tasks and the data file in a review session (outside the repository): I read it as binding a task's cycle, so I found no collision, but the decision does not say that a session with the human is outside it.
  - return step (author resumed), `docs/task-cycles/foundation-review-skill/reports/return_step_report.md`: The reminder reaches only requests written by a task cycle's orchestrator (WAY-300); the before-`main` guide for changes to the-way (`agent-instructions/README.md`) is silent on it. Same gap as in my first report; not corrected, since the row binds the cycle.
