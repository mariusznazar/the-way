# Report: author, correction 2, second part

**Status:** done

## Commit

- `0e3cb2a` Allow agent-instructions to depend on repository (on the merge `cde07dd`). One file by explicit path: `foundations/part_map.md` (+1/-1). The human's answer is cited in the commit message (the comment URL `https://github.com/mariusznazar/the-way/pull/127#issuecomment-6893500004`, 2026-11-15, item 1; the map has no field for a citation).

## What was changed

- `foundations/part_map.md`, part `agent-instructions`: `repository` appended to *Depends on* after `process-audit`, in the file's own form. Nothing else. The part `repository` is the one whose *Files* hold `/.python-version` (read by `.github/workflows/tests.yml:41`, a file of `agent-instructions`) and its own *Depends on* is `none`, so the allowance makes no mutual dependency and no cycle.
- Remark item 2 (the two prose mentions in `installation/README.md`): no change, as the answer says; `installation/README.md` untouched.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`): `0 errors`, exit 0.
- `python -B gate/run_tests.py elements/part-map`: 40 tests OK, exit 0 (the merge brought one more test than the 39 before it).
- `python -B gate/run_tests.py elements/common`: 242 tests OK, exit 0.
- Not run: the full gate (the orchestrator's).
- Own-work check: the requirement most likely unmet is "no other change and no map error". Checks: `git diff --stat` before the commit listed the one file with one line; the checker and the import test of parts (`test_cross_part_imports.py`, in `elements/part-map`) pass with the allowance.

## Reach beyond the handoff

None beyond the files the handoff names (the *Depends on* lines of `agent-instructions` and `repository` read in `foundations/part_map.md`; the answer in `reports/correction-2-remarks.md`).

## Unread material

WAY-225, the glossary entry "dependency of a part" and `elements/part-map/template.md` "Allowed dependencies" were not read again in this run; I read them whole earlier in this session (for correction 2 and its return step) and apply the same rule as for `instruction-files`.

## Searches not found or unclear

none

## Working copies

None made (`.runs/author-correction-2b/` was not created).
