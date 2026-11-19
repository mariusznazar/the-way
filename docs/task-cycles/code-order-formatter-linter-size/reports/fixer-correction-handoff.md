# Handoff - the correction for the human's remarks (stage: make-change, a correction for the human's remarks)

## Delegation

The human's remarks on the open request are binding; the coordinator of the day wrote them on the human's behalf. You never ask the
human; a question goes back to the orchestrator in your report. Never label an answer as the human's approval beyond what the
remarks say.

## Where you work

- The worktree: `the worktree's root` (branch `task/code-order-formatter-linter-size`).
  Work from its root. Your base, the current head of the request: `34d9970e0a7a130e6e0488c553170fbe7a6ca8a9`. Your range runs from there.
- Your directory for working copies: `.runs/fixer-correction/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/fixer-correction-report.md` (an ordinary report file the cycle requires; write it).
- You are resumed with your earlier context (the fix round of the review of the whole change); the method is the same:
  `task-cycle/change/SKILL.md` (`make-change`), variant "a correction for the human's remarks". Read it again at the sections the
  variant names.

## The remarks (binding), word for word in `.runs/task-cycles/code-order-formatter-linter-size/reports/correction-1-remarks.md`

What they ask you to change, and nothing else:

1. **The four test names in `process-audit/test_audit_count.py`** that still say "entry" for an item of a record's list
   (the remarks name the lines 545, 556, 1428 and 4986 as they stood at the head `34d9970e`; find them by the word, since
   the lines may have moved): rename them as the eleven tests in `process-audit/test_record_items.py` were renamed (read
   `git log -p -S` of those names, commit `462add5d`, for the words the cycle chose: an item of a list under the record's items is
   a "sub-item", a line of such a list an "item"). Only the names, and the comments or strings that name them; no assertion, no
   expected value changes (WAY-233). Keep every line `decision:` and `invariant:` of those tests as it is (WAY-03: the request
   names the tests it renames). Find by search every reference to the old names (`git grep`), in the file and outside.
2. **The relation of the size decision to the formatter decision**: add to the *Relations* of WAY-385 in `foundations/decisions.md`
   the relation to WAY-382, since the size decision counts lines on the code as WAY-382's formatter leaves it. The template
   (`elements/decisions/template.md`, read the rules on *Relations*) allows two types, `derives from` (a higher decision this one
   serves) and `narrows`; choose the one that fits, say why in your report, with the other way rejected and its cost if wrong, and
   do not change the binding sentence of WAY-385 or any other field (WAY-07: edit in place). Read `elements/decisions/skill/SKILL.md`
   as the foundation step gives for an entry, and run `python -B elements/common/foundation_check.py` (exit 0 required).

The remarks let through, with no change: the brackets of the 14 `except` lines (Python 3.14 only); the unproven fix of the flaky test;
the installer function `plan` at 109 lines. Touch none of them.

Format every changed `.py` file with `<ruff> format --config ruff.toml <file>` and check it with
`<ruff> check --config ruff.toml --ignore-noqa <file>` (`<ruff>` is
`the Ruff of the quality environment of the main checkout`). Run `python -B gate/run_tests.py process-audit` and
`python -B gate/run_tests.py elements/part-map` (focused runs; wait for each to finish) and `python -B elements/common/foundation_check.py`.
Do NOT run the full gate. Commit by path with English messages, one commit for the test names and one for the relation.

## Working copies (word for word)

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

Your directory is `.runs/fixer-correction/`.

## Your return

Status, your commits, a one-line check result naming what failed or did not run, and the report's path. The report holds, for each of
the two changes, what you changed with its evidence (commands with exit codes), the choice of the relation type with the way
rejected and its cost if wrong, the tests altered that hold a decision or an invariant (WAY-03), the own-work check (WAY-164), your
**Unread material**, **Searches not found or unclear**, reaches and working copies with their removal.
