PASS ddbdaf21bea70a6dcf6d7394c326e530c49f3863

# Review of correction 1 — decisions-list-in-refinement

Range `f50e58f..ddbdaf2` (one commit; `git rev-parse HEAD` = `ddbdaf2`). Read: `task-cycle/review/fix.md` (correction part), `reports/correction-1-remarks.md`, `reports/correction-1-report.md`, the diff computed by me (2 files, +13 / -12). The code is as I reviewed at `b084a4a` plus this commit.

Counts: remark 1 made; blocking 0; new Minor 0; out of scope 0.

## The remark

**Remark 1 (the only one that is the correction's work) — made.** The widened check named only a guess "settled in the repository". Now:

- `project-level/task/skill/final_review.md:29-30`, step 3: "each guess the critique keeps from the human by judging it already settled in the repository or in the task document or most likely right, open the file the critique quotes from and check the quotation word for word".
- `foundations/decisions.md`, WAY-378 binding sentence: "before it keeps a guess from the human on the critique's verdict that the repository or the task document already settles it or that it is most likely right, it checks the quotations behind that verdict".
- Same entry, *Verification* "complies" example, which repeated the old phrase: "6 already settled in the repository or the task document". The rest of the diff is rewrapping of the same sentences to 100 characters.

One phrase each in the skill and in the decision, as the remark asks. The skill, the entry and its example now say the same; they also match step 2 of `final_review.md`, where the critique settles "by the repository or the document" (line 24). Grep of `project-level/task/skill/` and the entry for "settled in the repository" / "already settles": the only hits are those three places, all widened, plus step 2's own sentence. `orchestrated_mode.md` and `SKILL.md` name the check only by pointing to `final_review.md` and need no change. My N1 of the fix review is closed.

Remarks 2 and 3 (let through), 4 to 8 (accepted), and the paragraph on merging `foundations`: no work of the correction, as the dispatch says; not judged.

## New findings in the correction diff

none. A reading note, not a finding: "judging it already settled in the repository or in the task document or most likely right" chains three alternatives with two "or", and a reader takes the last as a third group, which is what the entry says too ("or that it is most likely right"); no wrong reading follows.

## Checks I ran

- `python -B elements/common/foundation_check.py` — "0 errors", exit 0.
- `python -B instruction-files/check_instructions.py .` — 0 error, 0 warn, 3 info, exit 0.
- Line lengths of `final_review.md` (`awk 'length($0)>100'`) — lines 22 and 49 at 101 characters, both already in the base (they were lines 22 and 48 before the fix; not touched by this diff).
- Grep of the added lines for "gate", absolute paths, `[[` and URLs — no hit.
- Grep for "settled in the repository" / "already settles" in the skill directory and the decision log — see above.
- Not run: the whole gate (forbidden); the test directories (prose only, and the author's `project-level` run of 278 tests stands as theirs).

## Declined to judge

none

## Reaches beyond the dispatch

none

## Working copies

None made this time; `.runs/review-whole/` was removed after the fix review, and `.runs/` holds `orchestrator/` and `task-cycles/` only.

## Unread material

none beyond the earlier reviews': WAY-377 and WAY-378 were read in the changed paragraphs of this diff and in my earlier reviews; the other decisions of my selection are as in `reports/review-whole-report.md`.

## Searches not found or unclear

none
