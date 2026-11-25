# Author report — fix 2 (recommendation-not-below-goal)

Status: `blocked` — M1 and M2 are fixed and committed; only I1 waits for the human, with the wording of
I1's place unchanged.

Commit of the fix: `3130f1d9d0802b07acc90fb798e9f5832a7996c7` (on the reviewed head `42298f2a`), three
files: `elements/common/critique/prepare.md`, `elements/common/way_of_working.md`, `foundations/decisions.md`
(WAY-113 only). Against the base the whole change is now 3 files, 55 insertions, 10 deletions.

## Checks (after the fix)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B instruction-files/check_instructions.py .` | 0 (0 error, 0 warn, 5 info) |
| `python -B gate/run_tests.py elements/common` | 0 (316 tests, OK) |
| lines the whole change adds over 100 characters (script count over `git diff 301e4eae`) | 0 lines |

Not run: the full suite (the cycle's).

## M1 — fixed

`elements/common/critique/prepare.md`: the paragraph "Give the fresh agent the complete proposal or set" is
re-wrapped to 100 columns from its first line on; no word changed (the old lines the change had left
ragged are now filled; `git diff HEAD~1` shows only line breaks moved).

## M2 — fixed with a few words, by a route the foundation already gives

The goal paragraph of WAY-113 and the bullet of `elements/common/way_of_working.md` end the list of places
where a goal held not worth its cost is settled with: "the goal of an independent task with the human in
the same refinement, or in its cycle through a blocked draft request (WAY-227)". The route is not new:
WAY-227 ("Where does the human meet a task cycle's work?") says the request is the cycle's point of human
review and that a question the cycle cannot settle ends the cycle on a blocked draft request in which the
human meets it; WAY-30 sends a contradiction found in implementation to the human on the task branch; the
foundation step returns a question for the human as `blocked`, and the orchestrator opens the blocked draft
request. No new rule, nothing the task settles is changed: the words only name where the question goes once
no refinement is under way. The paragraph stays within three sentences; by my count 172 words (limit 300);
`foundation_check.py` is quiet.

Rejected: leaving it as the task words it ("with the human in the same refinement"): the reviewer is right
that the sentence has no place for a question asked inside a cycle, and the fix costs eleven words.

## I1 — not settled; the question for the human

No fix is made. The reviewer and I agree that no passage the human accepted gives the outcome (the task's
questions 1, 2 and 4 and its rows say nothing of WAY-166, the technology step or a goal that is an agent's
check), so WAY-25 says: stop and ask.

### The case, in plain words

In the technology step of a task whose need is that an agent can check the running product (for example
"an agent can read the product's logs"), every option of the logs may be a panel only a human can read.
WAY-166, with its copies in `project-level/technology/settle.md` and `project-level/definition_template.md`,
says: recommend by cost and upkeep, and say in one sentence that no option lets an agent check the running
product this way, so the check stays with the human. The new paragraph of WAY-113 says: a way below the goal
is never recommended, and where no way reaches the goal the question recommends none. WAY-166's *Rejected*
refuses "recommending nothing" here by name, as "an exception to WAY-113".

### Question for the human

1. In that case — the material's goal is an agent's check of the running product and no option reaches it —
   which of the two decisions holds?

   a. **WAY-166 prevails in its area** (my recommendation in the first fix). WAY-166 gets `narrows WAY-113`
      and states the area in its binding sentences ("also where the material's goal is that an agent checks
      the running product"); its *Rejected* line and *Rationale* are aligned with that. WAY-113 and the
      copies in `settle.md` and `definition_template.md` stay as they are. Once chosen: the step recommends
      by cost, says in one sentence the check stays with the human, and the human takes or changes the
      recommendation. Cost: one relation and a sentence in one decision; in that one area a recommendation
      reaches below the goal with its lack named in a sentence. Undoing: remove one relation and a
      sentence — cheap.
   b. **The same outcome, written in WAY-113** as a clause of the new paragraph ("except in a choice of an
      agent's way to the running product, where WAY-166 gives the recommendation"). Cost: as a, with the
      exception written in the general decision, not in the narrow one (the form WAY-25 does not use for a
      precedence). Undoing: remove one clause — cheap.
   c. **The goal rule overrides everywhere**: where no option can be used by an agent, the question
      recommends none. WAY-166's binding sentences, *Verification*, *Rationale* and *Rejected* change, and so
      do `settle.md` and `definition_template.md`. Once chosen: the human answers each such choice with no
      recommendation. Cost: edits in four places, an approved decision turned round, and the steps that
      presume a recommendation (the risk tests of WAY-138, "you choose" of `settle.md`) get no case.
      Undoing: four places — dear.
   d. **The goal rule prevails only where the goal itself is that an agent checks the running product**
      (the reviewer's recommendation). WAY-113 gets `narrows WAY-166` with that area in its binding
      sentences; `settle.md` and `definition_template.md` carry the same area; `settle.md` gets a step for
      a choice with no recommended option (what the risk tests run on, what "you choose" means there).
      Outside that area WAY-166 stays as it is, since where the material sets no such goal no option falls
      below it. Once chosen: a task or definition with such a goal gets a choice with no recommended
      option, and the human chooses between the options by their costs. Cost: edits in WAY-113,
      `settle.md` (twice) and `definition_template.md`, WAY-166's *Rejected* line and *Rationale* aligned,
      one new step to word; it overrides the approved refusal in WAY-166's *Rejected* ("the human answers
      with no hint"). Undoing: four to five places — dear.

   **Where the reviewer and I differ.** I recommended a, the reviewer d. The difference is what the human
   gets in the one area: with a, a recommendation that gives less than the goal, with the lack named in one
   sentence; with d, no recommendation, and the lack is the question.

   **What I would give now: d.** I weighed the first fix mainly by cost and by the form WAY-25 gives (the
   narrower decision records `narrows`), and I gave too little to the human's answer to question 2, which
   refused exactly "recommended, when its weak point says it falls below the goal". With a, WAY-166's one
   sentence beside a recommended option is that way: the very error the task removes, kept in the one area
   where the goal is stated. With d, the rule has an exception only where WAY-166's own premise ("an option
   an agent cannot use is a consequence") would otherwise stand against a goal, and the precedence is
   recorded as WAY-25 gives it; WAY-166 stays for every other choice.
   Weak point of d, the strongest argument against it: it costs four to five edits in four files, it
   overrides a refusal the human accepted in WAY-166 ("the human answers with no hint"), and it needs a new
   step in `settle.md` that no accepted text words, so the human would have to approve that step too.
   The cheaper way, a, is right if the human holds WAY-166's refusal a deliberate exception that
   outlasts this rule; b is a only written in another place (I do not recommend it).

The change is committed with I1's wording as it stands (WAY-113's goal paragraph, no `narrows` recorded);
nothing of a, b, c or d is written.

Not in the question, named for whoever carries it: `product-guidelines/*/new_tools.md:4` restate "Give a
recommendation and the weak point of the option recommended" with no word for a question that recommends
none; the reviewer left them out of the task. They would follow the human's answer if it is c or d.

## Own-work check (WAY-164)

- **Requirement likeliest not met by this fix:** M2 adds words to a binding sentence, so the added words
  must name a route the foundation already gives and no new rule, and the paragraph must stay within the
  limits; M1 must change no word.
- **Check:** read WAY-227 (the request is the cycle's point of human review; a question the cycle cannot
  settle ends on a blocked draft request), WAY-30 and `task-cycle/skill/foundation_step.md` ("returns it
  with the status `blocked`, and the orchestrator opens the blocked draft request holding it") for the
  route; `foundation_check.py` (0 errors) for the limits; `git diff HEAD~1 -- elements/common/critique/prepare.md`
  for M1 (line breaks only; the added lines of the change are all 100 columns or fewer).
- **What it showed:** both hold. A finding I hold wrong: none.

## Meaning sentences (entry changed)

WAY-113 — `row 1`, with eleven words added at the end of the goal paragraph (M2).

- English: A recommendation in a decision question gives no less than the goal the material sets to the
  work, and no less than the model the goal names, feature by feature; a way below the goal is listed with
  what it lacks and never recommended, a question where no way reaches the goal recommends none, and a
  goal held not worth its cost is asked as a separate question settled where the goal stands, which for an
  independent task is the same refinement, or in its cycle a blocked draft request.
- Polish: Rekomendacja w pytaniu o decyzję daje nie mniej niż cel, który materiał stawia pracy, a przy
  celu ze wzorcem nie mniej niż wzorzec, cecha po cesze; wariant poniżej celu stoi wśród wariantów z tym,
  czego mu brakuje, i nigdy nie jest polecany, pytanie, w którym żaden wariant nie osiąga celu, nie poleca
  żadnego, a uwaga, że cel nie jest wart swojego kosztu, idzie jako osobne pytanie o zmianę celu,
  rozstrzygane tam, gdzie cel stoi — dla zadania niezależnego w tym samym doprecyzowaniu, a w jego cyklu
  przez zablokowany szkic requestu.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-227 (the route of M2): read the passage found by a search of "blocked
  draft request" (lines of WAY-227 and the cited ones, not the whole entry) and the heading; WAY-30
  binding paragraph. Named because the handoff names the routes by number only.

## Working copies

None made. Check outputs stand under the ignored `.runs/` (`author-fix2-tests.txt`).

## Unread material

- WAY-227 and WAY-30: read in part (the passages found by the search above), not whole; the handoff names
  them as routes, not as entries to read.
- `project-level/technology/settle.md` and `project-level/definition_template.md`: read in the first fix
  (lines 28–46 and 236–250), not whole.
- The review report and findings: read whole.

## Searches not found or unclear

- A step in `project-level/technology/settle.md` for a choice with no recommended option (the risk tests,
  the answer "you choose"): not found (confirmed by the reviewer and by my reading of the cited lines).
