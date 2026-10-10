# Slice 3 report — the task cycle never makes an effect outside the repository itself

- Status: DONE
- Commit: 9692cbb feat(task-cycle): Leave every effect outside the repository to the human as an
  action the task names
- Files: `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` (both `i/lf`, kept LF)

## Changes, against the orchestrator's settled points

- (a) Intro, the one human contact: after the decision reserved to a human, a sentence that a human
  action the task document places in the cycle does not stop the cycle midway; the cycle does what
  the repository allows, lists the action in a blocked draft request, and the human performs it at
  the request (WAY-140).
- (b) Step 1: requires `Status: ready for cycle` and every human action its *Human actions* places
  before the cycle done (WAY-124); reads the in-cycle actions, which step 4 takes up. The rest of
  step 1 rewrapped only.
- (c) Paragraph after step 3: kept "writes only in the task's worktree and changes nothing outside
  the product repository"; added "reading outside the repository stays with the agent (WAY-140)".
  The WAY-107 backlog exception left as it was.
- (d) Step 4: removed "external side effect" from the sentence about the product's reserved
  authorization, which now covers only a security-sensitive action (with "prepare what can be
  reviewed and mark the request blocked" kept); irreversible-operation sentence kept unchanged.
  Added: an effect outside the product repository is a human action (WAY-140); for the actions the
  document places in the cycle, prepare what the repository allows and open the request as a
  blocked draft listing them; an effect outside the repository the cycle finds and the document
  does not name joins that list, for the human to place. Tail of step 4 rewrapped only.
- (e) Step 12: a request the cycle marks `blocked`, one that waits for human actions in the cycle
  (step 4) among them, stays a draft. Step 13: where the request waits for human actions in the
  cycle, list them for the human to perform as the task document names them, with each unnamed
  effect found, for the human to place (WAY-140).
- (f) `record_template.md` *Request handoff*: new line "Human actions the request waits for: <each
  action the task document places in the cycle, and each effect outside the repository the cycle
  found that the document does not name, or none>".
- Step numbering unchanged; no `description` changed; `foundations/` untouched.

## Checks

- `python -B gate/run_tests.py task-cycle` — 41 tests OK
- `python -B gate/run_tests.py gate` — 98 tests OK
- `python -B agent-instructions/skill_entry_points.py` — "entry points are current"
- No added line exceeds 100 columns; no CR introduced.
- Tests pinning text: none. `gate/test_skills_reach_the_way_sessions.py` and
  `installation/test_install.py` name `task-cycle/skill/SKILL.md` by path and read its
  `description` only; nothing reads `record_template.md`.

## Self-review against the brief, WAY-140 and WAY-124

- Every element of the brief's goal is present (a–f above). The rule is stated with WAY-140 /
  WAY-124 cited; the skill gives only where in the order of work it applies.
- WAY-140's "reads stay with the agent", "cycle does what the repository allows", "blocked draft
  request listing them", "the human performs them at the request" are each carried. "Before the
  cycle = not ready until done" is carried through WAY-124 in step 1.
- The "joins that list, for the human to place" rule for an unnamed effect was settled by the
  orchestrator; it is consistent with WAY-140's rejection of the agent placing an action alone.

## Concerns

1. The WAY-107 exception (the cycle writes the request link and state in the task's backlog entry,
   which can live outside the product repository, e.g. in private notes) stands next to the
   sentence "changes nothing outside the product repository". It predates this slice and WAY-140
   does not mention it; whether a backlog write is an "effect outside the repository" under WAY-140
   is not settled by the source. Left unchanged; flagged for the orchestrator.
2. A *Human actions* line whose placement still reads `TODO` (template rule): neither WAY-124 nor
   WAY-140 says what the cycle does with it, so step 1 states nothing about it. No rule added.
