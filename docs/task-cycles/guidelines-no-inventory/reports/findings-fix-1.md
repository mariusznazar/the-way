# Findings for the fix — review of the whole change, `FAIL 6df733c`

In the reviewer's words (`reports/review-whole-report.md`). Blocking finding first, then the Minor
findings of the review within the task.

## Blocking

**I1. WAY-312 binds only the template and the skills not to rename or drop known-practice and derivable sentences, so the row's meaning narrows.**
- Place: `foundations/decisions.md`, the second binding sentence of WAY-312, and the "violates" list of its *Verification*.
- Row 1 and *To do* 1 say known-practice sentences and derivable cases are "not replaced by a name and not taken out". They state it impersonally, and *To do* 1 adds that the template guards new text and the product's task cleans existing guidelines.
- The decision's sentence 2 is: "The template and the skills of guidelines neither replace a sentence that names a practice a model knows with the name of the practice nor take out a case that follows from a rule's purpose." Its subject is only the template and the skills. The template and skills are not the actors who would do this. The actor is the product's own cleaning task (sentence 3), and agents editing guidelines.
- Sentence 3 says that task cleans "of the sentences the first sentence rules out". That implies only those sentences are removed, but it does not forbid renaming or dropping the other two groups.
- The "violates" examples name only "the template or a skill replaces the sentence on an empty list with 'fail loudly'". A product task that does exactly that is not a violation as written.
- Why it matters: the next task, which cleans `loop2`'s other 13 guideline files, reads this decision to learn what it may do. The decision does not stop that task from renaming a known practice or dropping a derivable case. That is the thing the row exists to prevent. WAY-263 grades a departure from an entry the change writes as Important when it restates the row differently.
- Evidence: compare `foundations/decisions.md` (the sentence quoted above) with *To do* 1 and row 1 of the frozen task.
- Suggested fix: make the subject general, so that nothing that edits a product's guidelines, a product's cleaning task included, replaces such a sentence with a name or takes such a case out. Add a "violates" example for a product's cleaning task that does so.

## Minor, within the task

**M1. The fact entry joins two facts that the template asks to keep separate.**
- Place: `foundations/environment_facts.md`, entry `shorter-guidelines-trial`, sentence.
- It says the 45 of 45 pass result, and also that "the report gives one model, Sonnet 5.5, for every stage of the cycle that ran the trial".
- `elements/environment-facts/template.md` ("The sentence") says two facts from one edition about different things stand as two entries (WAY-76).
- Mitigation: row 3 of the task carries "Sonnet 5.5" as the scope of the result, so I read it as a qualifier rather than a second fact. A fix is to state the model as the condition under which the 45 of 45 holds, and drop "for every stage of the cycle".

**M2. The figures in WAY-312 *Rejected* do not match the fact's cited source.**
- Place: `foundations/decisions.md`, *Rejected*, "about 2¼ hours and 119 million tokens".
- The source the decision rests on (§ Cost) says "2 h 44 min of agent time" and "95.2 million tokens".
- I found 119.4 million tokens only in `stages.md` of the same cycle record, which also gives 1:35:03 of working time. I found "2¼ hours" nowhere in the record.
- The figures are the task's (question 7, "Not chosen"), so the author carried them faithfully.
- A reader who opens the fact sees a different cost than the decision states. Either source the figures or align them.

**M3. The "once in twenty sets" statement in the Rationale is the author's arithmetic, and the fact does not quote its basis.**
- Place: WAY-312 *Rationale*, "a pass rate near 55% still gives five of five once in twenty sets".
- The request's wording is "as low as about 55% is still compatible with 5 of 5 (one-sided 95%)". The fact's *Source* quotes neither that passage nor the 55% figure.
- 0.55^5 is about 0.05, so the arithmetic is right. The Rationale does not mark it as a derivation, although the author's report says it is one.
- Likewise "the tests cannot see whether the file is followed" is a derivation from the source's "the tests cannot tell the three apart".

**M4. The template bullet generalizes WAY-274's exemption.**
- Place: `product-guidelines/template.md`, new bullet, last sentence: "A list that is the product's promise and no copy of its code is no such state (WAY-312, WAY-274)".
- WAY-274 and the task's Context speak only of the `### Logging scope` list. The bullet exempts any list that is the product's promise.
- The task's Context licenses an exemption for the logging-scope list. A reader could take the bullet as a wider licence than the task gave. Narrowing it to "the `### Logging scope` list" would match the source.
- Separately, the author's report says the examples "endpoints the code has today" and "version of a tool" come from the task. "Endpoints" is not in the task. It comes from WAY-225's "violates" line, which is valid. The report is wrong about the origin, not the text.

**M6. Two lines in WAY-312 are long and ragged.**
- Place: `foundations/decisions.md`, the Rationale line starting "the skills stay as they are. Its weak points: ..." and the *Rejected* line "refresh mode of coding guidelines has heavy prerequisites; a separate task for the template...".
- They run past the file's wrapping.
- This is polish only.

## Not in this file

M5 (the body of commit `cd9d5af` names the private repository) is not fixed here: fixing it rewrites
reviewed history, and the repository's name already stands, by approval, in the fact's *Source* line.
The orchestrator records it as an autonomous choice (Q2) and carries it to the request's list.
