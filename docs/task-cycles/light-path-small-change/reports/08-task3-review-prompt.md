You are the task reviewer for Task 3 of one the-way task cycle (Superpowers 6.4.1
`subagent-driven-development`). Read and follow the reviewer template
C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/task-reviewer-prompt.md
— both verdicts (spec compliance AND task quality) are required.

Inputs (read each in full):
- Brief (requirements): docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-3-brief.md
- Implementer report: docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-3-report.md
- Review package (commit list, stat, full diff): docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) review-3bf1452..c64d49a.diff
- Spec the plan argues from: docs/task-cycles/light-path-small-change/spec.md §3, §6 (and §4 for the skill text the record must answer)
- You may read the whole files at HEAD: C:/Storage/repos/the-way-light-path/task-cycle/record_template.md and task-cycle/skill/SKILL.md (Task 2, 3bf1452), and
  WAY-13/1 and WAY-125/1 in C:/Storage/repos/the-way-light-path/foundations/decisions.md (committed in b977e5f).

Global constraints binding this task (verbatim from the plan): edit only `task-cycle/record_template.md`;
every new wording is copied from the brief (which copies the spec); LF; new and rewrapped lines at most 100
characters; rewrap only lines holding a changed word; bullets keep a two-space continuation; every slot the
new `- Cycle:` line and `## Cycle` section hold must answer something step 4, the "Light cycle" section or
step 13 of `task-cycle/skill/SKILL.md` asks the record for, and every such ask must have a slot; the
discarded attempt's last commit is a historical name, not a link to follow; a task failing the light-cycle
rule meets only the record lines spec §5 lists. The implementer did not run the brief's step 4 word-diff
reading — do that reading yourself.

Mariusz delegated intermediate choices to the orchestrator; report to the orchestrator only. Write nothing
except your full review to
docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-3-review.md and return the verdicts and
findings (severity Critical/Important/Minor) in under 20 lines.
