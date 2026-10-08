You are the code reviewer of the last range of one the-way task cycle: the settlement of its independent assessment and
the reconciliation with the target branch. You wrote none of it. Read-only, except the deliberate-break section, which you
restore completely.

## Range

**Base:** 76c3f3c  **Head:** e879e4f. Package (commit list, stat, full diff):
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\review-76c3f3c..e879e4f.diff`. Commits in it:
- cdb3fb9 — the settlement of the independent assessment (two foundation files; its message records the settlement); the
  settlement itself is in `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\assessment.md`
  (§ Settlement) — read that section only.
- 5024aef — merge of `origin/foundations` 099c190 (PR #6, #7 of others: WAY-13, WAY-125, the task-cycle skill, the
  installation README, one invariant renewal). Those changes were reviewed in their own requests; judge only how they meet
  this branch.
- e879e4f — the entry point of `implement-task` regenerated with `python -B agent-instructions/skill_entry_points.py --write`
  because PR #7 changed that skill's description (the gate's flow test reported it stale after the merge).

## Check

1. The settlement commit does exactly what § Settlement says (WAY-127 *Rationale* clause; WAY-27's repeated violates example
   removed; the part-map bracket removed, condition kept) and nothing else; fingerprints WAY-127 4439a64a and WAY-27 fb27e458
   unchanged (`python -B -I .runs/stale_refs.py WAY-127 WAY-27` from `C:\Storage\repos\the-way-skills-self`).
2. Foundation collision search against the new tip (WAY-33): read the merged WAY-13 and WAY-125 and the task-cycle skill's
   changes in the diff, and say whether any of them collides with or needs a link from WAY-127, WAY-09, WAY-27,
   `skill-entry-points/1`, `outbound-link-reach/1`, the four facts, or the part map's `agent-instructions` entry and flow
   `skills-reach-the-way-sessions`. Report each finding as link / change / none.
3. e879e4f: the two copies are byte-identical, only the description line changed, it starts with the new description of
   `task-cycle/skill/SKILL.md` followed by " Use this checkout's own the-way.", and the new description is a safe plain YAML
   scalar.
4. Deliberate break (WAY-69, WAY-08; the settlement changed assessed foundation entries, so the break is written again): read
   only the sentence of `skill-entry-points/1` in `foundations/invariants.md` (not the check's code), write at least three
   breaks of it in the worktree `C:\Storage\repos\the-way-skills-self`, one at a time — at least one on the regenerated
   `the-way-implement-task` copies — and after each run `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
   and read `.runs/gate-tests.jsonl`; report for each whether `test_every_skill_reaches_a_session_on_the_way` failed and
   `skill-entry-points/1` was recorded `fail`. Restore after each with
   `git restore --source=HEAD --staged --worktree -- .claude/skills .agents/skills` (and any other path you broke), remove
   directories you added (list with `git clean -n -d -- <path>`, delete those by path); end with `git status --short` empty
   and one clean gate run.

Do not dispatch subagents. Do not use globally installed skills named record-*, update-part-map, refine-task or critique.

## Output

Findings (Critical / Important / Minor, file:line), the collision-search results, the break table, the final clean run, and
a verdict: clean | needs fixes. Return it as your final message.
