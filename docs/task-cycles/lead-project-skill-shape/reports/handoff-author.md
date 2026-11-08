# Handoff — the one author

Delegation: the person who requested this cycle delegated every intermediate choice to the
orchestrator; nothing below is that person's approval. The human reviews the pull request only.

Worktree (work only here, from its root): `the root of the worktree`
Branch: `task/lead-project-skill-shape`, base `57795e4e700dad1e5979bbc6c8fc4cd5f66c8da4` (target `foundations`).
Do not touch the main checkout or any other worktree. Commit your work on this branch.
Do not run the product's gate (`gate/run_tests.py` without a directory); the orchestrator runs it.
Run focused checks only for what you touch (`python -B gate/run_tests.py <directory>`,
`python -B elements/common/foundation_check.py`).

Method: read `task-cycle/change/SKILL.md` whole, variant **"the whole change as the one author"**.
Read any file it names only when the step that names it comes. The foundation step is
`task-cycle/skill/foundation_step.md` (read whole, and the skill of an element when you write an entry
of it: `elements/decisions/SKILL.md` with its `template.md`). The return step comes later, on your
resumption, with its own handoff.

Frozen task (read whole): `.runs/task-cycles/lead-project-skill-shape/task.md`
(`Status: ready for cycle`, updated 2026-11-08). Its *To do* 1–7, *Acceptance criteria* and
*Questions to settle* 1–11 are the requirements; row 1 of *Settlements to record* is accepted and
settles its entry (meaning is the row's, wording yours, WAY-134).

Answers of step 4:
- Trust boundary: no. Irreversible operation: no.
- Open design choice: none (see the task's questions). Reserved choice: none.
- Route: one author without a plan. Your class: same as the orchestrator's.
- Base note (Q1): the task quotes line ranges and word counts at commit `a3206c1`. `foundations` is now
  at `57795e4`, which reworded two lines in `project-level/lead/skill/SKILL.md` (130–134, "table of
  choices" → "message on the choices", line numbers unchanged) and three lines in
  `project-level/lead/conversation_template.md`. Take "before" counts and quoted ranges at `a3206c1`
  as the task says (`git show a3206c1:<path>`; on Git Bash on Windows set `MSYS_NO_PATHCONV=1`),
  and state in the report every place where `57795e4` differs and every count that changes. The files
  you rebuild stand at `57795e4`; keep the two reworded lines as they now read.

What to produce (the task's *To do*):
1. Edit WAY-256 in place in `foundations/decisions.md` by row 1 of *Settlements to record* (three
   binding sentences at most, WAY-05; the *Rationale* takes the reason from the source of row 1 and
   *Rejected* the ways Mariusz did not choose, both stated in the task's questions 3 and 11), then the
   one search of the whole foundation (WAY-33, `elements/common/way_of_working.md` step 2) and the
   corrections of the places that repeat the old rule — the task names `instruction-files/kind_skill.md`
   lines 9, 13–14 and 20 and the rationales of WAY-125 and WAY-127, and whatever else the search finds.
2. Judge `lead-project` with the skill of `instruction-files` in judging mode (`instruction-files/SKILL.md`,
   `judging.md`, `kind_skill.md`, whichever of its files those name when the step comes), for a file of
   the kind "skill", after the search of session records that `judging.md` puts before the table: Claude
   Code records in the session-records folder of Claude Code for the product `loop2` (the eight uses listed in
   the task's *Context*), and Codex records as `judging.md` gives. Reading outside the repository is
   yours (WAY-140). The table is the judgement of WAY-257 and WAY-311: quote each fragment word for word
   with its line range at `a3206c1`, when it is needed, whether an agent recognises that moment, verdict
   (keep / move / remove / reword) and the place after the rebuild.
3. Rebuild the skill by that judgement within `project-level/lead/skill/` only (steps 0–4 stay in
   `SKILL.md`; step 5, the return of a task from a closed request (`:61–77`), the run of
   `settle-technology` (`:113–118`) and the definition change with the gate (from `:202–219`, boundary
   by your judgement) go to files beside it; `SKILL.md` names each file at the step that leads to it with
   the condition for reading it, WAY-265; headings of steps 0–5 and numbers 3.1–3.6 stay). Treat every
   acceptance criterion of the task as a check you carry out and report, including the conditions of
   the pointers (each stated as reaching the step, every road listed in the criterion), the separate
   reading of each moved sentence for pronouns and "below / above / this step", the references from
   the steps that stay to text that left, and the readers outside the skill that the criterion lists.
4. Touch nothing else: `project-level/lead/answering.md`, `project-level/lead/conversation_template.md`
   and other skills stay as they are. The `description` of the skill and Python code stay unchanged.
   If a change to a skill's entry points seems needed, say so in the report instead of running the
   writer.
5. The word counts for the six routes of the task's question 5, before (at `a3206c1`) and after, counted
   as `wc -w` in the C locale, made after the last change of a counted file; a helper script compares
   with the files every number you give in the report, prose included; a number of the task that does
   not agree with the file in the given range is reported as a discrepancy. The table of the
   assessment, the counts, the proposals "remove" / "reword" that change a rule's content, and what each
   outside reader loses (if anything) are the material the request needs: put them in the report in
   the form the request can copy.
6. `python -B elements/common/foundation_check.py` passes from the worktree root.

Scripts: before writing any script, including a one-off `python -c`, read
the author's rules file on writing scripts (line endings, console output encoding,
backslashes in Python literals). Searching the session records: records lie in
`~\.claude\projects\<slug>\<uuid>.jsonl`; a search by skill name alone gives false hits, since the list of
skills stands in every session's system prompt — search for the call, `command-name>/<skill name>`.
Open one element of a counted set to check it is the kind of object you ask about.

Privacy: session records may hold personal data of customers or users and secrets. Quote nothing of
that kind in the report, the table or a commit; keep a session id, a date and a short quote of the
skill's own text only.

Foundation entries to read by identifier (selected by "Reading the foundation"): the task's *Decisions in
play* — WAY-256, WAY-257, WAY-265, WAY-311, WAY-30, WAY-05, WAY-152, WAY-154, WAY-156, WAY-269, WAY-127,
WAY-259 — plus WAY-125, WAY-33, WAY-35, WAY-113, WAY-120, and the decisions whose *Scope* names
`instruction-files` that bear on skills (WAY-27, WAY-34, WAY-89, WAY-100, WAY-102, WAY-128–133, WAY-192,
WAY-212, WAY-245, WAY-254, WAY-258); from `project-level` the decisions that the lead skill carries
(WAY-106–118, WAY-120–124, WAY-126, WAY-150–156, WAY-214–218, WAY-267–270), each whole as the range of lines
from its heading to the next; the part-map entries of `decisions`, `project-level`, `instruction-files`;
glossary entries of the terms you use. The-way has no `guidelines/` of its own. The task's sources are
inside the task document.

Report: write the full report to
`.runs/task-cycles/lead-project-skill-shape/reports/author-report.md` as your method gives it. It must
hold: the assessment table, the counts, the proposals, the readers outside the skill, checks with
command and exit code, your own-work check, for the WAY-256 edit one sentence of its meaning in English
and one in Polish (the task document's language) marked `row 1`, and **Searches not found or unclear**
(`none` is an answer). Return status, commits, a one-line check result and the report path.
