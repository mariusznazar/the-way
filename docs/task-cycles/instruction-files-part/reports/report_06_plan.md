# Report 06 — planner (returned as text, saved by the orchestrator)

Plan written to `plan.md` (2,489 lines) with Superpowers 6.4.1 `writing-plans`; nothing executed, committed or changed in the task worktree (`git status` clean). The code of the check script, its tests and the two helper scripts (`.runs/stale_refs.py`, `sources_check.py`) was run in a scratch clone and spliced into the plan word for word.

## Task list
- Task 0 (orchestrator): check both roots; write `.runs/stale_refs.py`; copy the five prototype files from af585e3 into `instruction-files/` with `skill/SKILL.md` moved to `SKILL.md`, check the bytes; the part-map agent writes the new part's entry; one commit.
- Task 1 (foundation step): 1.1 glossary term; 1.2 six facts (both fallback paths of spec §5.2 and the missing-archive case N7 returned as questions); 1.3 six watches by a separate agent; 1.4 number check, WAY-09 edit, WAY-127 narrowing (option A), WAY-128–133; 1.5 answers recorded, term's uses re-read; 1.6 two invariants plus seven fingerprint renewals; 1.7 part map (`agent-instructions` *Depends on*, flow *Parts*); 1.8 invariant checks by an agent that sees only the sentences, the methods, the template's "Test" section and a form file (WAY-69); 1.9 guards, element tests, fingerprint comparison, three commits.
- Task 2: entry points (2 created, 22 rewritten).
- Tasks 3–5: check script, test-first — 3 safe reading (crafted-input rows of §4.6); 4 dead-path and network-path fixes A and C; 5 pointed files, skill copies, root layout (B, D, R18).
- Task 6: `SKILL.md` in full, two README lines. Task 7: principles, exact edits. Task 8: Cursor measurement V1–V5 with the negative control, rules for rewriting `tool_loading.md`, the sentence if it cannot run. Task 9: checks of spec §8, deliberate breaks by the final reviewer, second WAY-33 search, acceptance grep, list of what stays unchecked.
- A table of every expected red result between steps; the human step after the merge copied for the request.

## Confirmed in scratch
Starting point: same blob hashes as af585e3; part-map guard 0 errors with the spec's entry; 28 prototype tests pass; gate and agent-instructions each one known failure. Generator: 22 "would change", 2 "would create"; afterwards gate (98), agent-instructions, part-map guard green. Fingerprint script: 379 references, 0 stale at base; a planted change to WAY-09 gives six STALE lines, to WAY-127 one. Intermediate guard wordings reproduced. Check script red→green: prototype→stage 3 fails 11, errors 7 of 45; 3→4 fails 10, errors 1 of 57; 4→5 fails 5 of 69; final 69 pass (one skipped on Windows, FIFO). Known inputs: on the-way only `AGENTS.md:20 _zadania\` WARN remains; the global file gives WARN for `scripts/locations.json`, INFO for the memory path; `loop2` loses the skill-dir note. Acceptance grep finds only the `.runs` skip-list entry. Links and junctions can be made in the scratchpad. `cursor-agent.cmd --version` reports 2026.10.01-e373342. `loop2` pins c64a607 (no `instruction-files/`), so the skill stops there. WAY-128–133 free on the tip. Element tests take about 4.5 minutes.

## Open questions
- O-P1: if a Cursor run stops on workspace trust, rerun V1–V4 with `--trust` (scratch); V5 never gets `--trust` and then counts as not run.
- 1.6: the drafted `instruction-file-imports` sentence spells out what the glossary term defines; provisional answer: use the term (P10), give the check author the glossary entry (P8).

## Deviations from the spec
P1 entry points right after the foundation step (gate red only Task 0→2); P2 part-map split (new part in Task 0, the rest in 1.7); P4 fix A's paragraph also ends at a list item, heading or table row; P5 root layout for every `CLAUDE.md` with an `AGENTS.md` beside it; P6 "imports a file that is not there" for every `@` import whose file is missing; P7 the skill's Place step 2 and three places in the principles reworded to match WAY-133.

Values read at their source when the step runs: fact passages and archived copies, the version of arXiv:2606.15828, the key of Claude Code's "Project instructions" setting, documentation addresses for `tool_loading.md`.
