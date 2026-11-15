PASS d113238f887a7ba565bb667d2c638b3ab9c98b22

# Review of slice 2 (range `162bff8..d113238`)

`git rev-parse HEAD` of the worktree is `d113238f887a7ba565bb667d2c638b3ab9c98b22`, the head given. One commit, one file: `project-level/test_readiness_check.py`, 22 insertions, 7 deletions. `project-level/readiness_check.py` is not in the range's diff.

## Findings

Blocking (Critical or Important): none.

Minor: none.

Out of scope: none.

### What I checked against the task, foundation and slice

- **Cause 1 removed.** `FORM` (`project-level/test_readiness_check.py:25-31`) is written out, with its source named in the comment. It is the thirteen headings of the form in `project-level/definition_template.md:41-75`, in order. Every one of the seven former uses of `readiness_check.SECTIONS` in the file now takes `FORM[:-1]` (lines 100, 177, 179, 191, 389, 529, 581). `grep SECTIONS` in `project-level/test_readiness_check.py` finds only the comment at line 27. The `SECTIONS` of `plan_check.py` and `test_plan_check.py` is a different tuple and not this slice's.
- **The written list is tied to its source.** The added test `test_the_sections_written_in_this_file_are_the_headings_of_the_form` (line 123) reads the form block of the template and compares its `## ` headings with `FORM`. Nobody asked for it, but it keeps the comment's claim true, it is small, and it fails when `FORM` drifts (shown below). Not graded as an addition nobody asked for: it serves the goal "written out with its source".
- **Citation (item 8).** `# invariant: readiness-check-refuses-non-utf-8` is the first line of the body of `test_a_file_that_is_not_utf_8_exits_two` (line 586), the form the file's other tests use. It matches E28 in `foundations/invariants.md:488-496` (method `test`, exit 2 and a message "not UTF-8 text"); the test asserts exactly exit 2 and "is not UTF-8 text".
- **WAY-394 (E11).** The expected values of the changed lines come from the template (the headings) and from the description at the head of the script (exit 2); nothing is taken from a constant of the code under test any more. The existing exit-code tests carry no comment naming the description at the head of the script that WAY-394's *complies* line asks for. That comes from earlier code the slice does not touch, and the slice's Goal does not ask for it; I set it aside (Declined to judge).
- **Trust boundary.** The slice does not change `readiness_check.py`. Crafted input at its file read (`read()`, lines 311-320), run by me on the head: bytes `FF FE` and a surrogate encoding `ED A0 80` in a definition give exit 2 "is not UTF-8 text", also with `--fingerprint`; a directory as the path gives exit 2 "cannot read ...: Permission denied"; no traceback. The change only does what the slice says.
- **Tests fail when the behaviour breaks.** See the checks.
- **Guidelines.** The product has no coding or testing guidelines of its own at the plan's base (the plan's Choices say the rule of size binds after this task merges); nothing to compare. Ruff is clean on the file.
- **Invariants of the orchestrator's additions** (`script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`): the slice adds no import, no subprocess and no new language; `test-method-citation` is met for E28 (the check with citations on lists no error for it, per the executor's run and its absence from the citation rule's own reach in my `--skip-test-citations` run; I did not run the full one, see below).
- **Executor's claims.** The report's claims I relied on I reran (below); all held. Its "69 failures" with `Risks` dropped from the tuple I did not count; I saw failures in `Structure`, `Template` (`test_the_form_the_template_gives_has_the_structure_the_check_reads`) and `Whole` classes, which is the same behaviour.

## Declined to judge

- The exit-code tests of the file do not name the description at the head of `readiness_check.py` in a comment at the value (WAY-394 *complies* line): earlier code, outside this slice's goal.
- A definition with a UTF-8 byte-order mark reads as having no section instead of being refused (the executor's observation): behaviour of `readiness_check.py`, outside this slice.

## Checks (in a detached worktree of `d113238`, `.runs/review-2/wt`)

- `python -B project-level/test_readiness_check.py` — exit 0, 79 tests OK.
- `<ruff> check --config ruff.toml --no-cache --ignore-noqa project-level/test_readiness_check.py` — exit 0, "All checks passed!".
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 ("0 errors").
- Section test shown failing: `"Risks"` taken out of the tuple `SECTIONS` in `readiness_check.py` for a moment (`git diff --stat` showed that one line) — `python -B project-level/test_readiness_check.py` exit 1; failures include `Structure.test_a_missing_section_is_reported`, `Structure.test_a_section_standing_twice_is_reported`, `Structure.test_sections_out_of_order_are_reported`, `Template.test_the_form_the_template_gives_has_the_structure_the_check_reads`, `Whole.test_a_whole_approved_definition_has_no_finding`. The change was undone with `git checkout -- project-level/readiness_check.py`.
- The new template test shown failing: `"Risks"` taken out of `FORM` in the test file for a moment — `Template.test_the_sections_written_in_this_file_are_the_headings_of_the_form` fails (other tests listed under `Template` showed only this one); undone with `git checkout -- .`; `git status --short` empty.
- Cited test shown failing: `errors="replace"` put into the `open` of `read()` for a moment — exit 1, `FAILED (failures=1)`, the one failure `Command.test_a_file_that_is_not_utf_8_exits_two`; undone, `git status --short` empty.
- Crafted input: three runs of `python -B project-level/readiness_check.py` on a file with bytes `FF FE` and `ED A0 80`, on a directory, and with `--fingerprint` — exit 2 each, no traceback.
- `git diff 162bff8 d113238 --stat -- project-level/readiness_check.py` — empty.
- Not run: `python -B elements/common/foundation_check.py` without the flag (the later slices' invariants are uncited by design; the executor reported 11 errors none of which is E28, and my `--skip-test-citations` run is the check the slice names); the whole gate (forbidden to a reviewer).

## Reach beyond the dispatch

- `project-level/readiness_check.py` read to line 60 and `read()` and `main()` (lines 311-336) — to check that the broken-for-a-moment edits touch the refusal and the tuple, and the boundary. The handoff names lines 1-52.
- `foundations/decisions.md` WAY-394 (`:10113-10139`) — the handoff names E11 by identifier only; read whole to judge the expected values.
- `foundations/invariants.md:488-496` (E28) and `:160-180` — read as the handoff names them by identifier.
- `.runs/task-cycles/.../task.md:34-38, 177-181, 232-238, 543` and the end of `plan.md` — the passages the handoff names.

## Unread material

- `foundations/decisions.md` WAY-48, WAY-235, WAY-08, WAY-232, WAY-233 (named in the handoff's *Read*): not read whole; WAY-232 only through the passage WAY-394 quotes, the others not opened — the slice changes only a test's data and one citation, and E28 names WAY-48 · WAY-235 as its source.
- `foundations/invariants.md` `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`: not read whole; the slice adds no import, no subprocess and no new language file, so I judged them by the diff (an invariant-by-invariant read is not recorded).
- `foundations/part_map.md:80-99` (project-level): not read; the slice adds no file.
- `project-level/definition_template.md:39-75` read; `project-level/readiness_check.py` read in the parts named above.

## Searches not found or unclear

- none

## Working copies

- `.runs/review-2/wt`, a detached worktree of `d113238`, and `.runs/review-2/c.md`, the crafted input: removed (`git worktree remove --force`, `git worktree prune`, `rm -rf .runs/review-2`); `.runs/` holds only `task-cycles/`. Nothing remains. The reviewed worktree has no change (`git status --short` empty).
