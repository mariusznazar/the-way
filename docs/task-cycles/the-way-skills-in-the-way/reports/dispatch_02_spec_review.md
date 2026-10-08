You are the spec reviewer of one the-way task cycle (`implement-task`, step 7). You did not write the spec.
Mariusz (the task owner) delegated intermediate choices to the orchestrator; report to the orchestrator only,
and never present anything as Mariusz's approval. One-off run on the-way itself before `main`; run brief:
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\run_brief.md`.

## Your job

Review `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md` against
the frozen task `…\the-way-skills-in-the-way\frozen_task.md` (Polish) and the current foundation of the task
worktree `C:\Storage\repos\the-way-skills-self` (`foundations/*.md`, at c64a6071384fb57cdb9d7e9db4560ddc43e3b355).
Find: requirements of the task the spec misses or meets only in part; behaviour the spec invents without a
source; contradictions with the foundation (decisions, invariants, part map, facts) or within the spec; designs
that will not work as written. Use as a lens the Superpowers 6.4.1 spec reviewer prompt
`C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\brainstorming\spec-document-reviewer-prompt.md`
(read it). Search the foundation yourself; the spec's list of entries is a claim to check, not proof.

Also verify these orchestrator observations — confirm or refute each with evidence:
1. §4.2 entry point: `git rev-parse --show-superproject-working-tree` and `--show-toplevel` run in the session's
   working directory. In a product, the session's working directory is the product root, which is not a
   submodule: the superproject check prints nothing and `--show-toplevel` prints the product root, so the guard
   would not fire and the root would be wrong. Does the text need to run them in the directory that holds the
   entry point (the skill's base directory), and what then happens under the Claude Code worktree fallback
   (§6, a worktree without `.claude/skills` offered the main checkout's entry points)?
2. §2 environment quotes came through a summarising fetch. Check the two pages (Claude Code skills page, Codex
   skills page) for the exact sentences the design relies on, and say which claims hold verbatim.
3. §7 probes: compare with an existing fact and probe for a web page (e.g. `claude-code-path-rules` in
   `foundations/environment_facts.md` and `probes/`), and with the environment-facts template
   (`elements/environment-facts/`). Is the proposed shape right?
4. §4.4/§7: the invariant's *Method* form, the flow test's location and its `flow:` line against existing
   invariants and flows (e.g. `wording-reaches-dependants`, `gate/test_wording_reaches_dependants.py`) and the
   invariants template.
5. §5.6: point 5 against WAY-27, `outbound-link-reach`, WAY-25, WAY-30, WAY-107. Is the collision real, and is
   the spec's handling (section without the path, the request asks Mariusz) consistent with WAY-25 and the
   cycle skill (`C:\Storage\repos\the-way-process\task-cycle\skill\SKILL.md`, foundation step paragraph before
   step 9 and step 11)?

## Boundaries

Read-only everywhere. Do not edit the spec or any file; do not run commands that change files. You may run
read-only commands (git, python -B of read-only scripts, web fetch). Do not use globally installed skills named
record-*, update-part-map, refine-task or critique.

## Return

Return your full report as text (the harness refuses report files from subagents): findings numbered, each with
severity (blocking / should fix / minor), the spec section, evidence (file:line, quote or command output), and
the fix you propose. Then a verdict: approved / approved after fixes / not approved.
