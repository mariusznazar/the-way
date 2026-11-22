FAIL 1c222ce238c2194900ec246de5f8cc6cfa7faa5b

# Review of the whole change — installer-foundation-check-full-path

- Range: `fad52af301db6fd6b831850e9bf69f6a11559a4a..1c222ce238c2194900ec246de5f8cc6cfa7faa5b`, one
  commit `1c222ce2` ("Name the foundation check by its full path in the installer's block"). The
  route is one author with no plan, so no slice applies to any finding. `git rev-parse HEAD` in the
  reviewed worktree gave `1c222ce238c2194900ec246de5f8cc6cfa7faa5b`, which is the head the handoff gives.
- Changed files (`git diff --numstat`):
  - `foundations/invariants.md`: +10 / -0
  - `installation/install.py`: +3 / -3
  - `installation/test_install.py`: +25 / -3. The author's report says +26 / -2. The count is wrong
    and the content is right.
- Counts: 1 blocking finding (Important), 2 Minor findings, 0 findings outside the task's scope.
  Four behaviours are set aside under **Declined to judge**.

## Findings

### Important

**1. WAY-418's *Verification* does not name the invariant the change derives from it**
(`foundations/decisions.md:3349`, the entry WAY-418, against `foundations/invariants.md:334-342`).

The change adds the invariant `installation-agents-md-warnings` with `**Derives from:** WAY-418`.
WAY-418's *Verification* still holds only its pair of examples ("an agent compares a change with the
decision: complies … violates …") and has no `invariants:` clause. The foundation requires that link
in three places:
- WAY-12 (`foundations/decisions.md:768-770`), binding: "A decision names in *Verification* the
  invariants derived from it, by the identifiers of their entries, where such invariants exist".
- The decision template's section "Verification" (`elements/decisions/template.md:270-272`):
  "*Verification* names, after `invariants:`, the invariants of the product's invariants file that
  derive from the decision, each by its identifier, and only where such invariants exist; each of
  them names the decision in *Derives from*".
- The step of the invariants skill that the author's entry went through
  (`elements/invariants/skill/write.md:5-6`): "Step 4.4: what follows from this entry is a decision
  whose level 1 verification gains, loses or renames it, through `record-decision`."

The author's report reads step 4.4 as applying only to a decision whose verification "calls for"
the entry. That wording belongs to `decide_entry.md:19`, which governs the search for a decision
that asks for a rule. `write.md` says that the decision's verification *gains* the new entry. The
orchestrator left the decision unchanged because no row of *Settlements to record* asks for the
edit. Row 2, though, settles an invariant that derives from WAY-418, and WAY-12 makes the link a
part of writing such an invariant. It is no further change of meaning.

Why it matters: by the template's table of fields (`elements/decisions/template.md:130`),
*Verification* is where "whoever looks for the checks of the decision" finds its invariants. Someone
reading WAY-418 sees only an agent's comparison and does not learn that a test now holds part of it.
A later change of WAY-418 would then miss the invariant and its test. `elements/common/foundation_check.py`
does not check this link, so it passes with 0 errors and nothing else would catch the gap.

Evidence: the probe `reports/review-whole-probe-derived-links.py` lists, for each invariant, every
decision in its *Derives from* whose *Verification* does not name it.
- On the head: "16 of 75 links not named" (`reports/review-whole-probe-derived-links-head.txt`).
- On the base: "15 of 74" (`reports/review-whole-probe-derived-links-base.txt`).
- The one new gap is `installation-agents-md-warnings <- WAY-418`. The other 15 are older
  trust-boundary invariants (see **Declined to judge**). Elsewhere in the-way 59 of 75 links follow
  the rule, `installation-claude-guidance` in WAY-141 among them.

Fix: through `record-decision`, WAY-418's *Verification* gains
`invariants: installation-agents-md-warnings.` in the form the template gives at
`elements/decisions/template.md:42-44`. Its pair of examples stays and is introduced as covering the
part no invariant holds ("An agent compares a change with the part no invariant and no test
holds:"). The invariant covers only the installer's block in a fresh product. The examples cover
every change that names a path and the grading done by the review. The binding sentences do not
change.

Contradiction: yes — WAY-12 (and the rule of `elements/decisions/template.md` § Verification that
carries it).

### Minor

**2. The new test lets an error on the root `AGENTS.md` pass** (`installation/test_install.py:454`).

The assertion keeps only lines that match `WARN +\S+ AGENTS\.md:`. A sentence of the block that the
checker reports at the level `error` passes the test. The checker exits 1 on that error, and the
test does not assert the exit code. In a product such an error stops the one command, which is worse
than the warning this test guards against. No test of the-way runs the checker on the block, so the
first sign would be every product's gate going red after the next pin move.

Evidence:
- `reports/review-whole-probe-mutations.py error-line` inserts "See @docs/rules.md." into the
  block's sentence about the part map. The new test then passes, exit 0
  (`reports/review-whole-probe-error-line.txt`).
- On a file holding that same line (`reports/review-whole-probe-error-line-AGENTS.md`), the checker
  reports `ERROR at-import AGENTS.md:3 @docs/rules.md. — a punctuation mark right after the path
  stops Claude Code from loading it` and exits 1.

Suggested fix: match `(ERROR|WARN) +\S+ AGENTS\.md:` too. This lies within the task, since it
concerns the test that To do item 2 asks for, but it goes beyond the warnings that item names.

**3. The invariant's sentence can be read to cover the product's own lines of `AGENTS.md`**
(`foundations/invariants.md:336`).

The sentence: "In a product made by a full run of the installation command, before any skill of
the-way has run in it, the script that checks instruction files, run on the product's root,
reports no warning on the root `AGENTS.md`." The installer also runs on products that already
exist, which keep their own text in `AGENTS.md` outside the marked block (WAY-28, the part-map
entry `installation-command`). For such a product, a path that the product's own lines name and
that does not exist makes the sentence false, and no change of the installer can prevent it. The
test builds only an empty product (`test_install.py:442`), so it checks the narrower reading.

My reading of "made by" is a product the run creates, and on that reading the code meets the
sentence, so this is a matter of form (WAY-364), not of content. A reader weighing a change to how
the installer treats an existing `AGENTS.md` could still read it as a rule the installer cannot
keep. A wording that removes the doubt: "…reports no warning on the root `AGENTS.md` the installation
command created". This lies within the task: row 2 of *Settlements to record* carries the same
breadth.

## Declined to judge

- `installation/install.py:213-214`: the block's sentence "an error that script reports stops the
  tests, and a warning does not", and whether the block should tell a product's agents that WAY-418
  makes a warning a blocking finding of review. Outside the task, which changes only the sentence
  that names the foundation check by its bare name.
- The 15 older links from an invariant to a decision that the decision's *Verification* does not
  name: WAY-48 and WAY-235 for the seven trust-boundary invariants, and WAY-368 for
  `installation-paths-through-links`. They existed at the base, and this change touches none of them.
- The warning on the new path in a clone whose `.the-way` is not initialized. The task's question 2
  settles it: such a clone is not the product's state after installation.
- Whether the request names the invariant tests the change alters (WAY-03). The request is not
  written yet; the tests to name are listed under "Changed invariant tests" below.

## Against the task

- To do 1 / row 1: met. The installer's sentence about the empty part map (`install.py:207-209`) now
  names `{SUBMODULE}/elements/common/foundation_check.py` in backticks, the way the two sentences
  beside it name it. The expected `BLOCK` follows it (`test_install.py:75-77`), and the commit
  message gives the cause on the requirement's side (WAY-418).
- To do 2 / row 2: met, apart from findings 1 and 3. A git test builds the product by a full
  `--apply` installation. It asserts as a precondition that the product has no `.runs` (question 1)
  and runs the product's pinned checker on the product's root. It guards against an empty pass with
  the line that counts the findings, whose form comes from the checker's own description. It cites
  `invariant: installation-agents-md-warnings`, and the entry reads `Method: test`, `Violated: no`.
- Question 1: the sentence about `.runs/` is unchanged, and the test relies on the real `.gitignore`
  line. A mutation that drops that line turns the test red (below).
- Question 2: the full path is used, not the `python -B …` form and not plain words.
- Nothing outside the task was added, and no reserved choice was taken
  (`project-level/technology/reserved_choices.md`, read).

## Changed invariant tests (WAY-03, named for the request)

- `installation/test_install.py`, `InstallTest.test_preview_apply_rerun_and_preserve_foundation`.
  It cites `invariant: installation-claude-guidance` (`:280`), and its expected `AGENTS.md`, the
  constant `BLOCK` (`:283`), changed with the sentence.
- `installation/test_install.py`, `InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`
  (new, `:434`). It cites `invariant: installation-agents-md-warnings`.

## Tests read against the guidelines

- Where the expected value comes from (`guidelines/testing.md`, WAY-394): "no warning" comes from
  WAY-418 and the invariant. The form of the count line comes from the description at the head of
  `instruction-files/check_instructions.py`, which the test's comment names. The precondition comes
  from the task's question 1, a human's judgement, cited the way other tests of this file cite tasks.
- Behaviour, not implementation: the precondition `.runs` absent stands before the check and is
  marked as one. It checks a property that the requirement names (the fresh clone with no `.runs/`).
- Level: a git test, which is the lowest level that runs the real installer and the real checker
  together.
- Seen failing once (WAY-08): confirmed by the probes below.

## Trust boundary and structure

- `installation/install.py` is the trust boundary of `installation`. The diff changes only a string
  literal. The interpolation is `SUBMODULE`, the constant `".the-way"` (`install.py:17`). No new read
  of outside data was added, and no path, argument or file the installer reads is handled
  differently, so no crafted input reaches new code. The new test starts the product's pinned
  checker as a process on a product that the test built itself. That is test code, not product code.
- The change holds no operation that cannot be undone.
- Size: `install.py` stays at 857 lines (the author reports 858), and `product_guidance` keeps its
  number of lines. The test of `function-and-file-size` passes on both the base and the head. A test
  file is outside the rule. No finding of structure.
- `guidelines/coding-repository-changer.md`: I judged that its row's *When to read* ("before adding
  or changing a repository changer") matches. `install.py` is listed as a file of that kind
  (`coding-repository-changer.md:18`), and the change changes it. I read the file whole. Its one
  rule, "Changing nothing without the act", is not reached by a change of the block's text, so the
  author's not reading it left no defect.
- WAY-418 check on the head: 0 warnings.

## Checks run

| Command | Where | Exit | Result |
|---|---|---|---|
| `git rev-parse HEAD`; `git log` / `git diff` / `git diff --numstat` `fad52af3..HEAD` | reviewed worktree | 0 | head matches; 1 commit; counts above |
| `python -B instruction-files/check_instructions.py` (the command of `installation/README.md:82`, in the-way the path without `.the-way/`) | reviewed worktree, head | 0 | `0 error, 0 warn, 5 info` |
| `python -B task-cycle/change_file_sizes.py fad52af3… 1c222ce2…` | reviewed worktree | 0 | invariants.md 569→579, install.py 857→857, test_install.py 1401→1423 |
| `python -B -m unittest test_size_invariant` (agent-instructions) | worktrees of base and head | 0 / 0 | 4 tests OK in each run; nothing over a threshold |
| `python -B -m unittest` the new test, `test_preview_apply_rerun_and_preserve_foundation` and the three `test_guidance_*` tests (installation) | head worktree | 0 | 5 tests OK |
| `python -B probe.py old-sentence` (block sentence reverted to the base) | head worktree, restored after | 1 | new test red: `WARN  dead-path AGENTS.md:10 \`foundation_check.py\` does not exist` |
| `python -B probe.py moved-script` (full path to a file the commit lacks) | same | 1 | new test red on `.the-way/elements/common/foundation_checks.py` |
| `python -B probe.py no-ignore-line` (first form: `RUNS` renamed) | same | 0 | not a valid mutation: the block and `.gitignore` both moved; replaced by the next |
| `python -B probe.py no-ignore-line` (`.gitignore` created with `build/`) | same | 1 | new test red: `WARN  dead-path AGENTS.md:8 \`.runs/\` does not exist` |
| `python -B probe.py error-line` (an `@` import with a full stop in the block) | same | 0 | new test passes: finding 2 |
| `python -B instruction-files/check_instructions.py errprobe` (the error line alone) | review directory | 1 | `ERROR at-import AGENTS.md:3 …` |
| full installation into an empty repository (`install.py . --apply --url <head worktree>`), then `python -B .the-way/instruction-files/check_instructions.py .` | review directory | 0 / 0 | `0 error, 0 warn, 3 info` across the whole product, only `INFO` on `.runs/` |
| `python -B elements/common/foundation_check.py` | head worktree | 0 | `0 errors` |
| `python -B -m unittest -v test_linter_invariant` (Ruff linter and formatter invariants) | head worktree | 0 | 5 tests OK, none skipped |
| `python -B derived_links.py head` / `base` | review directory | 0 / 0 | 16 of 75 / 15 of 74 links not named: finding 1 |
| `python -B elements/common/decision_index.py --sections …` and `--section … --part installation --part instruction-files --decision WAY-418 …` | reviewed worktree, output in the review directory | 0 / 0 | the selection below |

Not run: the full gate (`python -B gate/run_tests.py`), as the handoff says. The whole
`installation` directory (74 tests, about 10 minutes) was not rerun. The author reports exit 0, and
I ran the five tests that the change reaches.

The probe scripts ran from `.runs/review-whole/` against the head worktree `head/` beside them.
Their copies in `reports/` keep the same relative paths.

## Selection and reaches

- Parts touched: `installation` (install.py and its test) and `instruction-files` (named by the new
  entry's *Part*; `foundations/invariants.md` collects entries, WAY-44).
- Decision index: four sections ("Instruction files", "Invariants", "The-way and how a product
  takes it", "Rules of a product's tests"), plus `--part installation`, `--part instruction-files`
  and `--decision WAY-418`. 34 decisions listed in full and 27 by heading alone. From the headings I
  opened WAY-16, WAY-392, WAY-393 and WAY-394, and I opened WAY-418 because the task names it.
- Guidelines read whole: `guidelines/coding.md`, `guidelines/coding-repository-changer.md`,
  `guidelines/testing.md`. The headers of every file under `guidelines/` were inspected.
  `coding-check.md` applies to `instruction-files`, but the change touches no check code there.
- Part map: its head, and the entries `invariants`, `instruction-files`, `installation`,
  `product-guidelines`, `installation-command` and `foundation-check-command`.
- Invariants: `foundations/invariants.md` read whole, every entry whose *Part* names a touched part
  or `every` among them.
- Glossary: `repository instruction file` and `git test`.
- Reaches beyond the selection, and why:
  - WAY-12, WAY-17 and WAY-30 (`foundations/decisions.md:766`, `:562`, `:1273`), whole: the rule on
    *Verification* links for finding 1, and whether the edit needs the human.
  - `elements/decisions/template.md:255-310` (§ Verification): finding 1.
  - `elements/invariants/template.md` whole: the form of the new entry.
  - `elements/invariants/skill/write.md` and `decide_entry.md`, the passages found by a search for
    "calls for|record-decision": the author's reading of step 4.4.
  - `instruction-files/check_instructions.py`, the description at its head (lines 1-60) and its
    lines of output (`:1001-1003`): the form the test relies on.
  - `installation/README.md:58-85`: the command of the instruction check and the row of the block.
  - `project-level/technology/reserved_choices.md` whole, as section 2 of the method gives.

## Working copies

All stood in `.runs/review-whole/`:
- two worktrees, `head` (1c222ce2) and `base` (fad52af3), each removed with
  `git worktree remove --force` and then `git worktree prune`;
- a product made by a full installation (`product`), the error probe (`errprobe`), the decision
  indexes, the probe scripts and their outputs.

The whole directory was removed (`rm -rf` by its full path), and `git worktree list` shows none of
them. What the findings need is kept in `reports/` with the prefix `review-whole-probe-`. The
reviewed worktree, its index and its branch were not changed (`git status --short` is empty). The
installation tests made their own products in the system's temporary directory and removed them by
their cleanup.

## Unread material

- Decisions of the index read whole: 5 (WAY-418, WAY-16, WAY-392, WAY-393, WAY-394). WAY-12,
  WAY-17 and WAY-30, read whole too, lie outside the index.
- Of the other 56 decisions of the index, the 29 listed in full were read in their binding
  sentences as the index gives them, and the 27 listed by heading were read by question only.
  - WAY-395 was read only in its first lines. Its binding fields stand in the recipes of
    `guidelines/testing.md`, read whole.
  - WAY-385 was not opened: size was settled by its invariant's test.
  - None of the unread decisions bears on the change beyond what the index lines show.
- Guideline files: none unread.

## Searches not found or unclear

- Whether adding `invariants: installation-agents-md-warnings.` to WAY-418's *Verification* needs a
  human's approval under WAY-30. It is unclear. My reading is no: the edit adds the link that WAY-12
  requires and changes no binding sentence, and settlement row 2 carries the invariant it links.
- `elements/common/foundation_check.py` does not check that a decision's *Verification* names its
  derived invariants. I found no check of the-way that does, so the link rests on review alone.
