# Return-step report

**Status:** done with concerns.

**Commit:** no new commit needed. The return comparison found no mismatch requiring a foundation
entry or source correction. HEAD remains `9c77136964881f39764d8ad1ed6c97061a126890`; the final
reviewed change is intact and the worktree is clean. No push or PR was made.

## Foundation comparison

The frozen task carries one accepted row under *Settlements to record*: row 1, a new decision for
product-installed entry points. Its content, scope, derivation from WAY-256, complies/violates pair,
and instruction to leave WAY-127 unchanged match the new WAY-259 entry in
`foundations/decisions.md`. WAY-259 says an installed entry point reads the pinned skill in full,
then reads a named file in `.the-way` only when its step or variant comes. Its Polish meaning
sentence for the request is: „Plik wejściowy, który instalator zapisuje w produkcie, każe czytać
skill w całości, a plik wymieniony przez skill w `.the-way` dopiero wtedy, gdy przychodzi nazwany
przez niego krok albo wariant — nie wszystkie pliki naraz na początku.”

The other task references were compared with the change and the foundation search recorded in
`author-report.md`:

- WAY-256 is the placement decision used for the `refine-task` reorganization and the basis of
  WAY-259. WAY-257 supplies the judgment-row method used in the assessment. Neither needs a new
  entry.
- WAY-127 governs sessions reaching the-way skills from the-way's own checkout or worktree. It
  remains unchanged and does not cover the product-installed entry point. The earlier search of
  installation-scoped decisions found no existing decision about the product entry point's read
  timing; the earlier invariant search found no invariant covering that timing. WAY-259 fills that
  narrow gap without broadening WAY-127.
- WAY-34 keeps product use pinned to a commit; the new generated wording reaches a product when it
  updates that pin and runs the installer. The changed installation behavior fits that boundary.
- WAY-128's routing sentence remains as reviewed. Its reference enumeration does not name WAY-259;
  this is the retained Minor M1 reference issue, not an unrecorded return-step repair.

Only settlement row 1 required a foundation entry, and it maps to WAY-259. The other *Questions to
settle* have answers already recorded in the task: they select an empty guideline set, keep the
cycle reading methods from its worktree, and assign the assessment and file layout to the cycle.
They do not create additional settlements or entries. No code-created projected decision or
invariant beyond row 1 was found.

## Invariants, surfaces, and other foundation elements

No invariant is written or changed. `skill-entry-points` remains a test-method invariant with
`Violated: no`; it covers tracked repository entry-point pairs and routing, not the text generated
for a product. `installation-claude-guidance` also remains `Violated: no`; it covers root Claude
guidance and is unaffected. The new behavior is checked by the installation integration tests that
exercise generated wrappers. No invariant test, invariant surface, or `Violated` mark changed.

The touched part-map entry, `installation-command`, still accurately describes the installer's
preview/confirmation boundary and ownership of the skill entry points it wrote. The sentence change
does not broaden the files the installer may rewrite, so no part-map change is needed. No source
fact outside the product foundation is newly assumed, and no product-specific word has a new or
conflicting meaning; no environment fact or glossary entry is needed.

## Review findings and limitation

The bounded review of the follow-up is PASS with zero new findings. The previous whole-change
reviews remain authoritative for the carried Minor findings. M1 remains: WAY-128's enumeration does
not mention WAY-259. M2 is partly addressed in the rewritten assessment, but it still does not say
whether semantic proposals were considered and none warranted. M3's concrete step-6 trigger/count
defect is addressed by the rewritten assessment, though the original remark remains carried with
that qualification. M4 remains: the assessment table summarizes some fragments rather than quoting
them and has stale source ranges, which limits traceability when a human reviews the placement
judgments. Per the cycle instruction, I did not use the return step to repair any of these Minor
remarks. The final gate verifies the repository tests; it does not remove those report-level review
qualifications.

## Checks

Root owns the successful final full-gate run. `python -B gate/run_tests.py` — exit 0, recorded in
`.runs/task-cycles/refine-task-skill-shape/final-gate.exit` and
`.runs/task-cycles/refine-task-skill-shape/final-gate.log`: 613 tests across 8 directories, every
directory passed, with 5 known Windows skips for POSIX/FIFO semantics. This is root-owned evidence,
not a gate run by this author.

Return-step inspection checks run from `C:/Storage/repos/the-way-refine-task-skill-shape`:

- `Get-Content -Raw -Encoding UTF8 '.runs/task-cycles/refine-task-skill-shape/reports/return-handoff.md'` — exit 0; read the complete return handoff.
- `Get-Content -Raw -Encoding UTF8 'task-cycle/skill/return_step.md'` — exit 0; read the return-step method whole.
- `Get-Content -Raw -Encoding UTF8 'task-cycle/skill/foundation_step.md'` — exit 0; read the foundation-step method whole.
- `Get-Content -Raw -Encoding UTF8 '.runs/task-cycles/refine-task-skill-shape/task.md'` — exit 0; read the frozen task whole.
- `Get-Content -Raw -Encoding UTF8 '.runs/task-cycles/refine-task-skill-shape/reports/gate-review.md'` — exit 0; confirmed PASS of the follow-up review.
- `rg -n 'WAY-259|WAY-127|skill-entry-points|installation-claude-guidance|installation-command|Settlements to record' foundations/decisions.md foundations/invariants.md foundations/environment_facts.md foundations/glossary.md foundations/part_map.md` — exit 0; located the comparison entries.
- `git diff --stat 3aee7d958835cc19b95519f4d21b37538b78e3e1..9c77136964881f39764d8ad1ed6c97061a126890` — exit 0; summarized the already reviewed task change, 18 files, 355 additions and 226 deletions.
- `git status --short --branch` — exit 0; clean tracked worktree on `task/refine-task-skill-shape`.
- `git rev-parse HEAD` — exit 0; `9c77136964881f39764d8ad1ed6c97061a126890`.
- `git check-ignore -v '.runs/task-cycles/refine-task-skill-shape/reports/return-report.md'` — exit 0; the return report is ignored under `.runs/` and is not a tracked source change.
- `Get-Content -Raw -Encoding UTF8 '.runs/task-cycles/refine-task-skill-shape/reports/return-report.md'` — exit 0; verified the saved report and its Polish meaning sentence.

The decision entry was validated earlier with `python -B elements/common/foundation_check.py` — exit
0, zero errors — as recorded in `author-report.md`. No source or foundation edit was required during
this return step, so no new commit or fresh review is needed.

An initial read probe mistakenly looked for `change-gate.exit` under a nonexistent `change/`
subdirectory: `Get-Content -Raw -Encoding UTF8 '.runs/task-cycles/refine-task-skill-shape/change/change-gate.exit'`
— exit 1 (path not found). The correction `Get-Content -Raw -Encoding UTF8
'.runs/task-cycles/refine-task-skill-shape/change-gate.exit'` — exit 0 — showed the earlier gate's
exit 1; that was not the final gate. The successful result above comes from the distinct
`final-gate.exit` and `final-gate.log` files.

## Reaches and choices

No reach beyond the return handoff's named task, foundation selection, part map, author reports and
review records was necessary. The return comparison found the task's one settlement already
recorded and the other named foundations correctly unchanged. I chose to keep the four Minor
remarks carried with the reviewer's current-state qualifications; fixing them here would cross the
handoff's explicit boundary and start another implementation round.
