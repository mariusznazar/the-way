# Handoff to the reviewer of the whole change

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Ask the
human nothing. A question goes to the orchestrator in your report as `questions`. You are an agent
that did not make the change.

## What you review

- The worktree: `the root of the task's worktree` (the root of
  the-way for this change). It is read-only for you: change nothing in it.
- The range: base `aba5ee92a0734c2e775cc69662af669bf6455795` to head
  `ab2c8c801b2ba9170a00ed6056b8b7c56b062868` — three commits by the one author: `6867078` (a move
  of a part of `process-audit/audit_count.py` into `process-audit/record_items.py`, claimed to change
  no behaviour), `19f7003` (the code, the tests and three foundation entries) and `ab2c8c8` (the
  instruction texts). The whole change is one-author, no plan, no spec; the task did not move a pin.
- Your method: `task-cycle/review/SKILL.md` (`review-change`), the review of the whole change. Read it
  whole, and `task-cycle/review/whole_change.md` as it says; read a file it names only when the
  step that names it comes. The change itself rewrites parts of `task-cycle/review/SKILL.md`; review
  under the method as it stands at the base (`git show aba5ee92:task-cycle/review/SKILL.md`), and
  review the head's text of it as part of the change.
- The frozen task: `docs/task-cycles/audit-answers-contradiction-after-code/task.md` — read whole.
- The author's report (a set of claims to verify, not evidence):
  `docs/task-cycles/audit-answers-contradiction-after-code/reports/author-report.md`.
- Your report: `docs/task-cycles/audit-answers-contradiction-after-code/reports/review-whole-report.md`.
- Your directory for working copies: `.runs/review-whole/` of the worktree.

## The answers of the two questions at start

- Trust boundary: **yes**. `process-audit/audit_count.py` is the trust boundary of the part
  `process-audit`; the change adds `process-audit/record_items.py`, which reads the items of cycle
  records taken from git history (untrusted input), and the author wrote it into the part map's
  *Trust boundary*. Check crafted input at it: a record text shaped like the new marker of *Discarded
  attempt* or like an entry of *Review rounds*, a very long or very many entries, a marker inside a
  code fence, an item doubled, control characters in what a reason repeats. A crafted record must
  not give a wrong `yes` or `no`, a hang, an unbounded result or a crash.
- Irreversible operation: **no**.

## What to give particular attention to

These come from the author's report and the orchestrator's reading; they are for you to verify, none
is a finding.

1. **Coverage.** Every item of *To do* (1 to 6), every answer of *Questions to settle* (1 to 5) and
   every row of *Settlements to record* (rows 1, 2 and 4 are foundation entries, row 3 is code),
   met by the commits; fidelity to the task's wording (for example the four examples of review #100
   that give `unknown`, and the one reason `wpis rundy nie mówi, czy była sprzeczność`, which the
   task gives in Polish: check how the code and the tests word it against the task's *To do* 5).
2. **Foundation entries the author wrote:** WAY-403 (row 1), WAY-404 (row 4), a new paragraph of
   WAY-337 (row 2), and a line added to the part map's *Trust boundary* of `process-audit`, marked
   `the cycle's`. Compare each with the row and the question it carries and with the code; WAY-263
   grades a departure of a change from an entry it writes as Important.
3. **WAY-344** — the author reports a concern: it kept a missing item of `cycle.md` (such as
   `Discarded attempt` or `Review rounds`) as `unknown` with a reason naming the item and exit code
   0, not a line `Error:` with exit code 1, because records of earlier forms lack items. Judge from
   the full sentence of WAY-344 (its part on the command that counts the audit, a record read from
   git history and a field an earlier form never had) whether that reading complies, and give the
   author's evidence its due without taking it as settled.
4. **The move (WAY-365, WAY-385).** Verify that commit `6867078` changes no behaviour (the moved
   code against the old code), that the first commit that changes the code is the move, and the
   sizes: take them from your own runs as `whole_change.md` gives. `audit_count.py` stood at 3310
   lines and stands at 3143; the invariant `function-and-file-size` is marked violated and stays so;
   judge the structure of the change under WAY-385, WAY-363 and the method.
5. **The instructions.** The mark of the reviewer's blocking findings, the findings file, the entry
   of a round in *Review rounds*, the item *Discarded attempt* with its marker (the two paragraphs of
   `task-cycle/skill/SKILL.md`, `task-cycle/skill/reserved_return.md`, `task-cycle/record_template.md`,
   `process-audit/SKILL.md`): the forms must agree with each other and with what the code reads. The
   author reports it found no step that names the moment the cycle's leader writes the entry of a
   round; judge whether the task requires one.
6. **Tests.** The author wrote the new tests after the code and checked them by mutation; judge
   them against `guidelines/testing.md`, the existing tests it deleted or changed (named in its
   report) and the requirement that the four examples of review #100 give `unknown`.
7. **Search of the foundation (WAY-33).** The author searched once for the entries the change touches
   and did not read WAY-229 and WAY-260 and read WAY-162 and WAY-294 in part (its **Unread
   material**); you select your own foundation and settle whether any bears on the change.

## Selection of the foundation and the guidelines

You select your own, by "Reading the foundation" in `elements/common/way_of_working.md`, for the
parts `task-cycle`, `process-audit` and `decisions` (the change writes decisions), and read the
guideline files of those parts by `product-guidelines/reading.md` — for the-way's code:
`guidelines/coding.md` whole, `guidelines/coding-measuring-report.md` whole, `guidelines/testing.md`
whole. The task's *Decisions in play* are WAY-337, WAY-339, WAY-135 and WAY-263. Write the index of
your whole selection with your own run of `elements/common/decision_index.py` in your directory for
working copies and report how many decisions you read whole.

## Checks you may run

Focused checks only, in your own directory for working copies (a worktree of the head there):
`python -B gate/run_tests.py process-audit` and `python -B gate/run_tests.py task-cycle`, the
`foundation_check.py` command, and anything else a finding needs. **Do not run the product's full
gate** (`python -B gate/run_tests.py` with no directory): its run is the orchestrator's (WAY-160),
and it must wait for the day advisor's signal. Report each check with its command and exit code.

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

Write it to the path above as `review-change` gives it: its first line `PASS <sha>` or `FAIL <sha>`
(or `questions`), graded findings with their places in the code, the checks you ran, **Unread
material**, **Searches not found or unclear**, and the line on your working copies. Return the report's
first line, a one-line check result, and the report's path.
