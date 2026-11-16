PASS 4bc1667cfafcc1af23d6bf4820eab61297952661

# Review of the whole change — script-invariants-by-test

Range: base `604907c88d9973ccf2dbf697e3ce7e1f358fa81c` to head `4bc1667c` (`git rev-parse HEAD` in the
worktree gives `4bc1667cfafcc1af23d6bf4820eab61297952661`, the head given). One commit, route of one
author without a plan, so this is the only review the change gets.

Changed files (`python -B task-cycle/change_file_sizes.py 604907c8… 4bc1667c`, exit 0):

| File | Before | After | Change |
|---|---|---|---|
| `elements/common/test_element_directory_contents.py` | — | 222 | +222 (added) |
| `elements/part-map/test_script_invariants.py` | — | 209 | +209 (added) |
| `foundations/invariants.md` | 546 | 546 | +0 (4 lines `Method: review` → `Method: test`) |

Blocking findings: 0. Minor findings: 4, all within the task. Out-of-scope findings: 0.

## Findings

### Critical

none

### Important

none

### Minor

**M1 — `elements/part-map/test_script_invariants.py:52` — the kind `.yml` lets more through than its reason covers (within the task).**
The comment at the kind gives one reason: "data: the CI configuration under `.github/workflows/`
names the commands CI runs". But the list admits the ending `.yml` anywhere in the repository, so a
file that is a program in all but language passes `script-language` without anyone adding it with a
reason of its own. Settlement row 1 chose a list of kinds so that nothing passes quietly. Here a kind
is admitted more widely than its reason, and that is the way a file would pass quietly. Evidence: in a
worktree of the head I tracked a root file `tools_deploy.yml` holding an Ansible-style playbook
(`- hosts: all / tasks: / - shell: echo deploy`).
`python -B -m unittest discover -s elements/part-map -p test_script_invariants.py -k test_every_file_git_tracks`
gave exit 0, `OK`, where `build_tool.sh` gave exit 1. The author's own report sees this ("a person who
wants it stricter narrows it to the name `tests.yml`"). The fix: list the CI configuration by its
place, a path under `.github/workflows/` ending in `.yml`, or by its name. Then the reach matches the
reason the comment gives. Effect today: none, since the only tracked `.yml` file is the CI workflow.
That is why it is Minor.
On the other three kinds the handoff asked me to judge (Q2): `ruff.toml`, `requirements-quality.in`
and `requirements-quality.txt` are listed by name. Each is data that a tool reads (linter
configuration, a package list, a package list with hashes). Their reasons hold and their reach matches
their reasons.

**M2 — expected values taken from the code's own wording, and test data with no source comment (within the task).**
- `elements/part-map/test_script_invariants.py:205` asserts the exact text
  `"a.py:2: imports a module the check cannot work out"`, which is the wording `Resolver.runs` of
  `elements/part-map/test_cross_part_imports.py:404` gives. `guidelines/testing.md`
  ("Where the expected value comes from", WAY-394: "never … from a constant or a function of the code
  it checks") and "Behaviour, not implementation" ("the exact wording of a message") both reach it;
  the requirement (settlement row 3) is that such an import is reported, which `len == 1` and the
  line number would carry.
- `elements/common/test_element_directory_contents.py:151-152`, `:159-160`, `:165`, `:170`,
  `:174-176` assert the full sentences that `missing()` of the same file builds (`:97-102`), so a
  rewording breaks five tests with no change of behaviour.
- The *Data* field of the recipes, which binds (WAY-395: "the values of a test written out in it,
  each with its source in a comment"): `test_script_invariants.py:135-140` (the listed kinds — source
  the task's list and settlement row 1), `:169-171` (patch release — source author's choice 4 against
  the sentence of `python-version-declared`), `:173-181` (the six forms — source settlement row 3)
  and the classes `Missing` and `MergeOntoExists` of `test_element_directory_contents.py:119-218`
  (source the invariant's sentence and `elements/common/rules.md:87-89`) carry no comment naming the
  source. The neighbouring `test_cross_part_imports.py` does the same, so this follows local habit,
  but the rule binds new tests. Consequence: brittleness and a reader who cannot tell where a value
  comes from; no wrong verdict — hence Minor.

**M3 — `elements/part-map/test_script_invariants.py` (whole file) — tests of `repository` and `every` placed in `part-map`, whose map sentence does not name them (within the task).**
WAY-44 says: "Tests belong to the part they test". The map gives `part-map` this sentence
(`foundations/part_map.md:19-20`): "the form of an entry, the skill that writes one, the map of the-way
itself and the test that holds the imports of the-way's code to the dependencies it allows". The test
of `script-imports` reuses that reader, so it fits the sentence. The tests of `python-version-declared`
(*Part* `repository`) and `script-language` (*Part* `every`) do not fit it. Nor does WAY-38 or WAY-89
name `part-map` in its *Scope*. A later change to this file would therefore select its decisions by
`--part part-map` and find neither of the two. WAY-62 and the *Derives from* links of the invariants
reduce that cost, since the citing test still reaches them. The author rejected only `gate/`. It did
not consider `agent-instructions/`. That part already holds the tests of the-way's own code rules
(`test_linter_invariant.py`, `test_size_invariant.py`). Its *Depends on* names both `part-map` and
`repository`, so it could also import the reader `imports` legally. Two ways to settle it: the return
step widens the sentence of `part-map` to name these tests, or the file (or its two tests that import
nothing) moves to `agent-instructions/`. No test result changes either way. That is why it is Minor.

**M4 — `elements/part-map/test_script_invariants.py:153` — a missing `.python-version` gives a misleading refusal (within the task).**
`(declared_lines(THE_WAY) or ["none"])[0]` turns a missing file into the version `none`. The test
then fails with "the tests have to run on Python none, the version .python-version declares, and this
run is on Python 3.14". It does fail. In the same run `python-version-declared` reports the real cause,
so nothing passes quietly. But the message names a version where it should name the missing file. That
is the reading of an absence as a value, which WAY-344 warns of, in a test rather than a script. Fix:
fail with a message that names `.python-version` as missing.

## Coverage against the task

- *To do* 1 (`python-version-declared`): met, `PythonVersionDeclared` at `:107-115`. It checks that git
  tracks the file, that it holds one line and that the line is `3.14` or `3.14.<patch>`.
- *To do* 2 (`script-language`): met. The task's five kinds plus four added kinds (M1). A file whose
  kind is not on the list is reported. A command inside a `.md` file is no script.
- *To do* 3 (`script-imports`): met. The test reads with `imports` of `test_cross_part_imports`, which
  gives the same reach as `cross-part-imports`: `import`, `from … import`, `import_module`,
  `__import__`, `runpy`, `-c`, `exec`, `eval` and `compile`. An import whose name cannot be worked out
  is reported. On another interpreter the test fails naming both versions. `outside_imports` reads every
  tracked `.py` file, so it reaches further than `check()` of `cross-part-imports`, which skips files no
  part claims. That is no loss.
- *To do* 4 (`element-directory-contents`): met. It covers the template, `examples.md` or a backticked
  tracked `foundations/*.md` under the template's `## Examples`, and `skill/SKILL.md`. The test is
  skipped with its reason where no main branch exists.
  I checked the reading of "where {merge-onto} exists" against WAY-60 and WAY-61. The condition is
  whether the main branch exists, and the commit being checked is what gets checked. That agrees with
  the sentence. CI sets `origin/HEAD` (`.github/workflows/tests.yml:42`, `:69`), so the test runs there
  and is not skipped. In my runs here it ran and was not skipped.
- *To do* 5: met. `git diff` of `foundations/invariants.md` shows exactly four lines changed, each
  `- **Method:** review` → `- **Method:** test`, under the four headings. Nothing else changed.
- *Settlements to record* row 1: met, `SUFFIXES`/`NAMES` with a reason at each kind (`:45-61`) and
  the module docstring; reach of `.yml` → M1.
- Row 2: met. `wrong_interpreter` (`:85-92`) is used at `:152-156`. The reason is in the docstring
  (`:19-23`) and in the comment at `:162-164`. Seen failing on Python 3.12, below.
- Row 3: met, through `imports` (same reach); seen below with a file holding `import yaml`, an
  `import_module` of an environment variable, `runpy.run_module("requests")` and `exec("import numpy")`.
- WAY-03: the tests are new invariant tests, all named in the author's report under "Tests written",
  for the request.
- WAY-61: only the repository tests on the real checkout cite the invariants. The tests on made-up
  input cite none. That is right.
- WAY-321: `foundation_check.py` with no switch gives `0 errors`, so every invariant whose method reads
  `test` is cited.

## Declined to judge

- A `.py` file that holds text of another language passes `script-language` (the author's concern).
  Settlement row 1 chose to recognise a script by its kind, so the content is outside what the task
  asks.
- The test of `cross-part-imports` takes its list of standard modules from whatever interpreter runs it,
  with no version check. That is another invariant's test, which this change does not alter.
- The test of `script-subprocesses`: named out of scope in the task.

## Checks run

- `git rev-parse HEAD` → `4bc1667cfafcc1af23d6bf4820eab61297952661`; `git log`/`git diff 604907c8..HEAD` → one commit, three files.
- `python -B task-cycle/change_file_sizes.py 604907c88d9973ccf2dbf697e3ce7e1f358fa81c 4bc1667c` → exit 0 (table above).
- Size of functions and files: `python -B -m unittest discover -s agent-instructions -p test_size_invariant.py -k test_no_function`
  in a worktree of the base and one of the head, with the `@unittest.expectedFailure` mark taken off
  (the invariant `function-and-file-size` reads `Violated: yes`). Both exited 1 with the same list,
  "11 functions over 80 lines and 2 files over 1000 lines". The diff of the two outputs differs only in
  the worktree path, so the change pushes nothing over a threshold. Test files stand outside the rule
  in any case (WAY-385).
- `python -B gate/run_tests.py elements/part-map` (reviewed worktree) → exit 0, 51 tests, OK.
- `python -B gate/run_tests.py elements/common` (reviewed worktree) → exit 0, 270 tests, OK, none skipped.
- `python -B elements/common/foundation_check.py` (reviewed worktree, no switch) → exit 0, `0 errors`.
- `ruff check --config ruff.toml --no-cache --ignore-noqa --output-format concise` on the two new files,
  Ruff 0.17.1 from `.runs/quality-venv` of the main checkout → exit 0, `All checks passed!`.
- Searched the two new files for absolute paths and note links → no match. Positive control: the same
  glob finds the 4 `# invariant:` lines.
- `git status --short` of the reviewed worktree after all runs → clean.
- WAY-08, each invariant's test seen failing and then passing, in a worktree of the head:
  - `python-version-declared`: `.python-version` written as `3.13`. Then
    `python -B -m unittest discover -s elements/part-map -p test_script_invariants.py -k PythonVersionDeclared`
    → exit 1, `AssertionError: False is not true : .python-version declares '3.13', not Python 3.14`.
    After it was restored: exit 0, OK.
  - `script-language`: tracked `build_tool.sh` → `-k test_every_file_git_tracks` exit 1,
    `AssertionError: Lists differ: [] != ['build_tool.sh']`; removed → exit 0 (and the `.yml` probe of M1, exit 0).
  - `script-imports`: a tracked `elements/part-map/zz_break.py` gave `-k test_no_python_file_git_tracks`
    exit 1, with four lines: `:4: imports \`yaml\`…`, `:5: imports a module the check cannot work out`,
    `:6: imports \`requests\`…` and `:7: imports \`numpy\`…`. Wrong interpreter:
    `py -3.12 -B -m unittest … -k test_no_python_file_git_tracks` → exit 1,
    `AssertionError: the tests have to run on Python 3.14, the version .python-version declares, and this run is on Python 3.12: …`.
    After the file was removed, on Python 3.14.3: `-k ScriptImports` → exit 0, OK.
  - `element-directory-contents`: `git mv elements/glossary/skill/SKILL.md …` → `-k test_every_element`
    exit 1, `['elements/glossary has no skill/SKILL.md']`. The backticked path in
    `elements/environment-facts/template.md` replaced by words → exit 1,
    `elements/environment-facts has no examples.md and its template points to no file of foundations/ as its examples`.
    A tracked `elements/newelement/template.md` alone → exit 1, both lacks listed. All restored →
    whole file exit 0, OK.

## Reaches beyond the selection

- `elements/part-map/test_cross_part_imports.py` (whole): the code under reuse, to judge settlement row 3 and M2.
- `elements/common/rules.md:80-89` (`{fork-point}`, `{merge-onto}`) and `elements/common/foundation_source.py` (`MAIN_BRANCHES`, by search): the condition of `element-directory-contents`.
- `elements/environment-facts/template.md` `## Examples` (by search): the pointer the test accepts.
- `.github/workflows/tests.yml` (whole): whether CI sets `origin/HEAD`, and the `.yml` kind.
- `agent-instructions/test_size_invariant.py` (the mark at `:88`): for the size runs.
- `foundations/environment_facts.md` `## python-stdlib-modules`: the fact `script-imports` rests on.

## Working copies

- `.runs/review-whole/base` (worktree of `604907c8`) and
  `.runs/review-whole/head` (worktree of `4bc1667c`).
  Both were removed with `git worktree remove --force`, then `git worktree prune`. The directory
  `.runs/review-whole/` was removed with them, and with it the outputs of the runs, the decision index
  and the list of sections. Nothing remains, and nothing was kept in `reports/` beyond this report.

## Unread material

16 decisions of the index of my selection were read whole: WAY-09, WAY-03, WAY-08, WAY-51, WAY-60,
WAY-61, WAY-62, WAY-69, WAY-44, WAY-38, WAY-55, WAY-63, WAY-89, WAY-344, WAY-394 and WAY-395. The
index was built from the sections "Invariants", "Scripts and the gate" and "The-way's own coding and
testing guidelines", the parts `part-map`, `elements-common`, `invariants` and `repository`, and the
decisions WAY-38, 89, 09, 08, 61, 344, 395 and 03. It lists 40 decisions in full and 47 by heading.
WAY-321 was read to the start of its rationale. The other decisions listed in full were read by their
binding sentences in the index. The 47 headings were run through by question. Of them I opened WAY-44
and WAY-55 whole.
The parts the change touches by the entries it changes are `decisions`, `invariants`, `glossary`,
`environment-facts` and `every`. For them I did not run `--part` beyond the four parts above. The
reason: the change alters only the *Method* of the entries, and the sections run cover the method of
an invariant.
Read whole as well: the guideline files `guidelines/testing.md` and `guidelines/coding.md` (no file
`guidelines/coding-<kind>.md` matches a test file), `product-guidelines/reading.md`, "Reading the
foundation" of `elements/common/way_of_working.md`, `foundations/part_map.md`, `foundations/glossary.md`,
and the invariants `element-directory-contents`, `script-language`, `script-imports`,
`script-subprocesses`, `python-version-declared`, `cross-part-imports`, `ruff-blocking-rules`,
`function-and-file-size` and `test-method-citation`.
The author's reading against WAY-344: it read WAY-344 only to its *Scope*. Its tests read
`.python-version` and the `## Examples` section of a template. A missing section is reported as a
finding of the check's list, which is the exception WAY-344 gives for a check of form. A missing
`.python-version` makes the test fail, but with a misleading message (M4). Nothing reads an absence as
a pass.

## Searches not found or unclear

- WAY-328, named in the task's *Decisions in play*, is withdrawn on this base. The orchestrator says so
  (Q1), and WAY-379 and WAY-392 stand in its place in the index.
- Unclear: what WAY-44's "Tests belong to the part they test" asks of a test whose invariant names
  `repository`. That part has no directory, and WAY-09 gives it only configuration files (M3).
