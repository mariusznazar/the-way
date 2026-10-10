# Independent assessment of 7335b5f..d0f6e5b (WAY-137 to WAY-140, WAY-124 edited)

Material read: the diff `change.diff`; in the assessed tree, `foundations/decisions.md` (the new
entries, the edited WAY-124, and WAY-04, 05, 07, 13, 14, 24, 25, 30, 31, 32, 36, 48, 95, 100, 107,
113, 120, 121, 122, 123, 125, 126, 134, 135, 136), `elements/decisions/template.md`,
`elements/decisions/skill/SKILL.md`, `elements/decisions/examples.md`, `elements/common/rules.md`,
`elements/common/way_of_working.md`, `elements/common/critique/SKILL.md`, `foundations/glossary.md`,
`foundations/part_map.md`, `project-level/definition_template.md`,
`project-level/technology/SKILL.md`, `project-level/task/template.md`,
`project-level/task/skill/SKILL.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`.
No `.runs/`, no other checkout, no git history.

Automated checks run on the tree (they establish form, not fidelity):

- `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none --today 2026-10-10`:
  0 errors, 10 warnings, 5 unchecked. The warnings are the five `<request link>` placeholders
  (expected before the request exists) and five overdue check-by dates on WAY-03, 21, 52, 55, 69,
  which this change does not touch.
- Fingerprints computed from the binding parts in the tree with `relation-model/fingerprint.py`:
  WAY-100 e7a74a18, WAY-122 b343277a, WAY-123 f3b45293, WAY-125 441e3a6a, WAY-140 d02ede05,
  WAY-106 63eddf70, WAY-118 5af868b3, WAY-126 35accf8b, WAY-134 b858b34f — every fingerprint the
  new or edited *Relations* carry matches. No entry anywhere carries `WAY-124@`, so the changed
  binding part of WAY-124 leaves no stale relation (WAY-31).

Line numbers below are those of the assessed tree.

## Observations

### A. Source fidelity, settlement by settlement

**1. Settlement 1 → WAY-137 (`foundations/decisions.md:4090-4128`). No concern on meaning.**
Checked each clause of the Polish settlement against the binding sentences (4092-4097): tie-break
only after WAY-123's "simplest and cheapest" leaves more than one option — present; the three
marks of agent-friendliness (terminal, scripted deployment, agent-readable documentation) —
present; "not a filter nor a weight" — present as "leaves no option out of the comparison and is
weighed against no consequence"; "stays although it will seldom act, because it keeps the property
from entering higher" — in *Rationale* 4120-4122, which is the right home for a motive. WAY-123's
own text is unchanged, as the settlement required. Nothing lost, nothing added to the binding part.

**2. Settlement 2 → WAY-138 (`foundations/decisions.md:4130-4178`). Meaning kept; one derived
clause added that the settlement implies but does not say.**
Every clause of the settlement maps: tests on the recommended option (4133), only choices this
project settles, constraints included (4133-4134), no test of choices held by existing decisions
and no retro-fit (4134-4135), risks shown before the choice in the table beside the recommended
option (4137), accepted risks reach the decision by the same channel as the chosen option's lacks,
marked as hypotheses (4138-4139), and the review condition narrowing the scope to the place to run
(*Review when* 4156-4157, outcome foretold in *Rationale* 4171-4172).
The added clause: "The risks these tests give are hypotheses with no source, not differences
claimed between options, so the critique of the comparison does not strike them" (4136-4137). The
settlement says only "oznaczone jako hipotezy". The clause is needed to reconcile WAY-138 with
WAY-122's rule that the critique refutes every claimed difference no source supports
(`decisions.md:3454-3455`), and it is sound, but it is the author's inference. What would change:
nothing in the text; the human should be told, at the merge, that this clause is the author's
reconciliation with WAY-122 rather than a thing settled.

**3. Settlement 2, the channel of the lacks.** The settlement says the risks go "kanałem braków
wybranej opcji" — by whatever channel the lacks take. Before this change no entry or skill named
that channel: WAY-122 says only "which the decision records if the human chooses it"
(`decisions.md:3451-3452`), and `technology/SKILL.md` step 7 listed "the lacks of a chosen option"
with no field. The change fixes the channel as *Rationale* — in WAY-138's binding sentence
(4138-4139), in `definition_template.md:216`, in `technology/SKILL.md:134-135` and in
`elements/decisions/skill/SKILL.md:77-79`. Fixing it was unavoidable to make the settlement
executable, and *Rationale* is a defensible choice (a risk is a motive weighed, not a fact with a
source; *Based on* names facts, WAY-90). Two consequences a reader should see:
(a) the decision template's rule that author-written *Rationale* "names no file, script or count"
(`elements/decisions/template.md:51-54`, WAY-05) now applies to every risk and lack written there —
a risk like "the free tier ends at N requests" cannot carry its number. WAY-138's own examples in
*Rationale* (4162-4165) avoid counts, but nothing warns the writer of a product's decision. What
would change: one clause in the record-decision skill line (`elements/decisions/skill/SKILL.md:77-79`)
or in the template saying a risk is written without the count or the file it would otherwise name;
or a decision that the rule does not bind quoted risks.
(b) `elements/decisions/skill/SKILL.md:77-79` cites "(WAY-122, WAY-138)" for "the lacks … stand
in *Rationale*". WAY-122 does not say where the lacks stand; only WAY-138 does, in passing. The
citation to WAY-122 is for the lacks' existence, not their home — acceptable, but a reader looking
for the rule's source will find it only in WAY-138.

**4. Settlement 3 → WAY-139 (`foundations/decisions.md:4180-4217`). Two phrases of the list carry a
translation the Polish does not fix.**
The structure of the settlement is kept: the-way holds no product skill, only the list; the list
stands in the binding sentence (verification 4202-4203 forbids moving it to a template); the check
runs while `refine-task` refines a task whose outcome deploys the product or changes how or where
it runs; the remedy is a To do item or a split by the human. Two items of the list, however, were
translated one way where the Polish allows two:
- "podgląd wdrożeń" → "a preview of deployments" (4183). In English "preview" reads as a preview
  environment or a dry run before deploying; the Polish reads at least as naturally as "a view of
  the deployments" — what is deployed where, and in what state. These are different things a
  deployment skill has to cover.
- "cofanie (ile kroków, co z danymi)" → "rollback, with how many steps it takes and what happens to
  the data" (4183-4184). "Ile kroków" can mean how many steps back a rollback can go (how many
  earlier versions remain restorable) rather than how many steps the procedure takes.
What would change: the human confirms the intended reading of each; the binding sentence, the
template copy in `project-level/task/skill/SKILL.md:80-84` (which points to the list rather than
copying it, so only the entry changes) follow.

**5. Settlement 4 and 5 → WAY-140 (`foundations/decisions.md:4219-4263`). Meaning kept; examples
in the binding sentences are the author's.**
Checked: effect outside the repository on a server, DNS, keys or an external account is a human
action (4221-4222); named and placed by the task document before the cycle or in it (4222-4223);
before-the-cycle actions done before readiness (4224); in-cycle actions: the cycle does what the
repository allows and opens a blocked draft request listing them, the human performs them at the
request (4225-4226); reads outside the repository stay with the agent (4223); the human places
each action at refinement on the agent's proposal, with the two placement rules of settlement 5
(4226-4229). All present; nothing of the two settlements is lost.
Added: the illustrations "such as an account, a key or a database" and "such as a deployment or a
DNS record pointing to a new address" (4228-4229) are the author's, not the settlement's. They are
examples inside binding sentences, so an agent reads them as binding cases. They look right; the
human should know they were not settled.

### B. Collisions with current decisions

**6. WAY-140 against WAY-107 and the backlog write: an exception lives only in the skill.**
WAY-140's first binding sentence makes every effect on an external account a human action. The
task cycle writes the request link and the task's state into the product's backlog entry
(`task-cycle/skill/SKILL.md:52-54`, WAY-107), and a backlog may be an external tracker — an
external account. The skill resolves this with a parenthetical of its own: "the cycle's own
record and not an effect of the task (WAY-140)" (`task-cycle/skill/SKILL.md:52`). WAY-140 says
nothing of it. The decision template requires an exception foreseen in advance to stand in the
binding sentences (`elements/decisions/template.md:101-102`, WAY-30: "no exception lives only in a
task's plan"), and a skill is not the decision. What would change: either a clause in WAY-140's
binding sentences naming the backlog write of WAY-107 as outside "a task's effect", or the
parenthetical removed from the skill and the collision left for the human to record (WAY-25).

**7. WAY-140 against WAY-13 and WAY-125. No concern.** WAY-13 ("a human decides on every change
that cannot be undone", `decisions.md:411-412`) and WAY-125 ("when required code cannot proceed
without one, the cycle opens a blocked draft request", 3593-3595) both pull the same way as WAY-140;
the skill's older clause that let the cycle execute an external side effect unless the product
reserved it (`change.diff:478-480`, removed) was the one text that would have collided, and the
diff removes it. WAY-140 `derives from WAY-125` is the right relation; no `narrows` is needed.

**8. WAY-137 against WAY-123: `narrows` is the right type. No concern.** WAY-123's binding part
says "a difference with no consequence for the product decides nothing" (`decisions.md:3503-3504`);
WAY-137 lets such a difference decide a recommendation in one narrow case, so it deliberately
goes against WAY-123 there (WAY-32, `decisions.md:912-913`), and WAY-123 itself stays unchanged,
as the settlement required. WAY-138 against WAY-120 ("two critics are run on one change" is a
violation, 3390-3391): the technology step now runs, per wave, one agent for the tests and one
critic of the whole table (`technology/SKILL.md:107-117`); the test agent is not a critic, so no
collision. WAY-138 against WAY-113: a recommended option taken as offered still passes without a
question, with the risks now beside it — consistent (`technology/SKILL.md:122-125`).

**9. WAY-139's rationale against WAY-140's example.** WAY-139 *Rationale* says "a skill of the
product reaches the agent when it deploys" (`decisions.md:4212`). WAY-140's binding sentence
gives "a deployment" as the example of an action in the cycle that the human performs (4229).
Under WAY-140 the agent writes and prepares the deployment; the human performs it. The sentence
is prose and binds nothing, but it states a premise WAY-140 denies. What would change: "when the
product is deployed" or "when it prepares a deployment" in 4212.

**10. WAY-04 and WAY-24. No concern.** WAY-138 rejects "an entry of its own for each risk" by
WAY-04's refusal of assumptions as a kind of entry (`decisions.md:4176-4177`, against 132-133),
which is a correct reading. WAY-138's *Review when* names an observable state (the tests on
choices other than a place to run give no new risk) and a date; under WAY-24 that is the right
form, and the foretold outcome in *Rationale* (4171-4172) does not pre-empt the review record.
The check-by date 2026-12-31 is the author's, since the settlement names none; the template
requires one, so it had to be set, and the human accepts it at the merge.

### C. Form of the entries

**11. One rule in two homes: readiness and before-the-cycle actions.** WAY-124's new clause
"every human action it places before the cycle is done (WAY-140)" (`decisions.md:3545-3546`) and
WAY-140's second binding sentence "An action placed before the cycle is done before the task is
ready (WAY-124)" (4224) state the same rule, in two binding parts. WAY-124 answers "When is a task
ready?", so the rule is its; WAY-140 need only say that an action is placed before the cycle or in
it and what the cycle does with each placement. What would change: cut the readiness clause from
WAY-140's binding part (keep the cross-reference, if at all, in *Rationale*), or accept the
duplication knowingly. Note that cutting it changes WAY-140's fingerprint, which WAY-124's
*Relations* carry (3557): both move together (WAY-31).

**12. A rule that forces later work stands only in prose.** WAY-140 *Rationale*: "checking the
code after the action falls to the round of corrections after it" (`decisions.md:4254-4255`).
This says what happens after the human performs an in-cycle action — a correction round — and
nothing in the binding sentences or the skill says it: `task-cycle/skill/SKILL.md` "Correction after
review" (290-300) takes "a link to the request, or to a comment holding review remarks" as input,
not a performed action, and step 12 (266-268) only keeps the request a draft. The settlement itself
stops at "człowiek wykonuje je przy PR-ze"; what unblocks the request afterwards is a gap in the
source. WAY-05 puts what a decision forces on later work in a binding sentence or a field, never in
prose (`template.md:53-54`). What would change: either a binding clause (and a line in the skill)
saying how the request leaves `blocked` once the actions are done, or the sentence removed from
*Rationale* and the question named as open for the human.

**13. "Human action" is a glossary candidate (WAY-95).** The phrase now stands in the binding
parts of WAY-124 (3545) and WAY-140 (4222, "as an action") and as a section name of the task
template, meaning one thing: an effect outside the product's repository that a human performs,
named and placed in the task document. A reader of the field reads "human action" as any act of a
person — approving a request, answering a question, cutting the candidate rows — and WAY-124's
sentence sits beside exactly such acts ("the human has accepted or rejected every candidate
settlement"). That is a meaning the field would not give, so WAY-95 asks for an entry; the glossary
(`foundations/glossary.md`) has none. "Placement" of an action and "effect outside the repository"
read as the field reads them and need none. What would change: a glossary entry for "human action"
in the same change, through `record-glossary-term`, and WAY-124/WAY-140 using the term as defined.

**14. Two marks for one thing in WAY-138.** The binding sentence says a risk taken reaches the
decision "marked as a hypothesis" (4139); the complies example says the table shows risks "each
marked as having no source" (4148); the skill says "each marked as a hypothesis with no source"
(`technology/SKILL.md:120`). Neither the entry nor any template says what the mark looks like in a
table or in *Rationale*. A product's agent will invent one. What would change: one wording across
the three places, and the form of the mark given once where the field's rules stand (the decision
template for *Rationale*, the definition template for the table).

**15. A rule of the entry's form placed in a skill rather than the template (WAY-35).** Where risks
and lacks stand in a projected technology decision is a rule of what *Rationale* holds; it was put
in `elements/decisions/skill/SKILL.md:77-79` under "Projected mode". `way_of_working.md:3-6` and
the template's own preamble (`template.md:9-11`) say a rule of an entry stands in the template, the
skill holding only the way of working. What would change: the sentence moves to
`elements/decisions/template.md` beside the *Rationale* rule (51-54), cited to WAY-138; the skill
may keep a pointer.

**16. Scope of WAY-139.** *Scope* reads `project-level` (4191). The first binding sentence,
"The-way holds no skill of a product", binds the whole repository, and the violating example
"the-way carries a deployment skill for one kind of host" (4200) would be a change to no part
named here. The second sentence binds `project-level` correctly. Minor: a reader of
`decisions-found-for-change` will not find WAY-139 when such a skill is added elsewhere. What
would change: nothing, if the human is content that the check in `refine-task` is the whole
enforcement; otherwise the parts where such a skill could be added.

**17. WAY-124's edit. No concern.** The binding part changed, so *Approved by* returning to
`merge of <request link>` (3571) is what WAY-07 and WAY-14 require; the new derives-from
WAY-140@d02ede05 (3557) matches; the new complies and violates examples (3561-3563, 3567-3568)
match the new clause; *Rationale* gained one sentence of motive (3576-3578) and no rule.

**18. Relations and fields of the four new entries otherwise. No concern.** Each has every
field; *Change* `new decision`; *Scope* names parts of the map; *Based on* `none` (no fact is
cited; the risks are explicitly not facts); *Origin* `none` with the reasoning in the entry;
*Rejected* names options and the reason for each; the binding parts stay within three sentences
and use no forbidden word. WAY-137 and WAY-138 `derive from WAY-100` as borrowed practices, and
each names what is adopted, where it applies and why, which is all WAY-100 asks.

### D. Fidelity of skill and template text to the entries

**19. The task cycle adds a rule the entries do not state: effects found during the cycle.**
`task-cycle/skill/SKILL.md:75-78`: "An effect outside the repository that the cycle finds and the
task document does not name joins that list, for the human to place; where the task document places
no action in the cycle, the request opens as a blocked draft listing that effect." Mirrored in
`task-cycle/record_template.md:101-102` and step 13 (282-284). WAY-140 says the human places each
action "while the task is refined" (4226-4227) and says nothing of an effect the refinement missed.
The skill's rule is the sensible gap-fill — it keeps the agent from making the effect and from
placing it alone — but it decides an outcome (the request is blocked) the entry does not. What
would change: a clause in WAY-140's binding sentences for an effect found in the cycle, or the
human settling that the skill's order of work may hold it.

**20. The technology skill adds "give that as the reason" (WAY-137).** `technology/SKILL.md:107`
and the complies example at `decisions.md:4106` require the agent-friendliness tie-break to be
stated as the reason of the recommendation. WAY-137's binding sentences do not say it; WAY-123
asks for the recommendation and the weak point, not the reason. Small, and it serves the human
who should see when the tie-break acted; but the rule stands in a verification example and a skill,
not in a binding sentence. What would change: add it to the binding sentence, or drop it from both.

**21. The technology skill adds a retest rule (WAY-138).** `technology/SKILL.md:129-131`: a
choice left unanswered goes into the next table with its risks, "and is not tested again unless
that option changes, when the new one is tested". The entry says tests run on the option
recommended and never on a decision already written; it does not say what happens to an
unanswered choice's risks. The skill's rule follows the entry's spirit and is order of work, which
the skill holds (`technology/SKILL.md:16`). No change needed; named so the author knows it is the
skill's, not the entry's.

**22. The definition template copies the binding sentences of WAY-137 and WAY-138 verbatim.**
`definition_template.md:203-217` repeats 4092-4097 and 4132-4139 word for word. This is the house
style of that template (every bullet of the Technology section restates its decision with the
number), so it is not an error, but it is the same rule in two homes, and an edit to either entry
before the merge has to be carried to the template by hand. No change proposed; the author should
check the two copies once more if any observation above changes a binding sentence.

**23. The task template's form line for the Human actions section.** `project-level/task/template.md:47`
gives one line: `- <action outside the repository, or none> — before the cycle, <done|not done> |
in the cycle | TODO`, while the rule (102-103) and the refine-task check
(`project-level/task/skill/SKILL.md:122`) speak of the section "reading `none`". A writer cannot
tell whether `none` stands alone under the heading or as a bullet with a placement. Minor. What
would change: the form shows the two shapes, a list of actions or the word `none`.

**24. Other skill and template text. No concern.** `task-cycle/skill/SKILL.md:27-28` (require
before-the-cycle actions done), 49-50 (reads stay with the agent), 73-75 (in-cycle actions →
blocked draft), 266-268 (such a request stays a draft), 281-284 (the list in the request);
`project-level/task/skill/SKILL.md:75-79` (name, propose, have the human place, `waiting for human`
until done) and 80-84 (the WAY-139 check, pointing to the list rather than copying it); 119-127
(readiness check extended); `project-level/task/template.md:93-104`; `technology/SKILL.md:13-14`
and steps 5–7 — each states what its entry states, with the entry's number, and no second
statement of a fact beyond those named in 11, 19, 20 and 22.

## Proposed cuts

1. **Cut from WAY-140's binding part** the sentence "An action placed before the cycle is done
   before the task is ready (WAY-124)" (`decisions.md:4224`) — WAY-124 now carries the rule
   (observation 11). WAY-124's relation fingerprint moves with it.
2. **Cut the opening restatement in the task cycle** (`task-cycle/skill/SKILL.md:21-23`, "A human
   action the task document places in the cycle does not stop the cycle midway either …"): step 4
   (73-75) and step 13 (281-284) say the same, with the number; three statements of one rule in one
   file. Keep the one in step 4.
3. **Cut "nor a decision already written"** from `technology/SKILL.md:111-112`: at step 5 the only
   decisions already written are projected ones of earlier waves, whose options were tested in
   their wave; the clause repeats the `held by` rule in words that could be read as covering every
   projected decision of the definition. Keep it in the entry, where it carries the "no retro-fit"
   meaning of the settlement.
4. **Cut the sentence from WAY-140's *Rationale*** "checking the code after the action falls to the
   round of corrections after it" (`decisions.md:4254-4255`) unless it becomes a binding clause
   (observation 12); as prose it binds nothing and misleads a reader into thinking the unblocking
   is settled.
5. **Cut "give that as the reason"** from `technology/SKILL.md:107` and "with that given as the
   reason" from `decisions.md:4106`, or raise the rule into WAY-137's binding sentences
   (observation 20). The complies example should not carry a rule the sentences do not.

Not cut, although considered: the verbatim copies in `definition_template.md:203-217`
(observation 22 — house style); the record template's new line (`record_template.md:101-102`),
which the request handoff reads; the refine-task check for WAY-139, which is the only enforcement
the entry has; the placement examples in WAY-140's binding sentences (observation 5), which the
human may want as binding cases.

Everything else in the change I would keep as it stands.
