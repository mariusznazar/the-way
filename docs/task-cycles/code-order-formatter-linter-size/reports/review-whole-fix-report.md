PASS 2e066ab4f6f7a0b30b29ed09bbafbaf61b6fea38

# Review of the fix of the Minor findings of the review of the whole change

- Reviewed: range `d0a861d9..2e066ab4`, nine commits (`3b3008b3` oldest .. `2e066ab4` newest);
  `git rev-parse HEAD` in the worktree gave `2e066ab4f6f7a0b30b29ed09bbafbaf61b6fea38`.
- Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` of the worktree, read whole.
- Bound: `reports/fix-findings.md` (my findings 1, 3-10 of `reports/review-whole-report.md`, all Minor).
- Counts: 9 findings fixed, 0 remain; no new Critical or Important finding; 1 new Minor finding.
- Changed files (18, +181 −149): `process-audit/audit_shared.py` +120 (new),
  `process-audit/record_reading.py` +5 −102, `process-audit/audit_count.py` +11 −8,
  `agent-instructions/test_linter_invariant.py` +8 −6, `process-audit/test_audit_series_scripts.py`
  +6 −5, `task-cycle/gate_times.py` +6 −6, `process-audit/audit_report.py` +5 −4,
  `guidelines/coding.md` +3 −3, `process-audit/test_audit_count.py` +3 −2,
  `process-audit/version_analysis.py` +1 −3, `README.md` +2 −1, `foundations/decisions.md` +2 −2,
  `foundations/invariants.md` +2 −2, `guidelines/coding-shared-module.md` +2 −1,
  `process-audit/price_list.md` +2 −2, `foundations/part_map.md` +1, `process-audit/problem_register.py`
  +1 −1, `process-audit/test_record_items.py` +1 −1.

## Each finding of the findings file

| # | Finding | Verdict | Evidence |
|---|---|---|---|
| 1 | `yapf: disable` / `yapf: enable` pass the formatter's test | **fixed** (`3b3008b3`) | `FORMATTER_SWITCH` (`agent-instructions/test_linter_invariant.py:50`) now matches the five comments, still among the comments `tokenize` gives; WAY-382's second paragraph and `formatter-layout` name the five. In my worktree of the head, `X = 1` / `# yapf: disable` / `Y = [1,2]` / `# yapf: enable` appended to `gate/run_tests.py`: the class `Formatter` failed (`Lists differ: ['gate/run_tests.py:223: # yapf: disable', …] != []`; the layout test passed, as Ruff honours the comment, so only the comment test catches it); file restored, the module passes (5 tests) |
| 3 | `README.md:106-107` "the settings of the linter" | **fixed** (`b0755488`) | now "the settings of the linter and the formatter of the-way's Python code" |
| 4 | `file` in `gate_times.py` | **fixed** (`e7055545`) | `run = parse_name(name)` at `task-cycle/gate_times.py:213-216` and `:239-242`; no other `run` stands in those functions (search: only the docstring uses the word), so the rename changes no binding; six lines, nothing else |
| 5 | test name of the nested list item | **fixed** (`42c2c76a`) | `test_a_nested_list_item_under_the_first_sub_item_is_no_sub_item_of_the_list`; body unchanged, no `decision:` or `invariant:` line on it |
| 6 | `coding-shared-module.md` lacks `task-cycle` | **fixed** (`33e6399d`) | *Applies to* `relation-model · process-audit · task-cycle` and `task-cycle/` under *Where in code*, nothing else: exactly what the finding states (judgment (c)) |
| 7 | shared base in the record reader | **fixed** (`2e066ab4`) | see (b) below |
| 8 | `audit-series-script-paths` and its test's docstring | **fixed** (`4760168a`) | both now read "whose history `process-audit/audit_count.py` reads through `process-audit/version_analysis.py`, which it imports"; what the sentence requires is unchanged |
| 9 | literals and constants in `audit_report.py` | **fixed** (`eff165f8`) | `:150-152` and `:323` now take `COST_SCRIPT` and `COST_MODULE`; the report's bytes equal (below) |
| 10 | "`cycle_stages.py` folds them in" | **fixed** (`dbacb903`) | `process-audit/audit_count.py:76-77` and `process-audit/price_list.md:21-22` say `task-cycle/stage_transcripts.py`, which `task-cycle/cycle_stages.py` imports, folds them in; the list's date is untouched |

## The coordinator's points

**(a) The edit of `guidelines/coding.md` in `3b3008b3` follows from finding 1; it does not go beyond it.**
The rule `### Formatter` (lines 45-55) restates WAY-382 in its *Bad* line and in its paragraph, with
the same list of comments. Finding 1's fix widened that list in WAY-382 and in `formatter-layout`.
Left as it was, the rule would name three comments while its decision names five. That is a rule that
says less than the entry it carries (WAY-168). A reader of the guidelines would take the `yapf:`
comments as allowed. The edit widens the same list in the same two places and changes nothing else
of the rule. Its one blemish is the new Minor finding below.

**(b) Finding 7, `2e066ab4`.**
- `process-audit/audit_shared.py` (120 lines) holds `AuditCountError`, `GitError`, `Git`,
  `GIT_TIMEOUT`, `table_cells`, `is_separator`, `THE_WAY`, `MAX_BYTES` and `display`.
  - My `astcmp.py` compares these nine top-level definitions with those of `record_reading.py` at
    `d0a861d9` by `ast.dump`. Each is the same.
  - No definition of `record_reading.py` was lost or changed beyond the move. `display` stays there
    as well, since the module uses it itself.
  - Importing `audit_shared` in a new interpreter loaded `remarks_check` and standard modules only,
    none of the audit's modules, and printed nothing.
- The imports:
  - `record_reading.py` takes `MAX_BYTES, Git, GitError, is_separator, table_cells`;
    `problem_register.py:19` takes what it took from the record reader; `version_analysis.py` takes
    `THE_WAY, Git, GitError`; `audit_report.py` takes `THE_WAY, AuditCountError`; `audit_count.py`
    takes the seven names.
  - The two tests of `test_audit_count.py` take `Git` and `GitError` from `audit_shared`. No
    expected value or assertion changed.
  - The linter (F401 and F821 blocking) passes, so nothing stands unused or undefined.
- **Behaviour on crafted input at `audit_count.py`.** I ran `cases.py` with the base code (`d0a861d9`)
  and the head code (`2e066ab4`) over the same inputs. Exit code, stdout, stderr and every result file
  were byte-equal in all four cases:
  - the register template, with a clone of the head as the counted repository: exit 0, result of
    265635 bytes;
  - a crafted register: escaped bars `\|` in cells and in an issue's name, a cell ending in a
    backslash, a row of bars only, a 5000-character cell, a short row, a separator with colons and an
    empty issue row: exit 0, 266769 bytes;
  - a register whose table `Weights` lacks `Minor`: exit 1 and the same `Error:` line;
  - the repository key pointing at a directory that is no git repository (the `Git` and `GitError`
    path): exit 0, 12784 bytes.
- **Sizes.** `audit_shared.py` 120 lines, `record_reading.py` 1052 (1149 before), `audit_count.py` 871,
  `audit_report.py` 558, `problem_register.py` 358, `version_analysis.py` 1056, all under 1200. The
  largest functions: `read_register` 93, `read_prices` 81, `gate_table_runs` 76; `Git.execute` 27.
  The size test passes at the head.
- **The part-map line naming `process-audit/audit_shared.py` a trust boundary of `process-audit`**
  (`foundations/part_map.md:140`).
  - It follows from the move and from WAY-48. `table_cells` and `is_separator` parse the text of the
    register's and the records' tables, which come from outside the product. Before the fix that code
    stood in `record_reading.py`, a listed boundary.
  - Leaving the new file off the list would take the review aimed at crafted input away from the
    very parser of that text.
  - `Git` reads from git, which the external context marks trusted. Even so, the file holds the
    parsing of untrusted text, which by itself makes it a boundary.
  - Correct, and within the finding's consequence. It is a change of the part map that the request
    names.

**(d) Tests and reworded sentences (WAY-233, WAY-03).**
- No expected value changed; no assertion was weakened, skipped or deleted. The comment test of
  `formatter-layout` is stricter: its pattern and its message widened.
- Reworded sentences:
  - WAY-382, second paragraph: no line `decision:` quotes it (search).
  - `formatter-layout`: cited by the two tests of `Formatter` in
    `agent-instructions/test_linter_invariant.py`, both changed in this fix.
  - `audit-series-script-paths`: cited by `process-audit/test_audit_series_scripts.py`, whose
    docstring changed.
  Both tests stand changed on the branch, so the foundation check lists no reworded invariant whose
  test was left as it was.
- Altered tests for the request:
  - `agent-instructions/test_linter_invariant.py` (`formatter-layout`);
  - `process-audit/test_audit_series_scripts.py` (`audit-series-script-paths`, docstring only);
  - `process-audit/test_record_items.py` (one test renamed; it holds no citation, though other tests
    of the file hold lines `decision:`);
  - `process-audit/test_audit_count.py` (two import lines in tests of a file that holds lines
    `decision:`).
- WAY-382's widened sentence and `formatter-layout` go beyond settlement row 5's three comments.
  The fixer marks them `the cycle's` for the request, which is right.

**(e)** `python -B elements/common/foundation_check.py` at the head: exit 0, "0 errors" and no
listed line. Every finding of mine in the findings file is fixed; none remains. Finding 2 (a sentence
in the request) and finding 11 (outside the task) were not in the file and stay with the request.

## New finding of the fix

### Minor — within the task

1. **`guidelines/coding.md:54` was not rewrapped.** The paragraph of `### Formatter` now has a line of
   127 characters ("one is no way out: … beside the one command of the gate"), followed by a line of
   nine characters (`(WAY-16).`). The paragraph's other lines and the rest of the paragraphs of the
   file stand at most 100 characters. Markdown renders it the same, so this is layout only; a
   rewrap of lines 53-55 fixes it.

No other new finding: the fix diff holds no code made to pass a test, no swallowed error and no
change of behaviour (above).

## Checks

| Check | Command or method | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `2e066ab4…`, exit 0 |
| Foundation check | `python -B elements/common/foundation_check.py` in the head worktree | exit 0, `0 errors`, no listed line |
| Formatter test seen failing on `yapf:` | the comments appended to `gate/run_tests.py` in the head worktree, `python -B -m unittest agent-instructions.test_linter_invariant.Formatter` | exit 1, the comment test lists both lines; restored, then `python -B -m unittest agent-instructions.test_linter_invariant`: exit 0, 5 tests |
| Size test | `python -B -m unittest agent-instructions/test_size_invariant.py` at the head | exit 0, OK |
| Moved definitions | `python -B astcmp.py d0a861d9 2e066ab4` | nine names `same`; nothing lost or changed in `record_reading.py` |
| Import runs nothing | `python -B -c "…import audit_shared…"` in a new interpreter, stdin empty | exit 0, no output; no audit module loaded |
| Crafted input at `audit_count.py`, base vs head | `python -B cases.py` (four cases above, `--locations` in my directory, `--today 2026-11-19`) | `ALL EQUAL`; exits 0/0, 0/0, 1/1, 0/0 |
| Focused `process-audit` | `python -B gate/run_tests.py process-audit` in the head worktree | exit 0, 277 tests OK |
| Focused `elements/part-map` | `python -B gate/run_tests.py elements/part-map` | exit 0, 40 tests OK |
| Focused `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | exit 0, 52 tests OK (linter, formatter and size invariants) |
| `gate_times.py` tests | `python -B -m unittest task-cycle/test_gate_times.py` | exit 0, 27 tests OK (skipped=1) |

Not run: the full gate (the orchestrator's or CI's).

## Reaches beyond the handoff

- `reports/fixer-checks/run_cases.py` and `make_register.py`, read only to learn the command's
  `--locations` option; my cases are my own.
- `a private rule file of the author` (read earlier in this session) for the
  scripts in my directory.

## Working copies

Under `.runs/review-whole-fix/`:
worktrees `base` (`d0a861d9`) and `head` (`2e066ab4`), a shared clone `clone` (the counted
repository), the scripts `astcmp.py` and `cases.py`, crafted registers, locations files, results and
run outputs. Removed: both worktrees by `git worktree remove --force`, then `git worktree prune`;
then the directory itself. `git worktree list` names none of them, `.runs/` holds only
`orchestrator/` and `task-cycles/`, and `git status` of the reviewed worktree is clean. Nothing
remains.

## Unread material

- `reports/fixer-handoff.md`: not read; the findings file and the fix report were enough to bound
  this review.
- The fixer's evidence files in `reports/` and `reports/fixer-checks/` (sha256 lists, logs): not
  read; I ran my own checks.
- `foundations/part_map.md`: the line added only, with the `process-audit` entry around it.
- Decisions: WAY-48 and WAY-168 from my earlier reading in this session; nothing new opened.

## Searches not found or unclear

- `decision: WAY-382` in tracked files: not found, as expected.
- Unclear: none.
