# Cycle record — what the cycle's leader does when an agent did not read the material it was pointed to

- Task source: the task's note in the author's backlog — `Status: ready for cycle`; settlements accepted 2026-11-08; frozen copy `task.md` beside this record
- Task relation: independent
- Product repository: the-way (https://github.com/mariusznazar/the-way)
- Process pin: not applicable (the-way itself)
- Target branch and base: `foundations` at `02c3d47f8891b66507687b40665b323f3d20def8`
- Task branch: `task/unread-material` (worktree `.runs/worktrees/unread-material`)
- Status: request open

## Two questions at start

- Trust boundary: no — the change edits skills, templates and foundation entries of parts `task-cycle`, `elements-common`, `decisions`; the part map gives all three `Trust boundary: none`.
- Irreversible operation: no.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — the task document settles where each piece goes (point 1 appendix in `task-cycle/skill/SKILL.md`, a fixed report section in the five stage methods, one item in the request's section for the human's decisions, WAY-150 and its carriers changed to the title screening) and carries four accepted settlement rows (kind decision). The exact wording of the report section's heading and of each sentence is a choice of how to make what the task settles. Line numbers the task cites for `foundations` @ a3206c1 have moved (e.g. WAY-150 is at `foundations/decisions.md:4209`); reconciled against the current files, no effect on the required outcome.
- Reserved choice: none — no language, framework, library, store, login or place to run.
- Execution route and reason: one author without a plan — documentation edits across ~10 files of three parts plus four decisions; each edit is specified by the task, and one agent can hold the whole change.
- Author: one author, class `same` (change across many parts: skill, five methods, template, common way of working, decision log), harness model `sonnet`.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code foreground `Agent` call (blocks until the agent returns).
- Whole-change review: fresh reviewer, general-purpose agent, harness model sonnet (class `same`, by `review-change`); range `02c3d47..afa4343`, first line `PASS afa43439b39b66fc1e737897b0c6b8b0e11aa129`, report `reports/review_whole_report.md`; 10 files changed (220 insertions, 49 deletions); covers every item of *To do* (points 1-4), the four rows of *Settlements to record* and source fidelity (the quoted dopisek checked as a substring, the dropped sentence searched and absent); 0 Critical, 0 Important, 5 Minor within the task, 0 out of scope; read 45 of 162 selected decisions whole and 117 by title, named none unread that bears on the change.
- Review rounds: no blocking finding. The 5 Minor findings of the review of the whole change were fixed once by the author (`613f100`, range `afa4343..613f100`, report `reports/author_report.md` fix section) and the same reviewer reviewed the fix once (`reports/review_fix_report.md`): `PASS 613f100a0a79f70d34aa7665b061b059ac9233eb`; all 5 fixed; one new Minor (the added test records the leak of `task-cycle/remarks_check.py` as expected behaviour) goes to the request's list; the fix was not reverted. The return step committed nothing, so it had no review.
- Weakest-point checks: one author: the requirement most likely unmet was the update of every place of the orchestrator's skill that lists what a report holds; the check was a grep for the two section names against each other over `task-cycle`, which showed no listing place missed (`reports/author_report.md`, own-work check). For the fix: the quoted dopisek compared word for word with *To do* point 1 after the edit, unchanged.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-10 | start | orchestrator (sonnet-5-5) | task.md | worktree `.runs/worktrees/unread-material`, base `02c3d47`; base gate started in `.runs/base-check-unread-material`, log `base_gate.log` | route chosen: one author; next: dispatch author |
| 2026-11-10 | author | one author, general-purpose agent, sonnet (class `same`) | `reports/author_handoff.md`, variant "the whole change as the one author", `task-cycle/skill/foundation_step.md` | `reports/author_report.md` | `done with concerns`; commits `ca376a0`, `afa4343`; task-cycle 234 tests, elements/common, agent-instructions, instruction-files green, foundation check 0 errors; mechanical check: clean worktree, changed files match the task's items (10 files); report has Searches, Unread material and own-work check. Next: whole-change review |
| 2026-11-10 | whole-change review | fresh reviewer, general-purpose agent, sonnet (not cheaper than orchestrator) | `reports/review_whole_handoff.md`, `review-change`, range `02c3d47..afa4343` | `reports/review_whole_report.md` | `PASS afa43439b39b66fc1e737897b0c6b8b0e11aa129`; 0 Critical, 0 Important, 5 Minor within the task; reviewer read 45 of 162 decisions whole, 117 by title; author's gap closed as far as its selection reaches (Q1) |
| 2026-11-10 | gate | orchestrator | `python -B gate/run_tests.py` on `afa4343` | `gate_head_afa4343.log` | exit 0, 863 tests in 9 directories, every directory passed; to be rerun after the fix |
| 2026-11-10 | fix of Minor findings | author resumed (class `same`, sonnet) | `reports/review_whole_findings.md` (the 5 Minor findings in the reviewer's words) | `reports/author_report.md` (fix section) | `done`; commit `613f100`; task-cycle 235 and elements/common 117 tests green, foundation check 0 errors |
| 2026-11-10 | review of the fix | the same reviewer resumed | range `afa4343..613f100`, `reports/review_whole_findings.md`, fix report | `reports/review_fix_report.md` | `PASS 613f100a0a79f70d34aa7665b061b059ac9233eb`; all 5 Minor fixed; one new Minor (the new test in `task-cycle/test_remarks_check.py:156-170` records the leak as expected behaviour) → request list |
| 2026-11-10 | return step | author resumed (class `same`, sonnet) | `task-cycle/skill/return_step.md` | `reports/author_report.md` (Return step section) | `done`, nothing to correct, no commit; foundation check exit 0, 0 errors; no review of it, since it committed nothing |
| 2026-11-10 | gate | orchestrator | `python -B gate/run_tests.py` on `613f100` (the final tree: the target branch had not moved, `origin/foundations` still `02c3d47`, so no reconciliation merge) | `gate_head_613f100.log` | exit 0, 864 tests in 9 directories, every directory passed |
| 2026-11-10 | stages | orchestrator | `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/unread-material/stages.md <session>` | `stages.md` | exit 0; about 31.7M tokens in all, 0:30:28 working time; all agents on claude-sonnet-5-5 |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The author's report says 94 of its 160 selected decisions were skimmed by title only, the glossary entries unread, WAY-82 read in part (author_report.md, *Unread material*). | Carry the gap into the handoff of the whole-change reviewer, who selects its own foundation and can judge it; do not resume the author. | `reports/author_report.md` lines 176-191; `reports/review_whole_handoff.md` | Resume the author to read the 94: would repeat the reading the reviewer does anyway, and the author's selection is not the one the change is judged against. | A decision outside the reviewer's selection that bears on the change goes unseen; the reviewer's own *Unread material* shows it. | review_whole |
| Q2 | Row 4: new decision or in-place edit of WAY-287? | Accept the author's in-place edit of WAY-287. | `reports/author_report.md` Choices | A third new entry beside WAY-287. | The human expected a new number; the meaning is the same. | whole-change review |
| Q3 | Where does the request template's new item stand in *For you to decide*? | Accept the author's item 14, last in the list. | `reports/author_report.md` Choices; the references by number in `task-cycle/skill/correction.md` and `task-cycle/skill/SKILL.md` that renumbering would break; the reviewer agreed | Insert it beside item 4 and renumber items 5-13. | The reader finds it at the end of the list, not beside the skipped steps; easy to move. | request, whole-change review |
| Q4 | What is the new report section called and where does it stand? | Accept **Unread material**, before **Searches not found or unclear** in every method. | `reports/author_report.md` Choices; the reviewer agreed | A name or place that lets the section fall inside the Searches section, which `task-cycle/remarks_check.py` reads. | A report written in the reverse order leaks a line into the process remarks (recorded by a test). | the five methods, the orchestrator's skill |
| Q5 | What does "closed on the way" mean for the request item? | The reviewer, or a fresh one, read what stayed unread; the orchestrator's autonomous choice does not close the gap for the request. Written into WAY-287 by the fix. | `reports/author_report.md` Choices; `reports/review_whole_report.md` Minor 1 | Letting the third way of the orchestrator's rule close it. | An item stands in a request where the orchestrator had a reason for the gap. | request template item 14, WAY-287 |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/unread-material/task.md` | orchestrator | n/a |
| code and foundation commits | `ca376a0`, `afa4343` (`02c3d47..afa4343`) | one author | `PASS afa43439b39b66fc1e737897b0c6b8b0e11aa129` |
| fix of Minor findings | `613f100` | one author | `PASS 613f100a0a79f70d34aa7665b061b059ac9233eb` |
| reports | `reports/author_report.md`, `reports/review_whole_report.md`, `reports/review_fix_report.md` | author, reviewer | n/a |
| stages | `stages.md` | orchestrator | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on the base | orchestrator, `02c3d47`, separate checkout `.runs/base-check-unread-material` | exit 0; 861 tests in 9 directories, every directory passed (log `base_gate.log`) | none failing on the base |
| `python -B gate/run_tests.py` on `afa4343` | orchestrator, worktree `.runs/worktrees/unread-material` | exit 0; 863 tests in 9 directories, every directory passed (`gate_head_afa4343.log`) | none; superseded by the run on the final tree |
| `python -B gate/run_tests.py` on `613f100`, the final tree | orchestrator, worktree `.runs/worktrees/unread-material` | exit 0; 864 tests in 9 directories, every directory passed (`gate_head_613f100.log`) | none failed or unrun |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | `merges: 18`, `threshold: 30`, `reminder: no` | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/unread-material` (original) | orchestrator | exit 1 on the last run, 1 line listed, held wrong (see the process remarks); 4 runs in all | the listing held wrong |

## Return step

- Foundation compared with code: WAY-150, WAY-287, WAY-325 and WAY-326 against `elements/common/way_of_working.md`, `task-cycle/review/SKILL.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md` item 14 and the five stage methods; the entries the task names (WAY-148, WAY-213, WAY-159, WAY-260, WAY-286) and those the search found (WAY-114, WAY-134, WAY-158, WAY-227, WAY-289, WAY-294); the part-map entries `task-cycle`, `elements-common`, `decisions`. Nothing no longer matched; corrected: none.
- Decisions written or changed: WAY-325 (new), WAY-326 (new), WAY-150 (edited in place), WAY-287 (edited in place)
- Invariants written or changed: none
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: row 1 — WAY-325; row 2 — WAY-326; row 3 — WAY-150; row 4 — WAY-287

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/96 — opened as a draft, to be marked ready after the record is committed
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py .runs/task-cycles/unread-material/request.md --task .runs/task-cycles/unread-material/task.md`, last run exit 0 (1 run); written and checked again after the record's commit (the edit that adds the record's link)
- Writes to the task's backlog entry: the request link and the state of the task's line (see the final report)
- Process remarks on the-way:
  - one-author change, .runs/task-cycles/unread-material/reports/author_report.md: The task cites "`task-cycle/skill/SKILL.md:191-193`", "`:193`" and WAY-150 at line 4060; they have moved (the handoff said so), and I found the places by content.
  - one-author change, .runs/task-cycles/unread-material/reports/author_report.md: *To do* point 4 says "keep *Rejected* as the task's sources describe it, which stands". I read it as "do not remove the existing ways" and added three ways not chosen from question 3's answer, as the decisions template asks of a decision written from a row; if the intent was to leave *Rejected* of WAY-150 entirely untouched, the added three sentences are the change to drop.
  - one-author change, .runs/task-cycles/unread-material/reports/author_report.md: The handoff asked for the new section to be separate from **Searches not found or unclear**; the task's wording for the section ("stały dział") gives no name. I named it **Unread material**.
  - review of the whole change, .runs/task-cycles/unread-material/reports/review_whole_report.md: The task cites `task-cycle/skill/SKILL.md:191-193`, `:193` and WAY-150 at line 4060; they have moved (the handoff says so). Found by content.
  - review of the whole change, .runs/task-cycles/unread-material/reports/review_whole_report.md: The author's report quotes "keep *Rejected* as the task's sources describe it, which stands" as *To do* point 4 of the task; the phrase is in the orchestrator's author handoff (`author_handoff.md:95`), not in the task. The author's reading (add the task's "Not chosen" ways, keep the old ones) is the reading I accepted, but the phrase is unclear: "which stands" could also mean "leave *Rejected* alone".
  - review of the whole change, .runs/task-cycles/unread-material/reports/review_whole_report.md: Where "closed on the way" is defined: not in the task, not in WAY-287, only in the template item (Minor 1).
  - review of the whole change, .runs/task-cycles/unread-material/reports/review_whole_report.md: Whether a decision read by title counts as "read in part" for WAY-325: not stated where the orchestrator's rule stands (Minor 2).
  - review of the whole change, .runs/task-cycles/unread-material/reports/review_whole_report.md: A test or check that the five methods hold **Unread material** before **Searches not found or unclear**: not found (the grep for the name in the test files returns only `test_remarks_check.py`). Nothing guards the sections mechanically; the orchestrator's repair rule is the only guard.
  - orchestrator: a listing of `task-cycle/remarks_check.py` the cycle holds wrong, two lines. (1) the line `---` of `.runs/task-cycles/unread-material/reports/author_report.md` is a horizontal rule that follows the last item of the report's **Searches not found or unclear** section and opens the next section of the report; the script reads it as a paragraph of that section. (2) the line of `.runs/task-cycles/unread-material/reports/review_whole_report.md` that begins `as a bold label outside a list` is the second line of a wrapped sentence of a Minor finding that mentions the section's name; it starts with the bold name, and the script reads it as a label of the section. Neither is an item of an agent's section, so neither is appended as an item.
