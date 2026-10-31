# Handoff — review of the whole change, task `base-checks-place`

The person who requested this cycle delegated intermediate choices to the orchestrator. Questions
go to the orchestrator, never to the human.

- **Worktree:** C:/Storage/repos/the-way/.runs/worktrees/base-checks-place. Read every file from it,
  never from another checkout. The review is read-only.
- **Method:** read `task-cycle/review/SKILL.md` of this worktree whole; a file it names, only when
  the step or variant that names the file comes.
- **Stage:** the whole change.
- **Range:** `00c0a747272a9a179b7a855f256daff985ea2ee1..b9b93af`.
- **Frozen task:** `.runs/task-cycles/base-checks-place/task.md`, whole. It is in Polish.
- **Author's report:** `.runs/task-cycles/base-checks-place/reports/author.md`.
- **Spec and plan:** none. The route was one author without a plan; no slices.
- **Report path:** `.runs/task-cycles/base-checks-place/reports/review.md`.

## Answers of the start

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none.

## Choices the orchestrator gave the author

1. The task's carried question on `task-cycle/record_template.md:116`: one place is enough; the
   template stays unchanged, since its *Verification* table already has the column "Actor, commit
   and environment".
2. The task places the sentence right after a clause that continues with ", and keep a frozen copy…";
   the existing sentence is divided after "failing on it", and the frozen copy opens its own
   sentence.

## Environment

The worktree's ignored `.runs/` holds the cycle's record and a full base gate running in
`.runs/base-checks`; leave both alone, and do not run the full gate: it is the orchestrator's
(WAY-160). Focused checks are yours where your method calls for them.
