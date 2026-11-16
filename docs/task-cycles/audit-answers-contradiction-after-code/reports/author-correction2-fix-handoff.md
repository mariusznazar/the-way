# Handoff to the one author — the fix of the review of correction 2

The review of your correction returned `FAIL 17065c8b9b2349b4f5953ac98a15285e3d221787`
(`reports/review-correction2-report.md`). The two blocking findings, I-1 and I-2, stand in
`reports/review-correction2-findings.md`, in the reviewer's words; fix them with `make-change`, variant
"the fix of a review's findings", on the same branch from head `17065c8b`. Your directory for working
copies: `.runs/author-correction-2-fix/`. Your report:
`.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-fix-report.md`.
Delegation as before: ask the human nothing, do not run the product's full gate.

- Fix I-1 and I-2 as the findings give, or by a way you hold better with its reason. Both are wording of
  WAY-405 and WAY-404 and their comments; no code change is asked (the code's behaviour is what the rule
  must say). I-1: say, in all five places the finding names (WAY-405's binding sentence and its "holds no
  other", its *Verification*, the docstring in `process-audit/audit_count.py` and the one in
  `process-audit/record_items.py`), that the text is read for a second `reason: ` followed by a word in
  backticks, so that a second reason written without backticks or in other words is not read, and that a
  later line `- reason: \`budget\`` (a word that is no marker, in backticks) gives unknown; correct the
  author's own test `test_a_later_line_with_no_marker_is_a_detail_even_where_it_names_a_second_attempt`
  where it cites a sentence it does not hold, and add the test the finding names (probes B3, B4: a second
  `reason: \`budget\`` gives unknown). I-2: qualify WAY-404's *Verification* clause so it holds for the
  record the code answers `yes`, or name the doubled item *Discarded attempt* among what a yes of the item
  does not stand over, and add a subtest for the doubled item to
  `test_a_yes_stands_over_an_unknown_wherever_the_unknown_comes_from` (rename the test if its name then
  says more than it holds).
- Search the repository for any other place that says the same wider or narrower sentence (the template's
  item, `process-audit/SKILL.md`, `task-cycle/skill/*.md`) and bring it in line (WAY-33).
- The Minor finding M-1 of that report is **not** to be fixed: the cycle carries it to the request's
  list. Do not change code, and do not widen beyond I-1 and I-2.
- Run the affected focused checks (`python -B gate/run_tests.py process-audit`, `... task-cycle`,
  `python -B elements/common/foundation_check.py` without `--skip-test-citations`), each with command and
  exit code, a command through a pipe included. Commit by path, messages in English.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## The report

As `make-change` gives it for a fix, with **Unread material**, **Searches not found or unclear**, the
own-work check and the fix's range from `17065c8b9b2349b4f5953ac98a15285e3d221787`. Return its status,
commits, a one-line check result and the report's path.
