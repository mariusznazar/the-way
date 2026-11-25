FAIL 7c2502a73f8360d9e47af85863c522392ec6c192

# Review of the whole change — recommendation-not-below-goal

Range: base `301e4eae1111310ccd80e466f62ea01838b9ff88` to head `7c2502a73f8360d9e47af85863c522392ec6c192`
(`git rev-parse HEAD` returned the head; one commit; three files: `foundations/decisions.md`,
`elements/common/way_of_working.md`, `elements/common/critique/prepare.md`). No plan, no slices, so no
finding names a slice. Blocking: 2. Minor: 1 (within the task). Out of scope: 0.

## Findings

### Important

**I1. The new WAY-113 paragraph collides with WAY-166 and with the two instruction files that restate it, and the change records no precedence.**

- Place: `foundations/decisions.md:1582-1590` (new paragraph of WAY-113: "where no way reaches the goal, the question recommends none and says so"), against `foundations/decisions.md:4842-4888` (WAY-166), `project-level/technology/settle.md:34-38` and `project-level/definition_template.md:242-247`.
- What is wrong: WAY-166 says that in a choice of an agent's way to the running product "where no option can be used by an agent, the recommendation goes by the other consequences", and its *Rejected* refuses the opposite in so many words: "the step recommending nothing where no option can be used by an agent — an exception to WAY-113, and the human answers with no hint". Its *Rationale* rests on "the human is owed a recommendation (WAY-113)". After this change WAY-113 itself says that a way that gives less than the goal is never recommended and that where no way reaches the goal the question recommends none. Where the goal the material sets is that an agent checks the running product — a task's need ("an agent can read the logs"), or a project definition's goal or measure of success, the two places the new rule names — both decisions apply to the same question and give opposite outcomes: recommend by cost (WAY-166, `settle.md`, `definition_template.md`) against recommend none (WAY-113). The author named this case in its report and left WAY-166 unchanged, judging that no accepted text gives the outcome. That is the situation WAY-25 and `agent-instructions/README.md` "Make the change" describe: a collision with no precedence recorded is never settled silently, and where what the human accepted does not give the outcome the finding goes to the human before the change goes on. The task's answers (questions 1, 2, 4) say nothing of WAY-166, so the outcome is the human's to give; the change neither asked nor recorded one, and neither did it say in WAY-113 that the case stays under WAY-166.
- Why it matters: an agent at the technology step of a task whose need is an agent's check of the running product, with every option human-only, meets two binding sentences that contradict, and WAY-25 then tells it to stop and ask; or it picks one silently. Which one holds is exactly what a reviewer of the next cycle cannot judge.
- Evidence: the texts cited above (read whole: WAY-113, WAY-166, WAY-25's binding paragraphs, `settle.md:30-45`, `definition_template.md:240-250`); WAY-166 *Relations* is `derives from WAY-121 · narrows WAY-123`, no `narrows WAY-113`.
- Fix direction (the human's choice, not mine): either WAY-113's new paragraph says that the case WAY-166 settles stays under WAY-166, or WAY-166 is recorded as the decision that prevails in its area (`narrows WAY-113`, the area stated in its binding sentences, its *Rejected* line corrected), or the goal-not-reached rule is allowed to override and WAY-166, `settle.md` and `definition_template.md` change with it.
- Slice: none (single commit, no plan).
- Contradiction: yes — WAY-166 (its binding sentence "the recommendation goes by the other consequences" and its *Rejected* line on recommending nothing), and WAY-25 (a collision with no precedence recorded).

**I2. The paragraph the change inserts into WAY-113 breaks the antecedent of "that question" in the paragraph after it.**

- Place: `foundations/decisions.md:1582-1590` (new paragraph) and `foundations/decisions.md:1592` ("While a project definition or a task document is refined, the technology step included, that question is asked only where the choice contradicts a sentence the human said earlier, which the question quotes").
- What is wrong: before the change, "that question" referred to the question against the human's choice, stated in the sentence just above it. The change puts a paragraph between them whose last sentence speaks of "a question of decision of its own — whether to change the goal … settled … the goal of an independent task with the human in the same refinement". The nearest question before "that question" is now the goal-change question, and read so the sentence says that while a task document is refined the goal-change question is asked only where the choice contradicts an earlier sentence of the human, which is the opposite of To do 2 (the question is settled with the human in the same refinement) and of the new paragraph's own last clause. The change restates an existing binding sentence differently by moving what it refers to (WAY-263). The same sentence in `way_of_working.md` is not hit: there the bullet after the new text says "the question against the answer" in full.
- Why it matters: this is a binding sentence about when an agent may ask the human during refinement; an agent that reads the antecedent as the nearer question skips the goal-change question in the one place the task wants it asked.
- Evidence: the two texts above; `git diff` shows the new paragraph inserted between the old first and second paragraphs with no change to the second.
- Fix direction: name the question in the second paragraph ("the question against that choice") or move the new paragraph after the second.
- Slice: none.
- Contradiction: yes — To do 2 and answer 2 of the task (the goal-change question is settled with the human in the same refinement for an independent task), which the unchanged sentence now reads against.

### Minor (within the task)

**M1.** `foundations/decisions.md:1583` (102 characters) and `foundations/decisions.md:1704` (106 characters, the old last line of *Rejected* with the new text run on after it) are wider than the lines of the entry around them, which wrap at about 100 (several old lines are 101). The recent commit "Re-wrap two lines of the README paragraphs on the foundation check to 100 columns" shows the wrap is kept, but no rule or check names the width (908 lines of the base `decisions.md` are over 100), so this is polish only.

## Against the task

- To do 1: met. `way_of_working.md:34-41` and WAY-113's new paragraph name the three goals of question 1 by their places and the model clause "feature by feature".
- To do 2: met in both texts, subject to I2 for WAY-113: a way below the goal stands "with what it lacks of the goal on its own line" and "is never recommended"; "where no way reaches the goal, the question recommends none and says so"; the goal-not-worth-its-cost question is "of its own … also where no way reaches it", settled where the goal stands (plan with its owner, definition by the approval of readiness (WAY-118), independent task's goal with the human in the same refinement).
- To do 3: met. `prepare.md:8-10` says the rules given always include "How a skill asks" where the proposal or set holds a question of decision to a human; `check.md` and `SKILL.md` are unchanged (verified by `git diff --stat`), so no second copy of the rule (WAY-35).
- Questions 1-4: each answer is carried. *Rejected* of WAY-113 carries exactly the three *Not chosen* ways of rows' questions 1, 2 and 4 (the ways of question 3 belong to row 2, a file of instructions, and are kept out, as the base commit "keep only the row's own rejected options" asks).
- Settlements to record: row 1 is a paragraph of WAY-113 (3 sentences, about 140 words; the check passes) plus *Verification* and *Rationale*; row 2 is `prepare.md` alone. Out of scope: no loop2 document or plan touched.
- Added that nobody asked for: the same sentences in `way_of_working.md` and WAY-113 as two near-identical texts is what To do 1 and row 1 together ask (the bullet already carries WAY-113's rule in prose); I judged it as asked, not as an extra copy against WAY-35. The *Rationale* of WAY-113 gained a price clause; WAY-05 allows it and names no file, script or count in it.

## WAY-166 and the author's named case

Judged on my own. Where an option's usability by an agent is only a consequence among others and no material goal states it, WAY-166 and the new rule do not meet: the new rule needs a goal the material sets. They meet where the material's goal is the agent's check of the running product, which is I1. A project definition's template does not require such a goal (its four matters of an agent's way to the running product are asked as matters), so the case is rarer for a definition than for a task whose need says "an agent can read the logs"; I graded I1 on both.

## Derived decisions and the other entries read for collision

- WAY-123 (and WAY-137): "the simplest and cheapest" recommendation applies where no difference with a consequence remains; no collision with a goal rule. WAY-123's "each choice with its recommendation" meets "recommends none" only in the same case as I1.
- WAY-114: "a question goes to the human only where the agent has no recommendation" fits a question that recommends none (the agent then asks before writing); no collision.
- WAY-155, WAY-174, WAY-378 and the entries at `foundations/decisions.md:5881, 6128, 9605` derive from WAY-113 and add rules of their own about how a question is shown; none says that a recommendation may fall below a goal; no change needed.
- WAY-120 unchanged, as the task says; `prepare.md` says which rule is among "applicable rules" and does not restate WAY-120.
- WAY-35 / WAY-33: `check.md` is untouched; the invariants `skill-rule-source` and `elements-pending-marker` of WAY-35 are not hit by the diff (author ran `gate/run_tests.py elements/common`, 316 tests OK; I did not repeat the suite).

## Structure of the code the change leaves

No code and no test is changed; three files of instructions and foundation. `python -B task-cycle/change_file_sizes.py` on the range: `elements/common/critique/prepare.md` 12 to 14 (+2), `elements/common/way_of_working.md` 203 to 211 (+8), `foundations/decisions.md` 11891 to 11924 (+33). The rule of size of a function and a file covers the-way's scripts; none changed, so I ran no worktrees of base and head for it. The first paragraph of WAY-113 stays 3 sentences; the new paragraph is 3 sentences and about 140 words; `foundation_check.py` reports no excess. Nothing left without a user; no name stopped being true (the entry's question "How does an agent of the-way ask a human decision?" still holds).

## Declined to judge

- Whether `foundations/decisions.md` should hold the goal rule in WAY-113 or a derived decision instead: the task's row 1 settles it as "sentence of WAY-113".
- The width of the *Verification* clauses (long single list item): it follows the entry's existing shape.

## Checks

| Command (from the worktree) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `7c2502a73f8360d9e47af85863c522392ec6c192` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B instruction-files/check_instructions.py .` (the command `installation/README.md:82` gives, run from the root) | 0 | `0 error, 0 warn, 5 info` |
| `python -B task-cycle/change_file_sizes.py 301e4eae1111310ccd80e466f62ea01838b9ff88 7c2502a73f8360d9e47af85863c522392ec6c192` | 0 | sizes as above |
| `python -B elements/common/decision_index.py --sections --output .runs/review-whole/sections.md` | 0 | 29 sections |
| `python -B elements/common/decision_index.py --output .runs/review-whole/index.md --section "How skills write and read the foundation" --section "Decision entries and the decision log" --part decisions --part elements-common --decision 113 --decision 166 --decision 120 --decision 35 --decision 33 --decision 123` | 0 | 17 in full, 75 by heading |
| manual: lines added by the range wider than 100 columns | n/a | two lines (M1) |
| manual: `grep -rn "WAY-113"` over the repository outside `.runs/`, and `grep` for "recommends nothing / passes over it / the check stays with the human" | n/a | the derived decisions above; `settle.md` and `definition_template.md` restate WAY-166 (I1) |

Not run: the full suite (the cycle's, WAY-160); a test of another directory (none cites WAY-113, `way_of_working.md` "How a skill asks" or `prepare.md`, as the author's grep and my own grep of WAY-113 show). No invariant test is changed by the range.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-25 (binding paragraphs), WAY-114, WAY-165, WAY-118 heading, WAY-137, WAY-155, WAY-174, WAY-378 and the derived entries at lines 5881, 6000, 6128 and 9605: to judge collision with the new rule (WAY-33's search from the reviewer's side); `project-level/technology/settle.md:30-45`, `project-level/definition_template.md:160-250` and `process-audit/SKILL.md:105-112, 166-173`: where the instruction files restate or use WAY-113 and WAY-166; `foundations/glossary.md` (grep of "model", "goal"): whether "model" as a pattern needs an entry (no hit; the glossary already uses "model" for an exemplar); `agent-instructions/README.md` lines 1-60: how a collision with no precedence is handled in the-way.

## Working copies

None made as a worktree or a clone. Two output files of the foundation's index script stand in `.runs/review-whole/` (`sections.md`, `index.md`), under the ignored `.runs/`; they are the index of my selection, kept for the report, not removed.

## Unread material

- Decisions of the index of my selection read whole: 8 (WAY-113 with *Rejected*, WAY-166, WAY-123, WAY-120, WAY-33, WAY-35, WAY-155, WAY-378). Read in part: WAY-25 (binding paragraphs and the start of *Verification*), WAY-114 (binding sentence, *Scope*, *Relations*, the start of *Verification*), WAY-165 (binding sentence and the start of *Verification*), WAY-137 (binding sentence and the start of *Verification*), WAY-174 (its last part only, lines 9595-9640), WAY-118 (heading only). The index's other listed decisions I read by their binding sentences in the index and by the run through the headings; none bears on the change beyond what is named above.
- The glossary, the invariants and the part-map entries: the part map read whole (its first 140 lines hold the parts `decisions` and `elements-common`); the glossary was searched, not read whole; the invariants file was not opened (the invariants of WAY-35 are named in its *Verification*, and the author ran the tests of `elements/common`).
- Guidelines: `guidelines/coding.md`, `guidelines/testing.md`, the coding-kind files: not read, since the change writes no code and no test.
- `product-guidelines/reading.md`: read to the end of "Select and read".
- `elements/decisions/template.md` and the examples: not read; the form of the entry was judged by WAY-05 and `foundation_check.py`.
- The author's report: read whole. The frozen task: read whole. `cycle.md` and other files of `.runs/task-cycles/...`: not read, as the handoff says.

## Searches not found or unclear

- No rule or check names a column width for `foundations/decisions.md` (M1 stays polish).
- Whether the definition of a project can state an agent's check of the running product as its goal or measure of success: the definition template does not forbid or require it; I found no definition in the repository that does (the-way has none), so I2/I1's case is read from the texts alone, not from an example.
- The decision's template (`elements/decisions/template.md`) was not read, so the form of the *Verification* clauses was compared with the entry's own existing clauses and WAY-12, not with the template.
