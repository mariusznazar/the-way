# Findings of the review of the whole change, for the fix

Cut word for word from `reports/review-whole-report.md` (first line `FAIL 474df77904b199e3ba1acb438c5a88c9a47d13c1`): the blocking finding, then the Minor findings of the review within the task. Finding 7 of that report is outside the task and is not here.

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
