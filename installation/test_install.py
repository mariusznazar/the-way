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
         ("task-cycle/spec/SKILL.md", "write-spec"),
         ("task-cycle/change/SKILL.md", "make-change"),
         ("task-cycle/review/SKILL.md", "review-change"),
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
            # The gitlink records the commit; an entry point that named it would change with
            # every move of the pin.
            self.assertIsNone(re.search(r"\b[0-9a-f]{7,40}\b", text), text)
            self.assertIn(f".the-way/{path}", text)
            self.assertIn("and read a file it names inside `.the-way` when the step or variant "
                          "that names it comes, not all of them at the start", text)
            self.assertNotIn("Read the files it references", text)
            self.assertIn("git ls-files --stage -- .the-way", text)
            self.assertIn("git -C .the-way rev-parse HEAD", text)
            self.assertIn("use this product's project skill of the same name with the "
                          "`the-way-` prefix, never an unprefixed one", text)
            for _, sibling in NAMES:
                self.assertIn(f"`{sibling}`", text)
        # invariant: installation-claude-guidance
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
                         "which runs `python -B .the-way/elements/common/foundation_check.py` "
                         "too", ".runs/",
                         "claimed by no part", "`the-way-update-part-map`", "never a pass",
                         "even where an installed plugin offers methods of its own"):
            self.assertIn(fragment, guidance)
        for _, name in NAMES:
            self.assertIn(f"`the-way-{name}`", guidance)
        self.assertTrue(BLOCK.startswith("<!-- the-way:begin -->\n" + guidance))
        self.assertTrue(BLOCK.endswith("<!-- the-way:end -->\n"))

    def test_guidance_names_only_scripts_the_pinned_commit_holds(self) -> None:
        # A script the guidance names but the pinned commit lacks leaves a product's agents with
        # a command that cannot run.
        paths = re.findall(r"\.the-way/([\w./-]+\.py)", install.product_guidance())
        self.assertTrue(paths)
        for path in paths:
            found = command("git", "cat-file", "-e", f"{self.commit}:{path}", cwd=SOURCE)
            self.assertEqual(found.returncode, 0, f"{path} is not in {self.commit}")

    def installed_from_a_remote(self) -> Path:
        """Install from a bare remote of the-way, commit the product and return the remote."""
        remote = Path(self.temporary.name) / "remote.git"
        cloned = command("git", "clone", "-q", "--bare", str(SOURCE), str(remote), cwd=SOURCE)
        self.assertEqual(cloned.returncode, 0, cloned.stderr)
        agents = self.product / "AGENTS.md"
        agents.write_bytes(b"# Product rules\r\n")
        mine = self.product / ".claude/skills/the-way-mine/SKILL.md"
        mine.parent.mkdir(parents=True)
        mine.write_bytes(b"---\nname: the-way-mine\n---\n\nThe product's own skill.\n")
        applied = command(sys.executable, "-B", str(INSTALL), str(self.product), "--url",
                          str(remote), "--apply", cwd=self.product, input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        agents.write_bytes(agents.read_bytes() + b"\r\nMore rules.\r\n")
        added = command("git", "add", "--", "AGENTS.md", "CLAUDE.md", ".gitignore", ".claude",
                        ".agents", "foundations", cwd=self.product)
        self.assertEqual(added.returncode, 0, added.stderr)
        self.assertEqual(command("git", "commit", "-q", "-m", "install",
                                 cwd=self.product).returncode, 0)
        return remote

    def later_process(self, remote: Path, change, publish: bool = True) -> tuple[Path, str]:
        """A later commit of the-way, published to the remote unless told otherwise: the
        installer under test, which the first run used too, and whatever `change` does."""
        later = Path(self.temporary.name) / "later"
        cloned = command("git", "clone", "-q", str(remote), str(later), cwd=SOURCE)
        self.assertEqual(cloned.returncode, 0, cloned.stderr)
        shutil.copyfile(INSTALL, later / "installation" / "install.py")
        change(later)
        for args in (("add", "-A"),
                     ("-c", "user.email=test@example.invalid", "-c", "user.name=Later", "commit",
                      "-q", "--allow-empty", "-m", "Later process"),
                     ("push", "-q", "origin", "HEAD:refs/heads/later")):
            if args[0] == "push" and not publish:
                continue
            step = command("git", *args, cwd=later)
            self.assertEqual(step.returncode, 0, step.stderr)
        return later, command("git", "rev-parse", "HEAD", cwd=later).stdout.strip()

    def move_pin(self, later: Path) -> subprocess.CompletedProcess[str]:
        # The route installation/README.md gives: the installer of a checkout at the new commit,
        # with the product's own URL, then the same with --apply.
        script = str(later / "installation" / "install.py")
        before = self.state()
        preview = command(sys.executable, "-B", script, str(self.product), cwd=self.product)
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        self.assertIn("Preview only", preview.stdout)
        # The preview moves nothing: the gitlink, the checkout and every product file stay.
        self.assertEqual(before, self.state())
        self.preview = preview.stdout
        return command(sys.executable, "-B", script, str(self.product), "--apply",
                       cwd=self.product, input_text="y\n")

    def state(self) -> tuple:
        return (command("git", "status", "--porcelain", "--untracked-files=all",
                        cwd=self.product).stdout,
                command("git", "-C", ".the-way", "rev-parse", "HEAD", cwd=self.product).stdout,
                command("git", "-C", ".the-way", "status", "--porcelain", cwd=self.product).stdout,
                self.product_files())

    def assert_pinned(self, commit: str) -> None:
        self.assertEqual(command("git", "-C", ".the-way", "rev-parse", "HEAD",
                                 cwd=self.product).stdout.strip(), commit)
        self.assertIn(f"160000 {commit}", command("git", "ls-files", "--stage", "--", ".the-way",
                                                   cwd=self.product).stdout)

    def test_moving_the_pin_to_the_same_process_changes_only_the_gitlink(self) -> None:
        remote = self.installed_from_a_remote()
        later, moved = self.later_process(remote, lambda later: None)
        result = self.move_pin(later)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"MOVE .the-way from {self.commit} to {moved}", result.stdout)
        self.assertNotIn("older than the pin", self.preview)
        self.assert_pinned(moved)
        status = command("git", "status", "--porcelain", cwd=self.product).stdout
        self.assertEqual(status.splitlines(), ["M  .the-way"])
        self.assertEqual(command("git", "commit", "-q", "-m", "move",
                                 cwd=self.product).returncode, 0)

        # Back to the earlier commit: the preview says the pin goes back.
        back = command(sys.executable, "-B", str(INSTALL), str(self.product), "--url",
                       str(remote), cwd=self.product)
        self.assertEqual(back.returncode, 0, back.stdout + back.stderr)
        self.assertIn(f"MOVE .the-way from {moved} to {self.commit} (older than the pin)",
                      back.stdout)

    def test_a_commit_the_url_does_not_reach_is_not_pinned(self) -> None:
        remote = self.installed_from_a_remote()
        later, moved = self.later_process(remote, lambda later: None, publish=False)
        before = self.state()
        result = self.move_pin(later)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(f"Commit {moved} is not available from", result.stderr)
        self.assertEqual(before, self.state())

    def test_uncommitted_changes_in_the_checkout_stop_the_move(self) -> None:
        remote = self.installed_from_a_remote()
        later, moved = self.later_process(remote, lambda later: None)
        changed = self.product / ".the-way" / "agent-instructions" / "README.md"
        original = changed.read_bytes()
        changed.write_bytes(original + b"\nA local edit.\n")
        (self.product / ".the-way" / "LOCAL_NOTE").write_text("note\n", encoding="utf-8")
        before = self.state()
        script = str(later / "installation" / "install.py")
        for args in ((), ("--apply",)):
            refused = command(sys.executable, "-B", script, str(self.product), *args,
                              cwd=self.product, input_text="y\n")
            self.assertNotEqual(refused.returncode, 0, refused.stdout)
            self.assertIn(".the-way has uncommitted changes", refused.stderr)
            self.assertIn("agent-instructions/README.md", refused.stderr)
            self.assertEqual(before, self.state())

        # An untracked file alone is warned about; the move goes on and keeps it.
        changed.write_bytes(original)
        result = self.move_pin(later)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("WARNING: .the-way holds files git does not track: LOCAL_NOTE",
                      self.preview)
        self.assert_pinned(moved)
        self.assertTrue((self.product / ".the-way" / "LOCAL_NOTE").is_file())

    def test_moving_the_pin_rewrites_what_the_installer_owns_in_one_run(self) -> None:
        remote = self.installed_from_a_remote()
        mine = self.product / ".claude/skills/the-way-mine/SKILL.md"
        own = mine.read_bytes()

        def change(later: Path) -> None:
            # A skill's description changes, a skill comes, a skill goes, the guidance changes.
            installer = later / "installation" / "install.py"
            text = installer.read_text(encoding="utf-8")
            for old, new in (('    "critique": "elements/common/critique/SKILL.md",\n',
                              '    "extra-skill": "task-cycle/extra/SKILL.md",\n'),
                             ('"# Pinned the-way process\\n\\n"',
                              '"# Pinned the-way process, later\\n\\n"')):
                self.assertEqual(text.count(old), 1, old)
                text = text.replace(old, new)
            installer.write_text(text, encoding="utf-8", newline="\n")
            skill = later / "task-cycle" / "change" / "SKILL.md"
            text = skill.read_text(encoding="utf-8")
            skill.write_text(re.sub(r"^(description: .+)$", r"\1 Changed later.", text, count=1,
                                    flags=re.M), encoding="utf-8", newline="\n")
            extra = later / "task-cycle" / "extra" / "SKILL.md"
            extra.parent.mkdir()
            extra.write_text("---\nname: extra-skill\ndescription: Use for extra work.\n---\n",
                             encoding="utf-8", newline="\n")

        later, moved = self.later_process(remote, change)
        result = self.move_pin(later)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assert_pinned(moved)
        for directory in (".claude", ".agents"):
            skills = self.product / directory / "skills"
            changed = (skills / "the-way-make-change" / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Changed later. Use this product's pinned the-way commit.", changed)
            self.assertIn("`extra-skill`", changed)
            self.assertNotIn("`critique`", changed)
            self.assertIn("Use for extra work.",
                          (skills / "the-way-extra-skill" / "SKILL.md").read_text(encoding="utf-8"))
            self.assertFalse((skills / "the-way-critique").exists())
        self.assertEqual(mine.read_bytes(), own)
        agents = (self.product / "AGENTS.md").read_bytes()
        self.assertTrue(agents.startswith(b"# Product rules\r\n\r\n<!-- the-way:begin -->\r\n"
                                          b"# Pinned the-way process, later\r\n"), agents)
        self.assertTrue(agents.endswith(b"<!-- the-way:end -->\r\n\r\nMore rules.\r\n"), agents)
        self.assertEqual(agents.count(b"<!-- the-way:begin -->"), 1)
        status = command("git", "status", "--porcelain", "--untracked-files=all",
                         cwd=self.product).stdout.splitlines()
        self.assertIn("M  .the-way", status)
        for line in status:
            self.assertRegex(line[3:], r"^(\.the-way|AGENTS\.md|\.(claude|agents)/skills/"
                                       r"the-way-(?!mine/)[a-z-]+/SKILL\.md)$", status)
        repeated = command(sys.executable, "-B", str(later / "installation" / "install.py"),
                           str(self.product), "--apply", cwd=self.product, input_text="y\n")
        self.assertEqual(repeated.returncode, 0, repeated.stdout + repeated.stderr)
        self.assertIn("Already installed; no changes", repeated.stdout)

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

    def test_rewrites_a_different_block_in_place(self) -> None:
        agents = self.product / "AGENTS.md"
        earlier = BLOCK.replace("Pinned the-way process", "Old the-way process")
        agents.write_bytes(("# Rules\n\n" + earlier + "\nMore rules.\n").encode("utf-8"))
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("REPLACE AGENTS.md", preview.stdout)
        self.assertIn("-# Old the-way process\n+# Pinned the-way process\n", preview.stdout)
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(agents.read_bytes(),
                         ("# Rules\n\n" + BLOCK + "\nMore rules.\n").encode("utf-8"))

    def test_a_rewritten_block_counts_the_new_file_only_against_the_codex_limit(self) -> None:
        agents = self.product / "AGENTS.md"
        earlier = BLOCK.replace("Pinned the-way process", "Old the-way process")
        # The rewritten file stays under the limit; the old and new text together would not.
        filler = "x" * (32 * 1024 - len(BLOCK.encode("utf-8")) - 100) + "\n\n"
        agents.write_bytes((filler + earlier).encode("utf-8"))
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertIn("REPLACE AGENTS.md", preview.stdout)
        self.assertNotIn("Codex reads at most", preview.stdout)

    def test_rejects_agents_file_with_broken_block_before_writing(self) -> None:
        agents = self.product / "AGENTS.md"
        for content, message in (
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

    def test_rewrites_an_entry_point_of_its_own(self) -> None:
        # An entry point that points to .the-way is the installer's, whatever commit wrote it.
        earlier = install.skill_wrapper("elements/decisions/skill/SKILL.md", "record-decision",
                                        self.commit).replace(
            "at the commit its gitlink records.", "at an earlier commit.")
        for directory in (".claude", ".agents"):
            wrapper = self.product / directory / "skills/the-way-record-decision/SKILL.md"
            wrapper.parent.mkdir(parents=True)
            wrapper.write_text(earlier, encoding="utf-8", newline="\n")
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertIn("REPLACE .claude/skills/the-way-record-decision/SKILL.md", applied.stdout)
        for directory in (".claude", ".agents"):
            wrapper = self.product / directory / "skills/the-way-record-decision/SKILL.md"
            self.assertEqual(wrapper.read_text(encoding="utf-8"),
                             install.skill_wrapper("elements/decisions/skill/SKILL.md",
                                                   "record-decision", self.commit))

    def test_a_file_without_every_mark_of_an_entry_point_is_the_products(self) -> None:
        # Only a file with the entry point's name, description and sentence is the installer's.
        own = install.skill_wrapper("elements/decisions/skill/SKILL.md", "record-decision",
                                    self.commit).replace("at the commit its gitlink records.",
                                                         "at an earlier commit.")
        wrapper = self.product / ".claude/skills/the-way-record-decision/SKILL.md"
        wrapper.parent.mkdir(parents=True)
        for content in (own.replace("name: the-way-record-decision", "name: the-way-other"),
                        own.replace(" Use this product's pinned the-way commit.", "")):
            wrapper.write_text(content, encoding="utf-8", newline="\n")
            result = self.install("--apply", input_text="y\n")
            self.assertNotEqual(result.returncode, 0, result.stdout)
            self.assertIn("Existing integration file differs", result.stderr)
            self.assertEqual(wrapper.read_text(encoding="utf-8"), content)
        wrapper.unlink()
        gone = self.product / ".claude/skills/the-way-gone/SKILL.md"
        gone.parent.mkdir(parents=True)
        kept = own.replace("name: the-way-record-decision", "name: the-way-elsewhere")
        gone.write_text(kept, encoding="utf-8", newline="\n")
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertEqual(gone.read_text(encoding="utf-8"), kept)

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

    def test_declined_apply_writes_nothing(self) -> None:
        result = self.install("--apply", input_text="n\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Cancelled; no changes", result.stdout)
        self.assertFalse((self.product / ".gitmodules").exists())
        self.assertFalse((self.product / "foundations").exists())
        self.assertFalse((self.product / "AGENTS.md").exists())
        self.assertFalse((self.product / ".gitignore").exists())

    def test_existing_claude_import_detection_and_cancel_preserve_bytes(self) -> None:
        # invariant: installation-claude-guidance
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
        # invariant: installation-claude-guidance
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
        # invariant: installation-claude-guidance
        claude = self.product / "CLAUDE.md"
        claude.mkdir()
        for args in ((), ("--apply",)):
            result = self.install(*args, input_text="y\n")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Existing CLAUDE.md is not a regular file", result.stderr)
        self.assertEqual(list(claude.iterdir()), [])
        self.assertEqual(sorted(path.name for path in self.product.iterdir()), [".git", "CLAUDE.md"])

    def test_rejects_claude_invalid_utf8_before_writing(self) -> None:
        # invariant: installation-claude-guidance
        claude = self.product / "CLAUDE.md"
        claude.write_bytes(b"\xff\xfe rules")
        for args in ((), ("--apply",)):
            result = self.install(*args, input_text="y\n")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Existing CLAUDE.md is not UTF-8 text", result.stderr)
        self.assertEqual(claude.read_bytes(), b"\xff\xfe rules")
        self.assertEqual(sorted(path.name for path in self.product.iterdir()), [".git", "CLAUDE.md"])

    def test_rejects_symlink_at_claude_without_touching_target(self) -> None:
        # invariant: installation-claude-guidance
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
        check = self.product / ".the-way" / "elements" / "common" / "foundation_check.py"
        result = command(sys.executable, "-B", str(check), str(self.product), cwd=self.product)
        # An empty map assigns no file to a part yet, so the check reports each file git tracks
        # as claimed by no part; it reports nothing about the form of the empty foundation files.
        errors = result.stdout.splitlines()[:-1]
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(".gitmodules: no part claims it: give it to a part or list it as left out "
                      "on purpose", errors)
        self.assertIn(".the-way: no part claims it: give it to a part or list it as left out on "
                      "purpose", errors)
        for line in errors:
            self.assertIn(": no part claims it:", line)

    def test_empty_foundations_are_in_the_current_form(self) -> None:
        # A foundation in an earlier form is what the migration rewrites; on the installer's
        # empty files it finds nothing to change.
        applied = self.install("--apply", input_text="y\n")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        migrate = self.product / ".the-way" / "elements" / "common" / "migrate_foundation.py"
        report = Path(self.temporary.name) / "migration.md"
        result = command(sys.executable, "-B", str(migrate), str(self.product), "--report",
                         str(report), cwd=self.product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("trial run, nothing written: 0 changes in 0 files, 0 files removed; "
                      "0 places for a human", result.stdout)

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
