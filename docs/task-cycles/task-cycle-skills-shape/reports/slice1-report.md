# Slice 1 report

**Status:** done

**Commit:** 746da1b on task/task-cycle-skills-shape. Changed: instruction-files/kind_skill.md (+7, -0).

**Change:** a paragraph in "Where a fragment of a skill stands": a one-instruction fragment of a step or variant, which would otherwise stand in a file beside the skill, stays in SKILL.md where its pointer would stand, since the pointer is an instruction too (WAY-256); bounded to one instruction against one pointer. No other file changed. It points to no other file.

**Checks** (base 40f0fd3):
- git diff --stat base..HEAD: kind_skill.md alone, exit 0.
- grep -n "WAY-256" instruction-files/*.md: exception in kind_skill.md:18; SKILL.md:13 and :144 are earlier citations, unchanged, not the exception. Matches the intent.
- python -B instruction-files/check_instructions.py . : 0 error, 1 warn (dead-path AGENTS.md:20 _zadania\, already present, not from this slice), exit 0.
- python -B gate/run_tests.py instruction-files: 104 tests OK (5 skipped), exit 0.
- git diff --check: empty, exit 0.
- Not run: whole gate/run_tests.py (orchestrator's).

**Own-work check:** requirement most likely missed: the exception stretching to rules WAY-35 places in templates. Checked by wording: "would otherwise stand in a file beside the skill" as in WAY-256 and the handoff note; the WAY-35 paragraph is untouched.

**Reaches beyond dispatch:** none. **Choices:** placed the paragraph after the two-bullet list and before the WAY-35 paragraph; rejected folding it into the second bullet (it would blur the bullet's rule). **Questions:** none.
