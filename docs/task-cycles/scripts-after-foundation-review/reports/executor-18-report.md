# Report — executor of slice 18 (the audit count on the real register of problems)

**Status:** done (no code changed; nothing was wrong or empty where the count should give it; one fact the orchestrator may want to judge is under "Problems as observed")

## Files changed and commits

None. `process-audit/audit_count.py` and `process-audit/test_audit_count.py` are unchanged. No commit.

## The run (counts and facts only)

- Command: `python -B process-audit/audit_count.py --locations <copy of the user's locations file>` with the copy's entry `audit_results` under `the-way` pointing to a directory under `.runs/executor-18/` of this worktree. Everything else of the copy is the user's file as it stands. The user's locations file, the register of problems and the repositories were only read. The count did not refuse the result directory (it lies in no checkout it reads). Exit code **0**, stderr empty, **0 `Error:` lines** on stderr and 0 in the result.
- The result (`count-<date>.md` and `count-latest.md`): 4332 lines. Two repositories read, both `yes`; 182 cycles (101 and 81); 182 rows in *Cost* and in *Mechanism measures*; 59 gate runs; 629 rows in *Problems by cycle*; 33 fixed, 9 open and 16 dropped issues; 58 rows in *Cost of an occurrence by issue*. No row of any of these tables has every value `unknown`.
- *Unknown values*, first table (values of cycles that the count did not establish, one row for each cycle and value): **1605 rows**. Rows for each kind: Fix rounds share 277, Discarded attempt 177, Mechanism measures 157, Gate runs 157, Working time without waiting for tools 135, Waiting for tools 135, Remarks 56, Plan 30, Slices returned too large 18, Cost 10, Process pin 4: together 1156 rows. The other 449 rows are of other values: per-version rows of two fields of the issues (named "contradiction only after code, version ..." and "slices too large, version ..."), and 2 rows of the gate directories (`Gate runs: Directory seconds`, `Gate runs: Directories`); I did not count the 449 further.
- *Unknown values*, second table (the values the register holds back, one line for each field and reason, WAY-330 and the change of Slice 9): **0 rows** — the register read without a refused row, a refused table or a problem of a cycle not read.
- *Mechanism measures*: 25 of the 182 cycles have measures (22 and 3 by repository), each with all values known; the other 157 are `unknown` as a row, with the reason in *Unknown values*. **The measures of a Codex cycle and of the nested Claude Code helper are not present, because the register's repositories hold no such cycle**: of the 29 copies of `mechanism_measures.md` and the 174 copies of `stages.md` in the history of the two repositories (last copy of each), none names Codex or a model of OpenAI (searched by `codex`, `gpt`, `o3`, `o4`, case-insensitively). So the count had no Codex cycle to count; the real Codex cycle's measures are the business of `task-cycle/cycle_measures.py` on a session, not of this run.

## Own-work check (section 3)

- Requirement most likely unmet: a result that is wrong or empty where the count should give it (To do 11), notably the register's side — problems and issues empty, the second table of *Unknown values* swallowing values, a stack trace from real data.
- Check: the tables above counted by a script on the result (rows per section, rows with every value `unknown`, the two tables of *Unknown values*), the `Error:` lines in stderr and result, and the exit code.
- Showed: every section filled, no all-`unknown` row, no `Error:` line, exit 0. Nothing to fix, so no test was written first.

## Other checks

- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: the first command ran past the 120-second foreground timeout and was moved to the background by the harness; see the last section for its result. They check the unchanged files of the base of this slice.

## Choices and reaches beyond the handoff

- I read the Codex and OpenAI traces in the repositories' history (read-only `git log` and `git show` of the copies of `mechanism_measures.md`, `stages.md` and `cycle.md`) to answer whether a Codex cycle exists in the register's repositories; the handoff names no other way. Rejected: reporting "present" or "absent" from the `Mechanism measures` table alone, which carries no agent column. Cost if wrong: the answer "no Codex cycle" would be false only if a Codex cycle names none of the four words in any copy.
- I did not touch `foundation_check.py` or WAY-344 (the parallel task).

## Problems as observed

- *Unknown values* has 1605 lines on the real register although the register's own side (the second table, where Slice 9 gives one line for each field and reason) has 0. The 1605 are the first table, which Slice 9's later commit keeps at one row for each cycle and value (the commit "Keep the unknown pins and per-issue values of the audit count in the first table"; the module text: "a table of each value given as `unknown` and why"). The task's To do 10 speaks of "values of the register"; the cycle-record values stay one row each by that commit. The 1605 is greater than the "about 830" of the template because the real repositories hold 182 cycles, mostly of earlier forms. Whether To do 10 means this first table too is for the orchestrator to judge; I changed nothing.

## Unread material

The plan and task beyond the passages the handoff copied (not named by my *Read*), and the whole of `foundations/decisions.md` and `invariants.md` beyond the ranges the handoff names; I read the ranges named (WAY-330, WAY-320, script-language, script-imports, script-subprocesses, process-audit) whole and the module text of `process-audit/audit_count.py` lines 1-310 and 436-450 (part of a 3293-line file, not changed).

## Searches not found or unclear

- A Codex cycle or a nested-helper cycle in the register's repositories: not found (see above).
- `foundations/decisions.md:7309-7341` and `:7183-7253` of the plan's *Read* were read at the current ranges named by the handoff; no mismatch.

## Working copies

`.runs/executor-18/` of the worktree held the copy of the locations file, the result directory, stdout and stderr; it was removed before the report was finished, and nothing else was made. No log was kept.

## Test results of the focused checks

- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`: 228 tests OK, exit 0 (287 s, run in the background by the harness).
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: 3 tests OK, exit 0.
- No whole-gate run (WAY-160).
