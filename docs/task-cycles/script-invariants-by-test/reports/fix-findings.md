# Findings for the fix — Minor findings of the review of the whole change (within the task)

Cut word for word from `reports/review-whole-report.md` (`PASS 4bc1667c`). No blocking finding. The reviewer marks each as within the task and none as outside the scope.

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
