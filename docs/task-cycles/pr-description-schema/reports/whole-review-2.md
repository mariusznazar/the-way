PASS 4327974f2cae1adcff3b50f24873d2629e8c7d5d

# Review of the fix — pr-description-schema, whole-change review `FAIL 5b685df`

Range `5b685df..4327974` on `task/pr-description-schema`, one commit (`4327974`, "docs: WAY-292
holds the block of an English task's request to none"). `git rev-parse HEAD` =
`4327974f2cae1adcff3b50f24873d2629e8c7d5d`, the head given. Bounded by
`reports/whole-review-findings.md` (I-1 only), as `task-cycle/review/fix.md` gives.

Counts: blocking 0; Minor 1 (in the fix diff); out of scope 0.

## The finding

**I-1 — fixed.** The defect: for an English task document, the template and the script held the
block to `none`, citing WAY-288, while no foundation entry said so and WAY-288 (row 3, written
whole) said the top part is repeated. On `4327974`:

- `foundations/decisions.md:8761-8784` adds WAY-292, a decision written from the spec (D1 item 6),
  not from a row. Its binding sentence says the block holds `none` for an English task document and
  the form check holds it to `none`. *Relations:* `narrows WAY-288 · narrows WAY-114 · narrows
  WAY-290`, which covers all three entries the finding named. WAY-288's binding sentence is
  unchanged, so row 3 keeps its meaning (WAY-134).
- Its *Rejected* (repeating the top part in English; leaving the block out) are ways the spec and
  the finding weighed. A decision from the spec is not bound by WAY-134's rule on a row's source.
- `task-cycle/skill/request_template.md:124` now cites `(WAY-288, WAY-292)`.
  `task-cycle/request_check.py:35` cites WAY-292 for the rule it enforces. No behaviour changed.
  `LanguageTest.test_an_english_task_with_a_translated_block_is_reported` still passes, so the
  script enforces what WAY-292 states.
- The fix report marks WAY-292 `the cycle's` with English and Polish meaning sentences, so it goes
  into this request's *For you to decide* under item 6, as WAY-291 does. That step belongs to the
  orchestrator when it writes `request.md`, and nothing in the repository can show it yet.

The template's skeleton line (`request_template.md:76-77`) still says "none where the task document
is in English" and cites nothing. It points to the same rule and needs no citation.

## What the fix itself could break

A search of the foundation for "collapsed block", "task document's language" and "human's language"
(`foundations/decisions.md:2457-2476, 4787, 8642-8648, 8704, 8731, 8761-8763`) finds no entry that
WAY-292 contradicts. WAY-291's "never empties the collapsed block" concerns a correct block that the
check misreads. It does not collide with WAY-292's `none` for an English task.

### Minor

**M-5. WAY-292 says the form check holds the block to `none` for any English task document, but the
script does so only when it can judge the task's language.**
`foundations/decisions.md:8763-8765`: "the form check holds the block to `none` there". The script
does not judge the language of a task document whose title, *Need* and *To do* hold fewer than
`MINIMUM_WORDS` (20) words, and then raises no language error (`task-cycle/request_check.py:269-273`,
`:433-440`). So a short English task with a repeated top part passes.

I grade this Minor, not Important under WAY-263, for three reasons:
- the same limit already stands under WAY-290's "the collapsed block in the task document's
  language", which the first review left as it is;
- spec D4 and the script's docstring (`:30-36`) state the minimum;
- a real task document's *Need* and *To do* run well past 20 words (this cycle's task has 582).

A wording such as "where the form check reads the task document as English" would match the code
exactly.

## Checks run

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `4327974f2cae1adcff3b50f24873d2629e8c7d5d` |
| `git log --oneline 5b685df..4327974`, `git diff 5b685df..4327974` | 0 | one commit, 3 files, +28 −3 |
| `python -B elements/common/foundation_check.py .` | 0 | 0 errors; WAY-292's relations resolve |
| `python -B gate/run_tests.py task-cycle` | 0 | OK, the English-task block test included |
| `python -B gate/run_tests.py elements/common` | 0 | OK |
| `git diff --check 5b685df..4327974` | 0 | no whitespace errors |
| `grep` for the citations of WAY-288 and WAY-292 in the template and the script | 0 | `request_template.md:124`, `request_check.py:35` |

Not run: the full gate (the orchestrator's run).

## Reaches beyond the handoff

- `foundations/decisions.md:2457-2476, 4787, 8642-8648, 8704, 8731`: the hits of the search above,
  to judge whether WAY-292 collides with an entry.
- `task-cycle/request_check.py:269-273, 433-440`: for M-5.

## Searches not found or unclear

none
