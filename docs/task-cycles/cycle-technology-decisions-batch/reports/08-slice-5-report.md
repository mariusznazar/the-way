# Slice 5 report: the installer test no longer depends on the commit current when it runs

**Status:** done

**Commit:** `815294c` on `task/cycle-technology-decisions-batch` (one commit, `installation/test_install.py` only, staged by path)

**Files changed:** `installation/test_install.py`, 17 lines added, 11 removed (measured against the pre-commit diff).

## What was wrong

`InstallTest.setUp` read `self.commit` from the live the-way repository's head (line 39). Tests compare against that value after installing, but the installer pins the live head itself when it runs (`installation/install.py:496`, `rev-parse HEAD` of `SOURCE`). A commit made to the-way between `setUp` and the install therefore made the pinned commit differ from the expected one. In `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` the failure was at the `MOVE .the-way from {self.commit}` assertion (line 216 before the fix).

Reading the pin at each install point does not fix this for `installed_from_a_remote`. The installer runs from the live checkout and verifies the commit against the remote (`verify_remote`, `install.py:327-336`). A commit made after the remote was cloned makes the pin absent from the remote, and the install is refused. So the fix needs a fixed source for the whole test, not a later read.

## Change

- `setUp` clones the-way into `<temporary>/source` and takes `self.commit` from that clone's head. Every test installs from this clone (`self.installer`, `--url self.source`), so the pin and the expected commit cannot move during the test.
- `installed_from_a_remote` clones the bare remote from `self.source` and installs with `self.installer`.
- `later_process` clones the remote from `self.source` and copies the installer from `self.installer`, not from the live working tree. Its `moved` value already came from its own clone; that is unchanged.
- `test_moving_the_pin_...`'s back-run uses `self.installer`, so it pins the clone's head as the expected `self.commit` requires.
- `test_preview_apply_rerun_and_preserve_foundation` reads the README from `self.source`.
- `test_guidance_names_only_scripts_the_pinned_commit_holds` runs its `cat-file` in `self.source`.
- Removed the now-unused module constant `INSTALL`.
- Assertions at (now) lines 216 and 228 and every other `self.commit` use are unchanged in text; they now compare with the clone's commit.
- `installation/install.py` is not touched; installer behaviour is unchanged.

## Choice made and its cost

- **Chosen:** a clone made in `setUp`, with the expected commit read from it. The clone is what the test installs from, and it cannot move.
- **Rejected:** reading the pin after each install. It cannot fix `installed_from_a_remote` (see above), and it does not cover the back-run or the guidance test.
- **Cost if wrong:** the tests now run the installer and the scripts from the committed head of the worktree, not from uncommitted edits to `installation/install.py` in the working tree (previously the live file was used). Each test adds one local clone of the-way, which took about 3.5 s per test on this machine.

## Showing the failure before the fix

Throwaway clone at `a scratch file outside the repository` (the unmodified test file). A line `command('git', ..., 'commit', '--allow-empty', ..., cwd=SOURCE)` was inserted as the first line of `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink`, so a commit lands between `setUp` and the install.

- Before the fix: `python -B -m unittest discover -s installation -p "test_install.py" -k test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` exited 1. Message: expected `MOVE .the-way from 491f048c…` (the `setUp` read), found `MOVE .the-way from 0a888798…` (the injected commit that was pinned).
- After the fix, same injection in `a scratch file outside the repository` (the fixed test file copied in): same command exited 0, 1 test OK.

The live repository was not changed by the demonstration.

## Own-work check (section 3)

- **Requirement:** the expected commit comes from what the test installs from, and a commit made to the-way during the run does not change it.
- **Check:** the injected-commit runs above, before and after the fix.
- **Showed:** failure before (exit 1, wrong expected commit); pass after (exit 0).

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Slice check 1 | `python -B -m unittest discover -s installation -p "test_install.py"` | 0 | 30 tests, OK (about 104 s) |
| Slice check 2 | `python -B -m unittest discover -s installation -p "test_installed_guidance.py"` | 0 | 4 tests, OK |
| Slice check 3 | `git diff --check` | 0 | clean |
| Failure reproduction (before fix) | `python -B -m unittest discover -s installation -p "test_install.py" -k test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` in `before-fix` clone with injected commit | 1 | AssertionError as described above |
| Fix check (after fix) | same command in `after-fix` clone with injected commit | 0 | OK |

Not run: the full `python -B gate/run_tests.py`, which the handoff forbids for this slice. The other installer test files (`test_coding_guidelines_installation.py`, `test_lead_installation.py`) were not run; they are out of this slice's scope.

## Reaches beyond the handoff

- `installation/install.py` lines 16, 83-125, 327-336 and 496: read to find where the pinned commit comes from and why `verify_remote` refuses a commit missing from the remote. This is why the fix uses one fixed clone rather than a later read.
- `a document in the author's private notes`: read before the commit, as the user's rules require. Commit added by explicit path.

## Handoff passages and drift

- The task's cited places `:39`, `:145-149`, `:216`, `:228` matched the current file by content: `setUp` line 39 and the other places named by their content are as described above; `:216` and `:228` are the assertions of the moving test.
- The installation README (`installation/README.md:78-116`), invariant `installation-claude-guidance` (`foundations/invariants.md:291-299`), part `installation` (`foundations/part_map.md:157-165`) and WAY-34 (`foundations/decisions.md:905-943`) were read. Nothing in them needed changing for this test change: the installer's behaviour and the invariant's text are unchanged.

## Searches not found or unclear

- The same pattern (a `self.commit` read from the live repository in `setUp`, compared with an install from the live repository) appears in `installation/test_coding_guidelines_installation.py:32` and `installation/test_lead_installation.py:32`. Not changed: out of this slice's file. Not run, so it is unverified whether they fail under a concurrent commit. Flagged for the orchestrator to decide.
- Nothing else unclear.
