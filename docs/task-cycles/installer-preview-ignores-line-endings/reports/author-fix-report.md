# Author fix report — installer-preview-ignores-line-endings

**Status:** done
**Commit:** `ee4cbe35` on `task/installer-preview-ignores-line-endings` (on top of `b2c31cc2`; not pushed)
**Files:** `installation/README.md`, `installation/test_install.py` (no code change)

## Findings

1. **Sentence on CRLF files claims too much (README).** Done. The sentence now reads: a file whose
   text differs "in anything other than those line endings is rewritten with LF". I dropped "shown
   with its real change", since a lone CR, a form feed or a missing last line ending gives no diff lines.
   The kept-file part ("kept as it is and shows no difference") stands: a kept file gets no diff.
2. **Agent-definition row says "byte for byte" (README row at line 60).** Done. It now reads "byte for
   byte as git stores them" and adds that a checkout may write CRLF, which the installer keeps. Row 59
   (the Codex entry points) I left as it was, since both copies come from one write and the reviewer
   found it holds.
3. **"Check the installer" list is incomplete (README).** Done. The list names the two new cases: a CRLF
   entry point or definition kept with no diff, not rewritten, answered "Already installed; no changes";
   and a CRLF file with a real change replaced with that change alone and written with LF.
4. **FileActionTest has no source comments.** Done. The class carries a comment on `TEXT` naming To do
   item 1 of the task as the source (a human's judgement). Each test with an expected value now has a
   "Source:" comment: the CRLF case, the mixed case, the changed-text case, the lone-CR case, the
   missing-last-ending case, and the empty and non-UTF-8 cases. Each names To do item 1 and says why its
   value follows from it.
5. **Empty and non-UTF-8 tests reach no run.** Held with a comment, not dropped. The class now has a
   comment above the two tests saying they guard the comparison alone, that `plan()` refuses such a
   file at an entry point's or definition's path before the comparison, and that the foundations branch
   keeps foundation files earlier. Reason for keeping: `file_action` is the unit that decides KEEP or
   REPLACE, and these two inputs are the boundary of its comparison; dropping them would leave the
   comparison's behaviour on those bytes unpinned. Cost if wrong: two small unit tests of a function
   no run reaches with those inputs.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Installation tests | `python -B gate/run_tests.py installation` | 0 | `Ran 73 tests`, `OK` |
| Pinned ruff, changed test file | `the pinned ruff binary of the main checkout's quality environment check --config ruff.toml --no-cache --output-format concise installation/test_install.py` | 0 | `All checks passed!` |
| Pinned ruff, `install.py` (not changed in this fix) | same, on `installation/install.py` | 1 | 2 pre-existing reports: `install.py:83` UP022, `install.py:467` PERF102, both on lines unchanged since the base commit; the foundation records `ruff-blocking-rules` as `Violated: yes` |

No code changed in this fix, so the `install.py` reports are the same as in the first report.

## Unread material

- `reports/review-whole-report.md`: not read. The findings file quotes its evidence, and the findings
  file is the handoff the coordinator named.
- Otherwise none beyond the first report's list: the README lines I edited were read in the first round.

## Searches not found or unclear

- None. The README row at 59 and the list in "Check the installer" were found by grep and section read.

## Working copies

- `.runs/author/`: I wrote `fix_run.txt` (the test output, deleted after reading) and
  `fix-commit-message.txt` (the commit message, deleted after committing). Both are removed. No worktree
  or clone was made. The `.runs/base` gate run was not touched.
