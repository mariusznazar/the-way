# Foundation-stage handoff (F1–F3)

The user invoked `the-way-implement-task` and delegated intermediate choices to the root
orchestrator. You are the foundation author of this cycle: you write the decisions (F1), the
glossary term and part-map changes (F2) and the invariant sentences (F3) of the plan, on the task
branch, before any slice. You will be resumed between stages; keep your identity. You are the
sentence author of every invariant (WAY-69): you never write an invariant's check (F4) or the code
of slices S2–S3. Send questions to the root by returning them; never ask the human.

- Worktree: `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, branch
  `task/product-guidelines-styleguide`, base `96623ed7710100fe6e11a0ce3c052fc44d4af52d`. the-way is
  the top-level repository; before `main` an existing entry is edited in place (README, WAY-07).
- Read whole: the frozen task `.runs/task-cycles/product-guidelines-styleguide/task.md` (binds; its
  27 rows carry accepted meanings — the wording is yours, the meaning the row's, WAY-134), the
  reviewed spec `spec.md` (§2, §3.3, §7, §9 especially), the plan `plan.md` (*Foundation entries*,
  *Foundation stages*), the root's rulings C5–C26 in `cycle.md`, `agent-instructions/README.md`,
  `elements/common/rules.md`, `elements/common/way_of_working.md`.
- Skills (project skills of this worktree, read whole when their stage runs):
  `elements/decisions/skill/SKILL.md` (F1), `elements/glossary/skill/SKILL.md` and
  `elements/part-map/skill/SKILL.md` (F2), `elements/invariants/skill/SKILL.md` (F3), each with the
  element's `template.md` and `examples.md`. Select the foundation by "Reading the foundation"
  (WAY-150) for each stage; the designer's `reports/foundation-selection.md` is a map.

## Stages and boundaries

- **Turn 1 — F1a:** G1–G6, G24, G25, G26; WAY-09 edited in place (spec §2.1, root C10); *Scope* of
  WAY-38 and WAY-27 gains `product-guidelines`. Run the decisions skill's whole-foundation search
  (WAY-33) for these entries. Commit. Return.
- **Turn 2 — F1b:** G7–G23 (they name G6's fingerprint). Search. Commit. Return.
- **Turn 3 — F2 and F3:** the glossary term "guidelines" (row 25); the part `product-guidelines`,
  the *Depends on* and flow changes, the surface `guidelines-form-check-command` (root C25); the
  eight new invariants of the plan with their *Part* fields (root C13) and the renewal of the six
  invariants deriving from WAY-09 (fingerprint only, sentence and version unchanged). Expected
  before the code: the part-map guard reports `product-guidelines/**` matching no file and the
  trust boundary and surface naming missing files — record, never stub. Record the
  whole-foundation search at the end of F3. Commit. Return.

Rules for every entry: *Approved by* `Mariusz, merge of <request link>` (WAY-14), never a date;
every *Review when* set by you; *Verification* per spec §9.3; G5 and G24 each `narrows WAY-114` with
its area; G19 `narrows` G2; every relation carries its fingerprint computed with
`relation-model/fingerprint.py`. Where the code of a later slice would contradict an entry you
write, say so. Ask the root (return without writing that entry) only where you have no
recommendation, an entry would change the meaning of an approved decision beyond WAY-09's edit, a
row's meaning cannot hold against a current entry, or a row needs a value neither the row nor your
work gives — never write a row with another meaning.

For the request, keep for every entry written or changed one sentence of its meaning in Polish
(the task document's language), in your report.

Commit only by explicit paths (`git add <file>`), English messages in the repository's style
(`docs(foundations): …`). Write only `foundations/*.md` and your reports under
`.runs/task-cycles/product-guidelines-styleguide/reports/`.

## Checks per turn

Run, keeping complete output in `reports/` as `foundation-<turn>-<name>.txt` with command and exit
code in your report: the decision guard
`python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`
(turns 1–3); in turn 3 also the invariant, glossary, part-map and environment-facts guards with the
same no-main options (part map: `--base none`), and `python -B gate/run_tests.py` for
`elements/decisions`, `elements/invariants`, `elements/glossary`, `elements/part-map`, `gate`;
`git diff --check`. Recompute by hand (script in `reports/`) every fingerprint a relation carries
and report stale ones (none acceptable). Every warning and `unchecked` line kept.

## Report

`reports/foundation.md`, one section per turn: entries written with identifiers and line ranges,
the Polish meaning sentences, the row each holds, relations and fingerprints, searches with what
they found, choices with evidence and cost if wrong, check commands with exit codes and output
paths, changed files with added/removed lines per commit, unresolved concerns. Return message:
status, commits, check results (failures and unchecked named), questions.
