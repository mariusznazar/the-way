PASS b2c31cc26504a51b445ec3210b0516444bcf3f5c

# Review of the whole change — installer-preview-ignores-line-endings

- Range: `9cc26f3eb5121c19be28e647170019982d2b08c7..b2c31cc26504a51b445ec3210b0516444bcf3f5c`, one
  commit, "Keep installer files whose text differs only in CRLF line endings". `git rev-parse HEAD`
  in the worktree gives the head the dispatch names.
- Route: one author, no spec, no plan, so no slice; no finding comes from a slice.
- Counts: blocking 0, Minor 5 (all within the task), out of scope 0.

## Against the task

The task's one *To do* item is met:

- A file the installer writes that differs from the new text only in CRLF for LF gets `KEEP`
  (`installation/install.py:517-519`). The comparison folds only `\r\n` to `\n` on the bytes on
  disk. The new text never holds a `\r`: `committed()` reads `git show` through `subprocess` with
  `text=True` (`installation/install.py:83-84`, `:91-92`), which translates line endings, and
  `skill_wrapper` writes `\n` alone. So a kept file is one whose bytes equal the new text with some
  `\n` written as `\r\n`, and nothing else.
- No diff appears under a kept file (`run()` prints a diff only for `CREATE` and `REPLACE`,
  `installation/install.py:604-608`). The apply writes only `CREATE` and `REPLACE`
  (`:665-671`), so a kept file is not rewritten.
- With every file `KEEP` and the pin unmoved, `run()` prints "Already installed; no changes."
  (`:639-643`). The shared files already compare after folding CRLF (`agents_change` `:275`,
  `ignore_change` `:294`, `claude_change` keeps every existing file), so a product whose files are
  all CRLF reaches that line too.
- Out of scope, kept: a file with a real change is still `REPLACE`, its diff is computed on
  `splitlines()` (`:608`, `:523-525`), so the CRLF does not show as a change, and the apply writes
  the new text with LF (`:671`). The test `test_a_crlf_file_with_other_text_is_replaced_and_shows_only_the_real_change`
  pins all three.

The task carries no *Settlements to record* and no projected entry. The foundation entries that the
change reaches — WAY-34, WAY-368 and the invariants listed below — say nothing that the code now
contradicts. Part-map entry `installation-command` ("rewrites only its own") still holds: the
change rewrites less, not more.

## Trust boundary (`installation/install.py`), crafted input

I ran `file_action` and `shown_diff` from a worktree of the head and from a worktree of the base on
twelve crafted inputs against the new text `# Skill\n\nFirst line.\nSecond line.\n`. Result, head
(base in brackets where it differs):

| Input on disk | Action | Diff lines shown |
|---|---|---|
| LF, same text | KEEP | 0 |
| CRLF, same text | KEEP (base REPLACE) | 0 |
| mixed CRLF and LF, same text | KEEP (base REPLACE) | 0 |
| lone CR between two lines | REPLACE | 0 |
| `\r\r\n` at one line end | REPLACE | 8 |
| missing last LF | REPLACE | 0 |
| missing last CRLF | REPLACE | 0 |
| an extra CRLF at the end | REPLACE | 7 |
| CRLF, other text | REPLACE | 8 |
| empty | REPLACE | 7 |
| UTF-8 BOM and CRLF | REPLACE | 8 |
| form feed where a line ending stood | REPLACE | 0 |

Only the two rows the task requires changed from `REPLACE` to `KEEP`. No file whose text really
differs became `KEEP`. Inputs `file_action` does not reach in a real run:

- A symlink at an entry point's or a definition's path: `plan()` refuses it first through
  `owned()` (`:336`, `:352`, `:474-475`). A link on a parent path: `check_parents` (`:323-328`).
  A foundation file that is a link: `:471-473`. None of these changed. Invariant
  `installation-paths-through-links` keeps its tests, and they pass.
- An empty file or a non-UTF-8 file at an entry point's path: `owned()` is false for both (no
  header, or a `UnicodeDecodeError`), so `plan()` stops the run before `file_action` (see Minor 5).

The rows with 0 diff lines under `REPLACE` (lone CR, missing last line ending, form feed) show
exactly the same on the base. They are not a regression, but see Minor 1.

## Findings

### Critical

none

### Important

none

### Minor

1. `installation/README.md:235-236` — the sentence the change adds says "a file whose text differs
   is shown with its real change and written with LF". This is not true for every file whose text
   differs. The preview diff is computed on `str.splitlines()` (`installation/install.py:523-525`,
   `:608`), which treats a lone `\r`, a form feed and a missing last line ending the same as `\n`.
   So such a file is shown as `REPLACE` with nothing beneath it. Evidence: my probe, rows "lone
   CR", "missing last LF", "missing last CRLF" and "form feed" above, all 0 diff lines. The
   behaviour predates the change and no checkout writes such a file. The flaw is only that the new
   sentence claims more than the code does. Fix: narrow the sentence, for example "a file whose
   text differs is rewritten with LF, and the preview shows the lines that differ". Within the task
   (the sentence is part of this change).
2. `installation/README.md:60` — the row of the agent definitions says they "are copies of
   `task-cycle/agent-types/` at the pinned commit, byte for byte". After this change a definition
   kept with CRLF is no longer a byte-for-byte copy in the working tree. Git stores it with LF, so
   the stored blob is still identical. A reader who compares this row with `:233-236` can read the
   two as contradicting each other. Row `:59` ("The same entry points for Codex, byte for byte")
   holds while both tool directories come from one checkout. Fix: name what is byte for byte, the
   text git stores, or add "apart from CRLF line endings that a checkout writes". Within the task.
3. `installation/README.md:278-301` ("Check the installer") lists every case the tests check, and
   the list does not name the new ones: a CRLF entry point or definition kept with no diff and no
   rewrite and answered "Already installed; no changes", and a CRLF file with a real change
   replaced with its real change alone and written with LF. The list is now incomplete, not false.
   Within the task.
4. `installation/test_install.py:1074-1127` (`FileActionTest`) — the values its tests depend on
   (`TEXT` at `:1079`, each crafted input, each expected `KEEP` or `REPLACE`) carry no source in a
   comment. The *Data* field of the recipe binds this (WAY-395), and so does
   `guidelines/testing.md` "Where the expected value comes from": "Where a test's name does not show
   the source of a value, a comment in the test names it." The two `InstallTest` methods carry
   their source (`:268-270`, `:289-291`), and the `FileActionTest` ones carry only "Break caught".
   This matters most for the cases the author's report calls its own judgement (choices 2, 4 and 5:
   lone CR, missing last line ending, empty, non-UTF-8). An agent's judgement is none of the sources
   the guidelines allow. The values do follow from the task's *To do* item 1 ("differs only in line
   endings (CRLF instead of LF)": a file that differs in anything else is no such file), so the
   source exists and only the comment naming it is missing. Within the task.
5. `installation/test_install.py:1118-1122` (`test_an_empty_file_is_replaced`,
   `test_a_file_that_is_not_utf8_is_replaced`) — in a real run neither input reaches `file_action`
   at an entry point's or a definition's path. `plan()` stops the run first, since `owned()` is
   false for an empty or non-UTF-8 file (`installation/install.py:336-345`, `:352-360`,
   `:474-475`). At a foundation path the foundations branch keeps every file before the comparison
   (`:517`). So both tests pin a path no run takes, which is a "test without value" example of
   `guidelines/testing.md` (`## Examples`, non-binding). The refusal they stand for is already
   tested elsewhere: a non-UTF-8 file at a skill path, for example. Keep them with a comment saying
   they guard the comparison alone, or drop them. Within the task.

## Declined to judge

none

## Tests against the guidelines

- Levels. `FileActionTest` is a files test (temporary directory, no git), the lowest level for
  `file_action`, which reads a file (WAY-393, "Choosing the level"). The two `InstallTest` methods
  are git tests on the existing fixture. They are needed because "not rewritten" and "Already
  installed; no changes" live in `run()` and need a product repository. The git test names as its
  break the return of the raw-byte comparison, which the files test also catches. It also protects
  the preview, the apply and the rerun, which only it reaches, so it is not a duplicate.
- Expected values. They are literals or come from the test's own `ENTRY_POINT` template and
  `NAMES` table. None is computed by `install.py`. The test `entry_point()` helper reads the
  skill's description through `git show` in the test itself, not through the installer.
- Old code. On the base with the new tests the three tests the author names fail, and only those.
  The guard passes on both, as the author's report says (see checks).
- Assertions. Each one checks behaviour the task names: `KEEP` lines, no `REPLACE`, no diff header,
  the "Already installed" line, unchanged bytes, and the real change in two diff lines.
  `assertNotRegex(... (---|\+\+\+) ...)` alone would pass on the old code, because the old diff
  under a CRLF `REPLACE` was empty. The `KEEP` assertions are what fail there, so the test still
  catches the break.

## Structure of the code

- `python -B task-cycle/change_file_sizes.py`: `installation/install.py` 693 to 696 (+3);
  `installation/README.md` 302 to 305; `installation/test_install.py` 1014 to 1131 (a test file,
  outside the size rule).
- Size invariant `function-and-file-size` (`Violated: yes`). I took the expected-failure mark off in
  a worktree of the base and one of the head and ran the test in each. Both name the same 11
  functions and 2 files. `installation/install.py` `run` has 120 lines on both, at `:564` on the
  base and `:567` on the head. Nothing new goes over a threshold. `run()` gains no line, since the
  diff touches only `file_action`, which has 9 lines.
- Linter: the pinned Ruff 0.17.1 with `--ignore-noqa` gives the same two reports on
  `installation/install.py` on base and head (`:83` UP022, `:467` PERF102), lines the change does
  not touch, and none on the head's `installation/test_install.py`. The author's claim holds.
- No code is left without a user, and no name stopped being true.

## Checks run

| Check | Command | Exit | Result |
|---|---|---|---|
| Head of the range | `git rev-parse HEAD` | 0 | `b2c31cc26504a51b445ec3210b0516444bcf3f5c`, as dispatched |
| Diff and log | `git diff 9cc26f3e..b2c31cc2`, `git log 9cc26f3e..b2c31cc2 --stat` | 0 | one commit, three files |
| Index of the selection | `python -B elements/common/decision_index.py --output .runs/review-whole/index.md --section "Skills and agent types in sessions" --section "Instruction files" --section "The-way's own coding and testing guidelines" --section "Scripts and the gate" --part installation --decision WAY-34 --decision WAY-379 --decision WAY-392` | 0 | 45 in full, 8 by heading (first tries with `--decision 34` and `--decision WAY-328` ended with exit 2: the number form and the withdrawn WAY-328) |
| File sizes | `python -B task-cycle/change_file_sizes.py 9cc26f3eb5121c19be28e647170019982d2b08c7 b2c31cc2` | 0 | as above |
| Size invariant, base, mark off | `python -B -m unittest test_size_invariant.Size` in `agent-instructions/` of the base worktree | 1 | 11 functions, 2 files, `install.py` `run` 120 |
| Size invariant, head, mark off | the same in the head worktree | 1 | the same list |
| Linter, head | `ruff.exe check --config ruff.toml --no-cache --ignore-noqa --output-format concise installation/install.py installation/test_install.py` (the main checkout's `.runs/quality-venv`, 0.17.1) | 1 | 2 old reports in `install.py`, none in the test file |
| Linter, base | the same on `installation/install.py` | 1 | the same 2 reports |
| Installation tests, head (reviewed worktree) | `python -B gate/run_tests.py installation` | 0 | `Ran 73 tests`, `OK` |
| New tests on the old code | head's `installation/test_install.py` copied into the base worktree, `python -B gate/run_tests.py installation` | 1 | `Ran 73 tests`, `FAILED (failures=3)`: `FileActionTest.test_the_same_text_with_crlf_endings_is_kept`, `FileActionTest.test_the_same_text_with_mixed_endings_is_kept`, `InstallTest.test_crlf_files_with_the_same_text_are_kept_and_not_rewritten` (the base preview shows `REPLACE` for all 44 entry points and both definitions) |
| Crafted inputs at the boundary | a probe script calling `install.file_action` and `install.shown_diff` of the head and of the base on 12 inputs | 0 | the table above |
| Reviewed worktree untouched | `git status --short` | 0 | empty |

Not run: the full gate, which the dispatch forbids. A symlink at an entry point's path was not run
by hand. Creating one needs extra rights on Windows, and the code path that refuses it is unchanged
(read in `owned_entry_point`, `owned_agent_definition`, `plan`).

## Reaches beyond the dispatch

- `foundations/invariants.md`, the invariants whose *Part* names `installation` or `every`, read
  whole by step 3 of "Reading the foundation", to check that no invariant describes the byte
  comparison.
- `foundations/part_map.md:192-235`, the entries `installation` and `installation-command`
  (step 3, trust boundary).
- `installation/README.md:50-69` and `:195-305`, to judge the added sentence and any sentence the
  change makes false (handoff, step-4 answer).
- `product-guidelines/reading.md` (method, section 1).

## Working copies

All of them were in `.runs/review-whole/`:

- the worktree of the base, `.runs/review-whole/base` (with the size test's mark off and the head's
  test file copied in), and the worktree of the head, `.runs/review-whole/head` (mark off). Both
  were removed with `git worktree remove --force`, then `git worktree prune`;
- `index.md`, `sections.md` (the decision index), `size_base.txt`, `size_head.txt`,
  `tests_head.txt`, `tests_base_with_new_tests.txt`, `base_test_install.py`, `probe.py` and
  `probe-files/`. All were removed, and what the report needs is quoted above.

The directory `.runs/review-whole/` stays, empty, as the handoff names it. No remainder. The
worktree `.runs/base` that
`git worktree list` shows is not mine; I left it.

## Unread material

- Decisions of the index read whole: 5 of 53 (WAY-34, WAY-368, WAY-385, WAY-393, WAY-394). The
  others were read through their binding sentences in the index. Of the 8 listed by heading alone
  (WAY-09, WAY-27, WAY-100, WAY-102, WAY-107, WAY-321, WAY-324, WAY-167), none has a question that
  bears on a comparison of line endings in the installer, so none was opened.
- Guideline files: none unread. I read whole `guidelines/coding.md`,
  `guidelines/coding-repository-changer.md` (`install.py` is in its table) and
  `guidelines/testing.md`. The other kind files do not match the work.
- `installation/README.md`: lines 1-49 and 70-194 were not read. They hold the product's setup and
  the section on CI, which the change does not reach. A grep of the whole file for `KEEP`,
  `REPLACE`, `CRLF`, `line ending`, `byte for byte`, `differs` and `rewrit` found no other
  sentence on the comparison.
- `installation/install.py`: lines 1-225 and 226-696 read, so the whole file.
  `installation/test_install.py`: the diff and lines 1-30, 100-110 and 180-190 were read. The rest
  of the file was not, beyond what the test run shows.
- Glossary: the entries `files test` and `git test` were not opened. I used them only as the
  guidelines use them.

## Searches not found or unclear

- `decision_index.py --decision 34` and `--decision WAY-328`: exit 2. The script takes `WAY-34`,
  and WAY-328 is withdrawn (`foundations/decisions.md:10949`, successors WAY-379 · WAY-392). I ran
  the index with the successors.
- A foundation entry that describes the preview's `KEEP` or `REPLACE` or the byte comparison: none
  found in the invariants of the touched part or in the part map entries, which matches the
  author's search.
