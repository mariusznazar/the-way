FAIL 5f01235516299634098e655e21ff28f845e82ae8

# Review of the whole change: agent-work-copies-in-task-directory

Range `671f4701880323623d40bd7fe86a7ead55f98681..5f01235` (one commit, `git rev-parse HEAD` in the reviewed worktree printed `5f01235516299634098e655e21ff28f845e82ae8`, the dispatch's head). No spec, no plan, no slice, no earlier review. The reviewed worktree, its index and its branch were not changed (`git status --short` empty before and after).

Counts: 1 blocking, 3 Minor within the task, 0 out of scope.

## Findings

### Critical

none

### Important (blocking, within the task)

**I-1. The rule's sentence on files a tool writes by itself is broader than the task, the binding answer and the decision.**
Place: `task-cycle/skill/SKILL.md:290-292` ("A file that a tool writes by itself outside that directory, such as the screenshot the Playwright server saves under its session's directory, is moved into the agent's directory and the original removed"). This sentence is in the first paragraph of "Working copies", which the handoff of every agent copies word for word, so it binds every agent.

What is wrong: the task asks for one thing here, in *Questions carried to cycle* (the screenshot the Playwright server writes under its session's directory: move and remove, or give the server the place). The author generalised it to every file "a tool writes by itself outside that directory". That reaches the temporary files a product's tools and tests make in the system's temporary directory (a test runner's temporary directories, a build cache, a bytecode cache), which the task's *Out of scope* (second item) leaves to the task of the hard block, and which binding answer 5 of `author-handoff.md` repeats as out of scope. WAY-373, the decision this change writes, says nothing about files a tool writes by itself; the paragraph restates it more broadly. By section 3 of the review method (WAY-263), a change whose files restate an entry it writes more broadly is Important. The other two places that carry the screenshot case (`task-cycle/review/SKILL.md:95-96`, `task-cycle/change/ui_check.md`) are correctly narrow ("the file the screenshot tool writes by itself").

Why it matters: an agent that runs the focused tests of the-way or of a product is told to move every temporary file those tests create into its directory and delete the original; it cannot comply, the rule stops being checkable, and the reviewer of the next cycle has no line between an agent that broke it and one that could not follow it.

Evidence: the sentence in the diff (`git diff 671f470..5f01235 -- task-cycle/skill/SKILL.md`), the task's *Out of scope* bullet 2 ("Pliki tymczasowe, które narzędzia i testy produktu tworzą same w katalogu tymczasowym systemu"), answer 5 of the author's handoff, and the text of WAY-373 (`foundations/decisions.md:12841-12877`), which has no such clause. Suggested fix: narrow the sentence to the screenshot a screenshot tool saves by itself (as the other two places do), or state in the decision and in the paragraph that a product's own tools and tests are outside it.

### Minor (within the task; the cycle can cut these into the fix)

**M-1. The request's section for the human's decisions gets an item that, by its own words, asks for nothing, and WAY-287 is not changed or linked.**
Places: `task-cycle/skill/request_template.md:338-341` (kind 18, under *You accept by merging*) against `task-cycle/skill/request_template.md:183` ("Everything whose merge needs the human's yes, and nothing else") and its own text ("that nothing waits for it"); WAY-287 (`foundations/decisions.md:9473`), whose list of what the section holds is closed ("holds everything whose merge needs the human's yes") and whose `none` says that nothing waits for a yes; WAY-373's *Relations* line (`derives from WAY-148`) names neither WAY-287 nor WAY-286.
What is wrong: a request with a leftover copy no longer reads `none` in the section although nothing waits for the human's yes, and the third group is defined as "what the cycle did within its authority", which a failed removal is not. The author names this doubt in its report. The task asks that the human see the remainder in the description, so the top part is a defensible place; what is missing is the foundation saying so.
Why it matters: a reader comparing the template with WAY-287 finds a kind the decision does not list; the `none` of the section loses its meaning in the requests that carry a remainder. Cost today is low (a rare, informational item).
Suggested fix: add WAY-287 (and WAY-286) to the decision's *Relations* and either list the remainder among the items WAY-287 names or reword the section's definition so it admits an informational item; or place the item in the lower part, *Checks*, and keep a single plain sentence in the top part.

**M-2. Nothing tells the orchestrator how it learns of a remainder before step 14.**
Place: `task-cycle/skill/SKILL.md:301-306` (second paragraph of "Working copies") and step 14 (`task-cycle/skill/SKILL.md:567-568`).
What is wrong: the short return an agent gives (status, commits, one-line check result, report path; WAY-148) does not carry a failed removal, a failed removal is no failed check, and routine progression does not reread full reports. The paragraph says "a remainder that a report names ... write it into the record", and step 14 asks the orchestrator to confirm the record lists every remainder "that a report names", but no step has it read the working-copies line of a report when the agent returns, as WAY-326 has it read **Unread material** in every report.
Why it matters: the remainder reaches the record and the request only if the orchestrator reads every report to the end at step 14; a remainder of an early agent can be missed, and the human sees nothing. Suggested fix: have the orchestrator read the working-copies line of each report when the agent returns (as it reads **Unread material**), or have the short return name a remainder.

**M-3. Line lengths and a ragged rewrap of the changed paragraphs.**
Places: `task-cycle/skill/SKILL.md:47` (a line of three words), `:77-78`, `:155`, `:186`, `:568`; `task-cycle/review/SKILL.md:99` (141 characters); `task-cycle/plan/SKILL.md:180-181`; `task-cycle/skill/request_template.md:340` (156); `foundations/decisions.md:12870` and `:12872` (110 and 149). The files wrap at about 100 characters; the edited paragraphs were patched in place without rewrapping. The gate's tests do not check it; it makes the diff of the next change to these paragraphs noisier. Polish only.

## Check against the task

- *To do* 1 (directory of its own under `.runs/`, one for each agent, never the system's temporary directory, the session's scratch directory or the main checkout; the places the task names): met. `task-cycle/review/SKILL.md:97-99`, `task-cycle/plan/SKILL.md:179-181`, the boundary paragraph and the handoff paragraph of `task-cycle/skill/SKILL.md` (`:77-78`, `:182-186`), plus `whole_change.md`, `change/SKILL.md:96-98`, `ui_check.md`, step 2 (`.runs/pin/`) and step 4 (`.runs/base/`). Searched `task-cycle/**/*.md` for `worktree|clone|checkout|scratch|tmp|temp`: no further place where an agent makes a copy to check something without a directory. The reviewed handoff gave me `.runs/review-whole/`, the same form as the rule's `<name>`; the paragraph the handoff copies matches the section word for word.
- *To do* 2 (remove before returning, keep in `reports/` what the report needs, say where the copy stood and that it was removed): met, in the first paragraph of the section and one report line each in `change/SKILL.md`, `plan/SKILL.md` and `review/SKILL.md`. Every agent's handoff carries the paragraph, so spec agents and the return-step agent are bound through it.
- *To do* 3 (failed removal: finish, name the remainder with its path; orchestrator carries it to the record and the description; also the base checkouts of step 4): met in text (rule, record item *Working copies left*, kind 18, step 14, step 4's `.runs/base/`); the gap is how the orchestrator learns of it (M-2) and where the item stands (M-1). `--output ../task-cycles/<task-slug>/gate_times.md` still reaches the record directory from `.runs/base/`.
- *Questions to settle* (where it stands, who removes it, failed removal does not stop the cycle): met; the two roads the human rejected are in *Rejected* of WAY-373 with the task's reasons. *Questions carried to cycle*: the directory form (`.runs/<name>/`, one per agent role, with a counter) is stated in one place, reasoned in the author's report, and `task-cycles`, `worktrees` are excluded as names; other directories of `.runs/` (`project-refinement`, `coding`, `styleguide`, `technology`) belong to other skills and do not collide with the cycle's agent names. The screenshot: moving and removing was chosen as binding answer 3 permits; the author's reason (could not verify that the tools of Claude Code and Codex accept a place under the agent's directory) is stated; I could not verify it either (see Searches).
- *Out of scope*: no hard block, no removal of task directories, no cleaning of session scratch directories added. The temporary files of a product's tools: touched by I-1.
- *Settlements to record*, row 1: carried out by WAY-373 (`foundations/decisions.md:12841`), *Scope* `task-cycle`, *Rationale* and *Rejected* from the task with no path to private notes and no count. Source fidelity: no invented outcome beyond I-1; "it goes when the task's directory goes" is the task's own answer and the author reports that it depends on a parked task.
- Own-work check of the author: the grep for `separate worktree|separate checkout|scratch run|scratch worktree` would catch a place left without a directory; it cannot catch a sentence that says too much, which is where the change is weakest (I-1).

## Against the foundation

- WAY-373 compared with the code it describes: the first paragraph of the section, the review/plan/change/ui_check places and the record and request additions do what the decision says, except the broader sentence (I-1) and the request item (M-1).
- WAY-148 (the record is the only log; handoff may copy a passage word for word): consistent; the copy of the paragraph in each handoff is the allowed form. WAY-125/256 (method read at its step, fragment place): the rule is copied by the handoff rather than read by each agent from the orchestrator's skill, a reasonable fit.
- WAY-308/309 (record and description cleaned of absolute paths): the report names a "full path", the record item and kind 18 ask for the path from the repository's root; the cleaning of the record copy can replace the absolute form. No absolute path or note link in the added lines (`git diff ... | grep` for a drive letter, `[[`, `/Users/`: nothing).
- WAY-316/317/318 (screenshots): the screenshot as a working copy and the screenshot shown to the human are kept apart in `ui_check.md`; the invariants `record-copy-image-check` and `record-copy-image-files` are untouched and would list a screenshot kept under `reports/`.
- WAY-298 (the one write to a checkout outside the task's worktree is the fast-forward): consistent with the boundary paragraph.
- WAY-361/362 (reviewer's runs in a worktree of the base and one of the head): the runs now stand in the reviewer's directory; consistent.
- Invariants: all 33 read whole; the ones the change could reach (`tracked-file-private-paths`, `skill-entry-points`, `outbound-link-reach`, `record-copy-image-*`) hold by the checks below; no invariant, test or part-map line changed. No changed invariant test.
- No reserved choice taken (no language, framework, library, store, login or place to run settled).
- Structure of the code: only Markdown changed, no code and no test. `python -B task-cycle/change_file_sizes.py 671f470 5f01235` (exit 0): `foundations/decisions.md` 12886 to 12923 (+37); `task-cycle/skill/SKILL.md` 667 to 696 (+29); `task-cycle/skill/request_template.md` 508 to 513 (+5); `task-cycle/change/SKILL.md` 164 to 169; `task-cycle/record_template.md` 228 to 231; `task-cycle/review/SKILL.md` 175 to 178; `task-cycle/plan/SKILL.md` 223 to 225; `task-cycle/change/ui_check.md` 18 to 21; `task-cycle/review/whole_change.md` 51 to 52; total +88. The-way has no `guidelines/coding.md` (WAY-328), so there is no test of a rule of size to run on the base and the head; no function, no code without a user, no name that stopped being true (the phrase "separate worktree" is gone from the places changed; `review/SKILL.md:97` keeps "a scratch run", a run, not a copy). No structure finding.

## Declined to judge

- Whether the stated reason for moving rather than redirecting the Playwright screenshot is right (the tools' behaviour in Claude Code and Codex): outside what a review of the text can show; the binding answer allowed either way.
- The parked task of removing task directories after a merge, on which "it goes when the task's directory goes" rests: outside the task.
- Product tools' own temporary files in the system's temporary directory: outside the task (but see I-1 for the sentence that reaches them).
- Other task branches that touch step 4 of the same skill (a branch `task/base-checks-place` exists in this repository): not part of this range.

## Checks I ran

All in a worktree of the head commit `5f01235` in my directory `.runs/review-whole/head/` (removed, see below), except the file-size script and the greps, which only read the reviewed worktree.

| Check | Command | Exit |
|---|---|---|
| foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| task-cycle tests | `python -B gate/run_tests.py task-cycle` | 0 (394 tests OK) |
| instruction-files tests | `python -B gate/run_tests.py instruction-files` | 0 (104 tests, 5 skipped) |
| agent-instructions tests | `python -B gate/run_tests.py agent-instructions` | 0 (25 tests OK) |
| sizes of changed files | `python -B task-cycle/change_file_sizes.py 671f4701880323623d40bd7fe86a7ead55f98681 5f01235` (reviewed worktree) | 0 |
| private paths in added lines | `git diff 671f470..5f01235 \| grep '^+' \| grep -nE '[A-Za-z]:[\\/]\|\[\[\|/home/\|/Users/'` | no match |
| places that name a copy without a directory | `grep -rn "separate worktree\|separate checkout\|scratch\|\btemp\b\|tmp" task-cycle --include=*.md` | two lines, both now with a directory or a run, not a copy |

Not run: `gate/run_tests.py elements/common` (the author reported it, I did not repeat it; the change touches no file of that part), the whole gate (the orchestrator's run), `agent_type_copies.py` and `skill_entry_points.py --write` (no agent-type definition or skill description changed; `agent-instructions` tests, which hold the copies, pass).

## Reaches beyond the dispatch

- `foundations/part_map.md` (whole of the entries of `decisions` and `task-cycle`, and the headings of the rest): to assign the changed files to parts, as "Reading the foundation" step 1 gives.
- `foundations/invariants.md` whole and `foundations/glossary.md` (entries `agent's way to the running product`, `foundation step`, `gate` and the file's intro): "Reading the foundation" steps 3 and 4.
- `task-cycle/skill/correction.md` (first 40 lines), `elements/common/way_of_working.md` lines 40-130: to see where else a copy of a branch is made and how the foundation is selected.
- `grep` across `foundations/`, `task-cycle/` and the repository for `.runs`, `worktree`, `checkout`, `scratch`, `clone`, `temporary`: to find a decision or place that states or contradicts the rule.
- `git worktree list`: to confirm my worktree was removed; it shows many worktrees left by other cycles under `.runs/` (outside this change).

## Working copies

- One: a worktree of the head commit `5f01235` at `.runs/review-whole/head/`, made with `git worktree add --detach`. Beside it, in `.runs/review-whole/`: my scripts `scope.py` and `scope.txt` (list of decisions whose *Scope* names `task-cycle`) and the output files `fc.txt`, `tc.txt`, `if.txt`, `ai.txt` of the checks above.
- Removed with `git worktree remove --force` (exit 0) and `git worktree prune`, then `rm -rf .runs/review-whole` (exit 0). `git worktree list` afterwards no longer shows it, and `ls .runs` of the reviewed worktree shows only `task-cycles/`. Kept in `reports/`: nothing but this report. Remainders: none.
- I wrote nothing to the system's temporary directory or the session's scratch directory.

## Unread material

Counts (WAY-150): the selection holds 137 decisions whose *Scope* names `task-cycle` (found by taking each `- **Scope:**` line with its continuation lines in `foundations/decisions.md`; the new WAY-373 included). **31 read whole, 106 run through by title only.** Read whole: WAY-125, WAY-136, WAY-140, WAY-148, WAY-160, WAY-227, WAY-256, WAY-260, WAY-261, WAY-262, WAY-269, WAY-286, WAY-287, WAY-289, WAY-294, WAY-295, WAY-296, WAY-298, WAY-308, WAY-309, WAY-316, WAY-317, WAY-318, WAY-319, WAY-326, WAY-349, WAY-361, WAY-362, WAY-363, WAY-367 and WAY-373 (in the diff).

Decisions that bear on the change and stayed unread (title only): WAY-33 (what the author of a foundation change searches for; the author read it whole and I judged its result, the search, from the rule text and my own greps), WAY-114 (what a human accepts of an entry), WAY-127 (a session reads skills from the directory it works in), WAY-150 (I read its method in `way_of_working.md`, not the entry), WAY-161 (grading and fixing of findings), WAY-255 (waiting for a long command). The other 100 decisions were run through by title and none points to a bearing on the change.

Guidelines: the-way has no guidelines files of its own (no `guidelines/` directory; WAY-328), so `product-guidelines/reading.md` was not read. The glossary: of 21 entries I read the intro and three whole (`agent's way to the running product`, `foundation step`, `gate`); the others I saw by heading only, since the change uses none of their terms. The part map: entries `decisions` and `task-cycle` whole, plus the lines up to the `agent-instructions` entry; the rest by heading. The orchestrator's `task-cycle/skill/SKILL.md` was read in the changed regions and their surroundings (lines 30-199, 274-313, and the diff), not whole; `task-cycle/skill/request_template.md` lines 180-380 and the diff, not whole.

## Searches not found or unclear

- I looked for a decision or invariant that states or contradicts the rule (copies in `.runs/`, removal of a copy, a remainder reaching the record and the request): none states it; no invariant touches it. The closest are WAY-148, WAY-316/317/318 (screenshots) and WAY-361 (the reviewer's worktrees), all consistent with WAY-373.
- Unclear: whether the Playwright tool of Claude Code and the one of Codex accept a `filename` under an agent's directory; the author's schema reading and the binding answer leave moving the file; I did not load the tool's schema.
- Unclear: whether a remainder belongs in the top part of the request (kind 18) or in the lower part (M-1).
- Unclear: which agent, if any, reads the working-copies line of a report on its return (M-2).
