# Report — executor of slice 11, task `scripts-after-foundation-review`

**Status:** done

**Slice:** 11 — The generator of the agent type copies ends with exit code 2 at a missing `name:` or `description:`

**Worktree:** `the root of the task's worktree`, branch `task/scripts-after-foundation-review`

## Commits

- `34e7692` — Exit with code 2 when an agent type definition lacks its name or description line (author as configured for the private repo, per the git rules)

## Files changed

| File | Added | Removed |
|---|---|---|
| `agent-instructions/agent_type_copies.py` | 33 | 1 |
| `agent-instructions/test_agent_type_copies.py` | 28 | 0 |

## What changed

- `agent-instructions/agent_type_copies.py`:
  - New `MissingFieldError(GeneratorError)`, raised by `check_definition` only when the head regex fails, the file opens with `---`, and the frontmatter (up to the closing `---`) has no line whose key is `name` or `description`.
  - New `missing_field(text)` helper: returns the first of `name`, `description` with no line in the frontmatter, matched case-insensitively with leading whitespace allowed; returns None otherwise.
  - `main` maps `MissingFieldError` to exit code 2 with `Error: <path>: the frontmatter has no line `<field>:`` on stderr. Every other error still goes to exit 1.
  - Module docstring's exit-code line now names exit code 2 and both fields.
- `agent-instructions/test_agent_type_copies.py`:
  - New class `MissingField` with two tests: a definition without `name:` and one without `description:`. Each asserts `(2, "", <message naming file and field>)` and that no file is written.
  - New `Errors` case "name in another form" (`Name: the-way-stage`): asserts exit 1 with the existing "must open with" message, so a line in another form is not claimed missing.

## Checks

Each check, its command and exit code:

1. **Red on the base (new tests, before the code change):** `python -B -m unittest discover -s agent-instructions -p "test_agent_type_copies.py"` — exit 1, `Ran 9 tests`, `FAILED (failures=2)`. Both new tests failed at their assertion: `(1, ...) != (2, ...)`, with the base's exit 1 and the "must open with `---`" message. Output saved at `.runs/executor-11/red-run.txt`.
   - The "name in another form" case was not red on the base: it pins behaviour the base already has, so it passes both before and after the change.
2. **Green after the change (focused unit tests):** the same command — exit 0, `Ran 9 tests`, `OK`. Output at `.runs/executor-11/green-run.txt`.
3. **Generator check (slice's Checks):** `python -B agent-instructions/agent_type_copies.py` — exit 0, prints `agent type copies are current`. The tracked copies were not touched; `git status` shows only the two changed files before the commit.
4. **Probe of the reader (ad hoc, not committed):** `python -B -c` calling `missing_field` on: empty text → None; body-only with both fields → None; name only → `description`; `Name:` plus description → None; `title:` in place of name → `name`; text without `---` → None. Output ASCII, exit 0.
5. **Whole gate (WAY-160):** not run, as the handoff requires.

## Own-work check (section 3 of make-change)

- Requirement: the generator ends with exit code 2 and names the file and missing field, and writes nothing; other errors stay at exit 1; a line in another form is not claimed missing.
- Check: the two new tests (exit 2 with exact message, file tree unchanged), plus the "name in another form" case (exit 1 with the existing message) and the existing 7 tests (including "no frontmatter" and "description before name", both still exit 1).
- Result: all pass after the change; the two new ones fail on the base for the stated reason.
- Mutation thought-check: if `missing_field` ignored case, the "name in another form" case would fail; if exit 2 were mapped to 1, both new tests fail; if the generator wrote before raising, the unchanged-file assertion fails.

## Choices made

- **Missing means no line at all in the frontmatter.** A line keyed `name` or `description` in any form (case, leading spaces) counts as present and stays exit 1, as WAY-344 asks. Rejected: exact column-0 `name:` match, which would call `Name:` missing; cost if wrong: an author with a capitalised key gets exit 2 when the fix is a case change. Chosen reading is the narrower one for the exit-2 claim.
- **A file that does not open with `---` keeps exit 1.** It has no frontmatter to be missing a field from, and the existing test "no frontmatter" pins exit 1. Rejected: exit 2 for every file without a `name:` line; cost if wrong: a file of arbitrary text gets exit 2 instead of 1, same stop either way.
- **A `title:` line counts as no `name:` line,** so a definition that uses another key for the name gets exit 2 naming `name:`. Read as WAY-344 says: "a line under another name is not claimed missing unless the definition has no such line at all" — here it has no `name:` line at all, so it is claimed missing. Cost if wrong: the message would name the field right but the author might rename the key rather than add `name:`; both fail the generator either way.
- **Order of checks:** name and description are reported in that order, first missing one wins. If both are missing, the message names `name:`. Cost if wrong: none; the author fixes one field, the next run names the other.
- **Message wording:** `Error: <path>: the frontmatter has no line `<field>:``, prefixed `Error:` as the other messages are. Rejected: a longer sentence explaining the form; the message already names file and field, which is the requirement.
- No `decision:` line and no invariant test was changed in this slice.

## Foundation entries and code reached beyond the slice's Read

- Read whole, as the slice names: `foundations/decisions.md` WAY-344 (2741–2901 in the base), WAY-38 (2545–2570), `foundations/invariants.md` script-language, script-imports, script-subprocesses (116–145), `task.md` lines 29 and 51–58 (within my `sed 25,60` read).
- Reach beyond the slice's Read: `agent-instructions/skill_entry_points.py` — read only the `GeneratorError` class (line 46) to confirm it is a plain `Exception` subclass; no change to it. Reason: `MissingFieldError` subclasses it.
- Reach beyond: a grep of `README.md` for "Exit code" to check whether the README states the generator's exit codes; it does not (the one hit is for another script's exit code). No README change.
- Not read: `plan.md` (the slice was copied in the handoff, and the handoff says the other parts of the plan are read only where a slice's Read names them).

## Unread material

- `.runs/task-cycles/scripts-after-foundation-review/plan.md` — not read; not named by slice 11's Read.
- `.runs/task-cycles/scripts-after-foundation-review/spec.md` — not read; not named by slice 11's Read.
- Otherwise none: every file and passage the Read names was read.

## Searches not found or unclear

- None found wanting. The search for other users of the generator (`agent_type_copies`) found only `AGENTS.md`, `README.md` and the test file; the generator's exit codes are described only in its own docstring.

## Working copies

- No worktree or clone was made. `.runs/executor-11` holds two run logs (`red-run.txt` and `green-run.txt`), which are this slice's evidence, not copies to remove. The directory is kept.

## Concerns and notes

- The committed author e-mail is the private address, as `git.md` says for this repository's remote; nothing else to flag.
- The "name in another form" test pins existing behaviour; it is not red on the base by design.
