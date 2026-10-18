# Check author report (F4) — product-guidelines-styleguide

- **Status:** done; the tests fail as expected, because `product-guidelines/form_check.py` does not exist.
- **Commit:** `8ea4679` on `task/product-guidelines-styleguide` (parent `eb9ff1e`),
  `test(product-guidelines): check what the form check of guidelines reports, before it is written`.
- **Changed files:** `product-guidelines/test_form_check_invariants.py`, +721 / −0. No other file is changed.

## Inputs read

- `foundations/invariants.md:2153-2212` (the six entries); `foundations/decisions.md`: WAY-168, WAY-169,
  WAY-170, WAY-171, WAY-176, WAY-188, WAY-189.
- `spec.md` §3.1, §3.2, §4.1, §4.2, §5.1, §5.3 only.
- `elements/invariants/template.md`, `gate/run_tests.py`, `gate/test_wording_reaches_dependants.py`.
- To write a valid decision log, invariants file and part map as fixtures, I also read the
  entry forms of the foundation, not the covered script: `elements/decisions/template.md:1-170`,
  and the fixture helpers at the top of `elements/decisions/test_format_guard.py` and
  `elements/invariants/test_format_guard.py`.
- `relation-model/fingerprint.py`, run once by hand on each fixture sentence.

## How the tests work

Each test builds a product in a temporary git repository. The base commit on `main` holds
`foundations/decisions.md` (prefix `ABC`), `foundations/invariants.md`, `foundations/part_map.md`
(one part, `web`), `src/tokens.css`, `src/components/button.tsx` and `tests/fixtures.py`. A second
commit on `main` adds the `guidelines/<name>.md` files under test. When a test passes `onto`, a branch
`onto` leaves the base commit and changes only foundation files there. The test then runs
`python -B <the-way>/product-guidelines/form_check.py [options] --record <tmp>/guidelines.jsonl` with
the product root as the working directory, and asserts:

- **Errors:** exit 1; a line `guidelines/<name>.md:<line>: error: …` (at the given line where one is
  given) whose message holds the given fragments; and in the record, `fail` for `guidelines-form/1`
  (form checks, run with no option) or for `guidelines-reference-current/1` (reference checks, run
  with `--merge-onto`).
- **Controls:** exit 0; no `: error:` in the output; no `fail` for either invariant of guidelines;
  and `pass` for the one the run records (`guidelines-form/1` with no option,
  `guidelines-reference-current/1` with `--merge-onto`).

Every break changes one line or one piece of the valid fixture. `with_line` and `replaced` first
check that the fixture holds the line or text they expect, so a fixture that moves fails loudly.

Against a stand-in script that exits 0 and writes nothing, all 25 tests failed, controls included,
and none failed through its own fixture or through git (152 subtest failures, all of them exit-code
or record assertions).

## Literal fixtures and fingerprints

| Entry | Binding sentence (literal in the test) | Fingerprint |
|---|---|---|
| ABC-01/1 | The background role primary marks the main action of a screen, and the text role primary-text stands on it. | `daa9cf8d` |
| ABC-01/2 (only on `onto`, new wording) | The background role primary marks the one main action of a screen, and the text role primary-text stands on it. | `cca35182` |
| ABC-02/1 | The role muted marks what matters less than what is around it. | `9bb0959d` |
| ABC-03/1 (the departing decision) | The product's styleguide drops the rules on design tokens, … until the product draws screens of its own. | `8503cafa` |
| ABC-04/1, then ABC-04/2 repeal | The product draws its text in one font of its own. | `7ba1b4bb` |
| ABC-05/1 | Each test of the product sets up its data through the product's fixtures. | `016b5b2a` |
| role-meaning/1 | No screen of the web interface uses a colour role in a meaning other than the one its decision gives. | `a2557545` |
| role-meaning/2 (only on `onto`) | … in any meaning other than … | `cbbaa72e` |
| background-pair/1 | Every background role of the styleguide's table names the text role that stands on it. | `169d4c67` |
| old-pair | in the invariants file's `## Withdrawn identifiers` table | — |

Each fingerprint was computed once with `relation-model/fingerprint.py`, from a scratch script
that held exactly these strings, and written into the test as a literal. The stale fingerprints
differ from the current ones only in their last character: `daa9cf80`, `a2557540`, `8503cafb`.

The fixture `STYLEGUIDE` (`guidelines/styleguide-web.md`) holds everything §4.1 lists, in order:

- the title and the header lines;
- `## When to read`;
- `## Roles`: `primary` (background, text `primary-text`), `primary-text` (text), `muted` (other);
- `## Rules`: "Each role in its meaning" (naming ABC-01 and ABC-02, invariant role-meaning) and
  "Every background with its text" (ABC-01, background-pair), then the seven other required rules,
  each dropped with `none — ABC-03@8503cafa`;
- `## Examples`: Mockups, and Plan of a user-interface change;
- `## Where in code`: `src/tokens.css` and `src/components`.

The fixture `TESTING` (`guidelines/testing.md`) is guidelines of a discipline that has no template:
one rule, with *Invariant* `none`.

## Tests per invariant

- **guidelines-check-form/1** (`Form`, plus the fixture test)
  - Header lines: *Applies to* missing, *Discipline* missing, the two swapped.
  - Sections: no `## When to read`, no `## Roles` (styleguide), no `## Examples` (no template),
    no `## Where in code`; `## Roles` before `## When to read`; `## Where in code` before `## Examples`.
  - Required rules: Visible focus missing, Every background with its text missing, Contrast before Visible focus.
  - Rule fields: no *Good* (styleguide), no *Bad* and no *Invariant* (no template), *Bad* before *Good*.
  - Drops: a reason instead of a decision, `none` alone, `none — ABC-03` with no fingerprint,
    `n/a — …`, text beside the departure, and a dropped section with a reason. Control: a section
    dropped with `none — ABC-03@8503cafa` passes.
  - Parts the map does not hold: `Applies to: web · mobile` (line 4), `Applies to: mobile`,
    the files `styleguide-mobile.md` and `testing-mobile.md`.
  - Name and *Discipline* disagree: `styleguide-web.md`/testing, `web.md`/testing,
    `look-web.md`/styleguide, `styleguide.md`/styleguide, `testing-web.md`/styleguide. Control:
    `testing.md` and `testing-web.md` holding testing, and `styleguide-web.md` holding the styleguide, pass.
- **guidelines-check-carrier/1** (`Carrier`)
  - A rule naming no decision: *Decision* `none` in the styleguide and in the testing file;
    *Decision* naming an invariant only.
  - A styleguide rule naming no invariant: *Invariant* `none`; *Invariant* naming a decision
    only; a further rule of the product with `none`. Control: `none` outside a styleguide passes.
  - A roles decision (ABC-02) that "Each role in its meaning" does not name: reported, and the
    message names ABC-02. Control: with that rule dropped, it passes.
- **guidelines-check-colour-pair/1** (`ColourPair`): the *Text on it* of `primary` (line 14) is
  empty, `—`, `muted` (kind other), `primary` (a background), or `ink` (not in the table); each is
  reported at line 14.
- **guidelines-check-reference-target/1** (`ReferenceTarget`, run with `--merge-onto none`)
  - Seven places: a *Decision* field (31), an *Invariant* field (32), a `## Roles` row (16), a
    rule's prose (36), inline code in prose (36), an example (70), a `none —` departure (44).
  - Absent or ended targets, in each place: `ABC-09@0123abcd`, the repealed `ABC-04@7ba1b4bb`,
    `missing-pair@0123abcd`, the withdrawn `old-pair@0123abcd`. Each is reported at its line, and
    the message holds the reference.
  - A part after `@` that is not eight lower-case hex, in each place: `ABC-01@daa9`,
    `ABC-01@DAA9CF8D`, `ABC-01@daa9cf8d0`, `ABC-01@zz`, `role-meaning@v2`, `old-pair@x`.
  - Controls that pass: `react@18` (in backticks and bare), `tailwindcss@4`, `lucide-react@0`,
    and the bare mentions `ABC-01`, `ABC-01/1`, `role-meaning`, `old-pair`, `ABC-09`. A fenced
    block, in both ``` and ~~~ fences, holding absent, withdrawn, malformed and stale references
    and `left-pad@0123abcd`, also passes.
- **guidelines-check-stale-reference/1** (`StaleReference`, plus the fenced test)
  - On the same commit (`--merge-onto none`), a stale fingerprint in *Decision* (22),
    *Invariant* (23), a `## Roles` row (14), prose (27), an example (70) and a departure (44).
    Each is reported at its line, and the message names the entry and its current fingerprint.
  - After a merge (`--merge-onto onto`), where only `onto` rewords ABC-01 or role-meaning: line 22
    names ABC-01 and `cca35182`; line 23 names role-meaning and `cbbaa72e`. Control: the same
    branch with `--merge-onto none` passes.
- **guidelines-check-code-path/1** (`CodePath`)
  - Line 78 replaced by each of: `../outside.md`, `src/../src/tokens.css`, `/etc/passwd`, `C:\x`,
    `C:/x`, `\\host\share\x`, `//host/share/x`, `:(glob)**`, `http://host/x`, `src/missing.css`,
    and `src/draft.css` (present but not tracked). Each is reported at line 78; for paths without
    a backslash, the message must also hold the path.
  - Control: a tracked file and a tracked directory pass.

The fixture test cites all six invariants: a check that reports errors on the valid fixtures gives
none of them a pass.

## Run

```text
python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl
```

- **Exit code:** 1.
- **Output:** "Ran 25 tests … FAILED (failures=152)". Every subprocess exits 2 with "can't open
  file '…/product-guidelines/form_check.py': [Errno 2] No such file or directory".
- **Full output:** `.runs/task-cycles/product-guidelines-styleguide/reports/check-author-run.txt`.
  It holds the unittest report and the record.
- **Record:** `fail` only — carrier 6, code-path 3, colour-pair 2, form 10, reference-target 5,
  stale-reference 5. No test is skipped.

## Questions for the root

1. **Where the templates come from.** The tests assume the script reads the-way's templates from
   its own checkout (`<the-way>/product-guidelines/…`); the temporary product pins no
   `.the-way`. WAY-170 says "at the commit of the-way the repository uses". If the script requires
   a pinned submodule in the product, every test exits 2. Is reading them from the script's own
   checkout the intended behaviour?
2. **Line and wording of messages.**
   - Located findings are asserted at the line of the token: references, paths, `## Roles` rows,
     *Applies to*.
   - Missing or misplaced items are accepted at any line, but the message must name the missing
     item: a section heading, a field name, a required rule's heading, or the unknown part. For a
     misplaced item, either of the two swapped names.
   - Reference messages must hold the reference; stale ones, the entry and its current fingerprint
     (§5.3 item 7).

   Do the executors take these as bound?
3. **Withdrawn identifiers.** The sentence of guidelines-check-reference-target says "an
   identifier of the invariants file"; §3.2 adds "as an entry or a withdrawn identifier". The tests
   read `old-pair@x` (withdrawn) as a reference with a malformed fingerprint, and `old-pair@0123abcd`
   as one to a withdrawn invariant. Does the sentence mean this?
4. **Tilde fences.** The tests take a `~~~` fence (CommonMark) as fenced code, like ```. Is that
   intended?
5. **No option and references.** Reference tests always pass `--merge-onto` (`none` or `onto`);
   nothing asserts what a run with no option prints or exits for a reference error. §5.1 says
   every check prints in every run, but whether those errors set exit 1 is not asserted.
6. **Name and discipline.** `guidelines/testing-web.md` holding `Discipline: styleguide` is
   asserted as an error ("a styleguide is always `styleguide-<part>.md`"). A dropped required
   section (`## When to read` → `none — ABC-03@…`) is asserted to pass, and a `none —` line with
   any further text in the body is asserted as an error ("holds only").

## Unresolved concerns

- The run takes about 37 s: 152 subprocess runs, each on its own temporary repository.
- WAY-03: the file is now read-only for the executors of the covered code.

## Addition: the reviewer's code-path break

- **Trigger:** the reviewer's deliberate break of guidelines-check-code-path/1 removed the script's
  refusal of a path that starts with `/`
  (`reports/slice-2-break-guidelines-check-code-path.txt`). No test caught it. Every absolute
  path in my fixtures was still reported, but only because it also named nothing git tracks.
- **Commit:** `8d97ab9`, `test(product-guidelines): report an out-of-repository path of
  guidelines whose remainder git tracks`. It changes
  `product-guidelines/test_form_check_invariants.py`, +33 / −1. No existing assertion is removed.
- **New test:** `CodePath.test_a_path_out_of_the_repository_is_reported_though_its_remainder_is_tracked`,
  citing `guidelines-check-code-path/1`.
  - First, control subtests check that `src/tokens.css`, `tests/fixtures.py` and
    `src/components` pass as paths.
  - Then each path below must be reported at line 78. For paths without a backslash, and other
    than the product root, the message must also hold the path. Each would name a tracked file
    or directory once its prefix or its `..` is stripped or resolved:
    - **Absolute:** `/src/tokens.css`, `/tests/fixtures.py`, `/src/components`, and the
      product's own absolute root + `/src/tokens.css`.
    - **Drive:** `C:/src/tokens.css`, `C:\src\tokens.css`, `C:src/tokens.css`,
      `c:/tests/fixtures.py`, `\src\tokens.css`.
    - **UNC and device:** `\host\share\src\tokens.css`, `//host/share/src/tokens.css`,
      `\?\C:\src\tokens.css`, `//?/C:/src/tokens.css`.
    - **`..` segments:** `../product/src/tokens.css` (the temporary repository stands in a folder
      named `product`), `src/components/../tokens.css`, `./src/../src/tokens.css`,
      `src\..\src\tokens.css`.
- **Helper change:** `check()` now replaces the marker `PRODUCT_ROOT` in the text of guidelines
  with the product's root, written with forward slashes.
- **Break re-checked:** I applied the reviewer's break byte for byte (one occurrence) in a scratch
  `git worktree` of `2e5d038`, without reading the script, and ran `CodePath`. The new test fails
  in the subtests `/src/tokens.css`, `/tests/fixtures.py` and `/src/components`, and the two older
  tests still pass. The worktree is removed.
- **Run at head:** `python -B gate/run_tests.py product-guidelines --record
  .runs/product-guidelines-tests.jsonl`, at `2e5d038` with the change in place (identical to the
  committed `8d97ab9`).
  - **Exit code:** 1. "Ran 46 tests … FAILED (failures=93)".
  - **Full output:** `reports/check-author-run-2.txt`.
  - **All three `CodePath` tests pass.**
  - **Record verdicts:**
    - code-path: pass 3, fail 1;
    - form: pass 9, fail 1;
    - carrier: pass 5, fail 1;
    - colour-pair: pass 1, fail 1;
    - reference-target: fail 5;
    - stale-reference: fail 5.
  - **Why the single fails outside the reference invariants:** each comes from
    `Fixtures.test_the_valid_fixtures_pass`, the test that cites all six invariants. With
    `--merge-onto none`, the record holds no `pass` for `guidelines-reference-current/1` yet.
    This and the reference tests stay red until slice 3.

## Addition: file names after WAY-167 (ruling C32)

- **What I read:** WAY-167 (`foundations/decisions.md:5439-5486`, as of `c355004`), and the
  sentences at `foundations/invariants.md:2133-2212`, including `guidelines-form/1` as reworded in
  `19d28f8`. I did not read `form_check.py` or its ordinary tests.
- **What WAY-167 says:**
  - The styleguide alone has a file per part: `guidelines/styleguide-<part>.md`, one per user
    interface.
  - Every other discipline has a single file, `guidelines/<discipline>.md`.
  - So a non-styleguide file under a part's name has a name that disagrees with its
    *Discipline* (guidelines-check-form/1, "every file whose name and *Discipline* disagree").
- **Commit:** `4a4f08e`. It changes `product-guidelines/test_form_check_invariants.py`, +12 / −6.
  - **`Form.test_a_file_whose_name_and_discipline_disagree_is_reported`:**
    - New error cases: `guidelines/testing-web.md` and `guidelines/testing-mobile.md` holding
      `Discipline: testing`, and `guidelines/testing.md` holding `Discipline: styleguide`.
    - The earlier five cases stay.
    - Each subtest is now labelled with its path and its discipline.
  - **`Form.test_a_file_whose_name_follows_its_discipline_passes`:** `guidelines/testing-web.md`
    is no longer a valid case. The valid cases are `guidelines/testing.md` (testing) and
    `guidelines/styleguide-web.md` (styleguide).
  - **`Form.test_a_part_the_map_does_not_hold_is_reported`:** the part-in-the-name case keeps only
    `guidelines/styleguide-mobile.md`, still required to name `mobile`.
    - `guidelines/testing-mobile.md` moved to the name test: under WAY-167 its name holds no
      part, so its error is the name's.
    - The *Applies to* cases are unchanged.
- **Run:** `python -B gate/run_tests.py product-guidelines --record
  .runs/product-guidelines-tests.jsonl`, at `c355004` with the change in place (identical to the
  committed `4a4f08e`).
  - **Exit code:** 1. "Ran 60 tests … FAILED (failures=1)".
  - **Full output:** `reports/check-author-run-3.txt`.
  - **Failure, RED as expected:** the subtest `(path='guidelines/testing-web.md',
    discipline='testing')`. The current script exits 0 with no error on it.
  - **`guidelines/testing-mobile.md`** is already reported by the current script, through its
    name or its unknown part; the test asserts only an error in that file.
  - **Record verdicts:**
    - form: pass 9, fail 1 (that subtest);
    - all other invariants pass: carrier 6, code-path 4, colour-pair 2, reference-target 5,
      stale-reference 5.
