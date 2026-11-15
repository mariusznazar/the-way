PASS cf4fe175b01d0efb362c7ffad5e3089ebbf28695

# Review of correction 1, task `scripts-after-foundation-review`

Range `3145e4f650a81fdbfa831092b2ea77c3ccc66b20..cf4fe175b01d0efb362c7ffad5e3089ebbf28695` (one commit, `cf4fe17`). `git rev-parse HEAD` in the worktree: `cf4fe175b01d0efb362c7ffad5e3089ebbf28695`, as given. The diff touches two files: `foundations/invariants.md` (1 line) and `process-audit/test_audit_series_scripts.py`.

Counts: blocking 0, Minor 1, out of scope 0.

## The remark, as made or not

- **Item 4 (add the cost script to the rule and its test): made.**
  - The sentence of `audit-series-script-paths` (`foundations/invariants.md:400`) now says the new series start "of the cost of cycles, of the measures ... or of the gate times" and names "the script that measures the cost, `task-cycle/cycle_stages.py`". Method, Rests on, Derives from, Part and Violated are untouched (the diff holds only that one line).
  - The test (`process-audit/test_audit_series_scripts.py`) adds `audit_count.COST_SCRIPT` to the paths checked as tracked by git. Its second test now compares the union of the paths of `audit_count.TOOL_GROUPS` (the audit's own list of what it splits by, `audit_count.py:505`) with the four named paths. The second test is renamed (`..._the_two_series` to `..._the_series`); `grep` over the tree showed no other citation, per the author's report, and the foundation check passes.
- Items 1 to 3, 5, 6 (let through) and 7 to 13 (accepted): the diff touches none of them. `process-audit/test_audit_count.py` and `audit_count.py` are untouched.

## Judgement

- **The sentence and its test agree.** Four paths in both: cost script, measures script, gate-times script, test runner. The test's docstring and the "four scripts" comment follow the sentence.
- **The test fails on the breaks the remark names** (run in a detached worktree of the head, see Checks):
  - cost script path moved in `audit_count.py` (`COST_SCRIPT` set to a path that does not exist): the first test fails (`['task-cycle/cycle_stages_moved.py'] != []`), exit 1;
  - a path added to a group of `TOOL_GROUPS` (`COST_SCRIPTS` given an extra path): the second test fails, exit 1;
  - the cost group emptied: the second test fails, exit 1.
  - On the previous head the test did not name the cost script at all, so the first break stayed green there; the correction closes that.
- **The test does not just compute its own expected value.** The first test asks git (`git ls-files`) whether the path is a tracked file; the second compares constants with a literal set of the four names, so a changed set of the audit's paths is a visible difference, not a silent one. Weak spot, not a defect: the second test compares constants with constants, so by itself it does not catch a moved cost script; the first test does, and the two together cover both breaks, as the author's own-work check also says.
- **WAY-339 stays true.** Its text names the script that measures the cost, `task-cycle/cycle_stages.py`, as the one whose change starts a series of the cost, and its *Verification* names `invariants: audit-series-script-paths` and no number of paths. The invariant now names what the decision names. I read WAY-339 whole (`foundations/decisions.md:7418` to its end).
- **The audit still reads what it read.** `audit_count.py` is untouched, so its behaviour cannot have changed; the tests named below pass.
- **Foundation entries consistent.** `foundation_check.py` exits 0 with `0 errors` and one `listed:` line, for `guidelines-file-place` (`foundations/invariants.md:418`): its sentence was reworded by an earlier commit of the request (`bfb774c`), its test left as it was, and the request document already names it (item 13 of the request, line 128 of `request.md`). The invariant changed by this correction, `audit-series-script-paths`, is not listed because its citing test changed in the same commit (WAY-03).
- **Changed invariant test (WAY-03), named for the request:** `process-audit/test_audit_series_scripts.py` for the invariant `audit-series-script-paths`, changed together with its sentence in `cf4fe17`.

## Findings

Critical: none. Important: none.

Minor (blocks nothing, within the change):

1. `process-audit/test_audit_series_scripts.py:2` — the first docstring line is 116 characters long, while every other line of the file is at most 100; the rewrap of the docstring left the second line long ("`process-audit/audit_count.py` reads, to start a new series of the cost of cycles, of the measures of how a cycle's"). Cosmetic only: no sentence is read wrongly, nothing fails (`awk 'length>100'` on the file showed this one line).

## Declined to judge

- The author's remark that the second test, as a comparison of constants with constants, cannot catch a moved script by itself: the first test does it, and the remark asked for no more (one sentence and one line of a test).

## Checks

- `git rev-parse HEAD` in the reviewed worktree: `cf4fe175...`, equal to the given head.
- `git diff 3145e4f..cf4fe17` and `git log`: one commit, two files, as listed above.
- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`): exit 0, `0 errors`, one `listed:` line for `guidelines-file-place` (see above).
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` on the head: exit 0, 3 tests OK.
- Mutation A (sed on `audit_count.py` in the detached worktree: `COST_SCRIPT = "task-cycle/cycle_stages_moved.py"`), same test command: exit 1, first test fails.
- Mutation B (my first try set paths already in the set, so the set did not change and the tests stayed green, exit 0 — a bad mutation of mine, not a gap; the second try added a new path `task-cycle/cycle_measures_extra.py` to `COST_SCRIPTS`): exit 1, second test fails.
- Mutation C (`COST_SCRIPTS = ()`): exit 1, second test fails.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k PriceBoundary -k ProcessVersions`: exit 0, 25 tests OK (in the head worktree, after each mutation was reverted with `git checkout`).
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k test_each_path_that_starts`: exit 0, 1 test OK.
- Not run: the whole gate (the orchestrator runs it, as the handoff says).

## Reach beyond the dispatch

- `process-audit/audit_count.py` lines 405 to 510 (grep of `COST_SCRIPT`, `TOOL_GROUPS` and the other constants): to confirm what the audit splits by and that the file is untouched.
- `git diff origin/foundations...HEAD -- foundations/invariants.md` and `request.md` lines 128 and 144: to see where the `listed:` line for `guidelines-file-place` comes from (an earlier commit of the request, not this correction).

## Unread material

- `elements/invariants/skill/SKILL.md` and its template: not read (the handoff names them for the author; the review judged the one changed sentence against WAY-339 and its own test). Of `foundations/invariants.md` I read the diff and the invariant `audit-series-script-paths` through the diff context, not the file whole. Everything else the handoff names (handoff, remarks, correction report, `review-change` skill, `fix.md`, WAY-339 whole, the test file whole) was read whole.

## Searches not found or unclear

- none

## Working copies

Directory `.runs/review-correction/`: one detached worktree of the head (`.runs/review-correction/wt`) for the mutations; removed with `git worktree remove --force`, and the directory is gone. The reviewed worktree, its index and its branch were not changed.
