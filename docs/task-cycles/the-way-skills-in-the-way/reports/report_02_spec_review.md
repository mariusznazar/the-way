# Report 02 — spec reviewer (saved by the orchestrator from the agent's returned text)

**Spec:** `spec.md`. **Checked against:** `frozen_task.md`, the foundation at c64a607, the Superpowers 6.4.1
spec-reviewer prompt, the cycle skill at the process root, and the two live pages (fetched raw, split into the
probe's text runs with `fact_probes.html_runs`, saved to the scratchpad). Nothing in the repository was changed.

## Findings

**1. Blocking. §4.2 entry point and §6: the product guard never fires, and the root is wrong.**
- git's rev-parse page: `--show-superproject-working-tree` "Outputs nothing if the current repository is not used
  as a submodule by any project". In a product the shell's directory is the product root: the command prints
  nothing (checked from `C:\Storage\repos\the-way`: `[]`), and `--show-toplevel` prints the product root, so
  "Read `<path>` there" points at a path that does not exist in the product.
- The danger is real: a nested `.claude/skills/` loads "the first time Claude reads or edits a file in that
  subdirectory"; both same-named skills "stay available"; Claude Code is told to invoke "the one whose directory
  holds the files it's working on", and an agent in a product works on `.the-way/…` files. The shell's working
  directory also moves: "That directory moves when Claude runs cd."
- Under the worktree fallback (v2.1.277+), the entry point sits in the main checkout: a guard run in the entry
  point's directory correctly stays silent; the root must not be taken from the entry point's directory (main
  checkout — the defect point 2 removes); it has to come from the directory the session started in. §6's
  "correct by construction" is also false because an old branch's `SKILL.md` still carries "Installed globally …
  resolve it first: `realpath <base>`" (`elements/decisions/skill/SKILL.md:13-16`), which resolves to nothing
  once point 6 removes the junctions.
- Fix: run the guard in the directory holding the entry point (`git -C <directory of this file> rev-parse
  --show-superproject-working-tree`; Claude Code documents `${CLAUDE_SKILL_DIR}`, Codex lists each skill's file
  path); take the root from `git rev-parse --show-toplevel` in the directory the session started in (Claude Code
  also offers `${CLAUDE_PROJECT_DIR}`); keep the text tool-neutral so the copies stay byte-identical, or change
  criterion 1, the invariant and `problems()`; add "if the skill tells you to resolve a link to find the-way, skip
  that; the root is the one above"; rewrite §6; same wording in §4.3.

**2. Blocking. §5.6, §4.5, §4.7: point 5 is settled by the agent, which WAY-25 and the cycle skill forbid.**
- Collision real: `outbound-link-reach` (`foundations/invariants.md:469`) "No file git tracks contains a link into
  a private note collection"; WAY-27 (`decisions.md:728`) "Nothing in this repository points to a source outside
  it that its readers cannot reach".
- §5.6 says WAY-25 forbids the agent to settle and then settles it; the variant ("in the author's private
  notes…") still points to a source readers cannot reach — avoids the invariant's word "link", not WAY-27's
  sentence; and does not deliver point 5's content.
- Cycle skill requires a blocked draft: `SKILL.md:19-21`, `:124-126`, `:172-174`, `:95-98`. Same reading under
  WAY-107 (`decisions.md:2974`) vs WAY-27 or WAY-30 (`decisions.md:818-822`).
- §4.7's second paragraph edits `C:\Users\Mariusz\.claude\CLAUDE.md` and its Codex copy: breaks `SKILL.md:43-45`
  (remarks about the user's agent instructions go to process remarks, never the request); the run brief allows
  an outside-repo human step only for point 6.
- Fix: implement everything else; blocked draft with one question: (a) path in `AGENTS.md` with precedence
  recorded (WAY-107 `narrows` WAY-27 for a product's own backlog section) or an exception in WAY-27 and
  `outbound-link-reach`, each a change of meaning re-accepted under WAY-07; or (b) the section names no
  location, point 5 not met. Add a recommendation. Personal-instructions idea to process remarks.

**3. Should fix. §5.1: the WAY-09 reading leans on a misquoted phrase.** WAY-09 admits "the root agent
instruction files" (`decisions.md:241-243`); `agent-instructions/` is "led to from the root agent instruction
files" (`:252-253`); the Verification "root entry points" (`:270-271`) refers to those root files.
`repository-file-location` passes literally by its disjunction (`invariants.md:148`), but WAY-09 is narrower; the
task asks the cycle to settle this (`frozen_task.md:53`). Fix: drop the argument; edit WAY-09 to name
`.claude/skills/` and `.agents/skills/` (in-place pre-main edit under WAY-07; fingerprint b829b86a renews in
`repository-file-location`, WAY-31) and ask for acceptance in the same blocked draft. Recommended: the edit.

**4. Should fix. §7: `skill-entry-points` names `Part: agent-instructions`.** WAY-62 (`decisions.md:1743-1745`):
an invariant names the parts where a change can make its sentence false; rationale rejects "the part holding the
check". Fix: `Part: every`; `Derives from: WAY-127@<fingerprint>`, `Correction: none`.

**5. Should fix. §4.4: the control test is called "the deliberate break".** WAY-69 (`decisions.md:1916-1918`): the
deliberate break "is written from the sentence by the reviewer of that code, who did not write the check"; cycle
`SKILL.md:83-84`, `143-145`. Fix: call it a control test of `problems()`.

**6. Should fix. §7 facts: shape and coverage.** WAY-76 (`decisions.md:2084-2087`): two facts about different
things are two entries. Settle: (a) upward loading to the repository root, linked-worktree limit, v2.1.277
fallback; (b) nested `.claude/skills` loading on first file access, both skills available, Claude told to invoke
the one whose directory holds the files — the reason for the guard and the failure mode; (c) Codex scanning from
the working directory up to the repository root. If the fix of 1 relies on `${CLAUDE_SKILL_DIR}` or Codex listing
paths, facts for those too (WAY-90, `decisions.md:2461-2464`). Shape after `claude-code-path-rules`
(`environment_facts.md:110-116`): Holds for "Claude Code, whose documentation code.claude.com publishes for its
current release without versions"; Source page plus "(archived: <copy>, date)"; Method `python -B
gate/run_tests.py probes/<id> --record .runs/fact-<id>.jsonl`; test `probes/<id>/test_<id>.py` calling
`watch_passages` with `# fact: <id>/1` in the method. The check is a watch, not a probe (`glossary.md:133-179`).
Codex: cite the redirect target (`developers.openai.com/codex/skills` → 200 at
`learn.chatgpt.com/docs/build-skills`); archived copy
`http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills`; for
`code.claude.com/docs/en/skills` none checked (Wayback 429). Feasible: every passage stands in one text run
(Claude Code runs 225, 226, 237, 443; Codex 767, 791, 813).

**7. Minor.** Success criterion 2 vs §4.3 (`critique`, `task-cycle` unchanged): reword criterion 2.

**8. Minor.** §2 "no tracked file holds a local path": `git grep -F 'C:/'` finds `foundations/decisions.md:3565`;
no vault path exists.

**9. Minor.** §4.2 sibling order "as the installer's `sibling_names()` does": the installer uses its `SKILLS` table
order (`installation/install.py:25-36, 101-103`). Drop the parenthesis.

**10. Minor.** §4.6 touches the trust boundary `installation/install.py` (`part_map.md:200`); cycle step 4 asks for
adversarial input checks. State why a string-only change needs none, or add them.

**11. Minor.** §4.7: add a Codex check; `Get-Item -ErrorAction Stop` aborts the loop at the first missing name —
check and `continue`. Junction facts verified: five `Junction` targets in `C:\Storage\repos\the-way\elements\…\skill`,
`.agents\skills` a junction to `.claude\skills`, `refine-task`/`critique` to vox-ai-tools.

## Orchestrator observations

1. Confirmed (finding 1).
2. Verbatim checks: start directory and parents up to repository root — holds; linked-worktree limit — verbatim;
   v2.1.277 fallback — holds ("On Claude Code v2.1.277 or later, when the worktree checkout has no .claude/skills
   directory at its root, Claude Code loads the main checkout's project skills instead."); nested loading —
   verbatim; "both stay available"/"the one whose directory holds the files it's working on" — verbatim;
   `<subdir>:<name>` — in substance; personal over project — "Enterprise over personal, and personal over
   project."; Codex scanning — verbatim after "For repositories,"; "both can appear in skill selectors" —
   verbatim; symlinks — paraphrase of "Codex supports symlinked skill folders and follows the symlink target
   when scanning these locations."
3. Shape mostly right, with the gaps of finding 6.
4. Method as `decision-guard-stale-reference` and `test-runner-pass-line` (`invariants.md:10, 1531`); `gate/` with
   `# flow:` as `gate/test_wording_reaches_dependants.py:15`; invariant cited inside the method
   (`gate/run_tests.py:13-15`); `Rests on: none` right under WAY-73; Part wrong (finding 4); no test cites
   `decision-guard-stale-reference`.
5. Collision real; handling inconsistent (finding 2).

## Verdict

Approved after fixes. 1 and 2 before planning; 3–6 in the same revision; brief re-check before the planner.
