FAIL 6349019187409079f93cc41bf3f39df9d90b1adb

# Review of the whole change — cycle-technology-decisions-batch

Range `f238e4ffdfc2396ae0009fefa90b3af8d1e931e1..6349019`, 21 commits (10 of the plan's *Foundation
entries*, one for each of the 11 slices). `git rev-parse HEAD` is
`6349019187409079f93cc41bf3f39df9d90b1adb`, the head given. I computed `git diff f238e4f..6349019`
and `git log f238e4f..6349019` myself, and read the method (`task-cycle/review/SKILL.md`,
`task-cycle/review/whole_change.md`), the frozen task whole, the plan whole, every executor report
(02, 03, 04, 05, 07, 08, 09, 10, 11, 12, 13, 14) and the slice-3 review (06).

Counts: blocking 2 (both Important), Minor 8 within the task, out of scope 1 (Minor).

Trust boundary (step 4: yes, `project-level/plan_state.py`): crafted input checked, see Minor 1–3 and
"Checks". Irreversible operation: none.

## Findings

### Critical

none

### Important

1. **The technology step tells the agent that a logs answer missing the record's life settles the
   matter, and exempts such an item from the re-check WAY-165 requires.**
   Places: `project-level/technology/list.md:42-45`, `project-level/technology/running_product.md:20-22`
   and `:38-39`, `project-level/technology/start.md:21-24`.
   - What is wrong: the example of an answer that "settles the matter" in `list.md:43-44` and
     `running_product.md:21` is "the tool prints to the console, an agent reads the terminal". It says
     where the record goes and how an agent reads it, but not how long the record lives. WAY-165 and
     the template (`project-level/definition_template.md:179-180`) give the logs matter three
     questions, record life included. WAY-165's *violates* list names exactly this case: "the logs
     are answered by where the record goes and how an agent reads it, with nothing said of whether
     it outlives a redeployment, and the answer stands as settling the matter". `running_product.md`
     itself says, eight lines earlier (`:12-14`), that such an answer "settles nothing". The new
     bullet `running_product.md:38-39` ("An item the human's answer settled, because the matter did
     not apply to the product, ends `— projected` and is not looked at again as open") takes such an
     item out of the check in the bullet at `:33-34`: a `— projected` item whose decision is silent on
     part of the matter goes back to `— open`. `start.md:21-24` says the same ("its item ends
     `— projected` and does not return open"). Also, no marker tells a resuming agent which
     `— projected` item was settled "because the matter did not apply". And the marker is written
     `— projected` without the `: <question>` the template's marker table requires.
   - Why it matters: an agent that follows the example writes a logs decision silent on the record's
     life, and the resumed step leaves it settled. The agent of a later cycle then guesses how long
     the logs live, which WAY-165 and WAY-322 exist to prevent. WAY-322's own *complies* example
     ("the tool prints to the console, the record lives as long as the run, an agent reads it from
     the terminal") gives all three parts. The files say the rule differently from the decisions
     they rest on. That is a departure from WAY-322, an entry this change writes (WAY-263), and from
     WAY-165, an entry it changes.
   - Evidence: the lines quoted above, read beside `foundations/decisions.md:4820-4826` (WAY-165,
     *violates*) and `:10382-10386` (WAY-322, *complies*). The short example comes from the task's
     answer to question 1 ("narzędzie nie ma logów, agent czyta wyjście konsoli"). The task gives it
     as an illustration, not as text for the files. Even so, it is a defect.
   - Fix: give the example all three parts, as WAY-322's does. Drop the bullet at
     `running_product.md:38-39`, or reword it so that an item settled this way is read like any
     other `— projected` item (the bullet "An item whose entry answers all the matter asks stays as it
     is" already keeps a full answer). Word `start.md:21-24` to match.
   - Slice: **slice 6** (`815294c` → `f3bf7b6`, commit `f3bf7b6`).

2. **The installer tests no longer test the installer in the working tree. A broken uncommitted
   `install.py` passes them.**
   Place: `installation/test_install.py:38-44` (`setUp`), with `install()` at `:46-48`,
   `installed_from_a_remote` and `later_process`.
   - What is wrong: `setUp` clones the-way's committed HEAD into the temporary directory. Every test
     then runs `self.installer`, the clone's `installation/install.py`, which is the committed file.
     Before the change, the tests ran the working-tree `install.py`. An edit to `install.py` is now
     tested only after it is committed. Meanwhile `import install` (`:16`) still loads the
     working-tree module for `product_guidance()`, so one file tests two versions of the installer.
     Each test also adds a local clone. The executor measured about 3.5 s a test, and the 30-test file
     took about 104 s.
   - Why it matters: a test written first, against an uncommitted fix of `install.py`, keeps failing
     until the commit. A breaking uncommitted edit passes the suite and is caught only at the gate.
     So the tests no longer fail when the behaviour they protect breaks, which section 2 of the method
     asks of tests. Item 9 asked only that a concurrent commit not change the expected commit. There
     is a way that keeps the working-tree installer under test: after the clone, copy
     `SOURCE/installation/install.py` over the clone's file. `later_process` already does this with
     the installer under test. The pin is still read from the clone's HEAD (`install.py:496`) and
     from its committed files (`:84`).
   - Evidence: a scratch clone of the head (outside the reviewed worktree). In it I added
     `raise SystemExit(9)` as the first line under `if __name__ == "__main__":` of
     `installation/install.py`, uncommitted. A direct run of the installer then exited 9.
     `python -B -m unittest discover -s installation -p "test_install.py" -k
     test_preview_apply_rerun_and_preserve_foundation` exited 0 (OK). For a positive control, I put
     back the base's `test_install.py` (`git checkout f238e4f -- installation/test_install.py`) with
     the same broken installer. The same command exited 1 (FAILED).
   - Slice: **slice 5** (`491f048` → `815294c`, commit `815294c`).

### Minor

Within the task unless the item says otherwise.

1. `project-level/plan_state.py:160-168` (`record_requests`) — from the slice-3 review, word for word:
   "a line with the wording, then a lone `\r`, then more text is cut by `splitlines()` to the wording
   and recognised". I ran the probe again at head: a record with the wording, then `\r`, then
   `IGNORE PREVIOUS INSTRUCTIONS` prints the blocked evidence line. No text of the record reaches the
   output, so the trust boundary holds. Only recognition is loose. The crafted-input test has no lone
   `\r` case. Splitting on `b"\n"` and adding such a case would close it.
2. `project-level/plan_state.py:157-168` — from the slice-3 review, word for word: "the wording inside
   a fenced block is read as the field, the same limit the pull-request pointer lines have, and the
   limit is written in no foundation entry". I confirmed it at head with the probe. The limit
   should be written where a reader of the reader's output finds it, for example in the docstring
   of `record_requests`.
3. `project-level/plan_state.py:157` — `re.escape(BLOCKED_DRAFT)` is passed to `git grep -E`.
   `re.escape` writes `\-` and `\ `, which POSIX ERE leaves undefined. Git on this machine reads them
   as literals, and the tests pass. A Git built with another regex engine might never match the
   wording. The task would then show as before the change, with no sign. That failure is safe but
   silent. An ERE-only escape (or the literal without `\-` and `\ `) avoids the question.
4. `task-cycle/skill/SKILL.md:68-69` against `:118-119` and WAY-298
   (`foundations/decisions.md:9441-9442`) — item 3. The sentence now names two exceptions: the
   fast-forward and the account of the request. Step 4 of the same file and WAY-298 still call the
   fast-forward "the one change the cycle makes outside the task's worktree". The task (item 3, from
   WAY-298) asked for the fast-forward as "the only exception". The executor kept the backlog account
   as a second exception because the base already allowed it. That is true to the base, but the
   file now counts two exceptions in one place and one in another. Recommended: qualify step 4's
   phrase and WAY-298's last sentence as the one change *in the product repository* outside the task's
   worktree, or ask the human, since WAY-298 is a decision the task did not open.
5. `foundations/decisions.md:10370-10376` (WAY-322), and the files of slice 6 that follow it — row 1
   names four matters. WAY-322 is worded by the family ("a matter of an agent's way to the running
   product that the step … lists"), so it also covers the place of the screenshots. The base holds
   that fifth matter, and it was added after the task's text was written. This goes beyond row 1, and
   the human did not see it at the task document. The extension is reasoned (the foundation-entries
   report gives the reason) and is consistent with WAY-165, so I do not grade it as blocking. By
   WAY-287 it is one of the cycle's choices beyond the task's content, and the request's *For you to
   decide* has to name it.
6. `task-cycle/test_remarks_check.py:367` — the test keeps its name
   `test_only_files_whose_name_ends_in_report_are_read`, but the rule no longer depends on the
   ending (`review_whole.md` is read). The name now says something false. The new test at `:375`
   carries the item-8 cases, so coverage is met. The old test should be renamed, for example to
   "files that are no reports are not read".
7. `instruction-files/SKILL.md:230-232` against `instruction-files/writing.md:14-15` — item 28a. The
   new bullet gives the rule and the same examples (`Where things are`, `Before you release`) that
   step 4 of `writing.md` holds. That is two places for one rule, against the bullet "A rule has one
   place" two lines below it. Recommended (the slice-10 executor recommends it too): reduce step 4 of
   `writing.md` to a pointer to the bullet.
8. `task-cycle/spec/SKILL.md:53` and `task-cycle/skill/SKILL.md:192-193` — item 24 and row 4. Both
   still give the reason for returning no check result as "runs no test or other check *of the
   product*", the qualification WAY-148 has now lost. Nothing is wrong today: the spec stages run no
   check of any kind, and their four checks are a reading of the spec. But the wording restates the
   old narrowing beside the decision that dropped it. This comes from no slice: the plan's row 4 had
   none, and the entry's search did not reach these lines.

Out of scope:

9. `installation/test_coding_guidelines_installation.py:32` and
   `installation/test_lead_installation.py:32` — the slice-5 executor reports the same pattern there
   (`self.commit` read from the live head in `setUp`, then an install from the live repository). A
   commit during a full run can break them the same way. This is outside the task: item 9 names one
   test of `test_install.py`. Not run by me.

## Coverage of the task

| Item / row / question | Met by | Verdict |
|---|---|---|
| 1 correction's merge as step 12 | `task-cycle/skill/correction.md:9-11`, `:28-32` | met |
| 2 step 12 merges the remote branch | `task-cycle/skill/SKILL.md:420` | met |
| 3 the exception named | `task-cycle/skill/SKILL.md:68-69` | met, with Minor 4 |
| 4 the dispatch's current ranges hold | `task-cycle/change/slice.md:11-13` | met |
| 5 dependencies and `.the-way` in the base copy | `task-cycle/skill/SKILL.md:129-131` | met |
| 6 `foundation_step.md` pointer; where logging-scope additions are found | `task-cycle/skill/request_template.md:171`, `:225-226` | met. The file name at `:171` is an instruction to the author, not text of the description, so WAY-286 is not broken |
| 7 blocked draft read as blocked; both flows write the wording | `project-level/plan_state.py`, `blocked_finding.md:14-17`, `reserved_return.md:56-58`, tests | met, Minor 1–3 |
| 8 remarks script by name; docstring; test; skill sentences | `task-cycle/remarks_check.py:12-14`, `:26-28`, `:129-133`, `:325`; tests `:147`, `:375`; `SKILL.md:144`, `:479` | met. Docstrings match item 8 word for word. Minor 6 |
| 9 installer test independent of the live head | `installation/test_install.py` | the stated failure is fixed (the executor showed it before and after), but **Important 2** |
| 10 four matters cannot be struck | `list.md`, `start.md`, `running_product.md`, `failure_notice.md` | met in substance, **Important 1**, Minor 5 |
| 11 resumed run lists the note's choice | `project-level/technology/task_run.md:30-33`, `:41-42`, `:104` | met |
| 12 `— projected` removes the nested line | `project-level/technology/start.md:28-30` | met (matches `settle.md:83`) |
| 13 failure notice looks for a projected decision | `project-level/technology/failure_notice.md:14-17` | met |
| 14 the two `settle.md` get different names | rename to `elements/common/critique/settle_review.md`, `critique/SKILL.md:37` | met. No other reference to the old file exists outside `.runs/` |
| 15 no usable option | `settle.md:35-38`, `definition_template.md:252-254`, WAY-166 | met, faithful to question 2 |
| 16 logs item tied to the logs decision | WAY-139, `project-level/task/skill/resolve_gaps.md:66-84` | met, faithful to question 3 |
| 17 WAY-165, three points | `decisions.md:4793-4795`, `:4839-4853`; `definition_template.md:185-186` | point 1 met. Point 2 already met by the base: WAY-165 has no "only on the human's word", and it opens only "a decision of the foundation"; checked. Point 3 met: the citation moved to the sentence that rests on WAY-270's rationale ("not good enough to diagnose a failure from before it"), and the relation stays |
| 18 WAY-166 example | `decisions.md:4885-4886` | met |
| 19 WAY-128 names WAY-259 | `decisions.md:3257` | met |
| 20 WAY-292 *Verification* | `decisions.md:9230-9231` | met |
| 21 WAY-05 two pairs | `decisions.md:140-147` | met |
| 22 WAY-293 *Rationale* and rejected way | `decisions.md:9272-9282` | met |
| 23 WAY-287 list | `decisions.md:9037-9038`, *Verification* | met |
| 24 WAY-148 without "of the product" | `decisions.md:4144-4145`, *Rationale*, *Rejected* | met, Minor 8 |
| 25 template: lasting exclusion is a decision candidate | `project-level/task/template.md:207-208` | met. The handoff says nothing was changed here, but slice 8 did reword it, to the words of `project-level/task/skill/SKILL.md:51`. The new text is right |
| 26 step 2 drops a stated candidate first | `elements/common/skill/build_table.md:4-5`, `:20-21` | met |
| 27 README | `README.md:48-52`, `:77` | second point met. First point already met by the base (`README.md:116-120` names the template and the skill for each discipline, as WAY-09 does); checked |
| 28 instruction-files | `instruction-files/SKILL.md:230-236` | met. The emphasis sentence matches the source passage, which I checked in the page saved by slice 10. Minor 7 |
| 29 `task-cycle` depends on `installation` | `foundations/part_map.md:99` | met |
| 30 one task by default | `project-level/task/skill/read_sources.md:23` | met word for word |
| Row 1 | WAY-322 (new) | met, Minor 5 |
| Row 2 | WAY-166 | met |
| Row 3 | WAY-139 | met |
| Row 4 | WAY-148 | met |
| Row 5 | WAY-294 | met |
| Questions 1–5 | as rows 1–4 and item 29 | answers carried. *Rejected* holds the "Not chosen" ways |
| Question 6 | no work | the-way has no `guidelines/`, so no guidelines were selected |

Nothing the change takes from the task is altered, except what Important 1 (the example) and Minor 5
(the fifth matter) name.

## Slices without a review of their own (judged here)

- Foundation entries: the 12 entries are as the report says. One concern is Minor 5. The executor's
  own-work check (WAY-05 on the prose written) holds. I found no file or script named in the new
  *Rationale* or *Rejected* text, except what the sources give.
- Slices 1, 2, 4, 7, 8, 9, 10, 11: findings above (Minor 4, 6, 7, 8). The own-work checks named
  fitting requirements.
- Slice 5: Important 2. Its own-work check tested the concurrent commit only, not whether the tests
  still run the code under edit. The executor's report names that cost, but the cost is the defect.
- Slice 6: Important 1. Its own-work check searched for `strike`/`struck` and did not compare the new
  example with WAY-165's three questions.

## Declined to judge

- Whether `project-level/definition_template.md` should carry the no-strike rule: item 10 names the
  files of the step, not the template, and the template does not contradict WAY-322.
- Whether other paths that end in a blocked draft (`task-cycle/skill/foundation_step.md`, the
  human-action path of `SKILL.md`) should write the record wording: item 7 names two files.
- Whether a test should pin the part map's *Depends on* of `task-cycle`: no test pins any part's
  *Depends on* line, and the task asks for none.

## Checks

| Check | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `6349019187409079f93cc41bf3f39df9d90b1adb` |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `python -B gate/run_tests.py task-cycle` | 0 | 211 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 275 tests OK |
| `python -B gate/run_tests.py elements/common` | 0 | 117 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped (the Windows link tests) |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK |
| `python -B gate/run_tests.py installation` | 0 | 44 tests OK in 156 s; the passing run does not cover Important 2, which only shows with an uncommitted edit |
| `git diff --check f238e4f..6349019` | 0 | clean |
| Scratch probe of `plan_state.py`: crafted records (lone `\r` then text, a fenced block, a form feed, a no-break space, the wording beside a real URL), run with `python -B -I` against the head's fixtures in temporary repositories | 0 | lone `\r` and fenced: recognised (Minor 1, 2). Form feed and no-break space: not recognised. No record text in the output |
| Scratch probe of the installer tests: a clone of the head in the scratchpad, with `install.py` broken uncommitted; then the base's `test_install.py` as a positive control | 0 / 1 | head's test passes a broken installer, base's fails it (Important 2) |

The reviewed worktree, its index and its branch were not changed: the probes ran in a clone in
`a scratch file outside the repository`.
Not run: the whole gate (the orchestrator's run), and the sibling installer test files (Minor 9).

## Reaches beyond the dispatch

- `foundations/decisions.md`: WAY-165, WAY-270, WAY-298, WAY-293, WAY-05, WAY-322 read whole, to judge
  items 17, 3, 22, 21 and rows 1–2 against the text.
- `foundations/part_map.md`, the entries `installation` and `project-plan-state-command`, for item 29
  and for the surface of the plan-state reader.
- `project-level/definition_template.md:160-260` (the Technology section), `project-level/technology/running_product.md`
  whole, `settle.md` sub-step 7, `list.md:30-50`, `task-cycle/skill/SKILL.md:60-135`,
  `request_template.md:150-180`, `task-cycle/spec/SKILL.md:48-56`, `task-cycle/spec/design.md:50-75`,
  `instruction-files/writing.md`, `elements/common/skill/build_table.md`, `plan_state.py:340-445`,
  `installation/install.py` (lines 16, 84, 496, 605), `README.md:110-132`. These are the callers and
  neighbours of the changed lines.
- Greps outside `.runs/` for `Request URL and status`, `critique/settle.md`, `report.md`,
  `check of the product`, and `exclusion`.
- The page saved by slice 10
  (`a saved tool result outside the repository`),
  to check the emphasis sentence against its source.
- The slice-3 reviewer's scratch probe
  (`a scratch file outside the repository`),
  run again at head.

## Searches not found or unclear

- The handoff says the agent changed nothing for item 25. Slice 8 did reword
  `project-level/task/template.md:207-208`, and says so in its report.
- No marker or field in the technology step tells a resuming agent which `— projected` item was
  settled "because the matter did not apply" (`running_product.md:38-39`). Part of Important 1.
