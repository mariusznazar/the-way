# Slice 1 execution — shorten the task cycle

Status: Slice 1 implemented, focused checks completed and committed; returned before review.

## Inputs and boundary

Worktree: C:/Storage/repos/the-way-wt/shorten-task-cycle.
Branch: task/shorten-task-cycle. Slice starts at
dba4cf81769446484d68b6260424260f7f1da85e, after the completed foundation stage.
This cycle follows its original base process d04c3feb1a47e0ffc9a3b2354c23aacafe25c74b;
the changed instructions govern future adopters, not this run.

Read the executor handoff, frozen task, reviewed spec, final plan, final size report and
foundation report. Read this worktree's AGENTS.md and agent-instructions/README.md,
the three changed files, the full glossary, all Slice 1 Read ranges in the finished
foundation, slice_size.py and test_slice_size.py. The ranges include the final WAY-148
and WAY-149 entries. Read the Obsidian rulebook before the skill-conventions reference;
the latter was read in full. No vault file is changed.

F7 is resolved without a new invariant/check. Foundation and invariant tests remain
read-only. Only the three planned instruction files are product writes. This report
and any command evidence stay in the ignored cycle record. No subagent, review,
subsequent stage, push or cleanup is dispatched by this executor. No executable
behavior or tests are changed, so instruction cases and existing checks provide the
planned verification without phrase-matching tests.

## Before comparison — dba4cf81769446484d68b6260424260f7f1da85e

The following comparison was written before changing any of the three files. Paths
and line numbers name their version at the slice-start commit.

| Spec case | Existing instructions and record | Verdict |
|---|---|---|
| 1. Normal completion | task-cycle/skill/SKILL.md:86 stores full handoffs and reports and :89 records events; :97 gives dispatch duties. No required short return or bounded routine reading. task-cycle/plan/SKILL.md:124 returns the size report itself; record_template.md:36 has events but no explicit handoff path. | Partial; add file routing, short return and resumption contract. |
| 2. Failed/unchecked check or unresolved decision | skill/SKILL.md:214 records failed and unchecked checks and :203 returns questions, but does not require the short return to expose every relevant concern, evidence reading before rulings, or repair before dependent dispatch. | Partial; preserve check reporting and add those duties. |
| 3. Costly decision-required invariant | skill/SKILL.md:162 requires the foundation step and :179 separates authors; :218 broadly writes uncovered behavior. It does not yet state the new classification's explicit safeguard for WAY-12/22. | Required invariant remains required; add the safeguard against misuse of the new criterion. |
| 4. Replaceable detail | skill/SKILL.md:218 says to write every discovered item binding after merge; record_template.md:79 has an unqualified behavior finding. No requirement/settlement criterion or reason for keeping a detail in ordinary tests. | Unmet. |
| 5. Assessment changes return-step check | skill/SKILL.md:225 sends the new check to its break before assessment at :228; :233 reruns checks/review for settlements, including another break for assessed-entry/test changes. | Unmet; first acceptance break must follow assessment settlements and final-check review. |
| 6. Earlier invariant check | skill/SKILL.md:210 keeps the code review's deliberate break before step 11. | Met; preserve that earlier point. |
| 7. Independent slices, skill forbids parallel executors | plan/SKILL.md:93 cuts reviewable slices and :103 orders dependencies, but neither plan nor cycle requires identifying independence despite the execution restriction. | Unmet. |
| 8. Shared file/dependency/mutable state | plan/SKILL.md:103 allows shared-file slices only with dependency and skill/SKILL.md:80 forbids concurrent writers in one worktree. No explicit execution ruling about shared state or independent review ranges. | Partial; keep those protections and require the ruling. |
| 9. One slice | skill/SKILL.md:198 makes the single review both slice and whole-change review; plan/SKILL.md:94 prohibits slices for their own sake. | Met; preserve one review and state no parallel slice work. |

Additional preserved boundaries: whole-task read at skill/SKILL.md:25; source duties
in its Inputs and authority; separate sentence/check/code authors at :179; filtered
assessment inputs at :228; reconciliation invalidation at :244. The chosen transfer
contract must not replace any of them with a summary or an operational assessor packet.

## Implementation choices and costs

| Choice | Alternative rejected | Costs and limits |
|---|---|---|
| Replace the dispatch paragraph with one reusable file-transfer contract and keep stage boundaries in place. | Add separate templates, a second ledger or stage-by-stage duplicated transfer text. | Manual review still establishes completeness; leaving the old wording permits full routine messages and incomplete returns, while duplicated contracts drift. |
| Replace step 11's old broad classification and break-before-assessment sequence in place. | Add exceptions after the obsolete instructions. | The new classification needs source judgment; retaining both orders or both criteria would leave contradictory instructions. Required checks still cost work. |
| Extend current Events, Spec and plan, Return step and Independent assessment sections. | Add a parallel coordination or verification ledger. | Existing sections become slightly fuller; a second ledger duplicates state and resumption obligations. |
| Keep names, descriptions and paths byte-identical. | Regenerate discovery entry points without a discovery change. | No entry-point write is needed; existing gate checks still verify discovery. |

## After comparison

The resulting instructions meet all nine cases. These references name the final
instruction text in the committed slice; the commit is recorded below.

| Spec case | Result and concrete evidence |
|---|---|
| 1. Normal completion | task-cycle/skill/SKILL.md:97 requires a file handoff and routing message; :107 requires the complete stage report with the borrowed method's duties; :115 requires short status/paths/commits/check results; :121 records events and choices before dependent dispatch and resumes from record/files/commits rather than history. task-cycle/record_template.md:39 records the handoff/report paths and short result. task-cycle/plan/SKILL.md:139 follows this return contract rather than returning the full size report in the message. |
| 2. Failed/unchecked check or unresolved decision | task-cycle/skill/SKILL.md:115 requires failed/unchecked work and every concern affecting dispatch in the short return, with concrete blocking decision/evidence; :121 requires authoritative sources and report evidence before a ruling; :126 repairs missing/incomplete reports and stale paths/ranges before dependent work. task-cycle/record_template.md:43 records these repairs and :80 keeps unrun checks unchecked. |
| 3. Costly decision-required invariant | task-cycle/skill/SKILL.md:261 explicitly preserves decision-derived invariants under WAY-12/22, existing invariants, accepted rows and applicable projected entries. No cost exception is introduced. The foundation step's existing entry/check duties remain intact. |
| 4. Replaceable detail | task-cycle/skill/SKILL.md:255 asks whether later change violates a requirement or settled product rule. A replaceable detail stays in ordinary tests and the change description; actual candidates receive their source/reason and paths, not an inventory of all functions. task-cycle/record_template.md:89 records those classifications. Required decisions/facts/terms/part-map entries remain part of the search. |
| 5. Assessment changes return-step check | task-cycle/skill/SKILL.md:270 first runs the new check on the product; :273 gives the single filtered assessment; :279 reruns affected checks and code review for changes to code, assessed entries or invariant tests; :283 requires review of the final check before a break written from the final sentence by a reviewer who did not write the check. :286 reuses an affected review covering that check; :287 rejects a pass/assessment alone and an undetected break; :288 requires restoration before the clean run and repeats affected verification for later corrections. task-cycle/record_template.md:100 records settlement/reruns and :104 links final acceptance evidence. |
| 6. Earlier invariant check | task-cycle/skill/SKILL.md:245 explicitly retains earlier check acceptance and deliberate-break points and :248 limits step 11's changed order to return-step checks. :291 reiterates the earlier points; task-cycle/record_template.md:110 preserves them in the evidence instructions. |
| 7. Independent slices, skill forbids parallel executors | task-cycle/plan/SKILL.md:75 adds one Independence and execution section; :100 recommends useful independent slices regardless of skill; :112 derives opportunities from dependencies/write sets and identifies the adopted Superpowers restriction. task-cycle/skill/SKILL.md:171 records the orchestrator's ruling before execution and sequential execution under 6.4.1, without suppressing the opportunity. task-cycle/record_template.md:26 holds both recommendation and ruling. |
| 8. Shared file/dependency/mutable state | task-cycle/skill/SKILL.md:172 requires dependencies, shared files or mutable worktree/test state, separately assessable review ranges and method restrictions; :174 rejects different files alone as proof. The existing no-concurrent-writers rule at :80 and dependency order remain. The planner's original same-file dependency rule remains at task-cycle/plan/SKILL.md:110. |
| 9. One slice | task-cycle/skill/SKILL.md:234 still makes the one slice's review the whole-change review. :177 and task-cycle/plan/SKILL.md:116 say one slice has no parallel slice work; :101 rejects artificial splitting. No additional whole-change review of an unchanged range is added. |

Preserved safeguards: the full-task read remains at task-cycle/skill/SKILL.md:25;
the reusable contract explicitly preserves required whole-entry/file reads at :101,
and existing input/diff/check/review duties at :125. The separate sentence/check/code
authors remain in the foundation step and are explicit again at :269. The independent
assessor receives only permitted commit/diff/files at :273, explicitly excluding the
operational handoff and all author material. Step 12's reconciliation, collision
search, affected-review and independent-assessment invalidation is unchanged at :299.
No scheduler, parser, validator, telemetry, compaction, executable behavior or test
was added. Names, descriptions and paths are unchanged; no entry-point regeneration
is required.

Changed product files:

- task-cycle/skill/SKILL.md — reusable handoff/report and short-return contract,
  evidence-reading/repair rules, execution ruling, return-step classification and order.
- task-cycle/plan/SKILL.md — independent-work recommendation section and file-based return.
- task-cycle/record_template.md — paths/coordination, execution ruling, classifications,
  and assessment/final-break evidence in the existing sections.

## Commands and results

Initial read/status commands completed successfully except the explicit upstream probe:
`git rev-parse --abbrev-ref --symbolic-full-name '@{u}'` exited 1 because this branch
has no upstream. This is not a mismatched upstream warning and changes no configuration.
Initial working tree was clean. Remote is https://github.com/mariusznazar/the-way.git.
Command output truncation during batched reads was repaired by smaller complete/ranged
reads before editing; no conclusion relies on omitted output.

All three planned focused checks completed twice: once after the main edit, then
again after restoring explicit question routing and the unchanged broad no-deferral
duty in the replacement text. No product check failed. No warnings or unchecked
results were emitted by these focused runs.

| Command/check | First result | Final result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | exit 0; 41 tests, OK, 0.593 s | exit 0; 41 tests, OK, 0.558 s |
| `python -B gate/run_tests.py gate` | exit 0; 98 tests, OK, 20.135 s | exit 0; 98 tests, OK, 20.403 s; includes existing critical-flow checks |
| `python -B task-cycle/slice_size.py .runs/task-cycles/shorten-task-cycle/plan.md` | exit 0; one slice, three change files, 160577 characters, 64231 estimated tokens, fits | exit 0; one slice, three change files, 160619 characters, 64248 estimated tokens, fits |
| Inline `python -B -` parser compatibility check | parsed real plan and new template successfully before a separate newline assertion failed in the combined command | standalone exit 0; real plan has one slice/three explicit change paths and Change/Read fields; extracted new template has one slice and unchanged placeholder path fields |
| Inline `python -B -` file-integrity check | two auxiliary assertion failures described below | standalone exit 0; original LF retained in all three files, no unexpected control characters, both skill frontmatters byte-identical to slice-start blobs |
| `git diff --check` | exit 0, no whitespace errors | exit 0, no whitespace errors |

The compatibility check reads the real plan and the Markdown template and calls the
existing `parse_plan`; it is a manual verification command, not a new product test.
The second-level Independence and execution section leaves Slice/Change/Read syntax
valid. The final size result is larger than the planner's pre-edit estimate because
Change files are also read; the updated change still fits comfortably. The planner's
existing size artifact is not overwritten by this executor.

Auxiliary failures, retained rather than hidden: the first combined parser/integrity
command exited 1 after parser assertions passed, because it asserted that a git blob
must have CRLF. A second integrity attempt asserted that the worktree must have CRLF;
its Python subcommand exited 1, although the enclosing shell returned 0 after later
successful diff/line-location commands. Both were faulty assumptions about line
endings inferred from PowerShell's displayed output. The final standalone integrity
command detects LF/CRLF from bytes, verifies unchanged style against the starting
blob, scans actual bytes for controls and compares frontmatter without that assumption;
it exits 0 and confirms LF throughout. The edit scripts themselves selected and retained
the existing file endings with newline='' before these probes. No product file was
changed to fix the probes.

Commit: 19c9cfee3fce8284712e2e1e2273fd1f5ce6a48f —
feat(task-cycle): Apply the shorter cycle contracts.
The commit's parent is dba4cf81769446484d68b6260424260f7f1da85e.
`git add -- task-cycle/skill/SKILL.md task-cycle/plan/SKILL.md task-cycle/record_template.md`
and `git diff --cached --name-only` both exited 0; the staged list was exactly those three
paths. `git commit -m "feat(task-cycle): Apply the shorter cycle contracts"` exited 0 and
recorded 3 files, 140 insertions and 48 deletions. `git status --short` after the commit
was empty; the ignored cycle reports remain available. The author address is the intended
private-repository address. No push, review dispatch, next stage or cleanup was performed.

## Concerns and unchecked work

Instruction comparisons and part/critical-flow tests are partial evidence, not a proof
of future agent behavior or measured time/token savings. Foundation authoring checks
and their warnings/TODO/unchecked work remain in reports/foundation.md; this slice
does not rerun or relabel them. Independent code review, the one foundation assessment,
the return step and integration-tip reconciliation remain root-owned stages after this
executor returns.
