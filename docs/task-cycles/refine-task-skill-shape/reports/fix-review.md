PASS 8f26dd665897d56da1b50cd83514484035aec0c4

# Independent review of the one fix

Range: `9f9001cf51812cdcfbbc16b12c819571e1769454..8f26dd665897d56da1b50cd83514484035aec0c4`.
R1, R2 and R3 are fixed. No new blocking defect found. One new Minor finding, M4, below;
the three prior Minor remarks remain carried to the request in their original wording, with the
current-state qualifications below. There are no out-of-scope findings. No finding was contested.

This is the bounded fix review, not another whole-change review. The original report remains at
`C:/Storage/repos/the-way-refine-task-skill-shape/.runs/task-cycles/refine-task-skill-shape/reports/review.md`.
The frozen task, both review handoffs, blocking findings, fix report and updated assessment were
read, and the fix diff and head were independently checked. Prose and code/tests were reviewed in
separate passes. No tracked file, index or branch was changed.

## Dispositions of the blocking findings

### R1 — fixed

`project-level/task/skill/SKILL.md:29` sends every invocation through `read_sources.md`.
`read_sources.md:13` now states the approved-definition condition independently of either task
relation and requires the readiness command before relying on approval, with findings returned to
`define-project`. A plan member still reads `project_plan_task.md`; a source-only task still reads
`source_only_task.md`, which no longer owns the only copy of this broadly applicable instruction.
An orchestrated plan member first reads its orchestration rules and then takes the same common
source-reading route. Independent tasks with no definition do not acquire an irrelevant command.

This repairs the lost reach rather than substituting the plan check for the readiness check.
Their separate purposes and the original missing-approver counterexample remain valid; the
implementation of either checker is unchanged. I compared the new common instruction with the
original baseline wording and its task-relation context. No additional live refinement run was
performed: the evidence establishes the instruction's reach and required timing.

### R2 — fixed

The revised main file keeps purpose, process location/prefix, the orchestration pointer, the
shared acceptance and document-scope rules, the six-step route and the single surviving-exclusion
instruction. Each common step names an adjacent procedure: `read_sources.md`, `draft.md`,
`resolve_gaps.md`, `carry_foundation.md`, `find_settlements.md` or `final_review.md`.

The concrete counterexamples are now at their steps: the Human-actions procedure is in
`resolve_gaps.md:23`, and the show/propose/apply/no-move procedure and readiness checklist are in
`final_review.md:3` and `:7`. The assessment no longer justifies these placements by shortness or
eventual use in every mode. It names their actual steps/conditions and recognizes that they contain
multiple instructions. Moving the document-scope boundary into the shared opening is appropriate:
it constrains drafting throughout the route. The one-instruction exclusion rule remains beside
the step-4 pointer as the accepted exception permits.

I matched the removed main-file paragraphs to all six new files, including the text around their
conditions and returns, not just the presence of filenames. The final-review file preserves
unresolved metadata, newly reached parts, final complete-document approval, manual Status and
orchestrated Status ownership. Main-file links also expose the variant siblings directly, so
reading them does not rely on discovering an otherwise unnamed nested reference. I found no lost
or narrowed rule introduced by these moves. The new table's presentation defect is M4; it does not
reopen the repaired placement defect.

### R3 — fixed

`installation/test_install.py:21` derives `NAMES` from all installed skills. It now has 20 entries,
including the three previously omitted ones. The test at `:81` builds the complete agreed literal
sentence with the path, asserts its presence and still rejects the old phrase. The same loop
checks byte equality of each Claude/Codex entry-point pair. Its expected sentence is independent
literal wording, not the generator's returned text used as its own oracle.

The focused integration test passed. An additional scratch probe executes the actual current
sentence assignment and assertions, extracted from the test's AST, for all 20 generated skills:
all correct outputs pass, and all 40 mutations fail (one changing `in full and follow it` to
`partially`, another appending the prohibited old instruction). Thus the previously demonstrated
false positive is closed and rejection of the old instruction is independently exercised.

## New Minor finding

### M4. The rewritten assessment replaces the reviewed material with summaries and stale ranges

**Grade / scope / thread:** Minor; in scope; new thread introduced by the assessment rewrite.

**Anchor:** `C:/Storage/repos/the-way-refine-task-skill-shape/.runs/task-cycles/refine-task-skill-shape/reports/assessment.md:43`;
also `:53` and `:71`.

**Do wklejenia:** The rewritten judgment table now describes fragments instead of quoting the
material it judges, and some ranges do not locate the described text: `read_sources.md:18–27`
does not include its guideline-reading paragraph, while `orchestrated_mode.md:41–54` extends beyond
that 48-line file and misses the exact-result paragraph above it. Restore the quoted fragments
alongside the corrected verdicts and check their anchors before using this table as the request's
assessment.

**Dlaczego to zgłaszam:** This table is the material the human is meant to use to inspect the
placement decisions. The previous assessment supplied full quoted fragments; the new version's
Human-actions row, for example, supplies only “Human-actions identification, placement, waiting and
completion”. That prevents the reader from assessing whether the fragment has the actions the
verdict relies on without separately opening the file. `instruction-files/judging.md:15` explicitly
calls for the quoted fragment with its address, and the user-facing review convention likewise
requires the material, not a summary of it.

The source addresses also need a pass: the guideline paragraph actually starts at line 28 of
`read_sources.md`; the orchestration exact-result paragraph starts at line 33, and its file ends
at line 48. This is not evidence that the skill lost those rules—I read and matched them in the
source, and R1–R3 are repaired. It is a presentation and traceability defect in the assessment to
carry to the request, so I grade it Minor. The repair is to preserve the current step/variant
judgments while supplying the actual text and accurate addresses, not to reverse the source moves.

## Prior Minor remarks carried to the request

Do not replace the original M1–M3 text with these observations; retain their complete wording from
the first review and attach these current-state dispositions where needed.

- **M1 remains.** WAY-128's enumeration at `foundations/decisions.md:2997` is unchanged. No foundation
  file changed in the fix.
- **M2 is partly addressed incidentally.** The rewritten assessment no longer contains the false
  statement that semantic proposals were unauthorized. It still does not document whether such
  proposals were considered and none warranted; the author's report says the old Minor remarks
  were not separately fixed. The prior remark therefore remains useful as a qualification of the
  assessment, without inventing a semantic proposal or turning this into a new blocker.
- **M3's concrete reporting defect is addressed by the rewrite.** The new count table says
  “Conditional guideline file when triggered”, and its judgment row for `guideline_findings.md:43–47`
  expressly includes a newly reached part at step 6 as well as a remaining finding. It no longer
  says a finding is the only trigger. The original comment should still be carried as requested,
  with this qualification; not editing the old review does not mean the defect necessarily remains
  in the new artifact. Source placement alone would not have repaired M3, but the changed reporting
  does.

There are four Minor review records across both reviews, one new. The PASS above means no blocker
remains; it does not silently discard the request's required review remarks.

## Counts and source fidelity

The current 11 Markdown files in the skill directory are fully accounted for by the seven common
files and four conditional/variant files. Independent complete-path words are 2,007; manual
plan-member words 2,212; orchestrated plan-member words 2,782. A guideline branch adds 453 words.
Source-only is 2,172 before that conditional addition. The unchanged task template is a separate
1,580 words. These reproduce the updated assessment. Before the overall change, the common skill
file was 2,933 words.

These are total words across the skill files read on the stated complete path, not a measurement
of how long rules are carried in a real session or all context loaded from product-specific
sources. The main file is 396 words, with the procedures reached at their numbered steps. No live
refinement trace validates actual reading or compliance behavior.

WAY-256, WAY-257 and WAY-259 were read whole at this head and compared with the fix. The earlier
selected foundation remains applicable and its content is unchanged by this range. The accepted
empty product-guideline selection and place-only treatment of the task template remain honored.
The task's Python boundary is respected: this fix changes only the sentence test and its skill
population; the generator is unchanged since the first reviewed head. No new invariant or invariant
assertion was introduced or changed; the enclosing integration test still carries the pre-existing
`installation-claude-guidance` checks unchanged.

The author's weakest-point check now addresses the observed failure: it compares the original
paragraphs with their destinations and reviews the retained main file under the actual step
criterion. The new source passes that comparison. The assessment-format issue M4 is distinct from
whether the source preserves and defers the procedures.

## Checks

All commands ran from `C:/Storage/repos/the-way-refine-task-skill-shape`.

| Command | Result |
|---|---|
| `git rev-parse HEAD` | Exit 0; `8f26dd665897d56da1b50cd83514484035aec0c4`, confirmed before and after review. |
| `git log --oneline 9f9001c..8f26dd6` | Exit 0; one fix commit. |
| `git diff 9f9001c..8f26dd6` | Exit 0; reviewed all nine changed paths. |
| `git diff --check 9f9001c..8f26dd6` | Exit 0. |
| `git diff --exit-code 9f9001c..8f26dd6 -- installation/install.py foundations/decisions.md project-level/task/template.md` | Exit 0; all three unchanged in the fix. |
| `python -B -m unittest installation.test_install.InstallTest.test_preview_apply_rerun_and_preserve_foundation` | Exit 0; 1 test passed in 6.392 seconds, all 20 generated entry-point pairs checked. |
| `python -B .runs/task-cycles/refine-task-skill-shape/reports/reviewer_fix_probes.py` | Exit 0; 20 correct outputs pass, 40 mutations rejected; complete 11-file count inventory and reported totals verified; main-file Markdown pointers resolve. |
| `git status --short` | Exit 0; tracked worktree clean. |

The scratch probe is a new ignored review artifact and leaves the original pre-fix probe intact.
The latter's assertion of three missing skills is historical evidence, not a current product test;
I did not treat its stale expected failure as a regression.

Trust-boundary scrutiny: the installer implementation, ownership recognition and all its file
guards are unchanged by the fix. I compared that diff with the prior crafted-input evidence for
incomplete ownership markers, conflicting product-owned wrappers and a symlink to an external
target. Their prior checks passed. No changed executable path or unresolved safety concern calls
for rerunning those same cases; the affected output test was rerun. No actual product installation,
pin movement, external effect or irreversible operation was performed.

The full gate is intentionally not repeated here; the orchestrator owns it after this review.

## Reaches

- Newly added common-step siblings: read whole and matched against the removed main-file text to
  verify R1/R2 and the absence of newly lost conditions or return routes.
- `instruction-files/judging.md`: reread the full output contract while checking the rewritten
  assessment, which establishes M4. The previously read skill and kind instructions remain the
  method for assessing placement.
- `task-cycle/skill/foundation_step.md`: read whole to check the author's claimed division between
  refinement's selective reading and the later foundation search; `find_settlements.md` preserves
  the earlier boundary.
- `installation/test_install.py`: traced the changed population and enclosing integration test;
  used its actual assertion AST in the scratch probe.

No further foundation or guideline selection was needed beyond the dispatched and retained
material. No subagent was dispatched.

## Declined to judge

None.
