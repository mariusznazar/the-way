# Report 06 — foundation step 1.1, facts agent (saved by the orchestrator from the returned text)

Wrote four entries in `foundations/environment_facts.md` (after `python-release-binaries/1`), committed nothing.
Guard exit 0, 0 errors. Every passage stands word for word at the address cited, read 2026-10-08. Stopped before any
watch.

| Identifier | Fingerprint |
|---|---|
| `claude-code-project-skills/1` | a06eaca7 |
| `claude-code-nested-skills/1` | 4dd3d448 |
| `codex-repository-skills/1` | 7db28f98 |
| `codex-skill-paths/1` | 5b5b6c79 |

- Holds for: "Claude Code, whose documentation code.claude.com publishes for its current release without versions";
  same form for "Codex … learn.chatgpt.com …".
- Method: `python -B gate/run_tests.py probes/<id> --record .runs/fact-<id>.jsonl` — a watch (a probe would need a
  run of the tool, credentials and a model). Unchecked until the watches exist. WAY-08's deliberate break for a
  fact's method left as the template's open question.

Changes to the brief's wording (WAY-80, no sentence says more than its source): project-skills — "has none at its
root" → "has no `.claude/skills` directory at its root"; "from v2.1.277" → "on v2.1.277 or later"; "in a linked git
worktree" → "in a session running in a linked git worktree"; first passage copied to the end of the page's sentence
("…up to the repository root, so starting in packages/frontend/ still picks up skills defined at the root.").
nested-skills — "nested" defined as "a `.claude/skills/` directory below the directory where it starts", with the
added passage "Skills in a .claude/skills/ directory below where you started don’t load at startup."
codex-repository-skills — starts "In a repository," after the source's "For repositories,". codex-skill-paths —
added "This budget applies only to the initial skills list.". WAY-76: no split (each entry is one thing).

Passages re-read with `fact_probes.page_runs`, then through `missing_passages` on the written entries: 0 missing.
- https://code.claude.com/docs/en/skills (200), § Load skills in monorepos and subdirectories: three passages of
  project-skills, four of nested-skills (typographic ’).
- https://learn.chatgpt.com/docs/build-skills (200): § Where Codex loads local skills — "For repositories, Codex
  scans .agents/skills in every directory from your current working directory up to the repository root."; § Build
  skills — "In Codex, the initial list also includes each skill’s file path." and "This budget applies only to the
  initial skills list."
- Codex address: learn.chatgpt.com cited; developers.openai.com answers `308 Permanent Redirect`, and every capture
  since 2026-08-05 is that redirect.

Archived copies (Wayback index): Claude Code http://web.archive.org/web/20261006214359/https://code.claude.com/docs/en/skills
(2026-10-06, all seven passages; first attempt "Temporarily Offline"); Codex
http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills (2026-10-02, both passages).

Whole-foundation search (WAY-33):
1. Link: WAY-127 must name all four facts in *Based on* with the fingerprints above (1.3).
2. Question: Codex page: "For large skill sets, Codex may omit some skills from the initial list and show a
   warning." — a skill left out carries no file path, a gap in the first product check in Codex. Provisional: no new
   fact; the part-map agent adds it to the `agent-instructions` failure modes.
3. Question: Claude Code page: "When you move the session with /cd on v2.1.246 or later, Claude Code adds the new
   directory’s project skills." The start-directory root rule still holds. Provisional: no fact (WAY-127 does not
   rest on it); pass to the reviewer of the entry-point text.
4. Question: the installer's product skills rely on the same loading behaviour; no decision records how they are
   written, so no *Based on* to link. Provisional: no change in this task; candidate for the return step.
5. Question: spec quotes on same-name precedence in both tools. Provisional: no facts — the prefix avoids relying on
   them.
6. No change needed: WAY-34 (a product session loading `.the-way/.claude/skills/` loads the pinned commit); WAY-52
   (different page); glossary; WAY-37; WAY-46.

Guard: exit 0 — 0 errors, 4 warnings (each new fact named by nothing yet, WAY-73; 1.3 fixes), 3 unchecked (from the
two `none`). No `human_verdicts.md` file.

Polish meaning sentences (WAY-114):
- `claude-code-project-skills/1`: Claude Code wczytuje skille projektu z `.claude/skills/` w katalogu startu i w
  każdym katalogu nadrzędnym aż do korzenia repozytorium, w połączonym worktree tylko do jego korzenia, a od wersji
  2.1.277, gdy worktree nie ma u siebie `.claude/skills`, bierze zamiast tego skille głównego checkoutu.
- `claude-code-nested-skills/1`: Claude Code wczytuje skille z `.claude/skills/` leżącego poniżej katalogu startu
  dopiero przy pierwszym odczycie albo edycji pliku w tym podkatalogu, przy zbieżnej nazwie zostawia oba skille i
  podaje modelowi warianty z nazwą katalogu z poleceniem wywołania tego, w którego katalogu leżą pliki, nad którymi
  pracuje.
- `codex-repository-skills/1`: W repozytorium Codex przeszukuje `.agents/skills` w każdym katalogu od bieżącego
  katalogu roboczego aż do korzenia repozytorium.
- `codex-skill-paths/1`: Początkowa lista skilli, którą dostaje Codex, zawiera ścieżkę pliku każdego skilla.
