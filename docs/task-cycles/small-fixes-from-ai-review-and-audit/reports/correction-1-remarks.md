Uwagi doradcy dnia w imieniu Mariusza

**Fix or let through**

1. Fix it in this request — both parts.
   - Timing script (Minor finding 1, N1): "A line holding `== ` after text inside a nested run's own output, after one of its directories (for example `assert x == y` in a failing nested test), now makes the script count too few lines as nested." The fix traded a case the old rule read right for the one it repaired, and the result is a made-up directory with somebody else's time — a silent wrong answer in the gate times. Make the rule read both cases right and add a test for each (the confirmed input from N1 as one of them).
   - Missing `decision:` lines (Minor finding 4, M2): add the lines the return-step review listed, so each part named by the `tests:` clauses of WAY-339 and WAY-417 is reached through the sentence it holds (`process-audit/test_process_versions.py:2012`, `:1709`, `:1974`, `:1293`, `:1354`).
   - With it, Minor finding 3 (M1): the comment at `process-audit/test_series_summary.py:93` sends the reader to a pair of examples that no longer exists — correct it.
2. Let it through for the decisions on how findings are graded (WAY-161, WAY-263, WAY-363, WAY-365, WAY-409): the review restates them in its own method and read every decision about the audit and the gate times whole. WAY-02 (how a test quotes a decision) is different: this fix writes `decision:` lines, so the review of the fix reads WAY-02 whole and says so in its report.

**You accept by merging:** items 3–8 accepted. Minor finding 2 (layout only) — let through.

