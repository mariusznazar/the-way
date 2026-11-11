# Fix report: the review of the whole change (reviewed head 9eb2bd6)

**Status:** done. Seven findings fixed, none contested.

**Commit:** `9d5743d` (one commit on top of `9eb2bd6`; explicit paths).

Files changed in it: `project-level/task_line.md`, `project-level/task/skill/read_sources.md`,
`project-level/task/skill/orchestrated_mode.md`, `project-level/task/skill/final_review.md`,
`project-level/lead/conversation_template.md`, `project-level/lead/skill/SKILL.md`,
`product-guidelines/coding/orchestrated_mode.md`, `product-guidelines/testing/orchestrated_mode.md`,
`product-guidelines/styleguide/orchestrated_mode.md`, `foundations/decisions.md`.

## Findings

- **B1 — fixed.** `project-level/task_line.md`, "Make the line", first bullet **When**: besides
  the first turn that creates the document, a line that could not be made then (the rules are not
  yet known and a question stands) or that never existed (a document written before, a parked task
  refined again) is made in the first later turn in which the rules are known, with the turn's text
  saying the line stands unmade until then. "Move to ready": where no line stands at acceptance,
  the line is made, already ready, with identifier and dependencies, and the acceptance record says
  so. WAY-154's binding sentence (`foundations/decisions.md`, "or in the first later turn that can
  where that turn could not") and the orchestrator's duty ("making it already ready where none
  stands") say the same. The sentences in `orchestrated_mode.md` and `read_sources.md` now point
  to `task_line.md` instead of repeating the moment.
- **Minor 1 — fixed.** `foundations/decisions.md`, WAY-107 *Rejected*: the way "rules kept at the
  product" now carries the human's word as its reason and `unknown` as its cost; the author's
  cost sentence is gone. WAY-107 *Rationale*: the price "a product whose tasks lie in a place with
  no such rules finds an agent asking" is removed; only the repeated path stays (question 5's cost).
- **Minor 2 — fixed.** `task_line.md`, "Make the line", last bullet: where another line already
  carries the identifier derived for the task, write nothing and ask the human. "The identifier": a
  paragraph naming the two assumptions (plan file names differ in the place; no two pairs join to
  the same text, with the `a-b.md` + `c` / `a.md` + `b-c` example) and saying the step above is
  what catches a clash.
- **Minor 3 — fixed.** The three `product-guidelines/*/orchestrated_mode.md` files now read "edits
  only the task document, its turn, the task's line in the backlog, as `refine-task` gives, and ...".
  Chosen over pointing to `orchestrated_mode.md` because each sentence lists the skill's own writes,
  and the added item is a pointer to `refine-task`, not a second copy of the rule.
- **Minor 4 — fixed.** The refiner's copies of the moment and of "parallel, no queue" in
  `read_sources.md`, `orchestrated_mode.md` and `lead/conversation_template.md` now point to
  `task_line.md`, the only place that holds them (`grep -rn "first creat"` over `project-level` and
  `product-guidelines` finds one line, `task_line.md:16`). The orchestrator's role-specific line in
  `lead/skill/SKILL.md` stays, with the moment taken out ("each makes its task's line as
  `project-level/task_line.md` gives, and you set no order between those writes").
- **Minor 5 — fixed.** WAY-154: "when the plan's dependencies change".
- **Minor 6 — fixed.** "Line" for "entry" in `final_review.md` (the move to ready) and
  `read_sources.md` (the line I added: "Where the task has no line there yet"). Existing sentences
  of those files that say "entry" for a task place item (for example "link it from that entry") are
  older text and untouched.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 3 info".
- `python -B task-cycle/test_tracked_files_private_paths.py` — exit 0, 1 test OK.
- One-off derivation check, `python -I -B -c ...`, exit 0, four inputs against hand-written
  literals: `player-game.md` + `forest-on-hex-grid` = `player-game-forest-on-hex-grid` (True);
  `MVP2 plan (v2).md` + `forest-on-hex-grid` = `mvp2-plan-v2-forest-on-hex-grid` (True);
  `a-b.md` + `c` = `a-b-c` (True); `a.md` + `b-c` = `a-b-c` (True), so the two Minor 2 inputs do
  clash, as the file now says and as the step "ask the human" covers.
- Not run, as the handoff says: `project-level` directory and the full gate.

## Own-work check

- Requirement most likely not met by the fix: that the rule has one place (finding 4) while B1's
  new cases (a late line, a line made at acceptance) are covered. Check: `grep -rn "first creat"`
  over `project-level` and `product-guidelines` (exit 0) printed one line, `task_line.md:16`, and
  `grep -n "task's entry\|no entry there"` over `final_review.md` and `read_sources.md` (exit 1)
  found none. The three B1 cases are covered as text only; no test reaches these files.
- The fix does not add a new rule beyond B1's sentence and Minor 2's step; both are the reviewer's
  own suggested wording, with the late-line step stated for a refiner of any turn.

## Reach beyond the handoff

- `foundations/decisions.md` WAY-154: besides Minor 5, I also changed the binding sentence's moment
  (B1) and added the orchestrator's making of a missing line at acceptance, so the entry and the
  skill text say the same. The findings name `task_line.md`; the entry would otherwise contradict it.
- `project-level/lead/skill/SKILL.md` step 3.1: the moment taken out, for Minor 4's one place. Not
  named by finding 4 as a copy to change ("the orchestrator's copy may stay"); I removed only the
  moment from it.

## Unread material

none. I re-read the handoff, `fix-findings.md`, `task-cycle/change/fix.md` and the files I changed.
`reports/whole-review-report.md` (the evidence behind the findings) I did not read; the findings
file carried the evidence I needed.

## Searches not found or unclear

none.
