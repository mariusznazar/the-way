# Author report: agent-work-copies-in-task-directory

**Status:** done

**Commits:** `5f01235` (range `671f470..5f01235`), one commit on `task/agent-work-copies-in-task-directory`. Nothing pushed.

## Files changed (added / removed lines)

| File | + / - |
|---|---|
| `foundations/decisions.md` | 37 / 0 (new decision WAY-373) |
| `task-cycle/skill/SKILL.md` | 35 / 6 (new section "Working copies"; the boundary paragraph, the handoff paragraph, steps 2, 4 and 14) |
| `task-cycle/review/SKILL.md` | 6 / 3 |
| `task-cycle/review/whole_change.md` | 4 / 3 |
| `task-cycle/plan/SKILL.md` | 4 / 2 |
| `task-cycle/change/SKILL.md` | 5 / 0 |
| `task-cycle/change/ui_check.md` | 4 / 1 |
| `task-cycle/record_template.md` | 3 / 0 |
| `task-cycle/skill/request_template.md` | 6 / 1 |

Total: 9 files, 104 insertions, 16 deletions (`git diff --stat HEAD~1`).

## The foundation entry

Row 1 of *Settlements to record*: no entry of the foundation stated the rule (WAY-33 search below), so one decision was written, **WAY-373** (*Scope* `task-cycle`, *Relations* `derives from WAY-148`, *Based on* `none`, *Origin* `none`), by `elements/decisions/skill/SKILL.md` and its template. *Rejected* holds the two ways the task's *Questions to settle* keeps, each with its reason. *Rationale* says in plain words what went wrong (copies outside the task's directory that could not be removed; agents of one cycle overwriting each other's scripts in a shared scratch directory), with no path to the private notes and no count.

- Mark: `row 1`.
- English: An agent of a task cycle makes each working copy to check something in a directory of its own under the task worktree's ignored `.runs/`, removes it before it returns and says in its report where it stood and that it was removed; a failed removal is named with its path, carried to the record and the request, and stops nothing.
- Polish: Agent cyklu robi każdą kopię roboczą do sprawdzenia we własnym podkatalogu w ignorowanym `.runs/` worktree zadania, usuwa ją przed oddaniem wyniku i podaje w raporcie, gdzie stała i że została usunięta; nieudane usunięcie agent wymienia ze ścieżką, cykl przenosi je do zapisu i do opisu PR-a i nie zatrzymuje się.

Choice about *Relations*: `derives from WAY-148` (the reports and the cycle record are where a remainder is carried). Alternative: `none`. Cost if wrong: a relation line that a reviewer finds loose; no check reads it beyond existence.

Search of the whole foundation (WAY-33), once, after the entry was settled: `grep -rn -i -E "scratch|\.runs/|temporary director|working cop|leftover|separate worktree|separate checkout" foundations/ elements/ --include=*.md`, and a search of `foundations/invariants.md`, `glossary.md`, `environment_facts.md` for `.runs`. Findings: WAY-140 (outside effects, not this rule), WAY-148 (reports and record; linked), WAY-316 (screenshot shown to the human, not as a working copy; unchanged), WAY-319 (an agent closes its browser; compatible, no link needed), WAY-154 (`.runs/project-refinement/` of project refinement, another place), the decision on the linter trial's "scratch worktree" (a skill of guidelines, not an agent of the cycle; left alone). No entry stated the rule; no invariant, glossary term or part-map line is touched.

## The rule's place and the answers of the orchestrator

- **One place (answer 2).** The section "Working copies" in `task-cycle/skill/SKILL.md`: its first paragraph is the rule for the agent, its second paragraph is for the orchestrator. The handoff paragraph of that skill has the handoff give the agent's directory and copy the first paragraph word for word (WAY-148), because a stage agent reads its own method and not the orchestrator's skill. Each method then says only "your directory for working copies that the dispatch names".
- **The form of the directory.** `.runs/<name>/` directly under the task worktree's `.runs/`, `<name>` being the stage or role and, where a stage is dispatched more than once, a counter (`author`, `planner`, `executor-3`, `review-whole`, `review-whole-2`); no two agents of a cycle share a name, a resumed agent keeps its own, and `task-cycles` and `worktrees` are never a name. Reason: the smallest form that is unambiguous between two agents of one cycle, matches the role names the cycle already gives report files, and cannot collide with the record's `.runs/task-cycles/`. Alternative rejected: a counter on every name or a subdirectory under `.runs/agents/` (one more level, nothing more unambiguous). Cost if wrong: two names collide and an orchestrator renames one in the handoff.
- **The orchestrator's own copies.** Step 2's clone stands in `.runs/pin/` and step 4's base checkout in `.runs/base/` (the existing `--output ../task-cycles/<task-slug>/gate_times.md` still reaches the record from there, since the checkout is directly under `.runs/`). A failed removal there is a remainder like any other. The answer's "the same rule covers the separate checkouts of the base" is met by the sentence in step 4 and by the second paragraph.
- **The screenshot (answer 3, Q4).** Picked: the agent moves the file the Playwright server saves under its session's directory into its own directory (or to the place the foundation settles for the screenshot shown to the human) and removes the original; a file it cannot move or remove is a remainder. Why: the schema of `browser_take_screenshot` that this session has says the `filename` parameter is "resolved against the workspace root", and the workspace root of the server is the session's, which for a stage agent need not be the task's worktree, and a tool may refuse a place outside its roots; I could not verify that either tool of Claude Code and Codex accepts a place in the agent's directory, so, as the answer says for that case, moving and removing. Alternative rejected: passing the place as `filename`. Cost if wrong: where the original lies in a directory the agent cannot write, the removal fails and a remainder is named, which the rule already handles.
- **The record and the request (task item 3).** Record: one new item *Working copies left* in *Request handoff* of `task-cycle/record_template.md`, after *Writes to the task's backlog entry* and before the corrections (so the process remarks stay the last item). Request: kind 18 in *You accept by merging* in `task-cycle/skill/request_template.md` (plain words in the top part, the paths in *Checks* of the lower part, from the repository's root, so the private-path check passes). Step 14 asks the orchestrator to confirm every remainder is in the record. Smallest place found: an item in a group the headings already hold, so no heading changes and `request_check.py` and `test_request_check.py` needed no change; the two template tests (`TemplateTest` in `task-cycle/test_request_check.py` and `task-cycle/test_remarks_check.py`) passed unchanged. Alternative rejected: a new section of the description (would change the script and its test).

## Places read and decided

Changed: `task-cycle/review/SKILL.md` (the run in a separate worktree; the screenshot sentence; one report line), `task-cycle/review/whole_change.md` (the reviewer's worktrees of the base and head, lines 33-45), `task-cycle/plan/SKILL.md` (the base run; one report clause), `task-cycle/skill/SKILL.md` (boundary paragraph, handoff paragraph, step 2, step 4, step 14, new section), `task-cycle/change/SKILL.md` (a bullet in section 3 and a line of the report in section 6; it also covers the slice, fix and correction variants, which read this skill), `task-cycle/change/ui_check.md` (the screenshot file as a working copy), `task-cycle/record_template.md`, `task-cycle/skill/request_template.md`.

Looked at and left alone: `task-cycle/change/slice.md` (about reading the plan; no copy), `task-cycle/change/fix.md` and `task-cycle/review/fix.md` (they inherit the report and the dispatch's paragraph through their `SKILL.md`), `task-cycle/spec/SKILL.md`, `design.md`, `review.md` (spec agents run no check and write only the spec; the handoff still gives them the paragraph), `task-cycle/plan/too_large.md`, `task-cycle/skill/return_step.md`, `correction.md`, `planning.md`, `blocked_finding.md`, `reserved_return.md`, `spec_review.md`, `plan_member.md` (grep for temp/clone/worktree/copy found only the record's copy under `docs/task-cycles/`, which is the cycle's own record and its removal, not an agent's working copy), `task-cycle/agent-types/*.md` (the type bodies send the agent to its handoff; no edit, so no copy to regenerate), the script `task-cycle/gate_times.py` and others (a registry of running gates under `~/.the-way/`, outside scope), the scripts' tests, the *Rejected* of WAY-316 and the product-guidelines decision on a linter's scratch worktree (a guidelines skill, not a cycle agent).

Not widened (answer 5): no hard block on writing outside the task directory, no removal of task directories after a merge, no cleaning of session scratch directories, no change to what a product's tools make in the temporary directory.

## Checks (each command and exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B gate/run_tests.py task-cycle` | 0 (394 tests OK) |
| `python -B gate/run_tests.py agent-instructions` | 0 (25 tests OK) |
| `python -B gate/run_tests.py instruction-files` | 0 (104 tests, 5 skipped) |
| `python -B gate/run_tests.py elements/common` | 0 (201 tests OK) |

Not run: `python -B agent-instructions/agent_type_copies.py --write` and `python -B agent-instructions/skill_entry_points.py --write` (no agent-type definition and no skill description changed); the whole gate (the orchestrator's run). No test was written: the change is instruction text and one decision, and a text that instructs agents is tested by what an agent does with it (`task-cycle/change/SKILL.md` section 2), which the review does; the decision carries a pair of examples for an agent comparing a change with it. No invariant was written or changed.

## Own-work check

Requirement most likely unmet: every place of `task-cycle/` where an agent makes a copy to check something or removes one names the rule or its place, and a leftover reaches the record and the request. Check: `grep -rn -i "separate worktree\|separate checkout\|scratch run\|scratch worktree" task-cycle --include=*.md`, exit 0, after the commit. It lists two lines: `task-cycle/review/SKILL.md:97` ("a scratch run" in the same bullet, which now says the copy stands in the reviewer's directory) and `task-cycle/skill/SKILL.md:153` (the base checkout, now `.runs/base/` with the pointer). Result: no place left that names a copy with no directory; the record item and request kind exist (`grep -n "Working copies left\|kind 18" task-cycle/record_template.md task-cycle/skill/*.md` finds the item, the kind and the pointer in the section). What the check cannot show: whether an agent given the copied paragraph removes its copy and reports it; that is shown by the first cycle run under it.

## My own working copies (rule 7)

I made no worktree, clone, script or prepared input of a test; `.runs/author/` was not created. One slip: to read the output of the four test runs I redirected it into a text file in the system's temporary directory (`the system's temporary directory`, a file named `x_<pid>.txt`), against the rule I was writing; I removed that file with `rm -f` and listed the directory after (the two other `x_*` entries there, `x_decisions` and `x_environment_facts`, are not mine and stay). Remainders: none.

## Reaches beyond the handoff

- `instruction-files/SKILL.md` and `instruction-files/kind_skill.md` (the handoff said to read the rules of writing an instruction file before editing one; I read these two whole and did not read `kind_main_file.md`, `changing.md`, `writing.md`, `placing.md`, `judging.md`, `tool_loading.md`; none of the files I edited is a main file or a path rule).
- `task-cycle/skill/foundation_step.md`, `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md`, `elements/decisions/template.md`, `elements/decisions/examples.md`, `elements/common/rules.md` and `way_of_working.md`, all whole: the foundation step names them.
- The schema of the Playwright tool `browser_take_screenshot` (loaded through the tool search), for Q4.
- `.gitignore` of the worktree (to confirm `.runs/` is ignored), `elements/...` none further.

## Unread material

- Whole: the handoff, the frozen task, `task-cycle/change/SKILL.md`, `foundation_step.md`, WAY-33, WAY-114, WAY-140, WAY-148, WAY-150, WAY-243, WAY-316 (each by its range up to the next heading), every file I changed (whole before editing, except `task-cycle/skill/SKILL.md`, which I read whole in two parts), `task-cycle/change/slice.md` (read 80 lines, which is the whole file's reading part), `fix.md` of change and review, both agent-type files, `task-cycle/plan/SKILL.md`, `whole_change.md`.
- Not read whole: "the decisions whose *Scope* names `task-cycle`, and the invariants whose *Part* names it or `every`" (step 2 and 3 of "Reading the foundation"): I did the one search the handoff asked for, by what the rule is about, with `grep` over `foundations/` and `elements/`, and read the hits, WAY-154 and WAY-319 and the linter-trial decision around their lines, but not every `task-cycle` decision and not the invariants. Gap risk: a decision or invariant that states the rule in words my search terms miss.
- `foundations/glossary.md` and `foundations/part_map.md` (the handoff names them "as the foundation step gives"): I read the part map's `task-cycle` entry by `grep` only, since I add no term and no file, and did not read the glossary.
- `product-guidelines/reading.md`: not read; the handoff says to read it only if a guideline file for the-way itself exists, and `ls product-guidelines` shows none for the-way (`audit_end.md`, `coding/`, `styleguide/`, `template.md`, `testing/`, `reading.md`).
- `task-cycle/skill/return_step.md`, `correction.md`, `planning.md`, `blocked_finding.md`, `reserved_return.md`, `spec_review.md`, `plan_member.md`, `plan/too_large.md`, `spec/SKILL.md` (read whole), `spec/design.md`, `spec/review.md`: searched with `grep -n -i "temp\|tmp\|clone\|worktree\|copy"`, read the hits only.

## Searches not found or unclear

- none found about the rule's text. Unclear: whether the second paragraph of "Working copies" (orchestrator's) should stand in the section the handoff copies; I split the section so that only the first paragraph is copied, and named that in the handoff paragraph.
- Unclear: "kind 18" in the request template stands under *You accept by merging*, though the item asks the human for no answer and the removal is an action; the other groups ask for an answer, so I kept it in the group of what the human accepts. A reviewer may judge it belongs elsewhere.
- The decision's *Relations* line (`derives from WAY-148`) is a choice, not something the task states.

## Concerns and problems as observed

- A claim in the new section, "it goes when the task's directory goes", rests on a parked task (removal of task directories after a merge), as the task's context says; it is true only once that task is done. I kept the claim because the task's answer states it, and the sentence does not promise a date.
- `git worktree remove --force` followed by `git worktree prune` is written in the rule for a worktree copy; I did not run it here, since I made no worktree. No test covers it.
- No questions.
