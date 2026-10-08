You are the foundation-correction agent for the final review's findings in one the-way task cycle. The orchestrator
dispatched you. Mariusz delegated intermediate choices to the orchestrator; questions go to the orchestrator; nothing you
write is his approval.

Read first: the final review, `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\report_16_final_review.md`
(Important 1 and 2, Minor 5). Rulings (provisional, under the delegation):

A. Important 2 — WAY-27 and `outbound-link-reach/1`: restrict the exception to where the pointer stands, not only what it
   points at. Use the reviewer's direction: WAY-27 keeps its original rule sentence ("Nothing in this repository points to
   a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in
   such a source is described in the entry instead of being pointed to.") and gains a second binding sentence: "The one
   exception is the place of its tasks, which only the `## Backlog` section of its root `AGENTS.md` names." (or a narrower
   equivalent you report). The *Verification* complies example stays; add a violates example: an entry's *Origin* points
   to a task's description in the private notes. `outbound-link-reach/1`: "No file git tracks contains a link into a
   repository that a reader not signed in to its host cannot open, or into a private note collection, other than the
   `## Backlog` section of the root `AGENTS.md` naming the place of tasks." (or a narrower equivalent); version stays `/1`
   (pre-main, WAY-57 unchecked with `--base none`); *Derives from* renewed to WAY-27's new fingerprint.
B. Important 1 — the code side is fixed by another agent (the generator will refuse a description that is not a safe plain
   YAML scalar; the gate check and the invariant stay unchanged). You record the remaining gap honestly in
   `foundations/part_map.md`, `agent-instructions`: a new failure mode such as "an entry point whose frontmatter a tool
   cannot parse — the session does not list that skill — high — not detected", with whatever the part-map template allows
   to say that the generator refuses such a description (if the template allows no such note, state the failure mode
   alone).
C. Minor 5 — WAY-127's *Rejected* reason for unprefixed names: reword it to the task's own reason (the prefix does not rely
   on how either tool settles two skills of one name), dropping the claim "in Claude Code a personal skill wins over a
   project skill", which no fact records. *Rejected* is not in the fingerprint; confirm.

Follow each element skill from the PROCESS ROOT `C:\Storage\repos\the-way-process\elements\<element>\skill\SKILL.md` with the
files it names (skip "Installed globally … resolve it first"; never a global skill, never the task worktree's copy of a
skill). Product: the task worktree `C:\Storage\repos\the-way-skills-self`. Write only `foundations/decisions.md`,
`foundations/invariants.md`, `foundations/part_map.md`. Commit nothing. Search the whole foundation (WAY-33) for effects.
Run the guards of the three files (`--base none`, `--merge-onto none` where available) and `python -B -I .runs/stale_refs.py`
(must end `stale 0`).

Return as text: each change as written (old and new for WAY-27 and the invariant), fingerprints old/new, guard results,
the comparison's last line, search findings, and one Polish sentence per changed entry (WAY-114), the WAY-27 and
`outbound-link-reach` sentences in full because they are the request's question.
