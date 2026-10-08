# Independent assessment (WAY-10) — c64a607..76c3f3c

Assessor: general-purpose subagent, sonnet (the assessed entries and invariant test were written by opus agents; the
first attempt on claude-fable-5-1 failed on that model's weekly limit, API 429, request req_011Cfp4itoku2gKV9JTEqB5X).
Skill: `elements/common/critique/SKILL.md` at the process root c64a607. Material: `git archive 76c3f3c` and
`git diff c64a607..76c3f3c` in the session scratchpad; no task, spec, plan, record, reports or commit messages.
Assessed files: the 47 files of `git diff --name-only c64a607..76c3f3c` (foundation entries, the gate test, the four
watches, the generator and its test, the 22 entry points, the nine skills and `way_of_working.md`, `AGENTS.md`,
`README.md`, the installer literal and its test). Report saved by the orchestrator from the returned text.

## Observations

1. Dead sentence pinned in the generator, the invariant and the test — should change. The 22 entry points say "If the
   skill tells you to resolve a link to find the-way, skip that: the root is the one above."; nothing in the commit tells
   anyone to resolve a link (the rewritten skills have no such paragraph); grep finds it only in the generator
   (`agent-instructions/skill_entry_points.py:178`), its test (`test_skill_entry_points.py:55`), the gate test
   (`gate/test_skills_reach_the_way_sessions.py:38`), the entry points and the invariant (`foundations/invariants.md:2033`).
   Remove it from the generator, the invariant and the gate test; WAY-127's "violates" clause already covers it.
2. Two environment facts each state several facts — should change. `claude-code-project-skills/1` joins four claims
   (parents up to the root, the worktree root, the v2.1.277 fallback, `/cd` from v2.1.246; `environment_facts.md:166`);
   `claude-code-nested-skills/1` joins three. Template: "One entry states one fact … with one reason to change"; the
   fingerprint covers the whole sentence; *Holds for* says "without versions" while the sentence names versions. Split.
3. `codex-skill-paths/1` has no real dependant — should change or cut. WAY-127 lists it in *Based on*
   (`decisions.md:3660-3661`) but nothing in its sentence, Verification or rationale uses it; the part map's failure mode
   says Codex "gives no file path for a skill it leaves out of its initial list", which is not what the fact says. The
   passage "This budget applies only to the initial skills list." could not be confirmed in context (the fetch
   paraphrased). Withdraw the fact, its watch and its *Based on*, or write the dependency into WAY-127.
4. The part-map failure mode asserts tool behaviour with no source and conflicts with the entry point's own check — should
   change. "names `${CLAUDE_SKILL_DIR}`" has no fact or *Source*; the failure mode says the agent does not know the entry
   point's path while check 1 (`git -C <the directory that holds this file> …`) needs it; check 2 carries the stop in
   practice; a session working inside `.the-way` uses the pinned copy anyway, so check 1 changes no outcome found. Drop
   check 1 or say what supplies the directory with a fact; remove or source the parenthetical.
5. The invariant test shows breaks for only part of the sentence — should change (WAY-08). The control test breaks a
   missing copy in each directory, a byte difference, an orphan, and a clean control; no test breaks the frontmatter
   name, description prefix, path in backticks, the four phrases, the sentence naming every skill, the prefix words. The
   generator's tracked-state test is a second check of the live state, not cited, no break. Add one fixture per property.
6. An unrelated change of meaning to WAY-27 and `outbound-link-reach` rides along — should change (separate it, or justify
   it to the human). The exception has no tie to entry points; it adds a local Windows path to private notes in
   `AGENTS.md`; the invariant says "link" but the text is a path; the new violates line repeats "*Origin* points to a
   private note"; WAY-107 is about a product's backlog. Costs the human a second decision at the merge.
7. The sibling list in every entry point costs 22 rewritten files per added skill — minor. A generic prefix sentence would
   do; the installer wrapper does the same, so name it as a parity choice.
8. Vocabulary not in the glossary — minor. "Entry point" beside the term *entry*; "project skill" and "process root" used
   in binding and generated text, undefined (WAY-97).
9. WAY-09 text not fully updated — minor. The `agent-instructions/` clause still describes only "the instructions for
   agents"; the probe docstrings are a third copy of each fact sentence that can drift.
10. Unchecked: live-repository gate test and generator tracked-state test need git (absent in `tree\`); generator tests 13
    ran, 1 error (no git); `installation/test_install.py` 22 failures and 13 errors in `tree\` (cause not examined, not
    attributed); the part-map guard cannot check file ownership without git.

## No concern found

Fingerprints (WAY-127 4439a64a, WAY-09 16b8026b, WAY-27 fb27e458, facts d58fb91f, 4dd3d448, 7db28f98, 5b5b6c79 recompute
exactly; WAY-44@2f2b6227 unchanged); the six renewals complete; `generated-overview/1` *Part* justified; source fidelity
of the Claude Code passages and the Codex sentences checked (exact wording of "For repositories, Codex scans …"
unverified — the fetch summarised); generator, entry points and invariant agree (copies byte-identical, descriptions
291–499 characters); WAY-127 against WAY-34, WAY-44, WAY-09: no contradiction; form (decisions guard 0 errors, 8
warnings: placeholders and past check-by dates); part map follows the template apart from 4; rewritten skill paragraphs
agree with the decision.

## What can be cut

1. The "resolve a link" sentence (1). 2. `codex-skill-paths` with its watch and *Based on*, unless the dependency is
written (3). 3. The `${CLAUDE_SKILL_DIR}` parenthetical, and probably check 1 (4). 4. The WAY-27 exception, the
`outbound-link-reach` rewording, `## Backlog` and the repeated violates line, as a separate change (6). 5. The sibling
list, if a generic sentence will do (7). 6. The generator's tracked-state test, if the gate test stays the single live
check (minor). Everything else is needed: the generator, the 22 entry points, WAY-127, `skill-entry-points/1`, the gate
test, WAY-09's edit, the rewritten skill paragraphs.

## Settlement (orchestrator)

1. Rejected. The sentence guards a case that exists outside this commit: Claude Code ≥ 2.1.277 offers a worktree without
   `.claude/skills` the main checkout's entry points (`claude-code-project-skills/1`), and such a worktree's own branch
   still holds the old "Installed globally … resolve it first" paragraph; several worktrees of this repository stand on
   branches from before this change. After point 6 removes the junctions, that instruction resolves to nothing; the
   sentence tells the agent to skip it. Cost of keeping: one sentence per entry point.
2. Rejected. Every clause answers one question — from which `.claude/skills/` directories a Claude Code session takes its
   project skills — in one section of one page; WAY-127 rests on them together (start directory, worktree, fallback,
   `/cd` decide which copy is read), so a change of any clause rightly sends WAY-127 to review. *Holds for* follows the
   template's form for documentation of a tool that shows only its current release ("without versions"), as
   `claude-code-path-rules/1` does; the versions in the sentence are what the page says, not an edition. The nested
   fact's three clauses are one behaviour (how a nested skill becomes available). Cost if wrong: one fingerprint renewal
   touches more than needed.
3. Accepted in part. The fact stays: check 1 in Codex rests on it. WAY-127's *Rationale* gains the dependency (the entry
   point's own directory, which Codex lists with each skill, lets check 1 find a product's submodule). The part map's
   unsourced Codex clause goes with 4.
4. Accepted in part. The bracket in the failure mode is removed (neither `${CLAUDE_SKILL_DIR}` nor the Codex omission is
   recorded as a fact); the failure mode keeps its condition. Check 1 stays: it stops a session that works inside a
   product's `.the-way` (its working directory is the pinned checkout, check 2 finds no `.the-way` gitlink there, and the
   process root would be the pinned copy with the-way's own `foundations/`, not the product's).
5. Rejected. WAY-08's deliberate break was written from the sentence by the reviewer of the code (report 13): 13 breaks —
   frontmatter name, description start, source path, the skip line, `':/.the-way'`, the prefix words, a sibling removed,
   moved and split, a missing copy, a changed byte, an orphan, an untracked new skill — each failed the citing test and
   recorded `fail`. The committed control test is not the deliberate break. The tracked-state test is the generator's
   derived-file equality (WAY-53), not an invariant check.
6. Kept, partly changed. The exception is what task point 5 requires and is the request's question 2 to Mariusz (WAY-07,
   WAY-30); its tie is the task, not the entry points. A filesystem path to a note is a link in the invariant's sense.
   The repeated violates example is removed from WAY-27's *Verification*.
7. Rejected. Naming the skills is the design's choice (spec §4.2): an unprefixed name could be the-way's or a personal
   skill (`critique`, `refine-task` from vox-ai-tools); the list lets the model tell which are the-way's. Regeneration is
   one command and the gate reports a stale list.
8. Rejected. "Entry point" is a fixed compound, not a use of *entry* (precedent: "readiness gate" beside *gate* in WAY-118;
   report 08); "project skill" is the tools' own term (both pages); "process root" is pre-existing installer wording.
   No word is used in two meanings (WAY-97).
9. Rejected. WAY-09's sentence on what `agent-instructions/` holds sets a minimum before `main`, not a full list (report
   08, finding 1); the docstrings follow the watch model (`claude-code-path-rules`) and are not binding.
10. Noted: the unchecked items are named in the request; the installation failures in `tree\` come from the absence of git
    there (the same suite passes 17/17 in the worktree, Verification).
