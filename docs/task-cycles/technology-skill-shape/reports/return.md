# Return step report

**Status:** done. **Commits:** none; nothing needed a correction. Worktree clean at `c7a4008` (`git status --short` empty). No push, no full gate.

## Foundation compared with code

Compared with the seven files at `c7a4008` (`project-level/technology/{SKILL,start,list,running_product,settle,research,close}.md`): decisions WAY-256, 257, 121, 122, 123, 137, 138, 165, 166, 120, 113, 118, 150, 106, 127, 259 (each read whole in the first step, binding sentences re-read now against the new text), the part-map entry `project-level`, the glossary and the three environment facts the handoff names. Also a search of the whole foundation for `settle-technology`, `technology/SKILL`, `project-level/technology`, `step 0` and `one file` in the decisions, part map, invariants, glossary and facts.

The four questions of the handoff:

- **A skill of this part is one file:** said by no entry. The only "one file" sentences are about the foundation files (`invariants.md`, `glossary.md`, `environment_facts.md`) and the skill of `instruction-files` (WAY-258), not about this part. WAY-125 and WAY-256 name files beside a skill's `SKILL.md`, which the layout now has.
- **What the leader reads at step 0:** WAY-150 and the glossary-free text of WAY-111 say the project level selects and reads the foundation selectively; `start.md` still does. WAY-120 and the task's note on it ("both critiques of step 2 stay, only the moment of reading changes") hold: `SKILL.md` step 2 and `settle.md` sub-steps 4 and 5 read the critique instruction. WAY-113 is carried by the section "How a skill asks", still read in `start.md`. No entry names what step 0 reads.
- **What the research agent is given:** WAY-122, WAY-123, WAY-166, WAY-138 name no list of what the agent receives. `settle.md` sub-step 1 gives the list with the new path item; `research.md` states it back to the agent.
- **Where the rule on reading critique stands:** no entry says where. WAY-120 states how a critique is given and settled, not when its instruction is read.

Part-map entry `project-level`: its responsibility, files (`project-level/**`, which holds the six new files), dependencies and trust boundary (`readiness_check.py`, `plan_check.py`, `plan_state.py`) are unchanged and still true. It names no skill file count.

## Decisions

none written or changed.

## Invariants

none written or changed. `skill-entry-points` and `derived-file-content` are met by the unchanged description line (`python -B agent-instructions/skill_entry_points.py` printed `entry points are current`, exit 0, in the fix step). `project-technology-record` and `project-readiness-gate` concern `readiness_check.py`, unchanged.

## Environment facts

none. The change rests on no source outside the product that the foundation does not hold. Read now: `single-rule-compliance` and `instruction-density-accuracy` (WAY-256's grounds: the change moves fragments by step and adds no threshold of length) and `claude-skill-nested-references`. On the last: `SKILL.md` names every file beside the skill directly (one level deep), as the fact recommends; `start.md`, `list.md` and `close.md` also name a step's file in passing, and `settle.md` names the critique instruction at its sub-steps. These second pointers add to the direct ones and the files are reached from `SKILL.md` whatever an agent does with them. WAY-258 binds only the files of `instruction-files`, so no entry is contradicted.

## Glossary terms

none written. Checked the 28 terms of `foundations/glossary.md` against the seven files by a whole-word search: the terms that occur are "agent's way to the running product", "entry", "foundation", "gate" and "read off".
- "agent's way to the running product" is used as its entry gives it (the means through which an agent checks behaviour a user sees in a running product); the gloss added in `research.md` ("the logs, the interface or the development data") names its three matters and does not widen it.
- "entry" and "foundation" are used as defined (`SKILL.md`: "the definition's foundation entries"; "the product's foundation").
- "gate": the text says "readiness gate" and "the gate has approved", the same use as in the unchanged old text and in the template. The glossary defines "the gate" as the command that runs all tests, so this is a use against the entry, but it stands unchanged in meaning from `525cde1` and in `definition_template.md`, and the task's *Out of scope* leaves the template alone; I did not reword it. Named here for the human, as the reviewer's "read off" at `research.md:22` against `glossary.md:121-123` is: that text is the old text, unchanged in meaning.
- "read off": as above, not reworded.
- New words of the change, "leader" and "research agent" (`research.md`, `SKILL.md`, `settle.md`), are used in their ordinary meaning and defined in `research.md` where the reader has nothing else.

## Part-map changes

none.

## Projected entries

none; the task carries none.

## Rows of *Settlements to record*

none; the task's section reads `none` and `Candidates: 6 shown, 0 accepted`.

## Checks

None run in this step: no file changed. (`git status --short` exit 0, empty.) Not run: `python -B elements/common/foundation_check.py`, because no foundation file changed; the full gate is the orchestrator's and passed on `c7a4008`.

## Searches not found or unclear

none
