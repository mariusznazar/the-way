# Handoff — review of the whole change

You are a reviewer of the task cycle `implement-task`. You did not make this change. The person who
requested the cycle has delegated intermediate choices to the orchestrator; no answer you get is that
person's approval. Read-only: change no file except your report.

- Method: `task-cycle/review/SKILL.md` of the worktree below, whole; it sends you to
  `task-cycle/review/whole_change.md` for the review of the whole change: read it and follow it. Read a
  file those name when the step that names it comes.
- Worktree (the root of the checkout to read and run in; never edit another checkout, never touch
  `.runs/base-check`):
  `the root of the task's worktree`
- Review: the whole change, range `f749cfc`..`264703f` (base `foundations` at `f749cfc`; head `264703f`;
  three commits `a6807f1`, `9bea9a1`, `264703f`).
- Frozen task, read it whole: `docs/task-cycles/gate-parallel-directories/task.md`
- The author's report, read it whole: `docs/task-cycles/gate-parallel-directories/reports/author-report.md`
  (the author had no plan: one author, no slices, no spec).
- Your report: `docs/task-cycles/gate-parallel-directories/reports/whole-review-report.md`

## Answers of the start (step 4)

- Trust boundary: `task-cycle/gate_times.py` (a trust boundary of the part `task-cycle`) is not changed,
  but it reads the output of `gate/run_tests.py`, which is. Check that it still reads the new output (the
  author added a test in `task-cycle/test_gate_times.py` for it) and that the runner takes no input from
  outside the repository other than its options; check crafted values of the options.
- Irreversible operation: no.
- Open design choice: none at start. The names of the two options (`--jobs`, `--slowest`), the form of the
  buffered report and the numbers WAY-366 and WAY-367 are the author's choices of how to make what the task
  settles; judge them, do not reopen what the task's *Questions to settle* answers.
- Reserved choice: none.
- Settlements to record: rows 1 and 2 (both accepted); the author wrote them as WAY-366 and WAY-367 and
  changed WAY-349 in place (the task's *Decisions in play* carries that change).

## Points the orchestrator asks you to check besides section 2 of the method

- Every item of the task's *To do* (1–5), every answer of *Questions to settle* and both rows of
  *Settlements to record* is covered; the source fidelity of the decisions: their wording against the
  task's wording and sources (task *Questions to settle*, *Decisions in play*). The task's words win over
  the author's where they differ.
- The step 4 paragraph of `task-cycle/skill/SKILL.md` states item 4 and item 5 as the task words them:
  the check in git (tree of the base equals the tree of the merged branch's head), skipping the run, taking
  the list from the final gate of that cycle (red too) from its record in git history, writing into the
  record where it came from, the fall back to running the gate as before, and item 5's run of the failing
  tests on the base. The author says "the last copy is the one" where the merged branch added the record
  more than once, and that this goes slightly past the task's words: judge whether it does.
- WAY-349's change is by one sentence and its *Verification* (the task's *Decisions in play*): nothing more.
- The files that name the run on the base (`task-cycle/skill/SKILL.md` steps 2, 4, 10, `record_template.md`,
  `request_template.md`, `agent-instructions/README.md`, and those the author judged true unchanged:
  `task-cycle/review/whole_change.md:43`, `task-cycle/plan/SKILL.md:177`, `task-cycle/skill/reserved_return.md`
  lines 39–46, `process-audit/SKILL.md` lines 50–70) agree with each other and with the decisions; any file
  the author did not search that names the run on the base. The author left unread the lines 31–39 of
  `request_template.md` and read only passages of four of those files: read them whole yourself where they
  bear on your judgment.
- The runner: the report of a directory whole under its `== <directory>` line with no interleaving; the
  final line and the exit codes as before (WAY-63, the invariant `gate-exit-code`); the options and their
  errors; `--slowest` and an older Python; memory and the failure of a directory that hangs; a directory
  whose output has no line end; the tests prove what they claim (fail on a runner that does the opposite).
  `python -B gate/run_tests.py gate` and `python -B gate/run_tests.py task-cycle` you may run; do not run a
  full run of the gate (the orchestrator runs it).
- The author's concerns, which you judge as findings or not: the audit takes the gate times as one series
  until `task-cycle/gate_times.py` changes (`process-audit/SKILL.md` lines 57–60); the unmeasured time in the
  README sentence; no live output with `--jobs 1`; the mark of the WAY-349 change.
- Foundation reading: you select your own, as the method gives (WAY-150): the parts touched are `gate`,
  `task-cycle`, `agent-instructions` and the decision log; the decisions the task's *Decisions in play* names
  you read whole. State in your report how many decisions you read whole and how many by title only.
- Product guidelines of the-way itself: none apply; report the reading as such.
