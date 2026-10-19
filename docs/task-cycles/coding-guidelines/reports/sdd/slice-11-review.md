# Slice 11 task review — the installer gives products the skill

Reviewer: task reviewer (Superpowers 6.4.1 template, cycle contract). BASE `8901da0`, HEAD `2eabf42`.
Read: brief, constraints, report, the review package diff once, spec §6.5–§6.6, rulings C36/C37
(`cycle.md:147-148`, `progress.md:110-111`), `foundations/invariants.md:2095-2103`.

### Spec Compliance

- ✅ Spec compliant. Each file in the brief's change list has its hunk, plus the file C36 adds:
  - `installation/install.py:40`: the one `SKILLS` entry `"maintain-coding-guidelines": "product-guidelines/coding/SKILL.md"`, and no other installer line changes. The `installation-command` surface keeps its wording.
  - `installation/README.md:56`: the table names `maintain-coding-guidelines`.
  - `installation/README.md:132-134`: the test list names the entry points and the three refusals.
  - `installation/test_coding_guidelines_installation.py`: new, 164 lines, follows the pattern of `test_styleguide_installation.py`.
  - `installation/test_styleguide_installation.py:92`: 30→32, as C36 rules.
- ✅ The sibling sentence and the block are built from `SKILLS`, so the new skill reaches every wrapper and the `AGENTS.md` block without other edits.
  - Risk: the brief's claim depends on generation code outside the diff.
  - Checked: `install.py:107-109` (`sibling_names()` iterates `SKILLS`), `install.py:145-146` (`product_guidance()` iterates `SKILLS`) and `install.py:310-313` (`plan()` writes one wrapper per `SKILLS` entry in both directories).
- ✅ WAY-48 crafted input: `test_coding_guidelines_installation.py:126-160` covers 12 subtests: `.claude`/`.agents` × a conflicting file, a directory or a non-UTF-8 file × preview or `--apply`. Each subtest asserts:
  - exit ≠ 0;
  - no "Installed.";
  - the whole tree outside `.git`, directories included, is unchanged;
  - the index is empty.
- ✅ The RED evidence shows the subtests went red for the intended reason. At BASE, all 12 failed on `0 == 0`, because the installer accepted the crafted path (`slice-11-red-installation.txt:3-7252`).
- ✅ The F4 `NAMES` tests pass at HEAD (`slice-11-names-tests.txt`). At BASE, 3 of the 4 were red (`slice-11-red-installation.txt:7920-7938`).
- ✅ C37 is applied as ruled. The non-UTF-8 case asserts only the exit and the unchanged tree (`test_coding_guidelines_installation.py:148-152`).
  - Risk: is the traceback real, and does it come before any write?
  - Checked: `install.py:364` calls `path.read_text(encoding="utf-8")` inside `plan()`, which runs before every write. `install.py:504` catches only `RuntimeError, OSError, EOFError`, so the `UnicodeDecodeError` escapes as a traceback. The traceback is pre-existing and affects every wrapper.
- ⚠️ Cannot verify from the diff: behaviour on Python 3.14 (O3). The executor ran 3.13.16.

### Deliberate break (installation-claude-guidance/1)

- Worktree: `git worktree add --detach <scratchpad>/review-2eabf42 2eabf42`. I deleted the line `"maintain-coding-guidelines": "product-guidelines/coding/SKILL.md",` from `installation/install.py` there.
- Command: `python3 -B gate/run_tests.py installation`. Result: exit 1, 35 tests, `FAILED (failures=17)`.
- Output: `docs/task-cycles/coding-guidelines/reports/sdd/slice-11-break-installation.txt`
- **Detected.** `test_install.InstallTest.test_preview_apply_rerun_and_preserve_foundation` cites `installation-claude-guidance/1` (`test_install.py:98`). It fails at `test_install.py:97` with ``'`maintain-coding-guidelines`' not found`` (output line 7931).
- The other failures:
  - 13 in the new file;
  - `test_guidance_names_no_commit_and_covers_the_product_rules` (`:139`);
  - `test_warns_before_writing_paths_git_ignores` (`:313`);
  - the styleguide count test (`30 != 32`).
- The worktree was removed with `git worktree remove --force` and `git worktree prune`. `git worktree list` shows only the checkout, and the checkout is unchanged (`git status --short` is empty, HEAD is `2eabf42`).
- See Minor 1: this break leaves the invariant's sentence true.

### Weakest point (WAY-164) and sharpness inputs

- The weakest point is the right one: whether a product's agent can reach and follow the skill through the new wrapper.
- `slice-11-weakest.txt` shows:
  - the installed `.the-way/product-guidelines/coding/SKILL.md` is identical to the source;
  - every path of the-way the skill names resolves under `.the-way/`;
  - the three ABSENT lines are explained correctly: two paths with a doubled `.the-way/.the-way/` prefix, and the product's own `guidelines/coding.md`;
  - the wrapper's text is as stated.
- Sharpness inputs match the diff:
  - `--numstat`: 4/2, 1/0, 164/0, 1/1.
  - The only part touched is `installation`.
  - The only trust-boundary file touched is `installation/install.py`. The change is one dict entry with no parsing, and the crafted-input tests are present.
  - `product-guidelines/form_check.py` is not touched.

### Strengths

- The change is minimal and exact: one dict line in `install.py:40`, and nothing else in the installer.
- The crafted-input test (`test_coding_guidelines_installation.py:52-56`, `:141-160`) compares the whole tree, directories included, and also checks that the index is empty. This is stricter than a plain file snapshot and catches a half-created directory.
- The refusal message is asserted on `directory` and `NAME` separately (`:155-156`), so the test holds on Windows path separators.
- The test expectations come from inputs:
  - the description is read from the committed skill (`:87-91`);
  - the counts and names are literals.
  - The test does not echo the installer's own code.
- Before anything else, the test checks that the skill is committed at HEAD (`:33-34`), so a stale checkout gives a clear failure, not a confusing one.
- The product-preservation checks use CRLF originals and include `guidelines/coding.md` (`:61-66`, `:113-114`), which is the file the skill will write.
- The report is thorough: every exit code and unchecked line is kept, and the 3 `instruction-files` failures are diffed against the BASE baseline.

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

None.

#### Minor (Nice to Have)

1. **Outside the task's scope, for the controller.** The dispatched break does not falsify the sentence of `installation-claude-guidance/1`.
   - That sentence (`foundations/invariants.md:2097`) is about root `CLAUDE.md`: created with `@AGENTS.md`, preserved byte for byte, warned on, and no `.claude/rules/the-way.md`. Removing a `SKILLS` entry leaves it true.
   - The break is caught only because `test_preview_apply_rerun_and_preserve_foundation` holds `NAMES` assertions (`test_install.py:84-97`) in the same method that carries the invariant citation (`:98`).
   - So the detection proves that `NAMES` covers the new entry. It does not prove the invariant's coverage, and none of this slice's code is in any invariant's sentence.
   - Possible fix, a separate task: limit citations to the assertions that state the sentence, or name the skills-in-product rule in an invariant of its own.
2. `slice-11-weakest.txt`: the evidence file has two gaps. Neither changes the conclusion.
   - Its section "--- where the-way lies, in the skill:" is empty. The report's claim ("line 20") is true: `product-guidelines/coding/SKILL.md:20` reads "in a product, it is the product's pinned `.the-way`". But the file does not carry it.
   - The second wrapper section is labelled "wrapper (claude)" where it should presumably read codex.
3. `test_coding_guidelines_installation.py:136-140`: the crafted test reassigns `self.product` to a fresh directory in each subtest.
   - The product that `setUp` creates goes unused.
   - After the loop, `self.product` points at a deleted directory.
   - This works, because `git()` and `install()` read `self.product`. A local variable passed to small helpers would be clearer. The cost is legibility only.
4. `test_coding_guidelines_installation.py:148-152`: the non-UTF-8 subtests assert only exit ≠ 0, as C37 rules. The cause is pinned only by the RED run, where the same subtests passed through to exit 0 without the entry. An assertion that stderr names `UnicodeDecodeError` or the wrapper path would keep that cause fixed if the code changes later. Optional, and it fits C37's "assert exit≠0" ruling.
5. Pre-existing, carried as concerns (not this slice):
   - C37: a non-UTF-8 wrapper gives a traceback, not an `Error:` line (`install.py:364`, `:504`).
   - C32: `test_install.py` `NAMES` lacks `lead-project` and `maintain-styleguide`.

### Assessment

**Task quality:** Approved

**Reasoning:** The slice adds exactly the one `SKILLS` entry, its README reflections and the C36 count. The new test shows the install, the byte-identical wrappers, the sibling sentence, the block and the preservation of product files. It also shows all 12 crafted refusals, each red at BASE for the intended reason. The deliberate break was detected by a test citing the invariant. That invariant's sentence does not state what the break removed (Minor 1, for the controller).
