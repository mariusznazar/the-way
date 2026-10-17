# Whole-change review — agent's path to the running product

- Reviewer: general-purpose subagent, claude-opus-5-5 (no subagents spawned)
- Method: Superpowers 6.4.1 `requesting-code-review`, filled by `review-handoff.md`, plus the-way's additions 1–8
- Range: `77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988..c657b2b020236c32fe4f1ea4d68ca30b0fae5dd4` (4 commits, 13 files, +597/−52)
- Read whole: `task.md`, `cycle.md` (C1–C12), `agent-instructions/README.md`, `author-foundation.md`, `author-implementation.md`, the whole diff, `project-level/readiness_check.py`, `project-level/test_readiness_marks.py`, the changed hunks of every other file with their surrounding steps, the binding sentences of WAY-34, 108, 112, 118, 137, 139, 140, 143, and the decision template.
- Passes: two. First the foundation (`596a660`, `4c251dc`) against the task. Second the checks (`8720107`) and the code, template and skills (`c657b2b`), followed by the deliberate break.
- The checkout under review was not modified. Every run that writes files happened in two temporary detached worktrees of `c657b2b` under the scratchpad. Both have since been removed (`git worktree list` shows none).

## Changed files

| File | Added | Removed | Commit |
|---|---|---|---|
| `foundations/decisions.md` | 121 | 11 | `596a660` |
| `foundations/invariants.md` | 2 | 2 | `4c251dc` |
| `project-level/test_plan_state.py` | 3 | 0 | `8720107` |
| `project-level/test_plan_state_invariant.py` | 4 | 1 | `8720107` |
| `project-level/test_readiness_check.py` | 169 | 22 | `8720107` |
| `project-level/definition_template.md` | 35 | 5 | `c657b2b` |
| `project-level/lead/skill/SKILL.md` | 5 | 1 | `c657b2b` |
| `project-level/plan/skill/SKILL.md` | 4 | 1 | `c657b2b` |
| `project-level/readiness_check.py` | 14 | 1 | `c657b2b` |
| `project-level/skill/SKILL.md` | 5 | 1 | `c657b2b` |
| `project-level/task/skill/SKILL.md` | 6 | 1 | `c657b2b` |
| `project-level/technology/SKILL.md` | 30 | 6 | `c657b2b` |
| `project-level/test_readiness_marks.py` | 199 | 0 | `c657b2b` |

Order: `596a660` (decisions only) → `4c251dc` (`invariants.md` only) → `8720107` (test files only) → `c657b2b` (code, template, skills, ordinary tests). The foundation entries and invariant checks come before the code that depends on them. Every commit has the private author address.

## Coverage, order and fidelity (addition 1)

| Item | Where it is carried | Verdict |
|---|---|---|
| To do 1 — three items always on the list, settled like any other | WAY-121 sentence 2; template Technology section (`definition_template.md:181-196`); `technology/SKILL.md:60-64` (step 1) and steps 2.1, 2.3, 2.5 | covered |
| To do 2 — the gate stops a list lacking one, approved definitions too | WAY-121 sentence 3; `project-technology-record/1`; `readiness_check.py:257-263`, which runs in both modes; routing in `task/skill/SKILL.md:80-85`, `plan/skill/SKILL.md:66-69`, `lead/skill/SKILL.md:38-42`, `skill/SKILL.md:63-67`, `technology/SKILL.md:37-45` | covered, except one sibling branch (Important 1) |
| To do 3 — request line on moving the pin | a line of the request, not a file. Nothing in the change contradicts it. The template (`:197-200`) and the skills say the same thing: an approved definition lacking the three goes back to the technology step and through the gate before work relies on it | nothing contradicts (the request itself is not yet written) |
| Row 1 | WAY-121 sentence 2: "every list also holds three choices … each an item of its own … each settled like any other choice, by a projected decision of its own unless the foundation already holds it, and each answered also where the product has no such thing" | faithful. "named in the definition's language and marked in English" is the form from C6, which carried question (a) left to the cycle |
| Row 2 | WAY-165 sentence 1 (logs; interface "as its user does — through a screen in a browser, a call of an API or a command in a terminal — and how it sees what the product answers") | faithful |
| Row 3 | WAY-165 sentence 2 ("leaving open whether they are set up from nothing or kept in a lasting environment dedicated to tests, both being options weighed by their consequences") | faithful. "weighed by their consequences" comes from the answer to question 5 |
| Row 4 | WAY-121 sentence 3, first clause after the semicolon; invariant `project-technology-record/1` | faithful (see Minor 1 on how the sentence reads) |
| Row 5 | WAY-121 sentence 3, last clause ("goes back to the step and through the readiness gate again once its product moves the commit of the-way it pins and the readiness check first runs on it, as the refinement of a task of its plan runs it"); invariant "approved or not" | faithful in meaning. C8 already flags the generalization for the request |
| Row 6 | WAY-165 sentence 3, plus `narrows WAY-137@86b2a30d` | faithful. "even where the option is a place the product runs" names the area of the narrowing (F4) and adds no meaning |
| Rejected alternatives of questions 1–6 | WAY-121 *Rejected* (one item; one item split; a requirement beside the list; WAY-139; only new definitions; manual catch-up; names in English) and WAY-165 *Rejected* (interface without "as its user does"; data from nothing; data with no word on state; agent use as a plain difference; log content rules) | all carried. The answer to question 1 (log content is out of scope) is in WAY-165 *Rejected* |
| Context: the A1 "hard limit" is not taken | WAY-121 *Rationale*, last sentence | carried (WAY-100) |

## Foundation consistency (addition 2)

- **Form.** Both decisions follow `elements/decisions/template.md`: 1–3 binding sentences, every field present, *Approved by* `Mariusz, merge of <request link>` as in the precedent of `466980f`. WAY-121 is edited in place and its approval is reset for renewed acceptance (README, WAY-07). `project-technology-record/1` follows the invariant form, with *Derives from* `WAY-121@d0b060e5`.
- **Fingerprints.** Recomputed with `relation-model/fingerprint.py` (script `review-fingerprint-links.py`, output `review-fingerprint-links.txt`). WAY-121 `d0b060e5`, WAY-165 `a179dbe4`, WAY-118 `5af868b3`, WAY-100 `e7a74a18`, WAY-106 `63eddf70`, WAY-116 `afbcd2fa`, WAY-123 `f3b45293`, WAY-137 `86b2a30d`: every relation carrying these values is current. In tracked `.md`/`.py` files there are 460 `WAY-n@fp` and invariant links. Nine are stale, and all nine are deliberate fixtures in `elements/*/test_format_guard.py` (`WAY-01@00000000` and similar). No stale link in `foundations/`, and no remaining reference to the old `740c254e`. The plan-state fixture's new `FINGERPRINT = "dcb10529"` matches an independent recomputation (`review-fixture-fingerprint.txt`).
- **Overlap search.**
  - WAY-108: English markers; the marks extend it, and WAY-121 cites it.
  - WAY-118: re-gating after a change; row 5 goes the same way.
  - WAY-122 and WAY-123: relation fingerprints renewed; the meaning holds.
  - WAY-137: narrowed explicitly, and its tie rule is kept for a place to run.
  - WAY-139: the deployment skill's logs item is a different question; cited in *Rejected*.
  - WAY-140: setting up an environment is a human's action; cited.
  - WAY-143: no conflict, since the definition settles the choice and the first task that uses it builds it.
  - Glossary `surface`: not used in any added line. No added line holds `should`, `will`, `logging` or capitalized RFC words.
  - No contradiction found, except Important 1, which is inside a skill rather than the foundation.

## Sharpness (addition 3)

The author's findings are confirmed: high criticality (part `project-level`), the trust boundary `project-level/readiness_check.py` is touched, and nothing is irreversible. The change adds three `str.startswith` calls over the texts that the existing `items()` already yields: no new regex, no I/O, linear in the number of items.

Adversarial probes, each run in both modes (`review-adversarial-probes.py`, output `review-adversarial-probes.txt`):

- **Rejected for the missing mark:** a fullwidth colon, a non-breaking space inside `development data:`, the mark in backticks, a `* ` list marker.
- **Rejected anyway:** a fence at column 0, an HTML comment holding the mark. Their own lines are findings ("no choice item").
- **Accepted:** two spaces after the dash, no space after the colon, two `logs:` items, a mark with no name (`- logs: — held by: ARC-03/1`), a fence indented under a nested item that holds a marked line.

Correction to the author's sharpness note and concern 1: a marked line inside a fenced block does count as an item, but a fence at column 0 adds its own "no choice item" findings, so such a definition is rejected anyway. Only a fence indented under a nested detail is skipped silently, which is a quirk `items()` already had (Minor 3).

## Weakest-point check (addition 4)

The author named To do 2 / row 5: an approved definition that the check fails to stop. Judgment: the check catches the miss it names.

- The `ApprovedBefore` test fails under break B1 below, in which the rule is skipped for approved definitions.
- I also ran the readiness check read-only on the real definition that answer 4 names (`definicja_mvp_loop2.md`, approved 2026-10-13; `review-loop2-readiness.txt`). The base `77c8a8b` reports nothing (exit 0). The head reports exactly three `g` findings, one per mark, at the Technology heading (exit 1). The real definition is therefore stopped for the three alone, as row 5 requires.
- What the check cannot reach is how each skill sends such a definition back. That is prose; I read every branch, and one of them contradicts row 5 (Important 1).

## Invariant checks and the deliberate break (addition 5)

**The checks against the sentence.** `TechnologyMarks` and `Command.test_a_definition_lacking_a_mark_exits_one_approved_or_not` test what the sentence says, and only that:

- Every case runs before approval and with a gate record ("approved or not").
- A rejection is detected as the findings that remain once the mark's valid item is added, so no message wording is fixed (the sentence fixes none).
- Negative controls cover the forms the sentence excludes: another case, no colon, the mark not at the start, on a continuation line, in a nested item, in prose, in another section, a second mark in one item.
- The two equality assertions (`test_a_definition_holding_all_three_marks_is_not_rejected_for_them`, `test_an_open_choice_carrying_a_mark_is_rejected_only_as_open`) stay within the sentence. Its list of rejection grounds is exhaustive, and an open item is a "choice item", so it carries the mark.
- The loosening of `test_none_is_reported` to `assertIn` (C12) loses nothing: `none` is still rejected in both modes.
- The fixture edits in `test_plan_state*.py` keep each assertion unchanged.

**The breaks.** They were written from the sentence alone, in a temporary worktree of `c657b2b`. The method run each time was `python -B gate/run_tests.py project-level --record <scratch>/project-level-tests-<B>.jsonl`:

| Break | Patch | What it breaks in the sentence | Exit | Result | Output |
|---|---|---|---|---|---|
| B1 (the one requested) | `check()` drops the mark findings unless `--before-approval`: an approved definition keeps its older list | "approved or not" | 1 | 34 failures; record: `project-technology-record/1` fail 11, plus `ApprovedBefore` | `review-break-B1.patch`, `review-break-B1.txt` |
| B2 | a mark anywhere in any line of the section counts | "a choice item whose text begins with" | 1 | 26 failures; record: `project-technology-record/1` fail 5 | `review-break-B2.patch`, `review-break-B2.txt` |
| B3 | any one of the three marks satisfies the rule | "none … `logs:`, none … `interface:`, or none … `development data:`" | 1 | 66 failures; record: `project-technology-record/1` fail 10 | `review-break-B3.patch`, `review-break-B3.txt` |

All three breaks are detected. The worktree was clean after each restore, and both temporary worktrees were removed. Script: `review-break-script.py`.

## Checks (addition 6)

All of these ran in a temporary worktree of `c657b2b`, with Git Bash and Python 3.14.

| Command | Exit | Result | Output |
|---|---|---|---|
| `python -B gate/run_tests.py project-level --record <scratch>/project-level-tests-head.jsonl` | 0 | 269 tests OK; record 154 checks, all `pass` (`project-technology-record/1` 30) | `review-tests-project-level.txt` |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK | `review-tests-gate.txt` |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | 0 errors, 7 warnings, 5 unchecked | `review-guard-decisions.txt` |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 3 unchecked | `review-guard-invariants.txt` |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | 0 errors, 0 warnings, 7 unchecked | `review-guard-part-map.txt` |
| `git diff --check 77c8a8b..c657b2b` | 0 | no output | `review-diff-check.txt` |
| `git diff --numstat 77c8a8b..c657b2b` | 0 | 13 files | `review-diff-numstat.txt` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | entry points are current | `review-skill-entry-points.txt` |
| fingerprint link scan (scratch script) | 0 | 460 links, 9 stale, all deliberate guard-test fixtures | `review-fingerprint-links.txt` |
| independent fixture fingerprint | 0 | `dcb10529` = constant | `review-fixture-fingerprint.txt` |
| readiness check on the real loop2 definition, base and head (read-only) | 0 / 1 | nothing / three `g` findings | `review-loop2-readiness.txt` |
| adversarial probes | 0 | see Sharpness | `review-adversarial-probes.txt` |
| deliberate breaks B1–B3 | 1 / 1 / 1 | all detected | `review-break-B*.txt` |

**Warnings, named.** Five are pre-existing: check-by dates passed on WAY-03, 21, 52, 55 and 69. Two are expected placeholders `merge of <request link>`: WAY-121 at `decisions.md:3469` and WAY-165 at `:5389`.

**Unchecked, named.**
- From `--base none`: main-branch lines and versions, template change without a version, invariant identifiers, versions, corrections and the violated list, part-map known violations, identifiers and criticality lowering.
- From `--merge-onto none`: `TODO` in the log and in invariants, copies of versions, relation and link fingerprints. My fingerprint scan covers these for this change.
- Part map: the parts lists of `wording-reaches-dependants` and `skills-reach-the-way-sessions`, promise-level change paths, and the dependency graph.

**Not run:** the full gate (it does not exist yet), the second WAY-33 search against the integration tip, and the independent assessment. These belong to later stages.

## Strengths

- **The mark design.** The readiness check can recognize the three items in any language with three `startswith` calls on text the parser already produces. Nested details, prose and continuation lines are excluded by construction rather than by special cases.
- **The invariant checks.** They are unusually well built. Detecting a rejection as the findings left over when the item is added makes them independent of message wording. They run in both modes, and the negative controls killed all three breaks, including the subtle "any line" break (B2).
- **The weakest point is evidenced, not just asserted.** There is a red/green `ApprovedBefore` test on a literal with its original gate fingerprint, a manual plan-state run, and (from this review) the real loop2 definition, stopped for exactly the three.
- **Foundation work.** Rows 2, 3 and 6 are separated into WAY-165 with an explicit `narrows WAY-137`, which keeps WAY-121 within three sentences and leaves an approved decision untouched. Every rejected alternative of questions 1–6 is carried. The relations and fingerprints are all current.
- **Process discipline.** Three agents wrote the sentence, the checks and the code, in that order. Fixtures of other invariants' tests were changed by the check agent rather than the code's author. The ordinary tests went in a new file instead of an invariant test.

## Issues

### Critical (Must Fix)

none

### Important (Should Fix)

#### 1. `define-project` still offers to "leave" a definition with no Technology section, which row 5 and WAY-121 now rule out

**Anchor:** `project-level/skill/SKILL.md:68-74`

**To paste:** Step 0 still offers the human "leaving it" for a definition with no `## Technology` section, and says that leaving it "leaves the choices to the breakdown". WAY-121 now sends every approved definition lacking the three choices back to the technology step and through the gate. Plan-project, refine-task and lead-project all stop on the readiness check's finding, so that option leads nowhere, and the cost it states is wrong.

**Why I report it:** This branch sits next to the approved-definition branch the change edited (`:58-67`). It covers a definition written before the technology step existed. Such a definition lacks all three marked items as well as the section.

Since `c657b2b`, WAY-121 says such a definition "goes back to the step and through the readiness gate again once its product moves the commit of the-way it pins". The answer to question 4 explicitly rejected exempting older definitions or catching them up by hand.

Example: a human answers "leave it". The definition stays `approved` without a Technology section. The next `refine-task` on its plan runs `readiness_check.py` and gets a structure finding ("the section `## Technology` is missing"), and "a finding returns to `define-project`" (`task/skill/SKILL.md:80`). `define-project` asks the same question again, so the project loops, while the skill told the human the choices would go "to the breakdown".

The inconsistency with plan-project existed before this change. This change turns it into a contradiction with a binding sentence.

Fix (about 3 lines): drop the "leave it" option. Say that the definition was written before the step and goes back through it: add `## Technology` reading `TODO`, set the status line, step 6, step 7, then a plan recheck through `plan-project` (WAY-121, WAY-118), as the branch above it now does for a list lacking marks. If the human must still be asked something, state the cost truthfully: no task of its plan can be refined until it goes back.

How often it happens: WAY-121 has existed since 2026-10-04 and loop2's definition has the section, so likely no definition meets this today. That keeps the cost low, but it does not change the contradiction.

### Minor (Nice to Have)

#### 1. WAY-121's third sentence can be read as making the gate rule depend on "When the foundation already holds every such choice"

**Anchor:** `foundations/decisions.md:3439-3444`

**To paste:** The gate clause and the catch-up clause follow a semicolon inside a sentence that opens with "When the foundation already holds every such choice, …". A reader can take both as holding only in that case. Would moving the gate clause before the "When" clause, or making it lead the sentence, read more plainly?

**Why I report it:** The sentence is "When the foundation already holds every such choice, the step records the decision that holds each and settles nothing; the readiness gate stops a definition whose list lacks one of the three, and a definition approved before …". The three-sentence limit (F2) pushed rows 4 and 5 into the tail of a sentence whose opening subordinate clause conditions the first independent clause. Readers commonly carry such a condition over the semicolon.

The intended meaning is unconditional. The verification examples and the invariant make it clear, so no agent is misled in practice; the risk is a human or agent quoting the sentence in a borderline case.

Possible rewording, same meaning and still three sentences: "The readiness gate stops a definition whose list lacks one of the three, and a definition approved before … runs it; when the foundation already holds every such choice, the step records the decision that holds each and settles nothing." This changes the fingerprint again, so `d0b060e5` has to be renewed in WAY-122, WAY-123, WAY-165 and `project-technology-record`, which is cheap before `main`. C8's question about "as the refinement of a task of its plan runs it" is separate and already goes to the request.

#### 2. The catch-up route adds the missing choices as `— open` without first looking for a decision of the foundation that holds them

**Anchor:** `project-level/technology/SKILL.md:37-45`

**To paste:** For a list lacking a mark, step 0 adds each missing choice as `— open` and sends it to research. Step 1, by contrast, first finds what settles each choice (`held by`, `projected`, `open`). Should the catch-up do the same, so that a product whose foundation already decides, say, its test server says `held by` instead of researching it again?

**Why I report it:** WAY-121 says each of the three is settled "by a projected decision of its own unless the foundation already holds it". The catch-up bullet looks only under "Projected foundation changes" (through the open-item bullet that follows it), never at the product's decisions.

Example: loop2's foundation holds `D-11/1 — Which branch deploys loop2 to the test server?` (`C:/Storage/repos/loop2/foundations/decisions.md:289`). Whether that decision or another holds loop2's development data is the product's judgment, which I did not make. If one does, the catch-up route researches the choice again and projects a decision next to it. The gate's whole-foundation search (condition c, WAY-118) would most likely catch the collision, so the cost is a wasted research wave and a collision found late, not a wrong definition.

Fix: in the catch-up bullet, "add each missing one … and find what settles it as step 1 does; an item nothing settles ends `— open`".

#### 3. A fenced block indented under a nested detail of a Technology item lets a line inside the block count as a marked item

**Anchor:** `project-level/readiness_check.py:214-219` (`items()`, unchanged) and `:257-259`

**To paste:** A fence at column 0 in `## Technology` already produces "no choice item" findings. A fence indented under a nested detail, however, is skipped silently, so `- logs: …` inside it counts as the logs choice. Worth a fence skip in `items()` for Technology, or is it too contrived to matter?

**Why I report it:** This answers the author's concern 1, which I judge as mostly moot. Probe `fence indented after a nested item, holding logs` (`review-adversarial-probes.txt`) passes in both modes. The input is `- Jezyk — held by: ARC-01/1`, `  - note`, `  ```` ` ``, `- logs: Logi — held by: ARC-03/1`, `  - x`, `  ```` ` ``, followed by the other two marks.

The same input already passed the per-item checks before this change, so this is an existing parser property, not a regression. The file is a declared trust boundary (WAY-48), but its inputs are definitions written by the step's agent and the human, and the form the template gives has no fenced block in that section. The fix is optional: `split()` already tracks fences, and `items()` could treat a fenced line as "no choice item".

## The author's two concerns (addition 7)

1. **A marked line inside a fenced block in `## Technology` counts as an item.** Partly true. A fence at column 0 makes the definition fail anyway through its own "no choice item" findings. Only the indented-after-nested case passes, which is pre-existing and contrived. Minor 3.
2. **`define-project` still offers "leave it" for a definition with no Technology section.** Confirmed, and it now contradicts WAY-121 and row 5. Important 1.

## Recommendations

- Fix Important 1 before the request. It is a few lines of one skill and needs no new test.
- Consider Minor 1 while WAY-121 is still editable in place, because the human is asked to re-accept WAY-121's wording at this merge anyway.
- The request has to carry three items: the To do 3 line on moving the pin (part map, *Change paths*), WAY-121 as a changed approved decision (README, WAY-07) together with C8's generalization, and the author's candidate failure mode for the human (WAY-46).

## Declined to judge

Each was set aside for the reason given; the executor rules on each.

- The English marks as the recognizable form, and their exact spelling (`logs:`, `interface:`, `development data:`): settled by C6, a cycle ruling on carried question (a).
- A second item with the same mark is accepted: settled by C7.
- An item holding a mark and no name (`- logs: — held by: …`) passes. WAY-121 and the template ask for a name in the definition's language, but the invariant does not, and the step's agent writes the items. A lenient form check, cost low.
- Two spaces after the dash and no space after the colon are accepted: lenient and consistent with "text begins with".
- The candidate part-map failure mode (author concern 2): recording a failure mode is the human's (WAY-46), so it belongs to the request.
- Whether an agent operating a lasting test environment is an "effect outside the repository" under WAY-140 (author concern 5): no row asks it, and it is outside the task.
- Whether WAY-121's *Rejected* clause "which the readiness gate cannot check" breaks the rule that prose names nothing about what the process's tools lack today: it states an inherent limit of a script, not today's state, so it is borderline. Left to the independent assessment.
- Line length of the added table rows and of one reflowed line in `technology/SKILL.md:99`: style only; tables are long elsewhere too.
- Whether loop2's `D-11/1` or another decision already holds one of loop2's three choices: the product's judgment, not this change's.
- The second WAY-33 search against the integration tip, the independent assessment and the request text: later stages of the cycle.

## Assessment

**Ready to merge?** With fixes

**Reasoning:** The code, the foundation and the invariant checks carry To do 1–2 and rows 1–6 faithfully and in the right order. Every test and guard passes, and all three deliberate breaks are detected, including the approved-definition miss, which also holds on the real loop2 definition. One sibling branch of `define-project` still offers an option that the new WAY-121 rules out, and it should be fixed (a few lines) before the request.
