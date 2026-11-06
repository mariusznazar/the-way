# Report 02 — the one author of the whole change

**Status:** done with concerns (the concerns are listed under "Concerns"; none blocks the change)

## Commits

On `task/part-boundaries-test`, base `dfd50e5`:

- `e7947e8` feat: cross-part-imports holds the-way's Python imports to the dependencies its part map allows
- `b4a5509` docs: the part map template states the invariant of allowed dependencies and the part of test helpers

Each commit passes `python -B elements/common/foundation_check.py`. The decision, the invariant
and the test sit in one commit because each one names the others.

## Files changed (added / removed lines, `git diff --numstat dfd50e5..HEAD`)

| File | + | − |
|---|---|---|
| `elements/part-map/test_cross_part_imports.py` (new) | 456 | 0 |
| `foundations/decisions.md` (new WAY-299; WAY-44 edited in place) | 80 | 9 |
| `foundations/invariants.md` (new `cross-part-imports`) | 10 | 0 |
| `foundations/part_map.md` (sentence of `part-map`) | 2 | 2 |
| `elements/invariants/examples.md` (example line) | 3 | 0 |
| `elements/part-map/template.md` (*To do* 1 and 2, fields table) | 25 | 4 |

Every file keeps LF endings (`git ls-files --eol`: `i/lf w/lf` for all six).

## What was made

- **To do 1** — `elements/part-map/template.md`, "Allowed dependencies": a new paragraph and a
  three-item list. It states the duty: one invariant of allowed dependencies, with its test, and
  its two exceptions. It says when the invariant is written (the change that brings in a second
  part holding code; a task of its own in a product that already has such parts), and that the
  product's task settles how a test file is recognised. It names `cross-part-imports` as the-way's
  own. The paragraph on an accepted dependency stays. It now says that the invariant of allowed
  dependencies lets that import pass and keeps every other boundary, and that such an invariant is
  a whole entry, not a list of known violations (WAY-299, WAY-40). In the "Fields and their
  readers" table, the rows *Files* and *Depends on* gain the new test as a reader.
- **To do 2** — "Assigning files": a new bullet. The files that serve the tests of several parts
  are a part of their own, which its sentence describes, with no new field. The tests of every
  part may import from it; code that is not a test may not (WAY-44).
- **To do 3** — the test `elements/part-map/test_cross_part_imports.py`, the invariant
  `cross-part-imports`, and its example line in `elements/invariants/examples.md`.
- **Part map**: the sentence of `part-map` now also names the test, because the part now holds it
  (template: a change that changes what a part answers for rewrites the entry in the same change,
  WAY-11). This is a reach beyond the handoff. See below.

## The test: each choice, the way rejected and its cost if wrong

| Choice | Rejected | Cost if wrong |
|---|---|---|
| Lives in `elements/part-map/`, a new test directory. It reuses `foundation_check`'s parser of the map and the invariants (`blocks`, `fields`, `ENTRY`, `items`, `read`, `git`). `part-map` may depend on `elements-common`. | `gate/` (`Depends on: none`, so it could not import the parser); a self-contained parser (a second reader of the map that could drift) | The directory runs only once tracked. It is tracked in `e7947e8`. |
| Files are assigned to parts by `git check-attr` with a temporary attributes file, as `foundation_check.check_files` does. The extraction of patterns is copied, not shared. | Refactoring `check_files` so it returns the assignment — that would touch `elements-common` beyond the task | Two copies of about 15 lines of pattern extraction. If one changes and the other does not, the two disagree. |
| Imports are read with `ast` from every tracked `*.py`: `import` and `from … import` anywhere in the file, inside functions too. Relative imports resolve against the package directory. | A regex scan (it would count imports inside strings) | — |
| A name resolves to **every** tracked file it names in each search directory: the file's own directory, the repository root, and each directory the file adds to `sys.path`. It tries each dotted prefix, as `name.py` or `name/__init__.py`, and `module.name` for `from module import name`. | Modelling Python's real order of `sys.path` (it depends on how a file is started: as a script, under `unittest discover`, or under the gate) | A name that exists in two search directories counts as importing both. The check is then stricter than Python, never weaker. |
| `sys.path` additions it recognises: `.insert(i, X)`, `.append(X)`, `.extend([..])`, `sys.path[i] = X`, `sys.path = [..]`, `sys.path += [..]`. For `X` it can evaluate: string constants, `__file__`, a name assigned exactly once in the file, `os.path.join/dirname/abspath/realpath/normpath`, `str()`, `Path()`/`pathlib.Path()`, `.resolve()`, `.absolute()`, `.parent`, `/`, and `os.getcwd()`, which it takes as the repository root (the gate and the scripts run from the root). | — | — |
| An addition to `sys.path` that it **cannot evaluate fails the test**. It is listed among the "problems" that the test asserts are empty, as `path:line: adds to sys.path a directory the check cannot work out`. | Reporting it and passing | A new way of writing an addition to `sys.path` makes the test fail until the evaluator learns it. That is deliberate: a check that silently sees less would still pass. |
| A tracked `*.py` that no part claims, or that two parts claim, also fails (`claimed by N parts`). | Skipping it | The test overlaps a little with `foundation_check`. |
| A test file is a file whose name starts with `test_` and ends with `.py` — the files the gate runs. | — | — |
| Parts of test helpers: `TEST_HELPER_PARTS = ()`. The-way has none. The check function takes the helper parts as an argument. | A new field in the map (rejected by the task, question 7) | A helper part added to the map but not to the tuple makes the test fail on the test imports that use it. It fails loudly, not silently. |
| Marked exception: an entry of `foundations/invariants.md` whose sentence matches ``The part `X` does not depend on `Y`.`` (capital or small T, the sentence wrapped over lines), with `Violated: yes`. This lets X → Y imports pass. | — | A marked invariant worded differently from the template's form is not recognised, and its import fails the shared test. |
| Running another file as a script (`runpy`, a new process) is no import. This follows the orchestrator's answer; the sentence bounds itself to `import` / `from … import` statements. No test pins it: only a deliberate decision could change it. | — | — |
| The test cites `# invariant: cross-part-imports` at its one test on the-way's real tree. The fixture tests cite nothing, because they check the checker. | — | — |

## Checks run (command → exit code)

All commands run from the worktree root.

- **The invariant's test, seen failing** — I temporarily removed `relation-model` from
  `project-level`'s *Depends on* in `foundations/part_map.md`:
  `python -B gate/run_tests.py elements/part-map` → **exit 1**. The failure:
  `test_the_way_imports_only_from_allowed_parts`, `AssertionError: Lists differ: [] !=
  [('project-level/readiness_check.py', 46, …relation-model…)]`. The file was restored from a
  copy, and `git diff --stat foundations/part_map.md` was empty afterwards.
- **The same test, passing** — `python -B gate/run_tests.py elements/part-map` → **exit 0**
  (12 tests, OK). The last run was after both commits.
- **Mutations of the checker** — each run as `python -B gate/run_tests.py elements/part-map`, each
  restored from a copy afterwards:
  - `sys.path` directories dropped from the search → exit 1, 5 fixture tests fail. The test on
    the-way's tree still passes, which shows why the fixtures are needed.
  - helper exception removed → exit 1 (`test_test_importing_a_part_of_test_helpers_passes`);
  - marked-invariant exception removed → exit 1 (`test_import_a_marked_invariant_names_passes`);
  - problems discarded → exit 1 (`test_sys_path_the_check_cannot_work_out_fails`);
  - string constants no longer evaluated → exit 1, 7 tests fail, the-way's tree among them.
- **Focused directories**, all before the last two re-wraps of lines (only the HEADER constant
  and template prose changed after them):
  `python -B gate/run_tests.py elements/common` → exit 0 (109 tests);
  `python -B gate/run_tests.py agent-instructions` → exit 0 (18);
  `python -B gate/run_tests.py gate` → exit 0 (20).
  `elements/part-map` was rerun after the commits → exit 0.
- **Form of the foundation** — `python -B elements/common/foundation_check.py` → exit 0,
  `0 errors` (after the commits).
- **Not run:** the whole gate `python -B gate/run_tests.py`. The handoff reserves it for the
  orchestrator.

## Own-work check (section 3)

- **The requirement most likely missed:** that the test actually sees imports made through
  `sys.path` on the real tree, rather than passing because it sees nothing. **Check:** a scratch
  script (`…\scratchpad\edges.py`, outside the repository) printed every import edge the checker
  resolves on the-way. **Result:** 20 edges, two of them across parts:
  `project-level/readiness_check.py:46 → relation-model/fingerprint.py` (through
  `os.path.join(HERE, "..", "relation-model")`) and
  `elements/part-map/test_cross_part_imports.py:35 → elements/common/foundation_check.py` (allowed:
  `part-map` depends on `elements-common`). It found no problems and no marked pairs. The
  `sys.path.insert(0, str(Path(reader).parent))` inside the string literal of
  `project-level/test_plan_state_subprocesses_invariant.py` is not counted; if it were, it would
  show up as an addition the check cannot evaluate. That is evidence on the real tree that strings
  are skipped.
- **The second requirement checked:** WAY-299's *Rejected* and the additions to WAY-44's
  *Rejected* carry only the ways the source does not choose (WAY-134). I checked each item against
  the task:
  - WAY-299 — Q1 A (script of the process) and C (left to the return step); Q2 b (advice) and c
    (template unchanged); Q6 b (one invariant per part) and c (WAY-51 alone).
  - WAY-44 — Q3 b (Depends on loosened) and c (imports from tests unchecked); Q7's only *Not
    chosen* (a field or mark). I added no way of my own.
  - The product-specific facts were made general: "the violation in loop2's simulation test" →
    "a dependency outside the map that came in stays"; "18 merges" → "many merges". The rule
    against counts in *Rationale* and *Rejected* asks for that.

## Entries written — meaning sentences and mark

| Entry | Mark | Meaning (English) | Meaning (Polish) |
|---|---|---|---|
| WAY-299 (new) | row 1 | Every product whose parts import code from other parts holds one invariant with a test: a file imports only its own part, the parts its *Depends on* names, a part of test helpers when it is a test, and a part that a marked "X does not depend on Y" invariant names. The product writes it when a second such part enters the map, or in a task of its own in an existing product. Such marked invariants are whole entries a human accepted, not a list of known violations. | Każdy produkt, którego części importują kod z innych części, ma jeden niezmiennik z testem: plik importuje tylko z własnej części, z części dopuszczonych w *Depends on*, z części pomocników testów, gdy jest testem, i z części, którą wskazuje oznaczony jako naruszony niezmiennik „X nie zależy od Y”. Produkt zakłada go, gdy w mapie pojawia się druga taka część, a produkt już działający robi to osobnym zadaniem. Taki oznaczony niezmiennik to pełny wpis zaakceptowany przez człowieka, a nie lista znanych naruszeń. |
| WAY-44 (edited in place) | row 2 | The files that serve the tests of several parts form a part of their own, described by its sentence, with no new field; tests of every part may import from it, code that is not a test may not. | Pliki obsługujące testy kilku części tworzą osobną część, opisaną jej zdaniem, bez nowego pola; testy każdej części mogą z niej importować, a kod, który nie jest testem — nie. |
| `cross-part-imports` (new) | row 3 | In the-way no Python file imports, by an import statement and through `sys.path` too, a file of a part its own part's *Depends on* does not name, except a test importing a part of test helpers and an import a marked "X does not depend on Y" invariant covers. | W the way żaden plik Pythona nie importuje — instrukcją import, także przez `sys.path` — pliku części, której *Depends on* jego części nie dopuszcza, poza importem z testu do części pomocników testów i importem objętym oznaczonym niezmiennikiem „X nie zależy od Y”. |
| `part-map` part sentence (edited) | the cycle's | The part-map part now also answers for the test that holds the-way's imports to the dependencies the map allows. | Część part-map odpowiada teraz także za test, który pilnuje, żeby importy kodu the way trzymały się zależności dozwolonych w mapie. |

Other fields, for the review:

- WAY-299: *Scope* `part-map, invariants`; *Relations* `derives from WAY-225 · derives from
  WAY-51`; *Verification* `invariants: cross-part-imports`, plus a complies/violates pair;
  *Based on* and *Origin* `none`. The "why it is no list of known violations" is in *Rationale*.
- WAY-44 gains `invariants: cross-part-imports` in *Verification* and one complies/violates
  example each. Its *Rationale* gains why a helper part is consistent with "tests belong to the
  part they test". The existing *Rejected* item "tests as a part of their own" is kept, with the
  clause "while a helper serving the tests of several parts tests nothing" added.
- `cross-part-imports`: *Method* `test`; *Rests on* `git-path-patterns` (the part of a file is
  decided by git's matching — `elements/invariants/skill/draft.md` gives this exact case);
  *Derives from* `WAY-299 · WAY-44`; *Part* `every`; *Violated* `no`.

## Reaches beyond the handoff

- `elements/part-map/skill/SKILL.md` and `elements/part-map/examples.md` — read to see whether
  the skill or the examples state the rule I changed. The skill's *Depends on* step points to the
  template's "Allowed dependencies", so it needed no edit.
- `foundations/environment_facts.md` — `git-path-patterns` and `python-stdlib-modules`, read whole
  for the invariant's *Rests on*.
- WAY-03, WAY-25, WAY-30, WAY-42 and WAY-298 — read whole: WAY-298 to confirm the last number,
  WAY-30 and WAY-25 for the in-place edit and possible collisions, WAY-42 for the binding part of a
  part sentence, WAY-03 as the decisions' example.
- `foundations/glossary.md` — the entries *invariant*, *invariant test*, *part*, *part map* and
  *return step*, to decide whether "part of test helpers" needs a term. It does not: a reader of
  the field reads "test helpers" in its usual sense.
- `elements/common/rules.md`, `elements/common/way_of_working.md` and
  `elements/decisions/skill/{read,decide_entry}.md` — named by the element skills' steps.
- `gate/run_tests.py`, `elements/common/foundation_check.py` and several test files — read to build
  the test.
- The edit of `part-map`'s sentence in `foundations/part_map.md` (see "What was made").

## Search of the foundation (WAY-33)

I searched `foundations/*.md` for: Depends on, allowed dependenc*, does not depend on, known
violation*, part they test, test helper*, helpers, import graph, imports code, dependency/ies the
code. Outside the foundation I searched `elements/`, `task-cycle/`, the skills, does not depend
on, known violations and part they test.

- **WAY-40** — *Verification* forbids "a list of known violations" in the map. Consistent: the
  marked invariants stay in the invariants file, and WAY-299 says why they are no such list. No
  edit.
- **WAY-51** — consistent. The shared invariant is met while an accepted dependency is marked, so
  it is never marked violated. WAY-299 derives from it. No edit.
- **WAY-225** — its complies example ("the return step compares them with the dependencies the
  code holds") still holds. A test now compares them too. No edit.
- **WAY-11** — the return step still compares the map with the code. No edit.
- **WAY-38** — the test is in Python, the-way's own language. The *Rejected* item "scripts parsing
  other languages" is not touched. No edit.
- **WAY-42** — the edited part sentence names a responsibility, not paths.
- No collision without a recorded precedence was found, and no glossary term was needed.

## Searches not found or unclear

- **Line numbers of the task:** every quoted place still matches at `dfd50e5` —
  `elements/part-map/template.md:84`, `:86-94`, `:90-94` and `:38-47`; WAY-44 at
  `foundations/decisions.md:1070`; WAY-51 at `:1184`; `project-level/readiness_check.py:45`;
  `relation-model/test_fingerprint.py:108`; `project-level/test_plan_state_subprocesses_invariant.py:82`
  (inside a string literal). No correction needed.
- **Unclear: which environment fact covers Python's own rules of import resolution.** None exists.
  The test approximates those rules (search directories, prefixes). The entry does not rest on a
  Python fact, the same as `script-imports`, which rests only on the standard-library fact. Whether
  one is needed is left to the review.
- **Unclear: the order of search directories on `sys.path`.** Python's real order depends on how a
  file is started. I chose "every directory" (stricter). See the choices table.

## Concerns

1. **The pattern extraction is copied.** `parts()` in the test repeats about 15 lines of
   `foundation_check.check_files` (pattern cleanup and the `git check-attr` call) instead of
   sharing a function, so that `elements-common` stays untouched. If the map's pattern syntax
   changes in one place, the two can disagree. A later refactor could expose an assignment
   function from `foundation_check`.
2. **The marked-invariant exception depends on the exact wording.** Only the template's form ("The
   part `X` does not depend on `Y`.") is recognised. A marked invariant worded otherwise is not
   recognised, and the shared test fails. It fails loudly, which I think is acceptable; I mention
   it because WAY-299's *Rationale* names the cost "a reviewer may take it for such a list".
3. **The task's *Context* says the earlier scan missed the-way's sys.path import.** This test sees
   it (own-work check). Nothing outstanding.
4. **Possible follow-up, not done:** `elements/part-map/skill/SKILL.md` could name, at its *Depends
   on* step, the moment a second part holding code enters the map. Today the template carries the
   rule and the skill points to it, so I left the skill alone (and the handoff asks for no change
   to skill descriptions).

## Questions

none
