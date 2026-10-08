# Report 05 — spec revision 2 (design agent, returned as text, saved by the orchestrator)

Applied N1–N8 to `spec.md` (only file written), added §15; stopped before `writing-plans`.

- **N1:** the definition is the glossary term **"repository instruction file"**, WAY-96 noun form, written through `record-glossary-term` before the decisions (§5.0, §5.8, §7). WAY-128 loses its defining sentence; WAY-129–133 lose `derives from WAY-128` and keep `derives from WAY-100@e7a74a18`; decisions and invariants say "the-way's repository instruction files"; §5.9 gains WAY-32, WAY-95–97.
- **N2:** product check `git -C <repository under review> ls-files --stage -- ':/.the-way'`; skipped for `--file`-only review; a directory outside git is no product; WAY-127's narrowing speaks of the repository under review and gains a complies/violates pair.
- **R18 edge (A20):** in a `CLAUDE.md` with no `AGENTS.md` beside it, `@AGENTS.md` gets no exemption — a `WARN`.
- **N3:** junction to a dedicated detached worktree `C:\Storage\repos\the-way-global` at the merged `foundations` tip; §5.4 gives the commands (`git worktree add --detach`, `cmd /c rmdir`, `mklink /J`, moving the worktree after each later merge); A's cost in Q-M1 is that upkeep; O1 names the new target.
- **N4:** V5 in `C:\Storage\repos\the-way-process`, negative control outside `C:\Storage`, `--mode ask --sandbox enabled`, answers limited to marker phrases and first headings, nothing below `.runs/`; O2 and path 1 of §5.2 recorded as settled.
- **N5:** WAY-133's complies example replaced; one reading of "a mechanism that runs without the agent choosing to" (runs on its own, not by hand); `AGENTS.md:13–15` is a WAY-133 finding as well as a WAY-128 one.
- **N6:** WAY-129's first sentence states the present state ("the-way's repository instruction files hold no `@` import other than…"), matching `instruction-file-imports`.
- **N7:** a page with no archived capture is path 1 of §5.2 or a step-4 question of the facts skill.
- **N8:** WAY-129 "a pointer … names the file"; WAY-131 applies where the skill or a change's request says a rule works; fix A's test counts phrase tests per paragraph, falling back to the ratio of run times at 64 KiB and 1 MiB.

Choices to confirm: the word (A16), which the glossary skill or guard may rename; the `Not` field draft "skill". Nothing unapplied; no new questions.
