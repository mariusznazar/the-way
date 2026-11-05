# Blocking findings of the review of the whole change

From `reports/whole-review.md` (`FAIL 5b685df`), in the reviewer's words; the range under review was `f45ca40..5b685df`. Only this finding blocks; the Minor findings and the line under *Declined to judge* are not fixed.

**I-1. For a task document in English, the template and the script require the opposite of what
WAY-288 says: the block must read `none`, while WAY-288 says the top part stands a second time in
the task document's language.**

What a human would see: a request for a task written in English gets no repeated top part, and the
script reports an error if the cycle writes one. That is a sensible rule. But the foundation entry
the change writes says something else, and nothing in the foundation says it.

- `foundations/decisions.md:8641-8642` (WAY-288, written whole from row 3): "A request's description
  is written in English, and its top part stands a second time, in the language of the task
  document, in a collapsed block of the description." No exception for an English task document.
- `task-cycle/skill/request_template.md:76-77` (skeleton: "none where the task document is in
  English") and `:122-124` ("where the task document is in English, the block holds only `none`
  after its summary (WAY-288)"). These cite WAY-288 for a rule WAY-288 does not hold.
- `task-cycle/request_check.py:433-434`: where the task is English and the block holds anything but
  `none`, it reports "the task document is in English; the block reads `none`". The docstring says
  the same at `:34-35`.
- The same unstated exception also reaches two other entries the change writes or changes:
  WAY-114 at `foundations/decisions.md:2461-2462` ("repeated in the human's language in the
  description's collapsed block"), and WAY-290 at `:8703-8704` ("the collapsed block in the task
  document's language"). For an English task document, the files make that block `none`.

Why it matters: WAY-263 grades this Important. The change's files fail to do what an entry the
change writes requires (repeat the top part), and they cite that entry for a rule it does not hold.
The exception changes row 3's meaning. WAY-134 lets the cycle write a row only whole, keeping its
meaning, and `task-cycle/skill/foundation_step.md` says "The writer never writes a row with another
meaning". So the exception cannot go into WAY-288 either. This is the same shape as finding A of
`reports/spec-review-2.md`, which the orchestrator settled in spec D10 A by writing the exception as
a decision of its own (WAY-291, `narrows WAY-290`, marked `the cycle's`). Spec D1 item 6 gives this
exception the same way, but no entry records it. The author's report saw it and passed it to the
orchestrator to weigh for *For you to decide* (`reports/author.md`, *Choices under Left to the
maker*, "WAY-288's binding sentence"). That shows the choice to the human, but after the merge
WAY-288 would still say one thing while the script enforces another. A later reviewer of an
English-task request, judging by WAY-288, has a foundation that contradicts the script.

Evidence: the lines quoted above. The script holds the `none` rule:
`test_request_check.py::LanguageTest::test_an_english_task_with_a_translated_block_is_reported`
passes on HEAD, as part of `python -B gate/run_tests.py task-cycle` (exit 0).

Fix (the smallest form the rules allow): add a decision written from the spec, not from a row.
Something like "What does the block hold where the task document is in English?": `none`, since the
English top part already serves that reader. It `narrows WAY-288`, is marked `the cycle's`, and
stands in this request's *For you to decide* under item 6, as WAY-291 does. Point the template's
`(WAY-288)` at `:124` to it. The other permitted way is to drop the `none` rule from template and
script, so that an English task's block repeats the top part, but that buys the reader nothing.
