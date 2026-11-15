# Executor report — slice 2 (the sections of a definition written out in the readiness test, and the refusal invariant of `readiness_check.py`)

**Status:** done

**Commit:** `d113238` — "Write the sections of a definition out in the readiness test and cite the refusal invariant of the UTF-8 check" (branch `task/the-way-coding-and-testing-guidelines`, base `162bff8`).

**Files changed:** `project-level/test_readiness_check.py` — 22 insertions, 7 deletions. No other file changed; `project-level/readiness_check.py` is at its committed state (`git diff -- project-level/readiness_check.py` empty, `git status` clean apart from nothing).

**One-line check result:** all focused checks pass (unit tests 79/79, ruff clean, `foundation_check.py --skip-test-citations` exit 0); the full `foundation_check.py` without the flag still reports 11 uncited invariants of later slices, none of them this slice's.

## What the slice changed

1. A module-level constant `FORM` in the test file, written out with a comment naming its source, `project-level/definition_template.md` (the headings of the form, in order: the twelve sections above the gate record, then `Gate record`). It replaces every use of `readiness_check.SECTIONS` in the file: the `definition()` helper, the three structure tests (missing, standing twice, out of order), the Technology-missing test, and the two `body_text` calls in the gate-record and fingerprint tests. Seven occurrences in all, each `FORM[:-1]` or `list(FORM[:-1])`.
2. A new test in class `Template`: `test_the_sections_written_in_this_file_are_the_headings_of_the_form` — reads the form block of the template and asserts its `## ` headings equal `list(FORM)`. This ties the written list to its source, so the comment is checkable.
3. The citation `# invariant: readiness-check-refuses-non-utf-8` as the first line of the body of `test_a_file_that_is_not_utf_8_exits_two`, as the file's other tests cite theirs (`test-method-citation`).

## Checks (command and exit code)

Before any edit:
- `python -B project-level/test_readiness_check.py` — exit 0 (79 tests, OK).
- `<main checkout>/.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa project-level/test_readiness_check.py` — exit 0, "All checks passed!".
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0.

After the edits (the commit state):
- `python -B project-level/test_readiness_check.py` — exit 0 (79 tests, OK). Run again after the commit: exit 0.
- ruff command above — exit 0, "All checks passed!" (the slice's lines are clean; the file's older lines at 77, 205, 294, 299, 371, 373 are over 100 columns but ruff does not select E501, and they are not mine).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0.

Failing run 1 — the sections test (`SECTIONS` changed for a moment):
- Edit: `project-level/readiness_check.py`, the tuple `SECTIONS` without `"Risks"`.
- `python -B project-level/test_readiness_check.py` — exit 1, `FAILED (failures=69)` of 79. Among them `Whole.test_a_whole_approved_definition_has_no_finding` and `Template.test_the_form_the_template_gives_has_the_structure_the_check_reads` (the representative tests for the sections; the run had no single "sections test" of its own, so this is the set).
- Undone: `git checkout -- project-level/readiness_check.py`; `git status` shows no change to that file.

Failing run 2 — the cited test (refusal broken for a moment):
- Edit: `project-level/readiness_check.py`, `read()` opens with `errors="replace"` instead of refusing bytes that are not UTF-8.
- `python -B project-level/test_readiness_check.py` — exit 1, `FAILED (failures=1)`: `Command.test_a_file_that_is_not_utf_8_exits_two`.
- Undone: `git checkout -- project-level/readiness_check.py`; the suite afterwards exit 0.

Full foundation check, for information: `python -B elements/common/foundation_check.py` — exit 1, 11 errors, all of invariants not yet cited by a test (`ruff-blocking-rules`, `function-and-file-size`, `generator-writes-only-with-write`, `repository-changer-acts-only-when-told`, `command-runner-passes-exit-code`, `shared-module-import-runs-nothing`, `cycle-stages-refuses-crafted-names`, `cycle-measures-refuses-nested-line`, `gate-times-refuses-impossible-entry`, `audit-count-refuses-record-links`, `check-instructions-refuses-outside-links`). `readiness-check-refuses-non-utf-8` is not among them (grep count 0).

Not run: `python -B gate/run_tests.py` (the whole gate, WAY-160, forbidden to the executor); `python -B gate/run_tests.py project-level` (not named by the slice's checks; the focused file run covers it).

## Own-work check (section 3 of the method)

- **Requirement most likely unmet:** that the sections list is now a source of its own — a section dropped from `readiness_check.SECTIONS` must make the tests fail, and the written list must really be the template's headings, not a copy of the code.
- **Check:** failing run 1 (69 failures, the whole-definition test among them) and the new template test (passes, so the written list equals the form's headings).
- **Second requirement:** the cited test must be the one that fails when the refusal breaks — failing run 2 shows that it is.
- **Crafted input at the trust boundary** (`project-level/readiness_check.py`; the slice did not change the file, so this is a check of its behaviour on hostile input). Inputs made in `.runs/executor-2/crafted/`, each run as `python -B project-level/readiness_check.py <file>`:
  - a directory given as the path: exit 2, "cannot read …: Permission denied" (handled as an OSError, no traceback);
  - a file containing the UTF-8 encoding of a surrogate (bytes ED A0 80): exit 2, "is not UTF-8 text";
  - a file with bytes FF FE after a heading: exit 2, "is not UTF-8 text";
  - a file with a UTF-8 byte-order mark before the title: exit 1, 13 findings (every section reported missing; no crash, no refusal as non-UTF-8);
  - a file with NUL bytes between text: exit 1, 13 findings (no crash);
  - an empty file: exit 1, 14 findings (no crash);
  - a path to no file: exit 2, "no file …";
  - no argument: exit 2 (argparse usage);
  - `--fingerprint` on the surrogate file: exit 2; on the BOM file: exit 1.
  No traceback in any run. Observation, not a finding of this slice: a definition with a BOM is not refused as non-UTF-8 but reads as having no sections; whether that is wanted is outside this slice.

## Choices made (way rejected, cost if wrong)

1. Name `FORM`, not `SECTIONS`. Way rejected: keeping the name `SECTIONS` in the test, which would look like the code's tuple and hide where the data comes from. Cost if wrong: a rename, nothing else.
2. Added the test `test_the_sections_written_in_this_file_are_the_headings_of_the_form` — not among the changes the slice names. Way rejected: the comment alone as the source. Cost if wrong: the written list could drift from the template and no test would show it; the test is a one-function removal if the orchestrator rules it out of scope.
3. `FORM[:-1]` relies on `Gate record` being the last heading of the form. The template test pins that order, so a change to it fails there. Way rejected: a separate `BEFORE_GATE` tuple, which would repeat the twelve names. Cost if wrong: none seen.
4. The citation sits as the first line of the test body, as the other tests in the file do (not above the `def`).

## Reach beyond the handoff (what, where, why)

- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md` read whole — the method (the handoff names them).
- `ruff.toml` read whole — the rules the file must not break; the handoff names the file only as the config of the check.
- `project-level/definition_template.md` and `project-level/readiness_check.py` read whole, where the handoff names lines 39-75 and 1-52 — the form's source must be checked in full, and the file is the boundary the slice names.
- `foundations/environment_facts.md` lines 18-28 (`utf-8`) — the entry E28 rests on; the handoff does not name it. Why: to know what the citation rests on.
- `foundations/invariants.md` lines 488-496 (E28) and 160-180 (`test-method-citation`) — read in place of the handoff's ranges, as the entries are written; the handoff's ranges (166-175) are inside what I read.
- `foundations/decisions.md` 10113-10139 (WAY-394, E11) — read whole.
- `a file of the author's private notes` — read because the user's rules require it before a commit; a hook also delivered it.

## Unread material

- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` lines 14-66 (the plan's *Foundation entries*) — not read; the entries E11 and E28 were read as written in `foundations/`, which is what the handoff gives as their text.
- `foundations/invariants.md` script-language, script-imports, script-subprocesses, cross-part-imports and test-method-citation — read whole (the orchestrator's additions); none read in part.
- Everything else the handoff names: read whole or in the range it gives.

## Searches not found or unclear

- `grep` of `SECTIONS` in `project-level/` found the seven uses in the test file and the definition of the tuple in `readiness_check.py`; no other user of `readiness_check.SECTIONS` exists in the repository's Python files (`project-level/plan_check.py` has its own `SECTIONS`, not related).
- Unclear: the handoff's Checks say "the section test shown failing" without naming a test. I ran the whole file with the tuple changed and report the whole run and the whole-definition test as the representative; if the orchestrator meant one named test, that run stands.
- Not found: nothing sought in the repository was missing.

## Working copies

- `.runs/executor-2/` held the crafted input files (`crafted/`) and the run outputs of the failing runs (`sections_broken.txt`, `refusal_broken.txt`, `final_run.txt`, `fc_full.txt`). Removed with `rm -rf` before the commit; `.runs/` now holds only `task-cycles/`. It was not a git worktree, so no `git worktree remove` was needed. Nothing remains.

## Problems observed

- None in the slice's own code.
- The full `foundation_check.py` is red by design until the later slices cite their invariants (see Checks).
- A first `git commit` was blocked by a hook that delivers a rules file once per session; the command was repeated unchanged and went through. No effect on the commit.
