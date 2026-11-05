# Handoff — the one author of the change

You make the whole change of one task as the one author, without a plan. The person who requested
this cycle has delegated intermediate choices to the orchestrator; nothing here is the human's
approval.

- Worktree (work from its root, on branch `task/stage-remarks-check`, base `b96cfff`):
  `C:\Storage\repos\the-way\.runs\worktrees\stage-remarks-check`
- Method: `task-cycle/change/SKILL.md` in that worktree — read it whole; your variant is "the whole
  change as the one author". Read a file it names only when the step that names it comes. After
  the code, take the foundation step as `task-cycle/skill/foundation_step.md` gives (read it whole
  for that step), writing each entry through the skill of its element
  (`elements/decisions/skill/SKILL.md` for a decision).
- Frozen task, read whole: `.runs/task-cycles/stage-remarks-check/task.md` in the worktree. No
  spec, no plan.
- Report path: `.runs/task-cycles/stage-remarks-check/reports/01-author-report.md`
- Do not run the product's gate (`python -B gate/run_tests.py`); the orchestrator runs it. Run the
  tests of the directory you change: `python -B gate/run_tests.py task-cycle`. A new test file
  runs only once it is added to git (`git add`).
- Product rules: `agent-instructions/README.md` (commit on the task branch, short English commit
  messages, no unrelated changes).

## Answers at start

- Trust boundary: no. Irreversible operation: no. Open design choice: none; reserved choice: none.
  How the script reads the reports and matches items is a choice of how to make what the task
  settles: make it and name it in your report.
- Route: one author without a plan. Your class is `same` as the orchestrator's.

## What to read (selected by the orchestrator)

Foundation entries, each whole, from `foundations/decisions.md`: WAY-260 (the rule this task
enforces), WAY-148, WAY-159, WAY-164, WAY-290, WAY-291 (the pattern the new script's
"holds wrong" rule copies), WAY-286, WAY-38 and WAY-89 (scripts: Python 3.14, standard library
only), WAY-293. Parts touched: `task-cycle` (the script, its tests, the three process files) and
`decisions` (the entries you write). Read the part map entries for both and the glossary entries
for terms you use.

Files to read before changing: `task-cycle/skill/SKILL.md` (steps 5, 9–14 and the paragraph on
reports; the rule for copying **Searches not found or unclear** is near line 71),
`task-cycle/skill/correction.md`, `task-cycle/record_template.md` (the block *Process remarks on
the-way* in *Request handoff*), `task-cycle/skill/request_template.md` (it names the handling of
a form-check error; the new script's rule must read like it) and, as models for a script and its
tests, `task-cycle/request_check.py`, `task-cycle/test_request_check.py` and `task-cycle/cycle_stages.py`.
`.claude/skills/` and `.agents/skills/` entry points need regeneration only if you change a
skill's description (you should not).

## External material (read-only, outside the repository)

- The nightly digest, which cuts the remarks block out of a record:
  `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py`,
  functions `_opens_block` and `extract_remark_blocks` (about lines 208–280). The block form you
  fix in the template must be one it cuts: an item starting "Process remarks" (also accepted:
  "Process remark", "Process improvements", "Other process remarks", "Searches not found") or the
  indented lines under it deeper than its list marker. That script is out of scope: do not change it.
- Real archives for the acceptance test, read with `git show` from `C:\Storage\repos\loop2`,
  never checked out:
  `31ac651:docs/task-cycles/plomyk/`, `b311814:docs/task-cycles/reset-hasla/`,
  `d79c8e4:docs/task-cycles/kopia-bazy/` (and `67620ff` for the first `kopia-bazy` archive). Each
  holds `cycle.md` and `reports/`. Stage reports hold the section in two forms: a heading
  `## Searches not found or unclear`, or a bold label inside a line/paragraph; items are also
  written in forms such as "None unresolved. Unclear: …". Use these archives to learn the real
  forms. Your script's tests may carry small fixtures copied from them (trimmed, no secrets or
  personal data); they do not read `C:\Storage\repos\loop2` at test time, since the repository
  must pass its gate on any machine.

## What to make

Everything in the frozen task: *To do* 1–3, both acceptance criteria, and the three rows of
*Settlements to record* (rows 1–3) as decisions. Specifically:

1. A script under `task-cycle/` (Python standard library only) that, given a cycle-record
   directory, reads the **Searches not found or unclear** section of every report in `reports/`
   in both forms, and lists every item other than `none` that the record's process remarks do not
   contain word for word, with the item's report path. It only lists; it exits non-zero when it
   lists something. With tests (WAY-215 has no guidelines in the-way yet; follow the existing
   tests of `task-cycle/`).
2. `task-cycle/skill/SKILL.md` and `correction.md`: the orchestrator runs the script before every
   commit that adds the record to `docs/task-cycles/<task-slug>/` — step 12, its repetition in a
   correction, and the variants of a blocked request (step 9 sub-step 4 stop; the blocked
   variants in `request_template.md` if they commit a record) — appends each listed item word for
   word with stage name and full report path, and runs the script again until it lists nothing.
   A listing the orchestrator holds a script error does not stop the archive and the script is not
   fixed in that cycle: the archive is written, the case is entered in the process remarks, and
   the request's section for the human's decisions names it, as for `task-cycle/request_check.py`.
3. `task-cycle/record_template.md`: one form of the process-remarks block, the one the digest
   cuts and your script reads; remarks stand only in that form, not in a separate section or file.
4. Acceptance: your script, run on the three `loop2` archives, lists each item described in the
   task's *Context* (the return step in `plomyk`; the reconciliation and its review in
   `reset-hasla`; slice 6's fix and correction 2 in `kopia-bazy`). Report the command and its
   output. The tests need not contain this run.
5. Foundation: the three rows as decisions, and the search of the whole foundation for the entries
   they touch (WAY-33), including WAY-260's text that says where the items go.

Commit on the task branch; the report is not committed. The report states the own-work check
(WAY-164), every check with its command and exit code, every reach beyond this handoff, and
**Searches not found or unclear**, each item or `none`. Return your status, your commits, a
one-line check result and the report path.
