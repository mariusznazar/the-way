# Task 2 review — The form check: form, carriers, parts and paths

- **Reviewed:** `e62ca49..2e5d038` (`6496a2f`, `2e5d038`), from the review package
  `.superpowers/sdd/plan-tasks/review-e62ca49..2e5d038.diff`; runs in the detached worktree
  `C:/Storage/repos/the-way-wt/pg-review-s2` at `2e5d038`, removed after the review.
- **Read against:** `task-2-brief.md`, `global-constraints.md`, spec §3–§5
  (`.runs/task-cycles/product-guidelines-styleguide/spec.md:105-437`), rulings C11–C13 and C28
  (`cycle.md:80-82`, `cycle.md:97`), `foundations/invariants.md:2133-2212`, the contract
  `product-guidelines/test_form_check_invariants.py`, and the styleguide template
  `product-guidelines/styleguide/template.md:1-90`.
- Line numbers below are of the files at `2e5d038`: `product-guidelines/form_check.py` (FC) and
  `product-guidelines/test_form_check.py` (TFC).

## Spec Compliance

❌ **One item of §5.3 is missed: 5a lets a styleguide escape its template.** Spec §5.3 5a
(`spec.md:397-401`) names `guidelines/styleguide-web.md` "naming another discipline" an error "so no
file is held to the wrong template in silence" (root, finding R9). A file
`guidelines/styleguide-web.md` whose *Discipline* reads `styleguide-web` passes with exit 0: the name
is `<discipline>.md` for the discipline `styleguide-web`, which has no template, so the file is held
to the common form alone — no `## Roles`, no required rule, no invariant per rule. Probe below
(Important 1).

✅ Everything else the brief's goal lists is present in the diff:

- the command of §5.1 — `ROOT` checked against `git rev-parse --show-toplevel` (FC:806-814),
  `--merge-onto` accepted and handed to the shared `Report` as the option that selects the
  reference checks, with `SELECTED_BY` empty until S3 (FC:73, FC:816-817), `--record` refused
  without `.jsonl` and before anything is written (FC:776-785), exit codes 0/1/2 (FC:838), one
  `Report` per file under `guidelines/<name>.md` and one for the run under `guidelines`
  (FC:817-832);
- templates read from the checkout the script lies in (C28 (1), FC:63-65, FC:274-321);
- what §5.2 gives except decisions and invariants: the `ls-files` call of §5.2 word for word
  (FC:687-689), a `warning:` for every other listed path (FC:705-706), a `note:` and `pass` with no
  `guidelines/` (FC:672-674) — confirmed by the record of the-way's own run the report names;
- `~~~` fences as fenced code, closed only by the same character at least as long (C28 (4),
  FC:359-377) — confirmed by the deliberate break of `guidelines-form/1` below;
- errors 1–6 of §5.3 under `guidelines-form/1`, the F4 tests of `Form`, `Carrier`, `ColourPair` and
  `CodePath` passing (baseline run below: the only failures are the 91 reference subtests and the 2
  `--merge-onto` subtests of `Fixtures`, expected until S3);
- `# invariant: guidelines-form/1` in every check function that records it (FC:404, 416, 453, 505,
  567, 613, 666, 726);
- the part-map guard's parser loaded by path (FC:119-128). Its `read_rules` and `parse_map`
  (`elements/part-map/format_guard.py:201`, `:285`) take no report, so "a discarded report of its
  own" has nothing to discard: the requirement holds vacuously;
- the statement C28 (5) asks for (report, "No-option run meeting a reference error") — it matches
  `Report.recorded` (`elements/common/guard_shared.py:241-246`).

⚠️ **What the diff cannot show, or leaves to a later decision:**

- **The departure from §5.3 item 6 and §5.4 on paths** (concern 3) is a change of the spec's letter
  that only the spec's owner can accept; the trust-boundary judgement is below (WAY-48). It needs a
  line in the cycle's ledger, not only a concern in a report.
- **Carriers by shape** (concern 2): with the log and the invariants file left to S3, *Decision*
  accepts any `<UPPER>-<digits>@…` and *Invariant* any `<identifier>@…` (`react@18` included).
  The invariants' sentences say "a decision of the log"; S3 must narrow both, and its review should
  check that it did.
- **Required examples and the place of further rules.** The styleguide template calls `### Mockups`
  and `### Plan of a user-interface change` required ("the required rules and examples of the
  styleguide in their places", `styleguide/template.md:19-21`) and says "The product's further rules
  follow the required ones" (`styleguide/template.md:63-64`). The script reads the examples into
  `Form.required["Examples"]` (FC:262-265) and checks neither. No invariant's sentence names
  examples, and "rules … in their order" does not clearly cover a further rule placed between
  required ones, so this is not a miss of this task; it is a gap between the template and its
  check for the whole-branch review to settle (either the template stops calling them required or
  a check and an invariant say so).
- **`--merge-onto` records nothing** until S3 fills `SELECTED_BY`; a `--merge-onto` run on a
  product today writes an empty record. Expected, and the two `Fixtures` subtests show it.

## Strengths

- The trust boundary is held by construction, not by a list of bad inputs: every component
  `lstat`-ed with links and reparse points refused (FC:157-178), a size test before and a read cap
  after opening, the opened file compared by `(st_dev, st_ino)` with the one looked at
  (FC:186-209), strict UTF-8 (FC:210-213). No path a file names reaches the file system or git.
- `2e5d038` closes a real hole the implementer found himself with a Windows junction probe: an
  untracked directory `y.md` that git lists only as `y.md/inner.md` would have been a warning and
  never an error (FC:707-711, TFC:320-329).
- Every value from a product's file is cut, then escaped, before it is printed (FC:134-139), and a
  test with a terminal escape sequence proves it (TFC:380-390).
- The ordinary tests carry positive controls where a test could pass for the wrong reason: the
  record-path and not-a-root tests first show the same run exiting 1 (TFC:441-451, TFC:453-462),
  the socket test proves its own patch (TFC:419-437), the git-capture test proves `ls-files` was
  seen (TFC:413).
- Structural words are checked against the templates at start, and a broken template exits 2
  (FC:274-321), so most template drift fails loudly.

## Issues

### Critical

None.

### Important

#### 1. A styleguide whose *Discipline* reads `styleguide-<part>` is held to the common form in silence

**Anchor:** `product-guidelines/form_check.py:579-592` (`check_parts`, the name test of 5a), with
`product-guidelines/form_check.py:652` (the form chosen by *Discipline*).

**What:** the name test accepts a file when its stem equals *Discipline* (`stem == discipline and
not form.per_part`). For *Discipline* `styleguide-web` in `guidelines/styleguide-web.md`, the form
looked up at FC:652 is the common one (no template `styleguide-web`), `per_part` is False, the stem
equals the discipline, and no error is reported.

**Why:** spec §5.3 5a (`spec.md:397-401`) gives this exact file as an error — "a styleguide is
always `styleguide-<part>.md`; `guidelines/styleguide-web.md` naming another discipline … is an
error, so no file is held to the wrong template in silence" (root, finding R9). The probe
(`make_probe.py … discipline`, the common-form testing file written under the name
`guidelines/styleguide-web.md` with `- **Discipline:** styleguide-web`) printed two
`0 error(s), 0 warning(s), 0 unchecked` lines and exited 0: no `## Roles`, none of the nine
required rules, no invariant per rule — every check of the styleguide's template is skipped while
the run passes. The name the product chose is exactly the name of a styleguide; a reader and every
other tool take it for one. The F4 tests do not hold this case
(`test_form_check_invariants.py:470-481`), and the ordinary tests do not either.

**Fix:** in the name test, before accepting `<discipline>.md` or `<discipline>-<part>.md`, refuse a
file whose name matches `<t>.md` or `<t>-<part>.md` for a discipline `t` the-way holds a template
of while *Discipline* is not `t` — the message as the existing one ("does not agree with its
*Discipline*"). An ordinary test in `test_form_check.py`: `guidelines/styleguide-web.md` with
*Discipline* `styleguide-web` exits 1 with an error naming the discipline. Test first.

#### 2. Removing the guard against an absolute path goes unseen by every test

**Anchor:** `product-guidelines/form_check.py:603-604` (`refused`), with
`product-guidelines/form_check.py:637` (the normalization that drops empty segments).

**What:** the deliberate break of `guidelines-check-code-path/1` removed the two lines that refuse a
path starting with `/`; the whole `product-guidelines` suite gave the same verdicts as before (see
"Deliberate breaks"). Every absolute path the tests use — `/etc/passwd`, `//host/share/x` — still
fails afterwards, only as "names nothing git tracks". But the normalization at FC:637 drops the
empty first segment, so with the guard gone `/tests/fixtures.py` becomes `tests/fixtures.py` and
passes as a tracked file.

**Why:** the sentence of `guidelines-check-code-path/1` (`foundations/invariants.md:2205`) makes
"absolute" an error of its own, whatever git tracks; the tests give that guard no case in which it
alone decides. The guard is correct today (the probe `make_probe.py … absolute` reports
`/tests/fixtures.py` at its line); the finding is that a later edit can drop it with the gate
green. This is WAY-69's point: the invariant's tests must fail on a break of what its sentence
speaks of. The F4 file is read-only (WAY-03), so the case belongs in the ordinary tests, and the
contract's gap is worth naming to its author.

**Fix:** an ordinary test in `TFC` `TrustBoundary` (or a new class): `## Where in code` naming
`/tests/fixtures.py`, a tracked file once its slash is dropped, exits 1 with an error at its line
naming "absolute". The same for `./../tests/fixtures.py` would pin the `..` guard against a later
normalization that resolves `..`. Report the gap of `CodePath.test_a_path_outside_what_git_tracks_is_reported`
to the author of the F4 tests rather than editing it.

### Minor

#### 3. A broken part-map template exits 1 with a traceback, not 2

**Anchor:** `product-guidelines/form_check.py:801-805`.

**What:** `except (…, shared.TemplateError, …)` names the `TemplateError` of the copy of
`guard_shared.py` the form check loaded. The part-map guard loads a copy of its own
(`elements/part-map/format_guard.py:73-74`) and raises that copy's class
(`format_guard.py:115`, `TemplateError = shared.TemplateError`). Two loads by path make two
distinct classes, so the clause never matches.

**Why:** spec §5.1 gives exit 2 when "a template of the-way" cannot be read. Focused check: on a
copy of the-way pieces in the scratchpad whose `elements/part-map/template.md` lost its field
lines, the form check printed a traceback ending
`elements_common_guard_shared.TemplateError: no fields in the form of "Part"`, exited 1 and left
the record empty — the exit code says "errors in the guidelines" for a run that could not start.
The input is the-way's own, so the harm is a misleading exit and an unexplained empty record, not
a wrong `pass`.

**Fix:** catch `part_map.TemplateError` (or `part_map.shared.TemplateError`) beside
`shared.TemplateError`, and add the case to `CannotRun` (a copy of the-way whose part-map template
gives no fields exits 2 naming the template).

#### 4. The path test refuses legitimate tracked paths holding `:` or `\`

**Anchor:** `product-guidelines/form_check.py:599-602`.

**What:** any `\` and any `:` anywhere in a path is refused. Since no path reaches git or the file
system any more, these refusals add no safety: a URL, `C:/x`, `:(glob)**` and a UNC path all fail
the tracked-set lookup anyway (they cannot be index paths). What the wider test adds is false
errors: on POSIX, a tracked `docs/a:b.md` or `src/a\b.css` is reported, though
`guidelines-form/1` holds for it ("each path … naming something git tracks").

**Why:** the sentence of `guidelines-check-code-path/1` lists absolute, `..`, a drive and a UNC
prefix; a drive is `^[A-Za-z]:`, a UNC prefix `\\` or `//` at the start. Rare in practice, and a
product can rename, so Minor — but it is a departure from both sentences that the report presents
as "wider than the spec's list" without saying it can fail a file the invariant passes.

**Fix:** refuse `:` only as a drive (`^[A-Za-z]:`) or a leading `:` (pathspec magic, kept for the
day a path does reach git), and `\` only where Windows would read it as a separator or UNC prefix;
or keep the wider test and record the departure, with this price, in the cycle's ledger.

#### 5. Quadratic de-duplication of listed guidelines

**Anchor:** `product-guidelines/form_check.py:701-711`.

**What:** `if name not in names` and `first not in names` test a list. A crafted product with tens
of thousands of `guidelines/a<N>.md` makes the listing quadratic (100 000 files ≈ 5·10⁹ string
comparisons).

**Why:** the docstring promises a run bounded on crafted input (FC:39-45), and the bound the tests
show is per line, not per file count. Low likelihood; one-word fix.

**Fix:** keep a `set` beside `names` (or drop `names` membership: `seen` already removes duplicate
paths, and only the directory case can add a name twice).

#### 6. `setUp()` called again inside a subtest loop

**Anchor:** `product-guidelines/test_form_check.py:365`.

**What:** the 1 MiB test calls `self.setUp()` per subtest to get a fresh repository, leaving the
first temporary directory unused and making `self.root` change under the test.

**Why:** it works, but it reads as a mistake and breaks if `setUp` gains state that must not be
duplicated. A helper `fresh_root()` used by `setUp` and the loop says what is meant.

**Fix:** extract the directory creation into a helper and call it from both.

#### 7. Missing sections are reported at line 0

**Anchor:** `product-guidelines/form_check.py:428-429`.

**What:** `check_sections` passes no `missing_at`, so a missing section prints as
`guidelines/<name>.md:0:`. Rules and fields got a heading line in the self-review; sections did not.

**Why:** line 0 is no line of the file; an editor jump lands nowhere. The heading of the section
before the missing one, or the last line of the file, would point where it belongs.

**Fix:** pass the line of the preceding found section (or 1), or keep 0 and say so in the
docstring.

## The trust boundary (WAY-48)

Read against spec §5.4 (`spec.md:412-426`), the crafted inputs of the brief and the departure:

- **Links, reparse points, directories, non-regular files:** every component is `lstat`-ed from the
  root (FC:157-178); a link or reparse point at any depth is refused; `O_NOFOLLOW` where the
  platform has it, and the `(st_dev, st_ino)` comparison after opening catches a swap at the last
  component (FC:186-195). `guidelines` itself a link or a file is refused before git is asked
  (FC:679-686). The part map goes through the same reader (FC:729). ✅
- **Encoding and size:** strict UTF-8 with no guess (FC:210-213); the size is tested on `lstat`
  and the read is capped at `MAX_BYTES + 1` (FC:182-208). ✅
- **Matching:** every regular expression is anchored or behind a look-behind, with no nested
  repetition (FC:92-102); `FIELD_LINE`'s lazy `.+?` and the tokens' greedy runs stay linear because
  each start is a word start. The part-map guard's own patterns, which also run on the product's
  map (`format_guard.py:106-108`), are of the same shape. ✅
- **Paths and git — the departure.** No path a file names is opened or given to git; git is asked
  once, `ls-files -z` with no pathspec, and each path is matched in Python against the index's
  files and the directories holding them (FC:743-765, FC:619-643). I checked the answer against
  what `git ls-files -- ':(literal)<path>'` would give: a file, a directory through the files below
  it, a trailing `/` requiring a directory, `.` segments and doubled slashes, untracked files not
  counting, a path inside a submodule not counting — the same in each. This is stricter than the
  spec's letter on the boundary (nothing of the file reaches git at all) and bounded where the
  letter is not (one git call, not one per span of a crafted file). **No input escapes**: there is
  no channel left from the file's text to a process or the file system. The price is item 4
  above (false errors for `:` and `\`) and the coverage gap of item 2.
- **Network:** only git runs; the script's own code opens no socket (TFC:419-437). ✅
- **Writes:** only the record and its directory (FC:776-785, FC:768-771). ✅
- **Output:** values cut and escaped (FC:134-139). The reasons `read_untrusted` returns embed only
  `guidelines` or `foundations` as a path component and an OS message, never a name from a file. ✅

Inputs I looked for that would escape and found none: a hard link inside `guidelines/` is not
something git writes, so it lies outside the boundary the spec sets; an intermediate directory
swapped for a link between `lstat` and `open` is caught by the inode comparison only at the last
component, but a race against the run on the product's own checkout is outside the threat this
boundary answers (a product's committed files).

## Deliberate breaks (WAY-69, WAY-08)

Baseline in the worktree before any break: `python -B gate/run_tests.py product-guidelines --record
<scratch>/baseline.jsonl` → exit 1, `Ran 45 tests`, `FAILED (failures=93)`; record: check-form 9
pass / 1 fail, carrier 5/1, colour-pair 1/1, code-path 2/1, reference-target 0/5,
stale-reference 0/5 — the report's figures. A break counts as detected when the record gives the
invariant more `fail` lines than the baseline (the one `fail` each from `Fixtures` stands in both).

| Invariant | Break | Command | Exit | Detected | Output |
|---|---|---|---|---|---|
| `guidelines-form/1` | crafted file, no change to the script: `guidelines/testing.md` of a temporary product opens a `~~~~` fence in `## When to read` and writes `~~~` after it, so by CommonMark `## Rules`, `## Examples` and `## Where in code` stand in fenced code (a check closing on a shorter fence would pass it) | `python -B <worktree>/product-guidelines/form_check.py <product> --record <scratch>/form-break.jsonl` | 1 | **yes** — three `the section … is missing` errors, three `check_sections` `fail` lines | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-guidelines-form.txt` |
| `guidelines-check-form/1` | `check_parts`: the guard on a part of *Applies to* the map does not hold → `if False:` (FC:576) | `python -B gate/run_tests.py product-guidelines --record …` | 1 | **yes** — fail 1 → 2; new failures: F4 `Form.test_a_part_the_map_does_not_hold_is_reported` and three ordinary tests | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-guidelines-check-form.txt` |
| `guidelines-check-carrier/1` | `read_templates`: the reading "its *Invariant* names at least one invariant" no longer matches (FC:304), as a reworded template would make it | same | 1 | **yes** — fail 1 → 2; new failure: F4 `Carrier.test_a_styleguide_rule_naming_no_invariant_is_reported` | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-guidelines-check-carrier.txt` |
| `guidelines-check-colour-pair/1` | `check_roles`: *Text on it* accepted when it names any role of the table, not only one of kind `text` (FC:542) | same | 1 | **yes** — fail 1 → 2; new failure: F4 `ColourPair.test_a_background_without_a_text_role_is_reported` | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-guidelines-check-colour-pair.txt` |
| `guidelines-check-code-path/1` | `refused`: the guard on an absolute path removed (FC:603-604) | same | 1 | **no** — fail 1 → 1, no new failing test; the same broken script then passes a product naming `/tests/fixtures.py` (exit 0) | `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-break-guidelines-check-code-path.txt` |

Every mutated `form_check.py` was restored and compared byte for byte (`True` in each file); the
worktree showed no change afterwards. The undetected break is Important 2. Evidence of the probes
behind Important 1 and Minor 3: `.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-review-probes.txt`.

## Weakest-point check (WAY-164) and the sharpness inputs

- **The check itself is real and sharp for what it chose**: a required rule added to a copy of the
  styleguide template made the valid fixture fail with exactly one error; the evidence file
  `slice-2-weakest-point.txt` is named. It shows the form is read from the templates, not from
  lists that match today's templates.
- **It was not the weakest point.** Two requirements the task holds fail or are unguarded where the
  check did not look: 5a's "no file held to the wrong template in silence" fails outright
  (Important 1), and the absolute-path guard of `guidelines-check-code-path/1` can be removed with
  the gate green (Important 2). Both are found by reading each sentence against the inputs the
  F4 tests do not use, which is what a weakest-point check of a check is for.
- **Sharpness inputs — confirmed with one correction.** Parts touched: `product-guidelines` only,
  two new files (confirmed by the diff's file list). Trust-boundary file:
  `product-guidelines/form_check.py`, declared at `foundations/part_map.md:279` (confirmed).
  Nothing irreversible (confirmed). **Correction:** the boundary reaches into borrowed code — the
  part-map guard's `parse_map` (`elements/part-map/format_guard.py:285-317`) parses the product's
  untrusted `foundations/part_map.md`, and that guard loads a second copy of `guard_shared.py`
  (the source of Minor 3). A change to `elements/part-map/format_guard.py` therefore changes this
  trust boundary; the sharpness inputs should name it, not only "loads, without changing".

## Concern 4 of the brief: settings read from template prose

Judged against the two readings that would switch off silently (FC:304-306): whether a
styleguide's every rule names an invariant, and whether its files are named per part.

- **At run time they are silent**: a reworded template makes `requires_invariant` or `per_part`
  False with no error, unlike the *Kind* list, which raises (FC:313-317).
- **At the gate they are not silent**: the F4 tests run against the real templates, and the
  template lies in the part `product-guidelines`, whose change runs `gate/run_tests.py
  product-guidelines`. The carrier break above is exactly a reworded `requires_invariant` reading,
  and the F4 carrier test caught it (fail 1 → 2). Focused check of the other reading: the per-part pattern of FC:306 changed so it no longer matches, then the one F4 test of names run (`python -B -m unittest test_form_check_invariants.Form.test_a_file_whose_name_and_discipline_disagree_is_reported`, cwd `product-guidelines`) → exit 1, `FAILED (failures=1)` (`.runs/task-cycles/product-guidelines-styleguide/reports/slice-2-review-per-part-reading.txt`). Both readings are therefore guarded by the gate, not only by the script.
- **Verdict:** acceptable for this task; Minor at most, not raised as an issue. The readings
  cannot raise when absent, because a discipline template that does not require an invariant is
  legitimate. The sounder form, for the whole-branch review: a marker the form block itself carries
  (a field line or a fixed sentence the script checks for in the styleguide template, failing at
  start when a template with a table of roles lacks it), so a rewording breaks at start rather than
  only in the tests.

## Assessment

**Spec compliance:** ❌ — one item of §5.3 missed (5a, Important 1); the rest present.

**Task quality:** Needs fixes.

The script is careful where it matters most — the trust boundary holds against every crafted
input I could build, and the departure on paths makes it stricter, not weaker. Two things stop
trusting the task as it stands: a styleguide can escape its whole template by writing its
discipline as `styleguide-<part>` (a spec-named error that passes with exit 0), and the guard
against absolute paths is unprotected by any test, so the gate would stay green if it went. Both
are small, test-first fixes in the two files of the task. The Minor items can ride with them.
Counts: Critical 0, Important 2, Minor 5.
