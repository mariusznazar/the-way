# The end of an audit

What the audits of `maintain-coding-guidelines`, `maintain-styleguide` and
`maintain-testing-guidelines` do alike, so that they end alike: every finding belongs to one cause,
every cause has one weight, the causes stand in one order of repair, the first few are gone back to
and put to the human, and the rest stay in the task document (WAY-280 to WAY-285). Read it from the
checkout or pinned the-way the skill runs from, at each step of the skill that names it. It binds
these skills, never a product's code, screens or tests (WAY-173), and a weight blocks nothing.

A **finding** is one thing an audit found at one place. A **cause** is the one source of one or
more findings, which one fix removes; a single finding can make a cause.

Each discipline's audit comes first and brings here its findings, each with its place and effect:
the styleguide's with the category of each cause, coding's with the files marked `do not copy` and
the trial run's reports, testing's with the trust boundaries at which a test of refusal is due and
none exists. Step 3 takes the sections below in their order, up to and including "The list"; steps 4
and 5 take the last two.

## Merge into causes

Merge every finding into a cause: several violations from one source are one cause and one fix, and
each finding belongs to one cause (WAY-281). Two faults stay two causes where no one fix removes
both. Tell each cause in one sentence of its effect on the user or the owner.

## Weigh

Give each cause one weight. It is measured by the effect on the user or the owner, and it follows
from what is at stake, never from how many places break a rule (WAY-280).

| Weight | What it means |
|---|---|
| `grave` | a real situation in the running product ends in lost data or money, in access to someone else's data, or in the main thing a user comes for not working; harm nobody would learn of belongs here too |
| `heavy` | a user does not finish an important task or gets untrue information; a problem the owner sees and cannot trace to its cause belongs here too |
| `medium` | a user can get round it, or the harm comes with time: further files copy a bad pattern and the repair grows dearer |
| `light` | today neither a user nor the owner feels it |

- Code: an endpoint reads data from the request unchecked and lets someone reach another person's
  order — `grave`, even in one file.
- Tests: the test of a payment passes whatever the code computes — `grave`, since the fault reaches
  a customer and nobody notices.
- Screens: a delete button looks like an ordinary button — `heavy`; forty spacings typed by hand —
  `light`.

A weight has no link to a critical flow: a flaw inside one is not `grave` for that reason alone.

## A task joining code and tests

A task carrying a product's coding and testing guidelines (WAY-247) has one list, one order and one
top, made once, at the end of the audit that runs last (WAY-282). Which discipline runs first is
free.

- **Whether this audit stops.** Run the other skill's step 1 now, by the file this skill's step 3
  names. This audit stops here where that step gives the other skill the audit in this task and that
  audit has not yet run. The test is the audit that runs, never what the product has: the route of
  one kind of code and a new level of tests are no audit, so with either of them this audit ends as
  any other.
- **The audit that stops** writes its causes into *Context* in the form of "The list", weighed, with
  no number and no top. Its step 4 settles all it settles except the top, and its skill hands back to
  `refine-task` step 3, as its `hand_back.md` gives.
- **The audit that runs last** takes up the causes standing in *Context*, which carry the first
  audit's work over where the two skills run in separate sessions. From here they are the list's,
  whichever discipline found them. Merge causes of the two audits only where one fix removes both,
  the heavier weight standing, and go on through the sections below, lowering or withdrawing a cause
  of either discipline by what you see. In the order the first audit's causes get their numbers, and
  its `do not copy` lines with them.
- **What the first audit's step 4 settled stands.** The check moves a cause, never an answer of the
  human. Where the last audit withdraws a cause on which something settled rests, such as the
  `do not copy` status of a file, the status stays as the human settled it, with the `Withdrawn:`
  item as its mark, and goes back to the human with the top, as one question for each: keep it or
  change it, with what the check saw. The answer stands under the question that settled it, with its
  own source. A cause lowered touches nothing settled.

## Order

Put the causes in one order of repair, from `grave` down; within one weight the cause that removes
more and reaches less stands first (WAY-282). Beside its fix each cause shows two plain facts and no
score:

- `Removes:` how much of the problem goes with that one fix: its count of places, or what goes where
  a count says nothing;
- `Reaches:` how far the fix goes, one of `one file`, `one part` or `several parts`, `part` as the
  product's part map means it.

Where the two pull apart, judge, and let the line of the cause you put first say why in one clause.
The sentence of the fix names whatever makes it long despite a small reach. Give no hours, points or
ratio: a count of places is no number on the scale, and a weight is never turned into one.

## The top of the list

The top is the first causes of the order, counted over the whole audit and never by level of tests
(WAY-283): as many as the larger of three and the number of `grave` causes; then, up to five, the
next cause while it weighs as much as the one before it. Over five `grave` causes it holds all of
them and nothing more. With fewer than three causes it holds all of them.

## Go back

Before step 4, go back to each cause of the top: return to the places it names and see whether the
effect it describes occurs (WAY-285). This is your own check, made before the set of proposals is
complete. A cause takes the form of the discipline that found it:

- **Code:** follow the way from the input to the harm, through the lines.
- **Tests:** follow what the test asserts and see that the fault named gets past it.
- **Screens:** open the screen by the agent's way to the running product where the foundation
  settles one; otherwise go from the code, marking what shows only on a running screen.

Go back to every place given by file and line. A cause placed by a number of files has no line to
return to: read the reports behind the number, and its line says how many were followed. For a
boundary's cause, look for the test.

- What does not hold is lowered or withdrawn, and `Checked:` records what was gone back to, whatever
  the check did to the cause.
- What cannot be seen without the running product stays `Unchecked:`, its weight kept, and the human
  hears so.
- What the check lowers or withdraws moves the order. Order again and check in its turn a cause that
  so enters the top, until every cause of the top stands `Checked:` or `Unchecked:`.
- A cause withdrawn because its place shows no break takes that `do not copy` with it while the
  status is still a proposal; once a step 4 has settled it, "A task joining code and tests" gives the
  way. A cause lowered takes nothing with it.

## The list

As step 3 ends, write the list into *Context*, one list, labels in English and values in the
document's language. It opens with one item, in English, naming itself as the audit's list and
saying which places of the order are its top. Under it stands one item for each cause, in the order,
with its details nested below it, as *Questions to settle* nests them:

```markdown
- The audit's list; places 1 to <n> are its top.
- 1 — `heavy` — <the cause, in one sentence of its effect on the user or the owner>
  - Category: <one of the styleguide's four categories>
  - Places: <file and line of each; for a linter's rules the number of files; for a boundary its name>
  - Fix: <one sentence of what the one fix does>
  - Removes: <its count of places, or what goes>
  - Reaches: `one file` | `one part` | `several parts`
  - Checked: <the places gone back to and what was seen>
  - Taken: <the *To do* item>
- Withdrawn: <the cause, in one sentence> — it weighed `medium`
  - Checked: <the places gone back to and what was seen>
```

- `Category:` stands in a styleguide's list alone, one category for each cause (WAY-187).
- `Checked:` holds also the weight the cause had where the check lowered it. In its place,
  `Unchecked:` says what could not be seen and why. One of them stands on every cause the check went
  back to: the top, and a cause the check lowered out of it, which keeps its mark. A cause the human
  takes from below the top, which the check never went back to, gets no such mark.
- `Taken:` names the *To do* item, or for a boundary's cause its invariant. In its place, `Deferred:`
  gives the reason; a cause below the top that the human did not take reads
  `Deferred: below the top`. Step 4 writes both.
- A cause's data stand in its item alone; the *To do* item gives the fix and names the cause by its
  number.
- A cause the check withdraws leaves the order and stays in the list. After the last cause stands one
  item for each, with no number, opening `Withdrawn:`, holding the cause in one sentence, the weight
  it had and its `Checked:`, with no `Fix:` and no `Taken:` or `Deferred:`.
- An audit with no finding says so in one item, and has no top and no question.

## At step 4

An audit that stopped for the other discipline's leaves this section to the audit that runs last,
which puts all of it to the human, once.

- **The proposal.** Propose which causes of the top the task takes and which it defers, the weight
  proposing and the human deciding (WAY-284). A proposal to take a linter's cause takes that reason's
  files and never grows into cleaning the whole product (WAY-205). The proposal and the top join the
  set of proposals before the critique, with the full list among the critic's sources, so that a
  critic can see a heavier cause standing too low (WAY-120). A cause the author's verdict moves goes
  through the order again, and a cause entering the top is checked before the set is shown. A cause
  the verdict withdraws takes the form of a `Withdrawn:` item, its `Checked:` saying so.
- **What the human hears.** After the critique, with the rest of the set: the top and the proposal,
  each cause by its effect, never by a rule's or a technique's name, its weight in the human's
  language, as its meaning, with the sentence of what it means at first use; in the document the
  English word stays, as a marker (WAY-174). Add in one line how many causes the check withdrew or
  lowered out of the top, and where they stand. The causes below the top reach the human as one
  choice, with their number and where they stand: deferred together, unless the human takes one.
  Each settled status put back under "A task joining code and tests" comes with them.
- **A deferred `grave` cause.** For each `grave` cause the human defers, as soon as the human has
  decided, ask whether to open a task for it in the product's backlog. The skill writes no backlog
  and no plan: a yes goes to step 5. A no leaves the cause deferred in the document, and nothing
  forces a return, which is that answer's weak point.
- **What the results set off.** `settle.md` proposes the invariants of the linter and of the trust
  boundaries as it does without a list, whatever the human decides of the cause, and an invariant is
  never a second question inside the decision on the top (WAY-205, WAY-235). A boundary's cause whose
  fix is the test its accepted invariant brings stands `Taken:`, naming that invariant, also below
  the top. A linter's cause is not closed by a marked invariant.
- **Where the answers go.** Write the human's decision and each answer on a backlog task under
  *Questions to settle*, with the human's words and date, and each cause `Taken:` or `Deferred:` in
  the list. Which causes a task takes ends with the task (WAY-36), so these answers are no rows of
  *Settlements to record* and pass without the one question against an answer.

## Before handing back

Check that every cause stands `Taken:` or `Deferred:`, every cause of the top stands `Checked:` or
`Unchecked:`, a cause the check moved out of the top keeps its `Checked:`, a withdrawn cause stands
as a `Withdrawn:` item, every deferred `grave` cause has its answer, and every settled status put
back to the human has its answer. An audit that stopped for the other discipline's checks only that
its causes stand weighed.
