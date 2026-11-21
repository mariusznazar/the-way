# Handoff to the one author — hide the entry points of the-way's skills from the model

You are the one author of this change, dispatched by the orchestrator of the task cycle of the-way.
The person who requested the cycle has delegated intermediate choices to the orchestrator; no answer
here is that person's approval.

## Where and what

- Worktree: `the root of the task's worktree`, on the branch
  `task/hide-the-way-skills-from-models`, base `19e5774aed6d1d628042e23deccc110ed9f112c0` (`foundations`).
  Work from the worktree's root. You are the only agent that writes in it.
- Your stage: make the whole change as the one author, with the foundation step, before review. Your
  variant of `make-change`: "the whole change as the one author".
- Method: `task-cycle/change/SKILL.md` of the worktree. Read it whole; read a file it names only
  when the step or variant that names it comes.
- The foundation step: `task-cycle/skill/foundation_step.md` of the worktree, read whole. It writes
  the two rows of *Settlements to record* by the `SKILL.md` of each element (decisions:
  `elements/decisions/skill/SKILL.md`, environment facts: `elements/environment-facts/skill/SKILL.md`,
  invariants: `elements/invariants/skill/SKILL.md`), each read as a file; you have no skill tool.
- The frozen task, which you read whole: `.runs/task-cycles/hide-the-way-skills-from-models/task.md`.
  It is a copy of the task document, `Status: ready for cycle`, `updated: 2026-11-21`. It is written in
  Polish; the foundation and the code are in English.
- No spec and no plan: the cycle found no open design choice. How the entry points and the skills'
  paragraphs phrase "read that skill's `SKILL.md` from the checkout or worktree" is a way of making
  what the task's To do 2 settles; make it and name it among your choices in the report. The path of
  each skill must be reachable from the text the model reads (a name alone gives no path).
- Answers of step 4: the change touches no trust boundary and holds no irreversible operation.
- Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/hide-the-way-skills-from-models/reports/author-report.md`. The
  cycle's script `task-cycle/remarks_check.py` reads this report file, so write it to that path as
  the method gives; if the harness refuses the write, return the report whole as your answer.

## Working copies (word for word)

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
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

## What you do not read, what you do not run

`cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and
findings — are not yours to read unless this handoff names them. You do not run the product's gate
(`python -B gate/run_tests.py` with no argument): its run is the orchestrator's or CI's. You run the
focused checks of the directories you change (`python -B gate/run_tests.py <directory>`), and
`python -B elements/common/foundation_check.py`.

## What you read (named by the orchestrator)

- `agent-instructions/README.md` — how a change to the-way itself is made before `main` exists. Read it
  whole.
- Foundation, each entry whole (a decision's range runs from its heading to the next heading):
  - decision WAY-127 (`foundations/decisions.md`, heading `### WAY-127`), whose sentence, *Rationale*
    and *Verification* the task changes; and the decisions it names under *Relations* and *Based on*
    as far as the change needs them (WAY-125, WAY-34, WAY-44, WAY-256);
  - the invariant `skill-entry-points` (`foundations/invariants.md`), which derives from WAY-127;
  - the environment facts `claude-code-project-skills`, `claude-code-nested-skills`,
    `codex-repository-skills`, `codex-skill-paths` (`foundations/environment_facts.md`), the ones
    WAY-127 is based on; and the entry of the part map for `agent-instructions`.
  Select the rest of the foundation as `elements/common/way_of_working.md` ("Reading the foundation")
  and the skill of each element you write give; the task's *Decisions in play* names only WAY-127.
- Guidelines, each whole: `guidelines/coding.md`, `guidelines/coding-generator.md` (the entry-point
  generator is a generator) and `guidelines/testing.md`.
- The files of the code and the texts the change reaches, each whole before you change it:
  `agent-instructions/skill_entry_points.py`, `agent-instructions/test_skill_entry_points.py`,
  `gate/test_skills_reach_the_way_sessions.py`, `AGENTS.md`, and the paragraphs of the skills that say
  where the-way lies and name another the-way skill (a search of `project skill` and `the-way-` prefix
  over the-way's `SKILL.md` files and over `instruction-files/`, `README.md` finds them; at the
  least `elements/*/skill/SKILL.md`, `elements/common/skill/SKILL.md`, `foundation-review/SKILL.md`,
  `project-level/**/SKILL.md`, `project-level/technology/SKILL.md`). The installer
  (`installation/install.py`) writes the product's entry points on its own and must not change: the
  product's hand-over stays as it is.

## The task, in the orchestrator's reading

1. `agent-instructions/skill_entry_points.py` writes `disable-model-invocation: true` in the header
   of every entry point it generates (both copies, byte-identical, in `.claude/skills/` and
   `.agents/skills/`), and the 46 generated entry points are regenerated and committed
   (`python -B agent-instructions/skill_entry_points.py --write`; then run without `--write` to see it
   current). Mind the generator's own checks of the header and its docstring.
2. In the-way itself, wherever an entry point or a skill of the-way tells a session to use another
   skill of the-way, the session reaches it by reading that skill's `SKILL.md` from the checkout or
   worktree it works in, not by calling a skill. In a product the hand-over stays as it is: through
   the product's own entry point written by the installer; where a skill's paragraph serves both
   places, it distinguishes the two cases (the paragraph on where the-way lies already does).
3. The `## Skills` section of `AGENTS.md` says that a human starts the-way's skills — in Claude Code
   with the command `/the-way-<name>` — and that a skill hands work to another through its file.
   `README.md` (line about `the-way-<name>`) and any other text of the repository that says a session
   or model finds the skills by calling them is corrected the same way where it would be false.
4. The foundation step: row 1 of *Settlements to record* is a sentence of WAY-127 (edit the decision
   in place, with its *Rationale* and *Verification*, and the invariant `skill-entry-points`, which
   derives from it, and whatever test cites them); row 2 is a new environment fact written from the
   quotation of the Claude Code documentation the task's *Context* gives (https://code.claude.com/docs/en/skills,
   § Restrict Claude's skill access, "Hide individual skills", and the table "Control who invokes a
   skill", read 2026-11-21), cited by WAY-127's *Based on*. Take the exact wording from the page: it
   is the source; if you cannot read the page, say so and write what the task's *Context* quotes, with
   its date, and name the gap. Follow the elements' skills for the form.
5. Tests: the stable test of the field in the header of both copies (task's acceptance criterion 1) —
   in the existing tests of the entry points; the checks of the generator's text; and the end-to-end
   test `gate/test_skills_reach_the_way_sessions.py` keeps its property that it computes nothing the
   generator computes. Write a test only as `guidelines/testing.md` gives. For an invariant's test
   the change writes or changes, report its failing run and its passing run.
6. Codex question carried to the cycle: the cycle's answer (autonomous choice) is that both copies carry the
   field and the invariant keeps them byte-identical, because nothing shows that Codex refuses a skill
   with an unknown field (the Codex page and the Agent Skills specification are silent; a probe of
   `codex exec` failed on the model). Do not make the copies differ. Do not claim in a text that Codex
   hides or shows such a skill; write what the sources say.

The task's *Out of scope* — moving loop2's pin and measuring the effect there — is not yours.

## Where you stop and what you return

Make the change with its tests and the foundation entries, commit by path (`git add <file> …`, never
`git add -A` or `git add .`), messages in English in the form the history uses, and return before
review: the report as `task-cycle/change/SKILL.md` gives it, including the own-work check, **Unread
material**, **Searches not found or unclear**, the one-line English and Polish sentence of each
foundation entry with its mark `row <n>`, a one-line check result, and the changed files. Name each
reach beyond this handoff. You do not start the return step; the orchestrator resumes you for it.
Return `questions` or `returned` as the method says where it applies.
