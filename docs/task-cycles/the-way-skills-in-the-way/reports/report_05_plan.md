# Report 05 — planner (saved by the orchestrator from the returned text)

Plan at `plan.md`; Superpowers 6.4.1 `writing-plans` read from its installed path with
`plan-document-reviewer-prompt.md`; self-review run; execution handoff not run. Repository unchanged
(`git status` clean).

Foundation step (WAY-69, N1–N5): element agents read skills from the process root; four facts first, then their
watches by a separate agent, then WAY-09, WAY-27, WAY-127, then the invariants, then the part map, then the check
author (only the sentence, method and flow entry; never the generator or spec §4.1–4.3). Deliberate break by Task
3's reviewer.

Checks the planner ran: read-only fingerprint script (in the plan, Task 0; to be saved at `.runs/stale_refs.py`)
reusing the guards' parsers and `relation-model/fingerprint.py` — at base 372 references, 0 stale; with one word of
WAY-09 changed in a copy, all six WAY-09 references flagged. Generator and its 11 tests run in a scratch clone: all
pass; 22 byte-identical entry points; equality test, gate and installation tests pass; installer sentence change
with its test passes. Part-map guard reproduced in the clone: with the new patterns and no entry points, exactly
two "matches no file" errors. Point-6 PowerShell with N1 fix parses in Windows PowerShell 5.1 (0 errors), not run.
All ten fact passages on the live pages today, with typographic apostrophe ’.

Units: 0 pre-flight and fingerprint script; 1 foundation step (1.1 facts → 1.2 watches → 1.3 decisions → 1.4
orchestrator answers → 1.5 invariant sentence → 1.6 part map → 1.7 gate test → 1.8 guards and three commits); 2
generator and tests (TDD); 3 22 entry points, equality test, deliberate break; 4 nine skill paragraphs and
`way_of_working.md`; 5 `AGENTS.md`, `README.md`; 6 installer sentence and test; 7 partial checks, unchecked list,
final review.

Questions and provisional answers: N5 — the sentence states every property the check asserts, literal strings
included; the invariants agent words the sentence from a property list (the plan carries the generator's code);
watches by a fresh agent; WAY-127 *Review when* `none`; generator root = repository of the script; entry-point
paragraphs one line each, folded YAML or BOM stop the generator; two known red checks after the foundation commit
(part-map pattern errors, flow test) until Task 3; equality test cites no invariant; "entry point" vs glossary
`entry` treated as no second meaning unless the decisions agent's search finds otherwise.

Spec points that cannot run as written: §8 stale WAY-09/WAY-27 fingerprints (script replaces it as a partial
check); §8 glossary guard rationale ("22 new files") does not apply — it still runs because `way_of_working.md`
changes; §8 part-map patterns reach files only after Task 3. Open for the foundation step's search: WAY-76 may split
`claude-code-nested-skills`; WAY-52 on files generated for agents; whether WAY-09's sentence on what
`agent-instructions/` holds admits a generator script.

Orchestrator note: `.runs/stale_refs.py` did not exist in the task worktree after the planner returned (the planner
used a scratch clone); Task 0 writes it.
