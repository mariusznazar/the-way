"""Capture a required check without losing its exit code or complete output."""

import datetime
import json
from pathlib import Path
import re
import subprocess
import sys


label, *command = sys.argv[1:]
directory = Path(__file__).resolve().parent
output = directory / ("orchestrator-" + label + ".txt")
metadata = directory / ("orchestrator-" + label + ".json")
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
with output.open("wb") as stream:
    result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT)
record = {
    "command": command,
    "cwd": str(Path.cwd()),
    "started": started,
    "finished": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "exit_code": result.returncode,
    "full_output": output.name,
}
metadata.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(label + ": exit=" + str(result.returncode))
print(output.as_posix())
for line in output.read_text(encoding="utf-8", errors="replace").splitlines():
    if re.search(r"^(Ran \d|OK$|FAILED|FAIL:|ERROR:|Error:|Warning:|warning:|unchecked:|Summary:)", line):
        print(line.encode("ascii", errors="backslashreplace").decode("ascii"))
sys.exit(result.returncode)
