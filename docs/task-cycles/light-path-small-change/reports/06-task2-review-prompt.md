You are the task reviewer for Task 2 of one the-way task cycle (Superpowers 6.4.1
`subagent-driven-development`). Read and follow the reviewer template
C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/task-reviewer-prompt.md
— both verdicts (spec compliance AND task quality) are required.

Inputs (read each in full):
- Brief (requirements): docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-2-brief.md
- Implementer report: docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-2-report.md
- Review package (commit list, stat, full diff): docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) review-b977e5f..3bf1452.diff
- Spec the plan argues from: docs/task-cycles/light-path-small-change/spec.md §3–5
- You may read the whole file at HEAD: C:/Storage/repos/the-way-light-path/task-cycle/skill/SKILL.md, and
  WAY-13/1 and WAY-125/1 in C:/Storage/repos/the-way-light-path/foundations/decisions.md (committed in b977e5f).

Global constraints binding this task (verbatim from the plan): edit only `task-cycle/skill/SKILL.md`; every
new wording is copied from the brief (which copies the spec); the file writes "behavior"; LF; new and
rewrapped lines at most 100 characters except line 3, the front-matter `description`, which stays ONE line
(`installation/install.py` reads `^description: (.+)$`); rewrap only lines holding a changed word;
continuation indentation 3 spaces under steps 1–9, 4 spaces under steps 10–14; the "Light cycle" section
sits between the dispatch-contract paragraph and `## Design and plan`, so its "below"/"above" and step
numbers must name the right places; acceptance (spec §5): every change a task failing the light-cycle rule
meets is one of those spec §5 lists; the four "simple and obvious" conditions must match WAY-125's binding
sentence.

Mariusz delegated intermediate choices to the orchestrator; report to the orchestrator only. Write nothing
except your full review to
docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-2-review.md and return the verdicts and
findings (severity Critical/Important/Minor) in under 20 lines.
