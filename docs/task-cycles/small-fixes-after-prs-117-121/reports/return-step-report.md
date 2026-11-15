# Report of the return step — task `small-fixes-after-prs-117-121`

**Status:** done. Range compared: `b6b3416..eaf815c`. One commit: `4066ae5` (changes four files: `foundations/decisions.md`, `foundations/part_map.md`, `agent-instructions/README.md`, `elements/invariants/template.md`).

## Foundation compared with the code

- **WAY-344** (sentence, *Verification*) against `list_invariants` and its tests. Mismatch 1: the new sentence said "a field missing from that copy is listed", the code lists it only for an invariant that reads `test` now, has both fields now and whose sentence a change reworded — a field the script needs for the comparison. Corrected: "a field it needs for a comparison and finds missing from that copy is listed…" (the sentence still begins as the test's line `decision:` quotes it). Mismatch 2 (the return step's own rule on pairs): the two clauses I had added to WAY-344's pair of examples ("the same script, reading a copy… lists an absent section of that copy on a line `listed:`…" and "a script that checks the form of a file ends with an error at a field missing from the copy… or passes over it without a word") state what the tests `test_reworded_invariant_lacking_method_or_part_at_base_is_listed_with_the_field`, `…_lacking_both_fields_at_base_is_listed_in_one_line` and `…_though_its_citing_file_changed` now hold, and the *Verification* clause `tests:` already names it; the clauses are removed, so the pair is the one the base had.
- **WAY-139, WAY-60, WAY-61, WAY-229, rationale of WAY-160**: compared with `resolve_gaps.md`, the templates, the plan skill and the two steps of `task-cycle/skill/SKILL.md`; no mismatch. No place other than WAY-229 and those two steps repeats the sentence on the strongest class.
- **`agent-instructions/README.md` and the *sentence* row of `elements/invariants/template.md`** (the review's Minor n1): both read as if the base-copy listing happens only where no citing file changed; the code and WAY-344 list it either way. Corrected both: README "an invariant whose sentence a change rewords and whose copy at that commit lacks *Method* or *Part* it lists too, naming the field, whether or not a file citing it changes"; template row "…naming the field and whether or not a file citing it changed, one that reads `test` whose reworded sentence's copy at the base lacks *Method* or *Part* (WAY-344)".
- **Part map**: the part `elements-common` now names "the module that reads the files and git for" the check script (`elements/common/foundation_source.py`, which `elements/common/**` already claims). The other touched parts' descriptions (`gate`, `decisions`, `invariants`, `project-level`, `product-guidelines`, `task-cycle`, `agent-instructions`) match; no *Depends on* or *Trust boundary* changes: the new module imports only the standard library.
- Glossary terms: none used in a new meaning. Environment facts: none (the session record named in To do 20 is a source of the task, not one the foundation rests on; WAY-229 states the observed fallback as observed, per the review).

## What the change wrote (account carried from `author-fix-report.md`, with the return step's correction)

| Entry | Mark | Note |
|---|---|---|
| WAY-139 | `the cycle's` (settlement of row 1; the added pair is not the row's) | pair as in `author-fix-report.md` |
| WAY-60 | `the cycle's` (row 5; added pair) | pair as in `author-fix-report.md`, the *complies* clause as m1 changed it |
| WAY-344 | **`row 3`** (corrected by the return step) | the added pair clauses are removed above because tests hold them; no added pair remains, so the mark `the cycle's` of the fix report no longer applies |
| WAY-61 *Scope* | `the cycle's` (To do 15) | unchanged |
| WAY-229 | `the cycle's` (To do 20) | unchanged |
| WAY-160 rationale | `the cycle's` (To do 14) | unchanged |

Rows of *Settlements to record*, each with its place: 1 → WAY-139 (sentence, *Verification*, *Rationale*, *Rejected*) and `project-level/task/skill/resolve_gaps.md`; 2 → `product-guidelines/coding/template.md`, `styleguide/template.md`, `testing/template.md`; 3 → WAY-344 (and the code and tests of To do 8); 4 → `elements/decisions/template.md`, `task-cycle/skill/foundation_step.md`; 5 → WAY-60 and `elements/invariants/template.md`; 6 and 8 → `task-cycle/plan/SKILL.md`; 7 → `project-level/task/template.md`; 9 → `task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md`. The return step writes no decision, invariant, environment fact, glossary term or projected entry; no row was missed by the foundation step.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` | 0 | 246 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 37 OK (expected failures=2, as on the base) |

Not run: the full gate.

## Own-work check

The requirement most likely not met: "no entry left false after the change" for WAY-344 — checked by reading the sentence against the three branches of `list_invariants` (field lacking now: error, no listing; lacking at base with sentence reworded: listed; lacking at base, sentence unchanged: not listed) and by the foundation check passing with the test lines `decision:` of the sentence unchanged in their quoted start.

## Unread material

None beyond the earlier reports; the files compared were read at the lines named.

## Searches not found or unclear

None.

## Working copies

`.runs/author/` held scripts and run outputs; removed (`find .runs/author -mindepth 1 -delete`). Remainder: none.
