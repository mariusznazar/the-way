# Human remarks on PR #49 — correction after review

Mariusz, 2026-10-28, in the conversation after the request opened, asked why the restatements between
the skill's files were not corrected in this task, and decided: "poprawiamy teraz". He accepted the
orchestrator's recommendation to correct the following findings now, in this request. These remarks
bind. The findings are quoted in the reviewers' words; the full text is in `return-review-report.md`
and `review-report.md` beside this file.

## R1 — return-step review, Minor 1

"`instruction-files/SKILL.md:88-89`: the step now reads the kind file after the mode's procedure is
followed. The new text: 'Read the mode's file in full and follow it. Then read in full the file of
each kind of file the mode works on'. […] taken in order, 'follow it. Then read' puts the kind file —
the per-fragment question of `kind_skill.md` (WAY-256), the three conditions as applied in
`kind_main_file.md` — after the judgement it is needed for. […] Wording that keeps the order: 'Read in
full the mode's file and the file of each kind of file the mode works on …, then follow the mode's
file.'"

## R2 — return-step review, Minor 2

"the move puts rules into two files, against WAY-258 […]:
- `instruction-files/placing.md:12-13` ('Search the instruction files for a rule on the same subject;
  when one stands, the new wording replaces it') and `instruction-files/SKILL.md:253-255` […]; also
  `SKILL.md:236-238` ('A change to a rule replaces its previous wording where that wording stood') and
  `instruction-files/changing.md:5` ('A reworded rule replaces the sentence that stands');
- `instruction-files/placing.md:8-11` ('When it must happen every time, propose the mechanism first —
  a CI check, a linter, a check of a step's output, or a local git hook […]') and `SKILL.md:117` and
  `:180-182` (WAY-133, same list, same hook qualifier).
[…] `instruction-files/judging.md:32-35` 'recommended only for a mistake found more than once; …
unless the rule carries a decision the repository records or a step of the activity its file leads
(WAY-130)' against `SKILL.md:244-247` […]. The fix is the one correction 4 used: the mode file names
the `SKILL.md` section ('as "When to add a rule" gives it', 'by "Where a rule stands"') instead of
restating it."

Beyond the pairs named: the remark is that no rule stands in two of the skill's files (WAY-258). Check
every file of `instruction-files/` (except `tool_loading.md`, which holds no rules of placement) for
any other restatement of the same kind, and remove it the same way.

## R3 — return-step review, Minor 3

"`instruction-files/placing.md:5-7`: 'A rule with neither is not placed' reads against the wrong
antecedent and drops the threshold from the step's own text. […] Suggested: 'A rule with none of
these is not placed', and keep 'found more than once' in the clause or rely on the pointer alone
without listing the grounds." (Under R2, prefer the pointer alone.)

## R4 — return-step review, Minor 4

"`instruction-files/SKILL.md:144-147`: the citation of `single-rule-compliance` still leaves out the
fact's scope. The fact measured 'compliance with a trivial target annotation across Claude Code CLI
sessions' […]. Adding 'in Claude Code sessions' after 'target annotation' closes it."

## R5 — whole-change review, Minor 3

"two tool-documentation sources disappeared with the *Sources* list of `principles.md`. […]
`https://code.claude.com/docs/en/best-practices` and `https://learn.chatgpt.com/guides/best-practices`
now stand nowhere in `instruction-files/` or `foundations/environment_facts.md` […]. Either cite the
two addresses beside the principles that rest on them, or say in the request that they were dropped
and why." The remark: cite them beside the principles that rest on them (find which, from
`principles.md` at `0b8c1bd`).

## R6 — whole-change review, Minor 5

"reflow leftovers. `foundations/decisions.md`, WAY-128 *Rejected*: the edit leaves a short line
'stand today — every' before 'unchanged line would become…'. And
`instruction-files/check_instructions.py:4` is now 123 characters, while the rest of the docstring
wraps near 100." Reflow both; `check_instructions.py` stays a docstring-only change (trust boundary).

## Not in this correction

Whole-change review Minor 4 (WAY-256 against the reading rule of WAY-125) stays for the task that
rebuilds the-way's skills: changing WAY-125's meaning is the human's decision, not taken here.
