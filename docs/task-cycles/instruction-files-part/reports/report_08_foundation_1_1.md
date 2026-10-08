# Report 08 — glossary agent, foundation 1.1 (returned as text, saved by the orchestrator)

Wrote `repository instruction file` into `foundations/glossary.md` (lines 145–150, between `read off` and `result`). Guard exit 0, `0 error(s), 1 warning(s), 5 unchecked` as expected. Only the glossary changed; nothing staged (the glossary guard does not read the index).

```markdown
## repository instruction file

A repository instruction file is an instruction file for coding agents that a repository's git tracks as an `AGENTS.md` or a `CLAUDE.md`, or as a Markdown file its root `AGENTS.md` or `CLAUDE.md` names by its path.

- **Avoid:** none
- **Not:** none
```

Deviations from spec §5.0: "in backticks" removed (question 1); *Not* `none` — *Not* lists other meanings the word carries, and a new word has none; what the definition leaves out is a reader's meaning WAY-94 keeps out of *Not*; skills and entry points fall outside anyway (each is a `SKILL.md`; the root `AGENTS.md` names only the directories).

Guard: one warning `foundations/glossary.md:147: … the term has no use outside the glossary; a merge onto the main branch fails on it` (uses come with WAY-128–133; 1.5 re-reads them); five unchecked, all from `--base none` / `--merge-onto none`.

Meaning (Polish): Plik instrukcji repozytorium to plik instrukcji dla agentów kodujących, który git repozytorium śledzi jako `AGENTS.md` albo `CLAUDE.md`, albo plik Markdown, który główny `AGENTS.md` lub `CLAUDE.md` wskazuje ścieżką — skille the-way i wygenerowane wskaźniki do nich się do tego nie zaliczają.

Planned uses: WAY-128, 129, 130, 131, 133 in binding sentences; WAY-132 none (spec §5.5 overstates); `instruction-file-imports` spells the files out (question 2). `--uses` today: 0 uses of the term, 9 of bare "instruction file", all ordinary meaning.

Comparison with identifiers (WAY-93): the guard's `read_alike` against 265 identifiers and the planned ones — no match.

WAY-33: WAY-95, 96 confirmed; WAY-97 confirmed for decisions, finding for the invariant; WAY-35, 127 — skills and entry points outside without *Not*; last-word use "instruction file" ordinary in WAY-09, part map, WAY-131/133 drafts (WAY-99) — writers must write the whole term where they mean it; no *Avoid* words qualify (WAY-98): "root agent instruction files", "context files", "instructions for agents", "rule files for agents"; WAY-104 — "file" becomes a protected last word; WAY-52 — path-rule files (`.claude/rules/*.md`, `.cursor/rules/*.mdc`) outside the term; the-way tracks none.

Questions with proposed answers: 1 "in backticks" out — yes; 2 the invariant uses the term — yes; 3 WAY-128 *Rationale* rewrite "Process skills and their entry points answer to their own decisions (WAY-35, WAY-127), not to this one." — yes; 4 "file" joins the protected words (WAY-104) — accept, name it in the request; 5 path-rule files outside the term — leave, state the limit; 6 rewrite WAY-09's "root agent instruction files" — no.
