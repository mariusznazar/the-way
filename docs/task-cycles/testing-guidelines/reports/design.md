# Design report — testing-guidelines (designer, `write-spec`)

Status: done. Spec: `.runs/task-cycles/testing-guidelines/spec.md`.

## Questions sent and answers

Batch 1 (the only batch):

- **Q1 — row 25 asks for a decision the decision template says is no question.**
  `elements/decisions/template.md:40-42` ("what do we take from X" is no question, WAY-19); WAY-175,
  WAY-195 and WAY-222 were withdrawn for that shape; WAY-27 forbids pointing to the private 10xDevs
  course. Recommended: no entry of its own; each borrowed piece in the *Based on* of the decision
  that carries it, each piece left out in the *Rejected* of the decision whose question it answers,
  the 10xDevs piece in prose. **Answer C3: accepted as recommended.** Spec: D9 "Row 25", *Foundation
  entries*.
- **Q2 — who designates a level's exemplar test when the level has no test yet.** Recommended: row
  12's decision carries WAY-200's split, plus one bullet in `product-guidelines/reading.md` shaped like
  the WAY-216 bullet, plus a skill mode. **Answer C4: the split and the reading bullet accepted; the
  skill gets no mode beyond what `maintain-coding-guidelines` has for the same case.** The coding
  skill has "A new kind" (step 1 modes, step 3), so the testing skill mirrors it as "A new level" and
  nothing more. Spec: D3 *Exemplar* field, D5 steps 1 and 3, D6, WAY-242.

## Ways weighed and why the rejected ones lost

Each is carried in the spec with its cost if wrong; in short:

1. **Words (D1).** Widen `exemplar` in place (chosen) vs a term "exemplar test" (a phrase holding the
   word, the shape WAY-99 refuses; two entries for one concept) vs leaving the entry (reads two ways
   once row 15 takes tests out of kinds of code). "test level", "property test", "the source of the
   expected value" in plain words (WAY-95); "test oracle" avoided because the field counts the
   previous version among oracles, which row 2 excludes.
2. **WAY-228 (D4).** Edit in place (chosen: same question, WAY-19; WAY-70's successor stays valid) vs a
   new number (second number for one question) vs a narrowing decision with WAY-228 left in coding
   (contradicts Q9).
3. **Selection (D6).** *Applies to* alone, WAY-213 unchanged (chosen) vs also checking `## When to
   read` (judged before a diff; a wrong "no" drops the file from an agent that then writes a test; a
   second conditional mechanism) vs a row in the coding index (contradicts Q9, row 1). The *missing*
   finding uses "the work writes or changes a test" (item 4). Row 20's "a part that has tests" read one
   way: parts whose code the tests check and parts holding test files (the union; each narrower
   reading misses a case).
4. **Installer (D7).** One `SKILLS` entry, no new mechanism (chosen), with the evidence: `install.py`
   `plan` `:343-346`, `file_action` `:431-436`, `run` `:580-584`, `product_guidance` `:147-162`,
   `agents_change` `:245-250`, `stale_entry_points` `:308-321`; test
   `installation/test_install.py:278-319` creates an added skill's entry points on a pin move. Rejected:
   a step of its own for pinned products (a second route beside WAY-34's pin move); nothing in the
   installer (item 2 requires the entry). Trust boundary: the change adds a constant pair and no
   parsing; `check_parents` and `owned_entry_point` refuse a crafted file, directory or non-UTF-8 file
   at the new path before writing; tests mirror `test_coding_guidelines_installation.py:127-160`.
5. **Rows onto the foundation (D9).** Twenty new decisions WAY-231–WAY-250 in row order (rows 1+15
   one decision; row 21 its own because WAY-215 already holds three binding sentences, WAY-05);
   WAY-228, WAY-174, WAY-215, WAY-218, WAY-214 edited in place; row 25 per C3. Rejected: rows 2–13 as
   one or a few decisions (each is a question of its own, as the styleguide's rules are one per
   decision; three sentences could not hold them).

## The four checks

1. Placeholders, `TBD`, empty sections: none. Template placeholders such as `<the product>` and
   `<level>` name parts of the form the template gives, not gaps. "if relied on" for two environment
   facts is the writer's call under WAY-90, stated as such.
2. Contradictions: fixed one — the Limen piece first pointed to "WAY-237 or WAY-231 for `## Examples`";
   `## Examples` carries no decision (WAY-168), so it now goes to WAY-237 alone. Checked: WAY-233 vs
   WAY-03 (an invariant test changed is named in the request; a cause for every changed test adds to
   it, no collision); WAY-243 vs WAY-68 (derives from it); WAY-235 vs WAY-48 (adds a standing test to
   the aimed review, no collision); WAY-237's return condition in binding sentences, since WAY-119 is
   withdrawn; WAY-241's command field vs WAY-16 (the gate's own command narrowed, as
   `agent-instructions/README.md` "Check the change" does); WAY-213 unchanged vs its first clause.
3. Several independent changes: no. The template, the skill, the move of WAY-228 out of the coding
   template, the reading and refinement edits, the installer entry and the decisions depend on each
   other (WAY-228 must leave the coding template in the same change the testing template takes it;
   the installer entry needs the skill file; the decisions are what the template's rules cite). A plan
   may still cut slices.
4. Requirements read two ways, settled: "a part that has tests" (D6); where the Limen piece goes (D9);
   the order of the template's added sections and the recipe's fields (D3); `## Where in code` before
   the first test (may hold no item, D3).

## Reaches beyond the dispatch

- `elements/decisions/template.md` whole — to judge row 25 and the limit of binding sentences.
- Decisions WAY-03, WAY-05, WAY-07, WAY-10, WAY-12, WAY-19, WAY-30, WAY-60, WAY-61, WAY-63, WAY-68,
  WAY-69, WAY-80, WAY-86, WAY-90, WAY-94, WAY-95, WAY-96, WAY-99, WAY-114, WAY-135, WAY-226, and the
  withdrawn list (WAY-119, WAY-175, WAY-179, WAY-195, WAY-222) — to place rows 3, 5, 6, 7, 13 and the
  words, and to check collisions.
- `foundations/environment_facts.md` headings and `impossiblebench-test-modification` — WAY-90 makes a
  model finding a fact; row 3's decision can rest on the existing one.
- `foundations/invariants.md` entries of `every` and those named — no invariant changes.
- `agent-instructions/README.md` whole — edits in place before `main`.
- `installation/test_install.py:19-60, 180-320` — how a moved pin brings an added skill.
- `task-cycle/change/SKILL.md:52-79`, `task-cycle/review/SKILL.md:64-76` — to keep the process steps
  unchanged (Q11).
- Research: `watek_5_open_mercato.md` (the list of weakenings comes from `open-mercato/skills` at
  `e320bd5`, read from a local clone), `watek_6_limen.md` (public at `github.com/overment/limen`,
  `89ef378`).

## Concerns

- **Volume of the foundation step**: twenty new decisions and five edits, each with quotations the
  writer must re-read on the page; the raport marks most quotations as tool-extracted. The spec's
  quotation table names them; a source the writer cannot reach stops it.
- **`maintain-instruction-files` in a product**: the testing skill, like the coding skill, sends the
  `AGENTS.md` pointer through `maintain-instruction-files`, which the installer does not install in a
  product (it is not in `SKILLS`; WAY-127 reaches it by a global link). This gap is shared with the
  coding and styleguide skills and is not widened here.
- **The wait in `loop2`** (Q8's accepted price): once `loop2` moves its pin, every task of it that
  writes a test — in practice every code task — waits for its testing-guidelines task.
- **Pre-existing**: the coding installation test notes that the non-UTF-8 case stops on an uncaught
  `UnicodeDecodeError` (C37 of the coding cycle); the new test mirrors that assertion and does not fix
  it.
- **WAY-214 and WAY-218 wording**: both read awkwardly already; the edits add a discipline to lists
  inside long sentences, and the writer should keep each within three binding sentences.

## Revision after spec review

The review (`reports/spec-review.md`, FAIL: F1 Important, F2–F7 Minor) is accepted in full; no
finding is held wrong. One revision, the changes below; line ranges are of the revised `spec.md`.

- **F1 (Important) — authorization table inside a decision.** Changed: the table who × resource ×
  action → expected result stands in the rule's text of `guidelines/testing.md`, as `## Roles` does,
  each row naming the product decision on permissions it comes from, those decisions grouped within
  three binding sentences each (WAY-05); *Decision* names the product's decisions on permissions; no
  decision holds the table. Where: D3 `### Trust boundaries`, lines 260–270; D5 step 4, lines 422–423;
  the WAY-235 row, line 588.
- **F2 — Limen in a *Based on* that does not rest on it.** Changed: Limen is named with its address
  and passage in the *Rationale* of WAY-237, never in a *Based on*, with the reason (the piece lands
  in `## Examples`, which carries no decision; withdrawn WAY-179; WAY-33). Where: quotations table,
  line 128; D9 "Row 25", lines 556–560; the WAY-237 row, line 590.
- **F3 — reason of an exclusion.** Changed: the product decision's binding sentences carry the return
  condition and its rationale the reason. Where: D3 `## Not tested on purpose`, lines 306–310; the
  WAY-237 row, line 590. *Constraints* line 99–100 already said only the return condition and stays.
- **F4 — WAY-215 and WAY-247 deriving from each other.** Changed: WAY-215's *Relations* gain WAY-244
  only, with the reason. Where: WAY-215 edit, lines 615–617; WAY-247 keeps "derives from WAY-215".
- **F5 — research again at every refresh.** Changed: the clause dropped from step 2 (the smaller
  reading of row 23 and B3), and the WAY-249 row says no research again at a refresh where the human
  has preferences. Where: D5 step 2, line 405; the WAY-249 row, line 602.
- **F6 — a diverging level's definition twice.** Changed: the levels table has *Level* and *Decision*
  only; a diverging name is a term of the product's glossary defined there by resources, and the table
  names the term and copies no definition; a field-meaning name takes no definition. Where: D3
  `## Levels`, lines 217–225.
- **F7 — WAY-238's *Scope*.** Changed: WAY-238 takes *Scope* `product-guidelines, task-cycle,
  project-level`, with the reason (WAY-21). Where: the WAY-238 row, line 591.
- **Reviewer's side note on D7** ("the only product path it touches" is loose): reworded — the only
  new product path is the entry-point path; the block and the siblings' lists go through the paths the
  installer already writes, under the same checks. Where: D7 trust boundary, lines 501–504.

Four checks after the revision: no placeholder or empty section; no new contradiction (WAY-235's
*Decision* and the refusal test both name the decisions on permissions; WAY-237's binding sentences
and rationale split agrees with *Constraints*); scope unchanged; no requirement left readable two ways
among those the findings touched.
