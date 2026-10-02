"""Tests of how the gate reads the script a command runs (WAY-105).

Each form of a command is written out with the script a POSIX shell and the Python interpreter
would run for it, so that a word the command passes to an option, or to the script itself, is never
taken for the script.

Run from the root of the-way: python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import method_script  # noqa: E402

# (command, the script it runs, or None where it runs no script of the product)
FORMS = [
    ("python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl", "gate/run_tests.py"),
    ("python gate/run_tests.py", "gate/run_tests.py"),
    ("python3 -B tools/check.py", "tools/check.py"),
    ("python3.14 -B tools/check.py", "tools/check.py"),
    ("python.exe -B tools/check.py", "tools/check.py"),
    ("python3.exe tools/check.py", "tools/check.py"),
    ("python.EXE tools/check.py", "tools/check.py"),
    ("py -B tools/check.py", "tools/check.py"),
    ("py -3 -B tools/check.py", "tools/check.py"),
    ("py -3.14 tools/check.py", "tools/check.py"),
    ("py -3.14-64 tools/check.py", "tools/check.py"),
    ("py -V:3.14 tools/check.py", "tools/check.py"),
    ("py.exe -3 tools/check.py", "tools/check.py"),
    ('python -B "my tools/check.py" --record .runs/a.jsonl', "my tools/check.py"),
    ("python -B 'my tools/check.py'", "my tools/check.py"),
    ("python -B my\\ tools/check.py", "my tools/check.py"),
    ('python -B "gate/run_tests.py" gate', "gate/run_tests.py"),
    ("python -W error tools/check.py", "tools/check.py"),
    ("python -Werror tools/check.py", "tools/check.py"),
    ("python -BW error tools/check.py", "tools/check.py"),
    ('python -W "ignore::DeprecationWarning" tools/check.py', "tools/check.py"),
    ("python -X utf8 tools/check.py", "tools/check.py"),
    ("python -X dev -W ignore tools/check.py", "tools/check.py"),
    ("python --check-hash-based-pycs never tools/check.py", "tools/check.py"),
    ("python -u -B -E tools/check.py", "tools/check.py"),
    ("python -OO tools/check.py", "tools/check.py"),
    ("python -- tools/check.py", "tools/check.py"),
    ("python -- -dash.py", "-dash.py"),
    ("py -3.14-arm64 tools/check.py", "tools/check.py"),
    ("py -V:conda/3.12 tools/check.py", "tools/check.py"),
    ("python tools/check.py;echo done", "tools/check.py"),
    ("python tools/check.py>out.txt", "tools/check.py"),
    ("python tools/check.py|tee log.txt", "tools/check.py"),
    ("python >out.txt tools/check.py", "tools/check.py"),
    ("python;tools/check.py", None),
    ("python|tools/check.py", None),
    ("python tools/check#1.py", "tools/check#1.py"),
    ("python tools/check.py #a comment", "tools/check.py"),
    ("python #tools/check.py", None),
    ('python "#tools/check.py"', "#tools/check.py"),
    ("python tools/check.py;#comment", "tools/check.py"),
    ("python 2>err.txt tools/check.py", "tools/check.py"),
    ("python 2>>err.txt tools/check.py", "tools/check.py"),
    ("python 0<in.txt tools/check.py", "tools/check.py"),
    ("python 2>&1 tools/check.py", "tools/check.py"),
    ("python >&2 tools/check.py", "tools/check.py"),
    ("python 2 >err.txt", "2"),
    ('python "2">err.txt', "2"),
    ("python - tools/check.py", None),
    ("python -Ximporttime tools/check.py", "tools/check.py"),
    ("python -Wmodule tools/check.py", "tools/check.py"),
    ("python tools/check.py\npython other.py", "tools/check.py"),
    ("python\ntools/check.py", None),
    ('python "tools\\check.py"', "tools\\check.py"),
    ('python "tools\\$x.py"', "tools$x.py"),
    ('python "" tools/check.py', ""),
    ("python \\2>err.txt tools/check.py", "2"),
    ("python\t-B\ttools/check.py", "tools/check.py"),
    ("python tools/check.py &>out.txt", "tools/check.py"),
    ("python &>out.txt tools/check.py", None),
    ("python tools/check.py '$(x)'", "tools/check.py"),
    ("python \\$\\(x\\).py", "$(x).py"),
    ("python my\\\ntools/check.py", "mytools/check.py"),
    ('python "my \\"tools\\"/check.py"', 'my "tools"/check.py'),
    ("python tools/check.py -W error other.py", "tools/check.py"),
    ("python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} "
     "--record .runs/invariants-base.jsonl", "elements/invariants/format_guard.py"),
    ('python -B gate/run_tests.py "{merge-onto}"', "gate/run_tests.py"),
    ("python -m unittest discover", None),
    ("python -Bm unittest", None),
    ('python -c "print(1)"', None),
    ('python -Bc "print(1)"', None),
    ("python", None),
    ("python -B", None),
    ("python -", None),
    ("python {fork-point}", None),
    ("git log --oneline", None),
    ("pytest tests", None),
    ("pythonx tools/check.py", None),
    ("npm test", None),
]


class ScriptOfTest(unittest.TestCase):
    def test_reads_the_script_as_a_shell_and_the_interpreter_do(self):
        for command, script in FORMS:
            with self.subTest(command=command):
                self.assertEqual(method_script.script_of(command), script)

    def test_a_command_a_shell_cannot_split_raises(self):
        with self.assertRaises(ValueError):
            method_script.script_of('python -B "tools/check.py')
        with self.assertRaises(ValueError):
            method_script.script_of("python -B 'tools/check.py")
        with self.assertRaises(ValueError):
            method_script.script_of("python tools/check.py \\")

    def test_a_command_the_reader_cannot_read_as_the_shell_would_raises(self):
        for command in ("python $(echo tools/check.py)", "python `echo tools/check.py`",
                        'python "$(echo tools/check.py)"', 'python "`echo x`.py"',
                        "python $'tools/check.py'", "python tools/check.py <<<input"):
            with self.subTest(command=command), self.assertRaises(ValueError):
                method_script.script_of(command)


if __name__ == "__main__":
    unittest.main()
