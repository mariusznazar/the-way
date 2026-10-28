from pathlib import Path

FILES = (
    Path("project-level/task/skill/SKILL.md"),
    Path("project-level/task/template.md"),
)

for file_path in FILES:
    word_count = len(file_path.read_text(encoding="utf-8").split())
    print(f"{file_path.as_posix()} {word_count}")
