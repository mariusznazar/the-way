"""Product installation checks for the styleguide skill and the guidance naming the form check."""

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation/install.py"
SKILL_SOURCE = "product-guidelines/styleguide/SKILL.md"
WRAPPERS = (".claude/skills/the-way-maintain-styleguide/SKILL.md",
            ".agents/skills/the-way-maintain-styleguide/SKILL.md")
FORM = "python -B .the-way/product-guidelines/form_check.py"
REFERENCES = "python -B .the-way/product-guidelines/form_check.py --merge-onto <main commit>"
# Before every merge: a renamed file `## Where in code` names, or a moved pin, breaks guidelines
# whatever files the change touches (product-guidelines/template.md, the invariants' *Part*).
SENTENCE = (f"Where this repository holds `guidelines/`, run `{FORM}` and `{REFERENCES}` before "
            "every merge.")


def command(*args: str, cwd: Path, input_text: str | None = None):
    return subprocess.run(args, cwd=cwd, input=input_text, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class StyleguideInstallationTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="the-way-styleguide-install-")
        self.addCleanup(temporary.cleanup)
        self.product = Path(temporary.name) / "product"
        self.product.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Styleguide Installation Test")
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

    def test_preview_apply_repeat_exposes_the_styleguide_skill_and_preserves_product(self) -> None:
        # A product left without the wrapper cannot reach the skill; product files must survive.
        originals = {
            "foundations/decisions.md": b"# Product decisions\r\n",
            "guidelines/styleguide-web.md": b"# Styleguide guidelines - web\r\n",
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
        self.assertIn(SENTENCE, preview.stdout)
        self.assertEqual(before, self.product_files())
        self.assertFalse((self.product / ".the-way").exists())
        self.assertFalse((self.product / ".gitmodules").exists())

        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        claude, codex = (self.product / name for name in WRAPPERS)
        self.assertEqual(claude.read_bytes(), codex.read_bytes())
        wrapper = claude.read_text(encoding="utf-8")
        self.assertTrue(wrapper.startswith("---\nname: the-way-maintain-styleguide\n"), wrapper)
        self.assertIn(f"Its commit is `{self.commit}`", wrapper)
        self.assertIn(f"Read `.the-way/{SKILL_SOURCE}` in full and follow it.", wrapper)
        self.assertIn(f"If `.the-way/{SKILL_SOURCE}` is absent", wrapper)
        siblings = [path for directory in (".claude", ".agents")
                    for path in (self.product / directory / "skills").glob("the-way-*/SKILL.md")]
        self.assertEqual(len(siblings), 32)
        for sibling in siblings:
            text = sibling.read_text(encoding="utf-8")
            self.assertRegex(text, r"names another the-way skill — [^\n]*`maintain-styleguide`"
                                   r"[^\n]* — use this product's project skill", sibling)

        agents = (self.product / "AGENTS.md").read_bytes()
        self.assertTrue(agents.startswith(originals["AGENTS.md"]))
        block = agents[len(originals["AGENTS.md"]):].decode("utf-8").replace("\r\n", "\n")
        self.assertIn("`the-way-maintain-styleguide`", block)
        self.assertIn(SENTENCE, block)
        # The block holds the-way's own paths only, never one the product chose (WAY-107).
        for product_path in ("docs/backlog/", "styleguide-web", "local-data/"):
            self.assertNotIn(product_path, block)
        for name in ("foundations/decisions.md", "guidelines/styleguide-web.md", "CLAUDE.md"):
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

    def test_guidance_names_both_form_check_commands_and_they_run_in_the_product(self) -> None:
        # A command the guidance names that the pinned checkout cannot run leaves guidelines unchecked.
        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        guidance = (self.product / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(SENTENCE, guidance)
        named = re.findall(r"`(python -B \.the-way/product-guidelines/form_check\.py[^`]*)`",
                           guidance)
        self.assertEqual(named, [FORM, REFERENCES])
        self.git("add", "--", "AGENTS.md", "CLAUDE.md", ".gitignore", "foundations",
                 ".claude", ".agents")
        self.git("commit", "-q", "-m", "Install the pinned process")
        main_commit = self.git("rev-parse", "HEAD").stdout.strip()
        commands = [text.replace("<main commit>", main_commit).split() for text in named]
        for args in commands:
            with self.subTest(command=args, guidelines="none"):
                ran = command(*args, cwd=self.product)
                self.assertEqual(ran.returncode, 0, ran.stdout + ran.stderr)
                self.assertIn("note:", ran.stdout)
        # the-way holds no guidelines either, so only a product file can fail the run.
        broken = self.product / "guidelines" / "styleguide-web.md"
        broken.parent.mkdir()
        broken.write_text("# Styleguide guidelines - web\n\nNo header lines.\n", encoding="utf-8")
        for args in commands:
            with self.subTest(command=args, guidelines="broken"):
                ran = command(*args, cwd=self.product)
                self.assertEqual(ran.returncode, 1, ran.stdout + ran.stderr)
                self.assertIn("guidelines/styleguide-web.md:0: error: the header line "
                              "*Discipline* is missing", ran.stdout)

    def test_block_of_an_earlier_pin_without_the_sentence_is_refused_before_writing(self) -> None:
        # Keeping the earlier block would leave a product's agents without the form check.
        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        agents = self.product / "AGENTS.md"
        current = agents.read_text(encoding="utf-8")
        earlier = current.replace(SENTENCE + " ", "")
        self.assertNotEqual(earlier, current)
        agents.write_text(earlier, encoding="utf-8", newline="\n")
        for name in WRAPPERS:
            (self.product / name).unlink()
        before = self.product_files()
        for args in ((), ("--apply",)):
            refused = self.install(*args)
            self.assertNotEqual(refused.returncode, 0, refused.stdout)
            self.assertIn("differs from this commit's guidance", refused.stderr)
            self.assertEqual(before, self.product_files())


if __name__ == "__main__":
    unittest.main()
