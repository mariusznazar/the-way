# Walking through the running product

What the own-work check adds when a change alters behaviour that a user sees in the running
product: a screen, an answer of an API, a command in a terminal, data the product shows. You make
the walk after the code and before you return, as the one author of a change or as the executor of
a slice, against the passages of the task your handoff gives; the fix of a review's findings does
not repeat it (WAY-406). The walk finds what the tests of the change leave out. It does not
replace the tests, the own-work check of `SKILL.md` or the screenshot of `ui_check.md`, which stand
beside it.

Judge first whether the change alters such behaviour, and say so in your report either way. A change
that only rebuilds code, with no change of what a user sees, has no walk: the report says that and
gives the one sentence why.

## 1. Prepare

- The task: the whole of it as the one author, the passages your handoff gives as the executor of a
  slice. The change: your diff.
- The way to the running product, which the foundation of the product settles: its logs, its
  interface, its development data and the place of its screenshots. Read the decisions that settle
  them. A skill of the product may hold the steps of operation and cites the decision, so search the
  product's skills for the identifier of each of those decisions and read each skill found.
- Whether the product runs: start it, or probe it, by that way before anything is called
  unavailable. A product that does not start is a fact to report with its evidence, not a reason to
  skip the case.
- Where the foundation settles no way to the running product, the walk is not performed. Make
  sections 2 to 4 all the same, do not run section 5, mark every case of the plan unchecked with
  that reason, and go on; the cycle does not stop (WAY-406).

## 2. What the change alters

In the words of the user, not of the code: what the user sees or does differently. Then the code shared
with other paths that the change touches — callers beyond the changed path, a function several
screens or commands use. That shared code is where a case of regression comes from.

## 3. Scope

Set each requirement of the task against what the tests of the change already cover. The walk takes
what they do not cover: a behaviour no test reaches, a join of layers no test crosses, what the
user sees that no assertion reads.

## 4. The plan of cases

A table, one row per case:

| Case | By what | Verdict |
|---|---|---|
| what is checked and which result is right, by the requirement of the task | the way of the running product that checks it: a screen in a browser, a call of an API, a command in a terminal, a reading of the data the running product holds | filled at the end |

- A reading of the code is no way to the running product and fills no row of that column: a case
  that only the code could check stays unchecked, with that reason.
- The cases follow the requirements of the task, not the code alone. No one approves them before the
  walk (WAY-407).
- Order the cases by their conditions: first those whose state later cases need, in the order the
  state is built, then those that use it. A rule that puts first the case most likely to fail is not
  taken: it collides with the order that the state gives and pushes to speculation in a small
  change.
- The last row is always "side observation": the place for what you notice on the way that no one
  planned. A plan without it is a cage, and the end of the list looks like the end of the checking.

## 5. The run

Case by case, by the way of the product that the row names.

- A case that fell wrong does not break off the walk: note the result and go on. Diagnosis waits
  for the end, since cases that fell wrong often share a cause, and a diagnosis from one symptom
  leads aside when the second comes.
- The plan widens only on a hard signal from the run: an error in the logs on a path no case
  checks, a difference between the answer of the API and what the screen draws, a write nobody
  expected. A thought that one could also check an empty list is no signal.
- The walk triggers no effect outside the product that costs or cannot be undone — a real mail, a
  payment, a call of a paid API — unless the product settles a stand-in for it. Without a stand-in
  the case stays unchecked, with that reason (WAY-406; WAY-13 for what cannot be undone).
- Where a case can be checked by reading the state of the page or the answer of the API, the verdict
  rests on that reading, made in code or by a query; a screenshot serves the human, and your own
  reading of a screenshot is no measurement. A screenshot you show the human, the browser and the
  working copies follow `ui_check.md` and the dispatch's paragraph on working copies.
- The verdict takes in everything the user sees on the screen, dialogs and messages too, and not the
  element you check alone.
- Where the way to the product or the browser does not work, write down the limitation and give the
  evidence from the layer you did check, such as the answer of the API, instead of calling the case
  checked.
- Where a case stays unchecked for want of a tool, name the tool that was missing; a task for it is
  the human's to open, not yours.
- Where a case shows behaviour that depends on the platform, say where you checked it: the system,
  the browser and the address.

## 6. The verdict

First one statement, "what I did not check": each area outside the plan that you did not touch and
each case left unchecked, with the reason of each, and what you noticed on the way that has no
bearing on the task. It is the one thing that makes you look beyond the list; without it the walk
ends in "all cases passed" and nothing more is known.

Then the verdict of each case, not one for all. Name the layer where the case decides, where it
does: "the API computes right, the screen draws wrong" is a full result. Before you call a
difference between two measurements a regression, say what you compared with what and when you
measured each; where the two cannot be made comparable, the verdict is "do not know", not
"regression".

A case that fell wrong is yours to correct before you return, with a test at the lowest level that
catches the error (WAY-408). Every disagreement with the task is an error to correct, not a remark
in the margin. An error outside the task's scope you do not correct: the report names it, and the
request puts it before the human.

The report holds, as `SKILL.md` section 6 gives it, the plan with the verdict of each case, where
you checked, what fell wrong and what you corrected with which test, what you did not check and why,
and the errors outside the task's scope.
