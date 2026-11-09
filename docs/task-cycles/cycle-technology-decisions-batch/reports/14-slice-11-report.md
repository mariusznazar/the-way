# Slice 11 report — Part map: the task cycle depends on the installer

**Status:** done
**Worktree:** the task's worktree root
**Branch:** task/cycle-technology-decisions-batch
**Method:** make-change (`task-cycle/change/SKILL.md`), variant slice (`task-cycle/change/slice.md`)

## Commits

- `6349019` Make the task cycle depend on the installer in the part map

## Files changed

- `foundations/part_map.md`: +1 / -1 line. In the part `task-cycle`, *Depends on* gains
  `installation` at the end of line 99 (`... · product-guidelines · installation`).

No other file was changed. No other entry of the map changed.

## Reads

- Handoff, `task-cycle/change/SKILL.md` (whole), `task-cycle/change/slice.md` (whole),
  `agent-instructions/README.md` (whole).
- Plan: slice 11 section and the *Foundation entries* table. The table has no row for item 29; the
  slice depends on no foundation entry being written in this cycle.
- Passages named by the slice, read at the current ranges: `task-cycle/skill/SKILL.md:30-55`
  (step 2), `installation/README.md:75-120` (Moving the pin), `foundations/part_map.md` (whole),
  `foundations/decisions.md:875-907` WAY-33, `:1116-1166` WAY-44, `:9488-9541` WAY-299,
  `foundations/invariants.md:146-155` map-reference-target, `:322-336` cross-part-imports.
  The ranges and headings matched the handoff, so there was no drift.
- Element: `elements/part-map/skill/SKILL.md`, `decide_entry.md`, `write.md`, `template.md` (whole),
  `elements/common/rules.md` (whole, 84 lines), `elements/common/way_of_working.md` (lines 1-120,
  covering steps 1 and 2; steps 3 and 4 were not read because the slice does not draft or ask).
- Task passages from the handoff (item 29, question 4) were taken as quoted in the handoff.

## Reaches beyond the handoff

- `elements/common/way_of_working.md` lines 120 onward and `elements/common/rules.md` were read
  as the element skill names them; the skill's steps 3 and 4 were not needed for a one-line change.
- `foundations/decisions.md` was searched by grep for `task-cycle`, `installation`, and for
  dependency wording (`depends on`, `acyclic`, `circular`, `mutual`, `cyclic`). The 91 decision
  entries whose *Scope* names `task-cycle` were not read whole; the search read the lines the grep
  found and none of them states a rule about which parts may depend on each other.

## Own-work check

- **Requirement:** the slice's goal, item 29 — the part `task-cycle` lists `installation` in its
  *Depends on*, and no other entry of the map changes.
- **Check:** `git diff HEAD~1 -- foundations/part_map.md` showed one changed pair of lines, and
  `grep -n "product-guidelines · installation" foundations/part_map.md` returned line 99.
  `git show --stat 6349019` showed `foundations/part_map.md` as the only file.
- **Result:** the requirement holds.
- **Gap I did not close:** no test reads that `task-cycle`'s *Depends on* names `installation`. A
  later edit that drops it would pass every check named in the slice, because the cross-part-imports
  test only loosens for listed dependencies and no code of `task-cycle` imports `installation`
  today (grep of `task-cycle/**/*.py` for `installation` found nothing). The dependency is through
  the skill's text, not code. Naming the gap for the orchestrator; I did not add a test, because
  the slice's *Checks* do not include one and the change is a map entry, not behaviour.

## Whole-foundation search (WAY-33)

Entries the change touches: the part `task-cycle` and every entry that names it or that it names.

Findings:

1. `foundations/part_map.md:154`, `instruction-files`, *Depends on* `installation`; `:157-164`,
   `installation`, *Depends on* `task-cycle`; `:174`, `product-guidelines`, *Depends on* `task-cycle`
   and `installation`. Together with the new line, `task-cycle` and `installation` depend on each
   other, which is the trade the plan's question 4 accepted. No change needed.
2. `foundations/decisions.md:2420` (WAY-101 / WAY-320 scope: `project-level, installation,
   foundation-review, product-guidelines`) and `:727`, `:918` — name the parts but say nothing about
   `task-cycle` dependencies. No change needed.
3. No decision or invariant forbids cyclic dependencies between parts (searched for `acyclic`,
   `circular`, `mutual`, `cyclic`, `each other`). Nothing to correct.
4. `foundations/invariants.md:345` (`task-cycle` part, image-extension check) and `:88` mention
   `task-cycle` scripts only; unaffected.

Nothing found needed a correction in the same change.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| Element tests | `python -B gate/run_tests.py elements/part-map` | 0 | Ran 39 tests, OK |
| Whitespace | `git diff --check` | 0 | no output |

The full suite (`python -B gate/run_tests.py` without a directory) was not run, as the handoff asks.
No test was written first; the slice is a one-line map entry, so the test-first rule does not fit
(`task-cycle/change/SKILL.md` section 2, "configuration, formatting, wiring, prose").

## Searches not found or unclear

- A test that the part map's *Depends on* of `task-cycle` names `installation` — none exists (see
  the own-work check).
- Whether the 91 decisions scoped to `task-cycle` say anything about its dependencies — not read
  whole; the grep found no such statement.
- Whether a dependency in a part's text (a skill sending the agent to another part's README) counts
  as a *Depends on* — the map's template says `Depends on` names what the part may depend on, and
  "may" covers it; no entry says otherwise. Reported as read, not as a finding.

## Questions for the orchestrator

None.
