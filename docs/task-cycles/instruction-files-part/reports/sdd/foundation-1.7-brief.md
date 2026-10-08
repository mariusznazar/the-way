#### 1.7 Part-map agent — `update-part-map`

**Files:** Modify `foundations/part_map.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\part-map\skill\SKILL.md` and (spec §5.1, task point 8, run brief): `agent-instructions` *Depends on* gains `instruction-files` (its entry points read the skill); the critical flow `skills-reach-the-way-sessions` *Parts* gains `instruction-files`. The search also answers whether `instruction-files` needs a new failure mode now that the flow runs through it, and returns the finding.
- [ ] **Step 2: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && git add foundations/part_map.md && python -B elements/part-map/format_guard.py foundations/part_map.md --base none > $R/reports/check_1_7_guard_part_map.txt 2>&1; echo "part-map $?"; grep -v "^unchecked" $R/reports/check_1_7_guard_part_map.txt; grep -n -A2 "^- \*\*Parts:\*\* agent-instructions" foundations/part_map.md
```
Expected: `0`, `0 error(s), 0 warning(s)`; the flow's *Parts* line names `instruction-files`.


#### Orchestrator's addition (ruling Q21.2, from the invariants agent)

Also add to `agent-instructions` the failure mode the two new invariants detect, in the map's form,
e.g.: "the root `CLAUDE.md` stops opening with `@AGENTS.md`, or a repository instruction file of the-way
gains an `@` import — Claude Code sessions on the-way lose the shared instructions, or load a whole file
into every session — high — detected by root-claude-md-import · instruction-file-imports" (word it by
the skill and template; the identifiers are as written in `foundations/invariants.md`).
