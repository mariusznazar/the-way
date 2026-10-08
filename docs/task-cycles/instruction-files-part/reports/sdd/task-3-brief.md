### Task 3: Check script — read only what may be read (trust boundary, spec §4.6)

The check script reads files the-way does not control. This task makes every read safe: at most 1 MiB, only regular files, the UTF-8 byte order mark stripped, any other encoding reported; no link to a directory followed and no file read through a link out of the root; every value printed escaped and cut; an unreadable file or directory reported and the run going on; a bad ROOT or `--file` stopping with exit 2. The checks themselves stay as the prototype has them, with every printed value passed through `shown()`.

**Files:**
- Modify: `instruction-files/check_instructions.py` (replaced whole below)
- Test: `instruction-files/test_check_instructions.py` (replaced whole below)

**Interfaces:**
- Consumes: the prototype's `Finding(level, check, file, line, message)` and checks.
- Produces (used by Tasks 4 and 5): constants `MAX_BYTES = 1048576`, `MAX_SHOWN = 200`; `shown(value) -> str`; `reason(error: OSError) -> str`; `inside(path, directory) -> bool`; `is_instruction_name(rel, name) -> bool`; `instruction_files(root, findings) -> list[str]`; `read_text(path, shown_as, findings) -> str | None`; `prose_lines(text)`; `looks_like_path(token) -> bool`; `is_relative(token) -> bool`; `check_file(path, shown_as, root, findings, in_repo=True) -> str | None`; `check_cursor_rule(rel, text, findings)`; `check_layout(root, files, texts, findings)`; `check(root, extra=()) -> list[Finding]`; `main(argv=None) -> int`. New finding checks: `read` (cannot be read, not UTF-8, cut at 1 MiB, link out of the repository) and `walk` (a link to a directory, a directory that cannot be listed). Test helpers: `write(base, rel, content)`, `Repo(files, outside=None)` with `.base`, `.root`, `.findings(extra=())`, `checks()`, `dead()`, `run_main()`, `make_file_link()`, `make_directory_link()`, and `CheckTestCase.setUp` setting `HOME` and `USERPROFILE` to an empty temporary directory.

- [ ] **Step 1: Write the failing tests** — replace `instruction-files/test_check_instructions.py` whole with:

```python
"""Tests of the mechanical checks of instruction files: each check fires on a repository broken on
purpose and stays silent on a sound one, and crafted input neither reaches past the files given
nor stops the run.

Every fixture is built in a temporary directory, and the home directory is an empty temporary
one, so no file of this repository or of the machine takes part.

Run from the root of the-way: python -B gate/run_tests.py instruction-files
"""

import contextlib
import io
import os
import stat
import sys
import tempfile
import unittest
from unittest import mock

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_instructions  # noqa: E402

SKILL = "---\nname: x\ndescription: Use for x.\n---\n"
DEFECTS = "Read `docs/gone.md`.\n\nIMPORTANT: a.\nIMPORTANT: b.\n"


def write(base, rel, content):
    path = os.path.join(base, *rel.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = content if isinstance(content, bytes) else content.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)


class Repo:
    """A temporary repository at `<temporary directory>/repo`, its files given as {relative path:
    text or bytes}; the OUTSIDE files are written beside it, in the temporary directory."""

    def __init__(self, files, outside=None):
        self._dir = tempfile.TemporaryDirectory()
        self.base = self._dir.name
        self.root = os.path.join(self.base, "repo")
        os.makedirs(self.root)
        for rel, content in files.items():
            write(self.root, rel, content)
        for rel, content in (outside or {}).items():
            write(self.base, rel, content)

    def findings(self, extra=()):
        return check_instructions.check(self.root, [os.path.join(self.root, e) for e in extra])

    def close(self):
        self._dir.cleanup()


def checks(findings, level=None):
    return sorted({f.check for f in findings if level is None or f.level == level})


def dead(findings):
    return [f for f in findings if f.check == "dead-path"]


def run_main(arguments):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = check_instructions.main(arguments)
    return code, out.getvalue(), err.getvalue()


def make_file_link(test, target, link):
    try:
        os.symlink(target, link)
    except (OSError, NotImplementedError) as error:
        test.skipTest(f"a file link cannot be made here: {error}")


def make_directory_link(test, target, link):
    try:
        if sys.platform == "win32":
            import _winapi
            _winapi.CreateJunction(target, link)
        else:
            os.symlink(target, link, target_is_directory=True)
    except (OSError, NotImplementedError) as error:
        test.skipTest(f"a directory link cannot be made here: {error}")


class CheckTestCase(unittest.TestCase):
    def setUp(self):
        home = tempfile.TemporaryDirectory()
        self.addCleanup(home.cleanup)
        self.home = home.name
        patcher = mock.patch.dict(os.environ, {"HOME": self.home, "USERPROFILE": self.home})
        patcher.start()
        self.addCleanup(patcher.stop)

    def repo(self, files, outside=None):
        repo = Repo(files, outside)
        self.addCleanup(repo.close)
        return repo


class AtImport(CheckTestCase):
    def test_import_followed_by_punctuation_is_an_error(self):
        repo = self.repo({"CLAUDE.md": "See @docs/a.md.\n", "docs/a.md": "x\n"})
        found = [f for f in repo.findings() if f.check == "at-import"]
        self.assertEqual([f.level for f in found], ["error"])
        self.assertEqual(found[0].line, 1)

    def test_import_used_as_a_pointer_is_a_warning(self):
        repo = self.repo({"CLAUDE.md": "See @docs/a.md for errors\n", "docs/a.md": "x\n"})
        self.assertEqual(checks(repo.findings(), "warn"), ["at-import"])

    def test_agents_import_alone_on_its_line_is_sound(self):
        repo = self.repo({"CLAUDE.md": "@AGENTS.md\n", "AGENTS.md": "Rules.\n"})
        self.assertNotIn("at-import", checks(repo.findings()))

    def test_at_inside_code_and_in_addresses_is_ignored(self):
        repo = self.repo({
            "AGENTS.md": "Mail a@example.com, run `npm i @scope/pkg`.\n```\n@x.md.\n```\n",
        })
        self.assertNotIn("at-import", checks(repo.findings()))


class DeadPath(CheckTestCase):
    def test_missing_path_in_backticks_is_reported(self):
        repo = self.repo({"AGENTS.md": "Before releasing, read `docs/release.md`.\n"})
        found = dead(repo.findings())
        self.assertEqual(len(found), 1)
        self.assertIn("docs/release.md", found[0].message)

    def test_existing_paths_relative_to_root_or_file_are_sound(self):
        repo = self.repo({
            "AGENTS.md": "Read `docs/a.md` and `src/`.\n",
            "docs/a.md": "x\n",
            "src/x/AGENTS.md": "Read `notes.md`.\n",
            "src/x/notes.md": "x\n",
        })
        self.assertNotIn("dead-path", checks(repo.findings()))

    def test_commands_globs_placeholders_and_urls_are_not_paths(self):
        repo = self.repo({
            "AGENTS.md": "Run `npm run dev`, edit `src/**/*.js`, see `<repo>/x.md`, "
                         "`https://example.com/a.md`, `--flag`.\n",
        })
        self.assertNotIn("dead-path", checks(repo.findings()))

    def test_slash_commands_versions_keys_domains_and_ellipses_are_not_paths(self):
        repo = self.repo({
            "AGENTS.md": "Use `/park`, tag `vX.Y.Z`, set `user.email`, see "
                         "`github.com/someone`, open `…\\SKILL.md:42`.\n",
        })
        self.assertNotIn("dead-path", checks(repo.findings()))

    def test_a_line_number_after_an_existing_path_is_sound(self):
        repo = self.repo({"AGENTS.md": "See `docs/a.md:3`.\n", "docs/a.md": "x\n"})
        self.assertNotIn("dead-path", checks(repo.findings()))

    def test_relative_path_in_a_file_outside_the_repository_is_only_noted(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "global/x.md": "Read `scripts/a.json`.\n"})
        found = [f for f in repo.findings(extra=["global/x.md"]) if f.check == "dead-path"]
        self.assertEqual([f.level for f in found], ["info"])


class CursorRules(CheckTestCase):
    def test_mdc_without_header_is_an_error(self):
        repo = self.repo({".cursor/rules/a.mdc": "Rule text.\n"})
        self.assertEqual(checks(repo.findings(), "error"), ["cursor-rule"])

    def test_md_in_cursor_rules_is_an_error(self):
        repo = self.repo({".cursor/rules/a.md": "---\nalwaysApply: true\n---\nRule.\n"})
        self.assertEqual(checks(repo.findings(), "error"), ["cursor-rule"])

    def test_mdc_with_header_is_sound(self):
        repo = self.repo({".cursor/rules/a.mdc": "---\nalwaysApply: true\n---\nRule.\n"})
        self.assertNotIn("cursor-rule", checks(repo.findings()))


class RootLayout(CheckTestCase):
    def test_claude_md_beside_agents_md_without_import(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n", "AGENTS.md": "Rules.\n"})
        self.assertIn("root-layout", checks(repo.findings(), "warn"))

    def test_claude_local_md_beside_agents_md(self):
        repo = self.repo({"CLAUDE.local.md": "Mine.\n", "AGENTS.md": "Rules.\n"})
        self.assertIn("root-layout", checks(repo.findings(), "warn"))

    def test_claude_md_importing_agents_md_is_sound(self):
        repo = self.repo({"CLAUDE.md": "@AGENTS.md\n", "AGENTS.md": "Rules.\n"})
        self.assertNotIn("root-layout", checks(repo.findings()))


class NestedAgents(CheckTestCase):
    def test_nested_agents_md_without_pointer(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "src/client/AGENTS.md": "Client.\n"})
        found = [f for f in repo.findings() if f.check == "nested-pointer"]
        self.assertEqual(len(found), 1)
        self.assertIn("src/client/AGENTS.md", found[0].message)

    def test_nested_agents_md_with_pointer_is_sound(self):
        repo = self.repo({
            "AGENTS.md": "When working in `src/client/`, read `src/client/AGENTS.md`.\n",
            "src/client/AGENTS.md": "Client.\n",
        })
        self.assertNotIn("nested-pointer", checks(repo.findings()))


class Skills(CheckTestCase):
    def test_skill_only_in_agents_skills_is_invisible_to_claude_code(self):
        repo = self.repo({".agents/skills/x/SKILL.md": SKILL})
        self.assertIn("skill-dir", checks(repo.findings(), "warn"))

    def test_skills_in_claude_skills_without_pointer_get_one_note_for_codex(self):
        repo = self.repo({
            "AGENTS.md": "Rules.\n",
            ".claude/skills/x/SKILL.md": SKILL,
            ".claude/skills/y/SKILL.md": SKILL,
        })
        found = [f for f in repo.findings() if f.check == "skill-dir"]
        self.assertEqual([f.level for f in found], ["info"])
        self.assertIn("2 skills", found[0].message)

    def test_skill_pointed_to_from_agents_md_is_sound(self):
        repo = self.repo({
            "AGENTS.md": "Releases follow `.claude/skills/x/SKILL.md`.\n",
            ".claude/skills/x/SKILL.md": SKILL,
        })
        self.assertNotIn("skill-dir", checks(repo.findings()))


class Emphasis(CheckTestCase):
    def test_more_than_one_emphasised_rule_is_a_warning(self):
        repo = self.repo({"AGENTS.md": "IMPORTANT: a.\nIMPORTANT: b.\n"})
        self.assertIn("emphasis", checks(repo.findings(), "warn"))

    def test_one_emphasised_rule_is_sound(self):
        repo = self.repo({"AGENTS.md": "IMPORTANT: a.\nb.\n"})
        self.assertNotIn("emphasis", checks(repo.findings()))


class Size(CheckTestCase):
    def test_every_instruction_file_gets_its_size(self):
        repo = self.repo({"AGENTS.md": "one\ntwo words\n", "notes.md": "not an instruction file\n"})
        found = [f for f in repo.findings() if f.check == "size"]
        self.assertEqual([(f.file, f.message) for f in found], [("AGENTS.md", "2 lines, 3 words")])

    def test_extra_file_outside_the_repository_is_checked(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "global/CLAUDE.md": "See @x.md.\n"})
        found = [f for f in repo.findings(extra=["global/CLAUDE.md"]) if f.check == "at-import"]
        self.assertEqual([f.level for f in found], ["error"])


class Discovery(CheckTestCase):
    def test_dependency_and_git_directories_are_skipped(self):
        repo = self.repo({
            "AGENTS.md": "Rules.\n",
            "node_modules/pkg/AGENTS.md": "IMPORTANT: a.\nIMPORTANT: b.\n",
        })
        self.assertEqual([f.file for f in repo.findings() if f.check == "size"], ["AGENTS.md"])

    def test_nested_repositories_and_submodules_are_skipped(self):
        repo = self.repo({
            "AGENTS.md": "Rules.\n",
            ".the-way/.git": "gitdir: ../.git/modules/the-way\n",
            ".the-way/AGENTS.md": "Process rules.\n",
        })
        self.assertEqual([f.file for f in repo.findings() if f.check == "size"], ["AGENTS.md"])

    def test_files_alone_are_checked_without_scanning_a_repository(self):
        repo = self.repo({"AGENTS.md": "IMPORTANT: a.\nIMPORTANT: b.\n", "g/CLAUDE.md": "x\n"})
        found = check_instructions.check(None, [os.path.join(repo.root, "g/CLAUDE.md")])
        self.assertEqual([f.check for f in found], ["size"])


class Links(CheckTestCase):
    def test_a_directory_link_or_junction_is_not_followed(self):
        repo = self.repo({"AGENTS.md": "Rules.\n"}, outside={"elsewhere/AGENTS.md": DEFECTS})
        make_directory_link(self, os.path.join(repo.base, "elsewhere"),
                            os.path.join(repo.root, "linked"))
        make_directory_link(self, repo.root, os.path.join(repo.root, "loop"))
        found = sorted((f.level, f.check, f.file, f.message) for f in repo.findings()
                       if f.file != "AGENTS.md")
        self.assertEqual(found, [("info", "walk", "linked", "a link to a directory, not followed"),
                                 ("info", "walk", "loop", "a link to a directory, not followed")])

    def test_a_file_link_out_of_the_repository_is_neither_read_nor_listed(self):
        repo = self.repo({}, outside={"secret.md": "Read `MARKER-SECRET-9/x.md`.\n"})
        make_file_link(self, os.path.join(repo.base, "secret.md"), os.path.join(repo.root, "AGENTS.md"))
        self.assertEqual([(f.level, f.check, f.file, f.message) for f in repo.findings()],
                         [("info", "read", "AGENTS.md", "a link out of the repository, not read")])
        code, out, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        self.assertNotIn("MARKER-SECRET-9", out)

    def test_a_file_given_with_file_is_read_through_its_link(self):
        repo = self.repo({}, outside={"global.md": "IMPORTANT: a.\nIMPORTANT: b.\n"})
        link = os.path.join(repo.base, "link.md")
        make_file_link(self, os.path.join(repo.base, "global.md"), link)
        self.assertIn("emphasis", checks(check_instructions.check(None, [link]), "warn"))


class LargeAndOddFiles(CheckTestCase):
    def test_only_the_first_mebibyte_is_read(self):
        repo = self.repo({"AGENTS.md": "word\n" * (check_instructions.MAX_BYTES // 5 + 100)})
        found = repo.findings()
        self.assertIn(("info", "read", "only the first 1048576 bytes were checked"),
                      [(f.level, f.check, f.message) for f in found])
        lines = check_instructions.MAX_BYTES // 5 + 1
        self.assertIn(f"{lines} lines, {lines} words", [f.message for f in found if f.check == "size"])

    def test_a_file_that_is_not_regular_is_not_opened(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "CLAUDE.md": "@AGENTS.md\n"})
        target = os.path.join(repo.root, "AGENTS.md")
        real_stat, real_open = os.stat, open

        def device_stat(path, *args, **kwargs):
            if os.fspath(path) == target:
                return os.stat_result((stat.S_IFCHR | 0o644,) + (0,) * 9)
            return real_stat(path, *args, **kwargs)

        def no_open(path, *args, **kwargs):
            if os.fspath(path) == target:
                self.fail("a file that is not regular was opened")
            return real_open(path, *args, **kwargs)

        with mock.patch("os.stat", device_stat), mock.patch("builtins.open", no_open):
            found = repo.findings()
        self.assertIn(("warn", "read", "AGENTS.md", "cannot be read: it is not a regular file"),
                      [(f.level, f.check, f.file, f.message) for f in found])

    @unittest.skipUnless(hasattr(os, "mkfifo"), "no FIFO on this platform")
    def test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run(self):
        repo = self.repo({"CLAUDE.md": "@AGENTS.md\n"})
        os.mkfifo(os.path.join(repo.root, "AGENTS.md"))
        found = repo.findings()
        self.assertIn(("warn", "read", "AGENTS.md"), [(f.level, f.check, f.file) for f in found])

    def test_a_utf8_byte_order_mark_is_stripped_before_every_check(self):
        repo = self.repo({".cursor/rules/a.mdc": "﻿---\nalwaysApply: true\n---\nRule.\n",
                          "CLAUDE.md": "﻿@AGENTS.md\n", "AGENTS.md": "Rules.\n"})
        self.assertEqual(checks(repo.findings(), "error") + checks(repo.findings(), "warn"), [])

    def test_a_character_cut_at_the_limit_does_not_make_the_text_invalid(self):
        data = b"a" * (check_instructions.MAX_BYTES - 1) + "ż\n".encode("utf-8")
        repo = self.repo({"AGENTS.md": data})
        found = [(f.level, f.check, f.message) for f in repo.findings()]
        self.assertIn(("info", "read", "only the first 1048576 bytes were checked"), found)
        self.assertNotIn(("warn", "read", "not UTF-8 text; its content was not checked"), found)

    def test_text_that_is_not_utf8_is_reported_and_its_content_not_checked(self):
        text = "Read `gone/x.md`. IMPORTANT: a.\nIMPORTANT: b.\n"
        for label, data in (("utf-16", text.encode("utf-16")), ("utf-32", text.encode("utf-32")),
                            ("invalid", b"Read \xc3\x28 `gone/x.md`.\n")):
            with self.subTest(label):
                repo = self.repo({"CLAUDE.md": data})
                found = repo.findings()
                self.assertEqual([(f.level, f.check, f.message) for f in found],
                                 [("warn", "read", "not UTF-8 text; its content was not checked")])


class PrintedValues(CheckTestCase):
    def test_control_and_bidirectional_characters_are_escaped_and_long_values_cut(self):
        token = "gone‮\x07/x.md"
        long_token = "a/" * 150 + "x.md"
        repo = self.repo({"AGENTS.md": f"Read `{token}` and `{long_token}`.\n",
                          "odd‮dir/AGENTS.md": "Rules.\n"})
        code, out, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        self.assertNotIn("‮", out)
        self.assertNotIn("\x07", out)
        self.assertIn("gone\\u202e\\x07/x.md", out)
        self.assertIn("odd\\u202edir/AGENTS.md", out)
        self.assertIn(long_token[:199] + "…", out)
        self.assertNotIn(long_token, out)


class UnreadableFiles(CheckTestCase):
    def test_a_directory_named_agents_md_is_reported_and_the_run_goes_on(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n", "AGENTS.md/x.txt": "x\n"})
        found = [(f.level, f.check, f.file, f.message) for f in repo.findings()]
        self.assertIn(("warn", "read", "AGENTS.md", "cannot be read: it is a directory"), found)
        self.assertIn(("info", "size", "CLAUDE.md", "1 lines, 1 words"), found)

    def test_a_broken_link_is_reported(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n"})
        make_file_link(self, os.path.join(repo.root, "missing.md"), os.path.join(repo.root, "AGENTS.md"))
        found = [(f.level, f.check, f.file) for f in repo.findings()]
        self.assertIn(("warn", "read", "AGENTS.md"), found)

    def test_a_file_without_permission_is_reported(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "CLAUDE.md": "@AGENTS.md\n"})
        target = os.path.join(repo.root, "AGENTS.md")
        real_open = open

        def refuse(path, *args, **kwargs):
            if os.fspath(path) == target:
                raise PermissionError(13, "Permission denied", target)
            return real_open(path, *args, **kwargs)

        with mock.patch("builtins.open", refuse):
            found = [(f.level, f.check, f.file, f.message) for f in repo.findings()]
        self.assertIn(("warn", "read", "AGENTS.md", "cannot be read: Permission denied"), found)

    def test_a_file_gone_mid_run_is_reported_and_the_run_goes_on(self):
        repo = self.repo({"AGENTS.md": "Rules.\n"})
        with mock.patch.object(check_instructions, "instruction_files",
                               return_value=["AGENTS.md", "gone/AGENTS.md"]):
            found = [(f.level, f.check, f.file) for f in repo.findings()]
        self.assertIn(("warn", "read", "gone/AGENTS.md"), found)
        self.assertIn(("info", "size", "AGENTS.md"), found)

    def test_a_directory_that_cannot_be_listed_is_reported(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "locked/AGENTS.md": "x\n"})
        real_scandir = os.scandir

        def refuse(path="."):
            if os.path.basename(os.fspath(path)) == "locked":
                raise PermissionError(13, "Permission denied", os.fspath(path))
            return real_scandir(path)

        with mock.patch("os.scandir", refuse):
            found = [(f.level, f.check, f.file) for f in repo.findings()]
        self.assertIn(("info", "walk", "locked"), found)
        self.assertNotIn("locked/AGENTS.md", [file for _, _, file in found])


class CommandLine(CheckTestCase):
    def test_a_root_that_is_not_a_directory_exits_with_2(self):
        repo = self.repo({"AGENTS.md": "Rules.\n"})
        code, out, err = run_main([os.path.join(repo.root, "AGENTS.md")])
        self.assertEqual((code, out), (2, ""))
        self.assertIn("ROOT is not a directory", err)

    def test_a_file_that_is_not_a_readable_regular_file_exits_with_2(self):
        repo = self.repo({"AGENTS.md": "Rules.\n"})
        for path in (repo.root, os.path.join(repo.root, "missing.md")):
            with self.subTest(path=path):
                code, out, err = run_main(["--file", path])
                self.assertEqual((code, out), (2, ""))
                self.assertTrue(err.startswith("Error: --file"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run them to see them fail**

Run: `cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py instruction-files 2>&1 | grep -E "^(FAIL|ERROR):|^Ran|^FAILED" | sed 's/ (.*//' | sort | uniq -c`
Expected (planner, against the prototype script): `Ran 45 tests`, `FAILED (failures=11, errors=7, skipped=1)` — the ERRORs `test_a_broken_link_is_reported`, `test_a_character_cut_at_the_limit_does_not_make_the_text_invalid`, `test_a_file_gone_mid_run_is_reported_and_the_run_goes_on`, `test_a_file_that_is_not_a_readable_regular_file_exits_with_2` (two subtests), `test_a_file_without_permission_is_reported`, `test_only_the_first_mebibyte_is_read`; the FAILs `test_a_directory_link_or_junction_is_not_followed`, `test_a_directory_named_agents_md_is_reported_and_the_run_goes_on`, `test_a_directory_that_cannot_be_listed_is_reported`, `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`, `test_a_file_that_is_not_regular_is_not_opened`, `test_a_root_that_is_not_a_directory_exits_with_2`, `test_a_utf8_byte_order_mark_is_stripped_before_every_check`, `test_control_and_bidirectional_characters_are_escaped_and_long_values_cut`, `test_text_that_is_not_utf8_is_reported_and_its_content_not_checked` (three subtests). The skip is the FIFO test on Windows. (On a machine where links cannot be made, the link tests skip instead of failing; the skip names why.)

- [ ] **Step 3: Write the implementation** — replace `instruction-files/check_instructions.py` whole with:

```python
"""Mechanical checks of a repository's instruction files for agents.

Settles, without reading what the rules say, the checks of section 6 of principles.md, which lies
next to this script: paths that do not exist, `@path` imports that Claude Code loads into every
session or silently skips, Cursor rules that Cursor ignores, a root layout that hides `AGENTS.md`
from Claude Code, subdirectory `AGENTS.md` files Codex will not reach, skills one of the tools
cannot discover, emphasis spread over several rules, and the size of every file.

Usage, from anywhere:

    python -B <the-way>/instruction-files/check_instructions.py [ROOT] [--file PATH ...]

ROOT defaults to the current directory. --file adds an instruction file outside the repository,
such as the user's global file. Each finding is printed as `LEVEL check file:line message`; the
last line counts the findings by level. The exit code is 1 when there is an error, 2 when ROOT is
not a directory or a --file is not a readable regular file, else 0.

The files it reads are not the-way's, so it trusts none of them: it reads at most 1048576 bytes of
a file, opens only regular files, reads no file through a link that leads out of ROOT, follows no
link to a directory, and prints every value escaped and cut to 200 characters. It writes nothing
and starts no program.
"""

import argparse
import codecs
import os
import re
import stat
import sys
from dataclasses import dataclass

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".runs"}
MAIN_NAMES = {"AGENTS.md", "CLAUDE.md", "CLAUDE.local.md", "AGENTS.override.md"}
SKILL_DIRS = (".claude/skills", ".agents/skills", ".cursor/skills", ".codex/skills")
MAX_BYTES = 1048576
MAX_SHOWN = 200
EMPHASIS = re.compile(r"\b(IMPORTANT|YOU MUST|CRITICAL|MUST NOT|NEVER EVER)\b")
FENCE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN = re.compile(r"`([^`\n]+)`")
AT_IMPORT = re.compile(r"(?<![\w.@/\\])@([^\s`<>\"']+)")
TRAILING = ".,;:)!?]}"
EXTENSIONS = ("md", "mdc", "json", "jsonl", "js", "mjs", "cjs", "ts", "tsx", "jsx", "py", "toml",
              "yaml", "yml", "txt", "sh", "ps1", "bat", "cmd", "sql", "html", "css", "vue", "php",
              "go", "rs", "java", "kt", "rb", "lock", "ini", "cfg", "env", "xml", "csv")
FILE_LIKE = re.compile(r"\.(" + "|".join(EXTENSIONS) + r")$", re.IGNORECASE)
LINE_SUFFIX = re.compile(r":\d+(:\d+)?$")
BOMS_NOT_UTF8 = (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE, codecs.BOM_UTF16_LE,
                 codecs.BOM_UTF16_BE)


@dataclass(frozen=True)
class Finding:
    level: str  # error, warn or info
    check: str
    file: str
    line: int
    message: str


def shown(value):
    """VALUE as it may be printed: control and bidirectional-format characters escaped, and cut
    to MAX_SHOWN characters, the last of them `…`."""
    out = []
    for character in str(value):
        code = ord(character)
        if code < 0x20 or 0x7F <= code <= 0x9F:
            out.append("\\x%02x" % code)
        elif 0x202A <= code <= 0x202E or 0x2066 <= code <= 0x2069:
            out.append("\\u%04x" % code)
        else:
            out.append(character)
    text = "".join(out)
    return text if len(text) <= MAX_SHOWN else text[:MAX_SHOWN - 1] + "…"


def reason(error):
    """The reason an OSError gives, without the path it names."""
    return error.strerror or type(error).__name__


def inside(path, directory):
    """True when the real PATH lies in the real DIRECTORY or is it."""
    try:
        common = os.path.commonpath([path, directory])
    except ValueError:
        return False
    return os.path.normcase(common) == os.path.normcase(directory)


def is_instruction_name(rel, name):
    if name in MAIN_NAMES or rel.endswith(".claude/CLAUDE.md"):
        return True
    if "/.claude/rules/" in "/" + rel and name.endswith(".md"):
        return True
    if "/.cursor/rules/" in "/" + rel:
        return True
    return name == "SKILL.md" and any(("/" + d + "/") in "/" + rel for d in SKILL_DIRS)


def instruction_files(root, findings):
    """Every file under ROOT that an agent tool reads as instructions, as paths relative to ROOT.
    A link to a directory is not followed, a file reached through a link that leads out of ROOT
    is not listed, and a directory that cannot be listed is reported."""
    real_root = os.path.realpath(root)
    found = []

    def relative(path):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        return "" if rel == "." else rel

    def cannot_list(error):
        findings.append(Finding("info", "walk", relative(error.filename or root) or ".", 0,
                                f"a directory that cannot be listed: {reason(error)}"))

    for current, dirs, files in os.walk(root, onerror=cannot_list):
        rel_dir = relative(current)
        rel_dir = rel_dir + "/" if rel_dir else ""
        kept = []
        for name in sorted(dirs):
            full = os.path.join(current, name)
            if name in SKIP_DIRS:
                continue
            if os.path.islink(full) or os.path.isjunction(full):
                findings.append(Finding("info", "walk", rel_dir + name, 0,
                                        "a link to a directory, not followed"))
                continue
            if os.path.exists(os.path.join(full, ".git")):
                continue
            if name in MAIN_NAMES:
                findings.append(Finding("warn", "read", rel_dir + name, 0,
                                        "cannot be read: it is a directory"))
            kept.append(name)
        dirs[:] = kept
        for name in sorted(files):
            rel = rel_dir + name
            if not is_instruction_name(rel, name):
                continue
            full = os.path.join(current, name)
            if os.path.islink(full) and not inside(os.path.realpath(full), real_root):
                findings.append(Finding("info", "read", rel, 0,
                                        "a link out of the repository, not read"))
                continue
            found.append(rel)
    return found


def read_text(path, shown_as, findings):
    """The text of the regular file at PATH, its UTF-8 byte order mark removed, or None when it
    cannot be read or is no UTF-8 text; what stopped it is reported as a finding."""
    try:
        mode = os.stat(path).st_mode
    except OSError as error:
        findings.append(Finding("warn", "read", shown_as, 0, f"cannot be read: {reason(error)}"))
        return None
    if stat.S_ISDIR(mode):
        findings.append(Finding("warn", "read", shown_as, 0, "cannot be read: it is a directory"))
        return None
    if not stat.S_ISREG(mode):
        findings.append(Finding("warn", "read", shown_as, 0,
                                "cannot be read: it is not a regular file"))
        return None
    try:
        with open(path, "rb") as handle:
            data = handle.read(MAX_BYTES + 1)
    except OSError as error:
        findings.append(Finding("warn", "read", shown_as, 0, f"cannot be read: {reason(error)}"))
        return None
    cut = len(data) > MAX_BYTES
    if cut:
        data = data[:MAX_BYTES]
        findings.append(Finding("info", "read", shown_as, 0,
                                f"only the first {MAX_BYTES} bytes were checked"))
    if data.startswith(BOMS_NOT_UTF8):
        findings.append(Finding("warn", "read", shown_as, 0,
                                "not UTF-8 text; its content was not checked"))
        return None
    if data.startswith(codecs.BOM_UTF8):
        data = data[len(codecs.BOM_UTF8):]
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as error:
        if cut and error.start >= len(data) - 3:
            return data[:error.start].decode("utf-8")
        findings.append(Finding("warn", "read", shown_as, 0,
                                "not UTF-8 text; its content was not checked"))
        return None


def prose_lines(text):
    """(line number, line) for every line outside fenced code blocks."""
    inside_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            inside_fence = not inside_fence
            continue
        if not inside_fence:
            yield number, line


def looks_like_path(token):
    if not token or token.startswith(("-", "http://", "https://", "$")):
        return False
    if any(c in token for c in "*<>{}|$…") or token.endswith("()"):
        return False
    if token.startswith("/") and "/" not in token[1:] and "." not in token:
        return False  # a slash command such as /park
    first = re.split(r"[\\/]", token)[0]
    if "." in first and not first.startswith(".") and not FILE_LIKE.search(first):
        return False  # a domain such as github.com/someone
    if re.match(r"^[A-Za-z]:[\\/]", token) or token.startswith("~"):
        return True
    if " " in token:
        return False
    return "/" in token or "\\" in token or bool(FILE_LIKE.search(token))


def is_relative(token):
    return not (token.startswith(("~", "/", "\\")) or re.match(r"^[A-Za-z]:", token))


def resolve(token, file_dir, root):
    token = os.path.expanduser(LINE_SUFFIX.sub("", token).rstrip("/\\"))
    if os.path.isabs(token) or re.match(r"^[A-Za-z]:", token):
        return os.path.exists(token)
    return any(os.path.exists(os.path.join(base, token)) for base in (file_dir, root) if base)


def check_file(path, shown_as, root, findings, in_repo=True):
    """The per-file checks of one instruction file; returns its text, or None when it was not
    read."""
    text = read_text(path, shown_as, findings)
    if text is None:
        return None
    name = os.path.basename(path)
    file_dir = os.path.dirname(path)
    emphasised = []
    for number, line in prose_lines(text):
        for span in CODE_SPAN.findall(line):
            token = span.strip()
            if looks_like_path(token) and not resolve(token, file_dir, root):
                if not in_repo and is_relative(token):
                    findings.append(Finding(
                        "info", "dead-path", shown_as, number,
                        f"`{shown(token)}` is relative in a file outside the repository and does "
                        "not resolve from here"))
                else:
                    findings.append(Finding("warn", "dead-path", shown_as, number,
                                            f"`{shown(token)}` does not exist"))
        bare = CODE_SPAN.sub("", line)
        for match in AT_IMPORT.finditer(bare):
            token = match.group(1)
            if line.strip() == "@AGENTS.md" and name == "CLAUDE.md":
                continue
            if not ("." in token or "/" in token):
                continue
            if token[-1] in TRAILING:
                findings.append(Finding(
                    "error", "at-import", shown_as, number,
                    f"@{shown(token)} — a punctuation mark right after the path stops Claude Code "
                    "from loading it, without a warning"))
            else:
                findings.append(Finding(
                    "warn", "at-import", shown_as, number,
                    f"@{shown(token)} — Claude Code loads the whole file into every session; Codex "
                    "reads it as plain text; a pointer is a path in backticks"))
        if EMPHASIS.search(line):
            emphasised.append(number)
    if len(emphasised) > 1:
        findings.append(Finding("warn", "emphasis", shown_as, emphasised[0],
                                f"{len(emphasised)} emphasised lines — emphasis on one rule at most"))
    if name != "SKILL.md":
        findings.append(Finding("info", "size", shown_as, 0,
                                f"{len(text.splitlines())} lines, {len(text.split())} words"))
    return text


def check_cursor_rule(rel, text, findings):
    if not rel.endswith(".mdc"):
        findings.append(Finding("error", "cursor-rule", rel, 0,
                                "Cursor reads only .mdc files in .cursor/rules; this one is ignored"))
        return
    if text is None:
        return
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        findings.append(Finding("error", "cursor-rule", rel, 1,
                                "a Cursor rule without a YAML header is never attached"))


def check_layout(root, files, texts, findings):
    present = set(files)
    if "AGENTS.md" in present:
        claude = texts.get("CLAUDE.md")
        if claude is not None and "@AGENTS.md" not in [l.strip() for l in claude.splitlines()]:
            findings.append(Finding(
                "warn", "root-layout", "CLAUDE.md", 0,
                "CLAUDE.md stands beside AGENTS.md without an `@AGENTS.md` line, so Claude Code "
                "does not read AGENTS.md"))
        if "CLAUDE.local.md" in present:
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
            unpointed.append(skill_dir)
    if unpointed:
        findings.append(Finding(
            "info", "skill-dir", ".claude/skills", 0,
            f"{len(unpointed)} skills in .claude/skills have no pointer in AGENTS.md; Codex does "
            "not read .claude/skills, so point to the SKILL.md of each one Codex needs"))



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
    texts = {}
    seen = set()
    for rel in files:
        path = os.path.join(root, *rel.split("/"))
        seen.add(os.path.realpath(path))
        texts[rel] = check_file(path, rel, root, findings)
        if rel.startswith(".cursor/rules/") or "/.cursor/rules/" in rel:
            check_cursor_rule(rel, texts[rel], findings)
    for path in extra:
        if os.path.realpath(path) in seen:
            continue
        check_file(path, path, root, findings, in_repo=False)
    check_layout(root, files, texts, findings)
    return findings


def usage_error(message):
    print(f"Error: {shown(message)}", file=sys.stderr)
    return 2


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", nargs="?", default=None,
                        help="the repository; defaults to the current directory unless --file is given")
    parser.add_argument("--file", action="append", default=[],
                        help="an instruction file outside the repository")
    args = parser.parse_args(argv)
    root = args.root or (None if args.file else ".")
    if root is not None and not os.path.isdir(root):
        return usage_error(f"ROOT is not a directory: {root}")
    for path in args.file:
        try:
            if not stat.S_ISREG(os.stat(path).st_mode):
                return usage_error(f"--file is not a regular file: {path}")
            with open(path, "rb"):
                pass
        except OSError as error:
            return usage_error(f"--file cannot be read: {path}: {reason(error)}")
    findings = check(root, args.file)
    order = {"error": 0, "warn": 1, "info": 2}
    for f in sorted(findings, key=lambda f: (order[f.level], f.file, f.line)):
        print(f"{f.level.upper():5} {f.check} {shown(f.file)}:{f.line} {f.message}")
    counts = {level: sum(1 for f in findings if f.level == level) for level in order}
    print(f"{counts['error']} error, {counts['warn']} warn, {counts['info']} info")
    return 1 if counts["error"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

- [ ] **Step 4: Run the tests to see them pass, and the script on the-way**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B gate/run_tests.py instruction-files > $R/reports/check_3_tests_instruction_files.txt 2>&1; echo "instruction-files $?"; tail -1 $R/reports/check_3_tests_instruction_files.txt; python -B instruction-files/check_instructions.py . ; echo "exit $?"; python -B instruction-files/check_instructions.py instruction-files/SKILL.md; echo "exit $?"
```
Expected (planner, on a clone): `0`, `OK (skipped=1)` (45 tests); on the-way exactly

```text
WARN  dead-path AGENTS.md:20 `_zadania\` does not exist
INFO  skill-dir .claude/skills:0 12 skills in .claude/skills have no pointer in AGENTS.md; Codex does not read .claude/skills, so point to the SKILL.md of each one Codex needs
INFO  size AGENTS.md:0 21 lines, 187 words
INFO  size CLAUDE.md:0 1 lines, 1 words
0 error, 1 warn, 3 info
```
and exit 0 (the false `skill-dir` note on the twelve entry points of Task 2 goes in Task 5, fix B); for a file given as ROOT `Error: ROOT is not a directory: instruction-files/SKILL.md` on stderr and `exit 2`.

- [ ] **Step 5: Crafted-input review note (WAY-48)** — the task's reviewer confirms each row of spec §4.6 this task owns against a test above: directory link or junction and a loop (`test_a_directory_link_or_junction_is_not_followed`), a file link out of the repository (`test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`, with `--file` read through its link in `test_a_file_given_with_file_is_read_through_its_link`), a huge file (`test_only_the_first_mebibyte_is_read`), a non-regular file (`test_a_file_that_is_not_regular_is_not_opened`, `test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run`), BOM (`test_a_utf8_byte_order_mark_is_stripped_before_every_check`), other encodings (`test_text_that_is_not_utf8_is_reported_and_its_content_not_checked`), printed values (`test_control_and_bidirectional_characters_are_escaped_and_long_values_cut`), unreadable files (`UnreadableFiles`), an unlistable directory (`test_a_directory_that_cannot_be_listed_is_reported`), bad arguments (`CommandLine`). The network row and the 1 MiB paragraph row belong to Task 4, the pointed-file row to Task 5.

- [ ] **Step 6: Commit**

```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && S="Claude-Session: https://claude.ai/code/session_01NcSfTaYPmi5KV9LwkzJLjZ" && git commit -m "fix(instruction-files): Read only regular UTF-8 files inside the root, and report what cannot be read" -m "$S" -- instruction-files/check_instructions.py instruction-files/test_check_instructions.py
```

---

