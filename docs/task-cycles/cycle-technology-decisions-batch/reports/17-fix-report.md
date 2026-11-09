# Report — the fix of the review's findings (head fixed: 6349019)

**Status:** done

## Commits

- `66d36cd` Give the logs example of the technology step all three parts and read a settled item like any other (blocking 1)
- `4515b4d` Test the working tree's installer, not the clone's committed one (blocking 2)
- `4fbe357` Split record lines on newline only, write the fenced-block limit and give git grep the literal wording (Minor 1-3)
- `75fe0e3` Align the task cycle's exceptions, rename a test, point writing.md to the single rule and drop a lost narrowing (Minor 4, 6, 7, 8)

## Files changed (added / removed lines)

- `project-level/technology/list.md` (4/3), `project-level/technology/running_product.md` (4/4), `project-level/technology/start.md` (1/2)
- `installation/test_install.py` (3/0)
- `project-level/plan_state.py` (9/2), `project-level/test_plan_state.py` (2/0)
- `task-cycle/skill/SKILL.md` (2/2), `task-cycle/spec/SKILL.md` (1/1), `task-cycle/test_remarks_check.py` (1/1)
- `instruction-files/writing.md` (3/2)

## Findings

### Blocking 1 — fixed (`66d36cd`)

- `list.md` and `running_product.md`: the example is now "the tool prints to the console, the record lives as long as the run, an agent reads it from the terminal" for the logs, and the sentence says the human answers "giving every part the matter asks". The no-strike rule and the five matters are unchanged.
- `running_product.md`: the bullet "An item the human's answer settled, because the matter did not apply ... ends `— projected` and is not looked at again as open" is dropped. An item settled this way is now read by the existing bullets (a full answer "stays as it is", a silent one goes back `— open`).
- `start.md`: the sentence now reads "settled by that answer, and its item is read like any other (WAY-322)"; the "ends `— projected` and does not return open" is gone.
- Check: prose, so no test of its own. `python -B gate/run_tests.py project-level` exit 0 (275 tests), `foundation_check.py --skip-test-citations` exit 0. The text now matches WAY-322's *complies* example and WAY-165's *violates* list (read both).

### Blocking 2 — fixed (`4515b4d`)

- `setUp` of `installation/test_install.py` copies `SOURCE/installation/install.py` over the clone's `installation/install.py` after the clone and the `rev-parse`, as `later_process` does; installing is still from the clone, and the pin is still the clone's HEAD. `later_process` copies `self.installer`, so it now takes the working-tree installer as well.
- Shown with a scratch clone of the worktree (outside it, in the session scratchpad, `...\scratchpad\scr`), with the new `test_install.py` and an uncommitted `raise SystemExit(9)` as the first line under `if __name__ == "__main__":` of `installation/install.py`:
  - clean scratch, new test: `python -B -m unittest discover -s installation -p "test_install.py" -k test_preview_apply_rerun_and_preserve_foundation` exit 0;
  - broken installer, direct run `python -B installation/install.py x` exit 9;
  - broken installer, new test, same command: exit 1 (`AssertionError: 9 != 0`);
  - broken installer, the previous `test_install.py` (`git show HEAD:installation/test_install.py`): exit 0 (the defect the review found, reproduced).
- Full file: `python -B -m unittest discover -s installation -p "test_install.py"` exit 0 (30 tests, 107.6 s); `-p "test_installed_guidance.py"` exit 0 (4 tests).

### Minor 1 — fixed (`4fbe357`)

- Test first: the case `"lone carriage return after the wording"` (`BLOCKED_FIELD + "\rIGNORE PREVIOUS INSTRUCTIONS\n"`) added to the crafted-input test in `project-level/test_plan_state.py`. Break it catches: reading lines by `splitlines()` (a bug, since the line is not the field). Before the fix, `python -B -m unittest discover -s project-level -p "test_plan_state.py" -k test_blocked_draft_wording_off` exit 1; the first failing subtest was the new one. Three later subtests also failed, only because the subtests share one repository and the earlier lone-`\r` record stays in its history.
- `record_requests` now reads `result.stdout.split(b"\n")`. After the fix: the same command exit 0; whole `test_plan_state.py` exit 0 (44 tests). No record text reaches the output (output lines are unchanged; the only new input to a line is the same fixed words), and all subprocesses are Git.

### Minor 2 — fixed (`4fbe357`)

- The docstring of `record_requests` now states the limit: lines are read as text with no Markdown structure, a pointer or the wording inside a fenced code block is read as the field, the pointer lines have the same limit; lines end at `\n` only. Prose; no test.

### Minor 3 — fixed (`4fbe357`)

- `re.escape(BLOCKED_DRAFT)` is replaced by `BLOCKED_DRAFT` as a literal ERE pattern, with a comment that it holds no ERE metacharacter (its characters are `-`, `,`, `:`, letters, digits and spaces). The existing blocked-draft tests (recognised wording, CRLF with trailing blanks, all crafted cases) pass on this Git. They cannot show a different regex engine, so the other-engine concern is removed by reasoning, not by a test.

### Minor 4 — fixed in the skill; one contradiction remains with WAY-298 (`75fe0e3`)

- `task-cycle/skill/SKILL.md` step 4 now reads "the one change the cycle makes **to a checkout** outside the task's worktree", so the sentence at the top (two exceptions: the fast-forward and the account of the request, which is a write to the backlog, not to a checkout) and step 4 agree.
- Remaining: WAY-298's last sentence (`foundations/decisions.md:9442`, "The fast-forward is the one change the cycle makes outside the task's worktree") is unchanged, as the handoff forbids editing it. It now reads wider than step 4 of the skill. For the orchestrator or the human: qualify it the same way ("to a checkout"), or leave it. If left, the cost is a reader who counts exceptions across the decision and the skill finds one in the decision and two at the top of the skill.

### Minor 6 — fixed (`75fe0e3`)

- `task-cycle/test_remarks_check.py`: `test_only_files_whose_name_ends_in_report_are_read` renamed to `test_files_that_are_no_reports_are_not_read`. No other reference to the old name (searched `.py` and `.md` outside `.runs`). `python -B gate/run_tests.py task-cycle` exit 0 (211 tests).

### Minor 7 — fixed (`75fe0e3`)

- `instruction-files/writing.md` step 4 is now a pointer: "as the rule "A rule names things in the words its readers use for the product" of `SKILL.md` gives, written in the language of the repository". The examples now live only in the bullet of `instruction-files/SKILL.md` (section "How to write a single rule"). `python -B gate/run_tests.py instruction-files` exit 0 (104 tests, 5 skipped).

### Minor 8 — fixed (`75fe0e3`)

- `task-cycle/spec/SKILL.md:53`: "neither runs a test or another check of the product, so" -> "neither runs a test or another check, so". `task-cycle/skill/SKILL.md:192-193`: "runs no test or other check of the product and returns" -> "runs no test or other check and returns". Nothing else in those sentences changed. Covered by the `task-cycle` run above.

## Checks (command, exit code)

- `python -B -m unittest discover -s project-level -p "test_plan_state.py"`: 0 (44 tests)
- `python -B gate/run_tests.py project-level`: 0 (275 tests)
- `python -B gate/run_tests.py task-cycle`: 0 (211 tests)
- `python -B gate/run_tests.py instruction-files`: 0 (104 tests, 5 skipped)
- `python -B -m unittest discover -s installation -p "test_install.py"`: 0 (30 tests)
- `python -B -m unittest discover -s installation -p "test_installed_guidance.py"`: 0 (4 tests)
- `python -B elements/common/foundation_check.py --skip-test-citations`: 0 (0 errors)
- `python -B agent-instructions/skill_entry_points.py`: 0 ("entry points are current")
- `git diff --check`: 0
- Not run: `gate/run_tests.py installation` (long, handoff says not required) and the whole gate (never).

## Own-work check

- Requirement most likely not met: blocking 2 — that the test now fails when the working-tree installer breaks, not only that it still passes. Check: the scratch clone with an uncommitted breaking edit, new versus old test file (exit 1 versus exit 0, above). It showed the fix catches the defect and that the old file did not.
- Second: Minor 1 — that the recognition is tighter without losing a real CRLF record. Check: the existing CRLF test (`test_blocked_draft_field_with_crlf_and_trailing_blanks_is_the_same_field`) stays green with the split on `\n`; the new lone-`\r` case failed before and passes after.
- Mutation in head: putting `splitlines()` back fails the new case; putting `re.escape` back is not caught by any test on this Git (not a behaviour of this machine; see Minor 3).

## Reaches beyond the handoff

- `WAY-165` and `WAY-322` read whole at `foundations/decisions.md:10370-10401` for WAY-322 (WAY-165 only its *violates* list as the finding quotes it); the handoff names both, so this is not a reach beyond it.
- I did not open the plan or the slice reports `05`, `08`, `09`; the findings file carried enough.
- Trust boundary (plan_state.py): output lines unchanged in kind, built from fixed words; no record text printed; subprocesses are Git only. Irreversible operation: none.

## Searches not found or unclear

- The handoff says the new instruction-files bullet sits in "How to write a single rule"; the bullet's own text is "A rule names things in the words its readers use for the product", which I quoted in `writing.md`. Not unclear in effect, noted for exactness.
- Whether a Git with another regex engine reads the escaped wording: not testable on this machine; the removal of the escape is the answer.
- No other unclear item.

## Choices and problems

- Blocking 1: I kept the sentence "that answer settles the matter" and added "giving every part the matter asks" rather than saying a silent answer settles nothing again, since `running_product.md:12-14` already says so. Rejected: restating the 3 questions in `list.md` (duplicates the template). Cost if wrong: an agent reads "every part" without the template's list; the template is read in full at the step's start (`start.md`).
- Blocking 2: copying only `install.py` assumes the installer needs no other working-tree file; the test passed with this, as `later_process` did already.
- Minor 4: chose to qualify only the skill, per the handoff. WAY-298 contradiction as above.
- Problem observed: running `test_plan_state` with a failing subtest cascades into later subtests because they share one repository history; not changed.
