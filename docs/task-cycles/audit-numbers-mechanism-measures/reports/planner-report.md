# Planner report — audit-numbers-mechanism-measures

Status: done with concerns (concerns and reaches below)

- Plan: `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md` — 8 slices, 8 foundation-entry rows plus one part-map row.
- Size report (last run, every slice fits): `.runs/task-cycles/audit-numbers-mechanism-measures/plan-size.md`
- Check run: `python -B task-cycle/slice_size.py .runs/task-cycles/audit-numbers-mechanism-measures/plan.md`, exit 0, 8 of 8 `fits` (largest: slices 5, 6, 7 at about 108k estimated tokens).
- No code, test or foundation entry written; the product's gate not run.

## Shape of the plan

1. `task-cycle/cycle_measures.py` for Claude Code sessions (trust boundary).
2. The same script for Codex sessions (trust boundary).
3. `task-cycle/gate_times.py` (runs the declared gate, relays output, appends times and the count of other runs).
4. Cycle instruction and record template (`task-cycle/skill/SKILL.md`, `blocked_finding.md`, `reserved_return.md`, `task-cycle/record_template.md`).
5. `audit_count.py`: cost from either form of `stages.md`, the missing-field mechanism (exit 1, `Error:`) (trust boundary).
6. `audit_count.py`: reading the two new files, per-cycle sections `Mechanism measures` and `Gate runs` (trust boundary).
7. `audit_count.py`: series by instrument, medians per version, "falls" (trust boundary).
8. `process-audit/SKILL.md`.

No slice changes `task-cycle/cycle_stages.py` or `task-cycle/change|plan|review|spec`, and none edits `TREE_PATHS`; the checks of slices 1, 5, 6 and 7 verify both with `git diff` against the base `2292f334d5499f45b68b00c477cd76a2effd7537`.

The two file forms (labels and columns of `mechanism_measures.md` and `gate_times.md`) are fixed in the *Goal* of Slices 1 and 3; Slices 4, 6 and 7 read those slices' lines of the plan, so the writer and the readers use one form.

## Concerns for the orchestrator (each with a proposed answer)

1. **Scope of the missing-field rule in `stages.md` (WAY-344, "the whole reading of the file").** Read literally, a missing `- Working time without waiting for tools:` line would be a missing field. I checked the 93 copies of `stages.md` in this repository's history: 86 have neither time line and no `Stages:` section (the oldest form), 7 have everything. Making an absent time line an error would end every weekly count with exit 1 for good. Proposed answer, already in the plan (Choices): both absent is the earlier form (values unknown, no `Error:`); exactly one of the two lines is a missing field; the fields of the cost of both forms are checked. If you hold the other reading, Slice 5 changes in one paragraph.
2. **The registry of concurrent gate runs lies outside the repository.** Counting other gate runs "on this machine" needs state shared between worktrees. The plan keeps empty files named with start and end in `~/.the-way/gate_runs/` (override `--registry`); an unusable registry gives `unknown` and the gate still runs. The sentence in `task-cycle/skill/SKILL.md` that the cycle writes nothing outside the worktree gets this one named exception (Slice 4). It is no effect of the kind WAY-140 lists (server, DNS, keys, external account), but it is a write outside the repository: if you want it to be a human action instead, the count of other runs becomes `unknown` always. Rejected ways and costs are in Choices.
3. **`gate_times.py` is not marked a trust boundary** (only `cycle_measures.py` is, per the handoff). It reads the output of the product's own declared gate, which the orchestrator itself runs; the audit re-reads the file it writes as untrusted. Slice 3 therefore has no review of its own. If you want it reviewed, add the script to the part-map row and set its Risk.
4. **The audit shows cycle-level values only.** The per-agent rows (first, middle, last call, cache writes per agent) stay in `mechanism_measures.md`; the result shows the cycle-level lines and the orchestrator's first, middle and last context. Item 5 says "values of each cycle" and "median of each measure"; I read "measure" as the cycle-level lines. Cost if wrong: one more slice for per-agent rows or medians of subagents' contexts.
5. **WAY-344 for the gate script.** It reads a stream, not a file; the rule's test (a file without a field) is replaced by a test where a `== dir` block has no `Ran` line and the directory time is `unknown`, never zero. Slice 1 and 2 give exit 2 with an `Error:` naming file and field for a missing field of a transcript, as the handoff asks.
6. **Where the product declares its gate.** I found no single place in the foundation or the instructions where a product declares the gate command; the plan makes the orchestrator pass the command after `--` (the-way: `python -B gate/run_tests.py`). Slice 4 words this.
7. **Step 4 runs before step 5 names `<task-slug>`**, yet item 4 wants the base-state run recorded in the cycle's file. Slice 4 tells its agent to settle the order in the instruction (name the slug before the base run, or use the file step 5 names) and to give the output path in a form that holds from a separate checkout of the base.
8. **A future environment fact.** The usage fields the measures script needs (`cache_creation.ephemeral_5m_input_tokens` and `...1h...` in Claude Code transcripts, `input_tokens` in Codex) are facts about outside tools the foundation does not hold. The plan writes none (no settlement row asks); the return step may find them. I checked the presence of these fields in one current Claude Code transcript only; Codex's per-call usage form was not checked against a real rollout, only against `task-cycle/cycle_stages.py`'s reader and its tests.

## Guidelines

Missing or uncertain: none; WAY-328 says the-way departs from the general coding and testing guidelines in these parts. The styleguide's order-of-work example does not apply (no user interface).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-140 (read whole; to decide whether the registry outside the repository is an effect WAY-140 reserves to a human).
- Git history of this repository: the 93 copies of `stages.md` under `docs/task-cycles/` added in any branch, classified by the presence of the section heading, the by-model table, the two time lines and the column `Files named` (read-only; to settle concern 1).
- One current Claude Code transcript under the user's `~/.claude/projects`: only the count of assistant responses lacking each usage field (no content read or kept).
- `elements/part-map/test_cross_part_imports.py` (head), to name the focused check of the invariant `cross-part-imports`.
- `instruction-files/SKILL.md` (head), `instruction-files/kind_skill.md` (head), `instruction-files/changing.md` (whole), `instruction-files/check_instructions.py` (docstring), `agent-instructions/README.md` (head), `agent-instructions/skill_entry_points.py` (usage lines), `task-cycle/tracked_private_paths_check.py` and `task-cycle/test_tracked_files_private_paths.py` (heads), `task-cycle/slice_size.py` (lines 1-120), `gate/run_tests.py` (whole), `task-cycle/skill/blocked_finding.md` (1-40) and `reserved_return.md` (45-60), `foundations/part_map.md` (entries `task-cycle`, `process-audit`, `gate`, `test-runner-command`, External context) — the last group is within what the handoff names, listed for the selection of the slices' *Read*.
- Titles of the decisions the handoff lists (by `grep` of the headings), to take their ranges for *Read*.

## Unread material

Named by the handoff and not read whole (what I read in brackets):

- Decisions read whole: WAY-337, WAY-338, WAY-339, WAY-340, WAY-341, WAY-344, WAY-160, WAY-140 (extra). Decisions of the handoff's list read by title only: WAY-38, WAY-328, WAY-331 (named in slices' *Read*, which carry them to the executors; I did not read their text), WAY-09, WAY-89, WAY-320, WAY-330, WAY-332, WAY-333, WAY-334, WAY-335, WAY-336, WAY-342, WAY-343, WAY-345, WAY-346, WAY-147, WAY-148, WAY-158, WAY-159, WAY-229, WAY-260, WAY-294, WAY-296, WAY-308, WAY-309, WAY-316, WAY-325, WAY-326, WAY-16, WAY-51, WAY-53 and the rest of the `gate` list. The 117 decisions whose *Scope* names `task-cycle` were not searched beyond those listed by the handoff.
- Invariants read whole: `script-language`, `script-imports`, `script-subprocesses`, `tracked-file-private-paths`, `cross-part-imports`, `record-copy-image-check`, `record-copy-image-files`. Not read: `skill-entry-points` (no slice changes a skill's description, so I did not select it).
- Glossary entries gate, slice, part, cost of an occurrence, standing check: not read (headings located only; `gate` is in Slice 3's *Read*).
- Part-map entries `decisions` and `part-map`: not read (the change reaches them only through the foundation entries).
- `process-audit/audit_count.py`: read lines 1-300 and 420-1260 and 1530-2245 (not read: 300-420 the locations reading, 1260-1530 the register reading). `process-audit/test_audit_count.py`: read 1-220, 690-860, 960-995 and 1840-2140 (the rest not read). `process-audit/price_list.md` and `problem_register.md`: not read. `task-cycle/test_cycle_stages.py`: read 30-140 and 224-303. `task-cycle/slice_size.py`: lines 1-120. `task-cycle/skill/planning.md`, `correction.md`, `request_template.md`: not read.
- The task's sources outside the repository (`weryfikacja_usprawnienia_the_way_dane/s05_metrics.py`, `miary_kontekstu.md`): not read, as the handoff says; the rewrite definition is taken from the task's *Questions to settle*.

## Searches not found or unclear

- A single place where a product declares its gate command: not found (concern 6).
- Whether the product's own tools (a game with Node build and tests) print `== <directory>` blocks: the task says only the process runner does; for a gate that prints none, the plan records the run with no directory rows.
- The shape of a Codex per-call usage entry in a real rollout (only the reader of `cycle_stages.py` and its tests were seen): unclear; Slice 2 asks for an error naming the file and the field where `input_tokens` is absent.
- How the later task that runs gate directories in parallel will order the output: unclear; Slice 3 attaches a directory's time to the first `Ran … in …s` line after its `== ` header, so interleaved output would give `unknown`, never a wrong time.

## Open questions

None that stop the plan; concerns 1 to 4 each carry a proposed answer.
