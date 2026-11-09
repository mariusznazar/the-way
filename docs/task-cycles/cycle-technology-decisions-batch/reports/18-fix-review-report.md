PASS 75fe0e37597b7f1b6d4a5b98f57ab5e4796d77a2

# Review of the fix — cycle-technology-decisions-batch

Fix range `6349019187409079f93cc41bf3f39df9d90b1adb..75fe0e3`, 4 commits (`66d36cd`, `4515b4d`,
`4fbe357`, `75fe0e3`). `git rev-parse HEAD` is `75fe0e37597b7f1b6d4a5b98f57ab5e4796d77a2`, the head
given. I computed `git diff 6349019..HEAD` and `git log` myself, and read `task-cycle/review/fix.md`,
the findings file (`reports/16-fix-findings.md`) and the fix report (`reports/17-fix-report.md`). The
fix report was a set of claims to check; each verdict below rests on my own reading and runs.

Counts: blocking findings remaining 0. Minor findings remaining 1 (Minor 4, the part about WAY-298).
New findings in the fix diff: 0 Critical or Important, 1 Minor.

## The findings, one by one

### Blocking 1 — fixed

- `project-level/technology/list.md:42-45` and `running_product.md:21-24`: the example now gives all
  three parts of the logs matter. It reads "the tool prints to the console, the record lives as long
  as the run, an agent reads it from the terminal", the same as WAY-322's *complies* example. The
  sentence also says the answer gives "every part the matter asks".
- The bullet that took a "did not apply" item out of the re-check (`running_product.md:38-39` at the
  old head) is gone. Such an item now goes through the existing bullets: a full answer stays, and a
  silent one goes back to `— open`, as WAY-165 requires.
- `start.md:21-23` now reads "settled by that answer, and its item is read like any other". With the
  bullet gone, the bare `— projected` marker and the missing distinguishing marker are gone too.

### Blocking 2 — fixed

- `installation/test_install.py:45-47`: `setUp` now copies the working-tree
  `installation/install.py` over the clone's copy, after the clone's HEAD is read. The pin and the
  expected commit still both come from the clone, so the concurrent-commit fix of item 9 stands.
- Evidence: in my scratch clone at `75fe0e3` (outside the reviewed worktree), the test
  `test_preview_apply_rerun_and_preserve_foundation` passed with a clean tree (exit 0). I then added
  `raise SystemExit(9)` under `if __name__ == "__main__":` of `install.py`, uncommitted. The same
  test failed (exit 1), and so did
  `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` (exit 1). At the old head the
  same probe passed (exit 0), so the defect is gone.

### Minor 1 — fixed

- `project-level/plan_state.py:167` now reads `result.stdout.split(b"\n")`. My probe at head: a record
  with the wording, then `\r`, then `IGNORE PREVIOUS INSTRUCTIONS` gives no blocked line. At the old
  head it gave one.
- The crafted-input test now has a lone-`\r` case (`project-level/test_plan_state.py:257-258`).
- A CRLF record is still recognised (the existing CRLF test passes), because `rstrip(" \t\r")`
  handles a trailing `\r`.
- Pointer lines lose nothing: `PR_LINK.findall` runs on the whole line text, so a URL after a lone
  `\r` is still found.

### Minor 2 — fixed

- The docstring of `record_requests` (`plan_state.py:155-158`) states the limit: no Markdown structure
  is read, so a fenced block is read as the field, the pointer lines share the limit, and lines end
  at `\n`. My probe still recognises the fenced case, which is the documented limit.

### Minor 3 — fixed

- `plan_state.py:163` passes `BLOCKED_DRAFT` itself to `git grep -E`, and a comment says why. The
  constant holds only letters, digits, spaces, `-`, `,` and `:`. None of these is special in POSIX
  ERE outside a bracket expression, so the pattern is defined on any engine. A later edit that adds a
  special character is warned by the comment. No test covers it, which is acceptable for a constant.

### Minor 4 — fixed in the skill; the part about WAY-298 remains (Minor, blocks nothing)

- `task-cycle/skill/SKILL.md:119` now reads "the one change the cycle makes to a checkout outside the
  task's worktree". This agrees with `:68-69`, which names two exceptions, the fast-forward and the
  account of the request. The account is a write to the backlog, not to a checkout, so the skill no
  longer contradicts itself.
- What remains: WAY-298's last sentence (`foundations/decisions.md:9441-9442`, "The fast-forward is
  the one change the cycle makes outside the task's worktree") still has no qualifier, and the
  handoff forbids the fix to touch it. The skill is now narrower than the decision. A reader who
  counts across the two files finds one exception in the decision and two in the skill. I grade
  this Minor and not a new finding of the fix: the fix made the skill internally consistent and did
  not widen the gap. Recommended: put a one-word qualification of WAY-298 ("to a checkout") before
  the human, in the request's *For you to decide*, or in a later task.

### Minor 6 — fixed

- `task-cycle/test_remarks_check.py:367` is renamed `test_files_that_are_no_reports_are_not_read`. No
  other reference to the old name exists outside `.runs/` (searched).

### Minor 7 — fixed

- `instruction-files/writing.md:14-16`, step 4, now points to the bullet "A rule names things in the
  words its readers use for the product" of `SKILL.md`. The examples stand only there, so the rule
  has one place.
- One small effect: the old step also listed `Rules` as an example, and that example is now gone. It
  needs no action.

### Minor 8 — fixed

- `task-cycle/spec/SKILL.md:53` and `task-cycle/skill/SKILL.md:193` no longer say "of the product".
  Both now match WAY-148.

## New in the fix diff

- Minor (new, within the task): `task-cycle/skill/SKILL.md:119` is now 110 characters, past the file's
  wrap of about 100. It is cosmetic.
- No Critical or Important finding. Trust boundary: the output lines of `plan_state.py` are unchanged
  in form. They are built from fixed words, the path Git lists (through `display`) and the commit id.
  Recognition is now stricter, not looser, and the only subprocess is still Git.

## Declined to judge

- Whether WAY-298 should be qualified: the handoff forbids the fix to touch any decision, so this is
  for the orchestrator or the human (see Minor 4).
- Whether a failing subtest of the crafted-input test should stop affecting the later subtests (the
  fix report's "problem observed"): it is a property of the existing test fixture and is outside the
  findings file.

## Checks

| Check | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `75fe0e37597b7f1b6d4a5b98f57ab5e4796d77a2` |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `git diff --check 6349019..HEAD` | 0 | clean |
| `python -B gate/run_tests.py task-cycle` | 0 | 211 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 275 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0 | 104 tests OK, 5 skipped (the Windows link tests) |
| `python -B -m unittest discover -s installation -p "test_install.py"` | 0 | 30 tests OK (115 s) |
| `python -B -m unittest discover -s installation -p "test_installed_guidance.py"` | 0 | 4 tests OK |
| Installer probe: a scratch clone at `75fe0e3`, clean, then with `install.py` broken uncommitted | 0 / 1 / 1 | clean passes; broken fails both tests run (Blocking 2 fixed) |
| `plan_state.py` crafted-input probe at head (`scratch_review.py`, `python -B -I`): lone `\r`, fenced block, form feed, no-break space, wording beside a real URL | 0 | lone `\r`: not recognised (Minor 1 fixed). Fenced: recognised (documented limit, Minor 2). Form feed and no-break space: not recognised. No record text in the output |

The reviewed worktree, its index and its branch were not changed. The probes ran in
`a scratch file outside the repository`
and in temporary repositories. Not run: the whole gate (the orchestrator's run).

## Reaches beyond the dispatch

- `foundations/decisions.md:9432-9442` (WAY-298), to judge what remains of Minor 4.
- `a scratch file outside the repository`,
  my probe from the review of the whole change, run again at the fix head.

## Searches not found or unclear

none
