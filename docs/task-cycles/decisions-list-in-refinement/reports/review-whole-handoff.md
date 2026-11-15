# Handoff to the reviewer of the whole change — decisions-list-in-refinement

You review the whole change of one task as an agent that did not make it. The orchestrator delegated
the intermediate choices to itself; none of its words is the human's approval.

- Worktree (work from its root, read-only except your report and your directory): `the task's worktree (the repository's root)`, branch `task/decisions-list-in-refinement`.
- Method: read `task-cycle/review/SKILL.md` whole; your variant is **the whole change**, so read `task-cycle/review/whole_change.md` as it says and follow it. Read a further file of the method only when its step comes.
- Range: base `9cbc6b2c46837c956f863843de0dd0bc3d32d8f1` (target branch `foundations`) to head `51f2590` — compute the diff yourself (`git diff 9cbc6b2..51f2590`) and confirm `git rev-parse HEAD` is `51f2590`.
- Frozen task (read whole): `.runs/task-cycles/decisions-list-in-refinement/task.md`. Its language is Polish; the change's texts are English.
- Spec, plan, slices: none (one author without a plan; the whole change is yours to judge, no slice had a review of its own).
- Author's report (claims to verify, not evidence): `.runs/task-cycles/decisions-list-in-refinement/reports/author-report.md`. The foundation entries it writes are WAY-377 (row 1) and WAY-378 (row 2); `request.md` will take their meaning sentences from that report.
- Answers of step 4: trust boundary — no; irreversible operation — no. Move of a pin: none.
- Your directory for working copies and the index of your selection: `.runs/review-whole/`. Remove any copy before you return and say so in the report.
- Your report: `.runs/task-cycles/decisions-list-in-refinement/reports/review-whole-report.md`, first line `PASS <sha>` or `FAIL <sha>`.
- Select your own foundation and guidelines by "Reading the foundation" in `elements/common/way_of_working.md` (the change touches the part `project-level` and the decision log; the-way holds no `guidelines/` directory). `decision_index.py` takes `--decision WAY-377`, not the bare number `377`.

## Points the orchestrator puts to you (to judge, not to accept)

The author's report lists choices the task does not state. Check each against the task's words and the foundation, and grade it yourself:

1. A guess that the critique finds "most likely wrong" is treated as a gap of the document and shown to the human (the task says: the human sees only matters really open and gaps of the document).
2. A critique quotation that does not hold voids the critique's verdict on that matter; the refining agent settles it from the file or counts it open.
3. The name `.runs/decisions-list/<task-name>.md` and who writes which part of it (the refining agent in the manual mode; the project orchestrator writes *List* and *Critique* and the refining agent *Verdicts* in the orchestrated mode, in two turns).
4. The decision pair WAY-377 / WAY-378 as two decisions, and WAY-377's *Rejected*, which holds only the three ways the task keeps, against what WAY-100 asks of a decision that adopts an outside practice.
5. The step runs "when the document has a non-empty *Decisions in play* or the task changes a skill or an instruction file": check that the three skill files and WAY-377 say the same, and that nothing outside them (for example `project-level/lead/` or the task template) now contradicts the new text.

Also check: the task's *Out of scope* (`resolve_gaps.md` and WAY-374 untouched; the "strongest argument" rule not made), that the section 6 sentence of `project-level/task/skill/SKILL.md` stays one sentence next to the check of the complete document, and that no word of the new text uses "gate" in a meaning the glossary gives another.

The author left unread, by its report: WAY-113, WAY-134, WAY-124 and WAY-154 whole (read by their binding sentences), the part-map entries of `project-level` and `decisions`, the linked entries of the invariants of the part, and `instruction-files/changing.md`, `writing.md`, `judging.md`, `tool_loading.md`. You select your own reading; take these into it where they bear on the change.

## Boundary

Run no check that is the orchestrator's: never the whole gate (`python -B gate/run_tests.py` with no directory). Focused checks (`foundation_check.py`, `check_instructions.py`, one directory of the gate) are yours to run if you need them. Do not fix anything. Return your status, the first line of your report, the checks you ran with exit codes, your **Unread material** and **Searches not found or unclear**, and the report's path.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
