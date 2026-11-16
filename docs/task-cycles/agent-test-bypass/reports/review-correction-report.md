FAIL 637d7787cade17fa6d338e70df0ce4c85a8e478b

# Review of correction 1 — agent-test-bypass

Range `20332036..637d7787`, one commit (`637d7787`, "Correction 1: WAY-134 narrows WAY-100 on what
a decision from a row puts in Rejected, and refinement shows the parts a practice leaves out as
ways"), five files: `foundations/decisions.md`, `elements/decisions/template.md`,
`elements/common/skill/task_variant.md`, `project-level/task/template.md`,
`project-level/task/skill/find_settlements.md` (64 added, 10 removed). `git rev-parse HEAD` is
`637d7787cade17fa6d338e70df0ce4c85a8e478b`, the head given. Reviewed as `task-cycle/review/fix.md`
gives for a correction: the remarks (`reports/correction-1-remarks.md`) take the findings file's
place, then the diff is reviewed as section 2 of `task-cycle/review/SKILL.md` gives.

Counts: 1 blocking (Important, within the correction), 1 Minor, 0 out of scope.

## The remarks

Item 1 of the remarks, part by part:

- **"the second rule narrows the first"** — made. WAY-134 *Relations* reads `derives from WAY-33 ·
  narrows WAY-114 · narrows WAY-100` (`foundations/decisions.md:5315`), and its new second
  paragraph states the area where it prevails (`:5304-5310`), as the template's "Relations and
  precedence" and WAY-25 give. WAY-100 names no `narrows` back, so the two do not narrow each other.
- **"refinement puts what an adopted practice leaves out among the ways the person weighs, so the
  row that settles it names them"** — made in substance: WAY-134 `:5304-5306`; the task template's
  *Questions to settle* (`project-level/task/template.md:148-150`) and *Source*
  (`:222-225`); `find_settlements.md:29-31`; `task_variant.md:33-38`. One part goes beyond the answer
  and contradicts WAY-134: finding 1.
- **"Write that answer into both rules where they stand, so that each names the other"** — made.
  WAY-100 gains a third paragraph naming WAY-134 and the outcome (`:208-210`), a pair and a sentence
  of *Rationale*; WAY-134 names WAY-100 in its binding sentences and *Relations*; the decisions
  template's bullet on the *Rejected* of a decision written from a row carries it
  (`elements/decisions/template.md:93-97`).
- **"and into the refinement step that builds the rows of settlements"** — made, in the three places
  that build the rows (`task_variant.md`, `find_settlements.md`, the task template). They disagree
  on the state of such a row: finding 1.
- **"The two new decisions of this request stay as they are now"** — made. The diff has no hunk in
  WAY-409 or WAY-410. Both comply with the rule as narrowed: their *Rationale* names what they take
  from the card and the paper (WAY-409: "The signals are those the card and the paper name…";
  WAY-410: the option to hand a task to a human), and their *Rejected* holds only the ways their
  rows' sources keep, with no left-out part — the case "where the source keeps none".

## Findings

### Important — within the correction

**1. The refinement step now makes a row that repeats the human's choice wait for the human's
acceptance when it adopts an outside practice. WAY-134 forbids that, and the task template, the
third copy of the step, still says such a row enters accepted.**

Place: `elements/common/skill/task_variant.md:33-38` ("A candidate that adopts a practice from
outside the product (WAY-100) is built `waiting` and not as the human's choice unless the question
that settled it showed the parts the practice leaves out among its ways … before the row is
accepted") and `project-level/task/skill/find_settlements.md:29-31` ("where the human did not see
them as ways, the row waits and a question shows them, before the row is accepted").

What is wrong. WAY-134, the entry this correction changes, keeps its rule that a row repeating a
choice the human made between ways shown enters accepted:

- binding sentence (`foundations/decisions.md:5283-5285`): the task document keeps "those that
  repeat a choice the human made between ways shown included unless the human struck them";
- *violates* (`:5344-5346`): "a row that repeats the human's choice between ways shown waits for the
  human's acceptance like a row the agent derived";
- *Rejected* (`:5398-5399`): "every row accepted separately, as before — a second consent to the
  same choice".

The new second paragraph of WAY-134 (`:5304-5310`) asks the refinement to show the left-out parts
among the ways of the question. It says nothing about the row's state, and it creates no exception
to the rule above. The remark does not either: it asks that refinement put the left-out parts among
the ways the person weighs. A row such as row 1 of this task — the answer to question 1, chosen
among ways shown, whose *Not chosen* holds no part of the card or the paper — would under
`task_variant.md` start `waiting`. Step 5 does not close until it is accepted, so the human gives a
second consent to a choice already made: exactly WAY-134's *violates* example.

The three copies of the step also disagree. `project-level/task/template.md:208-209`, which
`task_variant.md` step 1 orders read "in full", keeps the unqualified "A row that repeats a choice
the human made between ways shown enters accepted, and the human cuts only the rows the agent
derived (WAY-134)". So does `elements/common/skill/build_table.md:17-21` ("is built `accepted`, not
`waiting`"), and `task_variant.md:39-41` repeats it four lines below the new exception. A refiner
reading the template and `build_table.md` builds the row accepted; one reading the new bullet builds
it waiting.

This is the author's own choice 3 (`author-correction-report.md`), which the answer does not give.
Its reason — building the row accepted "is what let the parts slip through unseen" — does not hold:
an accepted row can still get the question that shows the left-out parts. The answer then goes into
the row's *Source*, as `task_variant.md` step 4 already does for a question against a choice ("write
each answer into the row, with the ways that question showed and the human did not take in the row's
*Source*").

Why it matters. Each refinement of a task that adopts an outside practice re-asks the human to
accept a choice already made. That is the second consent WAY-134 rejected. A refiner following the
task template does the opposite, so the step behaves differently depending on which file is read.

What would fix it, the narrowest way: in `task_variant.md` and `find_settlements.md`, drop the
`waiting` state and keep the question. The row repeating the human's choice enters `accepted` as the
human's choice. Where its source keeps no left-out part, the question of "How a skill asks" shows
those parts as ways, and the parts the human turns down go into the row's *Source* (or the *Not
chosen* of its question) before the table closes. Making the row wait would instead need WAY-134's
first paragraph, its *violates* and its *Rejected* changed — a change of meaning the remark does not
give.

Grade: Important by WAY-263. The change's files do what an entry the change itself changes
forbids, and they restate it more broadly than the entry allows.

Contradiction: yes — WAY-134 (its first binding paragraph, and its *violates* example "a row that
repeats the human's choice between ways shown waits for the human's acceptance like a row the agent
derived").

### Minor — within the correction

**2. "The parts the practice leaves out" reads as what the practice itself omits, not as the parts
of the practice the decision does not take.**

Place: WAY-134 `foundations/decisions.md:5305`, `:5327-5328`, `:5375` ("A practice adopted from
outside leaves parts out"), `:5402`; WAY-100 `:209`; `elements/decisions/template.md:94`;
`elements/common/skill/task_variant.md:34-35`; `project-level/task/template.md:149-150` ("the parts
of the practice it leaves out", where "it" may be the question or the adoption).

What is wrong. WAY-100's own words are "what it leaves out of the practice", where "it" is the
decision. The new sentences make the practice the subject: read literally, a refiner would show the
human what the system card or the paper does not cover, not the parts of them the decision does not
take. The cited sentence that reads wrongly is WAY-134's *Rationale* "A practice adopted from outside
leaves parts out". The remark used the same shorthand ("what an adopted practice leaves out"), but
the meaning is the human's and the wording the writer's.

Grade: Minor. Most copies sit beside wording that steers to the right reading — WAY-100's "what it
leaves out of the practice", `find_settlements.md`'s "the parts of the practice the human turned
down", the task template's "each part of the practice the human turned down". So the misreading
needs a reader of one sentence alone. One wording — "the parts of the practice the decision leaves
out" — fixes every place.

## Third question: places left alone, places missed

- `task-cycle/skill/foundation_step.md:39-42` ("a decision's *Rejected*, which takes the ways not
  chosen that the row's source keeps, … as the decisions' template gives (WAY-134)") stays true:
  under the narrowed rule the left-out parts enter *Rejected* only as ways the source keeps, and the
  sentence defers to the template, which now carries the exception.
- `elements/common/way_of_working.md:140` ("a decision's *Rejected* holds an option already weighed
  and refused") is general and stays true. The file holds no rule on the *Rejected* of a row.
- Missed: `project-level/task/template.md:208-209` and `elements/common/skill/build_table.md:17-21`
  state the entry state of a repeating row without the exception `task_variant.md` adds — part of
  finding 1. No other place states what a row carries for a decision's *Rejected*. I searched
  `elements/`, `task-cycle/`, `project-level/`, `product-guidelines/` and `foundations/` for "source
  keeps", "ways not chosen", "rejected options", `WAY-134`, `WAY-100` and *Rejected*. The hits in
  `project-level/task/skill/resolve_gaps.md`, `final_review.md`, `orchestrated_mode.md`,
  `project-level/lead/answering.md`, `project-level/lead/conversation_template.md`, the three
  `product-guidelines/*/task_document.md` and `task-cycle/skill/request_template.md` carry ways not
  chosen as the template gives them and stay true. `resolve_gaps.md` asks its questions "as the
  template's *Questions to settle* gives", so it picks up the new sentence there.

## Fourth question: the copies against each other and the two decisions

Apart from the row's state (finding 1), the copies agree with WAY-134's second paragraph:

- The question that settles the adoption shows the left-out parts among its ways: WAY-134
  `:5304-5306`; the task template `:148-150`; `task_variant.md:36-37`; `find_settlements.md:30-31`.
- The parts turned down stay in the row's source and reach *Rejected*: WAY-134 `:5305-5306`; WAY-100
  `:208-210`; the decisions template `:93-95`; the task template `:222-225`.
- Where the source keeps none, no left-out part enters *Rejected* and the decision names what it
  takes in its binding sentences or *Rationale*: WAY-134 `:5306-5308`; the decisions template
  `:95-97`; WAY-100's pair `:226-228` (the pair names *Rationale* only, a subset, not a broadening).
- The precedence: WAY-134 `:5308-5310` "In this area this decision prevails over WAY-100"; WAY-100
  `:210` "there WAY-134 prevails over the paragraph above"; the decisions template `:97` "WAY-100,
  which WAY-134 narrows here". All three say the same.

No copy drops a qualification of the two decisions except the state of the row (finding 1).

## Fifth question: collisions and tests

- No new collision found beyond finding 1, which is a collision of the skills with WAY-134 itself.
  WAY-100 and WAY-134 do not narrow each other. WAY-25 is met by the `narrows` relation and the
  area stated in WAY-134. The request still has to name the precedence with the passage of the
  remark that gives it, which is the orchestrator's job in the rewritten description and not a fault
  of this commit.
- The edits of WAY-100 and WAY-134 change approved decisions in place (WAY-07), at the human's
  explicit remark on the request. The merge is the human's acceptance (WAY-14). I raise no consent
  question beyond finding 1, which goes beyond what the remark gives.
- No test reads a sentence of WAY-100 or WAY-134 (no line `decision: WAY-100` or `decision: WAY-134`
  in any file outside `.runs/`; searched). The focused runs below pass.

## The author's own-work check

The requirement the author named — that the answer stands in both rules and in the refinement step,
with WAY-409 and WAY-410 unchanged — fits the remark. The check reads wording by pattern, so it could
not catch the weakest point: whether the new step agrees with the rest of WAY-134 and with the other
copies of the step. Finding 1 lies there.

## Declined to judge

- Whether a product's task that adopts one of the-way's guideline templates counts as adopting "a
  practice from outside the product" under WAY-100 and so takes the new question. The guideline task
  documents (`product-guidelines/*/task_document.md`) have their own route, and the remark does not
  reach them.

## Checks

- `git rev-parse HEAD` — exit 0, `637d7787cade17fa6d338e70df0ce4c85a8e478b`.
- `git log --oneline 20332036..637d7787 --stat` and `git diff 20332036..637d7787` — exit 0; one
  commit, five files.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, 270 tests, OK.
- `python -B gate/run_tests.py project-level` — exit 0, 279 tests, OK.
- `python -B gate/run_tests.py installation` — exit 0, 73 tests, OK (its tests read the decision
  log and the templates the installation copies).
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK
  (`test_skill_references.py` reads skill files).
- `python -B gate/run_tests.py agent-instructions` — exit 0, 50 tests, OK (expected failures=2).
- `elements/decisions` holds no test.
- Manual: searches of `elements/`, `task-cycle/`, `project-level/`, `product-guidelines/`,
  `foundations/` as the third question gives; line-by-line comparison of the copies (fourth
  question).
- Not run: the full gate — not the reviewer's, as the dispatch gives. The author's
  `author-correction-check.py` was not run again; its claims did not bear on finding 1.

## Reaches beyond the dispatch

- `elements/common/skill/build_table.md`, read whole — the rule on the entry state of a row that
  repeats a choice, which `task_variant.md` cites.
- `project-level/task/skill/resolve_gaps.md`, read whole — whether the question that settles an
  adoption is built there.
- `elements/common/way_of_working.md` lines 20-194 ("How a skill asks", "Reading the foundation",
  "Search the foundation", "Ask, show, write").
- `project-level/task/template.md` lines 140-239 (*Questions to settle* to *Settlements to record*).
- WAY-25 binding sentences (`foundations/decisions.md:1162-1171`), read in the earlier review of
  this cycle.

## Working copies

None in the worktree. `.runs/review-correction/` was
never created. The outputs of the focused runs stood in the session's scratchpad
(files `rt_*.txt` in it)
and were removed; nothing remains.

## Unread material

- The selection: I did not write a decision index. The dispatch named the parts, and the decisions
  I relied on are those the correction changes or names. Read whole: WAY-100, WAY-134 (at the head).
  WAY-25 binding sentences only. WAY-07, WAY-14, WAY-33, WAY-113, WAY-114, WAY-313, WAY-314, WAY-315:
  not opened. Their sentences as cited in the files read (the decisions template, `way_of_working.md`,
  `resolve_gaps.md`) left nothing open for the judgment.
- `elements/common/skill/SKILL.md` and `read.md` (the skill `find-foundation-entries`): not read;
  the step the correction touches is its task variant, read whole.
- `project-level/task/skill/orchestrated_mode.md`, `final_review.md`,
  `project-level/lead/answering.md`, `project-level/lead/conversation_template.md`, the
  `product-guidelines/*/task_document.md` files: only the lines the search found.
- `project-level/task/template.md`: lines 140-239 only.
- `reports/author-correction-check.py`: not read.

## Searches not found or unclear

- A line `decision: WAY-100` or `decision: WAY-134` in any file outside `.runs/` — searched, none
  found (so no test holds a sentence of the two changed decisions).
- Whether the request's rewritten description names the precedence with the remark's passage
  (WAY-25) — not in the range; unclear until the orchestrator rewrites `request.md`.
