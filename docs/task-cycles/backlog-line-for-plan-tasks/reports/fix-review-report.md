PASS 9d5743d7648b4a5095fba28a7d6ab100cd078c3b

# Review of the fix of the whole-change review (reviewed head 9eb2bd6, fix commit 9d5743d)

Range `9eb2bd637697fd5f3cccdb891091110054f9d292..9d5743d7648b4a5095fba28a7d6ab100cd078c3b`, one commit,
confirmed by `git rev-parse HEAD`. Paths are relative to
`the task's worktree root`.

Counts: 0 blocking, 2 Minor (new, within the task, non-blocking), 0 out of scope. All seven findings of
the findings file are fixed.

## The findings, each as fixed or remains

- **B1 (no route for a line the first turn could not make) — fixed.** `project-level/task_line.md:16-22`
  ("Make the line", bullet **When**) now covers all three cases of my finding: the rules not yet known
  with a question standing, a document that exists without a line (written before, or a parked task
  refined again), and in both the line is made in the first later turn in which the rules are known, with
  the turn's text saying it stands unmade. `task_line.md:60-66` ("Move to ready") makes the line already
  ready at acceptance where none stands, with identifier and dependencies, and says so in the acceptance
  record. WAY-154's binding sentence (`foundations/decisions.md:4442-4453`) says the same. The
  orchestrator's pointers (`project-level/lead/skill/SKILL.md` step 4, unchanged) reach the new text
  through `task_line.md`. I judged the orchestrator's new duty (below) as the fix of this finding, not
  as a new defect.
- **Minor 1 (cost in WAY-107's *Rejected* in the author's words) — fixed.** `foundations/decisions.md:2484-2489`:
  the way now carries the human's word as its reason and `unknown` as its cost; the invented cost is
  gone, and the rationale's price about a product with no rules is removed (`:2476-2478`), leaving only
  question 5's cost, the repeated path.
- **Minor 2 (identifier assumption and clash) — fixed.** `task_line.md:22-23` (ask the human, write nothing,
  where another line already carries the identifier) and `task_line.md:43-46` (the two assumptions named,
  with the `a-b.md`+`c` / `a.md`+`b-c` example). I re-ran the example (`python -I`, exit 0): both give
  `a-b-c`, as the file says.
- **Minor 3 (three guidelines skills say "edits only the task document and its turn") — fixed.** The
  three `product-guidelines/{coding,testing,styleguide}/orchestrated_mode.md` now add "the task's line in
  the backlog, as `refine-task` gives" to the skill's own writes.
- **Minor 4 (the rule in five places) — fixed.** `grep -rn "first creat\|first later" project-level
  product-guidelines AGENTS.md` finds one line, `task_line.md:16`. `read_sources.md`,
  `orchestrated_mode.md` and `lead/conversation_template.md` point to `task_line.md`; the orchestrator's
  role-specific "you set no order between those writes" stays in `lead/skill/SKILL.md:104-106`. (WAY-154
  holds the moment as the entry's binding sentence; that is the entry, not a copy in a skill.)
- **Minor 5 (WAY-154 "when it changes them") — fixed.** `foundations/decisions.md:4449`: "when the plan's
  dependencies change", which matches `route_changes.md`.
- **Minor 6 (entry/line vocabulary) — fixed** at the two places named: `project-level/task/skill/final_review.md:27`
  ("the task's line") and the paragraph the change added to `read_sources.md:23` ("no line there yet").

## The two reaches the author names

- **WAY-154's binding sentence reworded for B1, and the orchestrator's making of a missing line at
  acceptance added to the entry:** within the fix. B1's sentence in `task_line.md` would otherwise
  contradict the entry (WAY-263), so the entry had to change. The orchestrator's fallback is a duty of
  the kind question 1 *Not chosen* names ("the orchestrator takes the whole backlog ... one more duty"),
  but only as a narrow fallback where no line stands, not as a general taking of the backlog; the
  refiner still makes every line it can. I suggested the fallback myself, and it is the least change
  that closes B1 case 3. The human may weigh it at the request; not a defect.
- **`project-level/lead/skill/SKILL.md` step 3.1 with the moment taken out:** within the fix (Minor 4),
  the sentence now reads correctly and keeps the orchestrator's "no order between those writes".

## New findings in the fix diff

Both Minor, within the task, blocking nothing.

1. **WAY-154's *Verification* "complies" example still names only the first turn.**
   `foundations/decisions.md:4462-4464` ("each, in its first turn that creates its document, also writes
   its task's line") against the binding sentence, which now also allows the first later turn that can.
   The example is not contradicted (the first-turn case still complies) and a refiner that makes a late
   line complies by the binding sentence, so it is narrower, not wrong. Fix: add "or in the first later
   turn that can" to the example.
2. **Adjacent vocabulary in `read_sources.md`.** `project-level/task/skill/read_sources.md:17-24`: "link
   it from that entry" (older text) stands one paragraph above "Where the task has no line there yet".
   Both name the same object; Minor 6 asked for the two named places only, which are fixed. Cosmetic; and
   one wrapped line in `foundations/decisions.md:2488-2489` ("... reports a mismatch; a status of a line
   fixed in the-way's skills — a skill of the-way would assume") runs to about 140 characters.

## Declined to judge

- The out-of-scope finding of the first review (a task returned to refinement keeps a Ready line): not in
  the findings file, so not fixed and not judged here (WAY-161).
- Whether the status and dependency forms of the vault's rulebook are right: private notes, out of the
  change (WAY-107), as before.

## Checks run

All read-only, from the reviewed worktree, `python -B`; `git status --short` empty.

| Check | Command | Exit |
|---|---|---|
| Foundation identifiers and references | `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0 ("0 error, 0 warn, 3 info") |
| Private paths and note links in tracked files | `python -B task-cycle/test_tracked_files_private_paths.py` | 0 (1 test OK) |
| One rule, one place | `grep -rn "first creat\|first later" project-level product-guidelines AGENTS.md` | 0; one hit, `task_line.md:16` |
| Guidelines skills updated | `grep -rn "edits only the task document" product-guidelines` | 0; three hits, each with the line added |
| Clash example | one-off `python -I` expression | 0 (`a-b-c` for both inputs) |
| Diff and log | `git diff 9eb2bd6..9d5743d`, `git log 9eb2bd6..HEAD`, `git rev-parse HEAD` | 0; head confirmed |

Not run: the full gate and the `project-level` directory run (the orchestrator's); the skill entry-points
test, since no skill description changed in the fix (the diff holds no frontmatter change).

## Reaches beyond the dispatch

None beyond the fix diff, the findings, the fix report and the files they name. I re-read
`project-level/task_line.md` whole and the full fix diff; I did not re-read decisions of the first review
beyond WAY-154 and WAY-107, which the fix changed.

## Unread material

Decisions: WAY-154 and WAY-107 read whole on the new head (the only decisions the fix changes); the other
decisions of the first review stand as I recorded them (28 whole, 114 by title; unchanged by this fix).
Invariants, part map, glossary: read in the first review, not changed by the fix. Guidelines: none exist.
The fix report's claims were verified against the diff.

## Searches not found or unclear

none.
