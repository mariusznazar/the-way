PASS 546eb523483a6234f7c09b1852bb86c7e5c0166d

# Review of the whole change: skipped-test-names

Range `2f51e6c..546eb52`, one commit, one author, no plan, no spec. `git rev-parse HEAD` in the
worktree is the head given. Two files change: `gate/run_tests.py`, `gate/test_run_tests.py`.

## Findings

### Critical

none

### Important

none

### Minor

**1. The two new tests hold only one skipped test, in a passing directory, so "each" and a failing
run are not protected.**

- Place: `gate/test_run_tests.py:28-35` (`SKIPPING`), used at `:125` and `:207`.
- What is wrong: To do 1 asks for each skipped test by name. `SKIPPING` holds one skipped test
  beside one passing test, so no test tells "every skip" from "the first skip", or a passing
  directory from a failing one.
- Why it matters: the code at `gate/run_tests.py:43-44` does the right thing today. A later edit
  that dropped all skips but one, or hid them in a failing run, would pass the suite, and a failing
  run is when a reader most wants to see what did not run. `make-change` asks the author to treat a
  mutation no test catches as behaviour left unprotected; the author's report does not name these
  two.
- Evidence: in a scratch worktree of the head, with `python -B -m unittest gate.test_run_tests`,
  the mutations `self.skipped[:1]` and `self.skipped if self.wasSuccessful() else []` both exit 0.
  The behaviour itself is right at the head: the probe below names six skips in one directory and
  names the skip beside a failure.
- Not blocking: To do 3 asks for exactly what the tests hold, and the mutations are unlikely edits
  of a plain loop. Fix if wanted: a second skipped test in `SKIPPING`, and one test with a skip
  beside a failure.

**2. The docstring sentence stands inside the sentence the task places it after.**

- Place: `gate/run_tests.py:10-13`.
- What is wrong: To do 2 places the sentence after the sentence about the `unittest` report at
  `:10-12` of the base. That sentence runs to "names each directory that failed." at `:12`. The
  change instead breaks it at its semicolon ("prints; without DIRECTORY" became "prints. ...
  Without DIRECTORY") and inserts the new sentence between the two pieces. The author's report
  says "after" and does not name the split. Line 12 is also left shorter than its neighbours.
- Why it matters: little. The sentence stands word for word, and "there" reads more clearly
  beside "the one `unittest` prints" than it would after the sentence on the last line of a full
  run. It is a silent departure from the task's position, recorded so that the request does not
  repeat "after".
- Evidence: `git diff 2f51e6c..546eb52 -- gate/run_tests.py`, first hunk.
- Not blocking: the required sentence stands, and nothing reads the docstring by position.

## Coverage of the task

| Item | State | Evidence |
|---|---|---|
| To do 1, one directory | met | `python -B gate/run_tests.py instruction-files`: five skips named with reasons, then dashes, `Ran 104 tests`, `OK (skipped=5)` |
| To do 1, full run | met | scratch repository of seven directories, each directory's report holds its skips before its closing lines; `EveryDirectory.test_a_directory_with_a_skipped_test_still_passes_and_the_report_names_it` |
| To do 2 | met | sentence word for word at `gate/run_tests.py:11-12`; position is Minor 2 |
| To do 3 | met | the test at `gate/test_run_tests.py:204` runs without a directory, in a temporary git repository, and asserts exit 0, name and reason, and "every directory passed" |
| Out of scope, `verbosity=2` | kept | the runner call sets no verbosity; the real run still prints dots |
| Questions to settle | kept | the change holds no guidelines, no decision and no foundation entry; the diff of `foundations/` is empty |
| Settlements to record, projected entries | none in the task | nothing to check |

Fidelity to the task's source: `NamingSkipsResult` and the `TextTestRunner` line are identical to
the task's *Context*, and nothing is added to them. The diff adds no import, no subprocess and no
new file.

## Foundation and guidelines

Part touched: `gate`. Decisions read whole: WAY-09, WAY-16, WAY-38, WAY-51, WAY-53, WAY-55, WAY-60,
WAY-61, WAY-62, WAY-63, WAY-65, WAY-68, WAY-69, WAY-82, WAY-89, WAY-100, WAY-102, and from the
task's *Decisions in play* WAY-215 and WAY-217. Invariants read whole: `gate-exit-code` and those
whose *Part* is `every`.

- **Changed invariant test (WAY-03):** `gate/test_run_tests.py`,
  `EveryDirectory.test_a_directory_with_a_skipped_test_still_passes_and_the_report_names_it`, new,
  cites `gate-exit-code`. The request must name it. No existing test is altered: the diff of the
  file is insertions only.
- Read against the sentence of `gate-exit-code` (WAY-69): the citation holds. The test keeps "zero
  when every test it runs passes" and the clause on a report `unittest` ends with OK. Moving the
  names after `.run` makes it fail at `assertEqual(code, 0, output)` with
  `failed: b (exit code 0 without unittest's OK)`, so it fails on the invariant's own clause.
- Seen failing (WAY-08): the author records `python -B gate/run_tests.py gate` at exit 1,
  `failures=2`, both new tests, then exit 0. Confirmed in kind by the `no-resultclass` mutation.
- `gate-exit-code` and WAY-63 still say what the code does: `wasSuccessful()` and the exit paths are
  untouched, and a failing directory with a skip exits 1, alone and in the full run.
- `test-runner-command` in `foundations/part_map.md`: name, argument and exit codes are unchanged.
- Other invariants of *Part* `every`: `script-language`, `script-imports`, `script-subprocesses`
  and `repository-file-location` hold; the others are not reached by this diff.
- No foundation entry changes, so no finding under WAY-263.
- **Guidelines:** the-way holds no `guidelines/`, so none was read. This is the state WAY-215 would
  hold in refinement, and no decision under WAY-217 departs from it. The task's *Questions to
  settle* carries Mariusz's answer that this task does not wait, and the handoff repeats it, so it
  is no finding of this review.
- Reserved choice: none. The change subclasses a class of the standard library the runner already
  uses (WAY-38).
- Trust boundary: none; the part map gives `gate` none. Operation that cannot be undone: none.
- Author's own-work check: its requirement, names before the closing lines, is the weakest place
  of this change, as the task's *Context* says. Its check runs one directory, where the last-line
  rule of `run_all` does not run, so its exit code would not catch the requirement unmet; reading
  the printed order does, and the full-run test catches it by exit code. No finding.

## Declined to judge

- A multi-line reason beginning a line with `Ran 99 tests in` raises the sum of the full run's last
  line (scratch run: 113 for 14): outside the task, whose *Context* records it as accepted and as
  already possible with `print`.
- Reasons reach a pipe in the console's code page, so non-ASCII text is cp1250 bytes and what that
  cannot hold is escaped, with no crash: the same path as every other line of the report, and no
  requirement of the task.
- A directory whose only tests skip in `setUpModule` passes with `Ran 0 tests` and
  `OK (skipped=1)`: behaviour from before this change, outside the task.

## Checks run

| Command or method | Result |
|---|---|
| `git rev-parse HEAD` | `546eb52...`, the head given |
| `python -B gate/run_tests.py gate` | exit 0, 20 tests, OK |
| `python -B -m unittest discover -s gate -p "test_*.py"` | exit 0, 20 tests, OK |
| `python -B gate/run_tests.py instruction-files` | exit 0, 104 tests, `OK (skipped=5)`, five named with reasons |

Mutations of `gate/run_tests.py`, in a scratch worktree of the head since removed, each with
`python -B -m unittest gate.test_run_tests`:

| Mutation | Exit | Tests that failed |
|---|---|---|
| `resultclass` removed | 1 | both new tests |
| names written after `.run` | 1 | both new tests |
| reason dropped | 1 | both new tests |
| name dropped | 1 | both new tests |
| names before the lists of errors | 1 | the one-directory test |
| `self.skipped[:1]` | 0 | none (Minor 1) |
| only when the run succeeds | 0 | none (Minor 1) |

Manual probe: the head's runner on a throwaway git repository of seven directories, Python 3.14.3,
one directory at a time and in a full run. Every kind gave one line and the closing lines stayed
last:

- `@skip`, `skipTest`, `skipTest` in `subTest` (one line per subtest), a skipped class, one line
  each;
- `setUpClass` and `setUpModule` as `setUpClass (module.Class)` and `setUpModule (module)`, which
  the task's *Context* expects;
- `SkipTest` at the top of a module, not in the task's trial, as
  `unittest.loader.ModuleSkipped.<module>`: the module's name stands last and the reason is given;
- reasons of `None`, a tuple and `100% %s %d`, written as they are, no formatting error;
- a skip beside a failure: named after the failure, exit 1, directory listed as failed in the
  summary.

Not run:

- The full `python -B gate/run_tests.py` on the repository: the cycle's own run, by the handoff and
  section 2.
- Any run on Linux: only this Windows machine was available.
- The task's citations into loop2 (`docs/task-cycles/plomyk/cycle.md:136`, `scripts/test.py:31,45`)
  and `docs/task-cycles/plan-partial-foundation/cycle.md:87` at `94adb60`, and the count of 615
  tests: nothing in the change takes from them.

## Reaches beyond the dispatch

- WAY-03, WAY-08, WAY-10 in `foundations/decisions.md`: their *Scope* does not name `gate`; read
  because the change adds a test citing an invariant.
- `task-cycle/change/SKILL.md:55-91`: to judge the author's test-first record and own-work check.
- `task-cycle/skill/SKILL.md:390-399` and `task-cycle/record_template.md:126`: to check the task's
  citations of the rule that the request names each check that did not run. Both say so.
- `README.md:140-155`: to check that no text describing the report turned false. None did.
- `project-level/technology/reserved_choices.md`: named by section 2 of the skill.

## Searches not found or unclear

- `foundations/environment_facts.md` and `foundations/glossary.md` hold no entry on `unittest` or
  on skipped tests, by a search of both. Nothing in this change needs one.
- To do 2's `:10-12` covers a whole sentence, and "after" could be read as after its first clause,
  which is the reading the change took (Minor 2).
