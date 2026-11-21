PASS 429cade12c23fb9053fec841094258b6fde4ffda

# Review of correction 1 — and the reading of four decisions whole

Reviewer: fresh; did not make the change and wrote no earlier review. Head confirmed:
`git rev-parse HEAD` = `429cade12c23fb9053fec841094258b6fde4ffda`. Ranges: the whole change
`19e5774aed6d1d628042e23deccc110ed9f112c0..429cade1` (part 1 of the handoff); the correction
`48e64f104b2a4f656f4be4606c98c0959ffa975e..429cade1`, one commit (part 2).

Counts: 0 blocking, 4 Minor (one of them out of the diff, see M4), 0 out of scope.

## Findings

### Critical

None.

### Important

None.

### Minor

**M1 — `gate/test_skills_reach_the_way_sessions.py:228-234` and `AGENTS.md:19-24`: "the line of
another skill" names less than the check reports, and both openings frame causes that are no
entry point.** The check builds `listed` from every skill (`problems`, line 182) and
`entry_problems` (lines 151-157) reports a missing line for each of them, the entry point's own
skill included; the invariant says "lists every such skill". "Another" leaves out the own line.
Both openings — "a skill of the-way whose entry points break the invariant" (message) and "each
way an entry point breaks the invariant" (`AGENTS.md`) — then list a skill file that cannot be
read and an orphan directory `the-way-*`, which are not an entry point that breaks. Why it
matters little: the lines under the message name each problem exactly, and every cause of
`problems` and `entry_problems` is in both lists (matched one by one below, under Remark 3), so
remark 3's "every cause" is met in substance. Fix, if wanted: "the line of a skill of the-way"
and "each way the invariant breaks".

**M2 — `foundations/part_map.md:170-173`: the Codex clause rests on no source a reader of the
foundation reaches, names the field only as "the field", and makes the next clause read
ambiguously.** The sentence now reads "…which Claude Code keeps from the model because of the
field in their header while Codex ignores that field and the skills stay visible to the model
there, and the script that generates them, for the copies…": "and the script that generates
them" now follows "the skills stay visible … there" and can be read as continuing the Codex
clause. The Codex statement is the one hand check of remark 1 (codex-cli 0.163.0), which the
human asked to have written here; nothing flags this sentence when Codex begins to honour the
field. WAY-90 does not bind it: its rule is for the citations of a decision's *Based on*, and no
decision rests on Codex's behaviour with the field (WAY-127 states the hiding as Claude Code's
only). On the author's concern (author report, "Questions and concerns"): by WAY-90 no fact entry
is due while no decision rests on the reading. Were WAY-127 later to name that price in its
*Rationale*, the reading would become a citation of it; the comment stands at a public address
(the repository `mariusznazar/the-way` is public, `gh repo view … visibility` → `PUBLIC`), so by
WAY-90's last complies/violates pair it is "a citation like any other" and would become a fact
entry, not prose marked as the product's own measurement.

**M3 — WAY-256 and WAY-35 against the hand-over paragraph of the 15 skills (whole change; most
pronounced at `project-level/lead/skill/SKILL.md:20-27`).** The change rewords one paragraph in
15 `SKILL.md` files, so WAY-256 binds it ("one a change to a skill of the-way adds or rewords").
Its the-way-itself half is a fragment only one variant needs (a session on the-way itself; a
product's session reads it and does not use it) of about 80 words. WAY-256 keeps such a fragment
in `SKILL.md` only where it is "one instruction"; six of the 15 are element skills
(`elements/common/skill/SKILL.md`, `elements/decisions/skill/SKILL.md`,
`elements/environment-facts/skill/SKILL.md`, `elements/glossary/skill/SKILL.md`,
`elements/invariants/skill/SKILL.md`, `elements/part-map/skill/SKILL.md`), for which WAY-256
defers to WAY-35: "the way of working the skills share stands once in that part, and a skill
reads … from there instead of restating them". My judgment, and why it does not block:
(a) in 14 of the 15 the fragment reads as one instruction — read the named skill's `SKILL.md`,
located by the entry point's list or a search, and follow it — which WAY-256 lets stand where its
pointer would; (b) WAY-127, which derives from WAY-256 and which this change writes, requires the
hand-over in each skill's paragraph by its *Verification*: "a skill's paragraph names … another
the-way skill it hands to as the file `SKILL.md` read from that checkout or worktree for the-way
itself and as the project skill with the `the-way-` prefix for a product" — the more specific
decision governs these paragraphs, and the per-skill paragraph predates the change. What remains:
`project-level/lead/skill/SKILL.md:20-27` adds a second instruction to the the-way-itself half
("give the brief of an agent you dispatch for such a skill the path of that file, so that no
personal skill of the same name stands in"), which is WAY-256's violating case "a step keeps
several instructions only one variant needs in `SKILL.md` because each of them is short" in
miniature (two against one pointer). The consequence is small: about 90 words read and unused in
every product use of `lead-project`. For the next task of the queue, which changes skill files
again: the tension between WAY-127's *Verification* (a paragraph in each skill) and WAY-35 (a
shared way of working stands once in `elements/common/`) is in the foundation itself, and a change
that rewords this paragraph again meets it; settling it once — the procedure in one shared file,
each skill keeping one sentence — would also shorten 15 copies that must change together.

**M4 — WAY-131 against the request's description, outside the diff.** WAY-131 binds "the request
of a change to the-way's repository instruction files" where it says whether a rule works. The
description of https://github.com/mariusznazar/the-way/pull/154 ("What you will see") says: "In a
session on the-way, when one skill tells the session to use another skill of the-way, the session
now opens that skill's file in its own checkout and follows it, instead of calling the skill." That
states that agents follow the hand-over rule (WAY-131's second question). No session settled it:
the probe sessions of the review of the whole change (`reports/review-whole-probe-evidence.txt`)
settled loading — the hiding, with a control that has to load (the product stand-in
`the-way-critique` and the nested `the-way-control-probe`), which complies with WAY-131's first
question — not following. The rule's behaviour is one that hardly happens without it, so by
WAY-131's complies case a few sessions with and without would settle it. The text lies in the
request, which the orchestrator writes, not in the range; it is no defect of the code. Fix, if
wanted: "the skill tells the session to open … instead of calling it", or a few sessions.

## Remarks of correction 1 (`reports/correction-1-remarks.md`)

- **Remark 1 — made (by the author's part), the record is the orchestrator's.** No code change was
  asked. I checked that no text of the change says, without the Claude Code qualification, that
  the model is offered no skill of the-way: a search outside `.runs/`, `.claude/`, `.agents/` for
  "hidden from the model|offered to the model|offers the model|visible to the model" finds only the
  new part-map sentence (the other occurrences break across lines and were read in place: WAY-127
  "so that Claude Code offers the model no skill", the test's docstring "by Claude Code", the
  generator's docstring "in Claude Code", `README.md` "a Claude Code session does not call",
  `AGENTS.md` "which in Claude Code keeps the model"). The generated entry points say "do not call
  it, since Claude Code does not offer the entry points of the-way's skills to the model"
  (`.agents/skills/the-way-critique/SKILL.md:17`); in Codex, where the model sees them, the
  instruction not to call still holds and the reason given is true of Claude Code — no conflict.
- **Remark 2 — made by this review** (section *Unread material* and the judgment below).
- **Remark 3 — made.**
  - Part map: `foundations/part_map.md:170-172` says Claude Code keeps the entry points from the
    model because of the field and that Codex ignores the field and the skills stay visible to the
    model there. Wording notes in M2.
  - The causes, matched against the code:
    `problems` — cannot be read (line 171) → "a skill file that cannot be read"; no name (176) and
    no description (179) → "has no name or description"; no file in a copy (189) → "an entry point
    that is missing"; not byte-identical (194) → "a pair that differs in bytes"; orphan directory
    (212-214) → "a directory `the-way-*` that no skill produces".
    `entry_problems` — no frontmatter (133) → "no frontmatter"; name (135) → "whose header does not
    name the skill"; description (139) → "does not start with its description"; the field (143) →
    "lacks `disable-model-invocation: true`" / "lacks the field" (`AGENTS.md` names the field
    earlier in the same paragraph); path of the skill (145) → "whose text lacks the path of its
    skill"; `REQUIRED_WORDS` (147-149: three git commands, the skip sentence, "do not call it",
    "read that skill's `SKILL.md`") → "a command or sentence the invariant requires"; the list
    (151-157) → "the line of another skill" (see M1). No cause is left out of either text. The
    control assertion (`assertIn` of `CONTROL`, lines 222-223) fails with its own message and is no
    cause of `found`; leaving it out is right.
  - The diff of the test file is its docstring and that message alone: no assertion, constant or
    helper changed (`git diff 48e64f10..429cade1 -- gate/test_skills_reach_the_way_sessions.py`).
    No invariant test changed in what it asserts in this correction.

New defect introduced by the correction: none Critical or Important; M1 and M2 are Minor.

## The four decisions read whole, and the whole change judged against them (remark 2)

- **WAY-44 — what assigns a file to a part.** Complies. The change adds no file; the 46 entry
  points are generated and stand in the part of their generator, `agent-instructions`
  (`foundations/part_map.md:182-184`: `.claude/skills/**`, `.agents/skills/**`), as WAY-44's
  "generated files to the part of their generator" and WAY-127's *Rationale* say;
  `foundation_check.py` reports 0 errors (no file unassigned, none claimed twice, no pattern that
  matches nothing). Its last clause — for a file that collects entries about many parts, the parts
  a change touches follow from the entries it changes — is kept: WAY-127's *Scope* gained
  `foundation-review` and `product-guidelines`, the parts whose skill files the change now governs.
  The part-map sentence changed is the description of a part, which WAY-44 does not regulate.
- **WAY-256 — where a fragment of a skill stands.** No breach that blocks; see M3 (the
  the-way-itself half of the hand-over paragraph in 15 skills, the second instruction in
  `lead-project`, and the tension with WAY-35 for the element skills that the next task will meet).
  The entry point text has the skill and each named file read when its step comes, not at the
  start, which complies with WAY-256 and WAY-127's first complies case.
- **WAY-90 — which citations become environment fact entries.** Complies for what the change
  writes: the new fact `claude-code-skill-model-hiding` (`foundations/environment_facts.md:156-160`)
  is a behaviour of a tool the process uses whose change would call WAY-127 into question; WAY-127's
  *Based on* names it by its identifier alone; its source gives the address, an archive, the place
  (two sections, the table row and columns) and the passages word for word, and the date read
  (2026-11-21). WAY-127's *Rationale* cites no measurement of the product's own people. The Codex
  reading of remark 1 stands in the part map, not in a decision; WAY-90 does not reach it (M2).
- **WAY-131 — how it is settled whether a rule of an instruction file works.** The files of the
  change state no claim that a rule works. The request's description does (M4): the loading of the
  hiding was settled by sessions with controls, as WAY-131 asks; the following of the hand-over
  rule is stated without sessions. Remark 1's Codex check is one session showing all 23 skills
  listed — a positive result, which needs no control file.

## Declined to judge

- WAY-127 saying nothing of Codex's behaviour with the field (its *Rationale* names only Claude
  Code's price): the remarks ask for the part map only, and the author's report raises it; whether
  the decision should carry it is the human's call, not a defect of the correction. Its
  consequence for WAY-90 is in M2.
- The text of the generated entry points read in Codex ("since Claude Code does not offer …"): true
  of Claude Code, harmless in Codex; not a remark of this correction.

## Checks (command → exit code)

- `git rev-parse HEAD` → `429cade12c23fb9053fec841094258b6fde4ffda` (matches the handoff's head).
- `python -B agent-instructions/skill_entry_points.py` (no `--write`) → 0, "entry points are
  current".
- `python -B gate/run_tests.py gate` → 0, 36 tests OK.
- `python -B gate/run_tests.py agent-instructions` → 0, 53 tests OK.
- `python -B elements/common/foundation_check.py` → 0, "0 errors".
- `git status --short` after the runs → empty (the reviewed worktree unchanged).
- Manual: the causes of the message and of `AGENTS.md` matched line by line against `problems` and
  `entry_problems` (above); a search for unqualified hiding claims (above); the generator's diff
  and one generated entry point read.
- Not run: the whole gate (the handoff forbids it); a mutation run of the test (the correction
  changed no assertion, so no behaviour of the test needed it).

## Reaches beyond the dispatch

- WAY-35 (`foundations/decisions.md`, heading "WAY-35 — What does an element's skill hold?"), read
  whole: WAY-256 defers to it for a way of working the element skills share, which M3 needed.
- WAY-127 (`foundations/decisions.md:3329-3421`), read whole: the decision the change writes, whose
  *Verification* governs the paragraphs judged in M3.
- The description of https://github.com/mariusznazar/the-way/pull/154 (`gh pr view 154`), read for
  what it says about rules working (WAY-131, M4), and `gh repo view … visibility` for WAY-90 (M2).
- `reports/review-whole-probe-evidence.txt`, searched, to see what the probe sessions settled (M4).
- The first paragraph of "Working copies" in `reports/review-whole-handoff.md`, as the handoff binds.

## Working copies

None made; `.runs/review-correction-1/` was not created. The tests' own temporary repository is
the test's fixture and is removed by it.

## Unread material

- Read whole: WAY-44, WAY-256, WAY-90, WAY-131 (each from its heading to the next heading, with
  *Scope*, *Based on*, *Relations*, *Verification*, *Rationale*, *Rejected*); also WAY-35 and
  WAY-127 whole (reaches above).
- `fix.md` and `SKILL.md` of `task-cycle/review/` read whole; the remarks file and the author's
  report read whole; the correction's diff read whole.
- Of the whole change: the diffs of `foundations/`, `AGENTS.md`, `README.md`, the generator and the
  test read; the hand-over paragraph of all 15 skills read in the diff (the skills themselves not
  read whole beyond that paragraph); of the 46 entry points, one read (`.agents/skills/the-way-critique/SKILL.md`, the head), the rest held
  current by the generator check. `agent-instructions/test_skill_entry_points.py` not read (covered
  by its passing run, unchanged by the correction).
- The PR description read in the parts that bear on the remarks (English part); the Polish part
  not read.
- The record's other reports (`review-whole-report.md`, `review-fix-report.md`, the findings file)
  not read, by choice, to keep the judgment unanchored.

## Searches not found or unclear

- A source in the repository for Codex's behaviour with `disable-model-invocation`: none found
  (the part-map sentence is the only place); matches the author's own finding.
- Whether running a skill in the-way itself versus a product counts as a "variant" in WAY-256's
  sense: the decision's examples speak of modes and steps, not of where the skill runs; I read it
  as a variant (M3). Unclear in the foundation.
- A plain-text grep for the hiding wording misses sentences broken across lines; the hits were
  completed by reading the places named in the author's report.
