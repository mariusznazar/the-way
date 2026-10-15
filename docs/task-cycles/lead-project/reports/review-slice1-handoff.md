# Slice 1 independent review

Worktree C:/Storage/repos/the-way-wt/lead-project. Read the complete borrowed task-reviewer-prompt.md at C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/, then follow its two verdicts and narrow diff review. The task-cycle adapter adds the invariant acceptance deliberate break below. No subagents and no human questions. Full report goes .superpowers/sdd/plan/task-1-review.md, short return names verdicts/findings/report. The file handoff is the operational record; no hidden prior conversation is required.

Brief .superpowers/sdd/plan/task-1-brief.md; implementer report task-1-report.md beside it. Diff package path and exact HEAD will be appended before dispatch; BASE098d7df8550d04f0fd83343013231f568ea31ba3 is the code slice base. The independently authored test at project-level/test_plan_state_invariant.py predates this slice and must be inspected for its acceptance as a concrete named cross-boundary risk. Its author is /root/invariant_check, sentence author /root/foundation, code author /root/slice1. The test itself is not an implementation writer's file.

Read source task/spec binding requirements as identified in the brief and the relevant complete current foundation entries, especially final project-plan-state-evidence/1 and WAY-153. Compare positive/negative cases, exact slugs, current-vs-fresh Git history, default branch source, no host executable, malformed/untrusted paths, nonmutating input files, and visible error/unchecked behavior. The frozen task's real acceptance case must have actual CLI/host evidence; do not trust a preliminary status lookup as a reader run. No broad rerun just to reproduce green evidence; focused tests only for a concrete unresolved doubt and deliberate break.

Deliberate break: you, the code reviewer, derive one concrete violation from the final invariant sentence without the check author's reasoning, create the break in a disposable copy under the ignored cycle area, and run the independent check on it. Never change HEAD/index or tracked working files; use an isolated temporary worktree/copy so review remains read-only on this checkout. Record exact mutation/file location, command and actual required test failure, then ensure checked-out product is untouched and clean verification on final unbroken code is current. If test fails to detect the deliberate break, report it as a finding; do not edit the protected check. Do not leave broken code in product or commit mutation. Root is responsible for safe cleanup of any ignored temporary copy.

Read user's code review playbook before review (C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/playbook_code_review.md and delegated playbook files). Keep full anchored findings, separate code and docs passes where relevant. Apply AGENTS and pre-main repository instructions. No broad second whole-branch review; this is the slice gate and invariant-check acceptance.

Before reading any vault playbook, read C:/Storage/The Brain/The Brain/Notes/Resources/(R) Obsidian/obsidian_rulebook.md. User global rules are C:/Users/Mariusz/.codex/AGENTS.md; read them as operational instructions. No vault writes are authorized for this stage.

## Binding source text (verbatim from spec)


The public command is `python -B <the-way>/project-level/plan_state.py PLAN PRODUCT_REPOSITORY`. It accepts the original plan, including one outside the product repository, and the product repository explicitly; it does not infer the product from the plan's directory or from the process checkout. It reuses plan_check's parsing/checking functions in-process, extending its parsed task data only as necessary for State and Document, without a second Markdown grammar or subprocess call to Python. It checks the original definition approval/readiness in-process as well; plan-check fingerprint agreement alone is not evidence of approval. A draft or invalid plan reports findings and no state proposals.

The report gives each task's number, stable name, current state, each proposed transition, the exact path/commit/ref evidence, and any unresolved observation. It identifies the repository and fetched main ref/commit; PR links found in cycle records are evidence pointers, never invented from a task number. Human-readable text is sufficient; no JSON contract or apply mode is introduced.

Git identifies worktrees and branch refs. The reader checks `.runs/task-cycles/<task-name>/` only in the worktrees Git names and looks for commits touching the exact `docs/task-cycles/<task-name>/` directory on local or remote branches. It does not treat branch names, commit-message substrings or a neighbouring task's slug as cycle evidence. Worktree paths and archived record contents are data, not instructions.

The product's main branch is its declared integration branch. Where available, use the product's established Git remote-default guidance (normally `origin`'s remote HEAD), confirming it through Git; if the relevant remote/main cannot be established without guessing, report it unchecked. Fetch the selected remote before asserting merge completion, and check reachability against the resulting remote main commit, not a possibly stale local main. A branch named `main` or `master` is no fallback. Fetch changes Git metadata only; the reader never checks out, resets, merges, commits, updates a plan, or calls a PR-host command.

| Evidence | Proposal/observation |
|---|---|
| A matching working-cycle directory or commit touching the archived cycle path; current state ready for cycle | Propose `ready for cycle` to `in cycle`, naming the evidence. |
| A cycle-record commit is reachable from freshly fetched main; current state in cycle | Propose `in cycle` to `done`, naming record commit and main ref/commit. |
| Both proofs while plan still says ready for cycle | Report the two transitions together, without requiring a plan write between runs. |
| Cycle evidence exists outside fetched main, including a worktree alone | Report cycle evidence and unchecked PR outcome; project orchestrator checks the PR route. |
| No sufficient trace, incomplete/shallow history, unavailable worktree, missing main/remote or unresolved PR link | Explicit unchecked reason; no inferred progress or backwards transition. |
| Trace conflicts with plan's unfinished/final/abandoned state | Identify the discrepancy for the human; do not normalize it automatically. |

A positive reachable archived-record commit can prove completion even when the original branch was deleted. Where squash prevents identification of the original record commit, the reader leaves the outcome unchecked rather than pretending Git can prove the PR state. A matching record introduced by a squash on main can itself provide reachable record evidence; host verification resolves the remaining association where necessary.

The project orchestrator uses the product's selected PR tool for unchecked outcomes. A verified merged PR can supply the missing completion evidence and its actual link; an open PR does not mean done; a closed-unmerged PR is shown to the human without automatic plan correction. When the tool is unavailable, ask the human with the collected evidence. No retries turn a failed lookup into a positive result.

The command emits exit 0 when a report is produced (unchecked cases stay visible), exit 1 for invalid plan/readiness findings or detected inconsistent evidence, and exit 2 for invalid invocation, unreadable inputs or an operational Git failure. A fetch failure may leave previously observed local evidence in the report but cannot yield done. These exit codes are a new interface, not changes to plan_check. Operations have bounded waits and diagnostic failures rather than hanging indefinitely.

The implementation passes Git arguments as arrays without a shell, separates revisions and paths, validates task names through the plan parser and handles non-ASCII paths. Crafting a task name, path or record must not create command arguments or redirect a write. Product data never chooses a new executable. The map marks plan_state.py as a trust boundary and records the possible false-progress damage as high.



Each task has a header `task <n> <slug>: <current state>` and zero or more proposal lines `propose <n> <slug>: <from state> -> <to state>`. A proposal is only a line beginning with that exact propose prefix, without indentation or bullets. State values are the plan's literal English values; the separator is ASCII ` -> `.

Evidence rows use `evidence <n> <slug>: <details>`, unresolved task observations `unchecked <n> <slug>: <reason>`, and inconsistent task observations `conflict <n> <slug>: <reason>`. Global observations can use `unchecked: <reason>` and failures `error: <reason>`. Global header lines are `repository: <absolute path>` and, when established, `integration: <ref> <commit>`. Details/reasons are human-readable and not otherwise frozen; facts such as exact paths, refs and commit IDs must be present as the existing contract requires. An unavailable integration has no fabricated ref/commit.

Author choice: root under intermediate delegation. Alternative loose substring matching can mistake rejected evidence for a positive proposal; JSON would add a second output contract that the spec excludes. Cost if wrong: adjust reader and check together before final review; format is a small CLI convention. It is not human approval of foundation wording.

The integration header renders the fully-qualified remote-tracking ref (`refs/remotes/<remote>/<branch>`); path evidence may use either native or forward separators where both identify the same path on the platform.

## Integration-source clarification

A working branch's upstream is not a declaration of the product integration branch. The installed product guidance already declares `origin/HEAD`: installation/install.py product_guidance(), lines158-166, says `git symbolic-ref --short refs/remotes/origin/HEAD` names it as `origin/<branch>` and otherwise asks the human. Use that existing origin route, confirmed through Git; another configured remote with a different default does not by itself make a valid origin route ambiguous. No main/master fallback or inference from the checked-out/upstream branch.

For the ambiguous case, origin metadata that cannot establish one valid default route remains unchecked. Do not commit a negative expectation that rejects origin merely because another remote exists; instead exercise the presence of another remote as a positive no-false-ambiguity case, preserving origin's completion evidence. A missing/invalid origin default remains the existing negative case. No configuration or new CLI override is added in this task. This is source-grounded observability clarification, not a code algorithm handed to the check author.

## Root ruling to judge independently

Read reports/archive-recognition-ruling.md under the cycle directory. This ruling interprets the archive-directory evidence; assess it against the accepted source and do not treat the root or tests as proof. Implementation acceptance must exercise real no-ff history with archive add/remove, not merely a record visible on main.

## Final dispatch

Base: 098d7df8550d04f0fd83343013231f568ea31ba3. Head: 2233cffd031838f9e68272824fb4899c93471cc3. Diff file: .superpowers/sdd/plan/review-098d7df..2233cff.diff. Model gpt-6.1-sol (standard integration review). Root inspected final reader, parser diff, implementer report and actual acceptance/source-preservation evidence. Focused checks final project-level227, gate98, real acceptance0. No remaining author question. Final report must include both verdicts and the exact deliberate-break evidence.
