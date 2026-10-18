# Task 2 report — The form check: form, carriers, parts and paths

- **Status:** DONE_WITH_CONCERNS
- **Commits:** `6496a2f` feat(product-guidelines): check the form of a product's guidelines ·
  `2e5d038` fix(product-guidelines): report a directory named like a file of guidelines that git
  lists only through what lies below it (both on `task/product-guidelines-styleguide`, author
  `mariusznn@gmail.com`, base `e62ca49`)
- **Outputs:** every full output named below lies in
  `.runs/task-cycles/product-guidelines-styleguide/reports/` (git ignores `.runs/`).

## What I implemented

`product-guidelines/form_check.py` (859 lines):

- **Command** as spec §5.1 gives it: `[ROOT] [--merge-onto REF|none] [--record PATH]`. ROOT must be
  what `git rev-parse --show-toplevel` prints (checked with `os.path.samefile`), else exit 2. A
  record path not ending in `.jsonl` exits 2 and writes nothing; an unwritable one exits 2.
  `--merge-onto` is accepted and passed to the shared `Report` as the run's option; it selects the
  checks of references, which S3 adds to `SELECTED_BY` (empty now), so a `--merge-onto` run
  records no check of form. Exit 0/1/2.
- **Templates from its own checkout** (C28 (1)): `THE_WAY = dirname(dirname(__file__))`; the form
  is parsed from the fenced block under `## Required form` of `product-guidelines/template.md` and
  of each `product-guidelines/<identifier>/template.md` (today `styleguide`). Placeholders `<…>`
  are free; literal `### ` headings under `## Rules` are required rules; the rule fields come from
  the common form; a section's table header gives the roles columns. Read from the styleguide
  template's prose: the *Kind* list, "its *Invariant* names at least one invariant", and
  `` `guidelines/styleguide-<part>.md` `` (files named per part). Template sanity checks raise →
  exit 2.
- **Reports:** one shared `Report` per file under `guidelines/<name>.md`, one for the run under the
  path `guidelines`; each prints its count line; the record is the lines of all reports. Every
  check function carries `# invariant: guidelines-form/1` and records under it.
- **Errors 1–6 and 5a of §5.3:** missing/misplaced header lines, sections (each once), required
  rules, rule fields (missing ones reported at the heading that should hold them); a rule with no
  `<NUMBER>@…` in *Decision*; in a styleguide (template-driven), no `<identifier>@…` in
  *Invariant*; `## Roles`: columns, cell count, *Kind* outside the list, a background whose
  *Text on it* is no `text` role of the table, a row with no decision, a table decision not named by
  "Each role in its meaning" unless that rule is dropped; a drop holding anything but one line
  `none — <PREFIX-NN>@<8 hex>`; parts in *Applies to* and in the file name checked against the map
  (part-map guard's `read_rules`/`parse_map` loaded by path); name vs *Discipline*
  (`<d>.md`/`<d>-<part>.md`, styleguide only `styleguide-<part>.md`); paths of `## Where in code`.
- **Fenced code** (C28 (4)): ```` ``` ```` and `~~~` fences, closed by the same character at least
  as long; nothing inside counts (headings, fields, rows, paths).
- **What it reads** (§5.2, minus decisions and invariants, which S3 reads): `git ls-files -z
  --cached --others --exclude-standard -- ':(literal)guidelines/'`; every other listed path gets a
  `warning:`; no `guidelines/` → a `note:` and `pass`.
- **Trust boundary** (§5.4): see "Sharpness" and the tests below.

`product-guidelines/test_form_check.py` (479 lines, 20 ordinary tests, no citations — they cover
what no invariant's sentence holds).

## Tests and results

- Ordinary tests: 20/20 pass (`slice-2-green-ordinary.txt`; symlink tests ran, not skipped).
- F4 tests: every test of `Form`, `Carrier`, `ColourPair`, `CodePath` passes. Red, as planned until
  S3: all `ReferenceTarget` and `StaleReference` tests (91 subtests) and **two subtests of
  `Fixtures.test_the_valid_fixtures_pass`** — the `--merge-onto none` and `--merge-onto onto`
  runs, which exit 0 with no error but record no `guidelines-reference-current/1` line. Because that
  test cites all six invariants, the gate record also holds one `fail` each for
  `guidelines-check-form`, `-carrier`, `-colour-pair`, `-code-path` from it until S3.
- `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl` →
  exit 1, `Ran 45 tests`, `FAILED (failures=93)` = 91 reference subtests + the 2 fixture
  subtests. Record: check-form 9 pass / 1 fail, carrier 5/1, colour-pair 1/1, code-path 2/1
  (each fail from the fixtures test), reference-target 0/5, stale-reference 0/5.

## TDD evidence

| Step | Command | Exit | Output | Why this was the expected failure or pass |
|---|---|---|---|---|
| RED, F4 + ordinary | `python -B gate/run_tests.py product-guidelines` (no script) | 1 | `slice-2-red-tests.txt` — `Ran 43 tests`, `FAILED (failures=166, errors=3)`, 169 × "can't open file …form_check.py" | the script did not exist; the 3 errors are the in-process tests loading it |
| RED found two tests passing without the script | same run | — | the record-path and not-a-root tests were absent from the failures: Python itself exits 2 on a missing file | fixed by a positive control in each (the same run with a `.jsonl` path / from the top exits 1) and an assertion on `.jsonl` in the message |
| RED, ordinary after the fix | `python -B -m unittest product-guidelines/test_form_check.py` | 1 | `slice-2-red-ordinary.txt` — `Ran 18 tests`, `FAILED (failures=16, errors=3)`, all "can't open file"/`FileNotFoundError` | script missing |
| GREEN | same, then the F4 file | 0 / 1 | ordinary `OK`; F4 `FAILED (failures=93)`, only reference tests and the 2 fixture subtests | form checks in place, reference checks are S3's |
| RED, directory found by the junction probe | `python -B -m unittest product-guidelines.test_form_check.TrustBoundary.test_an_untracked_directory_named_like_a_guidelines_file_is_an_error` | 1 | `slice-2-red-directory.txt` — `AssertionError: 0 != 1`, only the warning printed | an untracked directory `y.md` reached the run only as `y.md/inner.md` |
| GREEN | `python -B -m unittest product-guidelines/test_form_check.py` | 0 | `slice-2-green-ordinary.txt` — `Ran 20 tests`, `OK` | — |

Not test-first: `test_a_value_taken_from_a_file_is_printed_escaped` was written after `shown()`
existed; it was then shown to catch the break by mutation (`shown` returning its value unescaped →
`FAILED`).

**Mutation checks** (`slice-2-mutations.txt`; each mutation applied, the named test run, the file
restored and compared byte for byte): caught — links followed, decoding with `replace`,
`check_rules` selected by `--merge-onto`, one report for every file, no note without guidelines,
a file `guidelines` not refused, paths sent to git before the shape test, `.MD` read as guidelines,
size limit and read cap both removed, values printed unescaped. Survived, understood: the size
limit alone and the read cap alone (each backs up the other); CRLF normalization (every reader
strips lines, so a CRLF file passes without it — the test guards the behaviour, the normalization
is a second guard).

## Check commands

| Command | Exit | Full output | Result |
|---|---|---|---|
| `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl` | 1 | `slice-2-tests-product-guidelines.txt` (record appended) | expected red: F4 reference tests and 2 fixture subtests until S3 |
| `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | `slice-2-form-check-the-way.txt` | `note: the repository holds no guidelines/…`; record: one `pass` for `guidelines-form/1` |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` (after the commit) | 0 | `slice-2-invariants-guard.txt` | 0 errors, 3 unchecked; no `invariant-citation-target` finding |
| positive control: the same guard with the script's citations changed to `guidelines-forms/1`, staged, then restored | 1 | `slice-2-invariants-guard-control.txt` | 8 errors "cites `guidelines-forms`, which is not an entry" — the guard reads the script's citations |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` (after the commit) | 0 | `slice-2-part-map-guard.txt` | 0 errors, 7 unchecked: the trust boundary and the surface `guidelines-form-check-command` (`form_check.py · main`) name existing items. Before the commit it exited 1 on the untracked trust-boundary file |
| `python -B gate/run_tests.py gate` | 0 | `slice-2-tests-gate.txt` | 98 tests OK |
| `python -B gate/run_tests.py elements/part-map` (extra: the own-map test was red until the trust-boundary file existed) | 0 | `slice-2-tests-elements-part-map.txt` | 162 tests OK |
| weakest-point check (below) | — | `slice-2-weakest-point.txt` | — |
| junction probe (manual, Windows) | — | `slice-2-junction-probe.txt` | below |
| `git diff --check` before each commit | 0 | — | clean |

## Files changed (`e62ca49..2e5d038`)

| File | Added | Removed |
|---|---|---|
| `product-guidelines/form_check.py` | 859 | 0 |
| `product-guidelines/test_form_check.py` | 479 | 0 |

(`6496a2f`: +849 / +468; `2e5d038`: form_check +16/−6, tests +11.)

## Sharpness inputs from the diff

- Parts touched: `product-guidelines` only (two new files). The script loads, without changing,
  `elements/common/guard_shared.py` (elements-common) and `elements/part-map/format_guard.py`
  (part-map), which loads `relation-model/identifier.py`.
- Trust-boundary files: `product-guidelines/form_check.py`, the part's declared trust boundary
  (WAY-48), new. Crafted inputs covered by tests: a symlinked file, a symlinked `guidelines`, a
  tracked file replaced by a directory, an untracked directory `y.md`, `guidelines` as a file,
  non-UTF-8 bytes, a file of 1048577 bytes refused unread (one error only), two ~1 MiB one-line
  files of backticks, `@` and hex runs (prose and `## Where in code`) finished under 30 s with
  both count lines, a control character printed escaped, git calls captured (no refused path in
  any argument, a positive control that `ls-files` was called), `socket.socket`,
  `create_connection` and `getaddrinfo` patched to fail (none called; a control call proves the
  patch). Manual: a Windows junction as `guidelines/` and as `guidelines/inner.md` — both errors,
  nothing read (`slice-2-junction-probe.txt`).
- How the boundary is held: every component looked at with `lstat`, a link or reparse point never
  passed; only a regular file of at most 1048576 bytes, opened with `O_NOFOLLOW` where the platform
  has it and checked by `fstat` to be the file looked at; strict UTF-8; no path a file names is
  opened, and none is given to git (see concern 3); git is the only program; output escaped and
  cut to 200 characters; regular expressions anchored or behind a look-behind, no nested
  repetition.
- Nothing irreversible.

## Weakest-point check (WAY-164)

- **Requirement:** the form check reads the form from the-way's templates of the checkout it lies in
  (brief, spec §5.2, C28 (1), WAY-171 "rules live in the templates") — not from lists in the script
  that happen to match today's templates. The F4 tests cannot tell the two apart: both pass them.
- **Check:** manual, by me (executor), on a copy of this checkout's `product-guidelines/`,
  `elements/` and `relation-model/` in the scratchpad, whose styleguide template gains one required
  rule `### Spacing on a grid` after `### The kitchen-sink page`; the F4 valid fixtures
  (`guidelines/styleguide-web.md`, `guidelines/testing.md`) run through the F4 test harness against
  this branch's script and against the copy.
- **What it showed:** this branch: exit 0, three `0 error(s)` count lines. The copy: exit 1, exactly
  one error, `guidelines/styleguide-web.md:18: error: the required rule `### Spacing on a grid` is
  missing`; `guidelines/testing.md` (no template) unaffected. Evidence:
  `slice-2-weakest-point.txt`. The requirement holds for required rules; it does not hold for the
  three readings from the styleguide template's prose (concern 5).

## No-option run meeting a reference error (C28 (5))

The exit code counts the errors of every report whatever the options, and the record holds only
the checks the options select (shared `Report.recorded`). In S2 there are no reference checks, so a
no-option run reports no reference error at all. Once S3 adds them with `SELECTED_BY` mapping them
to `--merge-onto`, a run with no option still runs and prints them: a reference error prints as
`guidelines/<name>.md:<line>: error: …` and the run exits 1, while its record holds
`guidelines-form/1` lines only — `pass` where the form holds. The verdict of
`guidelines-reference-current/1` comes only from the `--merge-onto` run, and the gate reads verdicts
from the record, not the exit code (WAY-61). This is how the decisions guard treats its merge
checks.

## Self-review findings (fixed before the report)

- A literal BOM character had landed in the source in place of the `﻿` escape — replaced, and
  the escapes of both files checked by a literal search.
- `shown()` escaped a whole value before cutting it — now cuts first.
- Missing fields and required rules were reported at line 0 — now at the heading that should hold
  them.
- The junction probe found an untracked directory or junction named `x.md` reported only as a
  warning — fixed test-first (`2e5d038`).

## Concerns

1. **Fixtures test red until S3.** `Fixtures.test_the_valid_fixtures_pass` cites all six
   invariants and runs with `--merge-onto`, so the gate record gives `guidelines-check-form`,
   `-carrier`, `-colour-pair` and `-code-path` one `fail` each until S3 records the reference
   checks. Recording a `pass` without the check is not an option (WAY-38, WAY-61).
2. **Carrier by shape, not by the log.** With decisions and invariants left to S3, *Decision* counts
   any `<UPPER>-<digits>@…` and *Invariant* any `<identifier>@…`: in a product with prefix `ABC`,
   `WAY-170@c1b230d2` counts as naming a decision, and `react@18` in *Invariant* as naming an
   invariant. S3 should narrow both to the log's prefix and the invariants file's identifiers
   (spec: "names no decision of the log").
3. **Paths never reach git — a departure from the spec's letter.** Spec §5.3 item 6 and §5.4 say
   paths go to git as `:(literal)` pathspecs after the shape test. The script instead asks git once
   for `git ls-files -z` and matches each path in Python against the tracked files and the
   directories holding them (letter case counts, `.` segments and doubled slashes dropped, a
   trailing `/` requiring a directory). The answer is the same for a file or a directory; the
   reason is that one git call per path is unbounded on a crafted file (tens of thousands of
   spans). The shape test also refuses any backslash, any `:`, and unprintable characters — wider
   than the spec's list (absolute, `..`, drive, UNC). The WAY-48 reviewer should judge this.
4. **Not checked, since no item of §5.3 names it:** the title line; sections the template does
   not give; the required examples `### Mockups` and `### Plan of a user-interface change` (the
   invariant's sentence names header lines, sections, rules and fields, not examples); an example
   carrying a *Decision* field; a styleguide's *Applies to* naming more than one part, or a part
   other than its file name's; *Text on it* of a non-background role.
5. **Three readings from template prose by regular expression:** whether every rule needs an
   invariant ("its *Invariant* names at least one invariant"), whether files are named per part
   (`` `guidelines/styleguide-<part>.md` ``), and the *Kind* list. The *Kind* list raises a
   template error when missing (exit 2); the other two would silently switch their requirement off
   if the styleguide template were reworded. The structural words `Rules`, `Where in code`,
   `Roles` columns and `Each role in its meaning` are constants checked against the templates at
   start.
6. **Windows reparse points:** a file that is a cloud placeholder (OneDrive) is a reparse point and
   is refused like a link.
7. **Run-level findings print under `guidelines:0:`**, the run report's path — a part map that
   cannot be read included. With `--merge-onto`, nothing of form is recorded, read failures
   included; S3 decides what a `--merge-onto` run records for a file it could not read.
8. **Size.** `form_check.py` is 859 lines before S3 adds references and the merge; not split.
9. **Known mismatch carried, not settled** (ledger M6): names `guidelines/<discipline>-<part>.md` are
   accepted, as the spec and the F4 tests have it, though WAY-167 does not give them.

## Fix round 1 (review `task-2-review.md`, findings I1 and I2)

- **Commit:** `d79f692` fix(product-guidelines): report a file named for a discipline with a
  template under another Discipline, and pin the guards on absolute and .. paths —
  `product-guidelines/form_check.py` +11/−3, `product-guidelines/test_form_check.py` +31/−0.
  Branch range of the slice now `e62ca49..d79f692` (with the F4 author's `8d97ab9` between,
  not mine).

### Changes

- **I1** — `check_parts` (`form_check.py`, the name test of 5a) now receives the disciplines the-way
  gives templates of; before accepting `<discipline>.md` or `<discipline>-<part>.md`, it refuses a
  file whose name is `<t>.md` or `<t>-<part>.md` for a discipline `t` with a template while
  *Discipline* is not `t`: "the file's name is one of guidelines of the discipline `styleguide`,
  whose template the-way gives, but its *Discipline* reads `styleguide-web`; it would be held to
  the wrong form". `guidelines/styleguide-web.md` with *Discipline* `styleguide-web` now exits 1.
- **I2** — no code change: the guards were correct; they gained ordinary tests in which each alone
  decides.

### Covering tests (new, in `test_form_check.py`)

- `Names.test_a_name_of_a_discipline_with_a_template_under_another_discipline_is_an_error` —
  the case of I1; exit 1 and an error under `guidelines/styleguide-web.md` naming
  `styleguide-web` and *Discipline*.
- `Paths.test_a_path_refused_for_its_form_whose_remainder_git_tracks_is_an_error` —
  `/tests/fixtures.py` (error at line 29 naming "absolute") and `./../tests/fixtures.py` (error at
  line 29 naming "`..` segment"); `tests/fixtures.py` is tracked, so only the guard decides.

### Evidence

| Step | Command | Exit | Full output |
|---|---|---|---|
| RED, I1 | `python -B -m unittest product-guidelines.test_form_check.Names product-guidelines.test_form_check.Paths` (before the fix) | 1 | `slice-2-fix1-red.txt` — `Names…` fails `0 != 1` (run exits 0, `0 error(s)` twice); `Paths…` passes on the correct guards |
| RED, I2 by mutation | the `Paths` test against the script with `if path.startswith("/")` removed, then with the `..` guard removed and `..` resolved by `normpath` (script restored and compared byte for byte) | 1, 1 | `slice-2-fix1-red.txt` (appended) — each fails its subtest, `0 != 1` |
| GREEN, ordinary | `python -B -m unittest product-guidelines/test_form_check.py` | 0 | `slice-2-fix1-green-ordinary.txt` — `Ran 22 tests`, `OK` |
| product-guidelines | `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl` | 1 | `slice-2-fix1-tests-product-guidelines.txt` (record appended) — `Ran 48 tests`, `FAILED (failures=93)`: the same 91 reference subtests and the 2 `--merge-onto` subtests of `test_the_valid_fixtures_pass` as before, red until S3; the F4 author's new `CodePath.test_a_path_out_of_the_repository_is_reported_though_its_remainder_is_tracked` passes (code-path 3 pass, 1 fail from the fixtures test) |
| invariants guard | `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | `slice-2-fix1-invariants-guard.txt` |
| part-map guard | `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | `slice-2-fix1-part-map-guard.txt` |
| form check on the-way | `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | `slice-2-fix1-form-check-the-way.txt` — `pass` for `guidelines-form/1` |
| gate | `python -B gate/run_tests.py gate` | 0 | `slice-2-fix1-tests-gate.txt` |

### For the author of the F4 tests (I2, not edited: WAY-03)

`CodePath.test_a_path_outside_what_git_tracks_is_reported` used absolute paths (`/etc/passwd`,
`//host/share/x`) whose remainders name nothing git tracks, so removing the absolute-path guard
left it green. Commit `8d97ab9` (`test_a_path_out_of_the_repository_is_reported_though_its_remainder_is_tracked`)
now holds remainders that git tracks; the ordinary test above pins the same guards as well.
