# Handoff — fix of the findings of the review of the whole change (`make-change`: "the fix of a review's findings")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Your questions go to the orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`,
  HEAD `a5ebc88`. The fix's range starts at `a5ebc88`.
- Method: `task-cycle/change/SKILL.md` whole, then `task-cycle/change/fix.md` whole (you are a fresh agent: the findings span several slices, so no executor
  is resumed).
- Findings file (the reviewer's words): `docs/task-cycles/weekly-process-audit/reports\review_whole_findings.md`.
  It holds 5 blocking findings (B1–B5, all Important), then the Minor findings of the review of the whole change within the task, then the Minor findings of
  the slice reviews that review graded. The full review is `...\reports\review_whole_report.md` in the same directory (read it only where a finding needs the
  context).
- Report path: `docs/task-cycles/weekly-process-audit/reports\whole_fix_report.md`.

## What to fix

- Fix **every blocking finding and every Minor finding of the file** (the Minor findings within the task are fixed in this request, WAY-161). A Minor
  finding that you hold wrong, or that cannot be fixed without changing what the task settles, you answer in your report with evidence; do not silently skip it.
- Orchestrator's notes on the blocking findings (what the cycle decided; where your reading differs, say so in the report):
  - **B1** (the working time and the wait for tools are `unknown` in every cycle, because the call that runs `cycle_stages.py` at step 12 has no result yet): the
    fix belongs to the reader (`task-cycle/cycle_stages.py`) and, if you need it, one sentence of step 12 of `task-cycle/skill/SKILL.md`. Choose the smallest
    sound rule (for instance: the last call of the live session that runs this script itself is no wait and is no unknown call, said in the docstring),
    test it on a transcript whose last call has no result, and show on this very session (id `b065500f-249b-4808-a8bf-172d19a2724a`, run with
    `--output` outside the repository) that the totals are no longer `unknown` for that reason.
  - **B2** (`files_named` drops a findings path written at the end of a sentence): fix the extraction so that trailing sentence punctuation is no part of a name;
    a test for each ordinary ending (full stop, comma, closing backtick, bracket, quote).
  - **B3** (nothing leads the widening of the list of classes): the skill leads it — where a problem fits no class, with the human's yes the session adds a
    class (name, meaning, the date it is added) to the register's *Classes* table, in the user's register and never in a repository; the template and the skill say
    so in one voice; what the skill says about not touching the register is narrowed to the rest of the register. The command already refuses a problem whose
    class is not in the list; make the skill say how that shows in the result and what the session does.
  - **B4** (the part map records no trust boundary for `task-cycle/cycle_stages.py`): the entry of `task-cycle` names it, written through the project skill
    `the-way-update-part-map`; nothing else of the part map changes. The foundation check must report 0 errors.
  - **B5** (the skill and the result define a series more broadly than WAY-338): state the series as the code computes it and as WAY-338 says it, once, and cite
    only what the decision says; the conservative computation stays.
- **Minor findings that touch the decisions** (the glossary words "issue" and "series"): the return step decides about glossary entries after this fix;
  here fix only a sentence a reader would read wrongly for lack of one, as the finding says.
- Keep every lesson of the earlier trust-boundary reviews: no backtracking pattern, no unguarded conversion, every cell through `cell()`, size caps, a failure of
  one cycle is `unknown` for that cycle. Do not weaken a test to make a fix pass.
- Nothing outside the files the findings name; the target branch's files stay as they are. Commit with `git add <paths>`, messages in English; several
  commits grouped by concern are fine.

## Checks (each as command and exit code in your report)

`python -B gate/run_tests.py process-audit`, `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py`, `python -B gate/run_tests.py elements/part-map`,
`python -B agent-instructions/skill_entry_points.py` (lists nothing to create or change; where you change `process-audit/SKILL.md` the entry points are
generated again with `--write` and committed), `python -B elements/common/foundation_check.py`,
`python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`, and a run of `process-audit/audit_count.py` with stdin closed on a temporary
locations file naming this worktree and a temporary register and results directory. Long commands (a directory of the gate takes a minute or more): run them in
the background and wait in stretches under four minutes. Do not run the full suite: the cycle runs it.

## Report

As `make-change` gives: status, commits, a one-line check result, questions, concerns, each reach beyond this handoff, **Unread material**,
**Searches not found or unclear**, the own-work check, and a table of every finding of the file (B1–B5, each Minor) as fixed (commit), held wrong (evidence)
or left (reason).
