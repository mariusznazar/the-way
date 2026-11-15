# Executor report — slice 18

**Status:** done

**Commits:** `38c1ff8` on branch `task/the-way-coding-and-testing-guidelines` — "Write the guidelines of the kinds check and shared-module and the guidelines directory in the part map" (base `f16616c`). The worktree is clean after the commit.

**One-line check result:** all three checks of the slice pass (`foundation_check.py` 0 errors, `git ls-files guidelines` lists both files, tracked-file-private-paths lists 0 hits); no check failed or was skipped.

**Report path:** `.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-18-report.md`

## Files changed

| File | Added | Removed | Note |
|---|---|---|---|
| `guidelines\coding-check.md` | 42 | 0 | new; kind `check` |
| `guidelines\coding-shared-module.md` | 40 | 0 | new; kind `shared-module` |
| `foundations\part_map.md` | 1 | 0 | line 173: `guidelines/**` added to the *Files* of `agent-instructions` (E40) |

Content of the two guideline files (the decisions and the statuses they hold):

- `coding-check.md`: *Applies to* `task-cycle · project-level · elements-common · instruction-files`; `## Files of this kind` lists 9 files, exactly those the Context of the task allocates to `check` (line 219 of `task.md`): `task-cycle/tracked_private_paths_check.py` `exemplar` WAY-386; `task-cycle/request_check.py` `do not copy`; the other seven `copy`. `## Rules` holds `none — WAY-386`. `## Examples` has one entry, "The rest of the exemplar". `## Where in code` lists `task-cycle/`, `project-level/`, `elements/common/`, `instruction-files/`.
- `coding-shared-module.md`: *Applies to* `relation-model`; `## Files of this kind` lists `relation-model/fingerprint.py` `exemplar` WAY-391; one rule "Importing runs nothing" with *Decision* WAY-391 and *Invariant* `shared-module-import-runs-nothing` (E27); one example; `## Where in code` lists `relation-model/`.

No value is copied from code or from a decision. No absolute path and no note link is written.

## Checks run

Commands run from `the root of the worktree`:

1. Baseline before any change: `python -B elements/common/foundation_check.py` → "0 errors", exit 0.
2. Baseline: `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` → "checked: 316 files, 0 listed", exit 0.
3. After the edits, before `git add`: `python -B elements/common/foundation_check.py` → `foundations/part_map.md:173: the pattern guidelines/** ... matches no file git tracks`, "1 error", exit 1. Expected: the check reads tracked files only, so the new files had to be staged first.
4. After `git add guidelines/coding-check.md guidelines/coding-shared-module.md foundations/part_map.md`:
   - `python -B elements/common/foundation_check.py` → "0 errors", exit 0 (the slice's first *Check*).
   - `git ls-files guidelines` → `guidelines/coding-check.md`, `guidelines/coding-shared-module.md`, exit 0 (the second *Check*).
   - `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` → "checked: 318 files, 0 listed", exit 0 (the third *Check*).
5. Own-work mutation (section 3): in `guidelines/coding-shared-module.md` the invariant name was changed to `shared-module-import-runs-something` for a moment, then `python -B elements/common/foundation_check.py` → "guidelines/coding-shared-module.md:21: `shared-module-import-runs-something` names no invariant", "1 error", exit 1. The file was restored from a backup copy and the check rerun → "0 errors", exit 0. `git status` showed the worktree clean; the file is identical to the staged version.

No test was written: the slice adds prose and a part-map line, and its *Checks* are the three above. No invariant test was changed. `<ruff>` was not run: no Python file changed. The product gate was not run (WAY-160).

## Own-work check (section 3)

- **Requirement most likely missed:** the status of each file in the two tables must match the Context's allocation, and the table must list every file of the kind the Context names. Check: compared the nine `check` rows and the one `shared-module` row with `task.md` lines 218–224; confirmed each path is tracked by `git ls-files`. Result: match; `check` has no file that carries a `do not copy` place other than `request_check.py`, so the other seven are `copy`.
- **Second requirement:** a rule's *Invariant* must name an entry the foundation holds. Check: the mutation run in check 5 shows the reference is checked; the real value `shared-module-import-runs-nothing` is accepted (check 4).
- **Weakest point:** the table statuses come from the Context of the task (the orchestrator's allocation), not from re-reading `.runs/coding/kinds_audit.md` (see Unread material). Check made: the Context list was counted per kind (9 for `check`, 1 for `shared-module`) against the rows written, and the `do not copy` file is the one the handoff names. The second weak point is the form of the *Good* and *Bad* lines (see choices).

## Choices made

1. **Good and Bad lines in `coding-shared-module.md`.** The coding template gives a rule *Good* and *Bad* as one line each or `none`. I wrote one line each. Way rejected: `none` for both. Cost if wrong: a reviewer who expects `none` has a single line to delete.
2. **Directories in `## Where in code`, with a trailing slash** (`task-cycle/` and so on). The template asks for paths git tracks; a directory holds tracked files, and `foundation_check.py` does not check this section. Way rejected: naming each file. Cost if wrong: the section drifts when a file is added, which the template allows for kinds.
3. **Statuses as backticked words** (`` `exemplar` ``, `` `copy` ``, `` `do not copy` ``), matching the form WAY-386 uses ("lists the file as `exemplar`"). Way rejected: plain words. Cost if wrong: none the check reads.
4. **One commit for the three files.** The part-map line and the first file it matches must land together, since `foundation_check.py` reports a pattern that matches no tracked file. Way rejected: two commits. Cost if wrong: an intermediate commit would fail the check.
5. **Language of the guideline text: English**, as the foundation entries and the handoff's commit rule give; the template leaves the language to the product.

No adaptation of section 4 of `make-change`. No changed invariant test.

## Questions

None.

## Concerns

- The *Description* of part `agent-instructions` in `foundations/part_map.md` does not name guidelines; WAY-09 places the guidelines of the-way's own code there, and the update-part-map steps do not require a change of the binding sentence for a *Files* change, so I did not change it. Named here for the orchestrator to judge.

## Working copies

- `.runs\executor-18\` — created for one backup copy of `guidelines/coding-shared-module.md` (check 5). The backup file was removed and then the directory was removed with `rmdir`. Nothing remains. No worktree was made; no screenshot was taken.

## Reaches beyond the handoff

- `elements\part-map\skill\write.md` — read whole; the method of `update-part-map` names it ("read `write.md` beside this skill" at step 4), and the handoff's method for the part-map line calls for that skill.
- `elements\common\foundation_check.py` — read lines 1–60 and 855–990, to learn how `guidelines/` files are read (*Applies to* and *Invariant*) and how a tracked pattern is matched. Not named by the handoff.
- `.ai\rules\git.md` (in the vault) — read, since the user's rules name it before a commit.

## Unread material

- `foundations\decisions.md`, WAY-09 (the E16 entry), lines 41–59 — not read; I read 11–40 and 60–89. The change of WAY-09 is already written; the slice does not edit it.
- `elements\common\way_of_working.md` — named by `update-part-map` (step 1, "Reading the foundation") and by `elements/part-map/skill/SKILL.md`; not read. The slice's change is one *Files* line in an existing part, which the part-map template's "Assigning files" covers.
- `elements/part-map/skill/decide_entry.md` — named by `update-part-map` step 2; not read, for the same reason: the entry is an existing part, not a new one.
- `.runs/coding/kinds_audit.md` (named by the Context of the task, not by the handoff) — not read; the statuses come from the Context of the task.
- `foundations/invariants.md` — the six invariants the handoff names were read whole (`repository-file-location`, `derived-file-content`, `ci-checking-commands`, `tracked-file-private-paths`, `guidelines-file-place`, `map-reference-target`); the Python-file invariants of the handoff (`script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation`) were not read, since the slice adds no Python file.
- Everything else the handoff names was read whole: `task.md` lines 28, 130–147, 218–224, 529–545; E8 (WAY-386 to WAY-391, lines 9925–10049); E27 (`shared-module-import-runs-nothing`, lines 478–486); `foundations/decisions.md` WAY-167, WAY-168, WAY-173, WAY-312, WAY-198, WAY-199; `product-guidelines/template.md`, `product-guidelines/coding/template.md`, `product-guidelines/reading.md`; `task-cycle/tracked_private_paths_check.py`; `relation-model/fingerprint.py`; `elements/part-map/skill/SKILL.md`; `elements/part-map/template.md`; `elements/common/rules.md`; and the plan's *Choices* and "Orchestrator's additions" (lines 1003–1041).

## Searches not found or unclear

- `write.md` was first looked for beside `elements/part-map/`; it is in `elements/part-map/skill/`. Found.
- The Context of the task (`task.md` line 144) reads "osiem miejsc w siedmiu plikach ma status `do not copy`" and lists the places with "ok. l." (approximately line). I read "ok." as "około" (about). Its list gives eight places in seven files, which matches the `do not copy` annotations. Not needed for my tables beyond `request_check.py`.
- The handoff's "E8 in its Decision cell" for `check` is six identifiers for six kinds; the `check` kind is WAY-386 (the handoff's table: WAY-386 to WAY-391 are E8, one per kind). Resolved by the decision's own title.
- The coding template does not say whether a directory in `## Where in code` may end in `/`. Used the trailing slash; no check reads this section.
