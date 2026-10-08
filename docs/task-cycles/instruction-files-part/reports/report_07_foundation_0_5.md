# Report 07 — part-map agent, Task 0 step 5 (returned as text, saved by the orchestrator)

Wrote the `instruction-files` part entry in `foundations/part_map.md` (between `agent-instructions` and `installation`), staged, nothing committed, no other file changed. Text is spec §5.1 revision 3 word for word; prose says "the check script" throughout. `agent-instructions` and the flow `skills-reach-the-way-sessions` unchanged.

Files the pattern claims: `instruction-files/**` → `SKILL.md`, `check_instructions.py`, `principles.md`, `test_check_instructions.py`, `tool_loading.md`; none taken from another part.

Guard (`git add instruction-files foundations/part_map.md && python -B elements/part-map/format_guard.py foundations/part_map.md --base none`): `0 error(s), 0 warning(s), 7 unchecked`, exit 0 — three unchecked from `--base none`, four pre-existing (two flows without coverage, change paths, dependency graph).

Meaning (Polish, WAY-114): Nowa część `instruction-files` odpowiada za zasady pisania, oceniania i utrzymywania plików instrukcji dla agentów, za opis tego, jak Claude Code, Codex i Cursor je wczytują, oraz za skill stosujący te zasady razem ze skryptem, który mechanicznie sprawdza pliki instrukcji; wolno jej zależeć tylko od dziennika decyzji i faktów o otoczeniu, a granicą zaufania jest skrypt sprawdzający, bo czyta pliki, nad którymi the-way nie panuje.

## WAY-33 findings

- Q1 — the trust boundary has no row in the external context list (WAY-48, `external-exchange-row`); proposed row `| a repository or a user's files an agent's instructions are read from — instruction files, tool configuration, session records | them → us | untrusted | no |`.
- Q2 — *Scope* of WAY-27, WAY-38, WAY-89, WAY-120 does not name `instruction-files` (WAY-21, `decisions-found-for-change`); proposed: add it through `record-decision` as in-place edits (outside the binding part, fingerprints unchanged), listed in the request; WAY-38/89 already miss `gate`, `project-level`, `agent-instructions`, `elements-common` — outside this task.
- Planned for later steps: WAY-09 and `repository-file-location` (false until §5.3; method `TODO`); `skill-entry-points` (untracked files counted; entry points come in Task 2); `agent-instructions` *Depends on* and the flow's *Parts*; "checker" left in the prototype files (`SKILL.md:21`, docstrings) — renamed in later tasks; `foundation-search-record` — this list is material for the first search record.
- Checked, no change: WAY-44 (the skill is the process's own content); WAY-46 (severity "high" raised); `gate-boundary-change` (method `TODO`); `script-language`, `script-imports`, `script-subprocesses` hold; `outbound-link-reach` holds at a glance (public addresses and the `".runs"` skip-list name); no `glossary` dependence; no surface for the check script's command; element-only invariants do not reach the part.

## Resumed for Q1

Row added after the existing three rows of External context: `| a repository or a user's files an agent's instructions are read from — instruction files, tool configuration, session records | them → us | untrusted | no |` — names kinds of files, no part or path (template). Guard: `0 error(s), 0 warning(s), 7 unchecked`, exit 0, unchanged. Meaning (Polish): Repozytorium albo pliki użytkownika, z których czytane są instrukcje dla agentów — pliki instrukcji, konfiguracja narzędzi, zapisy sesji — przekazują dane tylko w stronę the-way, są niezaufane i nie zmieniają się razem z the-way. Q2 left to the decisions step.

## Resumed for foundation 1.7

Changes in `foundations/part_map.md`: `agent-instructions` *Depends on* gains `instruction-files`; two failure modes at `agent-instructions` — "the root `CLAUDE.md` stops opening with `@AGENTS.md` — Claude Code sessions on the-way lose the instructions the root `AGENTS.md` carries — high — detected by root-claude-md-import" and "a repository instruction file of the-way gains an `@` import — Claude Code loads the whole imported file into every session on the-way — high — detected by instruction-file-imports" (split: a failure mode names one detecting invariant; the guard reads the text after "detected by" as one name); flow `skills-reach-the-way-sessions` *Parts* gains `instruction-files`. Guard `0 error(s), 0 warning(s), 7 unchecked`.

Meaning (Polish): Część `agent-instructions` może zależeć od `instruction-files`, bo wygenerowane wskaźniki czytają skill tej części. · Przepływ `skills-reach-the-way-sessions` przechodzi teraz także przez `instruction-files`, bo jej skill też musi być widoczny w sesjach na the-way pod nazwą z prefiksem `the-way-`. · Jeśli główny `CLAUDE.md` przestanie zaczynać się od `@AGENTS.md`, sesje Claude Code na the-way tracą instrukcje z `AGENTS.md` (wysoka waga, wykrywa `root-claude-md-import`). · Jeśli któryś plik instrukcji repozytorium the-way dostanie import `@`, Claude Code wczytuje cały importowany plik do każdej sesji na the-way (wysoka waga, wykrywa `instruction-file-imports`).

WAY-33: `instruction-files` needs no new failure mode for the flow (recorded once at `agent-instructions`, detected by `skill-entry-points`); the new failure modes sit at `agent-instructions` because every repository instruction file of the-way lies there today; severity high raised beyond the scale's wording (WAY-46); no separation on the new dependency, no cycle; tests in `agent-instructions/`; WAY-128–133 *Scope* names exist. Questions: Q3 failure mode for the narrowed WAY-127 at `instruction-files` (accepted); Q4 use the term in `agent-instructions`' responsibility (declined).
