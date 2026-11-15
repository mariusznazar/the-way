# Report — the fix of the review's findings — decisions-log-after-foundation-review

**Status:** `done` — the blocking finding I-1 and the Minor findings M-1 … M-6 are fixed; none is contested.

## New commits (on `dfe14f7`, not pushed; the six earlier commits untouched)

- `03455ed` Give WAY-330 its rejected way and settle the wording of WAY-229 and WAY-44 and the archived copy of the cache-lifetime fact — I-1, M-2, M-4, M-5, M-6.
- `cecc49e` Reflow the lines the change left long or short in WAY-10, WAY-44, WAY-140, WAY-241, WAY-287, WAY-339 and the task-cycle skill — M-1, M-3 (wrapping only).

## Each finding

- **I-1 (blocking), WAY-330 carries no rejected way for row 10.** Fixed: the *Rejected* of WAY-330 now ends "…instead of every night; the price left in its conditional form, true for every new user — a reader takes the audit for a tool that has nothing to count today." (the way row 10's source keeps, in the words of the source; no way derived by me). The paragraph was refilled to width. Check: `git diff --word-diff -U0 foundations/decisions.md` over the commit shows `night.` → `night; the price left … today.` as the only change there.
- **M-1, WAY-339 still held the line "WAY-350 and the".** Fixed: the whole *Rejected* paragraph of WAY-339 is refilled, so the line is gone (`grep -n "^WAY-350 and the$" foundations/decisions.md` → no hit). Words unchanged.
- **M-2, `claude-code-prompt-cache-ttls` gives no archived copy.** The reviewer is right, and my report's Choices 6 was wrong. I fetched the capture `…/web/20261114163725id_/https://code.claude.com/docs/en/prompt-caching` (the HTML page the fact's address names): it holds "charges a higher rate for cache writes" and no "bills cache writes". (The `.md` address of the page, which I had looked at, holds the other wording; the fact's address has no `.md`.) Fixed: the *Source* now gives `(archived: https://web.archive.org/web/20261114163725/https://code.claude.com/docs/en/prompt-caching, 2026-11-14)`, as the two sibling facts do.
- **M-3, over-long and short lines made by the change.** Fixed by refilling, to width 100 as the neighbouring lines, the paragraphs of the six places: WAY-44 binding paragraph (also the 122-character line), WAY-140 binding paragraph (105), WAY-10 *Rationale* (154), WAY-241 *Rationale* (132), WAY-287 *Rejected* from "a decision adds in a group it names" to the end of the paragraph (the 59-character line), and `task-cycle/skill/SKILL.md` lines 452–456 (the 102-character line). Check: `git diff --word-diff=porcelain` of the commit, filtered to added or removed words → no output, so no word changed; a script over the added lines of the fix: 0 lines over 100 characters, no code span of backticks broken across lines.
- **M-4, "the version after the change" in WAY-229's *Rationale*.** Fixed: "the audit of the process shows what it costs (WAY-337, WAY-339)". On the reviewer's reading, the fact rests on WAY-337 (cost of a cycle) and WAY-339 (audit comparing versions); I agree, and my report's last bullet of **Searches** ("I found no decision that holds it") was incomplete.
- **M-5, "the strongest model" in WAY-229's *Rejected*.** Fixed with the reviewer's words: "never above a model the human names" and "a line that keeps a model out of the cycle's work has to be drawn somewhere all the same". Check: `grep -i strongest` over the entry shows only "strongest class available", "strongest available", the Rationale's sentence on what is available, "strongest price" (a price, not a class), and "the strongest class of the family the cycle runs on" (the rejected way itself).
- **M-6, WAY-44 "the map goes on with no effect".** Fixed: "the gap has no effect on the map or its check, but a reader of this decision who reads it strictly sees a map that goes against it."

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` → exit 0, `0 errors` (after each commit).
- `python -B gate/run_tests.py task-cycle` → 0 (514 tests); `python -B gate/run_tests.py elements/common` → 0 (242 tests). The other changed files lie in `foundations/` (no tests).
- Not run: the full gate (the orchestrator's run).

## The own-work check

Requirement most likely unmet by the fix: "a finding that asks only for a rewrap changes no word" (the handoff). Check: `git diff --word-diff=porcelain HEAD~1 HEAD` of the rewrap commit, filtered to added or removed words → empty; and the six touched places listed above were checked against the finding's line numbers by `sed -n` on each before and after. Whole range `dfe14f7..HEAD`: 19 changed word lines, all in the intended edits of the first commit.

## Unread material

none beyond the report of the first change: I read the findings file and the handoff whole, `task-cycle/change/fix.md`, and each place the findings name. I did not open `reports/review-whole-report.md` (the findings file carries the reviewer's words).

## Searches not found or unclear

- none; the claim of M-2 was found true and the earlier note of mine false (above).

## Reaches beyond this handoff

- The web capture of the prompt-caching page, both the HTML and the `.md` address (to test M-2); nothing else.

## Working copies

`.runs/fix/` (edit scripts and two downloaded captures): removed before this return. No worktree or clone was made.
