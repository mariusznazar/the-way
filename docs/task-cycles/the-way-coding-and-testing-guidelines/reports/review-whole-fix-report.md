PASS f0482d0db5618978899f0d69aa6d22e4f2b04f4d

# Review of the fix of the findings of the review of the whole change

Fix range `be9b44d..f0482d0` (7 commits, 19 files, +194 −107). `git rev-parse HEAD` of the reviewed worktree is `f0482d0db5618978899f0d69aa6d22e4f2b04f4d`. Method: `review-change`, variant the fix of earlier findings (`task-cycle/review/fix.md`). Bounded by `reports/whole-change-findings.md` (4 blocking, 12 Minor within the task). I read the fix report as claims and the whole diff of the range.

Result: all four blocking findings are fixed; all twelve Minor findings are fixed. No new Critical or Important finding in the fix diff. Two new Minor notes, which block nothing.

## Each finding

| Finding | Verdict | Evidence |
|---|---|---|
| I-1 cross-part-imports | **fixed** | `python -B gate/run_tests.py elements/part-map` in a clean worktree of `f0482d0`: exit 0, 40 tests, OK (red at `be9b44d`). `process-audit/test_audit_count.py` keeps `run_count` on the literal `SCRIPT` and adds `run_count_of_the_copy` for the checkout built in the temporary home; `relation-model/test_fingerprint.py:123` assigns `here = sys.argv[1]` first. Meaning of both tests unchanged (diff read). `relation-model` exit 0, `process-audit` exit 0. |
| I-2 report-order race | **fixed** | `gate/test_run_tests.py` `runner_noting`: the test appends `released` to the log when the runner has printed `== b`, and `a` waits for `released`, so `b` is first by construction. 50 runs of the test alone at the head: 0 failures (before: 1 in 40 and 1 in 60 at the head). `log()` returns one fixed path, so the note reaches `a`. |
| I-3 "input closed" | **fixed** | `foundations/invariants.md` (`shared-module-import-runs-nothing`) and `guidelines/coding-shared-module.md` read "with its input open and empty"; test unchanged. |
| I-4 migrate_foundation vs invariant | **fixed**, by the first way I listed (Q12) | The invariant now excepts "a report that the human names with `--report`"; WAY-389, which restated the sentence, was changed the same way (the fix report names it); `guidelines/coding-repository-changer.md` Good/Bad/rule follow it, the status paragraph is gone, the status is `copy`. `python -B elements/common/foundation_check.py`: exit 0, `0 errors`. The direction Q12 is a cycle choice, the human accepts it at the request; I find it sound (writing a report to a path the human names is what `--report` is for). |
| M-1 | **fixed** | `# invariant: gate-times-refuses-impossible-entry` on `task-cycle/test_gate_times.py:394`; `task-cycle` exit 0. |
| M-2 | **fixed** | Docstring of `MissingFieldError` reworded; `required`, `TOKEN_DIGITS`, `required_count`, `required_text`, `required_time` moved under `# Fields a reading needs`, above `# Codex` (a pure move: diff read, no change of code). |
| M-3 | **fixed** | `read_codex_agent` raises `MissingFieldError("<path>:<n>: the line is not a JSON object")`. My crafted rollouts with a later line `[1]`, `5`, `null`, `"x"`: exit 2 and that message for each (before: `AttributeError`, exit 1). Tests added: the non-object line, and `10**15-1` accepted. The fix report notes, rightly, that the Claude Code half skips such a line and does not end with exit 2; the direction's comparison was loose, the behaviour asked for (exit 2 naming rollout and line) is what the review asked for. |
| M-4 | **fixed** with I-4 | Paragraph deleted. |
| M-5 | **fixed** | `guidelines/coding.md:99-101`: the exemption is for a module with no more for the command line than a fixed `if __name__ == "__main__":` block — true of `relation-model/fingerprint.py`. |
| M-6 | **fixed** | The comments of `NAMES`, `BLOCK`, `SIBLINGS`, `ENTRY_POINT` in `installation/test_install.py` name the README of the installation, section "Files in the product" (exists, `installation/README.md:48`), no code line. `installation` exit 0. |
| M-7 | **fixed** | `test_the_way_foundation_passes` also keeps `` `<name>` is withdrawn; name its successor `` for each row of the part map's *Withdrawn identifiers*; comment says why by name. `elements/common` exit 0. |
| M-8 | **fixed** | README names the two invariants the test checks and says the whole check runs on its own. |
| M-9 | **fixed** | README lines for `guidelines/` and for `ruff.toml` with the two requirement files; the sentence of `agent-instructions` in `foundations/part_map.md` names the guidelines. |
| M-10 | **fixed** | A test in each of `test_linter_invariant.py` and `test_size_invariant.py` that every tracked `.py` file lies under a directory of `PARTS`, naming the file otherwise. `agent-instructions` exit 0 (37 tests, 2 expected failures). No shared helper (see M-new-1). |
| M-11 | **fixed** (text made true, Q15) | Header of `agent-instructions/skill_entry_points.py` and `guidelines/coding-generator.md` say an empty value ends with exit 1, a missing line with exit 2. |
| M-12 | **fixed** | The two state sentences of `guidelines/coding.md` replaced by what the author is to do. |

## New findings in the fix diff

Critical / Important: none.

Minor (block nothing, within the fix):
- **M-new-1** `agent-instructions/test_linter_invariant.py:68-74` and `agent-instructions/test_size_invariant.py:76-84` — the same coverage test and the same tuple `PARTS` stand twice, so a new part must be added in two files; the finding asked for "each of the two tests or one shared helper", so this meets it, at the cost the fix report names.
- **M-new-2** `guidelines/coding-repository-changer.md` — `elements/common/migrate_foundation.py` is `copy` while its `--report` can overwrite a tracked file the human names; the invariant now allows it, but a new script that copies it inherits that writing. It is what the narrowed invariant says; mention only.

## Declined to judge

- The flake of `gate/test_run_tests.py` `DirectoriesAtOnce` (`test_by_default_every_directory_runs_at_the_same_time`, `test_a_number_of_jobs_limits_the_directories_that_run_at_once`; O-3 of the review of the whole change, outside the task): `python -B gate/run_tests.py gate` ended with exit 1 in my run at the head, on that test (120 s wait, "did not meet the others"), as at the base per the fix report (5 failures in 40 at each). The test I-2 fixed is not among the failures. It can turn the orchestrator's one run of the gate red.
- O-1 (`Z` forms of a time): not the fix's.

## Checks run (command and exit code), all in a clean worktree of `f0482d0`

- `python -B gate/run_tests.py elements/part-map` — 0 (40 tests).
- `agent-instructions` 0 (37, expected failures 2); `relation-model` 0 (13); `elements/common` 0; `instruction-files` 0; `product-guidelines` 0; `task-cycle` 0; `process-audit` 0; `installation` 0; `gate` **1** (the flake above; 36 tests, 1 failure).
- `python -B elements/common/foundation_check.py` — 0, `0 errors`.
- 50 runs of the report-order test alone — 0 red.
- Crafted Codex rollouts (non-object later line, 4 forms) — exit 2 with the message naming the line.
- Ruff over the ten directories with `--ignore-noqa`: 25 reports, the same list as before the fix; none new.
- Not run: the full gate; a POSIX shell.

## Reaches beyond the dispatch

`installation/README.md` heading "Files in the product" (to confirm the section the comments name); `gate/test_run_tests.py` `log()` (to confirm the note reaches the other directory). Nothing else.

## Working copies

`.runs/review-whole-fix/head` (a worktree of `f0482d0`) and the files in `.runs/review-whole-fix/` (run logs, crafted rollouts): removed with `git worktree remove --force`, `git worktree prune` and deletion of the directory. Nothing remains.

## Unread material

The decisions I read whole this time: WAY-389 (the hunk, from the diff) and the invariants `shared-module-import-runs-nothing` and `repository-changer-acts-only-when-told` (the entries, from the diff). I read no other decision whole; the foundation and guidelines I selected for the review of the whole change stand as read there. Not read: the executor reports of the fix beyond `fix-whole-report.md` and the handoff's first 150 lines; the rest of `installation/README.md`; the 17 unchanged hunks of `guidelines/coding.md` outside the diff (read whole in the earlier review).

## Searches not found or unclear

none
