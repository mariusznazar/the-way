# Making a slice

What a slice, or the retry of a slice, reads, how it decides whether a failing test is its fault,
and what it does when the plan and the code disagree.

## Read

- For a slice, your section of the plan and the passages of the task, spec and plan its *Read*
  names, which the dispatch carries word for word, each with its file as its address; you open
  neither the whole plan nor the whole task. The task binds where the plan says less: the passages
  of the task your dispatch gives bind where your section says less.
- The dispatch gives the ranges of lines beside the copied passages and files, as they stand in the
  worktree when it is made. Where a range differs from the plan's, the dispatch's current range holds,
  as `task-cycle/skill/planning.md` ("A slice's handoff") gives the orchestrator.
- For the retry of a slice, the failed executor's report and what failed; the branch is back at the
  slice's base, so its commits are not yours to continue.

## A failing test

The dispatch lists no failing tests: you decide by a measure on your slice's base whether a test
that fails after your change is the fault of your slice (WAY-136). Run on the base, in a working
copy of it in your directory for working copies, only the tests that failed for you.

- A test that fails on the base too is no failing check of your slice: report it, and do not make
  it pass outside your slice's *Change*. The exception is a test that an earlier slice's *Goal*
  announced as left failing, with your slice as the one that repairs it, and that your slice's
  *Checks* hold: it is a failing check of your slice, though it failed on the base too.
- A test that passes on the base and fails after your change is a failing check of your slice,
  unless your slice's own *Goal* announces that the slice leaves it failing and names the slice that
  repairs it.
- Your report gives, for each such test, its result on the base.

## When the plan and the code disagree

- A small mismatch — a name, a path, a signature that moved — adapt to the code and report it in
  one line.
- A structural one — the plan assumes something that is not there, or the change needs a different
  shape — stop and report what the plan expected, what you found and why it matters.
- When unsure which it is, treat it as structural.
