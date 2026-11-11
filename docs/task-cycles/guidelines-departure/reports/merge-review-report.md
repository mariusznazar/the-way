PASS 66cc61d89e06b8d9d4cf12198415993587222aaa

# Review of the reconciliation with the target branch (merge 66cc61d)

Reviewed: merge `66cc61d` in the worktree `the root of the task worktree`
(`git rev-parse HEAD` printed `66cc61d89e06b8d9d4cf12198415993587222aaa`, the head given). Method:
`task-cycle/review/SKILL.md`, read whole; the variant files `whole_change.md` and `fix.md` do not apply to
this review and were not read.

One mismatch in the handoff, no effect on the verdict: it names the first parent as `b4bfca8`; the first
parent is `dae4cf9` (the cycle's record commits `54c820e` and `dae4cf9` on top of `b4bfca8`).
`git diff b4bfca8 dae4cf9` is empty, so the two trees are the same and the reviewed change is unchanged.

## What the merge holds

`git diff 024f486 66cc61d` (the merge against the other side) is one file, `foundations/decisions.md`,
49 added lines, none removed: the entry WAY-328, placed after WAY-327 and before *Withdrawn identifiers*.
`git diff b4bfca8 66cc61d` equals the other side's changes `b4bfca8..024f486` (14 files), so the merge
added nothing of its own beyond the placement and the new number. `git diff e3825a8 b4bfca8 -- . ':!.runs'`
is the same one file with the same 49 lines, so the entry is the one the two earlier reviews passed, with
only its number changed (the old number is not repeated anywhere in the entry's text).

## Findings

### Critical

none

### Important

none

### Minor

none

### Out of scope

none

## Answers to the handoff's questions

1. Does the renumbered entry conform to the template as the merge changed it? Yes. Read against
   `elements/decisions/template.md` as merged: heading `### WAY-328 — <question>`; one paragraph of
   binding sentences (four sentences in one paragraph; the first paragraph under the heading counts and
   the entry was passed on this point in the earlier reviews, no change); *Scope* names parts of the
   map; *Based on* `none` is allowed by the new form (`<…> | TODO — <…> | none`) and the entry names no
   source outside the product; *Relations* `derives from WAY-217 · derives from WAY-173`, both
   decisions exist (lines 6475 and 5242) and neither was touched by the merged side; *Verification*
   holds only the pair of examples, which the template allows with no invariants; *Origin* `none`,
   which the new rule on *Origin* (a task document is never named there) requires when the reasoning is
   in the entry; *Rationale* and *Rejected* are present and name no file, script or count of the
   foundation. The foundation check passes (below).
2. Does any entry, relation or text point at the entry under its old number? No. `git grep -n WAY-327`
   outside the log finds only `task-cycle/skill/request_template.md:14` and `:320`, both about the
   four parts of an item in which the human chooses, which is the meaning of WAY-327 (log line 10720,
   "What does an item of a request's section for the human's decisions carry where the human chooses?").
   Inside the log WAY-327 is only its own heading. `git grep WAY-328` finds only the heading of the
   entry. Nothing in the other 14 files of the merged side or in the cycle's earlier files uses the
   departure's old number.
3. Do the identifiers run on without a gap or a duplicate? Yes. A script over `foundations/decisions.md`
   found 286 entries and 42 withdrawn identifiers, no duplicate, no number both an entry and withdrawn,
   no gap from 1 to 328, and the entries in ascending order ending 326, 327, 328. (The template's rule
   "no entry and no withdrawn number holds the next free number" holds: 329 is free.)
4. Does anything in the merged side contradict the entry? No. The merged side's edits touch WAY-287,
   WAY-289, WAY-290, WAY-317 and add WAY-327 (the groups of the request's section for the human's
   decisions), the *Based on* `TODO` form and the *Origin* rule (template, `rules.md`,
   `foundation_check.py`), the invariants template's `TODO` form, and the task-cycle skill, correction,
   blocked-finding, request template and their scripts. A search of the merged side's diff of the log
   (`git diff e3825a8 024f486 -- foundations/decisions.md`) for "guidelines", "depart", WAY-217,
   WAY-215, WAY-173 and "part map" found no line. WAY-215, WAY-217, WAY-173 and the part map
   (`git diff e3825a8 024f486 -- foundations/part_map.md` is empty) are unchanged by the merge, so the
   entry's anchors stand. The entry's own *Origin* `none` and *Based on* `none` agree with the new rules.
   *Scope* lists exactly the 16 parts of the map's part sections (decisions to product-guidelines, in the
   map's order); the five command surfaces after them have no files and are not parts of the departure.

## Declined to judge

- The five command surfaces of the map (`test-runner-command` and the four after it) are not in *Scope*;
  the frozen task names 16 parts and the checker accepts the entry. Whether a surface is a part for this
  purpose is outside the task.
- The merged side's own changes (the request template, the scripts and their tests) were not reviewed
  for their own correctness; they passed review in their own cycles. Only their bearing on the entry
  was checked.

## Checks run

| Command (from the worktree's root) | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `66cc61d89e06b8d9d4cf12198415993587222aaa` |
| `git diff --stat b4bfca8 dae4cf9` | 0 | empty (same tree) |
| `git diff 024f486 66cc61d` | 0 | only the 49 added lines of WAY-328 |
| `git diff --check 024f486 66cc61d` | 0 | no whitespace error |
| `git grep -n -E '^(<<<<<<<\|>>>>>>>\|=======)' -- foundations` | 1 (no match) | no conflict marker left |
| `git grep -n WAY-327` / `git grep -n WAY-328` | 0 | as in answer 2 |
| `python -B -I <scratchpad>\ids.py` (numbering script) | 0 | as in answer 3 |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B -m unittest elements/common/test_foundation_check.py` | 0 | 125 tests OK |
| `python -B -m unittest task-cycle/test_request_check.py` | 0 | OK |
| `python -B -m unittest task-cycle/test_remarks_check.py` | 0 | OK |

The numbering script is `a scratch script of the session's scratchpad, outside the repository`.
The gate (`gate/run_tests.py`) was not run, as the handoff says. The three focused test files were run
because the merged side changed the check and the request scripts that read the log; they are not the
full suite. No file of the repository was modified (`git status --short` empty before and after).

## Reaches beyond the dispatch

- `elements/decisions/template.md`, `elements/common/rules.md`, `elements/invariants/template.md`
  (read whole or in the changed passages): to judge conformance with the template as merged.
- `foundations/part_map.md` (headings and the sections of the 16 parts and the surfaces): to confirm
  that *Scope* names every part and that the merge did not change the map.
- `foundations/decisions.md` lines 5242, 6376, 6475, 10720 and the tail from 10756: WAY-173, WAY-215,
  WAY-217 (the anchors), WAY-327 (the neighbour) and the withdrawn list, for the relations and the
  numbering.
- `task-cycle/skill/request_template.md` lines 10-16 and 316-324: the two remaining mentions of WAY-327.
- `git diff b4bfca8 024f486` for the template, rules, skill, correction and blocked-finding files: for
  contradiction with the entry.
- the author's private rules for scripts and for searching (the author's rules for scripts
  and searches), read before the numbering script and the searches.

## Unread material

- Of the dispatch: the handoff and the frozen task `.runs/task-cycles/guidelines-departure/task.md`
  were read whole. The two earlier reports (`review-whole-report.md`, `review-fix-report.md`) were not
  read; their verdicts were taken from the handoff and the entry was compared with the task and the
  template myself.
- Of the merged side: `request_template.md`, `request_check.py`, `remarks_check.py`,
  `foundation_check.py` and their tests were not read whole; I read their diff stats, the two
  mentions of WAY-327 in the template, and ran their tests. The diffs of `SKILL.md`, `correction.md`,
  `blocked_finding.md`, the three element files and the rule files were read whole. The diff of the log
  against the departure (`e3825a8..024f486`) was searched by keyword and by hunk headers, not read line
  by line.
- The log's other 285 entries were not read; WAY-173, WAY-215 and WAY-217 were found by identifier and
  their headings checked, not their whole text (the frozen task quotes WAY-215 and WAY-217).

## Searches not found or unclear

- The handoff names `b4bfca8` as a parent of the merge; the first parent is `dae4cf9` (explained above).
- A search of the merged side's log diff for text about departures from guidelines found nothing; this
  is the expected result and was a search for a contradiction, not for a thing that should exist.
- Otherwise none.
