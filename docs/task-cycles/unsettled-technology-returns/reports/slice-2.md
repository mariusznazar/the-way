# Slice 2 report

**Status:** done

Commit: see `git log -1` on task/unsettled-technology-returns ("docs: send a reserved choice from refinement to the technology step").

Files: project-level/technology/reserved_choices.md (new, 40 lines); resolve_gaps.md (+20/-2); find_settlements.md, carry_foundation.md, final_review.md, draft.md, project_plan_task.md (small additions). All LF, as git ls-files --eol shows.

Checks:
- `python -B gate/run_tests.py project-level` exit 0 (267 tests OK)
- `python -B instruction-files/check_instructions.py . --file project-level/technology/reserved_choices.md` exit 0 (one pre-existing WARN on AGENTS.md:21 `_zadania\`)
- `git grep -l -F "reserved_choices.md" -- project-level/task/skill/resolve_gaps.md` lists the file

Own-work check: requirement most likely missed is that each exception reaches only the opened decision. Re-read each sentence: resolve_gaps, find_settlements and carry_foundation name "a decision the human opened" only; any other collision keeps its old sentence.

Reach beyond dispatch: read project-level/technology/task_run.md, task/template.md Technology section, task/skill/SKILL.md and orchestrated_mode.md, to align wording and the orchestrated pointer.

Choices: refine-task's SKILL.md left unchanged (resolve_gaps carries the pointer, as the slice lists no SKILL.md edit). The three-case run stands as a paragraph and bullets in resolve_gaps.md after the "new choice discovered" sentence. The plan-member text is a new section in project_plan_task.md, not tied to a numbered step.

Entries: none cannot hold; WAY-265/266/267 and glossary match the texts.

**Searches not found or unclear:** none
