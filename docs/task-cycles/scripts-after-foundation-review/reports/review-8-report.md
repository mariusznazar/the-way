PASS 6e3ab99a5d540d97fe1755e617a9c66893e960ee

# Review of slice 8 — a cycle that changed the tool that measures gives that tool's measures as unknown

Range `f1d632396d25f47cddf7efee7d4659a2e7e47e7c..6e3ab99a5d540d97fe1755e617a9c66893e960ee` (one commit, `6e3ab99`); `git rev-parse HEAD` is the head. Files: `process-audit/audit_count.py`, `process-audit/test_audit_count.py`. Counts: blocking 0, Minor 1, out of scope 0.

## Findings

### Blocking (Critical / Important)

None.

### Minor

1. **A field missing from the file of a changed tool is dropped silently; the foundation does not say that.** `process-audit/audit_count.py` `withdraw_values` (about l. 2518-2538) clears `cycle.missing` and the `missing_in` pairs of the file whose tool changed, and `note_changed_tools` runs before the `Error:` lines are built in `main` (about l. 3248-3254). So a cycle that changes `task-cycle/cycle_measures.py` and writes a file that lacks a label gives the measures `unknown` with the reason, and the run ends with exit 0.
   - The orchestrator's note says the executor's reading is "as the foundation entries now say it". I read WAY-339 (`foundations/decisions.md:7432-7585`) and WAY-344 (`foundations/decisions.md:2741-2900`), and grep found no sentence in the foundation that says the file of a changed tool is not read. WAY-339 says only "the audit gives the measures of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote them, and its other measures as they stand". WAY-344 says a missing field in a file of the record read from git history ends the run with exit 1 and a line `Error:`, and does not except a changed tool. Both readings fit the words, so this is a choice of the executor, not something the foundation settles.
   - Why Minor and not Important: the reading is reasoned (a file in the intermediate form of a tool that the cycle itself changed would give an `Error:` at every later run, and WAY-344's rationale calls an exit code that every run gives a signal-less one); the loss is limited to the one cycle that changed the tool, since the next cycle's file is read and its missing field shows; the values are `unknown` either way, so no figure is wrong; and one test pins it (`MechanismMeasures.test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run`), and the module description says it (`audit_count.py:222-223`, "The file of a changed tool is not read for the cycle, so no field of it is missing").
   - Price if left: the very cycle whose change may have broken a tool's output form gives no `Error:` for it. Price if reversed (keep the `Error:` for the missing field): such a cycle's `Error:` line stays in every later run, since a copy in git history cannot be mended.
   - Recommendation: the orchestrator confirms the reading and has it written in the sentence of WAY-339 (or the "complies" list of WAY-344) that the next foundation step touches, so the code and the entry say the same. Nothing for the executor to change.

## Declined to judge

- A merge of the target branch into the task branch makes the diff between the version the cycle ran on and its last copy include another task's change of a tool (executor's choice 6). The slice names this commit (`git diff --quiet` between the version and the last copy), and the result is `unknown` with a reason that names the two commits' meaning accurately ("changed between the version it ran on and the last copy of its record"), not a wrong figure; narrowing it needs the base of the cycle's branch, which the audit does not read. Set aside as the task's own design.
- Three `git diff --quiet` calls per cycle of the-way, with no cache: cost in run time only, outside the task.
- Lines of 101 characters (l. 485 is new); the files already hold such lines in many places and no rule of the foundation sets a length I found.

## Review against the task and the foundation

- To do 8 and Settlements row 4 (`task.md:35`, `:146`): met. `TOOL_GROUPS` is built from `COST_SCRIPTS`, `MEASURES_SCRIPT` and `GATE_SCRIPTS` (the constants Slice 6 uses for series), not a second list. The change is found by `Ancestry.differs` (`git diff --quiet`, a failure counting as changed) between `ancestry.commit(cycle.pin)` and `cycle.later[-1]` or `cycle.record`, the commit `fill` reads the values from (`commits[-1]` of `read_repository`). The three groups give: times, cost and share of cost in fix rounds unknown from `stages.md`; `Mechanism measures` and each label unknown; `Gate runs` unknown. The number of fix rounds stands (it comes from the record). The other values stand under the version the cycle ran on (`ProcessVersions` and `MeasureVersions` tests show the cycle stays in its version and series, only its value is out of the median).
- Cycles of other repositories: only `read.key == THE_WAY` is checked; `read_repository` for that key reads the same checkout `Ancestry` reads (`repositories` / `the_way_checkout`), so both commits lie in one history. Earlier copies: a group is checked only where the copy held the file (`cycle.held`, a text that was read), so a copy with no `mechanism_measures.md` or `gate_times.md` keeps its own reason; a pin that does not resolve leaves the cycle as it is. Each is pinned by a test.
- To do 9 (`task.md:36`): the comment at `MEASURES_FILE` now reads "A copy that holds neither is of an earlier cycle or of one whose script failed." and the module description says the same words (`audit_count.py`, in the paragraph on `mechanism_measures.md`).
- Foundation: WAY-339 text for this behaviour is met by the code; WAY-350 untouched (the median over runs alone uses `gate_timed`, which is emptied for a changed tool); `audit-series-script-paths` still holds (`test_audit_series_scripts.py` ran OK; the new list reuses the constants it checks). script-language, script-imports, script-subprocesses: the change adds no import and starts only `git diff --quiet` through the existing `Git`/`Ancestry` (no new program). WAY-344: see the Minor finding.
- Trust boundary (answer yes): the text of the input reaches the new code as `cycle.pin` (matched by `SHORT_HASH`, resolved to a full hash by `rev-parse --disambiguate` before any diff; a crafted pin gives None and the cycle is left) and commit hashes from git output; the paths are constants; the reason string is built from constants only, so no text of a record reaches the result; no path of the input is followed and nothing is written outside the result; no option can be injected into `git diff` (hex hashes and paths after `--`). The new code cannot raise on a crafted record: `commit` returns None on every failure and `differs` catches `GitError`. A scratch input of a pin that does not resolve is covered by `test_a_cycle_of_the_way_whose_pin_does_not_resolve_is_not_put_in_doubt`.
- Tests: do they fail when the behaviour breaks? I ran the head's tests against the base `audit_count.py` in a working copy: the new tests of `Times`, `MechanismMeasures`, `GateRunsMeasures`, `ProcessVersions` and `MeasureVersions` fail on the base (17 failures in that run; the 7 of `test_each_path_that_starts_a_series_is_a_path_git_tracks` fail only because the working copy is no git checkout, not because of the change). Their expected values are worked out by hand (0:20:00, 0:05:00, 0.000300, 12 calls, 100.000 seconds), not computed by the code. Guards (no change, product's cycle, earlier-form copy, unresolved pin, corrected copy judged by its last copy) are present for each group.
- WAY-03: no test holding a sentence of a decision (a line `decision:`) and no invariant test was changed or added; `test_audit_series_scripts.py` is untouched. Nothing to name.
- Own-work check of the executor (the requirement most likely unmet is "a cycle of another repository and a copy of an earlier cycle are not put in doubt"): it fits the weakest place, and its three mutations are covered by named tests that I confirmed exist and that fail on the base or are guards that pass on it by design.

## Checks run

- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MechanismMeasures -k GateRunsMeasures -k Times -k ProcessVersions -k MeasureVersions` on the head: exit 0, `Ran 77 tests ... OK`.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` on the head (run by me, after the executor's renames): exit 0, `Ran 226 tests ... OK`.
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: exit 0, `Ran 3 tests ... OK`.
- Same focused command with the base `audit_count.py` and the head's tests in a working copy: `FAILED (failures=17)`, all for the expected reason as listed above (the 7 failures of `test_each_path_that_starts_a_series_is_a_path_git_tracks` come from the copy having no `.git`).
- No run of the whole gate (WAY-160). Not run: a scratch run of the command on a real register and real history (outside the slice's checks).

## Reaches beyond the dispatch

- `foundations/decisions.md:2741-2900` WAY-344, whole: the dispatch names WAY-339 and WAY-350 but the orchestrator's note asks for a judgement against WAY-344; read to judge the missing-field reading.
- Grep of `foundations/*.md` for "changed the tool" / "changes a tool that measures" / "not read for": to find whether any entry says the file of a changed tool is not read; found only WAY-339 sentences quoted above.
- `process-audit/audit_count.py` around `Cycle`, `fill`, `add_cost`, `read_measures`, `read_gate`, `read_repository`, `Ancestry`, `main` and `repositories`, to follow what the new code touches.

## Working copies

`.runs/review-8/` of the worktree held the output of the whole-file run and a copy of `process-audit`, `task-cycle`, `elements` and `gate` with the base `audit_count.py` for the red check; the directory was removed before this report was finished. No other copy, worktree or clone. The reviewed worktree, its index and branch are unchanged.

## Unread material

none. (Dispatch passages read whole: handoff, `task-cycle/review/SKILL.md`, `task.md` lines 30-40, 68-76, 130-135, 144-148, WAY-339, WAY-350, WAY-344, the invariants `audit-series-script-paths`, `script-language`, `script-imports`, `script-subprocesses`, the part-map entries `task-cycle` and `process-audit`, the diff of the range and the executor's report. `spec.md` and `plan.md` were not opened: the handoff copies the slice whole and names no passage of them to read. `audit_count.py` and `test_audit_count.py` were read where the diff and its callers reach, not whole.)

## Searches not found or unclear

- The orchestrator's note says the foundation entries "now say" that the file of a changed tool is not read for the cycle; I did not find that in WAY-339, WAY-344 or elsewhere in `foundations/` (see the Minor finding). Line numbers the handoff gives for WAY-339 (`decisions.md:7384-7469`) differ from the current ones (`7432-7585`); the entry named matched.
