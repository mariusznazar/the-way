FAIL 8c6d6688cc9eff8a839ee4718bad435fb5583fcc

# Review of the return step's commit (`8c6d668`), task `scripts-after-foundation-review`

Range `c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2..8c6d6688cc9eff8a839ee4718bad435fb5583fcc`; `git rev-parse HEAD` is the head. One commit; files: `foundations/decisions.md` (WAY-339 and WAY-344), `foundations/part_map.md` (`product-guidelines`), and comment lines `decision:` in three test files. I read the diff of the three test files whole: only comment lines are added, and the three files parse.

Counts: blocking 1, Minor 2, out of scope 0.

## Findings

### Important (blocking)

**1. WAY-344 *Verification*, clause `tests:`, says the register of problems gives exit code 1 for a missing field; the code and the entry's own *Rationale* give exit code 2.**
Place: `foundations/decisions.md:2783-2786` ("that the command that counts the audit, at a field missing in the file of the measures, the file of the gate times, a stage report or the register of problems, gives the values that need it as unknown, writes its result and ends with exit code 1 and a line `Error:` that names the file and the field").
What is wrong: for the register, a heading, a table or a column the count needs and cannot find ends the run with exit code 2 and nothing written. Only a missing *level* of a table of weights or of costs is exit 1 with the result written. The clause lumps "a field missing in … the register of problems" in with the three files of a cycle's record, so it restates the rule more broadly than the entry's binding sentences and *Rationale* give it (WAY-263).
Evidence: `process-audit/audit_count.py` `register_table` and `read_register` (about lines 2057-2132): a missing heading, table or column is appended to `missing` and `read_register` raises `AuditCountError("the register of problems lacks …")`; `main` catches it and `return 2` before any write (the module docstring says the same: "2 … the register lacks a heading, a table or a column it needs"). The test `test_a_register_lacking_a_field_ends_the_run_with_an_error_naming_it` (`process-audit/test_audit_count.py:2445`) asserts `assertEqual(2, done.returncode)` and an empty results directory; I ran it, it passes. The *Rationale* of the entry (`foundations/decisions.md:2843-2845`) says: "a heading or a table that the register lacks leaves what depends on it unreadable and stays exit code 2." The binding first paragraph (`:2752-2754`) limits exit 1 to "a file of a cycle's record that it reads from git history". The old pair of examples said the register case only for a missing *level* of the table; the rewrite widened it.
Why it matters: an agent that compares a later change with this clause would call correct code (a register missing a heading ends with exit 2) a violation, or would accept a change that turns a missing register heading into exit 1 with a result written, which the entry forbids.
Fix direction (not made, I am read-only): name the register in the clause only for the missing level of a table ("a table of weights or of the costs … which lacks a level", already in the clause) and drop "or the register of problems" from the list of files at the head of that part of the clause; or add that a heading, a table or a column the register lacks ends with exit code 2 and nothing written, which the test above holds, with a line `decision:` at it quoting a sentence that says so (the sentence that says it today is in *Rationale*, which a line `decision:` cannot quote, so the first option is the simpler).

### Minor

**2. WAY-339 clause drops the instructions of the reviewer from the changes that start a series of the count of remarks.**
Place: `foundations/decisions.md:7454-7456`: "a series of the count of remarks also at a date of the list of classes and a change of the files that give the form of a stage report or of the type of agent the reviewer receives its instructions as". The binding sentence (`:7423-7424`) says "a change of the form of a stage report, of the list of classes or of the instructions of the reviewer", and `COUNT_PATHS` (`audit_count.py:421`) holds `task-cycle/review` among the four method directories and the type `the-way-stage.md`. The old pair named "a change of the reviewer's instructions" outright. The clause now reads as if the directory `task-cycle/review` were not among the paths; the test `test_a_change_under_the_review_starts_a_series_of_the_count_and_none_of_the_cost` (decision line present) holds it. A reader who takes the clause for the full list would read the reviewer's instructions as outside it. Minor because the binding sentence is untouched and the test holds the case; one phrase ("or of the instructions of the reviewer") would close it.

**3. Two sentences of the old pairs lost their only statement.**
(a) WAY-339, the author's instructions: the binding sentence says "no change of the instructions of the cycle, the reviewer's and the author's included, starts one"; the old *violates* line named "a change of the reviewer's or the author's instructions divides the series of the gate times". The new clause says "none of these splits …", where "these" are the price list, the scripts, the list of classes and the files of the form and of the reviewer; a change of the author's instructions is in no clause and in no tagged test for the measures (the author's type of agent appears only in a test of the count and the cost, `test_audit_count.py:3354-3362`, and in the table at `:3429`, neither tagged for WAY-339's measures). (b) WAY-344, the entry `repository` "for that entry alone": the old *violates* line "reads any other missing entry of that file as having a value of its own" has no clause; the test `test_a_named_repository_the_file_lacks` (`test_audit_count.py:830-835`) holds it but carries no line `decision:`. Both are covered by code and by tests; the loss is in what an agent comparing a change reads. Minor.

## Checked against the task and the foundation, and found true

- Each of the 49 lines `decision:` added quotes a sentence start that stands in the entry's binding sentences (`python -B elements/common/foundation_check.py` reads the quotations: exit 0, 0 errors). I read each tagged test for what it asserts: the tests of the stage report forms (`StagesForms`), of the files of measures and gate times, of the two tables of levels, of the entry `repository`, of the series (`ProcessVersions`, `MeasureVersions`, `PriceBoundary`), of the cache write columns and across the two scripts, and the three tests of the readings of a transcript and of an agent type's definition; each holds the sentence it is tagged with. `test_the_way_without_a_repository_entry_is_this_checkout` does not assert the absence of `Error:` (the other test of the pair does: `assertEqual(b"", done.stderr)`), so the sentence is held in full by the pair.
- The splitting of the third sentence of WAY-344 into three keeps its meaning word for word apart from "the same command" becoming "the command that counts the audit" and "that command"; the entry is edited in place (WAY-07), nothing appended.
- The clause `tests:` of WAY-339 matches the code on the cost, the times and the share (`STAGES_VALUES`, `audit_count.py:504`) and on the series (`COST_SCRIPT`, `COUNT_PATHS`); the tool-change clause is held by `test_a_changed_stage_script_gives_the_times_the_cost_and_the_share_unknown`.
- Part map `product-guidelines`: the added clause matches `product-guidelines/test_skill_references.py` (`PARTS = ("product-guidelines", "project-level")`, finds a file, a step or a heading that is not there); the file is claimed by `product-guidelines/**`; `Depends on` unchanged.
- Glossary entry *Markdown file* (`foundations/glossary.md:199`) and the invariants `test-method-citation`, `guidelines-file-place`, `audit-series-script-paths`: no sentence of the commit contradicts them; the commit changes none of them. WAY-97, WAY-62, WAY-03, WAY-07, WAY-337 read; the commit touches no sentence of them.
- Trust boundary (handoff: yes): the commit holds no script and no change of code; only comment lines in tests. The code paths the clauses describe (transcript, register, locations file, stage report from git history) were not changed by this commit and were not re-reviewed for crafted input beyond the register behaviour read for finding 1.

## WAY-03: tests named

Changed tests: none altered in behaviour. Tests that hold a sentence of a decision by a new line `decision:` (the request names them, WAY-03): in `process-audit/test_audit_count.py` the tests of `StagesForms` (10), `MechanismMeasures` (3), `GateRunsMeasures` (4), `RegisterCount` (2), `Locations`, `Run`, `Cost`, `Times`, `ProcessVersions` (8), `MeasureVersions` (8), `PriceBoundary`; in `task-cycle/test_cycle_stages.py` `ClaudeFieldsTest.test_a_needed_field_that_is_missing_…` and the five tests of `CacheWriteColumnsTest`, `CodexCacheWriteColumnsTest`, `CacheWritesAcrossScriptsTest`; in `agent-instructions/test_agent_type_copies.py` the two `MissingField` tests. The invariant test `elements/common/test_guidelines_place.py` is listed by the check for `guidelines-file-place` (sentence changed by an earlier commit of the change, test left as it was); the request must name it, saying the sentence now names the suffix `.md`.

## Declined to judge

None set aside.

## Checks

- `python -B elements/common/foundation_check.py`: exit 0, "0 errors", one `listed:` line, for `guidelines-file-place` only; `test-method-citation` is not listed.
- `python -B -c "import ast; ast.parse(...)"` for the three changed test files: exit 0.
- `python -B -m unittest discover -s agent-instructions -p test_agent_type_copies.py`: exit 0 (9 tests).
- `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py -k test_a_needed_field_that_is_missing -k CacheWriteColumnsTest -k CacheWritesAcross`: exit 0 (7 tests).
- `python -B -m unittest discover -s process-audit -p test_audit_count.py -k a_register_lacking_a_field -k test_the_way_without_a_repository_entry`: exit 0 (2 tests). The whole file and the whole gate were not run (WAY-160).
- Manual: compared each sentence of the rewritten *Verification* of WAY-339 and WAY-344 with the code (`audit_count.py` register, stage and locations paths, `COUNT_PATHS`, `STAGES_VALUES`) and the tagged tests; result above.

## Reaches beyond the dispatch

- `elements/decisions/template.md` lines 228-267 and 106-110: the form of the clause `tests:` and of the line `decision:`, to judge the quotations and the clause.
- `process-audit/audit_count.py` (module docstring, `COUNT_PATHS`, `register_table`, `read_register`, `main`) and `process-audit/test_audit_count.py` (tests named above): to compare the clauses with the code.
- `product-guidelines/test_skill_references.py` (head) and `foundations/part_map.md` entries `installation`, `product-guidelines`: to compare the added clause of the part map.

## Working copies

None made. I created the empty directory `.runs/review-return/` at the start and removed it before returning; no worktree or clone.

## Unread material

- The decisions and entries named by the dispatch were each read whole (WAY-339, WAY-344, WAY-337, WAY-03, WAY-07, WAY-97, WAY-62; the glossary entry *Markdown file*; the three invariants; the part map entry `product-guidelines`).
- Not read whole: `process-audit/audit_count.py` (read the docstring head, lines 415-425, 2040-2140 and 3260-3300), `process-audit/test_audit_count.py` (read the diff, and the bodies of the tests at lines 540, 836-860, 1634-1760 by diff context, 2430-2500, 3180-3200, 3918-3965, 3420-3436), `task-cycle/test_cycle_stages.py` and `agent-instructions/test_agent_type_copies.py` (the diff and the tests named). The bodies of most other tests of `ProcessVersions` and `MeasureVersions` were read by name and the comment in the diff, not line by line.
- `task.md`, `spec.md` and `plan.md` were not opened: the dispatch carried no passage of them to judge the return step against beyond the files named, and the return step's report states what it compared.

## Searches not found or unclear

- No test carries a line `decision:` for the sentence of WAY-339 that no change of the instructions of the cycle, the author's included, starts a series of the measures (finding 3a); no test holds that the entry `repository` exception is for that entry alone with a line `decision:` (finding 3b).
- The dispatch names no passage of the task to compare the part-map sentence with; I compared it with the code of `test_skill_references.py` only.
