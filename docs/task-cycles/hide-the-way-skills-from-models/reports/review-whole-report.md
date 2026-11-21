PASS 7d063ef278748884de28577f582b2ab0767d068d

# Review of the whole change — hide the entry points of the-way's skills from the model

Range `19e5774aed6d1d628042e23deccc110ed9f112c0..7d063ef278748884de28577f582b2ab0767d068d`, three
commits (`f9cae3a6`, `f3188faa`, `7d063ef2`); `git rev-parse HEAD` in the worktree gave
`7d063ef278748884de28577f582b2ab0767d068d`, the head of the handoff. One-author route, no plan, no
slices: no blocking finding, so no slice attribution is due.

## Findings

### Critical

none

### Important

none

### Minor (all within the task unless said otherwise)

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

### Out of scope

none beyond the note in Minor 6 that its gap is older than the change.

## Declined to judge

- Whether Codex reads or ignores `disable-model-invocation` and still loads the `.agents/skills`
  copies: the cycle did not settle it (handoff), nothing was run on Codex.
- The effect in loop2 (58 instead of 81 skills at a subagent's start): the task's *Out of scope*.
- Whether a citation of Claude Code's settings behaviour in WAY-127's new *Rejected* ("a product's
  project settings match a skill by its name alone") should be an environment fact by WAY-90: it
  supports a rejected way, the task's row 2 asks for one fact only, and the passage is faithful to
  the task's *Not chosen*.

## The orchestrator's points

**The clause "each entry point giving the path of every skill" (WAY-127) and "lists every such skill
... with the path of its `SKILL.md`" (invariant).** No contradiction with the settlements. Row 1 says
"skill przekazuje pracę innemu przez jego plik czytany po ścieżce", and *To do* 2 says "czytając jego
`SKILL.md` po ścieżce w checkoucie albo worktree". The list is the means that puts the path in front
of the session. No *Not chosen* rejects a list, and the list is generated, not kept by hand, so
WAY-127's "keeps no list of skills by hand" stands. It is no finding. Its only consequence is Minor 3.

**Acceptance criterion 1 (checked once in a real session).** The author's report rests on the model's
own answer in a probe with one hand-made hidden skill. The author did not cite the transcript, but it
is still on disk (`~/.claude/projects/<worktree-key>--runs-author-probe/f11feccc-....jsonl`). I read
it: after the read of `sub/file.txt`, the `dynamic_skill` attachment names only
`the-way-shown-probe` and the `skill_listing` delta has `skillCount: 1`. That is stronger than the
reply, but it is still not the "wygenerowane wejścia the way" that the criterion names.

I ran the check the criterion asks for (Probe A, evidence in `reports/review-whole-probe-evidence.txt`):
- Claude Code 2.1.330, model haiku, a repository whose `.the-way` is a real git submodule (gitlink
  `160000`) holding the 23 generated entry points of `7d063ef2`, a root product stand-in
  `.claude/skills/the-way-critique` without the field, and a nested control without the field.
- After the read of `.the-way/file.txt`, `dynamic_skill` loaded only `the-way-control-probe`.
- None of the 23 entry points reached the list, and the product's own `the-way-critique` of the same
  name stayed in the initial listing.
- The model named exactly those two.

Probe B, on the-way's own layout (entry points at the root): the initial listing held none of the 23,
and a hidden probe skill started by its command `/hidden-magic-probe` ran (reply `PINEAPPLE-42`). That
backs criterion 2's "dalej uruchamia ... poleceniem" by the same field.

The criterion is met for Claude Code 2.1.330 in `-p` mode. Still unchecked:
- loop2 itself and the skill list of a subagent started from such a session, which the task's
  *Context* names as the measure (out of scope);
- an interactive session;
- other releases of Claude Code;
- Codex.

**Codex.** See Minor 1 for every text of the change that claims something about Codex. The change
makes no other claim about Codex: `AGENTS.md` and `README.md` name `/the-way-<name>` for Claude Code
only.

**Texts that still tell a session of the-way to call a skill of the-way, and the product's
hand-over.** I searched for these:
- the phrases `the-way-` prefix, `project skill`, `prefixed`, `the-way-<name>`;
- every literal `the-way-<skill>` name;
- the verbs invoke / call / start / run with skill;
- the 23 skill names in backticks, in the unchanged skills (`task-cycle/*`, `process-audit/`,
  `instruction-files/`, `elements/common/critique/`, `elements/common/way_of_working.md`).

What I found:
- At the base, 15 skills, `AGENTS.md`, `README.md`, WAY-127 and the invariant carried the "project
  skill with the prefix" hand-over. All of them now carry the file hand-over for the-way itself.
- The unchanged task-cycle skills already reach methods by path (`task-cycle/skill/SKILL.md:71-75,
  253-256`).
- The remaining prefixed texts are all the product's: `installation/install.py:160-161, 195-197`,
  its tests, and `task-cycle/skill/request_template.md:470` ("the skill `the-way-review-foundation`,
  started in a session in this repository" of a product).
- The only text left that names a skill for a dispatched agent without a path is the one of Minor 4.

The product's hand-over: `installation/` is not in the diff. `install.py` keeps its own
`sibling_names` (`installation/install.py:124`), so removing the generator's `sibling_names` breaks no
import (`git grep` of `sibling_names|skill_entry_points|skill_list`). The 15 paragraphs keep "In a
product, it is the project skill ... with the `the-way-` prefix".

## Against the task

- *To do* 1: all 46 entry points hold `disable-model-invocation: true` in their header; both copies
  are byte-identical (gate test, generator check "entry points are current").
- *To do* 2: entry points and the 15 skills hand over by file in the-way, and by the prefixed project
  skill in a product.
- *To do* 3: `AGENTS.md` `## Skills` says that a human starts the skills with `/the-way-<name>` and
  that a skill hands over through the file.
- Row 1 → WAY-127's second paragraph, *Rationale*, *Rejected* (from the two *Not chosen* lists, the
  unchecked-entry-points way already present), *Verification*; and the invariant.
- Row 2 → `claude-code-skill-model-hiding`, in WAY-127's *Based on*. I checked its quotes against the
  live page (WebFetch, 2026-11-21): the sentence "Hide individual skills ... entirely." and the table
  row "Yes · Not on its own · Description not in context, full skill loads when invoked" match.
- Part map: the `agent-instructions` sentence no longer says the entry points make skills visible.
- No reserved choice. No trust boundary is touched; the changed files lie on no pattern of a
  *Trust boundary*.
- Changed invariant test: `gate/test_skills_reach_the_way_sessions.py` (invariant
  `skill-entry-points`). The change to its expected values, the removal of `PREFIX_WORDS`/`sentences`
  and the count 5 → 7, follows the requirement (row 1) and comes with the failing run in
  `reports/author-invariant-test-failing-run.txt`.
- Tests fail when the behaviour breaks: the new e2e case `epsilon` fails without the field, `zeta`
  without a line of the list; the generator test pins the whole text. Nothing in the code exists only
  to pass a test.
- The author's report says the failing invariant run had "46 lines"; the file holds 23 problem lines
  plus the message, since the test checks byte-identical copies once. The claim is inaccurate, the
  evidence holds.

## The structure the change leaves

`python -B task-cycle/change_file_sizes.py 19e5774a... 7d063ef2` → 0. Lines of the changed files
(before → after):
- 46 entry points, each 15 → 40;
- `AGENTS.md` 35 → 38; `README.md` 242 → 246;
- `agent-instructions/skill_entry_points.py` 282 → 287;
  `agent-instructions/test_skill_entry_points.py` 411 → 433;
- `elements/common/skill/SKILL.md` 64 → 67; `elements/decisions/skill/SKILL.md` 65 → 68;
  `elements/environment-facts/skill/SKILL.md` 53 → 56; `elements/glossary/skill/SKILL.md` 50 → 53;
  `elements/invariants/skill/SKILL.md` 63 → 66; `elements/part-map/skill/SKILL.md` 70 → 73;
- `foundation-review/SKILL.md` 117 → 121;
- `foundations/decisions.md` 11689 → 11715; `foundations/environment_facts.md` 341 → 347;
  `foundations/invariants.md` 569 → 569; `foundations/part_map.md` 298 → 298;
- `gate/test_skills_reach_the_way_sessions.py` 316 → 335;
- `product-guidelines/coding/SKILL.md` 159 → 163; `product-guidelines/styleguide/SKILL.md`
  106 → 110; `product-guidelines/testing/SKILL.md` 132 → 136;
- `project-level/lead/skill/SKILL.md` 204 → 207; `project-level/plan/skill/SKILL.md` 81 → 84;
  `project-level/skill/SKILL.md` 78 → 81; `project-level/task/skill/SKILL.md` 65 → 69;
  `project-level/technology/SKILL.md` 69 → 72.

In all, 70 files, +1285 lines.

The size invariant `function-and-file-size` (`agent-instructions/test_size_invariant.py`) passes on
the head within the `agent-instructions` run. `skill_entry_points.py` (287 lines) and
`entry_point_text` (about 50 lines) are far below WAY-385's thresholds. I made no base run: nothing is
over a threshold on the head, so nothing was pushed over. `sibling_names` was replaced by `skill_list`
and no code is left without a user. Names that stopped being true: Minor 5.

## Checks

- `git rev-parse HEAD` → `7d063ef2...`, matches.
- `python -B gate/run_tests.py agent-instructions` → 0 (53 tests, including the size, linter and
  formatter invariants and `generator-writes-only-with-write`).
- `python -B gate/run_tests.py gate` → 0 (36 tests).
- `python -B gate/run_tests.py product-guidelines` → 0 (14 tests; the reference test reads the
  changed skill paragraphs).
- `python -B elements/common/foundation_check.py` → 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py` (no `--write`) → 0, "entry points are
  current".
- `python -B task-cycle/change_file_sizes.py <base> <head>` → 0.
- `python -B elements/common/decision_index.py --sections ...` and the index of the selection → 0.
- Real-session Probe A and Probe B (above), Claude Code 2.1.330, `claude -p --model haiku
  --allowedTools Read` → 0 each. One earlier run of Probe B is discarded: Git Bash rewrote
  `/hidden-magic-probe` into a path; it was rerun with `MSYS_NO_PATHCONV=1`. The discarded run's
  session ran `ls`, `git status` and `git log` in the reviewed worktree, all read-only.
- Manual: the author's probe transcript read (above).
- Manual: WebFetch of https://code.claude.com/docs/en/skills for the fact's quotes (above).
- Manual: the searches of the orchestrator's last point.
- Not run: the other focused directories the author ran (`elements/common`, `elements/part-map`,
  `instruction-files`, `project-level`, `task-cycle`, `installation`). The diff touches only Markdown
  in them, apart from the three directories run above; `installation` takes about 700 s and is
  unchanged. Also not run: the full gate (the cycle's own run).

## Reaches beyond the dispatch

- The author's probe transcript under `~/.claude/projects/` — to judge acceptance criterion 1, which
  the handoff asks about.
- The live documentation page, by WebFetch — to check the new fact's quotes.
- `installation/install.py` (lines around 124 and 160-197, by search) — to confirm the product's
  hand-over is untouched and keeps its own `sibling_names`.
- `task-cycle/skill/SKILL.md:60-80, 245-262`, `task-cycle/skill/foundation_step.md:1-30`,
  `task-cycle/plan/SKILL.md:10-22`, `elements/common/way_of_working.md:186-196`,
  `process-audit/SKILL.md:16-22` and `project-level/lead/` by search — for texts that hand a skill
  on.
- WAY-21 by search — for Minor 6.

## Working copies

- `.runs/review-whole/` held the decision index and its sections list, the test log, and two probe
  repositories: `.runs/review-whole/probe` (with the submodule `.the-way`) and
  `.runs/review-whole/tw-src`. All were removed with `rm -rf` by their full paths; `.runs/` now holds
  only `author/` and `task-cycles/`. No git worktree was made (`git worktree list` shows none of
  mine).
- Kept beside this report: `reports/review-whole-probe-evidence.txt`, with absolute paths replaced by
  `<worktree>`.
- Remainder, made by Claude Code itself and not by me: the transcripts of my probe sessions in
  `a transcript folder of Claude Code in the user's home directory (the reviewer's first probe) `
  and `...--runs-review-whole-tw-src\`. They are left in place, outside the repository, as evidence.

## Unread material

- Decisions read whole: 3 of the index of my selection (WAY-127, WAY-34, WAY-35). The 47 decisions
  the index lists in full were read as the index gives them (sentence and *Scope*). I ran through the
  157 headings outside my sections, which were "Skills and agent types in sessions", "The part map
  and derived files", "Environment facts", "Instruction files" and "The-way's own coding and testing
  guidelines", with the parts agent-instructions, gate, decisions, part-map, invariants,
  environment-facts, glossary, elements-common, foundation-review, product-guidelines and
  project-level. WAY-21 was opened by search for its sentence only.
- Decisions bearing on the change that stayed unread whole: WAY-44, WAY-256 and WAY-90, read by
  their binding sentences in the index only; WAY-131, read by its index sentence only.
- Guideline files: `guidelines/coding.md`, `guidelines/coding-generator.md` and
  `guidelines/testing.md` read whole. `guidelines/coding-check.md`, `-command-runner.md`,
  `-measuring-report.md`, `-repository-changer.md` and `-shared-module.md` were not read: their kinds
  are not reached by the change.
- Part map: read whole. Invariants: `skill-entry-points`, `derived-file-content`,
  `generated-overview`, `generator-writes-only-with-write`, `skill-rule-source`,
  `outbound-link-reach`, `test-method-citation`, `tracked-file-private-paths` and
  `function-and-file-size` read whole. The other invariants with *Part* `every` or a touched part
  were not read beyond their *Part* line.
- Environment facts read whole: `claude-code-project-skills`, `claude-code-nested-skills`,
  `codex-repository-skills`, `codex-skill-paths` and `claude-code-skill-model-hiding`.
- Glossary: the term list, and `dependency of a part`, `invariant test` and `repository instruction
  file` whole.
- The element templates of environment facts and invariants: not read.
- The documentation page: read only for the two passages.

## Searches not found or unclear

- Codex's treatment of `disable-model-invocation`: not found in the foundation (no Codex fact covers
  it), not probed.
- In Probe A no `skill_listing` delta followed the `dynamic_skill` attachment, unlike the author's
  run, yet the model named the nested control. How Claude Code 2.1.330 hands a dynamically loaded
  skill to the model in `-p` mode is unclear. Both runs agree that the hidden entry points are absent
  from `dynamic_skill.skillNames`.
