"""Integration checks for installing a pinned process in another repository."""

from __future__ import annotations

from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation" / "install.py"
sys.path.insert(0, str(SOURCE / "installation"))
import install  # noqa: E402

NAMES = (("decisions", "record-decision"), ("invariants", "record-invariant"),
         ("glossary", "record-glossary-term"), ("part-map", "update-part-map"),
         ("environment-facts", "record-environment-fact"))
BLOCK = install.agents_block()


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
        for element, name in NAMES:
            claude = self.product / ".claude" / "skills" / f"the-way-{name}" / "SKILL.md"
            codex = self.product / ".agents" / "skills" / f"the-way-{name}" / "SKILL.md"
            self.assertTrue(claude.is_file(), claude)
            self.assertEqual(codex.read_bytes(), claude.read_bytes())
            text = claude.read_text(encoding="utf-8")
            self.assertIn(f"name: the-way-{name}", text)
            self.assertIn(self.commit, text)
            self.assertIn(f".the-way/elements/{element}/skill/SKILL.md", text)
            self.assertIn("git ls-files --stage -- .the-way", text)
            self.assertIn("use this product's project skill of the same name with the "
                          "`the-way-` prefix, never an unprefixed one", text)
            for _, sibling in NAMES:
                self.assertIn(f"`{sibling}`", text)
        rule = (self.product / ".claude/rules/the-way.md").read_text(encoding="utf-8")
        self.assertEqual(rule, install.product_guidance())
        self.assertEqual((self.product / "AGENTS.md").read_text(encoding="utf-8"), BLOCK)
        self.assertEqual((self.product / ".gitignore").read_bytes(), b".runs/\n")
        before = self.product_files()

        repeated = self.install("--apply", input_text="y\n")
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertIn("KEEP AGENTS.md", repeated.stdout)
        self.assertIn("KEEP .gitignore", repeated.stdout)
        self.assertIn("Already installed; no changes", repeated.stdout)
        self.assertEqual(before, self.product_files())

    def product_files(self) -> dict[str, bytes]:
        return {path.relative_to(self.product).as_posix(): path.read_bytes()
                for path in self.product.rglob("*") if path.is_file() and
                not {".git", ".the-way"} & set(path.relative_to(self.product).parts)}

    def test_guidance_names_no_commit_and_covers_the_product_rules(self) -> None:
        guidance = install.product_guidance()
        self.assertIsNone(re.search(r"\b[0-9a-f]{7,40}\b", guidance), guidance)
        self.assertNotIn(self.commit, guidance)
        for fragment in ("git submodule update --init -- .the-way",
                         "git -C .the-way rev-parse HEAD", "git ls-files --stage -- .the-way",
                         "python -B .the-way/gate/run_tests.py <directory>",
                         "python -B .the-way/elements/<element>/format_guard.py foundations/<file>",
                         "git merge-base HEAD main", "--merge-onto", "`none`", ".runs/",
                         "claimed by no part", "never a pass"):
            self.assertIn(fragment, guidance)
        for _, name in NAMES:
            self.assertIn(f"`the-way-{name}`", guidance)
        self.assertTrue(BLOCK.startswith("<!-- the-way:begin -->\n" + guidance))
        self.assertTrue(BLOCK.endswith("<!-- the-way:end -->\n"))

    def test_appends_block_to_agents_file_without_one(self) -> None:
        agents = self.product / "AGENTS.md"
        original = b"# Product rules\r\n\r\nKeep it small."
        agents.write_bytes(original)
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("APPEND AGENTS.md", preview.stdout)
        self.assertEqual(agents.read_bytes(), original)
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(agents.read_bytes(), original + b"\r\n\r\n" +
                         BLOCK.replace("\n", "\r\n").encode("utf-8"))
        repeated = self.install("--apply", input_text="y\n")
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertIn("KEEP AGENTS.md", repeated.stdout)
        self.assertIn("Already installed; no changes", repeated.stdout)

    def test_keeps_agents_file_with_identical_block(self) -> None:
        agents = self.product / "AGENTS.md"
        content = ("# Product rules\n\n" + BLOCK + "\nMore rules.\n").encode("utf-8")
        agents.write_bytes(content)
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertIn("KEEP AGENTS.md", applied.stdout)
        self.assertEqual(agents.read_bytes(), content)

    def test_rejects_agents_file_with_other_or_broken_block_before_writing(self) -> None:
        agents = self.product / "AGENTS.md"
        changed = BLOCK.replace("Pinned the-way process", "Old the-way process")
        for content, message in (
                ("# Rules\n\n" + changed, "differs from this commit's guidance"),
                ("# Rules\n\n<!-- the-way:begin -->\nNo end.\n",
                 "1 <!-- the-way:begin --> and 0"),
                ("<!-- the-way:end -->\n" + BLOCK, "1 <!-- the-way:begin --> and 2"),
                (BLOCK + "\n" + BLOCK, "2 <!-- the-way:begin --> and 2"),
                ("<!-- the-way:end -->\n<!-- the-way:begin -->\n",
                 "1 <!-- the-way:begin --> and 1")):
            with self.subTest(message=message):
                agents.write_text(content, encoding="utf-8", newline="\n")
                for args in ((), ("--apply",)):
                    result = self.install(*args, input_text="y\n")
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn(message, result.stderr)
                self.assertEqual(agents.read_text(encoding="utf-8", newline=""), content)
                self.assertEqual(sorted(path.name for path in self.product.iterdir()),
                                 [".git", "AGENTS.md"])

    def test_adds_runs_line_to_gitignore_only_where_missing(self) -> None:
        ignore = self.product / ".gitignore"
        ignore.write_bytes(b"node_modules/")
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertIn("APPEND .gitignore", applied.stdout)
        self.assertEqual(ignore.read_bytes(), b"node_modules/\n.runs/\n")

        ignore.write_bytes(b"")
        emptied = self.install("--apply", input_text="y\n")
        self.assertEqual(emptied.returncode, 0, emptied.stderr)
        self.assertIn("APPEND .gitignore\n(added at the end; the existing content stays byte for "
                      "byte)\n+.runs/\n", emptied.stdout)
        self.assertEqual(ignore.read_bytes(), b".runs/\n")

        ignore.write_bytes(b"build/\r\n")
        appended = self.install("--apply", input_text="y\n")
        self.assertEqual(appended.returncode, 0, appended.stderr)
        self.assertEqual(ignore.read_bytes(), b"build/\r\n.runs/\r\n")

        ignore.write_bytes(b".runs/\nbuild/\n")
        kept = self.install("--apply", input_text="y\n")
        self.assertEqual(kept.returncode, 0, kept.stderr)
        self.assertIn("KEEP .gitignore", kept.stdout)
        self.assertIn("Already installed; no changes", kept.stdout)
        self.assertEqual(ignore.read_bytes(), b".runs/\nbuild/\n")

    def test_invariants_guard_accepts_a_record_under_runs_in_a_fresh_product(self) -> None:
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        path = self.product / "foundations" / "invariants.md"
        entry = ("## save-round-trip/1\n\n"
                 "A game saved and loaded back holds the same state as before it was saved.\n\n"
                 "- **Method:** `python -B tools/check.py --record .runs/saving.jsonl`\n"
                 "- **Rests on:** none\n- **Derives from:** none\n- **Part:** saving\n"
                 "- **Correction:** none\n\n")
        path.write_text(path.read_text(encoding="utf-8").replace(
            "## Withdrawn identifiers", entry + "## Withdrawn identifiers", 1),
            encoding="utf-8", newline="\n")
        guard = (sys.executable, "-B", ".the-way/elements/invariants/format_guard.py",
                 "foundations/invariants.md", "--base", "none", "--merge-onto", "none")
        result = command(*guard, cwd=self.product)
        self.assertIn("error(s)", result.stdout, result.stderr)
        self.assertNotIn("git does not ignore", result.stdout)
        # Control: the same guard reports the record path once git no longer ignores it.
        (self.product / ".gitignore").write_text("", encoding="utf-8")
        result = command(*guard, cwd=self.product)
        self.assertIn("git does not ignore `.runs/saving.jsonl`", result.stdout)

    def test_rejects_conflicting_integration_file_before_writing(self) -> None:
        wrapper = self.product / ".claude/skills/the-way-record-decision/SKILL.md"
        wrapper.parent.mkdir(parents=True)
        wrapper.write_text("user's skill\n", encoding="utf-8")
        result = self.install("--apply", input_text="y\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Existing integration file differs", result.stderr)
        self.assertEqual(wrapper.read_text(encoding="utf-8"), "user's skill\n")
        self.assertFalse((self.product / ".the-way").exists())
        self.assertFalse((self.product / "AGENTS.md").exists())
        self.assertFalse((self.product / ".gitignore").exists())

    def test_declined_apply_writes_nothing(self) -> None:
        result = self.install("--apply", input_text="n\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Cancelled; no changes", result.stdout)
        self.assertFalse((self.product / ".gitmodules").exists())
        self.assertFalse((self.product / "foundations").exists())
        self.assertFalse((self.product / "AGENTS.md").exists())
        self.assertFalse((self.product / ".gitignore").exists())

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
