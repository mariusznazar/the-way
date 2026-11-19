"""What the modules of the audit share: the error of the command, git run to read only, the
cells of a table, and the name of the repository and the size limit its readers use.

The error of the command (`AuditCountError`), git run to read (`Git`, `GitError`), the cells of a
table (`table_cells`, `is_separator`), the name of the repository whose history is read (`THE_WAY`)
and the size above which a file of a copy is not read (`MAX_BYTES`), which `record_reading.py`,
`problem_register.py`, `version_analysis.py`, `audit_report.py` and `process-audit/audit_count.py`
import from here. A text of a table and the output of git are untrusted input (WAY-48). It imports
nothing of the audit's other modules, is imported, never run, and runs nothing when imported.
Standard library only.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

display = remarks_check.display

THE_WAY = "the-way"
# A copy's file larger than this is not read: no record or `stages.md` comes near it.
MAX_BYTES = 4 * 1024 * 1024
GIT_TIMEOUT = 120


class AuditCountError(Exception):
    """A wrong argument, a missing or wrong key of the locations file, or a result that cannot
    be written: nothing is written."""


class GitError(Exception):
    pass


# Git


class Git:
    """Git run to read only, with no prompt, no pager and nothing on stdin."""

    def __init__(self, repository: Path):
        self.repository = repository

    def execute(self, arguments: tuple[str, ...]) -> subprocess.CompletedProcess:
        # A `GIT_` variable of the environment the command starts in, such as GIT_DIR set by a
        # hook, would point git at another repository or add configuration: none is passed on.
        environment = {
            name: value for name, value in os.environ.items() if not name.upper().startswith("GIT_")
        }
        environment.update(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never", GIT_OPTIONAL_LOCKS="0")
        try:
            return subprocess.run(
                [
                    "git",
                    "--no-pager",
                    "-c",
                    "core.fsmonitor=false",
                    "-c",
                    "log.showSignature=false",
                    "-C",
                    str(self.repository),
                    *arguments,
                ],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=GIT_TIMEOUT,
                env=environment,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitError(f"git {arguments[0]}: {display(error)}") from None

    def run(self, *arguments: str) -> bytes:
        result = self.execute(arguments)
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise GitError(f"git {arguments[0]} failed ({result.returncode}): {display(detail)}")
        return result.stdout

    def code(self, *arguments: str) -> int:
        """The exit code of git run to read, for a command whose exit code is its answer."""
        return self.execute(arguments).returncode


# Tables


def table_cells(line: str) -> list[str]:
    """The cells of a table row; a backslash escapes the character after it, so that an escaped
    bar stays inside its cell. Linear in the length of the line."""
    text = line.strip()
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in text:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip())
    if text.startswith("|") and cells[0] == "":
        cells.pop(0)
    if text.endswith("|") and cells and cells[-1] == "":
        cells.pop()
    return cells


def is_separator(cells: list[str]) -> bool:
    return all(cell and set(cell) <= set("-:") for cell in cells)
