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

NAMES = (("elements/decisions/skill/SKILL.md", "record-decision"),
         ("elements/invariants/skill/SKILL.md", "record-invariant"),
         ("elements/glossary/skill/SKILL.md", "record-glossary-term"),
         ("elements/part-map/skill/SKILL.md", "update-part-map"),
         ("elements/environment-facts/skill/SKILL.md", "record-environment-fact"),
         ("elements/common/skill/SKILL.md", "find-foundation-entries"),
         ("project-level/skill/SKILL.md", "define-project"),
         ("project-level/plan/skill/SKILL.md", "plan-project"),
         ("project-level/technology/SKILL.md", "settle-technology"),
         ("project-level/task/skill/SKILL.md", "refine-task"),
         ("task-cycle/skill/SKILL.md", "implement-task"),
         ("task-cycle/plan/SKILL.md", "plan-task"),
         ("elements/common/critique/SKILL.md", "critique"),
         ("product-guidelines/coding/SKILL.md", "maintain-coding-guidelines"))
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
        self.assertIn("CREATE CLAUDE.md", preview.stdout)
        self.assertIn("+@AGENTS.md", preview.stdout)
        self.assertFalse((self.product / "CLAUDE.md").exists())
        self.assertIn("CREATE foundations/invariants.md", preview.stdout)
        self.assertIn("KEEP foundations/decisions.md", preview.stdout)
        self.assertNotIn("WARNING", preview.stdout)
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
        for path, name in NAMES:
            claude = self.product / ".claude" / "skills" / f"the-way-{name}" / "SKILL.md"
            codex = self.product / ".agents" / "skills" / f"the-way-{name}" / "SKILL.md"
            self.assertTrue(claude.is_file(), claude)
            self.assertEqual(codex.read_bytes(), claude.read_bytes())
            text = claude.read_text(encoding="utf-8")
            self.assertIn(f"name: the-way-{name}", text)
            self.assertIn(self.commit, text)
            self.assertIn(f".the-way/{path}", text)
            self.assertIn("git ls-files --stage -- .the-way", text)
            self.assertIn("use this product's project skill of the same name with the "
                          "`the-way-` prefix, never an unprefixed one", text)
            for _, sibling in NAMES:
                self.assertIn(f"`{sibling}`", text)
        # invariant: installation-claude-guidance/1
        self.assertFalse((self.product / ".claude/rules/the-way.md").exists())
        self.assertEqual((self.product / "CLAUDE.md").read_bytes(), b"@AGENTS.md\n")
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

    def test_wrapper_sends_the_skill_to_the_product_case_of_where_the_way_lies(self) -> None:
        for path, name in NAMES:
            with self.subTest(name):
                text = install.skill_wrapper(path, name, self.commit)
                self.assertIn("Where it says where the-way lies, the product's case applies: "
                              "here the process root is `.the-way`.", text)
                self.assertNotIn("global install", text)
                self.assertIn("Do not substitute a global skill.", text)

    def test_guidance_names_no_commit_and_covers_the_product_rules(self) -> None:
        guidance = install.product_guidance()
        self.assertIsNone(re.search(r"\b[0-9a-f]{7,40}\b", guidance), guidance)
        self.assertNotIn(self.commit, guidance)
        for fragment in ("git submodule update --init -- .the-way",
                         "git -C .the-way rev-parse HEAD", "git ls-files --stage -- .the-way",
                         "python -B .the-way/gate/run_tests.py <directory>",
                         "python -B .the-way/elements/<element>/format_guard.py foundations/<file>",
                         "git symbolic-ref --short refs/remotes/origin/HEAD",
                         "git merge-base HEAD <main branch>", "--merge-onto", "`none`", ".runs/",
                         "claimed by no part", "never a pass"):
            self.assertIn(fragment, guidance)
        for _, name in NAMES:
            self.assertIn(f"`the-way-{name}`", guidance)
        # The main branch is a role; the guidance never names one product's branch.
        self.assertIsNone(re.search(r"`main`|HEAD main\b|no `main`", guidance), guidance)
        self.assertTrue(BLOCK.startswith("<!-- the-way:begin -->\n" + guidance))
        self.assertTrue(BLOCK.endswith("<!-- the-way:end -->\n"))

    def test_appends_block_to_agents_file_without_one(self) -> None:
        agents = self.product / "AGENTS.md"
        original = b"# Product rules\r\n\r\nKeep it small."
        agents.write_bytes(original)
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        header = "APPEND AGENTS.md\n(added at the end; the existing content stays byte for byte)\n"
        self.assertIn(header, preview.stdout)
        self.assertEqual(agents.read_bytes(), original)
        shown = []
        for line in preview.stdout.split(header, 1)[1].split("\n"):
            if not line.startswith("+"):
                break
            shown.append(line[1:])
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        added = original + b"\r\n\r\n" + BLOCK.replace("\n", "\r\n").encode("utf-8")
        self.assertEqual(agents.read_bytes(), added)
        # The preview shows the added lines: a blank one, then the block; the first newline
        # appended only ends the existing last line.
        self.assertEqual("\n".join(shown) + "\n",
                         added[len(original):].decode("utf-8").replace("\r\n", "\n")[1:])
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
                 "A document saved and loaded back holds the same content as before it was saved.\n\n"
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
        for directory in (".claude", ".agents"):
            with self.subTest(directory=directory):
                wrapper = self.product / directory / "skills/the-way-record-decision/SKILL.md"
                wrapper.parent.mkdir(parents=True)
                wrapper.write_text("user's skill\n", encoding="utf-8")
                result = self.install("--apply", input_text="y\n")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Existing integration file differs", result.stderr)
                self.assertIn(directory, result.stderr)
                self.assertEqual(wrapper.read_text(encoding="utf-8"), "user's skill\n")
                self.assertEqual(sorted(path.name for path in self.product.iterdir()),
                                 sorted([".git", directory]))
                shutil.rmtree(self.product / directory)

    def test_rejects_agents_or_ignore_file_that_is_no_regular_utf8_file(self) -> None:
        for name in ("AGENTS.md", ".gitignore"):
            path = self.product / name
            for kind, message in (("directory", "is not a regular file"),
                                  ("bytes", "is not UTF-8 text")):
                with self.subTest(name=name, kind=kind):
                    if kind == "directory":
                        path.mkdir()
                    else:
                        path.write_bytes(b"\xff\xfe rules")
                    for args in ((), ("--apply",)):
                        result = self.install(*args, input_text="y\n")
                        self.assertNotEqual(result.returncode, 0, result.stdout)
                        self.assertIn(f"Existing {name} {message}", result.stderr)
                    self.assertEqual(sorted(entry.name for entry in self.product.iterdir()),
                                     sorted([".git", name]))
                    if kind == "directory":
                        self.assertEqual(list(path.iterdir()), [])
                        path.rmdir()
                    else:
                        self.assertEqual(path.read_bytes(), b"\xff\xfe rules")
                        path.unlink()

    def test_warns_where_codex_would_miss_the_block(self) -> None:
        (self.product / "AGENTS.override.md").write_text("# Override\n", encoding="utf-8")
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("WARNING: AGENTS.override.md exists; Codex reads it instead of AGENTS.md",
                      preview.stdout)
        self.assertNotIn("bytes; Codex reads at most", preview.stdout)
        (self.product / "AGENTS.override.md").unlink()

        (self.product / "AGENTS.md").write_bytes(b"x" * 32000 + b"\n")
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn(f"WARNING: AGENTS.md will hold {32001 + 1 + len(BLOCK.encode('utf-8'))} bytes; Codex reads "
                      "at most 32768 bytes", preview.stdout)
        self.assertNotIn("AGENTS.override.md", preview.stdout)

    def test_warns_before_writing_paths_git_ignores(self) -> None:
        (self.product / ".gitignore").write_text(".claude/\n.agents/\n", encoding="utf-8")
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        warning = [line for line in preview.stdout.splitlines()
                   if line.startswith("WARNING: git ignores these paths")]
        self.assertEqual(len(warning), 1, preview.stdout)
        for _, name in NAMES:
            self.assertIn(f".claude/skills/the-way-{name}/SKILL.md", warning[0])
            self.assertIn(f".agents/skills/the-way-{name}/SKILL.md", warning[0])
        self.assertNotIn(".claude/rules/the-way.md", warning[0])
        self.assertNotIn("AGENTS.md", warning[0])
        self.assertNotIn("foundations/", warning[0])
        # A warning, not a refusal: the run goes on and shows it before asking.
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertLess(applied.stdout.index("WARNING: git ignores these paths"),
                        applied.stdout.index("Apply these changes?"))
        self.assertTrue((self.product / ".agents/skills/the-way-record-decision/SKILL.md").is_file())

        (self.product / "AGENTS.md").unlink()
        (self.product / ".gitignore").write_text("AGENTS.md\n.runs/\n", encoding="utf-8")
        preview = self.install()
        self.assertIn("WARNING: git ignores these paths in this repository, so they cannot be "
                      "committed and other clones and cloud sessions will not get them: AGENTS.md\n",
                      preview.stdout)

    def test_rejects_an_ignored_submodule_path_before_writing(self) -> None:
        # git submodule add refuses an ignored path, so the run is refused, not warned about.
        ignore = self.product / ".gitignore"
        ignore.write_bytes(b".*\n!.gitignore\n")
        for args in ((), ("--apply",)):
            result = self.install(*args, input_text="y\n")
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertIn("Git ignores .the-way in this repository", result.stderr)
        self.assertEqual(ignore.read_bytes(), b".*\n!.gitignore\n")
        self.assertEqual(sorted(path.name for path in self.product.iterdir()),
                         [".git", ".gitignore"])

    def test_guidance_finds_a_main_branch_not_called_main(self) -> None:
        self.assertEqual(command("git", "symbolic-ref", "HEAD", "refs/heads/master",
                                 cwd=self.product).returncode, 0)
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(command("git", "add", "--", "AGENTS.md", ".gitignore", ".claude", ".agents",
                                 "foundations", cwd=self.product).returncode, 0)
        self.assertEqual(command("git", "commit", "-q", "-m", "install",
                                 cwd=self.product).returncode, 0)
        clone = Path(self.temporary.name) / "clone"
        cloned = command("git", "clone", "-q", str(self.product), str(clone), cwd=SOURCE)
        self.assertEqual(cloned.returncode, 0, cloned.stderr)
        self.assertEqual(command("git", "switch", "-q", "-c", "task/x", cwd=clone).returncode, 0)
        guidance = (clone / "AGENTS.md").read_text(encoding="utf-8")
        finder = re.search(r"`(git symbolic-ref [^`]+)`", guidance).group(1).split()
        main = command(*finder, cwd=clone).stdout.strip()
        self.assertEqual(main, "origin/master")
        base = command("git", "merge-base", "HEAD", main, cwd=clone)
        self.assertEqual(base.returncode, 0, base.stderr)
        onto = command("git", "rev-parse", main, cwd=clone).stdout.strip()
        self.assertTrue(command("git", "-c", "protocol.file.allow=always", "submodule", "update",
                                "--init", "--", ".the-way", cwd=clone).returncode == 0)
        guard = command(sys.executable, "-B", ".the-way/elements/decisions/format_guard.py",
                        "foundations/decisions.md", "--base", base.stdout.strip(),
                        "--merge-onto", onto, cwd=clone)
        self.assertEqual(guard.returncode, 0, guard.stdout + guard.stderr)
        self.assertNotIn("--base none", guard.stdout)
        self.assertNotIn("--merge-onto none", guard.stdout)

    def test_declined_apply_writes_nothing(self) -> None:
        result = self.install("--apply", input_text="n\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Cancelled; no changes", result.stdout)
        self.assertFalse((self.product / ".gitmodules").exists())
        self.assertFalse((self.product / "foundations").exists())
        self.assertFalse((self.product / "AGENTS.md").exists())
        self.assertFalse((self.product / ".gitignore").exists())

    def test_existing_claude_import_detection_and_cancel_preserve_bytes(self) -> None:
        # invariant: installation-claude-guidance/1
        claude = self.product / "CLAUDE.md"
        cases = (
            (b"@AGENTS.md\r\n# Guidance\r\n", False),
            (b"Read @AGENTS.md for shared guidance.\n", False),
            (b"`@AGENTS.md`\n", True),
            (b"``@AGENTS.md``\n", True),
            (b"``example ` @AGENTS.md `\n", True),
            (b"~~~markdown\n@AGENTS.md\n~~~\n", True),
            (b"```markdown\n@AGENTS.md\n````\n", True),
            (b"```\nexample\n```\n@AGENTS.md\n", False),
            (b"@AGENTS.md.backup\n", True),
            (b"@AGENTS.md,\n", True),
            (b"# Local instructions only\r\n", True),
        )
        for original, warns in cases:
            with self.subTest(original=original):
                claude.write_bytes(original)
                before = self.product_files()
                preview = self.install()
                cancelled = self.install("--apply", input_text="n\n")
                for result in (preview, cancelled):
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("KEEP CLAUDE.md", result.stdout)
                    self.assertEqual("WARNING:" in result.stdout, warns, result.stdout)
                    if warns:
                        self.assertIn("@AGENTS.md", result.stdout)
                self.assertIn("Cancelled; no changes", cancelled.stdout)
                if warns:
                    self.assertLess(cancelled.stdout.index("WARNING:"),
                                    cancelled.stdout.index("Apply these changes?"))
                self.assertEqual(before, self.product_files())
                self.assertEqual(claude.read_bytes(), original)

    def test_warns_for_ignored_new_claude_import(self) -> None:
        # invariant: installation-claude-guidance/1
        (self.product / ".gitignore").write_bytes(b"CLAUDE.md\n")
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("WARNING: git ignores these paths", preview.stdout)
        self.assertIn("CLAUDE.md", preview.stdout.split("WARNING:")[1])
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertLess(applied.stdout.index("WARNING:"), applied.stdout.index("Apply these changes?"))
        self.assertEqual((self.product / "CLAUDE.md").read_bytes(), b"@AGENTS.md\n")

    def test_rejects_claude_directory_before_writing(self) -> None:
        # invariant: installation-claude-guidance/1
        claude = self.product / "CLAUDE.md"
        claude.mkdir()
        for args in ((), ("--apply",)):
            result = self.install(*args, input_text="y\n")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Existing CLAUDE.md is not a regular file", result.stderr)
        self.assertEqual(list(claude.iterdir()), [])
        self.assertEqual(sorted(path.name for path in self.product.iterdir()), [".git", "CLAUDE.md"])

    def test_rejects_claude_invalid_utf8_before_writing(self) -> None:
        # invariant: installation-claude-guidance/1
        claude = self.product / "CLAUDE.md"
        claude.write_bytes(b"\xff\xfe rules")
        for args in ((), ("--apply",)):
            result = self.install(*args, input_text="y\n")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Existing CLAUDE.md is not UTF-8 text", result.stderr)
        self.assertEqual(claude.read_bytes(), b"\xff\xfe rules")
        self.assertEqual(sorted(path.name for path in self.product.iterdir()), [".git", "CLAUDE.md"])

    def test_rejects_symlink_at_claude_without_touching_target(self) -> None:
        # invariant: installation-claude-guidance/1
        outside = Path(self.temporary.name) / "outside.md"
        outside.write_bytes(b"@AGENTS.md\n")
        claude = self.product / "CLAUDE.md"
        try:
            claude.symlink_to(outside)
        except OSError as error:
            self.skipTest(f"Symlinks unavailable: {error}")
        for args in ((), ("--apply",)):
            result = self.install(*args, input_text="y\n")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Existing CLAUDE.md is not a regular file", result.stderr)
        self.assertTrue(claude.is_symlink())
        self.assertEqual(outside.read_bytes(), b"@AGENTS.md\n")
        self.assertEqual(sorted(path.name for path in self.product.iterdir()), [".git", "CLAUDE.md"])

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
