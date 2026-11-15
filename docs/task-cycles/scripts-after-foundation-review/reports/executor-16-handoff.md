# Handoff — executor of slice 16, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 16 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **cheaper (a model cheaper than the orchestrator's)**.
- Directory for your working copies: `.runs/executor-16/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-16-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 16 — The check of tracked files reads all the Markdown suffixes; the README says what is read; two installation tests install from a clone

- **Goal:** (a) `task-cycle/tracked_private_paths_check.py` looks for note links in files whose name ends in `.md`, `.markdown`, `.mdx` or `.mdc` in any letter case (today `MARKDOWN_SUFFIX = ".md"`), and its description and the description of the command in `installation/README.md` ("… each note link in a Markdown file …") say the same, with the word of the glossary term that the foundation step wrote (row 8); the sentence of WAY-320 and of the invariant `tracked-file-private-paths` stays as it is. The new reading does not make `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` fail on the files git tracks now. (b) `installation/README.md` (the sentence "a tracked file is not UTF-8 text") says that a file that starts with a UTF-16 byte order mark is read, as `private_paths_check.py` reads it, and a file with a NUL byte near its start is not. (c) `installation/test_styleguide_installation.py` and `installation/test_testing_guidelines_installation.py` install from a clone of the checkout made in `setUp`, as the four other tests of the installation of guidelines do (`installation/test_coding_guidelines_installation.py`, `setUp`), so that a commit made in the checkout of the-way during a full run (`self.commit = self.git("rev-parse", "HEAD", cwd=SOURCE)`) fails neither: the commit pinned and the commit expected are those of the clone, the installer under test is the one of the working tree, and the skill the test names must be committed.
- **Change:** `task-cycle/tracked_private_paths_check.py` · `task-cycle/test_tracked_private_paths_check.py` · `installation/README.md` · `installation/test_styleguide_installation.py` · `installation/test_testing_guidelines_installation.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:45-47` To do 18 to 20 · `.runs/task-cycles/scripts-after-foundation-review/task.md:91-95` Questions to settle 8 · `.runs/task-cycles/scripts-after-foundation-review/task.md:130-130` Decisions in play, WAY-320 · `.runs/task-cycles/scripts-after-foundation-review/task.md:150-150` Settlements to record, row 8 · glossary row 8, the term for a Markdown file as the foundation step wrote it · `foundations/decisions.md:7183-7253` WAY-320 · `foundations/decisions.md:7255-7302` WAY-324 · `foundations/invariants.md:86-95` tracked-file-private-paths · `foundations/part_map.md:242-249` tracked-private-paths-command · `task-cycle/private_paths_check.py:110-194` the reading of a file, its byte order mark · `installation/test_coding_guidelines_installation.py:28-60` setUp of the model test
- **Model:** cheaper
- **Risk:** none
- **Checks:** start from the new tests in `task-cycle/test_tracked_private_paths_check.py` (a note link in a `.mdc`, `.mdx`, `.markdown` file listed; one in a `.py` file not), red on the base; `python -B -m unittest discover -s task-cycle -p "test_tracked_private_paths_check.py"` · `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` exits 0 · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `python -B -m unittest discover -s installation -p "test_styleguide_installation.py"` · `python -B -m unittest discover -s installation -p "test_testing_guidelines_installation.py"`
- **Depends on:** the glossary entry of row 8 (the foundation step)


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7231-7302` WAY-320
- `foundations/decisions.md:7303-7351` WAY-324
- `foundations/invariants.md:86-95` tracked-file-private-paths
- `foundations/part_map.md:242-250` tracked-private-paths-command

## Working copies

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
all the same and names in the report the remainder, with its full path and the reason it stayed.
