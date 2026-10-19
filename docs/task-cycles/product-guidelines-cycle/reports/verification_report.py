"""Build the orchestrator's verification summary from captured check records."""

import json
from pathlib import Path
import re
import subprocess


directory = Path(__file__).resolve().parent
head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
lines = [
    "# Orchestrator verification",
    "",
    "Actor: /root. Completed change: `" + head + "`. Windows, local Python.",
    "",
    "These are the required available checks under agent-instructions/README.md. "
    "The full gate does not exist and is not claimed as passed.",
    "",
    "| Command | Exit | Result | Complete output and execution metadata |",
    "|---|---|---|---|",
]
total = 0
expected = ["task-cycle", "project-level", "product-guidelines", "elements-decisions", "elements-part-map", "gate"]
for label in ["tests-" + item for item in expected] + ["guard-decisions", "guard-part-map"]:
    metadata = directory / ("orchestrator-" + label + ".json")
    record = json.loads(metadata.read_text(encoding="utf-8"))
    output = directory / record["full_output"]
    content = output.read_text(encoding="utf-8", errors="replace")
    summaries = re.findall(r"^Ran (\d+) tests in .*", content, flags=re.MULTILINE)
    if summaries:
        total += int(summaries[0])
    result_lines = [line for line in content.splitlines() if re.match(r"^(Ran \d|OK$|FAILED|\d+ error\(s\))", line)]
    command = subprocess.list2cmdline(record["command"])
    lines.append("| `" + command + "` | " + str(record["exit_code"]) + " | " + "; ".join(result_lines) + " | [Output](" + output.name + "), [metadata](" + metadata.name + ") |")
lines += ["", "Total executed test cases: " + str(total) + ".", "", "## Warnings and unchecked work", ""]
for label in ["guard-decisions", "guard-part-map"]:
    output = directory / ("orchestrator-" + label + ".txt")
    lines += ["### " + label, "", "```text", output.read_text(encoding="utf-8").rstrip(), "```", ""]
lines += [
    "The eleven request-link placeholders will be replaced only after a real PR exists. "
    "The five pre-existing overdue-review warnings remain outside this change. "
    "No unchecked guard result is relabelled as passed.",
    "",
    "The author's unchanged invariant, glossary and environment guards remain current "
    "as recorded in foundation-report.md, including their eleven unchecked results. "
    "No runtime UI was changed, so a running-product screenshot is not applicable; "
    "the new instructions' screenshot behavior was checked by the recorded manual scenarios.",
    "",
]
(directory / "verification-report.md").write_text("\n".join(lines), encoding="utf-8")
print("verification_report_written")
