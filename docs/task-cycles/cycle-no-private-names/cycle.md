# Cycle record — the way: cykl zadania nie publikuje prywatnych nazw w publicznej historii

- Task source: the task document in the author's private notes (not published), `Status: ready for cycle`, copied 2026-11-07 to `task.md` beside this record; its citations stand at `foundations` `52889bc`
- Task relation: independent
- Product repository: `the-way` (the-way working on itself, under `agent-instructions/README.md`)
- Process pin: none — the process root is this worktree
- Target branch and base: `foundations`, `ad44b84` (`origin/foundations`, the local branch stood at the same commit)
- Task branch: `task/cycle-no-private-names`, worktree `.runs/worktrees/cycle-no-private-names`
- Status: blocked

## Two questions at start

- Trust boundary: no — the change touches `task-cycle/**` (part map: trust boundary none), `foundations/decisions.md` and possibly the instruction files of the cycle; no file of it takes in data from the network, keys, the deployment or files from outside. The script it adds reads the cycle's own record copy.
- Irreversible operation: no — the change makes a script, rules and a decision; it publishes nothing and deletes nothing.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none. Rows 1 and 2 of *Settlements to record* and the answers to questions 1–5 settle what the cycle does (clean the copy to relative paths and descriptions, a script that lists absolute paths and `[[...]]` links by pattern, run on the copy before each commit that adds the record and on the description before each publication, no check of commit messages, no list of private words). What stays to the author is how to make it: the script's name, call and exit codes, its patterns, the places of the rules. *Questions carried to cycle* (the order of the cleaning and the remarks check) is no design choice: the orchestrator rules on it in the handoff (Q1 below).
- Reserved choice: none. A Python script beside the existing ones of `task-cycle/`; no new language, library, store, login or place to run.
- Execution route and reason: one author without a plan. The change is one script with its test, the same step added to the places of the cycle that already run `remarks_check.py`, two small edits to the record and request templates and one or two decisions: about six files of two parts, `task-cycle` and `decisions`, whose rules bind one another, so one agent holding them together keeps them consistent; nothing in the task calls for division. Trust boundary and irreversible operation stay no.
- Author: fresh agent, class `same` (claude-sonnet-5-5, the orchestrator's own model), for its code, foundation entries and return step. Class `same` rather than the default `cheaper`: the change writes a decision into a log of 300 entries, edits the step list of the cycle's main skill in five places that must agree, and the rules it adds apply to the cycle's own record.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code `Agent` tool; completion notification of the background agent, no polling
- Whole-change review: fresh reviewer other than the author, by `review-change`, claude-sonnet-5-5; range `ad44b84..b6d93e8` (commits `c8fe9f6`, `4643660`, `b6d93e8`); `FAIL b6d93e8`, `reports/whole-review-report.md`; 10 files, 620 added and 41 removed lines (`git diff --numstat`); coverage of every To do, settlement row and carried question under *Coverage of the task* in the report; source fidelity judged against the frozen task; no plan, no projected entry carried
- Review rounds: whole change, `reports/whole-review-report.md`: one Important finding (a cleaned committed copy of a plan item's record cannot be anchored by the plan-state reader, while WAY-308 says it can) and seven Minor within the task; fix `b6d93e8..4deb195` (`d745246`, `4deb195`), `reports/fix-report.md`, all eight addressed; review of the fix, `reports/whole-review-2-report.md`, `FAIL 4deb195`: the eight fixed, one new Important finding N1 in the fix diff (the rule for a listed `Task relation:`/`Project relation:` line has the cycle commit and push the copy with the listed path, against WAY-308 and WAY-309; it comes from the orchestrator's ruling Q3) and three new Minor (N2–N4). N1 counts as a blocking finding that remains: no third round, no ruling on it, the request opens blocked (`task-cycle/skill/blocked_finding.md`)
- Weakest-point checks: one author, `reports/author-report.md` (own-work check): a script that must not list a URL or prose while it lists the drive, home and POSIX-drive forms, and the Q1 order working with the real `remarks_check.py`; checked by running the script over the tracked text of the repository and over the frozen task, and the whole sequence on a made-up record outside the repository (exit codes 0, 0, 0 on the cleaned copy, 1 on the uncleaned original); named as the weakest point the interaction with the plan-state reader, which the review then confirmed with a fixture. Fix, `reports/fix-report.md`: see its own-work check

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-07 13:50 | start | orchestrator, claude-sonnet-5-5 | `implement-task`; task document | worktree at `ad44b84`, `task.md` | `origin/foundations` fetched, local branch level with it; branch `task/cycle-no-private-names` created with no upstream |
| 2026-11-07 13:55 | base checks | orchestrator | `python -B gate/run_tests.py` on `ad44b84`, in a separate checkout of the base under `.runs/base-check-cycle-no-private-names` (first start died with its shell, started again) | `base-gate.log`, `base-gate.exit`, `base-gate.head` | exit 0, 765 tests in 9 directories, every directory passed: no check fails on the base |
| 2026-11-07 14:05 | one author | fresh author, claude-sonnet-5-5 (class `same`) | `reports/author-handoff.md`, `task-cycle/change/SKILL.md`, variant "the whole change as the one author" | `reports/author-report.md`, commits `c8fe9f6`, `4643660`, `b6d93e8` | `done with concerns`: Task source concern (Q2 below); focused checks each exit 0 with command; WAY-308 and WAY-309 written; mechanical check passed (clean worktree, non-empty range, 10 files in `task-cycle`, `agent-instructions`, `foundations`, each check with command and exit code, Searches section and own-work check present) |
| 2026-11-07 14:25 | whole-change review | fresh reviewer, claude-sonnet-5-5 | `reports/whole-review-handoff.md`, `task-cycle/review/SKILL.md`, range `ad44b84..b6d93e8` | `reports/whole-review-report.md` | dispatched in the background |
| 2026-11-07 14:50 | whole-change review result | reviewer | `reports/whole-review-report.md` | range `ad44b84..b6d93e8` | `FAIL b6d93e8`: 1 blocking (Important: cleaned copy of a plan item's record cannot be anchored by `plan_state.py`; WAY-308 says it can), 7 Minor within the task, 0 outside; 10 files, 620 added, 41 removed |
| 2026-11-07 14:55 | fix | the one author, resumed, claude-sonnet-5-5 | `reports/fix-handoff.md`, `reports/whole-review-findings.md`, `task-cycle/change/SKILL.md`, variant "the fix of a review's findings" | `reports/fix-report.md`, commits `d745246`, `4deb195` | `done`: all eight findings addressed; `task-cycle` 187, `project-level` 271, `agent-instructions` 18 tests each exit 0, foundation check exit 0; mechanical check passed (clean worktree, non-empty range, 8 files, each check with command and exit code); one deviation from the ruling: a listed `Task relation:`/`Project relation:` line goes to the request as the existing plain `draft` row, not `blocked` |
| 2026-11-07 15:10 | review of the fix | the whole-change reviewer, resumed | message naming the range `b6d93e8..4deb195`, `task-cycle/review/fix.md`, `reports/fix-report.md` | `reports/whole-review-2-report.md` | `FAIL 4deb195`: the eight findings fixed; one new Important finding N1 in the fix diff (rule for a listed relation line commits and pushes the listed path), three new Minor (N2–N4), 0 outside the scope; 7 files, 162 added, 53 removed |
| 2026-11-07 15:40 | blocked | orchestrator | `task-cycle/skill/blocked_finding.md` | this record | N1 counts as a blocking finding that remains: no third round, no ruling on it, no return step, no reconciliation with the target branch; gate on the change, stages, record copy, then a blocked draft request |
| 2026-11-07 15:41 | gate on the change | orchestrator | `python -B gate/run_tests.py` on `4deb195` | `change-gate.log`, `change-gate.exit`, `change-gate.head` | exit 0, 804 tests in 9 directories, every directory passed |
| 2026-11-07 16:05 | stages | orchestrator | `python -B task-cycle/cycle_stages.py 9f5d073b-1bb6-40f8-a4e8-ace10f092e06 --output .runs/task-cycles/cycle-no-private-names/stages.md` | `stages.md` | exit 0, no warnings; 0:44:43 of work, 36,148,107 tokens; the other session of the harness's task directory, `a628800b-b34d-4157-9f36-4245b582cfc3`, holds no word of this cycle and is not counted |
| 2026-11-07 16:15 | request | orchestrator | blocked draft, branch pushed, description published from `request.md` after its form check and its check of private paths | https://github.com/mariusznazar/the-way/pull/83 | opened as a draft; the record copy is cleaned and committed next, then the description is edited with its link |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | In what order do the cleaning of the copy and the remarks check (WAY-294) run? *Questions carried to cycle* of the task | The remarks check runs as today on `.runs/task-cycles/<task-slug>` (the original), unchanged. The cleaning is then one rewriting applied to every text file of the copy, so an item of a report and the same item in the remarks come out in the same words. The new script and `remarks_check.py` both run on the cleaned copy before the commit that adds it. Autonomous choice, the smallest reading that fulfils the task | the task's *Questions carried to cycle*; `task-cycle/skill/SKILL.md` "The process remarks check" | cleaning the original in `.runs` first: the nightly review and a resumed session would read cleaned paths where they need real ones, and the reports would lose the paths they cite | a wrongly cleaned item shows as a listing of the remarks check on the copy; the commit is not made until it lists nothing | author handoff |
| Q2 | The author's concern: `Task source:` of the record template and the plan-state reader (`project-level/plan_state.py` 253-258). Author report, Problems 1 | Keep the absolute path in the working record in `.runs/` (the reader reads that directory in a worktree) and let the cleaning describe the document in the committed copy, where the reader takes the frozen copy the plan's *Document* links. Autonomous choice, the smallest reversible reading; the template line is a one-line edit either way | `reports/author-report.md` Problems 1; the whole-change review is asked to check the code path | the template stops asking for the path: the working-directory proof of a plan item then reports `unchecked` | a plan member's cycle loses its anchor until the Document links the copy; an independent task is not affected | whole-change review handoff |
| Q3 | How is the blocking finding of the whole-change review answered? `reports/whole-review-report.md`, finding 1 | Way (c): WAY-308, the template and the section say that for a plan item the done proposal waits until *Document* links the frozen copy; `plan_state.py` and the invariant unchanged; a test pins the reader's output on a cleaned copy; the `Task relation:` line stays unchanged and a listing of it goes to the human. Autonomous choice | reviewer's fixture evidence; WAY-153; the task's Out of scope | (a) teach the reader a new anchor: a change of a trust-boundary file of `project-level` and its invariant test, another task; (b) keep a described form the reader compares: still needs reader code | a plan member's cycle shows its done proposal late; the human links the copy as the plan template already has them do at the end | fix handoff |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `task.md` beside this record | orchestrator | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| base gate: `python -B gate/run_tests.py` | orchestrator, `ad44b84`, separate checkout of the base; checks already failing on the base: none | exit 0; 765 tests, 9 directories, all passed (`base-gate.log`) | none |
| focused checks of the author (c8fe9f6..b6d93e8) | author, worktree | `python -B gate/run_tests.py task-cycle` 0 (185 tests), `agent-instructions` 0 (18), `elements/part-map` 0 (39), `elements/common` 0 (109), `python -B elements/common/foundation_check.py` 0 (0 errors) (`reports/author-report.md`) | none |
| focused checks of the fix (d745246, 4deb195) | author, worktree | `task-cycle` 0 (187 tests), `project-level` 0 (271), `agent-instructions` 0 (18), `foundation_check.py` 0 (0 errors); mutation of the first new reader test: exit 1, restored: exit 0 (`reports/fix-report.md`) | none |
| gate on the change: `python -B gate/run_tests.py` | orchestrator, `4deb195`, the task worktree | exit 0; 804 tests in 9 directories, every directory passed (`change-gate.log`) | none |
| process remarks check: `python -B task-cycle/remarks_check.py .runs/task-cycles/cycle-no-private-names` | orchestrator, original record | first run exit 1 (11 items from 4 reports listed, `*report.md` rename needed first); after the entries were appended: exit 0; 2 runs | none |
| form check of the description: `python -B task-cycle/request_check.py .runs/task-cycles/cycle-no-private-names/request.md --task .runs/task-cycles/cycle-no-private-names/task.md` | orchestrator | exit 0; 1 run | none |
| check of private paths on the description: `python -B task-cycle/private_paths_check.py .runs/task-cycles/cycle-no-private-names/request.md` | orchestrator | exit 0, `checked: 1 files, 0 listed`; 1 run so far | none |

## Return step

- Foundation compared with code: not run: the return step does not run on code whose review a blocking finding remains on (`task-cycle/skill/blocked_finding.md`, WAY-163)
- Decisions written or changed: by the author's foundation step: WAY-308 and WAY-309 (new), WAY-294 narrowed through WAY-309's third binding sentence; the return step itself did not run
- Invariants written or changed: none
- Environment facts: none (the author kept `Based on: none`, see its report, choice 4)
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 as WAY-308, row 2 as WAY-309

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/83, draft, marked `blocked` in its title
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/cycle-no-private-names/request.md --task .runs/task-cycles/cycle-no-private-names/task.md` last exit 0 (1 run); check of private paths on it last exit 0 (1 run); in this copy, committed after the first publication: the edit that adds the record's link is checked after this commit
- Writes to the task's backlog entry: the request link as `[url::...]` on the task's line; its state symbol `[/]` is left as it stands
- Process remarks on the-way:
  - one author, .runs/task-cycles/cycle-no-private-names/reports/author-report.md: `elements/decisions/SKILL.md`, named by the handoff as the record-decision skill: not found; the skill is `elements/decisions/skill/SKILL.md` (with `read.md`, `decide_entry.md`, `projected.md`).
  - one author, .runs/task-cycles/cycle-no-private-names/reports/author-report.md: Unclear: what the record template's `Task source:` line should ask for. The handoff says it must stop asking for an absolute path. But `project-level/plan_state.py` (lines 253-258) anchors the record of a plan item to its task by that line's absolute path when it reads a working cycle directory, and a line that is no absolute path gives "original Task source or Document cannot be anchored", i.e. unchecked, for the invariant `project-plan-state-evidence`. I kept the absolute path in the working record and made the committed copy cleaned (see Problems 1).
  - one author, .runs/task-cycles/cycle-no-private-names/reports/author-report.md: Unclear: what to do if the new check lists the `Project relation:` line itself (the line must stay unchanged). Its template form is the plan's file name and the task's name, so it should never hold an absolute path; I wrote no rule for the case.
  - one author, .runs/task-cycles/cycle-no-private-names/reports/author-report.md: Unclear: how the record of an old cycle already in the history relates to the new rules: out of scope by the task; nothing written.
  - one author, .runs/task-cycles/cycle-no-private-names/reports/author-report.md: A decision, invariant or glossary entry that already states the rows: none found (search of the foundation for `private`, `remarks`, `task-cycles/`, `absolute path`); WAY-27 and the invariant `outbound-link-reach` are the nearest and are not changed.
  - one author, .runs/task-cycles/cycle-no-private-names/reports/author-report.md: A guideline file of the product (coding or testing): none (the task, question 4).
  - review of the fix, .runs/task-cycles/cycle-no-private-names/reports/whole-review-2-report.md: Unclear: whether the `blocked` state the handoff asked for on a listed relation line was meant to be reachable through the existing request template; the template's row "A draft for another reason" gives a plain draft (the author's choice, disclosed in `fix.md`). Not decided here.
  - review of the fix, .runs/task-cycles/cycle-no-private-names/reports/whole-review-2-report.md: Not found: any text in WAY-309 or the section that says what happens to the exit code and step 6's record of it when a relation line stays listed.
  - whole-change review, .runs/task-cycles/cycle-no-private-names/reports/whole-review-report.md: Unclear: whether cycles of plan items write the expanded `Task relation:` form (`plan item — <plan path> (...), item N <name>`) with the plan given by a path. `task-cycle/record_template.md` gives only `<independent | plan item | source only>`; the expanded form is known only from the reader's code and tests. No archived record of a plan item is in the tree. Finding 1's second form depends on it.
  - whole-change review, .runs/task-cycles/cycle-no-private-names/reports/whole-review-report.md: Not found: a test of `project-level/plan_state.py` that reads a record whose `Task source:` holds no absolute path (searched `test_plan_state.py` for `Task source` — only absolute or document-path forms).
  - whole-change review, .runs/task-cycles/cycle-no-private-names/reports/whole-review-report.md: Not found: a decision, invariant or guideline that says what the orchestrator does with the `binary files not read` count of the new script (Minor 7).
  - orchestrator: `task-cycle/remarks_check.py` reads only the files `reports/*report.md`, while `task-cycle/skill/SKILL.md` and `task-cycle/record_template.md` name no file name for a stage report; the first run on this record read 0 reports and listed nothing until the reports were renamed to end in `report.md`. The handoff's report paths should end in `report.md`, or the check should read every report not named a handoff.
