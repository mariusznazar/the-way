# Task 3 — fix round 2 (findings and the controller's ruling)

A prior implementer made fix round 1 (commit c06b237; ruling `task-3-fix-1.md`; its fix report at the
end of `task-3-report.md` — read both). You own the task now. The scoped re-review (opus) found the
network part fixed on Windows and these open findings in the fix diff:

1. **Critical — on POSIX every file link out of the repository is read** (`check_instructions.py:136-137`).
   `leads_out` passes every link target through `local_form` (`/` → `\`); on POSIX `/tmp/x/secret.md`
   becomes `\tmp\x\secret.md`, which `posixpath.isabs` does not treat as absolute; joined under the
   link's directory it looks inside the root, so the link is listed and `read_text` follows the real
   link out. Also on POSIX, `normpath` removes `..` by text, while the kernel resolves `..` after a
   directory link, so `dirlink/../x` can be judged inside when it is not. Round 0's `realpath` was
   right on POSIX.
2. **Important — a deep tree crashes the run** (`:188`): `visit` recurses once per directory level;
   about 1000 levels (reproduced at 1100, path 2328 characters) gives `RecursionError`, a traceback,
   exit 1 — against "the run goes on, no traceback".
3. **Important — the tests create real links to `\\192.0.2.1\share\x.md`, and creating them contacts the
   network** (`os.symlink` checks whether the target is a directory: 20–30 s per link, ~90 s per Windows
   run). The network guard (`guard_network_paths`, `:94`) cannot see the operating system following a
   link inside `DirEntry` calls, so a regression would show only as slowness.
4. **Important — on POSIX a directory link out of the root gets no finding** (`:145-154`,
   `directory_link`): without `st_file_attributes` such a link counts as "not a directory" and, not
   being an instruction file name, is dropped unreported — against the row "a directory symlink …
   `INFO` 'a link to a directory, not followed'".

## Ruling (the fix to make)

- **Platform split (1, 4).** Network paths are a Windows lookup problem; on POSIX a share is a mounted
  directory. Decide once, in a module constant (e.g. `WINDOWS = os.name == "nt"`):
  - On Windows keep round 1's behaviour: link chains followed with `os.readlink` only, `local_form` and
    the network-shaped test, never opening a target.
  - On POSIX use `os.path.realpath` of the link and `inside(real, root)` — as round 0 did — and no
    `local_form`; a link whose real path is outside the root is "a link out of the repository".
  - Directory links: on POSIX decide "is it a directory" with `entry.is_dir()` (it follows the link,
    which cannot reach a network there) and report **every** directory link or junction as
    `walk` INFO "a link to a directory, not followed", wherever it points; on Windows keep the junction
    and directory-symlink handling of round 1 without following.
- **Deep trees (2).** Walk with an explicit stack (no recursion), same order and findings as now. Add a
  test with a tree deeper than the interpreter's recursion limit (build it with relative `os.makedirs`
  from inside the temporary directory so the path length stays within the platform's limit, or skip
  with the reason where it cannot be built).
- **Offline tests (3).** No test creates a link whose target is a network path. For the network cases,
  create the link to a **local** file holding a marker string, and patch `os.readlink` (in the module's
  namespace) to return the network path for that link; the correct code reports "a link out of the
  repository" and never touches anything; a regression that follows the link reads the local marker
  and the test fails at once, offline. Keep the guard that fails on a network-shaped argument to
  `os.stat`, `os.lstat`, `open`, `os.path.realpath`, `os.path.exists`.
- **POSIX branch coverage.** Tests that only make sense on POSIX (a file symlink out of the root read
  through `realpath`; a directory symlink out of the root reported) carry
  `@unittest.skipUnless(os.name == "posix", …)` with a reason; Windows-only ones the converse. The
  whole suite must still pass on Windows here; the POSIX run is recorded as unchecked by the controller.
- **Network ROOT refusal** (round 1, beyond its ruling) stays; it agrees with the refused network
  `--file`.

Deferred (ledger): `..` in a Windows link target resolved by text (`junction\..\x`) — unverified.

## Constraints

Edit only `instruction-files/check_instructions.py` and `instruction-files/test_check_instructions.py`,
with the Write/Edit tools (never a shell heredoc, printf or python -c — they collapse backslashes). Keep
every name Task 3's brief lists under "Produces" with its signature (Tasks 4 and 5 use them). Python
3.14 standard library only; the script starts no program and writes nothing. Test first: write the new
tests, see them fail on c06b237 (name which and why), then fix. Run `python -B gate/run_tests.py
instruction-files` (the suite must finish in seconds, not minutes) and the script on the-way
(`python -B instruction-files/check_instructions.py .`, expected 0 error, 1 warn, 3 info). Never leave
a background process or monitor running when you report. Commit by paths, message in the repository's
style ending with `Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ`. Append a
"Fix round 2" report to `task-3-report.md`: RED and GREEN commands and output, what changed, the
covering tests, the suite's run time.
