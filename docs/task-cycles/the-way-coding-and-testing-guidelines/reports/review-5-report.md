PASS c07e286774fe5b686d17f80253835b146bcda846

# Review of slice 5 (`49be485..c07e286`)

`git rev-parse HEAD` in the worktree is `c07e286774fe5b686d17f80253835b146bcda846`, the head given. Two commits:
`5f19b1d` (the two places of the linter) and `c07e286` (the citation of the invariant). The diff is
five lines in two files.

| File | Added | Removed |
|---|---|---|
| `task-cycle/cycle_measures.py` | 3 | 2 |
| `task-cycle/test_cycle_measures.py` | 1 | 0 |

## Findings

Blocking (Critical or Important): none.

### Minor (within the task, not blocking)

1. **The slice's "behaviour does not change" is true for every valid time and not for two malformed ones; the
   executor named one of them, the other it did not.**
   `task-cycle/cycle_measures.py:198` — `datetime.fromisoformat(value)` replaces
   `datetime.fromisoformat(value.replace("Z", "+00:00"))`. I compared the old and the new expression on 19
   strings (script kept as `reports/review-5-date_edges.py`). Identical on 17, including `...Z`, `...00.123Z`,
   `+02:00`, `T09Z`, `20261006T090000Z`, a week date with `Z`, `T24:00:00Z`, lowercase `z` (refused by both),
   `ZZ` and `+00:00Z` (refused by both), an empty string and a bare `Z`. Two differ:
   - `2026-10-06Z09:00:00` (the executor's question): old `ValueError`, so exit 2; new a naive time read as
     UTC, 2026-10-06 09:00 UTC.
   - `2026-10-06Z` (a date with a `Z` and no time, not raised by the executor): old accepted it as
     2026-10-06 00:00 UTC, because the replacement made it `2026-10-06+00:00`; new `ValueError`, so exit 2.
   Failure scenario: a transcript line whose `timestamp` is one of these two strings is read differently
   than before. Neither string is a form a session writer produces, and neither goes beyond what the old code
   already did: the old code accepted `2026-10-06x09:00:00` and `2026-10-06 09:00:00` (any one character as the
   separator), so the first difference only removes an accident of the replacement, and the accepted value is
   the time the line plainly meant. No path to anything but a time of a line. Minor because the task's Fix for
   cause 30 (`task.md`, "`datetime.fromisoformat` bez podmiany `Z`") prescribes exactly this expression and the
   effect on a user is nil; it is a defect of the plan's wording ("behaviour does not change"), not of the code.
   Grade of the executor's question: Minor, in the task, not blocking. The executor's recommendation (keep the
   change) is right: a guard against a `Z` outside the last position would bring the replacement back in
   another form in a trust-boundary file for a form no writer emits. No test pins either string; adding one is
   not needed and would pin an accident.

2. **The invariant's break shown by the executor and by me exercises one of the two refusals the test needs.**
   `task-cycle/test_cycle_measures.py:835` — the test feeds 200 000 nested brackets; removing `RecursionError`
   from the `except` at `cycle_measures.py:211` makes it fail with the escaping `RecursionError`. The sentence of
   `cycle-measures-refuses-nested-line` (`foundations/invariants.md:508-516`) says "ends with exit code 2 and a
   line `Error:` that names the file and the line, and writes no result"; the test asserts all four (exit 2,
   `Error: ` prefix, file name, `:<n>: ` line, no output file) through `assert_error_names_line`. So the test
   protects the sentence. Noted only because the executor raised it; no change asked.

### Out of scope

none.

## Against the task and the slice

- Goal, first part: `read_time` takes the `Z` through `datetime.fromisoformat` with no replacement (line 198);
  the project declares Python 3.14 (`python-version-declared`, `foundations/invariants.md:196`), which accepts
  `Z`. Done.
- Goal, second part: `for before, after in itertools.pairwise(calls)` at `cycle_measures.py:578`, with `import
  itertools` placed in alphabetical order between `argparse` and `json` (line 100). `pairwise` yields nothing for
  fewer than two calls, as `zip(calls, calls[1:])` did; same pairs otherwise. Done, behaviour identical.
- Goal, third part: `# invariant: cycle-measures-refuses-nested-line` stands on the line directly above the
  test at `test_cycle_measures.py:834`, as `test-method-citation` (`foundations/invariants.md:166`) requires; the
  identifier is E30 as the handoff gives it, and the invariant exists at `foundations/invariants.md:508`.
  Only that test cites it; no other test carries the line.
- The code the slice wrote breaks no rule of `ruff.toml`: ruff reports only PYI034 at
  `test_cycle_measures.py:867` (the base report, moved by one line by the citation comment).
- Nothing was added beyond the slice: no other file, no new code path, no test that asserts nothing.
- Reserved choice: none taken (standard library only, as the module's docstring says).
- Foundation: the change writes no entry. The test citing E30 matches the entry. WAY-48 / WAY-235 (refusal at a
  trust boundary) hold: the trust boundary of the file, a transcript line from outside, still ends with exit 2
  naming file and line on a bad time (`read_time` raises `MeasuresError` on `ValueError`), on a non-JSON line, and
  on a nested one. I tried hostile times (empty, bare `Z`, `ZZ`, `+00:00Z`, `-05:00Z`, a non-string
  `12345`, per the existing test) and each ends in `ValueError` or a `MeasuresError`; none ends in another
  exception class.

## Declined to judge

- Whether `cycle_stages.py:225`, the other place of cause 30, still holds the replacement: it belongs to another slice.
- The other 36 places the ruff run reports in other files: outside the slice by the task's answer 5.
- Whether the plan's wording "behaviour does not change" should say "for every valid time": a matter of the
  plan, not of this change (see Minor 1).

## Checks

Run in the worktree at `c07e286` unless the line says otherwise.

- `python -B task-cycle/test_cycle_measures.py` — exit 0 (89 tests, OK).
- `<main checkout>/.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa task-cycle/cycle_measures.py task-cycle/test_cycle_measures.py` — exit 1; one report only, PYI034 at `test_cycle_measures.py:867` (the base report, not a line the slice wrote or changed).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 (0 errors).
- Invariant test shown failing, in a detached worktree of `c07e286` at `.runs/review-5/wt`: the clause `except (ValueError, RecursionError) as error:` changed to `except ValueError as error:` at `cycle_measures.py:211`, then `python -B task-cycle/test_cycle_measures.py EdgeReadingTest.test_a_line_nested_too_deeply_ends_with_exit_2_naming_the_file_and_line` — exit 1, `RecursionError: Stack overflow ... while decoding a JSON array` (FAILED errors=1); the file restored with `git checkout -- task-cycle/cycle_measures.py`, the same command — exit 0 (OK).
- `python -B -I .runs/review-5/cmp.py` (now `reports/review-5-date_edges.py`) — exit 0; old against new `fromisoformat` on 19 strings, 17 equal, 2 differ (Minor 1).
- Not run: the full gate (the method forbids it).

## Reaches beyond the dispatch

- `task.md` lines 30-50, 90-98, 175-182, 415-423, 433-441, 543 — the handoff names the passages by line range; I read those ranges, and a few lines around them to see the item boundaries.
- `foundations/invariants.md:196` (`python-version-declared`) — to check that Python 3.14 is declared, which the removal of the `Z` replacement rests on.
- `a file of the author's private notes` and `git.md` — shown by the user's hook before a script and a git command; they changed nothing in the review.
- `executor-5-report.md`: read whole, as the handoff names it; its claims I reran where I relied on them. `plan.md` I did not open (the handoff copies the slice and the identifiers word for word).

## Working copies

`.runs/review-5/wt` (a detached git worktree of `c07e286`, broken for a moment, restored) and `.runs/review-5/cmp.py`: both removed (`git worktree remove --force`, `git worktree prune`; the directory `.runs/review-5/` deleted). Kept beside this report: `reports/review-5-date_edges.py`. Nothing remains.

## Unread material

- The decisions WAY-48 (`foundations/decisions.md:2496-2525`), WAY-235 (`:9145-9200`), WAY-08 (`:1750-1779`) and the part-map lines `part_map.md:101-111`: not opened by me. The slice changes no refusal logic and no test of the method; my judgement of the trust boundary rests on running the refusals and on the text of the invariant E30 (read whole, `foundations/invariants.md:508-516`) and of `test-method-citation` (`:166-175`, read whole).
- The orchestrator's additions to the *Read* — `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports` — not read whole; the change adds an import of a standard-library module in an existing script, which none of them reaches.
- `plan.md`: not opened (see above).

## Searches not found or unclear

- A test that pins the refusal of a `Z` separator or of a date with a `Z`: none found; none needed (Minor 1).
- The line references of causes 30 and 33 in `task.md` (`cycle_measures.py:121`, `:352`) point to lines that no longer hold the code (now 198 and 578); the code was found by its text, as the executor said.
