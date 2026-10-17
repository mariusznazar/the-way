# Whole-change review — reviewer, turn 1

- Reviewer: general-purpose subagent, claude-opus-5-5; did not write the change.
- Method: Superpowers 6.4.1 `requesting-code-review` (`SKILL.md` and `code-reviewer.md` read whole
  from `C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/`),
  plus the no-plan coverage checks of WAY-136 / cycle step 9 named in the handoff.
- Range reviewed: `e7f7c3a15c3f80143f9ad582ec785c993cff3779..ac65ac3fda7284643704007b9055a6a11a069982`
  (`0761d6d`, `d88728d`, `ac65ac3`); 3 files, +351/−47: `foundations/decisions.md` +225/−8 (net
  diff), `task-cycle/skill/SKILL.md` +100/−35 then +24/−15, `task-cycle/record_template.md`.
  The full diff was read; the whole skill was read at `ac65ac3`, not only the diff.
- Also read whole: frozen `task.md`; `cycle.md` (questions table C1–C11); `author-foundation.md`;
  `author-implementation.md` with Addendum 2b; `elements/decisions/template.md`;
  `agent-instructions/README.md`; WAY-27, WAY-90, WAY-100, WAY-125, WAY-136 in full;
  `subagent-driven-development/SKILL.md` lines 355–475 and `re-review-prompt.md` lines 50–100 of
  Superpowers 6.4.1; glossary entries `correction`, `verdict`, `result`; part map `task-cycle`.
- Verdict: **With fixes** (2 Important, 4 Minor).

## Strengths

- Rows 1–7 map onto four well-cut decisions (WAY-161 rows 5–6, WAY-162 rows 1–3, WAY-163 row 4,
  WAY-164 row 7), each within the template's three binding sentences, with level 2 examples that
  name the exact failures the task guards against (e.g. WAY-162 *violates*: "a new Important
  finding in the fix is left out of the blocked request because the findings it set out to fix
  were fixed", `foundations/decisions.md:5183-5186`).
- The departure from adopted methods is written into WAY-125 itself, as the template's narrowing
  rule and the README's pre-`main` in-place edit ask, and every incoming fingerprint was renewed:
  my recomputation finds 0 stale relations across the log (`review-fingerprints.txt`).
- The skill holds the rule once, in the new section "The end of a code review"
  (`task-cycle/skill/SKILL.md:395-435`), and every older place that let the orchestrator settle
  findings now points there: intro `:16-22`, reading rule `:157-159`, step 9 `:296-301`, step 10
  `:323-324`, step 11 `:376-378`, step 12 `:446-448`, correction `:516-520`. The old "Nothing is
  deferred" sentence is scoped to foundation entries (`:358-360`), answering carried question b.
- The glossary's narrow `verdict` and `correction` are kept out of the new decisions' wording
  ("grade", "fix", "the human's remarks on the request").
- The author's weakest-point check caught a real loophole (lines 158 and 299 at `d88728d` let the
  orchestrator argue a blocking finding away before its fix); it was raised, ruled (C10) and closed.

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

1. **WAY-125 and the skill misstate the borrowed step they replace: Superpowers' "out-of-scope
   observations" are outside the fix diff, not outside the task — and on the planned route such an
   observation in the review of the final fix now has no destination.**
   - File: `foundations/decisions.md:3626-3627` (WAY-125 binding: "findings outside the task wait
     in the method's ledger"); `foundations/decisions.md:5105-5106` (WAY-161 *Based on* quoting
     "Out-of-scope observations go to the ledger as deferred minors"); `task-cycle/skill/SKILL.md:433`
     ("out-of-scope observations wait in its ledger").
   - What's wrong: in Superpowers 6.4.1 the sentence quoted comes from the scoped re-review, whose
     prompt defines the term: "Do NOT re-review code the fix did not touch: if you notice an issue
     entirely outside the fix diff, report it under Out-of-Scope Observations — it does not block
     this task and does not extend the loop" (`subagent-driven-development/re-review-prompt.md:57-61`).
     The method's step for findings outside the task is a different one — the "Declined to judge"
     list the executor rules on (`requesting-code-review/code-reviewer.md:43-48`), which WAY-125
     names separately. So WAY-125's binding part, a changed approved decision the human is asked to
     re-accept, describes a borrowed step that does not exist in the source, and drops the one that
     does. The task's *Decisions in play* makes the same reading ("odkładania uwag spoza zakresu do
     zapisu metody (wiersz 6)"), so this is partly an issue of the plan, not only of the author.
   - Why it matters: (a) source fidelity is a required check of this review; (b) a real gap
     follows. On the planned route the review of the final fix is the scoped re-review
     (`SKILL.md:412-413`). An issue its reviewer notices outside the fix diff — of any grade, in the
     task's scope — is no longer sent to the ledger (the skill says that step is replaced), is not
     "a new Critical or Important finding in the fix itself" (WAY-162), is not a finding the
     reviewer marked as beyond the task (WAY-161), and is not a graded finding of the whole-change
     review that went to the fix. It falls between all the kinds the orchestrator may not move
     findings between; a Critical issue seen at the last review can then reach a request marked
     ready, which is exactly what WAY-162's rationale forbids.
   - How to fix: correct the description in WAY-125 (`:3626-3627`) and in the skill (`:433`) to
     what the method does ("observations outside the fix diff wait in the method's ledger"), and
     keep the quote in WAY-161's *Based on* only if a sentence of WAY-161/162 replaces it. Then
     route those observations; two ways, of which only the orchestrator or the human can choose:
     - (i) count a Critical or Important observation outside the fix diff as a finding that
       remains (as WAY-162 counts new breakage in the fix) and list Minor ones with the Minor
       findings — closes the hole, but extends row 2's "new finding in the fix itself" to findings
       outside the fix, a meaning no row carries, so it would need the human (blocked draft
       question) or a ruling that it follows from row 1's "zostają uwagi blokujące";
     - (ii) list every such observation in the request with the reviewer's words and grade, in an
       item of its own, without a fix — stays within rows 5/8's "nothing only in reports", adds no
       blocking rule, but lets a Critical observation through to a ready request.
     I recommend (i) as the reading of row 1 ("gdy … zostają uwagi blokujące") — an observation the
     re-reviewer grades Critical or Important is a blocking finding that remains — but the choice
     and its record belong to the orchestrator.

2. **WAY-163 says the cycle record and record of stages are written before the blocked request is
   opened; the skill opens the request first.**
   - File: `foundations/decisions.md:5216-5217` ("Before the cycle opens a request that a remaining
     blocking finding blocks (WAY-162), it runs the product's full required gate on the change and
     writes its cycle record with its record of stages"; heading `:5214` asks the same) vs
     `task-cycle/skill/SKILL.md:424-427` ("Then open the request, write `stages.md` and the record
     as step 12 gives them") and `:439-440` (step 12 "starts at opening the request", whose order
     is open → placeholder swap → `stages.md` → record copy, `:452-466`).
   - What's wrong: the decision and the skill that implements it give opposite orders. Row 4 says
     "Przed otwarciem zablokowanego szkicu cykl uruchamia pełną bramkę i zapis cyklu".
   - Why it matters: WAY-163 is verified at level 2 by an agent comparing a cycle with the
     decision; a cycle that follows the skill literally violates the decision's text, and the
     human, re-accepting a decision whose wording the skill contradicts, cannot tell which binds.
     The practical cost of either order is small, which is why the fix is cheap — but the
     disagreement is a failure of handoff check 4, not polish.
   - How to fix: in the skill, write `stages.md` and the cycle record (running
     `task-cycle/cycle_stages.py`) before opening the blocked draft, then open it and commit and link
     the record as step 12 gives — nothing in step 12 makes `stages.md` depend on the request
     existing. Rewording WAY-163 instead ("before it hands the request to the human") is the other
     way, but row 4 says "przed otwarciem", so the skill is the side to move.

### Minor (Nice to Have)

1. **The review of the fix for a plan of one slice has no named reviewer.**
   - File: `task-cycle/skill/SKILL.md:397-398`, `:412-413`.
   - What's wrong: the section names "the one-author review of step 9, or the final whole-branch
     review of a planned change", and the fix review "by the same reviewer for a one-author change,
     by the scoped re-review of `subagent-driven-development` for a planned change". A plan of one
     slice gets step 9's `requesting-code-review` (`:311-312`) and does not run
     `subagent-driven-development` (`:302`), so neither branch fits it. The old sentence ("the same
     reviewer reviews the fix range once") covered it.
   - Fix: "by the same reviewer for a one-author change or a plan of one slice".

2. **Step 9's boundary for a planned change leaves out the review of the fix.**
   - File: `task-cycle/skill/SKILL.md:306-307` ("Its boundary is the final review and its one fix").
   - Why it matters: the scoped re-review of that fix is inside the method's Final Review section
     and is the review WAY-162 counts; a boundary read literally returns before it.
   - Fix: "the final review, its one fix and the review of that fix".

3. **"The review of the fix then keeps or drops it" has no counterpart in the scoped re-review's
   verdicts.**
   - File: `task-cycle/skill/SKILL.md:408-409`.
   - What's wrong: the re-review prompt verdicts each finding only "ADDRESSED | NOT ADDRESSED"
     (`re-review-prompt.md:82-84`); a finding the executor answers as wrong with evidence has no
     "dropped" verdict on the planned route, so a sound pushback reads as NOT ADDRESSED and blocks.
   - Fix: say in the skill that the fix handoff to the re-reviewer asks it to state, for a finding
     the executor contests, whether it keeps the finding; or accept the behaviour and say so.

4. **Ragged line wrapping left by Addendum 2b.**
   - File: `task-cycle/skill/SKILL.md:161`, `:308`, `:362`, `:411`, `:426`, `:450`, `:499`.
   - What's wrong: very short lines inside paragraphs ("fixes them in", "with what step 13",
     "partial work as complete."); harmless to agents, harder for the human reading the diff of the
     next change. Reflow the touched paragraphs when they are next edited.

## Coverage (no-plan checks, WAY-136 / cycle step 9)

| Task item | Entry (decisions.md at `ac65ac3`) | Skill and template (at `ac65ac3`) | Result |
|---|---|---|---|
| To do 1 / row 1 — one fix, one review of it; remaining blocking findings → blocked draft with place, reason, what the fix tried, cost from `stages.md` with rounds; no orchestrator ruling; slice loops unchanged | WAY-162 `:5151-5160` | intro `SKILL.md:16-22`; section `:406-414`, `:420-429`, `:431-435`; step 9 `:305-307`, `:317`; step 13 `:493-497`; template `record_template.md:46-49`, `:154-157` | Meaning held; see Important 1 for the planned-route hole and Minor 1–2 |
| Row 2 — not into step 11's settlements; new Critical/Important in the fix counts as remaining | WAY-162 `:5155-5158` | `:413-414`, `:420-421`; step 11 `:376-378` | Held |
| Row 3 — same bound for later code reviews (step 11, step 12, correction) | WAY-162 `:5151-5154` | `:414-418`; step 11 `:376-378`; step 12 `:446-448`; correction `:516-517` | Held |
| Row 4 — gate and record before the blocked draft; return step and assessment skipped, named, run after the human's decision | WAY-163 `:5216-5221` | `:420-429`; step 10 `:342-344`; step 13 `:493-497`; correction `:517-520` | Meaning held; order contradicts the decision — Important 2. Skipping step 12's reconciliation (C11) is an added skill rule from carried question 4's principle; I agree with it |
| To do 2 / row 5 — Critical/Important block unless marked out of scope; none blocking → request without a fix; Minor listed | WAY-161 `:5086-5094` | `:397-404`; step 13 `:476-480`; template `:151-153` | Held |
| To do 3 / row 6 — reviewer-marked out-of-scope findings (declined lines or described as beyond the task) not fixed whatever grade, listed with words and place, human creates tasks, no moving between kinds | WAY-161 `:5089-5094`; WAY-125 `:3624-3628` | `:397-403`; step 13 `:477-480`; template `:151-153` | Held; WAY-125's description of the replaced ledger step is wrong — Important 1. "Or a note that it names none" (C6) is a skill-level answer to a value the row does not give; acceptable |
| To do 4 / row 7 — author and each executor: requirement most likely unmet, check, report; reviewer reads it; request lists it in test evidence | WAY-164 `:5253-5257` | step 9 `:291-298`; step 13 `:476`; template `:50-51` | Held |
| WAY-125 edited in place | `:3624-3628`, verification `:3652-3653`, rationale `:3664-3666`, rejected `:3670-3672`; *Approved by* placeholder | skill `:431-435` | Allowed before `main` (README); C9 lists it in *What this request settles* |

- No meaning added that no row or answer carries in the decisions: checked; the one addition beyond
  the rows is in the skill (C11), and it follows carried question 4's stated principle.
- Source fidelity: every Superpowers quote in WAY-161 and WAY-162 *Based on* matches 6.4.1 text
  (`code-reviewer.md:45-47`, `:113`, `:116`, `:119`; `requesting-code-review/SKILL.md:45`;
  `subagent-driven-development/SKILL.md:401-403`, `:454-456`, `:465-469`), apart from the reading
  of "out-of-scope observations" (Important 1). WAY references and every relation fingerprint are
  current (0 stale). Glossary `verdict` / `correction` are not used for the reviewer's call or the
  fix in the new entries; the skill uses only its own existing name "correction after review".
- Commit order: foundation `0761d6d` precedes `d88728d` and `ac65ac3`. Held.
- Older skill sentences against WAY-161..164: intro, step 9's fix sentence, step 10's "resolve
  review findings", step 11's "Nothing is deferred", steps 12–13 and the correction section are all
  replaced or qualified; none still contradicts, apart from Important 2.
- Template conformance (`elements/decisions/template.md`, `elements/common/rules.md`): binding
  parts of 3, 3, 2, 2 sentences (WAY-125: 3); normative words only inside quotes; fields complete
  and in order; `Change: new decision` kept on the pre-`main` edit; *Approved by* placeholders on
  the five entries whose meaning is new or changed; *Review when* with observable states and dates;
  level 2 complies/violates pairs; rationale names no file or script, and the "the rule takes from
  … practice" wording follows the precedent of WAY-142..147 under WAY-27/WAY-100. Guard: 0 errors.

## Sharpness confirmation

The author's inputs hold against the actual diff: touched parts `decisions` (file
`foundations/decisions.md`) and `task-cycle` (`task-cycle/**`), whose part-map failure modes are
all high and not detected, so criticality is high; neither part declares a trust boundary
(`foundations/part_map.md:151` for `task-cycle`); no irreversible operation — text changes under
git. No growth since the start record.

## Weakest-point check (WAY-164)

- Right requirement: yes. To do 1 is where an older sentence elsewhere in a long skill could keep
  the orchestrator ruling on findings, and that is the failure the whole task exists to prevent.
- Did it catch what it claims: part (a), a keyword listing classified by hand, did catch two real
  loopholes (`:158`, `:299` at `d88728d`), which were then closed. Part (b), 24 anchor phrases
  present, only proves wording exists, not that nothing contradicts it — a check that only passes.
  The check did not look at order or at agreement between the skill and the decisions, which is
  where Important 2 sits, nor at the source's meaning of borrowed terms (Important 1). The script
  lives in the author's scratchpad and is not kept, so its output cannot be reproduced; WAY-164
  does not require that.

## Declined to judge

- Where Minor and out-of-scope findings of the code reviews after the review of the whole change
  (step 11 settlement, step 12, correction) go — rows 5 and 6 are scoped to the review of the whole
  change; ruling C5 keeps them in the reviews' reports. A reasonable reader may expect them in the
  request too; that is a new rule for the human, not this change.
- Whether slice-level deferred minors and parked rulings of `subagent-driven-development` should
  reach the request — row 1 keeps slice loops unchanged.
- The candidate failure mode for the part map (C8) — the return step's to weigh.
- Whether the weakest-point check is kept as a test (carried question c) — WAY-164 is silent.
- Bare "correction" for "correction after review" in `record_template.md:47` and `:110` — the
  `:110` use predates this change; the glossary conflict is older than the task.
- The active Superpowers install being 7.0.0 while 6.4.1 is read from disk (C2) — a process matter
  outside this change.

## Recommendations

- Treat Important 1 as a lesson for task refinement: before a task names a borrowed step it
  replaces, quote that step's defining text, not a sentence that uses its term.
- A weakest-point check on prose would be stronger as a comparison of each decision's binding
  sentence against the skill sentence that carries it, than as a presence list.

## Assessment

**Ready to merge?** With fixes

**Reasoning:** The four decisions carry rows 1–7 faithfully and the skill is cleanly re-centred on
one section, with fingerprints, guard and tests clean. Two blocking findings remain: WAY-125 and
the skill misdescribe the borrowed "out-of-scope observations" step, which leaves a planned-route
hole in the review of the final fix, and WAY-163 and the skill state opposite orders for the record
and the blocked request.

## Commands run (read-only checks; outputs under this reports directory)

| Command (from the worktree root at `ac65ac3`, Git Bash) | Exit | Output | Summary |
|---|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | `review-tests-task-cycle.txt` | 41 tests OK |
| `python -B gate/run_tests.py gate` | 0 | `review-tests-gate.txt` | 98 tests OK |
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | `review-guard-decisions.txt` | 0 errors, 10 warnings (5 pre-existing overdue check-by dates: WAY-03, 21, 52, 55, 69; 5 `<request link>` placeholders: WAY-125, 161–164), 5 unchecked from the `none` options |
| `python -B <scratchpad>/fp_check.py .` — relation fingerprints recomputed with `relation-model/fingerprint.py` and the guard's parser (script copied as `review-fp_check.py.txt`) | 0 | `review-fingerprints.txt` | 0 stale; WAY-125 `18d08c16`, 161 `d6d3137b`, 162 `ce2e41f0`, 163 `80d2e584`, 164 `898c9d56` match the author's report |

Unchecked: everything the `--base none` / `--merge-onto none` options leave unchecked (named in
`review-guard-decisions.txt`); the full gate does not exist yet (README).
