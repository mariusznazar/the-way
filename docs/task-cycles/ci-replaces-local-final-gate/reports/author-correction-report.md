# Author report — correction 1, ci-replaces-local-final-gate

**Status:** done

**Commit** (not pushed): one, on top of `026308f`, "Place process-audit/stage_pricing.py under the kind shared-module in the coding guidelines" (`guidelines/coding-shared-module.md`, 2 insertions, 1 deletion; hash in `git log -1`).

## The remarks, one by one

1. **Remark 1** (the required check `tests-windows`, the request ready): not mine; the orchestrator's, in the description. I left `foundations-branch-ruleset` as it is.
2. **Remark 2, N-3 — done.** Two lines of `guidelines/coding-shared-module.md`:
   - `- **Applies to:** relation-model` became `relation-model · process-audit`. This is the placement the remark asks for: `process-audit/stage_pricing.py` is a module that other scripts import (`audit_count.py` imports it), so by `guidelines/coding.md`'s index and `product-guidelines/reading.md` ("Read whole every file whose *Applies to* names an affected part") the next author who changes or adds a shared module in `process-audit` reads this file.
   - `- \`process-audit/\`` added to the section "Where in code". It was needed because that section lists the directories of the kind's code, and every other kind lists the directories of the parts in its *Applies to* (for example `coding-measuring-report.md`: task-cycle, process-audit, project-level); with only `relation-model/` it would contradict the new *Applies to*.
   - Not added: a row in "Files of this kind" (the table lists only the exemplar; no other shared module of the-way stands in it, and a row would need a status, which `exemplar` is not and `copy` would be a new designation), no rule, no exemplar mark, no decision.
3–4. Accepted: nothing to do.

The seven other Minor findings are let through, and I changed nothing for them.

## What the search found, and what the new *Applies to* changes for it

Searched the tracked `.py` and `.md` files (not the record and not the decision log's prose) for `shared-module`:
- `guidelines/coding.md:21` (the kind index row) and `:100` ("How a script starts and ends": a module with only a fixed `__main__` block is no script): unchanged; the index row's *When to read* already matches the work of a module of `process-audit`.
- `foundations/invariants.md`, `shared-module-import-runs-nothing` (*Part* `relation-model`, test `relation-model/test_fingerprint.py`) and WAY-391 (the exemplar `relation-model/fingerprint.py`, *Scope* `relation-model`): unchanged. The invariant's test still checks only the exemplar; for `stage_pricing.py` the rule "importing runs nothing" now binds through the review of each change (it defines only constants, classes and functions, so it meets it). WAY-391's *complies* says that the guidelines list the exemplar beside the decision, which they still do.
- Tests that read the guidelines' form (`product-guidelines`, `agent-instructions`): none names this file's *Applies to*; they pass.
- WAY-385 and `coding.md`'s rule of size read the part list in `coding.md` (it names `process-audit` already); unaffected.

## Checks (command, exit code)

| Check | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` (`0 errors`) | 0 |
| `python -B gate/run_tests.py product-guidelines` (14 tests) | 0 |
| `python -B gate/run_tests.py agent-instructions` (37 tests, 2 expected failures as before) | 0 |
| `python -B gate/run_tests.py elements/part-map` (40 tests) | 0 |
| `python -B gate/run_tests.py process-audit` (235 tests) | 0 |

The full gate was not run.

## Own-work check (WAY-164)

Requirement most likely not met: "the next author who adds a file of that kind finds a row for it". Check: the kind index row of `guidelines/coding.md` points to this file, whose *Applies to* now names `process-audit`, the part of `stage_pricing.py` (the part map assigns `process-audit/**` to it). It shows the file is found by *Applies to*; it shows no row for the file in a table of files of the kind, which I did not add (see above). If the human meant a table row, that is a further small edit.

## Unread material

- `product-guidelines/reading.md`: read to its "Select and read" and "Distinguish the gaps" sections, not the rest. `guidelines/coding.md`: read whole earlier in this cycle, and the kind index and the shared-module rule rechecked. The reviewer's `reports/review-fix-report.md` read at N-3 and its search note only.

## Searches not found or unclear

- No rule says whether a module imported by a script of another part needs a row among the files of its kind (the review's own note); I read "places it under the kind" as the *Applies to* line, as the remark and the handoff say.

## Working copies

`.runs/author-correction/` held the logs of the runs; removed. Nothing remains.
