# Handoff to the agent of the plan's *Foundation entries*

You write the foundation entries of one task cycle of the-way, in three turns the orchestrator gives you one
after another (you are resumed for turns 2 and 3). Work from the worktree root
`the task's worktree`, branch `task/decision-log-second-round`, base
`ec7929d` (also slice 1's base). The person who requested the cycle delegated intermediate choices to the
orchestrator; nothing you write is anyone's approval. Never push, never run the product's gate
(`gate/run_tests.py` without a directory), never touch a file outside the worktree.

## Method and stage

- Method: `task-cycle/change/SKILL.md` (`make-change`), read whole, with `task-cycle/skill/foundation_step.md`
  whole. Take no row of the table of variants of `make-change`: you are the agent of the plan's
  *Foundation entries*. Where `make-change` asks for tests of code, for you the checks below are the tests;
  write the own-work check and the report as `make-change` gives them.
- Entries are written by following `elements/decisions/skill/SKILL.md` (decisions), and for the invariants,
  the part map and the glossary the `SKILL.md` of that element, plus the element's template; a file a skill
  names by its name alone you read as a file.
- Stage boundary: the log work of rows F1–F8 of the plan, in three turns. You change only
  `foundations/decisions.md`, `foundations/invariants.md`, `foundations/part_map.md` and
  `foundations/glossary.md` — no other file (the slices do the rest). Commit each turn separately with
  `git add <path>` by path, an English message of the form of the log of `git log --oneline`.

## What binds

- The frozen task: `.runs/task-cycles/decision-log-second-round/task.md` (lines 1–490; Polish; its text of
  the addition to WAY-100 is English and is copied word for word).
- The plan: `.runs/task-cycles/decision-log-second-round/plan.md`, section *Foundation entries* (rows F1–F8)
  and *Choices*; the planner's report `reports/planner-report.md` (read all of it) with its surveys
  `reports/planner-survey-withdrawals.json` and `reports/planner-survey-adoptions.json` (hypotheses of
  survey agents, to be checked against the entries, never taken as the entries' content) and
  `reports/planner-refs-by-number.txt`.
- Foundation entries, each whole: WAY-100, WAY-29, WAY-293, WAY-19, WAY-02, WAY-27, WAY-90, WAY-36, WAY-14,
  WAY-114, WAY-25, WAY-07; each entry you edit or withdraw, whole, before you change it. The withdrawn-numbers
  list of the log and the section "Withdrawn numbers" of `elements/decisions/template.md`, and
  `elements/common/rules.md` ("Withdrawn identifiers"), for the form of a withdrawal.
- The first round of the same kind, for the form: `git show f0b2130 --stat` and the withdrawals in the
  history of `foundations/decisions.md` from the merge of request #37 (`git log -S"Withdrawn" --oneline --
  foundations/decisions.md` finds them).

## The orchestrator's answers to the planner's questions (they bind you)

1. Where an entry of F3 says nothing of what the practice leaves out, leave its *Rejected* as the entry has it
   and never write a sentence from memory; list such entries in your report, per entry, with the missing item.
   *Based on* with a missing source reads `TODO — <what is missing>` as the form of the field allows.
2. WAY-204 and WAY-258: no relation to WAY-100; WAY-167 gets it.
3. WAY-173 and WAY-140 lose `derives from WAY-100` by the task's rule (its answer 3). List both in your report
   (the request will put them before the human).
4. Order as planned: all log work now, slices later.
5. Invariant `project-definition-form`: *Derives from* `none`; `map-reference-target`: the nearest staying
   decision (WAY-02, whose *Verification* then names it, as the survey suggests); for the other two invariants
   the plan's F8. State each choice in your report.
6. The four entries WAY-263, WAY-287, WAY-294, WAY-295 stay in the log (out of F4); nothing changes in them
   except what F6 requires for references to numbers that leave.
Where something in the plan contradicts the task or the entry itself, the task and the entry hold; say so in
your report and do not decide for the human.

## The turns

- **Turn 1 (now): rows F1, F2, F3.** F1: the addition to WAY-100 in the exact words of the task's answer 2,
  and a complying example in its *Verification* as the task says. F2: WAY-29 — the description of the commit or
  merged request that introduced the shape of the code is a source quoted with the commit identifier, looked at
  before `unknown`. F3: the entries of lists (a), (b), (c) of the plan by the pattern; for (a) and (b) the
  entry says in its binding sentences or *Rationale* what it takes from the practice and what it does not,
  the source in *Based on* (a source a reader of the repository cannot open: described in *Rationale*, WAY-27);
  for (c) the relation is removed and the source stays in *Based on*; rows (d) unchanged. WAY-374 is in (a).
  Do not rewrite a decision's meaning; the pattern shapes what the entry already says. Check:
  `python -B elements/common/foundation_check.py` (record what it prints; before turn 2 it must exit 0) and
  `python -B gate/run_tests.py elements/decisions`.
- **Turn 2: rows F4 and F5**, when the orchestrator resumes you.
- **Turn 3: rows F6, F7, F8**, when the orchestrator resumes you.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies and scripts: `.runs/foundation/`. Scripts you write for repeatable edits of
the log live there, never in tracked files.

## Report

One report per turn, appended to `.runs/task-cycles/decision-log-second-round/reports/foundation-report.md`
(a new section for each turn), with each check as command and exit code, the entries written (a sentence of
meaning in English and one in Polish each, marked `row <n>`), your choices, questions, **Unread material**,
**Searches not found or unclear**, working copies, and the commits. Return status, commits, the one-line check
result and the report path.
