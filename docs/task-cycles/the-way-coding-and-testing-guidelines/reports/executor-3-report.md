# Executor report — slice 3: the installer test writes out its block, its skills and its entry point, and uses `capture_output`

- **Status:** done with concerns (the concerns are in *Choices* and *Own-work check*; none blocks the slice)
- **Worktree:** `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`
- **Base:** `d113238f887a7ba565bb667d2c638b3ab9c98b22`
- **Commit:** `43d7d9b` — "Write the installer's block, skills and entry point out in its test and use capture_output"
- **Files changed:** `installation/test_install.py`: 119 lines added, 19 removed. `installation/install.py` is not changed in the commit (the two temporary edits made for the failing run were undone; `git diff -- installation/install.py` is empty).
- **Check result:** all focused checks pass; none failed or was left out. The product's full gate was not run, as the slice requires.

## What changed

1. `NAMES` (was `tuple((path, name) for name, path in install.SKILLS.items())`) is now a literal tuple of the 21 (path, name) pairs. The paths are those of `installation/install.py:25-46`; the names are those of `installation/README.md:58`.
2. `BLOCK` (was `install.agents_block()`) is now a literal string: the text of `installation/install.py:169-214` (`product_guidance`) between the markers, written out with the same wording, placed with a comment naming the source.
3. A new module constant `SIBLINGS` holds the 21 skill names of the sentence "names another the-way skill", in the order of `sibling_names()`.
4. A new module constant `ENTRY_POINT` is the template of an entry point, the text of `installation/install.py:123-155` (`skill_wrapper`) with `{name}`, `{path}`, `{description}` and `{siblings}` placeholders.
5. A new test method `InstallTest.entry_point(path, name)` fills `ENTRY_POINT` for one skill. The description is read from that skill's own file at `self.commit` (`git show`), not from the installer.
6. Expectations that came from the installer now use the literal forms: `test_preview_apply_rerun_and_preserve_foundation` (the entry point is compared whole), `test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies` (the installer's output is compared whole with `entry_point`; its earlier substring checks were replaced by that equality), and the four tests that built a stale or own entry point with `install.skill_wrapper` (`test_rewrites_an_entry_point_of_its_own`, `test_a_file_without_every_mark_is_the_products`, `test_deletes_nothing_through_a_junction_at_the_folder_of_a_stale_entry_point`, `test_the_scan_for_stale_files_does_not_enter_a_junction_at_their_directory`) now use `self.entry_point`.
7. `command()` uses `capture_output=True` in place of `stdout=subprocess.PIPE, stderr=subprocess.PIPE` (cause 27, the place of this file only).

The remaining uses of `install.*` in the file are the installer's output that the tests check against literal fragments: `install.skill_wrapper` in the wrapper test (as the actual value), `install.product_guidance()` in the three guidance tests (actual value), and `install.OWN_AGENT_MARK` (see *Choices*).

## Checks run

| Check | Command | Exit code | Result |
|---|---|---|---|
| Lint before the change (baseline) | `<ruff> check --config ruff.toml --no-cache --ignore-noqa installation/test_install.py` | 1 | one error, UP022 at the old `subprocess.run` call (the place of cause 27) |
| Installer test after the change | `python -B installation/test_install.py` | 0 | Ran 35 tests, OK (about 146 s) |
| Installer test with the installer's block and an entry point changed for a moment (the invariant-style check of the slice) | `python -B installation/test_install.py` with two edits in `installation/install.py`: `product_guidance` heading `# Pinned the-way process` changed to `# Pinned the-way process, changed`, and `skill_wrapper` sentence `at the commit its gitlink records.` changed to `... records!` | 1 | Ran 35 tests, FAILED (failures=29): `test_appends_block_to_agents_file_without_one`, `test_guidance_names_no_commit_and_covers_the_product_rules`, `test_keeps_agents_file_with_identical_block`, `test_moving_the_pin_rewrites_what_the_installer_owns_in_one_run`, `test_preview_apply_rerun_and_preserve_foundation`, `test_rewrites_a_different_block_in_place`, `test_rewrites_an_entry_point_of_its_own`, `test_warns_where_codex_would_miss_the_block`, and the wrapper test in all 21 subtests. Log kept at `.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-3-mutated-run.log` |
| Undo of the two edits | `git diff --stat -- installation/install.py` | 0 | empty |
| Installer test after the undo | `python -B installation/test_install.py` | 0 | Ran 35 tests, OK (about 151 s) |
| Lint after the change | `<ruff> check --config ruff.toml --no-cache --ignore-noqa installation/test_install.py` | 0 | "All checks passed!" |
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | "0 errors" |

The full suite (`python -B gate/run_tests.py` without a directory) was not run, as WAY-160 requires.

## Own-work check (section 3 of `make-change`)

- **Requirement:** the test must fail when the installer's block or the text of an entry point changes, and must pass as written. Its expectations must come from a source other than the installer, as WAY-394 and WAY-232 require, and the lint must be clean.
- **Check:** the mutation run above, then the undo, then a re-run of the file and of the lint.
- **What it showed:** the mutation made 29 tests fail, so the block and the entry point are now pinned by literals. After the undo, the file passes and lint is clean.
- **Weakest point:** the literal block and the entry-point template are copies of the installer's own text. The README (`installation/README.md:61`) describes the block but does not spell it out, so the exact wording can only come from `installation/install.py`. If the installer and its test are changed in the same commit with the same wording, the test follows; this is the caveat WAY-394 names for the test's source. My check of it: each sentence of the literal was compared by hand with `product_guidance` and `skill_wrapper`, and the passing run shows the installer's written `AGENTS.md` equals the literal byte for byte in `test_preview_apply_rerun_and_preserve_foundation`.

## Choices

1. **Source of the block text:** written out from the installer's `product_guidance` (`install.py:169-214`). Rejected: taking the wording from the README, which does not give it verbatim. Cost if wrong: a wording change made in both places together goes unnoticed by this test; the review should ask where each assertion's value comes from, as the decision says.
2. **Entry point:** one template with the description read from the skill's own file at the pinned commit. Rejected: writing 21 descriptions out as literals, which would add about 21 long lines copied from the skills and drift with each skill edit. Cost: a change to the template's wording is caught only through the template (the test is the copy), and a change to a skill's description is correctly not a failure of the installer.
3. **Skill list:** written out as the 21 pairs. Rejected: adding a test that compares `install.SKILLS` with the literal list, which lies outside the slice's *Goal*. Cost: a skill added to the installer and not to the test passes silently, unless an entry-point test fails for another reason. Recommend a follow-up slice or task if the list must be pinned.
4. **Output capture:** only `command()` was changed (the slice names the call at the head of the file). The other seven test files of `installation/` are left, as the plan's cause 27 says (deferred).

## Reach beyond the handoff (what, where, why)

- I read `installation/install.py` whole (694 lines), not only the ranges 25-76 and 118-216 that the handoff named, because the test calls `product_guidance`, `skill_wrapper`, `OWN_AGENT_MARK` and the stale-file scans, and I needed the surrounding code to check the copies.
- I read `task-cycle/change/slice.md` whole, as `make-change` section 1 requires for a slice.
- I read the rule file `a file of the author's private notes` only after the pre-commit hook returned it; the first commit attempt was refused by the hook and re-run unchanged after reading the rule.

## Unread material

- `task-cycle/skill/planning.md` (named by `slice.md` for ranges that differ from the plan; no range differed, so not needed).
- `task-cycle/change/ui_check.md`: not needed, the slice changes no screen.
- `project-level/technology/reserved_choices.md`: not needed, no reserved choice arose.
- The plan's slice 3 section was taken from the handoff's word-for-word copy; `plan.md` itself was read in its header, *Choices* and *Orchestrator's additions* only.
- `foundations/decisions.md` WAY-392 (named by WAY-394's *Relations*): not read.

## Searches not found or unclear

- `install.OWN_AGENT_MARK` is still an input taken from the installer, at the test of the stale definition scan (about line 874 of the new file). It is a constant of the code under test, not an expected value; WAY-228 asks that such an input be written out. It is outside this slice's goal, so I left it and name it here.
- The handoff's *Read* names `foundations/invariants.md` for the five invariants (`script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`); I read each of their entries whole. None of them changed the work.
- Nothing else was not found.

## Questions

1. Should a later slice add a test that compares `install.SKILLS` with `NAMES` (see *Choices* 3)? My recommendation: yes, as its own small slice, since it pins the installer's list at a point where a new skill would otherwise pass silently.

## Working copies

- None made: no worktree, clone or prepared input. The mutation was made in the worktree's `installation/install.py` itself and undone, as the handoff's check describes.
- The run logs were kept in `.runs/executor-3/`; the mutation log is kept at `.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-3-mutated-run.log`, and the other logs were removed.
