# Report — executor-11, slice 11 (four over-long functions at three parts' trust boundaries divided)

## Status

`done`

## Commits (range from base `462add5d612623e09c0137d6b2b923d748661c38`)

- `612146a2` Divide run of the installer into the steps that show the plan, apply the submodule and write the files — `installation/install.py`
- `72150951` Divide check_file of the instruction check into the check of dead paths, of @ imports and of emphasis — `instruction-files/check_instructions.py`
- `679112e3` Divide check_header of the plan check and provenance and task_report of the plan state into named steps — `project-level/plan_check.py`, `project-level/plan_state.py`

Files changed (`git diff --stat 462add5d..HEAD`): `installation/install.py` 147 lines changed,
`instruction-files/check_instructions.py` 39, `project-level/plan_check.py` 90, `project-level/plan_state.py` 487;
total 456 insertions, 307 deletions. All files are LF, as they were. No other file was touched.

## What was divided, and how

Every function of the slice now stands well under 110 lines (counted with `function_sizes` of
`agent-instructions/test_size_invariant.py`). No function of the four files is over 110; the largest are
`plan` 109 (`install.py`, not in the slice, unchanged), `check_layout` 88, `read_tasks` 89, `observe` 63.

| Before | Lines | After | Parts moved out, each with a name of its own |
|---|---|---|---|
| `install.run` | 149 | 58 | `print_submodule_actions`, `print_file_actions`, `print_stale_deletions`, `print_shared_actions` (what the preview prints, in the same order), `apply_submodule` (add, initialize, move the submodule), `write_files` (write, delete, write the shared files) |
| `check_instructions.check_file` | 137 | 23 | `check_dead_paths`, `check_at_imports`, `check_emphasis` |
| `plan_check.check_header` | 123 | 69 | `check_status` (the `Status:` line), `check_fingerprints` (the fingerprint against the approval record and the text) |
| `plan_state.provenance` | 130 | 23 | `record_provenance` (one record), `anchored_parents`, `relation_problem`, `frozen_artifact_problem` |
| `plan_state.task_report` | 140 | 60 | `archived_cycles` (the commits that touch the archive directory), `report_verdict` (conflicts, proposals, unchecked lines), and a small dataclass `TaskEvidence` |

Choices made (with the way rejected and the cost if wrong):

1. **`TaskEvidence` dataclass in `plan_state.py`.** `task_report` kept seven lists that the moved parts
   append to, and on a `GitError` in the middle the lists keep what they hold so far (the report prints it).
   Helpers that returned new lists would drop that partial state. Rejected: passing the lists one by one
   (10 parameters for `archived_cycles`) and returning values (changes what a failed run prints). Cost if
   wrong: one extra small type in a file the guideline marks `do not copy`; behaviour is the same, as the
   73-run comparison below shows.
2. **Results of the `provenance` steps as `(kind, message)` pairs** with kind `"skip"`, `"owned"`,
   `"unresolved"` or `"foreign"`, so the loop of `provenance` sorts a record into the same three lists as
   before, in the same order. Rejected: raising an exception per problem (a new control path at a trust
   boundary).
3. **`check_emphasis` has its own pass over `prose_lines`**, where the old loop counted emphasis in the same
   pass as the `@` imports. The findings keep their order (all `@` import findings, then emphasis, then
   size), checked by the comparison below. Rejected: returning the emphasised lines from
   `check_at_imports` (couples two checks to keep one loop).
4. `run` of the installer: the preview is split into four printing functions in the old order, and the
   confirmation, the "already installed" exit and the warnings stay in `run`. The two fetch-and-checkout
   blocks of the pin (the add and the move) are kept as they were inside `apply_submodule`, not merged,
   so that no condition of the old code is rewritten.

## Checks (command, exit code)

- `<ruff> format --check --config ruff.toml installation/install.py instruction-files/check_instructions.py project-level/plan_check.py project-level/plan_state.py` — exit 0 ("4 files already formatted"). (`plan_state.py` was reformatted once by `<ruff> format --config ruff.toml` after the edit, as Slice 3 gives; the other three were unchanged by it.)
- `<ruff> check --config ruff.toml --ignore-noqa` on the same four files — exit 0 ("All checks passed!").
- The counting of `function_sizes` on the four files — no function over 110 (largest 109, `install.py plan`, outside the slice and unchanged).
- `python -B gate/run_tests.py installation` — exit 0, 73 tests OK (464 s). Output: `reports/executor-11-differential/t_install.txt`.
- `python -B gate/run_tests.py instruction-files` — exit 0, 105 tests OK, 5 skipped (the skips say "no FIFO on this platform" and "needs the real path of a link, as on POSIX": platform skips, the same on the base). `t_instr.txt`.
- `python -B gate/run_tests.py project-level` — exit 0, 281 tests OK (159 s). `t_proj.txt`.
- Not run, on purpose: the full gate (`python -B gate/run_tests.py` without a directory), as the handoff says.

All test runs and the differential runs started after the last edit of the four files; the commits hold exactly the files that were tested (`git status` clean after the commits).

## Trust boundary: same verdict, exit code and message before and after

Method: the base version of every file (`git archive HEAD` of the base into a working copy) was run next to
the changed one on the same crafted input, and the outputs, exit codes and (where it applies) the result files
were compared. The scripts stand in `reports/executor-11-differential/` (they refer to the working copy
`.runs/executor-11/`, removed now).

- `project-level/plan_state.py` (`record_ps.py`): the 44 tests of `test_plan_state.py` start the script as a
  process 73 times, on disposable Git repositories with crafted records (foreign source, duplicate
  provenance, frozen copy absent or different, non-ASCII paths, shallow clone, failed fetch, timeout...). The
  exit code, stdout and stderr of each of the 73 runs, with commit hashes and temporary paths normalised,
  are byte for byte the same for the base and the changed script: `plan_state_cli_old.json` and
  `plan_state_cli_new.json` (`cmp` equal).
- `project-level/plan_check.py` (`diff_pc.py`): `check()` of the base and of the changed module on 1795
  inputs — the test suite's valid plan and definition, each line of the plan and of the definition deleted or
  doubled, every `Status:` variant (including a date that is no calendar date and a missing line), the
  fingerprint swapped for others, the approval record's fingerprint changed, a definition with a draft status,
  and 1500 random one-to-three-character mutations. 1291 distinct finding lists came out; 0 differences.
- `instruction-files/check_instructions.py` (`diff_ci.py`): `check()` on 400 random trees (root and nested
  `AGENTS.md`/`CLAUDE.md`, skills in two directories, Cursor rules, dead paths, network-shaped paths, `@`
  imports with and without a trailing mark, emphasis words in and out of fences, sentences saying a file does
  not load in English and Polish, pointed files, `--file` extras), a root of `None`, a file with a UTF-16 BOM,
  one with a UTF-8 BOM and one over the size limit, the worktree and the repository above it; and the command
  line (exit code, stdout, stderr) for a tree, a missing root, `--file`, a network root and no argument:
  410 cases, 0 differences.
- `installation/install.py` (`diff_install.py`, `diff_move.py`): the base and the changed script run on fresh
  product repositories — five calls each (preview, `--apply` answered `n`, `--apply` answered `y`, the same
  again, preview again) with the files of the product compared after each call — for a fresh product, one with
  its own CRLF `AGENTS.md`, `.gitignore` and a `CLAUDE.md` without the import, one that ignores `.the-way`, one
  with stale entry points, stale agent definitions and `AGENTS.override.md`, and one with a broken marker pair
  in `AGENTS.md`; plus a missing target directory, a URL with credentials, and a pin moved from an older
  commit with an untracked file in the submodule. Exit codes, stdout, stderr and the product files are the same
  in every case (exit codes 0, 0, 0, 0, 0 for the working installs and 1 for the two refusals).

## Own-work check (WAY-164)

- Requirement most likely not met: "no change of behaviour, exit codes or messages" at four trust boundaries
  (`task.md:32` and the Goal of the slice), where the likeliest break is an order of output or findings, a
  `continue` that became a `return`, or the partial state of a failed run in `task_report`.
- Check: the differential runs above, built to hit exactly these: output order (`install.run` preview,
  `check_file` findings), the three result lists of `provenance` (the 73 CLI runs include foreign, unresolved
  and owned records), and an error in the middle of `task_report` (the tests of a failed fetch, a shallow clone
  and a Git timeout are among the 73).
- What it showed: 0 differences in every comparison (counts above).
- Weakest point checked: `task_report`'s state on a Git error. A `GitError` in `archived_cycles` leaves in
  `TaskEvidence` what was collected before it, as the old local lists did, and `merged` is reset after it. The
  tests that make Git fail (failed fetch, timeout, shallow clone) give the same output on base and change. What I did not
  test directly: a `GitError` raised in the middle of the archived loop after a first commit was already
  accepted — the 73 runs hold no such case, so that single path rests on reading the code (the lists are the
  same objects, mutated in the same order).

## Mutation of the code in my head

A `continue` of the old `provenance` loop that I mapped to the wrong result would drop a record into the
wrong list or skip it; the CLI comparison has foreign, unresolved, owned and skipped records. A swapped
order of `check_at_imports` and `check_emphasis` would show only between findings of the same level, file and
line (the print sorts stably), which the 410 cases compare as lists in order. An emphasis counted over lines
the `@` loop skipped with `continue` would differ in a fenced block or on an `@AGENTS.md` line; both appear in
the seeds.

## Behaviour a user sees in the running product

None changed: the four scripts print and exit as before (compared above), so no walk of `walkthrough.md`.

## Reaches beyond the dispatch

None. `slice.md` of `task-cycle/change/` was read as `SKILL.md` section 1 says for a slice.

## Plan against code

No mismatch. The handoff's line numbers matched the code (`run` 650, `check_file` 538, `check_header` 191,
`provenance` 281, `task_report` 413).

## Problems

None observed.

## Unread material

- `foundations/part_map.md:81-100` and `183-203` (the part map for project-level, instruction-files,
  installation): not read. The trust boundary files were named in the handoff, so I did not need the map.
- `foundations/invariants.md` ranges for `installation-paths-through-links`,
  `check-instructions-refuses-outside-links`, `project-plan-form`, `project-plan-state-evidence`,
  `function-and-file-size`: read in full by the line ranges the handoff gives.
- `foundations/decisions.md` WAY-365, WAY-48, WAY-385: read whole. F2 = WAY-385 read whole.
- `task.md:32` and `task.md:62-68`: read as lines (the line at 32 and the Questions block).
- `guidelines/coding.md`, `coding-check.md`, `coding-measuring-report.md`, `coding-repository-changer.md`,
  `agent-instructions/test_size_invariant.py`: read whole.
- Each of the four changed files: read whole before the change.

## Searches not found or unclear

None. (`fingerprint` module of the base working copy was missing in my first, partial `git archive`; I
re-made the copy from the whole base tree. A harness error, not a finding about the code.)

## Working copies and their removal

- `.runs/executor-11/` (scripts, the base working copy `old/` made by `git archive HEAD`, the product
  repositories of the installer comparison, the temporary `ci_root`): removed whole at the end;
  `ls .runs/executor-11` says it does not exist.
- `installation/install_old.py` (the base installer copied beside the new one for the comparison): created
  and deleted in the same step; it never entered a commit (`git status` clean).
- Kept in `reports/executor-11-differential/`: the comparison scripts, the two normalised result files of the
  `plan_state` runs and the three test outputs.
- No git worktree was made.
