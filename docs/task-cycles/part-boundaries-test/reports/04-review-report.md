FAIL b4a55092d8710ff59ec0110b2038f32ff5705ad2

# Report 04 — review of the whole change

Range reviewed: `dfd50e513c09bebe9d09d74209cd28612565da83..b4a55092d8710ff59ec0110b2038f32ff5705ad2`
(`git rev-parse HEAD` = `b4a55092d8710ff59ec0110b2038f32ff5705ad2`, the head the handoff gives).
Commits: `e7947e8` (decision, invariant, test, part map), `b4a5509` (template). One-author route,
no plan, so no slice attribution: each finding below comes from the one change.

Counts: blocking 1 (Important), Minor 4, out of scope 0.

## Findings

### Important

**I1 — the invariant `cross-part-imports` states its marked-invariant exception without its
direction, more broadly than row 3, WAY-299 and its own test.**

- Place: `foundations/invariants.md:310`, the clause "or an invariant "the part `<X>` does not
  depend on `<Y>`" naming the two parts reads `Violated: yes`".
- What is wrong: the clause binds `<X>` and `<Y>` to nothing; "naming the two parts" is met by an
  invariant in either order. Read as written, a marked "the part `shell` does not depend on `core`"
  names the two parts of an import `core` → `shell` and lets it pass. The settlement it is written
  from keeps the direction — row 3 of *Settlements to record*: "importu objętego niezmiennikiem
  „część X nie zależy od Y” oznaczonym jako naruszony" (the import the invariant covers, X → Y) —
  and so does everything else the change writes: WAY-299 (`foundations/decisions.md:9107`, "says
  part X depends on today"), the template (`elements/part-map/template.md:98`, "says it depends on
  today") and the test, which passes only the ordered pair (`elements/part-map/test_cross_part_imports.py:274`,
  `(part, other) in marked`).
- Why it matters: WAY-263 — an entry the change writes that restates its source more broadly or
  without a qualification is Important; WAY-114's *Rationale* names the review of the whole change
  as the only place a row's wording drift is caught, since the human accepted the meaning with the
  row and is not asked again. A later reader of the invariant (a return step, a product copying the
  example, which `elements/invariants/examples.md` now invites) can take the looser reading and the
  test then disagrees with its own sentence.
- Evidence: the three quoted lines above; the test's code at :274.
- Recommended fix: e.g. "…or an invariant "the part `<X>` does not depend on `<Y>`" reads
  `Violated: yes`, where X is the part of the importing file and Y the part of the imported one."
  (or "…an invariant … that covers that import"). No code change.

### Minor

**M1 — a name that resolves to no file the check can see is dropped in silence, so an import that
reaches another part through a directory another file put on `sys.path` passes unseen.**

- Place: `elements/part-map/test_cross_part_imports.py:216-225` (`resolve`) and the docstring at
  :7-8 ("a name that resolves to no such file … is no dependency").
- What is wrong: a module of part A imported by a test of part B (which adds A's directory) runs
  with B's directory on `sys.path` too (the gate's `discover` puts the test directory there,
  `gate/run_tests.py:53`), so `import helper` in A can resolve at run time to B's `helper.py`. The
  check resolves A's file only against A's directory, the root and A's own additions, finds nothing
  and counts no dependency, with no problem reported. The invariant's sentence ("by an `import`
  statement") covers that import.
- Evidence: scratch probe
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\miss.py`
  (run against the worktree's test module, outside the tree): fixture `core/lib.py: import helper`,
  `shell/helper.py`, `shell/test_x.py` adding `../core` → `check()` reports no forbidden import for
  `core/lib.py`, while Python with both directories on `sys.path` loads `shell\helper.py`.
- Why Minor: on today's tree every import resolves to the standard library or to a file the check
  sees (scratch `…\scratchpad\unresolved.py`: 0 unresolved non-standard-library imports over the
  38 tracked `.py` files, 20 edges), and the case needs code that would fail when run on its own.
- Cheap fix that matches the test's own principle ("a check that quietly sees less would pass",
  docstring :10-11): report as a problem an absolute import whose first name is neither in
  `sys.stdlib_module_names` nor resolved — the same boundary `script-imports` states and
  `python-stdlib-modules` already supports.

**M2 — several branches the author's report and docstring claim have no fixture, and mutating them
leaves the whole file green.**

- Place: `elements/part-map/test_cross_part_imports.py:174-175` (`extend`), :183-184
  (`sys.path = […]`, `+=`), :238-242 (relative imports, `level`), :219 (`__init__.py` candidate),
  :227-229 (dotted prefixes), :213 (own directory), :98-104 (a marked sentence wrapped over lines).
- Evidence: scratch mutation run
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\mutate.py`
  on a copy outside the tree (the test on the-way's tree still pointed at the worktree): each of
  these mutations survives with exit 0 and 0 failing tests — relative imports treated as absolute;
  `extend` branch removed; whole-`sys.path` assignment branch removed; prefixes reduced to the full
  name; own directory dropped from the search; `__init__.py` candidate removed; marked sentence read
  from its first line only. Killed (exit 1, one test each): `from … import name` resolution, root
  dropped, unclaimed-file problem dropped, `Violated` ignored, all test imports allowed.
- Why it matters: the test on the-way's tree uses none of these forms, so the fixtures are the only
  evidence the checker sees them; the author's own mutation of `sys.path` search showed exactly this.
  A fixture per claimed form would close it.

**M3 — a Python file the map lists under "Files left out on purpose" fails the test, though WAY-44
and `foundation_check` allow it.**

- Place: `elements/part-map/test_cross_part_imports.py:81-87` (`parts`), against
  `elements/common/foundation_check.py:530` and `:556-559`, which read the `Files left out on
  purpose` table and accept such a file.
- What is wrong: the copy of the pattern extraction (the author's concern 1) already diverges: it
  reports every unclaimed `.py` as `claimed by 0 parts`. The day a `.py` is left out on purpose, the
  invariant's test fails while the foundation is in order, and someone must edit the test. Loud, not
  silent, and no such file exists today — hence Minor.

**M4 — form of the prose.**

- `elements/part-map/template.md:97` is 122 characters, where the surrounding paragraph wraps at
  100 (the other lines over 100 in the file are table rows).
- `foundations/decisions.md:1083` — the re-wrap of WAY-44 leaves the short line "another. For a
  file that" before the old line continues.

## Declined to judge

- The invariant and test of loop2, and its current violations — *Out of scope* of the task.
- Whether running another part's script (`runpy.run_path`, a new process) is an import — the
  orchestrator's binding answer (no) stands; the change follows it (docstring :9, sentence bounded
  to `import` / `from … import`); it goes before Mariusz in the request.
- Naming the moment "a second part holding code" in `elements/part-map/skill/SKILL.md` (author's
  concern 4) — the task does not ask for it; the skill points to the template, which carries the
  rule.

## Against the task

- *To do* 1 — met: `elements/part-map/template.md:94-104` states the duty, when it is written, the
  two exceptions and the-way's own entry; the paragraph on an accepted dependency stays and refers
  to the rule (:106-115, WAY-299, WAY-40).
- *To do* 2 — met: `elements/part-map/template.md:71-74`, no new field.
- *To do* 3 — met: test, invariant, example line `elements/invariants/examples.md:15-17`.
- Acceptance criterion — met: the test passes on the tree; the checker resolves the one known
  cross-part import `project-level/readiness_check.py:46 → relation-model/fingerprint.py` as allowed
  and also `elements/part-map/test_cross_part_imports.py:35 → elements/common/foundation_check.py`
  (`part-map` depends on `elements-common`), no problems, no marked pairs (scratch
  `…\scratchpad\edges.py`).
- Row 1 → WAY-299: meaning kept (duty, when written, exceptions, "no list of known violations");
  *Rejected* holds exactly Q1 A/C, Q2 b/c, Q6 b/c of the task, nothing derived (WAY-134).
- Row 2 → WAY-44 edited in place: meaning kept; *Rejected* gains Q3 b/c and Q7's way, nothing
  derived; *Verification* gains `invariants: cross-part-imports`.
- Row 3 → `cross-part-imports`: meaning kept except the direction of the marked exception (I1).
  The restriction to Python files and import statements is not a narrowing in effect: WAY-38 holds
  every script of the-way to Python, the tree holds only `.py` and `.md`, and the orchestrator's
  binding answer bounds the invariant to import statements.
- *Part* `every` (WAY-62: the test reads the whole tree), *Method* `test`, the citation at the one
  test on the real tree and none at the fixtures (WAY-61, WAY-65) — consistent.
- Changed invariant tests: none changed; one new invariant test,
  `elements/part-map/test_cross_part_imports.py::TheWay::test_the_way_imports_only_from_allowed_parts`
  (`# invariant: cross-part-imports`).
- Reserved choice: none taken — standard library only (`ast`, `subprocess`, `tempfile`), git as
  `foundation_check` already calls it (WAY-38).
- Trust boundary: none — the test reads only the repository's own files; its temporary attributes
  file is created by `mkstemp` and removed in `finally`.
- Guidelines: the-way has no `guidelines/` directory; the task records the decided WAY-215
  departure. No guideline compared.
- Author's own-work check: it targeted a real weak point (does the check see `sys.path` imports on
  the real tree) and its scratch run would catch that requirement unmet; it does not reach the
  silent drop of unresolved names (M1) or the untested branches (M2).
- Author's open question on an environment fact for Python's import rules: none is needed — the
  sentence states no fact of Python's resolution; the test over-approximates it (every search
  directory), which can only make it stricter.

## Checks run

- `git rev-parse HEAD` → `b4a55092…`, exit 0; `git log` / `git diff dfd50e5..b4a5509` read whole.
- `python -B gate/run_tests.py elements/part-map` → exit 0, 12 tests OK.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` → exit 0, 109 tests OK.
- `python -B gate/run_tests.py agent-instructions` → exit 0, 18 tests OK.
- `python -B gate/run_tests.py gate` → exit 0, 20 tests OK.
- `python -B gate/run_tests.py elements/invariants` → exit 1, "no test found in
  elements/invariants" — expected: the directory tracks no `test_*.py`, so the full gate never
  runs it; not a failure of the change.
- `python -B gate/run_tests.py project-level` → exit 0, 268 tests OK (the importing side of the
  one cross-part import).
- `python -B gate/run_tests.py relation-model` → exit 0, 12 tests OK.
- Scratch mutation run (`…\scratchpad\mutate.py`, copy of the test outside the tree) → 13
  variants, results under M2.
- Scratch probes `…\scratchpad\unresolved.py`, `…\scratchpad\edges.py`, `…\scratchpad\miss.py` →
  results under M1 and *Against the task*.
- `git status --short` in the worktree after the checks → empty.
- Not run: the whole gate — reserved for the orchestrator by the handoff.

## Reaches beyond the dispatch

- `foundations/decisions.md`: WAY-40, WAY-42, WAY-51, WAY-225, WAY-62, WAY-134, WAY-114, WAY-19,
  WAY-63 read whole — the decisions the change's entries derive from, the task names, or that
  govern rows, numbering and invariant parts; WAY-16 and WAY-61 by their sentences, for the
  rationale's citations and the citation rule.
- `elements/decisions/skill/decide_entry.md` and `elements/decisions/template.md` "Changing a
  decision" — whether the in-place edit of WAY-44 follows the rule.
- `foundations/invariants.md` `script-imports` — for M1's boundary.
- `elements/common/foundation_check.py` (`check_files`, `read`, `git`, constants) — to compare the
  copied extraction (M3).
- `gate/run_tests.py` — how test directories put themselves on `sys.path` (M1).
- `elements/common/way_of_working.md` "Reading the foundation" and `product-guidelines/reading.md`
  — the method's selection.

## Searches not found or unclear

- Unclear: the selection by "Reading the foundation" step 2. The touched parts (`part-map`,
  `invariants`, and through WAY-44's *Scope* `agent-instructions` and `task-cycle`) give about 150
  decisions by *Scope*; I read whole those listed under *Reaches* plus WAY-44 and WAY-299 in the
  diff, not every decision of those scopes — chiefly the `task-cycle` ones, which govern the cycle
  rather than what this change writes.
- Not found: a line-width rule for Markdown in `elements/common/rules.md` or
  `agent-instructions/`; M4 rests on the file's own wrapping.
- Not found: any fixture for relative imports, `extend`, whole-`sys.path` assignment or a wrapped
  marked sentence (M2).
