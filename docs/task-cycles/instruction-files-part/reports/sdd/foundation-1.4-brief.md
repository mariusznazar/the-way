#### 1.4 Decisions agent — `record-decision`

**Files:** Modify `foundations/decisions.md` only.

- [ ] **Step 1: Check the numbers against the `foundations` tip (O4)**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && git fetch -q origin && git rev-parse origin/foundations && MSYS_NO_PATHCONV=1 git show origin/foundations:foundations/decisions.md | grep -E "^### WAY-1(2[89]|3[0-9])/" ; echo "taken: $?"
```
Expected: the tip hash (`252152a8…` unless something merged since), no heading line and `taken: 1` — WAY-128–WAY-133 are free. A printed heading means renumber from the first free number; give the agent the new numbers, and every later task uses them.

- [ ] **Step 2: Dispatch** with `C:\Storage\repos\the-way-process\elements\decisions\skill\SKILL.md` and:
  - **WAY-09/1, edited in place [change of meaning — WAY-07; the request names it]** as spec §5.3: the first binding sentence's list gains `instruction-files/` after `agent-instructions/`; the second gains "`instruction-files/` the principles of instruction files for coding agents, the account of how the tools load them, the skill that applies them, and the script that checks instruction files with its tests;"; *Scope* gains `instruction-files`; *Verification* level 2 covers `instruction-files/` and *complies* gains "the principles, the loading account, the skill and the check script of instruction files stand together in `instruction-files/`"; *Rationale* and *Rejected* gain the clauses of §5.3 (no file, script or count named there — WAY-05); *Approved by* becomes `Mariusz, merge of <request link>` (it reads `… pull/8`); *Review when* stays `none`.
  - **WAY-127/1, narrowed in place (option A of spec §5.4) [change of meaning — question Q-M1]**: its third binding sentence becomes "No global link reaches a skill of the-way other than one to `instruction-files/`, whose skill, judging a repository that pins the-way, follows that repository's pinned copy instead, and the-way is not installed in itself."; *Scope* gains `instruction-files`; *Verification* gains the level-2 pair of §5.4 (complies: a global link leads to `instruction-files/` of a worktree kept at the merged tip, and the skill judging `loop2` follows `loop2`'s `.the-way/instruction-files/SKILL.md`; violates: a global link leads to another skill of the-way; the skill judges a product that pins the-way with the copy its global link reaches); *Rationale* gains §5.4's why; *Approved by* `Mariusz, merge of <request link>`; WAY-34 is not changed.
  - **WAY-128/1 – WAY-133/1, new** as drafted in spec §5.5 (questions, binding sentences, *Based on* with the fingerprints of 1.2 step 2 and `context-file-effect@c44e5ef0`, `claude-code-path-rules@ac99f128` as `<id>@<fingerprint>` joined by ` · `, *Relations* `derives from WAY-100@e7a74a18` only, *Verification*, *Review when* — check by 2027-01-08 on WAY-128 and WAY-133, a date the skill confirms (A15) —, *Origin* `none`, *Approved by* `Mariusz, merge of <request link>`, *Rationale*, *Rejected*); *Change* `new decision`; *Scope* `instruction-files, agent-instructions`. Every binding sentence says "the-way's repository instruction files" (the term of 1.1, WAY-97), never a paraphrase of its definition, and none of the principles' words "main file", "trigger", "way in", "route". WAY-130's *Based on* quotes arXiv:2511.12884v2 § 4.2 as WAY-80 gives a citation, after the agent reads the passage at `https://arxiv.org/html/2511.12884v2`; no fact for it (A13). If 1.2 took path 2 for a fact, the decision resting on it is reworded without that reason, as the orchestrator's answer to 1.2 says.
  - Entries the search reads whole, besides those the skill leads to: WAY-03, WAY-04, WAY-05, WAY-07, WAY-12, WAY-14, WAY-16, WAY-21, WAY-25, WAY-26, WAY-27, WAY-28, WAY-30, WAY-31, WAY-32, WAY-33, WAY-34, WAY-35, WAY-44, WAY-46, WAY-48, WAY-52, WAY-69, WAY-73, WAY-80, WAY-85, WAY-90, WAY-93, WAY-95, WAY-96, WAY-97, WAY-100, WAY-107, WAY-114, WAY-126.
  - After step 4.4 the agent lists, and does not write, what follows in other elements: the two invariants WAY-129 and WAY-132 name (1.6) and the seven entries carrying WAY-09's or WAY-127's fingerprint (1.6).
- [ ] **Step 3: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none > $R/reports/check_1_4_guard_decisions.txt 2>&1; echo "decisions $?"; grep -v "^unchecked" $R/reports/check_1_4_guard_decisions.txt; python -B -I .runs/stale_refs.py > $R/reports/check_1_4_stale_refs.txt; echo "stale $?"; cat $R/reports/check_1_4_stale_refs.txt; python -B -I .runs/stale_refs.py WAY-09 WAY-127 WAY-128 WAY-129 WAY-130 WAY-131 WAY-132 WAY-133; python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none 2>&1 | tail -1; python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none 2>&1 | tail -1
```
Expected: decisions `0`, `0 error(s), 13 warning(s)` — the five baseline overdue reviews (WAY-03, WAY-21, WAY-52, WAY-55, WAY-69) and eight ``*Approved by* is the placeholder `merge of <request link>` `` (WAY-09, WAY-127, WAY-128–WAY-133; planner reproduced the wording); stale `1` with the seven known `STALE` lines and `references checked 395` (379 + 16: WAY-128 four, WAY-129 two, WAY-130 one, WAY-131 two, WAY-132 five, WAY-133 two — a different count only if 1.2 or 1.4 changed a *Based on*; `stale` always only the seven); eight fingerprints, none `NOT FOUND`, WAY-09 not `16b8026b`, WAY-127 not `4439a64a`; facts `0 error(s), 0 warning(s)`; glossary `0 error(s), 0 warning(s)`. The invariants guard is red until 1.6 (see the table above).


#### Orchestrator's addition (ruling Q14, from the part-map agent's search)

- Add `instruction-files` to the *Scope* of WAY-27, WAY-38, WAY-89 and WAY-120 (in-place edits before
  `main`; *Scope* is outside the binding part, so their fingerprints do not change; the request lists
  them). Do not add any other part to those fields.
- The part map now holds an External context row: `a repository or a user's files an agent's
  instructions are read from — instruction files, tool configuration, session records · them → us ·
  untrusted · no`.
- Ruling Q15.3 (glossary agent): WAY-128's *Rationale* must not say what the term is (WAY-95). Write,
  for skills and entry points: "Process skills and their entry points answer to their own decisions
  (WAY-35, WAY-127), not to this one." Where a decision means the glossary term, write the whole term
  "repository instruction file"; the bare words "instruction file" keep their ordinary meaning.
- The term as written (`foundations/glossary.md`): "A repository instruction file is an instruction
  file for coding agents that a repository's git tracks as an `AGENTS.md` or a `CLAUDE.md`, or as a
  Markdown file its root `AGENTS.md` or `CLAUDE.md` names by its path." ("in backticks" is not in it:
  the backtick form of a pointer is WAY-129's rule.)
- Facts as written in 1.2 (fingerprints): `claude-code-imports@5b9359fd`, `claude-code-agents-md@e4007cb8`,
  `codex-agents-md@6dc13475`, `cursor-agents-md@aaa19b03`, `single-rule-compliance@cf537693`,
  `agent-run-variance@538af710`; existing `context-file-effect@c44e5ef0`, `claude-code-path-rules@ac99f128`.
  Read each entry in `foundations/environment_facts.md` before citing it: the sentences follow the
  pages, not the spec's drafts (e.g. `single-rule-compliance` now states no compliance rate — see
  ruling Q17 below; `claude-code-imports` also says imports in code spans and fenced blocks are skipped — what
  WAY-129's backtick form rests on).
- Facts agent's findings for your wording: Claude Code prints "no CLAUDE.md found; AGENTS.md loaded" in
  interactive sessions when it reads `AGENTS.md` directly, so WAY-132 *Rejected* "without a sign" must
  say what is true (the line silently stops appearing); the same Claude Code page recommends "target
  under 200 lines per CLAUDE.md file" — WAY-128 *Rejected* "a fixed count of lines" must stay true
  beside that vendor advice.
- Ruling Q17: `single-rule-compliance/1` was re-sourced to the arXiv abstract alone; its fingerprint is
  `cf537693` (not 2aac5731). It states no compliance percentage: it says none of four structural
  variables (file size, instruction position, file architecture, contradictions in adjacent files)
  produced a detectable contrast, and compliance falls by about 5.6% in odds per additional function
  within a session. WAY-133 cites it for "a loaded rule is not always followed"; quote no percentage
  other than what the entry holds.
