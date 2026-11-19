PASS 015ce05c2a7209af7db05873775f561acdae408f

# Review of slice 2 (the one reformatting), range 6c13454c..015ce05c

`git rev-parse HEAD` in the worktree is `015ce05c2a7209af7db05873775f561acdae408f`, the head given. The range holds
one commit, `015ce05c` "Reformat the Python files of the named parts with ruff format and nothing else": 78 files,
16104 insertions, 7505 deletions, every one a `.py` file.

Findings: blocking 0, Minor 0, out of scope 0.

## Findings by grade

**Critical:** none.
**Important:** none.
**Minor:** none.

## What I verified against the slice

- Goal, "one commit, only the output of `ruff format --config ruff.toml --no-cache`, nothing else": the range
  holds exactly one commit; its changed names are 78 and none lacks the suffix `.py`; `ruff format --check` over
  the 79 tracked `.py` files reports "79 files already formatted". The 79th file was already formatted at the base,
  so it is not in the commit. Its subject says it is the reformatting by `ruff format` and nothing else; its body
  names the pinned Ruff 0.17.1, `ruff.toml`, and the use of the hash for `.git-blame-ignore-revs`, so slice 3 and
  the orchestrator can find it.
- The commit changes only files of the parts WAY-379 names: `git ls-files '*.py'` gives 79 files, and the 79 that
  match the slice's Change globs are the same 79, so no tracked `.py` file lies outside the globs and none of the
  globs' files was left out.
- No hand edit: the committed text of every one of the 78 files is a fixed point of the formatter (the check
  above); a hand edit that the formatter would not leave unchanged cannot pass it. Beyond the fixed point I
  checked that the code of each file did not change (next item) and that its comments did not.
- Behaviour: for each of the 78 files, `ast.dump(ast.parse(...))` of the file at `6c13454c` equals that at
  `015ce05c` (78 same, 0 differ). The ast tree holds the docstrings and every string, so a changed string would
  differ. The sequence of comment tokens of each file (right-stripped) is also equal at base and head (0 files
  differ).
- Line endings: all 78 changed files are `i/lf w/lf` (`git ls-files --eol`).
- `# fmt: off`, `fmt: on` and `fmt: skip` stand in no tracked `.py` file (grep over the 79 files, no hit), as
  F4 `formatter-layout` and WAY-382 require.
- Lint: `ruff check --config ruff.toml --no-cache .` reports 24 faults at head and 24 at base; with line and
  column numbers removed and the lines sorted, the two lists are equal (`review-2-checks/lint-base.txt`,
  `lint-head.txt`). The slice asked only for the same count; I compared the faults one by one.
- The executor's claims I re-ran: check 4 (ast), 5 (format check), 6 (only `.py`), 7 (24 faults). All hold. Its
  checks 10-12 had not run; I ran them (below) and all five directories pass.
- WAY-205: "a formatter enters a product by one reformatting of the whole of its code in the task that brings
  the formatter". The commit is that one reformatting, and F4 holds from it (the format check passes over every
  tracked `.py` file). No `elements/common` test was run by me, as the slice and WAY-321 ask.

## Trust-boundary files this range touches (crafted input, before and after)

All ten trust-boundary files of the part map's list are in the range (`git diff --name-only` shows each as
changed). For nine of the ten I ran the command at the base and at the head from two worktrees against the same crafted inputs and
compared exit code, stdout and stderr, with the worktree path and the commit hash masked:

- 66 cases, 66 identical (exit 1: 35 times, exit 2: 23, exit 0: 7, exit 3: 1), no traceback in any.
- Inputs: an empty file, a file of invalid UTF-8 and NUL bytes, a CRLF file with a NUL byte, a file with a
  200000-character line, a definition with an approval section, a truncated JSON file, a non-JSON JSONL file,
  a missing file or directory, a network-shaped path (`//server/share/...`), an invalid `--today`, a
  parent-escaping session name (`../../etc/passwd`), and a hostile `--url` (`ext::sh -c id`) for the installer
  in its dry-run form (no `--apply`, so nothing was written; the product repository stayed clean).
- Scripts covered: `gate_times.py` (6 cases), `check_instructions.py` (6), `readiness_check.py` (18, all three
  modes over six files), `plan_check.py` (7), `plan_state.py` (8), `cycle_stages.py` and `cycle_measures.py` (12),
  `audit_count.py` (5), `install.py` (4). `record_items.py` is a module with no command line (no `__main__`), so I ran no
  crafted input against it; its ast equality and the `process-audit` tests, which passed, are what covers it.
- Limit of this check: the crafted inputs that exercise `plan_check.py`, `plan_state.py` and `readiness_check.py`
  mostly end in their error paths (exit 1 or 2), since no well-formed plan or definition was made; the verdict of
  a well-formed one rests on the ast equality and on the focused tests, which exercise them.
- The one place in these files where a source position reaches a message is `process-audit/audit_count.py:624`,
  `error.lineno` of a JSON parser error about the input, not about the script's own source, so a layout change
  cannot move it. A grep for `inspect`, `getsource`, `co_firstlineno`, `traceback` and the reading of the file's
  own source in the ten files found nothing else.
- No operation that cannot be undone was run.

## Checks run

| # | Command | Exit | Result |
|---|---|---|---|
| 1 | `git rev-parse HEAD` | 0 | `015ce05c2a72...` = the head given |
| 2 | `git diff --name-only 6c13454c..015ce05c` and a count of names lacking `.py` | 0 | 78 names, 0 not `.py` |
| 3 | `python -B -I review-2-checks/ast_check.py` (ast of base against head, 78 files) | 0 | `files 78 same 78 differ 0` |
| 4 | `python -B -I review-2-checks/comments.py` (comment tokens, base against head) | 0 | `files 78 comment-differ 0` |
| 5 | `<ruff> format --check --config ruff.toml --no-cache` over `git ls-files '*.py'` (79) | 0 | 79 files already formatted |
| 6 | `<ruff> check --config ruff.toml --no-cache .` at head | 1 | `Found 24 errors.` (the faults exist at base) |
| 7 | the same `<ruff> check` with `--output-format concise` at base and at head, positions masked, sorted, `diff` | 0 | equal lists, 24 faults + 2 summary lines each |
| 8 | `git show --stat --format= HEAD`, and `git ls-files --eol` of the changed files | 0 | only `.py`; all `i/lf w/lf` |
| 9 | grep of `fmt: off`/`on`/`skip` over the 79 files | 1 (no hit) | none |
| 10 | `python -B -I review-2-checks/diff.py` (66 crafted-input cases, base worktree against head worktree) | 0 | `cases 66 diffs 0` |
| 11 | `python -B gate/run_tests.py installation` (in a worktree of the head) | 0 | Ran 73 tests, OK |
| 12 | `python -B gate/run_tests.py instruction-files` | 0 | Ran 105 tests, OK (skipped=5) |
| 13 | `python -B gate/run_tests.py process-audit` | 0 | Ran 276 tests, OK |
| 14 | `python -B gate/run_tests.py project-level` | 0 | Ran 281 tests, OK |
| 15 | `python -B gate/run_tests.py task-cycle` | 0 | Ran 534 tests, OK (skipped=2) |

The five focused runs went in parallel in the worktree of the head, never the full gate. I did not run the same
five directories at the base, so I cannot say whether the 5 and 2 skipped tests are skipped there too; the
executor's report names the 5 skips of `instruction-files` as the link tests that need POSIX real paths, which fits
a Windows host and does not depend on the layout. `<ruff>` is `the Ruff of the quality environment of the main checkout`
(0.17.1; `ruff.toml` pins it). The scripts and results I kept beside this report are in `review-2-checks/` (see
below).

## Declined to judge

- The line counts of functions and files after the formatter (WAY-385, `function-and-file-size`, marked violated):
  they grow by design, WAY-382 says its thresholds count the code after the formatter, and the cure of the
  oversized ones is a later slice, not this one.
- The commit author address `the author's private address` (the executor mentions it): every commit of the branch carries
  it, it is the repository's own configuration, and it is no matter of the task.
- The 24 faults of the linter: slice 2 must leave them as they are; their cleaning is a later slice.
- Whether the hash of this commit has been entered in `.git-blame-ignore-revs`: the slice says a later slice
  does it.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-379 (lines 10579-10612) and WAY-382 (10689-10729), `foundations/invariants.md`
  `formatter-layout` and the neighbours `function-and-file-size` and `generator-writes-only-with-write`
  (lines 448-480): the handoff names F1 and F4 by identifier; I read the entries in the worktree to check the
  scope list and the statement about `fmt:` comments. This is the named selection read by address, not a reach.
- `a private rule file of the author` and `.ai\rules\git.md`: the user's global rules, shown by
  a hook before my scripts and before `git worktree add`; neither touches the task.

## Working copies

- `.runs/review-2/head` (worktree of `015ce05c`) and `.runs/review-2/base` (worktree of `6c13454c`): removed with
  `git worktree remove --force`, then `git worktree prune`; `git worktree list` no longer shows them.
- `.runs/review-2/` (the scripts, the crafted inputs, the test logs, the temporary outputs): removed whole. What
  the report needs I kept in `.runs/task-cycles/code-order-formatter-linter-size/reports/review-2-checks/`:
  `ast_check.py`, `comments.py`, `diff.py` (the differential harness), `diff-log.json` (the 66 cases with their
  exit codes), `lint-base.txt`, `lint-head.txt`, `tests-summary.txt`. (The directory `.runs/executor-2/` named
  in the executor's report was already gone when I listed `.runs/`; I did not touch it.)
- No remainder.

## Unread material

none. I read the handoff, `task-cycle/review/SKILL.md`, the executor's report, WAY-205 (`foundations/decisions.md`
9604-9639), WAY-382, WAY-379, `formatter-layout`, `ruff.toml`, and the task's lines 29, 69-73 and 93, each whole
at the address the slice gives. The handoff names no guideline file for this slice; I read none.

## Searches not found or unclear

none. (The executor's report says the slice's Checks mean "the same 24 faults" by count; I read it as the same
faults and compared them one by one, which also holds.)
