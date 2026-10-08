### Task 9: The checks of spec §8, the final review and the second search (orchestrator, with the final reviewer)

- [ ] **Step 1: Run every check of the changed parts on the final commit** (about seven minutes; 600000 ms timeout)

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && git status --short; git log --oneline 252152a..HEAD; \
for d in instruction-files agent-instructions gate elements/decisions elements/invariants elements/part-map elements/environment-facts elements/glossary; do python -B gate/run_tests.py $d --record .runs/check-$(echo $d | tr / -).jsonl > $R/reports/check_9_tests_$(echo $d | tr / _).txt 2>&1; echo "$d $? $(tail -1 $R/reports/check_9_tests_$(echo $d | tr / _).txt)"; done; \
for id in claude-code-imports claude-code-agents-md codex-agents-md cursor-agents-md single-rule-compliance agent-run-variance; do python -B gate/run_tests.py probes/$id --record .runs/fact-$id.jsonl > $R/reports/check_9_watch_$id.txt 2>&1; echo "probes/$id $? $(tail -1 $R/reports/check_9_watch_$id.txt)"; done; \
python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none > $R/reports/check_9_guard_decisions.txt 2>&1; echo "decisions $?"; \
python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none > $R/reports/check_9_guard_invariants.txt 2>&1; echo "invariants $?"; \
python -B elements/part-map/format_guard.py foundations/part_map.md --base none > $R/reports/check_9_guard_part_map.txt 2>&1; echo "part-map $?"; \
python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none > $R/reports/check_9_guard_facts.txt 2>&1; echo "facts $?"; \
python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none > $R/reports/check_9_guard_glossary.txt 2>&1; echo "glossary $?"; \
python -B -I .runs/stale_refs.py > $R/reports/check_9_stale_refs.txt; echo "stale $?"; tail -1 $R/reports/check_9_stale_refs.txt; \
python -B agent-instructions/skill_entry_points.py; grep -E '"fail"' .runs/check-agent-instructions.jsonl .runs/check-gate.jsonl; echo "fail lines $?"
```
Expected: clean status; the twelve commits of Tasks 0–8; every test directory `0` (instruction-files 69 tests with one skip on Windows; gate 98; agent-instructions 13 plus the tests of 1.8; the element tests as at the base); each watch `0` — a skip is recorded as no verdict, never a pass; decisions `0` with the 13 warnings of 1.4; invariants, part-map, facts, glossary `0` with `0 error(s), 0 warning(s)`; `references checked 397, stale 0` (or the count 1.9 recorded); `entry points are current`; `fail lines 1` (none).

- [ ] **Step 2: The fingerprints by hand** — the `stale` line above is that check (spec §8: with `--merge-onto none` the guards leave every fingerprint a link carries unchecked): `.runs/stale_refs.py` reads the entries with the guards' own parsers, recomputes each fingerprint with `relation-model/fingerprint.py`, and lists every `<id>@<fingerprint>` in `foundations/decisions.md` and `foundations/invariants.md` (the only files of `foundations/` that carry one) that no longer matches. Copy `$R/reports/check_9_stale_refs.txt` into the record.

- [ ] **Step 3: The check script on known inputs** (spec §8)

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && python -B instruction-files/check_instructions.py . > $R/reports/check_9_script_the_way.txt; echo "the-way $?"; cat $R/reports/check_9_script_the_way.txt; python -B instruction-files/check_instructions.py --file "C:/Users/Mariusz/.claude/CLAUDE.md" | grep -v "INFO  size"; python -B instruction-files/check_instructions.py /c/Storage/repos/loop2 | grep -v "INFO  size"; T=/c/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/821bfb3e-7677-4acf-bd0e-ab8a94541c58/scratchpad/a20 && rm -rf $T && mkdir -p $T && printf '# Claude\n\n@AGENTS.md\n' > $T/CLAUDE.md && python -B instruction-files/check_instructions.py $T
```
Expected: on the-way the five lines of Task 5 step 4 (`` WARN  dead-path AGENTS.md:20 `_zadania\` does not exist `` — the known false alarm, R8 — no unpointed-skill note, `agent-instructions/README.md` checked); on the global file `WARN` for `scripts/locations.json` and `INFO` (not `WARN`) for `~\.claude\memory\`; on `loop2` no `skill-dir` line; on the A20 fixture `WARN  at-import CLAUDE.md:3 @AGENTS.md imports a file that is not there`.

- [ ] **Step 4: Acceptance greps** (frozen task: "Nic w `instruction-files/` nie wskazuje na `.runs/` ani na notatki vaultu.")

Run:
```bash
cd /c/Storage/repos/the-way-instruction-files-part && R=.runs/task-cycles/instruction-files-part && git grep -n -i -E "\.runs|The Brain|_zadania|_tasks_active|vault|Obsidian|private notes|C:\\\\Storage|/c/Storage" -- instruction-files/
```
Expected: exactly one line, `instruction-files/check_instructions.py:<n>:SKIP_DIRS = {…, ".runs"}` — the skip-list literal naming a directory to skip, not a source (spec §6 point 11; the planner saw only this line on the final scratch files).

- [ ] **Step 5: Recalculate the sharpness inputs** (cycle step 10) from `git diff --stat 252152a..HEAD`: touched parts (instruction-files — new, high; decisions, invariants, glossary, part-map, environment-facts — foundation files and probes; agent-instructions — entry points and the invariant checks; README left out on purpose); trust boundary `instruction-files/check_instructions.py` (WAY-48: the crafted-input table of spec §4.6, every row pinned by a test in Tasks 3–5); nothing irreversible in the repository (the junction stays the human's step). Add checks if they grew; never drop any run above.

- [ ] **Step 6: Final review, with the deliberate breaks** — the whole-branch review of `subagent-driven-development` over `252152a..HEAD` (no duplicate `requesting-code-review` for the same range). Its reviewer gets the spec, this plan and the diff, and:
  - confirms that `agent-instructions/test_instruction_files.py` is unchanged since its commit in 1.9 (`git log --oneline -- agent-instructions/test_instruction_files.py` shows one commit) and that its author wrote neither the sentences nor the code (the record names each);
  - **writes the deliberate breaks** (WAY-69, WAY-08), from the two sentences in `foundations/invariants.md` only, in a scratch clone so the worktree is never touched:
```bash
B=/c/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/821bfb3e-7677-4acf-bd0e-ab8a94541c58/scratchpad/breaks && rm -rf $B && git clone -q --branch task/instruction-files-part /c/Storage/repos/the-way-instruction-files-part $B && cd $B && \
brk() { python -B gate/run_tests.py agent-instructions --record .runs/break.jsonl > /dev/null 2>&1; echo "$1 exit $?"; grep -E '"invariant": "(instruction-file-imports|root-claude-md-import)/1"' .runs/break.jsonl | grep -o '"verdict": "[a-z]*", "invariant": "[^"]*"' | sort | uniq -c; git checkout -q -- .; }; \
mkdir -p .runs && brk control; \
printf '\nSee @docs/x.md for the style.\n' >> AGENTS.md && brk agents; \
printf '\nSee @docs/x.md for the style.\n' >> agent-instructions/README.md && brk readme; \
{ printf '# Claude\n'; cat CLAUDE.md; } > c.tmp && mv c.tmp CLAUDE.md && brk heading
```
    Expected: `control exit 0` with `pass` for both invariants; `agents` and `readme`: exit 1 and `fail` for `instruction-file-imports/1`; `heading`: exit 1 and `fail` for `root-claude-md-import/1` (and, since `@AGENTS.md` then stands on line 2, `fail` for `instruction-file-imports/1` too). The tests are deterministic, so 1 of 1 runs each. A break that does not fail its check is a finding against the check, returned to the orchestrator and from there to the foundation step (the check is read-only here). The reviewer may write further breaks from the sentences (a nested tracked `AGENTS.md` holding `@./x.md`; a tracked Markdown file the root `CLAUDE.md` names holding `(@docs/x.md)`), each reported the same way.

- [ ] **Step 7: The second search of the whole foundation (R14; WAY-33)** — the orchestrator runs `git fetch -q origin && git log --oneline HEAD..origin/foundations` and, whatever it prints, dispatches one fresh agent with `C:\Storage\repos\the-way-process\elements\common\way_of_working.md` step 2, the list of entries this branch writes or changes (the term; the six facts; WAY-09, WAY-127, WAY-128–WAY-133; the two invariants and the seven renewals; the part `instruction-files`, `agent-instructions`, the flow) and the `foundations/` of `origin/foundations` beside this branch's, to search the whole foundation at the tip again for each; every finding is settled through its element's skill, the affected checks of Step 1 rerun, and both searches recorded. Reconciling a moved tip is cycle step 12's.

- [ ] **Step 8: Record** in `cycle.md` every result above by name, the deliberate breaks with their verdicts, the Cursor measurement's result and the state of task point 5, and the list "Unchecked" below.

**Unchecked (name these in the record and the request; none is a pass):**
- Every guard check that needs `--base` or `--merge-onto` (each guard prints its list): among them identifiers and versions, `TODO` in entries, the uses of changed definitions, terms and identifiers that came to read alike, facts nothing names after the merge, the fingerprints relations and links carry (covered only by `.runs/stale_refs.py`).
- Invariants whose *Method* is `TODO` that this change touches: `repository-file-location` (the new directory's place), `outbound-link-reach` (no link into private notes — the acceptance grep is its stand-in), `script-language`, `script-imports`, `script-subprocesses` (the check script), `derived-file-content` (the entry points — covered in substance by the generator's own equality test).
- The part's failure modes are all "not detected": no invariant covers the check script's behaviour (A6); its tests are not read-only.
- The level-2 verifications of WAY-09, WAY-127 and WAY-128–WAY-133: left to the independent assessment and the review.
- The watches depend on the network; a page that cannot be read gives no verdict. Whether WAY-08's deliberate break binds a fact's method stays open. A fact on path 1 of spec §5.2, if any, is unchecked with *Method* `TODO`.
- Whether Claude Code, Codex and Cursor actually list and follow the new entry points and load the skill: no session runs them; the human step after the merge observes it.
- That a lookup of a UNC or `\??\UNC\` path, or of `/\host` or `\/host`, reaches the network on Windows was not exercised (spec §12); the tests only prove no such path reaches the file-system calls.
- The FIFO test is skipped on Windows; the non-regular-file row is covered there by the test that fakes a device.
- The full gate, which does not exist before `main`; the dependency graph between parts (no command reports it).

---

## For the request: the human step after the merge (spec §5.4, option A, N3)

Do not run in the cycle. After the merge, in `cmd` or Windows PowerShell (`cmd /c rmdir` removes the junction itself, never the prototype worktree it points to, which stays):

```text
git -C C:\Storage\repos\the-way fetch origin
git -C C:\Storage\repos\the-way worktree add --detach C:\Storage\repos\the-way-global origin/foundations
cmd /c rmdir C:\Users\Mariusz\.claude\skills\maintain-instruction-files
cmd /c mklink /J C:\Users\Mariusz\.claude\skills\maintain-instruction-files C:\Storage\repos\the-way-global\instruction-files
```

and after each later merge that changes `instruction-files/`:

```text
git -C C:\Storage\repos\the-way fetch origin
git -C C:\Storage\repos\the-way-global checkout --detach origin/foundations
```

Under option C the junction is replaced by a copy of the merged `instruction-files/`, refreshed after such merges; under option B the junction is only removed. The request states that the flattened layout changes task point 9's target from `…\instruction-files\skill` to `…\instruction-files`.

## Choices this plan makes (provisional, under the orchestrator)

| # | Choice | Alternative | Price if wrong |
|---|---|---|---|
| P1 | The entry points come first among the code tasks (Task 2), right after the foundation step | after the code and texts, as spec §7 step 5 orders them | none known: the skill's frontmatter does not change, Task 6 step 3 and Task 9 step 1 confirm `entry points are current`; the other order keeps `gate` and `agent-instructions` red through six code tasks, where a second failure could hide behind the known one |
| P2 | The part-map changes of `agent-instructions` and the flow are written in the foundation step (1.7), last, as the dispatch orders; the starting point's commit carries only the new part | the flow's *Parts* written with the entry points, as the dispatch's code list mentions | none: no guard ties the flow's *Parts* to the entry points, and WAY-01 puts foundation entries before dependent code |
| P3 | The check script is reworked in three test-first tasks: reading (3), dead paths and network (4), what the root files lead to (5) | one task per fix (seven) | larger review units; each still has its own red-green and commit |
| P4 | A paragraph for fix A ends at a blank line, a fence, a heading, a list item or a table row | consecutive prose lines only | a negating sentence in one list item would lower a dead path in the next to `INFO` (pinned by a test) |
| P5 | The root-layout rule (R18) applies to every `CLAUDE.md` that has an `AGENTS.md` beside it, not only the root's, with check name `root-layout` | the root only | a nested `CLAUDE.md` with `@AGENTS.md` on a later line would be reported by no check, since the import check exempts it |
| P6 | An `@` import whose target does not resolve is `WARN` "imports a file that is not there" for every import, not only `@AGENTS.md` (A20) | the message only for `@AGENTS.md` | none: an import of a missing file loads nothing in any case |
| P7 | The skill's Place step 2 and principles §1, §3 and §4 are reworded where they name a hook as a keeper, so that the skill does not propose what WAY-133's *violates* names | change only what spec §4.2 and §4.3 list | the independent assessment would find the skill contradicting WAY-133 |
| P8 | The check author of 1.8 also receives the glossary entry of every term its sentences use | the sentences and the method only | if 1.6 uses the term, the author could not read the population from the sentence alone |
| P9 | Fixture files of the Cursor measurement live in the session's scratchpad, outside `C:\Storage`, so V1 is also V5's negative control | a separate directory for the control | none |
| P10 | `instruction-file-imports` is to use the glossary term where it names the same files (provisional answer to the invariants agent; WAY-97) | keep the spelled-out population of spec §5.6 | the invariant's population drifts from the term if one changes without the other |

## Deviations from the spec

- **Order of §7 step 5:** the entry points move before the code (P1). Spec §7 gives no dependency for its order; the change shortens the known red span to Task 0 – Task 2.
- **Paragraph of fix A (§4.5):** "consecutive prose lines" is read as a Markdown paragraph, broken also at a list item, a heading and a table row (P4).
- **Root layout (§4.5):** applied beside every `AGENTS.md`, not only at the root (P5); the at-import message for a missing target generalised (P6).
- **WAY-133 consistency (§4.2, §4.3):** the skill's Place step 2 and three places of the principles that name a hook as a keeper are reworded (P7); the spec lists only §4 pitfalls and §6 for R11.
- Everything else follows the spec; where a value can only come from reading a source at writing time (a fact's passages, an archived copy, the version of arXiv:2606.15828, a documentation address of `tool_loading.md`, the Claude Code setting's key), the plan says where to read it and never gives it from memory.
