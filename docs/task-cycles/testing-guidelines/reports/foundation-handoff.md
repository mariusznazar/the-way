# Handoff — foundation entries (make-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You write the plan's *Foundation entries* — the cycle's foundation step — before
slice 1. Follow the project skill `the-way-make-change` (read `task-cycle/change/SKILL.md` in this
worktree whole), and read whole the paragraph "The foundation step writes the entries the task
carries …" in section "Execute, verify and review" of `task-cycle/skill/SKILL.md` (lines 232–250),
which holds this stage. Write each entry through the project skill of its element, read whole with
what it names: `the-way-record-decision`, `the-way-record-glossary-term`,
`the-way-record-environment-fact`. Each element skill's step 1 selects what you read of the
foundation, and its step 2 runs the search of the whole foundation once the entry is settled
(WAY-33). Write no code and nothing outside `foundations/`; no template, skill or test.
Questions go to the orchestrator: return `questions`, or `blocked` for a question the foundation
step leaves to the human (an entry that would change an approved decision's meaning beyond the
task, a row whose meaning cannot hold, a value neither the row nor the work gives). Never write a
row with another meaning.

## Turns

- **Turn 1 (now):** WAY-231 to WAY-243, and the environment facts their *Based on* needs (WAY-232,
  and WAY-236 only where it rests on WebTestBench). Commit, then return with your report.
- **Turn 2 (on resume):** WAY-244 to WAY-250, the five decisions edited in place (WAY-228, WAY-174,
  WAY-215, WAY-218, WAY-214), and the glossary term `exemplar`. Commit, then return.

## Worktree and commits

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`,
  base of slice 1 `4302f72ba638fb222fc3d9de73decacdf7ca6682` (HEAD at dispatch). The-way is the
  top-level repository; `agent-instructions/README.md` gives its route ("Make the change": the
  search of the whole foundation once the entry is settled; a finding you cannot settle by
  correcting an entry goes to the orchestrator).
- Commit with explicit paths (`git add <file> …`, never `-A` or `.`), English messages in the style
  of `git log`; check `git log -1 --format='%h %ae'` shows `mariusznn@gmail.com`. No push.
- Report: `.runs/task-cycles/testing-guidelines/reports/foundation.md` (turn 2 appends its section).
  For every entry keep one sentence of its meaning in Polish (the task document's language) for the
  request (WAY-114).

## Answers of step 4 and the cycle's rulings

- Trust boundary: yes (`installation/install.py`, slice 5) — no bearing on your entries.
- Irreversible operation: no.
- C3: row 25 gets no decision; its sources go to *Based on*, its pieces left out to *Rejected* of
  WAY-233, WAY-235, WAY-236, WAY-237, WAY-238, WAY-241, WAY-243 as the spec gives; 10xDevs described
  in prose without a link (WAY-27); Limen in WAY-237's *Rationale*.
- C4: WAY-242 carries WAY-200's split (audit proposes where a level has tests; the task writing a
  level's first test designates it, approved in refinement).

## What to read

- The whole frozen task: `.runs/task-cycles/testing-guidelines/task.md`.
- The whole reviewed spec: `.runs/task-cycles/testing-guidelines/spec.md` — its *Constraints*
  (the "Quotations" table above all), *D1*, *D3*, *D4*, *D9* and *Foundation entries* bind your
  entries; *Left to the maker* says the wording is yours within the meanings.
- Sources outside the repository (read only): every quotation an entry carries is read again by you
  on the source at a fixed address and copied from there, never from the research notes; a source
  you cannot reach stops you — ask the orchestrator. Research for orientation:
  `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/research_wytyczne_testow/raport_wytyczne_testow.md`
  and `propozycja_szablonu_i_skilla.md`.
- Foundation: the decisions of the task's *Decisions in play* (WAY-08, WAY-13, WAY-16, WAY-48,
  WAY-51, WAY-121, WAY-167, WAY-168, WAY-171, WAY-172, WAY-173, WAY-174, WAY-198, WAY-199, WAY-200,
  WAY-209, WAY-212, WAY-213, WAY-214, WAY-215, WAY-218, WAY-228), each whole, and those each
  element skill's step 1 adds; WAY-05, WAY-07, WAY-19, WAY-21, WAY-27, WAY-80, WAY-90 for form;
  glossary and part map whole; environment fact `impossiblebench-test-modification`.

## The plan's section, copied word for word (`plan.md`, "## Foundation entries")

## Foundation entries

Written before slice 1 by one agent through the skill of each element, as the spec's *Foundation
entries* and *D9* give them (numbers as the spec proposes them; an entry gets its number when
written). The new decisions stand at the end of the log after WAY-230, in this order. The sources
of their *Based on* are re-read on the page at a fixed address, never copied from the research
notes (spec *Constraints*, "Quotations").

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| WAY-231 (new) | decision | rows 1 and 15; spec *New decisions* | Slices 1, 2, 3 |
| WAY-232 (new) | decision | row 2 | Slices 1, 3 |
| WAY-233 (new) | decision | row 3; row 25 (Google ch. 12, Open Mercato in *Based on*; the red replacement in *Rejected*) | Slices 1, 3 |
| WAY-234 (new) | decision | row 4 | Slice 1 |
| WAY-235 (new) | decision | row 5; row 25 (OWASP in *Based on*) | Slices 1, 3 |
| WAY-236 (new) | decision | row 6; row 25 (Anthropic in *Based on*) | Slices 1, 3 |
| WAY-237 (new) | decision | row 7; row 25 (10xDevs described and Limen named in *Rationale*) | Slices 1, 3 |
| WAY-238 (new) | decision | row 8; row 25 (project test plan, risk map, proportions in *Rejected*) | Slice 1 |
| WAY-239 (new) | decision | row 9 | Slice 1 |
| WAY-240 (new) | decision | row 10 | Slices 1, 3 |
| WAY-241 (new) | decision | row 11; row 25 (Google ch. 13 in *Based on*) | Slices 1, 3 |
| WAY-242 (new) | decision | row 12; ruling C4 | Slices 1, 3, 4 |
| WAY-243 (new) | decision | row 13; row 25 (Google ch. 11 in *Based on*; quarantine in *Rejected*) | Slice 1 |
| WAY-244 (new) | decision | row 17 | Slices 3, 4 |
| WAY-245 (new) | decision | row 19 | Slice 3 |
| WAY-246 (new) | decision | row 20 | Slices 1, 3, 4 |
| WAY-247 (new) | decision | row 21 | Slices 2, 3, 4 |
| WAY-248 (new) | decision | row 22 | Slice 3 |
| WAY-249 (new) | decision | row 23 | Slice 3 |
| WAY-250 (new) | decision | row 24 | Slice 3 |
| WAY-228 (edited in place) | decision | row 14; spec D4 | Slices 1, 2, 3 |
| WAY-174 (edited in place) | decision | row 18; item 5 | Slice 3 |
| WAY-215 (edited in place) | decision | row 16; item 4 | Slices 3, 4 |
| WAY-218 (edited in place) | decision | row 16; item 4 | Slice 4 |
| WAY-214 (edited in place) | decision | item 4; spec *Decisions edited in place* | Slice 4 |
| `exemplar` (edited in place) | glossary term | spec D1 | Slices 1, 3 |
| a fact for WAY-232 (LLM-written oracles capture the implementation; Konstantinou et al.), and one for WAY-236 (WebTestBench) only where that decision rests on it | environment fact | spec *Environment facts*; WAY-90 | WAY-232, WAY-236 (no slice's code) |
| row 25 | none of its own (ruling C3) | row 25 | carried by WAY-233, WAY-235, WAY-236, WAY-237, WAY-238, WAY-241, WAY-243 |

Part map, invariants, withdrawn identifiers: none (spec *Part map and invariants*).

Checks of the foundation step: `python -B elements/common/foundation_check.py` exits 0 and
`python -B gate/run_tests.py elements/common` exits 0 (its tests include the check of the-way's
own foundation).


## Checks and report

Run and report each with its command and exit code: `python -B elements/common/foundation_check.py`
(exit 0 at your head) and `python -B gate/run_tests.py elements/common` (the test directories of
the-way are agent-instructions, elements/common, gate, installation, instruction-files,
project-level, relation-model, task-cycle; the elements have no tests of their own), plus any check
an element skill names. Return a short message:
status, commits, a one-line check result naming what failed or did not run, and the report's path.
In the report: each entry with its meaning sentence, the search findings and what you corrected,
each quotation with the address and date you read it, every reach beyond this handoff, and concerns.
