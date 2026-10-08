# Task 5 — fix round 2 (findings and the controller's ruling)

Re-review of 0683617..5fe6ed1 (opus): findings 1–3 fixed and verified; finding 4 partly; two new faults
in `names_something` (`check_instructions.py:371`), one cause:

1. **Critical — a `/` path through a directory link still makes a network lookup** (`:377–379`).
   `resolve` joins the token onto its base unnormalised, so `via/x.md` is one "part"; `os.lstat` follows
   `via` on the way. `root\via` → `\\192.0.2.1\share`: `via\x.md` 0.0 s; `via/x.md` 70.8 s, ending
   ``WARN `via/x.md` does not exist``. `C:/a/b.md` hits the same split. The test
   `test_a_token_through_a_directory_link_is_not_looked_up_through_it` forbids only `os.path.exists`.
2. **Important — a repository reached through a junction or link above its root silences the dead-path
   and `@` import checks** (`:377–383`): the walk starts at the drive root, so any junction, directory
   symlink or mount among the root's ancestors stops it with "exists" for every token (probe: two
   dead-path WARNs and the missing-import WARN disappear when the same repository is reached through a
   junction or symlink; the same for a `--file` reached through a junction).

**Ruling (one fix):**
- Normalise first: `os.path.normpath` of the joined candidate (which also turns `/` into `\` on
  Windows), then split on `os.sep`.
- For a relative token, walk components **from the base** (the file's directory or the root — the
  directory `resolve` joined onto), never from the drive root: the base itself was reached by the
  caller and is not re-judged. A component below the base that is a link, junction or reparse point
  stops the walk; the token counts as existing and nothing is looked up through it (as ruled in fix 1).
  A `..` that climbs above the base ends the walk as "does not lead anywhere checkable": count it as
  existing only if `os.path.lexists` of the normalised path says so without following links on the way
  — if that cannot be decided without following a link, count it as existing (no finding, no lookup).
- For an absolute token (or `~`-expanded), judge links on its path the way `leads_out` does: follow a
  link whose target is local with `os.readlink` (hop limit), stop on a network-shaped target or the
  limit (count as existing, no lookup); never call a following `stat`/`exists` on it.
- Keep the Windows/POSIX split as in Task 3 (POSIX: `lexists` on the normalised path is enough; it
  cannot reach a network through `lstat`).

**Tests (offline, test first, each failing on 5fe6ed1):**
- a spy on `os.lstat` (and `os.stat`, `os.path.exists`) failing on any path that continues past a
  link's prefix, for `via/x.md`, `via\x.md` and an absolute `C:/…/via/x.md` with `via` a bait directory
  link whose target `pretend_target` makes network-shaped;
- the same repository checked through a junction (or a directory symlink) above its root: the
  dead-path WARN and the "imports a file that is not there" WARN still appear;
- a `--file` reached through a junction: its dead paths still reported.

Rules as before (Write/Edit only; only the two files; standard library; no program; nothing written;
the suite in seconds; the-way 0/1/3; no background process). Commit by paths with the
`Claude-Session:` line. Append "Fix round 2" to `task-5-report.md`; reply with the short contract.
