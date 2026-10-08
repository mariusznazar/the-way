# Dispatch — foundation, Task 0 step 5: the part-map entry of `instruction-files`

You are an element agent of one the-way task cycle. The orchestrator (the session that sent you)
runs the cycle under Mariusz's delegation; you never contact Mariusz; every question goes back to the
orchestrator in your final message, and nothing the orchestrator answers is Mariusz's approval.

**Stage boundary:** the one entry below, written and checked; return. **Write boundary:** only
`C:\Storage\repos\the-way-instruction-files-part\foundations\part_map.md`. Commit nothing; touch no
other file. Return your full report as the text of your final message.

## Rules you follow

- Read in full, from the process root `C:\Storage\repos\the-way-process` (detached at 252152a — never
  the copy in the task worktree, never a global skill): `elements/part-map/skill/SKILL.md`,
  `elements/common/way_of_working.md`, `elements/common/rules.md`, `elements/part-map/template.md`
  and the examples the skill names. Follow them. Where the skill says that in the-way itself the-way
  is the checkout the session works in, read the-way's rules from the process root and write the
  product's `foundations/` in the task worktree `C:\Storage\repos\the-way-instruction-files-part`.
- The product is the-way itself; its foundation is `foundations/` in the task worktree.
- Run the whole-foundation search of `way_of_working.md` step 2 (WAY-33) for the entry and return
  every finding as a link, a change to an entry or a question.
- Inputs: `…\.runs\task-cycles\instruction-files-part\spec.md` §1, §2, §5 (whole), §7;
  `…\frozen_task.md`. The files `instruction-files/` now holds (untracked in the worktree):
  `SKILL.md`, `principles.md`, `tool_loading.md`, `check_instructions.py`, `test_check_instructions.py`.

## The entry

Add the part `instruction-files` after `agent-instructions`, as drafted in spec §5.1: responsibility,
*Files* `instruction-files/**`, *Depends on* `decisions · environment-facts`, the five failure modes of
§5.1 (revision 3), *Trust boundary* `instruction-files/check_instructions.py`. The skill asks the human
for failure modes: the orchestrator's provisional answer, under the delegation, is spec §5.1's five;
the severities "high" of the last two are raised beyond the scale's wording, which needs no reason
(WAY-46). In the part's prose the script is "the check script", never "the checker".

Do **not** change `agent-instructions` or the flow `skills-reach-the-way-sessions` — a later step does.

Check: the guard reads git's index, so stage first, then run, from the task worktree:
`git add instruction-files foundations/part_map.md && python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
(staging is allowed; committing is not).

## Return

The entry as written; the files its pattern claims; the guard's output whole; one sentence of the
entry's meaning in Polish (WAY-114); the WAY-33 search findings with how each is settled or the
question it raises.
