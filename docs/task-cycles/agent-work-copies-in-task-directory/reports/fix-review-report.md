PASS a300ee62676e5812141c86852357d32e54e3b068

# Review of the fix of the whole-change review's findings (task `agent-work-copies-in-task-directory`)

Range `5f01235516299634098e655e21ff28f845e82ae8..a300ee6` (one commit; `git rev-parse HEAD` in the worktree printed `a300ee62676e5812141c86852357d32e54e3b068`). The reviewed worktree, its index and its branch were not changed (`git status --short` empty before and after). Bounded by `reports/fix-findings.md` (I-1, M-1, M-2, M-3), the fix report and the diff.

## Findings of the findings file

- **I-1 (Important): fixed.** The first paragraph of "Working copies" (`task-cycle/skill/SKILL.md:288-296`) no longer says "a file that a tool writes by itself": it now names only "the screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory" (moved into the agent's directory, original removed) and adds "The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule". WAY-373 (`foundations/decisions.md:12846-12852`) carries the same clause, so the paragraph the handoffs copy and the decision agree, and the task's *Out of scope* bullet 2 and binding answer 5 are respected. `grep -rn "writes by itself outside" task-cycle foundations/decisions.md` finds nothing (exit 1). The clause sits beside "a prepared input of a test" being a working copy; the two read consistently (what the agent prepares is a copy, what the product's own tools make are not).
- **M-1 (Minor): fixed, by the second way the finding offered.** Kind 18 is deleted from `task-cycle/skill/request_template.md` (no `kind 18` anywhere in `task-cycle` or the decision log), so the section for the human's decisions again holds only what waits for a yes and WAY-286 and WAY-287 stay untouched and correct. The leftover copy is shown in one plain sentence under **Cost** (`request_template.md:420-423`: a copy stayed in the task's ignored working directory, nothing waits for it, it is removed by hand or goes with the task's directory) and with its agent and path under **Checks** (`request_template.md:454`, unchanged); the second paragraph of "Working copies" (`task-cycle/skill/SKILL.md:303-306`) and the record item *Working copies left* (`task-cycle/record_template.md:199`) point to the same places. The task asks that the human see the remainder in the description, and the Cost sentence does that in the top part. Note (not a finding): a sentence about a leftover copy is an unusual occupant of **Cost**, whose definition is time, models, tokens and rounds; it fits only as "what the cycle costs the human to clean", and `request_check.py` and its tests accept it (task-cycle tests below).
- **M-2 (Minor): fixed.** `task-cycle/skill/SKILL.md:245-247` now reads "In every report read its checks, reaches, unread material, searches and working copies", and the second paragraph of "Working copies" says the report of every agent holds the line on its working copies and the orchestrator reads it when the agent returns, as it reads **Unread material**. Step 14 still confirms the record lists each remainder.
- **M-3 (Minor): fixed for the changed paragraphs.** The rewrapped paragraphs (step 2, the boundary paragraph, step 4's base paragraph, the handoff paragraph, the paragraph on what is read in every report, step 14, the section "Working copies", the bullets of `review/SKILL.md` and `plan/SKILL.md`, WAY-373's *Rationale*) now wrap at about 100 characters. I compared the reflowed passages in the diff word by word with the text before: no word changed except the intended edits above. Remaining added lines over 100 characters: the heading of WAY-373 (116) and two lines of 101 characters (counted with the diff's `+`), which is the convention of the file. `git diff 5f01235..a300ee6 --check` exit 0.

## New findings in the fix diff

none (no Critical, no Important). One Minor note outside the fix's bounds: `task-cycle/plan/SKILL.md:180-183` leaves a short last line ("moves. The move is a choice of how to make the") before an unreflowed line, as the reflow stopped one line early; polish only, blocks nothing, lies within the task.

Counts: 0 blocking, 1 Minor (the note above), 0 out of scope.

## Declined to judge

- Whether a reader of the human's decisions section would rather see the leftover copy there (M-1's other way): a judgment of the human; the task allows either and the foundation's closed list favours the lower place.

## Checks I ran

All in a worktree of `a300ee6` in `.runs/review-whole/head/` (removed, below), except the greps and the diff checks on the reviewed worktree.

| Check | Command | Exit |
|---|---|---|
| foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| task-cycle tests | `python -B gate/run_tests.py task-cycle` | 0 (394 tests OK) |
| stale pointer | `grep -rn "kind 18\|writes by itself outside" task-cycle foundations/decisions.md` | 1 (no match, as wanted) |
| whitespace | `git diff 5f01235..a300ee6 --check` | 0 |
| long added lines | `git diff 671f470..a300ee6 -U0 \| grep '^+' \| awk 'length($0)>101'` | lists the WAY-373 heading and two 101-character lines |

Not run: `instruction-files`, `agent-instructions` and `elements/common` tests (the fix changes no file those read in a way the first review's runs did not cover; the author reports them at exit 0), the whole gate (the orchestrator's run).

## Reaches beyond the dispatch

none (I read the findings file, the fix report, `task-cycle/review/fix.md`, the fix diff, and grepped `task-cycle` and `foundations/decisions.md` for stale pointers).

## Working copies

One: a worktree of `a300ee6` at `.runs/review-whole/head/`, with the output files `fc.txt` and `tc.txt` beside it in `.runs/review-whole/`. Removed with `git worktree remove --force` (exit 0), `git worktree prune`, `rm -rf .runs/review-whole`; `ls .runs` shows only `task-cycles/` and `git worktree list` no longer lists it. Kept in `reports/`: nothing but this report. Remainders: none. Nothing written to the system's temporary directory or the session's scratch directory.

## Unread material

Read whole: the fix handoff, the findings file, the fix report, `task-cycle/review/fix.md`, the fix diff of all five files. Not read: the whole of `task-cycle/skill/SKILL.md` and of `request_template.md` (I read the diff and the surrounding passages of "Working copies", the report paragraph and the **Cost** passage), and `reports/fix-handoff.md` (the orchestrator's guidance to the author; not needed to judge the fix against the findings). No decision was read afresh in this round; the counts of the earlier review stand (31 read whole, 106 by title).

## Searches not found or unclear

none
