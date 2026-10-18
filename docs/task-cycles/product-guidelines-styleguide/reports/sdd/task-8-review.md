# Task 8 review — the installer gives products the skill and names the form check

Range `04920a1..9dd9880` (commits `2b5bf31`, `9dd9880`); files `installation/install.py`,
`installation/README.md`, `installation/test_styleguide_installation.py` (new).

### Spec Compliance

✅ — with one ⚠️ that the plan sanctions.

- ✅ `SKILLS` holds `"maintain-styleguide": "product-guidelines/styleguide/SKILL.md"`
  (`installation/install.py:39`). So `plan()` writes both wrappers, `sibling_names()` names the
  skill in every wrapper, and `product_guidance()` lists `the-way-maintain-styleguide` among the
  other skills (spec §8, brief *Goal*).
- ✅ `product_guidance()` holds the sentence of spec §8 word for word, built from `SUBMODULE`
  (`installation/install.py:176-180`). Both commands are there: `python -B .the-way/product-guidelines/form_check.py`
  and its `--merge-onto <main commit>` form, with the condition "a file of `guidelines/` or of
  `foundations/` changed". It stands in the last paragraph, before "A check that did not run is
  never a pass."
- ✅ `installation/README.md:56` names `maintain-styleguide` in the `.claude/skills` row.
  `:58` names the form check in the `AGENTS.md` row, and `:131` names the new tests' subject.
- ✅ The new ordinary test file (no invariant citation) shows everything the brief's *Checks*
  list. A preview lists `CREATE` for both wrappers and writes nothing. After apply the two
  wrappers are byte-identical, carry the pinned commit and the source path
  `.the-way/product-guidelines/styleguide/SKILL.md`, and all 30 wrappers' sibling sentences name
  the skill. The block holds the sentence. Product files are preserved (CRLF), only `.gitmodules`
  and `.the-way` are staged, and a repeated run changes nothing. Both commands run from the
  product root and judge the product's own `guidelines/`. An earlier block without the sentence
  is refused before anything is written.
- ✅ WAY-03: `git diff --stat 96623ed..9dd9880 -- installation/test_install.py installation/test_installed_guidance.py installation/test_lead_installation.py`
  is empty.
- ✅ The `installation-command` surface (preview and confirmation, replaces no existing file,
  adds only the named additions) still holds. No code path of the installer changed: the diff
  adds one dictionary entry and one constant string. The promised additions are still the same
  three: the `.gitmodules` section, the `AGENTS.md` block and the `.runs/` line. The surface's
  wording is unchanged.
- ✅ WAY-107: `product_guidance()` takes no argument and reads no product input. The only paths
  in the new sentence are the-way's convention paths (`guidelines/`, `foundations/`,
  `.the-way/…`), which WAY-167 fixes for every product.
- ⚠️ Spec §8 and §10 say `installation/test_install.py` `NAMES` gains the skill. The brief and
  the orchestrator's ruling C25 keep that file unchanged (WAY-03), and the new file carries the
  coverage instead. `installation/test_lead_installation.py` already set this pattern for
  `lead-project`. Effect: the generic loops over `NAMES` in `test_install.py` skip this skill —
  the wrapper's "product case" sentence and the warning about ignored paths. Both come from
  shared code, so no behaviour goes untested for this skill alone. The whole-branch review should
  record the departure from the spec's letter. It is the plan's, not this task's.

### Review checks run (detached worktree `9dd9880`, removed afterwards)

- `python -B -m unittest installation/test_styleguide_installation.py`: exit 0, 3 OK. Output:
  `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\3c9695bb-97dd-4f98-b7ec-dff4bae7e82e\scratchpad\s8-new-tests.txt`.
- WAY-48, crafted product files run against the changed installer, preview and `--apply` each.
  Script: `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\3c9695bb-97dd-4f98-b7ec-dff4bae7e82e\scratchpad\s8_crafted.py`.
  Result: `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\3c9695bb-97dd-4f98-b7ec-dff4bae7e82e\scratchpad\s8-crafted.txt`.
  All 5 cases passed:
  1. A CRLF `AGENTS.md` (a `## Backlog` naming `docs/backlog/`, text after the block) holding the
     block without the new sentence: both runs exit 1 with "differs from this commit's guidance",
     no file changes, and no `.the-way` or `.gitmodules` is created.
  2. A CRLF `AGENTS.md` holding the current block in CRLF, with product text around it: the
     preview shows `KEEP AGENTS.md`, and the file is byte-identical after apply.
  3. A block the product edited to hold its own path (`docs/backlog/`): refused before writing
     (WAY-107 from the product's side).
  4. A conflicting `.agents/skills/the-way-maintain-styleguide/SKILL.md`: refused with "Existing
     integration file differs", nothing written.
  5. A non-UTF-8 `guidelines/styleguide-web.md`: the installer neither reads nor changes it. The
     install succeeds, and the CRLF `AGENTS.md` gets the block in CRLF.
- I checked the report's evidence without re-running the suites. The final record
  `.runs/task-cycles/product-guidelines-styleguide/reports/slice-8-final-checks.json` lists all
  20 commands with exit 0. `slice-8-final-tests-installation.txt` shows 33 OK, written after the
  commit time of `9dd9880`. `slice-8-red.txt` shows 3 failures before the change, and
  `slice-8-weakest-point.txt` holds the control described below.

### Weakest-point check (WAY-164)

**Well chosen and decisive.** The requirement it picked is the one a green test could most easily
pass while unmet: the commands the guidance names, run as written from the product root, must
judge the product's `guidelines/` and not the-way's own. The first version of test 2 asserted
only "exit 0 with a `note:`" in a product without guidelines. That would also pass if the command
checked the-way's root, which holds no guidelines either. The executor showed this with a control
(the same command on the-way's root exits 0, "holds no guidelines/"). The broken-file case then
went into the test (`9dd9880`, `installation/test_styleguide_installation.py:138-147`): both
commands must exit 1 and name `guidelines/styleguide-web.md:0: error: the header line *Discipline* is missing`.
The evidence records the method, the actor, what was observed and the control.

### Sharpness inputs

**Accurate.** Parts touched: `installation` only. Every changed file is under `installation/**`,
and the part's *Depends on* already names `product-guidelines`. Trust-boundary file:
`installation/install.py`, with a correct description of the change (no new read, no new write
path, no new subprocess). Irreversible: nothing. The report names the change of the `pinned`
promise level correctly: a product moving its pin gets the refusal on its old block, and the
request should carry that line (spec §8).

### Strengths

- The smallest possible change to a trust boundary: no logic changed, so the existing 30 tests
  and the unchanged refusal and append code still govern every product file.
- The new tests use crafted CRLF product files and hold the block's text against product-chosen
  paths (`installation/test_styleguide_installation.py:102`). The tests 1–3 give this skill the
  three outcomes a product can meet: a fresh install, a repeated run, and the pin move that is
  refused.
- Test 3 models the pin-move route in `installation/README.md` faithfully: same pin, wrappers
  removed, old block kept. The block refusal comes first, as `plan()` orders it.
- The red state was recorded with each failure caused by the missing feature. The concerns
  section openly names the spec's `NAMES` departure and the placeholder `<main commit>`.

### Issues

**Critical:** none.

**Important:** none.

**Minor:**

1. `installation/test_styleguide_installation.py:90` — `self.assertEqual(len(siblings), 30)`
   hard-codes the total number of the-way's skills.
   - *Why:* the next task that adds any skill breaks this test for a reason that has nothing to
     do with the styleguide. Neither `test_install.py` nor `test_lead_installation.py` counts
     wrappers.
   - *Fix:* assert the set of wrapper directories instead, e.g. compare it with
     `{f"the-way-{n}" for n in install.SKILLS}` for each tool directory. Or drop the count and
     keep the per-sibling regex, with a check that the list is not empty.
2. `installation/install.py:158` against `:176-178` — the same block says "always name this
   repository's file or directory", and the new form-check commands name no `ROOT`.
   - *Why:* the commands are correct as written: `ROOT` defaults to the working directory, and a
     run outside the root exits 2. But an agent reading the block meets a rule and two commands
     that seem to break it. The wording is spec §8's, word for word, so this is not this task's
     defect. It is not a defect that makes the task untrustworthy either, so it stays Minor.
   - *Fix (spec-level, for the whole-branch review):* either accept it as is, or let the spec
     name `.` as `ROOT` in both commands. Any wording change also changes the block, which every
     installed product would then have to remove.

**Observation outside this task's scope (for the whole-branch review):**
`slice-8-weakest-point.txt:724-732` shows that `form_check.py --merge-onto <commit>` prints the
run report's `0 error(s), 0 warning(s), 0 unchecked` before a file's errors and its own
`6 error(s)` line. An agent that reads the first summary line could take the run as clean. This
is the output shape of the form check (slices 2–3), not of the installer.

### Assessment

**Task quality:** Approved.

Both of the task's requirements are met: the skill entry in `SKILLS` and the guidance sentence,
which is spec §8's word for word. The README names the skill. The new ordinary test file shows
the whole route: preview, apply, repeat, the byte-identical wrappers, the pinned source, the
sibling sentences, the sentence in the block, the commands judging the product's own guidelines,
and an earlier block refused before writing. The WAY-03 files are unchanged.

The trust boundary did not widen. The change is one constant entry and one constant sentence,
and five crafted product inputs behave as the `installation-command` surface promises: CRLF old
and current blocks, a block the product edited to hold its own path, a conflicting wrapper, and a
non-UTF-8 guidelines file. No product-chosen path can enter the block.

The weakest-point check found the real gap in the first test and closed it with a control. Both
Minor issues are optional: a brittle hard-coded count, and a wording tension that comes from the
spec.
