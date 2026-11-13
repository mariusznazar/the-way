# Slice 3 report — The script that runs the gate and records its times

**Status:** done

**Branch:** `task/audit-numbers-mechanism-measures`, worktree `the task's worktree`

**Commits** (base `036d24a` to head `7916a21`):
- `54d9232` Add the script that runs the gate and records its times
- `7916a21` Pass the made-up gate's code in arguments so the cross-part check can read it

**Files changed:**

| File | Added | Removed |
|---|---|---|
| `task-cycle/gate_times.py` (new) | 299 | 0 |
| `task-cycle/test_gate_times.py` (new) | 276 | 0 |

Only these two files are in the slice. Both were added by path; nothing else in the worktree was staged. The worktree is clean after the second commit.

## Checks

Each command was run from the worktree root. The product's gate (`gate/run_tests.py`) was not run.

| Check | Command | Exit code |
|---|---|---|
| Test-first run, script still empty (failed on assertions) | `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` | 1 (failures=8, errors=9) |
| Slice's tests, final | `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` | 0 (17 tests, OK) |
| Private paths, after the slice's commits | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 (OK) |
| Cross-part imports | `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` | 0 (39 tests, OK) |

Notes on the runs:
- The "fails on the base" check was done with the script present as an empty file, so the tests reach their assertions. This is the rule in `make-change` section 2. I did not run the tests with the script absent.
- The cross-part check first failed at `54d9232` with exit 1. It flagged six `-c` command lines in my test file whose code was passed as a variable. It passed (exit 0) after `7916a21`, which moves the dynamic values into the arguments and keeps each command's code a literal.
- No mismatch with the handoff's checks. The handoff named the private-paths test to run after the slice's commit; it was run after both commits.

## Own-work check (make-change section 3)

- **Requirement:** other gate runs are counted only where their interval met this run's, and the run's own entry is never counted; an unusable registry gives `unknown` with the gate still run.
- **Check:** `test_other_runs_counted_from_the_registry` (stale, old, ended-before, running, other-form, and a run that ended inside this run, plus the renamed own entry) and `test_unusable_registry_gives_unknown_and_the_gate_still_runs`.
- **Result:** both pass. Mutation: removing the own-token exclusion in `count_others` made 3 tests fail (exit 1). The committed script was restored with `git checkout` and the tests pass again (exit 0).
- **Large-line check (manual, not in the test suite):** a 3 MB line with no newline, followed by two blocks. Stdout was byte-identical to the command's output, the record was written, and the `Ran` line after the long block still gave its time. The long directory cell is cut at 1 MiB, which is the bound on memory the script keeps.

## Reaches beyond the handoff

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`: read whole, as the handoff's method names them.
- `task-cycle/cycle_measures.py`: read whole, as a pattern (handoff note 2). `task-cycle/test_cycle_measures.py`: read only its first 120 lines, as a pattern.
- `elements/part-map/test_cross_part_imports.py`: searched for the message `runs code the check cannot read` to understand the failure, then read the matching sections, not the whole file.
- `the author's rules file on git`: read before the commits, as the user's global instructions require. It asks for commit messages in English and for `git add` by path, both followed.
- `git` guard note: a scratch folder was left in the user's temp directory (`a scratch folder in the system temporary directory`, from the large-line check). A cleanup command on it was blocked by the sandbox guard because it lies outside the project. It is harmless and can be removed by hand.

## Unread material

- `task.md` passages: read through the copies in the handoff only; the file itself was not opened.
- `foundations/part_map.md` trust-boundary entry of `task-cycle` and the `python-stdlib-modules` invariant (which `script-imports` rests on): not read.
- All other named material was read: the handoff's `Read` list (`decisions.md` WAY-160, WAY-344, WAY-328, WAY-38, WAY-349, WAY-350; invariants `script-imports`, `script-subprocesses`, `cross-part-imports`, `tracked-file-private-paths`; part-map entries `task-cycle`, `gate`, `test-runner-command`; glossary `gate`) and `gate/run_tests.py` in full.

## Searches not found or unclear

- **Scope of trust boundary:** `foundations/part_map.md` names `task-cycle/cycle_stages.py` and `task-cycle/cycle_measures.py` as the trust boundary of `task-cycle`, not `task-cycle/gate_times.py`. The script reads the gate's output, which can carry bars and control characters that reach a table cell; `cell()` replaces them. Whether the script belongs in the trust boundary is for the cycle's foundation step, not this slice. Not changed.
- **"Ago" reference for running entries:** the spec says a running entry counts when it "started ... no more than six hours ago", without naming the reference time. I used the run's end time.
- **Signal exits:** the spec says the exit code is the command's own, which is not defined for a command killed by a signal. I chose 128 plus the signal number.

## Choices made

- **Ago reference:** running entries count when they started no more than six hours before this run ended. Rejected: six hours before this run started. Cost if wrong: a running entry from just before the six-hour mark could be counted or not, a difference only at the edge of six hours.
- **Output file pre-check:** the script creates an empty `--output` file before the command starts, to prove it can be appended to. Rejected: checking only the parent directory, which misses a path that is a folder. Cost: an empty file is left behind if the command never starts. The heading is written on the first real run because the file is then empty.
- **Own entry creation failure:** if the run's own entry in the registry cannot be created, a `Warning:` is written and the count of others is still computed. Rejected: calling the count `unknown`. Cost: other runs may not see this run for the duration of its run.
- **Command start failure:** the run's own registry entry is removed, then `Error: gate_times.py: cannot start ...` and exit 2. Cost: none known.
- **Line bound:** an unfinished line is kept for reading the times only up to 1 MiB; a longer line is cut. Rejected: no bound, which would let a long line grow memory without limit. Cost: a directory name longer than 1 MiB is cut in its cell.
- **Signal exit code:** 128 plus the signal number. Rejected: the negative return code, which is not a valid exit status. Cost: none known.
- **Home directory failure:** if `Path.home()` cannot be determined, a `Warning:` is written and the count is `unknown`; the gate still runs.
- **Test commands:** the made-up gate commands take the output and paths as arguments and keep their code literal, because the cross-part check cannot read code passed as a variable. Rejected: passing the code as a variable, which fails that check. Cost: none known.
- **Rename of own entry:** on the run's end, the own file is renamed with `os.replace`. A failed rename gives a `Warning:` and leaves a running entry that counts for other runs for up to six hours. Rejected: deleting the entry, which would hide the run. Cost: a phantom running entry until it is deleted.
