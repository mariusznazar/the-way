"""Product installation checks for the pinned project-leading entry point."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation/install.py"
LEAD_SOURCE = "project-level/lead/skill/SKILL.md"
WRAPPERS = (".claude/skills/the-way-lead-project/SKILL.md",
            ".agents/skills/the-way-lead-project/SKILL.md")


def command(*args: str, cwd: Path, input_text: str | None = None):
    return subprocess.run(args, cwd=cwd, input=input_text, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class LeadInstallationTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="the-way-lead-install-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.product = self.root / "product"
        self.product.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Lead Installation Test")
        self.commit = self.git("rev-parse", "HEAD", cwd=SOURCE).stdout.strip()
        available = self.git("cat-file", "-e", f"{self.commit}:{LEAD_SOURCE}", cwd=SOURCE)
        self.assertEqual(available.returncode, 0)

    def git(self, *args: str, cwd: Path | None = None):
        result = command("git", *args, cwd=cwd or self.product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def install(self, *args: str):
        return command(sys.executable, "-B", str(INSTALL), str(self.product),
                       "--url", str(SOURCE), *args, cwd=self.product, input_text="y\n")

    def product_files(self):
        return {path.relative_to(self.product).as_posix(): path.read_bytes()
                for path in self.product.rglob("*")
                if path.is_file() and path.relative_to(self.product).parts[0]
                not in (".git", ".the-way")}

    def test_preview_apply_repeat_exposes_lead_and_preserves_product(self) -> None:
        # Omitting lead from installation must fail before any product write.
        originals = {
            "foundations/decisions.md": b"# Product decisions\r\n",
            "AGENTS.md": b"# Product instructions\r\n\r\n## Backlog\r\nLocal tracker.\r\n",
            "CLAUDE.md": b"@AGENTS.md\r\n# Product guidance\r\n",
            ".gitignore": b"local-data/\r\n",
        }
        for name, content in originals.items():
            path = self.product / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        before = self.product_files()
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        for name in WRAPPERS:
            self.assertIn(f"CREATE {name}", preview.stdout)
        self.assertEqual(before, self.product_files())
        self.assertFalse((self.product / ".the-way").exists())
        self.assertFalse((self.product / ".gitmodules").exists())

        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        claude, codex = (self.product / name for name in WRAPPERS)
        self.assertEqual(claude.read_bytes(), codex.read_bytes())
        wrapper = claude.read_text(encoding="utf-8")
        self.assertIn("name: the-way-lead-project\n", wrapper)
        self.assertIn(f"Its commit is `{self.commit}`", wrapper)
        self.assertIn(f"Read `.the-way/{LEAD_SOURCE}` in full", wrapper)
        self.assertIn("git submodule update --init -- .the-way", wrapper)
        self.assertIn("git ls-files --stage -- .the-way", wrapper)
        self.assertIn("git -C .the-way rev-parse HEAD", wrapper)
        for directory in (".claude", ".agents"):
            for sibling in (self.product / directory / "skills").glob("*/SKILL.md"):
                self.assertIn("`lead-project`", sibling.read_text(encoding="utf-8"))
        self.assertIn("`the-way-lead-project`",
                      (self.product / "AGENTS.md").read_text(encoding="utf-8"))
        for name in ("foundations/decisions.md", "CLAUDE.md"):
            self.assertEqual((self.product / name).read_bytes(), originals[name])
        for name in ("AGENTS.md", ".gitignore"):
            self.assertTrue((self.product / name).read_bytes().startswith(originals[name]))
        self.assertEqual(self.git("-C", ".the-way", "rev-parse", "HEAD").stdout.strip(),
                         self.commit)
        self.assertIn(f"160000 {self.commit}",
                      self.git("ls-files", "--stage", "--", ".the-way").stdout)
        self.assertEqual(set(self.git("diff", "--cached", "--name-only").stdout.splitlines()),
                         {".gitmodules", ".the-way"})

        installed = self.product_files()
        repeated = self.install("--apply")
        self.assertEqual(repeated.returncode, 0, repeated.stdout + repeated.stderr)
        self.assertIn("Already installed; no changes", repeated.stdout)
        self.assertEqual(installed, self.product_files())

    def test_clone_can_initialize_the_exact_lead_source(self) -> None:
        # A wrapper whose pin lacks its source breaks a fresh product session.
        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.git("add", "--", ".gitmodules", ".the-way", *WRAPPERS)
        self.git("commit", "-q", "-m", "Install pinned project leading")
        clone = self.root / "clone"
        self.git("clone", "-q", "--", str(self.product), str(clone), cwd=self.root)
        self.assertFalse((clone / ".the-way" / LEAD_SOURCE).exists())
        self.git("-c", "protocol.file.allow=always", "submodule", "update", "--init",
                 "--", ".the-way", cwd=clone)
        self.assertEqual(self.git("-C", ".the-way", "rev-parse", "HEAD",
                                  cwd=clone).stdout.strip(), self.commit)
        expected = self.git("show", f"{self.commit}:{LEAD_SOURCE}", cwd=SOURCE).stdout
        self.assertEqual((clone / ".the-way" / LEAD_SOURCE).read_text(encoding="utf-8"),
                         expected)
        self.assertEqual((clone / WRAPPERS[0]).read_bytes(), (clone / WRAPPERS[1]).read_bytes())

    def test_conflicting_lead_wrapper_refuses_before_writing(self) -> None:
        # Accepting a conflicting entry point could silently use another process.
        for name in WRAPPERS:
            with self.subTest(wrapper=name):
                path = self.product / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"# Product-owned conflicting skill\r\n")
                before = self.product_files()
                for args in ((), ("--apply",)):
                    refused = self.install(*args)
                    self.assertNotEqual(refused.returncode, 0)
                    self.assertIn("Existing integration file differs", refused.stderr)
                    self.assertEqual(before, self.product_files())
                    self.assertFalse((self.product / ".gitmodules").exists())
                    self.assertFalse((self.product / ".the-way").exists())
                path.unlink()

    def test_different_product_pin_is_not_moved(self) -> None:
        # New skill availability must not silently migrate an existing product.
        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        other_commit = self.git("rev-parse", "HEAD^", cwd=SOURCE).stdout.strip()
        self.git("update-index", "--cacheinfo", "160000", other_commit, ".the-way")
        before = self.product_files()
        index = self.git("ls-files", "--stage").stdout
        for args in ((), ("--apply",)):
            refused = self.install(*args)
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn(f"pins {other_commit}, requested {self.commit}", refused.stderr)
            self.assertEqual(before, self.product_files())
            self.assertEqual(index, self.git("ls-files", "--stage").stdout)
            self.assertEqual(self.git("-C", ".the-way", "rev-parse", "HEAD").stdout.strip(),
                             self.commit)


if __name__ == "__main__":
    unittest.main()
