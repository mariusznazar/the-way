# Return step report — review-structure-form-class

**Status:** done. One commit: `b596eec` (head to compare was `c6af26a`).

## What was compared, and what no longer matched

Compared with the files at `c6af26a`:

- **WAY-355 to WAY-360, WAY-229, WAY-164** against the files they bind: `product-guidelines/coding/{template,settle,trial_run,recognize,task_document,hand_back,SKILL}.md`,
  `product-guidelines/audit_end.md`, `task-cycle/review/{SKILL,whole_change}.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`,
  `task-cycle/change_file_sizes.py` and its tests. They agree: the heading `### Size of a function and a file` after `### Logging scope`
  (WAY-355); the test naming each function and file over a threshold, run on the base and on the head, and no command of its own (WAY-356,
  `whole_change.md`); the two numbers of the review of the whole change (WAY-357, the script and `whole_change.md`); the two grades
  (WAY-358, WAY-359, section 3 of `review/SKILL.md`); the move-out slice and the first commit (WAY-360, `plan/SKILL.md`, `change/SKILL.md`);
  the violated mark only for code the exceptions do not name (WAY-355 binding sentence, template, settle, trial run, and its *Verification*).
  WAY-229 and WAY-164: binding sentences and fields as in the base (checked in the author report's own-work check).
- **The entries of the task's *Decisions in play* that the change does not edit** (WAY-161, WAY-297, WAY-263, WAY-51, WAY-135, WAY-16, WAY-271,
  WAY-278, WAY-168, WAY-173, WAY-203, WAY-05, WAY-27, WAY-328), each against the new entries: no collision. WAY-358 and WAY-359 each
  `narrow WAY-161` and say the area; WAY-263 and WAY-297 are kept as written; WAY-135 stays (WAY-360 says the addition is no open design
  choice); WAY-16 stays (WAY-356 derives from it); WAY-271 and WAY-278 are kept, the size rule following the six and reaching a
  product by the same extension; WAY-203 is kept, the size rule standing outside the linter's set; WAY-05 and WAY-27 are met (measurements
  stand with their conditions or a pointer to WAY-229, no pointer outside the repository).
- **Part map** entries of `task-cycle`, `product-guidelines`, `decisions`: the responsibilities still say what the part holds; the two new files
  lie under `task-cycle/**`; no part is added, so the *Scope* of WAY-328 and WAY-344 stays. The new script reads git and counts lines and
  names, runs no file it reads and writes nothing; I did not add it to the *Trust boundary* of `task-cycle`, as `slice_size.py` and the other
  scripts that read files of a product are not there either.
- **Glossary:** `standing check` (corrected in the fix, M2: the rule of size is none of the three the template requires), `binding sentence`,
  `open design choice`, `slice`, `invariant`, `gate`, `foundation` are used as their entries give. No word of the change needs an entry (WAY-95).
- **Invariants of the touched parts**: `script-language`, `script-imports` (standard library only), `script-subprocesses` (git only),
  `cross-part-imports` (the test imports a file of its own part), `tracked-file-private-paths`, `repository-file-location`,
  `skill-entry-points` (no description changed), `derived-file-content`. None is contradicted; no invariant is written (the task sets none for
  the-way).
- **Search of the whole foundation and of `task-cycle/`, `product-guidelines/`, `process-audit/`, `foundation-review/`** for a sentence that lists what the
  review of the whole change checks, what the plan begins with, or what the coding template requires: `task-cycle/skill/*.md`, `record_template.md`
  (its field *Whole-change review* lists what the orchestrator records, not what the review checks), `product-guidelines/template.md`,
  `product-guidelines/audit_end.md` (corrected in the fix, M3), `task-cycle/review/SKILL.md` section 2, `process-audit/`: nothing else still lists them.

**One correction:** `product-guidelines/coding/template.md`, the bullet on the six rules said "the product's further rules follow those"; with the rule of
size between the six and the further rules it now says "the rule of size below and then the product's further rules follow those" (and the bullet
of the rule of size was re-wrapped). WAY-271's *Verification* ("the product's further rules follow them") stays true as written, so it is not changed.

## Fields of the record's *Return step*

- Decisions written: none beyond the foundation step's WAY-355 to WAY-360; changed: none by this step (WAY-229 and WAY-164 were edited by the foundation step).
- Rows written: row 3 = WAY-355; row 4 = WAY-356; row 6 = WAY-357; row 1 = WAY-358; row 2 = WAY-359; row 5 = WAY-360. All six rows are written.
- Invariants: none. Environment facts: none. Glossary terms: none. Part-map changes: none. Projected entries: none (the task carries none).
- Choices that bind after the merge and have no entry: none.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B task-cycle/private_paths_check.py product-guidelines/coding/template.md` — exit 0.
- `python -B gate/run_tests.py instruction-files` — exit 0.
- Not run: the whole gate; `gate/run_tests.py task-cycle` (no file of `task-cycle/` changed in this step).

## Unread material

none.

## Searches not found or unclear

none.
