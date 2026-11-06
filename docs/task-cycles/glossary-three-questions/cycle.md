# Cycle record — the way: reguły słownika produktu — węższe znaczenie, słowa procesu w produkcie, pliki w innym języku, ocena uwag o słowach

- Task source: `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_slownik_trzy_pytania.md`, accepted 2026-11-05 (*Settlements to record*: "6 shown, 5 accepted — 2026-11-05"); frozen copy `docs/task-cycles/glossary-three-questions/task.md` (sha256 prefix `0c67bd3e963cca83`)
- Task relation: independent
- Product repository: `C:\Storage\repos\the-way` (the-way itself; worktree `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions`)
- Process pin: this repository at `61c72fb` (the-way is the product; no pin moved)
- Target branch and base: `foundations`, `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a`
- Task branch: `task/glossary-three-questions`
- Status: request open

## Two questions at start

- Trust boundary: no — the change touches `foundations/decisions.md`, `elements/glossary/template.md` and `task-cycle/review/SKILL.md` (parts `decisions`, `glossary`, `task-cycle`); the part map names no trust boundary in any of them.
- Irreversible operation: no — the change edits text of the foundation, a template and a review skill; nothing is deleted, migrated or published.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — all five questions of the task carry the human's answers with their *Not chosen* ways, and all five rows of *Settlements to record* settle their entries; the wording of the entries is the writer's (WAY-134). The sentence-test of question 1b is the row 3 settlement; the "Out of scope" item (fixing sentences in loop2) is not this cycle's.
- Reserved choice: none — no language, framework, library, store of data, way of logging in or place to run is in play.
- Execution route and reason: one author without a plan — the change is a set of text edits to three files that hang together (one decision log, one template, one review skill) and fits one agent; judged from the task document alone, no preliminary plan, no slice-size script.
- Author: one author with `make-change`, class `same` (Sonnet, the harness's model closest to mine) rather than the default `cheaper`: the change rewrites binding decisions whose wording decides how later reviewers grade (WAY-104, WAY-95, WAY-99, a new decision in `task-cycle` scope), and a wrong qualifier reaches every product pinned to the-way; resumed twice (the fix of the first review's two blocking findings; the return step); no replacement.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: the agents were launched through the `Agent` tool and resumed through `SendMessage`; each returned by a completion notification, and the turn was yielded while only that result remained; no timeout and no interruption; the limit was the tool's own.
- Whole-change review: a reviewer other than the author, `review-change`; range `61c72fb..24e092c` (7 files, +191/-83: `foundations/decisions.md` 200 lines changed, `elements/glossary/template.md` 48, `task-cycle/review/SKILL.md` +5, `elements/common/way_of_working.md` 5, `elements/glossary/skill/decide_entry.md` 8, `task-cycle/record_template.md` 4, `task-cycle/skill/return_step.md` 4); first line `FAIL 24e092ca8dd8ae2e7b6165133552e7590f73dc8c`, report `reports/review-1-report.md`; coverage: every *To do* item 1-5 and *Settlements to record* row 1-5 met, source fidelity (the *Rejected* lists take the task's *Not chosen* ways) checked; no plan, so no blocking finding comes from a slice. After the fix, the review of the fix passed (`reports/review-fix-1-report.md`), and the merge with the target passed (`reports/review-merge-report.md`, first line `PASS 826fff27d590d5f75e567c28816fe5a7276eb093`).
- Review rounds: whole change, range `61c72fb..24e092c`, `reports/review-1-report.md`: `FAIL`; blocking F1, F2 (form of decisions WAY-104 and WAY-293 against `elements/decisions/template.md`); fix `049e84e` (range `24e092c..049e84e`, `reports/fix-1-report.md`); review of the fix `reports/review-fix-1-report.md`: `PASS 049e84e`; no blocking finding remains
- Weakest-point checks: the one author named the requirement that the test of questions 2 and 1b works in both directions and only on sentences the files already hold; check: each of the three places read for both directions, the old rule's phrases searched across the repository, the new text applied to the task's two examples, the unchanged paragraph of the grading rule compared byte for byte; it showed that all hold, leaving open only whether "could be read" asks for a plausible reader's confusion (`reports/author-report.md`). The fix and the return step report no own-work check (Q6).

The last commit of a discarded attempt or of a slice returned too large is a historical name, not
a link to follow: the commit is reachable only until the reflog expires. A choice or ruling of a
discarded attempt keeps its row in the questions table, with *Used by* naming the discarded
attempt.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: one-author route.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-06 | start | orchestrator (Sonnet 5.5) | task read whole; `agent-instructions/README.md`, `task-cycle/skill/SKILL.md` read; foundation read by "Reading the foundation" for parts `decisions`, `glossary`, `task-cycle` (WAY-95, 97, 99, 104 read whole; part map read) | worktree `.runs/worktrees/glossary-three-questions`, branch `task/glossary-three-questions` from `61c72fb` | two questions: no / no; no open design choice; one author; base gate started in separate checkout `.runs/base-glossary-three-questions` (log `C:\Storage\repos\the-way\.runs\base-glossary-three-questions.log`) |
| 2026-11-06 | author returned | author (Sonnet) | handoff-author.md | report `reports/author-report.md`; commit `24e092c` (7 files, +191/-83) | status `done`; checks: foundation_check exit 0, `gate/run_tests.py task-cycle` exit 0, `gate/run_tests.py elements/common` exit 0 (as reported); concerns answered: Q3, Q4 below; next: whole-change review |
| 2026-11-06 | dispatch: whole-change review | reviewer, `review-change` variant whole change, class `same` (Sonnet), foreground; not the author | handoff `reports/handoff-review-1.md`; range `61c72fb..24e092c`, frozen task, author report | report `reports/review-1-report.md` | dispatched |
| 2026-11-06 | review returned; dispatch: fix 1 | reviewer (Sonnet) `FAIL 24e092c`: 2 blocking (F1 WAY-104 has 4 binding sentences, F2 WAY-293 uses "should"), 6 Minor, 1 out of scope | report `reports/review-1-report.md`; findings file `reports/findings-1.md` (copied word for word, lines 45-75); handoff `reports/handoff-fix-1.md` | author resumed (class `same`) for the fix; then the same reviewer reviews the fix range once | next: fix report, then review of the fix |
| 2026-11-06 | fix returned; dispatch: review of the fix | author `done`, commit `049e84e` (1 file); checks as reported: foundation_check exit 0, `gate/run_tests.py elements/common` exit 0, `task-cycle` exit 0; orchestrator read the diff: matches F1 and F2, nothing else moved | report `reports/fix-1-report.md`; handoff `reports/handoff-review-fix-1.md`; range `24e092c..049e84e` | same reviewer resumed, once | next: review-fix-1 |
| 2026-11-06 | review of the fix returned; gate | reviewer (Sonnet) `PASS 049e84e`, 0 blocking / 0 Minor / 0 out of scope; F1, F2 fixed | report `reports/review-fix-1-report.md` | orchestrator started full gate on `049e84e` (log `change-gate.log`, exit `change-gate.exit`) | next: gate result, then return step (`reports/handoff-return-step.md`) |
| 2026-11-06 | gate returned; dispatch: return step | orchestrator ran the gate (exit 0); author (Sonnet, class `same`) resumed for the return step | handoff `reports/handoff-return-step.md`; head `049e84e` | report `reports/return-step-report.md` | dispatched |
| 2026-11-06 | return step returned; reconciliation; dispatch: review of the merge | author `done`, no commits (nothing drifted); orchestrator fetched `origin/foundations` `2692e05` (4 merged PRs since base): conflict in `foundations/decisions.md`, two decisions numbered WAY-293; merged as `826fff2`, mine renumbered WAY-297, reference in `task-cycle/review/SKILL.md` updated; focused checks on the merged tree: foundation_check 0 errors, `task-cycle` OK (139 tests), `elements/common` OK (109 tests) | return report `reports/return-step-report.md`; handoff `reports/handoff-review-merge.md`; range parents `049e84e` and `2692e05`, head `826fff2` | fresh reviewer (Sonnet), not the author, not the earlier reviewer | next: review-merge, then full gate on the final tree, process remarks check, stages, description |
| 2026-11-06 | review of the merge returned; final gate; remarks; stages | reviewer (Sonnet) `PASS 826fff2`, 0/0/0; orchestrator: full gate on `826fff2` exit 0 (714 tests); remarks check exit 0; `stages.md` written | report `reports/review-merge-report.md`; `final-gate.log`; `stages.md` | all reports renamed `<stage>-report.md` so the remarks check reads them | next: description, form check, push, draft request, record commit |
| 2026-11-06 | dispatch: one author | author, `make-change` variant "the whole change as the one author", class `same` (Sonnet), foreground | handoff `docs/task-cycles/glossary-three-questions/reports/handoff-author.md`; inputs: frozen task, base `61c72fb` | report `docs/task-cycles/glossary-three-questions/reports/author-report.md` | dispatched; next: mechanical read of the short return, then whole-change review (step 9) |
| 2026-11-06 | record and request | orchestrator (Sonnet 5.5) | reports renamed `<stage>-report.md` (the remarks check reads only `reports/*report.md`); process remarks entered; description `request.md` written and form-checked (2 runs, last exit 0) | `request.md`, `stages.md` | branch pushed; draft request https://github.com/mariusznazar/the-way/pull/75 opened; next: record commit and its removal, link by SHA, mark ready |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the task leave an open design choice? Task, *Questions to settle* 1, 1a, 1b, 2, 3 | No — every question has the human's answer and its rejected ways; rows 1–5 of *Settlements to record* are accepted | frozen task | writing a spec — would re-ask what the human settled | a spec round (one agent) wasted | route |
| Q2 | Class of the one author | `same` (Sonnet) | WAY-229; wording of binding decisions | `cheaper` (default) — the change is subtle wording of binding rules | a review round if the wording is loose | Author |
| Q3 | Author: whose cost does the task mean in "z powodem, dla którego jego koszt jest teraz do przyjęcia" (WAY-104 *Rejected*, variant "reported as a warning rather than an error")? | The variant's cost, as the author read it | frozen task, To do 2: "jego" follows "wariantem" | reading the cost as the whole rule's | one clause of one *Rejected* item | author report (d) |
| Q4 | Author: does WAY-240 (test-level names as glossary terms) need aligning with narrowed WAY-95? | Not decided by the orchestrator; left to the whole-change review to grade and scope; the task names neither WAY-240 nor test levels | frozen task (*Decisions in play*, *To do*) | widening the task to WAY-240 | a later change | review handoff |
| Q5 | Target branch moved during the cycle (`origin/foundations` `2692e05`, base `61c72fb`); both added a decision numbered WAY-293. Which keeps the number? | The target's keeps WAY-293 (already merged, carries references in the record of its cycle); this task's decision becomes WAY-297, the next free number after WAY-296 | `git log 61c72fb..origin/foundations`, headings of `foundations/decisions.md` after the merge | renumbering the target's — would rewrite an accepted entry and its references | the entry's number in a commit message of `24e092c` ("WAY-293") still names the old number | merge `826fff2`, request |
| Q6 | Does the report of the fix (`fix-1.md`) need an own-work check, as the target's `SKILL.md` now asks of a `make-change` report of `done`? | No repair asked: `task-cycle/change/fix.md` gives a fix no own-work check, the fix is two edits to two sentences that the findings name, and the skill's new text was not in force when the fix ran | `task-cycle/change/fix.md`, `task-cycle/change/SKILL.md:134`, target's `SKILL.md` | returning the report to its author — one more round for two word edits | a process remark on the-way, entered below | request |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `docs/task-cycles/glossary-three-questions/task.md` | orchestrator | — |
| code and foundation commits | `24e092c` (the change), `049e84e` (the fix), `826fff2` (merge with `origin/foundations` `2692e05`) | one author; orchestrator for the merge | `FAIL 24e092c`, `PASS 049e84e`, `PASS 826fff2` |
| full reports | `reports/author-report.md`, `reports/review-1-report.md`, `reports/fix-1-report.md`, `reports/review-fix-1-report.md`, `reports/return-step-report.md`, `reports/review-merge-report.md` | agents | see the commits |
| handoffs and findings | `reports/handoff-*.md`, `reports/findings-1.md` | orchestrator | — |
| stages | `stages.md` | `task-cycle/cycle_stages.py` | — |
| request description | `request.md` | orchestrator | form check exit 0 |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` (final tree) | orchestrator, merge `826fff2`, worktree `.runs/worktrees/glossary-three-questions` (log `final-gate.log`) | exit 0; "714 tests in 8 directories; every directory passed" | none failed, none unrun |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/glossary-three-questions` | orchestrator, merge `826fff2` | 4 runs: exit 0 with "0 reports" (reports not named `*report.md`; renamed), exit 1 with 1 report, exit 1 with 16 items not held, exit 0 "checked: 6 reports, 16 items other than none, 0 not in the process remarks" | none |
| `python -B elements/common/foundation_check.py .`, `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py elements/common` | orchestrator, merge `826fff2` before its commit | "0 errors"; 139 tests OK, exit 0; 109 tests OK, exit 0 | none |
| `python -B task-cycle/request_check.py docs/task-cycles/glossary-three-questions/request.md --task docs/task-cycles/glossary-three-questions/task.md` | orchestrator | 2 runs, last exit 0, "form holds" | none |
| `python -B gate/run_tests.py` (reviewed change) | orchestrator, `049e84e`, worktree `.runs/worktrees/glossary-three-questions` (log `change-gate.log`) | exit 0; "667 tests in 8 directories; every directory passed" | none failed, none unrun |
| `python -B gate/run_tests.py` (base) | orchestrator, `61c72fb`, separate checkout `.runs/base-glossary-three-questions` (deleted after the run) | exit 0; "667 tests in 8 directories; every directory passed" | none failed, none unrun; no check failing on the base |

## Return step

- Foundation compared with code: the six entries the change writes or changes (WAY-11, WAY-95, WAY-97, WAY-99, WAY-104, WAY-293 as it was then, WAY-297 now), the decisions the task names and leaves as they are (WAY-161, WAY-263, WAY-226, WAY-72, WAY-171) and the part-map entries of `decisions`, `glossary`, `task-cycle` and `elements-common`, against the files at `049e84e`; nothing no longer matched, no correction (`reports/return-step-report.md`). One open point left on purpose: the review skill's sentence says "should" where the decision says "needs".
- Decisions written or changed: WAY-297 (new; WAY-293 when written, renumbered at the merge); WAY-95, WAY-97, WAY-99, WAY-104 (edited in place); WAY-11 (one phrase)
- Invariants written or changed: none
- Environment facts: none (the change rests on no source outside the product)
- Glossary terms: none; whether "qualifier" deserves an entry was judged no
- Part-map changes: none
- Projected entries written whole or in part: none (task is independent)
- Rows of *Settlements to record* written: row 1 -> WAY-95; row 2 -> WAY-297; row 3 -> WAY-99; row 4 -> WAY-104; row 5 -> WAY-99 (with WAY-97 narrowed to English text)

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/75, draft; to be marked ready after the link to the record is written
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py docs/task-cycles/glossary-three-questions/request.md --task docs/task-cycles/glossary-three-questions/task.md`, last run exit 0, 2 runs; in a copy committed before the link to the record was written, `written and checked after this commit`
- Writes to the task's backlog entry: none (the backlog is in the author's private notes, outside this repository)
- Process remarks on the-way: the entries under this line
  - the one author (make-change), docs/task-cycles/glossary-three-questions/reports/author-report.md: The handoff's "decisions lines near 1981–2008, 4958, 6858" were found (WAY-93, WAY-176, WAY-240). Only WAY-240 has a rule shaped like WAY-95 ("a level whose name means in the product something other than in the field ... is a term of the product's glossary"); I left it, since it fixes a particular case (test levels) in a product's guidelines and the task does not name it. It now reads as stricter than WAY-95; the human may want it aligned in a later change.
  - the one author (make-change), docs/task-cycles/glossary-three-questions/reports/author-report.md: The task's instruction that the *Rejected* of WAY-104 keep the variant "reported as a warning rather than an error" "with the reason for which its cost is now acceptable" is ambiguous (whose cost). I took it as the variant's cost (placement choice d).
  - the one author (make-change), docs/task-cycles/glossary-three-questions/reports/author-report.md: No test or script checks a rule of this change; focused tests only confirm the foundation and templates still parse.
  - the one author (make-change), docs/task-cycles/glossary-three-questions/reports/author-report.md: The handoff says "WAY-07" among the entries to edit; WAY-07 (edit in place) needs no change and was not edited.
  - the one author (make-change), docs/task-cycles/glossary-three-questions/reports/author-report.md: `agent-instructions/README.md` says the integration route; I made no request.
  - the fix of the one author (make-change), docs/task-cycles/glossary-three-questions/reports/fix-1-report.md: My own script to count sentences of binding paragraphs gave 0 for every entry (the regex was wrong); I counted by reading the paragraphs instead. The reviewer's script was not available to me.
  - the fix of the one author (make-change), docs/task-cycles/glossary-three-questions/reports/fix-1-report.md: The skill sentence at `task-cycle/review/SKILL.md:113` still says "should"; the fix is not asked to touch it, so its wording differs by one word from WAY-293. Whether to align it is for the reviewer or the orchestrator.
  - the return step (make-change), docs/task-cycles/glossary-three-questions/reports/return-step-report.md: The Minor and out-of-scope findings of `review-1.md` (M1-M6 and one out-of-scope) were read and left untouched (WAY-161); they are no foundation entries.
  - the return step (make-change), docs/task-cycles/glossary-three-questions/reports/return-step-report.md: Whether "qualifier" deserves a glossary entry is a judgment I took as "no"; the reviewer or the human may weigh it at the merge.
  - the return step (make-change), docs/task-cycles/glossary-three-questions/reports/return-step-report.md: The one-word difference between the skill sentence and WAY-293 ("should have" / "needs") is left, as the review of the fix put it, to the human; fixing it would add a commit and a review of that range.
  - the review of the whole change (review-change), docs/task-cycles/glossary-three-questions/reports/review-1-report.md: No script or test checks the sentence count or banned words of a binding paragraph (grep of `foundation_check.py`), so F1 and F2 pass the gate; found only by reading against the template.
  - the review of the whole change (review-change), docs/task-cycles/glossary-three-questions/reports/review-1-report.md: "jego koszt" in To do 2 is ambiguous (whose cost); I used the orchestrator's recorded reading and flagged the tail (M3).
  - the review of the whole change (review-change), docs/task-cycles/glossary-three-questions/reports/review-1-report.md: The edit of WAY-11 (`foundations/decisions.md:330`, "a meaning for which WAY-95 gives it an entry"), of `task-cycle/skill/return_step.md:10` and `task-cycle/record_template.md:154` is beyond the task's list; I found it a defensible follow-up of WAY-95 (the handoff asks for leftover places; those three restated the loose "a meaning other than the usual one"). Not graded as a finding; the wording "a meaning for which WAY-95 gives it an entry" is awkward but not wrong.
  - the review of the whole change (review-change), docs/task-cycles/glossary-three-questions/reports/review-1-report.md: Whether the human reads WAY-293 as `narrows WAY-161` or `derives from`: not settled by the task (see Declined).
  - the review of the whole change (review-change), docs/task-cycles/glossary-three-questions/reports/review-1-report.md: The task file's claim `elements/glossary/template.md:51-52` for the old `TODO` was for the base commit; at the head the `TODO` is gone (grep).
  - the review of the fix (review-change), docs/task-cycles/glossary-three-questions/reports/review-fix-1-report.md: none. The Minor findings M1-M6 and the out-of-scope finding O1 of `review-1.md` are not fixed by this commit, as WAY-161 provides for them; they are not reopened here.
  - the orchestrator: `task-cycle/remarks_check.py` reads only the files `reports/*report.md`, a pattern that stands in the script's docstring and nowhere else I found; the first run on this record said "checked: 0 reports, 0 items other than none, 0 not in the process remarks" with thirteen files in `reports/` named `author.md`, `review-1.md` and the like (as the earlier records name them), so a record named otherwise passes the check with nothing read. I renamed this record's six reports to `<stage>-report.md` and ran it again; the script is not changed here.
  - the orchestrator: two cycles that write a decision at the same time take the same next number; this task's decision and a decision of the target both took WAY-293, and the collision showed only at the merge of step 12 (a conflict at the end of the decision log), where this task's decision was renumbered WAY-297. The message of this task's first commit still says WAY-293.
  - the orchestrator: `task-cycle/skill/SKILL.md` (the repair of reports, as the target changed it) asks for an own-work check in a `make-change` report of `done`, while `task-cycle/change/fix.md` gives a fix none; the report of the fix of this cycle has no own-work check, and I did not return it for repair because the fix was two edits that the findings name.
