# Plan — Install a root CLAUDE.md that imports AGENTS.md

- Task: `.runs/task-cycles/installer-claude-md/task-frozen.md`
- Spec: none
- Base: `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995`

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Settlement 1: WAY-141/1, installer-owned Claude Code guidance reaches the product through a root `CLAUDE.md` import of the installer block in `AGENTS.md`; an existing root file without the import is warned about and left untouched | new decision in `foundations/decisions.md` | *Settlements to record* row 1 | Independent invariant check; Slices 1 and 2 |
| WAY-132/1 verification examples: remove the obsolete description of `.claude/rules/the-way.md` as an installer file, without changing the binding decision | edit of existing decision in `foundations/decisions.md` | To do 5 | Slice 2 |
| `installation-claude-guidance/1`: installed import, warning before confirmation, existing-file preservation, and no generated rule | new invariant in `foundations/invariants.md`; independent check in `installation/test_installed_guidance.py` | WAY-141/1; installer behavior made true by Slice 1 | Independent invariant check; Slice 1 |
| Installation part failure mode for missing or duplicated Claude guidance, detected by `installation-claude-guidance` | edit of existing part in `foundations/part_map.md` | WAY-141/1 and the new invariant | Independent invariant check; Slice 1 |

Before the first slice, search the whole foundation for effects of these entries; run `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`, `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`, `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`, and `python -B gate/run_tests.py` for `elements/decisions`, `elements/invariants`, and `elements/part-map`; record warnings and unchecked results. The orchestrator handles the independent assessment required for a foundation change.

**Independent invariant check before Slice 1:** A check author separate from the installer implementer writes `installation/test_installed_guidance.py` from the sentence and Method of `installation-claude-guidance/1`, without the installer's code reasoning. Each relevant test cites `# invariant: installation-claude-guidance/1`. Run `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl` against the old installer and observe the expected failure. The check file is read-only throughout implementation; any needed change returns to the foundation step.

## Slices

### Slice 1 — Install and inspect the Claude import

- **Goal:** A fresh product receives root `CLAUDE.md` containing one `@AGENTS.md` line; the preview and apply plan warn when an existing root `CLAUDE.md` does not effectively import `AGENTS.md`; the installer never edits that existing file or writes `.claude/rules/the-way.md`.
- **Change:** `installation/install.py` · `installation/test_install.py`
- **Read:** `.runs/task-cycles/installer-claude-md/task-frozen.md` · `foundations/decisions.md` · `foundations/invariants.md:2051-2074` · `foundations/part_map.md:228-248` · `foundations/environment_facts.md:198-214` · `instruction-files/tool_loading.md:14-53` · `agent-instructions/README.md`
- **Checks:** Start with the independent invariant check already failing against the old installer. Write any additional changed-behavior integration cases first in `installation/test_install.py`, and run `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl` before and after the installer change; the final run must pass and cite `installation-claude-guidance/1`. Cover preview versus apply, the exact new file, repeated runs, an existing import or absent import, byte-for-byte preservation of existing files, absence of the old rule, warning visibility before confirmation, and Git-ignored new `CLAUDE.md`. Exercise adversarial product input such as a misleading import in a code block, malformed UTF-8, a directory or symlink at `CLAUDE.md` where the platform permits it, and a cancelled apply; verify no unintended replacement or write. Run `python -B gate/run_tests.py gate` for the existing critical-flow tests.
- **Depends on:** Settlement 1 · `installation-claude-guidance/1` and the installation part-map edit · independent check authored and observed failing

### Slice 2 — Describe the product layout and pin movement

- **Goal:** Installer documentation and the instruction-files skill describe the single guidance route through `AGENTS.md` and root `CLAUDE.md`; pin-move instructions handle the old installed rule only when a product is migrating from an older pin, and no text treats that rule as a file the current installer writes.
- **Change:** `installation/README.md` · `instruction-files/SKILL.md`
- **Read:** `.runs/task-cycles/installer-claude-md/task-frozen.md` · `foundations/decisions.md` · `foundations/invariants.md:2061-2070` · `foundations/part_map.md:200-248` · `instruction-files/principles.md:126-151` · `instruction-files/tool_loading.md:14-53` · `installation/install.py`
- **Checks:** Run `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`, `python -B gate/run_tests.py instruction-files`, and `python -B gate/run_tests.py gate`. Inspect references with `rg -n 'the-way\.md|CLAUDE\.md|AGENTS\.md' installation/README.md instruction-files/SKILL.md foundations/decisions.md`, checking the full context of each remaining legacy-rule mention. Read the foundation guards' reports and the test reports, including warnings and unchecked results.
- **Depends on:** Slice 1 · Settlement 1 · WAY-132/1 verification edit

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Need: one guidance route for Claude Code, including the product's `## Backlog` section in root `AGENTS.md` | Settlement 1 · `installation-claude-guidance/1` · Slice 1 · Slice 2 |
| To do 1: create root `CLAUDE.md` with one `@AGENTS.md` line when absent | Settlement 1 · `installation-claude-guidance/1` · Slice 1 |
| To do 2: warn in the installation plan about an existing root `CLAUDE.md` without the import; leave it untouched | Settlement 1 · `installation-claude-guidance/1` · Slice 1 |
| To do 3: stop writing `.claude/rules/the-way.md` | Settlement 1 · `installation-claude-guidance/1` · Slice 1 |
| To do 4: update the installed-files and pin-move instructions | Slice 2 |
| To do 5: update `instruction-files/SKILL.md` and WAY-132 verification examples | Slice 2 · WAY-132/1 verification edit |
| *Settlements to record* row 1 | Settlement 1 · `installation-claude-guidance/1` · Slice 1 |
| New installation failure mode and invariant check | Part-map edit · `installation-claude-guidance/1` · independent check author before Slice 1 · Slice 1 |
| Keep `loop2` pin movement out of this task | Slice 2 documents the product task; no product repository change |
| Do not add a `CLAUDE.local.md` warning, as refinement found it would not signal a failure after the import | Settlement 1 · Slice 1 |
| Required checks for changed parts and the critical flow | Foundation-entry checks · independent invariant check before Slice 1 · Slices 1 and 2 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Treat an existing root `CLAUDE.md` as product-owned: inspect only to decide whether to warn, and preserve its bytes on apply and rerun. Recognize an effective import, rather than a mere occurrence of the text inside a code sample. | Require the existing file to equal the generated one, append an import, or accept any substring. | A false negative hides lost guidance; a false positive asks for an unnecessary manual edit. Mutating the file would break the installer's preservation promise. |
| Keep the old rule's deletion as a one-time product pin migration step where that file was installed by an older commit; later pin moves do not delete or recreate it. | Delete that product file in the installer or keep the old universal delete instruction. | An old product could keep duplicate guidance, while a blanket delete could remove a product-owned file. |
| Update WAY-132's verification examples in place, while the new installation decision binds the product-specific behavior. | Expand WAY-132's binding text to govern the installer's files. | A broader binding change would affect unrelated instruction-file work and require renewed acceptance. |
