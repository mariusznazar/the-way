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
import re
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
NETWORK_SPELLINGS = (
    "\\\\host\\share\\x.md",
    "//host/share/x.md",
    "/\\host\\share\\x.md",
    "\\/host/share/x.md",
    "\\\\?\\UNC\\host\\share\\x.md",
    "\\\\.\\pipe\\x.md",
    "\\??\\UNC\\host\\share\\x.md",
)
# What a network spelling becomes on its way to the file system, however it was joined or turned.
NETWORK_TRACE = re.compile(r"host[\\/]share|[\\/]pipe[\\/]")


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


WINDOWS_ONLY = unittest.skipUnless(os.name == "nt", "network paths are looked up only on Windows")
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


class SentenceSaysNotLoaded(CheckTestCase):
    def test_a_file_path_in_a_sentence_wrapped_over_two_lines_is_only_noted(self):
        repo = self.repo({"AGENTS.md": "The old guide `docs/old-guide.md` is\nnot read by any tool.\n"})
        found = dead(repo.findings())
        self.assertEqual([(f.level, f.line) for f in found], [("info", 1)])
        self.assertIn("named in a sentence saying it does not load or exist", found[0].message)

    def test_the_memory_sentence_is_only_noted(self):
        text = ("Który katalog pamięci sesja faktycznie widzi (globalny `~\\.claude\\memory\\` nie\n"
                "ładuje się do żadnej), co płaci się indeksem w każdej sesji.\n")
        repo = self.repo({"AGENTS.md": text}, outside={"global/CLAUDE.md": text})
        found = dead(repo.findings(extra=[os.path.join(repo.base, "global", "CLAUDE.md")]))
        self.assertEqual(sorted((f.level, f.line) for f in found), [("info", 1), ("info", 1)])

    def test_dead_paths_in_sentences_without_the_phrases_stay_warnings(self):
        repo = self.repo({"AGENTS.md": "Read `docs/gone.md` and the notes in `notes/gone/`.\n"
                                       "They load in every session. The cache does not load.\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["warn", "warn"])

    def test_a_sentence_in_one_list_item_does_not_reach_the_next(self):
        repo = self.repo({"AGENTS.md": "- The cache does not load\n- Read `docs/gone.md`\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["warn"])

    def test_a_near_miss_of_a_phrase_keeps_a_dead_path_a_warning(self):
        for sentence in ("The page `docs/gone.md` is not ready.",
                         "The page `docs/gone.md` is not readable.",
                         "The page `docs/gone.md` does not readily open.",
                         "Nie czytaj tego pliku, otwórz `docs/zasady/styl.md`."):
            with self.subTest(sentence=sentence):
                repo = self.repo({"AGENTS.md": sentence + "\n"})
                self.assertEqual([f.level for f in dead(repo.findings())], ["warn"])

    def test_the_prefix_phrase_still_matches_every_ending(self):
        repo = self.repo({"AGENTS.md": "Plik `docs/stary.md` nie jest wczytywany.\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["info"])

    def test_crlf_line_ends_still_join_a_wrapped_sentence(self):
        repo = self.repo({"AGENTS.md": b"The old guide `docs/old-guide.md` is\r\nnot read by any tool.\r\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["info"])

    def test_each_sentence_is_tested_once_whatever_the_number_of_paths(self):
        sentences = 300
        lines = []
        for index in range(0, sentences, 2):
            lines.append(" ".join(
                "See " + " ".join(f"`d{number}/p{path}.md`" for path in range(10)) + "."
                for number in (index, index + 1)))
        repo = self.repo({"AGENTS.md": "\n".join(lines) + "\n"})
        with mock.patch.object(check_instructions, "negates_loading",
                               wraps=check_instructions.negates_loading) as tested:
            found = dead(repo.findings())
        self.assertEqual(len(found), sentences * 10)
        self.assertEqual(tested.call_count, sentences)


class OutsideRepository(CheckTestCase):
    def outside_findings(self, text, files=None):
        repo = self.repo(files or {"AGENTS.md": "Rules.\n"}, outside={"global/CLAUDE.md": text})
        return dead(repo.findings(extra=[os.path.join(repo.base, "global", "CLAUDE.md")]))

    def test_a_dead_path_of_two_segments_is_a_warning(self):
        found = self.outside_findings("Repositories are listed in `scripts/locations.json`.\n")
        self.assertEqual([f.level for f in found], ["warn"])

    def test_a_name_of_one_segment_is_only_noted(self):
        found = self.outside_findings("Copy `full_template.md` with `references\\` into `.cursor/`.\n")
        self.assertEqual([f.level for f in found], ["info", "info", "info"])

    def test_a_path_that_exists_from_the_home_directory_or_the_root_is_sound(self):
        write(self.home, "scripts/locations.json", "{}\n")
        found = self.outside_findings("Read `scripts/locations.json` and `docs/a.md`.\n",
                                      {"AGENTS.md": "Rules.\n", "docs/a.md": "x\n"})
        self.assertEqual(found, [])

    def test_a_windows_path_of_two_segments_is_a_warning(self):
        found = self.outside_findings("Decisions stand in `docs\\adr\\`.\n")
        self.assertEqual([f.level for f in found], ["warn"])

    def test_files_alone_are_checked_from_the_home_directory_too(self):
        repo = self.repo({}, outside={"g/CLAUDE.md": "Read `scripts/locations.json`.\n"})
        found = check_instructions.check(None, [os.path.join(repo.base, "g", "CLAUDE.md")])
        self.assertEqual([f.level for f in dead(found)], ["warn"])


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

    def test_crlf_line_ends_keep_the_first_line_sound(self):
        repo = self.repo({"CLAUDE.md": b"@AGENTS.md\r\nNotes.\r\n", "AGENTS.md": "Rules.\n"})
        self.assertEqual([f for f in repo.findings() if f.check in ("root-layout", "at-import")], [])

    def test_agents_import_under_a_heading_is_one_warning_of_the_layout(self):
        repo = self.repo({"CLAUDE.md": "# Claude\n@AGENTS.md\n", "AGENTS.md": "Rules.\n"})
        found = [(f.check, f.level, f.line, f.message) for f in repo.findings()
                 if f.file == "CLAUDE.md" and f.check != "size"]
        self.assertEqual(found, [("root-layout", "warn", 2,
                                  "`@AGENTS.md` alone is not its first line")])

    def test_agents_import_with_no_agents_md_beside_it_is_a_warning_on_any_line(self):
        for text, line in (("@AGENTS.md\n", 1), ("# Claude\n\nRules.\n@AGENTS.md\n", 4)):
            with self.subTest(line=line):
                repo = self.repo({"CLAUDE.md": text})
                found = [f for f in repo.findings() if f.check == "at-import"]
                self.assertEqual([(f.level, f.line) for f in found], [("warn", line)])
                self.assertIn("imports a file that is not there", found[0].message)


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

    def test_the_agents_skills_warning_says_the_tool_does_not_document_it(self):
        repo = self.repo({".agents/skills/x/SKILL.md": SKILL})
        found = [f for f in repo.findings() if f.check == "skill-dir" and f.level == "warn"]
        self.assertIn("not documented as read by Claude Code", found[0].message)
        self.assertIn("a copy in .claude/skills", found[0].message)

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

    def test_a_git_link_counts_as_a_nested_repository_without_being_followed(self):
        repo = self.repo({"AGENTS.md": "Read `dir/a.md`.\n", "dir/a.md": DEFECTS})
        make_bait_link(self, repo.base, os.path.join(repo.root, "dir", ".git"))
        real = os.path.exists

        def exists(path):
            if str(path).endswith(".git"):
                self.fail("exists was called on a .git entry")
            return real(path)

        self.enterContext(mock.patch.object(check_instructions.os.path, "exists", exists))
        self.assertEqual([f.file for f in repo.findings() if f.file != "AGENTS.md"], [])

    def test_a_path_with_a_nul_is_skipped_without_a_traceback(self):
        repo = self.repo({"AGENTS.md": "Read `guide/a\x00.md`.\n", "guide/a.md": DEFECTS})
        code, out, err = run_main([repo.root])
        self.assertEqual((code, err), (0, ""))
        self.assertNotIn("guide/a.md:", out)

    def test_a_file_that_is_a_link_into_a_skipped_directory_is_not_read(self):
        repo = self.repo({"AGENTS.md": "Read `inside.md`.\n", "node_modules/pkg/a.md": DEFECTS})
        make_file_link(self, os.path.join(repo.root, "node_modules", "pkg", "a.md"),
                       os.path.join(repo.root, "inside.md"))
        self.assertEqual([f for f in repo.findings() if f.file != "AGENTS.md"], [])

    def test_a_file_that_is_a_link_into_a_nested_repository_is_not_read(self):
        repo = self.repo({"AGENTS.md": "Read `inside.md`.\n", "sub/.git": "gitdir: x\n",
                          "sub/a.md": DEFECTS})
        make_file_link(self, os.path.join(repo.root, "sub", "a.md"),
                       os.path.join(repo.root, "inside.md"))
        self.assertEqual([f for f in repo.findings() if f.file != "AGENTS.md"], [])

    @WINDOWS_ONLY
    def test_a_pointed_network_path_is_noted_and_never_looked_up(self):
        repo = self.repo({"AGENTS.md": f"Read `{NETWORK}` and `{NETWORK.replace(chr(92), '/')}`.\n"})
        guard_network_paths(self)
        found = repo.findings()
        self.assertEqual([f.file for f in found if f.file != "AGENTS.md"], [])
        self.assertEqual([(f.level, f.line) for f in dead(found)], [("info", 1), ("info", 1)])
        self.assertTrue(all("network path, not checked" in f.message for f in dead(found)))

    @WINDOWS_ONLY
    def test_a_pointed_file_that_is_a_link_to_a_network_path_is_not_followed(self):
        repo = self.repo({"AGENTS.md": "Read `inside.md`.\n"})
        link = os.path.join(repo.root, "inside.md")
        make_bait_link(self, repo.base, link)
        pretend_target(self, link, NETWORK)
        guard_network_paths(self)
        self.assertEqual([f for f in repo.findings() if f.file != "AGENTS.md"], [])


class NetworkShapesOffWindows(CheckTestCase):
    """The platform decision is two module values, patched here; no lookup reaches a network-shaped
    path."""

    def platform(self, name):
        self.enterContext(mock.patch.object(check_instructions, "WINDOWS", False))
        self.enterContext(mock.patch.object(check_instructions, "PLATFORM", name))
        self.guard()

    def guard(self):
        def shaped(path):
            text = str(path).replace("\\", "/")
            return (text.startswith("//") and not text.startswith("///")) or \
                text.startswith(("/net/", "/Network/"))

        def guarded(name, real):
            def checked(path, *args, **kwargs):
                if isinstance(path, str) and shaped(path):
                    self.fail(f"{name} received a network-shaped path")
                return real(path, *args, **kwargs)
            return checked

        for owner, attribute in ((os, "stat"), (os, "lstat"), (os, "scandir"), (os, "readlink"),
                                 (os.path, "realpath"), (os.path, "exists"), (os.path, "lexists"),
                                 (os.path, "isdir"), (os.path, "isfile"), (os.path, "islink"),
                                 (builtins, "open")):
            self.enterContext(mock.patch.object(owner, attribute,
                                                guarded(attribute, getattr(owner, attribute))))

    def levels(self, token):
        repo = self.repo({"AGENTS.md": f"Read `{token}`.\n"})
        return [(f.level, f.message) for f in dead(repo.findings())]

    def assert_network(self, token):
        found = self.levels(token)
        self.assertEqual([level for level, _ in found], ["info"], token)
        self.assertIn("network path, not checked", found[0][1])

    def test_two_leading_slashes_are_a_network_path_on_linux(self):
        self.platform("linux")
        self.assert_network("//host/share/x.md")

    def stub_lookup(self):
        """Replaces `lexists` with a stub that records its argument and finds nothing."""
        calls = []

        def lexists(path):
            calls.append(str(path))
            return False

        self.enterContext(mock.patch.object(os.path, "lexists", lexists))
        return calls

    def test_three_leading_slashes_or_one_are_not(self):
        self.platform("linux")
        calls = self.stub_lookup()
        for token, trace in (("///host/x.md", "host"), ("/host/x.md", "host")):
            calls.clear()
            self.assertEqual([level for level, _ in self.levels(token)], ["warn"], token)
            self.assertTrue(any(trace in call and "x.md" in call for call in calls), token)

    def test_cygwin_and_msys_are_judged_like_windows(self):
        for name in ("cygwin", "msys"):
            self.platform(name)
            for token in ("\\\\host\\share\\x.md", "//host/share/x.md"):
                self.assert_network(token)

    def test_net_and_network_are_mount_points_of_macos_only(self):
        self.platform("darwin")
        self.assert_network("/net/host/x.md")
        self.assert_network("/Network/Servers/x.md")
        self.platform("linux")
        self.assertEqual([level for level, _ in self.levels("/net/host/x.md")], ["warn"])

    def test_a_network_shaped_root_or_file_is_a_usage_error(self):
        for name, token in (("linux", "//host/share"), ("cygwin", "\\\\host\\share"),
                            ("darwin", "/Network/x")):
            with self.subTest(platform=name):
                self.platform(name)
                self.assertEqual(run_main([token])[0], 2)
                self.assertEqual(run_main(["--file", token])[0], 2)

    def test_a_mapped_drive_letter_is_looked_up(self):
        self.platform("linux")
        calls = self.stub_lookup()
        self.assertEqual([level for level, _ in self.levels("Z:/share/x.md")], ["warn"])
        self.assertTrue(any("share" in call and "x.md" in call for call in calls))


class NamesThroughLinks(CheckTestCase):
    def forbid_exists_under(self, *links):
        real = os.path.exists
        prefixes = tuple(os.path.normcase(os.path.normpath(link)) for link in links)

        def exists(path):
            if os.path.normcase(os.path.normpath(str(path))).startswith(prefixes):
                self.fail("exists followed a link")
            return real(path)

        self.enterContext(mock.patch.object(check_instructions.os.path, "exists", exists))

    @WINDOWS_ONLY
    def test_a_token_naming_a_link_to_a_network_path_is_not_looked_up(self):
        repo = self.repo({"AGENTS.md": "Read `linknet.md`.\n"})
        link = os.path.join(repo.root, "linknet.md")
        make_bait_link(self, repo.base, link)
        pretend_target(self, link, NETWORK)
        guard_network_paths(self)
        self.forbid_exists_under(link)
        self.assertEqual(dead(repo.findings()), [])

    def test_a_token_through_a_directory_link_is_not_looked_up_through_it(self):
        repo = self.repo({"AGENTS.md": "Read `via/x.md`.\n"})
        target = os.path.join(repo.base, "elsewhere")
        write(repo.base, "elsewhere/x.md", "Text.\n")
        link = os.path.join(repo.root, "via")
        make_directory_link(self, target, link)
        self.forbid_exists_under(link)
        self.assertEqual(dead(repo.findings()), [])

    @WINDOWS_ONLY
    def test_no_spelling_of_a_path_through_a_link_to_a_network_path_is_looked_up(self):
        repo = self.repo({})
        link = os.path.join(repo.root, "via")
        make_bait_link(self, repo.base, link)
        pretend_target(self, link, NETWORK)
        absolute = os.path.join(repo.root, "via", "x.md").replace("\\", "/")
        write(repo.root, "AGENTS.md", f"Read `via/x.md`, `via\\x.md` and `{absolute}`.\n")
        prefix = os.path.normcase(link) + os.sep
        for name in ("lstat", "stat"):
            real = getattr(os, name)

            def spy(path, *args, _real=real, _name=name, **kwargs):
                if os.path.normcase(os.path.normpath(str(path))).startswith(prefix):
                    self.fail(f"{_name} continued past a link")
                return _real(path, *args, **kwargs)

            self.enterContext(mock.patch.object(os, name, spy))
        self.forbid_exists_under(link)
        self.assertEqual(dead(repo.findings()), [])

    def reached_through_a_link(self, repo, rel):
        """The path of REL (inside `real/` of the repository's temporary directory) as seen through
        the directory link `jn` that points to `real`."""
        make_directory_link(self, os.path.join(repo.base, "real"), os.path.join(repo.base, "jn"))
        return os.path.join(repo.base, "jn", *rel.split("/"))

    def test_a_repository_reached_through_a_link_above_its_root_is_still_checked(self):
        repo = self.repo({})
        write(repo.base, "real/repo/AGENTS.md", "Read `docs/gone.md`.\n\n@missing.md\n")
        root = os.path.dirname(self.reached_through_a_link(repo, "repo/AGENTS.md"))
        found = [(f.check, f.level, f.line) for f in check_instructions.check(root)
                 if f.check in ("dead-path", "at-import")]
        self.assertEqual(sorted(found), [("at-import", "warn", 3), ("dead-path", "warn", 1)])

    def test_a_file_given_with_file_through_a_link_above_it_is_still_checked(self):
        repo = self.repo({})
        write(repo.base, "real/global.md", "Read `docs/gone.md`.\n")
        path = self.reached_through_a_link(repo, "global.md")
        found = [(f.check, f.level) for f in check_instructions.check(None, [path])
                 if f.check == "dead-path"]
        self.assertEqual(found, [("dead-path", "warn")])

    def test_a_token_naming_nothing_is_still_a_dead_path(self):
        repo = self.repo({"AGENTS.md": "Read `gone/x.md`.\n"})
        self.assertEqual([f.level for f in dead(repo.findings())], ["warn"])


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


@unittest.skipUnless(os.name == "nt", "network paths are looked up only on Windows")
class NetworkTokens(CheckTestCase):
    """A network path in a file under review never reaches the file system: on Windows a lookup of
    one reaches the network."""

    FILE_SYSTEM_CALLS = ("os.stat", "os.lstat", "os.scandir", "os.path.exists", "os.path.isfile",
                         "os.path.isdir", "os.path.islink", "os.path.isjunction",
                         "os.path.realpath", "builtins.open")

    def no_network_lookup(self):
        stack = contextlib.ExitStack()
        for name in self.FILE_SYSTEM_CALLS:
            module, attribute = name.rsplit(".", 1)
            real = getattr({"os": os, "os.path": os.path, "builtins": builtins}[module], attribute)

            def guarded(*args, _real=real, _name=name, **kwargs):
                if args and isinstance(args[0], (str, os.PathLike)):
                    if NETWORK_TRACE.search(os.fspath(args[0])):
                        self.fail(f"{_name} was given {os.fspath(args[0])!r}")
                return _real(*args, **kwargs)

            stack.enter_context(mock.patch(name, guarded))
        return stack

    def test_no_spelling_of_a_network_path_reaches_the_file_system(self):
        text = "".join(f"Read `{token}`.\n\nSee @{token} now\n\n" for token in NETWORK_SPELLINGS)
        repo = self.repo({"AGENTS.md": text, "CLAUDE.md": "@AGENTS.md\n" + text},
                         outside={"global.md": text})
        with self.no_network_lookup():
            found = repo.findings(extra=[os.path.join(repo.base, "global.md")])
        noted = [f for f in found if f.level == "info" and "network path, not checked" in f.message]
        self.assertEqual(len(noted), len(NETWORK_SPELLINGS) * 2 * 3)
        self.assertEqual([f for f in found if f.check in ("dead-path", "at-import")
                          and f.level != "info"], [])


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


def pretend_target(test, link, target):
    """Makes os.readlink report TARGET for LINK, whatever the link really points to. The tests of
    network paths use it: the link points to a local file, so nothing here reaches a network, and a
    script that followed the link would read that file."""
    real = os.readlink

    def readlink(path, *args, **kwargs):
        if os.fspath(path) == link:
            return target
        return real(path, *args, **kwargs)

    test.enterContext(mock.patch.object(check_instructions.os, "readlink", readlink))


POSIX_ONLY = unittest.skipUnless(os.name == "posix", "needs the real path of a link, as on POSIX")


def make_bait_link(test, base, link):
    """Makes LINK a file link to a local path in BASE, and only then a directory at that path. The
    link is a file link that points to a directory: a script that follows it, even only to
    classify it, sees a directory and reports "a link to a directory"."""
    target = os.path.join(base, "bait-" + str(len(os.listdir(base))))
    make_file_link(test, target, link)
    os.mkdir(target)


@WINDOWS_ONLY
class NetworkPaths(CheckTestCase):
    def test_a_link_to_a_network_path_is_never_looked_up(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n"})
        for name in ("AGENTS.md", "notes.txt"):
            link = os.path.join(repo.root, name)
            make_bait_link(self, repo.base, link)
            pretend_target(self, link, NETWORK)
        guard_network_paths(self)
        code, out, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        self.assertNotIn("a link to a directory", out)
        found = [(f.level, f.check, f.file, f.message) for f in repo.findings()]
        self.assertIn(("info", "read", "AGENTS.md", "a link out of the repository, not read"), found)
        self.assertNotIn("notes.txt", [file for _, _, file, _ in found])

    def test_a_chain_that_reaches_a_network_path_through_a_link_is_not_followed(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n"})
        mid = os.path.join(repo.root, "mid.md")
        make_bait_link(self, repo.base, mid)
        pretend_target(self, mid, NETWORK)
        make_file_link(self, "mid.md", os.path.join(repo.root, "AGENTS.md"))
        guard_network_paths(self)
        found = [(f.level, f.check, f.file, f.message) for f in repo.findings()]
        self.assertIn(("info", "read", "AGENTS.md", "a link out of the repository, not read"), found)
        self.assertNotIn("walk", checks(repo.findings()))

    def test_a_nested_repository_whose_git_is_a_link_is_skipped_without_a_lookup(self):
        repo = self.repo({"AGENTS.md": "Rules.\n", "sub/AGENTS.md": "IMPORTANT: a.\nIMPORTANT: b.\n"})
        link = os.path.join(repo.root, "sub", ".git")
        make_bait_link(self, repo.base, link)
        pretend_target(self, link, NETWORK)
        guard_network_paths(self)
        found = repo.findings()
        self.assertEqual([f.file for f in found if f.check == "size"], ["AGENTS.md"])
        self.assertNotIn("emphasis", checks(found))

    def test_a_network_path_given_as_root_or_file_exits_with_2_without_a_lookup(self):
        guard_network_paths(self)
        for arguments in ([NETWORK], ["--file", NETWORK]):
            with self.subTest(arguments=arguments):
                code, out, err = run_main(arguments)
                self.assertEqual((code, out), (2, ""))
                self.assertIn("network path", err)


class LinkChains(CheckTestCase):
    def test_a_chain_of_two_links_that_leaves_the_repository_is_not_read(self):
        repo = self.repo({}, outside={"secret.md": "Read `MARKER-SECRET-9/x.md`.\n"})
        make_file_link(self, os.path.join(repo.base, "secret.md"), os.path.join(repo.root, "mid.md"))
        make_file_link(self, "mid.md", os.path.join(repo.root, "AGENTS.md"))
        self.assertEqual([(f.level, f.check, f.file, f.message) for f in repo.findings()],
                         [("info", "read", "AGENTS.md", "a link out of the repository, not read")])
        code, out, _ = run_main([repo.root])
        self.assertEqual(code, 0)
        self.assertNotIn("MARKER-SECRET-9", out)

    @WINDOWS_ONLY
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

    @POSIX_ONLY
    def test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does(self):
        repo = self.repo({}, outside={"a/b/keep.txt": "x\n", "a/secret.md": "Read `MARKER-SECRET-9/x.md`.\n"})
        make_directory_link(self, os.path.join(repo.base, "a", "b"), os.path.join(repo.root, "d"))
        make_file_link(self, "d/../secret.md", os.path.join(repo.root, "AGENTS.md"))
        found = [(f.level, f.check, f.file, f.message) for f in repo.findings() if f.file != "d"]
        self.assertEqual(found, [("info", "read", "AGENTS.md", "a link out of the repository, not read")])

    @POSIX_ONLY
    def test_an_absolute_link_out_of_the_repository_is_not_read(self):
        repo = self.repo({}, outside={"secret.md": "Read `MARKER-SECRET-9/x.md`.\n"})
        make_file_link(self, os.path.join(repo.base, "secret.md"), os.path.join(repo.root, "AGENTS.md"))
        self.assertEqual([(f.level, f.check, f.file) for f in repo.findings()],
                         [("info", "read", "AGENTS.md")])

    @POSIX_ONLY
    def test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on(self):
        repo = self.repo({"CLAUDE.md": "Rules.\n"})
        make_file_link(self, "AGENTS.md", os.path.join(repo.root, "AGENTS.md"))
        found = [(f.level, f.check, f.file, f.message) for f in repo.findings()]
        self.assertTrue(any(f[:3] == ("warn", "read", "AGENTS.md") and f[3].startswith("cannot be read: ")
                            for f in found))
        self.assertIn(("info", "size", "CLAUDE.md", "1 lines, 1 words"), found)

    @POSIX_ONLY
    def test_every_directory_link_is_reported_wherever_it_points(self):
        repo = self.repo({"inner/x.txt": "x\n"}, outside={"elsewhere/x.txt": "x\n"})
        make_directory_link(self, os.path.join(repo.base, "elsewhere"), os.path.join(repo.root, "out"))
        make_directory_link(self, os.path.join(repo.root, "inner"), os.path.join(repo.root, "in"))
        found = sorted((f.level, f.check, f.file, f.message) for f in repo.findings())
        self.assertEqual(found, [("info", "walk", "in", "a link to a directory, not followed"),
                                 ("info", "walk", "out", "a link to a directory, not followed")])


class DeepTree(CheckTestCase):
    def test_a_tree_deeper_than_the_recursion_limit_does_not_stop_the_run(self):
        self.addCleanup(sys.setrecursionlimit, sys.getrecursionlimit())
        sys.setrecursionlimit(200)  # low enough that a few hundred levels are deeper than it
        depth = 300
        repo = self.repo({"AGENTS.md": "Rules.\n"})
        self.addCleanup(os.chdir, os.getcwd())
        os.chdir(repo.root)
        try:
            for _ in range(depth):
                os.mkdir("d")
                os.chdir("d")
            with open("AGENTS.md", "w") as handle:
                handle.write("Deep.\n")
        except OSError as error:
            self.skipTest(f"a tree this deep cannot be built here: {error}")
        finally:
            os.chdir(repo.base)
        deepest = "/".join(["d"] * depth + ["AGENTS.md"])
        self.assertIn(deepest, check_instructions.instruction_files(repo.root, []))
        code, _, _ = run_main([repo.root])
        self.assertEqual(code, 0)


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
