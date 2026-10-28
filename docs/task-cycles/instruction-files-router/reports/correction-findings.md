# Blocking findings of the correction review — to fix once

From `correction-review-report.md` (`FAIL 44475cf`), in the reviewer's words. Fix these two; the
review's Minor and out-of-scope findings are not fixed (they go to the request). Answer with evidence
a finding you hold wrong.

**I1 — the correction drops the second half of WAY-133 from the skill.** Place:
`instruction-files/placing.md:7-8` and the removed row of `SKILL.md` *Mistakes this skill prevents*.
Before the correction the skill said twice that, for a rule that must hold every time, an
instruction carries what the mechanism cannot do: `placing.md` step 2 at `f4bbf06` ("…and an
instruction only for what the mechanism cannot do") and the row "placing a rule that must hold every
time only as an instruction | a mechanism, and an instruction for the rest" (`SKILL.md:278` at
`f4bbf06`; both already stood in the base `0b8c1bd`, `SKILL.md:130` and `:159`). The correction
replaced the first with "propose first the mechanism that section gives" and cut the row as a
restatement. The section pointed to holds only "an instruction may explain what the check is for,
but does not replace it (WAY-133)" (`SKILL.md:117`) — it does not say that the instruction carries
the part the mechanism cannot check. WAY-133 says: "The instruction file then says what the
mechanism is for, or carries what the mechanism cannot check." At `44475cf`, `grep -i "cannot do\|for
the rest\|cannot check" instruction-files/*.md` finds nothing. Why it matters: an agent placing such a
rule now proposes a mechanism and has no rule telling it to keep, as an instruction, the part no
check can catch — the skill falls short of a decision in play, and the correction was to change no
meaning. The pointer is the right form; it fails only because its target lacks the content. Fix:
state the half once, in the row's *Notes* of `SKILL.md:117` (for instance "an instruction says what
the check is for, or carries what the check cannot catch; it does not replace the check (WAY-133)"),
and keep the pointer in `placing.md`.

**I2 — restatements between files remain (R2, WAY-258 "No rule stands in two of its files").**
- `SKILL.md:249-252` "a rule that carries a decision the repository records, or a step of an
  activity …, needs no repeated mistake — its reason and its way out are that decision or that
  work" and `SKILL.md:261-262` "the named mistake is later its way out", against
  `judging.md:79-81` "it was added for a mistake that can no longer be named — it is proposed for
  removal; … A rule that carries a decision or a step of an activity goes with that decision or that
  step, not by this test." The way out of a decision-carrying rule is stated in both files — the
  same rule, half of the WAY-130 pair R2 named, left in the removal list.
- `SKILL.md:116` (row "during an activity", note: "when the activity has no obvious way in, the main
  file points to it in one sentence") with condition 1 at `SKILL.md:122` ("or it points to a way in
  that would not be found otherwise"), against `kind_main_file.md:19-21` "Pointers to ways in … for
  activities whose way in the agent will not recognise from the request alone". The same rule — when
  the main file carries a pointer — in two files; the correction applied exactly this test to the
  main file's list of files and to "not derivable from the repository" and cut them, but not here.
Why it matters: the human's remark binds the correction to "no rule in two of the skill's files",
and WAY-258's rationale names the cost: "A rule kept in two files drifts." Fix the same way: the
removal bullet in `judging.md` points to the exception of "When to add a rule" (or `SKILL.md` drops
"its way out are…" and the removal list holds it alone); the pointer item of `kind_main_file.md`
says "Pointers to ways in, where condition 1 of the criterion allows one, in the form of the shared
layout…".

Before you commit, search the whole of `instruction-files/` once more (except `tool_loading.md`) for
any rule that still stands in two files, and for any content of a decision in play (WAY-128 to
WAY-133, WAY-256 to WAY-258) a pointer now leads to but its target does not hold; this is the one fix
the cycle allows.
