# Report of the planner — small fixes from the review of the AI layer and the audit of the process

Status: done with concerns (reaches beyond the dispatch, questions, guidelines uncertain).

- Plan: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan.md`
- Size report: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan-size.md` (last run of `python -B task-cycle/slice_size.py`: exit 0, all eight slices fit; slice 6 and slice 7 read about 64 000 estimated tokens each, slice 1 about 118 000, the rest under 52 000)
- Check result: size check passed for every slice; nothing unchecked; no code or test written, no foundation entry written.

## What the plan is

Eight slices, plus the *Foundation entries* the plan lists (rows 1 to 3 of the task's *Settlements to record*, written by the agent of the *Foundation entries* before slice 1) and one check of the whole change made once by the cycle (point 9's session).

1. Slice 1: move the helper and the two test classes of the versions (`ProcessVersions`, `MeasureVersions`, lines 4230 to 5711) out of `process-audit/test_audit_count.py` (5729 lines, 272 000 characters) into `process-audit/test_process_versions.py`. No behaviour changes. It exists only because the slices of points 4 and 5 change those tests and the large file alone is about 109 000 of the 150 000 tokens of a slice.
2. Slice 2: point 8, `task-cycle/gate_times.py` and its test. Risk: trust boundary, `task-cycle/gate_times.py`.
3. Slice 3: point 9, the new file `elements/common/hand_over.md`, the six skills of the elements and the line of WAY-127's Verification.
4. Slice 4: point 9, the other nine skills.
5. Slice 5: points 1 to 3, three wordings in three files.
6. Slice 6: point 4, the image of each series and Q1 as numbers of cycles (new module `process-audit/series_summary.py`).
7. Slice 7: point 5, the comparison before and after a fix inside each series.
8. Slice 8: points 6 and 7, `process-audit/SKILL.md`, and the docstring of `process-audit/audit_count.py`. Risk: trust boundary, `process-audit/audit_count.py` (it is the only slice that changes the file, so one review of its own).

The orchestrator's answers of step 4 held: trust boundary yes (slices 2 and 8, both marked), irreversible operation none, pin nothing moved. I found no open design choice in the sense of section 2 of the method; the one place where the way of making is a heuristic is named below as question 4.

## Answers to the questions of the handoff

- Where the single place of point 9 stands: `elements/common/hand_over.md`, beside `elements/common/way_of_working.md` (WAY-35: the way of working the skills share stands once in the part the elements share; WAY-256 places such a fragment there). `elements/common/way_of_working.md` stays untouched. The moved text is the hand-over sentences only ("In the-way itself, a skill named below … is read as a file, not called … In a product, it is the project skill of that name with the `the-way-` prefix"). Each of the 15 skills keeps its sentence on where it lives and where the-way lies and gets one instruction that names the file and has it read when the first hand-over comes. The 15 skills are the ones the-way#154 names (found by the phrase "read as a file, not called"): six element skills, `foundation-review`, three of `product-guidelines`, and five of `project-level` (`lead`, `plan`, `skill`, `task`, `technology`). In `project-level/lead/skill/SKILL.md` the second instruction (the brief of a dispatched agent gets the file's path) stays in the skill.
- WAY-127's *Verification* needs a change: its line on "the paragraphs of the skills that say where the-way lies" says that a skill's paragraph names the other skill it hands to as the file read from the checkout; after the move the paragraph points to the shared file. Slice 3 rewords that one line in place and leaves the binding paragraphs, the other lines, the *Rationale* and the *Rejected* of WAY-127 alone. See question 1. The invariant `skill-entry-points` and its test (`gate/test_skills_reach_the_way_sessions.py`, `agent-instructions/test_skill_entry_points.py`) need no change: they hold the entry points, which a skill's body does not enter, and no test or invariant greps the paragraphs of the skills. No description of a skill changes, so no entry point is regenerated; slices 3 and 4 check that `python -B agent-instructions/skill_entry_points.py` reports nothing.
- Which slices change a decision or an invariant sentence: slice 3 changes the Verification line of WAY-127 and nothing else of the foundation; no slice changes an invariant. The agent of the *Foundation entries* writes row 1 and row 2 as sentences of WAY-339 and row 3 as a new decision, as the task's column *Goes to* gives; the *Foundation entries* table of the plan holds exactly those three rows. The part map gets no change from the plan (see question 3).
- The one session of point 9: the section "Check of the whole change, made once" at the end of the plan. It is no test and no slice. After slice 4, on the finished tree, one fresh agent that has the skill tool is given the text of the entry point of one skill that names another the-way skill by name, plus a task that makes it hand on; the check holds where its transcript shows reads of `elements/common/hand_over.md` and of the other skill's `SKILL.md` and no call of the skill tool for a skill of the-way. It says nothing of the other fourteen skills, and the record says so.

## Choices (the table in the plan holds them with the rejected ways and the cost if wrong)

- The size test (`agent-instructions/test_size_invariant.py`) run on the base in a worktree of my own passes: no function or file over 110 or 1200 lines. The largest are `process-audit/version_analysis.py` (1056 lines), `process-audit/record_reading.py` (1052), `process-audit/audit_count.py` (871) and `read_prices` (81 lines), `fill` (66) and `main` of `audit_count.py` (73). So the rule of WAY-365 asks for no move of code first; the new code goes into a new module so that `version_analysis.py` does not pass 1200. The move of slice 1 is a move of tests for the size of a slice, not for WAY-365.
- The nested output of point 8 is read by the summary line of the runner (see question 4).
- The comparison is computed in `process_versions` into a new field of `Versions`, so that `measure_versions` and `main` of `process-audit/audit_count.py` keep their signatures and no code slice touches the trust-boundary file.
- The docstring of `process-audit/audit_count.py` changes in the last slice with the skill.

## Guidelines found missing or uncertain

- `guidelines/testing.md`: no recipe line says how a test of a script that reads the output of a child process should build the output (hand-written text, as `task-cycle/test_gate_times.py` does, or a real run); I took the hand-written form as the file's own example. Not a gap that blocks.
- `guidelines/coding-shared-module.md` lists only `relation-model/fingerprint.py`; the new `process-audit/series_summary.py` is a module that other scripts import, so I named the file in the reading of slices 6 and 7 although its table does not list the modules `version_analysis.py` and `audit_report.py` of the same kind. Uncertain whether the kind covers them.
- `guidelines/coding-command-runner.md` names `task-cycle/gate_times.py` the exemplar of its kind; WAY-199 lets an edit that keeps the rules a script checks from the exemplar (the exit code passed on) go with no approval. Slice 2 keeps them and says so; the reviewer of slice 2 compares.

## Order against the styleguide's example of order of work

Not applicable: the change touches no user interface and the styleguide was not read.

## Reaches beyond the dispatch (what, where, why)

- `task-cycle/skill/foundation_step.md` and `task-cycle/skill/return_step.md` whole, and `task-cycle/skill/SKILL.md` lines 225 to 255 and 430 to 490: to see which agent writes the rows of *Settlements to record* and when (before slice 1 on a planned route), and what *Read* may name.
- `product-guidelines/reading.md` lines 1 to 80: which guideline files a slice of markdown or of code is given.
- `elements/common/way_of_working.md` lines 1 to 40, `elements/common/foundation_check.py` lines 1 to 40, `agent-instructions/skill_entry_points.py` lines 1 to 40, `installation/install.py` lines 140 to 175: the neighbour file of the new one, the command for the check of a slice, what an entry point holds, and where the installer says "where the-way lies".
- `task-cycle/slice_size.py` lines 1 to 60 and `task-cycle/remarks_check.py` lines 1 to 70: the limits (150 000 tokens, 10 files) and what the report's sections must look like.
- `gate/run_tests.py` whole, `gate/test_run_tests.py` by search: the form of the output that point 8 reads. I also ran a made-up failing test whose message holds a nested run of `gate/run_tests.py` in a worktree of my own, to see the real shape (the first nested `== <directory>` has `AssertionError: 0 != 5 : ` before it on its line, the later ones start a line, the nested summary line follows, then the enclosing report's own closing lines).
- Foundation entries by identifier, selectively: WAY-07, WAY-30, WAY-199, WAY-390 (about their first lines and the *Verification*; WAY-07, WAY-30 and WAY-390 only the first 30 to 34 lines each), to judge whether a change of the exemplar and of a decision's Verification needs approval.
- `process-audit/audit_count.py` lines 1 to 445 and 780 to 871, `process-audit/record_reading.py` lines 166 to 232 and its list of definitions, `process-audit/problem_register.py` by search, `process-audit/test_audit_count.py` by the list of its classes and by search: to cut the slices and name the ranges.
- The project skills `project-level/lead/skill/SKILL.md` and `project-level/task/skill/SKILL.md`, the paragraphs of the 15 skills (read as a list of paragraphs, not the skills): to see how the hand-over is worded in each.
- The body of the request the-way#154 through `gh pr view` (public repository, text only): its *Technical changes* and the remarks 4 and 5 that the task's point 9 cites.

## Working copies

- A worktree of the base `268b2b074691a331ed8db136343b4060bdd44539` at `.runs/planner/base` (to run the size test): removed with `git worktree remove --force` and `git worktree prune`.
- A made-up git repository with two directories and one failing outer test at `.runs/planner/sample`: removed.
- Three text files in `.runs/planner/` (a list of the 15 skills' paragraphs, the body of the request, the size test's output): removed. `.runs/planner/` stands empty.
- Nothing remains. No file was written outside `.runs/`.

## Unread material

- `foundations/invariants.md`: I read the nine entries the handoff names and one more (`command-runner-passes-exit-code`) as the part of the file from each heading to the next, not the file.
- `process-audit/audit_count.py` lines 446 to 779 (reading of the locations file, the price list, the repository and `fill`) were not read; I read the function list and the sizes of those functions only.
- `process-audit/record_reading.py`: I read lines 166 to 232 and the list of its definitions; the rest was not read.
- `process-audit/audit_shared.py` was not read; I took its size (120 lines) and its function sizes by an `ast` count.
- `process-audit/problem_register.py` and `process-audit/record_items.py`: not read beyond a search for the classes `Problem` and `Register`.
- `process-audit/test_audit_count.py` and `task-cycle/test_gate_times.py`: the second read to line 320 of 558; the first by the list of its classes and by search only.
- `elements/environment-facts/template.md` lines 95 to 125 and `task-cycle/record_template.md` by the search line of its item (lines 204 to 206), not whole: they are in slice 5's *Change* and its agent reads them whole.
- `process-audit/SKILL.md` I read whole; the 15 skills of point 9 only in the paragraph that holds the sentences (the elements' skills as a list of paragraphs).
- `foundations/part_map.md`, `foundations/glossary.md`, `.runs/index.md`, the task and the sixteen decisions the handoff names (WAY-11, 33, 35, 84, 127, 160, 256, 330, 337, 339, 344, 350, 385, 404, 405, 416) and WAY-365 and WAY-361: read whole.
- Guidelines: all six files the handoff names read whole.

## Searches not found or unclear

- The task gives no shape of the nested output of point 8 and no real record of it: the output that loop2 and the-way produced in the failing runs of 14 and 15 November is not in the task or in the handoff. I derived the shape from a run I made (see reaches), and a real `gate_times.md` of such a run was not seen; slice 2 tests from the shape written out in its Goal.
- The task's wording for the first nested block (`a`, `b`, `c` as false directories) does not say whether the first nested `== <directory>` line stands at the start of a line; in the run I made it does not (text of the failure message is before it), so the first nested directory is no false block and its `Ran` line was the one that gave the enclosing directory a time of 0.012 s.
- `slice_size.py` marks a slice `unchecked` where *Read* names a file that an earlier slice makes, so slice 4 names `elements/common/hand_over.md` in its *Goal* and not in *Read*, and slices 6 to 8 name the new module and the new tests in *Change* and in their goals; the method does not say how a *Read* names such a file.
- WAY-127's *Verification* is the only place that names "the paragraphs of the skills that say where the-way lies"; I found no test or invariant that greps the paragraph, and no other entry of the foundation that names it.
- The part-map sentence of `elements-common` names "the way of working shared by foundation-entry skills"; the new file serves skills that are no foundation-entry skills, and the sentence does not say so. The foundation does not settle whether that wants a change of the map.
- The task's row 3 of *Settlements to record* says "decision" without a title or scope; I left both to the agent of the *Foundation entries*.
- WAY-344 binds a reading of a file that a change reworks; I found none in slices 6 and 7 (the new code reads cycles that `record_reading.py` has already read) and none in slice 2 (the script reads the output of a command, not a file an agent writes), so no slice carries a test that gives a file without a field; the review of each slice answers for that.

## Questions open, with proposed answers and evidence

1. Is the reword of WAY-127's *Verification* line a change that needs the human's approval before the code (WAY-30), or does the return step's correction (WAY-11: whatever no longer matches) cover it? Proposed: it is covered. The line is an example the reviewer compares with (*complies*), not a binding paragraph of WAY-127, whose two paragraphs already say that a skill hands another on by reading its file; the task's own text says the move is what WAY-256 with WAY-35 require. If the orchestrator judges otherwise, drop the line from slice 3 and carry it in a blocked draft request.
2. Should the form line of `**Source:**` at the top of `elements/environment-facts/template.md` (line 35: `… (archived: <address of the archived copy>, <YYYY-MM-DD>) § <place> …`) show the new variant `no archived copy exists in the Internet Archive's CDX index, checked <date>`? Proposed: no, for this change. The task gives wording for the bullet only (point 1) and the plan keeps the form line as it is (slice 5 says so); a reader who reads the form line literally may still block the variant, which is the very trouble that point 1 mends, so the orchestrator may want to add it as a one-line change to slice 5. Evidence: the task's *To do* 1, and `elements/environment-facts/template.md:35` and `:109-111`.
3. Should the sentence of the part `elements-common` in `foundations/part_map.md` (lines 65 to 75, "the way of working shared by foundation-entry skills") name the hand-over file? Proposed: leave it to the return step, which compares the part map of the touched parts; the existing `way_of_working.md` already serves every skill that asks the human and the sentence was not widened for it.
4. Is the way slice 2 reads the nested output acceptable? It is a heuristic with bounded failure: it needs the summary line of the runner, counts the surplus of block lines over the last summary's `<m>`, and reads a run without a recognizable nested run as today. The cases it leaves as today are failed runs whose nested output was cut off. Passing runs, which the audit compares, keep today's rule exactly, and the two existing tests that the task cites stay unchanged. I do not count it an open design choice (WAY-135): it is one local function, cheap to turn back, and it sets no entry; but if the orchestrator sees it as a way costly to turn back, this is the place to return it for a spec. Alternatives and costs are in the *Choices* table.
5. Is the removal of the version-level Q1 line from *Unknown values* (slice 6) what row 3 means? Proposed: yes: row 3 makes Q1 of every group the numbers `yes n · no n · unknown n`, so a version has no Q1 answer that can be unknown; each cycle's unknown, with its reason, stays. If the orchestrator wants the line kept as a count of versions with an unknown cycle, say so before slice 6.
6. Is the form of the check of point 9 acceptable: an agent given the text of an entry point (a subagent cannot start a `/the-way-<name>` command), not a session started by the command? Proposed: yes; it tests what the foundation's sentence tests, whether a skill's text leads an agent to read the file and not to call the skill. It cannot show how Claude Code's own start of a command behaves, and the record should say so.
