# Report 14 — foundation step reopened for R12 (saved by the orchestrator from the returned text)

All four R12 changes in the task worktree; guards and the watch pass; nothing committed; only the four foundation files
changed (LF). The watch rewrote `.runs/fact-claude-code-project-skills.jsonl` (ignored). Followed the four element skills
from the process root with their templates, `common/rules.md`, `common/way_of_working.md`; no global skill.

## Changes

1. `claude-code-project-skills/1` (edited in place, `/1`): sentence now ends "…the main checkout's project skills instead
   when the worktree checkout has no `.claude/skills` directory at its root; on v2.1.246 or later, when a session is moved
   with `/cd`, it adds the new directory's project skills." *Source* gains, in the page's order, `§ Load skills in monorepos
   and subdirectories — "When you move the session with /cd on v2.1.246 or later, Claude Code adds the new directory’s
   project skills."`; re-read with `page_runs`, same paragraph as the other three; `missing_passages` `[]`; archived copy
   `…/web/20261006214359/…` also holds it and is still the latest capture.
2. WAY-127/1: binding sentence 2 → "An entry point reads its skill and the files it names from the checkout or worktree
   the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another
   the-way skill on under the `the-way-` prefix."; *Rationale* → "The checkout or worktree the session works in sets which
   copy is read, because a tool may offer one checkout's entry points to a session in another worktree, and a session moved
   to another directory gains that directory's entry points beside the ones it started with;"; *Based on*
   `claude-code-project-skills@d58fb91f`. Beyond the dispatch: the level-2 "complies" example now says "the checkout or
   worktree the session works in" (not in the fingerprint; revertible in one line).
3. `skill-entry-points/1`: sentence unchanged, no "start directory"/"started in" wording; *Derives from* `WAY-127@4439a64a`.
4. `agent-instructions`: the not-detected failure mode says "…nor the session's working directory".

| Entry | Old | New |
|---|---|---|
| `claude-code-project-skills` | a06eaca7 | d58fb91f |
| WAY-127 | b40a68e5 | 4439a64a |
| `skill-entry-points` | eb5c0fb8 | eb5c0fb8 |

## Checks

Facts guard exit 0, 0/0, 3 unchecked; decisions guard exit 0, 0 errors, 8 warnings (5 overdue, 3 placeholders), 5
unchecked; invariants guard exit 0, 0/0, 3 unchecked; part-map guard exit 0, 0/0, 7 unchecked; glossary guard 0/0, 4
unchecked; watch exit 0, `pass`; comparison `references checked 378, stale 0`.

## Search findings (WAY-33)

1. `claude-code-nested-skills/1` says "below the directory where it starts" as its source does; the page does not say
   whether nested skills are measured from the new directory after `/cd`. Provisional: no change.
2. `codex-repository-skills/1` "from its current working directory" already agrees.
3. Question: the failure mode's bracket "(Claude Code's documentation states neither is given to the agent…)" now covers
   the working directory, which nobody checked against the documentation. Orchestrator to decide.
4. Outside the foundation with the old wording: all 22 entry points (lines 11, 13), `agent-instructions/skill_entry_points.py:166-167`,
   `agent-instructions/test_skill_entry_points.py:45,48-49`.
5. The watch's docstring (`probes/claude-code-project-skills/test_claude_code_project_skills.py:1-4`) restates the old
   sentence.
6. No other "started in"/"start directory" wording about a session in `foundations/` or `elements/`.

## Polish sentences

- `claude-code-project-skills/1`: Claude Code wczytuje skille projektu z `.claude/skills/` w katalogu startu i w każdym
  katalogu nadrzędnym aż do korzenia repozytorium, w połączonym worktree tylko do jego korzenia, od wersji 2.1.277 bierze
  skille głównego checkoutu, gdy worktree nie ma u siebie `.claude/skills`, a od wersji 2.1.246 po przeniesieniu sesji
  poleceniem `/cd` dokłada skille projektu nowego katalogu.
- WAY-127: Wskaźnik czyta skill the-way z checkoutu albo worktree, w którym sesja pracuje — tam, gdzie wystartowała, albo
  tam, dokąd ją ostatnio przeniesiono — w produkcie się wycofuje, a do innych skilli odsyła pod prefiksem `the-way-`;
  reszta decyzji bez zmian.
- `skill-entry-points/1`: sens bez zmian, nowy odcisk WAY-127.
- `agent-instructions`: niewykrywana awaria to wskaźnik samego the-way wczytany z `.the-way` produktu i wykonany zamiast
  skilla produktu, gdy agent nie zna ani ścieżki wskaźnika, ani katalogu roboczego sesji.

## 14b — rulings on findings 3 and 5 (agent resumed)

The orchestrator's example bracket was not used: the Claude Code page (§ Available string substitutions) says
"`${CLAUDE_SKILL_DIR}` — The directory containing the skill’s SKILL.md file. … Use this in bash injection commands to
reference scripts or files bundled with the skill, regardless of the current working directory." and "Claude Code
substitutes ${CLAUDE_SKILL_DIR} and ${CLAUDE_PROJECT_DIR} in two places: the skill’s markdown content, and Bash rules in
the allowed-tools frontmatter." None of the 22 entry points uses it (search). Bracket as written: "(Claude Code's
documentation names `${CLAUDE_SKILL_DIR}` as a way a skill's text receives the directory of its `SKILL.md`, and no entry
point holds it; Codex gives no file path for a skill it leaves out of its initial list)". Question raised: add a third
check with `${CLAUDE_SKILL_DIR}`? (orchestrator: no, cycle Q11). Watch docstring updated to the fact's current sentence
(lines 1–5). Part-map guard exit 0, 0/0, 7 unchecked; watch pass; `references checked 378, stale 0`. Polish sentence for
the part unchanged.
