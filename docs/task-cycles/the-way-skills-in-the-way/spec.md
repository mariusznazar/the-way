# Spec — the-way's skills in sessions on the-way itself

Task: `frozen_task.md` beside this file (Polish; `Project relation: independent`). Base:
`foundations` at c64a6071384fb57cdb9d7e9db4560ddc43e3b355, task branch
`task/the-way-skills-in-the-way`. Classification: architectural (a new mechanism that joins the
skills of five parts to two agent tools, a changed interface every skill states — where the-way
lies — and a new critical flow). This spec is the design agent's, revised under the orchestrator's
rulings R1–R11 (`reports/dispatch_03_spec_revision.md`) on the review in
`reports/report_02_spec_review.md`. The orchestrator holds the delegated choices; nothing here is
Mariusz's approval.

## 1. Understanding

**Outcome.** A Claude Code or Codex session started in a checkout or worktree of the-way sees all
eleven skills of the-way as project skills named `the-way-<name>`, each reading its `SKILL.md` and
every file it names from that same checkout or worktree; a skill handed to by name is again the
`the-way-` project skill. The-way stays uninstalled in itself. A skill the session would not see is
reported by the tests that run on every change. `AGENTS.md` names where the-way's tasks are kept,
with the path the task gives. The five global junctions are removed by Mariusz after the merge.

**Said by the task:** points 1–6, the `the-way-` prefix, "without a submodule, pin or foundation
files", the installer's shape (`.claude/skills/the-way-<name>/SKILL.md`,
`.agents/skills/the-way-<name>/SKILL.md`) as the model, AIR-393 absorbed.

**Assumed by this spec (each in §9 with price):** a new decision and invariant carry the choice;
the check is a critical-flow test; the entry points are generated. Two parts of the task need
approved decisions to change meaning (WAY-09, WAY-27, §5): the branch carries the proposed wording
and the request is a blocked draft holding both questions for Mariusz.

**Success criteria.**
1. `git ls-files .claude/skills .agents/skills` lists one pair per `SKILL.md` of the-way (22
   files at the base commit), the two of a pair byte-identical.
2. No `SKILL.md` of the-way tells an agent to resolve a global link; the nine that say where the-way
   lies name both cases — the-way itself (the checkout or worktree the session was started in) and a
   product (the pinned `.the-way`); `critique` and `implement-task`, which hold no such paragraph,
   rely on their entry points.
3. `python -B gate/run_tests.py gate` fails when a `SKILL.md` lacks either entry point, has a
   stale one, or an entry point names a skill that does not exist (shown by a control test of the
   check).
4. `AGENTS.md` holds `## Skills` and `## Backlog`, the latter with the vault path of
   `_tasks_active.md` and the `_zadania/` folder.
5. Every tracked file belongs to exactly one part; nothing lands in `docs/`, no `.gitmodules`,
   no `.the-way`, no product foundation files.
6. The request carries the exact commands of point 6 for Mariusz, not executed, and the two
   questions on WAY-09 and WAY-27 as a blocked draft.

## 2. Verified environment (read 2026-10-08)

- Claude Code docs, https://code.claude.com/docs/en/skills (installed 2.1.293). Checked verbatim
  by the orchestrator: project skills load from `.claude/skills/` "in the directory where you start
  it and in every parent directory up to the repository root"; "In a session running in a linked
  git worktree, Claude Code searches parent directories only up to the worktree root"; "On Claude
  Code v2.1.277 or later, when the worktree checkout has no .claude/skills directory at its root,
  Claude Code loads the main checkout's project skills instead."; a nested `.claude/skills/` loads
  "the first time Claude reads or edits a file in that subdirectory"; on a name clash "both stay
  available", and Claude is told to invoke "the one whose directory holds the files it's working
  on"; "Enterprise over personal, and personal over project." The page documents
  `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PROJECT_DIR}` as substitutions in a skill's text but does
  not state that the agent is told the path of the skill file it loads, nor the start directory;
  and "Claude Code runs each command in the session shell's current working directory. That
  directory moves when Claude runs `cd`."
- Codex docs, https://developers.openai.com/codex/skills (redirects to
  https://learn.chatgpt.com/docs/build-skills; archived
  http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills):
  "Codex scans `.agents/skills` in every directory from your current working directory up to the
  repository root."; "If two skills share the same `name`, Codex doesn't merge them; both can
  appear in skill selectors."; "In Codex, the initial list also includes each skill's file path."
  (the last read through a summarising fetch; the foundation step reads it verbatim).
- git: `--show-superproject-working-tree` "Outputs nothing if the current repository is not used
  as a submodule by any project" — so it must run in the directory of the entry point, not the
  shell's.
- `C:\Users\Mariusz\.agents\skills` links to `C:\Users\Mariusz\.claude\skills`; there the five
  element skills are junctions to `C:\Storage\repos\the-way\elements\<element>\skill`, and
  `refine-task`, `critique` link to vox-ai-tools. `maintain-instruction-files` links to the sibling
  worktree `the-way-instruction-files` (branch `task/instruction-files`, adds
  `instruction-files/skill/SKILL.md`).
- No tracked file of the-way holds a path into the vault; one local path exists,
  `foundations/decisions.md:3565` (the Superpowers plugin cache).

Consequences: tracked entry points at the worktree root give each worktree its own skills (points
1, 2); the prefix avoids the personal-over-project rule for `refine-task` and `critique`; and,
because the-way's tracked `.claude/skills/` will also lie inside every product's `.the-way`,
Claude Code in a product loads them once the agent reads files there — which every product skill
does — so the entry points must stop themselves in a product (§4.2).

## 3. Approaches

**A — tracked entry points generated by a script of `agent-instructions` (chosen).**
`agent-instructions/skill_entry_points.py` reads every tracked `SKILL.md` outside `.claude/` and
`.agents/` and writes its pair of entry points; they are committed. A critical-flow test in
`gate/` checks them on every change, independently of the generator.
*Cost:* 22 tracked derived files; every skill added, renamed or re-described regenerates them;
WAY-09 has to name their directories (§5.1).
*Gain:* every checkout, worktree and cloud session has them without a setup step; no list of skills
is kept by hand; WAY-44 puts generated files in their generator's part, `agent-instructions`.

**B — the installer gains a mode without a pin and writes the same entry points into the-way.**
Rejected: the generated files would belong to `installation` (WAY-44: generated files go to the
part of their generator), whose directory is `installation/`, so 22 files outside it would break
`repository-file-location`; the installer refuses `target == SOURCE` by design, and its trust
boundary (`installation/install.py`, WAY-48) would grow; its wrapper text is about a submodule and a
pin, none of which exist here. *Price if wrong:* low — the entry-point text is one function.

**C — entry points written per checkout, untracked (ignored), by a command each worktree runs.**
Rejected: a fresh worktree or cloud session has no skills until someone runs it — the failure the
task removes; the check of point 4 cannot run against files a checkout does not hold.

**D — keep global links, one per worktree, or symlinked directories in git.** Rejected: global
links read one checkout whatever branch it holds (the defect of point 2); git symlinks need
`core.symlinks` and extra rights on Windows.

## 4. Design

### 4.1 Discovery and the generator — `agent-instructions/skill_entry_points.py`

- A skill of the-way is a `SKILL.md` that `git ls-files -z --cached --others --exclude-standard
  -- ':(glob)**/SKILL.md'` lists, run at the repository root, whose path does not start with
  `.claude/` or `.agents/` and that exists on disk. (Untracked, non-ignored files count so that a
  skill not yet staged is already reported.)
- From its frontmatter (between the first two `---` lines) it takes `name:` and `description:`,
  each one line. It stops with an error naming the file when either is missing, when the name does
  not match `^[a-z0-9]+(-[a-z0-9]+)*$`, starts with `the-way-`, or is held by two files.
- For each skill it produces the text of §4.2 for both
  `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`.
- `python -B agent-instructions/skill_entry_points.py --write` writes every produced file (UTF-8,
  LF, creating directories) and prints each directory `.claude/skills/the-way-*` or
  `.agents/skills/the-way-*` that no skill produces, for the author to remove with `git rm`; it
  deletes nothing. Without `--write` it prints the plan (paths it would create or change, orphan
  directories) and writes nothing. Exit 0, or 1 with `Error: <message>` on stderr.
- Standard library only, Python 3.14, only `git` as a subprocess (invariants `script-language`,
  `script-imports`, `script-subprocesses`).

### 4.2 The entry point text

Tool-neutral, so the two copies stay byte-identical. For a skill at `<path>` named `<name>` with
description `<description>`, and `<siblings>` the backticked names of all skills, itself included,
sorted by the path of their `SKILL.md`, joined `, ` with ` or ` before the last:

```markdown
---
name: the-way-<name>
description: <description> Use this checkout's own the-way.
---

# the-way-<name>

This entry point serves a session that works on the-way itself. Stop following it, and use the
product's own project skill `the-way-<name>`, if either check shows a product:

- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` prints a
  path: this file lies in a product's `.the-way` submodule;
- `git ls-files --stage -- ':/.the-way'`, run in the directory the session was started in, prints
  a line: the session works in a product that pins the-way.

The process root is the checkout or worktree the session was started in: the directory
`git rev-parse --show-toplevel` prints when run in the session's start directory, not in the
shell's current directory, which moves. Read `<path>` there in full and follow it, and read the
files it names under the same root, never a copy in another checkout or worktree. If the skill
tells you to resolve a link to find the-way, skip that: the root is the one above. Do not
substitute a global skill.

Where this skill or a file it reads names another the-way skill — <siblings> — use this
repository's project skill of the same name with the `the-way-` prefix, never an unprefixed one.
```

Why two checks: the first needs the agent to know where the entry point lies — Codex documents
that its skill list includes "each skill's file path"; Claude Code's page does not state that the
agent is told the skill file's path (it offers `${CLAUDE_SKILL_DIR}` only as a substitution, which
would break the copies' identity and reach Codex as literal text). The second needs no such
knowledge: a product that installed the-way records the gitlink `.the-way` in its own index, and
the `:/` prefix makes git look at the repository's top even from a subdirectory. The
gap left — an agent that knows neither path nor start directory — stands in the failure mode
(§7), not as an invented fact.

Why the start directory: under the worktree fallback, the entry point lies in the main checkout
while the session runs in an older worktree; a root taken from the entry point's directory would
read the main checkout, the defect point 2 removes. The skip line covers an older branch whose
`SKILL.md` still says "Installed globally … resolve it first", which resolves to nothing once
point 6 removes the junctions.

The description keeps the source's text first so both tools select it for the same work; the
suffix tells it apart from a product's wrapper ("Use this product's pinned the-way commit.").

### 4.3 Where the-way lies, in each skill (points 2, 3)

Replace the "Installed globally …" paragraph — no case of it remains once the entry points exist,
and a global link is the defect of point 2; in a product a global skill already violates WAY-34.
"The session's start directory" is used as in §4.2.

- Five element skills (`elements/{decisions,environment-facts,glossary,invariants,part-map}/skill/SKILL.md`,
  lines 13–17): "This skill lives in `elements/<element>/skill/` of the-way. In the-way itself,
  the-way is the checkout or worktree the session was started in, the directory
  `git rev-parse --show-toplevel` prints in the session's start directory; in a product, it is the
  product's pinned `.the-way`. The element's directory is `elements/<element>/` there, and each
  the-way skill named below is the project skill of that name with the `the-way-` prefix. Follow
  the steps of `elements/common/way_of_working.md` there; below is what <a decision | an
  environment fact | a glossary entry | an invariant | the part map> adds to each."
- `elements/common/skill/SKILL.md` 16–20: "This skill lives in `elements/common/skill/` of
  the-way. In the-way itself, the-way is the checkout or worktree the session was started in, the
  directory `git rev-parse --show-toplevel` prints in the session's start directory; in a product,
  it is the product's pinned `.the-way`. `elements/common/` is there, and each skill named below
  is the project skill of that name with the `the-way-` prefix."
- `project-level/skill/SKILL.md` 16–20 and `project-level/technology/SKILL.md` 18–22: the same
  text with their own directory (`project-level/skill/`, `project-level/technology/`) and "The
  project level's directory, `project-level/`, is there" in place of the `elements/common/`
  sentence.
- `project-level/task/skill/SKILL.md` 12–14: "This skill lives in `project-level/task/skill/` of
  the-way. In the-way itself, read it in the checkout or worktree the session was started in; in a
  product, at the pinned `.the-way` commit. Another the-way skill named here is the project skill
  with the `the-way-` prefix."
- `elements/common/critique/SKILL.md` and `task-cycle/skill/SKILL.md` hold no such paragraph and
  stay as they are; their entry points carry both rules.
- `elements/common/way_of_working.md` lines 9–10, successor of the AIR-393 draft: "Paths under
  `elements/` below are those of the-way at the commit the product pins (WAY-34); in the-way
  itself, those of the checkout or worktree the session was started in." The draft's second
  sentence (a skill handed to by name read from the same worktree) is carried by the prefix rule of
  every entry point and of the paragraphs above, so it is not added.

### 4.4 The check (point 4) — critical flow `skills-reach-the-way-sessions`

`gate/test_skills_reach_the_way_sessions.py`, with `# flow: skills-reach-the-way-sessions` at the
top, so `python -B gate/run_tests.py gate`, which every change runs, runs it (WAY-45). It does not
import the generator; it discovers skills with its own `git ls-files` call (same rule as §4.1) and
checks properties, so a generator that drops a skill cannot make it pass. Its expected side — the
skills and their names, descriptions and paths — is read from the `SKILL.md` files, not computed by
the generator (WAY-69).

- `problems(root)` returns one line per problem: a skill without `.claude/skills/the-way-<name>/SKILL.md`
  or without `.agents/…`; the two differing in bytes; frontmatter name other than
  `the-way-<name>`; description not starting with the source's description; text not naming
  `` `<path>` ``, `--show-superproject-working-tree`, `git ls-files --stage -- ':/.the-way'`,
  `git rev-parse --show-toplevel` and the skip line; a sibling name missing from the prefix
  sentence; a directory `the-way-*` under either skills directory that no skill matches.
- `test_every_skill_reaches_a_session_on_the_way` — cites `# invariant: skill-entry-points/1`
  inside the method; asserts `problems(ROOT) == []` and, as positive control, that discovery found
  `elements/decisions/skill/SKILL.md` and `task-cycle/skill/SKILL.md`. Its failure message names
  `python -B agent-instructions/skill_entry_points.py --write`.
- `test_problems_reports_a_skill_the_session_does_not_see` — a control test of `problems()` on a
  temporary `git init` repository (no commit needed: untracked files count): a skill with no entry
  points, with only the `.claude` one, with differing bytes, with an orphan directory; each
  reported. It cites nothing. The deliberate break the check is accepted on is written by the
  reviewer of the code, who did not write the check (WAY-69), in the cycle's review stage.

`agent-instructions/test_skill_entry_points.py` (the generator's own tests, WAY-44: tests belong
to the part they test): the produced text for the real repository equals the tracked files
(derived equality, WAY-53); each frontmatter error of §4.1 stops with its message and writes
nothing; `--write` in a temporary repository writes exactly the two expected paths per skill with
the expected bytes and lists an orphan directory without deleting it. It does not import the gate's
test, nor the gate's test the generator.

### 4.5 Instructions — `AGENTS.md`, `README.md`

`AGENTS.md` keeps its paragraph and gains:

```markdown
## Skills

A session on this repository finds each skill of the-way as the project skill `the-way-<name>`,
in `.claude/skills/` for Claude Code and `.agents/skills/` for Codex, and each reads its skill and
the files it names from the checkout or worktree the session was started in. Use only these: a
personal skill of the same name without the prefix — `refine-task`, `critique` or another — is not
the-way's. A change that adds, renames or moves a skill, or changes its description, runs
`python -B agent-instructions/skill_entry_points.py --write` and commits what it writes; the gate's
tests report a skill a session would not see.

## Backlog

- Tasks: `<private notes>/Notes\Projects\(P) Proces pracy nad produktem\_tasks_active.md`.
  A task's description is a document in the `_zadania\` folder beside it, linked from the task's
  line. Both are in the author's private notes; an agent that cannot open them asks the human.
```

(No `Projects:` line: the task names no project place; `define-project` asks once, as its step 3
says.) The section stands only with the WAY-27 change of §5.2; without it, the alternative of §5.2
applies.

`README.md`: "Using the skills" is rewritten — a session on the-way gets every skill as
`the-way-<name>` from `.claude/skills/` and `.agents/skills/`, reading the checkout it was started
in; a product gets them from the installer; the junction command is removed. The
`agent-instructions/` bullet of "What else is here" names `.claude/skills/` and `.agents/skills/`.

### 4.6 Installer — one sentence

`installation/install.py` `skill_wrapper`: "Its paragraph about resolving a global skill link
applies only to a global install; here the process root is `.the-way`." becomes "Where it says
where the-way lies, the product's case applies: here the process root is `.the-way`." —
otherwise a product's wrapper points to a paragraph that no longer exists.
`installation/test_install.py` asserts the new sentence and that the wrapper no longer holds
"global install" (its "Do not substitute a global skill." stays). No other installer change;
`installation/README.md` already describes the wrappers without the global case.

WAY-48 position: the change replaces a string literal in generated wrapper text; it reads no new
input, parses nothing new and adds no path, argument or subprocess, so it adds no adversarial input
to check. The installer's inputs stay covered by the existing tests of `installation/test_install.py`:
`test_rejects_agents_file_with_other_or_broken_block_before_writing`,
`test_rejects_agents_or_ignore_file_that_is_no_regular_utf8_file`,
`test_rejects_conflicting_integration_file_before_writing`,
`test_rejects_an_ignored_submodule_path_before_writing`,
`test_warns_before_writing_paths_git_ignores`, `test_warns_where_codex_would_miss_the_block`,
`test_preview_apply_rerun_and_preserve_foundation`, `test_declined_apply_writes_nothing`; the
skill's description it copies comes from the-way's own commit, which the installer already reads.

Products take this only by moving their pin; the request carries the line the `pinned` change path
owes: "moving the pin rewrites the eleven wrappers' sentence on the process root; `.the-way` now
carries the-way's own `.claude/skills/` and `.agents/skills/`, which Claude Code may list as
`.the-way:the-way-<name>` and which stop themselves in a product".

### 4.7 Point 6 — the human's step after the merge (for the request description)

After `foundations` with this change is checked out in `C:\Storage\repos\the-way`:

1. Open a new Claude Code session there and check that `/the-way-record-decision` is listed.
2. Open a new Codex session there and check that its skill selector lists
   `the-way-record-decision`.
3. Then, in Windows PowerShell:

```powershell
$names = 'record-decision','record-invariant','record-glossary-term','record-environment-fact','update-part-map'
foreach ($n in $names) {
  $p = Join-Path $HOME ".claude\skills\$n"
  if (-not (Test-Path -LiteralPath $p)) { "$n: not present, nothing to remove"; continue }
  $i = Get-Item -LiteralPath $p
  if ($i.LinkType -ne 'Junction') { "$n: not a junction ($($i.LinkType)); left in place"; continue }
  cmd /c rmdir "$p"
}
foreach ($n in $names) { "{0}: {1}" -f $n, (Test-Path -LiteralPath (Join-Path $HOME ".claude\skills\$n")) }
Test-Path 'C:\Storage\repos\the-way\elements\decisions\skill\SKILL.md'
```

`rmdir` without `/s` removes the junction, never its target; `Remove-Item` is avoided because in
Windows PowerShell 5.1 it can descend into a junction's target. Expected: five `False`, then
`True`. `C:\Users\Mariusz\.agents\skills` is a link to the same directory, so Codex loses the same
five. `refine-task` and `critique` (vox-ai-tools) are not the-way's and stay.

## 5. Fit with the foundation

1. **WAY-09 — edited in place (question 1 of the blocked draft).** WAY-09 admits "the root agent
   instruction files, which the map gives to `agent-instructions` (WAY-44)"; `.claude/skills/` and
   `.agents/skills/` are not among them. The branch edits WAY-09 (pre-main, WAY-07) to name them as
   files of the `agent-instructions` part: "…the root agent instruction files and the project skill
   entry points under `.claude/skills/` and `.agents/skills/`, which the map gives to
   `agent-instructions` (WAY-44), …", with a *Verification* "complies" example for the entry
   points. A change of meaning: Mariusz accepts it again. Fingerprint b829b86a is renewed in every
   reference (WAY-31): `repository-file-location`, `element-directory-contents`,
   `relation-model-directory-contents`, `invariant-example-target`, `map-example-target`,
   `glossary-example-target` (`foundations/invariants.md:152-202`). `repository-file-location`'s
   sentence already admits files of the `agent-instructions` part and keeps its wording.
2. **WAY-27 / `outbound-link-reach` — point 5 (question 2 of the blocked draft).** WAY-27:
   "Nothing in this repository points to a source outside it that its readers cannot reach"; the
   invariant: "No file git tracks contains a link into a private note collection". The vault path in
   `## Backlog` is such a link. Under WAY-30 the branch delivers the task as written and carries the
   proposed change of the decision it contradicts:
   - WAY-27's binding sentence gains an exception: "Nothing in this repository points to a source
     outside it that its readers cannot reach, except the place of its tasks that the `## Backlog`
     section of its root `AGENTS.md` names: every entry carries its whole reasoning, …", with a
     rationale clause (a backlog place is where work is kept, not reasoning an entry rests on, and
     WAY-107 sends an agent there) and a *Verification* "complies" example;
   - `outbound-link-reach` becomes "No file git tracks contains a link into a private note
     collection, other than in the `## Backlog` section of the root `AGENTS.md`, or into a
     repository that a reader not signed in to its host cannot open.", edited in place;
   - WAY-27@770078ba is renewed in its one reference, `outbound-link-reach`
     (`foundations/invariants.md:473`).
   *Why the exception, not `narrows` from WAY-107 (WAY-25 form):* WAY-27 binds this repository
   alone, so the collision exists only here; a `narrows` relation would change WAY-107 — a decision
   for every product, scoped to `project-level` and `installation` — to state an area about
   the-way's own repository, and `outbound-link-reach`, derived from WAY-27 alone, would still need
   its sentence changed. The exception changes one clause of WAY-27 and one of the invariant; the
   smaller change of meaning.
   *Alternative for Mariusz:* no path in the section (or no section) — WAY-27 unchanged, point 5
   not met. The request names both and the orchestrator's recommendation.
3. **WAY-44.** Every new file belongs to one part: entry points and the generator with its test to
   `agent-instructions`; the flow test to `gate` (WAY-55); the watches to `environment-facts`.
4. **WAY-22 / WAY-90.** The choice (A over B–D, global mode dropped, prefix kept) binds every later
   skill, so it is a decision with a derived invariant; it rests on how two tools find skills and
   what Codex tells the agent, so its *Based on* names fact entries (§7).
5. **WAY-34.** Untouched for products; the entry point's two checks keep a product session from
   following the-way's own entry points from `.the-way`.
6. **WAY-101 / WAY-107.** The `## Backlog` section is the-way's own choice as a product; it stands
   in root `AGENTS.md`; the-way has no installer block, so "outside the block" holds trivially.
7. **WAY-45 / WAY-46.** The new flow is high; every part on it is already high (no part's
   criticality changes).
8. **WAY-62 / WAY-69.** The invariant names `every` (a change to any part can add a skill); the
   deliberate break stays with the code reviewer.
9. **Sibling work.** `task/instruction-files` adds a twelfth skill; whichever merges second runs
   `--write` and commits two more entry points. Decision number WAY-127 is provisional against
   other open branches; step 12 renumbers if taken.
10. **Out of scope.** `task-cycle/skill/SKILL.md` still assumes a product with a gitlink; the
   permanent mode of the cycle for the-way is the follow-up task named in the run brief. The
   installer's own list of skills is not checked against the repository.

## 6. Error handling

- Generator: a malformed or duplicate skill stops before writing anything; `--write` never deletes.
- An entry point read from a product's `.the-way`: the first check fires where the agent knows the
  entry point's path; the second fires in any product that pins the-way, without that knowledge.
  It names the product's own skill.
- An old worktree without `.claude/skills` (branched before the merge): Claude Code ≥ 2.1.277
  offers the main checkout's entry points. Both checks stay silent (the main checkout is no
  submodule; an old worktree of the-way records no `.the-way`). The root comes from the session's
  start directory — the old worktree — so its own `SKILL.md` is read; where that `SKILL.md` still
  says "Installed globally … resolve it first", the skip line sets it aside. Codex sees no entry
  points there until the worktree merges `foundations`.
- The shell moved by `cd`: the root is taken in the start directory, not the current one.

## 7. Foundation entries the task writes or changes (the foundation step writes them)

Marked **[meaning change]** where an approved decision's meaning changes — these are the request's
questions for Mariusz.

- **WAY-09/1, edited [meaning change — question 1]** — the process repository may also hold the
  project skill entry points under `.claude/skills/` and `.agents/skills/`, as files the map gives to
  `agent-instructions`.
- **WAY-27/1, edited [meaning change — question 2]** — nothing in the repository points to a source
  its readers cannot reach, except the place of its tasks that the `## Backlog` section of the root
  `AGENTS.md` names.
- **`outbound-link-reach/1`, edited (follows question 2)** — no tracked file links into a private
  note collection, except in that `## Backlog` section; Derives from renewed to WAY-27's new
  fingerprint.
- **`repository-file-location/1`, `element-directory-contents/1`,
  `relation-model-directory-contents/1`, `invariant-example-target/1`, `map-example-target/1`,
  `glossary-example-target/1`, fingerprint renewed (follows question 1)** — wording unchanged;
  `Derives from` carries WAY-09's new fingerprint.
- **WAY-127/1, new decision** — a session working on the-way itself reaches the-way's skills through
  tracked project skill entry points `.claude/skills/the-way-<name>/SKILL.md` and an identical
  `.agents/skills/the-way-<name>/SKILL.md`, generated by `agent-instructions`, which read the skill
  from the checkout or worktree the session was started in, stop themselves in a product and hand
  to other skills under the prefix; no global link and no installation of the-way in itself. Scope:
  agent-instructions, elements-common, project-level, task-cycle, decisions, invariants, glossary,
  part-map, environment-facts, installation. Based on: the four facts below. Relations: derives
  from WAY-44. Verification: level 1 — `skill-entry-points`; level 2 for the skills' paragraphs on
  where the-way lies. Rejected: B, C, D of §3, unprefixed names. New, so approved at the merge.
- **`skill-entry-points/1`, new invariant** — every `SKILL.md` git tracks outside `.claude/` and
  `.agents/` has both entry points, byte-identical, named `the-way-<name>`, starting with its
  description and naming its path, and every `the-way-*` entry-point directory matches such a
  skill. Method `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`; Rests on: none
  (WAY-73: the facts are reasons, not conditions of the sentence); Derives from:
  WAY-127@<fingerprint>; Part: every; Correction: none.
- **Part map, `agent-instructions`, changed** — responsibility adds the project skill entry points
  that make the-way's skills visible to sessions on it; Files add `.claude/skills/**` and
  `.agents/skills/**`; Depends on adds `project-level · task-cycle`; failure modes add "a skill of
  the-way has no entry point, or a stale one — a session on the-way uses a personal skill of that
  name or none — high — detected by skill-entry-points" and "the-way's own entry point, loaded from
  a product's `.the-way`, is followed instead of the product's, where the agent knows neither the
  entry point's path nor the session's start directory (Claude Code's documentation states neither
  is given to the agent) — a product entry is written against the-way's own foundation — high —
  not detected".
- **Part map, critical flow `skills-reach-the-way-sessions`, new** — someone adds, renames or moves
  a skill of the-way, or changes its description, and a session on the-way that would not find it
  under its `the-way-` name is reported before the change reaches the main branch. Criticality high;
  Parts: agent-instructions · elements-common · decisions · invariants · glossary · part-map ·
  environment-facts · project-level · task-cycle · gate; Invariant: skill-entry-points; Coverage:
  none.
- **Four new environment facts** (WAY-76: one fact per entry), each shaped after
  `claude-code-path-rules`: *Holds for* the tool "whose documentation <site> publishes for its
  current release without versions"; *Source* the page with "(archived: <copy>, <date>)" where a
  copy exists — the Codex page has
  http://web.archive.org/web/20261002133901/https://learn.chatgpt.com/docs/build-skills; for
  https://code.claude.com/docs/en/skills no archived copy could be checked (Wayback answered 429),
  so the foundation step tries again and, if none is found, the entry says so; *Method*
  `python -B gate/run_tests.py probes/<id> --record .runs/fact-<id>.jsonl`; the check is a watch:
  `probes/<id>/test_<id>.py` calling `watch_passages` with `# fact: <id>/1` inside the method.
  - `claude-code-project-skills/1` — Claude Code loads project skills from `.claude/skills/` in the
    start directory and each parent up to the repository root, up to the worktree root in a linked
    worktree, and from v2.1.277 the main checkout's when the worktree has none at its root.
  - `claude-code-nested-skills/1` — Claude Code loads a nested `.claude/skills/` the first time it
    reads or edits a file below it, keeps both skills when the names clash, and is told to invoke
    the one whose directory holds the files it works on (the reason for the checks and the failure
    mode).
  - `codex-repository-skills/1` — Codex scans `.agents/skills` in every directory from its working
    directory up to the repository root.
  - `codex-skill-paths/1` — Codex's initial list of skills includes each skill's file path (what the
    first check relies on in Codex).
- **No change:** WAY-34, WAY-44, WAY-107, the glossary.

## 8. Testing and checks

- `python -B gate/run_tests.py gate` (flow test with its control test), `… agent-instructions`,
  `… installation`, and each of the four watches `… probes/<id>` (network; a page that cannot be
  reached is a result, not a pass).
- Format guards with `--base none` (and `--merge-onto none` where available) on `decisions.md`,
  `invariants.md`, `part_map.md`, `environment_facts.md`; the glossary guard too, since it counts
  *Avoid* words in the-way's files and 22 new files arrive. The decision guard must report no
  stale fingerprint of WAY-09 or WAY-27.
- The part-map guard must show every tracked file claimed once and both new patterns reaching files.
- Reported as partial checks, never as the full gate.

## 9. Questions and provisional answers (summary; full table in the design report)

Carried question (installer or a separate mechanism) — a separate generator in
`agent-instructions` (§3). For Mariusz, in the blocked draft: WAY-09 edit (§5.1) and WAY-27
exception (§5.2). Provisional, under the orchestrator: a new decision and four facts (§5.4, §7),
the check as a critical flow (§4.4), the global mode dropped (§4.3), the two product checks (§4.2),
the installer sentence (§4.6).

## 10. Orchestrator amendment R12 (after the Task 3 review, report 13, Important 1)

Claude Code moves a session with `/cd` (v2.1.246 or later) and then adds the new directory's project skills. "The
directory the session was started in" is then the wrong root. Every place below takes "the session's working directory —
the directory the session was started in, or the one it was last moved to (Claude Code's `/cd`)" instead of "the session's
start directory", and both product checks run there.

- §4.2, the root paragraph becomes: "The process root is the checkout or worktree the session works in: the directory
  `git rev-parse --show-toplevel` prints when run in the session's working directory — the directory the session was
  started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which moves
  with `cd`. Read `<path>` there in full and follow it, and read the files it names under the same root, never a copy in
  another checkout or worktree. If the skill tells you to resolve a link to find the-way, skip that: the root is the one
  above. Do not substitute a global skill."
- §4.2, the second check becomes: "`git ls-files --stage -- ':/.the-way'`, run in the session's working directory, prints
  a line: the session works in a product that pins the-way."
- §4.3, §4.5 and `way_of_working.md`: "the checkout or worktree the session was started in" → "the checkout or worktree
  the session works in"; "prints in the session's start directory" → "prints in the session's working directory".
- §7: WAY-127's sentence says the checkout or worktree the session works in; `claude-code-project-skills` gains the `/cd`
  passage; the `agent-instructions` not-detected failure mode says "the session's working directory".
- The invariant `skill-entry-points/1` is unchanged (its strings are kept); its *Derives from* renews with WAY-127.

## 11. Orchestrator amendment R13 (after the final review, report 16)

- §4.1: the generator also stops, naming the file, when a skill's description is not a safe plain YAML scalar: it starts
  with one of `-` `?` `:` `,` `[` `]` `{` `}` `#` `&` `*` `!` `|` `>` `'` `"` `%` `@` or a backtick, or it contains `: ` or
  ` #`, or it ends with `:`. Such a description, copied with the suffix, would give frontmatter a tool cannot parse.
- §4.2, the root paragraph gains, right after "…never a copy in another checkout or worktree.": "If `<path>` is absent
  there, stop and say so."
- The invariant `skill-entry-points/1` and its gate check are unchanged; the part map records the remaining gap (an
  entry point whose frontmatter a tool cannot parse) as not detected.
