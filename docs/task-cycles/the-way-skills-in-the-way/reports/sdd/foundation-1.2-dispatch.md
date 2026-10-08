You are the watch author of the foundation step of one the-way task cycle. You did not write the facts. The
orchestrator dispatched you; questions go to the orchestrator; nothing you write is anyone's approval.

Your inputs, and only these:
- the four entries `claude-code-project-skills/1`, `claude-code-nested-skills/1`, `codex-repository-skills/1`,
  `codex-skill-paths/1` as written in `C:\Storage\repos\the-way-skills-self\foundations\environment_facts.md`
  (their *Method* is the command each watch must satisfy);
- `C:\Storage\repos\the-way-skills-self\probes\fact_probes.py`;
- `C:\Storage\repos\the-way-skills-self\probes\claude-code-path-rules\test_claude_code_path_rules.py` as the form;
- the "1.2 Watch author" section of `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\foundation-1.2-brief.md`
  (exact file names and form). The rest of that brief (global constraints) binds you; its "Inputs every element agent
  gets" line does not apply to you — do not read the spec or the plan.

Write ONLY `probes/<id>/test_<id_with_underscores>.py` for the four identifiers, in the task worktree
`C:\Storage\repos\the-way-skills-self`. Use the Write tool for file content. Commit nothing. Then run, for each id:
`python -B gate/run_tests.py probes/<id> --record .runs/fact-<id>.jsonl` from the worktree root, and report exit code
and the test line.

Return your report as text: files written, each run's result (a skip "no verdict: …" is a result, not a pass), and
any question.
