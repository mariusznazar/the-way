# Handoff — review of the whole change, `define-project` in the shape of WAY-256

## Delegation

Mariusz asked the orchestrator to take this task through its cycle; the orchestrator dispatches
this review. You did not make the change. You ask no human; questions go back to the orchestrator
(first line `questions`).

## Where you work

- Process root and worktree: `.`
  (branch `task/define-project-skill-shape`). Read every file from it. You are read-only: write
  only your report (and, if you need them, scratch scripts under the record's `reports/`, named
  `review_*.py`).
- Record directory (ignored by git): `.runs/task-cycles/define-project-skill-shape/`.

## Stage

Your method: `task-cycle/review/SKILL.md`, read whole; its section for the review of the whole
change is `whole_change.md` beside it — read it when the step names it. Your review: **the whole
change**, one author without a plan, no spec, no slices (no slice had a review of its own).

Range: base `2754675` (merge of PR #84 on `foundations`) to head `c0a0f52` (one commit, "Split
define-project into a picture of the whole and a file for each step and variant (WAY-256)").
Compute the diff yourself: `git diff 2754675..c0a0f52`. Changed: `project-level/skill/SKILL.md`
+23 −129 and nine new files beside it (+165).

## What is reviewed against

- The frozen task: `.runs/task-cycles/define-project-skill-shape/task.md` — read whole (in Polish);
  it is the requirement. No spec and no plan exist. The task carries no row of *Settlements to
  record* and no projected entry; the foundation step had nothing to write.
- The author's report: `.runs/task-cycles/define-project-skill-shape/reports/author_report.md` — a
  set of claims to verify, not evidence. Beside it in `reports/`: `assessment.md` (the assessment
  table and the proposals), `proposals.md`, `word-counts.md`, `verify_counts.py`,
  `compare_sentences.py` with `compare_sentences.txt`, `make_assessment.py`, `make_word_counts.py`,
  `check_pointers.py`.
- The base text of the skill: `git show 2754675:project-level/skill/SKILL.md` (identical to the
  task's base `dfd50e5`).

## Answers of the cycle's step 4

- Trust boundary: no (`project-level` names only three Python scripts as its boundary; none
  changes). Irreversible operation: no.
- The change made no move of a pin, so no checks of one are carried.

## What the task's acceptance criteria ask of you specifically

Besides the criteria of your method:

1. Walk routes 1, 3a, 4 and 5 of the task's question 4 by hand, from
   `project-level/skill/SKILL.md` to the file of the last step, as an agent that has the path of
   `SKILL.md` and no entry file would; list what stays and what drops on each. Compare every row
   of `reports/assessment.md` with the place where its fragment really stands after the rebuild,
   and every nonblank line of the base with exactly one row.
2. For every rewritten condition of a mode, variant or pointer, compare with the base: does it add
   a route or lose one? For every new sentence: what does it switch off? A check that sentences
   are present is not enough.
3. The delegated-mode file reaches step 7 (criterion 4 of the task): a dispatched agent does not
   ask the human itself, does not run the critique of 7.3 itself, and does not write the
   fingerprint or `approved` before the human's recorded approval, though the step 7 file speaks
   of these without reservation.
4. The fragments needed at several steps reach each of them (criterion 5 of the task, with the
   cases it names, the pointers of 7.1 to the files of steps 4, 5 and 6 included).
5. Each pointer names its step or variant in words an agent reading `SKILL.md` by path recognises.
   The delegated caller's words: `project-level/lead/skill/SKILL.md:202–219` and
   `project-level/lead/conversation_template.md`. Files that cite step numbers (which must still
   point right): `project-level/technology/start.md:8`, `project-level/lead/skill/SKILL.md:208`,
   `project-level/plan/skill/existing_plan.md:9`.
6. Nothing changed outside `project-level/skill/`; the skill's `description` and Python are as
   they were.
7. The word counts: recompute them yourself after the last change to a counted file and compare
   with every number the request will state (`word-counts.md`, `assessment.md` and the author's
   report). The author reports the base at 1937 words by `wc -w` under a UTF-8 locale and 1929 in
   the C locale; say whether that holds.
8. Foundation entries to check the change against are yours to select (WAY-150) by the parts the
   change touches; the task's *Decisions in play* are WAY-256, 257, 265, 106, 112, 118, 156, 120,
   113, 111, 127, 259.

The product's gate is not yours to run (the orchestrator runs it); run focused checks you need,
each with its command and exit code in the report.

## Report

Write the full report to `.runs/task-cycles/define-project-skill-shape/reports/review_report.md`
as your method gives it. Its first line is `PASS <sha>`, `FAIL <sha>` or `questions`. Include
**Searches not found or unclear** (each item or `none`). Return only: the first line, the report
path, a one-line check result naming what failed or did not run, and each blocking finding in one
line.
