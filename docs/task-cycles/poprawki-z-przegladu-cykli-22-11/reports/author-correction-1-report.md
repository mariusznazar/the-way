Author report — correction 1 for the human's remarks on the open request (`make-change`, "a correction for the human's remarks").

**Status:** done. One commit (hash below). Remarks 1 and 3 of the human need nothing from the author; remark 2 has three changes, all made.

## What I changed

1. **The executor's sentence** — `task-cycle/change/slice.md`, "Read", a new bullet: "The dispatch lists the tests the plan leaves failing at your slice's base, with their owners: report a listed test that fails as expected, not as a failing check of your slice, and do not make it pass outside your slice's *Change*." It names the dispatch as the source of the list (the executor does not open the plan) and stays within WAY-136 (a failure so named is no failing check) and WAY-229 (the retry is for a failing check of its slice); the planner's and the orchestrator's sentences are not copied.
   **Choice of place:** `slice.md`, not `SKILL.md` §3. Only the executor of a slice reads `slice.md`, and it is the file that says what the dispatch carries for a slice; §3 of `SKILL.md` is read by the one author and by the fix too, who get no such list, so a sentence there would be read by agents it does not concern. Rejected: §3 — it would speak to the wrong readers; cost if wrong: an executor that reads `slice.md` as a variant row finds the sentence all the same, since its handoff names the row.
2. **The idiom in the comment** — `instruction-files/check_instructions.py` line 456 (the comment was at 454 before the edit shifted lines in the docstring): `such as '\'' of a shell`, written with the editing tool; a search of the file for `'\''` finds the comment, and the docstring has `'\\''` as before.
3. **The count of the info cases** — the module docstring of the same file: "Four cases are noted at the level `info`", and the list now holds the four the code gives (`dead_path_note`): a path in a sentence that says it does not load or exist; in a file given with `--file`, a name of one part that does not resolve from the file, the repository or the home directory; in a file of the repository, an absolute path outside the repository and the home directory; and in a file of the repository, a relative path under a name of the root `.gitignore`.

No behaviour of `check_instructions.py` changed (a trust-boundary file): a comment and a docstring only. Evidence: the output of the script on a large real repository (loop2, read only) is byte for byte the same before and after the edit (`cmp` of the two outputs: identical).

Commit: see the line at the end of this report.

## Checks run

| Check | Command | Exit |
|---|---|---|
| foundation check, no switch | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| instruction check on the-way | `python -B instruction-files/check_instructions.py .` | 0 (0 warn) |
| output of the instruction check unchanged by the edit | `python -B instruction-files/check_instructions.py <loop2>` before and after, `cmp` | identical |
| tests of the file I changed | `python -B gate/run_tests.py instruction-files` | 0 |
| skills and guidelines tests bearing on `slice.md` | `python -B gate/run_tests.py agent-instructions` · `... product-guidelines` | 0 · 0 |
| ruff 0.17.1 format and lint of `instruction-files` | `.runs/author-correction-1/venv/Scripts/ruff format --check instruction-files` · `ruff check instruction-files` | 0 · 0 |

The gate with no argument was not run. No new file was created, so no run after a `git add` of a new file was needed.

## Return step (for what the correction touches)

- **Foundation compared with code.** WAY-136 (a slice may leave tests failing; a failure so named is no failing check of the slice that meets it), WAY-229 (the retry is for a failing check of the slice), the bullet of `task-cycle/plan/SKILL.md` (the handoff of each later slice lists the tests; the executor reports a listed failing test as expected), `task-cycle/skill/planning.md` ("A slice's handoff"), step 9 of `task-cycle/skill/SKILL.md` (sub-steps 2–4) and the new bullet of `slice.md`: they say the same thing in the places each agent reads, and none contradicts another. The part-map entries of `task-cycle` and `instruction-files` describe their parts in general terms and still match the files; no file was added, moved or newly depended on. The info cases of the check: the docstring (now four cases), `instruction-files/SKILL.md` ("What the check script settles", the `info` lines of step 1), WAY-418 and the README sentence match the code of `dead_path_note`; the SKILL's list does not name the bare-name case, which is the base's and is covered by "what it left out".
- **Decisions, invariants, environment facts, glossary terms, part-map changes, projected entries, rows of *Settlements to record*:** none written or changed in this correction; nothing found that no longer matches.

## Own-work check

Requirement most likely not met: the sentence of the correction must stay within WAY-136 and WAY-229 and name the dispatch as the source. Check: read the sentence against the two decisions' binding sentences — it says "reported as failing as expected, not as a failing check", as WAY-136 gives, and keeps the retry of WAY-229 for a failing check; and it contains no word of the plan's text for the planner. Second: that the docstring's four cases equal the code's. Check: `dead_path_note` returns `info` in exactly four branches (sentence, bare name outside the repository, absolute elsewhere, ignored name), read from the code.

## Reaches beyond the dispatch

none.

## Unread material

none beyond earlier reports: I read the handoff, the remarks, `slice.md`, the docstring and the comment whole; `task-cycle/change/fix.md` I did not re-read (the variant row gives the remarks as binding).

## Searches not found or unclear

none

## Working copies

`.runs/author-correction-1/` stood with a virtual environment `venv/` (ruff 0.17.1) and the outputs of the instruction check before and after; removed with the directory by its full path before I returned; no remainder, no worktree or clone.
