# Plan — the way: testy jako osobna dyscyplina wytycznych produktu

- Task: `.runs/task-cycles/testing-guidelines/task.md`
- Spec: `.runs/task-cycles/testing-guidelines/spec.md`
- Base: `4302f72ba638fb222fc3d9de73decacdf7ca6682`

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

## Slices

### Slice 1 — The template of the testing discipline

- **Goal:** `product-guidelines/testing/template.md` exists as spec D3 gives it: the opening on the
  pattern of the coding and styleguide templates, "Required form" with its fenced block (header,
  `## When to read`, `## Levels`, `## Rules` with the nine required rules in D3's order,
  `## Recipes`, `## Not tested on purpose`, `## Examples`, `## Where in code`), "What each section
  carries" and "Writing the file". Each rule and section cites the decision of the-way that sets it,
  as the foundation step wrote it (WAY-228, WAY-231–WAY-243, WAY-246). `### Test inputs and
  expected values` carries WAY-228 as edited, its property-test clause and the sentence on fixtures
  and builders the coding template holds today. The yes/no table of the research's section 1 stands
  in English under `### Choosing the level`, with its four questions about a property test, without
  the research's column of sources and without "red before the fix" (cut by Q14). Nothing of the
  Q14 cut list stands in the file; no proportion of levels; no command of a test tool.
- **Change:** `product-guidelines/testing/template.md`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:17-56` Need, To do
  `.runs/task-cycles/testing-guidelines/task.md:58-101` Questions to settle
  `.runs/task-cycles/testing-guidelines/task.md:103-112` Context
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/task.md:190-193` Out of scope
  `.runs/task-cycles/testing-guidelines/spec.md:59-136` Constraints
  `.runs/task-cycles/testing-guidelines/spec.md:139-163` D1. Words (open choice 1)
  `.runs/task-cycles/testing-guidelines/spec.md:164-183` D2. Where it lives (units)
  `.runs/task-cycles/testing-guidelines/spec.md:184-323` D3. The template of the testing discipline (product-guidelines/testing/template.md)
  `.runs/task-cycles/testing-guidelines/spec.md:324-351` D4. WAY-228 and the coding discipline
  `.runs/task-cycles/testing-guidelines/spec.md:533-572` D9. Rows onto the foundation
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `.runs/task-cycles/testing-guidelines/spec.md:645-659` Left to the maker
  `product-guidelines/template.md` · `product-guidelines/coding/template.md`
  `product-guidelines/styleguide/template.md`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:182-285` WAY-08 · WAY-09
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:1113-1141` WAY-48
  `foundations/decisions.md:1167-1211` WAY-51 · `foundations/decisions.md:2102-2124` WAY-100
  `foundations/decisions.md:2146-2170` WAY-102 · `foundations/decisions.md:2579-2678` WAY-120 · WAY-121
  `foundations/decisions.md:4390-5910` WAY-167–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:5992-6011` WAY-226 · `foundations/decisions.md:6036-6058` WAY-228
  · Foundation entries rows WAY-231–WAY-243, WAY-246, WAY-228 and the glossary term exemplar, as written
  · outside the repository, not measured: C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces
  pracy nad produktem/research_wytyczne_testow/raport_wytyczne_testow.md:25-63, section 1 "Poziom
  wybiera się po zepsuciu, nie po proporcjach piramidy" (the yes/no table)
  · guidelines: none — the-way has no guidelines directory
- **Model:** same — it words a long template of fifteen sections and renders the research's table
  in English, taking wording choices of its own within the spec.
- **Risk:** none
- **Checks:** prose; no test asserts the template. `python -B elements/common/foundation_check.py`
  exits 0 once the file is committed (every decision number it cites names an entry);
  `python -B gate/run_tests.py elements/common` exits 0; `git grep -n "^### " -- product-guidelines/testing/template.md`
  lists the nine required rules in D3's order; `git diff --check 4302f72 -- product-guidelines/`
  prints nothing.
- **Depends on:** Foundation entries (WAY-228, WAY-231–WAY-243, WAY-246, `exemplar`)

### Slice 2 — The coding discipline gives up the rule of tests

- **Goal:** `product-guidelines/coding/template.md` no longer holds `### Test inputs and expected
  values`: gone from the fenced block of "Required form", from the bullet on the order of the
  required rules (only the three standing checks remain, with their `none — <PREFIX-NN>`), and from
  "What each section carries"; where it introduces `## Kinds of code` and the form of a kind, it
  says a kind is code of the product other than its tests (WAY-231). `product-guidelines/coding/SKILL.md`
  loses the step-4 bullet on the rule of tests; its step 1's "kinds of code it already holds files
  of" excludes tests (WAY-231); "Where the skill works" gains that one task may carry the coding and
  the testing guidelines together, each skill leading its own matters (WAY-247). Its frontmatter
  `description` is unchanged. Nothing under `product-guidelines/coding/` names WAY-228 any more.
- **Change:** `product-guidelines/coding/template.md` · `product-guidelines/coding/SKILL.md`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:53-56` To do, items 3–6
  `.runs/task-cycles/testing-guidelines/task.md:84-86` Questions to settle, Pytanie 9
  `.runs/task-cycles/testing-guidelines/task.md:96-98` Questions to settle, Pytanie 13
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/spec.md:106-113` Constraints, From the code as it stands
  `.runs/task-cycles/testing-guidelines/spec.md:324-351` D4. WAY-228 and the coding discipline
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `product-guidelines/template.md`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:182-285` WAY-08 · WAY-09
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:1113-1141` WAY-48
  `foundations/decisions.md:1167-1211` WAY-51 · `foundations/decisions.md:2102-2124` WAY-100
  `foundations/decisions.md:2146-2170` WAY-102 · `foundations/decisions.md:2579-2678` WAY-120 · WAY-121
  `foundations/decisions.md:4390-5910` WAY-167–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:6036-6058` WAY-228
  · Foundation entries rows WAY-228, WAY-231, WAY-247, as written
  · created by Slice 1, not measured: product-guidelines/testing/template.md, where the rule now
  stands
  · guidelines: none — the-way has no guidelines directory
- **Model:** cheaper — it removes one rule and adds two clauses the spec settles.
- **Risk:** none
- **Checks:** `git grep -n "WAY-228\|Test inputs and expected values" -- product-guidelines/coding/`
  prints nothing (exit 1); `python -B agent-instructions/skill_entry_points.py` prints
  `entry points are current` (the description is unchanged); `python -B elements/common/foundation_check.py`
  exits 0; `git diff --check 4302f72 -- product-guidelines/coding/` prints nothing.
- **Depends on:** Slice 1 · WAY-228 · WAY-231 · WAY-247

### Slice 3 — The skill `maintain-testing-guidelines`, its entry points and the README

- **Goal:** `product-guidelines/testing/SKILL.md` exists as spec D5 gives it: frontmatter
  `name: maintain-testing-guidelines` and a one-line `description` starting "Use when", on the
  pattern of the two other skills and passing the generator's checks (spec *Constraints*, WAY-127
  bullet); the opening paragraphs, "Where the skill works" with its table, "What reaches the task
  document", "Orchestrated mode" and steps 0–5, mirroring `maintain-coding-guidelines` section for
  section with no mode or step the coding skill lacks — "A new level" mirrors its "A new kind"
  (ruling C4); reports under `.runs/testing/`. `README.md` names the testing discipline's directory
  in its `product-guidelines/` item and `product-guidelines/testing/` in "Using the skills" (spec
  D8). `python -B agent-instructions/skill_entry_points.py --write` has run and its output is
  committed: the two new entry points `the-way-maintain-testing-guidelines` and every existing one,
  whose list of sibling skills gains the name (invariant `skill-entry-points`); no entry point is
  edited by hand.
- **Change:** `product-guidelines/testing/SKILL.md` · `README.md`
  `.claude/skills/the-way-*/SKILL.md` · `.agents/skills/the-way-*/SKILL.md` (the generator's
  output: two new files and the forty existing ones it rewrites, none edited by hand)
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:17-24` Need
  `.runs/task-cycles/testing-guidelines/task.md:45-56` To do, items 2–6
  `.runs/task-cycles/testing-guidelines/task.md:58-101` Questions to settle
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/spec.md:59-136` Constraints
  `.runs/task-cycles/testing-guidelines/spec.md:139-163` D1. Words (open choice 1)
  `.runs/task-cycles/testing-guidelines/spec.md:164-183` D2. Where it lives (units)
  `.runs/task-cycles/testing-guidelines/spec.md:352-433` D5. The skill maintain-testing-guidelines (product-guidelines/testing/SKILL.md)
  `.runs/task-cycles/testing-guidelines/spec.md:525-532` D8. Entry points and READMEs
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `product-guidelines/coding/SKILL.md` · `product-guidelines/styleguide/SKILL.md`
  `product-guidelines/template.md` · `product-guidelines/reading.md`
  `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
  `elements/common/way_of_working.md:11-36` Critique before collective review; How a skill asks
  `elements/common/critique/SKILL.md` · `agent-instructions/skill_entry_points.py`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:6-93` WAY-01–WAY-03 · `foundations/decisions.md:182-318` WAY-08–WAY-10
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-757` WAY-27–WAY-29 · `foundations/decisions.md:819-849` WAY-33
  `foundations/decisions.md:955-979` WAY-38 · `foundations/decisions.md:1053-1086` WAY-44
  `foundations/decisions.md:1113-1141` WAY-48 · `foundations/decisions.md:1167-1211` WAY-51
  `foundations/decisions.md:1889-1912` WAY-89 · `foundations/decisions.md:2102-2124` WAY-100
  `foundations/decisions.md:2146-2170` WAY-102 · `foundations/decisions.md:2256-2277` WAY-107
  `foundations/decisions.md:2579-2734` WAY-120–WAY-122 · `foundations/decisions.md:2774-2819` WAY-124
  `foundations/decisions.md:2891-3138` WAY-127–WAY-133 · `foundations/decisions.md:3946-4013` WAY-154 · WAY-155
  `foundations/decisions.md:4390-5910` WAY-167–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:5992-6011` WAY-226 · `foundations/decisions.md:6036-6058` WAY-228
  · Foundation entries rows WAY-174, WAY-215, WAY-228, WAY-231–WAY-250 and the glossary term exemplar, as written
  · created by Slice 1, not measured: product-guidelines/testing/template.md (whole; the skill's
  step 0 reads it and its sections name it)
  · guidelines: none — the-way has no guidelines directory
- **Model:** same — it words a new skill of six sections and steps 0–5 from the spec, taking wording
  choices of its own.
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py --write` exits 0; then
  `python -B agent-instructions/skill_entry_points.py` prints `entry points are current` and no
  directory without a skill; `git status --short` before the commit shows only the two new
  entry-point directories, the forty rewritten entry points, `product-guidelines/testing/SKILL.md`
  and `README.md`; `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py gate`
  and `python -B gate/run_tests.py instruction-files` exit 0; `python -B elements/common/foundation_check.py`
  exits 0; `git diff --check 4302f72 -- product-guidelines/ README.md` prints nothing.
- **Depends on:** Slice 1 · Slice 2 (the coding skill it mirrors, as changed) · WAY-174 · WAY-215 ·
  WAY-228 · WAY-231–WAY-250 · `exemplar`

### Slice 4 — Reading, refinement and breakdown name the testing discipline

- **Goal:** the edits of spec D6. `product-guidelines/reading.md`: the opening sentence and "Name the
  affected work" add whether the work writes or changes a test; the first bullet of "Distinguish the
  gaps" counts test work in a product with no `guidelines/testing.md` as lacking discipline
  guidelines; a new bullet there, shaped like the WAY-216 bullet, gives the first test of a level
  whose recipe has an empty *Exemplar* its designation in the same task through
  `maintain-testing-guidelines`, with no separate exemplar wait (WAY-242); "Select and read" and the
  kind bullets stay, selection by *Applies to* alone (WAY-213 unchanged). `project-level/task/skill/SKILL.md`
  step 3 names `maintain-testing-guidelines` beside the two other skills, the first-level
  exemplar-test case beside the first-kind case, and one clause that a missing coding and a missing
  testing guidelines may be one prerequisite task (WAY-247). `project-level/plan/skill/SKILL.md`
  step 2 names missing testing guidelines beside the styleguide and the general coding file, one
  guidelines task carrying both coding and testing (WAY-247), and a level's first exemplar test with
  the task writing that level's first test (WAY-242). No skill's `description` changes.
- **Change:** `product-guidelines/reading.md` · `project-level/task/skill/SKILL.md`
  `project-level/plan/skill/SKILL.md`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:54-56` To do, items 4–6
  `.runs/task-cycles/testing-guidelines/task.md:81-86` Questions to settle, Pytanie 8 and 9
  `.runs/task-cycles/testing-guidelines/task.md:118-118` Questions carried to cycle, the third
  `.runs/task-cycles/testing-guidelines/task.md:158-188` Settlements to record
  `.runs/task-cycles/testing-guidelines/spec.md:434-476` D6. Reading, refinement and breakdown
  `.runs/task-cycles/testing-guidelines/spec.md:573-644` Foundation entries
  `elements/common/way_of_working.md:58-96` Reading the foundation
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:182-285` WAY-08 · WAY-09
  `foundations/decisions.md:387-425` WAY-13 · `foundations/decisions.md:450-473` WAY-16
  `foundations/decisions.md:668-694` WAY-27 · `foundations/decisions.md:955-979` WAY-38
  `foundations/decisions.md:1113-1141` WAY-48 · `foundations/decisions.md:1167-1211` WAY-51
  `foundations/decisions.md:1889-1912` WAY-89 · `foundations/decisions.md:2102-2170` WAY-100–WAY-102
  `foundations/decisions.md:2233-2819` WAY-106–WAY-124 · `foundations/decisions.md:2849-2945` WAY-126 · WAY-127
  `foundations/decisions.md:3140-3197` WAY-134 · `foundations/decisions.md:3316-3483` WAY-137–WAY-140
  `foundations/decisions.md:3506-3730` WAY-142–WAY-147 · `foundations/decisions.md:3792-4045` WAY-150–WAY-156
  `foundations/decisions.md:4315-5910` WAY-165–WAY-219 · `foundations/decisions.md:5936-5960` WAY-221
  `foundations/decisions.md:6036-6058` WAY-228 · `foundations/decisions.md:6119-6160` WAY-230
  · Foundation entries rows WAY-214, WAY-215, WAY-218, WAY-242, WAY-244, WAY-246, WAY-247, as
  written
  · guidelines: none — the-way has no guidelines directory
- **Model:** cheaper — it places in three files the clauses spec D6 settles.
- **Risk:** none
- **Checks:** prose; `python -B gate/run_tests.py project-level` exits 0;
  `python -B agent-instructions/skill_entry_points.py` prints `entry points are current`;
  `python -B elements/common/foundation_check.py` exits 0; `git grep -n "maintain-testing-guidelines" -- product-guidelines/reading.md project-level/task/skill/SKILL.md project-level/plan/skill/SKILL.md`
  shows each of the three files; `git diff --check 4302f72 -- product-guidelines/reading.md project-level/`
  prints nothing.
- **Depends on:** Slice 3 · WAY-214 · WAY-215 · WAY-218 · WAY-242 · WAY-244 · WAY-246 · WAY-247

### Slice 5 — The installer brings the skill to products

- **Goal:** spec D7. `installation/install.py` `SKILLS` holds `maintain-testing-guidelines` →
  `product-guidelines/testing/SKILL.md`, and nothing else in the installer changes. A new test file
  `installation/test_testing_guidelines_installation.py`, mirroring
  `installation/test_coding_guidelines_installation.py`, shows: the preview lists both new entry
  points and changes nothing; `--apply` creates them byte-identical, with the skill's description
  and the `.the-way/product-guidelines/testing/SKILL.md` path; every sibling entry point names
  `maintain-testing-guidelines`; the block names `the-way-maintain-testing-guidelines`; a repeated
  run changes nothing; and, in each of `.claude` and `.agents`, a foreign file, a directory and a
  non-UTF-8 file at `the-way-maintain-testing-guidelines/SKILL.md` stop the preview and `--apply`
  with a non-zero exit, the tree byte for byte as before and nothing staged (WAY-48). The exact
  counts of entry points in `installation/test_coding_guidelines_installation.py` and
  `installation/test_styleguide_installation.py` read 40, kept exact. `installation/README.md`
  names the skill in the table's list of entry points and in the list of what the tests check.
  `installation/test_install.py` stays as it is.
- **Change:** `installation/install.py` · `installation/README.md`
  `installation/test_testing_guidelines_installation.py`
  `installation/test_coding_guidelines_installation.py`
  `installation/test_styleguide_installation.py`
- **Read:** `.runs/task-cycles/testing-guidelines/task.md:45-52` To do, item 2
  `.runs/task-cycles/testing-guidelines/task.md:119-119` Questions carried to cycle, the fourth
  `.runs/task-cycles/testing-guidelines/spec.md:106-113` Constraints, From the code as it stands
  `.runs/task-cycles/testing-guidelines/spec.md:477-524` D7. Installer (open choice 4; item 2)
  `installation/test_install.py:15-40` · `installation/test_install.py:278-319`
  `foundations/part_map.md` · `foundations/invariants.md`
  `foundations/decisions.md:182-285` WAY-08 · WAY-09 · `foundations/decisions.md:387-425` WAY-13
  `foundations/decisions.md:450-473` WAY-16 · `foundations/decisions.md:668-694` WAY-27
  `foundations/decisions.md:851-879` WAY-34 · `foundations/decisions.md:955-979` WAY-38
  `foundations/decisions.md:1113-1141` WAY-48 · `foundations/decisions.md:1391-1425` WAY-61
  `foundations/decisions.md:1456-1483` WAY-63 · `foundations/decisions.md:1889-1912` WAY-89
  `foundations/decisions.md:2102-2124` WAY-100 · `foundations/decisions.md:2146-2170` WAY-102
  `foundations/decisions.md:2256-2277` WAY-107 · `foundations/decisions.md:2891-2945` WAY-127
  `foundations/decisions.md:3485-3504` WAY-141 · `foundations/decisions.md:4390-4458` WAY-167
  · guidelines: none — the-way has no guidelines directory
- **Model:** cheaper — one constant pair and a test copied from an existing example.
- **Risk:** trust boundary — `installation/install.py` (part `installation`): the new entry-point
  path in a product's `.claude/skills/` and `.agents/skills/`, and the block and sibling entry
  points it rewrites there.
- **Checks:** the failing test first: with `product-guidelines/testing/SKILL.md` committed (Slice
  3) and `SKILLS` not yet changed, the new test file and the counts of 40 are written and
  `python -B gate/run_tests.py installation` exits 1, the new test failing on the missing `CREATE`
  lines and the two counts on 38; after the `SKILLS` entry, `python -B gate/run_tests.py installation`
  exits 0 (the run takes about four minutes); `python -B elements/common/foundation_check.py` exits
  0; `git diff --check 4302f72 -- installation/` prints nothing.
- **Depends on:** Slice 3 (the skill file, committed: the installer's tests install the checkout's
  committed `HEAD`)

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome: an agent that writes or changes a test finds one source, `guidelines/testing.md`, written from a template of the testing discipline | Slice 1 · WAY-231 |
| To do 1 — the template `product-guidelines/testing/template.md`, its form, sections and every required rule (A1–A16) | Slice 1 · WAY-232–WAY-243, WAY-246, WAY-228 |
| To do 2 — the skill `maintain-testing-guidelines` in the full shape of the other two (B1–B6) | Slice 3 · WAY-244, WAY-245, WAY-248–WAY-250 |
| To do 2 — its entry points (`skill_entry_points.py --write`) and its entry in the installer's `SKILLS` and `installation/README.md` | Slice 3 (generator run, output committed) · Slice 5 |
| To do 3 — the rule of written-out values leaves the coding template and skill, WAY-228 moves and covers property tests, kinds of code exclude tests | Slice 1 (the rule arrives) · Slice 2 (the rule leaves) · WAY-228 · WAY-231 |
| To do 4 — no `guidelines/testing.md` stops a task that writes or changes tests; reading, refinement and breakdown name the discipline | Slice 4 · WAY-214, WAY-215, WAY-218 |
| To do 5 — WAY-174 covers the testing skill | WAY-174 · Slice 3 (step 4 "How to show") |
| To do 6 — one guidelines task may write coding and testing guidelines together | WAY-247 · Slice 2 · Slice 3 · Slice 4 |
| Questions carried to cycle 1 — the words, `exemplar` | glossary `exemplar` · Slices 1, 3 (spec D1) |
| Questions carried to cycle 2 — WAY-228's wording | WAY-228 (spec D4) · Slice 1 |
| Questions carried to cycle 3 — selection by *Applies to* alone | Slice 4 (spec D6; WAY-213 unchanged) |
| Questions carried to cycle 4 — the installer and a pinned product | Slice 5 (spec D7) |
| README of the-way names the discipline and its skill (spec D8) | Slice 3 |
| Row 1 | WAY-231 |
| Rows 2–13 | WAY-232–WAY-243, in row order |
| Row 14 | WAY-228 |
| Row 15 | WAY-231 |
| Row 16 | WAY-215 · WAY-218 |
| Row 17 | WAY-244 |
| Row 18 | WAY-174 |
| Rows 19–24 | WAY-245–WAY-250, in row order |
| Row 25 | no entry of its own (ruling C3): WAY-233, WAY-235, WAY-236, WAY-237, WAY-238, WAY-241, WAY-243 |
| Spec: environment facts under WAY-232 and, if relied on, WAY-236 | foundation step |
| Spec: the whole gate on the change as it goes into the request | the cycle's verification step, after Slice 5 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| All foundation entries written by one agent before Slice 1, as the method gives | each entry written with the slice whose code needs it — every slice's file cites decisions that must exist for `foundation_check.py` to pass on its commit | the foundation agent runs out of room with twenty decisions and the page re-reads; the orchestrator splits the foundation step into two dispatches (rows 1–13 with the facts; rows 14–24 with the edits and the glossary) |
| The entry points named in Slice 3's *Change* by two paths with `the-way-*`, the generator run once in the slice that adds the skill | batches of ten generated files per slice written in process, as an earlier cycle did — four more slices of mechanical output, the gate's `agent-instructions` and `gate` tests red between them | the size script counts two files for forty-two generated ones; if the orchestrator wants them named one by one, four batch slices are added after Slice 3 |
| The testing template (Slice 1) and the coding discipline's loss of the rule (Slice 2) in two slices | the move of WAY-228's rule in one slice | between the two slices the rule stands in both templates on the task branch; no merge falls between them |
| The yes/no table rendered in English without the research's sources column and without "red before the fix" | copying the table whole | its sources point to a private course (WAY-27) and "red before the fix" is cut by Q14; one table edit if wrong |
| The skill (Slice 3) after the coding skill's change (Slice 2) | the skill first | none: the skill mirrors the coding skill as it will stand |
| `README.md` with the skill in Slice 3 | with the installer | none |
| A new test file `installation/test_testing_guidelines_installation.py` | the coding skill's test generalized over both skills | about 160 lines of test code repeated, as the styleguide and coding skills already have one file each |
| `installation/test_install.py` `NAMES` left as it is | adding the skill to it | none: the new test covers the skill; `NAMES` already lacks `maintain-styleguide` and `lead-project` |
| Files created by an earlier slice, and the research file outside the repository, named in *Read* outside backticks | backticks, which the size script reads as missing files and leaves the slice unchecked | those slices' measured size is understated by the template's and the section's length, well within the limit |
