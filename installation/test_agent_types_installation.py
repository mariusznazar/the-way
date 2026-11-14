"""Product installation checks for the definitions of the task cycle's agent types: the plan shows
them, the installer replaces and deletes only its own, and it refuses what is not its own before it
writes anything (the trust boundary of `installation`: files a product already holds)."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent.parent
INSTALL = SOURCE / "installation/install.py"
DEFINITIONS = "task-cycle/agent-types"
TYPES = ("the-way-stage", "the-way-author")
PATHS = tuple(f".claude/agents/{name}.md" for name in TYPES)
MARK = "Dispatched only by the task cycle of the-way."
EARLIER = ("---\nname: the-way-stage\ndescription: Stage agent of an earlier commit. " + MARK +
           "\n---\n\nAn earlier body.\n")


def command(*args: str, cwd: Path, input_text: str | None = None):
    return subprocess.run(args, cwd=cwd, input=input_text, text=True, encoding="utf-8",
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


class AgentTypesInstallationTest(unittest.TestCase):
    products = 0

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="the-way-agent-types-test-")
        self.addCleanup(self.temporary.cleanup)
        self.new_product("product")
        # The tests install from this clone, not from the live repository: a commit made to the-way
        # while the run goes on cannot change the commit the installer pins or the one expected.
        self.source = Path(self.temporary.name) / "source"
        cloned = command("git", "clone", "-q", str(SOURCE), str(self.source), cwd=SOURCE)
        self.assertEqual(cloned.returncode, 0, cloned.stderr)
        self.commit = self.git("rev-parse", "HEAD", cwd=self.source).stdout.strip()
        self.installer = self.source / "installation" / "install.py"
        # The installer under test is the one in the working tree, committed or not; the clone
        # supplies the source that is installed, whose commit the installer pins.
        shutil.copyfile(INSTALL, self.installer)

    def new_product(self, name: str) -> None:
        self.products += 1
        self.product = Path(self.temporary.name) / f"{name}-{self.products}"
        self.product.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Agent Types Installation Test")

    def git(self, *args: str, cwd: Path | None = None):
        result = command("git", *args, cwd=cwd or self.product)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def install(self, *args: str, answer: str = "y\n"):
        return command(sys.executable, "-B", str(self.installer), str(self.product),
                       "--url", str(self.source), *args, cwd=self.product, input_text=answer)

    def committed(self, path: str) -> str:
        return self.git("show", f"{self.commit}:{path}", cwd=self.source).stdout

    def product_tree(self):
        """Every path outside .git with the bytes of each file, so a created directory counts."""
        return {path.relative_to(self.product).as_posix():
                (path.read_bytes() if path.is_file() else None)
                for path in self.product.rglob("*")
                if path.relative_to(self.product).parts[0] != ".git"}

    def write(self, relative: str, data: bytes | str) -> Path:
        path = self.product / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)
        return path

    def test_the_installer_names_every_definition_of_the_commit_and_no_other(self) -> None:
        listed = self.git("ls-tree", "--name-only", self.commit, f"{DEFINITIONS}/",
                          cwd=self.source).stdout.split()
        self.assertEqual(sorted(listed), sorted(f"{DEFINITIONS}/{name}.md" for name in TYPES))
        sys.path.insert(0, str(SOURCE / "installation"))
        try:
            import install
        finally:
            sys.path.remove(str(SOURCE / "installation"))
        self.assertEqual(sorted(install.AGENT_TYPES), sorted(TYPES))

    def test_the_plan_shows_the_definitions_and_apply_writes_them_unchanged(self) -> None:
        before = self.product_tree()
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        for path, name in zip(PATHS, TYPES):
            self.assertIn(f"CREATE {path}\n", preview.stdout)
            self.assertIn(f"+name: {name}\n", preview.stdout)
            self.assertIn("+disallowedTools: Skill\n", preview.stdout)
        self.assertIn("+  cacheTtl: 1h\n", preview.stdout)
        self.assertEqual(before, self.product_tree())

        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertLess(applied.stdout.index("CREATE .claude/agents/the-way-stage.md"),
                        applied.stdout.index("Apply these changes?"))
        for path, name in zip(PATHS, TYPES):
            self.assertEqual((self.product / path).read_bytes(),
                             self.committed(f"{DEFINITIONS}/{name}.md").encode("utf-8"))
            # The copy the-way keeps for its own sessions is the same file.
            self.assertEqual(self.committed(path), self.committed(f"{DEFINITIONS}/{name}.md"))
        stage = (self.product / PATHS[0]).read_text(encoding="utf-8")
        author = (self.product / PATHS[1]).read_text(encoding="utf-8")
        self.assertNotIn("cacheTtl", stage)
        self.assertIn("experimental:\n  cacheTtl: 1h\n", author)
        self.assertFalse((self.product / ".agents" / "agents").exists())
        installed = self.product_tree()
        repeated = self.install("--apply")
        self.assertEqual(repeated.returncode, 0, repeated.stdout + repeated.stderr)
        self.assertIn("Already installed; no changes", repeated.stdout)
        self.assertEqual(installed, self.product_tree())

    def test_an_own_definition_of_an_earlier_commit_is_replaced_and_the_products_files_stay(
            self) -> None:
        self.write(PATHS[0], EARLIER)
        mine = self.write(".claude/agents/reviewer.md",
                          "---\nname: reviewer\ndescription: The product's own.\n---\nBody.\n")
        lookalike = self.write(".claude/agents/the-way-mine.md",
                               "---\nname: the-way-mine\ndescription: The product's own.\n---\n")
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        self.assertIn(f"REPLACE {PATHS[0]}\n", preview.stdout)
        self.assertIn("-An earlier body.\n", preview.stdout)
        self.assertEqual((self.product / PATHS[0]).read_text(encoding="utf-8"), EARLIER)
        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertEqual((self.product / PATHS[0]).read_bytes(),
                         self.committed(f"{DEFINITIONS}/the-way-stage.md").encode("utf-8"))
        self.assertEqual(mine.read_bytes(),
                         b"---\nname: reviewer\ndescription: The product's own.\n---\nBody.\n")
        self.assertEqual(lookalike.read_bytes(),
                         b"---\nname: the-way-mine\ndescription: The product's own.\n---\n")

    def test_the_definition_of_a_type_the_commit_lacks_is_deleted_and_only_its_own(self) -> None:
        gone = self.write(".claude/agents/the-way-gone.md",
                          EARLIER.replace("the-way-stage", "the-way-gone"))
        kept = {
            "the-way-wrong-name.md": EARLIER,
            "the-way-nomark.md": EARLIER.replace(MARK, "").replace("the-way-stage",
                                                                    "the-way-nomark"),
            "the-way-bytes.md": b"\xff\xfe" + EARLIER.encode("utf-8"),
            "other-agent.md": EARLIER.replace("the-way-stage", "other-agent"),
            "the-way-notes.txt": EARLIER.replace("the-way-stage", "the-way-notes"),
        }
        for name, content in kept.items():
            self.write(f".claude/agents/{name}", content)
        (self.product / ".claude/agents/the-way-directory.md").mkdir()
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        self.assertIn("DELETE .claude/agents/the-way-gone.md (its agent type is no longer in "
                      "the-way)\n", preview.stdout)
        self.assertEqual(preview.stdout.count("DELETE "), 1, preview.stdout)
        self.assertTrue(gone.is_file())
        applied = self.install("--apply")
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertFalse(gone.exists())
        for name, content in kept.items():
            data = content.encode("utf-8") if isinstance(content, str) else content
            self.assertEqual((self.product / ".claude/agents" / name).read_bytes(), data, name)
        self.assertTrue((self.product / ".claude/agents/the-way-directory.md").is_dir())
        self.assertTrue((self.product / PATHS[0]).is_file())

    def test_a_file_that_is_not_the_installers_at_a_definition_path_stops_the_run(self) -> None:
        own = self.committed(f"{DEFINITIONS}/the-way-stage.md")
        crafted = {
            "a user's file": "user's agent\n",
            "another name in the header": own.replace("name: the-way-stage",
                                                      "name: the-way-other"),
            "no mark in the description": own.replace(" " + MARK, ""),
            "the mark moved out of the description": own.replace(" " + MARK, "") + MARK + "\n",
            "no frontmatter": "You are an agent.\n" + MARK + "\n",
            "non-UTF-8 bytes": b"\xff\xfe user's agent\n",
            "an own definition with a non-UTF-8 byte after it": own.encode("utf-8") + b"\xff",
        }
        for kind, content in crafted.items():
            for args in ((), ("--apply",)):
                with self.subTest(crafted=kind, args=args):
                    self.new_product("crafted")
                    path = self.write(PATHS[0], content)
                    before = self.product_tree()
                    refused = self.install(*args)
                    self.assertNotEqual(refused.returncode, 0, refused.stdout + refused.stderr)
                    self.assertIn("Existing integration file differs", refused.stderr)
                    self.assertIn("the-way-stage.md", refused.stderr)
                    self.assertNotIn("Installed.", refused.stdout)
                    self.assertTrue(path.is_file())
                    self.assertEqual(before, self.product_tree())
                    self.assertEqual(self.git("ls-files", "--stage").stdout, "")

    def test_a_directory_at_a_definition_path_stops_the_run(self) -> None:
        for args in ((), ("--apply",)):
            with self.subTest(args=args):
                self.new_product("directory")
                (self.product / PATHS[1]).mkdir(parents=True)
                before = self.product_tree()
                refused = self.install(*args)
                self.assertNotEqual(refused.returncode, 0, refused.stdout + refused.stderr)
                self.assertIn("Existing integration file differs", refused.stderr)
                self.assertEqual(before, self.product_tree())

    def test_a_file_where_a_parent_directory_belongs_stops_the_run(self) -> None:
        for relative in (".claude", ".claude/agents"):
            with self.subTest(relative=relative):
                self.new_product("parent")
                self.write(relative, "not a directory\n")
                before = self.product_tree()
                refused = self.install("--apply")
                self.assertNotEqual(refused.returncode, 0, refused.stdout + refused.stderr)
                self.assertIn("Parent path is not a regular directory", refused.stderr)
                self.assertEqual(before, self.product_tree())

    def test_a_symlink_in_the_way_stops_the_run_and_its_target_is_not_touched(self) -> None:
        # invariant: installation-paths-through-links
        outside = Path(self.temporary.name) / "outside"
        outside.mkdir()
        (outside / "agent.md").write_bytes(b"outside\n")
        kinds = (
            ("a symlinked .claude", lambda: self.link(".claude", outside)),
            ("a symlinked .claude/agents", lambda: self.link(".claude/agents", outside)),
            ("a symlinked definition", lambda: self.link(PATHS[0], outside / "agent.md")),
            ("a dangling symlink at a definition", lambda: self.link(PATHS[1], outside / "none")),
        )
        for kind, make in kinds:
            for args in ((), ("--apply",)):
                with self.subTest(crafted=kind, args=args):
                    self.new_product("link")
                    make()
                    before = self.product_tree()
                    refused = self.install(*args)
                    self.assertNotEqual(refused.returncode, 0, refused.stdout + refused.stderr)
                    self.assertTrue(
                        "Parent path is not a regular directory" in refused.stderr or
                        "Existing integration file differs" in refused.stderr, refused.stderr)
                    self.assertNotIn("Installed.", refused.stdout)
                    self.assertEqual(before, self.product_tree())
                    self.assertEqual(sorted(path.name for path in outside.iterdir()),
                                     ["agent.md"])
                    self.assertEqual((outside / "agent.md").read_bytes(), b"outside\n")

    def link(self, relative: str, target: Path) -> None:
        path = self.product / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            path.symlink_to(target, target_is_directory=target.is_dir())
        except OSError as error:
            self.skipTest(f"Symlinks unavailable: {error}")

    def test_a_symlink_named_like_an_own_definition_of_a_gone_type_is_not_deleted(self) -> None:
        # invariant: installation-paths-through-links
        outside = Path(self.temporary.name) / "outside.md"
        outside.write_text(EARLIER.replace("the-way-stage", "the-way-gone"), encoding="utf-8")
        self.link(".claude/agents/the-way-gone.md", outside)
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        self.assertNotIn("DELETE", preview.stdout)
        self.assertEqual(self.install("--apply").returncode, 0)
        self.assertTrue((self.product / ".claude/agents/the-way-gone.md").is_symlink())
        self.assertIn("the-way-gone", outside.read_text(encoding="utf-8"))

    def test_the_agent_directory_that_git_ignores_is_warned_about(self) -> None:
        self.write(".gitignore", ".claude/agents/\n")
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        warning = [line for line in preview.stdout.splitlines()
                   if line.startswith("WARNING: git ignores these paths")]
        self.assertEqual(len(warning), 1, preview.stdout)
        for path in PATHS:
            self.assertIn(path, warning[0])
        self.assertNotIn(".claude/skills", warning[0])

    def install_and_commit_in_the_product(self) -> None:
        self.assertEqual(self.install("--apply").returncode, 0)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "install")

    def later_commit(self, types: tuple[str, ...]) -> None:
        """A later commit of the-way whose installer names only `types`; the body of the author's
        definition reads differently in it, and every other definition is gone."""
        for name in TYPES:
            if name not in types:
                for relative in (f"{DEFINITIONS}/{name}.md", f".claude/agents/{name}.md"):
                    (self.source / relative).unlink()
        author = self.source / DEFINITIONS / "the-way-author.md"
        if author.exists():
            author.write_bytes(author.read_bytes().replace(b"You are the one author",
                                                           b"You are the only author"))
        installer = self.installer.read_text(encoding="utf-8")
        old = 'AGENT_TYPES = ("the-way-stage", "the-way-author")'
        self.assertEqual(installer.count(old), 1)
        names = "".join(f'"{name}", ' for name in types).rstrip()
        self.installer.write_text(installer.replace(old, f"AGENT_TYPES = ({names})"),
                                  encoding="utf-8", newline="\n")
        self.git("add", "-A", cwd=self.source)
        self.git("-c", "user.email=test@example.invalid", "-c", "user.name=Later", "commit", "-q",
                 "-m", "Later process", cwd=self.source)

    def test_the_directory_of_the_definitions_stays_where_the_commit_has_none(self) -> None:
        # The installer removes the directory of a skill's entry point when it empties, never the
        # directory the product's other agents may use.
        self.install_and_commit_in_the_product()
        self.later_commit(())
        self.assertEqual(self.install("--apply").returncode, 0)
        for path in PATHS:
            self.assertFalse((self.product / path).exists())
        self.assertTrue((self.product / ".claude/agents").is_dir())

    def test_a_moved_pin_rewrites_a_definition_and_deletes_the_one_the_commit_lacks(self) -> None:
        self.install_and_commit_in_the_product()
        self.later_commit(("the-way-author",))
        preview = self.install()
        self.assertEqual(preview.returncode, 0, preview.stdout + preview.stderr)
        self.assertIn("MOVE .the-way from ", preview.stdout)
        self.assertIn(f"REPLACE {PATHS[1]}\n", preview.stdout)
        self.assertIn("-You are the one author", preview.stdout)
        self.assertIn("+You are the only author", preview.stdout)
        self.assertIn("DELETE .claude/agents/the-way-stage.md (its agent type is no longer in "
                      "the-way)\n", preview.stdout)
        self.assertEqual(self.install("--apply").returncode, 0)
        self.assertFalse((self.product / PATHS[0]).exists())
        self.assertIn("You are the only author",
                      (self.product / PATHS[1]).read_text(encoding="utf-8"))
        self.assertIn("M  .the-way", self.git("status", "--porcelain").stdout)


if __name__ == "__main__":
    unittest.main()
