# Return step report: posix-class-not-a-link

**Status:** done
**Commits:** none in this step. The head stays `15c2062`, and nothing needed correcting.
**Check:** `python -B elements/common/foundation_check.py` exit 0 (0 errors); the tracked-files check exit 0 (275 files, 0 listed). The full gate was not run, as instructed.

## Compared with the code (`task-cycle/skill/return_step.md`)

- **WAY-323** (edited in the foundation step and the fix): binding sentence, *Verification* examples and *Rationale*
  checked against `task-cycle/private_paths_check.py`. The script takes no `[ [:name:] ]` for the twelve names, lists
  `[ [:other:] ]`, and lists a real link on the same line. The examples match the code. No correction needed.
- **WAY-328** (named by the task, *Scope* includes `task-cycle`): still true; the change adds no part. No change.
- **WAY-309, WAY-320, WAY-324** and invariant `tracked-file-private-paths` (found by the search): WAY-309 is narrowed by
  WAY-323 already (*Relations*); the invariant's sentence "a note link as WAY-309 and WAY-323 name them" and its
  *Derives from* still hold. No change.
- **Part map**: `task-cycle` covers `task-cycle/**`; no file is new, and the `tracked-private-paths-command` entry is
  unaffected. No change.

## Written or changed in this step

- Decisions: none beyond WAY-323, which is already in place.
- Invariants, environment facts, glossary, part map: none written. The task asks for no invariant. The glossary has no
  entry for note link or character class (checked earlier), and the change uses no term in a new meaning.
- Projected entries: none (the task is independent).
- Rows written: row 1 (WAY-323), as in the foundation step.

## Open point, not changed

- WAY-323 *Based on* reads `none`. The twelve class names rest on the POSIX definition of character classes. I
  searched the local Git for Windows install (`usr/share`, `usr/share/info`, `usr/share/doc`, `usr/share/man`) and found
  no passage that quotes the twelve names; no external source was fetched. Under the template, a source outside the
  product the decision rests on must be named with its passage quoted word for word, which I cannot supply from this
  checkout. I did not add an environment fact or a `TODO`. For the human: either accept `none` (the names are fixed by
  the list in the decision itself), or give a source to record.

## Unread material

- `task-cycle/skill/foundation_step.md`: read in the earlier step, not again.
- `foundations/environment_facts.md`: only its headings were read, to check for an existing POSIX or shell-class fact; none exists.

## Searches not found or unclear

- A local source for the POSIX character class names with a quotable passage: not found (see the open point above).
