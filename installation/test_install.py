"""Integration checks for installing a pinned process in another repository."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation" / "install.py"


def command(*args: str, cwd: Path, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, input=input_text, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class InstallTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="the-way-install-test-")
        self.addCleanup(self.temporary.cleanup)
        self.product = Path(self.temporary.name) / "product"
        self.product.mkdir()
        self.assertEqual(command("git", "init", "-q", str(self.product), cwd=SOURCE).returncode, 0)
        self.assertEqual(command("git", "config", "user.email", "test@example.invalid",
                                 cwd=self.product).returncode, 0)
        self.assertEqual(command("git", "config", "user.name", "Install Test",
                                 cwd=self.product).returncode, 0)
        self.commit = command("git", "rev-parse", "HEAD", cwd=SOURCE).stdout.strip()

    def install(self, *args: str, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        return command(sys.executable, "-B", str(INSTALL), str(self.product), "--url", str(SOURCE),
                       *args, cwd=self.product, input_text=input_text)

    def test_preview_apply_rerun_and_preserve_foundation(self) -> None:
        foundations = self.product / "foundations"
        foundations.mkdir()
        existing = foundations / "decisions.md"
        existing.write_bytes(b"# Existing decisions\r\n")

        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("CREATE foundations/invariants.md", preview.stdout)
        self.assertIn("KEEP foundations/decisions.md", preview.stdout)
        self.assertFalse((self.product / ".gitmodules").exists())
        self.assertFalse((self.product / ".the-way").exists())

        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(existing.read_bytes(), b"# Existing decisions\r\n")
        self.assertEqual(command("git", "-C", ".the-way", "rev-parse", "HEAD",
                                 cwd=self.product).stdout.strip(), self.commit)
        self.assertEqual((self.product / ".the-way" / "README.md").read_text(encoding="utf-8"),
                         command("git", "show", f"{self.commit}:README.md", cwd=SOURCE).stdout)
        staged = command("git", "ls-files", "--stage", "--", ".the-way", cwd=self.product)
        self.assertIn("160000 " + self.commit, staged.stdout)
        wrapper = self.product / ".claude/skills/the-way-record-decision/SKILL.md"
        self.assertIn("name: the-way-record-decision", wrapper.read_text(encoding="utf-8"))
        self.assertIn(self.commit, wrapper.read_text(encoding="utf-8"))
        for element, name in (("decisions", "record-decision"),
                              ("invariants", "record-invariant"),
                              ("glossary", "record-glossary-term"),
                              ("part-map", "update-part-map"),
                              ("environment-facts", "record-environment-fact")):
            path = self.product / ".claude" / "skills" / f"the-way-{name}" / "SKILL.md"
            self.assertTrue(path.is_file(), path)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"name: the-way-{name}", text)
            self.assertIn(f".the-way/elements/{element}/skill/SKILL.md", text)
            self.assertIn("git ls-files --stage -- .the-way", text)
        rule = (self.product / ".claude/rules/the-way.md").read_text(encoding="utf-8")
        self.assertIn("git submodule update --init -- .the-way", rule)
        before = {str(path.relative_to(self.product)): path.read_bytes()
                  for path in self.product.rglob("*.md") if path.is_file()}

        repeated = self.install("--apply", input_text="y\n")
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertIn("Already installed; no changes", repeated.stdout)
        self.assertEqual(before, {str(path.relative_to(self.product)): path.read_bytes()
                                  for path in self.product.rglob("*.md") if path.is_file()})

    def test_rejects_conflicting_integration_file_before_writing(self) -> None:
        wrapper = self.product / ".claude/skills/the-way-record-decision/SKILL.md"
        wrapper.parent.mkdir(parents=True)
        wrapper.write_text("user's skill\n", encoding="utf-8")
        result = self.install("--apply", input_text="y\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Existing integration file differs", result.stderr)
        self.assertEqual(wrapper.read_text(encoding="utf-8"), "user's skill\n")
        self.assertFalse((self.product / ".the-way").exists())

    def test_declined_apply_writes_nothing(self) -> None:
        result = self.install("--apply", input_text="n\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Cancelled; no changes", result.stdout)
        self.assertFalse((self.product / ".gitmodules").exists())
        self.assertFalse((self.product / "foundations").exists())

    def test_empty_foundations_have_valid_form(self) -> None:
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        for element, filename in (
            ("decisions", "decisions.md"),
            ("invariants", "invariants.md"),
            ("glossary", "glossary.md"),
            ("part-map", "part_map.md"),
            ("environment-facts", "environment_facts.md"),
        ):
            guard = self.product / ".the-way" / "elements" / element / "format_guard.py"
            result = command(sys.executable, "-B", str(guard),
                             str(self.product / "foundations" / filename), cwd=self.product)
            if element == "part-map":
                # An empty map cannot yet assign the two tracked submodule files to a product
                # part. These are content checks, not errors in the map's empty file form.
                self.assertIn("no part claims `.gitmodules`", result.stdout)
                self.assertIn("no part claims `.the-way`", result.stdout)
                self.assertIn("2 error(s)", result.stdout)
            else:
                self.assertEqual(result.returncode, 0, f"{element}: {result.stdout}\n{result.stderr}")

    def test_pinned_submodule_initializes_in_a_fresh_checkout(self) -> None:
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        fresh = Path(self.temporary.name) / "fresh"
        fresh.mkdir()
        self.assertEqual(command("git", "init", "-q", str(fresh), cwd=SOURCE).returncode, 0)
        shutil.copyfile(self.product / ".gitmodules", fresh / ".gitmodules")
        self.assertEqual(command("git", "add", "--", ".gitmodules", cwd=fresh).returncode, 0)
        indexed = command("git", "update-index", "--add", "--cacheinfo", "160000",
                          self.commit, ".the-way", cwd=fresh)
        self.assertEqual(indexed.returncode, 0, indexed.stderr)
        initialized = command("git", "-c", "protocol.file.allow=always", "submodule", "update",
                              "--init", "--", ".the-way", cwd=fresh)
        self.assertEqual(initialized.returncode, 0, initialized.stderr)
        self.assertEqual(command("git", "-C", ".the-way", "rev-parse", "HEAD",
                                 cwd=fresh).stdout.strip(), self.commit)


if __name__ == "__main__":
    unittest.main()
