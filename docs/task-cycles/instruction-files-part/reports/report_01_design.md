# Report 01 — design agent (returned as text, saved by the orchestrator)

I've written and self-reviewed the spec. The main open item is a change to WAY-127 that Mariusz has to decide (Q-M1): the global link in task point 9 contradicts WAY-127 as written. I stopped before `writing-plans`, wrote no plan or code, and made no commits.

**Spec:** `.runs/task-cycles/instruction-files-part/spec.md` (the only file I wrote). My experiments ran in a scratch clone and wrote nothing to any worktree.

## Classification
**Architectural.** The task adds a new part with a skill, a script that reads files the-way does not control (a trust boundary), and two documents. It also changes the foundation and the critical flow `skills-reach-the-way-sessions`. So it takes the full path: questions answered from the sources, approaches, design, written spec, self-review.

## Main design points
- **Skill layout (A1):** `instruction-files/` is itself the skill directory. `SKILL.md` sits beside `principles.md`, `tool_loading.md`, `check_instructions.py` and its test. The skill's files are then found however it is reached, so no text tells an agent to resolve a link.
- **Generator check in scratch:** with this layout the generator adds the two entry points and rewrites the other 22, since their list of sibling skills gains one name. The `gate` tests pass (98). The `agent-instructions` tests pass once the generated files are committed. The part-map guard accepts the draft entry with 0 errors.
- **Question carried to the cycle (how to write the method of a fact whose probe would need an agent run):** follow the precedent of `claude-code-path-rules` and the four facts from PR #8. Each such fact gets a watch of its documentation passage and no probe of the behaviour. No decision is needed, because every tool behaviour the new decisions rest on is documented. Behaviours known only from the prototype's measurements stay in `tool_loading.md` as described measurements and do not become facts.
- **Four script fixes, each with a test of the opposite failure:**
  - A: a path in a sentence saying the file does not load, and any missing directory, is reported as INFO instead of WARN.
  - B: a skill with a copy in `.agents/skills` no longer counts as having no pointer for Codex.
  - C: a relative file path with a directory part that resolves from nowhere, in a file outside the repository, is reported as WARN.
  - D: Markdown files that the root `AGENTS.md` or `CLAUDE.md` names are checked too: inside the repository root only, one level deep.
- **Trust boundary, problems reproduced in scratch:** Python 3.14's directory walk follows junctions, so the script reads files outside the repository; a junction pointing back to its parent makes the script list 63 phantom files and stop without saying so; a UTF-8 byte-order mark in a `.mdc` file gives a false ERROR; a UTF-16 file is printed with NUL characters. The spec adds a table of crafted inputs, each with the required behaviour and a test.

## Foundation entries the spec names
- Part map: new part `instruction-files` (four failure modes; trust boundary `instruction-files/check_instructions.py`); `agent-instructions` gains `instruction-files` in *Depends on*; flow `skills-reach-the-way-sessions` gains it in *Parts*.
- WAY-09 edited in place (change of meaning, renewed acceptance). Six invariants carry its fingerprint and get the new one. No code lists WAY-09's directories.
- WAY-127, proposed narrowing (Q-M1). `skill-entry-points` gets the new fingerprint.
- Six new decisions WAY-128–WAY-133, one per m1l4 settlement, all deriving from WAY-100, scope `instruction-files` and `agent-instructions`; none a trade-off principle.
- Two invariants with tests in `agent-instructions/` written by a second agent: `instruction-file-imports` (WAY-129), `root-claude-md-import` (WAY-132).
- Six new facts with watches: `claude-code-imports`, `claude-code-agents-md`, `codex-agents-md`, `cursor-agents-md`, `single-rule-compliance` (arXiv 2605.10039v1), `agent-run-variance` (arXiv 2602.07150v3). Existing facts newly named: `context-file-effect`, `claude-code-path-rules`.
- Glossary: nothing new; foundation entries say "check script" because `format guard` lists "checker" in *Avoid*.

## Questions for Mariusz (the request carries them)
- Q-M1, WAY-127 and the global link: A (recommended) narrow WAY-127 so a global link may reach `instruction-files/` alone; C replace the junction with a copy refreshed after each merge; B no global use.
- Renewed acceptance (WAY-07, WAY-114) of WAY-09, of WAY-127 if A, and of the meaning of every new entry.
- Reading of task point 7: facts are watches of documentation, not probes built from the measurements.

## Questions for the orchestrator (proposed answers)
- O1 flatten the layout; the junction (or copy) target becomes `C:\Storage\repos\the-way\instruction-files`.
- O2 the Cursor case has no source and no measurement; measure it in scratch with the installed `cursor-agent` if the logged-in account may be used, else an explicit unknown.
- O3 real tests for the two invariants, not method `TODO`.
- O4 numbers WAY-128–WAY-133, re-checked at writing.
- O5 check-by 2027-01-08 on WAY-128 and WAY-133.

## Autonomous choices
A1–A15 in the spec's table; beyond the above: A6 no invariants over the check script's behaviour; A8 one README line; A12 1 MiB read cap; A13 arXiv 2511.12884 quoted in WAY-130, not a fact; A14 root `AGENTS.md` and `CLAUDE.md` untouched.

## What I could not check
No page or paper re-read live; the Cursor case not measured; a UNC lookup reaching the network not exercised; decision numbers free at writing; with `--merge-onto none` the guards skip fingerprint checks, so the spec adds a by-hand recomputation with `relation-model/fingerprint.py`.
