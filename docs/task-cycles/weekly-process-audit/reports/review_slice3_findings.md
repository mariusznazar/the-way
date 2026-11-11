# Findings of the review of slice 3 (`876710c..9285a74`, `FAIL 9285a748fb35005dcc29cb6deeb3bca54bd7ae71`) — the reviewer's words

Full review: `.runs/task-cycles/weekly-process-audit/reports/review_slice3_report.md`

## Blocking findings

### 1. Important — a crafted header line stalls the command for hours (quadratic regex), and a long header continuation for minutes

Place: `process-audit/audit_count.py:106` (`HEADER_FIELD`), used by `header_fields` (`:285-307`) for every line before
the record's first `## ` heading; the continuation join at `:303-304`.

What is wrong: `HEADER_FIELD = -[ \t]+(?P<label>[^:\n]+?):[ \t]*(?P<value>.*)` is matched with `fullmatch` on each header
line. For a line of the form `-` + n spaces + `x` with no colon, `[ \t]+` and the lazy label (which may itself start with
spaces) can split the run of spaces in n ways, and each way scans the rest of the line before it fails: O(n²). The record
is untrusted input and is cut at 4 MiB (`MAX_BYTES`), which a line of this form fits many times over.

Why it matters: the command is meant to run unattended on the night from Friday to Saturday (WAY-338). One such record in
the history of one named repository blocks the whole run with no output and no error; there is no time limit on the parsing
(`GIT_TIMEOUT` bounds git only). The task and the handoff name "a malformed or oversized table" and crafted input at this
boundary (WAY-48) as the thing to check.

Evidence (measured on the head commit, `process_pin` + `remarks_count` on one record):

| input | size | time |
|---|---|---|
| `"- " + " "*10000 + "x"` | 10 KB | 0.88 s |
| same, 20000 spaces | 20 KB | 3.5 s |
| same, 40000 spaces | 40 KB | 13.6 s |

Time grows with the square; at the 4 MiB limit it is of the order of a day and a half per call (and `process_pin` runs
`header_fields` twice for the-way's own records). The join at `:304` (`values[-1] = (values[-1] + " " + line.strip())`)
copies the whole value for each continuation line: a header `- Process pin: a` followed by 400,000 lines ` x` took 37 s,
about 7 minutes at the limit. No test gives a long or oddly shaped header line, so the 43 tests do not see it.

Suggested direction (not binding): split the line at the first colon without a lazy scan (or forbid the label to start with
a blank), cap the length of a line read and of a joined value, and collect continuation pieces in a list.

### 2. Important — a folder name with a backslash before a bar breaks out of its table cell and shifts the columns of its row

Place: `process-audit/audit_count.py:486-488` (`cell`), used for the *Folder* column at `:532` and for the *Why* column at `:545`.

What is wrong: `cell` replaces `|` by `\|` and leaves a backslash as it is. In a Markdown table `\\|` is an escaped backslash
followed by a real cell separator. A folder name that contains `\|` (git accepts any bytes but NUL and `/` in a path
component on Linux) is written as `\\|`, which closes the cell.

Why it matters: the folder name comes from the history of a repository the user names, so a committer controls it. The
handoff lists "output that could break a Markdown table or pass for another row". Slices 4–6 and the skill read this table
by columns; a row with more cells than the header lets the folder name supply what looks like the *Process pin*, *Remarks*
or times of the row.

Evidence: with the folder `x\|none\|7777777\|99\|0:00:01\|0:00:02` (built with `cell()` from the head commit and a GFM-style
tokenizer that honours `\\`), the row `| q | <40 a> | 2025-10-09 | x\\|none\\|7777777\\|99\\|0:00:01\\|0:00:02 | none | <40 b> | 0 | unknown | unknown |`
gives 14 cells instead of 9, with `7777777`, `99` and `0:00:01` standing where *Later copies*, *Process pin* and *Remarks*
would. A real run of the command on a repository with the folder `a\|b` wrote `a\\|b` into the file. The test
`CraftedInput.test_control_characters_and_bars_stay_inside_one_cell_of_one_line` uses `|` and control characters but no
backslash, and its helper `AuditCountCase.rows` splits on `(?<!\\)\|`, which reads `\\|` as escaped and so would hide the defect.

### 3. Important — one commit with an out-of-range committer date aborts the whole run with a traceback and writes nothing

Place: `process-audit/audit_count.py:472-478` (the loop after the `try` of `read_repository`; `datetime.fromtimestamp(stamp, timezone.utc)` at `:475`).

What is wrong: `%ct` of a commit is taken as it is stored. `fromtimestamp` raises `OSError` or `ValueError` for a value
outside the supported years, and that call stands outside the `try ... except (GitError, ValueError, UnicodeError)` of the
same function and outside `main`'s `except AuditCountError`. The exception is not caught.

Why it matters: the docstring (`:58-61`) fixes the exit codes: 1 means "the result written but a repository that could not be
read", 2 means an error line and nothing written. Here the command exits 1 with a Python traceback, writes nothing for any
repository, and names no repository. One crafted or damaged commit in one named repository then costs the night's count of
all of them, and the exit code does not tell a scheduler's reader apart from the case the docstring gives it for.

Evidence: a repository with a commit added by `git hash-object -t commit` whose committer line reads `99999999999999 +0000`
and which adds `docs/task-cycles/t/cycle.md`; `python process-audit/audit_count.py --locations <temporary> --repository q`
exits 1, stdout empty, stderr ends `OSError: [Errno 22] Invalid argument` at `audit_count.py:475`, and the results directory
stays empty.

