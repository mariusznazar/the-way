# Findings for the fix of the whole-change review

Source: `reports/review-whole-report.md` (`PASS b2c31cc26504a51b445ec3210b0516444bcf3f5c`), range
`9cc26f3e..b2c31cc2`. No blocking findings. The five Minor findings below, within the task, are cut
from the report in the reviewer's words; the cycle fixes them in one round before the request opens.

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
