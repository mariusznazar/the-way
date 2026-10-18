# Task 3 review — the form check: references and the merge

Range `d79f692..10b5f4a` (one commit, `10b5f4a`), files `product-guidelines/form_check.py`
(+437 −57) and `product-guidelines/test_form_check.py` (+272 −4). Line numbers below are of
`10b5f4a`.

## Spec Compliance — ✅

Checked against the brief, spec §§3.2, 3.3, 5.1–5.4, rulings C11–C13, C17, C23, C28, C29,
`foundations/invariants.md:2133-2212` and WAY-169.

- ✅ **Both forms of §3.2, outside fenced code, any section.** `REFERENCE_TOKEN`
  (`form_check.py:131`) plus the sorting in `references` (`form_check.py:486-503`): a number with
  the log's prefix, an identifier the file holds as an entry or withdrawn (C28 (3)), or any
  identifier followed by exactly eight lower-case hex characters (the `[A-Za-z0-9]+` tail is
  greedy, so `FINGERPRINT.fullmatch` refuses a ninth letter or digit, as §3.2 asks). Inline code
  counts and fenced code of both characters does not (C28 (4); `fenced_lines` from slice 2). F4
  `PLACES` covers field, row, prose, inline code, example and departure (C17).
- ✅ **Error 7 of §5.3.** `check_references` (`form_check.py:926-952`): malformed fingerprint,
  decision absent or repealed, invariant absent or withdrawn, stale fingerprint; each message names
  the reference, the entry, its current fingerprint and the version that set it; none offers to
  renew one (WAY-31). Every fingerprint goes through `relation-model/fingerprint.py`.
- ✅ **After the merge, version rule.** Decisions from `merged_log` with a discarded `Report`
  (`form_check.py:612-622`); only `unowned` failures with no check carry over, and I confirmed in
  `elements/decisions/format_guard.py:805-905` that `merged_log`/`log_on_merge_base` file git
  failures exactly that way (`report.error(None, …)`) while `log-merge-copies` goes through the
  owned path, so it never leaks. Invariants: `merged_invariants` (`form_check.py:639-658`) takes
  each identifier from the branch where its sentence fingerprint differs from the fork point
  (`git merge-base HEAD <REF>`, `form_check.py:624`), else from the onto commit; withdrawal and
  removal count as a change. Tested for a change only on the onto commit: decision reworded there
  (F4), decision repealed there (`test_form_check.py:496`), invariant reworded, withdrawn and
  removed there, and reworded on both sides (`test_form_check.py:459`). My extra breaks (below)
  show each side of the rule is held by a test.
- ✅ **Options and record.** `SELECTED_BY` (`form_check.py:99`) makes a `--merge-onto` run record
  `guidelines-reference-current/1` lines only; `none` records the same-commit `pass`/`fail` and the
  merge `unchecked` with `shared.NO_COMMIT_REASON` (`form_check.py:1121-1141`); no option gives the
  `note:`; a no-option run that meets a reference error prints it and exits 1 with only
  `guidelines-form/1` in its record (C28 (5), asserted at `test_form_check.py:365`).
- ✅ **Borrowed code reports nothing of its own (finding 15).** Brief's ordinary test for
  conflicting log copies is present and asserts no `log-merge-copies`, no exit 1, all `pass`.
- ✅ **F4 tests of `guidelines-check-reference-target` and `-stale-reference` pass** (green output
  `reports/slice-3-green-product-guidelines-tests.txt`: 60 OK, 5 and 5 record lines, as reported;
  no noise in it).
- ✅ **C29 kept.** The new git calls take fixed foundation paths and the `--merge-onto` value from
  the command line; nothing from a product's file reaches git.
- ⚠️ **Extra behaviour beyond the brief's goal sentence: narrowing of the carrier checks.**
  *Decision*, the roles table and `none —` lines now need the log's own prefix, *Invariant* an
  identifier of the file (`form_check.py:445-458`, `482-483`). It follows the sentences of
  `guidelines-form/1` and `guidelines-check-carrier/1` ("a decision of the log") more faithfully
  than slice 2 did, so I accept it; the *Invariant* and roles-table halves are untested (Minor 5).
- ⚠️ **What the diff cannot show:** whether `guidelines-reference-current`'s *Part* in the-way
  (`product-guidelines · decisions · invariants`, spec §3.3) should also name `elements-common` and
  `relation-model`, through which its method now runs (`guard_shared.Report/file_at/call_git`,
  `fingerprint.py`). C13 gave those parts to the `guidelines-check-*` entries for this very reason.
  It is a foundation question, outside this slice (no slice edits `foundations/`); for the
  whole-change review.

## Strengths

- One pattern with a look-behind and no nested repetition, every refinement done by `fullmatch` on
  the matched word, digits bounded before `int()`. Clean answer to WAY-48 for the guidelines text.
- The discarded-report borrowing is exact: the carry-over filter matches how the decisions guard
  files its git failures, verified in the guard's code, and tested end to end.
- The version rule is small, symmetric and readable (`merged_invariants`, 20 lines), and tests pin
  both of its sides.
- The weakest-point check was real: the implementer broke the code, saw the tests pass for the
  wrong reason (the stale message holding every asserted fragment), tightened the assertions and
  re-ran the break.
- Test docstrings name the break each test catches; controls show the reference scan reads the line
  under test.

## Issues

### Critical

None.

### Important

None.

### Minor

1. **`form_check.py:1140` with `form_check.py:1203-1204` — the check after the merge records `pass`
   when it never ran.** `merge_check` calls `report.ran(AFTER_MERGE, …)` as soon as the commit
   exists; when the log or invariants file then cannot be read (`foundation.known` false), no merged
   foundation is built and no file is re-checked, yet the run's report still yields
   `check_merged_references … "verdict": "pass"`. Observed on a product whose log exceeds 1 MiB,
   with `--merge-onto HEAD`: the record held `check_references` `fail` and
   `check_merged_references` `pass`. The invariant's result is still `fail` (WAY-65), so no false
   green, but a line of the record says a check passed that did not run (WAY-74). Fix: record the
   merge check `fail` or `unchecked` with the same reason when `foundation.known` is false, or call
   `ran` only once `merged_foundation` returned a foundation.
2. **`form_check.py:955-962` — the check after the merge re-checks only references found current on
   the branch (implementer's concern 2).** A token that becomes a reference only in the merged
   foundation is not seen: the onto commit adds invariant `x`, the branch writes `x@v2`; on the
   branch it is no reference, after the merge it is one with a malformed fingerprint, and it reaches
   the main branch, which WAY-169 wants to prevent. The case is narrow (only a non-eight-hex tail
   after an identifier the onto commit adds, or a prefix that differs between sides) and the next
   same-commit run on the main branch reports it. Judgement: acceptable gap, but it should not stay
   silent. Fix, cheap: in `check_file`, scan `references(document, context.merged)` and check every
   reference not already reported on the branch; otherwise state the limit in the docstring of
   `check_merged_references` and in the request.
3. **`form_check.py:560-561`, limit `form_check.py:109` — the 1 MiB limit now binds the decision log
   and the invariants file (implementer's concern 1).** Judgement: acceptable now, needs an
   orchestrator ruling, not a code change in this slice. The-way's log is 426,585 bytes (about 41%
   of the limit); the foundation is read only when a product has guidelines (`form_check.py:1201`),
   so the-way's own runs never meet it; and the failure is loud (`fail` recorded, exit 1, message
   naming the file), not a silent skip. Two weak spots to put in the ruling: the decisions guard
   reads the same log with no such limit, so the two would disagree on a large log; and the copies
   read from git (`form_check.py:607`, `614`, `630`) have no limit at all, so the limit is not a
   bound on what the parsers read. Options: a separate, higher limit for foundation files, applied
   to git copies too; or accept the limit and say so in spec §5.4.
4. **`form_check.py:133`, `form_check.py:445-451` — decision numbers are normalised, not matched as
   written.** `int()` then `%02d` makes `ABC-5@<fp>` and `ABC-005@<fp>` references to `ABC-05`,
   although the log's grammar is `\d{2,}` (`elements/decisions/format_guard.py:253`); a number of
   ten or more digits silently stops being a reference instead of being reported as a decision the
   log does not hold. Both need a crafted or mistyped file, so nothing breaks in normal use. Fix:
   `[0-9]{2,9}` in `DECISION_NUMBER`, and report a longer run as an absent decision rather than
   dropping it.
5. **Untested branches at the trust boundary and in the narrowing.** No test reaches:
   `read_foundation`'s unreadable and unparsable paths and the fall-back to the slice-2 shape match
   (`form_check.py:553-582`, concern 3); `merge-base` exit 1 with no common ancestor
   (`form_check.py:625`); the *Invariant* and roles-table halves of the narrowing
   (`form_check.py:482-483`, the `check_roles` call of `decisions_named`). Each is small code whose
   mistake would show only on an odd product. Fix: one ordinary test each — a log over 1 MiB, or a
   link, beside a file of guidelines (exit 1, `fail`, no per-file reference lines); an *Invariant*
   naming an identifier the file lacks (carrier error); two unrelated histories with
   `--merge-onto`.
6. **`form_check.py:108` — `PARSE_ERRORS` includes `AttributeError` and `TypeError`.** A
   programming error in the borrowed parsers, or in this script's code inside the `try` blocks
   (`form_check.py:571-579`, `595-599`), is reported as "cannot be parsed" instead of a traceback.
   Cosmetic as long as tests stay green; consider narrowing to the exceptions the parsers are known
   to raise on bad text.
7. **Sharpness inputs — one correction.** The list of borrowed decisions-guard functions omits
   `versions_of` (`read_foundation`, `form_check.py:574`). Otherwise confirmed against the diff:
   parts touched `product-guidelines` only; trust-boundary file `product-guidelines/form_check.py`
   with the two new untrusted inputs as stated; nothing irreversible.
8. **File growth (`form_check.py`, 1247 lines).** In line with its siblings
   (`elements/decisions/format_guard.py` 1242, `elements/invariants/format_guard.py` 1685) and
   divided into sections; no action now. If a later slice adds to it, "what references name"
   (`form_check.py:427-658`) is the natural module to split out.

## Trust boundary (WAY-48)

- **Reference pattern.** `REFERENCE_TOKEN` is linear: a match starts only where no letter, digit or
  hyphen stands before it, so inside a word only its first character can start one; the greedy run
  backtracks once over that word. `IDENTIFIER`, `DECISION_NUMBER`, `FINGERPRINT` run by `fullmatch`
  on a word already matched. Both crafted-line tests (slice-2 line, now through the reference scan,
  and the new `test_form_check.py:658` with one long word ending in `@` + backtick and many `name@`)
  bound the run at 30 s.
- **Borrowed parsers on the product's foundation.** Focused check: a product whose
  `foundations/decisions.md` and `foundations/invariants.md` (about 950 KB each) hold long crafted
  lines aimed at the parsers' lazy and greedy patterns (`- **` + `:*`×95000, `### ABC-` + digits,
  `## ` + `/1`×95000, `## ` + `a/1`×95000, `| ` + `a|`×95000, and others). Form check with
  `--merge-onto none`: exit 0 in 0.3 s; with `--merge-onto HEAD`: exit 0 in 0.4 s. Script
  `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/3c9695bb-97dd-4f98-b7ec-dff4bae7e82e/scratchpad/s3review/crafted_foundation.py`,
  output beside it in `crafted_out.txt`. No runaway found.
- **Reads of the log and invariants file.** The working-tree copies go through `read_untrusted`
  (no links, regular file, at most 1 MiB, UTF-8); `merged_log` is given the log's path only to form
  the relative path for `git show` and does not open it. The git copies are read by fixed paths,
  undecoded errors replaced, no size limit (Minor 3).
- **Outside its contract.** Nothing found: no new subprocess but git, no path from a product's file
  to git or the file system, no write but the record, every value printed through `shown`.
- **Concern 1 (1 MiB on log and invariants file):** see Minor 3 — accept for now, record a ruling.

## Deliberate breaks (WAY-69, WAY-08)

Done in a detached worktree `C:/Storage/repos/the-way-wt/pg-review-s3` at `10b5f4a`; each change
restored (`cmp` with a saved copy) and the worktree removed.

| Invariant | Break | Command | Exit | Detected | Output |
|---|---|---|---|---|---|
| `guidelines-reference-current/1` | A temporary product (valid foundation, log prefix `ABC`) whose `guidelines/testing.md` line 19 reads "Set up each test's data as ABC-05@9f3e2c1d has it." — ABC-05's current fingerprint is `016b5b2a`. Control: the same product with `016b5b2a`. | `python -B product-guidelines/form_check.py --merge-onto none <product> --record …` | 1 (control 0) | Yes: `guidelines/testing.md:19: error: \`ABC-05@9f3e2c1d\` carries a fingerprint other than the current one: … current fingerprint of ABC-05 is 016b5b2a, set by ABC-05/1`; record `check_references` `fail`, merge `unchecked` | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-3-break-guidelines-reference-current.txt` |
| `guidelines-check-reference-target/1` | In `check_references`, the report of a reference to an entry not in force replaced by `pass` (the guard "names a decision the log does not hold or has repealed, or an invariant the file does not hold or has withdrawn"). | `python -B gate/run_tests.py product-guidelines --record …` | 1 | Yes: every subtest of `ReferenceTarget.test_a_reference_to_an_entry_not_in_force_is_reported_wherever_it_stands` fails (28 subtests), plus 3 ordinary tests; record `fail` for the invariant | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-3-break-guidelines-check-reference-target.txt` |
| `guidelines-check-stale-reference/1` | In `check_merged_references`, `elif value != carried:` made `elif value != carried and False:` (the guard "every one whose fingerprint differs … in the foundation a merge onto that commit leaves"). | `python -B gate/run_tests.py product-guidelines --record …` | 1 | Yes: `StaleReference.test_a_reference_a_merge_leaves_stale_is_reported` fails for the decision and the invariant, plus the ordinary "reworded on the commit merged onto alone" | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-3-break-guidelines-check-stale-reference.txt` |

Additional breaks of the version rule (duty 2), appended to the stale-reference file, run with the
focused command `python -B -m unittest test_form_check.References test_form_check_invariants.StaleReference test_form_check_invariants.Fixtures`
from `product-guidelines/`:

- every invariant taken from the onto commit: exit 1, the ordinary "reworded on both sides" subtest
  fails (no F4 test sees this side — it is held by the ordinary test alone);
- every invariant taken from the branch: exit 1, four failures (withdrawn, removed, reworded on onto
  alone; F4's invariant reworded on onto).

No break went undetected.

## Weakest-point check (WAY-164)

Sound. The implementer named the after-merge reading of withdrawn, removed and repealed entries,
which F4 does not assert, wrote tests for it, broke the code, found the tests passing for the wrong
reason and tightened them — evidence in `reports/slice-3-weakest-point.txt` and
`reports/slice-3-weakest-point-break.txt`. It was not the only weak point: the narrower gap of
concern 2 (Minor 2) and the `pass` recorded for an unrun merge check (Minor 1) are less covered,
but neither undermines the requirement named.

Sharpness inputs: confirmed with the one correction in Minor 7.

## Assessment

**Task quality:** Approved.

The slice does what the brief, spec §§3.2, 5.1–5.3 and the F4 contract ask, and every claim I
checked against the diff and the borrowed code held. All three deliberate breaks, and both halves of
the version rule, were caught. The reference pattern and the borrowed parsers withstood crafted long
lines. The eight findings are Minor: a misleading `pass` line for a merge check that did not run,
a narrow merge gap that should at least be stated, a size-limit question for the orchestrator, lax
decision-number parsing on crafted input, and missing tests for error branches. None makes the
slice's result untrustworthy; Minor 1–3 are worth settling before the whole-change review.
