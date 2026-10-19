# Slice 3 review: the form check's index of kinds and the files of a kind

Reviewer of `334ef34..0607656` (`product-guidelines/form_check.py` +216/−3,
`product-guidelines/test_form_check.py` +334). Read whole: the brief, constraints, report and the
review package; no hunk was cut off. Outside the diff, one focused read per named risk (below).

### Spec Compliance

- ✅ Spec compliant: spec §5.2 items 3 and 4, C31's two clauses, C32 (*File* in backticks) and C13
  (no completeness) are all met. The evidence:
  - Item 3 / `guidelines-check-kind-index/1`:
    - `check_kind_index` (form_check.py:1188-1248) reports at line 0 of each kind file one of three
      things: git tracks no `guidelines/coding.md`, the general file is unread, or no row names
      the file (:1232-1248).
    - At the row's line it reports an empty *When to read* (:1212), a bad or refused *File*
      (`row_path`, :1097-1112), a *File* that is no `coding-<kind>.md` (:1219), a *Kind* off its
      file's kind (:1224) and a *File* naming no tracked kind file (:1229).
  - Item 4 / `guidelines-check-exemplar/1`:
    - `check_exemplar` (:1115-1161) reports a *Status* off the template's list, each bad, refused
      or untracked *File*, a *Decision* other than `—` off the exemplar row, a second exemplar at
      its line naming the first, and no exemplar (at the heading, or line 0).
    - `check_designation` (:1164-1185) reports an exemplar row that names no decision, names one
      not in force, or names one whose binding sentences lack the *File* or the kind in backticks
      after whitespace is collapsed (`Foundation.names_in_backticks`, :565-578).
    - `Foundation.bindings` is filled from the latest versions, with `None` for a repeal (:684-685).
    - The fingerprint is left to `check_references`, as for every reference.
  - Every new finding is `report.error(..., (FORM,))`, so an error of `guidelines-form/1`. The
    docstring is extended (:52-64). `PROGRAM`, the options and the exit codes are untouched.
  - No new regular expression in `form_check.py`; stdlib only (WAY-38).
- ✅ Carried S2 ⚠️, the promise at `product-guidelines/coding/template.md:189-195`:
  - Each listed item now exists in the form check:
    - "the table of `## Kinds of code` and its agreement with the files of a kind" →
      `check_kind_index`;
    - "the closed list of *Status*, the one exemplar and its decision naming its path and kind" →
      `check_exemplar` and `check_designation`;
    - "each *File* naming something git tracks" → both tables (:1137-1144, :1229).
  - Only "the test cases of each rule with their paths" is still missing. It is S4's: the 7
    `ExampleFiles` tests are RED by name.
- ⚠️ Cannot verify from this diff: the template's promise is complete only once S4 lands the test
  cases. The controller should re-check `coding/template.md:189-195` at S4's review.

### Executor's concerns, judged

1. **"git lists" read as "git tracks". Accepted.** Under this reading an untracked kind file escapes
   the index check until it is added, and the executor reports that honestly as its weakest point.
   - F4 forces this reading:
     - `test_form_check_invariants.py:1153-1163` asks for an error on a row naming an untracked
       file;
     - `:1185-1201`, case "the general file untracked", asks for an error when `coding.md` exists
       untracked.
   - Reading "lists" as "tracked or not ignored" for kind files alone would give one phrase of
     one sentence two meanings.
   - The cost is real but small. The gate checks commits, and on a commit the untracked case
     cannot arise. Locally, an untracked kind file is still read and form-checked (exemplar
     included) by the per-file loop; only the index check skips it.
   - The wording problem lies in the foundation, not in the code (Minor 1).
2. **The stale fingerprint is reported under `guidelines-reference-current/1`. Accepted.**
   - Spec §5.2 item 4 says "the fingerprint of that reference is checked as every reference is
     (WAY-169)".
   - The sentence of `guidelines-check-exemplar/1` (invariants.md:2223-2232) names no fingerprint.
   - Routing the error through `check_references` is what the spec asks.
   - `FilesOfAKind.test_a_stale_fingerprint_of_the_exemplar_s_decision_is_an_error`
     (test_form_check.py:914) shows that the error is at the row's line and that `REFERENCES`
     fails.
3. **The 200 KiB *File* is reported as untracked, not refused. Accepted.**
   - Spec §5.3 asks that each crafted input is handled "without git seeing a refused path, without
     a socket and within a time bound".
   - No product path ever reaches git: `tracked()` (form_check.py:1417-1438) calls
     `ls-files -z` with fixed arguments, and the cell is only compared with the set.
   - `shown()` (:208-213) cuts the printed value.
   - The test covers this in-process with git's arguments captured (test_form_check.py:807-823,
     :947-961).
   - Adding a length rule to the shared `refused()` would change `## Where in code`, which this
     slice does not own.

### Weakest point and sharpness (WAY-164, WAY-48)

- **Weakest point.** The executor's reading is confirmed by the code: :1204 builds the kind files
  only from `tracked()`. The executor's evidence, `slice-3-weakest.txt`, matches it: the untracked
  `coding-job.md` gets no index error, and the committed one does.
- **Sharpness inputs.** These were checked against the diff stat:
  - the only part touched is `product-guidelines`;
  - the only trust-boundary file touched is `product-guidelines/form_check.py`;
  - `installation/install.py` is untouched;
  - nothing irreversible was done.
- **Crafted inputs, checked against the tests** (test_form_check.py:687-698, :701-728, :807-823,
  :947-961, :963-986):
  - The paths: absolute, UNC (both spellings), `..`, `\`, a drive with and without a slash, BEL,
    a zero-width space (`isprintable()` is false, so `refused()` catches it), `:(literal)`, `:!`,
    and 200 KiB.
  - How each is run: in-process, with `subprocess.run` recorded, the three socket entry points
    refused, the row's line asserted reported, no path asserted in any git argument, and git
    asserted to be asked `ls-files`. That last assertion makes the capture non-vacuous.
  - Also covered: case and Cyrillic look-alikes (:753-770), a row naming a tracked non-kind file
    (:772-786), *File* not one code span (:788-801, :935-945), two exemplars or none (:836-857),
    the C32 missing section (:859-872), the substring traps (:874-890), the `XYZ-06` prefix
    (:892-899), a repeal (:901-911), and 1 MiB of bars or backticks within 30 s (:963-986).
- **Bound on matching.**
  - `names_in_backticks` does one `str.split` on backticks per decision, cached, then a set
    lookup.
  - `code_path` and `bare` use `count` and slicing; `refused()` is linear.
  - `tracked()` is asked of git once and cached.
  - Nothing new is quadratic in the rows.

### Deliberate breaks (from the sentences of `foundations/invariants.md:2213-2232`)

The scratch worktree was `<scratchpad>/review-0607656` at `0607656`. It was removed afterwards and
the checkout is untouched (`git worktree list` shows only `/home/user/the-way`).

- **`guidelines-check-kind-index/1`.** Sentence made false: "reports … every file
  `guidelines/coding-<kind>.md` git lists that no row … names". Break: `elif path not in named:` →
  `elif False:` (form_check.py:1239).
  - Command: `python3 -B gate/run_tests.py product-guidelines --record …`. Exit 1.
  - `KindIndex.test_a_kind_file_no_row_names_is_reported` gives `fail` for
    `guidelines-check-kind-index/1` in the record.
  - The ordinary tests `test_a_kind_file_no_row_names_is_an_error` and the case/look-alike test
    also fail.
  - Detected. Output: `slice-3-break-kind-index.txt`.
- **`guidelines-check-exemplar/1`.** Sentence made false: "… names one whose binding sentences,
  their whitespace collapsed, lack its *File* in backticks or the file's `<kind>` in backticks".
  Break: the search made bare, `return word in self.quoted[key]` → `return word in text`
  (form_check.py:578).
  - Same command. Exit 1.
  - `Exemplar.test_an_exemplar_row_whose_decision_does_not_designate_it_is_reported` gives `fail`
    for `guidelines-check-exemplar/1`, in the subtests "the path with the kind bare" and "the path
    bare with the kind".
  - The ordinary test `FilesOfAKind.test_a_decision_naming_the_path_only_outside_backticks_is_an_error`
    also fails.
  - Detected. Output: `slice-3-break-exemplar.txt`.
- In both runs the only other failures are the 37 `ExampleFiles` subtests, which were RED before
  the break (S4).

### Strengths

- The binding search is correct and stays linear:
  - Asking whether a backtick-free word equals some piece between consecutive backticks of the
    collapsed text gives exactly the answer that substring search for `` `word` `` gives.
  - Caching those pieces per decision makes a file of many exemplar rows cost no repeated search
    of the log (form_check.py:565-578).
- No product path is ever opened or given to git. Both tables reuse the one cached `ls-files` list
  and the shared `refused()`. That keeps the trust boundary as small as it was.
- Findings are placed with care:
  - each row's own errors are at its line;
  - the second exemplar names the first;
  - a kind file's index errors are reported in that file's own report, with the git failure in the
    run's report;
  - malformed rows are already excluded by `check_tables`, so a broken row yields one error, not
    several.
- The crafted-input harness (`Watched`) records git's arguments, refuses sockets and times the
  in-process run. It asserts that git was in fact called, so the "unseen" assertion cannot pass
  vacuously.
- The executor's evidence is clean:
  - the product-guidelines run fails only the 7 S4 `ExampleFiles` tests (37 subtests), with no
    warnings or noise;
  - decisions 169, relation-model 19 and gate 98 all OK;
  - the RED ordinary run is on file with the kind-file-missing case among its failures.

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

None.

#### Minor (Nice to Have)

1. **`foundations/invariants.md:2215` (`guidelines-check-kind-index/1`) says "git lists" where its
   tests and code mean "git tracks". Outside this slice's scope: it is foundation wording.**
   - In `form_check.py`, "git lists" already means "tracked or not ignored" (:66, :1338). F4 and
     this slice read the invariant as "tracks" (:1192-1195 says so explicitly).
   - `guidelines-check-exemplar/1` and `guidelines-form/1` say "git tracks".
   - The ambiguity is what produces the untracked-kind-file gap.
   - Suggest the request name it, and that the invariant's next version say "git tracks", through
     `record-invariant`.
2. **form_check.py:572 — `names_in_backticks` collapses the decision's binding text on every call,
   before the cache lookup.**
   - The docstring (:566-570) says each decision's text is handled once.
   - The cost per exemplar row is one binding's length, bounded by the 1 MiB file, so this is no
     break of the time bound. It is an overstated docstring and avoidable work.
   - Fix: cache the collapsed text per key, and its pieces, inside the `if key not in self.quoted`
     branch.
3. **test_form_check.py — coverage gaps, both Minor.**
   - Choice 3 says a *File* of `## Files of this kind` must name a tracked file, not a directory
     (:1137-1144 uses `files` only). No test pins this: a tracked directory such as `src/api` in
     a `copy` row.
   - The 1 MiB-line test covers only the files table (:963-986). The index table has none,
     although its code is linear.

### Assessment

**Task quality:** Approved

**Reasoning:** Items 3 and 4 of spec §5.2 are implemented as written. Nothing crafted reaches git,
there are no sockets, and the cost is linear. Both deliberate breaks fail tests citing their
invariants. The executor's three concerns hold on their merits. What remains is foundation wording
outside this slice's scope and two minor polish points.
