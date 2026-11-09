# Report — the return step (resumed one author)

Saved by the orchestrator from the author's returned text; the author's Write tool refused the file
and the author did not work around it. The words below are the author's.

Return step: I corrected one thing and committed it as `2984b5f` on `task/locations-file`; the worktree is clean.

**Status:** done
**Check result:** `foundation_check.py` (0 errors), `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py elements/common` all exit 0. The full gate was not run; it is the cycle's.

## The correction
The invariant `tracked-file-private-paths` derives from WAY-309, but WAY-309's *Verification* did not name it. The decisions template asks a decision to name the invariants that derive from it. WAY-309's *Verification* now begins "invariants: tracked-file-private-paths". Only that field changed. Its binding sentences, *Rationale* and *Rejected* are untouched.

## Return-step record
- **Foundation compared with code:**
  - **Compared:** WAY-27, WAY-107 and WAY-320; WAY-308, WAY-309, WAY-140 and WAY-61; the invariants `outbound-link-reach` and `tracked-file-private-paths`; the part map for `project-level`, `task-cycle`, `foundation-review`, `product-guidelines` and `agent-instructions`.
  - **Only mismatch:** the WAY-309 *Verification* above, corrected.
  - **Match, no change:**
    - `task-cycle/test_tracked_files_private_paths.py` and `project-level/backlog_place.md` fall under the existing `task-cycle/**` and `project-level/**` globs.
    - The new dependencies are allowed: foundation-review, product-guidelines and task-cycle may depend on project-level.
    - The exempt files in the invariant's sentence equal the list in the test; a test checks this and passes.
    - `AGENTS.md` and the skill pointers agree with WAY-27, WAY-107 and WAY-320.
    - WAY-140 and WAY-308 still read correctly.
- **Decisions written or changed:** the earlier commits wrote WAY-320 and edited WAY-27 and WAY-107. This step edited WAY-309's *Verification* field.
- **Invariants written or changed:** none in this step. Earlier: `tracked-file-private-paths` (new) and `outbound-link-reach` (edited), set by rows 1–3 of the task.
- **Environment facts:** none. The change rests on no outside source that the foundation lacks.
- **Glossary terms:** none. No word takes a new meaning, and the "locations file" is described in plain words.
- **Part-map changes:** none. The new files sit under existing globs, and the locations file is read by instructions rather than by code of a part.
- **Projected entries:** none.
- **Rows of Settlements to record written:**
  - Row 1: WAY-107 and WAY-27 (edited).
  - Row 2: WAY-320.
  - Row 3: `tracked-file-private-paths` (new) and `outbound-link-reach` (edited).

## Checks
| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| `python -B gate/run_tests.py task-cycle` | 0 |
| `python -B gate/run_tests.py elements/common` | 0 |

## Searches not found or unclear
- None.
