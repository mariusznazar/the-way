# Author report — the fix of the review's findings

**Status:** done. **Commit:** `1a17406a` (range `c8eef488..1a17406a`; 4 files, 22 added, 16 removed). The findings file was read whole, with `task-cycle/change/fix.md`; I held no finding wrong.

## The findings and how the fix meets each

**I1 (Important, Contradiction: yes) — two restatements of WAY-410 dropped its second case.** Fixed.
- `task-cycle/skill/SKILL.md`, head of the skill: the early stop now reads "an agent's question about a test that contradicts the requirement, or that it cannot pass by code that meets the requirement for every input, is settled by no source (WAY-410)", and the next sentence takes the exception: a failed test is work to resolve "save the question about a test that no source settles".
- `task-cycle/skill/request_template.md`, the new row: its first line is now "a test contradicts the requirement, or no general code passes it, and neither the task, the spec, the decisions nor the invariants settle which holds" (it names all four sources, not "the task"); the ways open carry both cases ("for a contradiction, the requirement stands and the test changes, or the test stands and the requirement changes; for a test that no general code passes, the requirement is read another way, or the test changes"); the pointer now reads `SKILL.md`, "A question about a test is answered otherwise".
- Another narrow restatement I found by searching the five files: `task-cycle/change/SKILL.md` section 1 ("the expected value of a test that the requirement contradicts is the case of section 2") now adds "or a test you cannot pass by general code". Also in step 9 sub-step 4 the reason for no retry said "does not remove the contradiction", true of the first case only; it now reads "does not settle what the requirement is" and names both cases.
- Other restatements searched and found whole: the orchestrator's paragraph and the author's section 2 bullet and section 5 sentence (both cases, four sources), kind 2 of the template, `correction.md` and `review/fix.md` (they name no case: "a question about a test", and the code that passes a test).

**M1 — stages "not run" assumed a first question.** Fixed in the orchestrator's paragraph: "The stages that have not run on this code — of the review of the whole change, the return step and the reconciliation with the target branch — are named in the request as not run", and one sentence for a correction: the open request returns to a draft marked `blocked` and its description is rewritten as the template's variant gives.

**M2 — the zero count attributed to a register the task does not name.** Fixed in WAY-409 *Rejected*: "no case is known in the 83 task cycles of the process's author (his own record, not open to a reader of this repository)". The register and its date are gone.

**M3 — pointers named the paragraph before the rule.** Fixed in all three places: step 9 sub-step 4, the list of the record's copies, and the template row now name "the paragraph on a question about a test" / the opening words of that paragraph.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` — exit 0 (534 tests, 2 skipped; tail in `reports/author-fix-task-cycle-gate-tail.txt`).
- `python -B reports/author-own-work-check.py .` (the first check, from the earlier report) — exit 0, 18 of 18 ok on the fixed tree.
- Not run: the full gate (not mine).

## Own-work check (WAY-164)

- Requirement most likely not met by the fix: that every restatement of WAY-410 carries both cases and the four sources (the very thing I1 shows my first check could not see).
- Check: `reports/author-fix-restatement-check.py ROOT`. It reads the five files of the change, takes each paragraph, table row and table cell as a unit, and fails on a unit that describes the first case (a test the requirement contradicts) without the second ("general code" or "for every input"), a unit that lists the answering sources and not all four, and a unit that names "ways open" for a test without the second case.
- What it showed: on the reviewed head `c8eef488` (files taken with `git show`) it exits 1 with four failures: the head of the skill (one case), the template's first line (one case), the template's ways open, and the `change/SKILL.md` sentence of section 1 that I found myself; on the fixed tree it exits 0 with none. A first version of my script did not split the table row into cells and missed the template's first line; I saw it by running the script on the reviewed head and fixed the script before relying on it. Its limits: it reads wording by pattern, so a restatement in other words would pass it, and it covers the five files named, not the foundation entries (those I read: WAY-410 and WAY-409 carry both cases and the four sources).

## Reaches beyond the handoff

None beyond reading `foundations/decisions.md` around WAY-409 and WAY-410 and the files above, which the fix touches.

## Unread material

None; the handoff, the findings file and `change/fix.md` were read whole. I did not open `reports/review-whole-report.md` (the handoff allows it; the findings were enough).

## Searches not found or unclear

- None. (The reviewer's suggested wordings were taken as suggestions; I used my own where WAY-410 and the task's *Questions to settle* 3 supported a closer text, as the handoff allows.)

## Working copies

`.runs/author-fix/` of the worktree stood with the reviewed-head copies of five files (`head/`), the script, and the outputs of the checks; removed. Kept in `reports/`: `author-fix-restatement-check.py` and `author-fix-task-cycle-gate-tail.txt`. No worktree or clone was made.
