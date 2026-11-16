PASS 2e31b74b1a0dd3c9c787ed79a025bb7f372615a6

# Review of the merge of the target branch into the task branch (correction 2)

- Range: `git diff 7ef5b13 2e31b74b`; merge commit `2e31b74b` with parents `7ef5b13d` (task branch)
  and `30c947f6` (`foundations`, merge of PR #140). `git rev-parse HEAD` of the reviewed worktree was
  `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6`, the head given.
- Question: do the two sides still hold together? Answer: yes. No blocking finding.

## How the merge was read

- `git show --cc 2e31b74b` for the three conflicted files, and `git show --remerge-diff 2e31b74b`:
  the resolution differs from git's automatic merge only inside the three conflict hunks named in
  the handoff, and nowhere else. Every other file is git's automatic merge.
- Each side's contribution: `git diff 7ef5b13...30c947f` (target) and `git diff 30c947f...7ef5b13`
  (task), for `process-audit/`, the cycle's skill texts, `task-cycle/record_template.md` and
  `foundations/decisions.md`.

## Findings

### Blocking

None.

### Minor

1. `process-audit/audit_count.py:342-349` — the two sibling modules are imported on either side of
   `sys.path.insert(...)`: `from stage_pricing import ...` (the target's placement) comes before the
   line that adds `task-cycle/` to the path, `from record_items import ...` (the task's) after it,
   after `import remarks_check`. Both resolve from the script's own directory, so behaviour is the
   same and the tests pass. But a reader may conclude that `record_items` needs the `task-cycle/`
   path entry and `stage_pricing` does not. That is true of neither import: `record_items.py:31` adds
   that path itself. Grouping the two sibling imports together would remove the misreading. This is
   polish, within the task (the placement came out of this merge).

## The conflicted files

- `process-audit/audit_count.py`: both constant blocks are gone. `NO_MODEL` and `ORCHESTRATOR` are
  now defined only in `stage_pricing.py:13-14`, and `REPORT_FILE`, `ROUNDS_LABEL` and `ROUND_ENTRY`
  only in `record_items.py:38-44`. The automatic part of the merge also removed `UNKNOWN` and
  `MILLION` from `audit_count.py`, and both are defined in `stage_pricing.py`. A walk of each module's
  syntax tree (script `.runs/review-merge/names.py`, since removed) found:
  - in `audit_count.py`, no module-level name defined twice (the one hit, `sys`, is
    `sys.dont_write_bytecode = True`, a false positive of the script);
  - no imported name unused, apart from `from __future__ import annotations`;
  - no name that is loaded and never bound, apart from `__file__`.

  Every name imported from `stage_pricing` (`NO_MODEL, TEXT_CAP, UNKNOWN, ModelPrice, Prices,
  StageTokens, is_orchestrator_row, priced, priced_older`) and from `record_items` is used. No test
  reaches `audit_count.ORCHESTRATOR`, `.MILLION`, `.NO_MODEL`, `.ROUND_ENTRY`, `.REPORT_FILE` or
  `.ROUNDS_LABEL` (a search of `process-audit/` found none). `record_items.py` and `stage_pricing.py`
  define no constant in common.
- `process-audit/test_audit_count.py:3271-3273`: the tuple of files copied into the built checkout
  holds `audit_count.py`, `record_items.py`, `stage_pricing.py`, `price_list.md` and
  `task-cycle/remarks_check.py`, which covers every module `audit_count.py` imports. The `Run` tests
  that use it pass.
- `task-cycle/skill/correction.md:43-50`: one sentence carries the task's discard wording ("its
  reason written under *Discarded attempt* ... (WAY-405)"). The next carries the target's gate
  wording: "run the gate on the corrected tree on your own system as step 10 gives its local run,
  where CI does not run on the request and so is not its final gate". Both are word for word as each
  side wrote them, and the paragraph reads as one. The target's later paragraph on the wait for CI
  (`correction.md:59-69`) is intact.

## The automatically merged files

- `task-cycle/skill/SKILL.md`: the task's edits are at lines 221-235 (the findings file carries the
  reviewer's mark; *Review rounds* says `yes`/`no`, WAY-404) and lines 382-394 (a discard written
  under *Discarded attempt* with its reason, WAY-405). The target's edits, on CI as the final gate,
  are at steps 2, 4, 9.4, 10 and 12. No sentence of the task speaks of where the gate runs. The
  target's step 12 still has "a fresh reviewer review the merge with `review-change`". That review
  passed with no fix, so the task's new second form of a *Review rounds* entry (`review
  `reports/<file>.md`, PASS`) gives it a place, and no conflict follows.
- `task-cycle/record_template.md`: the task changed *Discarded attempt* and *Review rounds*. The
  target changed the paragraph on `gate_times.md` and the paragraph on the final gate in
  *Verification*. These are separate places, and none of these items refers to another.
- `task-cycle/skill/reserved_return.md`: the task's discard sentence is at line 35. The target's "no
  gate runs on your own system either" is at line 71. They are independent.
- `process-audit/SKILL.md`: the task's sentence on a record that lacks a line or item it reads
  (WAY-344) and its Q1 paragraph (WAY-404) stand beside the target's sentence that a copy with no
  `gate_times.md` may be of a cycle whose final gate ran in CI (lines 204-207). None of them
  contradicts another.
- `process-audit/audit_count.py`: the target added `ABSENCE_CAUSES` and the docstring sentence on CI,
  and the task added the reading of the record's items. The target's side adds no new reading of the
  record, since `ABSENCE_CAUSES` concerns copies of files, not record items. So the task's list in
  WAY-344 of the lines and items the count reads of a record (`Process pin`, `Target branch and
  base`, *Process remarks on the-way*, *Discarded attempt*, *Review rounds*, *Plan*, *Slices
  returned too large*) is still complete.

## The foundation entries

I mapped the merge's hunks of `foundations/decisions.md` to their entries with
`.runs/review-merge/hunks.py` (since removed). Of the entries the target changed, these bear on
`process-audit`, `task-cycle` or the decision log: WAY-16, WAY-160, WAY-148, WAY-162, WAY-164 and
WAY-256. I read each changed hunk. Against the task's WAY-337 (changed), WAY-344 (changed), WAY-404
and WAY-405 (new):

- WAY-160 (the final gate is CI's run where CI runs on the request; a local run otherwise) and WAY-16
  (CI on every system the product runs on). The task's entries say nothing about where or how the
  gate runs, so neither contradicts them.
- WAY-162 (a reverted Minor fix "has the gate run ... as WAY-160 gives"), WAY-148 (a source added
  under WAY-100) and WAY-164 (its *Based on* filled). None touches review marks, record items or the
  audit's reading of them.
- WAY-404 places the mark on blocking findings of a code review, the merge review included. WAY-160
  and step 12 keep the merge review, so the mark has a place in every review the target's flow still
  runs.
- WAY-337's added paragraph (an entry for a review that passed with no fix is no fix round) is
  untouched by the target.

The entries on the handoff's list that do not appear among the merge's hunks are WAY-261 and
WAY-161. In the merged file I found them referenced only from passages the target changed (WAY-160
cites WAY-261; the context of WAY-162 cites WAY-161), and their own text did not change in this
range.

## Declined to judge

- `foundations/part_map.md:134-135`, the trust boundary of `process-audit`, lists `audit_count.py`
  and `record_items.py` but not `stage_pricing.py`. `stage_pricing.py` came from the target side,
  and whether it belongs at the boundary was the target's own change, reviewed in PR #140, not a
  question of the two sides holding together.
- The rest of the target's changes to `foundations/decisions.md` (WAY-100, WAY-121, WAY-138,
  WAY-139, WAY-142 to WAY-147, WAY-165, WAY-167, WAY-199, WAY-203, WAY-206, WAY-212, WAY-228,
  WAY-233, WAY-236, WAY-237, WAY-268, WAY-270, WAY-273, WAY-280, WAY-374, WAY-381). They concern
  parts the task does not touch: project-level, technology, guidelines and tests of products.
- `.github/workflows/tests.yml`, `agent-instructions/README.md`, `installation/README.md` and the
  target's test edits in `project-level/` and `task-cycle/`. All are target-only, and I checked them
  only by running their tests.

## Checks

All were run in a detached worktree of `2e31b74b` at
`.runs/review-merge/wt`:

- `python -B gate/run_tests.py process-audit` — exit 0; 270 tests, OK.
- `python -B gate/run_tests.py task-cycle` — exit 0; 534 tests, OK, 2 skipped (one is the target's
  `skipIf(os.name == "nt")` test of a bar in a file name).
- `python -B gate/run_tests.py project-level` — exit 0; 279 tests, OK. The merge changed
  `project-level/test_plan_state.py` and `test_plan_state_invariant.py`.
- `python -B gate/run_tests.py agent-instructions` — exit 0; 37 tests, OK (2 expected failures).
  The merge changed `agent-instructions/README.md`.
- `python -B gate/run_tests.py installation` — exit 0; 62 tests, OK. The merge changed
  `installation/README.md`.
- `python -B elements/common/foundation_check.py` — exit 0; `0 errors`.
- Manual: a walk of the syntax trees of `audit_count.py`, `record_items.py` and `stage_pricing.py`
  for names defined twice, imported and unused, or loaded and never bound. Result as above.
- Manual: `git show --remerge-diff 2e31b74b`. Only the three conflict hunks differ from the
  automatic merge.
- Not run: the product's full gate, as the handoff directs.

## Reaches beyond the dispatch

- `guidelines/coding-shared-module.md`, read whole. The target extended its *Applies to* to
  `process-audit`, so the guideline now also reaches the task's `record_items.py`. Its one rule,
  "Importing runs nothing" (WAY-391), holds for `record_items.py`: its top level only defines
  constants and functions, puts `task-cycle/` on `sys.path` and imports `remarks_check`. It reads no
  input and writes no output. The invariant `shared-module-import-runs-nothing` is tested only on
  `relation-model/fingerprint.py` (`relation-model/test_fingerprint.py:122`), so neither new module
  is under its test. That was so on both sides before the merge and is not a matter of the merge.
- `foundations/part_map.md`, entry `process-audit`, to see whether the task's listed files and the
  target's new module sit together (see Declined to judge).
- The frozen task, `.runs/task-cycles/audit-answers-contradiction-after-code/task.md`, searched for
  `gate`, `CI`, `stage_pricing` and `audit_count`. Line 74 relies on the list of paths that starts a
  new series (`COUNT_PATHS`, `audit_count.py:429`), and neither side changed it.

## Working copies

- A worktree of `2e31b74b` at
  `.runs/review-merge/wt`. Beside
  it, in `.runs\review-merge\`, were the logs of the checks, the scripts `names.py` and `hunks.py`,
  and the diffs of each side. All of it is removed before return: the worktree with
  `git worktree remove --force`, then `git worktree prune`, then the directory itself. Nothing is
  kept in `reports/` besides this report.

## Unread material

- `foundations/decisions.md`: of the target's changes, I read the hunks of WAY-16, WAY-160, WAY-148,
  WAY-162 and WAY-164 whole as diffs, but did not read the entries whole outside those hunks. I read
  the task's WAY-337, WAY-344, WAY-404 and WAY-405 hunks whole. The hunks of the entries under
  Declined to judge I did not read.
- I read the target's diff of `task-cycle/skill/SKILL.md` and `task-cycle/record_template.md` as
  hunks, not the whole merged files.

## Searches not found or unclear

- The handoff names WAY-261 and WAY-161 among the entries the target changed. The range
  `7ef5b13..2e31b74b` holds no hunk inside either entry. Both are referenced from changed passages
  (WAY-160 and the context of WAY-162).
