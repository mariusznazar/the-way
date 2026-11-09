# Findings to fix — Minor findings within the task of the review of the whole change

Cut word for word from reports/review-whole-report.md (first line PASS e3fcc2025fa436467400f3ba56711c60f47f9c91). No blocking finding. Fix range: from e3fcc20.

**M1 — WAY-61's *Rationale* restates the permission as a fact, in a sentence that misreads.**
Within the task (To do 1: the rationale must agree with the new sentence).
Place: `foundations/decisions.md:1497-1499`:
"A change is judged finished, so an invariant written before its test within one change reads `test`
from its writing, and a later slice that writes the test leaves the entry as it is."
What is wrong: (a) "A change is judged finished" reads as "a change is deemed finished", not "a change
is judged once it is finished"; (b) the binding sentence (`:1471-1472`) and the template
(`elements/invariants/template.md:59-61`) grant "may read `test`", while the rationale says the
invariant "reads `test`", which a reader in a borderline case — the agent who forgot the switch and
turns the method back to `review`, the direction WAY-321's rationale calls safe — can take as an
obligation. A smaller point of the same entry: *Rejected* keeps "`TODO` as the method until the test
exists — it names nothing that keeps the rule meanwhile" (`:1505-1506`), a reason that now also fits
`test` mid-change; it holds only across changes, which the entry leaves to the reader.
Why it matters: *Rationale* is what an agent reads in a borderline case (decisions template, "Fields
and their readers"). The binding sentence and the examples carry the right meaning, so this is
polish, not a wrong rule.
Suggested wording: "A change is judged as a whole, once finished, so an invariant written before its
test within one change may read `test` from its writing, and a later slice that writes the test
leaves the entry as it is."
Evidence: reading of the entry against its binding sentence and the template line.

**M2 — `test-method-citation` derives from WAY-321 only, while its sentence is WAY-61's rule.**
Within the task (row 3 of *Settlements to record*; the row leaves the derivation to the writer).
Place: `foundations/invariants.md:162` (`- **Derives from:** WAY-321`); WAY-61's *Verification*
`foundations/decisions.md:1482` names no invariant.
What is wrong: the invariant's sentence ("Every invariant whose method is `test` is cited by …") is the
checkable form of WAY-61's own violates example "an invariant reads `test` on the finished change
while no test cites it" (`foundations/decisions.md:1491-1492`); WAY-321 answers when the check
reports, not what the data must hold. The model the row names, `map-reference-target`
(`foundations/invariants.md:146-154`), derives from the decision of its data rule (WAY-41), not from
a decision about a check. `elements/invariants/template.md:122-124`: *Derives from* names every
decision the invariant derives from, "neither link is optional".
Why it matters: the writer of a later change to WAY-61 who follows its *Verification* finds no
invariant to revisit. The harm is small, because WAY-321 "derives from WAY-61" and the search of the
foundation (WAY-33) reaches the invariant through it. The author's reason — avoiding an edit of
WAY-61's *Verification* — is a cost, not a reason for the link to be absent, and does not lower the
grade.
Suggested fix: `- **Derives from:** WAY-61 · WAY-321`, and WAY-61's *Verification* opens with
`invariants: test-method-citation.` before the pair of examples (the template's form allows both).
Evidence: the passages cited above.

**M3 — one docstring line over the file's line width.**
Within the task (To do 3).
Place: `elements/common/foundation_check.py:499` — 101 characters; it is the only line of the file
over 100, and the neighbouring code keeps 100.
Why it matters: style only; no linter of the-way enforces it.
Evidence: a scratch measurement of the line lengths (no file changed).
