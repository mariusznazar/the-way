# Author report — close-decision-pending-templates

**Status:** done with concerns

**Commits:** `2c27260` on `task/close-decision-pending-templates` (base `fca8491`, `foundations`). The commit was first made as `5b13810`; I amended only its message (it was my own, unpushed commit). One commit holds the whole change.

**Foundation step:** nothing written. *Settlements to record* is "none (0 accepted)" and the task carries no projected entry, so the foundation step has no entry to write. The decision log `foundations/decisions.md` is unchanged, as the task's *Out of scope* requires.

## Files changed

| File | Added | Removed |
|---|---|---|
| `elements/common/missing_element_file.md` | 2 | 6 |
| `elements/common/way_of_working.md` | 10 | 17 |
| `elements/environment-facts/template.md` | 13 | 27 |
| `elements/glossary/template.md` | 4 | 7 |
| `elements/invariants/skill/decide_entry.md` | 1 | 2 |
| `elements/invariants/template.md` | 9 | 26 |
| `elements/part-map/template.md` | 6 | 10 |

Thirty of the 32 `decision pending` markers are removed. Two remain on purpose: `elements/environment-facts/template.md:130` (S26) and `elements/invariants/template.md:82` (S28), both out of scope.

## What was done, per case

- **S1 (WAY-05)**: the four "field stays in this template" markers (env-facts, glossary, invariants, part-map) now end with `(WAY-05)`. WAY-05 quotes the same sentence verbatim.
- **S2 (WAY-64)**: invariants, "takes in a clause of another keeps its identifier, and the other is split (WAY-64)". WAY-64 says the same words.
- **S3 (WAY-61)**: invariants, "A test stands in a file of code (WAY-61); a Markdown file holds no citing test." See concern C3.
- **S4 (WAY-44)**: invariants, "whether a check belongs to the product is settled by the part map (WAY-44)". See concern C4.
- **S5 (WAY-62, WAY-22)**: invariants, "*Part* has no third value. A sentence no commit of this product can make false is not an invariant of this product (WAY-22, WAY-62)." The ending "it belongs to the foundation of the product whose commits decide it" is removed; this is the only change of sense among S1–S19.
- **S6 (WAY-73)**: env-facts, "is no such fact (WAY-73)".
- **S7 (WAY-90)**: env-facts, "The partners themselves stay in the part map's external context (WAY-90)". WAY-73 is not cited. See concern C2.
- **S8 (WAY-48, WAY-44, WAY-41)**: part-map, each on its own list: external context (WAY-48), files left out on purpose (WAY-44), withdrawn identifiers (WAY-41).
- **S9 (WAY-48)**: part-map, "A row names no part and no file (WAY-48)". See concern C5.
- **S10 (WAY-22, WAY-29)**: decide_entry, "one the human gives is written as a decision (WAY-22, WAY-29)."
- **S11 (WAY-44 next to WAY-28)**: missing_element_file, the sentence keeps `(WAY-28, for a product the process enters)`. WAY-44 is not added. See concern C1.
- **S12 (WAY-71)**: way_of_working, "never a `none` the agent writes (WAY-71); it is asked about before anything is written in it." The "first ask" wording is kept as plain text.
- **S13–S19**: markers removed, rule kept as plain template text (S16 identifier sentence, S17 edition of a citation, S18 descriptive source, S19 sentence edition, S13 value from source, S14 "entries following from one entry" as "each through the skill of its element: ...", S15 missing element file start).
- **Item 2 (step 4.1)**: replaced by the task's wording: "Ask in one round about everything still open, as »How a skill asks« gives it (WAY-113): a value the source does not give, with where to look for it and never the value itself; a choice, with the ways open, what each costs and a recommendation; a question of assessment, open."
- **Item 3**: "How a skill asks" now reads "A question of decision — a choice that settles something in a file — gives the ways open, what each costs, and a recommendation." The step 4.1 reference is removed.
- **Item 4 (S21)**: "in the present tense" removed; "today" kept.
- **Item 5 (S22)**: "and finding it is a task" replaced by "An entry that would stand on a missing fact takes `TODO — <the fact, with its source>` in its field, and a change that leaves it there puts it before the human (WAY-71)." See concern C6.
- **Item 6 (S23)**: "Moving the product to another release is a decision's to make" removed, nothing put in its place.
- **Item 7 (S24)**: part-map `Files: none` rule kept as plain text; only the marker removed.
- **Item 8 (S25)**: the whole Draft blockquote at the top of `elements/invariants/template.md` removed, with its sentences and marker.
- **Item 9 (S27)**: glossary, "The language of an entry follows `elements/common/rules.md` (WAY-72). An entry keeps the English term; a word the product shows its users in another language stays in the product's files, not in the glossary (WAY-72, WAY-99)."

## Checks run

1. `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors".
2. `python -B gate/run_tests.py elements/common` — exit 0, "Ran 144 tests ... OK".
3. `python -B gate/run_tests.py elements/part-map` — exit 0, "Ran 39 tests ... OK".
4. `grep -rn "decision pending" elements` — exactly two lines: S26 (env-facts:130) and S28 (invariants:82), as the handoff requires.
5. Every `WAY-nn` I added or kept on a changed line exists as a heading in `foundations/decisions.md` (checked by `grep "^### WAY-nn "`, one heading each).
6. `grep -n Draft elements/invariants/template.md` — no match.
7. `grep` of the whole repo (all tracked files) for the removed phrases ("present tense", "finding it is a task", "Moving the product", "**Draft", "step 4.1") — no test or script reads them. The only "step 4.1" hits are the element skills' own steps (`elements/environment-facts/skill/write.md`, `elements/glossary/skill/write.md`, `projected.md`), not `way_of_working.md` step 4.1; left unchanged.

**Not run:** the full gate (outside my boundary). Test directories other than `elements/common` and `elements/part-map` were not run; the task's own grep found no test reading the changed text, and the full gate is the orchestrator's. No invariant test was changed, so no failing-first run applies: the change is prose only.

## Own-work check (section 3)

- **Requirement:** each citation I wrote is supported by the whole text of its decision entry; every rule keeps its sense, except the S5 ending and items 2–9.
- **Check:** I read every decision the dispatch names whole (WAY-01, 05, 22, 28, 29, 33, 35, 36, 41, 44, 48, 61, 62, 64, 71, 72, 73, 76, 85, 89, 90, 99, 113, 114, 134, 150), compared each citation with its text, and ran checks 4–6 above.
- **Result:** no failing check. Four citations are weaker than the others, and I flag them as concerns below rather than hide them.

## Reaches beyond the dispatch

- `elements/common/way_of_working.md` step 4.1 references were searched by grep across `elements/`, `product-guidelines/`, `project-level/`, `foundation-review/` (the "How a skill asks" pointers). They still point at the same section, which I kept.
- Searched `foundations/` for the changed phrases ("one round", "Draft", "decision pending", "left out", "one at a time", "holds no files", "external context", "another language"). The matched decisions were read only where the match was on a cited entry; no other decision was contradicted.
- Read `foundations/invariants.md` entries `element-directory-contents`, `return-step-record`, `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`, `skill-rule-source` (the handoff named four; I read the block 36–105 which contains them). Read the five parts' entries in `foundations/part_map.md` (decisions, part-map, invariants, glossary, environment-facts, elements-common — the last two lines of the handoff's list).

## Unread material

- `elements/common/rules.md` — the shared rules on `none` and `TODO` that the templates point to. Not in the dispatch; not read. My sentence "takes `TODO — <the fact, with its source>` in its field" relies on the `TODO` form in `elements/common/rules.md` and WAY-71 — the rule was not read in its own file.
- `foundations/glossary.md` — only the headings were read; the entries of the words used in the rewritten sentences ("entry", "foundation", "invariant", "environment fact", "human action") were not read whole.
- Decisions cited on lines I reflowed but did not change in sense: WAY-02, WAY-17, WAY-65, WAY-80, WAY-82 — their headings were checked, their entries were not read.
- `elements/common/projected_mode.md`, the templates' `examples.md` files, and the other element skills named in the grep hits — not read.
- The whole foundation was not read whole; the foundation search for the changed text is by grep (see Reaches).

## Searches not found or unclear

- A search for an existing test or script that reads the removed text (`decision pending`, `Draft`, `present tense`, `finding it is a task`, `Moving the product`, `4.1`) — none found.
- The `return-step-record` invariant requires the record of this task's return step in one commit of the change. I wrote no such record: the dispatch does not name one, and it is the cycle's return step. Unclear whether the cycle expects it from the author; flagged here.
- Whether `elements/common/rules.md` says what a bare `TODO` means for a fact entry (concern C6).

## Concerns (for the reviewer)

- **C1 (S11, `elements/common/missing_element_file.md`).** The task pairs S11 with WAY-44. WAY-44 reads: "Every file git tracks belongs to exactly one part of the map, by path patterns that git itself matches ...". The sentence at this line is about the order in which the part map is written before another element's first file, which WAY-28 states ("The part map comes first"). WAY-44 is already cited for the `update-part-map` assignment one line above, in the same file. I did not add WAY-44 here. **Recommendation:** keep WAY-28 only, as written; a reviewer who reads the pairing as deliberate can add WAY-44 beside it.
- **C2 (S7, `elements/environment-facts/template.md`).** The task pairs S7 with WAY-90 and WAY-73. WAY-90 reads: "a decision's *Based on* ... names instead a fact entry ... for every citation that, once it stopped being true, would call the decision into question". Its *Rejected* says: "the partners of the part map's external context as linked facts — a new link with no known consumer." That matches the sentence exactly. WAY-73 defines which facts an invariant's *Rests on* names, and does not speak of outside facts. **Recommendation:** WAY-90 only (as written).
- **C3 (S3, `elements/invariants/template.md`).** WAY-61 reads: "`test` ... once a test of the product's test suite, written in the product's language". It does not say that a test stands in a file of code, nor that a Markdown file holds no citing test; those parts of the sentence are my reading. **Recommendation:** keep the citation, reviewer decides; alternatively drop it and keep the plain sentence.
- **C4 (S4, `elements/invariants/template.md`).** WAY-44 reads: "Every file git tracks belongs to exactly one part of the map". That supports "the part map settles belonging" for a file. Whether a file is a check "of the product" is an inference from "git tracks it in the product". Medium confidence, as the task's own report rated it.
- **C5 (S9, `elements/part-map/template.md`).** WAY-48 is cited on "A row names no part and no file". WAY-48 says a trust boundary is recorded at the part that holds it, and that an exchange with the external context records its direction. That supports the row's place, but not its absence of a part name verbatim. Medium; the same citation already sits on the next sentence.
- **C6 (item 5, `elements/environment-facts/template.md`).** The sentence I wrote is the task's content, but the `TODO — <...>` form is defined in WAY-71 for an invariant's *Rests on*, a decision's *Based on* and an invariant's *Derives from* — not for a fact entry, which has no such field. A reader of the fact template may look for the field and not find it. **Recommendation:** keep the sentence (the task asks for its content); a reviewer can cut it to "(WAY-71)" alone if the explanation seems too long.
- **C7 (S10, `elements/invariants/skill/decide_entry.md`, pre-existing, not changed).** WAY-35 says a skill holds only the way of working particular to its element; rules of entries stand in the template. The sentence "one the human gives is written as a decision" is a rule of entries sitting in a skill. This existed before the change, and the task did not ask to move it. Noted for a later task.

## Choices made

- **S5:** the ending removed, the citations WAY-22 and WAY-62 kept (task). Rejected: keep the ending as plain text; it contradicts the template's own *Part* rule. Cost if wrong: none for the product; a reviewer may restore it.
- **S7 and S11:** citations as in C1 and C2; rejected: the citations the task names in full. Cost if wrong: a reviewer finds a citation the decision does not carry; the sentence stays correct.
- **Draft header:** the whole blockquote removed, including its sentence "the template does not reach the main branch" (task item 8). Rejected: keep those sentences as plain text — the task says remove the header with its marker.
- **Item 5:** my explanatory sentence kept (see C6).
- **Line wrapping:** the rewritten paragraphs were reflowed to the file's width, not kept as the original breaks, where a sentence had changed.
