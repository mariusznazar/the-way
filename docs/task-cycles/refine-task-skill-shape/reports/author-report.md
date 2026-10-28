# Author report: refine-task skill shape

**Status:** done with concerns.

The scoped change is committed and ready for independent review. Variant-specific procedures moved to
step-named files, product-installed skill entry points now defer named-file reads until the step or
variant that names the file, and WAY-259 records the settled installation rule. WAY-127 is unchanged.
No skill rule was removed or semantically reworded. The only Python source change edits the generated
entry-point sentence; its existing installer test checks the new sentence and absence of the old
blanket-read wording for every generated skill entry point.

## Files and commit

Commit: `9f9001cf51812cdcfbbc16b12c819571e1769454` (`refactor: split refine-task variant instructions`).
`git show --numstat --format= HEAD` (exit 0) reports:

| File | Added | Removed |
|---|---:|---:|
| `foundations/decisions.md` (WAY-259) | 21 | 0 |
| `installation/README.md` | 1 | 1 |
| `installation/install.py` | 3 | 2 |
| `installation/test_install.py` | 3 | 0 |
| `project-level/task/skill/SKILL.md` | 24 | 101 |
| `project-level/task/skill/guideline_findings.md` | 47 | 0 |
| `project-level/task/skill/orchestrated_mode.md` | 48 | 0 |
| `project-level/task/skill/project_plan_task.md` | 28 | 0 |
| `project-level/task/skill/source_only_task.md` | 24 | 0 |
| **Total** | **199** | **104** |

## Foundation step and WAY-259

The handoff-selected decision and invariant entries were read whole by identifier; the full
`foundations/part_map.md` and `foundations/glossary.md` were also read as named in the handoff.
The selection included the installation-scope decisions WAY-09, WAY-27, WAY-34, WAY-38, WAY-89, WAY-100, WAY-102, WAY-107,
WAY-127, WAY-141 and WAY-167. WAY-256 supplies the placement rule; WAY-127 is the nearest existing
entry but answers how a session working on the-way itself reaches its skills. It does not answer
what an entry point written into a product tells an agent to read. The new question therefore stays
narrow in installation, derives from WAY-256, and leaves WAY-127 unchanged.

As required by the decision-writing method, I searched the log for an existing answer, overlap and
possible collision. `rg -n -i "entry point|product.*skill|skill.*product|installed skill" foundations/decisions.md`
(exit 0) found the WAY-127 passages and no existing decision for the product-installed entry-point
instruction. I read the selected relevant entries whole; I did not read the whole log in place of
the selected foundation reading. `rg -n -i "installation|skill-entry-points|entry point|skill entry" foundations/invariants.md`
(exit 0) showed `skill-entry-points` checks tracked repository entry-point presence, identity and
routing, not when a product entry reads named files; `installation-claude-guidance` concerns root
guidance. The
accepted task settlement called for a complies/violates pair, not a new invariant, so WAY-259 uses
that pair. `python -B elements/common/foundation_check.py` (exit 0) confirmed the entry and its
references are valid.

**WAY-259 meaning in Polish:** „Plik wejściowy, który instalator zapisuje w produkcie, każe czytać
skill w całości, a plik wymieniony przez skill w `.the-way` dopiero wtedy, gdy przychodzi nazwany
przez niego krok albo wariant — nie wszystkie pliki naraz na początku.”

## Counts

Baseline words were measured with Python UTF-8 `str.split()` from the clean base
`3aee7d958835cc19b95519f4d21b37538b78e3e1`: `python -B .runs/task-cycles/refine-task-skill-shape/reports/count_baseline.py` (exit 0) produced
2,933 for `SKILL.md` and 1,580 for the task template. Post-change counts use
`python -B .runs/task-cycles/refine-task-skill-shape/reports/count_variants.py` (exit 0).

| Variant | Skill files read | Before | After | Change |
|---|---|---:|---:|---:|
| Manual independent task | `SKILL.md` | 2,933 | 1,888 | -1,045 |
| Manual project-plan task | `SKILL.md`, `project_plan_task.md` | 2,933 | 2,093 | -840 |
| Orchestrated project-plan task | `SKILL.md`, `orchestrated_mode.md`, `project_plan_task.md` | 2,933 | 2,663 | -270 |

`guideline_findings.md` is conditional: it is read only if the product-guideline reading finds a
relevant issue. Its 453 words add to each after count, producing 2,341, 2,546 and 3,116. The
source-only path is outside the requested variants: `SKILL.md` plus `source_only_task.md` is 2,074
words, or 2,527 with the guideline branch. The task template is a separate, unchanged 1,580-word
read outside the skill directory in each variant.

## Checks

Each executed check and its result:

- `python -B .runs/task-cycles/refine-task-skill-shape/reports/count_baseline.py` — exit 0;
  base skill 2,933 words, task template 1,580.
- `python -B .runs/task-cycles/refine-task-skill-shape/reports/count_variants.py` — exit 0;
  post-change variant counts above.
- `python -B -m unittest installation.test_install` — exit 0; 30 tests passed in 362.799 seconds.
- `python -B elements/common/foundation_check.py` — exit 0; 0 errors.
- `python -B instruction-files/check_instructions.py .` — exit 0; 0 errors, 1 warning and 3
  informational lines. The warning is the existing absent private `_zadania\` path at
  `AGENTS.md:21`.
- `python -B agent-instructions/skill_entry_points.py` — exit 0; entry points current.
- `python -B agent-instructions/skill_entry_points.py --check` — exit 2; the script accepts
  `--write` but has no `--check` option. The supported no-argument check above passed.
- `rg -n "orchestrated_mode|project_plan_task|source_only_task|guideline_findings" project-level/task/skill/SKILL.md`
  — exit 0; every moved-file pointer is present at its common step or variant boundary.
- `$paths = @('project-level/task/skill/orchestrated_mode.md','project-level/task/skill/project_plan_task.md','project-level/task/skill/source_only_task.md','project-level/task/skill/guideline_findings.md'); $missing = $paths | Where-Object { -not (Test-Path -LiteralPath $_) }; if ($missing) { $missing; exit 1 }; 'all four sibling files exist'`
  — exit 0; all four files exist.
- The two targeted `rg` foundation searches shown above — exit 0.
- `git diff --check` and `git diff --cached --check` — each exit 0.
- `git rev-parse HEAD` — exit 0; returned the commit named above.
- `git status --short --branch` in the task worktree after commit — exit 0; clean.

The full post-change gate was not run by the author: the base gate had passed before edits, and the
handoff ends this turn at the author/review boundary with focused checks. The reviewer/cycle owns
its next gate. The modified wording assertions were not run red before changing the generator; the
test and generator wording were changed together, so there is no recorded failing run. The focused
test passed. No separate prose-only test was added: the existing integration test checks generated
entry-point output, while the manual crosswalk checks the skill-file reading boundaries.

## Own-work check

The requirement most likely to be missed is that moving a rule must not make the rule unavailable at
the step or variant that needs it, and a pointer must not cause unrelated variant instructions to
load early. I checked each `Move` row in `assessment.md` against the destination section and its
trigger, then checked that `SKILL.md` names the destination from the corresponding step or variant;
this was a manual source-to-destination crosswalk, not a text-only assertion. The pointer search and
path-existence check above passed. The 30 installer tests also passed, confirming that generated
product entry points carry the deferred-read wording for all skill entries. The checks show the
moved procedures are reachable from their intended boundaries. The test verifies generated text,
not an agent's actual reading behavior, so the crosswalk remains the evidence for the skill layout.
That difference is the principal unresolved validation limit.

## Autonomous choices

- I grouped all orchestration-only routing and result rules in `orchestrated_mode.md`, plan-member
  instructions by plan step in `project_plan_task.md`, source-only instructions in
  `source_only_task.md`, and guideline-finding branches in `guideline_findings.md`. Keeping all of
  these in one `SKILL.md` would retain instructions for modes a session may not take; splitting each
  short instruction into its own file would replace it with a pointer and create more files to
  maintain. If the chosen grouping is wrong, a later edit could miss a variant boundary or make a
  shared rule harder to find; the assessment maps every moved fragment to its new location.
- I kept WAY-127 unchanged and recorded WAY-259 as a separate, narrow installation decision, as the
  accepted task settlement specifies. Rewriting WAY-127 would conflate sessions working on the-way
  with product-installed entry points; the cost of the separate choice is that the related read-timing
  rule now appears in two decisions and could drift if future changes update only one.
- I kept the task template count outside the skill-directory totals because it is outside the
  measured directory. The conditional guideline file is counted only when that finding triggers.
  If the actual use path includes the guideline branch, its 453 words narrow the saving; the
  orchestrated variant then totals 3,116, 183 more than the former 2,933-word skill.
## Questions

None remain unresolved.

## Concerns

Conditional on a guideline finding, the orchestrated path reads 3,116 words from the skill directory,
183 more than before. The task asked to move that multi-instruction branch; keeping it loaded
unconditionally would preserve unused guidance in the other variants. Also, WAY-259 and WAY-127
cover related read-timing rules in different entry-point contexts, so future edits should keep their
scopes distinct.

## Reaches beyond the handoff and observed problem

The full decision-log search and the invariant search above were method-required to check whether
WAY-259 duplicates, collides with, or derives an invariant from existing material; no other
foundation entry was selected or read outside the handoff's whole-entry selection. The targeted
transcript search in the assessment used the documented invocation form and returned no matching
transcript; I infer no session behavior from that absence. No broad transcript history was loaded.

During editing, an `apply_patch` call resolved `project-level/task/skill/SKILL.md` against the main
checkout at `C:\Storage\repos\the-way`, not the task worktree. I restored that file from HEAD
and removed the unintended sibling file. `git status --short --branch` in the main checkout
subsequently exited 0 and showed only `## foundations...origin/foundations`. All intended changes
are in `C:\Storage\repos\the-way-refine-task-skill-shape`; its post-commit status check exited
0 and showed a clean branch. No unintended main-checkout change remains.
