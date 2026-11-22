"""Mutate install.py of the head worktree, run the new test, restore. Usage: probe.py NAME."""

import subprocess
import sys
from pathlib import Path

HEAD = Path(__file__).resolve().parent / "head"
INSTALLER = HEAD / "installation" / "install.py"

NEW = (
    b'        f"Until the part map has its first parts, '
    b'`{SUBMODULE}/elements/common/foundation_check.py` "\n'
)
MUTATIONS = {
    # The sentence of the base: the script by its bare name.
    "old-sentence": (
        NEW,
        b'        "Until the part map has its first parts, `foundation_check.py` reports '
        b'every file git "\n',
    ),
    # A moved script: a full path the pinned commit does not hold.
    "moved-script": (
        NEW,
        b'        f"Until the part map has its first parts, '
        b'`{SUBMODULE}/elements/common/foundation_checks.py` "\n',
    ),
    # The installation leaves `.runs/` out of `.gitignore`.
    "no-ignore-line": (b'        return "CREATE", RUNS + "\\n"', b'        return "CREATE", "build/\\n"'),
    # A sentence of the block that the checker reports as an error, not a warning.
    "error-line": (
        b'"pass. The first map is written with',
        b'"pass. See @docs/rules.md. The first map is written with',
    ),
}

name = sys.argv[1]
old, new = MUTATIONS[name]
original = INSTALLER.read_bytes()
assert original.count(old) == 1, name
INSTALLER.write_bytes(original.replace(old, new))
try:
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            "-m",
            "unittest",
            "test_install.InstallTest."
            "test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning",
        ],
        cwd=HEAD / "installation",
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
finally:
    INSTALLER.write_bytes(original)
out = Path(__file__).resolve().parent / f"probe-{name}.txt"
out.write_text(result.stdout + result.stderr, encoding="utf-8")
print(name, "exit", result.returncode)
