# Handoff 01 — the one author of the whole change

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You
work for the orchestrator. Do not ask the human anything; questions go back to the orchestrator as a
report with status `questions`. Never label your answer as the human's approval.

## Where you work

- Worktree (your working directory, the process root): `the task's worktree root`
- Branch: `task/private-path-patterns-in-code`, base `73b51db53716f5a7656ae73f327c18e30e9fd5c5` (target branch `foundations`)
- Write only in this worktree. Do not run `git add -A`, `git add .` or `git commit -a`; add by path.
  Commit messages in English, as the commits of this repository read.
- Code, identifiers, docstrings and comments in English. Text the code prints or inserts into a
  document, and literals it matches on, stay as they are.

## What you make

The whole change as the one author. The method of your stage is `task-cycle/change/SKILL.md` in
this worktree: read it whole and follow it. Read a file it names only when the step or variant that
names it comes. Your variant is "the whole change as the one author".

## The task

The frozen task is `.runs/task-cycles/private-path-patterns-in-code/task.md` in this worktree. Read
it whole. Its items 1–6 of *To do*, its *Acceptance criteria*, the five answered questions and the
three rows of *Settlements to record* are the change. The task is final: its answers bind you; an
answer you hold wrong goes into your report as a concern, not into the code.

Answers of the cycle's step 4 that bind you:

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. The name and argument form of the new command, the way it reads the file
  names out of the sentence of the invariant its argument names, and the exact patterns are how to
  make what the task settles: make each choice, the smallest reversible reading that fulfils the
  task, and name it in your report. If you meet a choice the task and the foundation do not settle
  and that changes what the product's users get, do not code it: return with status `returned` and a
  report holding the choice, where it shows, the ways open and what you found.
- Reserved choice: none (Python, standard library only; `.python-version` declares 3.14).

## What you read

Foundation entries, each whole (a decision runs from its `###` heading to the next heading, an entry
of another file from its `##` heading to the next):

- `foundations/decisions.md`: WAY-309, WAY-320, WAY-321, WAY-16, WAY-34 (the task's *Decisions in
  play*); WAY-61, WAY-62, WAY-63, WAY-69 (how an invariant's method and test are written and cited);
  WAY-308 and WAY-316 (what the cleaning of a record's copy and the image check do with the script's
  neighbours).
- `foundations/invariants.md`: `tracked-file-private-paths`; the entries it is linked to.
- `foundations/part_map.md`: the entries `task-cycle`, `installation`, `gate`, `elements-common`
  and `test-runner-command`; `foundations/glossary.md` whole (it is short).

Files you change or run, each whole before you change it: `task-cycle/private_paths_check.py`,
`task-cycle/test_private_paths_check.py`, `task-cycle/test_tracked_files_private_paths.py`,
`installation/README.md`, `gate/run_tests.py` (read only, to see how a `test_*.py` is found),
`elements/common/foundation_check.py` (read only, to see how a test citing an invariant is found).
There are no product guidelines in this repository (`guidelines/` does not exist; the task's
question 5 settles that the cycle does not wait for them).

You write the foundation entries of the task's *Settlements to record* (rows 1–3) in the same
change: follow `task-cycle/skill/foundation_step.md` (read it whole) and the skill of each element
you write (`the-way-record-decision`, `the-way-record-invariant`; use the repository's project
skills with the `the-way-` prefix), each of which selects the reading its entry needs. Run the
foundation check after writing an entry as the skills give, with `--skip-test-citations` only for
the run right after the entry is written and before its test exists (WAY-321). The invariant
`tracked-file-private-paths` keeps method `test`; its sentence changes as the task says (question 1
and item 4–5: the files the sentence names are the product-readable list).

## Tests and checks

- Test first where it fits, as the method says. The invariant's test is seen failing once and then
  passing; record both runs as command and exit code.
- Fixtures that hold an absolute path or a note link are assembled from pieces, as
  `task-cycle/test_tracked_files_private_paths.py` does, because a tracked file with such a text is a
  finding of the invariant.
- Focused checks to run yourself: `python -B gate/run_tests.py task-cycle`,
  `python -B gate/run_tests.py installation`, `python -B elements/common/foundation_check.py` (from
  the root). Do not run the whole gate (`python -B gate/run_tests.py`): the orchestrator runs it.
- The acceptance criteria use the tracked files of the product loop2 at a commit you have no access
  to. Show that the rules behave as the criteria say on made-up files that hold the same shapes
  (the five shapes of false hits named in *Need*, the real `C<colon>\new\dir` in a `.py`, the Git Bash
  example `/c<slash>...`, `zob.[[Notatka]]`, `C<colon>\n` standing alone, `s<colon>\n\n`, `"... s<colon>\nWynik"`), and say in
  your report that the loop2 count itself was not run.
- Before you commit, run your own-work check as the method gives it and put it in the report.

## Do not

- Do not touch loop2 or any repository other than this worktree (the task's *Out of scope*).
- Do not change WAY-309's rule about the cycle's copy and the request description: the three rules
  of items 1–3 change what the script counts; the copy of the record and the description are checked
  with links in every file, as today.
- Do not write a path of a private note or a user's disk in any tracked file.

## Report

Write the full report to `.runs/task-cycles/private-path-patterns-in-code/reports/01-author-report.md`
(under the process root), as `task-cycle/change/SKILL.md` gives, including **Searches not found or
unclear** (`none` is an answer; a missing section is not), the reaches beyond this handoff, the
choices you made, each check with its command and exit code, and your own-work check. Return your
status, your commits, a one-line check result naming what failed or did not run, and the report's
path. You will be resumed for the fix of findings and for the return step; commit your work before
you return.
