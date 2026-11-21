# Findings for the fix — the Minor findings of the review of the whole change

Source: `reports/review-whole-report.md`, review `PASS 7d063ef278748884de28577f582b2ab0767d068d`, range `19e5774a..7d063ef2`. No blocking finding. The reviewer lists these six Minor findings, all within the task; none is marked outside the task's scope. Cut from the report in the reviewer's words.

## Minor (all within the task unless said otherwise)

1. **Texts of the change that claim something about Codex.** The cycle left Codex open (task,
   *Questions carried to cycle*); the absence of a Codex check is not graded. These texts state the
   hiding without saying it is Claude Code's, and are read by Codex sessions too:
   - `AGENTS.md:11-13` — "The entry points carry `disable-model-invocation: true`, so the model is
     not offered a skill of the-way and never calls one". `AGENTS.md` is the file Codex reads
     (WAY-132).
   - `foundations/decisions.md:3342-3343` (WAY-127, sentence) — "so that the model is offered no
     skill of the-way, in the-way itself or in a product that carries it as `.the-way`". Its
     *Based on* gains only the Claude Code fact `claude-code-skill-model-hiding`. In a product the
     claim holds for Codex for another reason (`codex-repository-skills`: Codex does not scan the
     nested `.the-way/.agents/skills`); in the-way itself under Codex nothing backs it.
   - `foundations/decisions.md:3392-3393` (WAY-127, *Rationale*) — "a request naming a skill without
     its command brings no skill in the-way itself".
   - `agent-instructions/skill_entry_points.py:211`, hence all 46 entry points including the 23 under
     `.agents/skills/` that Codex reads, and the 15 skill paragraphs — "since the entry points of
     the-way's skills are hidden from the model".
   - `README.md:159-161` is qualified ("which Claude Code documents as removing ..."), but its
     consequence "so a session does not call a skill of the-way" is stated for Claude Code and Codex
     sessions alike. The generator's docstring (`skill_entry_points.py:12-13`, "in Claude Code") is
     the one text that keeps the claim to Claude Code.
   Why it matters: a reader of WAY-127 takes as settled for Codex a behaviour no fact gives. The
   consequence for behaviour is small: a Codex model that is still offered the skills and calls one
   reaches the same entry point, whose text sends it to the file. Suggested: qualify "in Claude Code"
   in `AGENTS.md` and in WAY-127's sentence and price.

2. **The invariant test checks only part of the sentence's new clause.** The invariant
   `skill-entry-points` (`foundations/invariants.md:286`) requires that the text "tells it not to
   call another such skill but to read that skill's `SKILL.md` there". The test
   (`gate/test_skills_reach_the_way_sessions.py:32-38`) adds only `"do not call it"` to
   `REQUIRED_WORDS`. An entry point that says "do not call it" without sending the session to the
   file would pass. The generator's test (`agent-instructions/test_skill_entry_points.py:64-70`,
   whole written-out text) does pin the sentence, so the gap is in the invariant's own test only.

3. **Two ways to find a named skill's file.** WAY-127's second paragraph
   (`foundations/decisions.md:3346`) and its *Rationale* (3393-3394, "with the path from the entry
   point's list") put the path in the entry point's list. The 15 skill paragraphs (for example
   `elements/decisions/skill/SKILL.md:16-20`) instead tell the session to search the files named
   `SKILL.md` under the root for the line `name: <that name>`. That is the convention already in
   `task-cycle/skill/foundation_step.md:19-21` and `task-cycle/plan/SKILL.md:18-20`, so this is no
   contradiction. But a search under the root that does not honour `.gitignore` also finds the copies
   in working copies of other commits under `.runs/`, which the list would not. Suggested: point the
   paragraphs at the entry point's list first.

4. **A dispatched agent in the-way is not told to get the path.** `project-level/lead/skill/SKILL.md:116`
   ("Dispatch one fresh `refine-task` agent ...") and `:142` ("dispatch one fresh independent
   `critique`") name a skill for a subagent. The new paragraph (`project-level/lead/skill/SKILL.md:20-24`)
   says that a skill named there "is read as a file, not called". It does not say that the brief of a
   dispatched agent carries that file's path. In a session on the-way the model is now offered no
   `the-way-*` skill but is still offered personal skills of the same unprefixed name (`AGENTS.md`
   itself names `refine-task` and `critique` as such). A brief that names the skill alone can let the
   personal skill stand in, which the prefix used to prevent (WAY-127 *Rationale*: "The prefix keeps
   a personal skill of the same name from standing in"). This is low in practice, since lead-project
   runs in products, where the hand-over is unchanged.

5. **A message and a docstring that stopped being true.** `gate/test_skills_reach_the_way_sessions.py:3-4`
   (docstring) and `:226-227` (failure message) still say "a skill of the-way a session would not
   find under its `the-way-` name". The test now also fails on an entry point the model *would* find
   (no hiding field). `AGENTS.md:19` was reworded ("a skill a human could not start under its
   `the-way-` name") but has the same gap for the field.

6. **WAY-127's *Scope* omits parts it governs.** It is partly older than the change, which rewrote the
   entry. `foundations/decisions.md:3350-3351` names neither `foundation-review` nor
   `product-guidelines`. The change rewrote the paragraphs of `foundation-review/SKILL.md` and
   `product-guidelines/{coding,styleguide,testing}/SKILL.md` to WAY-127's rule, and its
   *Verification* judges exactly those paragraphs. A later change to those files does not find WAY-127
   by `--part` (WAY-21). The omission existed at the base; the change, which rewrites WAY-127, is the
   cheap place to add the parts.
