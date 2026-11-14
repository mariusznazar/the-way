# Return report: task `resolve-gaps-two-meanings`

**Status:** done (nothing needed correcting)

## Commits

None. The head stays `187bbde`.

## What was compared

- **WAY-374** (written from row 1) against `project-level/task/skill/resolve_gaps.md` and the section "## 3. Resolve the gaps" of `project-level/task/skill/SKILL.md`: the sources searched, the conditions of a case, the example and the question of decision (WAY-113), the answer under *Questions to settle*, the glossary candidate judged by WAY-95, the ambiguity of the definition that changes it going to WAY-118, and "say nothing where nothing is found" stand alike in the entry and the skill after the fix. No departure.
- **Entries the task names** — WAY-100, WAY-113, WAY-95, WAY-99, WAY-118 — read in the author's step and compared with WAY-374's use of them: none is restated differently, none changes meaning. WAY-100 states the rule that a borrowed practice binds through a decision; WAY-374 is that decision, so no second entry.
- **Entries the search of the foundation found** (WAY-33 search made in the author's step, and a second look here at the decisions on refinement): WAY-134, WAY-154, WAY-155 (the answering agent makes an unanswered choice a question to the human with options, which the check's question is), WAY-109, WAY-112 (questions of a project definition, not of a task), WAY-313, WAY-314, WAY-315. No sentence of them states or contradicts the check.
- **Part map** `project-level`: its responsibility reads "the refinement of a task before its implementation cycle"; the check is part of it, no entry of the map changes. No file is added, so no *Files* or *Trust boundary* change.
- **Glossary:** WAY-374 and the skill text use no word in a meaning for which WAY-95 gives an entry; no entry written, no use corrected.

## Entries and places of settlements

- Row 1 -> decision WAY-374, written in the author's step; the place is the decision log.
- No source outside the product that the foundation lacks: the course (10xDEVS, lesson m2l2) is named in WAY-374's *Rationale* as the other adoptions (WAY-273, WAY-280) name theirs, with *Based on* `none`; it is no claim about agents or models or the behaviour of a tool that would call the decision into question, so no environment fact is written.
- No invariant: none is set by the task, a decision or the human.
- No choice that binds after the merge beyond row 1.
- No pair of examples to reduce: no test holds a sentence of WAY-374.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- No `gate/run_tests.py` directory run: no file was edited in this step.

## Working copies

None made; `.runs/author/` not created.

## Unread material

`task-cycle/skill/return_step.md` and `foundation_step.md` read whole. WAY-134's final lines, WAY-150's rest, WAY-154 and WAY-155 beyond the first paragraphs and *Verification*: read in part (the lines shown above), enough to compare with the check.

## Searches not found or unclear

None. A grep of `foundations/` for "gaps" and for decision headings with "refine", "question" or "task document" found no entry that lists what the step "Resolve the gaps" does.
