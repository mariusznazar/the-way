# Task 5 — fix round 1 (findings and the controller's ruling)

Task review (opus) of fe55716..0683617: functional requirements met; two Critical findings on the trust
boundary, one Minor, and one gap in the base code the controller brings into this round.

1. **Critical — a `.git` link sends the nested-repository test to the network**
   (`check_instructions.py:497`, `os.path.exists(os.path.join(root, *parts[:depth], ".git"))` follows
   links; `dir/.git` linked to `\\192.0.2.1\share\x.md` with `AGENTS.md` naming `dir/a.md`: a 20.2 s
   stall). **Fix:** `os.path.lexists`, as the walk does (`:222`): a `.git` link counts as a nested
   repository. **Test (offline):** a `.git` link made with the existing bait-link helpers (or a spy on
   `os.path.exists`) proving `exists` is never called on a `.git` entry and the pointed file is skipped.
2. **Critical — a NUL in a backticked `.md` token crashes the run** (`:504`: `os.stat` raises
   `ValueError: embedded null character`, not caught by `except OSError`). **Fix:** drop tokens holding
   `\x00` before any path is built (and catch `ValueError` beside `OSError` around the stat); **test:**
   a root `AGENTS.md` naming `` `guide/a<NUL>.md` `` — exit 0, no traceback.
3. **Minor — skipped directories judged on the path as written, not the real path** (`:493–495`; a
   `docs` link to `node_modules/pkg` lets a pointed `docs/a.md` be read). **Fix:** apply the
   skipped-directory and nested-repository checks to the real path relative to the real root too,
   after `realpath`. Test it.
4. **Brought into this round by the controller (same file, same rule; not in the diff):** `resolve`
   (`:383`) calls `os.path.exists` on candidate paths, which follows a file link or a directory link in
   the path; a root `AGENTS.md` naming `linknet.md` (a symlink to `\\192.0.2.1\…`) stalled 20–30 s.
   **Fix:** decide whether a token's path exists without following any link on the way: check the
   candidate with `os.path.lexists`, and on Windows, before that, walk its components from the base with
   `os.lstat` and stop at the first component that is a link or junction — a token reached through a
   link counts as existing (no dead-path finding) and is never looked up through the link. **Test
   (offline):** a token naming a file link and a token through a directory link, both with network
   targets via the bait helpers / `pretend_target` — no lookup through the link, no dead-path finding.

Rules as before: test first (show each new test failing on 0683617), Write/Edit tools only, only the two
files of `instruction-files/`, Python 3.14 standard library, no program started, nothing written, the
suite in seconds, the script on the-way unchanged (0 error, 1 warn, 3 info), no background process left.
Commit by paths with the `Claude-Session:` line. Append "Fix round 1" to `task-5-report.md` and reply
with the short status contract.
