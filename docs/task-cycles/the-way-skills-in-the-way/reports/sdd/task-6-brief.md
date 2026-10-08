### Task 6: Installer sentence and its test (`installation`, trust boundary)

**Files:**
- Modify: `installation/install.py:128` (one string literal in `skill_wrapper`)
- Test: `installation/test_install.py` (new method before `test_guidance_names_no_commit_and_covers_the_product_rules`)

**Interfaces:** Consumes Task 4's paragraphs (the wrapper now sends the agent to "where it says where the-way lies"). `install.skill_wrapper(path: str, name: str, commit: str) -> str` keeps its signature.

- [ ] **Step 1: Write the failing test** — insert into class `InstallTest`, before `def test_guidance_names_no_commit_and_covers_the_product_rules`:

```python
    def test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies(self) -> None:
        for path, name in NAMES:
            with self.subTest(name):
                text = install.skill_wrapper(path, name, self.commit)
                self.assertIn("Where it says where the-way lies, the product's case applies: "
                              "here the process root is `.the-way`.", text)
                self.assertNotIn("global install", text)
                self.assertIn("Do not substitute a global skill.", text)
```

- [ ] **Step 2: Run it to see it fail**

Run: `cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py installation`
Expected: exit 1, `FAIL: test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies` (11 subtests) with `AssertionError: "Where it says where the-way lies…" not found`.

- [ ] **Step 3: Change the sentence** — in `installation/install.py`, line 128, replace the literal
`"Its paragraph about resolving a global skill link applies only to a global install; "`
with
`"Where it says where the-way lies, the product's case applies: "`.
Line 129 (`f"here the process root is `{SUBMODULE}`. Do not substitute a global skill.\n\n"`) stays.

- [ ] **Step 4: Run the installer's tests**

Run:
```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && python -B gate/run_tests.py installation > $R/reports/check_6_tests_installation.txt 2>&1; echo $?; tail -3 $R/reports/check_6_tests_installation.txt
```
Expected: exit 0, `Ran 17 tests`, `OK` (the planner ran this change and test in a scratch copy: OK). WAY-48: the change replaces a string literal of generated text and adds no input, path, argument or subprocess; the installer's existing adversarial tests run in this suite (`test_rejects_agents_file_with_other_or_broken_block_before_writing`, `test_rejects_agents_or_ignore_file_that_is_no_regular_utf8_file`, `test_rejects_conflicting_integration_file_before_writing`, `test_rejects_an_ignored_submodule_path_before_writing`, `test_warns_before_writing_paths_git_ignores`, `test_warns_where_codex_would_miss_the_block`, `test_preview_apply_rerun_and_preserve_foundation`, `test_declined_apply_writes_nothing`).

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-skills-self && R=.runs/task-cycles/the-way-skills-in-the-way && git commit -m "fix(installation): Point a product's skill wrapper to the product case of where the-way lies" -- installation/install.py installation/test_install.py
```

For the request (step 12, `pinned` change path): "Moving the pin rewrites the eleven wrappers' sentence on the process root; `.the-way` now carries the-way's own `.claude/skills/` and `.agents/skills/`, which Claude Code may list as `.the-way:the-way-<name>` and which stop themselves in a product."

---

