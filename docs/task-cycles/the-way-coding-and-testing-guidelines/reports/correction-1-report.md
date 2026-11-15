# Report — correction 1 for the human's remarks

**Status:** done

**Commit:** `3b29618` (range of the correction: `db0c5f8..3b29618`).

## Remarks and how each was made

- **Remark, Fix, Minor finding 4 (WAY-395, `--today`).** In `foundations/decisions.md` (WAY-395) the sentence of *Time and
  randomness* now reads that the test gives the script its time "by replacing the clock function of the script in the process
  of the test or by giving a fixed time to a script that takes one, and no fixed pause". The *complies* example of WAY-395
  changed the same way ("a test replaces the clock function of the script, or gives a fixed time to a script that takes one,
  and does not read the real clock"). `guidelines/testing.md` line 181 (recipe `unit`; the other recipes read "as in `unit`")
  changed to the same wording. What the tests do: `task-cycle/test_gate_times.py:83` replaces `gate_times.now_ms`;
  `process-audit/test_audit_count.py` gives `--today` to a script that has it. No test or script changed.
- **Remark, Fix, Minor finding 3 (pairs of examples).** Each decision keeps its pair only for the part no invariant holds:
  - WAY-380: removed *complies* "the test of the invariant runs Ruff with the flag that ignores comments turning rules off"
    and *violates* "a comment that turns a blocking rule off stays in a file" (both held by `ruff-blocking-rules`). Kept: the
    fix of `F841` in one file with the configuration unchanged, the move of a rule among the examples by a change of the
    decision, a task that turns a rule off in the configuration, a rule of the examples that blocks (the invariant runs Ruff
    with `ruff.toml` and does not check what the configuration holds or that an example rule stays non-blocking).
  - WAY-388, 389, 390, 391: removed the second *violates* clause of each (no `--write` / no `--apply` / exit code 1 for every
    failure / import that reads or writes), held by `generator-writes-only-with-write`, `repository-changer-acts-only-when-told`,
    `command-runner-passes-exit-code`, `shared-module-import-runs-nothing`. Kept in each: the *complies* line that the guidelines
    of the kind list the file as `exemplar` (WAY-388 also its exit code 2) and the *violates* line "another file takes the status
    `exemplar` with no change of this decision" — a part no invariant holds. So no one of the five is left with nothing; the form
    for a decision with no pair did not apply, and I kept the existing form "For the designation, an agent compares ...".
- **Let through** (Minor findings 1, 2, 5, 6, 7) and answer 1: no change, as the remarks bind.

## Files changed

- `foundations/decisions.md`: +14 / -18 (WAY-380, WAY-388, WAY-389, WAY-390, WAY-391, WAY-395).
- `guidelines/testing.md`: +1 / -1.
- Total: 2 files, 15 insertions, 19 deletions.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors").
- `python -B gate/run_tests.py elements/common` — exit 0 (242 tests, OK).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (37 tests, OK, expected failures=2).
- Not run: the full gate (`python -B gate/run_tests.py` with no directory) — the orchestrator runs it after the start signal.

## Own-work check

Requirement most likely not met: a place that still quotes the old phrase, or a removed example that another entry or guideline
quotes. Check: searched `foundations`, `guidelines`, `README.md`, `agent-instructions`, `task-cycle`, `elements` for `--today`,
"reaches the script from outside", "from outside the script", and for each removed example's words across the repository (outside
`.git` and `.runs`). Showed: `--today` as a means of WAY-395 stood only in `foundations/decisions.md` (two places, both changed) and
`guidelines/testing.md:181` (changed); other `--today` hits are in `process-audit` (its own script, tests and skill, true there).
`WAY-395` stands in no other file than those two. Of the removed examples' words, two remain elsewhere and were left: `foundations/decisions.md:8650`
(another decision, about a flag that ignores comments, not a copy of the pair) and `guidelines/coding.md:30` (a *Bad* example of
a guideline, not a decision's pair). No test or `decision:` line quotes WAY-395 or the removed examples.

## Choices

- WAY-395 wording: named both means that the tests of the-way use (a replaced clock function in process, a fixed time for a
  script that takes one); rejected: naming only the clock function — it would leave out the tests of `process-audit` that give
  `--today`. Cost if wrong: a wording only, no code.
- Kept the "another file takes the status `exemplar`" lines in WAY-388 to 391; rejected: dropping the pair whole — that line is not
  held by any invariant. Cost if wrong: one line of an entry.

## Reach beyond the dispatch

None beyond the handoff's own files; I read the decision entries (WAY-380, 388 to 391, 395), the five invariants by their identifiers,
`elements/decisions/template.md`, `task-cycle/change/SKILL.md`, the remarks, and the review's Minor findings (lines 22 to 34 of `review-return-report.md`).

## Working copies

Made one directory, `.runs/correction-1/` (outputs of the three checks); removed. No worktree or clone. Nothing remains.

## Unread material

- `reports/review-return-report.md`: I read its *Minor* section and the first part of the *Against the task* section (lines 22 to 44 of the grep output), not the whole file.
- `.runs/task-cycles/.../request.md` and `task.md`: not read (the handoff points at the request for the findings; the review report carries them).
- `task-cycle/skill/foundation_step.md` (WAY-33 search as the foundation step gives): not read; I did the search by grep as the handoff describes.

## Searches not found or unclear

none
