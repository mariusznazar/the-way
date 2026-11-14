# Cycle record — the way: two changes of the decision log — a reading as the source of a fact about a setting in another's service, an invariant names the place of its condition — and a test that the "decision pending" notes do not return

- Task source: the task's note in the author's backlog (path withheld), status `ready for cycle`, frozen copy beside this record as `task.md` (sha256 prefix 423b29163083), human actions: none
- Task relation: independent
- Product repository: the-way (github.com/mariusznazar/the-way)
- Process pin: none (the-way itself)
- Target branch and base: foundations, `0e1cd3cd804433f7a82ffb631e96917ef74c1040` (checkout fast-forwarded from `d40d1cb` at the start)
- Task branch: task/service-reading-and-invariant-condition
- Status: request open

## Two questions at start

- Trust boundary: no — the files changed are templates, a skill, README text, the decision log, the invariants file and a test; the part map gives `none` as the trust boundary of `decisions`, `invariants`, `environment-facts`, `elements-common`.
- Irreversible operation: no.

## Spec and execution route

- Open design choice at start: none — every choice the task leaves is settled by its *Questions to settle* and *Settlements to record* (rows 1-6), which give the wording of the three decision changes, the new invariant and its method.
- Reserved choice: none
- Execution route and reason: one author without a plan; the change is eight listed edits of text over decisions, two templates, one skill file, the README and the invariants file, plus one small test; the settlements give the wording, so one agent holds it.
- Author: the-way-author, class `same` as the orchestrator's (a change over several parts — decisions, environment-facts, invariants, README, gate/test — in text where a wrong word binds later work); model: closest to the orchestrator's.
- Plan: none on the one-author route
- Discarded attempt: none
- Slices returned too large: none
- Agent waiting: completion notification of the harness for each background agent; no timeout or interruption; the gate ran as a background command and reported by completion notification
- Whole-change review: reviewer other than the author, `review-change`; range `0e1cd3c`..`8680824`; first line `FAIL 8680824c3c81f9a932eb20e3e2ff93ce503798c3`, `reports/whole-change-review-report.md`; changed files: decisions.md 68/31, invariants.md 10/0, test_elements_pending_marker.py 44/0, test_foundation_check.py 16/0, facts template 30/14, facts skill draft 9/5, invariants template 3/3, README 4/3; all 8 items, 6 rows and 6 answers judged covered, blocking finding B1 within the task (no slice)
- Review rounds:
  - correction 1, remarks `reports/correction-1-remarks.md`: review `reports/correction-1-review-report.md`, `PASS 43ffa5a`, no blocking finding, no fix; 2 Minor and 1 out of scope to the request's lists
  - findings `reports/whole-change-findings.md`: range `0e1cd3c`..`8680824`, report `reports/whole-change-review-report.md`, blocking B1 (template and WAY-80 rationale say nothing is cut from the output, against the allowed "lines the sentence rests on"), Minor M1-M5 fixed in the same round; fix range `8680824..4f26b6b` (commit `4f26b6b`, `reports/fix-report.md`), reviewed by the same reviewer resumed, `PASS 4f26b6b`, `reports/fix-review-report.md`, no blocking finding remained; the two Minor findings of that review went to the request's list, the first fixed afterwards by the return step
  - return step: commit `43ffa5a`, reviewed by a fresh reviewer, `PASS 43ffa5a`, `reports/return-review-report.md`, 0 findings
- Weakest-point checks: author: the invariant's test must fail on a tracked file holding the text, and the foundation check must read a multi-line command under *Source* — shown by the failing run (two real notes, a seeded one, one split by a line end) and a passing run, and by the scratch run for the carried question (`reports/author-report.md`); fix: the wrapped seeded note fails, a tab passes (`reports/fix-report.md`)

## Slices

| Slice | Base | Class, executor and model | Risk | Head | Mechanical check and retry | Review, fix and review of the fix |
|---|---|---|---|---|---|---|

## Events

| Time | Stage | Actor and model | Handoff, skill and inputs | Output or full report | Short result and next step |
|---|---|---|---|---|---|
| 07:42 | start | orchestrator | skill task-cycle/skill/SKILL.md; task.md | this record | checkout fast-forwarded to `0e1cd3c`; worktree and branch made with --no-track; base is a merge with the tree of its second parent equal, so the failing list is taken from the merged branch's record; next: dispatch the one author |
| 07:43 | one author | the-way-author, class same (no model override) | `reports/author-handoff.md`; make-change, the whole change as the one author | `reports/author-report.md` | dispatched on base `0e1cd3c`; next: read its short return and checks, then the whole-change review |
| 07:55 | one author return | the-way-author | `reports/author-report.md` | commits `19efdfd`, `8680824`; status done | read: checks (elements/common 201 tests exit 0, foundation_check 0 errors), unread material (WAY-07, WAY-33, WAY-328, glossary, examples.md: carried into the review handoff, which names them), searches: one unclear sentence-count remark; three choices beyond the task's letter passed to the review |
| 08:00 | whole-change review | the-way-stage, class same (no model override) | `reports/whole-change-review-handoff.md`; review-change, range `0e1cd3c`..`8680824` | `reports/whole-change-review-report.md` | dispatched after the mechanical check of the author's return (clean tree, non-empty range, report with checks, own-work check, unread material, searches); next: its first line |
| 08:20 | whole-change review return | the-way-stage | `reports/whole-change-review-report.md` | `FAIL 8680824`; 1 blocking (B1), 5 Minor (M1-M5), 0 out of scope | checks read: foundation_check 0, elements/common 201 tests 0, invariant test 0, private paths 0, git diff --check 0, file sizes 0; unread material: 98 of 112 decisions by title, invariants from `script-imports` on, 7 glossary entries read — none bears on a finding, recorded as an autonomous choice (the findings rest on the entries read); searches: nothing needing a decision; next: one fix |
| 08:25 | fix | the-way-author resumed, class same | `reports/fix-handoff.md`; `reports/whole-change-findings.md`; make-change, the fix of a review's findings | `reports/fix-report.md` | resumed for B1 and M1-M5 from head `8680824` |
| 08:40 | fix return | the-way-author | `reports/fix-report.md` | commit `4f26b6b`, status done | mechanical: clean tree, non-empty range `8680824..4f26b6b`, checks with exit codes (elements/common 201 tests 0, foundation_check 0 errors, invariant test 0), own-work check, unread material, searches present; M2 conceded by the author (claim withdrawn, test kept as a pin) |
| 08:45 | review of the fix | the-way-stage (the reviewer of the whole change, resumed), class same | `reports/fix-review-handoff.md`; `reports/whole-change-findings.md` | `reports/fix-review-report.md` | resumed once for range `8680824..4f26b6b` |
| 09:00 | review of the fix return | the-way-stage | `reports/fix-review-report.md` | `PASS 4f26b6b`; 0 blocking, 2 Minor (a long unreflowed line in WAY-80's second paragraph and a one-word last line of its *Rationale*; the invariant's sentence one long line) | to the request's Minor list; checks read: foundation_check 0, elements/common 201 tests 0, invariant test 0, private paths 0, diff --check 0 |
| 09:05 | return step | the-way-author resumed, class same | `reports/return-handoff.md`; `task-cycle/skill/return_step.md`, `foundation_step.md` | `reports/return-report.md` | resumed on head `4f26b6b` |
| 09:15 | return step return | the-way-author | `reports/return-report.md` | commit `43ffa5a` (rewrap of one line in WAY-80, one example reworded in WAY-84), status done | mechanical: clean tree, non-empty range, checks with exit codes (foundation_check 0, private paths 0), unread material and searches present; no new entry written |
| 09:20 | review of the return step | the-way-stage, fresh, class same | `reports/return-review-handoff.md` | `reports/return-review-report.md` | range `4f26b6b..43ffa5a` |
| 09:30 | review of the return step return | the-way-stage | `reports/return-review-report.md` | `PASS 43ffa5a`; 0 findings | checks read: foundation_check 0 errors, diff --check 0 |
| 09:35 | target branch | orchestrator | `git fetch` | `origin/foundations` unchanged at `0e1cd3c` | no merge, so no reconciliation review; the tree is the one the gate ran on |
| 09:40 | gate | orchestrator | `task-cycle/gate_times.py` | `gate_times.md`, `gate-run1.log` | exit 0, 1328 tests in 10 directories on `43ffa5a` |
| 09:50 | stages and measures | orchestrator | `task-cycle/cycle_stages.py`, `cycle_measures.py` | `stages.md`, `mechanism_measures.md` | both exit 0 |
| 10:00 | request | orchestrator | `task-cycle/skill/request_template.md` | `request.md`; draft request https://github.com/mariusznazar/the-way/pull/121 | form check exit 0, private-paths check exit 0, branch pushed |
| 10:30 | correction 1 | orchestrator | the human's comment on the request, `reports/correction-1-remarks.md` | remark: do item 1 (kind 14) in this request; items 2-7 accepted | `git fetch`: the target branch had not moved, nothing to merge; remarks recorded word for word |
| 10:35 | correction 1 review | the-way-stage, fresh, class same | `reports/correction-1-handoff.md`; review-change | `reports/correction-1-review-report.md` | a fresh reviewer reads whole the fourteen decisions the first review left unread and the example pairs of two of them against the new invariant |
| 10:50 | correction 1 review return | the-way-stage | `reports/correction-1-review-report.md` | `PASS 43ffa5a`; 0 blocking, 2 Minor within the task (M1: the identifier of a decision in an invariant's sentence against the links beside the sentence; M2: the identifier names what the sentence demands), 1 out of scope (O1: the derivation from WAY-35) | all fourteen read whole, none unread; 27 of 123 selected decisions read whole, 96 by title only; checks read: foundation_check 0 errors, invariant test 0, diff --check 0; the Minor and out-of-scope findings of a correction are not fixed: they go to the request's lists; no code changed, so no gate rerun (`git diff 43ffa5a HEAD` is empty) |
| 11:00 | request | orchestrator | `task-cycle/skill/request_template.md`, variant for a correction | `request.md` rewritten for the state after the correction | item of kind 14 closed by the fresh review; kind 8 item for M1 with only "Make a task of it?"; kind 17 sentence added; stages and measures rerun, both exit 0 |

## Questions and autonomous choices

| ID | Question and source | Answer or choice | Evidence | Alternative rejected | Cost if wrong | Used by |
|---|---|---|---|---|---|---|
| Q1 | The checkout was 26 commits behind `foundations`; the task cites `f749cfc` and quotes WAY-80/84/60 as they stood | Work on `0e1cd3c`; the author compares each quoted passage with the log as it stands | `git diff --stat d40d1cb HEAD` shows `foundations/decisions.md` and `elements/invariants/template.md` changed by PR #120 | Work on the old commit — the branch would not merge cleanly | the wording of a decision changed in PR #120 is overwritten | author |
| Q2 | Where does the new invariant's test stand? (task does not place it) | `elements/common/test_elements_pending_marker.py`, part `elements-common` | author report; whole-change review judged it allowed | `gate/` (that part answers for the runner) | moving a file and its citation | author |
| Q3 | Does the test read a note wrapped across lines? | yes: every run of spaces and line breaks counts as one space; sentence and pattern `decision[ \n]+pending` say the same | author report, fix report; M3 | a literal single space — a wrapped note would pass | a legitimate wrapped use of the words would fail; none exists | author |
| Q4 | WAY-80's *Rejected* clause "a reading of a host that a check reruns" | reads "of a host or a service" | author report; whole-change review: allowed | leaving it — it would contradict the new reading | a deleted clause | author |
| Q5 | Example pairs in the *Verification* of WAY-80, WAY-84, WAY-60 | one example each for the changed sentences | author report; whole-change review: allowed (the pair is optional) | no example — the new sentences would be unchecked | removable | author |
| Q6 | Binding paragraphs of WAY-80 (five sentences) and WAY-60 (four) | split into two paragraphs each, no sentence changed | review finding M1 | five sentences in one paragraph — the form does not allow it | a reader looks in the second paragraph | fix |
| Q7 | The carried question: does the foundation check read a fact whose *Source* has a multi-line code block? | yes, if the block is indented to the item; a test pins it, its claim of catching a break of `blocks` or `fields` withdrawn | author report; reviewer reproduced the passing run (M2) | no test — the template's promise would be unpinned | the test passes for any valid first *Source* line | author, fix |

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | `.runs/task-cycles/service-reading-and-invariant-condition/task.md` | orchestrator | n/a |
| code commits | `19efdfd`, `8680824` | the-way-author | whole-change review FAIL `8680824`, then PASS `4f26b6b` |
| fix | `4f26b6b` | the-way-author | `PASS 4f26b6b` |
| return step | `43ffa5a` | the-way-author | `PASS 43ffa5a` |
| tests | `elements/common/test_elements_pending_marker.py` (new), `elements/common/test_foundation_check.py` | the-way-author | reviewed within the change |
| full agent reports | `reports/author-report.md`, `whole-change-review-report.md`, `fix-report.md`, `fix-review-report.md`, `return-report.md`, `return-review-report.md` | agents | n/a |

## Verification

| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |
|---|---|---|---|
| list of the tests failing before the change | orchestrator, base `0e1cd3c` (merge; tree `48aa66e134cd01d4dad7882c163144701673258b` equals that of its second parent) | taken from `docs/task-cycles/co-trafia-do-dziennika-decyzji/cycle.md` of commit `07a2ba5`, *Verification*, its final gate run 4 on `8571691`: exit 0, 1326 tests in 10 directories | none failing on the base; no gate run on the base at the start; note: `gate/test_run_tests.py` `DirectoriesAtOnce.test_by_default_every_directory_runs_at_the_same_time` failed in 2 of 4 full runs of that cycle (flaky, WAY-243) |
| `python -B task-cycle/gate_times.py --output .runs/task-cycles/service-reading-and-invariant-condition/gate_times.md -- python -B gate/run_tests.py` (run 1) | orchestrator, `43ffa5a` (the final tree), Windows | 0; 1328 tests in 10 directories, 1179.8 s, one other registered gate at the same time | none |
| `python -B elements/common/foundation_check.py` | orchestrator, `43ffa5a`, without `--skip-test-citations` | 0; `0 errors`, no `listed:` line | none |
| `python -B gate/run_tests.py elements/common` | author, both reviewers, `4f26b6b` | each 0, 201 tests | not rerun after the return step's two edits of prose; the full gate covers them |
| `python -B task-cycle/review_reminder.py origin/foundations` | orchestrator | 0; `tag: foundation-review/2026-11-06`, `merges: 42`, `threshold: 30`, `reminder: yes` | none |
| `python -B task-cycle/cycle_stages.py --output .runs/task-cycles/service-reading-and-invariant-condition/stages.md 3accdae2-e092-4074-bed5-ead4d6ab0967`; `python -B task-cycle/cycle_measures.py --output .runs/task-cycles/service-reading-and-invariant-condition/mechanism_measures.md 3accdae2-e092-4074-bed5-ead4d6ab0967` | orchestrator | both 0 | none |
| `python -B task-cycle/request_check.py .runs/task-cycles/service-reading-and-invariant-condition/request.md --task .runs/task-cycles/service-reading-and-invariant-condition/task.md`; `python -B task-cycle/private_paths_check.py .runs/task-cycles/service-reading-and-invariant-condition/request.md` | orchestrator, on the description | both exit 0, 1 run each | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/service-reading-and-invariant-condition` | orchestrator, on the original | exit 1 listing 7 items, then 0 after they were appended to the process remarks; 2 runs | none |
| `python -B task-cycle/remarks_check.py docs/task-cycles/service-reading-and-invariant-condition`; `python -B task-cycle/private_paths_check.py docs/task-cycles/service-reading-and-invariant-condition`; `python -B task-cycle/image_files_check.py docs/task-cycles/service-reading-and-invariant-condition` | orchestrator, on the cleaned copy | all three exit 0 in the last run of each commit pair (private paths: exit 1 once, listing 7 files, before the first rewriting, then 0); 2 runs of each for the first pair, 1 run of each for the pair after correction 1 | none |
| `python -B task-cycle/cycle_stages.py` and `cycle_measures.py` again, for the orchestrator's session after correction 1 | orchestrator | both 0; 52 min of working time, 32.6 million tokens | none |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/service-reading-and-invariant-condition` after correction 1 | orchestrator, on the original | exit 1 listing 3 items of the correction review's report, then 0 after they were appended | none |
| gate on the corrected tree | not run: correction 1 changed no code, `git diff 43ffa5a HEAD` is empty | n/a | the gate of `43ffa5a` (exit 0, 1328 tests) stands for the same tree |

## Return step

- Foundation compared with code: WAY-80, WAY-84, WAY-60, WAY-35 *Verification*, the new invariant, the facts template, the facts skill, the invariants template, `README.md`, `foundation-review/weak_points.md`, `agent-instructions/README.md` and the part map against the code and the task; two mismatches corrected in `43ffa5a` (one long line of WAY-80 rewrapped, one example of WAY-84 reworded), no meaning changed (`reports/return-report.md`)
- Decisions written or changed: WAY-80, WAY-84, WAY-60 (changed in place), WAY-35 (*Verification* only)
- Invariants written or changed: `elements-no-pending-marker`, set by row 6 of the task, derived from WAY-35
- Environment facts: none
- Glossary terms: none
- Part-map changes: none
- Projected entries written whole or in part: none
- Rows of *Settlements to record* written: 1 → WAY-80 and WAY-84; 2 → WAY-84 *Rejected*; 3 → WAY-80; 4 → WAY-80; 5 → WAY-60; 6 → `elements-no-pending-marker` and WAY-35 *Verification*

## Request handoff

- Request URL and status: https://github.com/mariusznazar/the-way/pull/121, ready for review (corrected once)
- Description: `request.md` beside this record; form check and private-paths check on the description exit 0 (1 run each); the checks on the copy of the record are filled in by the edit that adds the record's link
- Corrections after the request opened:
  - correction 1, remarks `reports/correction-1-remarks.md`: item 14 · not-required
- Writes to the task's backlog entry: none
- Process remarks on the-way:
  - one author, .runs/task-cycles/service-reading-and-invariant-condition/reports/author-report.md: The handoff names `elements/environment-facts/skill/draft.md` for the skill's *Source* point; the point is in that file, found at once.
  - one author, .runs/task-cycles/service-reading-and-invariant-condition/reports/author-report.md: Unclear: the template's rule that a decision's binding paragraph holds one to three sentences, against WAY-80's existing four; the foundation check does not enforce it (see the choice above).
  - one author, .runs/task-cycles/service-reading-and-invariant-condition/reports/author-report.md: Not found: a glossary entry for "reading" (the term is used in the decision's sense, as it already was).
  - whole-change review, .runs/task-cycles/service-reading-and-invariant-condition/reports/whole-change-review-report.md: Not found: a glossary entry for "reading" (also the author's finding); the word is used as WAY-80 gives it, no finding.
  - whole-change review, .runs/task-cycles/service-reading-and-invariant-condition/reports/whole-change-review-report.md: Unclear: the author's report says the carried question's scratch run printed `the entry lacks *Source*` with a heading in column 0; I did not reproduce that run; I reproduced the passing run and the passing mutations of M2.
  - whole-change review, .runs/task-cycles/service-reading-and-invariant-condition/reports/whole-change-review-report.md: Unclear: no rule I found fixes how a binding paragraph answers a question that already has four sentences (WAY-05 gives "one paragraph for each part of another question"); the way out in M1 is mine.
  - whole-change review, .runs/task-cycles/service-reading-and-invariant-condition/reports/whole-change-review-report.md: `git worktree add` for the scratch worktree adds an entry to the shared worktree list while it exists; it was removed with `git worktree remove --force` and is absent from `git worktree list`.
  - correction 1 review, .runs/task-cycles/service-reading-and-invariant-condition/reports/correction-1-review-report.md: Not found: a sentence of any decision that forbids a pending marker in a template (O1); a rule that states whether an identifier in the sentence of an invariant is one of "the links" of WAY-56 (M1).
  - correction 1 review, .runs/task-cycles/service-reading-and-invariant-condition/reports/correction-1-review-report.md: Unclear: WAY-77 and the facts template speak of "the date it was read" where a reading has "the date run"; unchanged by this change.
  - correction 1 review, .runs/task-cycles/service-reading-and-invariant-condition/reports/correction-1-review-report.md: Unclear: whether "the foundation" in WAY-02 ("names an entry the foundation holds") includes the pinned the-way of a product; the check reads only the log's prefix, so nothing reports it, and I took it as not needing a finding.
