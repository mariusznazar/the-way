You are the foundation agent applying the settlement of an independent assessment in one the-way task cycle. The
orchestrator dispatched you; questions go to the orchestrator; nothing you write is anyone's approval.

Read the settlement at the end of
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\assessment.md` ("Settlement
(orchestrator)"). Apply exactly these three changes, following each element skill from the PROCESS ROOT
`C:\Storage\repos\the-way-process\elements\<element>\skill\SKILL.md` (skip "Installed globally … resolve it first"; never a
global skill, never the task worktree's copy), in the task worktree `C:\Storage\repos\the-way-skills-self`:

1. `foundations/decisions.md`, WAY-127/1 *Rationale*: add one clause that the entry point's own directory, which Codex
   lists with each skill (`codex-skill-paths`), lets the first product check find a product's submodule. Rationale only;
   the fingerprint must stay 4439a64a.
2. `foundations/decisions.md`, WAY-27/1 *Verification*: remove the violates example "an entry's *Origin* points to a task's
   description in the private notes" (the existing "*Origin* points to a private note" covers it). Fingerprint must stay
   fb27e458.
3. `foundations/part_map.md`, `agent-instructions`, the not-detected failure mode about the-way's own entry point in a
   product: remove the whole parenthetical bracket (the `${CLAUDE_SKILL_DIR}` and Codex clauses); keep "where the agent
   knows neither the entry point's path nor the session's working directory".

Write only those two files; commit nothing. Run the decisions and part-map guards (`--base none`, `--merge-onto none` where
available) and `python -B -I .runs/stale_refs.py` (must end `stale 0`; print WAY-127 and WAY-27 fingerprints). Return as
text: each change as written, the guard results, the comparison's last line, the two fingerprints, and the updated Polish
sentence for the part's failure mode (WAY-114).
