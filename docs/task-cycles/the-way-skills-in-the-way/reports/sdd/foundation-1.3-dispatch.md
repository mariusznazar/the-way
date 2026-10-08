You are the decisions agent of the foundation step of one the-way task cycle (`implement-task`). The orchestrator
dispatched you. Mariusz (the task owner) delegated intermediate choices to the orchestrator; questions go to the
orchestrator, never to Mariusz; nothing you write is his approval (*Approved by* carries the merge placeholder).

Read this first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\foundation-1.3-brief.md`.
Also read: `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md` §1, §2, §5, §7;
`…\reports\report_04_spec_recheck.md` (amendments N1–N5); `…\frozen_task.md`;
`…\reports\report_06_foundation_1_1.md` (what the facts agent wrote and found).

Values from earlier steps the brief cannot know:
- the four facts now in `foundations/environment_facts.md` and their fingerprints: `claude-code-project-skills@a06eaca7`,
  `claude-code-nested-skills@4dd3d448`, `codex-repository-skills@7db28f98`, `codex-skill-paths@5b5b6c79`;
- `WAY-44@2f2b6227`;
- fingerprints are computed by `python -B -I .runs/stale_refs.py <NAME>` from the worktree root, and
  `python -B -I .runs/stale_refs.py` compares every reference (read-only partial check).

Orchestrator answers to questions already raised (provisional, under the delegation):
- The facts agent's findings 2–5 do not change WAY-127's content; WAY-127 rests on the four facts only.
- Decision number 127 is provisional; use it.
- The two edits (WAY-09, WAY-27) change the meaning of approved decisions; write them on the branch anyway (WAY-30 route:
  the request is a blocked draft asking Mariusz). Keep each change to the smallest wording that delivers it.

Skill: follow `C:\Storage\repos\the-way-process\elements\decisions\skill\SKILL.md` (the PROCESS ROOT at c64a607) with the
files it names there. Where it says "Installed globally … resolve it first", skip that: the-way is
`C:\Storage\repos\the-way-process`. Never a globally installed skill, never the task worktree's copy of a skill.

Product: the task worktree `C:\Storage\repos\the-way-skills-self`. Write ONLY `foundations/decisions.md` there. Commit
nothing. Run the whole-foundation search (WAY-33) and the answers the brief asks for (the generator script under
`agent-instructions/` against WAY-09; "entry point" against the glossary term `entry`). If the search shows that a
glossary change is needed, return before writing the decisions.

Stage boundary: the three decision changes written and the decisions guard run (`--base none --merge-onto none`); stop
before invariants, part map or any other element.

Return your full report as text (the harness refuses report files from subagents): what you wrote (identifier, the
binding sentences as written, the fields), the new fingerprints of WAY-09, WAY-27 and WAY-127, the search findings each
as a link / change / question with your provisional answer, the guard summary and the output of
`python -B -I .runs/stale_refs.py` (expected: exactly seven STALE lines, six WAY-09 and one WAY-27 in invariants.md),
and one sentence in Polish of each change's meaning (WAY-114).
