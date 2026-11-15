# Report — executor of slice 22 (the testing guidelines)

**Status:** done with concerns (concerns: the proposal for the `product-guidelines` row, and the rows
of the question table left out; both below).

## Files and commits

- `guidelines/testing.md` — added, 270 lines, 0 removed.
- Commit `b47e1b2` — "Write the testing guidelines of the-way: five levels, the rules of the template, the recipe of each level and its exemplar" (on `task/the-way-coding-and-testing-guidelines`, base `6fd60ef`). The author address of the commit is the private one, as `git.md` of the author's rules gives for this account.

## Checks (each as command and exit code)

Run after the commit (the foundation check reads the files git tracks, so a run before the commit did not see the new file; I noticed that and repeated):

- `python -B elements/common/foundation_check.py` — exit 0 (`0 errors`).
- Seen failing, to prove the check reads the file: with `WAY-394` changed to `WAY-9999` in one *Decision* line, the same command prints `guidelines/testing.md:73: WAY-9999 names no decision of the log`, `1 error`; with the first invariant of `### Trust boundaries` changed to `no-such-invariant`, it prints `guidelines/testing.md:128: no-such-invariant names no invariant`, `1 error`. Both edits were reverted with `git checkout guidelines/testing.md` before I returned (the tree is clean).
- `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` — exit 0 (`checked: 324 files, 0 listed`).
- `python -B instruction-files/check_instructions.py . --file guidelines/testing.md` — exit 0 (`0 error, 0 warn, 4 info`; the infos are file sizes).
- Paths: `git ls-files -- <path>` lists each path of *Where in code* (the six files and the eleven directories) and each exemplar file; each of the five exemplar classes and methods exists (grep of the class and the `def` line in each file: `Fingerprint.test_a_tab_is_kept` at `relation-model/test_fingerprint.py:65`, `RewriteEdgesTest.test_a_rewrite_of_2000_tokens_is_not_counted` at `task-cycle/test_cycle_measures.py:604`, `PlanStateEvidence.test_fresh_remote_record_composes_both_transitions` at `project-level/test_plan_state_invariant.py:329`, `TrackedFilesUnderElementsTest.test_no_tracked_file_under_elements_holds_the_pending_marker` at `elements/common/test_elements_pending_marker.py:28`, `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` at `process-audit/test_audit_count.py:1042`).
- `grep -c "WAY-328" guidelines/testing.md` — 0. The identifiers the file names: WAY-253, WAY-392 to WAY-402; each exists in the log (the foundation check passes).
- Not run: the full gate (WAY-160). No test was written, so no failing test of mine.

## Own-work check

Requirement my work most likely does not meet: "every reference names an entry the foundation holds" and "the *Invariant* of `### Trust boundaries` names the refusal invariant of each of the nine boundaries". The check: the run of `foundation_check.py` with a false decision and a false invariant (above) shows the check reads this file, and the clean run shows all references hold. The nine invariants named: `readiness-check-refuses-non-utf-8`, `project-plan-form`, `project-plan-state-evidence`, `cycle-stages-refuses-crafted-names`, `cycle-measures-refuses-nested-line`, `gate-times-refuses-impossible-entry`, `audit-count-refuses-record-links`, `check-instructions-refuses-outside-links`, `installation-paths-through-links` — one for each of the nine boundaries of the part map (`project-level/readiness_check.py`, `plan_check.py`, `plan_state.py`; `task-cycle/cycle_stages.py`, `cycle_measures.py`, `gate_times.py`; `process-audit/audit_count.py`; `instruction-files/check_instructions.py`; `installation/install.py`). The mapping of `project-plan-form` to `plan_check.py` and of `project-plan-state-evidence` to `plan_state.py` is mine from the invariants' sentences; I read the two entries whole and did not check the tests that cite them.

Weakest point: the sentence of each row of the table of parts. The settlement gives only the classification (computation or connections); the sentence of each row is written by me from the part map's description of the part, with no source of its own for the reason.

## Choices (with the way rejected and the cost if wrong)

1. **Row of `product-guidelines` (orchestrator's proposal, to be confirmed by the human at the request):** written "In computation: its test reads the text of the skills and checks each reference in it against the files", as the handoff's binding answer says. Rejected: leaving the row empty (the handoff forbids it). Cost if wrong: the row is one sentence; the classification only decides where a mutation tool would run, and the-way adopts none (WAY-402).
2. **Rows left out of the question table of `### Choosing the level`:** the template's rows on a property test, on a double of someone else's service with a contract test, and on a smoke test after the build. No level of WAY-393 has those meanings, and a sixth level or a recipe is a change of that decision, which I may not make. Also left out of `### Test inputs and expected values`: the sentences on property tests and a generator of a test library. Rejected: keeping the rows and mapping them onto the five levels — an invented meaning. Cost if wrong: a reviewer comparing with the template sees the rows missing; the fix is to add the rows once the human settles whether the-way has such tests (it is a question for the human, not decided here).
3. **Rows of the question table for the three glossary levels** ask "Does it need the resources of a files test and no more?" instead of restating the glossary's sentence, so that no second definition stands in the file (WAY-393, WAY-240). Rejected: restating the definition in the question. Cost if wrong: a reader must open the glossary; the table names the term in each row.
4. **`### Mutation testing`** stands as `none — WAY-402` alone, as `guidelines/coding.md` writes its departures; the head-check of WAY-253 stands as an example under `## Examples`, which the template allows for text a departing decision keeps.
5. **Exemplar field:** the path of the file and the test written apart (`` `path`, the test `Class.test` ``), because `check_instructions.py` reads a backticked text holding a `/` as a path and `path::test` would be reported as a dead path once `AGENTS.md` names the file. It names WAY-395 (the field binds) and the decision that designates the exemplar (WAY-396 to WAY-400).
6. **Decision fields:** WAY-392 for each required rule (the decision adopting the template); `### Choosing the level` adds WAY-393, `### Where the expected value comes from` adds WAY-394. The decisions on a mutation tool, on permissions and on an AI tool do not exist, so none is named. Good and Bad lines read `none` except in `### Where the expected value comes from`, where WAY-394's verification gives a pair.
7. **Recipes:** *Shape* stands as an example (no decision, per WAY-395); the other binding fields end with WAY-395; fields that repeat another level read "as in `unit`"; *Time limit* reads `none — WAY-395` in every recipe, as the plan says. *Doubles* of the git test and of the repository test say what WAY-395's verification gives.
8. **No further rules of the product** and no rule of the-way's own beyond the template's required ones: the task and the decisions settle none.
9. **Where in code** lists `gate/run_tests.py` (the one command), the five exemplar files and the eleven directories that hold `test_*.py` files; the-way has no configuration file of a test tool.

## Reach beyond the handoff

- `foundations/decisions.md` WAY-232, WAY-233, WAY-234 (read whole, lines 9019-9143): the handoff names the template's text for these rules but not the decisions; I read them to word the rules. WAY-238, WAY-239, WAY-243, WAY-228, WAY-236 I did not read; their text I took from the template's description of the rules.
- `foundations/invariants.md`: the six invariants of the orchestrator's additions (`tracked-file-private-paths`, `repository-file-location`, `ci-checking-commands`, `guidelines-file-place`, `map-reference-target`, `derived-file-content`), each whole, as the additions name them.
- `guidelines/coding.md` and `guidelines/coding-check.md` (written by earlier slices): read as the model of the form, since the handoff does not name them.
- `instruction-files/check_instructions.py` lines 360-470 (path recognition) to settle choice 5; `gate/run_tests.py` head to confirm the form of the gate's command.

## Working copies

None made; `.runs/executor-22/` was not created. A temporary backup file of the guidelines in `.runs/` (made before the first edit-and-check, which ran before the commit) was removed in the same command.

## Unread material

- The task passages named: read whole (`task.md` 25-69, 145-210, 510-545) — the lines 70-144 and 546 on were not named and not read.
- `foundations/decisions.md`: WAY-167, 168, 173, 231, 235, 237, 240, 241, 242, 252, 253, 254, 312 and WAY-392 to WAY-402 read whole at the ranges the handoff gives; `foundations/invariants.md` 238-251, 311-320, 86-95 (via the awk of the entry) and 486-547 read. `foundations/part_map.md` read whole. `foundations/glossary.md` 203-222 read. Environment facts (E37, E38): not read; the file does not name them.
- `product-guidelines/testing/template.md`, `product-guidelines/template.md`, `product-guidelines/reading.md`: read whole.
- Invariants `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation` of the orchestrator's addition: not read, since the slice adds no Python file; the end of `plan.md` ("Orchestrator's additions") and the plan's *Choices*: not read (the handoff carries the slice and its answers; the plan was not opened, as `slice.md` says).

## Searches not found or unclear

- None not found. Unclear: the handoff says "named as the glossary terms" for E34-E36; I wrote them in the *Decision* cell next to WAY-393 as "the glossary term `files test`" and left the *Level* cell as the bare level name, because the template's table "names that term"; if the level cell should hold the term itself the cell reads the same words.
- The foundation check ignores an untracked file; I found it by running it before the commit and getting a clean run on a file it did not read.

## Questions

None blocking. For the human at the request: confirm (a) the `product-guidelines` row, (b) whether the-way has tests of the kinds of the three left-out rows (property, contract, smoke), (c) the mapping of the nine invariants to the nine boundaries.
