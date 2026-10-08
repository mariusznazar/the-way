"""Tests of the mechanical checks of instruction files: each check fires on a repository broken on
purpose and stays silent on a sound one.

Run from the root of the-way:
    python -B -m unittest discover -s instruction-files -p "test_*.py"
"""

import os
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_instructions  # noqa: E402


class Repo:
    """A temporary repository whose files are given as {relative path: text}."""

    def __init__(self, files):
        self._dir = tempfile.TemporaryDirectory()
        self.root = self._dir.name
        for rel, text in files.items():
            path = os.path.join(self.root, *rel.split("/"))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)

    def findings(self, extra=()):
        return check_instructions.check(self.root, [os.path.join(self.root, e) for e in extra])

    def close(self):
        self._dir.cleanup()


def checks(findings, level=None):
    return sorted({f.check for f in findings if level is None or f.level == level})


class CheckTestCase(unittest.TestCase):
    def repo(self, files):
        repo = Repo(files)
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
        found = [f for f in repo.findings() if f.check == "dead-path"]
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
        repo = self.repo({".agents/skills/x/SKILL.md": "---\nname: x\n---\n"})
        self.assertIn("skill-dir", checks(repo.findings(), "warn"))

    def test_skills_in_claude_skills_without_pointer_get_one_note_for_codex(self):
        repo = self.repo({
            "AGENTS.md": "Rules.\n",
            ".claude/skills/x/SKILL.md": "---\nname: x\n---\n",
            ".claude/skills/y/SKILL.md": "---\nname: y\n---\n",
        })
        found = [f for f in repo.findings() if f.check == "skill-dir"]
        self.assertEqual([f.level for f in found], ["info"])
        self.assertIn("2 skills", found[0].message)

    def test_skill_pointed_to_from_agents_md_is_sound(self):
        repo = self.repo({
            "AGENTS.md": "Releases follow `.claude/skills/x/SKILL.md`.\n",
            ".claude/skills/x/SKILL.md": "---\nname: x\n---\n",
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


if __name__ == "__main__":
    unittest.main()
