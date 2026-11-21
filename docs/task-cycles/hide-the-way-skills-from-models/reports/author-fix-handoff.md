# Handoff to the one author — the fix of the Minor findings of the review of the whole change

You are the author of the change (your first handoff: `reports/author-handoff.md`; your report:
`reports/author-report.md`). The review of the whole change by an agent that did not make it passed
(`PASS 7d063ef278748884de28577f582b2ab0767d068d`) and lists six Minor findings within the task. They are
fixed before the request opens, once (one fix, one review of the fix).

- Your variant of `make-change`: "the fix of a review's findings". Read `task-cycle/change/SKILL.md`
  in the worktree again as it tells you and `task-cycle/change/fix.md` whole.
- The findings file, in the reviewer's words: `reports/review-whole-findings.md` (beside your report, in
  `.runs/task-cycles/hide-the-way-skills-from-models/reports/`). No blocking finding; no finding is marked
  outside the task's scope.
- Worktree, branch and your directory for working copies are as in your first handoff (`.runs/author/`;
  the first paragraph of "Working copies" there binds you again, word for word).
- The range of the fix starts at the reviewed head `7d063ef278748884de28577f582b2ab0767d068d`.
- Your report for the fix: `.runs/task-cycles/hide-the-way-skills-from-models/reports/author-fix-report.md`.
  It is read by `task-cycle/remarks_check.py`; if the harness refuses the write, return it whole.
- Not yours: the foundation step's entries stay the rows' meaning; where a fix changes the wording of
  WAY-127, the invariant or the environment fact, follow the elements' skills for form, and keep the
  clause on the list of paths with what Minor 3 asks for. `cycle.md` and the other files of the record are
  not yours to read. Do not run the whole gate; run the focused checks of the directories you change and
  `python -B elements/common/foundation_check.py`, and run the generator without `--write` to see the entry
  points current (with `--write` if you change the generator's text, then commit the regenerated files).
- The reviewer's findings 1–6 each get a fix or, where you hold one wrong, an answer with evidence (as
  `fix.md` gives). The choice of wording is yours: qualify in Claude Code what Minor 1 lists; give
  the invariant's test the check Minor 2 names; point the paragraphs at the entry point's list first
  (Minor 3); say in `project-level/lead/skill/SKILL.md` that the brief of a dispatched agent carries the
  file's path (Minor 4); make the test's docstring and message and `AGENTS.md:19` true (Minor 5); add the
  two parts to WAY-127's *Scope* (Minor 6).
- Also correct, in your fix report, one claim of your first report that the reviewer found wrong: the
  failing run of the invariant test listed 23 problem lines, not 46 (`reports/review-whole-report.md`,
  last paragraph of the reviewer's return: the claim is wrong, the evidence holds). Say which file of
  `reports/` you checked it against.
- Commit by path, messages in English. Return the status, the commits, a one-line check result with each
  command and exit code in the report, the **Unread material** and the **Searches not found or unclear**
  sections, and the own-work check.
