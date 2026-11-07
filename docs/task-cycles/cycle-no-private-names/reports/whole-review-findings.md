# Findings of the review of the whole change (range ad44b84..b6d93e8), in the reviewer's words

Source: reports/whole-review-report.md. Blocking finding first, then the Minor findings within the task, none marked outside the task's scope.

## Blocking findings

### 1. Important — the cleaned committed copy of a plan item's record cannot be anchored by the plan-state reader, and WAY-308 says it can

Place: `task-cycle/record_template.md:3-5` (rule for `Task source:`), `task-cycle/skill/SKILL.md` section
"The record before it is committed" step 3, and `foundations/decisions.md` WAY-308 *Rationale* ("Cleaning
keeps the record, so its readers go on reading it: … the reader of a project plan's state … ties the
record to the plan's task by the `Project relation:` line").

What is wrong. The reader does not tie a record to the plan's task by `Project relation:` alone. In
`project-level/plan_state.py:253-265` (`provenance`), while the plan row's *Document* is still the path
of the task document (every state before `done`, per `project-level/plan/template.md:88`), the
candidates come only from absolute paths in the record's `Task source:` line; with none the record is
reported "original Task source or Document cannot be anchored" and nothing is proposed from it. The
committed copy has this line cleaned by the rule (absolute path replaced by a description), so the
archived commit gives nothing to the reader. The working record in `.runs/` keeps the absolute path, so
the "working cycle directory" proof is unaffected; the loss is in the commit of the archived copy.

Evidence (my own fixture, outside the repository, built on the reader's test class
`project-level/test_plan_state.py` with `Task source:` replaced by "the task document in the author's
backlog"; scratch files `scratchpad\ps_scratch.py` and `scratchpad\ps2.py` under the session scratchpad):

- Plan item, state `in cycle`, record archived and merged to the integration branch, *Document* = the
  task document path: output has no `propose ... in cycle -> done`; it prints
  `unchecked 1 reports: commit <sha>: docs/task-cycles/reports/record.md: original Task source or Document cannot be anchored`
  and `no sufficient cycle trace; PR outcome unchecked`. With the absolute `Task source:` (the base
  behaviour, tests `test_merged_record_composes_start_and_completion_with_evidence` and
  `test_canonical_cycle_filename_proves_completion`) the same fixture proposes `in cycle -> done`.
- Plan item, state `ready for cycle`, record archived on an unmerged branch: `unchecked ... cannot be
  anchored`, no `-> in cycle` from the archive (the same loss for the "entered a cycle" proof once the
  worktree is gone).
- Plan item, state `done`, *Document* linking the frozen copy (`frozen_copy` branch of `provenance`):
  works with a cleaned `Task source:`; evidence lines `archived cycle` and `cycle record ... reachable`
  are printed, no `unchecked`, no `conflict`. So the loss is only in the stretch before *Document* is
  changed to the frozen link, and that change is made after the done proposal.
- Independent task: the reader reads only a plan's tasks by the slug of the plan row; an independent
  task's copy is not in its path, so the rule does not touch it.
- A second form of the same gap: if a plan item's record carries the expanded `Task relation:` form
  (`plan item — <plan> (...), item N name`) with the plan given by a path, the cleaning turns the path
  into a description; with *Document* linking the frozen copy the reader then prints
  `conflict 1 reports: ... Task relation names plan the plan in the author's backlog item 1 reports;
  human reconciliation required` and exits 1 (fixture `ps2.py`, `test_relation_described`). The cleaning
  rule has no word for this line. Whether real records write the expanded form with a path is not
  established by the tree (see Searches).

Does the rule break the invariant `project-plan-state-evidence` (WAY-153)? Not in its safety content:
the reader fails closed, reports missing provenance as `unchecked`, proposes nothing it cannot prove,
and edits nothing; the invariant's tests pass (`python -B gate/run_tests.py project-level`, exit 0, 268
tests — but no test of the reader reads a cleaned copy, so they would pass either way). It does break
what the decision is for in the plan-item case: the reader no longer proposes `in cycle -> done` from the
merged archive; a human has to move the row and link the frozen copy by hand. The task's own text
(Question 1 answer: "Wszyscy czterej czytelnicy zapisu z *Context* działają dalej"; To do 1: only the
`Project relation:` line stays because "po niej czytnik stanu planu wiąże zapis z zadaniem planu") and
WAY-308's rationale both say the reader goes on working; for a plan item before *Document* links the
frozen copy that is not so. Grade per WAY-263: the entry states more broadly than the code does, and
the change's files (the template, the section) do what the entry says is harmless but is not.

Why it matters: the plan-state reader is one of the four readers the chosen route was picked to keep
(Question 1 "Not chosen" rejects "no commit" precisely because it would lose this proof). The change
loses a part of the same proof by another way and records the opposite in a decision. The author raised
the point (Problems 1) and read the code but ran no fixture; the orchestrator ruled the `Task source:`
split an autonomous choice. The ruling is sound for the working record; it does not cover the committed
copy.

Spans: the whole change (no slices); comes from the rule in `record_template.md`/the new section, and
partly from a gap in the task (it assumed `Project relation:` alone anchors the record).

Ways out for the cycle to weigh (not decided here): (a) make the reader anchor an archived copy whose
`Task source:` has no absolute path by the bare file name of the *Document* together with the frozen
task's `Project relation:` (change in `plan_state.py` plus tests and the invariant's test — a larger
change, probably its own task); (b) keep in the cleaned `Task source:` a form the reader can compare
(for example the document's file name beside the plan) and teach the reader that form; (c) correct
WAY-308's rationale and the template to say that, for a plan item, the done proposal waits for the
human to link the frozen copy, and add a fixture test that pins what the reader does on a cleaned copy;
and give the cleaning rule a word for the `Task relation:` line. At minimum the decision must stop
saying what does not hold.

## Minor findings within the task

2. `foundations/decisions.md` WAY-294 versus `task-cycle/skill/SKILL.md` section "The record before it
   is committed" step 5. WAY-294 says the orchestrator "appends each listed item" and runs the script
   until it lists nothing; step 5 runs the script a second time, on the copy, and says to append nothing
   when it lists. The two do not contradict (the second run is a different target) but WAY-294 is left
   describing one run, and step 5 forbids what WAY-294 requires. One sentence in WAY-308 or WAY-294
   naming the second run would close it. Within the task (the carried question on order).

3. `foundations/decisions.md` WAY-308 and WAY-309, line *Scope:* `task-cycle, agent-instructions`. The
   rule reaches the committed record that the `project-level` reader reads (finding 1), and the entries
   say so in their rationale; the scope does not name `project-level`, so a task touching the reader
   would not find these entries by scope. Within the task.

4. `task-cycle/skill/SKILL.md` step 12 with `task-cycle/skill/request_template.md` *Checks*. The first
   description is written and checked before the copy exists (step 12 order), yet *Checks* must name the
   private-paths check's last run on the copy. Nothing says that the edit that adds the record's link
   also fills in that line (the sentence only says "check it again ... and edit the request with it").
   The description can be published with *Checks* missing the copy's run. Within the task.

5. `task-cycle/record_template.md:93` still reads "copy that whole directory ... commit the copy and
   commit its removal" and does not say the copy is cleaned; only the closing paragraph at the end of the
   file points to the new section. A reader of the template's *Verification* paragraph is not sent there.
   Within the task.

6. `task-cycle/private_paths_check.py` (`PATH_TAIL`) and `task-cycle/test_private_paths_check.py:90`. A
   path with spaces is listed up to its first space (the test asserts the path up to the first space for a made-up path with a space in it). An orchestrator who replaces only what is shown leaves the rest of the path behind and the next run
   passes. The rule in the section says to correct "each listed place"; it does not say to replace the
   whole path to the end of the phrase. Also, the same test file uses a real vault directory name (the notes directory's real name) as its sample; the task counts that name as a thing the history should not repeat. Rename the
   sample and add one sentence to the rule. Within the task.

7. `task-cycle/private_paths_check.py` (binary probe, lines `BINARY_PROBE`/`check_file`). A text file that
   holds a NUL byte near its start — a UTF-16 file, as Windows PowerShell 5.1 `Set-Content`/`Out-File`
   writes by default — is skipped as binary and only counted in the last line; the section does not tell
   the orchestrator what to do with the count. A report saved by a shell in UTF-16 would pass with paths
   in it. Minor because the cycle writes records through tools that write UTF-8 and the count is shown.
   Within the task.

8. Heuristic edges, all documented or cheap: a web address with a drive-like segment is listed (a `/C:/` after a slash is
   not excluded by the boundary), an array index written with two brackets is listed as a note link (author's report states it),
   `file:///home/<name>/x` is not listed (the Linux-home boundary excludes a path after `/`), `%USERPROFILE%\x`
   and `~` paths are not listed (stated). I ran forms the author did not: a bare drive root alone (listed), a
   a lower-case drive letter with a users directory (listed), a Windows long-path prefix with a drive (listed), a path in a Markdown link a drive path in round brackets
   and in a link with angle brackets (listed, the second up to its first space), a path in a table cell
   plain and in a code span (listed), a note link with an alias, an embedded image and a link to a heading (listed), UNC
   `\\server\share` (not listed, stated), a drive path with doubled backslashes (listed), the WSL and Git Bash forms of a drive
   (listed), `[[ -f x ]]` (not listed). Run on the tracked text of the repository (`python -B
   task-cycle/private_paths_check.py .`): the only hits outside the new script, its test and the working
   directory `.runs/` are `AGENTS.md:20,25` (the vault path in the `## Backlog` section, the one
   exception of WAY-27) and `instruction-files/` code (a drive root inside a regular expression, a made-up
   drive path); no prose or URL line outside those is listed. Within the task.
