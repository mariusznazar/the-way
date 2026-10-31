# Handoff — one author, task `base-checks-place`

The person who requested this cycle delegated intermediate choices to the orchestrator. Questions
go to the orchestrator, never to the human.

- **Worktree:** C:/Storage/repos/the-way/.runs/worktrees/base-checks-place. Work from its root; read
  every file from it, never from another checkout. Branch `task/base-checks-place`, base
  `00c0a747272a9a179b7a855f256daff985ea2ee1`.
- **Method:** read `task-cycle/change/SKILL.md` of this worktree whole; a file it names, only when
  the step or variant that names the file comes.
- **Variant:** the whole change as the one author.
- **Stage and boundary:** make the change, commit it, return before review. Do not run
  `python -B gate/run_tests.py` without a directory: the full run is the orchestrator's (WAY-160).
- **Frozen task:** `.runs/task-cycles/base-checks-place/task.md`, read it whole. It is in Polish; the
  sentence to add is in English and goes in word for word.
- **Report path:** `.runs/task-cycles/base-checks-place/reports/author.md`. Return only the status,
  the commits, a one-line check result naming what failed or did not run, and the report path.

## Answers of the start

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Route: one author without a plan.

## Choices that bind you

1. The task's carried question on `task-cycle/record_template.md:116`: one place is enough; the
   template stays unchanged. The template's *Verification* table already has the column "Actor,
   commit and environment". If your reading of the template shows this wrong, say so in your report
   with the evidence; do not edit the template.
2. The task places the sentence right after the clause "Record the base commit and the checks
   already failing on it", which continues with ", and keep a frozen copy of the task document…".
   Divide that sentence after "failing on it": the new sentence stands next, and "Keep a frozen copy
   of the task document with its original path and its approval date or source commit." becomes its
   own sentence. The sentence after it, "Where step 2 moved the pin, the branch, its base and those
   checks already stand.", stays.

## Read

- Foundation entries, each whole in `foundations/decisions.md`, as the range from its heading to the
  next heading: WAY-140, WAY-160, WAY-256 (the task's *Decisions in play*).
- Invariant `return-step-record` in `foundations/invariants.md`.
- Part-map entry `task-cycle` in `foundations/part_map.md`.
- The product has no `guidelines/` directory, so no guideline file applies.

## Keep in mind

- Keep the file's wrapping: lines of about 100 columns, step 4 indented by three spaces. Rewrap only
  the paragraph you change. The file is stored with LF endings.
- The worktree's `.runs/` holds the cycle's record and a running base gate in `.runs/base-checks`;
  leave both alone. Commit by explicit paths, never `git add -A`, `git add .` or `git commit -a`.
- Commit message in English, in the form of the repository's recent commits (`docs: …`), body not
  needed.
- This is a text that instructs agents; per the method it gets no test of its text. Focused checks:
  the tests of the directories that read this file (`python -B gate/run_tests.py task-cycle`,
  `python -B gate/run_tests.py agent-instructions`) and
  `python -B elements/common/foundation_check.py .`.
