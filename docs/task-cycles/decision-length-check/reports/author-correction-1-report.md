# Author report — correction 1

**Status:** done

## Remarks (as made) and how each was met

1. **"Fix it in this request … Add `elements-common` to its *Applies to* and `elements/common/` to its *Where in code*."** Done in `guidelines/coding-shared-module.md`:
   - `- **Applies to:** relation-model · process-audit · task-cycle` → `… · task-cycle · elements-common`;
   - `elements/common/` added as the last item of *Where in code*, in the form of the other items (backticked directory with a trailing slash).
   No other line of the file changed (2 insertions, 1 deletion): the *Files of this kind* table, the rules and the examples stand as they were.
2. **The reading of six decisions whole** is the reviewer's work; I read and judged none of them, as the handoff says.

## Commit

`35796540` Hand the guidance for shared modules to an agent that changes one in elements/common (one file: `guidelines/coding-shared-module.md`). The worktree is clean; the head before it was `2ffff547`.

## Form of the file against the guidelines and the tests

- `guidelines/coding.md` (read whole in the first turn) lists the kind `shared-module` with its file in the index and says an *Applies to* names parts of the map, joined by ` · `; the new value uses the identifier `elements-common`, which `foundations/part_map.md` holds as a part, and the other kind files (`guidelines/coding-check.md`: `task-cycle · project-level · elements-common · instruction-files`) join parts the same way. `Where in code` there lists directories as `` `elements/common/` ``, as the new item does.
- `product-guidelines/reading.md` (read whole): a file whose *Applies to* names an affected part is read whole by the agent whose work touches that part, and a file `coding-<kind>.md` only where its index row's *When to read* also matches the work. After the change a change in `elements-common` meets this file by its *Applies to*, and its index row in `guidelines/coding.md` (`shared-module`: "before adding or changing a shared module") still decides whether it is read. The index row was not changed, as the handoff asks.
- What the tests accept: `python -B elements/common/foundation_check.py` reads the *Applies to* of every file of `guidelines/` as parts of the map and reports an unknown one; it accepts `elements-common` (`0 errors`). `product-guidelines` and `agent-instructions` accept the file (below), and `elements/common` (which holds `test_guidelines_place.py` and the foundation check's tests) too.

## Checks (command, exit code)

- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests, OK.
- `python -B gate/run_tests.py elements/common` — exit 0 (run beyond the handoff, since its tests read guidelines files).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Linter and formatter: not run, no Python file changed.
- Not run: the full gate (as handed).

## Own-work check

The requirement most likely not met: that the guidance reaches an agent that changes a shared module in `elements/common/`. The check is the reading of how it is selected (`reading.md`): *Applies to* now names `elements-common`, so the file is among those the selection reads for that part, and the index row of `guidelines/coding.md` still bounds it to shared-module work. No test fails or checks the selection itself (the-way does not test what an agent does with a skill), so this stands on reading, not a run.

## Unread material

- `guidelines/coding.md` was not re-read in this turn (read whole in the first turn); `guidelines/coding-shared-module.md` read whole in the first turn and its changed lines in the diff. Nothing else named by the handoff stayed unread, except the six decisions it tells me not to read.

## Searches not found or unclear

- none. One thing to note: the shared-module guidelines' rule "importing runs nothing" has the invariant `shared-module-import-runs-nothing`, whose test checks the one exemplar only (`relation-model/test_fingerprint.py`); it does not reach the modules of `elements/common/`. That is as the task of this correction leaves it (no change to the rules or the invariant), and is named here only so that the reviewer is not surprised.

## Working copies

- none made (`.runs/author-correction-1/` was not needed). One scratch file I wrote outside the worktree while running the checks (a path outside the task's worktree) was removed in the same command, and I confirmed it is gone. `.runs/quality-venv/` stays as before.
