# Handoff — the one author of the change (task `deployment-skill-guide`)

Delegation: the person who requested this cycle has delegated intermediate choices to the
orchestrator; nothing below is that person's approval. You do not ask the human; you send questions to
the orchestrator and return at your boundary.

Worktree (work only here, from its root): `the task's worktree`,
branch `task/deployment-skill-guide`, base `d40d1cb942c4fbaddb7ece1dc6d472d15cd83430`. Process pin: this
checkout is the-way itself, there is no pin.

Method: read `task-cycle/change/SKILL.md` whole; your variant is "the whole change as the one author".
Read a file it names only when the step that names it comes. Your stage ends with your report; you run
neither the product's full gate (the orchestrator does) nor the next stage. Also read
`agent-instructions/README.md` (the integration rules of the-way before `main`) and
`task-cycle/skill/foundation_step.md` (you write the foundation entry as it gives, following
`elements/decisions/skill/SKILL.md` and the files that skill names).

Task (frozen, read whole): `.runs/task-cycles/deployment-skill-guide/task.md` (copy of the task document,
`Status: ready for cycle`, settlements accepted 2026-11-14). Its *To do* items 1-7 are the change.
There is no spec and no plan.

Answers of step 4:
- Trust boundary: no (the change edits prose in `project-level/task/`, and the decision log; none of the
  three boundary scripts of the part `project-level`).
- Irreversible operation: no.
- Open design choice: none. Both rows of *Settlements to record* settle it; the file name is yours to
  choose (suggested: `project-level/task/deployment_skill_guide.md`).
- Route: one author without a plan, class `same` as the orchestrator (reason: the value of the guide is
  separating the general from what is loop2's, and leaking a real address into a public repository is the
  failure to avoid).

What you read (foundation, by identifier):
- Decisions: WAY-139 (the one the change edits in place, WAY-07), WAY-140, WAY-165, WAY-270 (the task's
  *Decisions in play*), WAY-09, WAY-07, WAY-33 (search the whole foundation once, after the entry is
  settled, for entries the change touches), WAY-267 (named by WAY-139).
- Part map: the entry `project-level` of `foundations/part_map.md`.
- Invariants whose *Part* is `project-level` or `every` (`foundations/invariants.md`): read those the
  change could touch; at least those whose *Part* is `project-level`.
- The step that points to the guide: `project-level/task/skill/resolve_gaps.md`, the paragraph beginning
  "When the task's outcome deploys the product or changes how or where it runs", and the list of the
  three items handled apart below it. Read the whole file.
- Product guidelines: the-way has none for its own code (WAY-328); nothing to read.

The source of the fragments: the public loop2 repository, skill `.claude/skills/loop2-deploy/SKILL.md`
and its `references/` (three files). A checkout is at `the local checkout of loop2`. Take every fragment from one
commit: `e54f23c0ea3bd1db13d2635333417eb50412d6a0` (tip of `origin/main` when this cycle started; read the
files with `git -C the local checkout of loop2 show e54f23c0ea3bd1db13d2635333417eb50412d6a0:<path>`, not from the
working tree). The guide links the skill in that commit on GitHub with the full SHA
(`https://github.com/mariusznazar/loop2/blob/<full SHA>/.claude/skills/loop2-deploy/SKILL.md`).
Reading outside the repository is yours; do not change loop2.

Binding points you must keep (all from the task; read it for the full words):
- One new file in `project-level/task/`, a part for each of the seven items of the WAY-139 list and one for
  what the skill is for and when an agent reaches for it (the description by which a session finds it).
- Each part: the questions the product answers, and a short fragment showing how loop2 answered, with what
  is loop2's own (Mikrus server, Cloudflare settings, concrete commands, paths, deployment parameters)
  marked in the fragment as belonging to that product.
- Do not copy the whole skill. Do not put into the public repository the real public address of the game or
  the sender's mailbox address in the author's domain; use an example in `example.com`.
- The guide says outright that it binds nothing: the list in WAY-139 and the check in `resolve_gaps.md`
  stay binding; the product writes and keeps the real skill; the guide is no ready-made skill for any kind
  of server.
- The guide must not contradict WAY-140 in its part on what the agent does and what the human does, and
  must show the refusal and "no notice" answers of the items on the logs, the record's life and a failure
  (task *Context*, 4th bullet; `resolve_gaps.md`) as complete answers.
- `resolve_gaps.md`: the paragraph says that the *To do* item it adds, and the task split off for that work,
  point to the guide; the agent reads the guide only when it writes or completes a deployment skill; the
  refinement of other tasks does not read it. Keep that paragraph's other rules as they are.
- WAY-139: edit in place (WAY-07). Its binding sentence says the-way holds, beside the list, a guide to
  writing a product's deployment skill with loop2 as the first example, that binds nothing and that the
  check of the list points to. The list stays in the binding sentence. *Rejected* gains the variants not
  chosen under questions 1 and 2 (task *Questions to settle*, "Not chosen"). Check *Verification*,
  *Rationale* and *Relations* still agree with the edit, and the entry's text "holds no skill of a product"
  is reworded consistently.
- Language: the-way's files are English; the guide is English.
- Do not mention the author's private notes, absolute paths on a disk, or private names in any file you
  commit (the check of private paths is run on the record, but keep the repository clean as well).

Checks you run (with command and exit code in the report): `python -B elements/common/foundation_check.py`;
`python -B -m unittest discover -s project-level -p "test_*.py"`; anything else the method asks; a search of
the committed text for the real game address and the author's mailbox domain (take the strings from the
loop2 files; name in the report only that you searched and found none, do not repeat the strings).

Report: write it to `.runs/task-cycles/deployment-skill-guide/reports/author-report.md` in the form the
method gives, including **Unread material** and **Searches not found or unclear**, your own-work check, and
the foundation step's marks (for the WAY-139 entry: one sentence of its meaning in English and one in Polish,
marked `row 1` and `row 2`). Commit your work on the branch; do not push. Return: status, commits, one-line
check result, report path.
