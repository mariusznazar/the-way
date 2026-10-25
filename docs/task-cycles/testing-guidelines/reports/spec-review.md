FAIL

# Spec review — testing-guidelines (reviewer, `write-spec`)

- Spec: `.runs/task-cycles/testing-guidelines/spec.md` (648 lines), read as the agent that has to
  plan and build from it.
- Against: the frozen task `.runs/task-cycles/testing-guidelines/task.md` whole (every *To do* item,
  Q1–Q14, rows 1–25, *Out of scope*, *Questions carried to cycle*); the orchestrator's rulings C3
  and C4 (`cycle.md`); the foundation entries the handoff names.
- Result: one Important finding and six Minor ones. Everything else the task asks is covered, with
  the meaning the task gives it; the four open choices and the row mapping are weighed and sound.

## Findings

### F1 — Important — the authorization table is put inside a product decision

Place: spec D3, `### Trust boundaries`, lines 259–260 ("*Decision*: adopting, and for
authorization the product's decision holding the table who × resource × action → expected
result"); D5 step 4, line 418 ("the authorization table's decision (WAY-235)"); the WAY-235 row,
line 578 ("an authorization table").

What goes wrong: the builder writes into the testing template, for every product, that the table
who × resource × action → expected result stands in a decision of the product's log. A decision is
one to three binding sentences followed by fields, then rationale and rejected options
(WAY-05, `elements/decisions/template.md:20-38`, "Binding sentences"); there is no place for a table,
and no decision of the-way's log holds one. The nearest precedent goes the other way: the
styleguide keeps its table (`## Roles`) in the guidelines, each row naming the decision that carries
its meaning, and groups the meanings into several decisions because one holds at most three
binding sentences (`product-guidelines/styleguide/template.md:78-89`, "Pairs and meanings",
WAY-176, WAY-05). The task does not say the table is a decision: item 1 lists it as part of the
rule ("dla autoryzacji tabela kto × zasób × akcja → oczekiwany wynik"), and Q2 says the test takes
the expected refusal "z decyzji o uprawnieniach" — from the decision on permissions, not from a
table inside it.

Fix: say where the table stands — in the rule's text in `guidelines/testing.md` (as `## Roles`
does), each row naming the product decision on permissions it comes from, those decisions
grouped within three binding sentences each — and keep "the product's decision on permissions" as
what the *Decision* field and the refusal test name. If the orchestrator prefers the table in the
test data of the refusal invariant instead, the spec says so; either way it leaves the decision's
form alone.

Cost if left: every product that adopts the rule meets a template that asks for a decision its
decision skill cannot write, and the first product task stops on it or writes a non-conforming
entry.

### F2 — Minor — Limen is set in the *Based on* of a decision that does not rest on it

Place: D9 "Row 25", lines 549–550; *Foundation entries*, WAY-237 row, line 580 ("ISTQB · Limen");
quotations table, line 128.

What goes wrong: the Limen piece (the kinds of tests without value) lands in the template's
`## Examples`, which the spec itself marks as binding nothing (line 305–307). WAY-237 answers what a
product deliberately does not test — categories with a product decision, reason and return
condition — and does not rest on Limen. *Based on* is read by the author of a change to a source,
searching for what rests on it (`elements/decisions/template.md:73`, WAY-33); a false entry there
sends that search to WAY-237. The log already holds that an example of a template needs no
decision (withdrawn WAY-179, "an example of a template needs no decision (WAY-168)").

Fix: name Limen, with its address and the passage, in the rationale of the decision that sets the
template's sections (WAY-231) or of WAY-237, not in a *Based on*; row 25's purpose — that the
request names what is taken from Limen — is still kept by the request, as C3 gives it.

### F3 — Minor — the reason of an exclusion: binding sentences or rationale

Place: D3 `## Not tested on purpose`, lines 302–303 ("the product decision whose binding sentences
carry the reason and the condition under which the category is tested again"), against the
WAY-237 row, line 580 ("the return condition in the product decision's binding sentences") and
*Constraints* line 99–100.

What goes wrong: the two places disagree, and the builder of the template has to pick. A reason
belongs in *Rationale* (WAY-05; `elements/decisions/template.md:53-56`); only what binds later
work — the return condition — goes into a binding sentence, which is why WAY-119's withdrawal is
cited. Fix: D3 reads "whose binding sentences carry the condition under which the category is
tested again, and whose rationale gives the reason".

### F4 — Minor — WAY-215 and WAY-247 would derive from each other

Place: WAY-247 row, line 590 ("derives from WAY-215"); WAY-215 edit, lines 605–606 ("*Relations*
gain WAY-244 and WAY-247").

What goes wrong: `derives from` names a higher decision this one serves, written in the entry that
depends on the other (`elements/decisions/template.md:145-148`). WAY-247 narrows the shape of the
prerequisite WAY-215 asks for, so it depends on WAY-215; WAY-215 naming WAY-247 as well makes each
the higher of the other. Fix: WAY-215's *Relations* gain WAY-244 only.

### F5 — Minor — the skill researches again at every refresh, which no row carries

Place: D5 step 2, lines 398–400 ("without them, and at every refresh or extension, research"),
against WAY-249's meaning, line 592, row 23 and item 2 (B3).

What goes wrong: row 23 and B3 (accepted whole in Q14) say: the human's preferences, and without
them research with a fresh agent per question and critique. Researching again at every refresh or
extension, even where the human has preferences, is what the coding skill does under its own
decision (WAY-211, "It researches again whenever …"); here no decision carries it, so the skill
would hold a behaviour no entry of the-way sets. Fix: either drop the clause (the smaller reading
of the task), or rule that WAY-249's meaning includes it and say so in the WAY-249 row. Cost
either way is one clause.

### F6 — Minor — a diverging level's definition would stand twice

Place: D3 `## Levels`, lines 217–221 (*May touch* column for every level, plus "a level whose name
means in the product something other than in the field also has an entry of the product's
glossary defined by those resources").

What goes wrong: for a level whose name diverges, the definition by resources stands in the
guidelines' column and in the product glossary; two copies of one meaning drift, and the glossary
entry is the one row 10 settles. For the other levels, a required resources column is more than
row 10 asks ("poziomy testów produktu po nazwie"; a definition by resources only for a diverging
name). Fix: the column either goes, or reads, for a diverging level, the glossary term instead of
its own text; the spec says which.

### F7 — Minor — WAY-238 binds the cycle and refinement but takes *Scope* `product-guidelines` alone

Place: *Foundation entries*, line 565 ("All decisions take *Scope* `product-guidelines` unless
noted") and the WAY-238 row, line 581.

What goes wrong: row 8 binds who chooses the level (the author, in the cycle) and that a task's
refinement holds no test plan. *Scope* is how a change finds the decisions it must read (WAY-21);
a later change to `task-cycle/change/SKILL.md` or `project-level/task/skill/SKILL.md` would not
find WAY-238. Fix: WAY-238 *Scope* `product-guidelines, task-cycle, project-level`.

## Coverage checked and found sound

- *To do* 1: every bullet A1–A16 has its place in D3, in the order the task gives; the Q14 cut list
  stays cut (line 63–68 and D3 hold none of the cut items: no snapshot exception, no red replacement,
  no flaky "fix before the next change", no single test among exclusions, no separate commands).
  *Applies to* "a part that has tests" is read one way (union, D6), weighed, and the cost named.
- *To do* 2: B1–B6 in D5, with the table of who writes what, *What reaches the task document*,
  orchestrated mode and steps 0–5; entry points and `SKILLS` (D7, D8). C4 applied as ruled: one
  mode "A new level" mirroring the coding skill's "A new kind" (`product-guidelines/coding/SKILL.md:126`,
  `:188-190`), nothing beyond it.
- *To do* 3: D4 removes the rule from `product-guidelines/coding/template.md:44,59-62,156-161` and
  `product-guidelines/coding/SKILL.md:220-222` (verified: the only uses of WAY-228 outside the
  foundation; the withdrawn WAY-70 names WAY-228 as successor, so editing in place is right).
- *To do* 4–6: D6 and the edits of WAY-214, WAY-215, WAY-218; WAY-174 edit; WAY-247.
- Rows 1–24 map onto entries with their meaning (D9 table checked row by row); row 25 per C3, every
  piece taken and left placed (only the Limen placement questioned, F2). C3 agrees with
  `elements/decisions/template.md:40-42`, WAY-19, WAY-100 and the withdrawals of WAY-175, WAY-195,
  WAY-222.
- *Out of scope* and Q11 kept: no change to `task-cycle/change` or `task-cycle/review`; process gaps
  of §8 and `loop2`'s guidelines left out.
- Questions carried to cycle: all four answered (D1, D4, D6, D7), each with ways rejected and cost.

## Designer's factual claims verified

- Installer: `SKILLS` at `installation/install.py:25-44` (19 skills); `plan` `:343-346` builds a
  wrapper for every name in both directories; `file_action` `:431-436` gives `CREATE` for a missing
  path; the write loop `:579-584`; `product_guidance` `:147-162` lists every name; `agents_change`
  `:245-250`; `check_parents` `:283-288`; `owned_entry_point` `:291-305`; `stale_entry_points`
  `:308-321`; the refusal "Existing integration file differs" `:394-395`; `committed` `:81-82`. All
  as the spec says.
- `installation/test_install.py:278-319` adds `extra-skill` at a later commit and asserts its entry
  points in both directories after the move — as the spec says; `installation/README.md:95-97`
  says the same.
- Entry-point counts: `assertEqual(len(siblings), 38)` at
  `installation/test_coding_guidelines_installation.py:97` and
  `installation/test_styleguide_installation.py:91`; 19 × 2 = 38, so 40 after the change. No other
  test counts them. `test_install.py` `NAMES` lacks `maintain-styleguide` and `lead-project` already,
  so leaving it to the maker is safe.
- Crafted-input test to mirror: `installation/test_coding_guidelines_installation.py:127-160`.
- Generator checks: `agent-instructions/skill_entry_points.py:42` (`UNSAFE_START`) and `:118-120`.
- Trust boundary (WAY-48): the spec says how a crafted product file cannot make the change write
  outside its own files — the new name is a constant, the skill text comes from the-way's commit,
  and the new entry-point path passes `check_parents` and `owned_entry_point` before anything is
  written, with tests for a foreign file, a directory and a non-UTF-8 file in both directories.
  The sentence "the only product path it touches" is loose — the change also alters the text the
  installer writes into the `AGENTS.md` block and into every sibling entry point — but those go
  through the existing guarded paths with the same checks, so the conclusion holds.

## Reaches beyond the dispatch

- Decisions WAY-05, WAY-68, WAY-69, WAY-201, WAY-210, WAY-211, WAY-219–WAY-221, WAY-225–WAY-227
  (`foundations/decisions.md`, read whole) — to check the relations the spec gives WAY-243 and the
  coding analogs of WAY-248–WAY-250, and the edits' neighbours.
- `## Withdrawn identifiers` rows WAY-119, WAY-175, WAY-179, WAY-195, WAY-222, WAY-70 — to check C3,
  F2 and the WAY-228 edit.
- Environment facts `visible-scoring-reward-hacking`, `oracle-in-loop-building` — to see whether the
  proposed Konstantinou fact duplicates one; it does not.
- `installation/install.py` (lines 20–50, 75–90, 140–170, 240–400, 425–440, 490–588),
  `installation/test_install.py` (15–150, 278–319), `installation/test_coding_guidelines_installation.py`
  (90–164), `installation/test_styleguide_installation.py` (85–95), `installation/README.md` (grep) —
  to verify D7.
- `agent-instructions/skill_entry_points.py:38-46,112-124`, `agent-instructions/test_instruction_files.py:280-330`
  — to verify the generator claim and that no other test counts skills.
- `project-level/task/skill/SKILL.md:140-170`, `project-level/plan/skill/SKILL.md` headings and
  `:108-120` — to place D6's edits.
- `task-cycle/review/SKILL.md:86-99` — the grades used above.
- `.runs/task-cycles/testing-guidelines/cycle.md` — the wording of C3 and C4.
- Research `raport_wytyczne_testow.md` whole, `propozycja_szablonu_i_skilla.md` whole, `mapa_pakietu_10x.md`
  section m3l1 whole (named in the dispatch).

## Checks run

Reading only; no command of the gate. Line references above verified with `sed -n`/`grep -n` on the
worktree at `4302f72`.

## Re-review of the revision

PASS

Read: the revised `spec.md` (659 lines) at the ranges the designer's "Revision after spec review"
(`reports/design.md:111-147`) names, and a search of the whole spec for what each finding touched
(`holding the table`, `table's decision`, `May touch`, `every refresh`, `Limen`, `resources`,
`permissions`), so that no old wording survives elsewhere.

### Earlier findings

- **F1 — resolved.** D3 `### Trust boundaries` (lines 260–270): *Decision* names the product's
  decisions on permissions; the table stands in the rule's text of `guidelines/testing.md`, each row
  naming its decision, the decisions grouped within three binding sentences (WAY-05); "No decision
  holds the table". D5 step 4 (lines 422–423) and the WAY-235 row (line 588) say the same. No
  "decision holding the table" remains anywhere.
- **F2 — resolved.** Limen goes to WAY-237's *Rationale* with address and passage, never a *Based
  on* (line 128, lines 556–560, line 590), with the reason.
- **F3 — resolved.** D3 `## Not tested on purpose` (lines 306–310): binding sentences carry the
  return condition, the rationale the reason; agrees with the WAY-237 row (line 590) and
  *Constraints* (lines 99–100).
- **F4 — resolved.** WAY-215 gains WAY-244 only (lines 615–617); WAY-247 keeps "derives from
  WAY-215".
- **F5 — resolved.** D5 step 2 (line 405) no longer researches at every refresh. The WAY-249 row
  (line 602) adds "no research again at a refresh where the human has preferences". That only
  restates what "the human's preferences, else research" already means, so it adds nothing beyond
  row 23. No research is the smaller reading.
- **F6 — resolved.** `## Levels` (lines 217–225) holds *Level* and *Decision* only. A diverging name
  is a glossary term of the product, defined there by resources, and the table names that term and
  copies no definition. This agrees with the WAY-240 row (line 593) and with D5 step 4.
- **F7 — resolved.** WAY-238 *Scope* `product-guidelines, task-cycle, project-level` (line 591).
- **Side note on D7 — resolved.** Lines 501–504 now name the new entry-point path as the only new
  product path, and the block and sibling lists as going through the existing guarded paths.

### New findings

None. The revision touched only the places above. It contradicts neither the task nor the
foundation entries of the first review (WAY-05, WAY-168, WAY-171, WAY-176 precedent, WAY-21,
WAY-33), nor any other section of the spec.
