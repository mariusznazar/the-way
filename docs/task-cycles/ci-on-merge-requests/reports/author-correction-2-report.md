# Report: author, correction 2 (the human's answer (a) to the blocking item)

**Status:** done

## Commit

- `2e83447` Allow installation to depend on instruction-files and drop the debt record (on `9a00830`). Files by explicit path: `foundations/invariants.md` (-10), `foundations/part_map.md` (+2/-1). The commit message carries the citation of settlement 5.

## What was changed, place by place

1. `foundations/invariants.md`: the entry `installation-instruction-files-dependency` removed whole (heading, sentence, five fields). The file's tail is now as on the fork point `7f5c5a5` (`git diff 7f5c5a5 --stat -- foundations/invariants.md` is empty). No withdrawn identifier is written: `elements/common/rules.md` ("Withdrawn identifiers") keeps a withdrawn identifier only for one the file held on the commit the branch left the main branch from; this one was written on this branch (by my fix `dcb1a19`) and "never reached the main branch, so may go". The file keeps no list of withdrawn identifiers, and the invariants template adds nothing further for a removal.
2. `foundations/part_map.md`, part `installation`: `instruction-files` appended to *Depends on*, after `foundation-review`, in the file's own form (` ·` at the line end and the continuation indented two spaces). No other line changed.
3. References to the identifier or its sentence: `git grep -n "installation-instruction-files-dependency"` over the tracked files (`.runs/` excluded) finds none now; the sentence "does not depend on `instruction-files`" has no other place. In my own earlier report `author-fix-merge-report.md` the identifier stands as history of that fix, which is the cycle's record, not a tracked file.

## The citation of settlement 5

- Frozen task `.runs/task-cycles/ci-on-merge-requests/task.md`, line 120, row 5 of *Settlements to record*: "Jedno polecenie testów produktu uruchamia też `check_instructions.py`; błąd skryptu zatrzymuje testy, ostrzeżenie nie." Its *Goes to* column: "skill or instruction file: blok instalatora w `AGENTS.md` produktu (`installation/install.py`)", and it is tied to the human's answer at line 67 ("Tak. Zdanie instalatora o jednym poleceniu testów mówi, że polecenie uruchamia też `check_instructions.py`…").
- Written in the commit message, in English, with the line number. Does the map's own form call for a citation anywhere in the file? No. The template's form of a part (`elements/part-map/template.md`, "Form of an entry", "Part") holds *Files*, *Depends on* and *Trust boundary* and no field for a source; *Depends on* "names the parts this part may depend on, not those its code reaches for today". So the file holds none. I wrote no citation into the map.

## Dependency cycle and other errors of the map

- `instruction-files` already lists `installation` in its *Depends on* (`foundations/part_map.md`, part `instruction-files`), so the two parts now allow each other. I searched the part-map template, its skill and `elements/common/foundation_check.py` for a rule against a dependency cycle (`cycl`, `circular`, `acyclic`): none exists, and `foundation_check.py` reports 0 errors. The map's *Depends on* is an allowance, not an ordering of builds. I name the mutual allowance here so that a reviewer sees it; I did not change `instruction-files`.
- `elements/part-map/test_cross_part_imports.py` passes (39 tests of `elements/part-map`), so the allowance causes no import error.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`): `0 errors`, exit 0.
- `python -B gate/run_tests.py elements/part-map`: 39 tests OK, exit 0.
- `python -B gate/run_tests.py elements/common`: 235 tests OK, exit 0.
- Not run: the full gate (the orchestrator's). No other directory has a changed file (the change is in `foundations/` only, which holds no tests).
- Own-work check: the requirement most likely unmet is "nothing else changed and no reference left". Checks: `git diff --stat 9a00830 2e83447` lists the two files only; the invariants file equals its fork-point version; the `git grep` above finds no reference.

## Remark as made

- Remark 1 (a): both parts of its first sentence made. The rest of the remark (the comparison of the foundation with the code, the merge if the target moved, the wait for CI) is the orchestrator's and mine at the return step later; not done here.

## Reach beyond the handoff

`elements/common/rules.md` "Withdrawn identifiers" (lines 57-76): to decide whether the removed identifier needs a withdrawn entry. `elements/common/foundation_check.py` searched for a cycle rule (by word). Nothing else.

## Unread material

`elements/part-map/skill/SKILL.md` was read only at line 41 (the *Depends on* paragraph) and `elements/invariants/skill/SKILL.md` and its `template.md` were read whole earlier in this session, for the fix; WAY-225, WAY-51, the glossary entry "dependency of a part" and `template.md` "Allowed dependencies" likewise (earlier in this session). WAY-11 was not read whole. The decision index script and the part-map skill's other files were not used.

## Searches not found or unclear

- A rule against a dependency cycle between parts: not found (see above).
- A place in the map for a citation: not found (the form has no field).

## Working copies

None made (`.runs/author-correction-2/` was not created).
