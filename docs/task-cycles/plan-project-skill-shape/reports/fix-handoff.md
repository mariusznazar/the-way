# Fix handoff — plan-project in the WAY-256 shape

The person who requested this cycle delegated intermediate choices to the orchestrator. The human
reviews the request, not this stage. Questions come back to the orchestrator; never ask the human.

Follow `task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**, in the worktree
`C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape`, branch
`task/plan-project-skill-shape`. The review judged `db3845c`; the fix's range runs from there.
`<cycle>` is the same directory as in `reports/author-handoff.md`, whose rules on commits, scripts,
language, line endings and where materials stand still hold.

## The finding

`<cycle>/reports/findings.md` holds the one blocking finding, in the reviewer's words. The whole
review is `<cycle>/reports/review.md`. The review's Minor findings 2 to 5 are not part of this fix:
they go to the request as they stand. Do not fix them, in the skill's files or in the materials.

## The answer the cycle gives to your concern 3

The orchestrator answers the question the finding raises, as a choice of the cycle (C4): "reads" in
the last bullet of `existing_plan.md` means that the session carries `read.md` out, as every other
"Read `<file>`" pointer of `SKILL.md` means.

Evidence, from the frozen task, question 3: the way not chosen is the one where the "agent zmienia
plan bez fundamentu w głowie", and the state it records is `readiness_check.py` run in each of the
14 sessions and `foundations/` of the product reached in 11. The first reading of the sentence is
the one that fulfils that answer, and the second is the outcome it turned down.

## What to do

1. The sentence was read in two ways by its own author, so make it say the first reading plainly.
   In `project-level/plan/skill/existing_plan.md:15-16`, keep its condition and its reasons and
   change only the verb, on the precedent of "goes through `refine-task` steps 1 and 2 first"
   (`product-guidelines/testing/SKILL.md:79-81`, WAY-266), so that a session that has not been
   through `read.md` goes through it before it goes on.
2. Check `project-level/plan/skill/SKILL.md:48-49` against that wording by what it selects. A session
   that went through `read.md` at step 0 has nothing left to do at step 1, and a session that did not
   does the whole of it. Change it only if the words no longer say that, and name what you did.
3. Correct what rests on the rejected reading: `assessment.md:81`, and the entry on that sentence
   under "Text added".
4. In `word-counts.md`: state the rule, and count routes 3 and 6 with step 1 carried out, the section
   "Reading the foundation" and `product-guidelines/reading.md` included, in both states, with the
   figure for the literal reading of the base beside it, since the base's text sent no resumed draft
   through step 1. Correct the route notes, the range of the comparison with the files read beside
   the skill, and the comparison with the task's estimates ("ok. 170 słów na każdej drodze z
   istniejącym planem" is the file alone, not what the sentence sets off). Say what each of the two
   readings of "before" gives.
5. Regenerate the materials after your last change to a counted file, and run the helper that
   compares each figure with the files.

For each new or changed sentence, name what it switches off.

## Checks

Run `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .`,
`python -B agent-instructions/skill_entry_points.py --write` (it should change nothing),
`python -B gate/run_tests.py project-level`, and your helpers on the regenerated materials. Do not
run the whole gate.

## Report

Commit with `git add <paths>`; keep the worktree clean; do not push. Full report:
`<cycle>/reports/fix.md`, with each check's command and exit code, your answer to the finding, every
figure of `author.md` this fix replaces, every reach, and **Searches not found or unclear**. Return:
your status, your commits, a one-line check result naming what failed or did not run, and the
report's path.
