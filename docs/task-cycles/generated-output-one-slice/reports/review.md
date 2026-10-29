FAIL 5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5

# Whole-change review

Range: `76cbe0ea4e766eb9561052355e370d6424c1d32f..5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5`.
Worktree: `C:/Storage/repos/the-way/.runs/worktrees/generated-output-one-slice`.
One-author change, without a spec or plan. Counts: 2 blocking Important findings, 0 Critical, 0 Minor, 0 out of scope.

The documentation and Python/test changes were inspected in separate passes. The focused suite and foundation checker pass. An in-memory expansion of the two patterns makes the new test fail for the expected reason. No reviewed file, index or branch was changed.

## Blocking findings

### 1. Remove the rejected option that the accepted source did not reject

**Grade and scope:** Important, within the task; new thread. No slice: one-author change, commit `5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5`.

**Anchor:** [foundations/decisions.md:7524](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/foundations/decisions.md#L7524).

**Do wklejenia:** The source does not contain “listing multiple patterns for one output directory” among the alternatives the human rejected. Q2's rejected wording concerns one pattern across both output directories, and its mention of two patterns means one for each of those directories. Remove the additional rejected alternative and its invented reason from WAY-263.

**Dlaczego to zgłaszam:** This entry records settlement 1, including the alternatives actually retained under Q1–Q3. Its rejected-options field tells later agents which proposals were already considered and why. The frozen task's Q2 rejects the old wording “one pattern of its output”: the stated failure is either an overly broad `.*/skills/the-way-*/SKILL.md` or two patterns contrary to that old instruction. Those two patterns are the `.claude/skills/` and `.agents/skills/` patterns explicitly accepted in Q2; the source says nothing about two patterns inside one output directory. The added alternative and the reason “each pattern is meant to stand for a single output group” are a derivation from the chosen rule, not an alternative in the source. A future proposal to use two narrowly targeted patterns in a single directory would therefore encounter a purported prior rejection that never happened. WAY-134 expressly prevents deriving rejected options this way, and `elements/decisions/template.md:59` gives the same source rule. This is a source-fidelity defect in the foundation entry this task exists to record, not wording polish. Remove this clause; retain the alternatives traceable to the source. No additional human answer is needed to remove it.

Evidence: [frozen task Q2:40](../task.md#L40), read with Q1–Q3 and settlement 1 in full; [decision template:59](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/elements/decisions/template.md#L59). The source was also searched for `multiple patterns|wzorc|Not chosen|odrzucon`; positive matches include the accepted two-directory patterns and the Q2 rejected wording.

### 2. Put the execution timing and cleanup in the slice material the executor receives

**Grade and scope:** Important, within the task; new thread. No slice: one-author change, commit `5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5`.

**Anchor:** [task-cycle/plan/SKILL.md:122](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/task-cycle/plan/SKILL.md#L122).

**Do wklejenia:** The planner is told that a slice runs the command at the end and handles reported obsolete paths, but the only content it is explicitly told to put in that slice's Goal is the command and the ban on hand editing. The executor does not read this planner skill, so a Goal that follows that stated content can omit the timing and cleanup obligations. Require the Goal to carry the complete action: run the named command after input changes, handle reported obsolete output paths and commit the complete result.

**Dlaczego to zgłaszam:** This task is intended to keep generated files current after every slice, not just after the last one, and Q2 puts the command in Goal precisely because the executor receives only its own plan section. The new paragraph gives the planner three execution obligations (run at the end, handle reported obsolete paths, commit all output), then gives a narrower explicit recipe for Goal (name the command and prohibit hand editing). For example, “Rename skill X to Y; `python -B agent-instructions/skill_entry_points.py --write`; do not edit generated output by hand” satisfies that Goal recipe but carries neither “after the input changes” nor the required treatment of obsolete outputs. The executor's own method, `task-cycle/change/SKILL.md`, and its slice-specific `slice.md` supply neither obligation. The handoff copies the section and its Read, not the planner skill. WAY-263 is scoped to task-cycle, so an ordinary product slice changing a generator input in another part does not acquire it through the mandated foundation selection either.

The repository's example makes the cleanup gap concrete: `agent-instructions/skill_entry_points.py` reports orphan directories and exits successfully without deleting them. Merely running and committing what it writes can leave the old skill's entry points in place; the entry-point invariant then fails and a later agent has to repair the slice. Naming the command also leaves its order relative to the input edit unstated. The broad instruction that a section must be self-contained helps, but the detailed Goal recipe should preserve these obligations rather than make the planner infer which parts of its own execution prose must be copied. Add them to the instruction about the slice's Goal, keeping the rule at the planner as the task requests. This repairs the transfer to the executor without making executors read the whole planner skill.

Evidence: [plan section handoff rule:113](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/task-cycle/plan/SKILL.md#L113), [slice reading:7](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/task-cycle/change/slice.md#L7), [handoff construction:25](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/task-cycle/skill/planning.md#L25), [generator behavior:15](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/agent-instructions/skill_entry_points.py#L15), and [new decision scope:7501](https://github.com/mariusznazar/the-way/blob/5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5/foundations/decisions.md#L7501).

## Minor findings

None.

## Out-of-scope findings

None.

## Declined to judge

None.

## What holds

- The new test builds twelve existing generated files, six for each pattern, plus one existing source. Its expected count of three is literal, and its fit assertion exercises the real size calculation. Expanding the patterns produces thirteen files and fails the test.
- The size script's executable code and limit are unchanged; only its introductory description changes.
- The orchestrator's own mechanical-check instruction now accepts every changed file matched by a Change pattern, at the point where it performs that check. The planner does not duplicate that mechanical-check rule.
- The accepted per-directory grouping, per-input-changing-slice generation rule, conditional inclusion of the generator source, and prohibition on editing generated content appear in the implementation and new decision. Findings 1 and 2 concern source fidelity and delivery of the complete execution instruction.
- No invariant test changed: the only changed test file contains no invariant citation in either the base or head diff. No UI, new trust boundary or irreversible operation is introduced. The task's Q5 authorizes the pre-main route and empty guidelines selection.
- The author's own-work check targets the relevant risk, but its comparison of the planner and orchestrator wording does not establish that the executor receives the full instruction; finding 2 is the remaining gap.

## Checks

All commands ran in the worktree named above unless their explicit path says otherwise.

| Command or manual method | Outcome |
|---|---|
| `git rev-parse HEAD` | Exit 0; `5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5`, matching dispatch, also confirmed after checks. |
| `git -C .agents/skills/the-way-review-change rev-parse --show-superproject-working-tree` | Exit 0; empty, top-level the-way. |
| `git ls-files --stage -- ':/.the-way'` | Exit 0; empty, no product pin in this worktree. |
| `git diff 76cbe0ea4e766eb9561052355e370d6424c1d32f..5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5` | Exit 0; read the entire five-file diff. |
| `git log --oneline 76cbe0ea4e766eb9561052355e370d6424c1d32f..5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5` | Exit 0; one author commit. |
| `python -B -m unittest discover -s task-cycle -p test_slice_size.py` | Exit 0; 16 tests passed. |
| `python -B elements/common/foundation_check.py` | Exit 0; 0 errors. |
| `git diff --check 76cbe0ea4e766eb9561052355e370d6424c1d32f..5be94fa4c9a5d50fbe3af14b1eca01f9c9694ed5` | Exit 0, run twice; no whitespace errors. |
| `git status --short` | Exit 0, run twice; empty before writing this ignored report. |
| Documentation pass: frozen task To do 1–3, Q1–Q5 and settlement 1 against the full diff, then trace planner → copied slice → executor and orchestrator | Findings 1 and 2. No plan/spec exists on this one-author route. |
| Python/test pass: read the size script and test file whole, check literal expectations, fixture paths, actual call to main and unchanged executable diff | No code/test defect found. |

The following exact scratch command exited **1**, expected: the new test failed at `self.assertEqual(code, 0)` with `1 != 0`. It changes only objects in that Python process, writes no reviewed file, and leaves no mutation to revert:

```powershell
@'
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path('task-cycle').resolve()))
import slice_size
import test_slice_size
original_measure = slice_size.measure
def expanded_measure(item, root):
    expanded = []
    for name in item.change:
        if '*' in name:
            expanded.extend(str(path.relative_to(root)).replace(chr(92), '/') for path in root.glob(name))
        else:
            expanded.append(name)
    return original_measure(slice_size.Slice(item.ident, expanded, item.read, item.fields), root)
slice_size.measure = expanded_measure
suite = unittest.TestSuite([test_slice_size.SliceSizeTest('test_change_patterns_each_count_as_one_file')])
result = unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
'@ | python -B -
```

The full gate was not run: the dispatch and review method assign it to the orchestrator. No end-to-end agent execution was run; the documentation findings use the prescribed reading and handoff routes, not a claim about an observed executor run. The generator was read, not run with `--write`; no generated file change is required by this diff's unchanged skill names and descriptions.

## Reaches beyond the dispatch

- `C:/Storage/repos/the-way/.runs/worktrees/generated-output-one-slice/task-cycle/change/SKILL.md`, `task-cycle/change/slice.md` and `task-cycle/skill/planning.md`: trace what a slice's executor actually reads and what its handoff carries.
- `C:/Storage/repos/the-way/.runs/worktrees/generated-output-one-slice/agent-instructions/skill_entry_points.py`: verify the example command's orphan reporting, success behavior and output directories.
- `C:/Storage/repos/the-way/.runs/worktrees/generated-output-one-slice/elements/decisions/template.md` and the complete WAY-114 entry: verify the source constraints and acceptance rules applicable to the new foundation entry. The whole-change foundation selection otherwise followed the part map and scoped-entry procedure; its list is not recorded.

## Searches not found or unclear

- I initially tried `C:/Storage/repos/the-way/.runs/worktrees/generated-output-one-slice/task-cycle/make/SKILL.md`; `Get-Content` failed because that presumed path does not exist. `rg --files task-cycle` found the actual method at `task-cycle/change/SKILL.md`, which I then read with its slice variant.
- The rejected alternative “listing multiple patterns for one output directory” was not found in the frozen task's Q1–Q3 or settlement 1; the superficially similar two-pattern mention in Q2 concerns the two different output directories. This is finding 1.
- No direct executor instruction for generation at the end or handling obsolete output was found in the complete change method and slice variant. Their reading route reaches the slice section and selected material instead of the planner skill. This is the visibility issue in finding 2.
- Some batched foundation reads exceeded the tool's output limit; the omitted entry ranges were read again in smaller batches before relying on them. A first Scope search considered only the first line; it was widened to include continuation lines before the final reading. No conclusion of absence was drawn from either incomplete output.
