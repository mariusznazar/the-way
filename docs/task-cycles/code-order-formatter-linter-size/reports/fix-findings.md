# Findings of the review of the whole change to fix (Minor, within the task), in the reviewer's words

Source: `reports/review-whole-report.md`, first line `PASS d0a861d9ca22cb2a1cb364d8224bc01f3cd65a44`, section *Minor — within the task*. Finding 2 of that report has no code to change (its fix is a sentence in the request) and is left out here; finding 11 is outside the task.

1. **A `yapf: disable` comment switches the formatter off and the gate stays green.**
   `agent-instructions/test_linter_invariant.py:49` (`FORMATTER_SWITCH`) and the class `Formatter` at
   `agent-instructions/test_linter_invariant.py:176-197`. Ruff 0.17.1 takes `# yapf: disable` and
   `# yapf: enable` as it takes `# fmt: off` and `# fmt: on`; the test's pattern finds only the three
   `fmt:` comments. A file can so stand outside the formatter's layout with both tests of
   `formatter-layout` passing — the consequence the task's answer "Czy komentarze wyłączające formater
   są zakazane? — tak (a)" names under its rejected way (b). Evidence: in
   `.runs/review-whole/yapf/` a file `X = 1` / `# yapf: disable` / `Y = [1,2]` / `# yapf: enable` /
   `Z = 1` gave `ruff format --check --config ruff.toml --no-cache` "1 file already formatted" (exit 0
   for that file), while the same file with `X = [1,2]` above the comment was reported; the pattern
   `\bfmt:\s*(?:off|on|skip)\b` does not match `yapf: disable`. Why Minor and not blocking: the code
   does what the settlement row 5, WAY-382 and `formatter-layout` say word for word — they name the
   three `fmt:` comments — and no file of the-way holds a `yapf:` comment today. The fix is the
   pattern widened to the two `yapf:` comments together with the words of WAY-382's second paragraph
   and of `formatter-layout` (both written by this change, F1 and F4), so it reaches a foundation
   entry and is the human's to accept; were it left, the request should name the gap.
3. **`README.md:106-107` still calls `ruff.toml` "the settings of the linter".** Since
   `6c13454c` the file also holds the formatter's width and its exclusion of Markdown (WAY-382), and
   the list of the repository's files there names neither the formatter nor `.git-blame-ignore-revs`.
   A name that stopped being true with this change; the agent of slice 3 saw it and left it as
   outside its section. Fix: "the settings of the linter and the formatter".

4. **`task-cycle/gate_times.py:213-216` and `:239-242` name the parsed name of a registry file
   `file`.** `file = parse_name(name)` holds a tuple (start, end, token), not a file or a path; the
   slice 10 renaming made `entry` into `file`, which reads as a path or an open handle beside the
   real file names of the same loops. Polish; a name such as `parsed` or `run` would say what it is.

5. **The test name `test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list`**
   (`process-audit/test_record_items.py`, renamed in `462add5d` from
   `test_a_sub_entry_under_the_first_entry_is_no_entry_of_the_list`). The record it reads holds a
   nested list item under the first sub-item; "a deeper line" drops that the line is itself a list
   item, which is what the test is about. Graded as the slice 10 review graded it: wording only.

6. **`guidelines/coding-shared-module.md:4` (*Applies to*) and `:38-41` (*Where in code*) do not name
   `task-cycle`, where `task-cycle/stage_transcripts.py`, a module of the kind `shared-module`, now
   stands.** The task carried to the cycle the question of the kind of the modules moved out
   ("Do jakiego rodzaju kodu należą moduły wydzielone przy podziale plików"), and the plan's *Choices*
   12 answered `shared-module` with no row in the kind's table; the table is not the gap — WAY-199
   asks a status only of the files a kind's guidelines list — but an agent changing
   `stage_transcripts.py` selects no guideline of its kind by `product-guidelines/reading.md`,
   since the file applies to `relation-model` and `process-audit` only. The slice 13 review graded
   this Minor and outside the task; I keep it Minor and within the task, since the task asked the
   question. The fix is an extension of the kind's guidelines (its *Applies to* and *Where in code*),
   made as `maintain-coding-guidelines` gives.

7. **The shared base of the audit's modules stands in the record reader.**
   `process-audit/record_reading.py` holds `AuditCountError`, `Git`, `GitError`, `table_cells`,
   `is_separator`, `THE_WAY` and `MAX_BYTES`, which `process-audit/problem_register.py:19`,
   `process-audit/version_analysis.py:35` and `process-audit/audit_report.py:19` import from it, so the
   register imports from the reader of records with which it shares only these. Below every threshold
   of WAY-385 (`record_reading.py` 1149 lines), so Minor by WAY-363, as the slice 15 review graded it.

8. **The sentence of `audit-series-script-paths` (`foundations/invariants.md`, rewritten by F9 in this
   change) and the first sentence of `process-audit/test_audit_series_scripts.py` still say the paths
   are those "whose history `process-audit/audit_count.py` reads".** Since `a30a04ff` the paths and
   the `git diff` that reads their history stand in `process-audit/version_analysis.py`, which the
   command imports; the docstring's second paragraph already says so. As a sentence of the command
   it stays true, so no departure from the entry (WAY-263) — a reader who looks for the reading in
   `audit_count.py` finds none. Graded as the slice 16 review graded it.

9. **`process-audit/audit_report.py` names the two files of the cost script by constants in one
   sentence and by literals in two others**: `:86` uses `COST_SCRIPT` and `COST_MODULE`, while
   `:150-152` and `:323-324` write `task-cycle/cycle_stages.py` and `task-cycle/stage_transcripts.py`
   out. A later move of either file would change one sentence of the report and leave two. Graded as
   the slice 17 review graded it.

10. **`process-audit/audit_count.py:76` and `process-audit/price_list.md:21` say that
    `task-cycle/cycle_stages.py` folds the cache writes into *Input*.** Since `1f09e4d6` the fold
    (`claude_usage`) stands in `task-cycle/stage_transcripts.py`, which `cycle_stages.py` imports. True
    of the command, as in finding 8; a name the change made less exact. The slice 17 review graded
    it outside the task; I grade it within, since the move that made it so is this task's
    (`whole_change.md`: a name that stopped being true). `audit_count.py:62` ("`stages.md` that
    `task-cycle/cycle_stages.py` writes") stays exact.
