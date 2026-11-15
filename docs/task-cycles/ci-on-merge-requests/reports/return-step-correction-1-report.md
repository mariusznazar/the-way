# Report: the return step after correction 1

**Status:** done
**Commits:** none. Nothing the step requires is missing, so nothing is written (as the handoff says for that case).

## What the step compared (range `3eacbc1..7d00a48`)

The correction changed two entries: the new fact `foundations-branch-ruleset` and WAY-16 (*Based on* only).

- The fact against the code: its source is the reading I ran and the reviewer reran (character for character, exit 0); the correction touches no code, so no file of the code can disagree with it. The sentence says what the reading shows and no more.
- WAY-16 against the code: its binding sentences, *Verification* and *Rationale* say the one command runs in CI on every merge request, from a file the product writes, and that the result is a required check with a bypass for the owner. Nothing in `.github/workflows/tests.yml`, `agent-instructions/README.md:70` or `installation/README.md:167` contradicts this or says the rule is missing (searched in the correction; the reviewer's searches agree). No change in this range moves them.
- The search of the foundation for entries naming what changed: the fact is named only by WAY-16; the invariants that derive from WAY-16 (`ci-checking-commands` and `gate-exit-code`, via *Derives from*) rest on no fact (`Rests on: none` for `ci-checking-commands`) and say nothing about the rule, so none needs correction. WAY-73 holds: the fact stands because WAY-16 names it. WAY-84 and WAY-90 are met (a reading for a setting outside the repository; the fact named by its identifier alone).
- The part map: the correction touched only `foundations/`; no part gained or lost a file, a dependency or an answer. No change.

## Places the settlements went to

- Foundation compared with code: done as above; nothing no longer matches.
- Decisions: none written (WAY-16 was already changed by the correction; no choice binds beyond it).
- Invariants: none.
- Environment facts: none written by this step (the correction wrote `foundations-branch-ruleset`; no further outside source rests unrecorded).
- Glossary terms: none (the correction uses no word for which WAY-95 gives an entry).
- Part-map changes: none.
- Projected entries: none.
- Rows of *Settlements to record*: none for this correction (the first cycle's return step stands); `none`.
- The three Minor findings of the correction's review (M1, M2, M3): not fixed, as the handoff says; they go to the request's list. Nothing here contradicts them. I note, so the orchestrator can carry it, that the entry for the new fact is a "the cycle's" entry in the sense of `foundation_step.md` (no row carries it; the human's remark 2 asks for it), and by WAY-114 it should stand in the lower list of the request's description with one English sentence: "The branch rule of `foundations` is an active ruleset `foundations_tests` that requires the check `tests` and lets the owner's admin role bypass it." I did not edit the description.

## Checks

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`): `0 errors`, exit 0 (run at head `7d00a48` in the worktree; nothing changed since).
- No directory was changed by this step, so no `gate/run_tests.py <directory>` was run; the full gate was not run.

## Unread material

- `elements/glossary/skill/SKILL.md` and the rest of `foundation_step.md`'s element skills: not read; no entry of those kinds was written.
- `.runs/task-cycles/ci-on-merge-requests/task.md`: not read whole this time; searched for the rule's words (no hit), the first cycle's return step stands per the handoff.
- The review report: read whole, to avoid contradicting it.

## Searches not found or unclear

- A row of *Settlements to record* of the frozen task concerning the branch rule: a search of the task for `bypass|required|ruleset|branch rule` found none (the task document may be written in another language; I did not search it in that language, so this is not a proof of absence).

## Working copies

None made (`.runs/return-step-correction-1/` was not created).
