# Findings of the second review of the whole change (`reports/review-whole-2-report.md`, head 42298f2a)

Cut from the reviewer's report in its words: the blocking finding, then the two Minor findings within the task.

## Blocking

**I1 — The new rule "where no way reaches the goal, the question recommends none" collides with
WAY-166, and the technology step that rests on a recommendation for every choice, with no precedence
recorded (WAY-25).**

Place: `foundations/decisions.md:1595-1597` (WAY-113, new third paragraph: "A way that gives less
stands among the ways [...] and is never recommended; where no way reaches the goal, the question
recommends none and says so") and its copy `elements/common/way_of_working.md:36-38`; against
`foundations/decisions.md:4847-4849` (WAY-166 binding: "Where no option can be used by an agent, the
recommendation goes by the other consequences and says in one sentence that no option lets an agent
check the running product this way"), `:4864-4866` (WAY-166 *violates*: "on a host where no option
can be used by an agent, the step recommends nothing"), `:4873-4875` (WAY-166 *Rationale*: "the human
is owed a recommendation (WAY-113)"), `:4886-4888` (WAY-166 *Rejected*: "the step recommending nothing
where no option can be used by an agent — an exception to WAY-113, and the human answers with no
hint"), and the copies of WAY-166 in `project-level/technology/settle.md:34-38` and
`project-level/definition_template.md:242-248`.

What is wrong: the human chose that the rule covers every goal the material sets (task, question 1:
"każdy cel, który materiał stawia pracy") — a task's need included. The step that settles technology
also runs at a task document (WAY-267), and a task's need can itself be that an agent checks the
running product, for example that an agent reads the product's logs (the deployment skill's item on
how to read the logs, WAY-139, sends such work to a task). In that run, where every option of the
logs is a panel only the human can read, WAY-166 and `settle.md` tell the agent to recommend by cost
and upkeep, and the new paragraph of WAY-113 tells it to recommend none, which WAY-166 names as its
own violation and its *Rejected* refuses by name as "an exception to WAY-113". Both decisions apply,
they pull opposite ways, and neither names the other `narrows` (WAY-113 *Relations*: none; WAY-166:
`derives from WAY-121 · narrows WAY-123`). WAY-166's *Rationale* also still says that WAY-113 owes the
human a recommendation, which the changed WAY-113 no longer says in this case.

The same new case reaches the rest of the technology step, which presumes a recommendation for every
choice: WAY-123 (`foundations/decisions.md:4171`, "each choice with its recommendation and the weak
point of the option recommended"), WAY-138 (index line: "tests the option it recommends for each
choice it settles"), `settle.md:39-41` (the risk tests run on "the option recommended for every
choice of the wave") and `settle.md:61-62` ("A human who answers "you choose" or "I do not know" takes
the recommendation"). Where no option of a choice reaches the definition's goal or measure of
success, or the task's need, the step's agent now has no recommendation to test and no answer for
"you choose", and no file says what it does instead. WAY-123 derives from WAY-113, so it may be read
under the new paragraph, but `settle.md` gives the agent no step for that case.

Why it matters: WAY-25 — "A collision between two decisions with no precedence recorded is never
settled silently by the agent that meets it"; the change must either record the precedence where what
the human accepted gives the outcome, or stop and ask. Merged as it stands, the head leaves every
agent of the technology step that meets this case with two binding decisions saying opposite things,
and each agent settles it its own way, which is the "case left unsaid" WAY-166's *Rejected* itself
refuses. WAY-33 requires each finding of the search to become a link, a change or a question before
the change is accepted; the author's first report judged "no collision", and the fix report asked
the human (author-fix-1-report.md, "I1 — not settled") but the head records nothing.

Evidence: the lines quoted above, read at head `42298f2a`; `grep -n "WAY-113" foundations/decisions.md`
finds the citation in WAY-166 at `:4875` and `:4887`.

Whether what the human accepted gives the outcome: the task's answers 1 and 2, read together
("każdy cel, który materiał stawia pracy"; "nigdy jako polecany"; not chosen: "polecany, gdy jego
słaby punkt mówi wprost, że schodzi poniżej celu"), point toward the goal rule prevailing where the
need is the agent's check, since WAY-166's one sentence "no option lets an agent check the running
product this way" beside a recommended option is exactly a way below the goal recommended with its
lack named. But WAY-166's *Rejected* refusing this very move was accepted by the human too, and no
passage of the task names WAY-166, the technology step or a goal that is an agent's check. I agree
with the author that the outcome is not given (WAY-25: "otherwise the agent stops and asks"), so the
fix needs the human's answer. My recommendation for that question, which differs from the author's
recommendation (a): the goal rule prevails only where the material's goal or need is itself that an
agent checks the running product, recorded as WAY-25 gives in the decision that prevails — WAY-113
names `narrows WAY-166` and its binding sentences state that area — with the copies in `settle.md`
and `definition_template.md` carrying the same area, and `settle.md` saying what the step does with a
choice that has no recommendation (the risk tests and "you choose"). Outside that area WAY-166 stays
as it is, since where the material sets no such goal no option falls below it. Weak point: it
overrides an approved refusal in WAY-166's *Rejected* ("the human answers with no hint") and costs
edits in four places (WAY-113, `settle.md` twice over, `definition_template.md`); the author's (a)
costs one relation, but in that one area it recommends a way below the goal with its lack named,
which is the way the human refused in question 2.

Contradiction: yes — WAY-166 (binding sentence, *Verification* "violates", *Rejected*), with no
precedence recorded under WAY-25.

## Minor (within the task)

**M1 — `elements/common/critique/prepare.md:8-10`, within the task.** The added sentence leaves the
paragraph ragged: line 10 ("`elements/common/way_of_working.md`. Ask it to read the target in full")
is 70 characters between lines of 87–99. The fix re-wrapped the lines the change added in
`foundations/decisions.md` but not here. Polish only; the paragraph reads correctly.

**M2 — `foundations/decisions.md:1597-1600` and `elements/common/way_of_working.md:38-41`, within the
task, mandated by its *To do* 2.** The places where a goal held not worth its cost is settled name
"the goal of an independent task with the human in the same refinement". An agent that asks a
question of decision inside a task's cycle (for example in the foundation step, or an item of
*Needed from you* of a blocked request) has no refinement under way; the rule does not say that
there the question goes to the human through the cycle's own route (WAY-30, a blocked draft request).
The wording is the task's own ("cel zadania niezależnego u człowieka w tym samym doprecyzowaniu"), so
this is a gap the task mandates, named as such; the consequence is small, since WAY-30 and WAY-315
already stop a cycle that would change what the task settles.
