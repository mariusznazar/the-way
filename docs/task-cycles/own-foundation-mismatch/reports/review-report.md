PASS 876482ee4545749f7e3daa8e8c3a3c607f1682fc

# Whole-change review

Reviewed the complete range `76cbe0ea4e766eb9561052355e370d6424c1d32f..876482ee4545749f7e3daa8e8c3a3c607f1682fc`, independently of its author, against the complete frozen task and its accepted settlement. The range contains one commit, adding 27 lines to the decision log and four lines to the reviewer skill. HEAD matches the dispatched head. No spec or plan applies to this one-author change.

## Findings

- Critical: none.
- Important: none.
- Minor: none.
- Blocking findings: 0.
- Out-of-scope findings: 0.

## Declined to judge

None.

## Task, settlement and source fidelity

The required grading instruction appears immediately after the sentence the task identifies in [the reviewer skill](../../../../task-cycle/review/SKILL.md:96). It requires Important for departures from a foundation entry the same change writes or changes. It covers doing what the entry forbids, omitting what it requires, and restating it differently, expressly including a broader account or a missing qualification. “Restate it differently” also covers a narrower account; the examples introduced by “including” do not exhaust that category.

The accepted settlement is recorded as [WAY-263](../../../../foundations/decisions.md:7491), a separate decision with `Relations: derives from WAY-161`, as Q3 requires. Its binding sentence and the skill's instruction have the same meaning. Its rejected alternatives correspond to the alternatives actually preserved under Q1, Q2 and Q3; no additional rejected choice was invented. Its rationale describes the incompatibility and later reliance the task identifies, without importing the historical incident or private source links into the repository's foundation.

WAY-161 is unchanged. The existing distinction between grade and task scope remains directly below the added instruction: an Important finding blocks when it lies within the task. The change does not authorize the orchestrator to regrade findings or change the treatment of Minor findings. The shared review method is used for slice, whole-change, return-step, reconciliation and correction reviews, so the added rule reaches the review stages named by the task. The excluded return-step instruction file is unchanged.

The entry's location, fields, identifier, reference and verification examples follow the decision template and shared rules. The new instruction is one instruction, consistent with the single-instruction exception of WAY-256. No part-map responsibility or file assignment changes. No invariant or invariant test changes. The changed material introduces no trust boundary, irreversible operation, human action, executable code or user interface.

## Checks and results

- `git diff 76cbe0ea4e766eb9561052355e370d6424c1d32f..876482ee4545749f7e3daa8e8c3a3c607f1682fc` — exit 0; read the whole diff, including all of WAY-263.
- `git log --oneline 76cbe0ea4e766eb9561052355e370d6424c1d32f..876482ee4545749f7e3daa8e8c3a3c607f1682fc` — exit 0; one commit, `876482e docs: grade foundation mismatches as important`.
- `git rev-parse HEAD` — exit 0; exact dispatched head.
- `git diff --numstat 76cbe0ea4e766eb9561052355e370d6424c1d32f..876482ee4545749f7e3daa8e8c3a3c607f1682fc` — exit 0; only the two dispatched files, with 27 and four additions respectively and no deletions.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `git diff --check 76cbe0ea4e766eb9561052355e370d6424c1d32f..876482ee4545749f7e3daa8e8c3a3c607f1682fc` — exit 0.
- `git diff d115159..76cbe0ea4e766eb9561052355e370d6424c1d32f -- task-cycle/review/SKILL.md` — exit 0; the intervening change adds the report's unsuccessful-search requirement, without changing the grading or foundation comparison on which the task relies.
- Manual semantic check: compared Q1, Q2, Q3 and the accepted settlement with both new passages. For an entry forbidding a duplicate rule and a changed file duplicating it, both passages prescribe Important. They do the same for an omitted requirement and for a repeated account that broadens, narrows or drops a qualification. Replacing a newly added entry with an existing entry edited by the change does not remove the criterion. A finding against an untouched entry is not newly forced to Important by this sentence; the existing review criteria still apply. No required case was lost or added beyond the settled meaning.
- Manual own-work-check review: the author correctly selected the restatement case as the weakest requirement, and its comparison would expose a missing restatement branch, missing qualification case or a restriction to newly written entries. Independently repeated that comparison above. The absence of a permanent test is appropriate for this change in grading prose; a string-presence test would not establish the instruction's meaning or a future reviewer's compliance.
- Manual integration check: read the review dispatch and review-ending passages in the cycle skill and the correction instructions. They route reviews through the changed method and leave the reviewer in control of grade and scope. No alternate grading implementation needs the new sentence copied into it.
- Manual foundation check: selected and read the touched part's decisions, relevant invariants and glossary through the prescribed selection method; compared the diff with their requirements. The foundation and its operational instruction agree. Repository integration follows the pre-main route of the repository guide. A lookup of `refs/heads/main` returned exit 128 (no such ref), consistent with that route; this is not a failed product check.
- `git status --short` — exit 0, empty before writing this ignored report. Reviewed files, index and branch were not changed by this review.

The full gate was not run: WAY-160 and the dispatch assign it to the orchestrator. No check attempted by this reviewer remains unverified. No UI or mutation-tool check applies to this prose change.

## Reaches beyond the dispatch and initial selection

- [Decision template](../../../../elements/decisions/template.md) and [shared rules](../../../../elements/common/rules.md), read whole, to verify the new entry's form and the allowed source of its rejected alternatives.
- [Cycle skill](../../../../task-cycle/skill/SKILL.md:289), the dispatch and review-ending passages, and [correction instructions](../../../../task-cycle/skill/correction.md), to verify that the shared grading method reaches the review stages named by the task.
- The author's named reaches WAY-07, WAY-35, WAY-64, WAY-145, WAY-169 and WAY-171 in [the decision log](../../../../foundations/decisions.md), read whole, to verify the report's consistency claims about editing entries, the placement of rules and accounts derived from entries. WAY-135 and WAY-148 were already covered by the required selection. None requires another change for this task.
- The earlier-to-base diff of the reviewer skill, to verify that the task's historical source still supplies the applicable grading context.

## Searches not found or unclear

- No root `guidelines/` directory was found (`Test-Path -LiteralPath guidelines` returned False). This is the known situation explicitly settled by Q4: this task follows the repository guide with an empty guidelines selection.
- No local `refs/heads/main` was found (`git show-ref --verify refs/heads/main`, exit 128). The repository guide explicitly supplies the integration route before that branch exists.
- A search for the literal `task-cycle/review/SKILL.md:` in non-ignored Markdown outside `.runs/` returned no matches. This search was for current line-number citations that the insertion might make stale; the task's historical citations are explicitly tied to their source commit.
- No unresolved ambiguity remains.
