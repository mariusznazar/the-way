# Handoff — the one author (cycle `cycle-subagent-types`)

You make the whole change of one task, as the one author, for the task cycle of the-way. The person
who requested the cycle has delegated intermediate choices to the orchestrator (me); I never label
an answer as that person's approval.

## Where you work

- Worktree (your working directory for everything): the repository's root, the task's worktree, branch `task/cycle-subagent-types`, base commit `715ae20` on `foundations`. Work only there; the process root is this worktree, not another checkout.
- Report: write the whole report to `docs/task-cycles/cycle-subagent-types/reports/author-report.md` (that directory is git-ignored; never commit it).
- Do not run the product's full gate (`python -B gate/run_tests.py` with no directory): the orchestrator runs it. Run the focused checks of the directories you change (`python -B gate/run_tests.py <directory>`), and `python -B elements/common/foundation_check.py`.

## Method

There is no `.the-way` here: this is the-way itself. Read `task-cycle/change/SKILL.md` of this worktree whole and follow it. Your variant, in the words of its row: **"the whole change as the one author"**. Read a file the method names only when the step or variant that names it comes. The foundation step is yours: read `task-cycle/skill/foundation_step.md` whole when you come to write foundation entries, and the skill of an element (`elements/<element>/skill/SKILL.md`, by its path in this worktree; the project skill `the-way-<name>` is the same file's entry point) when you write an entry of that element. After the change, you return before review; the orchestrator resumes you later for a fix and for the return step.

## Task

Frozen task, read it whole: `docs/task-cycles/cycle-subagent-types/task.md` (original approved 2026-11-13; "Settlements to record" candidates 3 shown, 3 accepted 2026-11-13). No spec and no plan: the cycle judged (step 4) that the task leaves no open design choice and that one agent holds the change. The two *Questions carried to cycle* — where the definitions stand as one source for the installer and for the-way's own `.claude/agents/`, whether a script generates the copies and a test checks them, and the names and wording of the two types — are choices of how to make what the task settles; you make each and name it in your report with the way you rejected, so that I enter it in the cycle's questions table. If you meet an open design choice that is not of that kind, return `returned` with a report and no code.

Answers of step 4 that bind your work:

- **Trust boundary: yes.** `installation/install.py` is the part `installation`'s trust boundary (files from outside: what a product already holds in `.claude/agents/`). The reviews of this cycle check crafted input there: a symlinked `.claude` or `.claude/agents`, a file at an owned path that is not the installer's, non-UTF-8 content, a malformed or hostile definition file, a name that would escape the directory. Make the installer's handling of `.claude/agents/` as strict as its handling of skill entry points, and test those cases.
- **Irreversible operation: no.** You never install into a product. Tests run the installer on temporary repositories only.
- Class of your model: `same` as the orchestrator's.

## Foundation to read (by identifier; each entry whole, to the next heading)

Decisions the task names (*Decisions in play*): WAY-255, WAY-125, WAY-148, WAY-127, WAY-34, WAY-229, WAY-347, WAY-05, WAY-27.
Decisions whose *Scope* names the parts you touch and that bear on the change: WAY-38 and WAY-89 (language and version of scripts), WAY-141 and WAY-259 (installer and entry point text), WAY-53 and WAY-225 (derived files compared with their generator), WAY-256 and WAY-265 (fragments and files of skills), WAY-33, WAY-35, WAY-44, WAY-150, WAY-328, WAY-344. Select the others of the parts `agent-instructions`, `installation`, `task-cycle`, `decisions`, `part-map` by "Reading the foundation" in `elements/common/way_of_working.md` (search *Scope*), as far as the work needs them.
Invariants: `skill-entry-points` (`foundations/invariants.md`, `## skill-entry-points`) and any whose *Part* names `agent-instructions` or `installation`; the test files an invariant cites by `invariant: <identifier>`.
Part map: the entries `agent-instructions`, `installation`, `installation-command`, `task-cycle` (the task says the entry `installation-command` lists every file the installer rewrites or deletes, and the new files change it).
Glossary: the terms you use (read the glossary whole; it is short).
The-way has no product guidelines of its own besides WAY-328 (it holds its code to the general coding guidelines as that decision says) — read WAY-328 and the files of `product-guidelines/coding/` it points to for the code you write.

## Files you will most likely touch (read each whole before you change it)

`agent-instructions/skill_entry_points.py` and its test (the pattern for a generator of tracked copies), `installation/install.py`, `installation/README.md` and the installation tests, `task-cycle/skill/SKILL.md` (steps 2 to 9, the paragraph "Write each dispatch's full handoff"), `task-cycle/skill/foundation_step.md`, `task-cycle/skill/return_step.md`, `task-cycle/change/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/record_template.md` if the record must say a stage ran without its type, `agent-instructions/README.md` if the commands of a change to the definitions belong there, the decision log, the part map, and the new tracked `.claude/agents/` of this repository. `AGENTS.md` of this repository tells a change that adds, renames or moves a skill to run `python -B agent-instructions/skill_entry_points.py --write`; do the like for whatever you generate, and make the gate's tests report a definition a session would not see.

## What the task asks, in its own words

Take the six items of *To do*, the one acceptance criterion and the four answers of *Questions to settle* from the frozen task as binding; do not widen them. Points the orchestrator wants you to hold in sight:

- The two types are definitions of Claude Code subagent types (files with frontmatter in `.claude/agents/`), each with its own body of at least two sentences about what the type is, and both give the agent every tool of the session except the skill tool. The acceptance criterion — that an agent of the type starts without the list of skills — is checked by one probe that the orchestrator runs after your change on the Claude Code version in use; make the definitions in the form the task fixes (`omitClaudeMd` not set; `cacheTtl: 1h` in `experimental` for the one author's type only).
- To do 5 is about *how a method is pointed at*: by the path of its file in the pinned the-way, not by a skill name to call. Go through every place the task names and every place of the same kind you find by search in the files of the cycle (`task-cycle/`), and name in your report each place you changed and each you looked at and left, with the reason.
- To do 4: the cycle's instruction text must say, in Claude Code, which type each stage is dispatched with and what the orchestrator does when the session has no such type (another harness; a session started before `.claude/agents/` existed): dispatch as today and write it in the cycle's record. Keep the instruction as short as the text around it.
- To do 6 and the three rows of *Settlements to record*: foundation entries, written through the skills of their elements. WAY-255 gets the exception by editing the entry in place (WAY-07); its *Rejected* line stays with the account by kind of agent. Write results of the task's probes as the decision gives them (WAY-05, WAY-27): what was measured and under which conditions, never a pointer to the private note.
- Tests: the installer's new group of files (preview, own-file rule, replacing and deleting only its own, stale definitions of types the commit no longer has, refusal on a file or directory that is not its own, a symlink, a bad encoding), the generator and the test that compares the tracked copies with what it produces, and the content checks of the definitions (the frontmatter fields, no `Skill` tool, the `cacheTtl` only on the one author's type). Write the invariant's test only if a decision, the task or a rule you must hold calls for an invariant (the foundation step says when); do not write an invariant merely because none covers the behaviour.

## Privacy

Nothing in the repository, the report or a commit message may carry a path of the author's disk outside this repository, a private note's name or title, or personal data. The task note's path appears in this handoff only; do not copy it into any file you commit. Commit messages in English.

## Report

Return, in the report and in your short return: status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your commits, a one-line check result naming what failed or did not run, the report's path, your questions and concerns, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), each reach beyond this handoff (what, where, why), each choice you made and the way you rejected, your own-work check with each check's command and exit code, and where the change touches the part `installation`'s trust boundary, the crafted inputs you tried and what each showed. Commit your work yourself, by explicit paths (`git add <path> …`), never `git add -A`; leave a clean worktree.
