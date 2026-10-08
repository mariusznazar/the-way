### Task 5: Check script — what the root files lead to (fixes B and D, the root layout; spec §4.5)

**Files:**
- Modify: `instruction-files/check_instructions.py` (docstring, one constant, new `pointed_files`, `check_layout` and `check` replaced whole)
- Test: `instruction-files/test_check_instructions.py` (two methods of `RootLayout`, two of `Skills`, class `PointedFiles`)

**Interfaces:**
- Consumes: Tasks 3–4.
- Produces: `POINTED_SUFFIXES = (".md", ".mdc")`; `pointed_files(root, texts, files) -> list[tuple[str, str]]` (real path, path from the root); the final `check_layout` and `check`. New message: `` `@AGENTS.md` alone is not its first line `` (`WARN`, `root-layout`, at the line of the import); the unpointed-skill note now reads "… have no pointer in AGENTS.md and no copy in .agents/skills; …".

- [ ] **Step 1: Write the failing tests** in `instruction-files/test_check_instructions.py`:

(a) Insert into class `RootLayout`, before `test_agents_import_with_no_agents_md_beside_it_is_a_warning_on_any_line`:

```python
    def test_crlf_line_ends_keep_the_first_line_sound(self):
        repo = self.repo({"CLAUDE.md": b"@AGENTS.md\r\nNotes.\r\n", "AGENTS.md": "Rules.\n"})
        self.assertEqual([f for f in repo.findings() if f.check in ("root-layout", "at-import")], [])

    def test_agents_import_under_a_heading_is_one_warning_of_the_layout(self):
        repo = self.repo({"CLAUDE.md": "# Claude\n@AGENTS.md\n", "AGENTS.md": "Rules.\n"})
        found = [(f.check, f.level, f.line, f.message) for f in repo.findings()
                 if f.file == "CLAUDE.md" and f.check != "size"]
        self.assertEqual(found, [("root-layout", "warn", 2,
                                  "`@AGENTS.md` alone is not its first line")])
```

(b) Append to class `Skills`:

```python
    def test_a_skill_with_its_copy_in_agents_skills_needs_no_pointer(self):
        repo = self.repo({
            "AGENTS.md": "Rules.\n",
            ".claude/skills/x/SKILL.md": SKILL,
            ".agents/skills/x/SKILL.md": SKILL,
        })
        self.assertNotIn("skill-dir", checks(repo.findings()))

    def test_a_copy_without_skill_md_or_under_another_name_leaves_the_skill_unpointed(self):
        repo = self.repo({
            "AGENTS.md": "Rules.\n",
            ".claude/skills/x/SKILL.md": SKILL,
            ".agents/skills/x/README.md": "Not a skill.\n",
            ".claude/skills/y/SKILL.md": SKILL,
            ".agents/skills/z/SKILL.md": SKILL,
        })
        found = [f for f in repo.findings() if f.check == "skill-dir"]
        self.assertEqual(sorted((f.level, f.file) for f in found),
                         [("info", ".claude/skills"), ("warn", ".agents/skills/z/SKILL.md")])
        self.assertIn("2 skills", [f for f in found if f.level == "info"][0].message)
```

(c) Insert after class `Skills`:

```python
class PointedFiles(CheckTestCase):
    def files_of(self, findings, rel):
        return sorted((f.check, f.level) for f in findings if f.file == rel)

    def test_a_markdown_file_the_root_agents_md_names_is_checked(self):
        repo = self.repo({"AGENTS.md": "Before you start, read `guide/README.md`.\n",
                          "guide/README.md": DEFECTS})
        self.assertEqual(self.files_of(repo.findings(), "guide/README.md"),
                         [("dead-path", "warn"), ("emphasis", "warn"), ("size", "info")])

    def test_a_file_named_by_both_root_files_is_checked_once(self):
        repo = self.repo({"AGENTS.md": "Read `a.md`.\n", "CLAUDE.md": "@AGENTS.md\nRead `a.md` too.\n",
                          "a.md": DEFECTS})
        self.assertEqual(self.files_of(repo.findings(), "a.md"),
                         [("dead-path", "warn"), ("emphasis", "warn"), ("size", "info")])

    def test_an_instruction_file_it_names_is_checked_once(self):
        repo = self.repo({"AGENTS.md": "When in `src/`, read `src/AGENTS.md`.\n",
                          "src/AGENTS.md": "Rules.\n"})
        self.assertEqual(self.files_of(repo.findings(), "src/AGENTS.md"), [("size", "info")])

    def test_files_outside_the_root_are_not_read(self):
        repo = self.repo({}, outside={"outside.md": DEFECTS})
        absolute = os.path.join(repo.base, "outside.md")
        write(repo.root, "AGENTS.md", f"Read `../outside.md` and `{absolute}`.\n")
        found = repo.findings()
        self.assertEqual([f for f in found if "outside" in f.file], [])
        self.assertEqual(dead(found), [])

    def test_a_link_out_of_the_root_is_not_read(self):
        repo = self.repo({"AGENTS.md": "Read `inside.md`.\n"}, outside={"outside.md": DEFECTS})
        make_file_link(self, os.path.join(repo.base, "outside.md"), os.path.join(repo.root, "inside.md"))
        self.assertEqual([f for f in repo.findings() if f.file != "AGENTS.md"], [])

    def test_a_file_named_by_a_pointed_file_is_not_followed(self):
        repo = self.repo({"AGENTS.md": "Read `a.md`.\n", "a.md": "Then read `b.md`.\n",
                          "b.md": DEFECTS})
        self.assertEqual(self.files_of(repo.findings(), "b.md"), [])

    def test_a_pointed_path_with_a_line_number_or_an_upper_case_suffix_is_checked(self):
        repo = self.repo({"AGENTS.md": "See `guide/A.MD:12` and `guide/b.md:3`.\n",
                          "guide/A.MD": DEFECTS, "guide/b.md": DEFECTS})
        found = repo.findings()
        for rel in ("guide/A.MD", "guide/b.md"):
            self.assertEqual(self.files_of(found, rel),
                             [("dead-path", "warn"), ("emphasis", "warn"), ("size", "info")])

    def test_files_that_are_not_markdown_or_lie_in_nested_repositories_are_not_read(self):
        repo = self.repo({
            "AGENTS.md": "Read `notes.txt`, `sub/a.md` and `node_modules/pkg/a.md`.\n",
            "notes.txt": DEFECTS,
            "sub/.git": "gitdir: ../.git/modules/sub\n",
            "sub/a.md": DEFECTS,
            "node_modules/pkg/a.md": DEFECTS,
        })
        self.assertEqual([f.file for f in repo.findings() if f.file != "AGENTS.md"], [])
```

- [ ] **Step 2: Run them to see them fail**

Run: `cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py instruction-files 2>&1 | grep -E "^(FAIL|ERROR):|^Ran|^FAILED" | sed 's/ (.*//' | sort | uniq -c`
Expected (planner): `Ran 69 tests`, `FAILED (failures=5, skipped=1)` — `test_a_file_named_by_both_root_files_is_checked_once`, `test_a_markdown_file_the_root_agents_md_names_is_checked`, `test_a_pointed_path_with_a_line_number_or_an_upper_case_suffix_is_checked`, `test_a_skill_with_its_copy_in_agents_skills_needs_no_pointer`, `test_agents_import_under_a_heading_is_one_warning_of_the_layout`. The other new tests are the opposite failures (a file outside the root, through a link, named by a pointed file, not Markdown, in a nested repository; a copy without `SKILL.md` or under another name; CRLF) and pass already.

- [ ] **Step 3: Write the implementation** in `instruction-files/check_instructions.py`:

(a) In the module docstring, after "…emphasis spread over several rules, and the size of every file." add "The Markdown files that the root `AGENTS.md` or `CLAUDE.md` names in backticks are checked as well." so that the paragraph reads:

```text
Settles, without reading what the rules say, the checks of section 6 of principles.md, which lies
next to this script: paths that do not exist, `@path` imports that Claude Code loads into every
session or silently skips, Cursor rules that Cursor ignores, a root layout that hides `AGENTS.md`
from Claude Code, subdirectory `AGENTS.md` files Codex will not reach, skills one of the tools
cannot discover, emphasis spread over several rules, and the size of every file. The Markdown
files that the root `AGENTS.md` or `CLAUDE.md` names in backticks are checked as well.
```

(b) Put `POINTED_SUFFIXES = (".md", ".mdc")` after the `SKILL_DIRS` line.

(c) Insert before `check_layout`:

```python
def pointed_files(root, texts, files):
    """The Markdown files the root AGENTS.md or CLAUDE.md names in backticks, as paths relative
    to ROOT: each a regular file whose real path lies inside ROOT, outside the skipped directories
    and nested repositories, that is not already an instruction file; each once, one level deep."""
    real_root = os.path.realpath(root)
    known = {os.path.realpath(os.path.join(root, *rel.split("/"))) for rel in files}
    found = []
    for main in ("AGENTS.md", "CLAUDE.md"):
        text = texts.get(main)
        if not text:
            continue
        for _, line in prose_lines(text):
            for match in CODE_SPAN.finditer(line):
                token = LINE_SUFFIX.sub("", match.group(1).strip())
                if not token.lower().endswith(POINTED_SUFFIXES) or is_network(token):
                    continue
                if not looks_like_path(token):
                    continue
                real = os.path.realpath(os.path.join(root, os.path.expanduser(token)))
                if real in known or not inside(real, real_root) or real == real_root:
                    continue
                rel = os.path.relpath(real, real_root).replace(os.sep, "/")
                parts = rel.split("/")
                if any(part in SKIP_DIRS for part in parts[:-1]):
                    continue
                if any(os.path.exists(os.path.join(real_root, *parts[:depth], ".git"))
                       for depth in range(1, len(parts))):
                    continue
                try:
                    if not stat.S_ISREG(os.stat(real).st_mode):
                        continue
                except OSError:
                    continue
                known.add(real)
                found.append((real, rel))
    return found
```

(d) Replace `check_layout` whole with:

```python
def check_layout(root, files, texts, findings):
    present = set(files)
    for rel in files:
        if rel != "CLAUDE.md" and not rel.endswith("/CLAUDE.md"):
            continue
        folder = rel[: -len("CLAUDE.md")]
        if folder + "AGENTS.md" not in present or rel.endswith(".claude/CLAUDE.md"):
            continue
        claude = texts.get(rel)
        if claude is None:
            continue
        lines = [line.strip() for line in claude.splitlines()]
        if "@AGENTS.md" not in lines:
            findings.append(Finding(
                "warn", "root-layout", rel, 0,
                "CLAUDE.md stands beside AGENTS.md without an `@AGENTS.md` line, so Claude Code "
                "does not read AGENTS.md"))
        elif lines[0] != "@AGENTS.md":
            findings.append(Finding("warn", "root-layout", rel, lines.index("@AGENTS.md") + 1,
                                    "`@AGENTS.md` alone is not its first line"))
    if "AGENTS.md" in present and "CLAUDE.local.md" in present:
        findings.append(Finding("warn", "root-layout", "CLAUDE.local.md", 0,
                                "CLAUDE.local.md stops Claude Code from reading AGENTS.md"))
    main = texts.get("AGENTS.md") or ""
    for rel in files:
        if rel != "AGENTS.md" and rel.endswith("/AGENTS.md") and rel not in main:
            findings.append(Finding(
                "warn", "nested-pointer", rel, 0,
                f"no line of the root AGENTS.md points to {shown(rel)}; Codex reads it only when a "
                "session starts in its directory"))
    unpointed = []
    for rel in files:
        if not rel.endswith("/SKILL.md"):
            continue
        skill_dir = rel[: -len("/SKILL.md")]
        if rel.startswith(".agents/skills/") or "/.agents/skills/" in rel:
            twin = skill_dir.replace(".agents/skills", ".claude/skills") + "/SKILL.md"
            if twin not in present:
                findings.append(Finding("warn", "skill-dir", rel, 0,
                                        "Claude Code does not read .agents/skills"))
        elif rel.startswith(".claude/skills/") and skill_dir not in main:
            if ".agents/skills/" + rel[len(".claude/skills/"):] not in present:
                unpointed.append(skill_dir)
    if unpointed:
        findings.append(Finding(
            "info", "skill-dir", ".claude/skills", 0,
            f"{len(unpointed)} skills in .claude/skills have no pointer in AGENTS.md and no copy "
            "in .agents/skills; Codex does not read .claude/skills, so point to the SKILL.md of "
            "each one Codex needs"))
```

(e) Replace `check` whole with:

```python
def check(root, extra=()):
    """Findings for the instruction files of the repository at ROOT and for EXTRA files. With ROOT
    None, only the EXTRA files are checked."""
    findings = []
    if root is None:
        for path in extra:
            check_file(path, path, None, findings, in_repo=False)
        return findings
    root = os.path.abspath(root)
    files = instruction_files(root, findings)
    present = set(files)
    texts = {}
    seen = set()
    for rel in files:
        path = os.path.join(root, *rel.split("/"))
        seen.add(os.path.realpath(path))
        folder = rel[: -len(os.path.basename(rel))]
        texts[rel] = check_file(path, rel, root, findings,
                                agents_beside=folder + "AGENTS.md" in present)
        if rel.startswith(".cursor/rules/") or "/.cursor/rules/" in rel:
            check_cursor_rule(rel, texts[rel], findings)
    for real, rel in pointed_files(root, texts, files):
        seen.add(real)
        check_file(real, rel, root, findings)
    for path in extra:
        if os.path.realpath(path) in seen:
            continue
        check_file(path, path, root, findings, in_repo=False)
    check_layout(root, files, texts, findings)
    return findings
```

- [ ] **Step 4: Run the tests to see them pass, and the script on known inputs**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py instruction-files > $R/reports/check_5_tests_instruction_files.txt 2>&1; echo "instruction-files $?"; tail -1 $R/reports/check_5_tests_instruction_files.txt; python -B instruction-files/check_instructions.py . ; echo "exit $?"; python -B instruction-files/check_instructions.py /c/Storage/repos/loop2 | grep -v "INFO  size"; echo "exit $?"
```
Expected (planner): `0`, `OK (skipped=1)` (69 tests); on the-way exactly

```text
WARN  dead-path AGENTS.md:20 `_zadania\` does not exist
INFO  size AGENTS.md:0 21 lines, 187 words
INFO  size CLAUDE.md:0 1 lines, 1 words
INFO  size agent-instructions/README.md:0 49 lines, 475 words
0 error, 1 warn, 3 info
```
— the `_zadania\` `WARN` is the known false alarm (R8: a directory relative to the private backlog file), the unpointed-skill note is gone (fix B), and `agent-instructions/README.md` is checked (fix D); on `loop2`: `0 error, 0 warn, 2 info` with no `skill-dir` line (the prototype gave "11 skills in .claude/skills have no pointer"); both exit 0.

- [ ] **Step 5: Commit**

```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && S="Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" && git commit -m "feat(instruction-files): Check the files the root instruction files name, count skill copies for Codex, and require @AGENTS.md first" -m "$S" -- instruction-files/check_instructions.py instruction-files/test_check_instructions.py
```

---

