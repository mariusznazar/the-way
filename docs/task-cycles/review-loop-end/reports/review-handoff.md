# Whole-change review handoff — reviewer, turn 1

You review the whole change of a one-author task cycle in the-way. You did not write it. This is the review of the whole change (WAY-136) and the final review.

Worktree (read-only for you): `C:/Storage/repos/the-way-wt/review-loop-end`. Range: `e7f7c3a15c3f80143f9ad582ec785c993cff3779..ac65ac3` (3 commits: `0761d6d` foundation, `d88728d` and `ac65ac3` skill and record template). Files: `foundations/decisions.md` +225/−8 approx., `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`.

## Method

Superpowers 6.4.1 `requesting-code-review`: read whole `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/SKILL.md` and its `code-reviewer.md` (not through the Skill tool, which loads another version). You are the reviewer of that template; follow its rules (read-only, no subagents, Declined to judge list, Critical/Important/Minor with file:line, explicit assessment).

- `[DESCRIPTION]`: the task cycle gains an end to the review loop of the whole change (one fix, one review of the fix, then a blocked draft request with cost), a grading of blocking findings by the reviewer's Critical/Important grade, request lists for unfixed Minor and out-of-scope findings, the steps run before a blocked request, and a weakest-point check by the author/executor before review. Four new decisions WAY-161..164, WAY-125 edited in place, the cycle skill and record template aligned.
- `[PLAN_OR_REQUIREMENTS]`: the frozen task `C:/Storage/repos/the-way-wt/review-loop-end/.runs/task-cycles/review-loop-end/task.md` — read whole: *To do* 1–4, answers to questions 1–9, *Settlements to record* rows 1–7, *Decisions in play*, *Out of scope*. It is in Polish; the entries are in English.

## No-plan coverage checks (WAY-136, cycle step 9) — in addition to the template

1. Every *To do* item and every row 1–7 of *Settlements to record* is written whole as a decision whose meaning is the row's (WAY-134) — wording may differ, meaning may not; no meaning added that no row or answer carries.
2. Source fidelity: quotations of Superpowers 6.4.1 in *Based on* match the files at that root; references to WAY entries and fingerprints are correct; the glossary's narrow `verdict` / `correction` (`foundations/glossary.md`) are not used for the reviewer's call or the fix.
3. Foundation entries precede the dependent instruction text (commit order).
4. The skill text and the decisions agree; no older sentence of `task-cycle/skill/SKILL.md` still contradicts WAY-161..164 (e.g. the intro's "Stop early only when…", step 9 fix sentence, step 11 "nothing is deferred", steps 12–13, correction after review). Read the whole skill at `ac65ac3`, not only the diff.
5. Template conformance of the new entries with `elements/decisions/template.md` and `elements/common/rules.md`.

The author's reports are inputs for you: `.runs/task-cycles/review-loop-end/reports/author-foundation.md` and `author-implementation.md` (including its weakest-point check and Addendum 2b). Check the author's sharpness findings (criticality of touched parts, trust-boundary files, irreversible operations) against the actual diff, and judge the weakest-point check (WAY-164): was it the right requirement, did the check catch what it claims? Orchestrator choices C1–C11 are in `.runs/task-cycles/review-loop-end/cycle.md` — read the questions table; a choice you disagree with is a finding.

You may run read-only checks (`python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py gate`, decision guard with `--base none --merge-onto none`) — save complete stdout+stderr under `.runs/task-cycles/review-loop-end/reports/review-*.txt` with command and exit code; these writes under `.runs/` are your only writes.

## Output

Full report `.runs/task-cycles/review-loop-end/reports/review.md`: the template's output format, plus the coverage table (To do 1–4, rows 1–7 → entry and skill lines), the Declined to judge list, the range reviewed, sharpness confirmation, and commands/exits/paths for anything you ran. Return message (short): verdict, counts by grade, report path, range.
