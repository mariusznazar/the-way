PASS 3043e760b93e16586d564a611837cad008478c19

# Review of the return step's commits — script-invariants-by-test

Range: `540aed04..3043e760`, one commit, `3043e760` "Return step: name the tests of the script rules and of the element
directories in the part map", changing `foundations/part_map.md` only (+5 / -3). `git rev-parse HEAD` in the worktree is
`3043e760b93e16586d564a611837cad008478c19`, the head given.

Counts: blocking 0, Minor 2, out of scope 0.

## Findings

### Critical

none

### Important

none

### Minor

**m1 — `foundations/part_map.md:166-168` — the colon makes the three tests the whole list of "the rules every script of the-way keeps" (within the task).**
The return step adds to the `agent-instructions` entry: "and for the tests of the rules every script of the-way keeps: the
language it is written in, the version of Python it runs on and the modules it imports". The colon reads as a definition, so
the rules every script keeps are these three. The same part holds the tests of two more rules of the-way's own scripts:
`agent-instructions/test_linter_invariant.py` (invariant `ruff-blocking-rules`, which runs Ruff over every part with Python
code) and `agent-instructions/test_size_invariant.py` (invariant `function-and-file-size`). The new sentence leaves them
unnamed, and the sentence before this change did not name them either.
What the new part says is true: the part answers for the three tests that `agent-instructions/test_script_invariants.py`
holds (`python-version-declared`, `script-language`, `script-imports`), and that is what the review of the fix asked for
(N1 of `review-fix-report.md`). So the effect is small. A reader who asks which part answers for the linter's or the size
test does not find it named here, and the closed list suggests the part does not hold them.
Possible fixes, either one: "the tests of three rules every script of the-way keeps: …"; or a sentence naming the tests of
the rules of the-way's own code with these three as examples. Also, the entry is now one sentence that strings together
"and for … and for … and for", against "briefly, in as few sentences as that needs" in `elements/part-map/template.md`.
That is form, so it is Minor (WAY-364).
Evidence: `git ls-files agent-instructions` lists `test_linter_invariant.py` and `test_size_invariant.py` beside
`test_script_invariants.py`. Their docstrings name the invariants they test.

**m2 — `foundations/part_map.md:166-168` with WAY-44 — the test of a `repository` invariant now stands, by the map, in `agent-instructions`, and the tension with "Tests belong to the part they test" is neither resolved nor raised (within the task).**
The *Part* of `python-version-declared` is `repository` (`foundations/invariants.md`, entry `python-version-declared`).
WAY-44 says "Tests belong to the part they test". The return step's sentence now gives the test of that invariant to
`agent-instructions` as a test of "the version of Python [every script] runs on". That reading follows WAY-89 ("The scripts
of the-way run on Python 3.14, which the repository declares in `.python-version`"), and WAY-89's *Scope* names
`agent-instructions`, so the framing can be defended.
`repository` cannot hold a test either way. WAY-09 gives it only the configuration files at the root, and it has no
directory. So the strict reading of WAY-44 leaves this test no place. The review of the whole change already flagged this
as unclear ("Searches not found or unclear" of `review-whole-report.md`). The author's return report says WAY-44 and the
*Scope* of other decisions "name `agent-instructions` and `elements-common`, so the two new test files stand inside them".
But WAY-44's *Scope* is `part-map, agent-instructions, task-cycle`, and its sentence speaks of the part tested, not of a
decision's *Scope*. So the report does not settle the point.
There is a precedent: `ruff-blocking-rules`, whose *Part* includes `repository`, is tested in `agent-instructions` too.
Consequence today: none for any verdict or any selection of decisions. A change to the test selects WAY-89 through
`agent-instructions` anyway, and the invariant's citing test links it. It is Minor for that reason. WAY-33 still asks that
such a finding becomes a link, a change or a question to a human. The cheapest form is one clause in the request's
questions table or in WAY-44 itself (for example, "a test of an invariant of `repository` stands in the part whose sentence
names it").

## Checked and found sound

- The `agent-instructions` sentence against `agent-instructions/test_script_invariants.py`:
  - The file holds exactly the three tests the sentence names: `PythonVersionDeclared`, `ScriptLanguage` and
    `ScriptImports`, with the unit tests of their functions.
  - "the version of Python it runs on" matches WAY-89 and the invariant's sentence ("The repository declares Python 3.14
    in `.python-version`").
  - The import of `imports` from `elements/part-map/test_cross_part_imports.py` is allowed: the *Depends on* of
    `agent-instructions` names `part-map`.
- The `elements-common` sentence against `elements/common/test_element_directory_contents.py`:
  - The test checks every directory under `elements/` but `common` for `template.md`, for `examples.md` or a pointer in
    the template's `## Examples` section, and for `skill/SKILL.md`. That is what "the test that every directory of an
    element holds its template, its examples or a pointer to them, and its skill" says.
  - The sentence leaves out the condition "Where {merge-onto} exists". I do not count that as a finding: the sentence
    names the test by what it checks, at the grain the map uses elsewhere. The `part-map` entry likewise names "the test
    that holds the imports … to the dependencies it allows" without the exceptions of `cross-part-imports`. A reader would
    not act differently.
  - The test imports only `foundation_source` of its own part.
- The search of the foundation (WAY-33) for the old sentences and for the place the moved file left:
  - `git grep` finds `test_script_invariants` only in the file itself, and `test_element_directory_contents` nowhere
    else. No `elements/part-map/test_script_invariants` path is left in any file.
  - The fragments of both old sentences ("critique skill", "those instructions point to") appear only in
    `foundations/part_map.md` and in `README.md:100`. The README binds nothing (part map, "Files left out on purpose").
  - No decision, invariant or glossary entry quotes the sentence of `agent-instructions` or `elements-common`.
  - The `part-map` sentence ("the test that holds the imports …") stays true: `test_cross_part_imports.py` stayed.
  - WAY-09's *Verification* ("the script that generates them stands with its test in `agent-instructions/`") does not
    list tests and needs no change.
- Corrections the change calls for:
  - *Files* patterns: `agent-instructions/**` and `elements/common/**` already claim both files.
  - *Depends on* and *Trust boundary*: no change is needed.
  - The four invariants: their *Method* fields already read `test`, from the change before the return step.
  - WAY-38, WAY-89 and WAY-09: their *Verification* fields already name the four invariants.
  - Beyond m2, I found no missed correction.
- The rule of the return step (`task-cycle/skill/return_step.md`):
  - No invariant was written for behaviour, and no entry is deferred or proposed for later. The author's "Unwritten on
    purpose" explains why nothing was written. It does not list anything for later.
  - The three rows of *Settlements to record* went to "data or code" and stand in the test file. Row 1: `SUFFIXES`,
    `NAMES` and `PLACES`, each with its reason. Row 2: `wrong_interpreter`. Row 3: `outside_imports` through `imports`.
    No log entry duplicates them.
  - The report names where each settlement went.

## Declined to judge

- Where the tests of the change stand: `agent-instructions/` for the script rules and `elements/common/` for the element
  directories. That placement belongs to the change before the return step, reviewed and passed twice (M3 of
  `fix-findings.md`, N1 of `review-fix-report.md`). I judged only whether the return step's sentences match it, and the
  tension with WAY-44 as m2.
- The linter and size tests missing from the `agent-instructions` sentence before this change. They come into this review
  only through the new sentence's colon (m1).

## Checks run

- `git diff 540aed04..3043e760`, `git log 540aed04..3043e760`, `git rev-parse HEAD` — exit 0. One commit, `part_map.md`
  only, head as given.
- `python -B elements/common/foundation_check.py` (Python 3.14.3) — exit 0, `0 errors`.
- `python -B -m unittest discover -s agent-instructions -p test_script_invariants.py` — 13 tests, `OK`.
- `python -B -m unittest discover -s elements/common -p test_element_directory_contents.py` — 13 tests, `OK`.
- `git grep` for `test_script_invariants`, `test_element_directory_contents`, `script_invariants`, "critique skill",
  "those instructions point to", "own code rules" and "the-way's own code" — the results are given above.
- Manual check: I read the two test files whole against the two new sentences.
- `git status --short` after the checks — empty. The worktree is unchanged.
- Not run: the full gate, which is the cycle's own run (WAY-160).

## Reaches beyond the dispatch

- `foundations/invariants.md`, the entries `ruff-blocking-rules`, `function-and-file-size` and `repository-file-location`
  (their *Part* and *Method* fields only): to see where tests of rules over many parts, `repository` among them, stand
  (m1, m2).
- `agent-instructions/test_linter_invariant.py` and `agent-instructions/test_size_invariant.py`, docstrings only: to see
  what else the part `agent-instructions` holds (m1).
- `README.md:90-112`: to check whether it repeats the old sentences.
- `foundations/decisions.md`, the passages that `git grep` found naming "the-way's own code": WAY-09 whole, which the
  dispatch named, and the heading of the section "Scripts and the gate". The aim was to find any entry quoting the old
  sentences.
- `docs/task-cycles/script-invariants-by-test/reports/fix-findings.md` (whole), `review-whole-report.md:215-225` and
  `review-fix-report.md:50-80`: to know what earlier reviews had asked the return step to settle (M3, N1) and not repeat
  them.
- `elements/part-map/template.md`, the head to "Assigning files" and the line of `skill/SKILL.md` that the word "sentence"
  finds: the form of a part's sentence, which the dispatch named.

## Working copies

None made. I changed no file, so no worktree of the head was needed. The directory `.runs/review-return/` was never
created.

## Unread material

- `elements/part-map/skill/SKILL.md`: only the lines found by the search for "sentence" were read, not the whole file.
- WAY-08 and WAY-61: only their *Scope* lines were read. The task quotes their sentences. Neither bears on a change to
  the part map.
- WAY-38 and WAY-89: read from the heading through *Scope*, not to the end of the rationale. Their sentences and
  *Verification* fields were checked against the author's claims.
- Everything else the dispatch names was read whole.

## Searches not found or unclear

- Unclear: what WAY-44's "Tests belong to the part they test" asks of a test of an invariant whose *Part* is
  `repository`. That part has no directory (WAY-09). See m2.
