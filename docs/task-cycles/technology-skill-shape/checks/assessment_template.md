# Assessment of the skill settle-technology

Mode: judge; kind: skill, by `instruction-files/SKILL.md` and `instruction-files/kind_skill.md`. File judged: `project-level/technology/SKILL.md` at `525cde1dd53c474f56ea0ece289cb60e868aa90d` (2122 words, 170 lines, no file beside it). The frozen task authorises the structural change (To do 1) and two changes of what the leader reads or hands over (To do 2 and 3); no other rule changes in meaning. Every verdict that would change the content of a rule stands below the table as a proposal and is not applied (To do 6).

## 1. Mechanical check

`python -B instruction-files/check_instructions.py .` in the worktree after the change: exit 0, `0 error, 1 warn, 3 info`. The warning is `dead-path AGENTS.md:21 `_zadania\` does not exist`: the root `AGENTS.md` names the private backlog folder relative to its notes folder, not to the repository. This task changes neither the file nor the line. The three `info` lines are size lines of `AGENTS.md`, `CLAUDE.md` and `agent-instructions/README.md`; none says something was left unread. The check was run once, after the change (the skill and its new files change nothing it reads, so a run before would print the same).

How the tools load what is judged: Claude Code and Codex reach the skill through the generated entry points `.claude/skills/the-way-settle-technology/SKILL.md` and `.agents/skills/the-way-settle-technology/SKILL.md`, which tell the session to read `project-level/technology/SKILL.md` in full and a file it names when the step that names it comes (WAY-127, WAY-259). The description does not change, so `python -B agent-instructions/skill_entry_points.py` still prints `entry points are current` (exit 0). A product's installer writes the same entry points for `.the-way/project-level/technology/SKILL.md`; a file beside the skill is read by the path the skill gives.

## 2. The records searched

- The one real run of the skill: the Codex session `01a107ae` of 2026-10-04, `C:\Users\Mariusz\.codex\sessions\2026\10\04\rollout-2026-10-04T18-10-39-01a107ae-806d-71e2-b005-c14a317d7a7f.jsonl.zst`. `zstd -dc <file>` exited 0 and gave 15,914,081 bytes, 5280 lines, so no "not found" below rests on an unread compressed file. The run used the text pinned at `2a8954e` (1335 words), older than the text judged.
  - It was compacted six times (lines 564, 1262, 1858, 2563, 3921, 5096), and the leader read `project-level/technology/SKILL.md` by command 17 times (lines 21, 577, 585, 592, 593, 1008, 1277, 1284, 1312, 1877, 2049, 2050, 2822, 3080, 3935, 3943, 5119). A skill carried through a long session is re-read after compactions; its size is paid again each time.
  - The text the leader gave its research agents is encrypted in the record (`spawn_agent` arguments), so it is read from the run's own brief, `C:\Storage\repos\loop2\.runs\technology-research\brief.md:13`: the agents were told to read `.the-way/project-level/technology/SKILL.md` whole and the Technology section of the template, although the work they did stands in what are now sub-steps 1 to 3 of step 2. The brief also repeated by hand what the old file did not give them: not to edit the definition or `foundations/`, and a report format.
  - Human replies: at line 160 the human answered the question on preferences for the whole list with "nie mam preferencji co do żadnego z tych punktów, nie wiem nawet o czym jest to pytanie" and then described the product. It is one occurrence.
  - Reports of the run use names like `data_store.md` (underscore); the pinned text had no naming rule (`git show 2a8954e:project-level/technology/SKILL.md` holds no `.runs/technology`), so the run says nothing for or against the current rule on the report name.
- Not found in the rollout, read through its 241 human messages and by search for each of `held by`, `critique: passed`, `unknown unknowns`, `you choose`, `I do not know`, `.runs/technology`: an agent that missed a rule of step 0, 1, 2 or 3 for lack of having read it at the right moment. The run's text lacked the tests of options (WAY-138), the look at the running product (WAY-165) and the tie rule (WAY-137), so it cannot show a miss of those.
- The Claude Code records were not searched again: the task's Context states that 41 agents read this `SKILL.md` while working on the-way, none invoked the skill.
- History of the file: `git log --follow --oneline -- project-level/technology/SKILL.md` lists 12 commits; each rule of step 2 cites the decision that sets it, which is the ground used below.

## 3. The table

Quotes reproduce the stated line ranges of the file at `525cde1`; the HTML line breaks keep the source line boundaries, and `&#124;` stands for a pipe. Rows over lines 89 to 91 and 91 to 96 divide line 91 at `Each finds the options`. Every non-blank line of the file belongs to a row. The numbers in the last column count the whitespace-separated words of the fragment.

@@TABLE@@

## 4. Contradictions between files that load together

None found. Two sentences stand twice on purpose: the sentence that the step writes into the definition only (WAY-106) in `SKILL.md` and `research.md`, and the rule on the report name `.runs/technology/<choice>.md` in `SKILL.md` and `research.md`. The research agent reads only its file, the leader reads `SKILL.md` and not `research.md`, and acceptance criteria 3 and 4 ask for both. If one of the two copies is changed, the other has to change with it.

## 5. Proposals

The first is required by To do 6. The other two are what the judgement found beyond the rebuild. None is applied.

### 5.1 Read from the project definition template only the sections the skill uses

Fragment, `project-level/technology/SKILL.md:29-30` at `525cde1`, now `start.md`: "Read the definition whole, `definition_template.md` in full, ..."

Proposed wording: read from `project-level/definition_template.md` the sections "Where it stands, and in what language", "The status line", "Every section, and the words `none` and `TODO`", "Open questions", "Technology" and "Projected foundation changes", and leave out "What a definition is not", "The form", "What is not yet known", "Gate record" and the opening paragraph. Section bounds as the counting rule takes them: from the heading line to the line before the next heading of level 2 that stands outside a code fence. Words saved on every leader route: 63 + 81 + 98 + 65 + 80 = 387 of 6828 on the longest route (about 6 percent).

Judged by `instruction-files/judging.md`:
- When an agent needs the rule: at the start of every leader route. Whether it recognises the moment: yes, it is the first bullet of the first step.
- Ground for the change: a cost of 387 words per leader run. A mistake: not found in the one real run (no record shows a rule of one of the omitted sections missed; the omitted sections were not searched for by name, because no step of the skill uses them) nor in the Claude Code records (no run). A carried decision: none; WAY-150 reads element templates whole, and this template is read whole by `define-project` too.
- By "When to add a rule" a reworded rule enters only on a repeated mistake or a carried decision; neither exists. By "When to remove a rule" the fragment is not unnecessary: the sections left out are not read for any step, but the leader cannot know that a later change of the template puts a rule it needs into one of them.
- Cost of leaving it: 387 words more on each leader run, paid again after each compaction (the real run was compacted six times).
- Cost of making it: the skill names template sections, so a renamed section silently drops a rule from the reading, and no check catches it; the choice of the sections is a judgement the next change of the template must repeat.
- Verdict: not recommended now. Revisit with the first record that shows the leader paying for the template's unused sections, or when the template is divided (the task puts that out of scope).

### 5.2 The weighing rules stand in the research file and in the template's Technology section

Fragments: `research.md` items 2 and 3 (old `SKILL.md:97-111`) and the Technology section of the template (`project-level/definition_template.md:203-234`) both give the properties to read, the lacks, the exclusion of an option with no documentation, the consequences and the lack "an agent does not check the running product this way". The research agent receives that section, so it reads both.

Proposed wording: in `research.md`, replace the restatement in items 2 and 3 by a pointer to the template's Technology section, keeping only the order of the work. Items 2 and 3 of `research.md` are 223 words, so at most about 200 words fewer for the agent.

Judged by `instruction-files/judging.md`: needed at the agent's work; the agent recognises the moment (it is its work). Ground: a cost (the agent reads the same rules twice) against a carried decision (WAY-122, WAY-123, WAY-166 are carried by both texts). No mistake found in the records.
- Cost of leaving it: two copies that can drift, and an agent that meets two wordings of one rule.
- Cost of making it: the agent's file stops being self-contained on the rule, the leader's later steps (`settle.md` sub-steps 5 and 6) and the agent read different texts for the same rule, and it is a change to the content of the rule's place, outside the structural rebuild.
- Verdict: reword, proposed, not recommended in this change; it decides the question of one source of rules for process skills, which WAY-35 settles for element skills only.

### 5.3 The question on preferences for the whole list

Fragment, `SKILL.md:74-78` at `525cde1`, now `list.md`: "In the same message ask, as one question of assessment for the whole list, whether the human has a preference or a constraint for any open choice; "I do not know" is an answer."

Evidence: one reply of the human, "nie mam preferencji co do żadnego z tych punktów, nie wiem nawet o czym jest to pytanie", at line 160 of the Codex session (older text).

Judged: needed when the list is shown; the agent recognises the moment. By "When to add a rule" a rule is reworded for a mistake found more than once in records of the work (WAY-130); this is one occurrence in the one run. Verdict: keep, watched, not reworded.
- Cost of leaving it: the human may meet a question they cannot read, and "I do not know" is allowed as an answer, so the cost is one extra exchange.
- Cost of making it: a reworded question costs words in every run and rests on one reply to an older text.
