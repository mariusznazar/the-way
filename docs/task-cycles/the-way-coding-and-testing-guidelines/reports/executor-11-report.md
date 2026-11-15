# Executor report — slice 11

The refusal invariant of `check_instructions.py` cited by its test of a link out of the repository

## Status

`done with concerns`

Concern: I edited `instruction-files/test_check_instructions.py` without reading it whole first, as
`task-cycle/change/SKILL.md` section 1 requires ("Every file you change, whole, before you change
it"). I read 1–30, 80–103 and 740–812 of it and grep hits. The change itself is one comment line.
A second file, `instruction-files/check_instructions.py`, was edited for a moment to break the
refusal; I read only lines 245–272 and its grep hits before that edit, not the whole file. It is
restored and `git diff` on it is empty.

## Commits

- `99340e9` — "Cite the refusal invariant of check_instructions.py from its test of a link out of the repository" (author as configured in this repo, `mariusznn@gmail.com`)

Base `d84dc5b`; the branch `task/the-way-coding-and-testing-guidelines` now at `99340e9`.

## Files changed

- `instruction-files/test_check_instructions.py`: +1 −0. Added `        # invariant: check-instructions-refuses-outside-links` as the first line of the body of `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed` (line 767 after the change).
- `instruction-files/check_instructions.py`: no net change (temporary edit at line 256, restored; `git diff --stat` empty).

## One-line check result

All slice checks passed: the test file exits 0 with the cited test `ok` (not skipped on this machine); the cited test failed (exit 1) with the refusal broken for a moment and passed again after restoring; `foundation_check.py --skip-test-citations` exits 0.

## Checks run

Each run's output was kept in a working copy that is removed (see Working copies); the key lines are quoted here.

1. Baseline, before any edit: `python -B instruction-files/test_check_instructions.py -v` — exit 0; `Ran 105 tests`, `OK (skipped=5)`. The cited test is not among the skipped ones: `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed ... ok`. The five skips are other tests (`no FIFO on this platform`, and four `needs the real path of a link, as on POSIX`). On this Windows machine file symlinks can be made, so the cited test ran rather than skipped.
2. After the citation was added: same command — exit 0; `Ran 105 tests`, `OK (skipped=5)`; the cited test `ok`.
3. Refusal broken for a moment: in `instruction-files/check_instructions.py` line 256 the condition `if entry.is_symlink() and leads_out(entry.path, root):` was changed to `if False and entry.is_symlink() and leads_out(entry.path, root):`. Same command — exit 1; `FAILED (failures=5, skipped=5)`. The cited test failed: `FAIL: test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`, at `test_check_instructions.py` line 770, `AssertionError: Lists differ: [('warn', 'dead-path', 'AGENTS.md', '`MARKER[79 chars]ds')] != [('info', 'read', 'AGENTS.md', 'a link out o[24 chars]ad')]`. The failure is the expected assertion: the link is read and reported as a dead path instead of "a link out of the repository, not read". Four other tests also failed in this run (chain and network-path tests in the same guard family); they were not investigated further, since the change under test is only a comment and the run was for the cited test.
4. Restored: the line was changed back; `git diff -- instruction-files/check_instructions.py` printed nothing (exit 0 of `git diff --stat`, empty output). Same command — exit 0; `Ran 105 tests`, `OK (skipped=5)`.
5. `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0; last line `0 errors`.
6. Own-work check (extra, not in Checks): `python -B elements/common/foundation_check.py` (with citations) — exit 1; `6 errors`. All six are invariants of other slices that no test cites yet: `ruff-blocking-rules` (foundations/invariants.md:432), `function-and-file-size` (442), `generator-writes-only-with-write` (452), `repository-changer-acts-only-when-told` (462), `command-runner-passes-exit-code` (472), `shared-module-import-runs-nothing` (482). `check-instructions-refuses-outside-links` is not among them, so the citation is recognised by the foundation check.

Not run: the product gate (`python -B gate/run_tests.py` without a directory), per WAY-160 and the handoff. `ruff` was not run: the slice's checks do not name it, and `ruff.toml` (slice 1) does not exist yet at the base.

## Own-work check (section 3)

- Requirement 1: the citation must name the identifier of E33 exactly, in a tracked file whose name does not end in `.md` (invariants.md `test-method-citation`). Check: the line is `# invariant: check-instructions-refuses-outside-links`, a comment in a `.py` file; the full foundation check (check 6) lists no error for this invariant. Shown: met.
- Requirement 2: the invariant's test is seen failing once (WAY-08). Check: check 3 above — the cited test failed with the refusal broken, passed again after restoring (check 4). Shown: met.
- Requirement 3: the skip path must not be claimed where links cannot be made. Check: on this machine the test ran (check 1). The skip path was not exercised here; the report does not claim a failing run on a machine that skips. Shown: not applicable on this machine.
- Mutation check: the change is a comment; the break in check 3 is the only mutation needed by the slice.

## Choices made

- The citation sits as the first line of the test's body, the same place as the existing citations in `agent-instructions/test_instruction_files.py:307` and `agent-instructions/test_agent_type_copies.py:211` (the method body, `# invariant: <id>`, indented to the body). Way rejected: a comment above the `def` line — no existing citation does it that way; cost if wrong: none found by the foundation check.
- The temporary break used `if False and ...` rather than deleting the branch, so the line stays in the diff-free state after the undo. Way rejected: editing a copy of the script in a working copy — the slice names the worktree and the restored file was verified by `git diff`. Cost if wrong: none; the diff is empty.

## Reach beyond the handoff

- `foundations/invariants.md:116-146` (script-language, script-imports, script-subprocesses) and `:348-356` (cross-part-imports) and `:166-176` (test-method-citation) — read whole as the orchestrator's additions. Not named by the handoff: the `Rests on` entries `python-stdlib-modules` and `git-path-patterns` were not read.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` lines 451–476 (Slice 11 in the plan) and 1003–1041 (Choices and the orchestrator's additions) — the second is named by the handoff's "end of plan.md" instruction; the first was read for comparison with the handoff's copy.
- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` — read whole (the method). `ui_check.md`, `reserved_choices.md`, `fix.md` not read: no screen changed; no language, framework or library choice arose; not a fix.
- `a file of the author's private notes` and `...\rules\git.md` — read because the local hook `rules-on-demand` blocked my Bash call twice and required them before the call (once before a `python -B` run, once before the commit). The commit message is English; the commit used a `-m` argument, per the rule.

## Unread material

- `instruction-files/test_check_instructions.py` — not read whole before the edit (1099 lines). Read: lines 1–30, 80–103, 740–812, and the grep of `def test_` and `invariant`. Concern above.
- `instruction-files/check_instructions.py` — not read whole (730 lines). Read: lines 245–272 and the grep of link-related names (`leads_out`, `directory_link`, `walk_exists`, `resolve`, and related). Concern above.
- `foundations/invariants.md` `python-stdlib-modules` and `git-path-patterns` (the *Rests on* of `script-imports` and `cross-part-imports`) — not read; not named by the handoff.
- Plan's *Coverage* section (plan.md:934–1002) — not read; not named by the handoff.
- Everything the handoff names was read: `task.md:34-35`, `task.md:177-181`, `task.md:543`, E33 (`foundations/invariants.md:538-546`), `foundations/decisions.md` WAY-48 (2490–2530), WAY-235 (9140–9205), WAY-08 (1745–1782), `foundations/invariants.md` test-method-citation (166–176), `foundations/part_map.md` instruction-files (170–190), and the orchestrator's additions as above.

Note on ranges: the plan's Slice 11 *Read* ranges differ from the handoff's copy (the plan has `decisions.md:2492-2520`, `9188-9242`, `1746-1774`, `invariants.md:166-174`; the handoff gives `2496-2525`, `9145-9200`, `1750-1779`, `166-175`). I used the handoff's ranges, which the handoff says are refreshed to the worktree; the entries I read fully covered both sets.

## Searches not found or unclear

- None unfound. The citation form was confirmed by grep (`grep -rn "invariant: " --include=*.py`), which found existing citations in `agent-instructions/` and `elements/common/`.
- Unclear: the plan's Slice 11 *Checks* say "shown failing ... or the reason it could not be". Here the cited test ran on this machine (file symlinks work), so no reason was needed; I did not verify the POSIX-only skip behaviour since this machine is Windows.

## Questions

None.

## Working copies

- `.runs\executor-11\` — the working directory of this slice, holding the outputs of checks 1–6 (`baseline.txt`, `run-pass-1.txt`, `run-broken.txt`, `run-restored.txt`, `foundation.txt`, `foundation-full.txt`). Its contents are quoted in this report; the directory is removed before I return (see the next line). Removal: `rm -rf` of that directory, then confirmation that it is absent.
- No git worktree was made by this slice (`git worktree list` shows only the existing ones); nothing to prune.
