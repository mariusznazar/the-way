# Author report — fix 1 (recommendation-not-below-goal)

Status: `blocked` — I2 and M1 are fixed and committed; only I1 waits for the human.

Commit of the fix: `42298f2a81d8d4600b7a3769ab5ab6795510f0f6` (on the reviewed head `7c2502a7`), changing
`foundations/decisions.md` only (+17 / -17 lines of the fix; the whole change against the base stays
three files). The wording of I1's place (the paragraph's text, WAY-166, `settle.md`,
`definition_template.md`) is as the reviewed head left it.

## Checks (after the fix)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B instruction-files/check_instructions.py .` | 0 (0 error, 0 warn, 5 info) |
| `python -B gate/run_tests.py elements/common` | 0 (316 tests, OK) |
| lines the whole change adds over 100 characters in `foundations/decisions.md` (script count over `git diff 301e4eae`) | 0 lines |

## I2 — fixed by moving the paragraph

- Choice: I moved the new paragraph of WAY-113 to the end of its binding sentences, after the paragraph on
  refinement (its text unchanged but for the wrap of M1). The base's first two paragraphs are now
  byte-for-byte as at the base (`git diff 301e4eae` shows only the added paragraph after them), so "that
  question" and "the rule above" keep their antecedents and no existing binding sentence is restated
  (WAY-263).
- Rejected: naming the question in the second paragraph ("the question against that choice"): it edits an
  existing binding sentence, and "the rule above" of that paragraph's last clause would still have the
  new paragraph above it.
- `foundation_check.py` stays at 0 errors (the entry stays 4 paragraphs of at most 3 sentences).
  The new paragraph still makes sense away from the first one: "the way recommended" is the phrase the first
  paragraph defines.

## M1 — fixed

The lines the change added to WAY-113 (the new paragraph, the *Verification* clauses, the *Rationale* and
the run-on *Rejected* text) are re-wrapped to 100 characters or fewer; the old line the new *Rejected* text
ran on after is wrapped where the new text starts. The words are unchanged.

## I1 — not settled; the question for the human

First, I judged it against what the human accepted (the frozen task) and WAY-25. No passage gives the
outcome. The task's answers to questions 1, 2 and 4 say "każdy cel, który materiał stawia pracy", "nigdy
jako polecany" and "gdy żaden wariant nie osiąga celu, pytanie nie ma wariantu polecanego"; none names a
choice of an agent's way to the running product, WAY-166, the technology step or a goal that is an agent's
check. *Context* and *Decisions in play* name only WAY-113 and WAY-120, and the *Context* line on WAY-123
says only that "poleć najprostszy i najtańszy wariant" does not collide. Read generally, "każdy cel"
could be taken to cover this case too, but read so it would silently reverse a decision whose *Rejected*
line refuses exactly that ("the step recommending nothing where no option can be used by an agent — an
exception to WAY-113"), and the task does not say it means to. A passage that needs reading in as the
answer to a decision it never names is no outcome "given" (WAY-25). So the ways below are the human's.

### Question for the human

1. Where the material's goal is that an agent checks the running product, and no option can be used by an
   agent (a task's need "an agent can read the logs", or a definition's goal or measure of success with
   the same content), the new rule of WAY-113 ("where no way reaches the goal, the question recommends
   none") and WAY-166 (and its copies in `project-level/technology/settle.md` and
   `project-level/definition_template.md`: "the recommendation goes by the other consequences and says in
   one sentence that no option lets an agent check the running product this way") give opposite
   outcomes. What does the human want for this case?

   a. **WAY-166 prevails in its area.** WAY-166 gets `narrows WAY-113` in its *Relations* and its binding
      sentences state the area ("in a choice of an agent's way to the running product … this holds also
      where the material's goal is that an agent checks it"); its *Rejected* line on "an exception to
      WAY-113" is corrected to say the same. WAY-113's new paragraph, `settle.md` and `definition_template.md`
      stay. Cost: one edit of an approved decision, no change of its meaning; the human gets, in this one
      area, a recommendation that reaches below the goal, with the lack said in one sentence. Undoing: remove
      one relation and one sentence — cheap.
   b. **The case stays under WAY-166 by a clause in WAY-113's new paragraph** ("except in a choice of an
      agent's way to the running product, where WAY-166 gives the recommendation"). Cost: the same
      outcome as a, with the exception written in the general decision instead of the narrow one, the
      form WAY-25 does not use for a precedence; one clause that WAY-113's 3-sentence paragraph must hold.
      Undoing: remove one clause — cheap.
   c. **The goal rule overrides; WAY-166 is changed.** Where no option can be used by an agent, the
      question recommends none and says so; WAY-166's binding sentences, its *Rejected* line, `settle.md`
      and `definition_template.md` change with it. Cost: three edits in three files (an approved decision
      included), the step no longer gives the human a hint where the human cannot choose from agent-use
      anyway, and the human answers every such host with no recommendation. Undoing: three places — dear.

   My recommendation: **a**. It is the form WAY-25 gives (the narrower decision records `narrows` and its
   area), it keeps both decisions as the human accepted them, and the lack that reaches below the goal is
   still said to the human in one sentence at the choice, which is what WAY-166 was written to guarantee.
   Its weak point, the strongest argument against it, anchored in the task's own *Context* (Mariusz, 2026-11-25:
   "rekomendacja jest, żeby nie robić rzeczy, czyli żeby było gorzej"): a is the one place where a
   recommendation is allowed to give less than the goal, which is the error the task removes, and the way
   that would be right were consistency no matter is **c**, where the rule has no exception; I do not
   recommend c because it costs three files and takes the hint from the human in the one choice where
   all the options are human-only.

The change is committed with I1's wording as it stands (WAY-113's new paragraph, no `narrows` recorded);
nothing of a, b or c is written.

## Own-work check (WAY-164)

- **Requirement likeliest not met by this fix:** that I2's fix changes no binding sentence of the entry
  except by adding the paragraph (WAY-263), and that the move leaves each paragraph of the entry within
  the limits.
- **Check:** `git diff 301e4eae -- foundations/decisions.md` (the first hunk): the added paragraph stands
  after the base's second paragraph and the base's first two paragraphs show no changed line;
  `python -B elements/common/foundation_check.py` exits 0 with `0 errors`.
- **What it showed:** both hold. Findings I held wrong: none.

## Meaning sentences (entries changed)

WAY-113 — `row 1`, wording only (paragraph moved, lines re-wrapped); the meaning is unchanged from the
report of the first return.

- English: A recommendation in a decision question gives no less than the goal the material sets to the
  work, and no less than the model the goal names, feature by feature; a way below the goal is listed with
  what it lacks and never recommended, a question where no way reaches the goal recommends none, and a
  goal held not worth its cost is asked as a separate question settled where the goal stands.
- Polish: Rekomendacja w pytaniu o decyzję daje nie mniej niż cel, który materiał stawia pracy, a przy
  celu ze wzorcem nie mniej niż wzorzec, cecha po cesze; wariant poniżej celu stoi wśród wariantów z tym,
  czego mu brakuje, i nigdy nie jest polecany, pytanie, w którym żaden wariant nie osiąga celu, nie poleca
  żadnego, a uwaga, że cel nie jest wart swojego kosztu, idzie jako osobne pytanie o zmianę celu,
  rozstrzygane tam, gdzie cel stoi.

## Reaches beyond the dispatch

- `project-level/technology/settle.md:28-46` and `project-level/definition_template.md:236-250`: read, to
  quote the sentences of I1 and judge it (the reviewer's findings name them).

## Working copies

None made. Check outputs `.runs/author-fix1-tests.txt` stay under the ignored `.runs/`.

## Unread material

- `task-cycle/change/fix.md`: read whole after the fix (it asks for each finding fixed with its check, or contested with evidence: the report holds that; the fix of M1 stays as small as the finding, a re-wrap with no word changed).
- The review report and findings: read whole. The frozen task: read whole in the first turn. WAY-25,
  WAY-166, WAY-113: read whole in the first turn; `foundation_step.md` read whole in the first turn (the
  sentence on a collision with a current entry included).

## Searches not found or unclear

- Whether the human gave an outcome for the goal that is an agent's check of the running product: I found
  none in the task's questions, sources, settlements or *Context* (read for the words "WAY-166", "agent",
  "running product", "log"; none appears), so the case goes to the human.
