PASS ee4cbe3579f70fea04e25fa4567500964d798dfd

# Review of the fix — installer-preview-ignores-line-endings

- Range: `b2c31cc2..ee4cbe3579f70fea04e25fa4567500964d798dfd`, one commit, "Narrow the CRLF notes in
  the installation README and name the sources of FileActionTest", touching `installation/README.md`
  and `installation/test_install.py`. `git rev-parse HEAD` in the worktree gives the head the
  dispatch names. No code of `installation/install.py` changed.
- Bound: `reports/fix-findings.md`, five Minor findings within the task and no blocking ones. Only a
  new Critical or Important finding in the fix diff would fail this review (WAY-162).
- Counts: blocking 0. Findings fixed: 5 of 5. New in the fix diff: 1 Minor, within the task. Out of
  scope: 0.

## The findings of the findings file

1. **Fixed.** `installation/README.md:236` now reads "a file whose text differs in anything other
   than those line endings is rewritten with LF". It no longer claims the preview shows the real
   change. The claim is true of the code: any byte difference other than CRLF for LF gives
   `REPLACE` (`installation/install.py:517-520`), and the apply writes the new LF text
   (`:670-671`). The first half ("kept as it is and shows no difference") is unchanged and true.
2. **Fixed**, with a new Minor flaw in how it was written (see below). The row now says the
   definitions are copies "byte for byte as git stores them", and that a checkout may write them with
   CRLF, which the installer keeps. That agrees with `file_action` and with the sentence at `:233-236`.
3. **Fixed.** `installation/README.md:287-289` names the two new cases: a CRLF entry point or
   definition with the installer's text kept with no diff, not rewritten and answered "Already
   installed; no changes", and a CRLF file with a real change replaced with that change alone and
   written with LF. These match what
   `InstallTest.test_crlf_files_with_the_same_text_are_kept_and_not_rewritten` (`test_install.py:265`)
   and `test_a_crlf_file_with_other_text_is_replaced_and_shows_only_the_real_change` (`:288`) assert.
4. **Fixed.** `TEXT` (`installation/test_install.py:1079-1082`) and each test with an expected value
   (`:1100-1150`) now name To do item 1 of the task as their source (a human's judgement), with the
   reason the value follows from it. I checked each reason against its input:
   - the CRLF and mixed inputs differ only in CRLF for LF, so `KEEP`;
   - "Changed line.", a lone CR, `\r\r\n`, an empty file, the `\xff\xfe` bytes and a missing last
     line ending all differ in more than that, so `REPLACE`.
   None of the comments says anything the test does not do.
5. **Fixed** (kept with a comment, the first of the two ways the finding offered).
   `installation/test_install.py:1129-1132` says the two tests guard the comparison alone and why.
   The comment is true:
   - `plan()` refuses a file at an entry point's or a definition's path when `owned()` is false
     (`install.py:474-475`), which it is for an empty file (no header) and a non-UTF-8 file
     (`:338-341`, `:354-357`);
   - the foundations branch short-circuits before the comparison (`:517`).
   "The refusal itself is tested through the installer elsewhere" holds too. Non-UTF-8 files at a
   skill path are refused in `installation/test_testing_guidelines_installation.py:155-170` and
   `test_coding_guidelines_installation.py:166`, and at a definition path in
   `test_agent_types_installation.py:180-196`. A file that is not the installer's is refused in
   `test_install.py:682`, `:701`.

## New in the fix diff

### Critical

none

### Important

none

### Minor

1. `installation/README.md:60-61`: the fix splits one row of the table "Files in the product" across
   two lines. Line 60 now ends with "byte for byte as git stores them," and line 61 begins "and name
   no commit; a checkout may write them with CRLF line endings, …". A Markdown table row ends at the
   end of its line, and a non-blank line right after a table is read as another row (GitHub's table
   extension). So the rendered README shows the row of the definitions cut off after "as git stores
   them,". Under it comes a new row whose first column ("Path") holds the rest of the sentence: "and
   name no commit; … Codex has no such files." The text is still all there and still true, so a
   reader is not misled about what the installer does. But the table now has a row that names no
   path, in the README every product reads. Fix: join line 61 onto line 60. Within the task (it is
   in the fix of finding 2). Evidence: `sed -n '58,62p' installation/README.md` shows line 61
   starting with "and name no commit;" with no leading `|`.

## Declined to judge

none

## Checks run

| Check | Command | Exit | Result |
|---|---|---|---|
| Head of the range | `git rev-parse HEAD` | 0 | `ee4cbe3579f70fea04e25fa4567500964d798dfd`, as dispatched |
| Diff and log | `git log --stat b2c31cc2..HEAD`, `git diff b2c31cc2..HEAD` | 0 | one commit, two files, comments and README text only |
| The README table around the changed row | `sed -n '58,62p' installation/README.md` | 0 | line 61 is the second half of the row of line 60 (Minor 1) |
| Linter on the changed test file | the main checkout's `.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa --output-format concise installation/test_install.py` (0.17.1) | 0 | `All checks passed!` |
| The changed test class | `python -B -m unittest test_install.FileActionTest`, run in `installation/` | 0 | `Ran 9 tests`, `OK` |
| Where the refusal of the two unreachable inputs is tested | grep of `installation/` for `Existing integration file differs` and non-UTF-8 bytes; read `test_testing_guidelines_installation.py:155-170`, `test_agent_types_installation.py:180-196`, `test_install.py:704-730` | 0 | as in finding 5 |
| Reviewed worktree untouched | `git status --short` | 0 | empty |

Not run: `python -B gate/run_tests.py installation`. The fix changes only comments of the tests and
README text, the class those comments sit in passes, and the run takes about 14 minutes here. The
author reports exit 0, 73 tests OK, on this head. That claim was not repeated, so it is unverified
by me. The full gate was not run, as the dispatch forbids.

## Reaches beyond the dispatch

- `installation/test_testing_guidelines_installation.py:155-170`,
  `installation/test_agent_types_installation.py:180-210` and `installation/test_install.py:704-730`:
  read to check the claim of the new comment that the refusal is tested elsewhere.

## Working copies

None made. The unit run used `python -B` in the reviewed worktree, which writes no file, and
`git status --short` shows the worktree clean. `.runs/review-whole/`
stays empty, as the first round left it.

## Unread material

- `reports/review-whole-report.md` was written by me and not re-read; the findings file quotes it.
- The rest of `installation/test_install.py` beyond the diff and the lines named above was not
  re-read in this round.
- Otherwise none: the findings file, the fix report and the whole fix diff were read whole.

## Searches not found or unclear

- A test that refuses an empty file at an entry point's path specifically, as opposed to a file that
  is not the installer's or a non-UTF-8 file: not found by grep for `write_bytes(b"")` (only a
  `.gitignore` case at `test_install.py:635`). The comment of finding 5 does not claim the empty case
  by name, so this does not make it false.
