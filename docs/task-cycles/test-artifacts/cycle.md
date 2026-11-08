# Cycle record — the way: artefakty sprawdzenia zmiany docierają do opisu PR-a spoza historii repo produktu

- Task source: `the task's note in the author's backlog`, `Status: ready for cycle`, settlements accepted 2026-11-08; frozen copy `docs/task-cycles/test-artifacts/task.md`
- Task relation: independent
- Product repository: the-way (itself)
- Process pin: not applicable — the-way itself, the checkout is the process
- Target branch and base: `foundations` @ f218b5542ae55b72a95832adde67591365abb72a
- Task branch: `task/test-artifacts` (worktree `.runs/worktrees/test-artifacts`)
- Status: request open

## Two questions at start

- Trust boundary: no — the part map names no trust boundary for `task-cycle`, `decisions`, `invariants`, `elements-common` or the files of `project-level` the change touches (the technology step's documents; the three scripts it names as a boundary are not touched).
- Irreversible operation: no — the change edits text and one check script; nothing it does cannot be undone.

The cycle prepares an irreversible operation and never performs it; preparing the code for it does
not authorize running it.

## Spec and execution route

- Open design choice at start: none — every row 1–7 of *Settlements to record* settles its entry; the form of the check of point 8 (an extension of `task-cycle/private_paths_check.py` or a script of its own) is a choice of how to make what the task settles, which the author makes and names.
- Reserved choice: none — no language, framework, library, store of data, way of logging in or place to run is needed; the place for screenshots is left to products by the task itself.
- Execution route and reason: one author without a plan; one agent can hold a change that is mostly text (about five foundation entries, the technology step's documents, the request template, `ui_check.md`) plus one small script check and its test; class `same` because the change reaches several parts (decisions, invariants, project-level, task-cycle).
- Author: one author, class `same`, model `sonnet` (the closest to the orchestrator's); resumptions: none yet. It did the foundation step with its code.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: Claude Code background agents; the result arrives by completion notification, the turn is yielded when only that result remains; no limit hit.
- Whole-change review: reviewer opus (other than the author), `review-change`; range f218b55..d0d3ce6, report `reports/review1_report.md`, `FAIL`; one author, no plan; blocking findings I-1 (glossary widening), I-2 (WAY-319 sentence 2), I-3 (row 7 narrower than accepted) come from no slice; Minor 1-4 within the task.
- Review rounds: whole-change review `FAIL` (3 Important, `reports/review1_report.md`); one fix ef0195e (`reports/fix1_report.md`) for the blocking and Minor 1-4 findings; review of the fix `PASS` (`reports/review2_report.md`); no blocking finding remained; 3 new Minor notes of the fix review stand for the request's list.
- Weakest-point checks: author — requirement named: item 8 on a realistic record and no repeated "three matters"; check: the script run on a throwaway record with a real photo (exit 1, 0 without it, 2 for a missing directory) and a grep for the old wording; it showed the script works and missed one enumeration in a decision (found by the review, Minor 1); report `reports/author_report.md`. Fix and return step: the fix report's grep for lists of three, `reports/fix1_report.md`.

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

Not used: one author without a plan.

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 2026-11-08 23:50 | start | orchestrator, sonnet 5.5 | task document read; `agent-instructions/README.md`, `task-cycle/skill/SKILL.md` read | — | checkout up to date with `origin/foundations` (f218b55), clean; branch and worktree created from it |
| 2026-11-08 23:58 | one author | author, sonnet (class `same`) | `docs/task-cycles/test-artifacts/reports/author_handoff.md`, `task-cycle/change/SKILL.md` variant "the whole change as the one author" | `reports/author_report.md` (pending) | dispatched in background; orchestrator waits for the completion notification |
| 2026-11-09 00:25 | one author returns | author, sonnet | handoff above | `reports/author_report.md`; commits dd84fba, d0d3ce6 | `done with concerns`; mechanical check passed: worktree clean, range non-empty, checks carry command and exit code, own-work check and Searches present; concerns go to the review |
| 2026-11-09 00:27 | whole-change review | reviewer, opus | `reports/review1_handoff.md`, `task-cycle/review/SKILL.md` | `reports/review1_report.md` (pending) | dispatched in background |
| 2026-11-09 00:40 | whole-change review returns | reviewer, opus | `reports/review1_handoff.md` | `reports/review1_report.md`, first line `FAIL d0d3ce6c913b04481fff652de175eeae37099013`; 3 Important blocking, 5 Minor within the task, 0 out of scope | findings file `reports/findings1.md` cut from the report in the reviewer's words; blocking findings come from no slice |
| 2026-11-09 00:42 | fix | author resumed, sonnet (class `same`) | `reports/findings1.md`, `task-cycle/change/fix.md` | `reports/fix1_report.md` (pending) | one fix for the blocking and the Minor findings; then one review of the fix |
| 2026-11-09 01:00 | fix returns | author, sonnet | `reports/findings1.md` | `reports/fix1_report.md`; commit ef0195e | `done`; mechanical check: worktree clean, range non-empty, checks carry command and exit code, Searches present; I-1 by revert of the glossary change, I-2 by removal, I-3 by new invariant `record-copy-image-files` (`Method: review`) |
| 2026-11-09 01:02 | review of the fix | reviewer opus, resumed | range d0d3ce6..ef0195e, `reports/findings1.md`, `reports/fix1_report.md` | `reports/review2_report.md` (pending) | dispatched in background |
| 2026-11-09 01:10 | review of the fix returns | reviewer opus, resumed | range d0d3ce6..ef0195e | `reports/review2_report.md`, `PASS ef0195edb7128b30f9768aab89e3b8846d2d8d5e`; 0 blocking, 3 new Minor notes (not fixed; go to the request's list) | review rounds closed |
| 2026-11-09 01:32 | gate (step 10) | orchestrator | `python -B gate/run_tests.py` on ef0195e | `.runs/gate_step10.log` | exit 0; 817 tests in 9 directories, every directory passed |
| 2026-11-09 01:33 | return step | author resumed, sonnet | `reports/return_handoff.md`, `task-cycle/skill/return_step.md` | `reports/return_report.md` (pending) | dispatched |
| 2026-11-09 01:45 | return step returns | author resumed, sonnet | `reports/return_handoff.md` | `reports/return_report.md`; commit 25dd4ba (docstring of `task-cycle/image_files_check.py` only); Searches `none` | `done`; no entry, glossary term or part-map change needed |
| 2026-11-09 01:47 | review of the return step | reviewer sonnet (fresh) | `reports/review3_handoff.md`, range ef0195e..25dd4ba | `reports/review3_report.md`, `PASS 25dd4bac8cb40dafe51ff04b4c945f3206a2b874`; 0 blocking, 0 Minor | return step closed |
| 2026-11-09 02:05 | gate (step 12, final tree) | orchestrator | `python -B gate/run_tests.py` on 25dd4ba | `.runs/gate_final.log` | exit 0; 817 tests in 9 directories; origin/foundations (f218b55) already in the branch, no merge needed |
| 2026-11-08 23:55 | base checks | orchestrator | `python -B gate/run_tests.py` in a detached checkout of the base under `.runs/base-check` | `.runs/base-check.log` (running) | result below under *Verification* |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | Does the task leave an open design choice? Task, *Questions to settle* 1–9 and *Settlements to record* 1–7 | No; the check script's form is the author's to make | each question has an answer and a source; row 7 names "a script, like private paths" | writing a spec | an extra spec stage for a choice the author can name in its report | route |
| Q2 | One author or a plan? Task document, `task-cycle/skill/SKILL.md` step 4 | One author, class `same` | the change is text in four directories plus a small script and its test | a plan of slices | if too large the author returns `returned` and the planner splits it | route |
| Q3 | Extend `task-cycle/private_paths_check.py` or make a script of its own for the image check? Task, To do 8; row 7 | A script of its own, `task-cycle/image_files_check.py` | the private-paths script is bound by WAY-309 to paths and note links, and it counts an image as a binary file and skips it; it also runs on the request description, where images stand as links | extending the existing script | one more command in the record step and a second script to keep | author's report |
| Q4 | How does the check recognize an image file? Task, row 7 says "plik obrazu" and no more | By the end of the file name only (a list of 12 extensions, case-insensitive); it never opens a file | signatures are values from outside standards and would need environment facts with sources | recognition by file signature too | an image under another extension, inside an archive or as base64 text passes unseen | author's report, Return step |
| Q5 | What does the fourth matter ask of a product? Task, row 4 names the place only | WAY-165 says the place of the screenshots asks where the files lie outside the product's repository and how the description shows each as an image | `running_product.md` settles a matter only where it answers all the matter asks (WAY-165); both halves come from rows 1 and 4 | a fourth matter without a definition | the step could not run on the new matter; reviewer accepted | WAY-121, WAY-165 |
| Q6 | How is row 7's property stated? Review finding I-3 | Two invariants: `record-copy-image-check` (test, the script) and `record-copy-image-files` (review, no image file in a record copy) | `elements/invariants/template.md` keeps a check and the data it reads as two entries; `review` is a method of the template | one invariant on the script only; widening WAY-316 only | the property would stand in no entry | fix of review 1 |
| Q7 | Does the technology step test the condition of row 6? Review finding I-2 | No: sentence 2 of WAY-319 and its sentence in `research.md` removed | WAY-166 keeps such an option open to the human; row 6 is a condition | an option that fails the condition stays in the comparison with the lack said | a product's technology step does not know the condition until the first cycle; put before the human in the request | fix of review 1 |
| Q8 | Is the term "agent's way to the running product" widened by the place of the screenshots? Review finding I-1 | No: the glossary entry is left as in the base | widening made WAY-219 and WAY-317 one case, and six uses would have to move | widening and rewriting the uses | the term says "means of checking" while WAY-121 counts the place as one of four matters; named by a Minor note of the review of the fix | fix of review 1 |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `docs/task-cycles/test-artifacts/task.md` | orchestrator | — |
| code and foundation commits | dd84fba, d0d3ce6 | one author | `FAIL` by `reports/review1_report.md` |
| fix commit | ef0195e | one author | `PASS` by `reports/review2_report.md` |
| return step commit | 25dd4ba | one author | `PASS` by `reports/review3_report.md` |
| full reports | `reports/author_report.md`, `reports/review1_report.md`, `reports/fix1_report.md`, `reports/review2_report.md`, `reports/return_report.md`, `reports/review3_report.md`; handoffs `reports/*_handoff.md`, `reports/findings1.md` | agents | — |
| request description | `request.md`, https://github.com/mariusznazar/the-way/pull/91 | orchestrator | form check exit 0 |
| table of stages | `stages.md` | orchestrator | — |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| `python -B gate/run_tests.py` on 25dd4ba, the final tree (step 12; it differs from ef0195e by a docstring) | orchestrator, 25dd4ba, worktree | exit 0; 817 tests in 9 directories, every directory passed (`.runs/gate_final.log`) | none |
| `python -B gate/run_tests.py` on ef0195e (step 10) | orchestrator, ef0195e, worktree | exit 0; 817 tests in 9 directories, every directory passed (`.runs/gate_step10.log`) | none |
| `python -B gate/run_tests.py` on the base | orchestrator, f218b55, detached checkout `.runs/base-check` | exit 0; 804 tests in 9 directories, every directory passed (log `.runs/base-check.log`) | none failing on the base |

## Return step

- Foundation compared with code: the entries the change writes or edits (WAY-316..319, WAY-121, WAY-165, WAY-267, WAY-270, both invariants), the entries the task names (WAY-219, WAY-286, WAY-308) and those the search found, and the part map of `task-cycle`, `project-level`, `decisions`, `invariants`, compared with the script, its test and the skills; one mismatch: the docstring of `task-cycle/image_files_check.py` said the private-paths check skips every image as binary, though an SVG is text; corrected in 25dd4ba (`reports/return_report.md`)
- Decisions written or changed: written WAY-316, WAY-317, WAY-318, WAY-319; edited in place WAY-121, WAY-165, WAY-267, WAY-270
- Invariants written or changed: `record-copy-image-check` (test; sets row 7), `record-copy-image-files` (review; sets row 7, the property of any image file)
- Environment facts: none
- Glossary terms: none (a widening of the term "agent's way to the running product" was written and reverted in the fix)
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: 1, 2 → WAY-316; 3 → WAY-317; 4 → WAY-121 (and WAY-165, WAY-267, WAY-270 for consistency); 5 → WAY-318; 6 → WAY-319; 7 → `record-copy-image-check`, `record-copy-image-files`

The return step corrects in the same change whatever no longer matches. It writes an invariant
only for a rule the task, a decision or the human sets, never for behaviour merely because no
invariant covers it.

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/91 — draft, then ready for review after the record commits (state line `ready`)
- Description: `request.md` beside this record, written by `task-cycle/skill/request_template.md`; form check `python -B task-cycle/request_check.py docs/task-cycles/test-artifacts/request.md --task docs/task-cycles/test-artifacts/task.md` last exit 0, 3 runs; check of private paths on it last exit 0
- Writes to the task's backlog entry: the request link and the state, written after the request opens
- Process remarks on the-way:
  - one author, docs/task-cycles/test-artifacts/reports/author_report.md: How an image file is to be recognized (extension or content) — the task and the row say nothing; I chose the end of the name (see above).
  - one author, docs/task-cycles/test-artifacts/reports/author_report.md: Who puts a reviewer's screenshot in the place, and what a read-only reviewer does about the place: the task says "autor albo recenzent pokazuje"; `task-cycle/review/SKILL.md` has no step for a reviewer taking a screenshot, so I added only the finding "a screenshot file among the commits".
  - one author, docs/task-cycles/test-artifacts/reports/author_report.md: Whether WAY-166 ("an option an agent cannot use stays in the comparison with a lack") binds the fourth matter: the task is silent; I took it as binding all four (see `task_run.md`).
  - one author, docs/task-cycles/test-artifacts/reports/author_report.md: Whether the step that settles technology must test row 6's condition on a way (the task only says the-way "sets a condition"); I added the sentence to WAY-319 and one sentence to `project-level/technology/research.md`, marked below.
  - one author, docs/task-cycles/test-artifacts/reports/author_report.md: A glossary or part-map entry that the new script needs: none (the file stays in `task-cycle/**`; no new word needed an entry, only the definition of an existing one changed).
  - one author, docs/task-cycles/test-artifacts/reports/author_report.md: The item order of *For you to decide* for the "no place settled" case: not given by the task; I appended it as item 13 so as not to renumber items other files cite (items 8 and 12).
  - fix of the review's findings, docs/task-cycles/test-artifacts/reports/fix1_report.md: Whether `record-copy-image-files` should have `Part: every` or `task-cycle`: the files it speaks of stand under `docs/task-cycles/`, which the part map does not give to a part of the-way; I took `every`, as `return-step-record` does.
  - review of the whole change, docs/task-cycles/test-artifacts/reports/review1_report.md: Who puts a reviewer's screenshot in the product's place, and how a read-only reviewer does so: the task says "autor albo recenzent pokazuje"; neither the task nor the review skill says how (Minor 4).
  - review of the whole change, docs/task-cycles/test-artifacts/reports/review1_report.md: Whether the-way's invariants may state a property of a product's repository (row 7 says "do repozytorium produktu") or only of the-way's own commits: `foundations/invariants.md:3` says "What the-way states as true or false on every commit"; unclear which repository's commits; I-3's fix offers wording that holds for the-way's own record copies.
  - review of the fix, docs/task-cycles/test-artifacts/reports/review2_report.md: Whether an invariant of the-way that holds only "where {merge-onto} exists" is meant to bind the-way's task branches while the-way has no main branch: `elements/common/rules.md:76-78` says a review reads `{merge-onto}` as `none` there, which reads as no; unclear whether that is intended for rules about record copies the-way commits today.
