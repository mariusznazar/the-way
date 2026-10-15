# Final whole-branch review

**Verdict: WITH FIXES — not ready while R1 remains.** One Important finding, no Critical or Minor findings. This is the final code review, not the independent foundation assessment or approval to merge.

## Range and method

Worktree: `C:/Storage/repos/the-way-wt/lead-project`.
Base: `db77ba549cb9ece7d3e62bf29e1256973f62deab`.
Head: `2cadf14fd3d21a82f1adee322f1022002b194385`.
Package: `.superpowers/sdd/plan/review-db77ba5..2cadf14.diff`.
The range has 51 changed files, 2361 insertions and 116 deletions. HEAD matched dispatch and the tracked working tree was clean. No product, index, HEAD or branch changes were made. Only ignored review evidence was written; disposable ordinary-test fixtures cleaned themselves up.

Applied Superpowers 6.4.1 requesting-code-review and its complete reviewer template, the final-review provisions of subagent-driven-development, the local code-review playbook and its delegated document-review-loop guidance. No children were dispatched. Reviewed code/tests separately from workflow/foundation/documentation, then their joins. Generated sibling prose was checked by generator equality rather than treating thirty copies as thirty independent designs.

Authoritative inputs were the complete frozen task (all 19 work items, acceptance criterion and ten settlements), spec, plan and size report. Reviewed the final changes with current source files and focused unchanged dependencies: the plan/readiness parsing and approval checks, installer wrapper/guidance production, generated entry-point source and plan/definition gate routing. Read the progress ledger, retained reader acceptance and host-association evidence, Slice 1 break evidence, final suite evidence, and the return-step subprocess contract/check report. Earlier reviewers' verdicts were evidence of completed stages, not the oracle for this verdict.

## Foundation selection

Selection refreshed at the reviewed HEAD, from the complete current part map and all current decision Scope fields, including continuation lines. Touched subjects/parts: project-level, task-cycle, installation and agent-instructions. For collection files, selection follows the changed subject under WAY-44, rather than treating all changes as work on a ledger's format. The map's project-level failure mode, trust boundary and new CLI surface were read whole, with its shared scales, flows and external context.

Expected Scope matches and selected whole entries, all version 1:

`WAY-01, 03, 09, 10, 11, 13, 16, 21, 25, 26, 27, 28, 30, 33, 34, 36, 37, 38, 44, 45, 46, 47, 48, 51, 55, 57, 62, 63, 65, 68, 69, 82, 89, 100, 101, 102, 103, 106–156`.

The expected set has 88 entries and equals the selected set. Complete selected text is retained in `reports/final-review-foundation-selection.md`; this is a reading record, not a new index or a claim that Scope matching proves semantic completeness. Additional whole linked entries read for the actual change include WAY-07/08/12/22/31/49; key operative entries include WAY-124/134/144/150–156. Read the complete glossary, including project orchestrator, and all current invariant Part fields; 58 applicable `every`/touched-part entries are retained in `reports/final-review-invariants-0.md` through `-2.md`. Read the other unchanged WAY-09 fingerprint dependents as well. Their unchanged sentences remain consistent with the enlarged inventory; project-plan-form continues to govern form, not agent dependency semantics. WAY-135's unchanged meaning remains consistent with the changed candidate-presentation route.

Searched the whole foundation for leading, refinement, state evidence, ready tasks, Git-only execution and incoming fingerprints of WAY-09/124/134/144/152–156. The hits connect to the entries and map already reviewed; no additional collision was established. This reviewer search does not replace the author's two WAY-33 searches or the later independent assessment. External studies about agent behavior and tool-loading facts were not freshly revalidated; no changed claim about those external facts is part of this branch.

## Strengths

- The state reader reuses the original whole-source checkers in process and explicitly requires an approved definition. It does not make a second Markdown grammar or infer approval from fingerprint equality alone.
- Real disposable repositories exercise remote freshness, deleted branches, archive add/remove history, exact task paths, conflicting states and document preservation. Git arguments are arrays, archive paths are literal pathspecs, calls have bounded waits, and archive prose is treated as data.
- Refinement has explicit file ownership, source-bound answers, one round answerer and exact resumption/acceptance rules. Human answers, quotations and code facts remain distinguishable; code cannot silently prescribe required behavior.
- Whole-document acceptance is present in manual and orchestrated modes. Canonical answers must reach every affected durable task before cleanup. Definition approval and the subsequent plan recheck both block new readiness.
- Installed wrappers and repository entry points follow their existing pin/checkout contracts. The new installer tests cover preview, apply, repeat, source availability after clone and refusal to overwrite conflicting integration.

## Critical

None found.

## Important

### R1 — valid non-ASCII paths fail on an ANSI output stream

**Thread:** new review finding confirming the already reported open R1.

**Anchor:** `C:/Storage/repos/the-way-wt/lead-project/project-level/plan_state.py:267` (same issue at the report writes on lines 264, 271–280); masking test configuration: `C:/Storage/repos/the-way-wt/lead-project/project-level/test_plan_state.py:108`.

**Do wklejenia:** Czytnik kończy poprawne wywołanie kodem 2, gdy nazwa repozytorium zawiera polskie znaki, a stdout używa kodowania cp1252: zapis nagłówka `repository:` rzuca `UnicodeEncodeError`. Test ścieżki z polskimi znakami tego nie wykrywa, ponieważ fixture wymusza UTF-8; wyjście czytnika potrzebuje jawnej, bezstratnej obsługi kodowania i regresji z wyjściem ANSI.

**Dlaczego to zgłaszam:** The command must report evidence for an explicitly supplied repository, including non-ASCII paths. `display()` escapes control characters but preserves printable Unicode. `main()` writes that string using the inherited stdout encoding; with a repository name `product zażółć & $(echo injected)` and `PYTHONIOENCODING=cp1252`, the first repository-header write fails. The catch returns exit 2 with an encoding error instead of performing the otherwise valid observation. This is a product failure, not an invalid source or failed Git operation. The same dependency affects paths, refs, source findings and evidence elsewhere in the report.

Independent reproduction used the existing ordinary command test and changed only its child environment after fixture setup. It exited 2 instead of the required 0, with `error: 'charmap' codec can't encode character '\u017c' ... character maps to <undefined>`. Full short output is `C:/Storage/repos/the-way-wt/lead-project/.runs/task-cycles/lead-project/reports/final-review-encoding-reproduction.txt`. The wrapper recorded the expected reproduction and exited 0; the reader's exit 2 is the failing observation. The existing positive test's unconditional `PYTHONIOENCODING="utf-8"` explains why a green suite did not expose it.

Fix the report boundary so correct input does not depend on the caller preconfiguring UTF-8, and retain exact usable evidence without lossy replacement. Add a command-level ordinary regression with a restricted inherited output encoding and verify decoded paths/evidence, transitions and exit status, rather than merely removing the troublesome characters or checking for absence of a traceback. Include non-ASCII diagnostics as well as a successful path. Keep protected invariant checks read-only; if their mechanics need changing, return that edit to the independent check author.

Leaving this unchanged means the advertised command fails for valid paths in the documented Windows console environment. Fixing it costs a small output-boundary change and focused regression verification; it does not require a new state format or changes to orchestration policy. The precise encoding strategy belongs to the fixer, but silently replacing characters would weaken the promised exact evidence.

## Minor

None raised. No stylistic rewrite or speculative hardening is requested.

## Requirement coverage and joins

This table is a static implementation/source assessment; it does not assert that live agents executed the workflow.

| Frozen To do | Observed implementation |
|---|---|
| 1 | lead/skill owns human-facing leading of a handed-over plan, through acceptance and evidence-backed upkeep. |
| 2 | Lead prohibits cycle dispatch; human starts implement-task separately. |
| 3 | Reconciliation gives the closure notice and stops, with no closure implementation. |
| 4 | Plan, task documents and per-task conversations hold recovery information; no additional session store. |
| 5 | Reader proposes both supported transitions; Git-only boundary and host fallback are separate. Exact-source validation and fresh origin integration are implemented. R1 prevents valid observations in the named output environment. |
| 6 | Round proposal counts distinct direct/transitive dependants, ties by task number; human confirms/changes it. |
| 7 | Fresh parallel refiners write separate files; sole answerer follows them; exact five results and path-mediated dispatch agree across companions. |
| 8 | Refiner owns task body; lead changes only final Status after acceptance. Shared plan edits are serialized. |
| 9 | Answering instructions require document quotation or factual code location; required behavior cannot come from code/inference. Duplicate choices share canonical IDs. |
| 10 | Single complete round package includes questions, candidate tables, Human actions, wording, quotation/source list and challenge questions; struck quotations reopen. Independent critique runs before collective presentation. |
| 11 | Exact full document shown one at a time; acceptance saved before status writes; cleanup waits for durable transfer. |
| 12 | Agent turns/questions/waits map to to refine; presented package/ready-for-approval map to waiting for human. |
| 13 | Wait retains its question and reason, is logged, and is proposed again after evidence establishes the prerequisite done. |
| 14 | Structural in-scope changes go to delegated plan-project; scope and projected-writer changes remain human choices. |
| 15 | Narrow direct-edit exception, delegated definition gate, root-dispatched critique, human approval and fresh plan step-0 recheck are joined. Pending gate/recheck blocks readiness. |
| 16 | Orchestrated refine-task redirects every otherwise direct human question and child-work request through the conversation. |
| 17 | Manual refine-task also requires final complete-document acceptance, including no-candidate tasks. |
| 18 | Plan template, refine-task, lead and implement-task agree that dependencies constrain cycle start, not refinement. Delivered-in chains require evidence; dropped is not delivered. |
| 19 | plan-project step 7 points to lead-project; installation and both tools expose the skill. |

All ten settlements have a retained home: 1 and 9 in WAY-152/lead; 2 in WAY-153/reader and its two invariants; 3 in WAY-154/conversation/refiner; 4 in WAY-155/answerer; 5 in WAY-124/manual and orchestrated acceptance; 6 in WAY-144/plan and cycle start; 7 in WAY-156/delegated gates; 8 in WAY-134/round presentation; 10 in the project-orchestrator glossary entry. No new daemon, task tracker, automatic implementation or closure was found.

Scenario review included parallel dependent tasks, an unanswered behavior choice, code offered as a requirement, duplicate questions, rejected quotations, candidate rejection/challenge, unfinished/unplaced Human actions, interruption between final writes, one accepted document while another remains pending, wait awakening, in-scope plan edits, writer reassignment, definition changes and absence of child capability. The current instructions route each without inventing acceptance. This remains prose analysis, not empirical compliance evidence.

## Checks and retained evidence

Reviewer executions:

1. Git HEAD/status/range inspection: exit 0; exact dispatched HEAD and clean tracked tree.
2. The ordinary non-ASCII path test, instantiated with only child `PYTHONIOENCODING` changed to cp1252: reader exit 2, assertion expected 0; independently reproduced R1. Evidence file named above.
3. `python -B agent-instructions/skill_entry_points.py`: exit 0, `entry points are current`.
4. In-process `produce(discover(ROOT))` verification: exit 0; all 30 generated files byte-equal to output and all 15 tool pairs byte-equal.
5. JSONL inspection of the exact declared `.runs/project-plan-state-evidence.jsonl`: exit 0; eighteen evidence-invariant rows and two subprocess-invariant rows, all `pass`; zero `fail` rows in the record. No initial RED is being substituted for the final record.
6. `git diff --check db77ba5 2cadf14`: exit 0.

Existing executions inspected, not repeated:

- Latest project-level Method: exit 0, 229 tests, 49.293 seconds; latest gate run: exit 0, 98 tests. Exact final completion and subprocess report inspected.
- Slice 7 logs: agent-instructions 18, task-cycle 41, installation 30, all OK/exit 0. `git diff ea9a23e HEAD -- installation agent-instructions task-cycle` is empty, so their covered sources have not changed. Slice 7's earlier project-level 227 is superseded by the 229-test result, not added to it.
- Real acceptance uses the original whole plan and disposable product clone, with both start and completion proposals for task 3 and reachable archive commits. The retained actual host result establishes its merged request separately. Source plan/definition hashes, original HEAD and status comparisons all remain equal. No private acceptance rerun was needed: reader behavior has not changed since that evidence.
- Slice 1 independently removed the fetch in an isolated copy; the freshness/composed-transition test failed on missing proposals, then the unbroken focused check passed. No later reader change invalidates that proof at this HEAD. Did not duplicate it.

The new subprocess check observes actual Python process-start audit events in the reader interpreter, records a nonempty trace, identifies the executed program and uses real remote-ref movement as a positive control. It does not read production code to produce its expected Git-only answer. Its operational-failure fixture fails remote lookup before fetch; this is disclosed and it still meaningfully checks a non-Git fallback on that observed error path. Windows command-line parsing and normal success/error starts are covered; a native unaudited start or an impostor executable named Git is not established by this instrument. These are explicit limits, not evidence of an actual current violation. The current production path starts Git directly.

R2's first deliberate break remains **pending after independent assessment and settlement**, as WAY-149 requires. This review inspected the final check quality and current PASS evidence but did not perform or claim that acceptance. If assessment changes the check or covered behavior, review the changed result before the break; otherwise reuse this review.

## Declined to judge and limits

- Live multiagent compliance with the refinement instructions: no live trial was provided or run; only the static scenario review above is established. Existing tests are not represented as agent-behavior tests.
- PR-host state computation by the reader: deliberately outside its Git-only contract; evaluated the explicit lead fallback instead. The retained real host result establishes the acceptance example, not every possible host integration.
- Repository-wide task-name uniqueness across distinct plans: current source promises uniqueness within a plan and uses that stable name for the reserved archive path. No new cross-project identity scheme was invented in this review; conversation identity checks do not prove archive identity for reused names. Treat any reused archive namespace as a source/plan reconciliation issue rather than assuming this reader can distinguish it.
- Approval authenticity, meaning of human answers and broad semantic collisions: syntax/fingerprint checks cannot establish these; workflow retains human gates. This code review does not substitute for the independent foundation assessment.
- Revalidation of unchanged external research/tool behavior facts: outside this code change; their citations were treated as existing constraints, not freshly verified current facts.
- Full gate, flow coverage, missing/TODO methods, final integration-tip search and merge approval: not established here. Existing guards/suites are partial checks, and the pre-main integration route still applies. No broad green suite was rerun without a new concern.

## Recommendation

Use the one final fix wave for R1, with an ordinary ANSI-output regression and focused affected verification. Then perform the one scoped rereview. Preserve the distinct independent foundation assessment and the post-assessment R2 deliberate break. At this HEAD, the implementation is substantially aligned with its sources, but the verified reader failure prevents a ready verdict.
