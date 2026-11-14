# Handoff — the one author of the change

You are the one author of a change in a task cycle of the-way, working without a plan. The person
who requested the cycle delegated intermediate choices to the orchestrator; nobody will answer a
design question, so where the task and the foundation leave you a way of making what they settle,
make it and name it in your report.

## Where you work

- Worktree (work only here, from its root): `the worktree's root`, branch `task/installer-junction-refusal`, base commit `6fa755ce9b7f749813bf2b2088bf3ce30ac90185`. Commit on this branch. Do not push. Do not run the product's whole gate (`python -B gate/run_tests.py` with no argument): the orchestrator runs it. You may run `python -B gate/run_tests.py installation` and any other single directory.
- Do not touch `.runs/` except to write your report. Do not edit anything outside the worktree.

## Method

Read whole `task-cycle/change/SKILL.md` (the method `make-change`) in the worktree; your variant is **"the whole change as the one author"**. Read a file it names, one beside it included, only when the step or variant that names it comes.

Your own-work check (WAY-164), the return-step reading and the commit rules are in that method. The foundation step that writes the entry the task carries is `task-cycle/skill/foundation_step.md`; the orchestrator's skill tells you to read it whole. The return step is `task-cycle/skill/return_step.md`; do **not** take the return step now — the orchestrator resumes you for it after the review of the whole change.

## The task

Frozen task, whole: `docs/task-cycles/installer-junction-refusal/task.md` (it is a copy of the task document; its *To do* items, *Acceptance criteria*, *Questions to settle* with their answers and *Settlements to record* row 1 bind you; read it whole).

Answers of the orchestrator's step 4, recorded for you:

- **Trust boundary: yes.** `installation/install.py` is the trust boundary of the part `installation`. Check crafted input at it yourself: a junction in `.claude` (the folder of the agent settings), in `.claude/agents`, in `.claude/skills`, in the folder of a skill entry (stale or current), in `.agents/skills`, in `foundations`, and at `.the-way`. A junction is a directory for which `Path.is_symlink()` is false and `Path.is_dir()` true; in Python 3.14 `os.path.isjunction` / `Path.is_junction` recognise it.
- **Irreversible operation: no.** The change only stops the installer from writing or deleting through a junction.
- **Open design choice: none.** The rule (refuse and recognise a junction wherever the installer recognises a symlink today, the removal of stale entries and `.the-way` included) and the means (the standard library, WAY-38) are settled by the task. Where the same symlink test appears at several places in `installation/install.py` (the task lists them in *Context*), one shared helper is a way of making it, not a choice to ask about.
- **Reserved choice: none.**

## What to read (selected by the orchestrator, WAY-150, WAY-213)

Foundation entries, each whole (decisions from their heading to the next `###`; other entries from their `##` heading to the next):

- Decisions of the task's *Decisions in play* in `foundations/decisions.md`: WAY-48, WAY-13, WAY-38, WAY-328, WAY-235.
- Decisions whose *Scope* names `installation` and that bear on what the installer writes and deletes: WAY-34, WAY-141, WAY-368.
- Invariants of the part `installation` and of `every` that your tests or the installer touch: `installation-claude-guidance`, `script-language`, `script-imports`, `script-subprocesses`, `test-method-citation`, `gate-exit-code`, `python-version-declared`, `cross-part-imports`. Read `script-subprocesses` first: a test of yours has to create a junction, and the standard library has no public call that creates one on Windows; find out from the invariant, and from how the existing tests of `installation/` create what they need, which way is allowed, and name the way you take in your report.
- The part map, whole (`foundations/part_map.md`), in particular the entries `installation`, `installation-command` and the invariants part.
- Glossary terms the work uses (`foundations/glossary.md`, short, whole).
- The element of the invariant you write: `elements/invariants/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/invariants/examples.md` and `elements/invariants/skill/SKILL.md`, each whole, and the foundation step above. A skill that one of these names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name; read it as a file, you have no skill tool.

Code and tests: `installation/install.py` whole, `installation/test_install.py` and `installation/test_agent_types_installation.py` whole (the existing tests that make symlinks, `test_install.py:661` and `test_agent_types_installation.py:263`, show the form the tests of the installer take), `installation/README.md` (sections *Files in the product*, *Existing files and incomplete setup* and *Check the installer*, which may need a sentence about junctions).

Product guidelines: the-way holds its own code and tests to none of the product guidelines (WAY-328); there are none to read.

## What the change must be

1. The refusal, the recognition at removal and at `.the-way`, and the two tests, as *To do* items 1–3 give.
2. The invariant of *Settlements to record* row 1, written whole by the foundation step in `foundations/invariants.md` as the element's skill gives (Method `test`; the tests of *To do* 4 cite it as `test-method-citation` gives). Run `python -B elements/common/foundation_check.py --skip-test-citations` after writing it, and once without the switch after the tests that cite it are committed.
3. *Acceptance criteria*: on Windows the tests of item 3 are not skipped. Run them here (this is Windows) and report that they ran and passed.
4. A test of an invariant is seen failing once (WAY-235's form): write the test, run it against the installer **before** the fix and report its failing run, then the passing run after the fix — record both with their commands and exit codes.
5. Do not change what the installer does for anything that is not a junction; the existing tests of `installation/` keep passing (run the directory).

## Report

Write your full report to `docs/task-cycles/installer-junction-refusal/reports/author-report.md` as `make-change` gives it, with the sections `make-change` and the cycle's skill require: status, commits, checks with command and exit code, the own-work check, the entry's meaning in English and in Polish with the mark `row 1`, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (or `none`), questions and concerns, reaches beyond this handoff.

Return only the status, the commits, a one-line check result and the report's path.
