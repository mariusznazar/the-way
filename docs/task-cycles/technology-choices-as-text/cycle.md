# Cycle record — the way: technology choices reach the human as text, one choice after another

- Task source: the task's note in the author's backlog, `Status: ready for cycle`, last updated 2026-11-07 (settlements accepted 2026-11-07); frozen copy `docs/task-cycles/technology-choices-as-text/task_frozen.md`
- Task relation: independent
- Product repository: the-way (the session works in the-way itself)
- Process pin: none — the-way is the repository changed
- Target branch and base: `foundations`, `a3206c17932cac9bc6ac33ecfe026a2a50fbe9d5` (equal to `origin/foundations` after fetch; no fast-forward needed)
- Task branch: `task/technology-choices-as-text`, worktree `.runs/worktrees/technology-choices-as-text`, created with `--no-track`
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits markdown of `project-level/**` and `foundations/decisions.md`; none of the three trust-boundary files of `project-level` (`readiness_check.py`, `plan_check.py`, `plan_state.py`) is touched.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — Questions 1–3 of the task are answered with the human's source and *Not chosen*; settlements 1–3 settle the entries (WAY-123 changed in place, the check wording in `settle.md`, the `— held by` sentence in `task_run.md`). What remains is how to word the replaced sentences, and the task gives that word for word for points 1, 2 and 5.
- Reserved choice: none — no language, framework, library, store, login or place to run is chosen.
- Execution route and reason: one author without a plan. About a dozen files of two parts, all prose; one agent holds it. No slice-size script run (step 4).
- Author: one author, class `same` as the orchestrator (Sonnet 5.5), model `sonnet`. Reason for not `cheaper`: point 3 changes the sense of an accepted decision and point 4 asks per-site judgments (WAY-137's "table of consequences", WAY-268's "a table for the human", plain tables to leave alone) where a wrong swap in either direction changes meaning.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: harness completion notification (background agent); the turn is yielded while only that result remains; no polling, no limit hit so far
- Whole-change review: fresh reviewer (Sonnet, `same` class), `review-change`; range `a3206c1..78c32c7`, 9 files +94/-57; first line `PASS 78c32c7f02e6b6b3148913441a0a3ad58d038a03`, report `reports/review_whole_report.md`; covers every point of *To do*, questions 1–3 and rows 1–3 and the source fidelity (its section "Against the task"); 0 blocking, 4 Minor within the task
- Review rounds: no blocking finding in the whole-change review. Fix for its 4 Minor findings within the task: range `78c32c7..f809953`, report `reports/fix_report.md`; review of the fix by the same reviewer, `reports/review_fix_report.md`, `PASS f8099532ddc5323b9cfd6dd0287414485ee452be`; the fix was not reverted. One new Minor from the review of the fix goes to the request's list
- Weakest-point checks: author: point 4 of the task (every site where "table" names what the human receives is changed and no ordinary table is); check: `git grep`/search of "table" and "tables" in `project-level/` and `foundations/`, every remaining hit read; showed: all remaining hits are ordinary tables; it also caught a draft error before the commit (a first draft of WAY-123 said the checking agent "sees only the message" while the step gives it the document too); report `reports/author_report.md`. Fix author: "the diff holds only the change", especially the WAY-165 clause; check: byte-and-character scan of every added line against the base and a read of the diff; showed: five over-long lines, fixed; report `reports/fix_report.md`. Return step: an entry or file still stating the old rule; check: `git grep` over every tracked file and a read of each decision citing WAY-123 or WAY-165; showed: nothing stale; report `reports/return_step_report.md`

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

One-author route: no slices.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-08 | Start | orchestrator, Sonnet 5.5 | `/the-way-implement-task` on the task document | worktree + branch created at `a3206c1` | Gate on the base started in the background (`gate_base.log`); no tracked file changes until it ended |
| 2026-11-08 | Author | one author, `same` class, Sonnet (`sonnet`), `Agent` call that the harness ran in the background; the result arrives as a completion notification | `reports/author_handoff.md`; method `task-cycle/change/SKILL.md`, variant "the whole change as the one author"; frozen task | `reports/author_report.md` | Base gate passed (exit 0, 804 tests); author dispatched |
| 2026-11-08 | Author returned | one author, Sonnet | `reports/author_handoff.md` | `reports/author_report.md`; commit `78c32c7` (9 files, +94/-57) | `done with concerns`. Mechanical check: worktree clean, range non-empty, files match the task (plus WAY-166, found by the author's own search and judged by it), searches section and own-work check present. One check row (verbatim text, "python one-off") has no command or exit code: report returned for repair (WAY-159). Author's questions answered from the task: row 2's "sees only the first message" is the cost the task names in question 1, so no addition to `settle.md`; candidate tables of `find-foundation-entries` stay tables (the task leaves ordinary tables alone) |
| 2026-11-08 | Author repair | one author (resumed) | message with the repair request | `reports/author_report.md` row 31 | Verbatim check now has command and exit code 0 (4 of 4 found); no new commit, worktree clean |
| 2026-11-08 | Whole-change review | fresh reviewer, Sonnet (class `same`, not cheaper than the orchestrator) | `reports/review_whole_handoff.md`; method `task-cycle/review/SKILL.md`; range `a3206c1..78c32c7`; frozen task; author report | `reports/review_whole_report.md` | `PASS 78c32c7f02e6b6b3148913441a0a3ad58d038a03`: 0 blocking, 4 Minor within the task, 0 outside; 9 files +94/-57. Minor findings go to one fix and one review of it (WAY-161, WAY-162) |
| 2026-11-08 | Fix of the Minor findings | one author (resumed), `same` class | `reports/findings_minor.md` (reviewer's words, cut from `reports/review_whole_report.md`); method `task-cycle/change/SKILL.md`, variant "the fix of a review's findings"; range runs from reviewed head `78c32c7` | `reports/fix_report.md` | `done`; commit `f809953` (4 files, +39/-39); worktree clean. Its Checks row "width of added lines" had no concrete command: returned for repair once, repaired (`width_check.py`, exit 0) |
| 2026-11-08 | Review of the fix | same reviewer, resumed (`review-change`) | range `78c32c7..f809953`; `reports/findings_minor.md`; `reports/fix_report.md` | `reports/review_fix_report.md` | `PASS f8099532ddc5323b9cfd6dd0287414485ee452be`: all four fixed, no new Critical or Important. One new Minor (to the request's list): the fix report says no added line exceeds 100 bytes, but 11 added lines are 102–105 bytes (100 characters or fewer; em dashes are 3 bytes) |
| 2026-11-08 | Target branch | orchestrator | `git fetch`; `origin/foundations` = `a3206c1`, 0 commits ahead of the base | — | Nothing to merge; the final tree is `f809953`. Gate started on it |
| 2026-11-08 | Gate | orchestrator | `python -B gate/run_tests.py` on `f809953`, log `gate_final.log` | exit 0 | 804 tests in 9 directories, every directory passed (5m53s); next: return step |
| 2026-11-08 | Return step | one author (resumed), `same` class | `task-cycle/skill/return_step.md` (and `foundation_step.md` it names); all entries the change writes or changes, the task's, the search's, the part map | `reports/return_step_report.md` | `done`, no commit: nothing compared no longer matched the code; tree stays `f809953`, worktree clean. No review of the return step, since it committed nothing |
| 2026-11-08 | Process remarks check | orchestrator | `python -B task-cycle/remarks_check.py .runs/task-cycles/technology-choices-as-text` | first run: `checked: 0 reports` (exit 0, nothing read: the script reads only `reports/*report.md`); after the rename: exit 1, 10 items not in the remarks; after the 10 entries were appended word for word: exit 0, `checked: 5 reports, 10 items other than none, 0 not in the process remarks` | 3 runs on the original; the cleaned copy is checked at the record step |
| 2026-11-08 | Stages | orchestrator | `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/technology-choices-as-text/stages.md 898273ba-05af-49cb-8238-eb7d8954c8bd` | `stages.md`: 15 stages, 0:30:09, 23,238,144 tokens, all `claude-sonnet-5-5` | exit 0 |
| 2026-11-08 | Reminder count | orchestrator | `python -B task-cycle/review_reminder.py origin/foundations` | `tag: foundation-review/2026-11-06`, `merges: 9`, `threshold: 30`, `reminder: no` | nothing added to *How to merge* |
| 2026-11-08 | Request | orchestrator | `request.md` written by `task-cycle/skill/request_template.md`; form check exit 0; private paths check exit 0; branch pushed | draft pull request https://github.com/mariusznazar/the-way/pull/87 | opened as a draft; marked ready after the record's link and the checks of the copy are added |
| 2026-11-08 | Correction of report paths | orchestrator | `task-cycle/remarks_check.py` reads only `reports/*report.md` and listed `0 reports` on the first run | the five stage reports renamed to `author_report.md`, `fix_report.md`, `return_step_report.md`, `review_whole_report.md`, `review_fix_report.md` | The handoffs and `findings_minor.md` still name the earlier paths (`author.md` and so on); the reports were written there and renamed afterwards. Rows above name the new paths |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| C1 | Line numbers of the task's points 3–4 are "@ 52889bc"; do they still hold? | `project-level/**` files unchanged since 52889bc (`git diff --stat 52889bc..HEAD` over them is empty); `foundations/decisions.md` grew by 349 lines, so its numbers moved (WAY-123 now at `:2901`). The author locates decision sites by heading, not by the task's numbers. | `git diff --stat`, `grep -n` at start | Trusting the task's numbers for `decisions.md` | Edit of the wrong passage | author handoff |
| C3 | Author's Q2: should `settle.md` tell the checking agent it sees only the first message? | No. Row 2 and question 1 say the check covers the first message and that jargon in later follow-ups stays; that is a cost, not an instruction to the agent. | `reports/author_report.md` questions 2–3; task question 1 *Answer* | Adding the sentence to `settle.md` | A rule the task did not settle enters the step | author |
| C4 | Author's Q3: candidate tables of `find-foundation-entries` | Stay tables: they are real tables in another step, and the task says to leave ordinary tables alone | `reports/author_report.md` "Ambiguous sites" | Changing them to "message" | Wrong meaning in an unrelated step | author |
| C2 | Author class | `same` (see Author) | — | `cheaper` (the default) | Wrong swap in an accepted decision, caught only at review | author |
| C5 | Where does row 2 (the fresh agent's check of the first message) live: WAY-120 or WAY-123? | WAY-123: it already narrows WAY-114 for this area and `settle.md` cites it for the showing | `reports/author_report.md`, "Row-to-entry ties"; reviewer agreed, `reports/review_whole_report.md` | WAY-120 (the general rule of critique of collectively reviewed sets) | A reader looking for the critique rules does not find the check there; a later move is one edit | author |
| C6 | Where does row 3 (the `— held by` sentence) live: WAY-165 or WAY-267? | WAY-165: its *Verification* already says the item stays held in a run at a task | `reports/author_report.md`; reviewer: "a defensible home" | WAY-267 | One sentence would move to the neighbouring entry | author |
| C7 | WAY-137 "the table of consequences" and WAY-166 (not on the task's list): what the human receives, or a comparison in a report? | Both read as what the human receives; reworded to "message". Nothing in `project-level/technology/` calls the report's comparison a table | `reports/author_report.md`, "Ambiguous sites"; reviewer agreed | Leave them as tables | Two violates examples keep a rejected form | author |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| Frozen task | `.runs/task-cycles/technology-choices-as-text/task_frozen.md` | orchestrator | — |
| Code and foundation entries | commit `78c32c7` (9 files, +94/-57) | one author | `PASS 78c32c7f02e6b6b3148913441a0a3ad58d038a03`, `reports/review_whole_report.md` |
| Fix for the Minor findings | commit `f809953` (4 files, +39/-39) | one author | `PASS f8099532ddc5323b9cfd6dd0287414485ee452be`, `reports/review_fix_report.md` |
| Reports and handoffs | `reports/author_handoff.md`, `reports/author_report.md`, `reports/review_whole_handoff.md`, `reports/review_whole_report.md`, `reports/findings_minor.md`, `reports/fix_report.md`, `reports/review_fix_report.md`, `reports/return_step_report.md` | agents and orchestrator | as above |
| Request | https://github.com/mariusznazar/the-way/pull/87, `request.md` | orchestrator | form check exit 0 |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the base | orchestrator, `a3206c1`, the task worktree, before any change | exit 0; 804 tests in 9 directories, every directory passed (5m37s); log `gate_base.log` | none failing on the base |
| `python -B gate/run_tests.py` on the final tree | orchestrator, `f809953`, the task worktree | exit 0; 804 tests in 9 directories, every directory passed (5m53s); log `gate_final.log` | none failed, none unrun |
| `python -B elements/common/foundation_check.py` | author, reviewers, author again (fix, return step), worktree at `78c32c7` and `f809953` | exit 0, "0 errors" in every run | none |
| `python -B gate/run_tests.py project-level` | author, whole-change reviewer | exit 0, 271 tests | none |
| `python -B gate/run_tests.py elements/common` | author (first run, with two other test runs at once), then alone, whole-change reviewer, fix author | first run exit 1 (2 tests of `test_foundation_check.py` failed); the next four runs exit 0, 109 tests | cause of the one failure not verified; the author's guess is contention on temporary git repositories. 1 failing run, 4 passing runs after it, plus the gate on the final tree |
| `python -B gate/run_tests.py installation` | author (a run across its own commit), then `python -B -m unittest discover -s installation -p "test_styleguide_installation.py"`; fix author | first run exit 1 (one test compares the pinned commit with the HEAD it found at start, and the author committed during the run); the file alone exit 0 (2 tests); the directory in the fix author's run exit 0 (44 tests) | the failure was caused by the commit during the run; 1 failing run, 3 passing runs after it |
| verbatim comparison of the task's sentences of points 1, 2 and 5 | author, scratchpad script `verbatim_check.py` run as `python -B -I <scratchpad>/verbatim_check.py` | exit 0, found 4 of 4 | none |
| width scan of added lines, `width_check.py` | fix author and whole-change reviewer | exit 0, 97 added lines, 0 over 100 characters (11 over 100 bytes, em dashes counted three bytes each) | the fix report's claim of 100 bytes is wrong (Minor, in the request) |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | exit 0; `tag: foundation-review/2026-11-06`, `merges: 9`, `threshold: 30`, `reminder: no` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/technology-choices-as-text` on the original | orchestrator | 3 runs: exit 0 with `0 reports` (no report read, invalid), exit 1 (10 items), exit 0 (`checked: 5 reports, 10 items other than none, 0 not in the process remarks`) | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/technology-choices-as-text/request.md --task .runs/task-cycles/technology-choices-as-text/task_frozen.md` | orchestrator | exit 0, 1 run before the pull request opened | none |
| `python -B task-cycle/private_paths_check.py .runs/task-cycles/technology-choices-as-text/request.md` | orchestrator | exit 0, `checked: 1 files, 0 listed`, 1 run | none |

## Return step

- Foundation compared with code: nothing no longer matched. Compared with the repository's files: WAY-123, WAY-165, WAY-137, WAY-138, WAY-166, WAY-267, WAY-268 against `settle.md`, `task_run.md`, `start.md`, `list.md`, `definition_template.md`, `orchestrated_mode.md` and `lead/skill/SKILL.md`; WAY-113, WAY-114 and WAY-120 named by the task; the decisions that cite WAY-123 for the new-tools routes (they name no table); the part-map entries of `project-level` and `decisions` (no file, part or dependency moved). One wording difference left on purpose: the project definition template says "a fresh agent has checked that message", WAY-123 says "in the first message, before it is shown"
- Decisions written or changed: WAY-123 and WAY-165 (rows 1 to 3, in `78c32c7` and `f809953`); one-word changes in WAY-137, WAY-138, WAY-166, WAY-267, WAY-268. The return step writes none
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none (the task is independent and has no project definition)
- Rows of *Settlements to record* written: row 1 — WAY-123; row 2 — WAY-123; row 3 — WAY-165
- Review of the return step: none; it committed nothing

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/87, draft; marked ready for review after the record's link and the checks of the copy are added
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/technology-choices-as-text/request.md --task .runs/task-cycles/technology-choices-as-text/task_frozen.md`, last exit 0, 1 run; check of private paths `python -B task-cycle/private_paths_check.py .runs/task-cycles/technology-choices-as-text/request.md`, last exit 0, 1 run; the description is edited once more after this record's copy is committed (the record's link and the checks of the copy), and both checks are run again on that edit: written and checked after this commit
- Writes to the task's backlog entry: the request link `https://github.com/mariusznazar/the-way/pull/87` as `[url::...]`, and the state set from Ready `[/]` to Selected `[>]` with the date 2026-11-08, as the two neighbouring tasks in progress stand
- Process remarks on the-way:
  - Author, docs/task-cycles/technology-choices-as-text/reports/author_report.md: Task point 4 lists line numbers "@ 52889bc" for `decisions.md`; they have moved (orchestrator finding C1). I found every site by heading and quoted words. All sites the task names were found; WAY-137's task-line (`:3547`) is the "table of consequences" violates example, now at `3573` — found, but only after checking the headings.
  - Author, docs/task-cycles/technology-choices-as-text/reports/author_report.md: The task's point 3 cites `"in separate tables"` at `:2897-2898` and `"the tables come one choice at a time"` at `:2912`; both were found in WAY-123 (now `2922-2923`, `2937`).
  - Author, docs/task-cycles/technology-choices-as-text/reports/author_report.md: The task's point 2 phrase "what one choice of the table contradicts in another" was found at `settle.md:45-46` but the point 4 list also tells to change the word "table" on `settle.md:46`; unclear which should win in that exact phrase, see the weakest point 3.
  - Author, docs/task-cycles/technology-choices-as-text/reports/author_report.md: The row 2 of *Settlements to record* says the check "sees only the first message"; unclear whether that means "the agent gets only the message as first shown" or "the agent receives nothing but the message". `settle.md` as the task gives it also gives the document, so I took the first meaning; see the weakest point 2.
  - Author, docs/task-cycles/technology-choices-as-text/reports/author_report.md: Row 1 says "the table with a plain paragraph beneath" and "leave as is" are rejected ways; the *Not chosen* of question 1 gives the first as "tabela z akapitem prostym językiem pod spodem" and the third as "zostawić jak jest"; I used both. No separate source keeps "the rejected table" apart from "leave as is", so the *Rejected* gives it once ("the options in one table as before").
  - Author, docs/task-cycles/technology-choices-as-text/reports/author_report.md: `foundation_check.py --help` does not exist as a flag (it ran with an error message about the working directory on that call); the script takes only the root directory. Not a finding about the work.
  - Whole-change review, docs/task-cycles/technology-choices-as-text/reports/review_whole_report.md: Task point 4 gives line numbers of `decisions.md` at 52889bc; at base `a3206c1` they have moved (the author also says so). I found every site by heading and quoted words; nothing was missing.
  - Whole-change review, docs/task-cycles/technology-choices-as-text/reports/review_whole_report.md: "Row 2: the check sees only the first message": unclear whether that means the first of the messages or the agent receiving nothing but the message. The author took the first meaning; `settle.md` gives the same agent the document too, so the first reading fits. Finding 1 is about the resulting wording.
  - Whole-change review, docs/task-cycles/technology-choices-as-text/reports/review_whole_report.md: No place found where the task says why the lines of the options left out stay (finding 2). It is a thing the task states, but without a reason.
  - Whole-change review, docs/task-cycles/technology-choices-as-text/reports/review_whole_report.md: Invariants and the part map for `project-level` were not searched for a rule on the form of the showing; I judged the change against the decisions, which hold the matter, and found none.
  - the orchestrator: `task-cycle/remarks_check.py` reads only the files `reports/*report.md`, but neither `task-cycle/skill/SKILL.md` nor `task-cycle/record_template.md` tells the orchestrator to name the reports so (the template says only "in `reports/`"). The first run listed `checked: 0 reports, 0 items other than none` with seven reports present and exit 0, which reads as a clean check; the reports were named `author.md`, `fix.md` and so on and had to be renamed to `author_report.md` and the like after the first run.
