# Report of the return step — cycle-instruction-seven-fixes

**Status:** done. **Commits:** none (the step found nothing to correct; head stays `52801a69`, tree clean).

## Return step, as the record's *Return step* gives it

- **Foundation compared with code:** none needed correcting. Compared:
  - WAY-136 (sentence on reviews of groups of slices, its *Verification*, *Rationale*, *Rejected*) with `task-cycle/skill/SKILL.md` step 9 sub-step 5: the skill says the same (the lead may dispatch a fresh reviewer with `review-change` on groups of the slices with no review of their own, in the plan's order, as for a slice with a review of its own, and records the grouping and its reason), by judgment and with no measure; it reads a group-reviewed slice as one "with a review of its own", so `task-cycle/review/whole_change.md` and the handoff text at SKILL.md:522 ("whether it had a review of its own") stay consistent. "The lead" in the skill against "the orchestrator" in the decision is review finding 5, outside the task: changed nothing.
  - WAY-255 with `task-cycle/change/SKILL.md` and `task-cycle/review/SKILL.md`: both now say "you end your turn only after it has ended and you have read its result (WAY-255)", which the decision now says.
  - WAY-134 with `elements/decisions/template.md`: the two sentences agree (`no cost to the product known` for a way with no cost or only a cost of the process; a way of the process stays out). `task-cycle/skill/foundation_step.md` states the *Rejected* rule shortly and sends the reader to the template ("as the decisions' template gives"); it says less than the template but contradicts neither it nor the decision, so I left it.
  - WAY-140, WAY-316, WAY-373, WAY-148 (named by the task, unchanged): WAY-140 and WAY-316 still collide as the task says (the skill's list of exceptions has the screenshot shown to the human; WAY-140 lists no such exception and WAY-316 is silent on WAY-140). The task settles this: the skill gets the exception, the decisions stay (*Questions to settle*, "Punkt 1 a WAY-140"); the request shows it to the human in one sentence. WAY-373 agrees with the new sentence on removing a copy by a path written out in full (it adds a rule on how, contradicts none). WAY-148 (a report is the cycle's file; a refused write is saved unchanged from the agent's answer) agrees with the new text of step 5 of the cycle.
  - The search of the whole foundation (WAY-33) was made in the foundation step: entries naming WAY-136, WAY-255 or WAY-134 in `foundations/*.md` (grep); none derives from or narrows them with a sentence now false; no invariant, glossary term or environment fact names them (grep of those three files for the numbers: no hit).
  - Part map: `decisions` (files `elements/decisions/**`, `foundations/decisions.md`; depends on elements-common, invariants, product-guidelines, project-level) and `task-cycle` (files `task-cycle/**`; its depends list; trust boundary on four scripts, none changed). The change adds no file, changes no dependency (`task-cycle/slice_size.py` imports the standard library only), touches no trust boundary: no change of the map needed.
- **Decisions written or changed:** WAY-136, WAY-255, WAY-134 (rows 1, 2, 3; `the cycle's` for the examples added to *Verification*, as the foundation step's report marks them), written in the change; this step changed none.
- **Invariants written or changed:** none.
- **Environment facts:** none (the change rests on no source outside the product that the foundation lacks).
- **Glossary terms:** none (no word used in a meaning for which WAY-95 gives it an entry; no term used against its entry).
- **Part-map changes:** none.
- **Projected entries:** none (the task carries none).
- **Rows of *Settlements to record* written, with the place:**
  - row 1 → sentence of WAY-136 (`foundations/decisions.md`), written in the foundation step;
  - row 2 → sentence of WAY-255 (`foundations/decisions.md`), written in the foundation step;
  - row 3 → sentence of WAY-134 (`foundations/decisions.md`) and the bullet of `elements/decisions/template.md`, written in the foundation step.
  Nothing was missed by the foundation step; no row is left for this step.
- **Pair of examples and tests:** the three decisions carry pairs (extended clauses of *Verification*) and no test holds a part of their sentences (no `decision:` line cites WAY-136, WAY-255 or WAY-134, by grep), so there is nothing to remove from a pair and no `tests:` clause to write.

## The two accepted choices: do they bind after the merge (WAY-36)?

Answered by the plan test of the decisions template ("does the rule still bind once the change is merged?") and, for the yes, the questions of "Where it goes".

1. **Q2 — a file that *Read* names both whole and by ranges counts whole** (`task-cycle/slice_size.py`). It binds after the merge: a later change that made ranges win would measure differently. It passes the plan test, so it goes through the questions in order. Question 1 (an instruction for how an agent works) is no: it is how a script counts. Question 2 (a rule for how to write code) is no. Question 3 ("a single text, number, list or location" — product data or code, "with the test that holds it and, where the reason is not obvious, a comment") is yes: it is one rule of one script's counting. So it is no entry of the log: it is already where question 3 puts it — the code, the docstring sentence ("a file that *Read* names whole counts whole, whatever ranges of it *Read* names beside"), and the test `test_changed_file_that_read_names_whole_and_by_ranges_counts_whole`, which holds it. Result: no entry written; no row of the questions table is needed for it beyond the cycle's own note of the choice.
2. **Q4 — a way of the process stays out of *Rejected* (rows 1 and 2: "only the skill", the two skill variants)**. This is no new rule: it applies the sentence of row 3, which is now written in WAY-134 and in the template, to the ways of the sources of rows 1 and 2. What it chose is that "where an answer is recorded" is a way of the process, the nearest case of the template's example "how or when an answer is recorded". It does bind later (it decides what WAY-255's and WAY-136's *Rejected* hold), but the settled sentence already decides it, and writing "where" into WAY-134 or the template would extend a meaning that the human accepted in row 3 beyond what the task gives (WAY-30), which this step may not do for a choice that the task's rows do not carry. Result: it stays a row of the cycle's questions table, as the return step gives for every other choice; the reviewer of the whole change read both entries with it and passed. Cost if wrong: two or three clauses in the *Rejected* of WAY-255 and WAY-136.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check on the current tree (nothing was changed by this step) | `python -B elements/common/foundation_check.py` | 0 (0 errors) — run for the last time after the fix's last commit, `52801a69`, and the tree is unchanged since |

Not run: the full gate (handoff). No test run: this step changed no file.

## Own-work check

- Requirement most likely unmet: that nothing in the foundation or the instruction files still says the opposite of what the change writes. Check: grep of `task-cycle` for "review of its own", "groups of" and of the three foundation files for the three decision numbers (output above); no sentence found that says the old thing. Showed: only the finding-5 word ("lead" against "orchestrator") and the short statement in `foundation_step.md`, both left as described.
- Behaviour a user sees in the running product: none; no walkthrough.

## Reaches beyond the handoff

- `foundations/part_map.md` lines 1–18 (`decisions`) and 103–115 (`task-cycle`), selectively, for the part-map comparison.
- Greps: `review of its own|reviews of groups|groups of` in `task-cycle/**/*.md`; `WAY-(136|255|134)` in `foundations/invariants.md`, `glossary.md`, `environment_facts.md`; `^### Return step|Return step` in `task-cycle/record_template.md` (lines 202–214, the shape of the *Return step* item).
- `task-cycle/skill/return_step.md` and the handoff, whole.

## Working copies

None made (`.runs/author-return/` not created).

## Unread material

Read in part, as the first report (`author-report.md`) names: the tail of the *Rationale* and the *Rejected* of WAY-316 (after about line 8132 of `foundations/decisions.md`) and the tail of the *Rationale* of WAY-148 (after about line 6373); the *Rejected* of WAY-140, which the range I read did not reach. All four are decisions the change does not touch. Everything else the handoff names was read whole.

## Searches not found or unclear

none
