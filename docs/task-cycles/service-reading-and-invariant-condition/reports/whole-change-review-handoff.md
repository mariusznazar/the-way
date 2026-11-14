# Handoff to the reviewer of the whole change

Delegation: the person who requested this cycle delegated intermediate choices to the orchestrator; no answer here is that person's approval. You may not ask the human; questions go to the orchestrator in your report.

Worktree (read from here, from its root; change nothing): `the worktree's root`
Method: `task-cycle/review/SKILL.md` of the worktree, read whole; a file it names only when the step or variant that names it comes. Your variant: the review of the whole change.

Range to review: base `0e1cd3cd804433f7a82ffb631e96917ef74c1040` to head `8680824` (two commits by the one author: `19efdfd`, `8680824`). Changed files (added / removed): `foundations/decisions.md` 68/31 in WAY-80, WAY-84, WAY-60, WAY-35 and so on (99 lines changed in all), `foundations/invariants.md` 10/0, `elements/common/test_elements_pending_marker.py` 44/0 (new), `elements/common/test_foundation_check.py` 16/0, `elements/environment-facts/template.md` 44 changed, `elements/environment-facts/skill/draft.md` 14 changed, `elements/invariants/template.md` 6 changed, `README.md` 7 changed.

Frozen task, read whole: `.runs/task-cycles/service-reading-and-invariant-condition/task.md` — the task the change carries out; check every item of *To do* (1-8), every row of *Settlements to record* and every answer of *Questions to settle*, and the fidelity of the change to them (the settlements give the wording of the three decision changes). No spec, no plan (one author without a plan).
Author's report: `.runs/task-cycles/service-reading-and-invariant-condition/reports/author-report.md`. Slices: none.
Answers of step 4: trust boundary: no; irreversible operation: no. The task did not move the pin (the-way itself).

You select your own foundation and guidelines by the parts of the change (`elements/common/way_of_working.md`, "Reading the foundation"); the parts are `decisions`, `environment-facts`, `invariants`, `elements-common`, and the files `README.md`. Beyond your selection, the orchestrator points at what the author's report says it left unread: WAY-07, WAY-33 and WAY-328 as entries, the glossary entries of the terms it used and `examples.md` of the invariants and facts elements; judge the change against them. The author's own report names three choices beyond the task's letter: WAY-80's *Rejected* clause now saying "a host or a service", an example each added to the *Verification* pairs of WAY-80, WAY-84 and WAY-60, and WAY-80's binding paragraph now holding five sentences where the decisions template says one to three — judge each as the method gives, and state whether the task or the foundation allows it. Judge too the choice to put the new test at `elements/common/test_elements_pending_marker.py` and the invariant's *Part* list.

Checks: run the focused ones you need (`python -B gate/run_tests.py elements/common`, `python -B elements/common/foundation_check.py`); you do not run the full gate. A negative control of the new invariant's test is yours to run on a copy or by a change you restore, never committed.

Report: write it to `.runs/task-cycles/service-reading-and-invariant-condition/reports/whole-change-review-report.md` as the method gives, its first line `PASS <sha>` or `FAIL <sha>`, with the sections **Unread material** (for your own selection) and **Searches not found or unclear**, each check with its command and exit code, and for each finding its grade, scope and a full statement. Return the first line, the checks, and the path.
