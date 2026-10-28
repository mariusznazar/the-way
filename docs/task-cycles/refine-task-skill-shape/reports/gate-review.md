PASS 9c77136964881f39764d8ad1ed6c97061a126890

# Review of the full-gate follow-up

Reviewed range: `8f26dd665897d56da1b50cd83514484035aec0c4..9c77136964881f39764d8ad1ed6c97061a126890` in `C:/Storage/repos/the-way-refine-task-skill-shape`.

New findings: 0 blocking, 0 Minor, 0 out of scope. This is the bounded review of three changed test assertions, not a replacement for `review.md` or `fix-review.md`. Their findings and dispositions remain unchanged, including the carried Minor remarks M1–M4 with the qualifications in `fix-review.md`.

## Scope and fidelity

The scope interpretation is justified by the frozen task, independently of the author's and orchestrator's claims. Its acceptance criterion says: “Kod w Pythonie zmienia się tylko w zdaniu pliku wejściowego w `installation/install.py` i w teście tego zdania (To do 1).” The accepted answer on wording also explicitly identifies the three existing guideline tests as checking the old first sentence, with `installation/test_coding_guidelines_installation.py:93` as the example. The restriction concerns the entry-point sentence and testing that sentence. It is not a requirement to leave contradictory expectations for the same sentence in the three named existing tests. Updating only those literals is within the task; changing their scenarios or unrelated Python would require a different assessment.

I read the full diff and all three changed files, reviewing the expected prose separately from the surrounding test code. At `installation/test_coding_guidelines_installation.py:93`, `installation/test_styleguide_installation.py:87` and `installation/test_testing_guidelines_installation.py:93`, the assembled expected string is precisely:

> Read `.the-way/<path>` in full and follow it, and read a file it names inside `.the-way` when the step or variant that names it comes, not all of them at the start.

Each `<path>` comes from that test's fixed `SKILL_SOURCE`, respectively `product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md` and `product-guidelines/testing/SKILL.md`. The expectation is independent of the generator. Each assertion requires the whole accepted sentence, including the original obligation to read and follow the skill in full and the timing restriction for referenced files. It is not reduced to a shorter passing fragment. The test reads the actual installed wrapper and also requires the two client wrappers to have equal bytes. The previous wording with a period immediately after “follow it” fails this new expectation. The three old expectations failed against the accepted generator wording, as the preceding gate log demonstrates.

The three assertion replacements are the entire diff: 9 added lines and 3 removed lines. The generator, installer guards, foundation entries, test scenarios and product-preservation assertions are unchanged. This agrees with the accepted wording and WAY-259 examined in the earlier review. No invariant test changed. The author's own-work check targets the vulnerable part of this follow-up—the exact independent expected sentence and each fixed path—and is appropriate.

## Trust boundary

The installer works with outside product files, but this range changes only expected strings. The focused runs still exercise preview, apply, repeat, wrapper equality, product preservation and pinning in disposable product repositories. No guard or hostile-input scenario changed, so the earlier crafted-input verification remains relevant; I did not repeat it or install into an actual product. No irreversible operation is introduced.

## Checks

All commands ran in `C:/Storage/repos/the-way-refine-task-skill-shape`.

- `git rev-parse HEAD` — exit 0; the exact dispatched head.
- `git log --oneline 8f26dd6..9c77136` — exit 0; one commit, `test: align skill entrypoint sentence assertions`.
- `git diff 8f26dd6..9c77136` — exit 0; full diff inspected as described above.
- `git diff --stat 8f26dd665897d56da1b50cd83514484035aec0c4..9c77136964881f39764d8ad1ed6c97061a126890` — exit 0; only the three test files, 9 additions and 3 removals.
- `git diff --check 8f26dd665897d56da1b50cd83514484035aec0c4..9c77136964881f39764d8ad1ed6c97061a126890` — exit 0.
- `python -B -m unittest installation.test_coding_guidelines_installation.CodingGuidelinesInstallationTest.test_preview_apply_repeat_exposes_the_coding_guidelines_skill_and_preserves_product installation.test_styleguide_installation.StyleguideInstallationTest.test_preview_apply_repeat_exposes_the_styleguide_skill_and_preserves_product installation.test_testing_guidelines_installation.TestingGuidelinesInstallationTest.test_preview_apply_repeat_exposes_the_testing_guidelines_skill_and_preserves_product` — exit 0; all 3 tests passed in 22.129 seconds.
- `git status --short` — exit 0; clean tracked worktree after the focused tests.
- Manual evidence check of `change-gate.log` and `change-gate.exit` — confirms exit 1 and the three old first-sentence assertions as the installation failures. The log reports 613 tests across 8 directory runs. This is the orchestrator's preceding full-gate evidence, not a new full-gate run by this reviewer.

No attempted check was unavailable. The full gate was deliberately not repeated: the review method reserves it for the orchestrator after this review.

## Declined to judge

None.

## Reaches beyond the dispatch

None. The frozen task, the three full test files, the author report and handoff, earlier reviews, selected foundation context and preceding gate evidence are all within the dispatch.
