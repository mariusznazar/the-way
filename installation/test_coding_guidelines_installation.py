"""Product installation checks for the coding-guidelines skill and its refusals."""

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation/install.py"
SKILL_SOURCE = "product-guidelines/coding/SKILL.md"
NAME = "the-way-maintain-coding-guidelines"
WRAPPERS = (f".claude/skills/{NAME}/SKILL.md", f".agents/skills/{NAME}/SKILL.md")


def command(*args: str, cwd: Path, input_text: str | None = None):
    return subprocess.run(args, cwd=cwd, input=input_text, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class CodingGuidelinesInstallationTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="the-way-coding-install-")
        self.addCleanup(temporary.cleanup)
        self.product = Path(temporary.name) / "product"
        self.product.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Coding Guidelines Installation Test")
        self.commit = self.git("rev-parse", "HEAD", cwd=SOURCE).stdout.strip()
        available = command("git", "cat-file", "-e", f"{self.commit}:{SKILL_SOURCE}", cwd=SOURCE)
        self.assertEqual(available.returncode, 0, f"{SKILL_SOURCE} is not committed")

    def git(self, *args: str, cwd: Path | None = None):
        result = command("git", *args, cwd=cwd or self.product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def install(self, *args: str, answer: str = "y\n"):
        return command(sys.executable, "-B", str(INSTALL), str(self.product),
                       "--url", str(SOURCE), *args, cwd=self.product, input_text=answer)

    def product_files(self):
        return {path.relative_to(self.product).as_posix(): path.read_bytes()
                for path in self.product.rglob("*")
                if path.is_file() and path.relative_to(self.product).parts[0]
                not in (".git", ".the-way")}

    def product_tree(self):
        """Every path outside .git with the bytes of each file, so a created directory counts."""
        return {path.relative_to(self.product).as_posix():
                (path.read_bytes() if path.is_file() else None)
                for path in self.product.rglob("*")
                if path.relative_to(self.product).parts[0] != ".git"}

    def test_preview_apply_repeat_exposes_the_coding_guidelines_skill_and_preserves_product(
            self) -> None:
        # A product left without the wrapper cannot reach the skill; product files must survive.
        originals = {
            "foundations/decisions.md": b"# Product decisions\r\n",
            "guidelines/coding.md": b"# Coding guidelines\r\n",
            "AGENTS.md": b"# Product instructions\r\n\r\n## Backlog\r\nTasks in docs/backlog/.\r\n",
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
            self.assertIn(f"CREATE {name}\n", preview.stdout)
        self.assertEqual(before, self.product_files())
        self.assertFalse((self.product / ".the-way").exists())
        self.assertFalse((self.product / ".gitmodules").exists())

        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        claude, codex = (self.product / name for name in WRAPPERS)
        self.assertEqual(claude.read_bytes(), codex.read_bytes())
        wrapper = claude.read_text(encoding="utf-8")
        source = command("git", "show", f"{self.commit}:{SKILL_SOURCE}", cwd=SOURCE).stdout
        description = re.search(r"^description: (.+)$", source, re.M).group(1)
        self.assertTrue(wrapper.startswith(
            f"---\nname: {NAME}\ndescription: {description} "
            "Use this product's pinned the-way commit.\n---\n"), wrapper)
        self.assertNotIn(self.commit, wrapper)
        self.assertIn(f"Read `.the-way/{SKILL_SOURCE}` in full and follow it.", wrapper)
        self.assertIn(f"If `.the-way/{SKILL_SOURCE}` is absent", wrapper)
        siblings = [path for directory in (".claude", ".agents")
                    for path in (self.product / directory / "skills").glob("the-way-*/SKILL.md")]
        self.assertEqual(len(siblings), 40)
        for sibling in siblings:
            text = sibling.read_text(encoding="utf-8")
            self.assertRegex(text, r"names another the-way skill — [^\n]*"
                                   r"`maintain-coding-guidelines`[^\n]* — use this product's "
                                   r"project skill", sibling)

        agents = (self.product / "AGENTS.md").read_bytes()
        self.assertTrue(agents.startswith(originals["AGENTS.md"]))
        block = agents[len(originals["AGENTS.md"]):].decode("utf-8").replace("\r\n", "\n")
        self.assertRegex(block, r"Use the project skills [^\n]*`" + NAME + r"`[^\n]* for their "
                                r"named work\.")
        # The block holds the-way's own paths only, never one the product chose (WAY-107).
        for product_path in ("docs/backlog/", "guidelines/coding.md", "local-data/"):
            self.assertNotIn(product_path, block)
        for name in ("foundations/decisions.md", "guidelines/coding.md", "CLAUDE.md"):
            self.assertEqual((self.product / name).read_bytes(), originals[name])
        self.assertTrue((self.product / ".gitignore").read_bytes().startswith(
            originals[".gitignore"]))
        self.assertEqual(self.git("-C", ".the-way", "rev-parse", "HEAD").stdout.strip(),
                         self.commit)
        self.assertEqual(set(self.git("diff", "--cached", "--name-only").stdout.splitlines()),
                         {".gitmodules", ".the-way"})

        installed = self.product_files()
        repeated = self.install("--apply")
        self.assertEqual(repeated.returncode, 0, repeated.stdout + repeated.stderr)
        self.assertIn("Already installed; no changes", repeated.stdout)
        self.assertEqual(installed, self.product_files())

    def test_crafted_entry_at_the_new_wrapper_path_stops_the_run_before_writing(self) -> None:
        # WAY-48: a product's file at the path the installer owns must never be overwritten or
        # half-installed around; the refusal must hold for the new wrapper in both directories.
        crafted = {
            "conflicting file": lambda path: path.write_text("user's skill\n", encoding="utf-8"),
            "directory": lambda path: path.mkdir(),
            "non-UTF-8 file": lambda path: path.write_bytes(b"\xff\xfe user's skill\n"),
        }
        for directory in (".claude", ".agents"):
            for kind, make in crafted.items():
                for args in ((), ("--apply",)):
                    with self.subTest(directory=directory, crafted=kind, args=args):
                        with tempfile.TemporaryDirectory(prefix="the-way-coding-crafted-") as root:
                            self.product = Path(root) / "product"
                            self.product.mkdir()
                            self.git("init", "-q")
                            path = self.product / directory / "skills" / NAME / "SKILL.md"
                            path.parent.mkdir(parents=True)
                            make(path)
                            before = self.product_tree()
                            refused = self.install(*args)
                            self.assertNotEqual(refused.returncode, 0,
                                                refused.stdout + refused.stderr)
                            if kind != "non-UTF-8 file":
                                # The non-UTF-8 case stops on an uncaught UnicodeDecodeError
                                # (pre-existing, C37); only its exit and the untouched tree count.
                                self.assertIn("Existing integration file differs",
                                              refused.stderr)
                                self.assertIn(directory, refused.stderr)
                                self.assertIn(NAME, refused.stderr)
                            self.assertNotIn("Installed.", refused.stdout)
                            self.assertEqual(before, self.product_tree())
                            self.assertEqual(
                                self.git("ls-files", "--stage").stdout, "")


if __name__ == "__main__":
    unittest.main()
