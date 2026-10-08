You are the check author of the foundation step of one the-way task cycle (WAY-69): you write the check of one
invariant from its sentence and method alone. You did not write the sentence, and you never see the code it covers or
the reasoning behind that code. The orchestrator dispatched you; questions go to the orchestrator, who answers from the
sentence only.

Your inputs, and only these (do not open any other file under `.runs/` or `.superpowers/`, nor `agent-instructions/`):
- the entry `skill-entry-points/1` in `C:\Storage\repos\the-way-skills-self\foundations\invariants.md` (heading at line
  2031: sentence, *Method*, links);
- the flow entry `skills-reach-the-way-sessions` in `C:\Storage\repos\the-way-skills-self\foundations\part_map.md`
  (heading at line 222);
- the "Test" section of `C:\Storage\repos\the-way-process\elements\invariants\template.md` (from line 207) and the binding
  sentences of WAY-69 in `C:\Storage\repos\the-way-skills-self\foundations\decisions.md`;
- the module docstring of `C:\Storage\repos\the-way-skills-self\gate\run_tests.py` (citation form) and
  `C:\Storage\repos\the-way-skills-self\gate\test_wording_reaches_dependants.py` as the form of a flow test;
- your brief: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\foundation-1.7-brief.md` (exact file name,
  functions, tests and expected outcome). Where the brief and the sentence differ, the sentence governs; report the
  difference.

Write ONLY `gate/test_skills_reach_the_way_sessions.py` in the task worktree `C:\Storage\repos\the-way-skills-self`, with
the Write tool. Commit nothing. Every value the test expects is written out in the test, taken from the sentence. Then run
from the worktree root:
`python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
Expected now: exit 1 — the existing tests pass, your control test passes, and the test citing `skill-entry-points/1`
FAILS because no entry points exist yet; `.runs/gate-tests.jsonl` holds a `fail` line for `skill-entry-points/1`. An
ERROR (import, syntax) or a passing citing test is a defect to fix before returning.

Return your report as text: the file's structure (functions, tests, what each asserts, mapped to the clauses of the
sentence), the run's result lines and the verdict line for `skill-entry-points/1`, every place where you had to read the
sentence (each with your reading), and any question.
