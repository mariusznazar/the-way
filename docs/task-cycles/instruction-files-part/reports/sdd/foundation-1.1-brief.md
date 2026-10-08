#### 1.1 Glossary agent — `record-glossary-term`

**Files:** Modify `foundations/glossary.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\glossary\skill\SKILL.md` and (spec §5.0, §5.8, N1):
  - the term `repository instruction file`, drafted in spec §5.0 in WAY-96's form for a noun ("A repository instruction file is an instruction file for coding agents that a repository's git tracks as an `AGENTS.md` or a `CLAUDE.md`, or as a Markdown file its root `AGENTS.md` or `CLAUDE.md` names by its path in backticks."); *Avoid* and *Not* settled by the skill (the draft proposes for *Not*: a skill's `SKILL.md` or a generated entry point — "skill");
  - its uses on this branch do not exist yet: the agent lists the planned uses from the drafts of spec §5.5 (WAY-128–WAY-133, "the-way's repository instruction files") and §5.6 (the population of `instruction-file-imports`), and takes the definition from what they share (skill step 3); 1.5 re-reads the real uses;
  - the term is compared by hand with the identifiers `instruction-files` and `repository` (skill step 2; the guard's comparison is unchecked with `--base none`); a match is a question to the orchestrator, whose provisional answer is that the term stays and the orchestrator records the reading;
  - "instruction file" keeps its ordinary meaning in WAY-09 and needs no entry (spec §5.8); "check script", never "checker".
- [ ] **Step 2: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none > $R/reports/check_1_1_guard_glossary.txt 2>&1; echo "glossary $?"; grep -v "^unchecked" $R/reports/check_1_1_guard_glossary.txt
```
Expected (planner, with the §5.0 draft placed before `## result`): exit 0; `0 error(s), 1 warning(s), 5 unchecked`; the one warning is the known "no use outside the glossary".

