from pathlib import Path
import subprocess

BASE = "3aee7d958835cc19b95519f4d21b37538b78e3e1"
FILES = ("project-level/task/skill/SKILL.md", "project-level/task/template.md")
for path in FILES:
    result = subprocess.run(["git", "show", f"{BASE}:{path}"], check=True,
                            stdout=subprocess.PIPE, cwd=Path(__file__).parents[4])
    text = result.stdout.decode("utf-8")
    print(f"{path} {len(text.split())}")
