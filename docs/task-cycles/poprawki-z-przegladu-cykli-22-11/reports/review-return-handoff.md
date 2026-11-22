# Handoff — the review of the return step's commit, `review-change`

You are a fresh reviewer of a task cycle of the-way, an agent that made none of the change. Work from
the root of the worktree `the worktree root` (branch
`task/poprawki-z-przegladu-cykli-22-11`); the-way is the product itself, no `.the-way`
submodule, every path below is relative to that root. You write nothing in the repository.

## Delegation

The person who requested this cycle has delegated every intermediate choice to the cycle's
orchestrator; nothing the orchestrator says is that person's approval; the person reviews the
finished pull request. You never ask the person anything.

## Method

Read `task-cycle/review/SKILL.md` whole (`review-change`): the review of the return step's commits,
which its section 1 and 2 give — against the task and the foundation entries the return step writes
or corrects. For a review that is no review of the whole change, you read what this handoff names;
you reach for more selectively and name each reach in your report.

## What is reviewed

- The range: base `41921006168c95b1de449ea546fab2271ec815e9`, head
  `fb60dc7d8578db8372a384e7fecf711459b169c9` (`git diff 41921006..fb60dc7d`, `git log`; one
  commit, two files: `task-cycle/skill/planning.md`, `instruction-files/SKILL.md`). Confirm that
  `git rev-parse HEAD` is that head.
- The return step is the stage where the one author compares the foundation entries and the part
  map with the code and corrects what no longer matches (`task-cycle/skill/return_step.md`: read it
  whole). Its report: `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-return-report.md`,
  a set of claims to verify, not evidence. Judge whether the two corrections it made are right and
  sufficient, and whether the claims "no other mismatch found, nothing else to write" hold for the
  entries the whole change (base `2a2f4106c216c0fef4e68b7ed8bd5728ae2660ae`, previous head
  `41921006`) writes: WAY-255, WAY-25, WAY-136 (edited), WAY-418 (new) in `foundations/decisions.md`,
  the templates and skills of `decisions`, `part-map`, `environment-facts`, the part-map entries of
  the touched parts (`foundations/part_map.md`), the sentences about the scripts in
  `instruction-files/SKILL.md` and `installation/README.md`.
- The task: `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md`, read whole; its quoted
  wordings were accepted by the human word for word. The change before the return step was
  reviewed (the whole change and its fix both reached PASS); do not review it again beyond what
  the return step's corrections touch or what a mismatch with the foundation needs.
- Trust boundary: yes (`task-cycle/gate_times.py`, `instruction-files/check_instructions.py`);
  the return step's commit touches neither file.
- The one Minor finding left unfixed by design: the comment at
  `instruction-files/check_instructions.py:454` writes `'''` for the shell idiom; it goes to the
  request's list; do not list it again as a finding of this review unless it bears on this range.

## Working copies and what you do not read

Your directory for working copies is `.runs/review-return/` of the worktree. The first paragraph of
"Working copies" of `task-cycle/skill/SKILL.md` binds you: a copy only in that directory, removed by
its full path before you return, your report says where each stood and that it was removed; a
probe's input and command that shows a finding go into `reports/` beside your report, and your
finding names that path. The files of the cycle's record directory other than those named here are
not yours to read.

## Your report

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/review-return-report.md`; its first line
`PASS <sha>` or `FAIL <sha>`; the sections `review-change` gives, **Unread material**, **Searches not
found or unclear**, each reach beyond what this handoff names and the line on your working copies. If
the harness refuses the write, return the report whole as your answer. Return the first line, the
changed files with their line counts, a one-line check result and the report's path.
