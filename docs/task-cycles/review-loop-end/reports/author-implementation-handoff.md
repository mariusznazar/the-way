# Implementation stage handoff — same author, turn 2

Worktree: `C:/Storage/repos/the-way-wt/review-loop-end`. Input commit: `0761d6d`; base `e7f7c3a`.
Authority: frozen task `.runs/task-cycles/review-loop-end/task.md`; the current whole entries WAY-125 and WAY-161..164 as you wrote them, and the applicable unchanged foundation. The orchestrator read the foundation diff and gives a provisional go-ahead under Mariusz's delegation (not human approval).

## Rulings on your concerns (also in the cycle record, C5–C9)

1. Later code reviews' Minor / out-of-scope findings: no new rule. The skill implements WAY-161's two request lists for the review of the whole change. For later reviews, WAY-162 grades blocking by WAY-161, so non-blocking findings there trigger no fix and stay in their review reports, linked from the record. Do not invent a request list for them.
2. A "Declined to judge" line with no place in the code: the request gives the place the reviewer names and says that none is given where the line names none. Foundation unchanged.
3. WAY-125 goes into *What this request settles* — orchestrator's job at the request; nothing for you.
4. WAY-125 stays edited in place.
5. The failure-mode candidate waits for your return step.

## What this stage does

Make `task-cycle/skill/SKILL.md` and `task-cycle/record_template.md` (and any other non-foundation file the change needs) carry WAY-161..164 and the edited WAY-125 coherently, replacing superseded obligations instead of appending contradictions. At least: the intro (lines 16–19: a remaining blocking finding is now a reason to stop with a blocked draft); step 9's fix/re-review sentence (one-author review and the final whole-branch review of `subagent-driven-development`; slice loops unchanged); steps 10–13 (blocked request contents: remaining findings with place and reason, what the fix tried, cost from `stages.md` with review-round count; gate and record yes, return step and assessment named as not run; WAY-163's later run); step 11's settlement reviews and step 12's reconciliation reviews under WAY-162; the "nothing is deferred" sentence (lines 348–349) limited to foundation entries so it does not contradict WAY-161's request lists; step 13's request lists (Minor findings; findings outside the scope, for the human to make tasks of); the correction-after-review section (WAY-162 bound, WAY-163's runs after the human's decision); the weakest-point duty of WAY-164 for the author (step 9 / one-author route) and each slice executor, and the reviewer reading that report; the record template's room for review rounds and the weakest-point evidence.

Read the skill conventions before editing a skill: `C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/konwencje_skilli_i_commandow.md` (read only). Keep the skill's current style and density. If the skill's name, description or path changes, run `python -B agent-instructions/skill_entry_points.py --write` and commit what it writes.

Use Superpowers 6.4.1 `test-driven-development` (read from `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/test-driven-development/SKILL.md`) for any behaviour change in code; prose-only policy needs no tests asserting prescribed prose (WAY-12/22). Do not edit invariant tests; if needed, return to the foundation step.

**WAY-164 applies to you now.** Before you return this stage for review, name the requirement of the task most likely not met by your work, write a check that would catch it (a test, a scripted search, or a manual method recorded as such), run it, and report which requirement, which check, and what it showed.

## Checks

Focused tests of changed parts (`python -B gate/run_tests.py task-cycle`, others you touch), `python -B gate/run_tests.py gate`, guards of any changed foundation file, `git diff --check`. Complete stdout+stderr under `.runs/task-cycles/review-loop-end/reports/`, command and exit code for each; warnings and `unchecked` named.

## Write boundary

As in turn 1: only this worktree; preserve line endings; explicit-path commits, English messages; never stage `.runs/`; no push, no PR; no agents; no vault or original-checkout writes. If you meet an open design choice or the change outgrows you, return a report without code as the cycle's recovery rules say.

## Output

Full report `.runs/task-cycles/review-loop-end/reports/author-implementation.md`: inputs and commits; changed files with added/removed line counts for `0761d6d..HEAD`; coverage of task To do 1–4 and rows 1–7 against the text you wrote (with line references); choices with rejected alternatives and cost; the weakest-point check (requirement, check, result); commands, exits, output paths; sharpness inputs from the actual diff; unresolved concerns. Short return: status, report path, commits, checks. Stop before review; the same author resumes later for the return step.
