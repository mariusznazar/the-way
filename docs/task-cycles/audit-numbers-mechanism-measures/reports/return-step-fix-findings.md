# Findings to fix — the return step

The blocking finding of the review of the return step's commits (`reports/return-step-review-report.md`, head `a1b2d471b96479ab9e26d5e3cfdcaad20f90a23b`), copied word for word from the reviewer's report. The review's Minor findings (M1, M2) and the finding outside the task (O1) are not part of this fix.

### Important (blocking, within the task)

**I1. WAY-344 now lists two earlier-form readings; the code makes a third, and a test pins it.**
`foundations/decisions.md:11349-11353` (binding paragraph), `:11375-11378` (*complies*), and the *Rationale* price at `:11414-11418`.

What the entry says: the count reads a file as an earlier form, with no `Error:` and no change of the exit code, "for a stage report that has no heading of its detailed section and holds a table of tokens by model, and for one that has neither of its two time lines". The return step's report calls these two cases "the whole of what the count reads as an earlier form".

What the code does: a third case. `process-audit/audit_count.py:938-941` (`section_table`) says "the column *Files named* is never one [a missing field]: a section without it is the earlier form of the section". `audit_count.py:957` sets `named` from the header row, and `:1357-1358` (`fix_rounds_share`) turns a missing column into the share of fix rounds as unknown with the reason "`stages.md` has no column `Files named`: an earlier form", with no `Error:`. Test `process-audit/test_audit_count.py:1342` (`test_the_column_files_named_is_never_a_missing_field`) pins exit 0, no `Error:` and a cost, for a newer section without the column. I ran it: OK.

Why it matters: the paragraph's rule is that a missing field ends the count with exit 1 and an `Error:` line, and the two cases are its only listed exceptions. By the entry as worded, a detailed section whose table lacks the column *Files named* is a missing field and must give `Error:`. The code gives none, and its own test requires none. The entry says something narrower than what the code does, so a later reader or reviewer holding the code to WAY-344 would call the third reading a violation, and the *Rationale* price does not name it either (WAY-263: an entry the change writes that restates the code differently). The whole-change fix wording (`8bb47d5`, "where the file's other signs name that form") covered this case in general; the narrowing by this commit is what dropped it. The return step read `audit_count.py` lines 915-1026, which include the docstring at `:940`, and its comparison table does not mention the column.

Fix, one clause in three places: add to the cases in the binding sentence "and for a detailed section whose table has no column *Files named*", to the *complies* case "a stage report whose detailed section has no column *Files named*" and to the price in the *Rationale* ("or its section without the column *Files named*"). Keep the paragraph at three sentences.
