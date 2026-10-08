#### 1.2 Facts agent — `record-environment-fact`

**Files:** Modify `foundations/environment_facts.md` only.

- [ ] **Step 1: Dispatch** with `C:\Storage\repos\the-way-process\elements\environment-facts\skill\SKILL.md` and the six facts of spec §5.7's table (`claude-code-imports`, `claude-code-agents-md`, `codex-agents-md`, `cursor-agents-md`, `single-rule-compliance`, `agent-run-variance`), with:
  - the sentences of §5.7 are drafts: the agent opens each address, copies the passages as the template's "Source" gives them and takes the sentence's words from the page (WAY-80); a passage that is not on the page makes the sentence follow the page;
  - shape after `claude-code-path-rules/1` for the three documentation pages and `cursor-agents-md`: *Holds for* "<tool>, whose documentation <site> publishes for its current release without versions"; *Source* `<address> (archived: <copy>, <date>) § <place> — "<passage>"; read <date>`; and after `context-file-effect/1` for the two studies (versioned arXiv addresses are editions and take no archived copy); *Method* `python -B gate/run_tests.py probes/<id> --record .runs/fact-<id>.jsonl`;
  - the archived copy of a page without editions is found through the archive's CDX index of captures (skill step 3), never made; **where no capture exists** (N7) the agent stops before writing that fact and returns it to the orchestrator as a question, with the two paths of spec §5.2 below — never a silent form;
  - **a behaviour the page does not document** (R5; spec §5.2) is returned to the orchestrator before writing, naming which of the two paths keeps the decision that rests on it true: path 1 — the fact takes an observation source (WAY-80: "observed: `<command>` on <tool and version, platform>; run <date>") rerun by the agent itself — for Claude Code a `claude -p` session in a scratch directory outside every repository, its fixture files holding marker phrases only (settled by the orchestrator as O2) — with *Method* `TODO`, its debt named in the request (the template's `TODO — decision pending` on a method whose runner's configuration a command cannot set, and `script-subprocesses`); path 2 — the decision is reworded without that reason and no fact is written. No probe that runs an agent is written on either path. The one case the spec foresees: `claude-code-agents-md` (the prototype marked it "measured");
  - whether WAY-08's deliberate break binds a fact's method stays the template's open question; the agent settles neither answer;
  - return: the entries as written and, for each, its fingerprint, by running `python -B -I .runs/stale_refs.py claude-code-imports claude-code-agents-md codex-agents-md cursor-agents-md single-rule-compliance agent-run-variance` (none `NOT FOUND`).
- [ ] **Step 2: Orchestrator check**

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none > $R/reports/check_1_2_guard_facts.txt 2>&1; echo "facts $?"; grep -v "^unchecked" $R/reports/check_1_2_guard_facts.txt; python -B -I .runs/stale_refs.py claude-code-imports claude-code-agents-md codex-agents-md cursor-agents-md single-rule-compliance agent-run-variance
```
Expected: exit 0, `0 error(s)`, one known warning per new fact ("no invariant's *Rests on* and no decision's *Based on* names it" — the planner reproduced its wording with a draft fact); six fingerprints, kept for 1.4.

