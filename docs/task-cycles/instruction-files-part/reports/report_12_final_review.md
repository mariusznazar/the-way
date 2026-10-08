# Report 12 — final whole-branch review (opus; returned as text, saved by the orchestrator)

Range 252152a..c60f3ea, 21 commits. Assessment: **With fixes.** No Critical.

Partial checks in the reviewer's scratch clone (none a pass of the full gate): `instruction-files` 95 OK (5 skipped), `agent-instructions` 18 OK, `gate` 98 OK; entry points current; 397 references, 0 stale; guards 0 errors (decisions 13 warnings: 8 placeholders, 5 overdue before the branch); script on the-way: the four expected lines.

## Strengths

The invariant checks are independent of the code (no import from `instruction-files/`, own `git ls-files`, literals; one commit d87d74f; author wrote neither sentences nor code). The trust boundary: own-stack walk never following a link; Windows link chains by `readlink` with a hop limit; every token through `is_network`; tests wrap 12 file-system calls; every spec §4.6 row pinned by a named test. The foundation describes the code (WAY-09 contents, part entry, WAY-128–133 in `SKILL.md` and `principles.md`, every named fact exists). Acceptance criterion met (only the `SKIP_DIRS` literal `.runs`). `tool_loading.md` says "not established" where no source exists, and describes every measurement.

## Issues

- **Important 1** — the skill can judge a product under a copy other than its pinned commit (`SKILL.md:16-30`, WAY-127 narrowed, WAY-34): (a) check 2 reads `.the-way/instruction-files/SKILL.md` as checked out, so a submodule HEAD differing from the pin is followed; an unfetched pinned commit gets "move the pin" advice; (b) check 1 "goes on" whenever this copy lies in some product's `.the-way`, even when the repository under review is another product (a gap of spec §4.2). Fix: check 1 goes on only when its superproject is the repository under review or the review is `--file` only; check 2 compares `.the-way` HEAD with the pinned hash before `cat-file -e`.
- **Important 2** — near-miss phrases lower really dead paths to INFO (`check_instructions.py:55-63`): confirmed by run — "is not ready", "is not readable", "does not readily", "Nie czytaj … `docs/zasady/styl.md`" → INFO; control WARN. Fix: trailing `\b` except "nie jest wczytywan"; tests.
- **Important 3** — off Windows the script assumes no network (`:64, 126-129, 144-145, 177-178, 412-416`, docstring :21): Cygwin/MSYS2 Python (`os.name == "posix"`) treats `//host/share` as UNC; macOS automounter maps `/net/<host>/…`. By reading only. Fix: guard (Cygwin/MSYS like Windows; leading `//` on POSIX; `/net/`, `/Network/` on darwin) or document as a limit.
- Minor 4 — `tool_loading.md:27-28` "Not read: … `.agents/`" vs ":57 not established"; the script's WARN "Claude Code does not read .agents/skills" asserts the withdrawn claim (spec §4.5 B).
- Minor 5 — two Codex check commands (`principles.md:213` vs `tool_loading.md:112`).
- Minor 6 — `principles.md:132` "always read it" (untrusted Codex projects; Cursor workspace trust).
- Minor 7 — WAY-132 *Rejected* "the notice an interactive session gives" has no fact or `tool_loading.md` line in the branch.
- Minor 8 — the script follows only backticked pointed files; the term and the invariant count a path named anywhere; undocumented.
- Minor 9 — task point 5 met for one level above (plain, linked, inside or outside git), unmet for the real two-level linked case.

## Deliberate breaks (WAY-69, WAY-08) — scratch clone, each run once, reverted

Prerequisite: `git log --oneline -- agent-instructions/test_instruction_files.py` → one commit, d87d74f. IFI = `instruction-file-imports/1`, RCI = `root-claude-md-import/1`.

| Break | Exit | IFI | RCI |
|---|---|---|---|
| control | 0 | pass | pass |
| `See @docs/x.md…` appended to `AGENTS.md` | 1 | fail | pass |
| same appended to `agent-instructions/README.md` | 1 | fail | pass |
| `# Claude` above `@AGENTS.md` in `CLAUDE.md` | 1 | fail | fail |
| tracked `pkg/AGENTS.md` holding `(@./x.md)` | 1 | fail | pass |
| same, untracked (control) | 0 | pass | pass |
| root `CLAUDE.md` names tracked `docs/brk.md` holding `"@docs/x.md` | 1 | fail | pass |
| root `AGENTS.md` names `docs\brk.markdown`, tracked, holding `„@x/y` | 1 | fail | pass |
| root `AGENTS.md` names `xdocs/brk.md` (letter before; control) | 0 | pass | pass |
| tracked `sub/CLAUDE.md` = `@AGENTS.md` | 1 | fail | pass |
| unclosed code span `` ` @docs/x.md `` | 1 | fail | pass |
| closed code span (control) | 0 | pass | pass |
| `@docs/after.md` after a closed fence | 1 | fail | pass |
| fence only (control) | 0 | pass | pass |
| `CLAUDE.md` = `@AGENTS.md\r\n` (control) | 0 | pass | pass |
| UTF-8 BOM before `@AGENTS.md` | 1 | pass | fail |
| `@AGENTS.md ` (trailing space) | 1 | fail | fail |
| root `CLAUDE.md` removed from git | 1 | fail | fail (the checks' positive control; the sentence holds vacuously — a reading) |

No break that should fail its check passed.

## Deferred minors triage

Fix before the request: Task 4 (1) phrase boundary; Task 6 (2) pinned hash and "move the pin" advice; Task 8 (3) `.agents/` line, with the section citation in the same pass. May stay: the remaining Task 3, 4, 5, 6, 7, 8 minors (reasons in the review: cosmetic, safe-side false negatives, test-only, already fixed, not reproduced — Git Bash passed `':/.the-way'` and `<hash>:path` unchanged).

## Declined to judge

Watches (network; the orchestrator's run); live re-read of documentation; the measurements themselves (WAY-131: one session per variant for loading); the POSIX branch beyond reading; level-2 verifications of WAY-09, WAY-127–133 (independent assessment); the second WAY-33 search (orchestrator); Polish wording and spec fidelity to the task; speed on very large trees.
