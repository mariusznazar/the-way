"""Integration checks for Claude Code guidance installed in a product repository."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation" / "install.py"


def command(*args: str, cwd: Path, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, input=input_text, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class InstalledGuidanceTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="the-way-guidance-test-")
        self.addCleanup(temporary.cleanup)
        self.product = Path(temporary.name) / "product"
        self.product.mkdir()
        initialized = command("git", "init", "-q", str(self.product), cwd=SOURCE)
        self.assertEqual(initialized.returncode, 0, initialized.stderr)

    def install(self, *args: str, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        return command(sys.executable, "-B", str(INSTALL), str(self.product), "--url",
                       str(SOURCE), *args, cwd=self.product, input_text=input_text)

    def test_creates_root_claude_import_when_missing(self) -> None:
        # invariant: installation-claude-guidance
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        claude = self.product / "CLAUDE.md"
        self.assertTrue(claude.is_file(), "Installer did not create root CLAUDE.md")
        self.assertEqual(claude.read_bytes(), b"@AGENTS.md\n")
        self.assertFalse((self.product / ".claude/rules/the-way.md").exists())

    def test_warns_before_confirmation_and_preserves_existing_file_without_import(self) -> None:
        # invariant: installation-claude-guidance
        claude = self.product / "CLAUDE.md"
        original = b"# Product guidance\r\n\r\nKeep this guidance.\r\n"
        claude.write_bytes(original)

        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        warning = applied.stdout.find("WARNING:")
        confirmation = applied.stdout.find("Apply these changes?")
        self.assertGreaterEqual(warning, 0, "Missing installation warning")
        self.assertGreater(confirmation, warning, "Warning must precede confirmation")
        self.assertIn("CLAUDE.md", applied.stdout[warning:confirmation])
        self.assertIn("@AGENTS.md", applied.stdout[warning:confirmation])
        self.assertEqual(claude.read_bytes(), original)
        self.assertFalse((self.product / ".claude/rules/the-way.md").exists())

    def test_code_fenced_import_mention_still_warns(self) -> None:
        # invariant: installation-claude-guidance
        claude = self.product / "CLAUDE.md"
        original = b"# Product guidance\n\n```markdown\n@AGENTS.md\n```\n"
        claude.write_bytes(original)

        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        warning = applied.stdout.find("WARNING:")
        confirmation = applied.stdout.find("Apply these changes?")
        self.assertGreaterEqual(warning, 0, "Missing installation warning")
        self.assertGreater(confirmation, warning, "Warning must precede confirmation")
        self.assertIn("CLAUDE.md", applied.stdout[warning:confirmation])
        self.assertIn("@AGENTS.md", applied.stdout[warning:confirmation])
        self.assertEqual(claude.read_bytes(), original)
        self.assertFalse((self.product / ".claude/rules/the-way.md").exists())

    def test_effective_import_needs_no_missing_import_warning_and_is_preserved(self) -> None:
        # invariant: installation-claude-guidance
        claude = self.product / "CLAUDE.md"
        original = b"@AGENTS.md\n\n# Product guidance\nKeep this guidance.\n"
        claude.write_bytes(original)

        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertNotIn("WARNING:", applied.stdout)
        self.assertEqual(claude.read_bytes(), original)
        self.assertFalse((self.product / ".claude/rules/the-way.md").exists())


if __name__ == "__main__":
    unittest.main()
