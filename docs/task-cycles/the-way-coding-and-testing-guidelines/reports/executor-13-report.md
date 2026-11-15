# Executor report — slice 13: the tests of the rule of a repository changer

**Status:** done with concerns

- Concern 1: ruff on the three test files exits 1 because of one finding that is not on a line the slice wrote (RUF059 at `elements/common/test_migrate_foundation.py:680`, in the existing `test_a_second_run_changes_nothing`). The diff adds lines only; that line is unchanged.
- Concern 2: the migration script writes its report to `.runs/foundation_migration.md` inside the repository when run without `--apply` and without `--report` (documented behaviour). I read "working directory" as a git worktree (the sense the glossary and WAY-376 use) and did not treat that report as a violation. Question 1 below asks the orchestrator to confirm this reading.

## Commits

- `d389ff5` — Check that the repository changers change nothing without the act (3 files, +88 lines, 0 removed)

## One-line check result

Tests exit 0 (removal 46 tests, migration 19, installer 36); ruff check on the three test files exits 1 on one pre-existing RUF059 at `elements/common/test_migrate_foundation.py:680`, not on a slice line; `foundation_check.py --skip-test-citations` exits 0.

## Report path

`.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-13-report.md`

## Changes

| File | Added | Removed | What |
|---|---|---|---|
| `task-cycle/test_remove_merged_worktrees.py` | 25 | 0 | helpers `state` and `changed`; the existing `test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` is cited with `# invariant: repository-changer-acts-only-when-told` and now compares the whole fixture tree and the worktree registrations before and after a dry run |
| `elements/common/test_migrate_foundation.py` | 23 | 0 | helpers `tree` and `changed`; the existing `Trial.test_a_run_without_apply_writes_nothing_but_its_report` is cited and now compares the whole tree under the repository root before and after a trial run |
| `installation/test_install.py` | 40 | 0 | helpers `tree` and `changed`; new test `test_without_apply_or_declined_no_tracked_file_or_working_directory_changes`, cited with the invariant; runs a preview and a declined `--apply` on a product that has committed `README.md` and `AGENTS.md` |

No change to the three scripts (`git diff` of each is empty after the break runs were undone).

## Checks run, with command and exit code

Baseline, before any edit (all on the base commit):

- `python -B task-cycle/test_remove_merged_worktrees.py` → exit 0
- `python -B elements/common/test_migrate_foundation.py` → exit 0
- `python -B installation/test_install.py` → exit 0

Test-first state: each strengthened or new test was run before its break and passed with exit 0 (the dry-run test with `-k dry_run`, the trial test with `-k Trial`, the installer test with `-k no_tracked_file`), because the scripts already behave as the invariant says.

Failing run and restore, per cited test (one break each, undone by `git checkout -- <script>`, then `git diff -- <script> | wc -l` gave 0):

- Removal script: break inserted in `run()` before `apply_removals`, writing `a.txt` in the main checkout when `--apply` is absent. `python -B task-cycle/test_remove_merged_worktrees.py -k dry_run` → exit 1, `FAIL: test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked`, `Lists differ: [] != ['main/a.txt']`. After restore → exit 0.
- Migration script: `if apply:` before the writes changed to `if apply or True:`. `python -B elements/common/test_migrate_foundation.py -k Trial` → exit 1, `FAIL: test_a_run_without_apply_writes_nothing_but_its_report`, `Lists differ: [] != ['foundations/decisions.md', ...]`. After restore → exit 0.
- Installer: a write to `README.md` inserted before the `if not args.apply:` preview return. `python -B installation/test_install.py -k no_tracked_file` → exit 1, `FAIL: test_without_apply_or_declined_no_tracked_file_or_working_directory_changes`, `Lists differ: [] != ['README.md']`. After restore → exit 0.

Final focused runs on the committed state:

- `python -B task-cycle/test_remove_merged_worktrees.py` → exit 0, 46 tests OK
- `python -B elements/common/test_migrate_foundation.py` → exit 0, 19 tests OK
- `python -B installation/test_install.py` → exit 0, 36 tests OK
- `<main checkout>/.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa task-cycle/test_remove_merged_worktrees.py elements/common/test_migrate_foundation.py installation/test_install.py` → exit 1; one finding, RUF059 at `elements/common/test_migrate_foundation.py:680`, pre-existing and not on a slice line
- `python -B elements/common/foundation_check.py --skip-test-citations` → exit 0, "0 errors"

Not run: the product's gate (`gate/run_tests.py` without a directory), per WAY-160.

## Own-work check (section 3)

- Requirement: without `--apply`, or with the confirmation declined, the three scripts change no tracked file and no working directory.
- Check: a snapshot of the whole tree before and after the run (`.git` directories left out), plus the worktree registrations for the removal script, compared; then a deliberate break in each script, to see the check fail.
- Result: each check passes on the real script and fails on the break (see above). The check does see a changed or new tracked file and a changed or added directory.

## Reaches beyond the handoff

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` read whole, because the method names them.
- `foundations/decisions.md` lines 6265–6360 read through a grep for "working directory" (WAY-375, WAY-376), to confirm that "working directory" means a git worktree in the-way's vocabulary.
- The rules-on-demand hook output (`scripts.md`, `git.md`) was shown when I ran a Bash command and a commit; I followed the commit rule (English message, `-m` arguments, paths staged by name).

## Choices made

1. **Strengthen versus write.** For the removal script and the migration script the existing test checks part of the rule, so I cited it and added the whole-tree comparison to it. For the installer the existing preview and declined-apply tests use a product with no committed file, so the tracked-file part of the rule could not be checked there; I wrote a new test instead of changing them. Way rejected: extending the existing declined-apply test to a second fixture — it would have mixed two fixtures in one test. Cost if wrong: a reviewer may ask why the installer's existing declined-apply test stays uncited; it checks only part of the rule.
2. **Snapshot scope.** The snapshot leaves out every `.git` directory, so changes inside git's own store (refs, index) are not seen except the registrations of the removal script. Way rejected: snapshotting `.git` too — the fetch in the removal script legitimately updates remote-tracking refs, so that would forbid the documented behaviour. Cost if wrong: a script could change git metadata without the test noticing.
3. **Reading of "working directory".** Worktree, not "any directory under the repository root". Way rejected: reading it as the repository root, which would make the migration script's default report a violation. Cost if wrong: the migration test would have to be changed to pass `--report` and the invariant would be marked violated by a documented act.

## Questions

1. Does the orchestrator (or the human, via the orchestrator) accept that the migration script's default trial report to `.runs/foundation_migration.md` is not "a working directory" under `repository-changer-acts-only-when-told`? My recommended answer: yes, since the script documents it as its only output without `--apply` and the glossary and WAY-376 use "working directory" for worktrees. If no, the invariant would need a human decision (WAY-51), and I would return `blocked`.

## Unread material

- `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` — read only lines 30–37, 134–148, 530–533 (the handoff's *Read* ranges and the lines they name); not read elsewhere.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` — read only the slice headings, the *Choices* table and the *Orchestrator's additions* section (lines 1003–1041) and the Slice 13 section from the handoff. The *Coverage* section and the other slices were not read.
- `foundations/decisions.md` — read WAY-08 (1750–1825, including WAY-51), WAY-198 (8517–8548) and WAY-389 (9991–10012). Not read: WAY-386, WAY-387, WAY-388, WAY-390, WAY-391 (the other exemplars named by E8).
- `foundations/invariants.md` — read `script-language`, `script-imports`, `script-subprocesses`, `test-method-citation`, `cross-part-imports` and `repository-changer-acts-only-when-told` (lines 116–177, 348–356, 458–466).
- `foundations/part_map.md` — read `elements-common` (65–78), `task-cycle` (101–111) and the first lines of `installation` (189–195); the `installation` *Depends on* list was cut off in my read and is not read in full.
- `elements/common/migrate_foundation.py` — read lines 1–80, 880–992 (the module description, rendering and `run`/`main`). Not read: lines 81–879 (the migration logic).
- `installation/install.py` — read lines 401–492 (`verify_remote` and `plan`), 564–693 (`run`), and a grep of its git calls. Not read: lines 1–400 and 493–563 in full.
- `task-cycle/test_remove_merged_worktrees.py` — read lines 1–150, 148–225, 338–378. Not read: the rest of the file (about 300 lines).
- `elements/common/test_migrate_foundation.py` — read lines 530–729 and a grep. Not read: lines 1–529.
- `installation/test_install.py` — read lines 100–219, 660–709 and a grep. Not read: the rest.
- `task-cycle/remove_merged_worktrees.py` — read in full.

## Searches not found or unclear

- "Working directory" in the foundation: unclear whether it means a git worktree or any directory under the repository root. Resolved as a worktree (Choice 3, Question 1).
- The handoff's *Read* entry `E8` names six decisions (WAY-386 to WAY-391); I read only WAY-389, the exemplar of the kind `repository-changer`, which is the one the invariant derives from.
- Nothing else searched was not found.

## Weakest point and its check

The weakest point is that the snapshot ignores `.git` directories, so a change to git's own state by the three scripts without `--apply` would not be seen by these tests (except registrations for the removal script). The check I made: the three breaks change working-tree files, which the tests catch; I did not break git metadata, and did not test a break there. The removal script's documented fetch changes remote-tracking refs, so a metadata snapshot would also need an allowance for that, which I left out on purpose.

## Working copies

None made. No worktree, clone or copy was created during this slice; the breaks were made in the worktree itself and undone with `git checkout` before each commit, so nothing needed removal.
