# Report 17 — final fix wave, foundation (saved by the orchestrator from the returned text)

Three corrections in `decisions.md`, `invariants.md`, `part_map.md` only; nothing committed; guards 0 errors;
`stale_refs.py` `stale 0`. Process-root skills (`record-decision`, `record-invariant`, `update-part-map`) with templates,
`common/rules.md`, `way_of_working.md`, examples, the product glossary. (The generator change was not yet in the worktree
when checked — it follows in the code fix.)

A. WAY-27 (`decisions.md:731`). Old: "Nothing in this repository points to a source outside it that its readers cannot
reach, except the place of its tasks that the `## Backlog` section of its root `AGENTS.md` names: every entry carries its
whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to." New:
"Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole
reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one
exception is the place of its tasks, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else."
("named in … and nowhere else" limits both the target and where the pointer stands.) Violates example added: "an entry's
*Origin* points to a task's description in the private notes". Rationale clause added: "…and WAY-107 sends an agent
there; named in that one section, it stays a place to find work and never becomes a source an entry points to."
Fingerprint 0b40467e → fb27e458.

`outbound-link-reach/1` (`invariants.md:469`). Old: "…or into a private note collection other than to the place of tasks
that the `## Backlog` section of the root `AGENTS.md` names." New: "No file git tracks contains a link into a repository
that a reader not signed in to its host cannot open, or into a private note collection, other than a link in the
`## Backlog` section of the root `AGENTS.md` to the place of the repository's tasks." Version `/1`; Correction none;
Method `TODO`; Derives from `WAY-27@fb27e458`; fingerprint 8577ad1d → 6d9df030; nothing refers to it.

B. Part map `agent-instructions` (`part_map.md:195-196`), new failure mode: "a tool cannot parse an entry point's
frontmatter — a session on the-way may not list that skill, and uses a personal skill of that name or none — high — not
detected". No prevention note (the template has no place for one). "may not list": no fact records how either tool
handles unparseable frontmatter.

C. WAY-127 *Rejected* (`decisions.md:3689-3690`): "names without the prefix — which skill a session gets would rest on how
Claude Code and Codex settle two skills of one name." Fingerprint 4439a64a unchanged.

Guards: decisions 0 errors, 8 warnings (5 overdue, 3 placeholders at :279, :751, :3672), 5 unchecked; invariants 0/0, 3
unchecked; part map 0/0, 7 unchecked; extra `--merge-onto c64a607`: decisions 5 errors all expected pre-merge (WAY-09,
WAY-27 differ from c64a607, three placeholders), no stale relation; invariants 0 errors, 1 unchecked. `references checked
378, stale 0`.

Search: `WAY-27`, `0b40467e`, `outbound-link-reach` only at WAY-27 and the invariant; no check cites the invariant; WAY-107
consistent; WAY-101 unaffected; `## Backlog` names the tasks file and `_zadania\` — both the place of tasks, inside that
section; only frontmatter-related entry is `skill-entry-points` (unchanged); glossary unaffected.

Polish sentences:
- WAY-27: Nic w tym repozytorium nie wskazuje źródła spoza niego, do którego czytelnik nie dotrze: każdy wpis niesie całe
  swoje uzasadnienie, a to, co widać tylko w takim źródle, jest opisane we wpisie zamiast wskazane; jedynym wyjątkiem jest
  miejsce zadań, nazwane w sekcji `## Backlog` głównego `AGENTS.md` i nigdzie indziej.
- outbound-link-reach: Żaden plik śledzony przez git nie zawiera linku do repozytorium, którego nie otworzy czytelnik
  niezalogowany u jego hosta, ani do prywatnego zbioru notatek, poza linkiem w sekcji `## Backlog` głównego `AGENTS.md`
  do miejsca zadań repozytorium.
- agent-instructions: Gdy narzędzie nie umie odczytać nagłówka (frontmatter) punktu wejścia skilla, sesja na the-way może
  tego skilla nie zobaczyć i użyć osobistego skilla o tej nazwie albo żadnego — szkoda wysoka, nic tego nie wykrywa.
- WAY-127: Nazwy bez prefiksu odrzucono, bo to, który skill dostanie sesja, zależałoby od tego, jak Claude Code i Codex
  rozstrzygają dwa skille o tej samej nazwie — znaczenie decyzji się nie zmienia.
