# Slice 11 report — the installer gives products the skill

**Status:** DONE_WITH_CONCERNS (one recorded concern, C37; nothing failing that this slice owns).
**Commit:** `2eabf42` on `claude/gallant-albattani-3k15lc`, parent `8901da0` (BASE). Not pushed.
**Python:** 3.13.16 (`python3`); the repository declares 3.14 (O3), so 3.14-only behaviour is unchecked.

All outputs are in `docs/task-cycles/coding-guidelines/reports/sdd/`. Each file
ends with its exit line.

## Pre-start question (resolved)

I first returned NEEDS_CONTEXT with no code. `installation/test_styleguide_installation.py:92` hard-coded
30 wrappers (15 `SKILLS` × 2), and the new entry makes 32. Rulings: **C36**: change it to 32, with the
file added to the change list. **C37**: for the non-UTF-8 case, assert exit ≠ 0 and nothing written, and
record the traceback as a concern. Both are applied below.

## What I implemented

- `installation/install.py`: `SKILLS` gains `"maintain-coding-guidelines": "product-guidelines/coding/SKILL.md"`
  (+1 line). No other text of the installer changed, so the `installation-command` surface keeps its
  wording. Every wrapper's sibling sentence and the `AGENTS.md` block's "Use the project skills …"
  sentence now also name the skill, because both are built from `SKILLS` (spec §6.5).
- `installation/README.md`: the table row for `.claude/skills/the-way-*/SKILL.md` names
  `maintain-coding-guidelines`. The list of what the tests check names its entry points and the refusal
  of a conflicting file, a directory or a non-UTF-8 file at their path in either skill directory.
- `installation/test_coding_guidelines_installation.py` (new ordinary test, cites no invariant, follows
  the pattern of `test_styleguide_installation.py`):
  - `test_preview_apply_repeat_exposes_the_coding_guidelines_skill_and_preserves_product` covers this
    sequence:
    1. The preview lists `CREATE` for both wrappers and writes nothing: no `.the-way` and no `.gitmodules`.
    2. Apply. Both wrappers are byte-identical.
    3. The frontmatter is the name plus the source description followed by "Use this product's pinned
       the-way commit."
    4. The pinned commit and the source path `.the-way/product-guidelines/coding/SKILL.md` appear in
       both its sentences.
    5. There are 32 wrappers, and every one's sibling sentence names `maintain-coding-guidelines`.
    6. The block's "Use the project skills …" sentence names `the-way-maintain-coding-guidelines`, and
       the block holds no product path.
    7. The product files survive byte for byte, `guidelines/coding.md` included. `.gitignore` is
       appended only.
    8. The gitlink is at HEAD, and only `.gitmodules` and `.the-way` are staged.
    9. A repeat run reports "Already installed; no changes" and leaves every file unchanged.
  - `test_crafted_entry_at_the_new_wrapper_path_stops_the_run_before_writing` (WAY-48) has 12 subtests:
    `.claude` or `.agents` × a conflicting file, a directory, or a non-UTF-8 file (`\xff\xfe…`) at
    `<dir>/skills/the-way-maintain-coding-guidelines/SKILL.md` × preview or `--apply` (answer `y`).
    Each subtest checks:
    - exit ≠ 0 and no "Installed.";
    - the whole tree outside `.git` is unchanged, directories included;
    - the index is empty.
    The conflicting-file and directory cases also check that stderr carries "Existing integration file
    differs" and names the directory and the wrapper. The non-UTF-8 case checks only the exit and the
    unchanged tree (C37).
- `installation/test_styleguide_installation.py:92`: 30 → 32 (C36).

## TDD evidence

- **RED, new file** (uncommitted test, installer at BASE):
  `python3 -B -m unittest installation.test_coding_guidelines_installation` → exit 1,
  `FAILED (failures=13)` (`slice-11-red-new-test.txt`).
  - The first test fails on `'CREATE .claude/skills/the-way-maintain-coding-guidelines/SKILL.md\n' not
    found in 'Product: …'` because the preview from the committed checkout lists no such wrapper.
  - All 12 crafted subtests fail on `AssertionError: 0 == 0`: without the entry, the installer ignores
    the crafted path and succeeds.
- **RED, suite**: `python3 -B gate/run_tests.py installation` → exit 1, 35 tests, `failures=16`
  (`slice-11-red-installation.txt`): the 13 above plus 3 of the 4 F4 `NAMES` tests
  (`test_preview_apply_rerun_and_preserve_foundation`, `test_guidance_names_no_commit_and_covers_the_product_rules`,
  `test_warns_before_writing_paths_git_ignores`). The fourth,
  `test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies`, passed at BASE. It was an
  error at F4 only because the skill was not yet committed (S6 committed it), and it reads the skill
  file, not `SKILLS`.
- **GREEN** after the edits (uncommitted): `python3 -B gate/run_tests.py installation` → exit 0, 35 OK
  (`slice-11-green-installation-uncommitted.txt`). After the commit, every check was run again from the
  committed checkout (below). All four F4 `NAMES` tests pass: `slice-11-names-tests.txt`, which records
  `python3 -B -m unittest -v installation.test_install` (22 OK). Its trailing `exit 0` line is grep's
  exit; the run's result is the `OK` line.

## Final check set (from the committed checkout, `2eabf42`)

Summary with exit codes: `slice-11-summary.txt`.

| Check | Exit | Result | Output |
|---|---|---|---|
| `python3 -B gate/run_tests.py gate --record .runs/s11-tests-gate.jsonl` | 0 | 98 OK | `slice-11-tests-gate.txt` |
| `… elements/decisions` | 0 | 169 OK | `slice-11-tests-elements-decisions.txt` |
| `… elements/invariants` | 0 | 233 OK | `slice-11-tests-elements-invariants.txt` |
| `… elements/glossary` | 0 | 204 OK | `slice-11-tests-elements-glossary.txt` |
| `… elements/part-map` | 0 | 162 OK | `slice-11-tests-elements-part-map.txt` |
| `… elements/environment-facts` | 0 | 165 OK | `slice-11-tests-elements-environment-facts.txt` |
| `… relation-model` | 0 | 19 OK | `slice-11-tests-relation-model.txt` |
| `… agent-instructions` | 0 | 18 OK | `slice-11-tests-agent-instructions.txt` |
| `… installation` | 0 | 35 OK | `slice-11-tests-installation.txt` |
| `… instruction-files` | 1 | 104 run, 3 failures, 10 skipped: the same 3 failures as the BASE baseline (`diff` of FAIL lines against `reports/baseline-tests-instruction-files.txt` is empty) | `slice-11-tests-instruction-files.txt` |
| `… task-cycle` | 0 | 41 OK | `slice-11-tests-task-cycle.txt` |
| `… project-level` | 0 | 250 OK | `slice-11-tests-project-level.txt` |
| `… product-guidelines` | 0 | 137 OK | `slice-11-tests-product-guidelines.txt` |
| `python3 -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 27 warnings, 5 unchecked | `slice-11-guard-decisions.txt` |
| `python3 -B elements/invariants/format_guard.py --base none --merge-onto none` | 0 | 0/0, 3 unchecked | `slice-11-guard-invariants.txt` |
| `python3 -B elements/glossary/format_guard.py --base none --merge-onto none` | 0 | 0/0, 5 unchecked | `slice-11-guard-glossary.txt` |
| `python3 -B elements/environment-facts/format_guard.py --base none --merge-onto none` | 0 | 0/0, 3 unchecked | `slice-11-guard-environment-facts.txt` |
| `python3 -B elements/part-map/format_guard.py --base none --record .runs/s11-part-map-guard.jsonl` (takes no `--merge-onto`) | 0 | 0/0, 7 unchecked | `slice-11-guard-part-map.txt` |
| `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | 0/0/0; note: no `guidelines/` in the-way; reference check not run without `--merge-onto` | `slice-11-form-check.txt` |
| `python3 -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl` | 0 | 0/0, 1 unchecked | `slice-11-form-check-reference.txt` |
| `python3 -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" | `slice-11-skill-entry-points.txt` |
| `git diff --check 235b0b4..HEAD` | 0 | no output | `slice-11-diff-check.txt` |

The 27 decision warnings are the ones F1b recorded (5 old dates, 22 placeholders), not from this slice.

### Failed checks (by name)

`instruction-files`. The 3 failures were also present at BASE and fail because of the platform (Windows network path and macOS `/net` tests on Linux):
- `CommandLine.test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup`: 2 subtests (`\\192.0.2.1\share\x.md` forms)
- `NetworkShapesOffWindows.test_net_and_network_are_mount_points_of_macos_only`

### Unchecked lines (every one, by name)

- **decisions guard:**
  - the lines the log holds on the main branch, and the versions it gains per number (`--base none`)
  - a change to the template without a new version in the log (`--base none`)
  - `TODO` in the log (`--merge-onto none`)
  - the copies of a version both logs hold (`--merge-onto none`)
  - the fingerprints relations carry (`--merge-onto none`)
- **invariants guard:**
  - identifiers, versions, corrections and the list of violated invariants (`--base none`)
  - `TODO` in the entries (`--merge-onto none`)
  - the fingerprints the links of the entries carry (`--merge-onto none`)
- **glossary guard:**
  - the count of the words of *Avoid* (`--base none`)
  - terms and identifiers that came to read alike (`--base none`)
  - the uses of every term whose definition changed (`--base none`)
  - `TODO` in the entries (`--merge-onto none`)
  - the terms with no use after the merge (`--merge-onto none`)
- **environment-facts guard:**
  - identifiers and versions (`--base none`)
  - the fingerprints decisions carry for facts (`--merge-onto none`)
  - the facts nothing names after the merge (`--merge-onto none`)
- **part-map guard:**
  - the list of parts of `wording-reaches-dependants` (its test leaves no coverage file)
  - the list of parts of `skills-reach-the-way-sessions` (its test leaves no coverage file)
  - the change path of every promise level in use (no command reports the levels)
  - the dependencies between parts, and new or stale violations (no dependency graph command)
  - the list of known violations (`--base none`)
  - the identifiers of the map (`--base none`)
  - the lowering of a part's computed criticality (`--base none`)
- **form check, `--merge-onto none`:** the references in the foundation a merge leaves
  (`guidelines-reference-current/1`). Without `--merge-onto`, the reference check does not run (note
  line).
- **instruction-files:** 10 tests skipped because "network paths are looked up only on Windows". This is
  unchecked on Linux and was the same at BASE.
- **Not checkable here:** Python 3.14 behaviour (O3). A symlink at the new wrapper's path was not
  tested, following the README's existing reason: on Windows, creating a symlink needs extra rights.
  The installer refuses it through the same `is_symlink()` check.

## Weakest point (WAY-164)

- **Requirement most likely unmet:** a product's agent reaches and can follow the skill through its new
  wrapper. Against the task (an installed product, e.g. `loop2`, gets the new skill's entry), the
  tests show the wrapper names `.the-way/product-guidelines/coding/SKILL.md`. They do not show that the
  file and the the-way files it references exist in the product's pinned checkout.
- **Check (manual, run by me, the executor):**
  1. Installed `2eabf42` into a fresh product with `--apply`.
  2. Compared the product's `.the-way/product-guidelines/coding/SKILL.md` with the source.
  3. Resolved every backticked `.md`/`.py` path the skill names inside `.the-way`.
  4. Read the wrapper.
- **Observed:**
  - The installation succeeded, and the skill in the submodule is byte-identical to the source.
  - Every path that belongs to the-way resolves under `.the-way/`:
    - `product-guidelines/coding/template.md`
    - `product-guidelines/template.md`
    - `elements/common/critique/SKILL.md`
    - `elements/common/way_of_working.md`
    - `project-level/task/skill/SKILL.md`
    - `project-level/task/template.md`
    - `installation/README.md`
    - `AGENTS.md`
  - Three paths were reported absent, and none is a fault:
    - Two already carry the `.the-way/` prefix, so the script doubled it; they resolve from the product root.
    - `guidelines/coding.md` is the product's own file, which the skill writes.
  - The skill states where the-way lies in a product ("the product's pinned `.the-way`", line 20), and
    the wrapper's product-case sentence matches it.
  - The wrapper's sibling sentence names all 16 skills.
- **Evidence:** `slice-11-weakest.txt`. The requirement is met.

## Sharpness inputs (from the actual diff `8901da0..2eabf42`)

`git diff --numstat 8901da0..HEAD`:

| Added | Removed | File |
|---|---|---|
| 4 | 2 | `installation/README.md` |
| 1 | 0 | `installation/install.py` |
| 164 | 0 | `installation/test_coding_guidelines_installation.py` |
| 1 | 1 | `installation/test_styleguide_installation.py` |

- **Parts touched** (`foundations/part_map.md`): `installation` only (`installation/**`). The surface
  `installation-command` (declared at `installation/install.py` · run) keeps its wording. What it writes
  in a product changes in content: two more wrappers, the sibling sentence in every wrapper, and the
  block's skill list. As spec §6.5 says, a product moving its pin must remove the old block first.
- **Trust-boundary files touched:** `installation/install.py` (WAY-48). One dict entry, no parsing.
  The crafted-input tests are above.
- **Irreversible operations:** none. One local commit, not pushed. The tests write only to temporary
  directories.

## Choices settled (how to make what is settled)

- The crafted-input test builds a fresh product per subtest and compares the whole tree, directories
  included. A plain file snapshot would miss a created directory.
- The refusal message is asserted to name the directory and the wrapper name separately, not as one
  path with `/`. The installer prints an OS path, and on Windows the separator is `\`.
- The README's test list adds the new entry points and their refusals. "Every refusal happens before
  anything is written" already stands in the README.

## Self-review

- The diff matches the brief, plus C36. No other installer text changed. `test_install.py` and the
  foundation were not touched.
- The test expectations are literals or come from the input. The source description is read from the
  committed skill, which is an input, not the code under test. The count of 32 is a literal.
- Each subtest of the crafted test went red for the intended reason (the installer accepted the path)
  before the entry existed.

## Concerns

1. **C37, pre-existing, for the request and a separate task:** a non-UTF-8 file at any wrapper path
   stops the installer with an uncaught `UnicodeDecodeError` traceback (exit 1), not an `Error:` line.
   `plan()` reads `path.read_text(encoding="utf-8")`, and `run()` catches only `RuntimeError, OSError,
   EOFError`. Nothing is written, since the plan precedes every write. Manual evidence:
   `slice-11-nonutf8-manual.txt`.
2. **C32, still open:** `installation/test_install.py` `NAMES` still lacks `lead-project` and
   `maintain-styleguide`. This is pre-existing and was left alone, as ruled.
