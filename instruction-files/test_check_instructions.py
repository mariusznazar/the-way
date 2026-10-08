"""Tests of the mechanical checks of instruction files: each check fires on a repository broken on
purpose and stays silent on a sound one, and crafted input neither reaches past the files given
nor stops the run.

Every fixture is built in a temporary directory, and the home directory is an empty temporary
one, so no file of this repository or of the machine takes part.

Run from the root of the-way: python -B gate/run_tests.py instruction-files
"""

import builtins
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


NETWORK = "\\\\192.0.2.1\\share\\x.md"  # the network path \\192.0.2.1\share\x.md


def guard_network_paths(test):
    """Fails the test when a file-system call of the script receives a network path."""
    def guard(name, real):
        def checked(path, *args, **kwargs):
            if isinstance(path, str) and path.replace("/", "\\").startswith(("\\\\", "\\??\\")):
                test.fail(f"{name} received a network path")
            return real(path, *args, **kwargs)
        return checked

    for owner, attribute in ((os, "stat"), (os, "lstat"), (os, "scandir"), (os, "readlink"),
                             (os.path, "realpath"), (os.path, "exists"), (os.path, "lexists"),
                             (os.path, "isdir"), (os.path, "isfile"), (os.path, "islink"),
                             (os.path, "isjunction"), (builtins, "open")):
        test.enterContext(mock.patch.object(owner, attribute,
                                            guard(attribute, getattr(owner, attribute))))


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


class NetworkPaths(CheckTestCase):
    def test_a_link_to_a_network_path_is_never_looked_up(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n"})
        make_file_link(self, NETWORK, os.path.join(repo.root, "AGENTS.md"))
        make_file_link(self, NETWORK, os.path.join(repo.root, "notes.txt"))
        guard_network_paths(self)
        code, _, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        found = [(f.level, f.check, f.file, f.message) for f in repo.findings()]
        self.assertIn(("info", "read", "AGENTS.md", "a link out of the repository, not read"), found)
        self.assertNotIn("notes.txt", [file for _, _, file, _ in found])

    def test_a_chain_that_reaches_a_network_path_through_a_link_is_not_followed(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n"})
        make_file_link(self, NETWORK, os.path.join(repo.root, "mid.md"))
        make_file_link(self, "mid.md", os.path.join(repo.root, "AGENTS.md"))
        guard_network_paths(self)
        found = [(f.level, f.check, f.file) for f in repo.findings()]
        self.assertIn(("info", "read", "AGENTS.md"), found)

    def test_a_nested_repository_whose_git_is_a_link_is_skipped_without_a_lookup(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "sub/AGENTS.md": "IMPORTANT: a.\nIMPORTANT: b.\n"})
        make_file_link(self, NETWORK, os.path.join(repo.root, "sub", ".git"))
        guard_network_paths(self)
        found = repo.findings()
        self.assertEqual([f.file for f in found if f.check == "size"], ["AGENTS.md"])
        self.assertNotIn("emphasis", checks(found))

    def test_a_chain_of_two_links_that_leaves_the_repository_is_not_read(self):
        repo = self.repo({}, outside={"secret.md": "Read `MARKER-SECRET-9/x.md`.\n"})
        make_file_link(self, os.path.join(repo.base, "secret.md"), os.path.join(repo.root, "mid.md"))
        make_file_link(self, "mid.md", os.path.join(repo.root, "AGENTS.md"))
        self.assertEqual([(f.level, f.check, f.file, f.message) for f in repo.findings()],
                         [("info", "read", "AGENTS.md", "a link out of the repository, not read")])
        code, out, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        self.assertNotIn("MARKER-SECRET-9", out)

    def test_a_chain_longer_than_the_hop_limit_is_not_read(self):
        names = [f"h{number}.md" for number in range(1, check_instructions.LINK_HOPS + 1)]
        repo = self.repo({"target.md": "Rules.\n"})
        make_file_link(self, names[0], os.path.join(repo.root, "AGENTS.md"))
        for here, there in zip(names, names[1:] + ["target.md"]):
            make_file_link(self, there, os.path.join(repo.root, here))
        self.assertEqual([(f.level, f.check, f.file, f.message) for f in repo.findings()],
                         [("info", "read", "AGENTS.md", "a link out of the repository, not read")])

    def test_a_chain_that_ends_inside_the_repository_is_read(self):
        repo = self.repo({"target.md": "IMPORTANT: a.\nIMPORTANT: b.\n"})
        make_file_link(self, "target.md", os.path.join(repo.root, "mid.md"))
        make_file_link(self, "mid.md", os.path.join(repo.root, "AGENTS.md"))
        self.assertIn("emphasis", checks(repo.findings(), "warn"))


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
        repo = self.repo({".cursor/rules/a.mdc": "\N{ZERO WIDTH NO-BREAK SPACE}---\nalwaysApply: true\n---\nRule.\n",
                          "CLAUDE.md": "\N{ZERO WIDTH NO-BREAK SPACE}@AGENTS.md\n", "AGENTS.md": "Rules.\n"})
        self.assertEqual(checks(repo.findings(), "error") + checks(repo.findings(), "warn"), [])

    def test_a_character_cut_at_the_limit_does_not_make_the_text_invalid(self):
        data = b"a" * (check_instructions.MAX_BYTES - 1) + "ż\n".encode("utf-8")
        repo = self.repo({"AGENTS.md": data})
        found = [(f.level, f.check, f.message) for f in repo.findings()]
        self.assertIn(("info", "read", "only the first 1048576 bytes were checked"), found)
        self.assertNotIn(("warn", "read", "not UTF-8 text; its content was not checked"), found)

    def test_an_invalid_byte_near_the_limit_is_not_taken_for_a_split_character(self):
        data = b"a" * (check_instructions.MAX_BYTES - 2) + b"\xff\n" + b"tail\n"
        repo = self.repo({"AGENTS.md": data})
        found = [(f.level, f.check, f.message) for f in repo.findings()]
        self.assertIn(("warn", "read", "not UTF-8 text; its content was not checked"), found)

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
        token = "gone\N{RIGHT-TO-LEFT OVERRIDE}\x07/x.md"
        long_token = "a/" * 150 + "x.md"
        repo = self.repo({"AGENTS.md": f"Read `{token}` and `{long_token}`.\n",
                          "odd\N{RIGHT-TO-LEFT OVERRIDE}dir/AGENTS.md": "Rules.\n"})
        code, out, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        self.assertNotIn("\N{RIGHT-TO-LEFT OVERRIDE}", out)
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

    def test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup(self):
        guard_network_paths(self)
        for arguments in ([NETWORK], ["--file", NETWORK]):
            with self.subTest(arguments=arguments):
                code, out, err = run_main(arguments)
                self.assertEqual((code, out), (2, ""))
                self.assertIn("network path", err)

    def test_a_file_that_is_not_a_readable_regular_file_exits_with_2(self):
        repo = self.repo({"AGENTS.md": "Rules.\n"})
        for path in (repo.root, os.path.join(repo.root, "missing.md")):
            with self.subTest(path=path):
                code, out, err = run_main(["--file", path])
                self.assertEqual((code, out), (2, ""))
                self.assertTrue(err.startswith("Error: --file"))


if __name__ == "__main__":
    unittest.main()
