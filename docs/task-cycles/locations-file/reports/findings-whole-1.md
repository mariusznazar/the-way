# Findings of the review of the whole change, `FAIL 973ee64` — for the fix

Range reviewed: `17b83bf..973ee64`. Cut word for word from `reports/review-whole-report.md`
(the reviewer's words, grades and scopes unchanged): the blocking findings first, then the Minor
findings of this review within the task, which are fixed in the same fix (WAY-161).

### Important (blocking)

**I-1 — WAY-320 states the rule of settlement row 3 without its qualification, and the repository's
files do what it forbids.** `foundations/decisions.md:10210-10211` (WAY-320):
"No file the repository tracks holds an absolute path or a note link; a file that points to such a
place names its entry in the locations file." Row 3 of *Settlements to record*, and the invariant
`tracked-file-private-paths` the change writes from it (`foundations/invariants.md:88`), both carry
the exception for the four files that write example paths. WAY-320 drops it, so on the head commit
four tracked files (`task-cycle/private_paths_check.py`, `task-cycle/test_private_paths_check.py`,
`instruction-files/check_instructions.py`, `instruction-files/test_check_instructions.py`) do what
the decision forbids — the task's *Context* counts 98 such hits in them. WAY-263 grades as Important
a change whose files do what an entry it writes forbids, or that restates an entry more broadly or
without a qualification; both hold here. Why it matters: a later agent reading WAY-320 alone, as a
decision a *Scope* search selects, would take the exemption list as a violation and "fix" the
examples or the test, the very way question 2 rejected. Related gap in the same entry: the reasoning
of question 2 — the price taken (a real path pasted into a listed file passes; adding a file to the
list shows in the diff) and its three not-chosen ways — stands in no entry; the invariant has no
rationale field and WAY-320, from which it derives, carries only question 1. Fix: qualify the
sentence (for example, "…other than the files the invariant `tracked-file-private-paths` names,
which write example paths in order to find or test them"), or narrow it to what the *violates* bullet
already says (the path of a place on the user's disk, a link to a private note), and add the price
and the not-chosen ways of question 2 to WAY-320's rationale and *Rejected*.
Evidence: the sentences quoted; `python -B gate/run_tests.py task-cycle` exit 0 only because the
test skips the four files.

**I-2 — `project-level/backlog_place.md` cites WAY-140 for a rule WAY-140 contradicts, and contradicts
the task-cycle skill that sends the orchestrator to it.** `project-level/backlog_place.md:23-25`:
"An agent that runs a task cycle writes nothing outside the repository (WAY-140): it names the
missing entry in its report and goes on only with what it can do without the place." WAY-140 says the
opposite for the backlog: "the cycle's record of the request and of the task's state in the backlog
entry the product names (WAY-107) is no effect of the task", and its *complies* example is "the cycle
itself adds the request link to the task's entry in the product's backlog". The change itself makes
`task-cycle/skill/SKILL.md:76-78` read "in the task's entry in the backlog the product names
(WAY-107), found as `project-level/backlog_place.md` gives, the cycle may add the request link and set
the task's state" — so the orchestrator follows a pointer into a file whose sentence, taken as
written, forbids that very write. This is a sentence the author added beyond the task (declared in
the report as a "weakest point"); the intended rule — a cycle does not create or change the user's
locations file — is right, but the wording is broader than the rule and misattributes it. Graded
Important: two instructions the same agent reads together disagree on whether it may write the
backlog entry, which is fragile behaviour of the cycle's last step. Fix: narrow the sentence to the
locations file, for example "An agent that runs a task cycle does not create or change the locations
file (WAY-140): …".

### Minor (within the task)

**M-1 — `project-level/backlog_place.md:20-21` widens the trigger of "missing" beyond WAY-107.**
"…or the path it holds does not exist, the place is missing." WAY-107 (as changed) names the place
unnamed, or the file or entry missing. Treating a dangling path as missing is a reasonable user's
expectation and contradicts nothing, so it is Minor; either add "or the path it holds does not exist"
to WAY-107 or leave it as the operational reading. The author declared it.

**M-2 — `project-level/backlog_place.md:10` and `:28` write the example as "the entry `tasks` under
`the-way`".** The file is read by skills working in any product; at `:28` the sentence reads as a
fixed phrase ("those say … and nothing more"), so an agent in a product may copy the-way's name.
Write it as "the entry `tasks` under the product's name, as …" or mark it as the-way's own example.
