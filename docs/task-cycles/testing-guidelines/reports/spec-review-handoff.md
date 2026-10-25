# Handoff — spec reviewer (write-spec), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You are the reviewer of the spec and did not write it. Follow the project skill
`the-way-write-spec` (read `task-cycle/spec/SKILL.md` in this worktree whole, and what it names) in
the role of the spec's reviewer. Read only; write nothing but your report. Questions go to the
orchestrator in your report, never to the human. Return `PASS` or `FAIL` as the method gives.

## Worktree and paths

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  base `4302f72ba638fb222fc3d9de73decacdf7ca6682` (`foundations`). The-way is the top-level
  repository; integration route `agent-instructions/README.md`.
- Frozen task (read whole): `.runs/task-cycles/testing-guidelines/task.md`.
- Spec to review: `.runs/task-cycles/testing-guidelines/spec.md`.
- Designer's report (its ways weighed and concerns): `.runs/task-cycles/testing-guidelines/reports/design.md`.
- Write your full report to: `.runs/task-cycles/testing-guidelines/reports/spec-review.md`.

## Answers of step 4 and orchestrator's rulings the spec follows

- Trust boundary: yes — `installation/install.py` (part `installation`). Check that the spec says
  how a crafted product file the installer reads cannot make the change write outside its own files.
- Irreversible operation: no.
- C3 (row 25 of *Settlements to record*): no separate decision, because
  `elements/decisions/template.md:40-42` (WAY-19) forbids a "what do we take from X" decision; each
  borrowed source goes to *Based on* of the decision carrying the piece, each piece left out to
  *Rejected* of the decision whose question it answers; 10xDevs in prose without link (WAY-27).
  The request names row 25 as tied to those decisions.
- C4 (row 12): the decision carries WAY-200's split; `product-guidelines/reading.md` gains one
  bullet shaped like WAY-216's; the testing skill mirrors the coding skill's mode for a new kind and
  adds nothing beyond it.

These rulings are the orchestrator's; you may still find that the spec applies them wrongly or that
they contradict a decision — say so.

## What to check

Check the spec against the whole frozen task — every item of *To do*, every answered question,
every row of *Settlements to record*, *Out of scope* — and against the foundation entries below:
coverage, fidelity to the task's meaning (no row written with another meaning, nothing widened),
contradictions with current decisions, and whether each design choice the spec makes is weighed and
sound. Verify the designer's factual claims about the code where a choice rests on them (e.g. the
installer evidence at `installation/install.py` and `installation/test_install.py:278-319`, the
test counts of entry points, the coding skill's mode "A new kind").

## What to read

- The task's sources, outside the repository included (read only):
  `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_testow/`
  (`raport_wytyczne_testow.md`, `propozycja_szablonu_i_skilla.md`) and
  `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Przejście 10xDEVS/mapa_pakietu_10x.md`, section m3l1.
- Analogous artifacts, whole: `product-guidelines/template.md`, `product-guidelines/reading.md`,
  `product-guidelines/coding/template.md`, `product-guidelines/coding/SKILL.md`,
  `product-guidelines/styleguide/template.md`, `product-guidelines/styleguide/SKILL.md`,
  `elements/decisions/template.md`.
- Foundation, each entry whole: decisions WAY-08, WAY-13, WAY-16, WAY-19, WAY-27, WAY-48, WAY-51,
  WAY-90, WAY-100, WAY-121, WAY-167–WAY-174, WAY-198–WAY-200, WAY-209, WAY-212–WAY-218, WAY-228,
  and any other the spec names or edits; glossary (`foundations/glossary.md`, whole); part map
  (`foundations/part_map.md`, whole); invariants `skill-entry-points`, `skill-rule-source`,
  `installation-claude-guidance`; environment fact `impossiblebench-test-modification`.

## Report

Return a short message: the report's first line (`PASS` or `FAIL`), the report's path, and a
one-line check result. Grade each finding as the method gives, with its place in the spec.
