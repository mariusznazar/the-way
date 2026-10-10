# Foundation author report — installer Claude import

- **Model:** Codex GPT-6.
- **Worktree:** `C:/Storage/repos/the-way-wt/installer-claude-md`.
- **Base:** `b8ff05bf139fc394f3f0df351e5da6c0bc0b0995` on `foundations`; this checkout has no `main` branch.
- **Scope:** Foundation entries only. No installer code, invariant check, or commit was written.

## Inputs and question

Read `.runs/task-cycles/installer-claude-md/task-frozen.md` and `plan.md`, `agent-instructions/README.md`, the glossary and relevant complete entries in the other foundation files, the record-decision, record-invariant, and update-part-map project skills and their element skills and templates, decision and part-map examples, and `elements/common/way_of_working.md` and `rules.md`. Searched all six files in `foundations/`. Read the applicable `task-cycle/skill/SKILL.md` foundation and request-link instructions. The existing decision WAY-03 served as the decision-entry example.

**Decision question:** How does the installer give Claude Code the guidance in a product's root `AGENTS.md`?

**Meaning in task language:** Instalator zakłada w produkcie `CLAUDE.md` z jedną linią `@AGENTS.md`, gdy pliku nie ma; gdy plik istnieje bez skutecznego importu, ostrzega w planie, ale go nie zmienia; nie tworzy `.claude/rules/the-way.md`. Ostrzeżenia o `CLAUDE.local.md` nie dodano.

## Entries written

- `foundations/decisions.md`: WAY-141/1, a new decision scoped to `installation`, based on `claude-code-imports@5b9359fd` and `claude-code-agents-md@e4007cb8`, with `Review when: none` and `Approved by: Mariusz, merge of <request link>`. Its binding fingerprint is `5d0990a0`. The task cycle must substitute the request URL after opening the request.
- `foundations/decisions.md`: WAY-132/1 verification examples now treat root `CLAUDE.md` and the marked `AGENTS.md` block as installer-owned and no longer call the legacy rule an installer output. Binding sentences, change kind, and fingerprint `1242ac75` are unchanged.
- `foundations/invariants.md`: `installation-claude-guidance/1` derives from `WAY-141@5d0990a0` and rests on `claude-code-imports@5b9359fd`. It covers the generated file, warning before confirmation, byte-for-byte preservation of an existing file, and absence of the generated legacy rule. Its method is `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`; its binding fingerprint is `54443fde`.
- `foundations/part_map.md`: the `installation` failure modes now include missing or duplicated Claude guidance, detected by `installation-claude-guidance`. The part's binding responsibility and fingerprint are unchanged.

## Whole-foundation searches

**Before writing:** Searched `decisions.md`, `invariants.md`, `part_map.md`, `environment_facts.md`, and `violated_invariants.md` for install, Claude, `AGENTS.md`, instruction, rule, WAY-132, WAY-107, and WAY-33 language; read `glossary.md` in full and read the full relevant entries, including WAY-03, WAY-33, WAY-34, WAY-107, WAY-132, and the relevant part-map and environment-fact entries. WAY-132's verification examples described the legacy rule as installer output. The `installation` part lacked a failure mode for lost or duplicated Claude guidance. WAY-107 places Backlog outside the installer block; WAY-34 keeps pin moves in product tasks. WAY-129 and the the-way-only root import invariant govern this repository's own instruction files, so they do not collide with the new product installer decision. No glossary term, environment fact, or existing invariant required a wording change.

**After writing:** Searched all six foundation files for `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, `the-way.md`, installation and Claude Code; searched all foundation files for WAY-141, `installation-claude-guidance`, WAY-132 references, and import-fact references. The remaining legacy-rule references are the new decision and invariant prohibition, not a claim that the current installer outputs it. The part-map detection target exists; WAY-141 and the import fact fingerprints were computed from their binding parts; WAY-132's binding fingerprint remains `1242ac75`. No further unlinked effect or collision was found. The orchestrator must search again against the current `foundations` tip before merge under WAY-33.

## Checks

| Command | Exit | Result |
|---|---:|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | 0 errors, 6 warnings, 5 unchecked |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | 0 errors, 0 warnings, 3 unchecked; no `human_verdicts.md` |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | 0 errors, 0 warnings, 7 unchecked |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests passed |
| `python -B gate/run_tests.py elements/invariants` | 0 | 233 tests passed |
| `python -B gate/run_tests.py elements/part-map` | 0 | 162 tests passed |
| `python -B gate/run_tests.py gate` | 0 | 98 tests passed, including existing critical-flow tests |
| `git diff --check` | 0 | No whitespace errors |

The decision warnings are five overdue review dates on WAY-03, WAY-21, WAY-52, WAY-55, and WAY-69, plus the intentional `<request link>` placeholder on WAY-141. Its five unchecked checks are two requiring a base commit and three requiring a merge-onto commit. The invariant guard's three unchecked checks require a base or merge-onto commit. The part-map guard's seven unchecked checks concern two flow coverage files, unreported promise levels and dependency graph, and three base-dependent comparisons. These are partial checks, not a full gate pass.

An initial call to the part-map guard with `--merge-onto none` exited 1 because this guard does not accept that option; it was rerun with its supported `--base none` argument and exited 0. Initial concurrent captures of the invariant and part-map test runs returned before process completion; the completed reruns above give their verified exit codes.

## Uncertainty and handoff

No check yet cites `installation-claude-guidance/1` in `installation/`; the invariant's method is named, but it cannot report a verdict until an independent author writes the check. Put that check in a separate `installation/test_installed_guidance.py`, cite `# invariant: installation-claude-guidance/1` at each relevant test, and keep that file read-only for the installer implementer. The check author receives the invariant sentence and method without the installer's code reasoning. The installer implementer may edit `installation/install.py` and `installation/test_install.py` after the check is written and observed failing on the old behavior. The code reviewer writes the deliberate break from the sentence without the check author. This follows WAY-69 and WAY-03.
