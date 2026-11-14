FAIL 474df77904b199e3ba1acb438c5a88c9a47d13c1

# Review of the whole change — installer-junction-refusal

Range `6fa755ce9b7f749813bf2b2088bf3ce30ac90185..474df77904b199e3ba1acb438c5a88c9a47d13c1` (`git rev-parse HEAD` in the worktree is `474df77904b199e3ba1acb438c5a88c9a47d13c1`; `git log` shows `54ed53c`, `474df77`). Route: one author, no spec, no plan, no slices, so this review is the only one of the code. Trust boundary: yes (reviewed for crafted input). Irreversible operation: no.

Result in one line: the code does what the task's items 1 to 4 ask, and the three new tests fail when their site reverts; but the invariant's sentence claims more than the installer does (a junction at `.git/modules` is written through, exit 0), and that blocks.

## Blocking findings (Important, within the task)

### 1. The invariant sentence is broader than the code: a junction at `.git/modules` is written through with exit 0

- Place: `foundations/invariants.md:303` (the sentence), with `Violated: no` at `:309`; code `installation/install.py:636` (`git("submodule", "add", ...)`) after `plan`, which checks no path under `.git`.
- Sentence: "The installation command neither writes nor deletes anything through a symbolic link or a Windows junction that stands in a directory path of a product, `.the-way` included, ...". `.git/modules` is a directory path of a product.
- Evidence (my run, `python -B <scratchpad>/crafted.py`, exit 0): a product whose `.git/modules` is a junction to a folder outside the product, `install.py <product> --url <worktree> --apply`: exit code 0, `Installed.` printed, and the outside folder now holds `.the-way/HEAD`, `.the-way/config`, `.the-way/description`, `.the-way/hooks` — git's own directory of the submodule, written through the junction. Case B of the checks below.
- Why it matters: the entry says `Violated: no` and `Method: test`, and agents that later change the installer read it as holding on every directory path of a product; it does not. Section 3 of `review-change` (WAY-263) grades an entry that restates the settled rule more broadly than the files do as Important. The three tests cite the invariant and none of them reaches `.git`, so the test cannot show it false.
- What the task asks and does not: item 1 asks for refusal on "any directory on the path from the product's root to a file the installer writes", which `.git/modules` is not (git writes it). So the code is within the task; the sentence is not true to the code. The fix is one of two, both small: narrow the sentence to what the installer's own code writes and deletes (for example "...neither writes nor deletes, with its own code, anything ..."), leaving git's writes under `.git` outside it; or add a check of `.git` and `.git/modules` to `plan` and a test. The first is the cheaper and matches the task's wording. Row 1 of *Settlements to record* itself says "w ścieżce, którą dotyka"; if the human wants git's writes included, the second applies. Whichever is chosen, the sentence and the code have to agree.
- Slice: no plan; the whole change (commit `474df77`, the entry; the code is `54ed53c`).

## Minor findings

All within the task unless it says otherwise.

### 2. Three directory checks have no test (author's request to grade this)

- Place: `installation/install.py:366` (`is_link(target / ".claude")`, `is_link(agents)` in `stale_agent_definitions`) and `:379` (`is_link(skills)` in `stale_entry_points`).
- `plan` calls `check_parents` for every path of `files` before it calls either function (`install.py:455-456` before `:477`), and `files` always holds a file under `.claude`, `.claude/agents`, `.claude/skills` and `.agents/skills`, so a junction there is refused before the stale scan; I agree with the author that these checks are unreachable through `plan` today. Same as the symlink checks they replaced, which were no better protected. Grade: Minor, acceptable as it stands. I do not accept the reason the author gives for leaving them untested: `installation/test_install.py:719` already calls `install.skill_wrapper` directly, so a call of `install.stale_agent_definitions(product)` and `install.stale_entry_points(product)` on a product with a junction at `.claude/agents` or `.agents/skills` that holds the installer's own file, asserting an empty list, is cheap, and it is the one protection of the deletion half of the invariant against a later reordering of `plan` — the half that cannot be undone. Not required for a pass.

### 3. The invariant's sentence says "directory path", and tests that cite it exercise a link at the file itself

- Place: `foundations/invariants.md:303`; `installation/test_agent_types_installation.py:221` and `:257`.
- Both existing tests the change made cite the invariant. `test_a_symlinked_definition...` (cases "a symlinked definition", "a dangling symlink at a definition", at `:223-231`) and `test_a_symlink_named_like_an_own_definition_of_a_gone_type_is_not_deleted` (`:257`) put the link at the file, not in a directory path. By clause 2 ("on the path of a file it is to write") the first test is covered; by clause 1 ("deletes nothing ... that stands in a directory path") the second is not. Citing them is right in intent (they protect the same behaviour and the tests name the cited invariant, which `foundation_check.py` accepts), but the sentence should say "path" rather than "directory path" when it is reworded under finding 1. Grade Minor; changed invariant tests are named: these two, plus the three new ones in `installation/test_install.py:698, :719, :737`.

### 4. `Rests on: none` for a Windows junction

- Place: `foundations/invariants.md:306`.
- `elements/invariants/skill/draft.md` says to put through the template's test every fact "that neither the product nor the-way ... writes, such as a standard, a library or a law, found behind what the sentence names". "Windows junction" is named in the sentence and the sentence is true or false of a commit by how Python 3.14 reports one (`is_symlink()` false, `is_junction()` true — the task's own probe). `elements/common/rules.md` says `none` is a statement and "where a source is silent, the field reads `TODO`"; the author could find no source and wrote `none`. The sentence also holds without the fact if one reads the code as "uses `Path.is_junction`", so I grade by WAY-364: a form departure where the content agrees with the code, Minor, no sentence a reader would read wrongly. The author's recommendation (accept `none`, or add a small fact from the Python 3.14 documentation of `os.path.isjunction`) is a fair statement of the two choices; I favour adding the fact, since `TODO` is not allowed to stay on the main branch without the human and `none` hides it. The cycle's choice.
- `Derives from: WAY-48 · WAY-235 · WAY-368` — accepted. WAY-368 carries the deletion half ("replacing and deleting only its own files"), WAY-235 the shape (a boundary refusal checked by a permanent test, though WAY-328 exempts the-way from the testing guidelines), WAY-48 only the boundary and the review aimed at it; the link to WAY-48 is the weakest, but harmless, and `foundation_check.py` passes.
- `Part: installation` — right: only a change to `installation/**` can make it false (and, after finding 1, still so).
- One sentence (WAY-56): two clauses joined by "and it refuses ..."; WAY-56's *Rejected* lists "a split wherever a commit can break part of a sentence", and the task's row 1 is itself one sentence of both. Not a finding.

### 5. README names a "folder" of an agent type, which does not exist

- Place: `installation/README.md:183-188`: "a junction at the folder of a skill or agent type the commit lacks is not followed, so nothing is deleted through it".
- A skill entry is a folder (`.claude/skills/the-way-<name>/SKILL.md`); an agent type is a file (`.claude/agents/the-way-<name>.md`). A junction at a file's path is skipped because `is_file()` is false (I checked: case J below, exit 0, outside folder unchanged), not because of the junction check. The sentence reads as if the agent-type junction case went through `is_link`. Reword: "a junction at the folder of a skill the commit lacks, or at the path of an agent type's file, is not followed". Minor.

### 6. Size of the files left (no rule of size in the-way; Minor by WAY-363)

- `python -B task-cycle/change_file_sizes.py 6fa755c 474df77` (exit 0): `installation/install.py` 675 to 681 (+6), `installation/test_install.py` 713 to 807 (+94), `installation/test_agent_types_installation.py` 332 to 334, `installation/README.md` 250 to 257, `foundations/invariants.md` 356 to 366. The-way holds none of the product guidelines (WAY-328), so there is no threshold test to run; my numbers and the diff are the material. Nothing grew past a point I would name: `test_install.py` was already the largest file of its part and the three new tests and three helpers are the growth. `is_link` has five users and no dead code was added besides the three unprotected guards of finding 2. The names are true.

## Out of scope

### 7. Git writes through a junction at `.git` or `.git/modules`, and the installer does not refuse it

- Same evidence as finding 1 (case B). Outside the task: the task's items are about paths of files the installer writes, `.the-way` and stale entries; a junction at `.git/modules` is made by someone who keeps git's data elsewhere. If the human wants the installer to refuse it, it is a new task. Grade: Minor, out of scope (and it becomes in scope only if finding 1 is fixed by adding the check rather than by narrowing the sentence).

## Declined to judge

- A junction in the path above the product's root (the root given as an argument): `run()` takes `args.repo.resolve()`, so the real path is used; I ran it (case I, exit 0, the preview shows the real product); it is the user's choice of root, not a path inside the product.
- Time-of-check to time-of-use races (a junction made between `plan` and the writes): not in the task.
- Hard links and other reparse points than a junction: not in the task.

## Coverage of the task

Items of *To do*:

1. Refuse a junction on the path of a file written, before writing, message and non-zero exit: met. `check_parents` uses `is_link` (`install.py:305-316`); test 1 (`test_install.py:696`) covers `.claude`, `.claude/agents`, `.claude/skills`, `.claude/skills/the-way-make-change`, `.agents`, `.agents/skills`, `foundations`, preview and apply. I also ran a dangling junction at `.claude` (case G): exit 1 `Parent path is not a regular directory`, outside folder untouched. Foundation files, entry points and agent definitions all go through `check_parents`.
2. Recognise a junction wherever a symlink was recognised outside the write path: met. `stale_agent_definitions`, `stale_entry_points`, the `.the-way` check with a pin. The sites that stayed `is_symlink()` (`install.py:206, 324, 340, 439, 460`) test files; a junction is never a file, so `is_file()` already refuses or skips it (case H: `AGENTS.md` junction, exit 1; case J: a junction named like a stale definition, exit 0, untouched). `.the-way` as a junction without a pin: refused by the existing `os.path.lexists` (case A, exit 1, nothing outside).
3. Tests make a junction in a trial product and show nothing written or deleted, in the product or in the target: met. One with `.claude` (and six more paths), one with the folder of a stale entry (under `.claude` and `.agents`), one at `.the-way`; each skips where a junction cannot be made.
4. The tests cite the invariant of row 1: met, `installation/test_install.py:698, :719, :737`.

Acceptance criterion: "On Windows the tests of item 3 are not skipped": met. My run of the three on this Windows machine, `-v`: three `ok`, none skipped.

*Questions to settle*: question 1 (everywhere a symlink was recognised) — met as item 2; question 2 (an invariant with a citing test) — written, but with the defect of finding 1.

Row 1 of *Settlements to record* (invariant, written whole by the author): written in `foundations/invariants.md:301-309` with all five fields, identifier naming what it constrains, Part `installation`; Method `test` and cited by five tests; `foundation_check.py` reports 0 errors. The English meaning and the Polish meaning in the author's report match the row. Open: findings 1, 3, 4. The part map surface `installation-command` left unedited: right. That surface lists what products rely on (preview, confirmation, rewrites and deletes only its own files); a refusal through links narrows what the installer does and is not a promise to products, and the task's row names an invariant only.

Decisions in play: WAY-48 (boundary reviewed for crafted input: done, cases A to J and the tests); WAY-13 (both questions answered at the start; the deletion of stale entries still deletes only its own files, since `owned_entry_point` and `owned_agent_definition` still gate every deletion and the change added no deletion path; no irreversible operation added); WAY-38 (stdlib only: `Path.is_junction` and `_winapi` — `'_winapi' in sys.stdlib_module_names` is `True` on Python 3.14.3); WAY-328 (no product guidelines apply); WAY-235 (the refusal is checked directly, and the author saw the three tests fail before the code: reproduced for two of the sites by my mutations below).

Own-work check of the author: its weakest requirement ("a junction is recognised at every directory-level site") — its check (grep of `is_symlink`, one crafted case per place) would catch a missed site in `install.py`, and I found none missed in the installer's own code; it did not look at paths git writes (finding 1).

`_winapi.CreateJunction` in tests: `script-subprocesses` holds (no program started; `mklink` and PowerShell would have broken it); `script-imports` holds (`_winapi` is in `sys.stdlib_module_names`, so it is a module of the standard library of Python 3.14, per `python-stdlib-modules`); the private name has the precedent at `instruction-files/test_check_instructions.py:92-100`. I accept it. The helper is copied rather than imported, which `cross-part-imports` allows only from a part of test helpers; I did not check whether `instruction-files` is one, so I leave the copy undisputed.

The README sentence: see finding 5; the rest of the added paragraph (`installation/README.md:183-188`, `:250-252`) is true to the code.

## Checks I ran

| Check | Command | Exit | Result |
|---|---|---|---|
| Head | `git rev-parse HEAD` in the worktree | 0 | `474df77904b199e3ba1acb438c5a88c9a47d13c1` |
| Focused tests | `python -B -m unittest installation.test_install -k junction -k stale_entry -v` | 0 | `Ran 3 tests in 77.521s`, `OK`, no skip |
| Mutation of the `.the-way` site (separate worktree of head, `is_link(submodule_path)` back to `is_symlink()`) | `python -B -m unittest installation.test_install -k submodule_directory` | non-zero | `FAILED (failures=2)` (preview and apply) — the test catches its site |
| Mutation of the stale-entry site (same worktree, `not is_link(entry)` back to `not entry.is_symlink()`) | `python -B -m unittest installation.test_install -k stale_entry` | non-zero | `'DELETE' unexpectedly found` — the test catches its site |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| File sizes | `python -B task-cycle/change_file_sizes.py 6fa755c 474df77` | 0 | table above |
| Crafted input, my own script | `python -B <scratchpad>/crafted.py` (junctions made with `_winapi.CreateJunction` in a temporary directory, installer run from the worktree with `--url <worktree> --apply`) | 0 | A `.the-way` junction without pin: exit 1, nothing outside. B `.git/modules` junction: exit 0, `Installed.`, outside folder filled by git (finding 1). G dangling junction at `.claude`: exit 1, refused. H `AGENTS.md` junction: exit 1, `not a regular file`. I root given through a junction: exit 0, real path used. J junction named `.claude/agents/the-way-gone.md`: exit 0, outside folder unchanged |

The scratch worktree was removed after the mutations (`git worktree remove --force`); the reviewed worktree, its index and branch are unchanged. Not run: the whole gate and `gate/run_tests.py installation` (the orchestrator's, about 15 minutes); the three unprotected checks of finding 2, since no flow reaches them.

## Reaches beyond the dispatch

- `elements/invariants/template.md`, `elements/invariants/skill/draft.md`, `elements/common/rules.md`: the template and the rules of form of the entry.
- Decisions WAY-56 (whole), WAY-34 (opening lines) in `foundations/decisions.md`: for the one-sentence rule and the pin.
- `foundations/environment_facts.md` entry `python-stdlib-modules`; `foundations/invariants.md` entries `script-subprocesses`, `script-imports`, `installation-claude-guidance`, `cross-part-imports` (opening sentence); `foundations/part_map.md` parts `installation`, `invariants` and surface `installation-command`.
- `installation/test_agent_types_installation.py:205-270`: the two tests that now cite the invariant.

## Unread material

- Counts of decisions of my selection (the 18 whose *Scope* names `installation`, the ones the task names, and the invariants-scope ones for the entry written): read whole 10 — WAY-13, WAY-38, WAY-48, WAY-56, WAY-89, WAY-141, WAY-235, WAY-321, WAY-328, WAY-368; by title only: the rest of the 18 installation-scope decisions (WAY-09, WAY-27, WAY-34 — opening lines only —, WAY-100, WAY-102, WAY-107, WAY-127, WAY-167, WAY-259, WAY-324, WAY-344, WAY-370), and the titles of about 60 decisions whose *Scope* names `invariants`, which I listed and skimmed.
- Each decision that bears on the change and stayed unread whole: WAY-58, WAY-60, WAY-61, WAY-62, WAY-65, WAY-71, WAY-73 and WAY-33 — their titles point to the form of an invariant entry; I read the template that carries their rules whole (`elements/invariants/template.md`, `elements/common/rules.md`) instead and did not open the decisions.
- Guideline files: none apply (WAY-328); none read.
- Not read whole: `foundations/part_map.md` outside the parts `installation`, `invariants` and the surface `installation-command`; `foundations/invariants.md` outside the entries named above; `foundations/glossary.md` (searched `junction|symlink|symbolic` — no entry; see below).
- The repository tests other than the three I ran.

## Searches not found or unclear

- Glossary entry or environment fact for "Windows junction": searched `foundations/glossary.md` and `foundations/environment_facts.md` for `junction`, `symlink`, `symbolic`: no entry (the same as the author found). No finding for the glossary: no sentence is read wrongly for lack of it.
- Whether `instruction-files` is "a part of test helpers" under `cross-part-imports`: not looked up; it matters only for the helper copy and I do not dispute it.
- The author's report says `installation/README.md` is +9 / -2; the diff shows +9 / -2 (11 lines in `--stat`); consistent.
