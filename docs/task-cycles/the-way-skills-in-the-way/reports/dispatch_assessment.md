You are the independent assessor of one change to the-way's foundation and to an invariant test (WAY-10). You did not
write the change. Follow the critique skill at `C:\Storage\repos\the-way-process\elements\common\critique\SKILL.md` (read
it in full; this is its case "a change to an invariant test or to the foundation needs its independent assessment").

## Your material, and only this

Everything lies under `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\7d836947-fefd-4498-a36c-f4292adbafce\scratchpad\assess-76c3f3c\`:
- `change.diff` — the diff of the assessed range c64a607..76c3f3c; `change.stat`; `changed_files.txt` (47 files);
- `tree\` — the files of the assessed commit 76c3f3c (the whole repository at that commit: code, foundation in
  `tree\foundations\`, the invariant test `tree\gate\test_skills_reach_the_way_sessions.py`, the skills, the rules).
Read the target files in full where you judge an entry: `tree\foundations\decisions.md`, `invariants.md`, `part_map.md`,
`environment_facts.md`, `glossary.md`, the element templates and rules in `tree\elements\`, and
`tree\agent-instructions\README.md`. Do not read anything else — no task document, spec, plan, cycle record, reports,
prompts or other worktrees; they are the author's reasoning and are kept from you on purpose. The commit messages are
not part of your material either.

## What is assessed

The foundation entries and invariant tests the range adds or changes: decisions WAY-127 (new), WAY-09 and WAY-27 (edited
in place, before `main`, `agent-instructions/README.md` allows this; both changes of meaning go to the human at the merge);
invariants `skill-entry-points/1` (new), `outbound-link-reach/1` (edited), six *Derives from* renewals, `generated-overview/1`
(*Part*); four environment facts and their watches under `probes/`; the part map's `agent-instructions` part and flow
`skills-reach-the-way-sessions`; the gate test `gate/test_skills_reach_the_way_sessions.py` that checks
`skill-entry-points/1`. Judge them against the code of the same commit (the generator `agent-instructions/skill_entry_points.py`,
the 22 entry points, the skills' paragraphs, `AGENTS.md`).

## Ask, per the skill

Purpose, evidence, cost, source fidelity (each fact's sentence against its quoted passages — you may fetch the pages it
cites), contradictions between entries and with the code, form against each element's template and rules. And name what
of the change can be cut, or that nothing can.

## Boundaries

Read-only. Write nothing; do not run commands that change files. You may run read-only commands (e.g. the format guards
or tests on `tree\`, git is not available there) and fetch the cited web pages. Do not use globally installed skills named
critique, refine-task, record-* or update-part-map.

## Return

Your full report as your final message: numbered observations, each with what you checked, where the evidence stands
(file:line in `tree\` or a quoted passage) and what would have to change, with severity (blocking / should change /
minor); an explicit line for each assessed group in which you found no concern; then "What can be cut".
