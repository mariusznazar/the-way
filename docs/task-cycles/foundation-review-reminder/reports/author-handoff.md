# Handoff — the one author, whole change

Stage: the change of one task, made without a plan by one author, with its foundation entries and its own-work check, returning before review.

Variant of `make-change`: the whole change as the one author.

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the orchestrator. Your questions go to the orchestrator, in your report, never to a human; the orchestrator answers them from the task, its sources, the foundation and the code. Nothing the orchestrator answers is a human's approval. You return at your boundary: you do not start a review, a gate run or a request.

## Where you work

- Worktree, which you work in and from whose root you start every command: `the task's worktree`, branch `task/foundation-review-reminder`, base `ff88ca3bc6beae07dbe1ee5adb1792773d28bcac` (the head of `foundations` on 2026-11-15). This repository is the-way itself, no product pins it here: read every file from this worktree, never from `the main checkout of the repository`.
- Your directory for working copies: `.runs/author/` of the worktree.
- Your report: `docs/task-cycles/foundation-review-reminder/reports/author-report.md`.
- Git: commit on the task branch only; message in English, in the form of the recent commits (`git log --oneline -10`); `git add` each file by its path, never `git add -A`, `git add .` or `git commit -a`; several commits are fine, one for each coherent step; no push, no merge, no tag.

## The method

Read whole `task-cycle/change/SKILL.md` and follow it. Read a file it names, and `task-cycle/skill/foundation_step.md` for the foundation step, when the step that names it comes; read no other file of the method at the start. The foundation step writes the rows of the task's *Settlements to record*; follow the `SKILL.md` of an element, at the path `foundation_step.md` gives, when you write an entry of that element. Your report keeps for each entry one sentence of its meaning in English and one in the task document's language (Polish), marked `row <n>`, `projected` or `the cycle's`, as `foundation_step.md` gives.

## The task

The frozen task, which you read whole because you make the whole change: `docs/task-cycles/foundation-review-reminder/task.md`. It is in Polish; code, comments, commit messages and every text you write into the repository are in English (the-way's own language). Its five points of *To do* are your change; its *Settlements to record* rows 1–5 are the entries or the places you write whole; its *Questions to settle* hold the answers that bind and the options not chosen. *Out of scope* binds.

The task names no spec and no plan; it settles its design choices. A choice of how to make what it settles — for example how `review_reminder.py` tells a tag that does not exist from an error of git, which a message of git may not tell reliably where git's messages are localised — is yours: make it, name it in your report and say what you rejected.

## Answers of the orchestrator at the start

- Open design choice: none. Reserved choice: none.
- Trust boundary: no. Irreversible operation: no. The change touches no file the part map lists as a trust boundary and holds no operation that cannot be undone.
- The change reaches these parts of `foundations/part_map.md`: `decisions` (`foundations/decisions.md`), `task-cycle` (`task-cycle/**`), `foundation-review` (`foundation-review/**`) and the root `README.md`, which the map leaves out on purpose.
- Where the task's *Decisions in play* says "zmiana w tym zadaniu", that is the change you write; a decision it marks "bez zmiany" you leave as it is.
- Of the task's text, the ready phrase for the reminder is yours to write: the task gives what it says and in which two forms (point 1), not its words.
- The product's backlog of the-way is the entry `tasks` under `the-way` in the user's locations file, read as `project-level/backlog_place.md` gives; the step 13 text you write tells the orchestrator to read it as that file says, and tells nothing about where on the user's disk it lies. No path of the user's disk and no title or link of a private note enters any committed file (WAY-308): the task's *Context* names the author's notes, which you do not copy.
- The skill `foundation-review` is named by its entry point in `.claude/skills/` and `.agents/skills/`. If a change of yours alters the `description:` line of `foundation-review/SKILL.md`, run `python -B agent-instructions/skill_entry_points.py --write` and commit what it writes; if it does not alter it, run nothing.

## What you read

Foundation entries, by identifier, in `foundations/decisions.md` unless stated:

- The decisions the change rewrites, whole with their *Rationale* and *Rejected*: WAY-24 and WAY-300.
- The decisions the task names, whole: WAY-140, WAY-161, WAY-107, WAY-22, WAY-36, WAY-293, WAY-328, WAY-344. Of the others the task names, WAY-329 is withdrawn; its rule stands in `project-level/task_line.md`, which you read only if the text you write touches how a task's line is found.
- The decisions on the form of an entry and of the log, whole: WAY-05, WAY-18, WAY-19, WAY-33 (the search of the whole foundation after you settle an entry), WAY-150 and WAY-12 (how a decision is held by a test).
- The invariants of `foundations/invariants.md`, each whole: `script-language`, `script-imports`, `script-subprocesses`, `test-method-citation`, `skill-entry-points`, `cross-part-imports`, `tracked-file-private-paths`, `return-step-record`.
- The entries of `foundations/part_map.md` for `decisions`, `task-cycle` and `foundation-review`, and the whole `foundations/glossary.md`.
- The decisions template, rules and examples as `elements/decisions/skill/SKILL.md` gives them, since you write two decisions.

Files the change touches, read whole before you change them: `task-cycle/review_reminder.py`, `task-cycle/test_review_reminder.py`, `foundation-review/SKILL.md`, `foundation-review/weak_points.md`, `foundation-review/proposals.md`, `foundation-review/with_the_human.md`, the paragraph of `task-cycle/skill/SKILL.md` that opens with "Before you write the description, count the merges" and the passage of `task-cycle/skill/request_template.md` that begins "Where the count of `SKILL.md` step 13 reads `reminder: yes`" with the line of its *How to merge* summary that mentions the reminder, `README.md` where it speaks of the reminder, and `elements/decisions/template.md` at the questions "Where it goes", which the new group of non-decisions is told by.

Guidelines: none to read. WAY-328 departs, for the-way's own code and tests, from the coding and testing guidelines of a product, so a change in a part of the-way waits for none.

You select no other part of the foundation to read at the start; where you meet something the task or the foundation does not settle, reach for it by a search for an identifier or a word and a read of the passage, and name each such reach in your report.

## Checks you run

Focused checks only. The product's gate, `python -B gate/run_tests.py` without a directory, is the orchestrator's, and the person who requested the cycle has asked that no full gate run before a signal `start` of the day's advisor: you run none.

- `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py elements/common` before you return, and `python -B elements/common/foundation_check.py` for the foundation entries you write.
- The first failing run of the test you write or change, before the code it holds, and its passing run after; both in your report with their command and exit code.
- `python -B task-cycle/request_check.py` and the tests of the check, if you change the template's text in a way its form check reads.
- The own-work check `make-change` gives, in your report.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## What you return

Your status, your commits, a one-line check result naming what failed or did not run, and the path of your report. In the report: your checks with command and exit code, your reaches beyond this handoff, your **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), your **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), your working copies, and the own-work check.
