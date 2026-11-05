# Fix report — pr-description-schema, whole-change review `FAIL 5b685df`

**Status:** done

Variant: the fix of a review's findings. Range of the fix: `5b685df..4327974`, one commit.

## I-1 — fixed

The finding holds. WAY-288 is written whole from row 3 and has no exception for a task document in
English. But the template (`task-cycle/skill/request_template.md:77`, `:122-124`) and the script
(`task-cycle/request_check.py`, docstring and the check "the task document is in English; the block
reads `none`") hold that block to `none`, and the template cited WAY-288 for that rule.

**How:** I followed the finding's smallest form, in the same shape as WAY-291 and spec D10 A. A new
decision, written from the spec (D1 item 6) and not from a row, states the exception, and WAY-288
keeps row 3's meaning unchanged.

- `foundations/decisions.md`: new **WAY-292** — "What does the collapsed block of a request's
  description hold where the task document is in English?". Binding: where the task document is in
  English, the block holds `none` in place of a second English copy of the top part, and the form
  check holds it to `none` there. *Relations:* `narrows WAY-288 · narrows WAY-114 · narrows
  WAY-290`. The finding says the exception also reaches WAY-114's "repeated in the human's
  language in the description's collapsed block" and WAY-290's "the collapsed block in the task
  document's language", so the new decision names all three. *Rejected:* the top part repeated in
  English (a copy that buys nothing), and the block left out for an English task (the skeleton
  would differ, and a forgotten block could not be told apart). Both are the ways the finding and
  the spec weighed; no row's source keeps ways for this choice.
- `task-cycle/skill/request_template.md:124`: the citation now reads `(WAY-288, WAY-292)`.
- `task-cycle/request_check.py` docstring: "Where TASK is English, the block reads `none`
  (WAY-292)". No behaviour changed.

**Check that shows it:** `python -B elements/common/foundation_check.py .` exit 0. The relations
resolve, and no two decisions narrow each other. The script's existing test
`LanguageTest.test_an_english_task_with_a_translated_block_is_reported` still passes inside
`python -B gate/run_tests.py task-cycle` (exit 0). So the rule now enforced is the one WAY-292
states.

Search of the whole foundation for the new entry (WAY-33): `grep` for "collapsed block", "in the
task document's language" and "human's language" over `foundations/*.md`. Hits: WAY-114, WAY-288,
WAY-290 (each now narrowed by WAY-292) and WAY-291. WAY-291's "never empties the collapsed block"
is about a form error held wrong, and WAY-292 does not collide with it. Also hit: WAY-172's line on
a definition's headings (`:4787`), which is unrelated. No invariant, glossary term, environment fact
or part-map entry needs a change.

## Entry written

| Entry | Mark | English meaning | Polish meaning |
|---|---|---|---|
| WAY-292 (new) | the cycle's | Where the task document is in English, the collapsed block of the request's description holds `none` instead of a second English copy of the top part, and the form check holds it to `none`. | Gdy dokument zadania jest po angielsku, zwinięty blok w opisie PR-a ma `none` zamiast drugiej, angielskiej kopii górnej części, a skrypt sprawdzający formę tego pilnuje. |

As an entry the cycle wrote, WAY-292 stands in this request's *For you to decide* under item 6, as
WAY-291 does.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py .` (after the entry) | 0 | 0 errors |
| `python -B gate/run_tests.py task-cycle` | 0 | OK |
| `python -B elements/common/foundation_check.py .` (after the docstring reflow) | 0 | 0 errors |
| `python -B gate/run_tests.py elements/common` (the fix touches the decision log, which its tests read) | 0 | OK |

Not run: the full gate, which is the orchestrator's. Minor findings M-1 to M-4 were not touched, as
the handoff gives.

## Reaches beyond the handoff

none

## Searches not found or unclear

none
