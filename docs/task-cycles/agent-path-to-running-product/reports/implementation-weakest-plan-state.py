"""Manual weakest-point check (author, turn 2): does the plan-state reader, which lead-project runs
on an approved definition, stop a definition approved before the three choices were required?

Builds, in a temporary folder, the plan, task and definition the plan-state invariant checks held at
commit 77c8a8b (their literals, read from that commit's test file), then calls
plan_state.sources(plan) of the working tree and prints its findings.
Run from the worktree root: python -B <this file>
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
base = subprocess.run(["git", "show", "77c8a8b:project-level/test_plan_state_invariant.py"],
                      capture_output=True, check=True, env=dict(os.environ, MSYS_NO_PATHCONV="1"))
namespace = {"__file__": os.path.join(ROOT, "project-level", "x.py")}
exec(compile(base.stdout.decode("utf-8"), "base_test", "exec"), namespace)
sys.path.insert(0, os.path.join(ROOT, "project-level"))
import plan_state  # noqa: E402

with tempfile.TemporaryDirectory() as folder:
    os.makedirs(os.path.join(folder, "tasks"))
    with open(os.path.join(folder, "definition.md"), "w", encoding="utf-8", newline="") as h:
        h.write("# Report download\n\nStatus: approved 2026-10-01\n\n" + namespace["DEFINITION_BODY"]
                + "## Gate record\n\n- Approved by: Fixture, 2026-10-01\n"
                "- Foundation searched at: 595f839\n- Definition fingerprint: %s\n"
                % namespace["FINGERPRINT"])
    with open(os.path.join(folder, "tasks", "report-download.md"), "w", encoding="utf-8",
              newline="") as h:
        h.write(namespace["TASK"])
    plan = os.path.join(folder, "plan.md")
    with open(plan, "w", encoding="utf-8", newline="") as h:
        h.write(namespace["PLAN"].format(fingerprint=namespace["FINGERPRINT"],
                                         state="ready for cycle"))
    result = plan_state.sources(plan)
    print("exit code the reader gives:", result[2])
    for line in result[1]:
        print(line)
