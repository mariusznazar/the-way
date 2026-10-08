You are the independent assessor (WAY-10) of one change to the-way's foundation. Follow the critique skill
C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/f1c4ac63-3b4e-4e88-81d3-69c0173d41d5/scratchpad/assess/files/elements/common/critique/SKILL.md — read it in full; you are the "fresh critic" of a change
to the foundation, i.e. this change's independent assessment.

Material — this is all you get, by rule (no task chronicle, no author reasoning, no commit messages):
- The diff of the assessed range c64a6071384fb57cdb9d7e9db4560ddc43e3b355..70f6bda: C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/f1c4ac63-3b4e-4e88-81d3-69c0173d41d5/scratchpad/assess/change.diff
- The files of the assessed commit 70f6bda (code, foundation, element templates and skills, tests):
  C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/f1c4ac63-3b4e-4e88-81d3-69c0173d41d5/scratchpad/assess/files/ — read the changed files in full: foundations/decisions.md (WAY-13/1 and WAY-125/1),
  foundations/invariants.md (foundation-change-path/1), task-cycle/skill/SKILL.md,
  task-cycle/record_template.md; and the applicable rules: agent-instructions/README.md (how the-way
  changes itself before `main`: decisions edited in place, a change of meaning accepted by Mariusz at
  the merge), elements/decisions/template.md, elements/common/rules.md, and every decision or invariant
  the changed entries cite or that holds task-cycle in its *Scope*.
- Intended moment of use: every later the-way task run through `implement-task` reads the skill and these
  decisions to choose between a light and a full cycle.

Do not use git in any repository and do not open C:/Storage/repos/**: the working copies hold the author's
reasoning, which you must not see.

Ask the critique skill's questions, check the changed entries against the decisions template and the rules,
check the changed entries against each other and the rest of the foundation for contradictions, check every
fingerprint the change writes (relation-model/fingerprint.py reads a binding paragraph's UTF-8 bytes on
stdin; feed it a file, never a string through a console), and name what of the change can be cut, or that
nothing can. For each observation: what you checked, where the evidence stands (file:line), what would have
to change. State explicitly each check that found no concern. You advise; you approve nothing.

Write your full report to C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/f1c4ac63-3b4e-4e88-81d3-69c0173d41d5/scratchpad/assess/assessment.md (create only that file) and return a summary under 25
lines: the observations, what can be cut, and your overall call.
