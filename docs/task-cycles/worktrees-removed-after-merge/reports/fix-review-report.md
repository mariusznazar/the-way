PASS b8a16cc2d40c703c3a6870e0af0973e38667c182

# Review of the fix — worktrees removed after merge

Range `a849408fade7f5454a2a1535fc14ee364a0fa7bf..b8a16cc2d40c703c3a6870e0af0973e38667c182` (`git rev-parse HEAD` confirmed), commits `1f27200` and `b8a16cc`; three files changed (`task-cycle/remove_merged_worktrees.py`, `task-cycle/test_remove_merged_worktrees.py`, `foundations/decisions.md`). Findings judged: `reports/fix-findings.md`. Blocking findings: 0. New Minor: 1. The invariants and the glossary were read whole against the whole change (`835344f..HEAD`).

## The findings, one by one

- **I1 — fixed.** `inspect_state` now passes `--ignore-submodules=none` (`remove_merged_worktrees.py:332-334`); the docstring states it. Evidence: my own driver of the first review (`reports/review-whole-submodule-check.py`: a merged, pushed task directory with a populated submodule declared `ignore = all`, uncommitted work in a tracked file and a new file in it), run against the fixed script with `--apply`: the line is now `keep … uncommitted changes: a tracked file changed or a new file that git does not ignore`, exit 0, and the directory stands (`task dir exists after: True`). The new test `test_a_change_in_a_submodule_that_the_configuration_hides_keeps_the_directory` fails without the flag: in a copy of script and test in my directory with the flag taken out it fails (`AssertionError: False is not true`, one failure). The test asserts first that plain `git status --porcelain` is empty and the strict one is not, so it cannot pass for another reason. The `--force` retry stays and now stands behind the stricter status, as I asked.
- **M1 — fixed.** The retry looks for git's own sentence, `SUBMODULE_REFUSAL = b"working trees containing submodules cannot be moved or removed"`, in the message (`:79-81`, `:431`), no longer for the word anywhere. `RefusalTest.test_only_gits_sentence_about_submodules_makes_the_removal_forced` replaces `git` by a refusal for changed files whose path holds `submodule` and asserts one call without `--force`; the wording of git's real sentence is the one the existing test `test_a_populated_submodule_does_not_keep_a_clean_directory` meets with a real populated submodule (it still passes, so the constant matches this git, 2.55).
- **M2 — fixed.** The fetch is `git fetch --no-tags --no-prune <remote>` (`:224`); docstring updated. The test now sets `fetch.prune true` in the repository's configuration; with `--no-prune` taken out of a copy it fails (one failure), so it tells the break apart now.
- **M3 — fixed.** WAY-375's first paragraph now says the tree is clean "as git's own check for removing a checkout reads it", that a cycle's directory stands on a branch beginning with `task/` or whose directory holds the record of a cycle, or is a detached copy of a base, and that a nested detached checkout goes with its directory whatever its name only where it is clean and on the remote, else the directory stays. This matches `describe_owner` (`:349-364`) and `judge` (`:371-386`). `foundation_check.py`: `0 errors`; the `decision:` quotations of the tests still match.
- **M4 — fixed.** The reason is the fixed text `git cannot read its state` (`:337`); `RefusalTest.test_a_reason_for_the_list_never_holds_what_git_says_of_a_path` asserts `entry.hard == ["git cannot read its state"]` with a made-up message that names a path.
- **M5 — fixed.** `test_a_listed_path_that_is_a_junction_is_kept` (uses `_winapi.CreateJunction`; skipped with a reason where the module or the junction is missing) and the I1 test are added. `_winapi` is in `sys.stdlib_module_names` (checked: `True`), so `script-imports` holds. It ran here, not skipped (the whole file: 46 tests OK).

## New findings of the fix

None Critical or Important. Does the fix touch what the findings do not name? Yes, in two small ways, both harmless: the test file now imports the script as a module (`sys.path.insert` of its own directory, `import remove_merged_worktrees`, `types.SimpleNamespace`, `unittest.mock`) for the two tests of git's messages, and `add_submodule` was extracted from the old submodule test. Both stay in one part (`task-cycle`), standard library only, and the gate shows no break.

**Minor (new, within the task, does not block): the task's own word "human action" and WAY-375's second paragraph.** Glossary: "A human action is an act outside the product's repository that a task needs and a human performs." WAY-375 says that removing a checkout git names, "also one that stands outside the repository's own directory, ... needs no human action". A reader who takes the glossary meaning reads that as a contradiction with the task's *Human actions* line, where the human's one-time removal of the directories in `the-way-wt` and `loop2-wt` is a human action. The entry limits itself in the same paragraph ("no effect outside the repository in the sense of WAY-140", with the server, DNS, key or account named), and the task's row 5 and its *Answer* settle exactly this, so I judge it a defect of the task's wording that the change carries, graded Minor by the method (no sentence a reader would act on wrongly: the script and the one-time step both work as designed). It goes to the request's list; the human may want WAY-140's phrase "outside the product's repository" tightened in its own decision, not in this change.

## The invariants (whole file read) against the whole change `835344f..HEAD`

- `script-language`: both new scripts are Python. Holds.
- `script-imports`: the script imports `argparse`, `os`, `re`, `subprocess`, `sys`, `dataclasses`, `__future__`; the test also `shutil`, `stat`, `tempfile`, `unittest`, `pathlib`, `types`, `unittest.mock` and, where present, `_winapi`, all in the standard library of 3.14 (`sys.stdlib_module_names`); the one module of the repository it imports, `remove_merged_worktrees`, is a tracked Python file. Holds.
- `script-subprocesses`: the script starts `git` only (`git()`); the test starts `git` and `sys.executable`. Holds.
- `cross-part-imports`: the test imports a file of its own part (`task-cycle`), through a directory it adds to `sys.path`; same part, so no part's *Depends on* is needed. The gate's run of the invariant's test passed. Holds.
- `tracked-file-private-paths`: `grep` of both new files for a drive letter path found none; the gate's test `test_tracked_files_private_paths` passes. The `decisions.md` text holds no absolute path. Holds.
- `map-reference-target`: WAY-375 and WAY-376 name only `task-cycle` as *Scope*, which is an entry of the part map. Holds (`foundation_check.py`: 0 errors).
- `test-method-citation`: no invariant of method `test` was added or reworded; the cited ones are untouched. Holds.
- `skill-entry-points`: `SKILL.md` description unchanged; `python -B gate/run_tests.py agent-instructions`: 25 tests OK. Holds.
- `repository-file-location`: both new files lie in `task-cycle/`. `element-directory-contents`, `skill-rule-source`, `elements-no-pending-marker`, `generated-overview`, `instruction-file-imports`, `root-claude-md-import`, `derived-file-content`: the change touches none of what they state; `elements-no-pending-marker` concerns `elements/` only. Holds.
- `foundation-change-merge-route` and `return-step-record` (method review, on the merge onto `{merge-onto}`) and `outbound-link-reach` (no link added): the first two concern the integration and the committed record the cycle makes at its return step, after review; nothing in the commits conflicts with them, and I did not judge the return step, which is not in this range.
- The invariants of other parts (`fingerprint-definition`, the `project-*`, `installation-*`, `gate-exit-code`, `python-version-declared`) and `record-copy-image-check` / `record-copy-image-files`: not reached by the change; no image file is added.
- WAY-38 / WAY-89 and `python-version-declared`: Python 3.14 features used (`str.removeprefix`, `os.path.isjunction`) are within it.

## The glossary (whole file read)

Terms of WAY-375, WAY-376 and the skill's new text, and the glossary's reading of each: "part" (used only as *Scope*), "entry", "gate", "foundation step", "return step", "human action" (the Minor above), "record" and "cycle" (not entries). Nothing else in the new text uses a glossary term in a meaning other than its entry gives. The words "merged branch", "base copy" and "belongs to a cycle" have no entry, and WAY-375's own sentences define them where they are used; no sentence of the change reads differently for a reader who knows git's field except the one under the Minor.

## Declined to judge

- The return step's commits and the record copy (not in the range).
- The part map's trust-boundary list (the orchestrator's answer of step 4, unchanged).

## Checks I ran (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest task-cycle.test_remove_merged_worktrees` | 0 | 46 tests OK, none skipped |
| `python -B gate/run_tests.py task-cycle` | 0 | 440 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B <reports/review-whole-submodule-check.py>` against the fixed script (throwaway repository in `.runs/review-whole/sm`) | 0 | `keep … uncommitted changes`, directory stands (I1 closed) |
| in `.runs/review-whole/mut/`, a copy of the script with `--ignore-submodules=none` taken out, then the I1 test | 1 | fails (the test tells the break apart) |
| in the same copy, the script with `--no-prune` taken out, then the fetch test | 1 | fails (the test tells the break apart) |
| `python -c "'_winapi' in sys.stdlib_module_names"` | 0 | `True` |
| `grep` for drive-letter paths in the two new files | 1 | none found |

Not run: the product's full gate (the orchestrator's); the script with `--apply` against any real worktree; the mutation of M1, M4 and M5's tests (I read them: each asserts on a made-up git answer or a made junction, and cannot pass for another reason; the author reports that it mutated each).

## Reaches beyond the dispatch

None beyond the handoff's reading list: the fix-findings file and the diff of the range; `foundations/invariants.md` and `foundations/glossary.md`, each whole.

## Unread material

- The author's fix report was read; the commit messages of `1f27200` and `b8a16cc` were not.
- Decisions: this review reads WAY-375 and WAY-376 again as changed and no others; the counts of the first review stand (8 whole, 132 by title only).
- Guidelines: the-way has no `guidelines/coding.md` (WAY-328); none read.

## Searches not found or unclear

- none

## Working copies

- `.runs/review-whole/` of the worktree (the driver's throwaway repository `sm`, the copy of script and test in `mut/`, the outputs of my runs): all removed; `.runs/` holds `task-cycles/` alone, `git status --short` is empty and `git worktree list` holds the same 96 entries. Remainder: none.
