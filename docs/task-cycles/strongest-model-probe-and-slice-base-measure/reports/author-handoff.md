# Handoff — the one author of the change (task cycle of the-way)

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; no
answer of the orchestrator is that person's approval. You have no contact with a human: send your
questions to the orchestrator by returning `questions`.

- Worktree: `the task's worktree` (branch
  `task/strongest-model-probe-and-slice-base-measure`, base `b502011f53225451ddf121e2b772a903b87492db`).
  Work from its root. Never write in another checkout. You are the only agent writing in this worktree.
- This is the-way itself: there is no `.the-way` pin; the process files are the ones in the worktree.
- Method: `task-cycle/change/SKILL.md` (`make-change`). Your variant, in the words of its table:
  **"the whole change as the one author"**. Read that `SKILL.md` whole, and a file it names (one beside
  it included) only when the step or variant that names it comes.
- Stage and boundary: you make the whole change — the foundation entries and the files — commit it
  and return before any review. The foundation step is `task-cycle/skill/foundation_step.md`:
  read it whole before you write an entry, and the `SKILL.md` of an element, at the path it gives,
  when you write an entry of that element (decisions: `elements/decisions/skill/SKILL.md`). You do
  not run the product's gate (`python -B gate/run_tests.py`); that run is the orchestrator's or CI's.
  Run the focused checks the change needs (`python -B elements/common/foundation_check.py`, the
  instruction check `python -B instruction-files/check_instructions.py .`, and the tests of a
  directory you touch with `python -B gate/run_tests.py <directory>`).
- Frozen task, read it whole: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/task.md`
  (under the worktree). No spec and no plan exist. Its *Questions to settle* hold the human's
  answers with their source; *Settlements to record* rows 1–3 go to a sentence of WAY-229 (row 1)
  and a sentence of WAY-136 (rows 2 and 3). Its *Context* lists the places of the rules as they
  stand (line numbers there are approximate, search by the quoted words).
- Answers of the start: trust boundary — no (`task-cycle/cycle_stages.py` already prints the
  model each agent worked on, from the session record; if you find you must change it, or any file
  the part map names as a trust boundary, return that as a reach in your report and do not change it
  without telling); irreversible operation — no; open design choice — none; reserved choice — none;
  route — one author without a plan; your class — `same` (Claude Sonnet 5.5).

## What to read

- Foundation entries, by identifier, each whole with its *Rejected*: WAY-229, WAY-136, WAY-227
  (and WAY-160 and WAY-125 as far as the files you change cite them). Then select the rest as
  "Reading the foundation" in `elements/common/way_of_working.md` gives for an agent writing an
  entry through an element's skill (the part is `task-cycle`; `elements/common/decision_index.py`
  writes the index into `.runs/author/` — your directory below). You are to search the foundation
  once for the entries your change touches and correct them in the same change (WAY-33).
- Guidelines: `guidelines/coding.md` and `guidelines/testing.md`, each whole, only where you write
  code or a test; the change is expected to be prose, and no test holds the present wording of
  these rules (the task's *Context* last line). If a test of the-way turns out to hold it, change
  the test with the rule.
- `agent-instructions/README.md` (the form of the foundation, how a change is made before `main`).

## The change

Make the five points of the task's *To do*, in the files the task's *Context* names and any other
file that restates the same rule (search `availableModels`, `strongest class`, `leaves failing`,
`fails as expected`, `fails as the plan says`, `the plan leaves failing`, `known failing`, and the
words of the rule in `task-cycle/review/SKILL.md`, `task-cycle/change/SKILL.md`,
`task-cycle/skill/planning.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/slice.md`,
`task-cycle/record_template.md` and `task-cycle/skill/SKILL.md`). In short:

1. The probe: in every cycle, before the first dispatch of the strongest class, the orchestrator
   dispatches a small agent on the candidate model and reads from the session record
   (`task-cycle/cycle_stages.py`) the model that agent actually worked on; the first candidate is
   the model named at the start of the cycle, else the strongest the dispatch tool offers; on a
   substitution it tries the next model down; every dispatch of the strongest class in the cycle
   then runs on the model so fixed; the record gives the tries and their results. This replaces
   WAY-229's source for the strongest class (the list `availableModels`, or every model the session
   offers) — change WAY-229's sentence, its *Verification* and *Rationale* / *Rejected* as the rule
   requires, and the three places of `task-cycle/skill/SKILL.md` that the task names. The probe asks
   no human (WAY-227).
2. The record gives, for each agent, the model it actually worked on, read from the session record,
   and where it differs from the model asked for, both. Say it where the record's rows are defined
   (`task-cycle/record_template.md` and the steps of `task-cycle/skill/SKILL.md`).
3. The measure on the base: the executor of a slice decides whether a failing test is its slice's
   fault by running it on the slice's base (only the tests that failed for it); the exact rule is
   point 3 of the task, including its exception for a test of the owner slice's *Checks* and for a
   test the slice's own *Goal* announces it leaves red naming the slice that repairs it; its report
   gives the base result of each such test.
4. The slice's dispatch no longer carries the list of tests the plan leaves failing at its base and
   the orchestrator stops composing it; the same measure replaces the comparison with that list in
   the orchestrator's check of the executor's report and in the rule of the retry on a stronger
   model. The rule that a failing test with no owner slice gets an owner by an edit of the plan
   before the next slice is dispatched stays.
5. The planner, announcing in a slice's *Goal* a test the slice leaves red, writes the same test
   into the *Checks* of the slice that repairs it; a test of the owner's *Checks* that still fails
   after the owner's change is a failed check of the owner, though it failed on its base too.

WAY-136's sentence and its *Verification* change with points 3–5 (the task's *Decisions in play*
says which clauses). Keep to the limits the foundation check enforces on binding sentences and
paragraphs. Widen nothing: the task's *Out of scope* and its *Not chosen* lists bind you — in
particular, no `CLAUDE_CODE_SUBAGENT_MODEL`, no check of the model after a review with a repeat
review, no list "built anew for each slice", and no added conditions for a test to join a list.
A skill whose description or name changes needs `python -B agent-instructions/skill_entry_points.py
--write`; run it only if that is the case. Edit a decision in place (WAY-07); give the decisions
their relations and verification as the element's skill gives.

## Your report

- Report path: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/author-report.md`
  (under the worktree). Write the full report there; its first line is yours. This file is the
  input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); the note that a subagent
  returns findings as text is no reason not to write it. If the harness refuses the write, return
  the report whole as your answer.
- Return: status, your commits, a one-line check result naming what failed or did not run, and the
  report's path. The report holds, as `make-change` gives it: the own-work check (the requirement
  likeliest not met and how you checked it), each check with its command and exit code, concerns,
  reaches beyond this handoff, **Unread material** (what this handoff names that stayed unread or
  was read in part, or `none`) and **Searches not found or unclear** (each thing looked for and not
  found or unclear, or `none`). For the foundation entries, the meaning sentences and the mark the
  foundation step asks for.
- `cycle.md` and the other files in `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/`
  (other agents' handoffs, reports, findings) are not yours to read unless this handoff names them;
  it names only the frozen `task.md` and the report path above.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/author/` (the index of the decisions and any probe go
there). Commit by path (`git add <path> …`), never `git add -A`; commit messages in English.
