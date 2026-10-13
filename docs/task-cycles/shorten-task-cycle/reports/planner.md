# Planner report — shorten the task cycle

Status: plan written; returned before foundation writes or implementation.

## Inputs and authority

- Worktree: `C:/Storage/repos/the-way-wt/shorten-task-cycle`.
- Branch: `task/shorten-task-cycle`.
- HEAD and merge base with foundations: `d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b`.
- Frozen task: `.runs/task-cycles/shorten-task-cycle/task.md`, read in full; independent, ready for cycle, four accepted rows, no human actions.
- Spec: `.runs/task-cycles/shorten-task-cycle/spec.md`, read in full, including the corrected S1 acceptance sequence.
- Review: `.runs/task-cycles/shorten-task-cycle/reports/spec-review.md`; its scoped confirmation passes S1 and leaves no review finding open.
- Local project entry point `.agents/skills/the-way-plan-task/SKILL.md` and `task-cycle/plan/SKILL.md`, read in full; checkout checks show no product submodule.
- Current integration route: `agent-instructions/README.md`, read in full.
- Foundation read for planning: full part map and glossary; relevant whole decision entries WAY-01/02/03, WAY-07/08, WAY-10/11/12/13/14, WAY-22/25, WAY-30/31/32/33, WAY-35/36, WAY-45/46/47, WAY-69, WAY-114/125/126/134/135/136/140/144, and affected assessment/return/verification/search invariants. This is planning context, not the element writers' required whole-foundation search.
- Existing implementation read: full `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md`, `task-cycle/slice_size.py` and `task-cycle/test_slice_size.py`; relevant element skills/templates and common way of working to identify foundation prerequisites and authorship boundaries.
- No code, source instruction, foundation entry or commit was written. Only the authorized plan, size report and this report are outputs.

Root's provisional spec go-ahead is under the user's delegation, not human approval. The cycle
continues under the base process; the planner did not execute the proposed new process.

## Result and coverage

Plan: `.runs/task-cycles/shorten-task-cycle/plan.md`.
Size report: `.runs/task-cycles/shorten-task-cycle/plan-size.md`.

One cohesive slice changes the cycle skill, planner skill and record template after the
foundation stage. Its coverage table maps the outcome, all four To do items, all four accepted
rows, the answered movement-rule example, both carried questions, S1 and the stated exclusions.
No additional open design choice was established by these reads.

The foundation table assigns accepted rows 1/3 to new decisions and rows 2/4 to in-place edits of
WAY-11/1 and WAY-136/1. It includes the known WAY-126 and return-step-record dependency renewals.
The existing part-map assignment covers every planned instruction file.

## Ruling on derived invariants

Question returned to root: the spec leaves concrete decision wording and mandatory derived
invariants to the foundation writers. The planner proposed naming this as an explicit foundation
prerequisite, with final identifiers, methods and any checks fixed before implementation, rather
than inventing speculative sentence-matching tests.

Root accepted that handling provisionally: record-decision/record-invariant must determine what
the concrete sentences derive; the plan must hold the final identifiers, methods and check paths
before slice dispatch. Root also accepted one cohesive slice and no extra slice merely to claim
parallel work. This ruling adds no foundation meaning and is not human acceptance.

Accordingly F7 is a mandatory conditional prerequisite, not permission to defer a known
invariant. The foundation stage must enumerate actual consequences or document its no-derivation
finding. The orchestrator updates this plan's entries and new Read ranges and reruns slice_size
before dispatch. Any finding that instead leaves an open design choice returns to design through
the current process.

## Choices to copy into the cycle record

1. One cohesive slice. Its three files share the workflow and record interfaces; splitting by
   settlement creates repeated file edits, while splitting by file creates incomplete interfaces.
   The cost is a broader single review; if it outgrows its agent, the current discard/replan rule
   applies. Keeping the current instructions costs no edit but leaves all four changes undelivered.
2. Reuse existing record sections and borrowed briefs/reports. This requires manual evidence
   review; a new ledger/schema/validator adds a second contract without proving completeness.
3. Resolve concrete invariant consequences through the foundation skills before dispatch and
   refresh the plan. This requires one explicit boundary check; speculative invariants/tests risk
   enforcing wording or assuming the sentence author's interpretation.
4. Keep discovery names, paths and descriptions unchanged. If one actually needs changing,
   regenerate entry points and expand checks then; doing it now adds an unrelated write set.
5. Existing tests plus semantic comparison against all nine spec cases. No new proof of agent
   behavior or measured time/token saving is claimed; phrase-matching tests would add upkeep with
   no such proof.

## Checks and limitations

The planner verified the CLIs through `--help` for `gate/run_tests.py` and both affected format
guards. It read the current size script and its tests to retain the accepted slice fields and
support for a separate second-level plan section. The final actual size result is recorded below
and in plan-size.md.

`python -B task-cycle/slice_size.py .runs/task-cycles/shorten-task-cycle/plan.md` exited 0. Slice 1
changes three files and reads 144,989 characters, estimated at 57,996 tokens: fits, with no
unchecked path or oversized slice. The report was saved as UTF-8 directly from the command's
stdout. The size must be checked again after the foundation-stage range update.

Implementation checks are planned, not run or passed here: affected part tests, critical-flow
tests, element guards, changed-fingerprint comparison, whole-foundation searches, the independent
foundation assessment and semantic instruction review. The none-mode format guards intentionally
leave merge comparisons unchecked; the plan requires a separate direct comparison of changed
fingerprints. A TODO Method remains visible debt, not a successful check. These commands are
partial repository checks, not a pass of the full gate.

## Handoff

No unresolved planning question remains after root's ruling. Before dispatch, the foundation
stage must complete F1–F7 resolution, add the final new-entry ranges/methods/check paths and
refresh the size report. Human renewed acceptance of changed decision meanings remains at the
request/merge. No later stage was invoked.
