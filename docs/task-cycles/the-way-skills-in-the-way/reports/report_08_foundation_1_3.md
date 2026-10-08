# Report 08 — foundation step 1.3, decisions agent (saved by the orchestrator from the returned text)

Wrote three decision changes to `foundations/decisions.md` only; committed nothing. Guard exit 0, `0 error(s),
8 warning(s), 5 unchecked`; reference comparison: exactly the seven expected STALE lines. The search found no glossary
change needed.

## What was written

**WAY-09/1, edited in place (meaning change; question 1).** Binding sentence 1 now ends: "…the files that configure the
whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files and the
project skill entry points under `.claude/skills/` and `.agents/skills/`, which the map gives to `agent-instructions`
(WAY-44), and a `README.md` that describes the repository." Sentences 2–3 unchanged. *Verification* level 2 "complies"
gains, after "…root entry points;": "the project skill entry points under `.claude/skills/` and `.agents/skills/` stand
at the root as files of `agent-instructions`, and the script that generates them stands with its test in
`agent-instructions/`;". *Approved by* `Mariusz, merge of <request link>` (was `…/pull/4`). *Review when* `none`.

**WAY-27/1, edited in place (meaning change; question 2).** Binding sentence: "Nothing in this repository points to a
source outside it that its readers cannot reach, except the place of its tasks that the `## Backlog` section of its
root `AGENTS.md` names: every entry carries its whole reasoning, and what is seen only in such a source is described in
the entry instead of being pointed to." *Verification* "complies" gains: "the-way's root `AGENTS.md` names, in
`## Backlog`, the private note where its tasks are kept;". *Approved by* `Mariusz, merge of <request link>` (was
`Mariusz, 2026-09-16`). *Rationale* gains: "A backlog place is where work is kept, not reasoning an entry rests on, and
WAY-107 sends an agent there."

**WAY-127/1, new, appended.** "How does a session working on the-way itself reach the-way's skills?" Binding: "A session
working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical
tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a
script of `agent-instructions` generates from the skill's `SKILL.md`. An entry point reads its skill and the files it
names from the checkout or worktree the session was started in, stops itself in a product, and hands another the-way
skill on under the `the-way-` prefix. No global link reaches a skill of the-way, and the-way is not installed in
itself." *Scope* agent-instructions, elements-common, project-level, task-cycle, decisions, invariants, glossary,
part-map, environment-facts, installation. *Based on* `claude-code-project-skills@a06eaca7 ·
claude-code-nested-skills@4dd3d448 · codex-repository-skills@7db28f98 · codex-skill-paths@5b5b6c79`. *Relations*
`derives from WAY-44@2f2b6227`. *Verification* level 1 — invariants: `skill-entry-points`; level 2 for the skills'
paragraphs on where the-way lies (complies: a paragraph names the start checkout/worktree for the-way itself and the
pinned `.the-way` for a product, and names a handed-to skill with the prefix; violates: a skill tells an agent to
resolve a global link; a skill run in the-way hands its work to `critique` without the prefix). *Review when* none;
*Origin* none; *Approved by* `Mariusz, merge of <request link>`. *Rationale*: own branch's copy; tracked entry points
reach every checkout, worktree and cloud session without setup; generated, no hand list, in the generator's part
(WAY-44); start directory decides which copy is read; stopping in a product keeps it on its pin (WAY-34); prefix keeps a
personal skill from standing in. *Rejected*: B installer mode without a pin; C untracked per-checkout files; D global
links, per-worktree links, tracked links; names without the prefix. Number 127 provisional.

## Fingerprints

| Decision | Before | Now |
|---|---|---|
| WAY-09 | b829b86a | 16b8026b |
| WAY-27 | 770078ba | 0b40467e |
| WAY-127 | — | b40a68e5 |

## Search findings (WAY-33)

1. Change — generator under `agent-instructions/` vs WAY-09: the sentence on what the directory holds sets a minimum
   before main, not a full list; WAY-44 admits generator and test there; added to the complies example (no fingerprint
   change). Hand-off: the part map's `agent-instructions` responsibility does not cover a generator → 1.6.
2. Question — "entry point" vs glossary `entry`: provisional no change; the glossary guard matches by word
   (`--uses entry` already lists `decisions.md:271` "root entry points"); precedent "readiness gate" in WAY-118 with
   `gate`; a fixed compound. Consequence: a future change to `entry` lists these uses for review.
3. Question — relation to WAY-34? Provisional: none (WAY-34 binds products, WAY-127 sessions on the-way; rationale cites
   it). Cost: a change to WAY-34 will not flag WAY-127. Alternative `derives from WAY-34@<fp>`.
4. Link — WAY-27 and WAY-107: no relation type fits; rationale cites it. Cost: renaming `## Backlog` in WAY-107 would not
   flag WAY-27's exception. Provisional: accept.
5. Question — "the-way is not installed in itself" has no level-1/2 check in WAY-127; today `file-part-assignment`
   catches a `.the-way` gitlink or `.gitmodules` (no part claims them). Provisional: no change; alternative: a separate
   invariant.
6. No change needed: WAY-52, WAY-53, WAY-38, WAY-45, WAY-55, WAY-69, WAY-73/WAY-90 (facts named; facts guard 0
   warnings), WAY-101/WAY-107, WAY-25/WAY-30 (exception written into the decision), WAY-07/WAY-14, WAY-19, WAY-36,
   WAY-22, WAY-04, WAY-125 (its *Based on* cites a local plugin-cache path — an observation source, possibly for the
   return step), WAY-14, 31, 33, 57, 76, 97.

## Guard and comparison

Guard exit 0, 0 errors, 8 warnings (five baseline overdue check-by dates WAY-03, WAY-21, WAY-52, WAY-55, WAY-69; merge
placeholder for WAY-09 :279, WAY-27 :750, WAY-127 :3670), 5 unchecked (from `none`). Glossary guard 0/0; facts guard 0
warnings. `stale_refs.py`: STALE invariants.md:152, 162, 172, 182, 192, 202 WAY-09@b829b86a now 16b8026b;
invariants.md:473 WAY-27@770078ba now 0b40467e; references checked 377, stale 7.

## Polish meaning sentences (WAY-114)

- WAY-09: Repozytorium the-way może na gałęzi głównej trzymać, obok głównych plików instrukcji agentów, także wskaźniki
  skilli projektu w `.claude/skills/` i `.agents/skills/` — jako pliki części `agent-instructions`.
- WAY-27: Nic w repozytorium nie odsyła do źródła, którego czytelnik nie otworzy, z jednym wyjątkiem: miejsca zadań
  the-way wskazanego w sekcji `## Backlog` głównego `AGENTS.md`; każdy wpis nadal niesie całe swoje uzasadnienie.
- WAY-127: Sesja pracująca na samym the-way dostaje każdy skill the-way jako skill projektu `the-way-<nazwa>` przez dwa
  identyczne, śledzone w gicie wskaźniki w `.claude/skills/` i `.agents/skills/`, generowane skryptem części
  `agent-instructions`; wskaźnik czyta skill z checkoutu albo worktree, w którym sesja wystartowała, w produkcie się
  wycofuje, a do innych skilli odsyła pod prefiksem `the-way-`; żadne globalne dowiązanie nie prowadzi do skilla the-way
  i the-way nie jest instalowane w sobie samym.
