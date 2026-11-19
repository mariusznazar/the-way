# Report of the fix of the Minor findings of the review of the whole change

**Status:** done

Base: `d0a861d9ca22cb2a1cb364d8224bc01f3cd65a44`. Worktree `the worktree's root`,
branch `task/code-order-formatter-linter-size`. Evidence files stand in
`.runs/task-cycles/code-order-formatter-linter-size/reports/` (`fixer-finding1-*.txt`) and in its subdirectory
`fixer-checks/`.

## Commits (oldest first; finding 7 stands alone in the last)

| Commit | Finding | Files |
|---|---|---|
| `3b3008b3` | 1 | `agent-instructions/test_linter_invariant.py`, `foundations/decisions.md` (WAY-382), `foundations/invariants.md` (`formatter-layout`), `guidelines/coding.md` |
| `b0755488` | 3 | `README.md` |
| `e7055545` | 4 | `task-cycle/gate_times.py` |
| `42c2c76a` | 5 | `process-audit/test_record_items.py` |
| `33e6399d` | 6 | `guidelines/coding-shared-module.md` |
| `4760168a` | 8 | `foundations/invariants.md` (`audit-series-script-paths`), `process-audit/test_audit_series_scripts.py` |
| `eff165f8` | 9 | `process-audit/audit_report.py` |
| `dbacb903` | 10 | `process-audit/audit_count.py`, `process-audit/price_list.md` |
| `2e066ab4` | 7 | `process-audit/audit_shared.py` (new, 120 lines), `process-audit/record_reading.py` (1149 -> 1052 lines), `process-audit/problem_register.py`, `process-audit/version_analysis.py`, `process-audit/audit_report.py`, `process-audit/audit_count.py`, `process-audit/test_audit_count.py` (two import lines), `foundations/part_map.md` (one line) |

Every `.py` file changed: `ruff format --config ruff.toml` left it unchanged (or laid it out) and
`ruff check --config ruff.toml --ignore-noqa` passed (exit 0 each).

## Findings

### 1. `yapf:` comments (fixed, `3b3008b3`)

- The pattern `FORMATTER_SWITCH` is now `\b(?:fmt:\s*(?:off|on|skip)|yapf:\s*(?:disable|enable))\b`, found among
  the comments with `tokenize` as before; the message of the test and the docstring of the file name the five
  comments. The words of WAY-382 (second paragraph), of `formatter-layout` and, as the same list stood there, of
  the *Formatter* rule of `guidelines/coding.md` (two places) name the five comments, edited in place (WAY-07).
- The first wording of the comment above the pattern itself held the words `yapf: disable` and the test found it:
  the comment was reworded (the test reads comments of the test file too).
- Seen failing once (WAY-08): `# yapf: disable` appended for a moment to `gate/run_tests.py`:
  `python -B agent-instructions/test_linter_invariant.py Formatter` exit 1, "Lists differ: ['gate/run_tests.py:222:
  # yapf: disable'] != []" (`fixer-finding1-failing.txt`); the file restored with `cp` from a copy before the commit
  (`git status` showed only the intended files); the same command afterwards exit 0 (`fixer-finding1-passing.txt`).
- `python -B elements/common/foundation_check.py` exit 0, "0 errors" (`fixer-finding1-foundation-check.txt`, and
  again at the end, `fixer-checks/foundation-check-final.txt`).
- Tests that hold a sentence I reworded: the two tests of the class `Formatter` in
  `agent-instructions/test_linter_invariant.py` cite `formatter-layout`; no test holds WAY-382 by a line `decision:`.
  Both stand changed in the file (the pattern and the message), see "Tests altered".

**Entries marked `the cycle's`** (they widen what the task's row 5 settled; the request puts them before the human):

- WAY-382, second paragraph. English: "A comment `yapf: disable` or `yapf: enable` in a file the rule covers is forbidden
  like `fmt: off`, `fmt: on` and `fmt: skip`, because Ruff takes it as it takes those." Polish: "Komentarz `yapf: disable`
  albo `yapf: enable` w pliku objętym regułą jest zakazany tak samo jak `fmt: off`, `fmt: on` i `fmt: skip`, bo Ruff
  traktuje go tak jak tamte."
- Invariant `formatter-layout`. English: "A tracked Python file may not be left out of the formatter by any of the five
  comments, the two `yapf:` ones included." Polish: "Śledzony plik Pythona nie może być wyłączony z formatera
  żadnym z pięciu komentarzy, w tym dwoma komentarzami `yapf:`."

### 3. README (fixed, `b0755488`)

`README.md:106-107` reads "the settings of the linter and the formatter of the-way's Python code and the version it is
installed at". Only that wording; the list's other gaps the finding mentions (`.git-blame-ignore-revs`) are not what
its fix asks for and stay.

### 4. `file` in `gate_times.py` (fixed, `e7055545`)

`file = parse_name(name)` is `run = parse_name(name)` in `prepare` and `count_others` (6 lines). Trust boundary
(`task-cycle/gate_times.py`), shown on crafted input: a registry with a running file, an ended file ending after
the run's start, an old ended file, a file over a day old, a running file over six hours old, a file ending before it
starts, a file starting in the future, a file named `notes.txt` and one `123_456_xx.run`; the base file and the new
file run as a process over the same registry shape (`fixer-checks/f4-gate_times-drive.py`): exit 3 both, stdout
identical, stderr empty both, count of other runs `2` both, the same files left in the registry (the stale and
malformed ones deleted, `notes.txt` and the old-but-not-stale file kept). `python -B task-cycle/test_gate_times.py`
exit 0, 27 tests, 1 skipped (`f4-test_gate_times.txt`). Also `python -B gate/run_tests.py task-cycle` exit 0,
534 tests, 2 skipped (`gate-task-cycle.txt`).

### 5. Test name (fixed, `42c2c76a`)

`test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list` is now
`test_a_nested_list_item_under_the_first_sub_item_is_no_sub_item_of_the_list` (the only place of the name; the test
carries no `decision:` or `invariant:` line and its body is unchanged). Run with `process-audit` (below).

### 6. Guidelines of the kind `shared-module` (fixed, `33e6399d`)

*Applies to* is `relation-model · process-audit · task-cycle`; *Where in code* gains `` `task-cycle/` ``. Nothing
else. I read `product-guidelines/coding/SKILL.md` (the skill `maintain-coding-guidelines`),
`product-guidelines/template.md`, `product-guidelines/coding/template.md` and `product-guidelines/coding/kinds.md`.
The table *Files of this kind* lists the exemplar only (WAY-199), so no status of `stage_transcripts.py` or of
`audit_shared.py` was needed and no `copy` / `do not copy` judgment made. The foundation check (exit 0) holds the part
`task-cycle` in the map.

### 8. Sentence of `audit-series-script-paths` (fixed, `4760168a`)

The invariant now reads "Each path of a script whose history `process-audit/audit_count.py` reads through
`process-audit/version_analysis.py`, which it imports, to start a new series ...", the rest unchanged; the first
sentence of the docstring of `process-audit/test_audit_series_scripts.py` says the same (the docstring rewrapped to
100 columns). What they require is unchanged. The invariant's test is changed by me, docstring only:
`process-audit/test_audit_series_scripts.py` (cites `audit-series-script-paths`). `python -B
process-audit/test_audit_series_scripts.py` exit 0 (3 tests); foundation check exit 0.

### 9. Constants in `audit_report.py` (fixed, `eff165f8`)

Both literal pairs (the sentence of *Measure versions*, twice, and the sentence of *Cost*) take `COST_SCRIPT` and
`COST_MODULE` (f-strings). Output bytes shown identical, below.

### 10. Cache writes sentence (fixed, `dbacb903`)

`process-audit/audit_count.py` (docstring) and `process-audit/price_list.md` say "`task-cycle/stage_transcripts.py`,
which `task-cycle/cycle_stages.py` imports, folds them in". The list's date (`- List date`) is untouched, so no series of
the cost starts (the series follow that date, not the file's text). Before and after, below.

Before/after for 9 and 10 (and again for 7): a clone of the worktree at `d0a861d9` (base code) against the worktree
code, both reading the same clone as the repository whose history is counted (118 cycles of this repository), with
`--today 2026-11-19`; scripts `fixer-checks/make_register.py` and `fixer-checks/run_cases.py`. Four cases: the template
register (exit 0), a crafted register (open/fixed/dropped issues, a fix missing from the checkout, a short hash,
problems of unread cycles, refused rows by class and weight, an unknown issue, a late class date: exit 0), a results
directory holding a directory `.count-2026-11-19.md.tmp` (exit 2, "cannot write count-2026-11-19.md ... Permission
denied") and a key the locations file lacks (exit 2). Every stdout, stderr and exit file and both `count-*.md` files
of the results (268053 and 265635 bytes) compared equal with `cmp` after the change of 9 and 10 and again after the
move of 7 (sha256 lists in `fixer-checks/f9-f10-before.sha256` and `f9-f10-f7-after.sha256`; the crafted result
`c5371d2f...`, the template result `45c3cccf...` in both).

### 7. Move of the shared base (fixed, `2e066ab4`, alone, the last)

- New `process-audit/audit_shared.py` holds `AuditCountError`, `GitError`, `Git`, `GIT_TIMEOUT` (only `Git` uses it),
  `table_cells`, `is_separator`, `THE_WAY`, `MAX_BYTES` and `display` (a line `display = remarks_check.display` with
  the same `sys.path` line for `task-cycle` that the other modules of the audit hold, since `Git` writes its errors
  with it). It imports nothing of the audit's modules (only `os`, `subprocess`, `sys`, `pathlib` and
  `task-cycle/remarks_check.py`); `python -B -c "import audit_shared"` loaded none of the audit's other modules and
  ran nothing. `record_reading.py`, `problem_register.py`, `version_analysis.py`, `audit_report.py` and
  `audit_count.py` import each moved name from it. No cycle of imports.
- No behaviour change: the moved definitions compare equal as syntax trees with those of the base
  `record_reading.py` (`fixer-checks/f7-astcmp.py`: nine names identical; nothing else removed from or changed in
  `record_reading.py`); the same four cases of the audit as above, every file equal with `cmp`.
- The tests change only in the module their imports name: two lines of `process-audit/test_audit_count.py`
  (`from audit_shared import Git, GitError` and `from audit_shared import Git`); no expected value, no assertion.
- `python -B gate/run_tests.py process-audit` exit 0, 277 tests (`f7-gate-process-audit.txt`);
  `python -B gate/run_tests.py elements/part-map` exit 0, 40 tests (`f7-gate-part-map.txt`);
  `python -B agent-instructions/test_size_invariant.py` exit 0, 4 tests (`f7-size-test.txt`); sizes: `audit_shared.py` 120,
  `record_reading.py` 1052, `audit_count.py` 871, `audit_report.py` 558 lines (the file limit is 1200); no function was
  changed in length (the moved ones stand as they were; the biggest of them, `Git.execute`, is 33 lines).
  `python -B gate/run_tests.py agent-instructions` exit 0, 52 tests (`gate-agent-instructions.txt`).
- **Decision on the part map (WAY-48): yes, `process-audit/audit_shared.py` is a trust boundary of `process-audit`.**
  Reason: the file holds the parsing of the text of a record's tables (`table_cells`, `is_separator`) and the git that
  reads the copies of the records out of history, which are files that come from outside the product, as the pattern
  for the same code in `record_reading.py` already recorded. WAY-48 asks that a change touching such code gets a review
  aimed at crafted input; leaving the new file out would take that review away from code that was inside a listed
  boundary a commit earlier. The module computes nothing from values already read, which the plan's choice 13 gives as
  the case of a module that is none. One line added to `foundations/part_map.md` after `process-audit/record_reading.py`.
  Cost if wrong: one more file in the review's list of crafted input.

## Tests altered that hold a decision or an invariant (WAY-03)

- `agent-instructions/test_linter_invariant.py`: the two tests of `Formatter` cite `formatter-layout`; the pattern and the
  message of the second test widened (finding 1).
- `process-audit/test_audit_series_scripts.py`: cites `audit-series-script-paths`; docstring only (finding 8).
- `process-audit/test_record_items.py`: one test renamed, with no citation (finding 5); other tests of the file hold
  decisions and are untouched.
- `process-audit/test_audit_count.py`: two import lines (finding 7); no test of it changed in a citation or assertion.

## Own-work check (WAY-164)

Requirement most likely not met: "no change of behaviour, exit codes, messages or the bytes of the report" of the
move (finding 7) and of the sentences made constants (9), and "the same verdict for the same input" of the two files
of the part map (`gate_times.py`, `audit_count.py`). Checks: the four audit cases byte for byte (twice), the syntax-tree
comparison of the nine moved names, the crafted registry for `gate_times.py`, and the focused test runs above, all as
shown. The first run of the check showed nothing wrong; the first wording of the comment in the formatter's test (finding
1) was caught by the test itself and corrected before the commit (failing run: the same command, exit 1 with
`agent-instructions/test_linter_invariant.py:49`; passing run after rewording, exit 0).

## Runs (command, exit code)

| Command | Exit |
|---|---|
| `python -B agent-instructions/test_linter_invariant.py Formatter` with `# yapf: disable` added for a moment | 1 |
| the same command with the file restored | 0 |
| `python -B elements/common/foundation_check.py` (after 1, after 6, after 8, at the end) | 0 |
| `python -B task-cycle/test_gate_times.py` | 0 |
| `python -B process-audit/test_audit_series_scripts.py` | 0 |
| `python -B agent-instructions/test_size_invariant.py` | 0 |
| `python -B gate/run_tests.py elements/part-map` | 0 |
| `python -B gate/run_tests.py process-audit` | 0 |
| `python -B gate/run_tests.py agent-instructions` | 0 |
| `python -B gate/run_tests.py task-cycle` | 0 |

The full gate was not run (handoff).

## Reaches beyond the handoff

- `guidelines/coding.md` (the rule `### Formatter`, two places): the same three-comment list stood there as in WAY-382
  and `formatter-layout`; left alone it would say the narrower thing beside the widened entries. It is a change
  of the same list, in the same commit, one line each. The orchestrator may take it out of `3b3008b3` if it counts as
  outside the finding.
- `product-guidelines/template.md`, `product-guidelines/coding/template.md`, `product-guidelines/coding/kinds.md`
  (finding 6), `elements/part-map/skill/SKILL.md`, `decide_entry.md`, `write.md` and `elements/part-map/template.md`
  (sections on trust boundaries, the one I read for the part-map decision), and the decision WAY-48 whole: read for
  those two decisions; the handoff named only the skill of `maintain-coding-guidelines` and the file edited.
- `elements/common/way_of_working.md`, `elements/common/rules.md`, the templates and examples of decisions and invariants:
  read whole for finding 1 as `foundation_step.md` points to them.

## Choices

- Name `audit_shared.py` for the new module (the handoff gave none). Rejected: `audit_base.py` (the finding's word
  "base" is the reviewer's; "shared" names the kind `shared-module`, whose rule the file follows). Cost if wrong: a rename.
- `display` and `GIT_TIMEOUT` moved with `Git` (the "what only they use"); `display` stays also defined in each other
  module as it was (each uses it itself).
- Wording of the two entries of finding 1 follows the handoff's list; I added no rationale text and no `Rejected`.

## Unread material

none.

## Searches not found or unclear

- None unfound. Unclear: whether `guidelines/coding.md` should carry the five-comment list (see "Reaches"); I wrote it.

## Working copies

- `.runs/fixer/` (copies of `gate/run_tests.py` and the base `gate_times.py`, the clone of the worktree at `d0a861d9`
  under `.runs/fixer/ba/clone`, the results directories, the locations files, the cases' outputs and scratch logs):
  removed with `rm -rf .runs/fixer`; `git worktree list` shows no worktree of mine (the clone was a `git clone`, not a
  worktree). What the report needs was copied to `reports/fixer-checks/` before. Remainder: none.
