# Findings of the review of the whole change, to fix

Review: `FAIL 9b44856c6b8bda6ea17f22808e3332694b026601`, range `294af7f..9b44856`. Cut from the
reviewer's report `reports/review_whole_report.md` in the reviewer's words. One blocking finding,
then the Minor findings of the review within the task (WAY-161).

## Blocking

### Important (blocking; all inside the task)

**I1. WAY-25 *Rejected* says more than the human settled about the singular "the passage".**
Place: `foundations/decisions.md`, WAY-25 *Rejected*, last item (around line 681-683): "one passage of
what the human accepted in the singular - an outcome can come only from two passages read together,
and an agent reading the wording literally would stop where the outcome is given."
Source: task *Questions to settle* 3, third "Not chosen": "cytat jednego fragmentu ('the passage') - w
przypadku `logging-guidelines` wynik daje dopiero połączenie dwóch fragmentów, więc agent czytający
dosłownie stanąłby tam, gdzie zaczęła się sprawa". The source says that in one case the outcome came
only from the combination of two passages. The entry says, as a general statement, that an outcome
"can come only from two passages read together". Read plainly that is a universal ("only two
passages give an outcome"), which is false and contradicts the entry's own *Verification* (*complies*:
"in one passage or in two read together"). WAY-263 grades a changed entry that restates the human's
settlement more broadly or without its qualification as Important; the handoff asks that no wording
say more than was settled.
Why it matters: *Rejected* is what a later reader takes as the reason a way was dropped; this one
gives a reason that is false in general and mismatches the Verification a few lines above it.
Evidence: the two texts above, side by side. Fix: say what the source says, e.g. "an outcome can come
from two passages read together, and an agent reading the wording literally would stop where the
outcome is given".

## Minor findings of the review of the whole change, inside the task

**M1. "often" in WAY-25 *Rejected*.** `foundations/decisions.md`, WAY-25 *Rejected*, item "an exception
only for a settlement that says which decision prevails - the outcome often follows from settlements
that do not say so". Source (Q1, first "Not chosen"): the wording "did not even cover the case that
started it" (one case). "Often" is a frequency the source does not give. The author reported the
rewording as a choice; the reason itself is faithful, the frequency is not. Fix: "the outcome can follow
from settlements that do not say so".

**M2. WAY-293 *Rationale* now states WAY-25 without the qualifier.** `foundations/decisions.md`,
WAY-293 rationale (line about "the agent that meets the collision may not settle it (WAY-25)").
WAY-25 now says "never settled silently" and allows recording where the accepted task document gives
the outcome. The author judged that WAY-293's case (task or spec exclusion; a spec is not accepted by
the human, WAY-135) still stops the agent. That holds for a spec, but a task document that itself
excludes an entry is a collision of exactly the kind WAY-25 now lets the cycle record. Unqualified,
the clause reads wider than WAY-25. Found by the search of WAY-33 the task asks for; a one-word
correction ("settle it silently") or an explicit note would close it. Checked also WAY-26, WAY-32,
WAY-172, WAY-268: they say why precedence is recorded or that without it the agent has nothing to
choose between; not contradicted.

**M3. `task-cycle/skill/request_template.md:194-196` takes the quoted passages "from the foundation
step's report" only.** The same item 6 takes entries from "the foundation step's and return step's
reports"; the return step "writes as this step writes" (`foundation_step.md`, header) and can record a
precedence too, keeping the passages in its own report. The wording leaves the return step's case
without a named source. Fix: "from the report of the step that wrote it".
