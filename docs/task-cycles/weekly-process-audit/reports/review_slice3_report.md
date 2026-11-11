FAIL 9285a748fb35005dcc29cb6deeb3bca54bd7ae71

# Review of slice 3 — the counting command (`876710c..9285a74`)

Reviewed range: `git log 876710c..9285a74` holds two commits (`58ca0de`, `9285a74`); `git diff --stat` holds
`process-audit/audit_count.py` (599 lines), `process-audit/test_audit_count.py` (587) and `foundations/part_map.md`
(+2 −1). `git rev-parse HEAD` in the reviewed worktree is `9285a748fb35005dcc29cb6deeb3bca54bd7ae71`, as given.
The reviewed worktree, its index and its branch were not changed; all runs were made in a separate detached worktree of
the head commit (removed at the end) and on temporary directories.

Counts: **3 blocking**, **3 Minor**, **2 out of scope** (the lines of Declined to judge).

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

## Minor findings

### M1. A very large integer in the locations file gives a traceback

Place: `process-audit/audit_count.py:156-162`. `json.loads` raises a plain `ValueError` ("Exceeds the limit (4300 digits)")
for an integer of more than 4300 digits; only `JSONDecodeError` and `RecursionError` are caught. Evidence: a locations file
with `"n": 99…9` (5000 digits) exits 1 with a traceback instead of `Error: the locations file … is not JSON` and exit 2.
Minor because the locations file is the user's own.

### M2. Git runs in the inherited environment and with the repository's own configuration for `log`

Place: `process-audit/audit_count.py:243-250` (`Git.run`). The command passes `-C <repository>` but inherits `GIT_DIR`,
`GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_CONFIG_PARAMETERS`, `GIT_CONFIG_COUNT` and the like. Evidence: with `GIT_DIR` set to
another repository's `.git` and `--repository q`, the command exits 0 and writes the cycles of the other repository under
the name `q` (run on two temporary repositories). Started from a git hook, or by a tool that sets these variables, the count
would be silently the wrong repository's. Related hardening: `log.showSignature=true` in a repository's configuration with
a program in `gpg.program` makes `git log` start that program for a signed commit; `core.fsmonitor` is already switched off
at `:248` for the same reason, so `-c log.showSignature=false` (and removing the `GIT_*` variables from `environment`) would
complete it. Reaching it needs write access to a checkout the user named, hence Minor; it bears on invariant
`script-subprocesses` only through what git itself then starts.

### M3. The refusal to write the results inside a repository covers only the repositories being read

Place: `process-audit/audit_count.py:575-580`. WAY-329 says "No repository, the repository of the-way included, holds
them". With `--repository acme` and `audit_results` pointing inside the checkout of the-way (or of any repository not named
in this run), the command writes the result there. The executor named this as a concern and gave the reason (a user's notes
may be a git repository); the reason holds for repositories in general but not for the-way's own checkout, which
`the_way_checkout` already finds (`:202-206`). Adding that checkout to the set the guard compares against would close the
case WAY-329 names. Minor: a misconfigured entry in the user's own file, the content is not committed by the command.

## The part-map change (asked in the handoff)

- `Trust boundary: process-audit/audit_count.py` — right by WAY-48: the file takes in files from the user's disk and
  repositories the user names, and is not a script that checks the product's own files. The pattern is a path and matches
  the form of the other entries (`project-level/readiness_check.py`, `instruction-files/check_instructions.py`).
  `python -B elements/common/foundation_check.py` exits 0 with it.
- *Depends on* stays `task-cycle · project-level`. The only import of another part is `remarks_check` from `task-cycle/`
  (`audit_count.py:79-80`), which `task-cycle` covers; `project-level` was written by Slice 1 for the skill of Slice 7. No
  other file is imported or run by path. Right.
- The new *External context* row (`a user's places outside every repository — … | both | untrusted`): WAY-48 says "an
  exchange with the external context records its direction and marks what comes in as untrusted", and the command both
  reads the locations file and the register and writes the results there, so the row is of the form the decisions give
  (direction `both`, `untrusted`, naming no part and no file of the product). It adds a fact of the map that the task did
  not name, but the task's item 1 asks for the part's entry and the entry's boundary needs its exchange recorded; I find it
  within the change and not a finding. The row does not name the cycle records of the user's repositories (they come
  through the existing `git` row, marked trusted, though their content is untrusted); the row's wording "the places its
  entries name" covers the `repository` entries, so I leave it.

## The orchestrator's binding choices 1–6 and the executor's concerns

- Choices 1–6 hold in the code: keys with `repository` and `--repository` (`:209-225`); `problem_register` and
  `audit_results` as constants and in the docstring (`:86-88`, `:16-18`); `--locations` (`:567`); the-way's own pin from
  *Target branch and base* (`process_pin`, `:322-333`); no surface entry added; one cycle per folder with the first
  commit as *Record* and the later commits listed (`:472-477`).
- A moved pin read as the commit moved to (`MOVED_PIN`, `:105`, `:316-318`): consistent with `record_template.md:11-12`,
  which does not say; stated by the executor; no finding.
- Short pins kept as written: fine for slice 3; slice 5 must resolve them.
- Values read from the last copy of a corrected cycle (`:477`): matches choice 6 and the test at
  `test_audit_count.py:204-216`; the "last" is the last in `--topo-order` of the listing, which is a defined order but not
  a date; no finding.
- Results directory refused only inside a repository being read: see M3.
- `--full-history --branches --remotes` (`:457-459`): checked against an independent listing, below.

## Other checks of the trust boundary (no finding)

- Control characters and escape sequences: `display` (from `remarks_check`) escapes every non-printable character; the
  folder, key and reason cells pass through it, and the record text reaches the result only as a hex commit, a number or
  `h:mm:ss`. A key with a lone surrogate (`"bad\ud800key"`) is written escaped, not as an encoding error (run).
- A record path that leaves its directory: the folder comes from `diff-tree -z` names of exactly four components; git does
  not store `..`; a symbolic link or submodule at `cycle.md` or `stages.md` is refused by mode and type (`read_file`,
  `:395-410`); the test for the link exists.
- Git options injected through a name or commit: the repository goes after `-C`, commits and blob ids come from git's own
  output, pathspecs are after `--` and `:(literal)`/`:(glob)`; the `--repository` value is only a key looked up in the file.
- What the command may run: `rev-parse`, `log`, `diff-tree`, `ls-tree`, `cat-file` through `subprocess.run` with a list
  and `stdin=DEVNULL`; nothing else is started; invariant `script-subprocesses` holds. `script-imports`: standard library
  and `remarks_check`; `cross-part-imports`: `process-audit` depends on `task-cycle`; `script-language`: Python.
- Doubled or missing fields: a doubled key in the locations file is refused (`:147-154`); doubled or missing lines in a
  record or `stages.md` give `unknown` with the reason; a `stages.md` that says `unknown` stays `unknown`.
- Malformed or oversized: a file over 4 MiB is not read (the test uses 4.2 MB); a non-UTF-8 file gives `unknown`.
  The time cost of a small malformed line is finding 1.
- The locations file: wrong types (`42`, a string for `the-way`, a list for a key) refused with `Error:` and exit 2;
  relative paths refused; the error names the entry and never the path it holds.

## Declined to judge

- `task-cycle/cycle_stages.py` reads session transcripts on the user's disk while the part `task-cycle` records no trust
  boundary (the executor's observation): outside this slice and its files.
- Older archived records in this public history carry absolute paths of the author's disk in their header lines (the
  executor's observation): history before this task; the command copies none of that text into its result (confirmed by the
  structure of the result and by the test `assertNotIn(str(self.home) …)`).

## Checks run

All in a detached worktree of `9285a74` under the session's scratchpad (`…\scratchpad\rv`), removed at the end, unless noted.

| Command | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` (reviewed worktree) | 0 | `9285a748fb35005dcc29cb6deeb3bca54bd7ae71` |
| `python -B gate/run_tests.py process-audit` | 0 | 43 tests OK in 34 s. (A first run in a `git archive` copy with no `.git` gave 1 failure in `test_the_way_without_a_repository_entry_is_this_checkout`, which needs a git checkout; not a defect of the head commit, and rerun in a real worktree it passes.) |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | 278 files, 0 listed |
| the command on this repository, `--locations <temporary file naming the reviewed worktree as the-way's `repository`, a temporary register and results directory> <&-` (stdin closed) | 0 | `Wrote count-2026-11-11.md and count-latest.md: 69 cycles in 1 of 1 repositories.`; the first rows match the executor's report |
| `git status --short` in the reviewed worktree after all runs | 0 | empty |
| scratch probes (own scripts in the scratchpad: `probe1.py` timing of `process_pin`/`remarks_count` on crafted records; `probe2.py` continuation timing, big integer, lone surrogate, backslash folder, `GIT_DIR`; `probe4.py` cell shift; `probe5.py` committer date) | 0 each, except the results reported above | finding 1 timings, finding 2 (14 cells), finding 3 (exit 1, traceback), M1, M2 |

Not run: the full suite (the cycle's own run, WAY-160). Not verified: that the executor's mutation tests failed as stated; I
read the tests instead. The independent listing of cycle folders the executor gives as its own-work check was not repeated;
the run on this repository gave the same 69 cycles the report names. The effect of `log.showSignature` with a configured
`gpg.program` (M2) is read from git's documented behaviour and was not run.

Mutation-resistance of the tests (read, not run): the tests protect the found behaviour with literal expected values (pin, counts,
cells) and do not compute expectations with the code under test. They have no case for a long header line, a backslash in a
folder name, a committer date out of range, an integer too large in the locations file, or `GIT_*` in the environment; findings
1–3 and M1–M2 are the cases that stay untested.

## Reaches beyond the dispatch

- `task-cycle/record_template.md` lines 1–30 and 175–195, to read the forms of *Process pin* and of the remarks item that
  the command parses (the dispatch names the file as read material; I read the parts it bears on).
- `task-cycle/remarks_check.py` (`display`, `split_lines`, `fenced_flags`, the regexes at `:60-75`, `check` at `:316-340`),
  to judge what the command reuses.
- `foundations/part_map.md` lines 100–125 and 205–245, and `elements/part-map/template.md` lines 120–175, for the part-map
  change and the form of *External context*.
- `foundations/decisions.md` WAY-40 (`:1051-1076`), read whole, for what the map's entries hold; WAY-48 and WAY-49 at the
  ranges the dispatch gave.
- `process-audit/problem_register.md` lines 1–80, to confirm the register's *Repository* wording the command's keys follow.
- `project-level/backlog_place.md`, whole, as WAY-320 and the slice send the reading of an entry there.

## Unread material

- `foundations/decisions.md` WAY-327 and WAY-328 (named in the executor's report, not in my selection) were not read.
- The rest of `process-audit/problem_register.md` after line 80 (the *Issues* and *Problems* tables) was not read; the
  slice reads neither.
- `.runs/task-cycles/weekly-process-audit/task.md` lines 1–14 and 90–end were not read; the passages the handoff names
  (`:23-36`, `:38-65`, `:67-71`, `:77-80`) were read whole, with `:82-89` beyond them.
- `task-cycle/cycle_stages.py` and `project-level/plan_state.py` (named in the slice's *Read*) were not read: the command
  imports neither, and the stage report's form was judged from the tests' sample lines and the output on this repository.
- Otherwise: the handoff, the executor's handoff and report, the method `task-cycle/review/SKILL.md`, WAY-38, WAY-48, WAY-49,
  WAY-89, WAY-320, WAY-329, WAY-335, WAY-338 and the five invariants were read whole; WAY-107, WAY-140, WAY-260 and WAY-296
  were not opened (they concern the backlog place, the human actions, the report items and the remarks form, which the code
  was judged against through `record_template.md` and `backlog_place.md`).

## Searches not found or unclear

- The slice says the cycle's remarks "may reuse the cutting of `task-cycle/remarks_check.py`"; the command reuses its
  helpers (`split_lines`, `fenced_flags`, `HEADING`, `MARKER`, `reads_none`) but counts the entries itself, and
  `remarks_check.py` exposes no function that returns the entries of the item `Process remarks on the-way` to reuse. Not
  unclear in effect; noted.
- `record_template.md` does not say which version a cycle that moved its pin ran on; the executor chose the commit moved to.
  Unclear in the foundation, not a finding.
- I did not find a decision that bounds the time a script may spend on one untrusted file; finding 1 rests on WAY-48
  ("crafted input"), the handoff's "oversized" and WAY-338 (unattended run), not on a stated limit.
