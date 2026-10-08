#### 1.6 Invariants agent (sentence author) — `record-invariant`

**Files:** Modify `foundations/invariants.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\invariants\skill\SKILL.md` and:
  - **Fingerprint renewal** (WAY-31): `repository-file-location`, `element-directory-contents`, `relation-model-directory-contents`, `invariant-example-target`, `map-example-target`, `glossary-example-target` carry `WAY-09@<new fingerprint>`; `skill-entry-points` carries `WAY-127@<new fingerprint>`. Each sentence is read again against the new binding part and keeps its wording; versions stay `/1` (spec §5.3, §5.4).
  - **`instruction-file-imports/1`** and **`root-claude-md-import/1`, new**, as drafted in spec §5.6: *Method* `python -B gate/run_tests.py agent-instructions --record .runs/agent-instructions-tests.jsonl`; *Rests on* `none`; *Derives from* `WAY-129@<fp>` and `WAY-132@<fp>` (from 1.4 step 3); *Part* `every` and `agent-instructions`; *Correction* `none`. The draft of `instruction-file-imports` spells out the population that the term `repository instruction file` names; `way_of_working.md` step 2 asks for the term instead of a paraphrase (WAY-97). The orchestrator's provisional answer: the sentence uses the term where it names the same files, keeps "that git tracks" and the definition of an `@` that starts a word, and states nothing beyond WAY-129's first sentence (R6, N6); the agent reports the wording it chose. Tracked `SKILL.md` files stay out (A18).
  - Each sentence states every property its check will assert, with its literals, because the check's author receives the sentence and the method only (WAY-69).
  - After step 4.4 the agent returns the instruction for the checks (skill: "the entry, its method, and the checks citing an identifier this change retires or a version it raises" — none here) to the orchestrator.
- [ ] **Step 2: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none > $R/reports/check_1_6_guard_invariants.txt 2>&1; echo "invariants $?"; grep -v "^unchecked" $R/reports/check_1_6_guard_invariants.txt; python -B -I .runs/stale_refs.py > $R/reports/check_1_6_stale_refs.txt; echo "stale $?"; tail -1 $R/reports/check_1_6_stale_refs.txt; python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none 2>&1 | tail -1; python -B elements/glossary/format_guard.py --uses "repository instruction file" | tail -2
```
Expected: invariants `0`, `0 error(s), 0 warning(s)`, the note on `human_verdicts.md` (planner reproduced with a draft `instruction-file-imports`); stale `0`, `references checked 397, stale 0` (395 + the two new *Derives from*); decisions `0 error(s), 13 warning(s)`; the uses list names the decisions and, where 1.6 used the term, the invariant.


#### Orchestrator's addition (ruling Q15.2)

`instruction-file-imports` uses the glossary term instead of spelling out its files: its sentence
reads in the form "No repository instruction file of the-way holds, outside code spans and fenced code
blocks, …" (WAY-97). The term's definition says a Markdown file the root files name "by its path"
(no backticks): the sentence states, checkably, what counts as naming a path, so the check's author
can find the population from the sentence alone (WAY-69).
- Fingerprints from 1.4 (use these): WAY-09@e360ca30 (six renewals from 16b8026b), WAY-127@69651fc7
  (`skill-entry-points`, from 4439a64a), WAY-129@1336c32b (`instruction-file-imports`),
  WAY-132@1242ac75 (`root-claude-md-import`). Read WAY-129 and WAY-132 as written in
  `foundations/decisions.md` before writing: WAY-129's first sentence states the present state
  ("The-way's repository instruction files hold no `@` import other than the line `@AGENTS.md` alone
  at the top of the root `CLAUDE.md`…"); WAY-132 says a root `CLAUDE.md`, "where there is one", has
  `@AGENTS.md` alone as its first line. The invariants state nothing beyond them (R6, N6).
