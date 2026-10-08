# Report 07 — foundation step 1.2, watch author (saved by the orchestrator from the returned text)

Wrote four watch files under `probes/`: `claude-code-project-skills/test_claude_code_project_skills.py`,
`claude-code-nested-skills/test_claude_code_nested_skills.py`, `codex-repository-skills/test_codex_repository_skills.py`,
`codex-skill-paths/test_codex_skill_paths.py`. Each follows the `claude-code-path-rules` model: docstring restating the
fact, saying the docs are published without versions so the watch reads the passages at the address and not the archived
copy, and that no behaviour probe is written because a tool run takes credentials and a model; class
`<CamelCaseId>Watch(fact_probes.FactCheck)`; `test_the_passages_stand` holding `# fact: <id>/1` and
`self.watch_passages(IDENTIFIER)`. All four runs exit 0, "Ran 1 test … OK", none skipped. Committed nothing. Output was
piped to the terminal, so the brief's `check_1_2_watch_<id>.txt` files were not written (the orchestrator reran and
wrote them). WAY-08's deliberate break for a fact's method not settled. No questions.
