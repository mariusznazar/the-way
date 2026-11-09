# Plan — the way: zadanie zbiorcze z uwag PR-ów — cykl zadania, krok technologii, brzmienie decyzji

- Task: .runs/task-cycles/cycle-technology-decisions-batch/task.md
- Spec: none
- Base: f238e4ffdfc2396ae0009fefa90b3af8d1e931e1

The task's line numbers come from older commits of `foundations` (`a3206c1`, `f218b55`); the base is
`f238e4f`, 46 commits later, and the text has moved. Every slice finds each place by its content.
Where the current text of a place already says what its item asks, the slice changes nothing there and
says so in its report. Item numbers below are the numbers of the task's *To do*.

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Foundation entries row 1 — the four matters of an agent's way to the running product (logs, interface, development data, failure notice) cannot be struck from the technology list; the human answers them like any choice and the answer settles them | decision | row 1 of *Settlements to record* (question 1) | Slice 6, Slice 9 |
| Foundation entries row 2 — when no option of the agent's access to the running product can be used by an agent, the step recommends by the other consequences and says in one sentence that the check stays with the human | decision | row 2 of *Settlements to record* (question 2) | Slice 6, Slice 9 |
| Foundation entries row 3 — the deployment-skill item "how to read the logs" is tied to the logs decision as the items on the record's life and on a failure are | decision | row 3 of *Settlements to record* (question 3) | Slice 8 |
| Foundation entries row 4 — every stage that runs a test or another check gives the check-result line in its short return, not only a stage that checks the product (this is also the whole of item 24) | decision | row 4 of *Settlements to record* (question 5) | none; Slice 10 changes the same file after it |
| Foundation entries row 5 — the reports the remarks script reads are the `.md` files of `reports/` whose name holds neither `handoff` nor `findings` | decision | row 5 of *Settlements to record* | Slice 4 |
| Foundation entries item 17 — WAY-165 reworded in place at three points: development-data options named as examples and not a closed pair; the reservation about opening a decision only on the human's word limited to decisions of the foundation; no citation of WAY-270 in the sentence on an entry that answers part of a matter, and the relation to WAY-270 kept only where another sentence rests on it | decision, reworded in place | item 17 of *To do*; accepted with the document (WAY-30, task *Context*) | Slice 6 (the same sentence in `project-level/definition_template.md`) |
| Foundation entries item 18 — WAY-166: the example of compliance has the server container's output kept in a store that outlives a redeployment | decision, reworded in place | item 18 of *To do* | none |
| Foundation entries item 19 — WAY-128: the closing sentence on process skills and their entry points names WAY-259 as well | decision, reworded in place | item 19 of *To do* | none |
| Foundation entries item 20 — WAY-292: *Verification* says the form check reports the repeated block wherever it reads the task document as English | decision, reworded in place | item 20 of *To do* | none |
| Foundation entries item 21 — WAY-05: *Verification* in two pairs of `complies` and `violates` | decision, reworded in place | item 21 of *To do* | none |
| Foundation entries item 22 — WAY-293: *Rationale* without a description of what the request template does or lacks today; the rejected way "no change, which withdraws the rule" says that no change leaves the return step without a precedence | decision, reworded in place | item 22 of *To do* | none |
| Foundation entries item 23 — WAY-287: the list names also a listing of the remarks check held wrong (WAY-295) and an error of the form check held wrong (WAY-291) | decision, reworded in place | item 23 of *To do* | none |

Whether a row becomes a new decision or an edit in place of WAY-121, WAY-139, WAY-148, WAY-165,
WAY-166 or WAY-294 is for the writer of the foundation step (WAY-134, WAY-07); the plan names the rows
and words nothing. No projected entry is carried, and there is no spec.

The rewordings of items 17 to 23 are named here as entries, and are not slices, because the size script
counts a changed file whole: `foundations/decisions.md` alone is about 755,000 characters, above the
limit of one slice, and cannot be cut. The foundation step writes entries named by the plan
(`task-cycle/skill/foundation_step.md`), through the skill of the decisions element, on the class WAY-229
gives the writer of a plan's entries, with the search of the whole foundation of WAY-33 for each; the
entry's first sentence above says the change, never its wording. The review of the whole change reads
them against the task's items 17 to 23 and 24.

## Slices

### Slice 1 — The cycle skill's merge, base-check and exception sentences

- **Goal:** `task-cycle/skill/SKILL.md` and `task-cycle/skill/correction.md` say, each place found by its content: (item 1) the correction's merge of the remote target branch — both places in `correction.md` that merge it — does there what step 12 does with its merge: where the merge changes code the cycle reviewed, a fresh reviewer reviews the merge with `review-change` as step 12 gives (WAY-306), and the checks the merge touches run again; (item 2) step 12 merges the remote target branch, not "the current target branch", as `correction.md` and WAY-298 give, in a product too; (item 3) the sentence "The cycle writes only in the task's worktree and changes nothing outside the product repository" names as its exception the fast-forward of the checkout in step 4, and the paragraph does not end with two things each called "the one exception"; (item 5) step 4's second way of running the base checks, a separate copy of the base commit under the worktree's ignored `.runs/`, says that in a product the copy gets its dependencies installed, as the product's own rules give, and its `.the-way` populated before the checks run, since otherwise they fail for that reason and not on the base. Prose only; no other rule changes.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/skill/correction.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:28-30` To do, items 1 to 3 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:32-32` To do, item 5 · `foundations/decisions.md:9370-9425` WAY-298 · `foundations/decisions.md:9675-9715` WAY-306 · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `python -B gate/run_tests.py task-cycle` · `git diff --check`
- **Depends on:** none

### Slice 2 — The slice executor's current ranges and the request template's two pointers

- **Goal:** (item 4) `task-cycle/change/slice.md` says that where the ranges of lines the dispatch gives differ from the ranges in the plan, the dispatch's current ranges hold, as `task-cycle/skill/planning.md` ("A slice's handoff") gives the orchestrator; (item 6, first point) in `task-cycle/skill/request_template.md` the item of *For you to decide* on *Questions* points to `task-cycle/skill/foundation_step.md`, the file that says which questions the foundation step allows; (item 6, second point) the item on additions to a product's logging scope says where the author of the request finds them: in the diff of the change to the product's logging-scope rule (WAY-274). Prose only.
- **Change:** `task-cycle/change/slice.md` · `task-cycle/skill/request_template.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:31-31` To do, item 4 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:33-35` To do, item 6 · `task-cycle/skill/planning.md:26-37` A slice's handoff · `task-cycle/skill/foundation_step.md` · `foundations/decisions.md:4119-4179` WAY-148 · `foundations/decisions.md:8480-8529` WAY-274 · `foundations/decisions.md:8982-9024` WAY-287 · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_request_check.py"` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** none

### Slice 3 — A blocked draft request shown as blocked by the plan-state reader

- **Goal:** (item 7) a task whose cycle ended in a blocked draft request opened after the record was written is reported by `project-level/plan_state.py` as blocked, not as a task with no request. The record's field *Request URL and status* then reads `blocked draft, opened on this commit` — the wording `task-cycle/skill/reserved_return.md` (step 2 of "Open the request") already gives — and `task-cycle/skill/blocked_finding.md` says the same of its record copy, which is committed before the request exists; the script recognises that wording on the field's line in an archived record, in the same way and from the same Git reads that it finds the pointer to a request today (`record_pointers`, `PR_LINK`), and prints one evidence line for such a record naming the task, the commit and the record file and saying the request is a blocked draft. The line is built from fixed words and the match; no other text of the record reaches the output (test `test_record_instructions_are_data_and_markdown_is_not_part_of_pr_url` is the precedent). It adds no proposal, no conflict, no exit code and changes no existing line (the surface `project-plan-state-command`); every subprocess it starts is Git (`project-plan-state-subprocesses`). Write first a test in `project-level/test_plan_state.py` that fails for the reason stated, using the fixture helpers there (`archive`, `cycle`, `run_reader`), and make it pass; the test covers a record carrying the wording, a record carrying look-alike text elsewhere (not on the field's line), and a record with a real pull-request URL, which keeps its existing pointer line.
- **Change:** `project-level/plan_state.py` · `project-level/test_plan_state.py` · `task-cycle/skill/blocked_finding.md` · `task-cycle/skill/reserved_return.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:36-36` To do, item 7 · `task-cycle/record_template.md:176-195` Request handoff · `foundations/decisions.md:4302-4333` WAY-153 · `foundations/decisions.md:4678-4715` WAY-163 · `foundations/decisions.md:8228-8292` WAY-269 · `foundations/invariants.md:301-327` project-plan-state-evidence and project-plan-state-subprocesses · `foundations/part_map.md:77-101` project-level and task-cycle · `foundations/part_map.md:203-210` project-plan-state-command · `project-level/test_plan_state_invariant.py:290-345` tests citing project-plan-state-evidence
- **Model:** same — a script that reads untrusted record text at a trust boundary and keeps a pinned output surface
- **Risk:** trust boundary — `project-level/plan_state.py` is named as a trust boundary by the part map entry `project-level`
- **Checks:** `python -B -m unittest discover -s project-level -p "test_plan_state.py"` (the new test first fails, then passes) · `python -B gate/run_tests.py project-level` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** none

### Slice 4 — The remarks script reads reports by name

- **Goal:** (item 8 and row 5) `task-cycle/remarks_check.py` reads as reports every `.md` file of `reports/` whose name holds neither `handoff` nor `findings`, in the order of their names; a handoff, a findings file and any file that is not `.md` are not read. The module docstring says it in the words item 8 gives, and its description of what an item of a section is says what the code does (a paragraph after a list is an item too), in the words item 8 gives. `test_only_files_whose_name_ends_in_report_are_read` in `task-cycle/test_remarks_check.py` becomes a test of the new rule with the files item 8 names: `review_whole.md` and `report-planner.md` are read; `01-author-handoff.md`, `handoff_author.md`, `slice-1-findings.md`, `notes.txt` and `gate.log` are not; write that test first and see it fail. Where no test pins that a paragraph after a list is read as an item, add one. In `task-cycle/skill/SKILL.md` the sentence that says where a stage's handoff stands in `reports/` says it is a file whose name holds `handoff`, and the sentence under "The process remarks check" that says which reports the script reads adds ", a file whose name holds neither `handoff` nor `findings`"; the script's exit codes stay as they are. The match on the names is a literal, case-sensitive match of the two words, as the settlement words it.
- **Change:** `task-cycle/remarks_check.py` · `task-cycle/test_remarks_check.py` · `task-cycle/skill/SKILL.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:37-41` To do, item 8 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:166-169` Settlements to record, header · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:174-174` Settlements to record, row 5 · Foundation entries row 5 · `foundations/decisions.md:9235-9274` WAY-294 · `foundations/decisions.md:9275-9307` WAY-295 · `foundations/decisions.md:9308-9329` WAY-296 · `task-cycle/record_template.md:176-195` Request handoff · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` (the rewritten test first fails, then passes) · `python -B gate/run_tests.py task-cycle` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** Slice 1 · Foundation entries row 5

### Slice 5 — The installer test no longer depends on the commit that is current when it runs

- **Goal:** (item 9) `installation/test_install.py`: the test `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink`, and any other test in the file that compares with `self.commit` taken in `setUp`, does not fail when someone commits to the-way's own repository while the full test run is going. The expected commit is taken from what the test installs from, at the point it installs, not from a read made earlier of the live repository's head (the places: `setUp`, `installed_from_a_remote`, `later_process`, the assertions of that test and of `test_guidance_names_only_scripts_the_pinned_commit_holds`). No change to the installer's behaviour and to `installation/install.py`. Show the failure the item describes before the fix, for example with a throwaway copy of the repository in which a commit is made between `setUp` and the install, and say in the report how it was shown.
- **Change:** `installation/test_install.py`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:42-42` To do, item 9 · `installation/README.md:78-116` Moving the pin · `foundations/invariants.md:291-299` installation-claude-guidance · `foundations/part_map.md:157-165` installation · `foundations/decisions.md:905-940` WAY-34
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s installation -p "test_install.py"` · `python -B -m unittest discover -s installation -p "test_installed_guidance.py"` · `git diff --check`
- **Depends on:** none

### Slice 6 — The technology step: listed matters, resumed runs and recommendation

- **Goal:** the skill `project-level/technology/` says, each place found by its content: (item 10) when the step shows the list for confirmation, the matters of the logs, the interface, the development data and the failure notice cannot be struck from it; the human to whom a matter does not apply answers it like any choice, and that answer settles it, so on resuming it does not return as open (`list.md`, `start.md`, `running_product.md`); (item 11) a run at a task interrupted between writing the note and writing its item, once resumed, lists the choice of that note and does not close without it (`task_run.md`, the bullets of "Start" on a list with a note the section already holds and on a list with no open item); (item 12) the look for a projected decision on resuming (`start.md`), when it ends the item `— projected`, removes the line nested under it, as sub-step 7 of `settle.md` does; (item 13) the look at how a human learns of a failure (`failure_notice.md`) also looks for a projected decision of this definition and then gives `— projected`, as `list.md` does for a matter it finds a projected decision for, and not `— open`; (item 15) where no option of the agent's way to the running product can be used by an agent, `settle.md` has the recommendation go by the other consequences and say in one sentence that no option lets an agent check the running product this way, so the check stays with the human; and `project-level/definition_template.md`, where it carries WAY-166's sentence, says the same; (item 17, first point) in `project-level/definition_template.md` the sentence that names data set up from scratch and a dedicated test environment that persists reads as WAY-165 reads after Foundation entries item 17: examples, none ruled out. Foundation entries rows 1 and 2 and item 17 are written before this slice and bind it; word the files to agree with them. Prose only.
- **Change:** `project-level/technology/list.md` · `project-level/technology/start.md` · `project-level/technology/running_product.md` · `project-level/technology/failure_notice.md` · `project-level/technology/task_run.md` · `project-level/technology/settle.md` · `project-level/definition_template.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:46-49` To do, items 10 to 13 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:51-51` To do, item 15 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:56-57` To do, item 17, first point · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:83-95` Questions to settle, questions 1 and 2 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:166-171` Settlements to record, rows 1 and 2 · Foundation entries row 1 · Foundation entries row 2 · Foundation entries item 17 · `project-level/technology/SKILL.md` · `project-level/technology/research.md` · `elements/common/way_of_working.md:20-45` How a skill asks · `foundations/decisions.md:2568-2621` WAY-113 · `foundations/decisions.md:2827-2918` WAY-121 · `foundations/decisions.md:2979-3039` WAY-123 · `foundations/decisions.md:4754-4838` WAY-165 · `foundations/decisions.md:4839-4869` WAY-166 · `foundations/decisions.md:8096-8161` WAY-267 · `foundations/decisions.md:8293-8373` WAY-270 · `foundations/invariants.md:218-227` project-technology-record · `foundations/part_map.md:77-91` project-level
- **Model:** same — rules for resuming an interrupted run interact across five files of the step
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** Foundation entries row 1 · Foundation entries row 2 · Foundation entries item 17

### Slice 7 — Two files named settle.md, and the order of step 2 of find-foundation-entries

- **Goal:** (item 14) the two files named `settle.md` — the technology step's `project-level/technology/settle.md` and the critique's `elements/common/critique/settle.md` — no longer share a name: the critique's file is renamed with `git mv` to `elements/common/critique/settle_review.md` and the one place that names it, the last section of `elements/common/critique/SKILL.md`, names the new file; the technology step's file and the references to it stay. (item 26) in `elements/common/skill/build_table.md` the rule that a settlement an entry read in step 1 already states is no candidate stands before the table is written and shown, so that such a candidate is excluded first, as `task_variant.md` and `definition_variant.md` (the lines that write and show the table) expect; the rule that a candidate which collides with such an entry is shown beside it stays. Skill entry points do not change (no description of a skill changes); run `python -B agent-instructions/skill_entry_points.py` without `--write` and expect it to report no change. Prose and one rename.
- **Change:** `elements/common/critique/settle.md` · `elements/common/critique/settle_review.md` · `elements/common/critique/SKILL.md` · `elements/common/skill/build_table.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:50-50` To do, item 14 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:71-71` To do, item 26 · `project-level/technology/SKILL.md:56-62` 2. Settle the open choices · `elements/common/skill/SKILL.md` · `elements/common/skill/task_variant.md` · `elements/common/skill/definition_variant.md` · `foundations/decisions.md:2668-2707` WAY-115 · `foundations/decisions.md:2799-2826` WAY-120 · `foundations/decisions.md:3445-3540` WAY-134 · `foundations/decisions.md:7704-7814` WAY-256 · `foundations/decisions.md:8042-8069` WAY-265
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py` (expects no change reported) · `python -B gate/run_tests.py elements/common` · `python -B gate/run_tests.py agent-instructions` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** none

### Slice 8 — The refinement skill: the logs item, lasting exclusions and the split

- **Goal:** the refine-task skill says, each place found by its content: (item 16 and row 3) in `project-level/task/skill/resolve_gaps.md` the deployment-skill check handles three items apart, how to read the logs, how long the record of the logs lives and how a human learns of a failure: where a decision of the foundation or an approved definition the task carries answers the item, the refinement quotes it with its location and asks nothing, and the task's *To do* gains the item that writes the answer into the skill; a logs decision silent on how an agent reads the logs answers nothing for that item, as one silent on the record's life answers nothing for the item on the record's life; without such a decision the item goes as it does today. Foundation entry row 3 is written before this slice and binds it; word the file to agree with it. (item 25) `project-level/task/template.md`, under *Out of scope*, says that an exclusion that lasts beyond the task and that later work builds on is a decision candidate — a row of *Settlements to record* or a decision — as `project-level/task/skill/SKILL.md` ("Carry the foundation decisions", WAY-26) says; where the current sentence already says it, change nothing. (item 30) in `project-level/task/skill/read_sources.md` the sentence "Check that this is one task. If it joins independent outcomes, identify the split." is replaced by the sentence item 30 gives, word for word. Prose only.
- **Change:** `project-level/task/skill/resolve_gaps.md` · `project-level/task/template.md` · `project-level/task/skill/read_sources.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:52-52` To do, item 16 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:70-70` To do, item 25 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:79-79` To do, item 30 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:96-101` Questions to settle, question 3 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:172-172` Settlements to record, row 3 · Foundation entries row 3 · `project-level/task/skill/SKILL.md:48-52` 4. Carry the foundation decisions · `foundations/decisions.md:400-439` WAY-13 · `foundations/decisions.md:685-714` WAY-26 · `foundations/decisions.md:3760-3820` WAY-139 · `foundations/decisions.md:4754-4838` WAY-165 · `foundations/part_map.md:77-91` project-level
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** Foundation entries row 3

### Slice 9 — README: product guidelines and the host-state source

- **Goal:** (item 27) in `README.md`: the sentence on `product-guidelines/` says it holds the template, and the skill that leads the work on it, for each discipline of work for which the-way gives a template, as WAY-09 says (where the current sentence already says it, change nothing); the sentences on the sources a rule rests on (the list of what the foundation keeps and the row of `environment_facts.md` in the table of the five files) also cover the reading of the state of a host that the product's people run — the command, the host, the tool, its output and the date — as WAY-80 gives. The README binds nothing (WAY-09; the part map's "Files left out on purpose"), so no decision and no guarantee changes. Prose only.
- **Change:** `README.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:72-74` To do, item 27 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:126-126` Context · `foundations/decisions.md:219-296` WAY-09 · `foundations/decisions.md:1829-1868` WAY-80 · `foundations/glossary.md:49-53` environment fact · `foundations/glossary.md:121-125` read off · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** none

### Slice 10 — The instruction-files skill: names and emphasis

- **Goal:** (item 28) in `instruction-files/SKILL.md`, section "How to write a single rule": (a) a rule says that things are named in the words of the readers of the product, which now stands only in the mode of writing (`instruction-files/writing.md`, step 4); (b) the sentence on piled-on emphasis says what its source says — cautiously and about Claude, not categorically about every model. The source is the page named in the sentence (https://code.claude.com/docs/en/best-practices, § "What you can stop doing"): read that passage and word the sentence to say no more than it; where the page cannot be read, leave the sentence as it is and return the item as a question with the passage not found. `instruction-files/kind_main_file.md` cites the same page; report what it says there, change nothing in it. One rule keeps one place (the section's own bullet "A rule has one place"): word (a) so that the two files do not give two accounts.
- **Change:** `instruction-files/SKILL.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:75-77` To do, item 28 · `instruction-files/writing.md` · `instruction-files/kind_main_file.md:10-22` emphasis · `foundations/decisions.md:3313-3349` WAY-130 · `foundations/decisions.md:3414-3444` WAY-133 · `foundations/environment_facts.md:162-166` single-rule-compliance · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py instruction-files` · `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** none

### Slice 11 — Part map: the task cycle depends on the installer

- **Goal:** (item 29) in `foundations/part_map.md` the part `task-cycle` lists `installation` in its *Depends on*, because the cycle skill sends the agent to `installation/README.md` for moving the pin (`installation` and `task-cycle` then depend on each other, as `installation` and `product-guidelines` already do). Follow the skill of the part-map element (`elements/part-map/skill/SKILL.md`) for the edit and WAY-33 for the search of the whole foundation afterwards. No other entry of the map changes.
- **Change:** `foundations/part_map.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:78-78` To do, item 29 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:102-107` Questions to settle, question 4 · `task-cycle/skill/SKILL.md:37-48` step 2, the move of the pin · `installation/README.md:78-116` Moving the pin · `foundations/decisions.md:872-904` WAY-33 · `foundations/decisions.md:1113-1163` WAY-44 · `foundations/decisions.md:9426-9479` WAY-299 · `foundations/invariants.md:146-155` map-reference-target · `foundations/invariants.md:328-336` cross-part-imports · `elements/part-map/skill/SKILL.md` · `elements/part-map/skill/decide_entry.md` · `elements/part-map/skill/write.md` · `elements/part-map/template.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B gate/run_tests.py elements/part-map` · `git diff --check`
- **Depends on:** none

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Item 1 — correction merges the target branch as step 12 does | Slice 1 |
| Item 2 — step 12 merges the remote target branch | Slice 1 |
| Item 3 — the fast-forward named as the exception | Slice 1 |
| Item 4 — current ranges of the dispatch hold | Slice 2 |
| Item 5 — dependencies and `.the-way` in the base copy | Slice 1 |
| Item 6 — pointer to `foundation_step.md`; where logging-scope additions are found | Slice 2 |
| Item 7 — plan-state reader shows a blocked draft; both flows write the wording it recognises | Slice 3 |
| Item 8 — remarks script reads reports by name; docstring on items; test; skill sentences | Slice 4, Foundation entries row 5 (Slice 1 first, same file) |
| Item 9 — installer test independent of the live head | Slice 5 |
| Item 10 — four matters cannot be struck | Slice 6, Foundation entries row 1 |
| Item 11 — resumed run lists the note's choice | Slice 6 |
| Item 12 — `— projected` removes the nested line on resume | Slice 6 |
| Item 13 — failure notice looks for a projected decision | Slice 6 |
| Item 14 — the two `settle.md` files get different names | Slice 7 |
| Item 15 — no usable option: recommend by other consequences, check stays with the human | Slice 6, Foundation entries row 2 |
| Item 16 — logs-reading item tied to the logs decision | Slice 8, Foundation entries row 3 |
| Item 17 — WAY-165 wording (three points) | Foundation entries item 17; the sentence in `definition_template.md`: Slice 6 |
| Item 18 — WAY-166 example | Foundation entries item 18 |
| Item 19 — WAY-128 names WAY-259 | Foundation entries item 19 |
| Item 20 — WAY-292 *Verification* | Foundation entries item 20 |
| Item 21 — WAY-05 *Verification* in two pairs | Foundation entries item 21 |
| Item 22 — WAY-293 *Rationale* and rejected way | Foundation entries item 22 |
| Item 23 — WAY-287 list | Foundation entries item 23 |
| Item 24 — WAY-148 without "of the product" | Foundation entries row 4 (the planner's skill stays; no slice) |
| Item 25 — template: lasting exclusion belongs to a decision | Slice 8 |
| Item 26 — step 2 excludes the candidate an entry already states, before the table is shown | Slice 7 |
| Item 27 — README: guidelines sentence; host-state source | Slice 9 |
| Item 28 — instruction-files: names in the readers' words; emphasis | Slice 10 |
| Item 29 — part map: `task-cycle` depends on `installation` | Slice 11 |
| Item 30 — refinement starts from one task | Slice 8 |
| Settlements row 1 | Foundation entries row 1 |
| Settlements row 2 | Foundation entries row 2 |
| Settlements row 3 | Foundation entries row 3 |
| Settlements row 4 | Foundation entries row 4 |
| Settlements row 5 | Foundation entries row 5, Slice 4 |
| Question 6 (no waiting for the way's own guidelines) | no work; the-way has no `guidelines/`, the cycle goes by `agent-instructions/README.md` |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Eleven slices grouped by the part and the reading each needs, not one slice per family of items; the files that two slices both change (`task-cycle/skill/SKILL.md`) are changed in dependent order only | one slice per item (30 handoffs, most of a few lines); one slice per family of the task's headings (the cycle family alone would mix a script at a trust boundary with prose and an installer test, each needing a different reading) | a slice found too large or too mixed is split by the cycle's rule for a slice that proves too large |
| Rows 1–5 of *Settlements to record* and the rewordings of items 17 to 23 are entries the foundation step writes before any slice; the slices that follow their text (Slices 4, 6, 8) depend on them | rewording the decisions in slices (the size script counts a changed file whole, and `foundations/decisions.md` alone exceeds the limit of one slice, so the slice is `too large` and cannot be split); the wording slices before the rows (they would edit text the rows then edit again) | the writer of the foundation step carries nine more entries and their searches of the whole foundation; a collision of two edits to one decision shows in the review of the whole change |
| Item 7: the reader adds one evidence line for a record whose *Request URL and status* reads `blocked draft, opened on this commit`; no new proposal, state, conflict or exit code | a new state `blocked` proposed to the plan (changes the surface `project-plan-state-command` and the project orchestrator's rules); treating such a record as a conflict (it is not one, the human has not closed the request) | a product that reads the reader's output line by line sees one new line; removing it again is one commit |
| Item 14: the critique's `settle.md` is the one renamed (`settle_review.md`) | renaming the technology step's `settle.md` (references to it stand in six files: `SKILL.md`, `close.md`, `running_product.md`, `start.md` and `task_run.md` of `project-level/technology/`, and `project-level/lead/skill/technology_run.md`) | a reference to the old critique file left in a product's own notes breaks; inside the-way the only reference is the one line of `SKILL.md` |
| Item 8: the name test is a literal, case-sensitive match of `handoff` and `findings` | a case-insensitive match or a pattern on a prefix or suffix (the settlement words "holds"; a stricter rule would again pass files the cycle names otherwise) | a handoff file written with capitals is read as a report and its lines are listed; the orchestrator holds the listing wrong as WAY-295 gives |
| Item 28b: the executor reads the cited page on the web and words the sentence from it; if it cannot read it, it returns the item as a question | taking the wording from the task's phrase alone (no passage in the repository; a wording from memory is the failure the source rule names) | the item is returned open and goes to the human through the cycle's question route |
| Items 17(b), 25 and 27 (first point) may already be met by the text of the base; the entry or the slice changes nothing where it is so and says it | rewriting them to the task's words regardless (churns accepted text for nothing) | an item reported as met that the reviewer reads as not met is fixed in the one fix the review of the whole change allows |
