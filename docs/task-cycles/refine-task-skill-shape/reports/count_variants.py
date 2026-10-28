from pathlib import Path
root = Path('project-level/task/skill')
variants = {
    'manual independent': ['SKILL.md'],
    'manual project-plan task': ['SKILL.md', 'project_plan_task.md'],
    'orchestrated project-plan task': ['SKILL.md', 'orchestrated_mode.md', 'project_plan_task.md'],
    'source-only task (outside requested variants)': ['SKILL.md', 'source_only_task.md'],
}
for label, names in variants.items():
    counts = [(name, len((root / name).read_text(encoding='utf-8').split())) for name in names]
    print(label + ':')
    for name, count in counts:
        print(f'  {name}: {count}')
    print(f'  skill directory total: {sum(count for _, count in counts)}')
    print(f'  + guideline_findings.md if a relevant guideline finding occurs: {len((root / "guideline_findings.md").read_text(encoding="utf-8").split())}')
print(f'outside skill directory, read in each variant: project-level/task/template.md {len(Path("project-level/task/template.md").read_text(encoding="utf-8").split())}')
