# Author report — the return step after correction 1

**Status:** done. Nothing no longer matches within what the correction's remarks and the task settle, so I changed and committed nothing; the head stays `35796540` and the worktree is clean.

## Commits

none

## Return step (in the form of the record)

- **Foundation compared with code:** what correction 1 changed — `guidelines/coding-shared-module.md`, whose *Applies to* now ends `· elements-common` and whose *Where in code* now holds `elements/common/` — against the entries that bear on it.
  - **WAY-391 and the invariant `shared-module-import-runs-nothing`** (read whole): the decision's rule, "importing a file of the kind runs nothing", is the rule of the guidance and is unchanged; the invariant's sentence names `relation-model/fingerprint.py` and its *Part* is `relation-model`, and its test checks that file alone, so the correction does not make it false and extends nothing it states. The two modules of `elements/common/` that follow the rule in spirit, `foundation_source.py` and `foundation_text.py`, import with exit code 0 and no output (`python -B -c "import <module>" < /dev/null` from `elements/common/`, exit 0 each); no test or invariant reaches them, which is as it stood and is not for this step to add (an invariant is written only for a rule the task, a decision or the human sets).
  - **WAY-386 to WAY-390** (the *Scope* line of each read, WAY-386 whole): a decision of a kind of code carries the same parts as the *Applies to* of its guidance file — WAY-386 `task-cycle, project-level, elements-common, instruction-files` and `coding-check.md` the same four; WAY-387 and `coding-measuring-report.md` `task-cycle · process-audit · project-level`; WAY-388 and `coding-generator.md` `agent-instructions`; WAY-389 and `coding-repository-changer.md` `task-cycle · elements-common · installation`; WAY-390 and `coding-command-runner.md` `task-cycle · gate`. WAY-391 stands apart: its *Scope* is `relation-model` alone, and the guidance named `relation-model · process-audit · task-cycle` before the correction and names those and `elements-common` now. So the gap between WAY-391's *Scope* and the guidance's *Applies to* existed before the correction and the correction widens it by one part, as the human asked.
  - **Part map, `elements-common`:** its sentence (both modules named in the fix) and its *Files* are unaffected by a change to a guidance file, which sits in the part `agent-instructions` (`guidelines/**`); the new *Applies to* value is a part of the map.
- **Decisions written:** none.
- **Invariants written:** none.
- **Environment facts written:** none.
- **Glossary terms written:** none.
- **Part-map changes:** none.
- **Projected entries written:** none.
- **Rows of *Settlements to record* written:** none (the correction's remark 1 is a change to a guidance file, which "goes in its place by the rule of that place" and writes no entry).

## Findings of the review of correction 1 that are not mine to fix here

As the handoff gives, each is outside the task's scope and is left as it stands; it goes to the request's list:

- the *Scope* of WAY-391 (`relation-model`), which no longer matches the *Applies to* of `guidelines/coding-shared-module.md` that WAY-386 to WAY-390 keep equal to their decisions' *Scope* — a change of a decision beyond what the remarks and the task carry (WAY-30);
- the wording of WAY-19 and of WAY-150, which the reviewer of the correction named in reading six decisions against the new rule of WAY-05 (their entries were not changed by this change, and the next task shortens WAY-150).

## Checks (command, exit code)

- No file changed, so no focused check was repeated; the runs of the correction stand: `python -B gate/run_tests.py product-guidelines` exit 0 (14 tests), `agent-instructions` exit 0 (52), `elements/common` exit 0, `python -B elements/common/foundation_check.py` exit 0 with `0 errors`.
- Run in this step: `python -B -c "import foundation_source"` and `… "import foundation_text"` from `elements/common/` — exit 0 each, no output.
- Not run: the full gate (as handed).

## Unread material

- `foundations/decisions.md`: WAY-386 and WAY-391 read whole with their *Rationale* and *Rejected*; of WAY-387 to WAY-390 only the *Scope* line (by search), not the entries whole.
- `foundations/invariants.md`: the entry `shared-module-import-runs-nothing` read whole; the rest of the file not read.
- The part map: not read again in this step (the `elements-common` and `agent-instructions` entries were read in the return step before).
- The review of correction 1 and its findings file: not read (the handoff names the findings only by its summary).

## Searches not found or unclear

- none

## Working copies

- none made (`.runs/author-correction-1-return/` was not needed) and no file outside the worktree. `.runs/quality-venv/` stays as before.
