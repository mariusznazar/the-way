You are the planner of one the-way task cycle (`implement-task`, step 8). The orchestrator dispatched you.
Mariusz (the task owner) delegated intermediate choices to the orchestrator; questions go to the orchestrator, never
to Mariusz, and nothing you write is his approval. One-off run on the-way itself before `main`; run brief:
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\run_brief.md` (read it).

## Method

Use Superpowers 6.4.1 `writing-plans`: read
`C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\writing-plans\SKILL.md`
and its linked files in full and follow its work. Adapter changes: write the plan to
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\plan.md` (not the default
location, not committed); your boundary is the finished plan — return BEFORE any execution and do not invoke the
skill's execution handoff or any other Superpowers skill. Where the skill asks the user, choose the smallest
reversible answer that fulfils the spec and list it under "Questions and provisional answers" in your report.

## Inputs (binding)

- Reviewed spec: `…\the-way-skills-in-the-way\spec.md`.
- Amendments the plan must carry (from the spec re-check, `reports/report_04_spec_recheck.md` — read it): N1 fix the
  PowerShell of §4.7 (`"${n}: …"`); N2 the fingerprint renewals are checked by the invariants guard only with
  `--merge-onto`, so with `none` they stay unchecked — the plan computes the new WAY-09 and WAY-27 fingerprints with
  `relation-model/fingerprint.py` and compares every `Derives from`/relation reference by hand, reported as a partial
  check; N3 `outbound-link-reach` stays `/1` (WAY-57, no main branch), sentence as proposed in report 04 or a
  narrower equivalent; N4 WAY-127 relations and *Based on* carry fingerprints; N5 the `skill-entry-points` sentence
  states everything the citing test asserts (or the test asserts only what the sentence states).
- Frozen task `frozen_task.md`; foundation and code in the task worktree `C:\Storage\repos\the-way-skills-self`
  (branch `task/the-way-skills-in-the-way` at c64a6071384fb57cdb9d7e9db4560ddc43e3b355); integration route
  `AGENTS.md`, `agent-instructions/README.md`.
- The cycle skill at the process root `C:\Storage\repos\the-way-process\task-cycle\skill\SKILL.md` — read the
  paragraph before step 9 (the foundation step) and steps 9–11; the plan must fit them.

## What the plan must arrange

1. **Foundation step first** (before dependent implementation): every entry of spec §7, written by agents that
   follow the-way's element skills read from the PROCESS ROOT `C:\Storage\repos\the-way-process\elements\<element>\skill\SKILL.md`
   (and `elements/common/way_of_working.md` there) — never globally installed skills, never the task worktree's copy,
   which this task edits. *Approved by* of new or changed decisions: `Mariusz, merge of <request link>` (placeholder
   swapped at step 12). Set every *Review when*. Include the whole-foundation search for unlinked effects (WAY-33) and
   the guards with `--base none` / `--merge-onto none`.
2. **Three agents for the invariant (WAY-69):** the invariant's sentence (foundation-step agent), its check — the
   `gate/` critical-flow test citing `skill-entry-points/1` — written by a different agent given only the sentence and
   its method, never the generator's design or code; the code (generator, entry points) by implementers. The check is
   read-only during implementation; if implementation needs it changed, the plan returns to the foundation step.
   The watches of the four facts are part of the foundation step.
3. **Implementation units** for `subagent-driven-development` (fresh implementer + reviewer per unit, TDD for behaviour
   changes): generator and its tests in `agent-instructions/`; generated entry points; skill paragraphs and
   `way_of_working.md`; `AGENTS.md` (`## Skills`, `## Backlog`) and `README.md`; installer sentence and its test.
   Each unit with exact files, commands that actually run on Windows (Git Bash or PowerShell; `python -B`), expected
   results, and the commit message (English, the repository's style: `feat(<part>): …`, `chore(foundations): …`).
4. **Checks**: tests of every changed part (`python -B gate/run_tests.py <directory>` for `gate`,
   `agent-instructions`, `installation`, each `probes/<id>`), always `gate`, guards of every changed foundation file;
   reported as partial checks, never as the full gate. Name what stays unchecked.
5. **Not in the plan**: the request, the record pair, the independent assessment, the human step of point 6 — the
   orchestrator runs those (steps 11–12). The plan may name the exact text for the human step (spec §4.7 with N1).

## Write boundary

Only `plan.md`. Everything else read-only; no commands that change files (read-only git, `python -B` of read-only
scripts such as `relation-model/fingerprint.py` are fine).

## Return

Return as text (the harness refuses report files from subagents): summary (under 300 words), the plan's unit list
with dependency order, "Questions and provisional answers", and anything in the spec you found unimplementable.
