# Task 3 — fix round 3 (findings and the controller's ruling)

Re-review of fix round 2 (opus): findings 1, 2, 4 ADDRESSED; finding 3 partly. Open:

1. **Important — the offline network tests cannot catch the original Critical if it returns**
   (`NetworkPaths`, `test_check_instructions.py:326-351`, `pretend_target`). A walk that follows a link
   only to classify it (as `os.walk`'s `entry.is_dir()` did) follows to a harmless local file: findings
   unchanged, guard blind (the OS follows inside `DirEntry`). Reproduced: planting `entry.is_dir()`
   before the walk's classification leaves all four `NetworkPaths` tests passing.
   **Fix (reviewer's, accepted):** create each link while its local target does not exist yet (so it is
   a file link), then create a **directory** at that target. The correct code still reports "a link out
   of the repository, not read"; a regression that follows the link to classify it sees a directory and
   reports "a link to a directory", so the test fails at once, offline. Show RED by planting the
   regression temporarily (do not commit it) and name the output in the fix report.
2. **Minor — `DeepTree` fails where paths are limited to 1,024 characters (macOS).** Lower
   `sys.setrecursionlimit` temporarily in the test (restore it with `addCleanup`) and build only a few
   hundred levels, so the deepest absolute path stays well below 1,024 characters while still deeper
   than the lowered limit.
3. **Minor — no POSIX test for a link loop** ending as a `read` WARN "cannot be read: …"; add it next to
   the other POSIX-only tests (skipped on Windows with the reason).
4. **Comment** — soften the docstring/comment claiming that following a link off Windows "cannot reach
   a network": say it reaches only what the system has mounted.

Constraints as in `task-3-fix-2.md`. Append "Fix round 3" to `task-3-report.md` (RED with the planted
regression, GREEN, run time) and reply with the short status contract.
