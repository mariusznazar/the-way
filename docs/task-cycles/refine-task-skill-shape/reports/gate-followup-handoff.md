# Complete the one-author change after a full-gate failure

Work in `C:/Storage/repos/the-way-refine-task-skill-shape`, on the existing branch, current head `8f26dd665897d56da1b50cd83514484035aec0c4`. User implementation-cycle delegation continues. This is completion of **the whole change as the one author** after step 10 found affected tests, not another fix of the already resolved R1–R3 review findings. Read worktree `task-cycle/change/SKILL.md` whole, taking named files when applicable. No spec or plan, no new design choice. Questions to /root, no human or next-stage work. Do not read cycle.md.

Frozen task `.runs/task-cycles/refine-task-skill-shape/task.md` remains the authority, whole. Its acceptance criterion says:

> Kod w Pythonie zmienia się tylko w zdaniu pliku wejściowego w `installation/install.py` i w teście tego zdania (To do 1).

Its To do 1 says:

> test `installation/test_install.py:123`, który przechodzi po plikach wejściowych wszystkich skilli, sprawdza w każdym, że nowe zdanie w nim stoi, a „Read the files it references” nie;

The task's accepted answer also explicitly notes three existing guideline tests of the first sentence. Root's initial two-file-only dispatch was a narrower interpretation than that sentence-subject boundary. The full gate now demonstrates that the same deliberate sentence change affects three pre-existing exact-text assertions. The smallest meaning-preserving completion is to update only those assertions to the same complete accepted sentence; this changes tests of this sentence, not any other Python behavior. Record that bounded interpretation and any objection supported by the source; do not widen it.

Current full-gate log `.runs/task-cycles/refine-task-skill-shape/change-gate.log` shows three failures:
- `installation/test_coding_guidelines_installation.py:93`, test_preview_apply_repeat_exposes_the_coding_guidelines_skill_and_preserves_product;
- `installation/test_styleguide_installation.py:87`, test_preview_apply_repeat_exposes_the_styleguide_skill_and_preserves_product;
- `installation/test_testing_guidelines_installation.py:93`, test_preview_apply_repeat_exposes_the_testing_guidelines_skill_and_preserves_product.

All require the old first sentence ending `in full and follow it.`; the agreed new text continues with a comma. Update each expected literal to the full agreed sentence with its SKILL_SOURCE. Do not weaken it to a substring or change the generator, other assertions, imports, fixtures or product behavior. Read each changed test file whole. Keep Minor M1–M4 untouched. No foundation changes are expected; current WAY-259 and the earlier foundation selection apply. Empty guideline selection remains expressly accepted. Trust boundary yes (installer); no actual product installation or irreversible action.

Wait for /root's explicit message that the running gate completed before editing tracked source. You may read and prepare now. Then run the three affected test methods, record exact commands/exits and the gate's failing evidence, commit only the three explicit paths. Root owns the final full gate and an independent review of this new range. No push/PR or return step in this dispatch.

Full report: `.runs/task-cycles/refine-task-skill-shape/reports/gate-followup-report.md`. Include status, changes/commit, commands/exits, weakest-point check, choices/reaches, and acknowledge the revised bounded scope interpretation. Return before review.
