"""Crafted inputs of the review: old heading and old status at readiness_check and plan_check."""
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "project-level"))
import readiness_check  # noqa: E402
import test_readiness_check as trc  # noqa: E402
import test_plan_check as tpc  # noqa: E402
import plan_check  # noqa: E402

out = []
work = Path(__file__).resolve().parent


def run(label, text, *args):
    path = work / "definition_case.md"
    path.write_text(text, encoding="utf-8")
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            code = readiness_check.main([str(path), *args])
        except SystemExit as e:
            code = e.code
    out.append(f"== {label} args={args} exit={code}\n{buf.getvalue()}")


good = trc.definition()
run("new form approved", good)
old_heading = good.replace("## Approval record", "## Gate record")
run("old heading, approved", old_heading)
run("old heading, before approval", old_heading.replace("approved 2026-10-03", "awaiting approval"),
    "--before-approval")
run("old heading, fingerprint", old_heading, "--fingerprint")
waiting = trc.definition(status="Status: awaiting approval", approval="")
run("new status before approval", waiting, "--before-approval")
run("old status before approval", waiting.replace("awaiting approval", "ready for gate"),
    "--before-approval")
run("both headings", good.replace("## Approval record", "## Gate record\n\nnone\n\n## Approval record"))
run("lower-case heading", good.replace("## Approval record", "## approval record"))

# plan_check: a definition with the old heading beside a valid plan
plan_dir = work / "plan_case"
plan_dir.mkdir(exist_ok=True)
for label, definition in (("plan, new definition", tpc.DEFINITION),
                          ("plan, old heading", tpc.DEFINITION.replace("## Approval record",
                                                                       "## Gate record"))):
    findings = tpc.conditions(tpc.PLAN, definition)
    out.append(f"== {label}: conditions={findings}")
    (plan_dir / "definition.md").write_text(definition, encoding="utf-8")

(work / "crafted_out.txt").write_text("\n".join(out), encoding="utf-8")
print("done")
