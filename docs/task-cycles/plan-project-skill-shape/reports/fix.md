# Fix report - blocking finding 1 of the review of db3845c

**Status:** done. Range of the fix: db3845c..HEAD (one commit, see below).

## Commit

- Commit message: "Have a session on an existing plan go through step 1 before it goes on" (`git log -1`, author `mariusznn@gmail.com`). File changed: `C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape/project-level/plan/skill/existing_plan.md` (2 lines, +2 words).

## Answer to the finding

The cycle's choice C4 is taken: "reads" means the session carries `read.md` out. The last bullet of `existing_plan.md` now reads: "Whichever step the plan goes on from, a session that has not been through `read.md` beside this skill (step 1) yet goes through it before it goes on." Condition and reasons unchanged; only the verb changed, on the precedent "goes through `refine-task` steps 1 and 2 first" (`product-guidelines/testing/SKILL.md:79-81`).

What the changed sentence switches off: a resumed draft that skipped step 1 altogether (the base sent it from the first unfinished step, past step 1); nothing else. It adds no route that a session on an existing plan did not take in the 14 recorded sessions (readiness check run in 14, foundation reached in 11).

## `SKILL.md:48-49`

Not changed. "Read `read.md` ..., each unless step 0 had you read it" selects what the finding needs: every other "Read `<file>`" pointer of `SKILL.md` means to carry the file out, so a session that went through `read.md` at step 0 has nothing left at step 1, and a session that did not does all of it. It selects the same sessions as before the fix; the fix made the step 0 side say plainly what this side already meant.

## Materials corrected

- `assessment.md:81` (the entry on that sentence under "Text added"; generator `tools/make_assessment.py` patched, file regenerated): now says the session carries `read.md` out and that it switches off a draft resume that skips step 1; the false "does not make step 1 run" is gone. Build: 34 rows, the one known mid-sentence artefact of lines 102-104, exit 0.
- `word-counts.md` (generator `tools/word_counts.py` patched, regenerated after the last change of a counted file; `tools/verify_counts.py`: 279 figures compared, 0 differ, exit 0):
  - the rule is stated: on routes 3 and 6 step 1 is carried out, the section "Reading the foundation" (492 words) and `product-guidelines/reading.md` (1141) are counted, in both states, because the recorded sessions ran the readiness check in 14 of 14 and reached the foundation in 11;
  - route notes for 3 and 6 and the rule about `existing_plan.md` corrected;
  - a new section "The literal reading of the base on routes 3 and 6" gives the other reading of "before": route 3 5264 words (change of the total to after +23.5%), route 6 5852 (+17.4%); with step 1 carried out in both states: route 3 6897 to 6502 (-5.7%), route 6 7485 to 6871 (-8.2%);
  - the comparison with the task's estimates is corrected: "about 170 words on every route with an existing plan" is the file alone (141); what the sentence sets off on routes 3 and 6 is 1774 words with the file; the estimate figures in the comparison are now computed from the table.

## Figures of `author.md` this fix replaces

| Figure in `author.md` | Now |
|---|---|
| route 3 skill text 1947, total before 5264, after 4867 (-7.5%) | skill text 1949; total 6897 to 6502 (-5.7%); literal base 5264 (+23.5%) |
| route 6 skill text 1728, total before 5852, after 5236 (-10.5%) | skill text 1730; total 7485 to 6871 (-8.2%); literal base 5852 (+17.4%) |
| 5a 1984, 5b 3045, 7 2869, 2 2583 unchanged, 1 2407 unchanged | 5a 1986, 5b 3047, 7 2871 (the two added words of `existing_plan.md`) |
| reading everything +701 words (+30%), sum of files 3045 | +703 (+30.0%), sum 3047 |
| totals with the files read beside the skill, -10.5% to +9.4% | -8.2% to +9.4% (step 1 counted in both states on routes 3 and 6) |
| range of the skill text -26.3% to +29.9% | -26.2% to +30.0% |
| "step 1 is not run" on routes 3 and 6; the hand walk of routes 3 and 6; concern 3 | step 1 is carried out there; concern 3 is answered by C4 |

`author.md` itself was not edited (the handoff asks for this table instead).

## Checks (worktree, after the last change of a counted file)

- `python -B elements/common/foundation_check.py` exit 0 (0 errors)
- `python -B instruction-files/check_instructions.py .` exit 0 (0 error, 1 warn - the base's dead path on `AGENTS.md`, 3 info)
- `python -B agent-instructions/skill_entry_points.py --write` exit 0 ("entry points are current", changed nothing)
- `python -B gate/run_tests.py project-level` exit 0 (OK)
- `python -B .runs/task-cycles/plan-project-skill-shape/tools/verify_counts.py reports/word-counts.md` exit 0 (279 figures, 0 differ)
- `compare_sentences.py` exit 0: the same 3 reworded pointers as before; `existing_plan.md` changes only the verb.
Not run: the whole gate; installation and agent-instructions tests (the fix changes no file they read beyond one Markdown sentence).

## Reach beyond the handoff

None. Review Minor findings 2-5 untouched.

## Searches not found or unclear

none
