# Handoff — the fix of a review's findings

You are the one author, resumed, making the fix of the review of the whole change. Method:
`task-cycle/change/SKILL.md`, variant **"the fix of a review's findings"**; read `task-cycle/change/fix.md`
whole first. Same worktree and branch: `.`,
`task/cycle-no-private-names`. Commit on it, do not push, do not run the full gate.

- Findings file, in the reviewer's words (one blocking finding, seven Minor findings, all within the
  task): `.runs/task-cycles/cycle-no-private-names/reports/whole-review-findings.md`. The full review is
  `reports/whole-review-report.md`; the reviewed head is `b6d93e8`. Your fix range runs from `b6d93e8`.
- Fix report: `.runs/task-cycles/cycle-no-private-names/reports/fix-report.md`, as `fix.md` gives, with
  **Searches not found or unclear**, each check with command and exit code, and your own-work check.
  A finding you hold wrong you answer with evidence; you may not simply skip one.

## The orchestrator's ruling on the blocking finding (autonomous choice, Q3)

The way out is the reviewer's (c), with the fixture test, and not a change of `plan_state.py`:

- The goal of the task stays: the committed copy publishes no absolute path and no private note
  link. For a **plan item**, that costs the plan-state reader part of its proof in one stretch: before
  the plan row's *Document* links the frozen copy, the reader cannot anchor the cleaned copy
  and reports it `unchecked`, so the `in cycle -> done` proposal waits until a human links the copy.
  The reader fails closed (reviewer's evidence), the invariant `project-plan-state-evidence` is not
  broken. An independent task is not touched.
- Correct WAY-308's rationale so it says exactly that, and does not claim the reader goes on
  working in this stretch. Correct `task-cycle/record_template.md` and the new section of
  `SKILL.md` in the same way where they repeat the claim. Do not change `plan_state.py` and do not
  edit the invariant (a reader that anchors a cleaned copy is another task; name it in your report
  under the concerns, not in the decision).
- Add a test that pins what the reader does with a cleaned copy (the reviewer built the fixture from
  the reader's own test class in `project-level/test_plan_state.py`; build yours the same way, a new
  test method or class in a new file `project-level/test_plan_state_cleaned_copy.py` or in the
  existing file, as that file's conventions allow): (1) a plan item in `in cycle` whose archived
  copy has a cleaned `Task source:` and whose *Document* is not yet the frozen copy gives `unchecked`
  and no `done` proposal; (2) the same copy with *Document* linking the frozen copy is read
  without `unchecked` or `conflict`. Assert the reader's actual output, spelled out in the test.
- The `Task relation:` line (second form of the finding): the cleaning rule leaves the record's
  `Task relation:` line unchanged, as it leaves the task copy's `Project relation:` line, for the same
  reason (the reader reads it). Their form names the plan by its file name, so neither is expected
  to hold an absolute path. Say in the rule: if the script lists either line, the orchestrator does
  not rewrite it; it puts the line to the human in the request's *For you to decide* and the
  request opens as a draft marked `blocked` ("Merge as it stands?" in the form of
  `request_template.md`), as the form for an item the cycle holds for the human to decide gives; look
  at how `request_template.md` and WAY-295 do it and keep the wording short. If you cannot make this
  fit without a new variant of the request, return `questions` with what you found.

## Minor findings (2–8): all are fixed; the task and the reviewer put them within the task

- 2: add the one sentence that closes WAY-294 against step 5 of the new section.
- 3: add `project-level` to the *Scope* of WAY-308 and WAY-309 (and keep `foundation_check.py` green).
- 4: say in `SKILL.md` step 12 / `request_template.md` that the edit that adds the record's link also
  fills in the *Checks* line for the copy's run.
- 5: `task-cycle/record_template.md` line 93: say the copy is cleaned and point to the section.
- 6: change the sample of the test that uses the real name of a private notes directory; add one
  sentence to the rule: replace the whole path, to the end of the phrase, not the printed part. You
  may also make the script print the whole phrase up to a line end or a closing quote if that is
  simple and tested; your choice, named in the report.
- 7: say in the rule what to do with the count of files not read: read them by hand or save them as
  UTF-8 and run again; the count must reach zero before the commit (or the script exits 1 for it, if
  you make that change, with its test). Your choice, named in the report.
- 8: fix the two cheap edges (a web address with a drive-like segment listed; `file:///home/<name>/x` missed) with tests
  if a boundary change does it simply; leave the rest as documented.

Reading beyond the handoff: name each reach in the report. Read each file you change whole before
you change it, again if it changed since you read it. Keep the line ends of existing files.
