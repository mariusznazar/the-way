# Author report — correction 1 (recommendation-not-below-goal)

Status: `done`

Commit: `e08834e4317de5961519bed739b02f49b7a89d0f` (on head `e5a69f85`), one file: `foundations/decisions.md`
(WAY-166 only, +20 / -6 lines; entry otherwise unchanged).

## What the remarks bind, and what I wrote

The remarks answer item 1 of *Needed from you* with way **a**, with this relation: WAY-166 "nie jest
wyjątkiem od nowej reguły, tylko z góry przyjętą odpowiedzią na pytanie o zmianę celu"; where the goal is an
agent's check of the running product and no option gives it, "cel zostaje jawnie zawężony do sprawdzenia
przez człowieka — to jedno zdanie, które WAY-166 już każe napisać — i dopiero wobec tak zawężonego celu
pytanie poleca wariant najtańszy". I wrote exactly that, in WAY-166, and nothing of way b, c or d.

WAY-166, changed in place:

- **Binding sentences:** its first paragraph gained a third sentence (3 sentences, 172 words): "Where the goal
  the material sets is that an agent checks the running product, that sentence narrows the goal openly, in
  the same question, to the check by the human, and the recommendation goes against the goal so narrowed; it
  is the answer, accepted in advance, to the question of changing the goal that WAY-113 asks where no way
  reaches the goal, and it prevails in this area over WAY-113's rule that such a question recommends none."
  The first two sentences are unchanged.
- **Relations:** `derives from WAY-121 · narrows WAY-123 · narrows WAY-113`. I chose `narrows` (the form
  WAY-25 gives for a precedence: the decision that prevails names the other, and its binding sentences state
  the area) over leaving the relation unwritten; WAY-113 does not name WAY-166, so no cycle of `narrows`
  arises (the foundation check reports none).
- **Verification:** *complies* gained the case of a task whose need is that an agent reads the logs while every
  option is a panel only a human reads: the same sentence narrows that need to the human's reading and the
  option recommended is the one that wins by cost and upkeep against it; *violates* gained "leaves that goal
  as it stands beside the option recommended".
- **Rationale:** says that where the goal is an agent's check the sentence is also the change of that goal,
  made openly in the same question and not by a recommendation that falls below the goal in silence, and that
  this decision answers WAY-113's question of changing a goal in advance for this area.
- **Rejected:** the words "an exception to WAY-113," are removed from the way "the step recommending nothing
  where no option can be used by an agent" (it no longer says what the remarks say); the rest is unchanged
  and no way is added (the remarks' ways b, c, d are the request's, not an earlier source's).

Marked `the cycle's` (WAY-114/foundation step): the entry's change is a precedence the cycle records, with a
wording of my own from the remarks (not a row of the task's *Settlements to record*), and the added example
in *Verification* (the logs case) is the writer's own, kept word for word below for the request.

### Passages of the remarks that give the outcome (WAY-25), quoted

- "Needed from you 1 — **a**, z takim brzmieniem relacji: starsza decyzja (WAY-166) nie jest wyjątkiem od
  nowej reguły, tylko z góry przyjętą odpowiedzią na pytanie o zmianę celu, które nowa reguła i tak stawia,
  gdy żaden wariant nie osiąga celu."
- "W kroku technologii, gdy celem jest sprawdzenie produktu przez agenta, a żaden wariant tego nie daje, cel
  zostaje jawnie zawężony do sprawdzenia przez człowieka — to jedno zdanie, które WAY-166 już każe napisać —
  i dopiero wobec tak zawężonego celu pytanie poleca wariant najtańszy."
- "Powody: b i c stawiają Mariuszowi pytanie bez rekomendacji, a Mariusz chce, żeby pytanie do niego miało
  gotową rekomendację […] a kosztuje jedną relację i zdanie, cofnięcie tanie […]."

(Source: `reports/correction-1-remarks.md`, comment `https://github.com/mariusznazar/the-way/pull/160#issuecomment-7172993204`,
2026-11-25T19:57:34Z.) The remarks accept items 3 and 4 of the request (place of the paragraph, the eleven
words); no change was needed for them.

### The pair of examples added, word for word, for the request

- *complies*, added: "where a task's need is that an agent reads the logs and every option for them is such
  a panel, the same sentence narrows that need to the human's reading and the option recommended is the one
  that wins by cost and upkeep against it"
- *violates*, added: "or, where the material's goal is that an agent checks the running product, leaves that
  goal as it stands beside the option recommended"

## Places that restate WAY-166 or the new paragraph (WAY-33), judged for mismatch

I read them for a mismatch with the wording above and changed none:

- `project-level/technology/settle.md:34-38` and `project-level/definition_template.md:242-248` restate WAY-166's
  first two sentences ("the recommendation goes by the other consequences and says in one sentence that no
  option lets an agent check the running product this way, so the check stays with the human"). The new
  sentence narrows the goal by that very sentence, so nothing in them is false; the area where the goal rule
  yields is stated in WAY-166 alone, as WAY-25 gives for the decision that prevails.
- The new paragraph of WAY-113 and the bullet of `elements/common/way_of_working.md` ("where no way reaches the
  goal, the question recommends none"): unchanged. WAY-166 now records that it prevails in its area, so the
  general rule stays general. Cost of leaving them: a reader of `way_of_working.md` alone does not see the
  exception; adding a pointer to WAY-166 there would be a word the remarks do not give, so I did not.
- No step added for a choice with no recommended option (way c's).
- Needed more than "one relation and a sentence"? One more sentence in the *Rationale* and the clauses of
  *Verification* (the entry must say, in each of its parts, what it now says in the binding sentence); no
  other file changes.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`; WAY-166's binding paragraph 3 sentences, 172 words) |
| `python -B instruction-files/check_instructions.py .` | 0 (0 error, 0 warn, 5 info) |
| `python -B gate/run_tests.py elements/common` | 0 (316 tests, OK) |
| lines the correction adds over 100 characters (script count over `git diff HEAD`) | 0 |

Not run: the full suite (the cycle's). No test cites WAY-166 (grep of `*.py`, no hit).

## Own-work check (WAY-164)

- **Requirement likeliest not met:** that the entry records exactly the relation of the remarks and nothing
  more — the narrowing of the goal to the human's check, the recommendation against the goal so narrowed, no
  recommendation below an unchanged goal — and that no new step or way is added.
- **Check:** read the added sentence against the three quoted passages: "nie jest wyjątkiem … tylko z góry
  przyjętą odpowiedzią" → "it is the answer, accepted in advance, to the question of changing the goal";
  "cel zostaje jawnie zawężony … jedno zdanie, które WAY-166 już każe napisać" → "that sentence narrows the
  goal openly, in the same question, to the check by the human"; "dopiero wobec tak zawężonego celu pytanie
  poleca" → "the recommendation goes against the goal so narrowed". *Violates* names the case the remarks rule
  out (a goal left as it stands beside the recommended option).
- **What it showed:** each clause is carried; one wording I weighed: "the cheapest option" of the remarks
  stays "by the other consequences", WAY-166's own words (cost and upkeep, which WAY-123 reads as the simplest
  and cheapest where no consequence differs), so I did not add a word the entry's rule did not have.
- Not checked: a reading by an agent in a real technology step (no product to run it on).

## Meaning sentences (entry changed)

WAY-166 — `the cycle's` (precedence recorded from the human's remarks).

- English: Where no option of a choice of an agent's way to the running product can be used by an agent and
  the material's goal is that an agent checks the product, the goal is narrowed openly, in the same question,
  to the human's check, and the recommendation goes against the goal so narrowed; this is the answer to the
  question of changing the goal that WAY-113 asks, given in advance, and it prevails over WAY-113's rule that
  such a question recommends none.
- Polish: Gdy w wyborze drogi agenta do działającego produktu żaden wariant nie jest do użycia przez agenta,
  a celem materiału jest sprawdzenie produktu przez agenta, cel zostaje jawnie zawężony, w tym samym pytaniu,
  do sprawdzenia przez człowieka, a rekomendacja idzie wobec tak zawężonego celu; to z góry przyjęta
  odpowiedź na pytanie o zmianę celu, które stawia WAY-113, i w tym obszarze przeważa nad jego regułą, że
  takie pytanie nie poleca żadnego wariantu.

WAY-113 and the files `way_of_working.md`, `prepare.md` are unchanged by this correction.

## Reaches beyond the dispatch

None beyond the handoff (settle.md and definition_template.md lines were read in the earlier fixes and
re-read for the mismatch judgement).

## Working copies

None made; check output `.runs/author-corr1-tests.txt` under the ignored `.runs/`.

## Unread material

- `task-cycle/skill/foundation_step.md`: read whole in the first turn; reread in part (the sentences on a
  precedence between two decisions) for this correction.
- `project-level/technology/settle.md`, `project-level/definition_template.md`: read in part (the lines
  quoted above), not whole.

## Searches not found or unclear

- none. (A relation word for "not an exception but an answer given in advance" does not exist in the
  template's closed list of two types; I used `narrows`, which WAY-25 gives for a precedence, and said in the
  binding sentence what the remarks say.)
