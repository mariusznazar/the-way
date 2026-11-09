# Findings of the review of the whole change, `FAIL 6349019` (report `reports/15-whole-change-review-report.md`)

Cut word for word from the reviewer's report. Blocking findings first, then the Minor findings within the task.

## Blocking (Important)

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

## Minor findings within the task (to fix with the blocking ones; numbering is the report's)

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
