# Return step report

**Status:** done
**Commits:** none. The comparison found nothing that needed a correction, and every entry the task carries is already committed (`0f34dc1`, `172bc71`, `8dae4be`).

## Record fields

- **Foundation compared with code:** WAY-294 (the one entry the change writes) compared with `task-cycle/remarks_check.py`:
  - the Verification examples match the code: `planner-report.md` and `review_whole.md` are read, `01-author-handoff.md`, `slice-1-findings.md`, `notes.txt` and `gate.log` are not, a report with no section gives no item and exit 0, and exit 2 is not given for it;
  - the binding sentence's exception matches `section_items`, which returns no item for a report without the section;
  - the part map entry `task-cycle` (*Files* `task-cycle/**`) covers every file the change touches; nothing to change there.
  - Decisions WAY-148 and WAY-260 were read against the report-name rule in `task-cycle/skill/SKILL.md`: reports still go through files, so no conflict.
  - No stale wording was found in the foundation or in the skill's remarks-check section (`task-cycle/skill/SKILL.md`, the "process remarks check"), which describes the script without the label or rule details. Nothing corrected.
- **Decisions written or changed:** WAY-294 (task row 1). Committed in `0f34dc1`, Rationale in `8dae4be`.
- **Invariants written or changed:** none. The task sets no invariant, and no decision or human sets a rule that needs one. The new behaviour is covered by the unit tests in `task-cycle/test_remarks_check.py`, which the gate runs.
- **Environment facts:** none. The task's *Context* says the naming rule stands in the skill with its reason inline and without an environment fact, and its *Settlements to record* carries only row 1, so the task's exclusion prevails over the general rule. **Question for the orchestrator:** the rule in `task-cycle/skill/SKILL.md` (the sentence after the WAY-148 handoff sentence) rests on Claude Code's refusal of subagent writes to files named with `report`, `summary`, `findings` or `analysis` (observed 2026-11-12, Claude Code 2.1.322). `foundations/environment_facts.md` does not hold that behaviour. Recommendation: leave it as none, as the task decided; if you want it held, that is a new entry the task did not carry and needs its own decision.
- **Glossary terms:** none. The change uses "thematic break", "bold label", "process remarks" and "Searches not found or unclear" with their ordinary meanings. The glossary has no entry for them and no word is used against an entry.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task is independent).
- **Rows of *Settlements to record* written:** row 1 → WAY-294 (decision, narrows WAY-344).

## Checks

Run on the worktree at head `8dae4be`, from its root:

- `python -B elements/common/foundation_check.py foundations`: exit 0, "0 errors".
- `python -B -m unittest task-cycle.test_remarks_check`: exit 0 (59 tests OK).
- Grep for stale wording (`start of a line`, `sub-heading is no item`, `no section are not read`, `report-planner`, `thematic`, `bold label`) across the repo's `.md` and `.py` files outside `.runs/`: only the intended hits in `task-cycle/remarks_check.py` and `task-cycle/test_remarks_check.py`.
- Not run: the full gate (the orchestrator runs it on this tree).

## Unread material

- `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`: read whole.
- `task-cycle/record_template.md`: read only the *Return step* section (lines 161-200); the rest not read.
- `foundations/decisions.md` WAY-148, WAY-260: read in full for their Verification; WAY-294 and WAY-295 read whole; WAY-344 read whole earlier.
- `foundations/glossary.md`: not read; searched by grep only.
- `foundations/environment_facts.md`: headings listed and grepped; entries not read.
- `task-cycle/skill/SKILL.md`: remarks-check section read in part (around lines 476-490), as before.

## Searches not found or unclear

- Glossary: no entry for "Searches not found or unclear", "process remarks", "bold label" or "thematic break" (grep, not found).
- Environment facts: no entry on Claude Code refusing subagent writes of report-named files (grep for `Claude Code` with `refus`, `subagent`, `report files`: not found). This is why the question above is raised.
- Unclear: whether the return step's general rule (environment facts for sources a change rests on) reaches a rule whose reason the task put inline. The reading taken: the task's exclusion prevails, so none.
- Pre-existing over-long line at `task-cycle/skill/SKILL.md` line 151 (the open Minor finding): left as the handoff asked.
