# Slice 6 task review — skill `maintain-coding-guidelines` and its entry points

Reviewer: task reviewer S6 (Claude Code subagent, claude-opus-5-5), read-only. BASE `faf43c9`,
HEAD `aaaab9d`, package `slice-6-review-package.diff` read whole. Line numbers are of
`product-guidelines/coding/SKILL.md` at `aaaab9d` unless named otherwise.

### Spec Compliance

- ✅ Spec compliant. Every item of brief and spec §6.1–§6.5 has its place: frontmatter (2–3) is
  spec §6.1's description word for word, a safe plain scalar (no `: `, no ` #`); where the-way lies,
  the `the-way-` prefix, no Superpowers method (WAY-125), WAY-195 pointed to without naming a source
  (18–24; grep for Mercato/Google/Sadowski/"false positive"/"false alarm" → none: WAY-27, C2);
  writes/never-writes table with `.runs/coding/` only (35–38); §6.5 as one sentence (32–33); §6.4
  (45–85); §6.3 incl. the trial run's fresh judge requested from the orchestrator (89–99); steps 0–5
  (101–258). README names `product-guidelines/coding/` in both lists (diff README 82–84, 89–91).
  The four files the brief lists are the four the diff touches.
- Rows against text: row 2 (185–188, 220–221); row 3 (179–193, 200–204); row 5 (211–212, 252–254);
  row 8 (164–175, 157–158, 238–240); row 14 (200–209); row 18 (116–117 + template 66–67); row 19
  (125–126, 191–193, added in `aaaab9d`); row 20 (131–133, 147); row 21 (137–156); row 22 (180–190);
  *To do* 2, 3, 4, 7 as the report's table gives them — each checked against the cited lines; the
  table is accurate. Rulings C5 (68–70), C10 (241–244, both weak points of WAY-206), C12 (61–63),
  C13 (182–183), C33 (53–55) carried.
- ✅ Entry points: both new files are the same blob `a4bdcd5`; `slice-6-entry-points-bytes.txt`
  records `equal` against `produce(discover(ROOT))`. Focused check I ran (read-only dry run):
  `python3 -B agent-instructions/skill_entry_points.py` → 32 `would change`, none naming
  `coding-guidelines`, 0 `would create`; `git status --short` clean. The two expected red tests are
  recorded by name (`slice-6-tests-agent-instructions.txt`, `slice-6-tests-gate.txt`, 1 failure
  each, nothing else); part-map guard exit 0; `git diff --check` exit 0.
- ⚠️ Cannot verify from diff: none beyond the expected S7–S10 staleness; the `installation` side
  (`SKILLS`, README table line 56) is S11's.

### The executor's six choices, judged against the frozen task

1. **Human picks which kinds the task audits** (181–182). WAY-201's text ("each kind of code it
   audits") leaves it open, and the styleguide skill lets the human say which user interface a task
   covers under WAY-183's "every user interface" — a direct precedent. Holds, but row 22 says "dla
   każdego rodzaju" and Q6 rejected leaving agents to "copy what they find" until a later decision;
   the skill gives this choice no recommendation and no cost (Minor 1). Not a ruling the human made:
   the orchestrator should record it as a provisional choice for the request.
2. **No trial run or no fresh judge → no split, stop** (173–174). The only reading consistent with
   Q14 (both alternatives — all rules block, human rule by rule — rejected) and WAY-204; mirrors
   WAY-211/WAY-120's "no critic, no research". Holds.
3. **Missing part for code → question + `update-part-map` in *To do*** (117–119, 69–70). The
   styleguide skill's way (styleguide SKILL 105–108); needed because *Applies to* must name parts
   the map holds. Holds.
4. **Modes combine** (124). Needed: a kind file needs the general file (WAY-167). Holds; one wording
   seam with step 3's preamble (Minor 2).
5. **Terms explained before use** (207–209). WAY-194, unlike WAY-174, has no such clause, but
   "plain words" to a human who is no developer (K2) cannot be met while naming "a linter" bare.
   Holds as a how; cited to the bullet's decisions, not claimed as their text.
6. **Trial-run output to `.runs/coding/`, verdicts beside, no file name** (169–172). Spec §6.2 fixes
   none. Holds; see Minor 3 for its orchestrated-mode seam.

### Restates no rule

Checked the executor's overlap evidence (`slice-6-weakest-overlap.txt`) against the text: the five
template runs are pointers or things put to the human; the decision runs are steps cited to the
decision that gives them, as the styleguide skill does with WAY-183–WAY-192. The rules of form
(headings, tables, *Status* list, test-case shape, pinned versions, record of a run) appear only
as pointers to the template's sections — "Writing the files", "Test cases of a rule", "The tools of
the standing checks", "What each section carries", item "Test cases of the standing checks" — all
of which exist (`product-guidelines/coding/template.md` 117, 196, 215, 244; `template.md` 94). The
two-ways sentence at 229–232 is the template's own instruction "the skill names in the task which
way the tool allows" (template, Linter 2), so it belongs here. Weakest-point finding confirmed.

### Strengths

- Faithful to the model's structure section by section, while adding exactly what the coding
  discipline needs (trial run, kinds, three standing checks, WAY-205/206 weak points) — styleguide
  SKILL 26–220 vs coding SKILL 26–258.
- The hand-back check of one decision per standing check (252–254) makes WAY-202's "not complete
  without" operable.
- Trial run's isolation and the judge's independence stated precisely (164–172), with "technically
  right or not" carried from WAY-203/204.
- Second commit `aaaab9d` closed row 19's gap found by the executor's own requirements table.

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

None.

#### Minor (Nice to Have)

1. **181–182 — the choice of kinds has no recommendation.** "the human settles which kinds the task
   audits" sits in step 3, outside step 4's "How to show", so an agent may ask an open question.
   Row 22 ("dla każdego rodzaju") and WAY-200 point to every kind; deferring one leaves agents
   copying what they find (Q6's rejected way). Fix: recommend auditing every kind the product holds
   files of, naming the cost of deferring one. Orchestrator: list choice 1 as provisional.
2. **162 vs 128, 191 — step 3 opens "Where the product has code:", yet the "new kind" mode routes
   into it.** A product that has guidelines but no code yet (WAY-209's order) and a task creating its
   first endpoint is sent to "A new kind" behind a preamble that excludes it. Fix: scope the
   preamble to the trial run and the audit of kinds, or move "A new kind" out of it.
3. **98 vs `project-level/task/skill/SKILL.md:36` — orchestrated mode widens refine-task's write
   rule.** refine-task's orchestrated mode says "Edit only your task document and your conversation
   turn"; the skill adds "the trial run's output under `.runs/coding/`", while line 32 says neither
   `refine-task` nor the cycle changes for it. An agent meets two opposite rules. Fix: in
   orchestrated mode request the trial run itself from the orchestrator, as the research and the
   judge already are, or state the exception as refine-task's borrowed-skill output.
4. **56 vs 213–219, 76 — *To do* installs each tool "at the version … the task settles", but step 4
   and *Questions to settle* settle no version** (linter: tool, set, edition; formatter: tool,
   configuration; audit: tool, database, severity). The trial run's split is evidence at the version
   run (165); a cycle that installs another version may lose it. Spec §6.2/§6.4 have the same gap.
   Fix: add each tool's version (the one tried, or the product's pinned one) to step 4 and to
   *Questions to settle*, or drop "at the version" from *To do*.
5. **164–175 vs 213 — no rerun when the human picks a tool or set other than the one tried.** If in
   step 4 the human prefers another linter than step 2's proposal, the split has no trial behind it,
   which WAY-204 requires for a product with code. Fix: one clause — a set chosen in step 4 that was
   not tried goes through the trial run before its split is proposed.
6. **38 — "or any other file git tracks"** (spec §6.1's wording) also forbids the task document where
   a product keeps its backlog in its repository (refine-task finds it through `## Backlog`), while
   the "Writes" cell orders it. Spec-mandated wording; fix: "… save the task document".
7. **167 — "installed only there, never into a file git tracks"**: in a scratch worktree installing
   the tool edits its tracked manifest and lockfile, so the clause can read as forbidding the trial
   itself. Fix: "never into the product's working tree".

No noise in the reported test output beyond the two expected, named failures. No trust-boundary
file touched (`product-guidelines/form_check.py`, `installation/install.py` absent from the diff);
no invariant's code covered, so no deliberate break was due.

### Assessment

**Task quality:** Approved

**Reasoning:** The skill carries every row and *To do* item the brief names, points to the
templates for every rule of form, and its entry points equal the generator's output. The seven
Minor items are wording seams an agent could trip on: two orchestrated-mode or mode-routing
conflicts, the tool version, and a rerun of the trial. None leaves a row uncarried.

Verdict lines:
- Spec compliance: ✅ Spec compliant (no ⚠️ beyond the expected S7–S10 staleness)
- Issues: 0 Critical, 0 Important, 7 Minor
- Task quality: Approved
