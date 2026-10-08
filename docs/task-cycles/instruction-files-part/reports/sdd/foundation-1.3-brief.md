#### 1.3 Watch author — six watches

**Files:** Create `probes/<id>/test_<id_with_underscores>.py` for each fact whose *Method* is a command (six unless 1.2 took path 1 or 2 for one).

- [ ] **Step 1: Dispatch a fresh agent** (not the facts agent; facts skill, "After step 4.4") with only: the entries as written in 1.2, their *Method*, `probes/fact_probes.py`, and as form `probes/claude-code-path-rules/test_claude_code_path_rules.py` (documentation) and `probes/context-file-effect/test_context_file_effect.py` (a study). Each file: a module docstring as in its model — for a page without editions the watch reads the passages at the address, never the archived copy, and no probe of the behaviour is written because a run of the tool takes credentials and a model; for a study, what the study measured cannot be asked here and now without a model run; a class `<CamelCaseId>Watch(fact_probes.FactCheck)`; for the documentation facts one method `test_the_passages_stand` holding `# fact: <id>/1` and `self.watch_passages(IDENTIFIER)`; for `single-rule-compliance` and `agent-run-variance` also `test_the_paper_is_neither_revised_nor_withdrawn` holding `# fact: <id>/1` and `self.watch_arxiv(IDENTIFIER)`. Whether WAY-08's deliberate break binds a fact's method stays the template's open question.
- [ ] **Step 2: Run each watch**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && for id in claude-code-imports claude-code-agents-md codex-agents-md cursor-agents-md single-rule-compliance agent-run-variance; do python -B gate/run_tests.py probes/$id --record .runs/fact-$id.jsonl > $R/reports/check_1_3_watch_$id.txt 2>&1; echo "$id $? $(grep -E '^(Ran|OK|FAILED)' $R/reports/check_1_3_watch_$id.txt | tr '\n' ' ')"; done
```
Expected: each `0` — 1 test OK for a documentation fact, 2 for a study. A skip ("no verdict: …") is recorded as no verdict, not a pass, and rerun once later; a failure means a passage does not stand — back to 1.2.

