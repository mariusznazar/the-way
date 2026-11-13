# Report — author of correction 1, `defects-found-after-merge`

**Status:** done

## Commits

- `a3152c9` Give kind 17 of the request template the sentence of a correction that only refreshes the target branch

Files changed: `task-cycle/skill/request_template.md` (+6 −1). Nothing else.

## The remark, as made and how

Remark (item 3 of *Fix or let through*): the template does not say what a refresh-only correction
(`target-branch · none`) writes in the one sentence, so the writer improvises. Decision: fix it here.

Done in kind 17 of `request_template.md`: after the existing sentence of the kind, added

- the sentence a `target-branch · none` correction carries, as an example: "This correction only
  refreshed the branch from the target branch at your request; nothing else changed, and the cycle
  made no judgment of whether the task required anything." — it says the cycle judged nothing, as the
  kind `none` means;
- the case of two sources: the one sentence carries each pair once, with an example
  ("This correction answered your remark about a defect the task required, and it refreshed the
  branch from the target branch at your request, which the cycle judged nothing about."). The kind's
  earlier text did not say this (only `correction.md` says "pairs ... in one sentence").

Plain words, no file names, no identifiers of entries in the example sentences. The wording of the
kind's earlier sentence is unchanged.

## Agreement with decisions

- WAY-287 (the description shows the pairs in one sentence in *You accept by merging*; after a
  correction the section does not read `none`): agrees; the new sentence is that sentence.
- WAY-356 (`target-branch` takes `none`; each pair once; the description shows the pairs in one
  sentence): agrees. WAY-355, WAY-286 (top part in plain words), WAY-289, WAY-306, WAY-337: no
  collision (306 and 337 do not touch this kind; 289 concerns the answers to items 8, 4, 9, 14).
- No decision changed.

## Own-work check (WAY-164)

Requirement most likely not met: the example sentences must obey the top part's rule (no file names,
no identifiers of entries) and agree with the pair meanings.
- `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` — exit 0
  ("checked: 1 files, 0 listed").
- Read the two example sentences against the rule by hand: no file name, no WAY-number, no pair
  notation in them; the pair notation `target-branch · none` stands only in the instruction around
  them, which is read by the writer, not placed in the description.

## Checks run

- `python -B gate/run_tests.py task-cycle` — exit 0 (367 tests, OK; includes
  `task-cycle/test_request_check.py`, the only test file that names `request_template`).
- `python -B elements/common/foundation_check.py --skip-test-citations .` — exit 0 (0 errors). Run
  although `foundations/` is untouched, for the foundation check.
- Not run: the full gate (the orchestrator runs it, as handed off); no review; no return step.

## Test

No test added. The sentence is prose for the agent writing a description; `request_check.py` judges
no content (the template says so), and a test of the wording would only check a deliberate wording.
The new text does not need a test to stay true.

## Foundation step (WAY-33)

Searched `foundations/*.md` once for `refresh`, `target-branch`, `cause of a correction` and
`judged nothing`/`made no judgment`. Entries the new sentence touches: WAY-287 (the pairs in one
sentence; its *complies* case names only the remark case), WAY-355, WAY-356 (the `target-branch ·
none` pair; its *complies* case already names it). All agree with the new text; none needs a change,
so none was written. The other `refresh` hits (WAY-251 and the guideline decisions) are about
guidelines, not about corrections.

## Reaches beyond the handoff

None beyond the decisions and files named. I read `task-cycle/change/SKILL.md` and
`agent-instructions/README.md` as the handoff gave. Additionally ran `grep` over the repository
for `target-branch` / `cause of a correction` / `kind 17` to find readers of the text: only
`process-audit/test_audit_count.py:370` (a fixture line) and `task-cycle/record_template.md`,
`task-cycle/skill/correction.md` (descriptions of the line in the record, which agree).

## Questions

none

## Concerns

- `task-cycle/skill/correction.md` step on rewriting `request.md` says only "the pairs of the
  correction in one sentence as the item of kind 17"; it needs no change, since kind 17 now holds
  the example. Left alone as the handoff says to make no other change.

## Choices

- Put the sentence in the kind 17 text itself, with "such as" examples, not as a separate block:
  the kind's other sentences are inline. Rejected: a fixed required wording — the form check cannot
  read it and the writer needs to adapt it for two-source cases; cost if wrong: a writer takes the
  example too literally, which is harmless.

## Unread material

none (all decisions WAY-287, 356, 355, 286, 289, 306, 337 read whole; request_template.md,
correction.md read whole; `record_template.md` read the item *Corrections after the request opened*
and its paragraph; the frozen task not read, not needed).

## Searches not found or unclear

none
