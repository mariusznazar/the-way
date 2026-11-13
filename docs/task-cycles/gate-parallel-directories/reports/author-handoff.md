# Handoff — the one author

You are the one author of this change, dispatched by the orchestrator of the task cycle `implement-task`.
The person who requested the cycle has delegated intermediate choices to the orchestrator; no answer
you get is that person's approval.

- Variant of `make-change`: "the whole change as the one author".
- Method: read `task-cycle/change/SKILL.md` whole, from the worktree below, and a file it names (one
  beside it included) only when the step or variant that names it comes.
- Worktree (your working directory; never edit another checkout, and never touch `.runs/base-check`,
  where the orchestrator's gate on the base is running):
  `the root of the task's worktree`
- Branch: `task/gate-parallel-directories`, base commit `f749cfc` (`foundations`).
- Frozen task, read it whole: `docs/task-cycles/gate-parallel-directories/task.md`
  (the task document `zadanie_the_way_bramka_rownolegle_katalogi_i_stan_wyjsciowy.md`, status
  `ready for cycle`, updated 2026-11-13).
- Your report: `docs/task-cycles/gate-parallel-directories/reports/author-report.md`

## Boundary

Make the whole change the task requires, with the foundation step (below), and return before any review.
The orchestrator runs the product's gate (`python -B gate/run_tests.py`, about 16 minutes) — you do not.
You may run the focused checks you need: `python -B gate/run_tests.py gate`, `... task-cycle`,
`... elements/common`, `python -B elements/common/foundation_check.py` (the foundation check for this
repository), and the like. Another gate run is going at the same time on this machine: your focused
checks are slower for it; do not run a full run.

## Answers of the start (step 4)

- Trust boundary: `task-cycle/gate_times.py` is a trust boundary of the part `task-cycle` and reads the
  output of `gate/run_tests.py`. The task keeps the report of every directory one block under its
  `== <directory>` line, so the script needs no change; prove it with a test that feeds `gate_times.py`
  the output of the new runner (or an equivalent block form) if `task-cycle/test_gate_times.py` does not
  cover it already. Do not change `gate_times.py` unless the proof shows it must; if it must, say so in
  the report.
- Irreversible operation: no.
- Open design choice: none. Every question of the task's *Questions to settle* is answered there; do not
  reopen one. The names of the two options, the form of the buffered report and the numbers of the new
  decisions are yours to choose and to name in the report. Where you meet a real open design choice,
  return `returned` with no code.
- Reserved choice: none.
- Settlements to record: two rows, both accepted (see the task's *Settlements to record*): row 1 (the gate
  runs directories in parallel by default, an option limits the number at once, 1 runs them one after
  another, a product writes the option into its gate command) and row 2 (the cycle skips the gate on the
  starting state under the conditions of item 4, takes the list of failing tests from the final gate of
  that cycle, even a red one, and runs the failing tests on the starting state when the final gate fails
  on a test outside the list). Both are decisions of the log: write them through the project skill
  `.claude/skills/the-way-record-decision/SKILL.md` (read it whole; it names the element's template and
  rules). The task also changes WAY-349 — by one sentence and in its *Verification* (see its *Decisions in
  play*): the run on the starting state goes through the script when the cycle makes it (item 4), and
  *Verification* requires that run only in such a cycle. Edit WAY-349 in place (WAY-07), as the skill gives.
- Where the task says "the cycle", the files that carry the rule are: `task-cycle/skill/SKILL.md` (step 4,
  the paragraph that begins "Create a task branch from the current target branch", about line 128; and
  step 2's mention of the run on the commit that moved the pin, and step 10's list of the runs of the
  gate), `task-cycle/record_template.md` (*Verification*), `task-cycle/skill/request_template.md` (the
  variant of a request with a reserved choice, and wherever the base run is named), and
  `agent-instructions/README.md` (the time of a full run, "about 16 minutes"). Grep the tracked files (not
  `.runs/`, not `docs/`) for what else names the run on the base, e.g.
  `grep -rnE "starting state|run on the base|the base alone|checks already failing" .` and read each place
  whole before you decide it needs no change (`task-cycle/review/whole_change.md:43` and
  `process-audit/` read the base run or the gate times: check that they stay true).

## What to read (selected by "Reading the foundation" in `elements/common/way_of_working.md`)

Parts touched: `gate`, `task-cycle`, `agent-instructions`; the log itself (`decisions`) and the part map
entry `test-runner-command` (the agreement with products: the command keeps its name, argument and exit
codes; a new option does not break it).

- `agent-instructions/README.md` — how the-way's own changes are made before `main` (the search of the
  foundation, WAY-33, and the return step of the change included).
- Decisions in `foundations/decisions.md`, each whole, from its heading to the next heading: the task's
  *Decisions in play* — WAY-16, WAY-55, WAY-160, WAY-243, WAY-349 — and besides them WAY-350 (derives from
  WAY-349) and every decision whose *Scope* names `gate` or `task-cycle` that your search of the log
  finds and whose topic is the gate, its times, the base run or the test runner (search `Scope` for the
  two parts, then read the titles; read whole each that bears on your change).
- Invariants in `foundations/invariants.md` whose *Part* names `gate`, `task-cycle`, `agent-instructions`
  or `every`.
- Part map `foundations/part_map.md`: the entries of `gate`, `task-cycle`, `agent-instructions` and
  `test-runner-command`.
- Glossary: the entries for the words your sentences use (read `foundations/glossary.md` whole, it is short).
- Files you change and the tests beside them: `gate/run_tests.py`, `gate/test_run_tests.py`,
  `task-cycle/gate_times.py` and `task-cycle/test_gate_times.py` (read; change only as said above),
  the four instruction files above.
- `task-cycle/skill/foundation_step.md` — the foundation step of the cycle; read it whole and follow it.
- The product guidelines of the-way itself: there are none; `product-guidelines/` holds the method for
  products. Report the reading as `none apply`.

## Facts the orchestrator found (use them, check what you rely on)

- `gate/run_tests.py:93` — `run_all` has a loop `for directory in directories:` that starts a child process
  (`python -B gate/run_tests.py <directory>`) and waits for it before the next. The summary line is
  `<n> tests in <m> directories; every directory passed` or `...; failed: <dir> (exit code <c>), ...`.
- `task-cycle/gate_times.py` reads a time from the block that a line `== <directory>` opens and the first
  line `Ran <n> tests in <s>s` in that block, directories in any order. So each directory's report must be
  written whole, after its end, under its `== <directory>` line, never interleaved. The per-directory time
  reported stays the directory's own `Ran ... in <s>s` line.
- `unittest.TextTestRunner` takes `durations` (Python 3.12 and later, checked on 3.14.3 on this machine);
  the option that prints the slowest tests must work on the Python the-way pins (`.python-version`:
  3.14); say in the report what happens on an older Python (a clear message, not a traceback) or that you
  checked the lowest version a product could use and found none.
- The runner's exit codes stay as `gate/run_tests.py` documents them (WAY-63 included). With the option for
  the number of directories at once, a wrong value (zero, negative, not a number) is an error of the call,
  exit code 2 with a message, like the other errors of the call.
- Memory: a parallel run of ten directories starts as many processes at once by default ("all at once, or
  as many as the cycle chooses" — the task, item 2). Your default is: all directories at once. Name in the
  report what you chose for the value of the option and its default.
- A new test file in a new directory runs only after `git add`; a test file you add in an existing directory
  runs with it.

## Reminders from the orchestrator

- Edit only what the task requires. Out of scope: parallel test files within one directory; any change in the
  game's repository.
- The runner's docstring is its documentation: bring it up to date (parallel by default, the options, the
  form of the report). Keep to the style of the file.
- Tests: cover (1) the report of every directory whole under its own line and no interleaving when two
  directories finish in an order other than the sorted one, (2) the limit option: 1 runs one after another,
  a wrong value exits 2, (3) the option that names the slowest tests, and that without it the output keeps
  its form, (4) the final line and the exit codes as before, (5) that `gate_times.py` reads the output.
  Follow how `gate/test_run_tests.py` tests today (it may use temporary git repositories).
- In the instruction files, write the new text the way the file writes: step 4's paragraph states the rule
  of item 4 in the task's words (the check in git, what the orchestrator records and from where it takes the
  list, the fall back to running the gate on the starting state, and item 5's run of the failing tests on
  the starting state); step 2's and step 10's mentions of the run on the starting state say that it is made
  when step 4 requires; the record template's *Verification* says where the list comes from when the run is
  skipped (the record names its source); `request_template.md` keeps working for a cycle with no base run.
  Do not widen the rule beyond the task's text.
- The foundation step writes WAY-349's change and the two decisions; the return step compares the entries
  and the part map with the repository afterwards (the orchestrator dispatches the return step later; you do
  the foundation step and return before review).
- Check the foundation of the change before you return: `python -B elements/common/foundation_check.py`
  (add what its usage gives for this repository) and the focused tests of the directories you changed.
- Own-work check, commits and the report: as the method gives them. Commit messages: English, as the
  history of the repository does; `git add` by path only.
