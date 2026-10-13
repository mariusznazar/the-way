# Foundation-stage check evidence

These are existing partial checks, not a pass of the full gate. Commands ran from C:/Storage/repos/the-way-wt/shorten-task-cycle on the prepared foundation diff over d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b.

## python -B gate/run_tests.py elements/decisions --record .runs/task-cycles/shorten-task-cycle/reports/foundation-decisions-tests.jsonl

Exit: 0. 169 tests pass; 29.121 s.

```text
........................................................
----------------------------------------------------------------------
Ran 169 tests in 29.121s

OK
```

## python -B gate/run_tests.py elements/invariants --record .runs/task-cycles/shorten-task-cycle/reports/foundation-invariants-tests.jsonl

Exit: 0. 233 tests pass; 88.463 s.

```text
............
----------------------------------------------------------------------
Ran 233 tests in 88.463s

OK
```

## python -B gate/run_tests.py gate --record .runs/task-cycles/shorten-task-cycle/reports/foundation-gate-tests.jsonl

Exit: 0. 98 tests pass; 21.552 s; existing critical-flow tests included.

```text
..................................................
----------------------------------------------------------------------
Ran 98 tests in 21.552s

OK
```

## python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --record .runs/task-cycles/shorten-task-cycle/reports/foundation-decisions.jsonl

Exit: 0. 0 errors, 9 warnings, 5 none-mode unchecked.

```text
foundations/decisions.md:71: warning: WAY-03: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:374: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:623: warning: WAY-21: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1459: warning: WAY-52: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1541: warning: WAY-55: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:1955: warning: WAY-69: check-by date 2026-10-02 has passed without a review record
foundations/decisions.md:4096: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:4589: warning: *Approved by* is the placeholder `merge of <request link>`
foundations/decisions.md:4631: warning: *Approved by* is the placeholder `merge of <request link>`
unchecked: the lines the log holds on the main branch, and the versions it gains per number — --base none: there is no commit the branch left the main branch from
unchecked: a change to the template without a new version in the log — --base none: there is no commit the branch left the main branch from
unchecked: `TODO` in the log — --merge-onto none: there is no commit to merge onto
unchecked: the copies of a version both logs hold — --merge-onto none: there is no commit to merge onto
unchecked: the fingerprints relations carry — --merge-onto none: there is no commit to merge onto
0 error(s), 9 warning(s), 5 unchecked
```

## python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none --record .runs/task-cycles/shorten-task-cycle/reports/foundation-invariants.jsonl

Exit: 0. 0 errors, 0 warnings, 3 none-mode unchecked.

```text
unchecked: identifiers, versions, corrections and the list of violated invariants — --base none: there is no commit the branch left the main branch from
unchecked: `TODO` in the entries — --merge-onto none: there is no commit to merge onto
unchecked: the fingerprints the links of the entries carry — --merge-onto none: there is no commit to merge onto
note: there is no human_verdicts.md; no human verdict is given
0 error(s), 0 warning(s), 3 unchecked
```

## git diff --check

Exit: 0. no whitespace errors.

```text
(no output)
```

## python -B .runs/task-cycles/shorten-task-cycle/reports/foundation_fingerprints.py

Exit: 0. all affected values match; see foundation-fingerprints.md.

```text
all affected fingerprint values match; 2 dependant references
```

## Warnings and unchecked work

- Existing overdue review: WAY-03, check by 2026-10-02; no later review record.
- Existing overdue review: WAY-21, check by 2026-10-02; no later review record.
- Existing overdue review: WAY-52, check by 2026-10-02; no later review record.
- Existing overdue review: WAY-55, check by 2026-10-02; no later review record.
- Existing overdue review: WAY-69, check by 2026-10-02; no later review record.
- Approval placeholder: WAY-11/1; root replaces it with this request's URL before review.
- Approval placeholder: WAY-136/1; root replaces it with this request's URL before review.
- Approval placeholder: WAY-148/1; root replaces it with this request's URL before review.
- Approval placeholder: WAY-149/1; root replaces it with this request's URL before review.
- Decision none-mode unchecked: 5 total, 2 from --base none and 3 from --merge-onto none. The guard did not compare unchanged original lines/version additions, template-triggered version additions, merge TODO, merge copies or fingerprint values.
- Invariant none-mode unchecked: 3 total, 1 from --base none and 2 from --merge-onto none. The guard did not compare identifiers/versions/corrections/violated-list growth, merge TODO or link values.
- Other guard unchecked lines: none. The invariant guard notes that no human_verdicts.md exists and no human verdict is given.
- Existing return-step-record/1 Method TODO remains unchecked debt; this stage supplies no executable method or pass for it.
- The semantic level-2 comparisons do not prove future agents follow the instructions or establish measured savings.
- The current-integration-tip search, independent assessment, later instruction review and full-cycle checks remain later stage obligations; none is claimed as done here.
