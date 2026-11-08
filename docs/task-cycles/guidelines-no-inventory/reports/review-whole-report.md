FAIL 6df733c

Saved by the orchestrator from the reviewer's returned text (a subagent may not write report files).

Counts: 1 blocking (Important), 6 Minor (all within the task), 0 out of scope. Checks: all run checks passed. I did not run the full gate, which is the orchestrator's. The report cannot be saved as a file because subagents may not write one, so this reply is the report.

## Findings

### Important (blocking)

**I1. WAY-312 binds only the template and the skills not to rename or drop known-practice and derivable sentences, so the row's meaning narrows.**
- Place: `foundations/decisions.md`, the second binding sentence of WAY-312, and the "violates" list of its *Verification*.
- Row 1 and *To do* 1 say known-practice sentences and derivable cases are "not replaced by a name and not taken out". They state it impersonally, and *To do* 1 adds that the template guards new text and the product's task cleans existing guidelines.
- The decision's sentence 2 is: "The template and the skills of guidelines neither replace a sentence that names a practice a model knows with the name of the practice nor take out a case that follows from a rule's purpose." Its subject is only the template and the skills. The template and skills are not the actors who would do this. The actor is the product's own cleaning task (sentence 3), and agents editing guidelines.
- Sentence 3 says that task cleans "of the sentences the first sentence rules out". That implies only those sentences are removed, but it does not forbid renaming or dropping the other two groups.
- The "violates" examples name only "the template or a skill replaces the sentence on an empty list with 'fail loudly'". A product task that does exactly that is not a violation as written.
- Why it matters: the next task, which cleans `loop2`'s other 13 guideline files, reads this decision to learn what it may do. The decision does not stop that task from renaming a known practice or dropping a derivable case. That is the thing the row exists to prevent. WAY-263 grades a departure from an entry the change writes as Important when it restates the row differently.
- Evidence: compare `foundations/decisions.md` (the sentence quoted above) with *To do* 1 and row 1 of the frozen task.
- Suggested fix: make the subject general, so that nothing that edits a product's guidelines, a product's cleaning task included, replaces such a sentence with a name or takes such a case out. Add a "violates" example for a product's cleaning task that does so.

### Minor (all within the task)

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

**M5. Commit `cd9d5af`'s body names the private repository.**
- Place: `git log deded3f..6df733c`, body of `cd9d5af`: "The environment fact of the trial on loop2 waits for its source."
- The handoff asked whether the name appears anywhere but the fact's *Source* line. In tracked files it does not: `git grep -i loop2 -- . ':!.runs'` hits only `foundations/environment_facts.md:208`. It does appear in this commit message, and the message is also stale now.
- Fixing it needs a reword, which is the orchestrator's decision.

**M6. Two lines in WAY-312 are long and ragged.**
- Place: `foundations/decisions.md`, the Rationale line starting "the skills stay as they are. Its weak points: ..." and the *Rejected* line "refresh mode of coding guidelines has heavy prerequisites; a separate task for the template...".
- They run past the file's wrapping.
- This is polish only.

## Coverage of the task

- **To do 1 / row 1:** WAY-312 is present and `foundation_check` is clean. The meaning is met except for I1.
- **To do 2 / row 2:** the bullet "A rule lists no state and repeats no decision or value" is in `product-guidelines/template.md` "Required form". WAY-312 says the product's own task cleans existing guidelines and the skills get no search step, which matches the "Not chosen" of question 5.
- **Row 3:** the environment fact `shorter-guidelines-trial` is written, and WAY-312 *Based on* names it (changed from `none` in `6df733c`). Both quoted passages are word for word in the source, markup dropped.
- **WAY-312 *Rejected*:** it holds only the "Not chosen" ways of questions 5 and 7, with their costs (WAY-134). I found nothing derived by the author.
- **Consistency with the decisions in play:** I found no contradiction with WAY-130, 168, 169, 171, 172, 173, 213, 100, 271–276, 225 or 274.
- **Foundation search:** the author's search was reasonable. The coding, testing and styleguide templates ("copy no value", the `### Logging scope` text, "never copies the list of components") stay consistent with the bullet. No other entry names the new fact. No invariant has *Part* `product-guidelines`.
- **Part map:** `product-guidelines` covers the template and the skills (Files `product-guidelines/**`), so *Scope* `product-guidelines` is correct.
- **Own-work check:** the author found and fixed the unsupported Rationale claims in `6df733c`. What remains is M3.

## Checks run

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `6df733c07e2b8ed2e3a46924ec164a5716376deb`, matches the head given |
| `git diff deded3f..6df733c` and `git log deded3f..6df733c` | read whole: 3 files, +65, no removals |
| `python -B elements/common/foundation_check.py` in the worktree | exit 0 ("0 errors") |
| Python check of the two quoted passages against `git -C the local clone of the game repository show 9c0dfc8faa7b3024dfa1e488b18b955f087b57a0:docs/task-cycles/proba-krotszych-wytycznych/request.md`, with `**` dropped | both occur word for word; headings "What you will see" and "Cost" exist |
| `git grep -i loop2 -- . ':!.runs'` and `git grep -i "mariusznazar/loop2"` | one hit only: `foundations/environment_facts.md:208` (the *Source* line) |
| `git log deded3f..6df733c --format=%B` | "loop2" appears in the `cd9d5af` body (M5) |
| `git grep` in the record at `9c0dfc8` for 119 and 2¼ | 119,365,163 tokens in `stages.md`; no "2¼" anywhere |
| `git status --short` | clean, no change made |

**Not run:**
- The full gate, which is the orchestrator's.
- `private_paths_check.py`, which takes a cycle record or a request description. The changed files hold no absolute path or note link on a read.
- A check that the GitHub address opens. The repository is private and I did not fetch it.

## Declined to judge

- Whether publishing the private repository's address in the *Source* line is acceptable. The orchestrator approved it, and the author raised it as a concern.
- Whether the shape of the fact (a cycle's request in a private repository) satisfies "an edition with its publisher's own address". The template does not cover this case, and the orchestrator settled it.
- The pin. It did not move.

## Reaches beyond the dispatch

- `elements/decisions/template.md` and `elements/environment-facts/template.md`, to judge the form of WAY-312 and of the fact.
- WAY-225, WAY-274 and WAY-168 in `foundations/decisions.md`, to check the bullet's examples and exemption.
- `foundations/part_map.md`, section `product-guidelines`, to check *Scope*.
- `product-guidelines/coding/template.md` lines 150–165 and 278–295, and the testing and styleguide templates by grep, to look for contradictions with the new bullet.
- `stages.md` and `request.md` of the `loop2` record at `9c0dfc8`, read only, to trace the cost figures.

## Searches not found or unclear

- I found no source for "about 2¼ hours" in the `loop2` record at `9c0dfc8` (M2). The 119 million figure is in `stages.md`; the cited request says 95.2 million.
- Whether the bare-`git` view of `elements/environment-facts/template.md` treats a private-repository blob at a full SHA as "an edition with its publisher's own address" is unclear. The template is silent, so I treated it as the orchestrator's settled choice.
