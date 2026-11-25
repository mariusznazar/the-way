# Author report — recommendation-not-below-goal

Status: `done`

Commit: `7c2502a73f8360d9e47af85863c522392ec6c192` on `task/recommendation-not-below-goal` (base `301e4eae`).

## Files changed

| File | Added / removed lines |
|---|---|
| `foundations/decisions.md` (WAY-113: new binding paragraph, *Verification* complies and violates, *Rationale*, *Rejected*) | +37 / -4 (the four removed lines are lines of the same entry re-ended where text was appended) |
| `elements/common/way_of_working.md` (rule "How a skill asks", bullet "A question of decision") | +9 / -1 |
| `elements/common/critique/prepare.md` (paragraph "Give the fresh agent the complete proposal or set") | +3 / -1 |

Total by `git diff --stat HEAD~1`: 3 files, 49 insertions, 6 deletions. Untouched on purpose:
`elements/common/critique/check.md`, `elements/common/critique/SKILL.md`, WAY-120, WAY-166, every skill
description (no entry point regenerated).

## What I wrote

- **To do 1 and 2 / row 1:** one new paragraph of WAY-113's binding sentences (3 sentences, about 140
  words), placed right after the first paragraph, so the first paragraph (already 3 sentences) is
  untouched and `foundation_check.py` stays quiet. It says: the way recommended gives no less than the goal
  the material sets to the work (task goal in a plan, need in a task document, goal and measure of
  success of a definition), and against a model no less than the model gives, feature by feature; a way
  below the goal stands among the ways with what it lacks on its own line and is never recommended; where
  no way reaches the goal the question recommends none and says so; a goal held not worth its cost is a
  separate question of decision, also where no way reaches it, settled where the goal stands (plan with
  its owner, definition by the approval of readiness (WAY-118), independent task's goal with the human in
  the same refinement). The same content stands, once, in the bullet "A question of decision" of
  `elements/common/way_of_working.md`, as row 1 asks (that bullet already carries WAY-113's rule in
  prose).
- **To do 3 / row 2:** in `prepare.md`, after the sentence that lists what the fresh agent gets: "Where the
  proposal or the set holds a question of decision to a human, the rules given always include "How a
  skill asks" in `elements/common/way_of_working.md`." No copy of the rule's content in `check.md`,
  `SKILL.md` or any skill that asks (WAY-35).
- *Verification* of WAY-113: complies and violates each gained the clause for the new rule (recommended way
  not below goal / model feature by feature; way below goal not recommended; none recommended where no way
  reaches the goal; goal not worth its cost asked as its own question). *Rationale* gained the reasons and
  the price (a question that may recommend none; one question more where an agent holds a goal too dear).
  *Rejected* gained the three ways of the rows' sources: the rule only for a goal with an explicit model,
  a way below the goal recommended when its weak point says so, the rule with no word on the case where no
  way reaches the goal. The ways of question 3 (a point in `check.md`, no change) belong to row 2, a file
  of instructions, not to the decision, so they are not in *Rejected* (WAY-134).

Choices of the words and the division (yours, per the handoff): the new sentences stand in a paragraph of
their own, as a part of the question of the heading the entry sets apart (template "Binding sentences").
Rejected: adding the sentences to the first paragraph (it would pass 3 sentences and `foundation_check.py`
would report it). Cost if wrong: the check reports an excess, which the run shows it does not.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (no `--skip-test-citations`; no invariant of mine reads `test`) | 0 (`0 errors`), run twice (before and after the commit) |
| `python -B gate/run_tests.py elements/common` | 0 (316 tests, OK) |
| `python -B instruction-files/check_instructions.py .` | 0 (0 error, 0 warn, 5 info) — files I edited are not instruction files read by it; run to be sure |

Not run: the full suite (WAY-160, the orchestrator's), any test of another directory: no test file under
`foundation-review`, `task-cycle`, `project-level` or elsewhere cites `way_of_working.md`, "How a skill
asks", `critique/prepare.md` or WAY-113 (grep of `test_*.py`, no hit), so the change reaches no test but
the checks and templates read in `elements/common`. I wrote no test and no code, so the guidelines of
code and tests were not read, and no failing-test run applies. `skill_entry_points.py --write` not
needed: no skill's description or name changed.

## Own-work check (WAY-164)

- **Requirement likeliest not met:** "no less than the goal" covers every goal the material sets and not
  only a goal with a pattern (question 1), and the new sentences leave "the goal is not worth its cost" a
  separate question (question 2 and 4) instead of a weak point of a recommended way.
- **Check:** read the new paragraph against the answers of questions 1, 2, 4: the first sentence names the
  three goals of question 1 by their places and treats the model as a second clause ("where the goal
  compares the result with a model"), so a goal with no model is covered by the first clause alone; the
  third sentence makes the goal's cost a question "of its own", "also where no way reaches it", and the
  *violates* clause names the weak-point route as a violation. `foundation_check.py` on the result:
  0 errors, so the paragraph is within 3 sentences and 300 words and the binding part within 600.
- **What it showed:** both hold in the wording. Limit: I did not run a separate test that the script counts
  WAY-113 as altered (it reports a decision a change alters); the exit 0 with the entry changed is what
  I rely on, and the paragraph is, by my count, 3 sentences and about 140 words.
- Second place checked: `check.md` stays as it was (`git diff` names no change to it).

## Search of the foundation (WAY-33) and WAY-166

- Entries that name WAY-113 (grep `WAY-113` in `foundations/`, `elements/`, `project-level/`,
  `product-guidelines/`, `process-audit/`): the derived decisions (the ones whose *Relations* say
  `derives from WAY-113`, including the technology step's and the styleguide's) add their own rules and
  none says a recommendation may fall below a goal; WAY-123's "simplest and cheapest" recommendation
  applies only where no difference with a consequence for the product remains, as the task says. No change
  needed to them. Glossary, invariants, part map: no entry of "recommendation" or "question of decision".
- **WAY-166 (read whole, with *Rejected*):** judged no collision. WAY-166 treats whether an agent can use
  an option as a *consequence* of an option compared with others, and recommends by the other
  consequences where no option can be used. The new rule speaks of a *goal the material sets to the
  work* (plan goal, task need, definition goal and measure of success); the agent's use of an option is
  none of those, so the case WAY-166 settles is not a way "below the goal". I left WAY-166 unchanged and
  recorded no precedence (no WAY-25 passage needed). The one place a collision could still arise is a
  project definition that states "an agent checks the running product" as its goal or measure of success;
  then the new rule applies to the question and the human would be asked, instead of a recommendation by
  cost. Name this for the reviewer; I did not correct WAY-166 because no accepted text gives that outcome.
- WAY-120 unchanged, as the task says; the new `prepare.md` sentence says which rule is always among
  "applicable rules" and does not restate WAY-120.

## Meaning sentences of each entry written or changed

Entry: WAY-113 (changed, binding paragraph, *Verification*, *Rationale*, *Rejected*) — `row 1`.

- English: A recommendation in a decision question gives no less than the goal the material sets to the
  work, and no less than the model the goal names, feature by feature; a way below the goal is listed with
  what it lacks and never recommended, a question where no way reaches the goal recommends none, and a
  goal held not worth its cost is asked as a separate question settled where the goal stands.
- Polish: Rekomendacja w pytaniu o decyzję daje nie mniej niż cel, który materiał stawia pracy, a przy
  celu ze wzorcem nie mniej niż wzorzec, cecha po cesze; wariant poniżej celu stoi wśród wariantów z tym,
  czego mu brakuje, i nigdy nie jest polecany, pytanie, w którym żaden wariant nie osiąga celu, nie poleca
  żadnego, a uwaga, że cel nie jest wart swojego kosztu, idzie jako osobne pytanie o zmianę celu,
  rozstrzygane tam, gdzie cel stoi.

Row 2 goes to an instruction file (`elements/common/critique/prepare.md`), so no entry is written for it
(foundation step). Its meaning, for the request: Polish — Gdy krytyk dostaje propozycję albo zestaw z
pytaniem o decyzję do człowieka, wśród reguł podanych krytykowi zawsze stoi „How a skill asks”, w jednym
miejscu, bez kopii jej treści.

No entry marked `projected` or `the cycle's`; no pair of examples added beyond the *Verification* clauses
of row 1 (the entry already carried an agent-compares pair, which I extended; no test holds WAY-113's
sentences, so the pair stays).

## Reaches beyond the dispatch

- `elements/decisions/skill/read.md` and `elements/decisions/skill/decide_entry.md` (the decision skill's
  files named by `SKILL.md`), `elements/common/rules.md` first 150 lines: read for the entry; named by the
  skill I was told to read. `agent-instructions/README.md` "Make the change" (the handoff names it).
  `instruction-files/check_instructions.py` head (to find the check the handoff asks me to find).
  `foundations/decisions.md` WAY-118 heading (to confirm the identifier cited). Nothing else outside the
  handoff.

## Working copies

None made (the `.runs/author-fc.txt` and `.runs/author-tests-common.txt` outputs under the ignored
`.runs/` are check outputs, not copies; left there).

## Unread material

- `agent-instructions/README.md`: read only "Make the change" (lines 38–55) and the start of "Check the
  change", not the whole file.
- `elements/common/rules.md`: read the first 150 lines (the whole file was not needed; the rest holds no
  rule of a decision's prose).
- WAY-33, WAY-35, WAY-25, WAY-114, WAY-120, WAY-166, WAY-113: read whole.
- `guidelines/coding.md`, `guidelines/testing.md`: not read, since no code and no test was written.

## Searches not found or unclear

- Instruction-file check for the files I edited: `check_instructions.py` reads the root instruction files
  and the skills they name; I found no separate check for `way_of_working.md` or `prepare.md`, so I ran
  it on the repository root as a whole.
- No test cites WAY-113 by a line `decision:`, so no test needs to be changed (grep of `test_*.py` for
  `WAY-113`, no hit).
- The count of *Verification* words of WAY-113 is not limited by the script (only binding sentences); no
  check read this.
