# Report — the return step

**Status:** done with concerns (one open question for the orchestrator, under "Searches not found or unclear": the merge of step 12 and WAY-298).

Worktree `the task's worktree root`, branch `task/cycle-technology-decisions-batch`, compared at head `75fe0e3`, range `f238e4f..75fe0e3`.

## Commit

- `5b3eb46` Qualify WAY-298's last sentence as a change to a checkout and give WAY-322's rationale the answer WAY-165 asks for. One file: `foundations/decisions.md` (4 added, 3 removed lines).

## Foundation compared with code

Compared: the entries the change writes or edits (WAY-322 new; WAY-05, 128, 139, 148, 165, 166, 287, 292, 293, 294), the entries of the task's *Decisions in play*, the entries the foundation step's search found, `foundations/part_map.md` for `task-cycle`, `project-level`, `installation`, `elements-common`, `instruction-files`, `agent-instructions`, and the invariants and glossary, each against the files at the head.

What no longer matched, and the correction:

1. **WAY-298, last sentence.** "The fast-forward is the one change the cycle makes outside the task's worktree" contradicted WAY-140 and WAY-107 (the cycle's account of its request in the backlog entry is a write outside the worktree and is allowed) and the cycle skill, which names that account beside the fast-forward at the top. Corrected to "the one change the cycle makes **to a checkout** outside the task's worktree", the wording step 4 of `task-cycle/skill/SKILL.md` already has. The rationale's "one write to the checkout outside the task's worktree" already said it so it stays. No other file quotes the sentence (`git grep 'one change the cycle makes'`).
2. **WAY-322, *Rationale*.** It gave "the tool has no logs, an agent reads the console output" as the answer that settles the logs matter. That answer omits how long the record lives, and WAY-165 (the decision the sentence cites) says an answer settles a matter only if it gives every part the matter asks. The fix of the review (`66d36cd`) had already given `list.md` and `running_product.md` the three-part example and WAY-322's own *Verification* carries it; the *Rationale* still held the short one. Corrected to the three-part example ("the tool prints to the console, the record lives as long as the run, an agent reads it from the terminal"). `git grep 'tool has no logs'` now finds nothing.

Candidates the handoff named and found to hold:

- **WAY-322 and the files that follow it** (`project-level/technology/list.md`, `running_product.md`, `start.md`, `failure_notice.md`): all say the same as the decision after the fix — the five matters (logs, interface, development data, place of the screenshots, how a human learns of a failure) cannot be struck; an answer giving every part settles the matter; a resumed run reads its item like any other. WAY-121 in the base already names four matters of the agent's way including the screenshots, so WAY-322's wording by the family ("a matter of an agent's way to the running product that the step lists") covers the screenshots matter by the decision it derives from, not beyond it. `task_run.md` keeps its own rule that the looks are not taken in a run at a task and a matter enters only where the note touches it; WAY-322 says "stay on the list the step shows", which does not conflict.
- **WAY-148** against `task-cycle/skill/SKILL.md:190-193`, `task-cycle/spec/SKILL.md:53` and `task-cycle/plan/SKILL.md:201-203`: the planner returns a check result, the spec agent runs no check and returns none; consistent.
- **WAY-139** against `project-level/task/skill/resolve_gaps.md`: three items handled apart, the logs-reading item goes as the other items where nothing answers it; same as the decision.
- **WAY-165, WAY-166** against `project-level/definition_template.md` and `settle.md`: "examples of options, none ruled out" and the no-usable-option sentence stand in both.
- **WAY-294** against `task-cycle/remarks_check.py` (`is_report`: `.md` files whose name holds neither `handoff` nor `findings`) and `SKILL.md:140` and the "process remarks check" paragraph: same. The name test is case-sensitive in the code; the decision does not say either way (the foundation step left it to the code on purpose). The files of this very record fit: `19-return-step-report.md` is read, `19-return-step-handoff.md` and `16-fix-findings.md` are not.
- **WAY-287, WAY-291, WAY-292, WAY-293, WAY-295**: match `request_template.md` (items 10 and 11 of the lower part, the section for the human's decisions) and the form check; WAY-293 no longer describes the request template.
- **WAY-306, WAY-150**: unchanged; `task-cycle/skill/correction.md` and step 12 now carry the review of the merge (see the open question below for the word "remote").
- **WAY-128, WAY-259, WAY-05**: matched as the foundation step wrote them; `instruction-files/` changes do not touch them.
- **Part map**: `task-cycle` *Depends on* now lists `installation`; `installation` already lists `task-cycle`, as `installation` and `product-guidelines` already stand. Files of the touched parts all fall under their `**` patterns (the one rename, `elements/common/critique/settle.md` to `settle_review.md`, stays under `elements/common/**`; `git grep` finds no other reference to the old critique file name; the `settle.md` files of `project-level/technology/` and `product-guidelines/` are other files). `project-level/plan_state.py` is a listed trust boundary of `project-level`: its change (item 7) was reviewed in the whole-change review; I did not change its code.
- **Invariants**: `cross-part-imports` and `map-reference-target` hold (the part-map tests run them; see Checks). `project-plan-state-evidence` and `project-plan-state-subprocesses` still hold for the changed `plan_state.py`: the new evidence line is built from a fixed phrase and the record path, the only subprocess is Git. No invariant needs an edit.
- **Glossary**: the words the change uses in a meaning of its own are *agent's way to the running product*, *reserved choice*, *return step* (as the glossary has them) and ordinary words (strike, matter, settle). None is used against its entry.

## Decisions written or changed

By the foundation step (confirmed in its report `02-foundation-entries-report.md` and by `git show --stat` of each commit): WAY-322 new, WAY-05, 128, 139, 148, 165, 166, 287, 292, 293, 294 edited. By this step: WAY-298 (last sentence) and WAY-322 (*Rationale*), both corrections of wording, in `5b3eb46`.

## Invariants, environment facts, glossary terms, part-map changes

None written or changed by this step. The part-map change (`installation` in `task-cycle`'s *Depends on*) was written in the change by `6349019`.

## Projected entries

None; the task is independent of a project definition.

## Rows of *Settlements to record* written

Each carried by a commit of `foundations/decisions.md` (checked with `git show --stat`):

| Row | Entry | Commit |
|---|---|---|
| 1 | WAY-322 (new) | `f3b90d5` |
| 2 | WAY-166 | `2ec17d4` |
| 3 | WAY-139 | `a0c6607` |
| 4 | WAY-148 | `a407365` |
| 5 | WAY-294 | `932726d` |

No row missed by the foundation step. No choice binding after the merge was found that the foundation step missed (the one near candidate is the open question below).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py --skip-test-citations`: 0 (0 errors), before and after `5b3eb46`.
- `python -B gate/run_tests.py elements/part-map`: 0 (39 tests), before and after `5b3eb46`; this run holds `cross-part-imports` and `map-reference-target`.
- `git diff --check`: 0.
- Not run: the whole gate (the return step does not run the suite) and `gate/run_tests.py` on other directories (this step changed only `foundations/decisions.md`; the directories of the change were run by the slices and the fix, see `17-fix-report.md`).

## Own-work check

- Requirement most likely not met: after my edits no text still gives the short logs answer as sufficient, and no text still counts the fast-forward as the only change outside the worktree. Checks: `git grep -n 'tool has no logs' -- . ':!.runs'` finds nothing (exit 1); `git grep -n 'one change the cycle makes'` finds only step 4 of `task-cycle/skill/SKILL.md`, which already carries "to a checkout". The foundation check passes.

## Reaches beyond the handoff

- `foundations/decisions.md`: WAY-107, WAY-140, WAY-153, WAY-306, WAY-121 and WAY-322 read whole (the handoff names WAY-298 and the task's list; WAY-107 and WAY-140 for the account of the request, WAY-153 for the plan-state reader, WAY-306 for the merge review, WAY-121 for the family of matters).
- `foundations/invariants.md` and `foundations/glossary.md`: headings listed, and the entries of the invariants named above and the glossary entries *agent's way to the running product*, *reserved choice*, *return step* read.
- `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md` (the skill of the element, for the two edits).
- `README.md:112-125` and plan slice 9, for item 27's first bullet (the sentence already said what WAY-09 gives).

## Searches not found or unclear

- **Open question: the merge of step 12 and WAY-298.** Task item 2 says step 12 merges the remote target branch "as WAY-298 justifies". WAY-298's sentence ("the merge of the target branch it makes takes the remote branch, in a product as well") stands in the sentence about a correction after review, and its *Verification* names only a correction. WAY-306 says "the current target branch". So the foundation does not state in so many words that the merge before the request opens takes the remote branch; step 12 of the skill does (the reasoning of WAY-298's *Rationale* applies to it unchanged). I did not widen WAY-298: that would extend an approved decision beyond what the task's settlements row gives (no row names it; WAY-114), and the skill stricter than the decision contradicts nothing. Recommendation: leave as it is; if the human wants it in the log, one clause in WAY-298 ("the merge of the target branch the cycle makes, before the request opens as in a correction, takes the remote branch"). Cost of leaving: a reader who looks for the step-12 rule in the foundation finds its reason in WAY-298's rationale but not its sentence.
- Line 119 of `task-cycle/skill/SKILL.md` (and one in `project-level/task/skill/read_sources.md:23`, `request_template.md:171`, `definition_template.md:185-186`) run past the roughly 100-column wrap of the neighbouring lines; the checks do not mind. Not changed.
- None else.

## Choices

- WAY-298: qualified the last sentence rather than leaving the contradiction with WAY-140 and the skill. Rejected: leaving it (the handoff names it as a candidate and the skill already carries the qualifier). Cost if wrong: one clause reverted.
- WAY-322 *Rationale*: reworded the example instead of removing it. Rejected: dropping the example (it carries the point that the answer is one sentence). Cost if wrong: one sentence changed back.
- Item 7 (`plan_state.py`): not touched, as the handoff says.

## Problems observed

None beyond the above.
