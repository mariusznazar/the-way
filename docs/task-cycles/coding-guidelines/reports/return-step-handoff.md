# Return-step handoff — coding guidelines (task cycle step 11, WAY-11)

## Delegation and boundaries

Mariusz asked for the-way's task cycle to take this task to a pull request; the orchestrator holds
his delegation. You are the return-step agent of this planned change. Never ask Mariusz anything;
a question goes back to the orchestrator in your report (the foundation step's limits on asking
apply). Worktree `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc`, HEAD `5a00041`.
Never use the Artifact tool or any publishing tool. Commit what you write, message in English,
ending after a blank line with:

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_01DYywki95VF5wQGh3SzcQZB

Do not push. Write only foundation files, through the-way's element skills (`the-way-record-*`,
`the-way-update-part-map`, read whole from this checkout). Write **no check, no test and no code**:
an invariant sentence you write or change gets its check from another agent and is broken by a
reviewer (WAY-69); return its identifier and say which check it needs.

## Inputs

- The real diff: `git diff 235b0b4..5a00041` (package `reports/sdd/final-review-package.diff`
  covers `235b0b4..2eabf42`; add `git diff 2eabf42..5a00041`).
- The cycle's choice log: the questions table of `cycle.md` (O1–O4, C1–C38) and the `Ruling:`
  lines of `reports/sdd/progress.md`; the frozen task `task-frozen.md` (rows of *Settlements to
  record*); the spec `spec.md`; the final review `reports/final-review.md` and the slice reviews
  `reports/sdd/slice-*-review.md` (their Minor findings, some of which touch foundation wording —
  e.g. ledger "Task 3: minor … guidelines-check-kind-index/1 says 'git lists' where it means 'git
  tracks'").
- Refresh the foundation selection by "Reading the foundation" (`elements/common/way_of_working.md`,
  WAY-150) for the real diff and the current foundation.

## What to do (WAY-11; cycle step 11)

Identify newly learned decisions, rules, uncovered behaviour, environment facts, terms and
part-map changes; compare the touched parts of the foundation with the code (product-guidelines,
installation, task-cycle, agent-instructions, decisions, invariants, glossary, part-map). For
uncovered behaviour ask: would changing it in a later task violate a requirement or a settled rule
of the product? If yes, preserve it with an invariant; if no, keep it as a replaceable detail and
name its ordinary tests or the change description. Record the candidates actually found with the
supporting requirement or settlement, or the reason for classifying a detail and its test paths;
do not inventory every function. Write every entry that binds after the merge (WAY-36) as the
foundation step writes (*Approved by* `Mariusz, merge of <request link>`); every other choice stays
one line in the choice table. No entry is deferred: an entry this request does not write is neither
proposed nor listed for later. Read the rows of *Settlements to record*: write a row the foundation
step missed (WAY-134). Write a new entry only for a rule none of them states. Search the whole
foundation (WAY-33) for what you write; run the guards (`--base none`, `--merge-onto none` where
available) and the tests of `elements/decisions`, `elements/invariants`, `elements/glossary`,
`elements/part-map`, `gate`, `product-guidelines`.

## Report

`reports/return-step.md`: candidates found and how each was settled (entry written with link,
or detail with test path, or nothing after search); entries written with old/new sentence for an
edited one and a Polish meaning sentence each; invariants whose check must be written or changed
(with the sentence); part-map changes; foundation compared with code; checks with commands, exit
codes and output paths (`return-*.txt`); commits with changed files and line counts. Return a
short message: status, commits, entries written, checks needed, questions.
