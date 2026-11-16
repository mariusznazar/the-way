"""Tests of the invariant element-directory-contents: where {merge-onto} exists, every element
directory holds a template, examples or a pointer to entries of the-way that serve as its examples,
and a skill (WAY-09).

An element directory is a directory directly under `elements/` that is the directory of one of the
foundation's elements: every one but `common`, the directory of the part the elements share
(`elements-common`), which holds their rules and no element. A directory holds:

- a template: the file `template.md`;
- examples: the file `examples.md`, or a pointer, the section `## Examples` of the template naming a
  file of `foundations/` that git tracks, in backticks (the template of the environment facts
  points to `foundations/environment_facts.md` so);
- a skill: the file `skill/SKILL.md`.

{merge-onto} is the tip of the main branch (`elements/common/rules.md`), which is the first of
`MAIN_BRANCHES` of `foundation_source.py` that exists. Where none exists, the sentence of the
invariant says nothing and the test is skipped, with its reason, which the run names.

The test reads the files git tracks and the working tree holds, so a directory that a change adds is
checked as the change leaves it.

Run from the root of the-way: python -B gate/run_tests.py elements/common
"""

import os
import re
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
THE_WAY = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

from foundation_source import MAIN_BRANCHES, git  # noqa: E402

# The elements named by the *Part* of the invariant, which the test finds among the directories.
ELEMENTS = ("decisions", "part-map", "invariants", "glossary", "environment-facts")
# The directory under `elements/` that is no element's.
SHARED = "common"
EXAMPLES_HEADING = re.compile(r"^## Examples\s*$", re.MULTILINE)
FOUNDATION_FILE = re.compile(r"`(foundations/[\w./-]+\.md)`")
# Git with the configuration of the user and of the system shut out, for the repositories a test
# builds (WAY-400).
CLEAN_GIT = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")


def tracked_files(root):
    """The paths git tracks in the repository at `root`, written with `/`."""
    run = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True)
    return [name for name in run.stdout.decode("utf-8").split("\0") if name]


def merge_onto_exists(root):
    """Whether one of the branches that may be the main branch exists in the repository."""
    for branch in MAIN_BRANCHES:
        code, tip = git(root, "rev-parse", "--verify", "--quiet", branch + "^{commit}")
        if code == 0 and tip.strip():
            return True
    return False


def element_directories(paths):
    """The names of the directories under `elements/` that hold a tracked file, without the
    directory of the part the elements share."""
    names = {path.split("/")[1] for path in paths
             if path.startswith("elements/") and path.count("/") >= 2}
    return sorted(names - {SHARED})


def pointer(root, base, known):
    """The file of `foundations/` among the tracked paths `known` that the section `## Examples` of
    the template of the element directory `base` names, or None."""
    try:
        with open(os.path.join(root, *base.split("/"), "template.md"), encoding="utf-8") as handle:
            text = handle.read()
    except OSError:
        return None
    start = EXAMPLES_HEADING.search(text)
    if not start:
        return None
    rest = text[start.end():]
    following = re.search(r"^## ", rest, re.MULTILINE)
    section = rest[:following.start()] if following else rest
    return next((name for name in FOUNDATION_FILE.findall(section) if name in known), None)


def missing(root, tracked):
    """(directory, what it lacks) for each thing an element directory lacks, `what` being
    "template", "examples" or "skill", in the order of the directories."""
    known = set(tracked)
    lacking = []
    for name in element_directories(tracked):
        base = "elements/%s" % name
        if base + "/template.md" not in known:
            lacking.append((base, "template"))
        if base + "/examples.md" not in known and not pointer(root, base, known):
            lacking.append((base, "examples"))
        if base + "/skill/SKILL.md" not in known:
            lacking.append((base, "skill"))
    return lacking


class ElementDirectoryContents(unittest.TestCase):

    def test_every_element_directory_holds_a_template_examples_or_a_pointer_and_a_skill(self):
        # invariant: element-directory-contents
        if not merge_onto_exists(THE_WAY):
            self.skipTest("no main branch exists, so {merge-onto} does not and the invariant "
                          "says nothing")
        paths = tracked_files(THE_WAY)
        self.assertTrue(set(ELEMENTS) <= set(element_directories(paths)),
                        "git lists the directories of the five elements under elements/")
        self.assertEqual([], missing(THE_WAY, paths),
                         "element directories that lack a template, examples or a pointer to "
                         "examples (the section `## Examples` of the template naming a file of "
                         "foundations/ in backticks), or a skill/SKILL.md")


class Missing(unittest.TestCase):
    """What an element directory lacks, on small directories made for each case.

    The data of each case, a directory with some of the three things the sentence of
    element-directory-contents names (a template, examples or a pointer to examples, a skill), is
    made of the names `template.md`, `examples.md` and `skill/SKILL.md` that the invariant's entry
    and the elements' directories in this repository give; the pointer is the form of the section
    `## Examples` of `elements/environment-facts/template.md`."""

    def directory(self, files):
        """A directory holding `files`, a text for each name, and the list of their names."""
        made = tempfile.TemporaryDirectory()
        self.addCleanup(made.cleanup)
        for path, text in files.items():
            full = os.path.join(made.name, *path.split("/"))
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        return made.name, sorted(files)

    def test_a_directory_with_a_template_examples_and_a_skill_lacks_nothing(self):
        root, paths = self.directory({"elements/facts/template.md": "# T\n",
                                      "elements/facts/examples.md": "# E\n",
                                      "elements/facts/skill/SKILL.md": "# S\n"})
        self.assertEqual([], missing(root, paths))

    def test_a_template_that_points_to_a_tracked_foundation_file_stands_for_examples(self):
        template = ("# T\n\n## Examples\n\nThe entries of `foundations/facts.md` serve as this "
                    "element's examples.\n\n## Other\n")
        root, paths = self.directory({"elements/facts/template.md": template,
                                      "foundations/facts.md": "# Facts\n",
                                      "elements/facts/skill/SKILL.md": "# S\n"})
        self.assertEqual([], missing(root, paths))

    def test_a_pointer_to_a_file_git_does_not_track_stands_for_no_examples(self):
        template = "# T\n\n## Examples\n\nThe entries of `foundations/facts.md` serve.\n"
        root, paths = self.directory({"elements/facts/template.md": template,
                                      "elements/facts/skill/SKILL.md": "# S\n"})
        self.assertEqual([("elements/facts", "examples")], missing(root, paths))

    def test_a_pointer_outside_the_section_of_examples_stands_for_no_examples(self):
        template = ("# T\n\n## Examples\n\nNone yet.\n\n## Links\n\nSee `foundations/facts.md`.\n")
        root, paths = self.directory({"elements/facts/template.md": template,
                                      "foundations/facts.md": "# Facts\n",
                                      "elements/facts/skill/SKILL.md": "# S\n"})
        self.assertEqual([("elements/facts", "examples")], missing(root, paths))

    def test_a_directory_without_a_skill_is_reported(self):
        root, paths = self.directory({"elements/facts/template.md": "# T\n",
                                      "elements/facts/examples.md": "# E\n"})
        self.assertEqual([("elements/facts", "skill")], missing(root, paths))

    def test_a_directory_without_a_template_is_reported(self):
        root, paths = self.directory({"elements/facts/examples.md": "# E\n",
                                      "elements/facts/skill/SKILL.md": "# S\n"})
        self.assertEqual([("elements/facts", "template")], missing(root, paths))

    def test_a_new_directory_with_one_file_is_reported_for_the_other_two(self):
        root, paths = self.directory({"elements/new/template.md": "# T\n"})
        self.assertEqual([("elements/new", "examples"), ("elements/new", "skill")],
                         missing(root, paths))

    def test_the_directory_of_the_shared_part_is_no_element_directory(self):
        root, paths = self.directory({"elements/common/rules.md": "# R\n",
                                      "elements/common/skill/SKILL.md": "# S\n"})
        self.assertEqual([], missing(root, paths))


class MergeOntoExists(unittest.TestCase):
    """The condition of the invariant, on repositories that each hold one state of the branches.

    The states are those of `elements/common/rules.md`, section `{fork-point}`: {merge-onto} is the
    tip of the branch `refs/remotes/origin/HEAD` names, else of `main`, else of `master`, and
    reads `none` where the main branch does not exist; the branch names `foundations` and `work`
    are made up for the cases."""

    def repository(self, branch, remote_head=None):
        """A repository with one commit on `branch`, and where `remote_head` is given, the
        `origin/HEAD` that names that branch of the remote."""
        made = tempfile.TemporaryDirectory()
        self.addCleanup(made.cleanup)

        def run(*args):
            subprocess.run(["git", "-c", "user.name=test", "-c", "user.email=test@example.com",
                            *args], cwd=made.name, env=CLEAN_GIT, check=True, capture_output=True)

        run("init", "-q", "-b", branch)
        run("commit", "-q", "--allow-empty", "-m", "first")
        if remote_head:
            run("update-ref", "refs/remotes/origin/" + remote_head, "HEAD")
            run("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/" + remote_head)
        return made.name

    def test_a_repository_with_a_main_branch_has_one(self):
        self.assertTrue(merge_onto_exists(self.repository("main")))

    def test_a_repository_whose_origin_head_names_a_branch_has_one(self):
        self.assertTrue(merge_onto_exists(self.repository("work", remote_head="foundations")))

    def test_a_repository_with_branches_but_no_main_branch_has_none(self):
        self.assertFalse(merge_onto_exists(self.repository("work")))

    def test_a_repository_with_no_commit_has_none(self):
        made = tempfile.TemporaryDirectory()
        self.addCleanup(made.cleanup)
        subprocess.run(["git", "init", "-q", "-b", "main"], cwd=made.name, env=CLEAN_GIT,
                       check=True, capture_output=True)
        self.assertFalse(merge_onto_exists(made.name))


if __name__ == "__main__":
    unittest.main()
