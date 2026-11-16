# Handoff to the author — the return step

You are the one author, resumed, for the return step (step 11 of the cycle). Same worktree
`the task's worktree (the repository's root)`, branch `task/readiness-approval-rename`; the
code is reviewed (`PASS` at `cef14df7` for the fix, `PASS` earlier for the whole change); the head is
`cef14df7`. The delegation, the answers of step 4 (trust boundary: yes; irreversible operation: no) and
your first handoff's rules stand. Your directory for working copies: `.runs/author-return/` (removed
before you return; say where each stood).

**Stage.** Read whole `task-cycle/skill/return_step.md`, and `task-cycle/skill/foundation_step.md`
(as it names the way the return step writes), and the `SKILL.md` of an element at the path
`foundation_step.md` gives when you write an entry of that element. The return step is not a variant of
`make-change`; it compares and corrects. It needs no result of the full gate, and you do not run the gate.

**What to compare.** The foundation entries the change edits (decisions edited, the invariant
`project-readiness-check`, the glossary entries `gate` and `projected entry`, the part map where it names
files or words renamed), those the task names (*Decisions in play*, *Settlements to record* rows 1–6 —
the frozen task is `.runs/task-cycles/readiness-approval-rename/task.md`) and those a search of the
foundation finds, with the code and files of the repository, and correct in the same change whatever no
longer matches. In particular:
- the part map `foundations/part_map.md`: file names, the renamed file `project-level/skill/readiness_approval.md`,
  words of responsibilities (`gate`, `entry`) of the parts touched;
- every decision, invariant, term and fact that still holds the old names `readiness gate`, `gate record`,
  `ready for gate`, `project-readiness-gate`, `readiness_gate`, or "entry" in the locations-file or
  backlog-line meaning, in any file of `foundations/`, `elements/`, `project-level/`, `task-cycle/`,
  `process-audit/`, `foundation-review/`, `guidelines/`, `product-guidelines/`, `installation/`,
  `instruction-files/`, `agent-instructions/`, `AGENTS.md`, `README`s (English text; Polish untouched);
- WAY-342 (a row under *Withdrawn identifiers*, not a heading): confirm it is the one place the task's
  "cited question of WAY-342" means;
- each row of *Settlements to record* — the place it went to, as the record's *Return step* gives it
  (rows 1–2 glossary entries, row 3 template and script, row 4 invariant identifier, rows 5–6 sentences of
  WAY-320 and WAY-140);
- the entries you write or change must not carry history (no "formerly", no dates of events), as the
  foundation's rules say.
Do not write an invariant unless the task, a decision or the human sets the rule. The orchestrator
settles the request's description (To do 6), not you. Make no change outside what the comparison finds;
where nothing no longer matches, commit nothing.

**Report** to `.runs/task-cycles/readiness-approval-rename/reports/author-return-report.md`, with the
fields the record's *Return step* gives: foundation compared with code; decisions written or changed;
invariants; environment facts; glossary terms; part-map changes; projected entries written whole or in
part; rows of *Settlements to record* written (row number and where each went); each check with command
and exit code (`python -B elements/common/foundation_check.py`, the focused runs of directories you
touch); **Unread material**; **Searches not found or unclear** (`none` if nothing); working copies.
Return only status, commits (or none), a one-line check result and the report path.
