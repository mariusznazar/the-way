### Task 7: The principles (spec §4.3)

**Files:**
- Modify: `instruction-files/principles.md`

**Interfaces:**
- Consumes: the decision numbers of Task 1.4 (below as WAY-128–WAY-133; replace each by the number 1.4 reported if renumbered); the fact identifiers of Task 1.2.
- Produces: principles that name the decisions adopting them, one threshold for a rule, Codex's copies in `.agents/skills/`, the local hook as a keeper against slips only, and sources a reader can reach.

- [ ] **Step 1: Make the edits** with the Edit tool, each old text quoted from the file as Task 0 brought it:

1. Opening paragraph — "Code, Codex and Cursor at once. The skill in `skill/` applies these principles; the sources they\nrest on are listed at the end." becomes:
```markdown
Code, Codex and Cursor at once. The skill in `SKILL.md` beside this file applies these principles;
the sources they rest on are listed at the end. Where the-way has adopted a principle by a
decision, the principle names that decision in brackets.
```
2. §1, the bullet "**Loaded is not yet carried out.**": "What must happen every time goes into a hook, a linter or a CI check." becomes "What must happen every time goes into a CI check, a linter or a check of a step's output, and into a local hook only against slips (WAY-133)."
3. §2: "A line stays when it meets three conditions at once:" becomes "A line stays when it meets three conditions at once (WAY-128):".
4. §2, the bullet "**Pointers to ways in.**": "be recognisable at the moment X happens, and the target is given as a path in backticks." becomes "be recognisable at the moment X happens, and the target is given as a path in backticks (WAY-129)."
5. §3: "A rule's place is set by what should trigger it — not by how many rules an area has or how long\nthey are." becomes "A rule's place is set by what should trigger it — not by how many rules an area has or how long\nthey are (WAY-128)."
6. §3 table, the row "| every time, without exception | in a hook, a linter, a CI check or a check of a step's output | an instruction may explain what the check is for, but does not replace it |" becomes:
```markdown
| every time, without exception | in a CI check, a linter or a check of a step's output; in a local git hook only against slips | an instruction may explain what the check is for, but does not replace it (WAY-133) |
```
7. §4 table, the row "| main file | `AGENTS.md` at the root | … | `CLAUDE.md` only for additions meant for Claude Code alone; its first line is `@AGENTS.md` on its own |": the last cell ends "its first line is `@AGENTS.md` on its own (WAY-132) |".
8. §4 table, the row beginning "| procedures of activities |" becomes:
```markdown
| procedures of activities | a skill in `.claude/skills/`; for Codex, a pointer to its `SKILL.md` by path from `AGENTS.md`, or a copy in `.agents/skills/` | Claude Code and Cursor discover this directory themselves; Codex does not read it, so it gets there through the pointer, or reads the copy in `.agents/skills/` (fact `codex-repository-skills`) | — |
```
9. §4 table, the row "| what must happen every time | a git hook, a linter, CI, a check of a step's output | they work outside the agent | a Claude Code hook (text injected when a command is run) |" becomes:
```markdown
| what must happen every time | CI, a linter, a check of a step's output; a git hook against slips | they work outside the agent (WAY-133) | a Claude Code hook (text injected when a command is run), against slips |
```
10. §4 pitfalls: "- **`@path` only as `@AGENTS.md` in `CLAUDE.md`, on a line of its own.** Nowhere else does it serve" becomes "- **`@path` only as `@AGENTS.md` alone on the first line of `CLAUDE.md`** (WAY-129, WAY-132). Nowhere else does it serve"; and after the pitfall "- **No symbolic links on Windows** …" add:
```markdown
- **A local git hook keeps a rule against slips, not against an agent that can turn it off.** One
  switch skips it; a rule an agent must not be able to skip is kept by CI or by the check of a
  step's output (WAY-133).
```
11. §6 "Statically": after the bullet "- **Every line of the main file meets the three conditions of section 2.**" add:
```markdown
- **A verdict to add, reword or move a rule rests on a mistake found more than once in records of
  the work, or on a stated cost**; where no such mistake was found, the review says what it
  searched (WAY-130).
```
and in "Typical defects" add, after "two instructions that contradict each other;" (making that line end with `;`): "  - a rule that has to hold every time, kept only by a hook an agent can switch off." In "Mechanical checks": "`@path` appears only as `@AGENTS.md` on a line of its own;" becomes "`@path` appears only as `@AGENTS.md` alone on the first line of `CLAUDE.md`;", "a skill needed in Codex has a pointer in `AGENTS.md`." becomes "a skill needed in Codex has a pointer in `AGENTS.md` or a copy in `.agents/skills/`;", and add a last item "  - the Markdown files the root `AGENTS.md` or `CLAUDE.md` names pass the same checks."
12. §6 "In operation": "Judging in operation is three separate questions, each with a different cost:" becomes "Judging in operation is three separate questions, each with a different cost (WAY-131):".
13. §7 "When to add a rule", first bullet: the sentence "The threshold of \"twice\" is a convention, not a\n  measurement — the size of an insertion follows how often the mistake happens: for one occurrence\n  the smallest possible, for none a decision first whether to add anything at all." is **replaced** by "A rule enters only for a mistake found more than once in records of the work; a mistake seen once is watched, not ruled (WAY-130)." (R4); and the bullet "- **Every rule has a named mistake that it removes.**" gains "(WAY-130)" after its bold text.
14. `## Sources` is replaced whole by the text below. For each study the description is checked against the abstract at its address and keeps only what the abstract or the cited fact states; the version of arXiv:2606.15828 is the one its abstract page shows when read (`https://arxiv.org/abs/2606.15828`), written as `…/abs/2606.15828v<that version>`; the facts named are those 1.2 wrote (drop one 1.2 did not write):
```markdown
## Sources

Tool behaviour rests on an environment fact of the-way where one exists, named by its identifier;
the fact's entry in `foundations/environment_facts.md` holds the passage and its address.
Otherwise it rests on the tool's documentation, by address. What was measured is described in
`tool_loading.md`, where each measurement stands.

- Environment facts of tool behaviour: `claude-code-imports`, `claude-code-agents-md`,
  `claude-code-path-rules`, `claude-code-project-skills`, `codex-agents-md`,
  `codex-repository-skills`, `cursor-agents-md`.
- Tool documentation: https://code.claude.com/docs/en/memory, https://code.claude.com/docs/en/skills,
  https://code.claude.com/docs/en/hooks, https://code.claude.com/docs/en/best-practices,
  https://learn.chatgpt.com/docs/agent-configuration/agents-md,
  https://learn.chatgpt.com/docs/build-skills, https://learn.chatgpt.com/guides/best-practices,
  https://cursor.com/docs/rules, https://cursor.com/docs/skills.
- Studies:
  - https://arxiv.org/abs/2602.11988v3 — context files raise the cost of a task by over 20% on
    average, their instructions are followed, and repository overviews in them do not help (fact
    `context-file-effect`);
  - https://arxiv.org/abs/2605.10039v1 — a single rule given in `CLAUDE.md` is followed in about two
    thirds of the generated functions and in none without it (fact `single-rule-compliance`);
  - https://arxiv.org/abs/2507.11538v1 — accuracy falls as the number of instructions grows (fact
    `instruction-density-accuracy`);
  - https://arxiv.org/abs/2602.07150v3 — identical runs of one agent configuration differ by
    several percentage points (fact `agent-run-variance`);
  - https://arxiv.org/abs/2511.12884v2 — instruction files grow by frequent small additions, while
    deletions are negligible;
  - https://arxiv.org/abs/2606.15828v<version> — six typical defects of instruction files, found in
    91 of 100 popular files.
```
(The prototype's "Read on 2026-10-07 …" lines and its "Measured: …" paragraph leave this file; the measurements are described in `tool_loading.md`, Task 8. No date of the research, no pointer to `.runs/` or to private notes.)

- [ ] **Step 2: Check**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && grep -c "(WAY-1[23][0-9]" instruction-files/principles.md; grep -n -e "for one occurrence" -e "skill/" -e "Read on 20" -e "Measured:" -e "<version>" instruction-files/principles.md; echo "stale text $?"; for id in $(grep -o '`[a-z0-9]*-[a-z0-9-]*`' instruction-files/principles.md | tr -d '`' | sort -u); do grep -q "^## $id/" foundations/environment_facts.md && echo "fact $id"; done
```
Expected: at least 12 lines citing a decision; no stale line, `stale text 1`; eleven `fact` lines — `agent-run-variance`, `claude-code-agents-md`, `claude-code-imports`, `claude-code-path-rules`, `claude-code-project-skills`, `codex-agents-md`, `codex-repository-skills`, `context-file-effect`, `cursor-agents-md`, `instruction-density-accuracy`, `single-rule-compliance` (fewer only for a fact 1.2 did not write). The check script is not run on `principles.md`: it is no instruction file, and its example paths (`x/AGENTS.md`, `.claude/rules/`) would read as dead.

- [ ] **Step 3: Commit**

```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && S="Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" && git commit -m "docs(instruction-files): Name the decisions behind the principles, keep one threshold for a rule, and cite reachable sources" -m "$S" -- instruction-files/principles.md
```

---

