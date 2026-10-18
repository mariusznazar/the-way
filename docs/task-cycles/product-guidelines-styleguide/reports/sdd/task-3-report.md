# Task 3 report — the form check: references and the merge

Status: DONE. Commit `10b5f4a` on `task/product-guidelines-styleguide` (author
`mariusznn@gmail.com`), on top of `d79f692`.

## What I implemented

`product-guidelines/form_check.py`:

- **Finding references.** One pattern, `REFERENCE_TOKEN`
  `(?<![A-Za-z0-9-])([A-Za-z0-9][A-Za-z0-9-]*)@([A-Za-z0-9]+)`, finds each word followed by `@`
  and a run of letters and digits. It runs on every line outside fenced code, all sections
  included, inline code included. A fence of either character counts, as the slice-2
  `fenced_lines` reads it. Each match is then sorted in Python:
  - a decision number with the log's prefix (`DECISION_NUMBER`, digits bounded to 9) is a
    reference to a decision;
  - an identifier the invariants file holds, as an entry or as a withdrawn identifier, is a
    reference to an invariant;
  - any other identifier is a reference to an invariant only when exactly eight lower-case hex
    characters follow its `@`;
  - everything else is no reference: `react@18`, `lucide-react@0`, `anna@example.com`, and a
    number with another log's prefix such as `WAY-169@e2fb088c`.
- **Same-commit check** (`check_references`, cites `guidelines-reference-current/1`). It reports:
  - a part after `@` that is not eight lower-case hex characters;
  - a decision the log does not hold;
  - a decision whose latest version holds no binding sentences (repealed);
  - an invariant the file does not hold, or has withdrawn;
  - a fingerprint other than the current one, naming the entry, its current fingerprint and the
    version that set it.

  The foundation is read from the working tree through `read_untrusted`. An absent file is a note;
  an unreadable one is an error.
- **Check after the merge** (`check_merged_references`). It re-checks the references found current
  on the commit checked, against the foundation that `merged_foundation` builds:
  - **Decisions:** `elements/decisions/format_guard.py:merged_log`, given a `Report` of the check's
    own that is discarded. Only its failures with no check, which are git failures, carry over.
    `log-merge-copies` never reaches the output or the record.
  - **Invariants:** each identifier as on the branch where its sentence (fingerprint) differs from
    the fork point (`git merge-base HEAD <REF>`), and as on the onto commit otherwise. A
    withdrawal or removal counts as a change of sentence.

  Every fingerprint is computed by `relation-model/fingerprint.py`, loaded by path. No message
  offers to renew a fingerprint.
- **Record and options.** `SELECTED_BY` maps `check_references` and `check_merged_references` to
  `--merge-onto`, so a run given `--merge-onto` records `guidelines-reference-current/1` lines
  only. The other cases (`merge_check`):
  - `--merge-onto none`: the same-commit check records `pass` or `fail`. The merge check is
    `unchecked`, with `shared.NO_COMMIT_REASON` and `shared.NO_MERGE_ONTO`, plus an `unchecked:`
    line.
  - No option: a `note:` says the merge check is not run.
  - A commit that does not exist: an error of the run, from `shared.find_commit`.
  - A file of guidelines, or the listing, that cannot be read also records `fail` for the
    reference check, through `Report.fail`, with no second printed line.
- **C28.5 kept.** A no-option run that meets a reference error prints the `error:` line and exits
  1, while its record holds `guidelines-form/1` lines only (ordinary test asserts it).
- **Narrowing (C28.3).** What counts as a decision is now a number with the product's log prefix.
  What counts as an invariant is an identifier of its invariants file, an entry or a withdrawn
  one. This applies to a rule's *Decision* and *Invariant*, to the decisions of the roles table and
  of the meaning rule, and to a `none —` drop line. Where the log or the invariants file cannot be
  read, these fall back to the slice-2 shape match, so one unreadable file does not cascade into an
  error on every rule.
- **Borrowing.** `borrow()` now returns the shared code, the part-map, decisions and invariants
  guards, and `fingerprint.py`. `run()` reads the invariants template's rules (exit 2 if it cannot).
  - Touched slice-2 line: the part map's `read_rules` failure now catches `part_map.TemplateError`.
  - Why: each guard loads its own `guard_shared`, so the old `shared.TemplateError` was a different
    class and would not have caught it.

`product-guidelines/test_form_check.py`: a `References` class with 11 tests, one crafted-line test
in `TrustBoundary`, and the helpers `product_onto` and `invariants_with`. The three new
fingerprints are literals computed once by hand with `relation-model/fingerprint.py`.

## Tests and results

- `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl`
  - Exit 0: "Ran 60 tests … OK".
  - Record: every `guidelines-check-*` passes (reference-target 5, stale-reference 5).
  - Full output and record: `.runs/task-cycles/product-guidelines-styleguide/reports/slice-3-green-product-guidelines-tests.txt`.
- Ordinary file alone: 34 tests OK.

## TDD evidence

- **RED, ordinary tests.**
  - Command: `python -B -m unittest product-guidelines/test_form_check.py`, run before any
    behaviour change.
  - Result: exit 1, "Ran 33 tests … FAILED (failures=13)".
  - Output: `reports/slice-3-red-ordinary.txt`.
  - The failure the brief starts from: a run with `--merge-onto` recording REFERENCES lines only
    (`AssertionError: [] is not true`, empty record).
  - Also failing:
    - the no-option reference error ("0 != 1");
    - the missing note;
    - the other prefix in *Decision* and in a drop line;
    - the merge reading of invariants (3 subtests);
    - the log-copies test (no `pass` recorded);
    - a commit that does not exist;
    - the no-guidelines record;
    - the controls of the package-name and fence tests.
  - The new long-line test passed at RED, as a guard should.
- **RED, F4.**
  - Command: `python -B -m unittest test_form_check_invariants.Fixtures
    test_form_check_invariants.ReferenceTarget test_form_check_invariants.StaleReference`, from
    `product-guidelines/`.
  - Result: exit 1, "Ran 8 tests … FAILED (failures=93)".
  - Output: `reports/slice-3-red-f4.txt`.
- **GREEN.**
  - The ordinary file: 33/33 OK.
  - Then the full suite, as above (60 tests OK; the 34th ordinary test was added at the
    weakest-point check).

## Check commands (exit code, full output)

All paths are under `.runs/task-cycles/product-guidelines-styleguide/reports/`.

| Command | Exit | Output |
|---|---|---|
| `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl` | 0 (60 OK) | `slice-3-green-product-guidelines-tests.txt` |
| `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl` | 0 — `check_references` pass, `check_merged_references` unchecked with the shared reason | `slice-3-form-check-merge-none.txt` (record appended) |
| `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 — `guidelines-form/1` pass | `slice-3-form-check-form.txt` |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 (0 errors, 3 unchecked) | `slice-3-invariants-guard.txt` |
| `python -B gate/run_tests.py elements/decisions` | 0 (169 OK) | `slice-3-tests-elements-decisions.txt` |
| `python -B gate/run_tests.py elements/invariants` | 0 (233 OK) | `slice-3-tests-elements-invariants.txt` |
| `python -B gate/run_tests.py relation-model` | 0 (19 OK) | `slice-3-tests-relation-model.txt` |
| `python -B gate/run_tests.py gate` | 0 (98 OK) | `slice-3-tests-gate.txt` |
| End to end, scratch script below | 0 | `slice-3-e2e.txt` |

All rows were re-run after the last code change.

**End to end** — scratch script
`C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/3c9695bb-97dd-4f98-b7ec-dff4bae7e82e/scratchpad/e2e_reference.py`:

- It builds a temporary product:
  - a log with prefix `DEC`;
  - two invariants;
  - part `web`;
  - `src/tokens.css`;
  - `guidelines/styleguide-web.md`, filled from the merged form of the styleguide template: Roles
    table, all nine required rules (two kept, seven dropped by DEC-02), examples, where in code.
- Before the change, the no-option run and the `--merge-onto none` run both exit 0.
- After DEC-01/2 rewords DEC-01, the run exits 1 with five errors (lines 14, 15, 21, 30, 69), each
  of the form "`DEC-01@28b1c96c` carries a fingerprint other than the current one: on the commit
  checked, the current fingerprint of DEC-01 is 74319a6f, set by DEC-01/2". Both fingerprints
  are in the message.

**WAY-48, for the reviewer.**

- **Pattern.** `REFERENCE_TOKEN` has no nested repetition. Its look-behind lets a match start only
  where no letter, digit or hyphen comes before, so a word is scanned from one place, and
  backtracking within it is linear. `IDENTIFIER` and `DECISION_NUMBER` run only with `fullmatch`
  on a word already matched, and `DECISION_NUMBER` bounds digits to 9, so `int()` never meets a
  crafted run of digits.
- **Test.** The slice-2 crafted-line test (`TrustBoundary.test_a_file_just_under_one_mebibyte_…`)
  now passes through the reference scan too.
- **New test** (`…_words_and_at_signs_…`), on a line just under 1 MiB:
  - one word of letters, digits and hyphens ending in `@` and a backtick;
  - many `name@` followed by no letter or digit.

  Both finish well within the 30 s bound.

## Files changed (`d79f692..10b5f4a`)

| File | Added | Removed |
|---|---|---|
| `product-guidelines/form_check.py` | 437 | 57 |
| `product-guidelines/test_form_check.py` | 272 | 4 |

## Sharpness inputs from the diff

- **Parts touched:** `product-guidelines` only. The diff reads, without changing, `decisions`
  (`merged_log`, `parse_log`, `detect_prefix`, `same_binding`, `label_of`), `invariants`
  (`parse_file`, `read_rules`, `Entry`, `Table`, `label_of`), `elements-common` (`Report`,
  `call_git`, `file_at`, `find_commit`, `NO_COMMIT*`) and `relation-model` (`fingerprint`).
- **Trust-boundary file:** `product-guidelines/form_check.py`, a WAY-48 boundary. New untrusted
  inputs:
  - the product's `foundations/decisions.md` and `foundations/invariants.md`, read from the
    working tree through `read_untrusted`;
  - the same two files on the fork point and the onto commit, through `git show <commit>:<fixed
    path>`.

  No path taken from a product's file reaches git (C29 kept). The new git calls are `merge-base
  HEAD <REF>`, `rev-parse --verify`, `show`/`ls-tree` with the fixed foundation paths, and the
  decisions guard's own calls inside `merged_log`.
- **Irreversible:** nothing. No file of `foundations/` and no F4 test is touched.

## Weakest-point check (WAY-164)

- **Requirement most likely unmet:**
  - Text: "with `--merge-onto`, after the merge … an invariant as on the branch where its sentence
    differs from the fork point, else as on the onto commit", together with "a decision absent or
    repealed" after the merge.
  - Why: F4 asserts only a rewording on the onto commit, so an entry the onto commit withdraws,
    removes or repeals could pass the merge unseen.
- **Checks (tests, actor: me):**
  - `References.test_an_invariant_after_a_merge_is_the_branch_s_where_its_sentence_changed_there`,
    with four cases: withdrawn on onto, removed on onto, reworded on both sides (the branch's
    wins), reworded on onto alone.
  - `References.test_a_decision_the_commit_merged_onto_repeals_is_not_in_force_after_the_merge`.
- **What it showed:**
  - Both pass: exit 0, `reports/slice-3-weakest-point.txt`.
  - A first deliberate break went unseen, so I tightened the tests. The break was the
    not-in-force branch of `check_merged_references` disabled (`if value is None and False:`).
    It still passed the tests, because the stale-fingerprint message then fired with
    `current fingerprint … is None, set by its latest version, ABC-05/2 …`, which held every
    fragment the tests asked for.
  - After I tightened the assertions to the wording "not in force after a merge onto onto", the
    same break fails 3 subtests: `reports/slice-3-weakest-point-break.txt`, exit 1. The source
    was then restored byte for byte (`cmp` with the saved copy).

## Self-review

- Exact values of the brief:
  - the `guidelines-reference-current/1` record;
  - `NO_COMMIT_REASON`, plus the `--merge-onto none` description;
  - a `note:` with no option;
  - every F4 reference test passes;
  - no `log-merge-copies` line and no exit 1 when the log's copies conflict (ordinary test).
- **Messages:**
  - Each names the reference (escaped through `shown`), the entry and the current fingerprint,
    with the version that set it.
  - None tells the reader to change a fingerprint.
- **Lookups:**
  - Withdrawn wins over an entry of the same identifier.
  - An entry's highest version is taken.
  - Decisions are ordered by (number, version), as `merged_log` orders them.
- **Merge check scope:** it re-checks only references current on the commit checked. A reference
  already failing there is reported once, not twice.
- **Minor findings of the slice-2 review:** not addressed, except the `TemplateError` catch on a
  line I changed.

## Concerns

1. **The 1 MiB limit now applies to the decision log and the invariants file.** They are read
   through `read_untrusted`, whose limit is 1 MiB. The-way's log is 427 KB today. A product whose
   log grows past 1 MiB gets an error, and its references are unchecked. The spec sets the limit
   for guidelines files only, so this needs a decision: a higher limit for foundation files, or
   accept it.
2. **A token can become a reference only after the merge, and then it is missed.** The merge check
   re-checks only references that were current on the commit checked. Suppose the onto commit adds
   an invariant `x`, and the branch's guidelines write `x@v2`: on the branch, `x@v2` is no
   reference (unknown identifier, no eight-hex fingerprint), so the merge check does not see it.
   The next same-commit run on main reports it.
3. **With no readable log or invariants file, the carrier checks fall back to the slice-2 shape
   match.** In that state a rule naming another log's number passes the form checks. The reference
   check then does not run per file, and the run's report holds the reading error (`fail` for
   `guidelines-reference-current/1`).
4. **`form_check.py` is now 1247 lines.** It was 867, and the plan sets no line budget. The added
   code is one section, "what references name", plus two checks and `merge_check`.
