# Report 03 — the fix of the Minor findings of the whole-change review

**Status:** done

**Commit:** see the line "Commits" at the end (one commit on top of `287a027`).

## Findings as fixed

1. **WAY-320 rationale, the number (`foundations/decisions.md`).** Fixed in place: "listed 73 such
   texts among 88 findings" now reads "listed 71 such texts in code among 88 findings". I checked the
   source: `task.md` gives 73 `[[...]]` hits, of which 70 are arrays in arrays and 1 a shell class
   (71 in code) and 2 are specification slots in a Markdown file, which the Markdown-only rule does
   not remove (WAY-323 does). Every other word of the entry is unchanged. Check:
   `python -B elements/common/foundation_check.py` exit 0, 0 errors.
2. **README, the exit codes and the backticked texts (`installation/README.md`).** Fixed: the README
   now gives exit 2 for each case in the command's docstring: the identifier not given once, no git
   repository, `foundations/invariants.md` or the invariant not there, a named file git does not
   track, a tracked file that is not UTF-8 text; and that a file with a NUL byte near its start is
   counted as binary and not read. It also says that every text between backticks in the sentence is
   read as the path of such a file, so the sentence holds no other backticked text. Each case is one
   the tests of `task-cycle/test_tracked_private_paths_check.py` already run (missing or surplus
   argument, outside a repository, no invariants file, invariant absent, untracked named file,
   cp1250 file, binary file), so the text matches the command's behaviour.
3. **README, *Derives from* of the product's invariant.** Fixed: the README now says the *Derives
   from* of the invariant names a decision of the product's own log that records the choice (the
   repository is public, so no tracked file holds such a path or link), or, where the product has no
   such decision, the source of the rule as the invariant template's "Links" gives (address, place,
   quoted passage, date read); and that a decision of the-way is no decision entry of the product,
   so WAY-324 is not written there. This follows `elements/invariants/template.md` "Links"
   ("An entry that no decision entry of the product's own log carries ... names in *Derives from* each
   such source ..."; "A decision named anywhere but the product's own log — ... a decision of the-way
   at the commit the product pins — is no decision entry of it"). I wrote nothing the template does
   not allow.

No finding is contested.

## Checks

| Check | Result |
|---|---|
| `python -B elements/common/foundation_check.py` (after the decision edit) | exit 0, 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (the README and the decision are tracked files) | exit 0, 275 files, 0 listed |
| `python -B gate/run_tests.py installation` (after the README edit) | see the line "Installation run" at the end |
| whole gate | not run (the orchestrator runs it) |

No code and no test changed, so no other focused check applied; the command's exit codes in the
README were read against `task-cycle/tracked_private_paths_check.py` (the docstring, lines 20-23, and
`main`) and against its tests.

## Own-work check

- Requirement the fix most likely does not meet: "say all the exit codes the command gives". Check:
  the README list was compared case by case with the code's `PrivatePathsError` raises (argument
  count or leading `-`; git failing, including no repository; invariants file unreadable or invariant
  heading absent; empty sentence; named file untracked; file not UTF-8) and with the test names above.
  One case is in the code but not named in the README: the empty sentence under the heading and
  `git` not startable; both fall under "cannot check" in the README's wording and give the same exit 2
  with a message.
- The new README text holds no absolute path and no note link: the command above lists 0.

## Reaches beyond the handoff

- `elements/invariants/template.md` "Links" (lines about *Derives from*): read, as the handoff
  asked ("check the invariant template and the foundation skills"). `elements/invariants/skill/*`
  were read in the first pass of this change, not again.

## Searches not found or unclear

none

## Closing lines

Installation run: `python -B gate/run_tests.py installation` exit 0, 44 tests OK (run on the README
as committed).

Commits: `578a8bd` (on top of `287a027`; files `foundations/decisions.md`, `installation/README.md`).
