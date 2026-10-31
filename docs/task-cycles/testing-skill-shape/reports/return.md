# Return step report

**Status:** done. **Commits:** none (nothing needed correcting). Head `c17f4f8`; worktree clean.

## What I compared with the files at the head

- The entries the change writes or changes: WAY-256 (the sentence on a fragment some steps need, three binding sentences, *Verification*, *Rationale*, *Rejected*), WAY-265 (variant file named in `SKILL.md`; exemption by step file) and WAY-266 (session without refine-task steps 1 and 2; exemption of unrebuilt skills of guidelines), against `product-guidelines/testing/SKILL.md` and its ten files, `product-guidelines/styleguide/SKILL.md` and `instruction-files/kind_skill.md`.
  - WAY-256's complying cases match the files: the template named by steps 2, 3, 4 with "unless an earlier step did" (`SKILL.md` steps 3, 4, 5), the manner of asking in `SKILL.md`; its violating cases no longer occur since "Extend what exists" moved to `SKILL.md` ("Rules that hold across the steps").
  - WAY-265: `SKILL.md` names `research.md` at step 2 and `new_tools.md` at step 4 with their conditions, and the step files (`starting_set.md`, `settle.md`) name them too; the styleguide skill's unchanged step files are outside it.
  - WAY-266: the sentence ends step 0 of both skills; the coding skill (unchanged) is exempt by the entry's last sentence.
  - Citations: `kind_skill.md` and the "unless" clauses cite WAY-256, the variant pointers WAY-265, the step 0 sentences WAY-266; no other file cites the withdrawn old numbering (`grep` over `product-guidelines/`, `instruction-files/`).
- Each decision of *Decisions in play*: WAY-257 (unchanged; the assessment shows both answers in every row), WAY-258 (its "file a step names as WAY-256 gives" is consistent with the extension), WAY-127 and WAY-259 (the entry points read the skill whole and a named file when its step comes; `skill_entry_points.py --write` changed nothing), WAY-248 (step 1 names the parts before it reads anything), WAY-249 (research at every extension, never at a refresh: `starting_set.md`), WAY-250 (`audit.md`), WAY-242 (`new_level.md` and the exemplar item of `settle.md`), WAY-247 (the sentence in "Where the skill works" stands), WAY-120 (both critiques kept), WAY-154 (`orchestrated_mode.md`), WAY-172 (carried by "Where the skill works").
- Each entry the search of the repair found: WAY-125, 127, 128 (rationales still true), 258, 259, 35, 21, 133, 255, the invariant `skill-entry-points`, the facts `single-rule-compliance`, `instruction-density-accuracy`, `claude-skill-nested-references`: all still match.
- The part map entries `product-guidelines` (Files `product-guidelines/**` claims the ten new files), `instruction-files` (`instruction-files/**` claims `kind_skill.md`) and `decisions` (`foundations/decisions.md`): description, *Files* and *Depends on* still hold; the *Scope* values of WAY-265 and WAY-266 name parts the map holds.

## What no longer matched and its correction

none

## Written in this step

Decisions: none beyond those of the foundation step (WAY-256 changed in place; WAY-265 and WAY-266 new). Invariants: none. Environment facts: none (the sources rested on are held: `claude-skill-nested-references`, `single-rule-compliance`, `instruction-density-accuracy`). Glossary terms: none (no word used in another meaning). Part-map changes: none.

## Rows of *Settlements to record*

| # | Row | Entry |
|---|---|---|
| 1 | Extension of WAY-256 for a fragment some steps need | WAY-256 (in place) |
| 2 | Variant file named in `SKILL.md`; unchanged files exempt | WAY-265 |
| 3 | Session without refine-task steps 1 and 2 goes through them first | WAY-266 |

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` - 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` - 0, "0 error, 1 warn, 3 info" (the `_zadania\` warning of the base).
- `python -B agent-instructions/skill_entry_points.py --write` - 0, "entry points are current", nothing changed.
- The whole gate was not run (the orchestrator's gate on the head exited 0).

## Reaches

None.

## Concerns

none beyond those in `fix.md`.

## Searches not found or unclear

none
