# Correction 1 author report — review-structure-form-class

**Status:** done. One commit on `24cbe61`: `c04d9cc`.

## The remarks

- **Remark 1: made.** Where a product has no rule of size — it departed from the rule by a decision, or has no coding guidelines at all, as the-way itself
  under WAY-328 — a finding about the structure of code is always Minor.
  - `task-cycle/review/SKILL.md`, section 3: "A finding about the structure of code that lies below the threshold of the rule of size in the product's coding
    guidelines is Minor, and so is every such finding where the product has no rule of size — it departed from the rule by a decision, or it has no coding
    guidelines at all — and you judge its scope as for any finding; a finding about a function or a file over a threshold is graded as any other finding (WAY-363)."
  - WAY-363, edited in place (WAY-07; the entry is this branch's own): the binding sentence now reads "…and one in a product that has no rule of size — it
    departed from the rule by a decision, or has no coding guidelines at all — and judges its scope as for any finding (WAY-161). A finding about a function
    or a file over a threshold is graded as any other finding." Its other sentence and fields stay (*Relations* `narrows WAY-161`, *Scope*).
    *Verification*: *complies* gains a script of this repository with no coding guidelines (WAY-328) and a product that departed, both Minor; *violates* gains
    "a finding about structure in a product with no rule of size is graded Important and blocks the change". *Rationale*: one sentence, that with no rule there is
    no threshold and no such test, so the same reasoning leaves the finding Minor. *Rejected*: the way not taken, "the finding graded as any other where the
    product has no rule of size — with no threshold a finding of structure can block the change on the reviewer's impression and give a round of correction,
    with the same chance in the grade as today for the form of an entry". The entry does not name WAY-328 in its fields; it names it in the *Verification*
    example only (the relation types allow no other).
  - Made to agree (found by the search): `task-cycle/review/whole_change.md` ("…the first numbers and the diff are your material, and a finding of structure is
    Minor (WAY-363)"), `product-guidelines/coding/settle.md` (the departure item: "with no rule of size, a reviewer's finding about the structure of the
    product's code is always Minor (WAY-363)") and `product-guidelines/coding/template.md` (the bullet on a product that goes without the rule).
- **Remark 2: not made**, as the handoff says (a task of the author's notes; let through). Nothing was done about it.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` — exit 0.
- `python -B gate/run_tests.py elements/part-map` — exit 0; `python -B gate/run_tests.py instruction-files` — exit 0.
- `python -B agent-instructions/skill_entry_points.py` — exit 0 (no description changed).
- `python -B task-cycle/private_paths_check.py <file>` on each of the five changed files (`foundations/decisions.md`, `product-guidelines/coding/settle.md`,
  `product-guidelines/coding/template.md`, `task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`) — each exit 0.
- Not run: the whole gate.

## The own-work check

- **Requirement most likely unmet:** every sentence about this grade says the same about a product with no rule of size.
- **Check:** a scan of `foundations/decisions.md` (from WAY-360), `task-cycle/review/SKILL.md`, `whole_change.md`, `plan/SKILL.md`, `change/SKILL.md`,
  `product-guidelines/coding/template.md` and `settle.md` for each sentence with "below the threshold", "finding(s) about/of structure" or WAY-363.
- **Result:** 13 sentences. The ones that speak of the grade where there is no rule (the binding sentence, the *Rationale*, the *Rejected* variant, the
  skill's section 3, `whole_change.md`, `settle.md`) say it is Minor; the `template.md` sentence is about a product that departs, and says Minor; the others
  are the over-threshold case, the *Rejected* variants that are not this one (as any other; always outside the scope) and the rule that the orchestrator
  regrades nothing, which the correction leaves as it was. `plan/SKILL.md` and `change/SKILL.md` hold no sentence about this grade. No sentence says a finding
  of structure is graded otherwise where there is no rule. (A first reading of the scan flagged some sentences "NO-RULE: False"; I read each one: none concerns a
  product without a rule.)

## Return step for this correction's range

Compared WAY-363 with WAY-161 (still narrowed, its *Scope* area stated), WAY-328 (the-way has no coding guidelines, hence Minor there, which is what the
correction says), WAY-360 (the rule and its departure, unchanged), WAY-361, WAY-362 (what the review asks, silent on the grade), WAY-364 (form, same
pattern) and WAY-365; the part map entries of `task-cycle` and `product-guidelines` (no file added or moved); the glossary (no new word, no word used
against its entry); the invariants of the touched parts (none is touched by wording). Nothing else no longer matches. **Corrections beyond the files above:
none; no entry, invariant, environment fact, glossary term or part-map change written.**

## Unread material

none.

## Searches not found or unclear

none.
