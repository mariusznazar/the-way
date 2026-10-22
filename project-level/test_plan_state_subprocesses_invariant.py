"""Observe the reader's actual Python process-start boundary, not its source text.

The audit hook lives only in the interpreter running the reader. Git's children
do not inherit Python hooks, so they are outside this property's observation.
"""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

# Reuse literal inputs only; no old expected observations or test methods are used.
from test_plan_state_invariant import CYCLE_RECORD, DEFINITION_BODY, FINGERPRINT, PLAN, TASK


READER = Path(__file__).resolve().with_name("plan_state.py")
AUDITED_READER = r"""
import json
import ctypes
import os
from pathlib import Path
import runpy
import shlex
import sys

reader, plan, repository, trace = sys.argv[1:]
events = {
    "subprocess.Popen": 0,
    "os.posix_spawn": 0,
    "os.exec": 0,
    "os.spawn": 1,
    "os.system": None,
    "os.startfile": None,
    "os.startfile/2": None,
    "os.fork": None,
    "os.forkpty": None,
}

def command_arguments(command):
    if not isinstance(command, str):
        return [os.fsdecode(value) for value in command]
    if os.name != "nt":
        return shlex.split(command)
    count = ctypes.c_int()
    parse = ctypes.windll.shell32.CommandLineToArgvW
    parse.argtypes = [ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int)]
    parse.restype = ctypes.POINTER(ctypes.c_wchar_p)
    pointer = parse(command, ctypes.byref(count))
    if not pointer:
        raise ctypes.WinError()
    try:
        return [pointer[index] for index in range(count.value)]
    finally:
        release = ctypes.windll.kernel32.LocalFree
        release.argtypes = [ctypes.c_void_p]
        release.restype = ctypes.c_void_p
        release(pointer)

def observe(event, arguments):
    if event not in events:
        return
    position = events[event]
    # Shell/association/fork starts do not directly identify a Git executable.
    argument_position = 2 if event == "os.spawn" else 1
    command = command_arguments(arguments[argument_position]) if position is not None else []
    program = None if position is None else arguments[position]
    # Windows Popen supplies a command line and no separate executable when the
    # OS is to resolve argv[0]; explicit executable overrides still take priority.
    if position is not None and program is None and command:
        program = command[0]
    row = {"event": event, "program": None if program is None else os.fsdecode(program),
           "arguments": command}
    with open(trace, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(row) + "\n")

sys.addaudithook(observe)
sys.path.insert(0, str(Path(reader).parent))
sys.argv = [reader, plan, repository]
runpy.run_path(reader, run_name="__main__")
"""


class PlanStateSubprocesses(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="process boundary ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.remote = self.root / "remote.git"
        self.publisher = self.root / "publisher"
        self.repo = self.root / "product"
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_TERMINAL_PROMPT="0", GIT_AUTHOR_NAME="Process fixture",
                        GIT_AUTHOR_EMAIL="fixture@example.invalid", GIT_COMMITTER_NAME="Process fixture",
                        GIT_COMMITTER_EMAIL="fixture@example.invalid")
        self.git(self.root, "init", "--bare", "--initial-branch=delivery", str(self.remote))
        self.git(self.root, "clone", str(self.remote), str(self.publisher))
        self.write(self.publisher / "README.md", "Fixture product\n")
        self.git(self.publisher, "add", "README.md")
        self.git(self.publisher, "commit", "-m", "Initial product")
        self.git(self.publisher, "push", "origin", "delivery")
        self.git(self.root, "clone", str(self.remote), str(self.repo))
        self.initial = self.git(self.repo, "rev-parse", "refs/remotes/origin/delivery")
        cycle = self.publisher / "docs/task-cycles/report-download"
        record = CYCLE_RECORD.format(source=self.root / "notes/tasks/report-download.md",
                                     repository=self.repo, frozen="accepted-task.md")
        record = record.replace("## Request handoff\n\nnone",
                                "## Request handoff\n\n- Request URL and status: "
                                "https://example.invalid/pull/41 and ready")
        self.write(cycle / "record.md", record)
        self.write(cycle / "accepted-task.md", TASK)
        self.git(self.publisher, "add", "docs/task-cycles/report-download")
        self.git(self.publisher, "commit", "-m", "Deliver report download")
        self.delivered = self.git(self.publisher, "rev-parse", "HEAD")
        self.git(self.publisher, "push", "origin", "delivery")
        self.plan = self.root / "notes/plan.md"
        self.write(self.plan, PLAN.format(fingerprint=FINGERPRINT, state="ready for cycle"))
        self.write(self.plan.with_name("definition.md"),
                   "# Report download\n\nStatus: approved 2026-10-01\n\n" + DEFINITION_BODY +
                   "## Gate record\n\n- Approved by: Fixture, 2026-10-01\n"
                   "- Definition fingerprint: " + FINGERPRINT + "\n")
        self.write(self.plan.parent / "tasks/report-download.md", TASK)

    @staticmethod
    def write(path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8"))

    def git(self, directory, *arguments):
        result = subprocess.run(["git", "-C", str(directory), *arguments], env=self.env,
                                capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    def observe_reader(self):
        trace = self.root / "reader-starts.jsonl"
        result = subprocess.run([sys.executable, "-B", "-c", AUDITED_READER, str(READER),
                                 str(self.plan), str(self.repo), str(trace)],
                                env=self.env, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=60)
        self.assertTrue(trace.is_file(), "Reader reached no observed process start: " + result.stderr)
        rows = [json.loads(line) for line in trace.read_text(encoding="utf-8").splitlines()]
        self.assertTrue(rows, "Empty observation cannot prove the property")
        return result, rows

    def assert_only_git(self, rows):
        for row in rows:
            self.assertIsNotNone(row["program"], "Indirect program start: " + repr(row))
            executable = row["program"].replace(chr(92), "/").rsplit("/", 1)[-1].lower()
            self.assertIn(executable, ("git", "git.exe"), "Non-Git reader subprocess: " + repr(row))

    def test_successful_evidence_read_starts_only_git(self):
        # invariant: project-plan-state-subprocesses
        # Break caught: an extra non-Git child during a complete successful observation.
        self.assertNotEqual(self.initial, self.delivered)
        result, rows = self.observe_reader()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        proposals = [line for line in result.stdout.splitlines() if line.startswith("propose ")]
        self.assertCountEqual(proposals, [
            "propose 1 report-download: ready for cycle -> in cycle",
            "propose 1 report-download: in cycle -> done",
        ], result.stdout + result.stderr)
        self.assertIn("https://example.invalid/pull/41", result.stdout)
        self.assertIn("docs/task-cycles/report-download/", result.stdout)
        self.assertIn("integration: refs/remotes/origin/delivery " + self.delivered,
                      result.stdout.splitlines())
        self.assert_only_git(rows)
        # Real remote-ref movement proves these are actual starts, not simulated calls.
        self.assertEqual(self.git(self.repo, "rev-parse", "refs/remotes/origin/delivery"), self.delivered)

    def test_failed_fetch_read_starts_only_git(self):
        # invariant: project-plan-state-subprocesses
        # Break caught: a non-Git fallback program on an operational failure path.
        self.git(self.repo, "remote", "set-url", "origin", str(self.root / "missing.git"))
        result, rows = self.observe_reader()
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assert_only_git(rows)
        self.assertEqual(self.git(self.repo, "rev-parse", "refs/remotes/origin/delivery"), self.initial)


if __name__ == "__main__":
    unittest.main()
