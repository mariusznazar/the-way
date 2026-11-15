# Report of correction 1 — task `small-fixes-after-prs-117-121`

**Status:** done. Head before: `aefe984`; one commit: `5cb2e1f` (5 files).

## How each remark was made

1. **The added pair is quoted under its entry.**
   - `task-cycle/skill/request_template.md`, item 6 of the top part: an entry marked `the cycle's` because of a pair of examples its writer added says so in its sentence there, and the pair stands word for word under the entry in *Foundation entries*; a pair kept only until a test of the same change holds the sentence, and a link in *Relations*, make no such mark (so the rule is no wider than the foundation step's marking).
   - The same file, *Foundation entries* of the lower part: under an entry marked `the cycle's` because of an added pair, the pair word for word, the *complies* and the *violates* sentence each as the entry holds it. This is the form this request already has.
   - `task-cycle/skill/foundation_step.md`: the writer keeps the added pair word for word in its report, for the description to quote (without this the description's writer has nothing to quote from; one clause).
2. **r1.** `agent-instructions/README.md`: "an invariant that reads `test` whose sentence a change rewords and whose copy at that commit lacks *Method* or *Part* it lists too, naming the field, whether or not a file citing it changes" (code: `list_invariants` skips an invariant whose *Method* is not `test` before it computes the missing fields).
3. **r2.** `elements/invariants/template.md` row *sentence*: "and, whether or not a file citing it changed, one that reads `test` whose sentence a change reworded and whose copy at the base lacks *Method* or *Part*, the line naming the invariant and the field (WAY-344)".

## Search of the foundation (WAY-33) and the entries changed for it

- Decision WAY-114 states what the description gives ("one English sentence" per entry in the lower part) and now disagrees with the rule. I changed it in place, as a clarification of what the description shows and no change of its meaning: the binding sentence gains "and an entry that is marked as the cycle's because of a pair of examples its writer added has that pair there word for word under it"; *Verification* gains a clause in *complies* ("and an entry that gained a pair of examples the row did not give has the pair there word for word") and in *violates* ("an entry marked as the cycle's for an added pair of examples reaches the merge with the pair not shown"); *Rejected* gains one way ("the sentence of meaning alone for an entry that gained a pair of examples — the examples are what agents measure every later change by, and a sentence of meaning does not show them"). WAY-114 is a decision that changed by the human's remark, not by an added pair of the cycle; the orchestrator may show the added clauses with the entry. If the orchestrator holds the change of WAY-114 wider than the remark, one `git revert` of the hunks in `foundations/decisions.md` of `5cb2e1f` is the way back; the rule of the request template does not need it to work.
- Other places that say "one plain sentence of its meaning": `request_template.md` lines for rules with decision `none`, working copies and directories — different matters, no change. No skill other than the request template and the foundation step repeats item 6.

## Return step for what the remarks touch

Compared the README and the template rows with `list_invariants` (`elements/common/foundation_check.py`): the code lists one line, `` `<name>` reads `test` and its sentence is changed by this change, while its copy at the base lacks <fields>, so it was not compared with the files that cite it ``, only for an invariant that reads `test` now, has both fields now and whose sentence differs. The README and the template agree with it now; before the correction both read more broadly or ambiguously (r1, r2). The sentence of WAY-344 and its test lines needed no change. Marks of entries written earlier are unchanged (WAY-344 `row 3`; WAY-139 and WAY-60 `the cycle's` with their pairs; WAY-61 *Scope*, WAY-229, rationale of WAY-160 `the cycle's`). WAY-114 is the only entry this correction writes; no invariant, environment fact, glossary term or part-map change.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | 534 tests OK (skipped=1); once more after the `foundation_step.md` edit, 0, same count |
| `python -B gate/run_tests.py agent-instructions` | 0 | 37 OK (expected failures=2, as on the base) |
| `python -B gate/run_tests.py product-guidelines` | 0 | 14 OK |
| `python -B gate/run_tests.py elements/common` | 0 | 246 OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Not run: the full gate. No test checks the wording of the request template's rule (behaviour of an agent following a text is not tested, per the testing guidelines); the review reads it.

## Own-work check

Requirement most likely not met: remark 1's "no wider than the rule" — the rule is limited to an entry marked for an added pair; I checked that the three limits (pair kept until a test holds the sentence; link in *Relations*; entry marked for another reason) are named in item 6. A weak point: the top part's item 6 does not itself show the pair, only says it stands in the lower part; I followed this request's form (item 8 of its description says so and the lower part carries the pairs).

## Unread material

`docs/task-cycles/small-fixes-after-prs-117-121/reports/review-return-report.md` was read only at findings r1–r3 (lines 50–90). Finding r3 (a meaning sentence for WAY-344) is the orchestrator's: the return step's report did not state one; the sentences the reviewer suggested are the ones I hold right.

## Searches not found or unclear

None.

## Working copies

`.runs/author/` held scripts and run outputs; removed (`find .runs/author -mindepth 1 -delete`). Remainder: none.
