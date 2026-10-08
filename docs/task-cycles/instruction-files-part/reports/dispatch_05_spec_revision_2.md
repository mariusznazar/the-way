# Dispatch 05 — spec revision 2 (task cycle step 7)

The re-check (`reports/report_04_spec_recheck.md`, read it in full) returned "approved after fixes"
with new findings N1–N8. Rulings, all accepted; apply them to `spec.md` (same boundaries as before)
and add §15 "Changes in revision 3, by ruling". Return a short report as text.

- **N1:** the definition becomes a glossary term written through `record-glossary-term` (process root
  `elements/glossary/skill/SKILL.md`; form of WAY-96; pick the term so it reads as the foundation would
  write it in running text, WAY-93); WAY-128–133 use it (WAY-97) and lose `derives from WAY-128`; keep
  each decision's `derives from WAY-100@e7a74a18`. Revise §5.0, §5.8, A16, O6 and the order of work
  (the term is written before the decisions that use it).
- **N2:** as the reviewer's fix; add the complies/violates pair to the WAY-127 narrowing's
  *Verification*; the R18 edge case (a `CLAUDE.md` with no `AGENTS.md` beside it, `@AGENTS.md` on a
  later line) — decide and say.
- **N3:** the human step after the merge points the junction at a dedicated detached worktree kept at
  the merged `foundations` tip (name it, e.g. `C:\Storage\repos\the-way-global`, with the exact
  commands: `git worktree add --detach`, `cmd /c rmdir` of the old junction, `mklink /J`), moved by the
  human after each merge that changes `instruction-files/`; Q-M1 states that upkeep as A's cost instead
  of "uncommitted edits".
- **N4:** as the reviewer's fix: V5 in `C:\Storage\repos\the-way-process`, a negative control started
  outside `C:\Storage`, `--sandbox enabled` and `--mode ask`, nothing below `.runs/` involved. The
  orchestrator settles O2: the measurement may run on the logged-in Cursor account; the global
  `CLAUDE.md` already reaches Cursor in every Cursor session the user starts under `C:\Storage`
  (that is what the `C:\Storage\AGENTS.md` link is for), so V5 sends nothing Cursor does not already
  receive; the answer asked of the session is limited to marker phrases and the first heading of each
  loaded file. Path 1 of §5.2 (`claude -p` on the user's Claude Code account, scratch fixtures with
  marker phrases only) is settled the same way.
- **N5, N6, N7, N8:** as the reviewer's fixes. For N7: a page without an archived copy is path 1 of
  §5.2 or the facts skill's question, never a silent form. For N8's timing test: compare operation
  counts or the ratio of run times at two input sizes.
