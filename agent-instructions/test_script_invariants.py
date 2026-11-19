"""Tests of the invariants python-version-declared, script-language and script-imports: the
repository declares Python 3.14 in `.python-version`, every script git tracks is a Python file, and
no Python file git tracks imports a module other than one of the standard library of Python 3.14
or a Python file git tracks (WAY-38, WAY-89).

Each invariant has one test of the real checkout, a repository test, and tests of the functions that
test uses, on small inputs written out in them, so that a function that quietly sees nothing turns a
test red.

script-language: git does not say which of its files are scripts, so the test takes the other way
round (WAY-38: "a check that quietly sees nothing would pass"). A file git tracks that is a Python
file or of a kind on the lists `SUFFIXES` and `NAMES` passes, and any other file is reported as a possible
script. A kind that is no script is added to the list, with the reason, by the author of the change
that brings the first file of that kind.

script-imports: the imports are read by `imports` of `elements/part-map/test_cross_part_imports.py`,
the reader of the
invariant cross-part-imports, in the same reach: `import` and `from ... import` statements,
`importlib.import_module`, `__import__`, `runpy`, code given to `-c`, `exec`, `eval` and `compile`;
an import whose name cannot be worked out is reported. The module names of the standard library
come from `sys.stdlib_module_names` of the interpreter that runs the test, which lists the standard
library of its own version (fact python-stdlib-modules), so the test fails, naming both versions,
on an interpreter other than the version `.python-version` declares, and never takes the list of
another version.

The tests stand in `agent-instructions`, whose map sentence covers the tests of the-way's own code
rules and whose *Depends on* names `part-map` and `repository`, so the import of the reader from
`elements/part-map/` is one the map allows.

Run from the root of the-way: python -B gate/run_tests.py agent-instructions
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
THE_WAY = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "..", "elements", "part-map"))

from test_cross_part_imports import imports  # noqa: E402

# The version the invariant python-version-declared names in its sentence.
DECLARED = "3.14"
VERSION_FILE = ".python-version"

# The files a script of the repository is not, by the end of the name (SUFFIXES), by the whole name
# (NAMES) or by the place and the end of the path (PLACES), each kind with its reason; any other
# file git tracks is reported by the test of script-language as a possible script (settlement of the
# task: a list of the kinds that are no script, not a list of the kinds that are).
SUFFIXES = (
    ".py",  # a Python file, the language of every script (WAY-38)
    ".md",  # text for people and agents; a command written in it, as in a skill, is no script
)
PLACES = (
    # data: the CI configuration names the commands CI runs, which `ci-checking-commands` keeps
    (".github/workflows/", ".yml"),
)
NAMES = (
    ".gitignore",  # the patterns git ignores
    ".gitattributes",  # the attributes git gives paths
    ".python-version",  # the declared version of Python
    "ruff.toml",  # the configuration of the linter, data in TOML
    "requirements-quality.in",  # the packages the linter is installed from, one name to a line
    "requirements-quality.txt",  # the same with the sums of their files, for `pip`
)


def tracked_files(root):
    """The paths git tracks in the repository at `root`, written with `/`."""
    run = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True)
    return [name for name in run.stdout.decode("utf-8").split("\0") if name]


def possible_scripts(paths):
    """The paths that are neither a Python file nor of a kind the list gives as no script."""
    return [
        path
        for path in paths
        if path.rpartition("/")[2] not in NAMES
        and not path.endswith(SUFFIXES)
        and not any(path.startswith(place) and path.endswith(end) for place, end in PLACES)
    ]


def declared_lines(root):
    """The lines of `.python-version`, without the empty ones, or None where it does not exist."""
    try:
        with open(os.path.join(root, VERSION_FILE), encoding="utf-8") as handle:
            return [line.strip() for line in handle.read().splitlines() if line.strip()]
    except OSError:
        return None


def wrong_interpreter(declared, running):
    """The message of a test run on another version than the declared one, or None where the
    versions of Python are the same in major and minor number; `declared` is None where
    `.python-version` is missing or holds no version, which the message names."""
    if declared is None:
        return (
            "%s is missing or holds no version, so the version of Python the tests have to run "
            "on is not declared (this run is on Python %s)" % (VERSION_FILE, running)
        )
    if declared.split(".")[:2] == running.split(".")[:2]:
        return None
    return (
        "the tests have to run on Python %s, the version %s declares, and this run is on "
        "Python %s: the standard library of a version other than the declared one would "
        "decide the imports" % (declared, VERSION_FILE, running)
    )


def outside_imports(root, paths):
    """The problems `imports` reports for the Python files among `paths`: an import of a module
    that is neither of the standard library of the running interpreter nor a file of `paths`, and
    an import or a run the reader cannot work out."""
    known = set(paths)
    problems = []
    for path in paths:
        if path.endswith(".py"):
            problems += imports(root, path, known)[1]
    return problems


class PythonVersionDeclared(unittest.TestCase):
    def test_the_repository_declares_python_3_14_in_python_version(self):
        # invariant: python-version-declared
        self.assertIn(VERSION_FILE, tracked_files(THE_WAY))
        lines = declared_lines(THE_WAY)
        self.assertEqual(1, len(lines or []), "%s holds one line" % VERSION_FILE)
        self.assertTrue(
            lines[0] == DECLARED or lines[0].startswith(DECLARED + "."),
            "%s declares %r, not Python %s" % (VERSION_FILE, lines[0], DECLARED),
        )


class ScriptLanguage(unittest.TestCase):
    def test_every_file_git_tracks_is_a_python_file_or_of_a_kind_that_is_no_script(self):
        # invariant: script-language
        paths = tracked_files(THE_WAY)
        self.assertIn("gate/run_tests.py", paths, "git lists the files of the repository")
        self.assertEqual(
            [],
            possible_scripts(paths),
            "files that are no Python file and of no kind on the lists SUFFIXES and "
            "NAMES of the test; a script among them is rewritten in Python, a file "
            "that is no script has its kind added to a list, with the reason",
        )

    def test_a_file_of_another_language_is_reported(self):
        # The names are those of the scripts of the languages a repository usually holds.
        paths = [
            "tools/build.sh",
            "tools/deploy.ps1",
            "run.bat",
            "web/app.js",
            "bin/start",
            "Makefile",
            "lib/helper.rb",
            "tools/old.py.bak",
        ]
        self.assertEqual(paths, possible_scripts(paths))

    def test_a_python_file_a_text_and_a_file_of_the_listed_kinds_pass(self):
        # The names are those the lists give: the task's list of kinds (.py, .md, .gitignore,
        # .gitattributes, .python-version) and the four kinds the change added, each in a file that
        # git tracks in this repository.
        paths = [
            "gate/run_tests.py",
            "agent-instructions/skill.md",
            ".gitignore",
            "sub/.gitignore",
            ".gitattributes",
            ".python-version",
            "ruff.toml",
            "requirements-quality.in",
            "requirements-quality.txt",
            ".github/workflows/tests.yml",
        ]
        self.assertEqual([], possible_scripts(paths))

    def test_a_configuration_file_outside_the_place_of_its_kind_is_reported(self):
        # A `.yml` file passes only under `.github/workflows/`: a playbook in the root would run
        # commands no invariant keeps.
        paths = ["tools_deploy.yml", "docs/deploy.yml", ".github/workflows/notes.md.sh"]
        self.assertEqual(paths, possible_scripts(paths))

    def test_a_file_named_like_a_listed_kind_in_its_ending_only_is_reported(self):
        # `ruff.toml` is listed by its name, so another `.toml` file is no listed kind.
        self.assertEqual(
            ["tools/other.toml", "docs/ruff.toml.sh"],
            possible_scripts(["tools/other.toml", "docs/ruff.toml.sh"]),
        )


class ScriptImports(unittest.TestCase):
    def test_no_python_file_git_tracks_imports_a_module_outside_the_standard_library(self):
        # invariant: script-imports
        running = "%d.%d" % sys.version_info[:2]
        lines = declared_lines(THE_WAY)
        declared = lines[0] if lines else None
        refusal = wrong_interpreter(declared, running)
        if refusal:
            self.fail(refusal)
        paths = tracked_files(THE_WAY)
        self.assertIn("gate/run_tests.py", paths, "git lists the files of the repository")
        self.assertEqual([], outside_imports(THE_WAY, paths))

    def test_an_interpreter_of_another_version_is_refused_with_both_versions(self):
        # Python 3.12 against the declared 3.14: the lists of module names of the two differ
        # (`cgi` only in 3.12, `annotationlib` only in 3.14), so a verdict on 3.12 would not
        # be the one of the invariant.
        message = wrong_interpreter("3.14", "3.12")
        self.assertIn("3.14", message)
        self.assertIn("3.12", message)

    def test_a_missing_declaration_is_refused_by_naming_the_file(self):
        message = wrong_interpreter(None, "3.14")
        self.assertIn(VERSION_FILE, message)
        self.assertIn("missing", message)

    def test_the_declared_version_and_a_patch_release_of_it_are_accepted(self):
        # The patch release `3.14.3` declares Python 3.14, as the sentence of
        # python-version-declared reads it; a run on 3.14 is the version the invariant names.
        self.assertIsNone(wrong_interpreter("3.14", "3.14"))
        self.assertIsNone(wrong_interpreter("3.14.3", "3.14"))

    def test_a_module_outside_the_standard_library_is_reported_in_each_form_of_import(self):
        # The six forms are those of the reach settlement row 3 names: an import statement, a
        # from-import, `importlib.import_module`, `__import__`, code given to `-c` and to `exec`.
        forms = {
            "a.py": "import yaml\n",
            "b.py": "from yaml import safe_load\n",
            "c.py": "import importlib\nimportlib.import_module('yaml')\n",
            "d.py": "__import__('yaml')\n",
            "e.py": "import subprocess, sys\nsubprocess.run([sys.executable, '-c', 'import yaml'])\n",
            "f.py": "exec('import yaml')\n",
        }
        for path, text in forms.items():
            with self.subTest(path=path), tempfile.TemporaryDirectory() as root:
                with open(os.path.join(root, path), "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(text)
                problems = outside_imports(root, [path])
                self.assertEqual(1, len(problems), problems)
                self.assertIn("yaml", problems[0])

    def test_a_module_of_the_standard_library_and_a_tracked_file_are_no_failure(self):
        with tempfile.TemporaryDirectory() as root:
            files = {
                "helper.py": "VALUE = 1\n",
                "main.py": "import json\nimport os.path\nimport helper\n"
                "import importlib\nimportlib.import_module('helper')\n",
            }
            for path, text in files.items():
                with open(os.path.join(root, path), "w", encoding="utf-8", newline="\n") as handle:
                    handle.write(text)
            self.assertEqual([], outside_imports(root, sorted(files)))

    def test_an_import_whose_name_cannot_be_worked_out_is_reported(self):
        with tempfile.TemporaryDirectory() as root:
            with open(os.path.join(root, "a.py"), "w", encoding="utf-8", newline="\n") as handle:
                handle.write(
                    "import importlib, os\nimportlib.import_module(os.environ['MODULE'])\n"
                )
            problems = outside_imports(root, ["a.py"])
            # One report, at the line of the call (settlement row 3: reported, not passed).
            self.assertEqual(1, len(problems), problems)
            self.assertTrue(problems[0].startswith("a.py:2:"), problems)


if __name__ == "__main__":
    unittest.main()
