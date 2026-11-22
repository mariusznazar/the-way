# Handoff — the review of the whole change, `review-change`

You are the reviewer of the whole change of a task cycle of the-way, an agent that did not make it.
Work from the root of the worktree `the worktree root`
(branch `task/poprawki-z-przegladu-cykli-22-11`). The-way is the product itself: no `.the-way`
submodule; every path below is relative to that worktree root, and the process files you read are
the ones of that worktree. You write nothing in the repository; you work read-only, and make your
working copies as the paragraph below gives.

## Delegation

The person who requested this cycle has delegated every intermediate choice to the cycle's
orchestrator, who answers your questions from the task, its sources, the foundation and the code.
Nothing the orchestrator says is that person's approval. The person reviews the finished pull
request, not the steps before it. You never ask the person anything.

## Method

Read `task-cycle/review/SKILL.md` whole — `review-change`, the review of the whole change — and
`task-cycle/review/whole_change.md` when that skill sends you to it; other files it names only when
the step that names them comes. You alone select your own foundation and guidelines, as that skill
gives.

## What is reviewed

- The range: base `2a2f4106c216c0fef4e68b7ed8bd5728ae2660ae`, head
  `ae37fca3310ce6efe7e7939413b8b7a1205b0ead` (`git diff 2a2f4106..ae37fca3`,
  `git log 2a2f4106..ae37fca3`; nine commits, 26 files). Confirm that `git rev-parse HEAD` is that
  head before you go on.
- Route: one author, no plan, no spec, no slices — the review of the whole change is the only
  review. Every commit of the range is yours to judge.
- The frozen task, read whole: `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md`
  (Polish; the quoted wordings are English and were accepted by the human word for word). Check the
  coverage of every point of its *To do*, every row of its *Settlements to record*, and the fidelity
  of the change to the quoted wordings; the four questions of its *Questions to settle* are
  answered in it.
- The author's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-report.md`.
  It marks each foundation entry `row <n>` (rows 1–3: sentences of WAY-255, WAY-25, WAY-136; row 4:
  the new decision WAY-418) and lists its concerns; judge each yourself. The author names these as
  doubtful: (a) `task-cycle/skill/planning.md`, the file that lists what each slice's handoff
  carries, was left unchanged though point 3's quoted wording says "the handoff of each later slice
  lists the tests the plan leaves failing"; (b) `AGENTS.md`, one line reworded, outside the 13
  points; (c) a *Rejected* row of WAY-255 whose source is the task's *Context* point 1; (d)
  `task-cycle/change/walkthrough.md` not read, since the author judged that no behaviour a user sees
  in a running product changes — `task-cycle/change/SKILL.md` ("Before you finish a change that
  alters behaviour a user sees in the running product — a screen, an answer of an API, a command
  in a terminal, data the product shows") says when it is read; judge whether the changed
  scripts' command-line behaviour makes it apply and, if so, whether the author's own checks
  hold. The grade and the scope of every finding are yours.

## Answers of the orchestrator's start

- Trust boundary: **yes** — the change touches `task-cycle/gate_times.py` and
  `instruction-files/check_instructions.py`, both named as trust boundaries in
  `foundations/part_map.md`. Check crafted input at them (a crafted command line, path, file name,
  link, `.gitignore`, output), as `review-change` gives for a trust boundary.
- Irreversible operation: **no**.
- Tests failing before the change: none (the base's CI run was green on both checks).
- The task moved no pin; no project plan; the gate is run by CI later, not by you and not by the
  author. Do not run `python -B gate/run_tests.py` with no argument; run the focused checks your
  review needs, in your working-copy directory where they make files.

## Working copies

Your directory for working copies is `.runs/review-whole/` of the worktree. The first paragraph of
"Working copies" of `task-cycle/skill/SKILL.md`, word for word:

> An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
> clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
> directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
> in the system's temporary directory, in the scratch directory of a session or in the main checkout
> of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
> itself under its session's directory is moved into the agent's directory and the original removed,
> except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
> says, to the place the product's foundation settles for screenshots, and into the agent's directory
> only where no such place is settled. The files that a product's own tools and tests make by
> themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
> each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
> `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
> the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
> all the same and names in the report the remainder, with its full path and the reason it stayed. It
> removes a copy, as any directory, by its path written out in full in the command, never through a
> shell variable: an empty variable turns the removal on the directory the shell stands in.

The input and command of a probe that shows a finding go into `reports/` beside your report, and
your finding names that path with its evidence.

## What you do not read

`cycle.md` and the other files of the cycle's record directory
(`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/`) — other agents' handoffs, reports and
findings — are not yours to read, except the files this handoff names: the frozen task and the
author's report, and the report path below, which you write. Do not read the transcripts of other
sessions. Make no change to the author's `reports/author-decision-index.md`.

## Your report

Write it to `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/review-whole-report.md`
(the name starts with the role, since Claude Code refuses a subagent's write of a file named
`report…`; that file is the input of the cycle's scripts — `task-cycle/remarks_check.py` reads it —
the case the harness's note leaves open; if the write is refused, return the report whole as your
answer). Its first line is `PASS <sha>` or `FAIL <sha>` as `review-change` gives. It holds what
that skill gives, and, in the form it gives, **Unread material** (what this handoff names, or your
own selection, that stayed unread or was read in part, or `none`), **Searches not found or
unclear**, the number of decisions of your index you read whole, each reach beyond your selection
and the line on your working copies. List the Minor findings within the task's scope apart, as the
skill gives, since the cycle fixes them before the request opens. Return the report's first line,
the changed files with their line counts, a one-line check result naming what failed or did not
run, and the report's path.
