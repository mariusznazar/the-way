PASS a6ddd8ca313ce3528534db7c1d54d9ef98740c78

# Review of the fix of the failed gate — installer-junction-refusal

Range `e899494..a6ddd8c`, one commit (`Reset one product between subtests instead of assigning self.product again`), one file, `installation/test_install.py`, +16/-11, test code only. `git rev-parse HEAD` in the worktree is `a6ddd8ca313ce3528534db7c1d54d9ef98740c78`, the head given. Reviewed with `review-change` (read whole in the first review of this session; the section for a fix of failed gate applied as the handoff states it).

Counts: blocking 0, Minor 0, out of scope 0. One observation, not graded, below.

## Findings

None.

Observation, not graded: `make_writable` calls `os.chmod(path, stat.S_IWRITE)` on the failing path before it retries. If the failing entry were a junction itself, `chmod` would follow it and clear the read-only attribute of the folder outside (an attribute only, no file removed or changed in content). It cannot happen in these tests: in the probe below the only failing call was `unlink` of a read-only file inside the product, and a junction entry is removed by `rmdir` without a failure. No change asked for.

## The cause the author names is the cause

- Header of `elements/part-map/test_cross_part_imports.py` (lines 1-60 read): a path is worked out from, among others, "the names and `self.<name>` attributes the file assigns, where every plain assignment of the name gives the same value". Before the fix `self.product` was assigned in `setUp` and again in `another_product`, two different values; the two `command(sys.executable, ...)` runs of `test_empty_foundations_*` take their path from `self.product`. After the fix the only plain assignment of `self.product` is in `setUp`.
- Failing run on the unchanged `e899494`, in a scratch worktree of that commit: `python -B gate/run_tests.py elements/part-map` -> exit 1, `Ran 39 tests`, `FAILED (failures=1)`, the diff lists `installation/test_install.py:800` and `:819` "runs a file the check cannot work out". The scratch worktree was removed afterwards.
- Passing run on `a6ddd8c`: `python -B gate/run_tests.py elements/part-map` -> exit 0, `Ran 39 tests`, `OK`.

## Assertions and citations kept

The diff holds no removed or changed assertion: the changes are the helper (`another_product(name)` becomes `empty_product()`), the three call sites, and the move of the local `writable` handler of `test_rejects_a_junction_at_the_submodule_directory` to the module-level `make_writable` (same body). `grep -n "# invariant: installation-paths-through-links" -r installation` finds 6 citations, unchanged (four in `test_install.py`, two in `test_agent_types_installation.py`); the three changed tests keep theirs. The one difference in what a subtest starts from: the product is now emptied and `git init`-ed again in the same directory; before, it was a new directory with `git init`. In both the product carries no `user.email`/`user.name` from `setUp` after the first subtest, so no behaviour changed (these tests make no commit in the product).

## The new helper `empty_product`

`shutil.rmtree(self.product, onexc=make_writable)` on a product holding junctions to folders outside it.

1. **`rmtree` and junctions, Python 3.14.3, tested.** Script `junction_rmtree.py` in the scratchpad (`a file in the reviewer's scratch directory outside the repository`), run as `python -B junction_rmtree.py` -> exit 0. It makes, in a temporary directory, an `outside` folder holding `kept.md`, `sub/deep.md` and a read-only `readonly.txt`; a `product` with two junctions to `outside` (`.claude/skills/the-way-gone`, a nested one, and `foundations`) and a read-only file `.git/objects/pack.idx`; then `shutil.rmtree(product, onexc=make_writable)`. Result: the junction reported true before; `product exists after: False`; `outside` after: `kept.md`, `readonly.txt`, `sub`, `sub/deep.md` (everything intact); the read-only attribute of the outside file was kept; the handler was called once, for `unlink` of `pack.idx` with `PermissionError`. So `rmtree` removes the junction entry and does not follow it, nothing outside the product's temporary directory is deleted, and the handler fixes the read-only file.
2. **The handler retries only the failing call and cannot loop.** `make_writable` does one `chmod` and one `function(path)`; an exception from that second call is not caught by `rmtree`'s handler mechanism and propagates. Tested in the same script: a file held open (so its delete fails persistently) with a handler of the same shape -> `PermissionError` raised after exactly 1 handler call. It does not retry the whole tree.
3. **The outside folders of the tests are untouched when a subtest ends.** Script `outside_probe.py` (scratchpad, same directory) runs the three tests unchanged with `empty_product` wrapped to snapshot every `outside*` folder of the test's temporary directory (names, and the bytes of each file) before and after the reset: `python -B outside_probe.py` from the worktree -> exit 0, `Ran 3 tests in 90.842s`, `OK`, none skipped; for all 22 resets `unchanged_by_reset True`, with the junctions of the earlier subtest still in the product at the reset in 17 of them (the first reset of each test has none). The tests' own assertions guard the same: test 1 asserts after each subtest that its shared `outside` holds only `kept.md` and an unchanged tree.
4. **The last cleanup.** At the end of a test the product, with its last junction, is removed by `TemporaryDirectory.cleanup` as before this commit; the commit changes nothing there. Not checked beyond that (the commit does not touch it).

## Declined to judge

- Whether the installer behaves as the invariant says: this commit holds no installer code; earlier reviews judged that.
- The part-map check's own design (that two assignments of one attribute make it fail): outside the task.

## Checks run

| Check | Command | Exit | Result |
|---|---|---|---|
| range, head | `git rev-parse HEAD`; `git log e899494..a6ddd8c`; `git diff e899494..a6ddd8c` | 0 | head `a6ddd8c...`, one commit, one file |
| failing run on the base of the fix | `python -B gate/run_tests.py elements/part-map` in a scratch worktree of `e899494` | 1 | `FAILED (failures=1)`, lines 800 and 819 |
| part-map after the fix | `python -B gate/run_tests.py elements/part-map` in the reviewed worktree | 0 | 39 tests, `OK` |
| foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| rmtree and junction probe | `python -B junction_rmtree.py` (scratchpad) | 0 | outside folder intact, product gone, handler called once, persistent failure raised once |
| the three tests with a snapshot at each reset | `python -B outside_probe.py` (scratchpad), from the worktree | 0 | 3 tests `OK`, none skipped; outside folders unchanged at all 22 resets |
| citations | `grep -n "# invariant: installation-paths-through-links" -r installation` | 0 | 6 |

Not run: `python -B gate/run_tests.py installation` and the whole gate (the orchestrator runs the whole gate; the installation directory takes about 14 minutes). The three changed tests ran in the probe, the fourth test touched (`test_rejects_a_junction_at_the_submodule_directory`, only its handler moved) and the two `test_empty_foundations_*` tests were run by the author (`Ran 6 tests`, `OK`); I did not rerun those.

## Reaches beyond the dispatch

- `elements/part-map/test_cross_part_imports.py` lines 1-60 (the header), as the handoff names.
- `git worktree add` of `e899494` in the scratchpad and its removal (`git worktree remove --force`), to run the failing check; the reviewed worktree, its index and branch untouched.

## Unread material

- Read whole: the handoff, the author's gate-fix report, the author's gate-fix handoff (first 60 lines, which is all of it), the diff, and the three changed tests with `setUp`, `junction`, `tree_of` and `empty_product` of `installation/test_install.py`.
- Not read: `elements/part-map/test_cross_part_imports.py` past its header (the header states the rule and the two runs confirm it); `test_agent_types_installation.py` beyond its citation lines; the gate log `final-gate.log`.

## Searches not found or unclear

- none
