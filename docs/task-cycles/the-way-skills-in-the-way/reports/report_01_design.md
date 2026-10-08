# Report 01 — design agent (brainstorming)

Saved by the orchestrator from the agent's returned text: the subagent's write of this file was refused by the
harness ("Subagents should return findings as text").

## Summary

**Spec:** `spec.md` in this record.

**Classification:** architectural. The task adds a new mechanism, changes the paragraph in every skill that says
where the-way lies, and adds a check that runs on every change.

**Design:**
- **Entry points.** Each `SKILL.md` gets a short tracked file at `.claude/skills/the-way-<name>/SKILL.md` and an
  identical one at `.agents/skills/the-way-<name>/SKILL.md`. A new script, `agent-instructions/skill_entry_points.py --write`, generates them.
- **What each entry point does.** It reads its skill from `git rev-parse --show-toplevel`, the checkout or
  worktree the session works in. It names the other skills under the `the-way-` prefix. It stops itself when
  the checkout is a product's `.the-way` submodule.
- **Skill paragraphs.** The "Installed globally" paragraph in nine skills is replaced by two cases: the-way
  itself, or a product.
- **The test for point 4.** It runs on every change, through `python -B gate/run_tests.py gate`, and it does
  not use the generator to check itself.
- **Installer.** One sentence changes; it would otherwise point to the removed paragraph.

**Main finding:** point 5 collides with an approved rule.
- **The rule.** WAY-27 and its invariant `outbound-link-reach` forbid "a link into a private note collection" in
  any tracked file. Today no tracked file holds a vault or local path.
- **Provisional answer.** `## Backlog` names "the author's private notes" without the path. The path goes into
  Mariusz's personal instructions as a step after the merge.
- **The other way.** Putting the path in `AGENTS.md`, as the task words it, needs Mariusz to accept an exception
  to WAY-27. That blocks the request until he does.

**Other findings:**
- Claude Code loads skills nested inside a product's `.the-way` folder once the agent works on files there, and
  lists them as `.the-way:the-way-<name>`. That is why each entry point stops itself in a product.
- The five global links are junctions, not symlinks. The removal commands use `cmd /c rmdir`, which removes only
  the link. `Remove-Item` can delete inside the junction's target in Windows PowerShell 5.1.

**Foundation entries to write:** new decision WAY-127; new invariant `skill-entry-points`; part map: the
`agent-instructions` part changes and a new critical flow `skills-reach-the-way-sessions`; two new environment
facts with probes: `claude-code-project-skills` and `codex-repository-skills`. WAY-09 unchanged.

## Classification and path

Architectural. There is no existing route for a session on the-way to reach its own skills, so the task is not
bounded. Explored the context, answered questions from the sources (adapter rule), weighed four approaches,
wrote the design in sections and the spec, then self-reviewed it. No visual question came up, so the visual
companion was not offered.

## Sources read

- Dispatch and cycle files: the dispatch, `run_brief.md`, `frozen_task.md`, `cycle.md`.
- Method: brainstorming 6.4.1 `SKILL.md`, `spec-document-reviewer-prompt.md`, `visual-companion.md` (opening part).
- Task worktree, root and instructions: `AGENTS.md`, `CLAUDE.md`, `agent-instructions/README.md`, `README.md`,
  `.gitignore`, `.gitattributes`.
- Installer: `installation/install.py`, `installation/README.md`, `installation/test_install.py`.
- Skills: heads and mode paragraphs of all 11 `SKILL.md`; `task-cycle/skill/SKILL.md` lines 1–80;
  `way_of_working.md` lines 1–60; the Backlog parts of `definition_template.md` and the project-level and task skills.
- Gate and probes: `gate/run_tests.py` docstring, `gate/test_wording_reaches_dependants.py`, the
  `claude-code-path-rules` probe.
- Decisions: WAY-07, 09, 16, 22, 25, 27, 34, 35, 44, 45, 46, 52, 53, 55, 73, 90, 101, 107.
- Invariants: `repository-file-location`, `element-directory-contents`, `file-part-assignment`,
  `path-pattern-reach`, `left-out-file-assignment`, `skill-rule-source`, `script-*`, `derived-file-content`,
  `derived-subset-naming`, `generated-*`, `flow-test-location`, `invariant-method-form`, `invariant-test-break`,
  `flow-invariant-link`, `gate-reported-set`, `flow-test-run`, `outbound-link-reach`, `fact-dependants`,
  `decision-guard-stale-reference`.
- Rest of the foundation: the part map from `elements-common` to the end; the facts `git-path-patterns`,
  `gitignore-paths`, `context-file-effect`, `claude-code-path-rules`; the glossary headings.
- Other branches: `git log c64a607..origin/foundations` (PR #6 and #7), and the diff of the
  `the-way-instruction-files` worktree.
- Environment: Claude Code skills docs and Codex skills docs (Codex redirects to learn.chatgpt.com/docs/build-skills),
  both read through a fetch that summarises, so the quotes need a verbatim reading before fact entries are
  written; `Get-Item` on the five links; `claude --version` 2.1.293; git 2.55.0.windows.3; `git grep` for local
  or vault paths: none found.

## Verified facts and corrections to the dispatch

- The five global links are junctions.
- Claude Code loads nested `.claude/skills/` folders once it works on files in them. When names clash it keeps
  both, the nested one as `<subdir>:<name>`. So the-way's own entry points will load inside products'
  `.the-way`, which neither the task nor the dispatch anticipated.
- In Claude Code a personal skill wins over a project skill of the same name. Codex shows both. The prefix is
  therefore required.
- Claude Code bounds a session at the worktree's root. From version 2.1.277, a worktree with no `.claude/skills`
  falls back to the main checkout's project skills.

## Design decisions

| # | Decision | Rejected | Price if wrong |
|---|---|---|---|
| D1 | Tracked entry points, generated by `agent-instructions/skill_entry_points.py --write` | Installer mode without a pin: under WAY-44 the files would belong to `installation`, breaking `repository-file-location`; the installer refuses its own repository; its trust boundary grows. Untracked files made per checkout: fresh worktrees and cloud sessions see nothing. Global or per-worktree links, or symlinks in git: they read another branch, and need extra rights on Windows. | Low: the entry point text is one function, easy to move |
| D2 | Entry point: stops itself in a product submodule, process root from `--show-toplevel`, prefix rule naming every skill, description = source description + "Use this checkout's own the-way." | Working the root out from the skill's base directory (breaks under the worktree fallback); a prefix rule without names | Text regenerated in one place |
| D3 | Remove the global-mode paragraph from 9 skills; state two cases | Keep a third, global case | A hint lost for a setup the task removes |
| D4 | New sentence in `way_of_working.md` lines 9–10 for the-way itself; the second sentence of AIR-393 is not added, because the prefix rule carries it | AIR-393 word for word (it speaks of a resolved link that no longer exists) | One sentence to add later |
| D5 | Point-4 check as a critical-flow test in `gate/`, independent of the generator, plus a control test that breaks it on purpose; the generator's own tests in `agent-instructions/` | A test only in `agent-instructions/`: it does not run when a change touches only the skill's own folder | The flow can be withdrawn and the test moved |
| D6 | WAY-127, the invariant and two facts, because WAY-22 and WAY-90 require them | Part map change only; a decision with `Based on: none` (breaks WAY-90) | More entries, and two probes that read docs pages |
| D7 | One installer sentence changed, with a test | Leave it | Touches the trust-boundary file, so WAY-48 adversarial checks apply |
| D8 | Backlog section without the private path | The path in `AGENTS.md` (see Q2) | Point 5 not met to the letter |

## Questions and provisional answers

| ID | Question | Provisional answer | Alternatives | Price if wrong |
|---|---|---|---|---|
| Q1 | (carried) Installer code without a pin, or a separate mechanism? | A separate generator in `agent-instructions` | An installer self-install mode | That mode breaks `repository-file-location` |
| Q2 | Point 5 against WAY-27 / `outbound-link-reach`. No precedence recorded; WAY-25 forbids the agent to settle it. | Backlog section without the path; the path into `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md` as a human step | (a) the path in `AGENTS.md`, with Mariusz recording an exception in WAY-27 and the invariant — a change of meaning (WAY-07), blocks the request; (b) "ask the human" only, which WAY-107's reasoning rejects | Provisional: point 5 not met to the letter plus a second human step; (a): a blocked request and the private path shipped inside every product's `.the-way`. Main question. |
| Q3 | Do `.claude/skills/` and `.agents/skills/` fit WAY-09? | Yes, as root agent instruction files given to `agent-instructions`; WAY-44 names skills, WAY-09's verification speaks of "root entry points"; reading stated in WAY-127 and the request | Edit WAY-09 | A change of meaning (WAY-07) and the request waits |
| Q4 | New decision needed? | Yes, WAY-127 | Part map only | Reasons live only in a commit |
| Q5 | Premises as fact entries? | Yes, two facts with probes | Quote in the decision only | Breaks WAY-90 |
| Q6 | Where does the point-4 check run? | `gate/`, as a critical flow | `agent-instructions/` only | Report missed |
| Q7 | Keep global mode in skills? | No | Keep it | Minor |
| Q8 | Stop the-way's entry points being used inside a product? | Submodule check in each entry point only | Also a sentence in the product guidance | Relies on the model; recorded as an undetected failure mode |
| Q9 | Change the installer sentence? | Yes | Leave it | Stale cross-reference in products |
| Q10 | Adapt `implement-task`? | No; follow-up task | Adapt now | Outside the task |
| Q11 | Generator or hand-written entry points? | Generator with `--write` (lists orphans, deletes nothing) | Hand-written plus a test | Little |
| Q12 | Glossary entries? | None | "project skill" | Foundation step may still find one |
| Q13 | `Projects:` line in Backlog? | Omitted | "not named" | None |
| Q14 | Decision number? | WAY-127, renumbered at step 12 if taken | — | A renumber |
| Q15 | `task/instruction-files` adds a 12th skill | Whichever merges second runs `--write` | — | One failed gate run |
| Q16 | Check the installer's own skill list? | No | A test in `installation/` | New skills reach products late |

## Foundation entries named

- WAY-127/1, new decision — how a session on the-way reaches its skills: tracked, generated `the-way-` entry
  points that read the session's own checkout and pass to other skills under the prefix; no global link, no self-install.
- `skill-entry-points/1`, new invariant — every skill has both identical entry points, named after it, starting
  with its description and naming its path, and no orphan entry point exists. Method: the gate's tests. Derives from WAY-127. Part: `agent-instructions`.
- Part map, `agent-instructions` changed — files add `.claude/skills/**`, `.agents/skills/**`; responsibility adds
  the entry points; depends on `project-level` and `task-cycle`; two failure modes (missing/stale entry point,
  detected by `skill-entry-points`; the-way's own entry point followed inside a product, not detected).
- Part map, critical flow `skills-reach-the-way-sessions`, new — a change to a skill a session on the-way would
  not see is reported before it reaches the main branch; high; invariant `skill-entry-points`.
- `claude-code-project-skills/1`, new fact; `codex-repository-skills/1`, new fact.
- Unchanged: WAY-09, WAY-27 (unless Q2 goes the other way), WAY-34, WAY-44, WAY-107, `repository-file-location`, glossary.

## Self-review

Fixed one broken sentence in §4.4 and an unclear replacement rule in §4.3; installer test checks the phrase
"global install"; skill list order explicit; success criterion 1 no longer fixes the count at 22. Scope fits one
plan. Only open fork: Q2. No spec reviewer dispatched (inline self-review).
