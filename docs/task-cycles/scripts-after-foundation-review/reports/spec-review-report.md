FAIL

# Review of the spec of `scripts-after-foundation-review` (the route of the cache writes)

Reviewed: `.runs/task-cycles/scripts-after-foundation-review/spec.md` against the frozen task, the designer's report and the foundation entries the handoff names. No test or other check was run.

## What holds (no finding)

- The route (D1, columns of the detailed section, written by `cycle_stages.py`, read by `audit_count.py`) matches the code as it stands. In `process-audit/audit_count.py` the header test (`section_table`, ll. 953-994) is `STAGE_COLUMNS` or `STAGE_COLUMNS + [FILES_COLUMN]`, and the cells read by position are 5, 6, 7 and 8. Two columns appended after *Files named* keep every earlier position. The older table of tokens by model (`older_table`, ll. 997-1042) is untouched by the route. The three-form header is a sound extension. A copy without both columns is read as today, a lone column is a missing field, and a header with write columns but no *Files named* is left undefined, which nothing writes and I do not count against the spec.
- Foundation entries other than WAY-339 and WAY-344: I found none that the route makes untrue. WAY-337 stays true. WAY-255 and WAY-368 speak of the cache lifetime of agents, not of what the audit prices. `audit-series-script-paths` is about the scripts of the measures and the gate, and the route touches none of them. The part map already names `cycle_stages.py` and `audit_count.py` as trust boundaries. The glossary has no term the route touches (the only hit is *cost of an occurrence*, which is another thing).
- The rewrite of WAY-339 in D3 is a faithful reading. The second paragraph ("are never columns of the stage report"), the *violates* line, the *Rationale* sentence about a column for cache use and *Rejected* are the passages the route makes untrue, and D3 names them all.
- Designer's reading 1 (adding one field to a reading is a rework, so the whole Claude Code reading of `cycle_stages.py` comes under WAY-344): I accept it. The *violates* line of WAY-344 ("checks the field it added and leaves the other fields of that file unchecked") supports it, and the lenient alternative, reading a missing `cache_creation` as zero, is what the same entry forbids. The cost is in the list of fields, see F1.
- Readings 2 and 3 (a lone write column is a missing field with exit 1; every price table has both write columns, OpenAI's with `—`) follow WAY-344 and the existing price reader and are fine. Reading 4 (a Warning where the lifetimes do not sum) is fine: it is no missing field.
- Nothing in the spec is excluded by the task. The extra sentences in `task-cycle/skill/SKILL.md` (step 12, ll. 571-574, which today names only `cycle_measures.py` and `gate_times.py` for exit 2) and `process-audit/SKILL.md` are consequences of the route, not new behaviour.

## Findings

### F1. D4's list of fields "at least" includes fields that real transcripts leave null or that the script reads with a fallback; a literal build ends every real cycle with exit 2

D4 (spec.md ll. 257-269): the whole reading of the Claude Code transcript is checked, "a missing field ends the script with exit code 2 ... they include at least the `timestamp`, the `type`, the `message` of an assistant or user line, its `model`, `id`, `stop_reason`, `usage` with ...". It takes `cycle_measures.py` as the model, where "A `null` is a missing field".

- `stop_reason`. In `task-cycle/cycle_stages.py` l. 555 it is read as `if message.get("stop_reason"):`. That is optional on purpose, because Claude Code writes one response over several lines and the early lines carry `"stop_reason":null`. I checked this on real transcripts under the Claude Code home (read-only `grep`): `0973cdea-…jsonl` holds 224 assistant lines, of which 2 have `"stop_reason":null`, and the first of them is an assistant line with `message.model`, `message.id` and content. `cycle_measures.py` never requires `stop_reason`, so the model the spec points to gives no support for it. A builder who follows the list literally makes the script stop with exit 2 on such a transcript.
- `model`. The script reads a missing model leniently on purpose. The module description lists "a response naming no model" among its warnings, `find_warnings` has the line "response(s) name no model" (l. 809), `add_by_model` files it under the model `unknown`, and `audit_count.py` ll. 1268-1272 prices such a row as `unknown` ("tokens of a response that names no model"). Making `model` a required field removes that path for Claude Code, and the spec does not say that it does.
- `id`. The code takes `message.get("id") or entry.get("uuid")` (l. 541), a fallback and not a required field.
- `timestamp`. The code skips every line without it before looking at the type (l. 516). The spec lists `timestamp` as required and also leaves "a type that is missing on a line of a kind the reading does not use" as no error, but does not say whether an assistant or user line without `timestamp` is skipped, as today, or ends the script. The two readings give different tests and different results on a transcript with such a line.

Why it matters: WAY-344 binds a field the script *needs*. The spec's list, taken as written, binds fields the script reads with a fallback and a documented warning, and `stop_reason` appears to be absent on legitimate lines. Built literally, `cycle_stages.py` would stop with exit 2 on real sessions, in a script that runs at step 12 of every cycle, and the doc and tests of the "no model" warning would have to change without the spec saying so. Built with the guess that the lenient fields stay lenient, the builder has to decide alone which of the listed fields those are, and the one test the spec asks for (a transcript missing one field) cannot tell the two builds apart if it picks `cache_creation`.

Question for the orchestrator or designer: which of `timestamp`, `model`, `id` and `stop_reason` are fields the reading needs (missing means exit 2), and which stay as they are (lenient with a fallback or a warning)? My reading of the code: `stop_reason`, `id` (fallback `uuid`) and `model` (warning, model `unknown`) stay lenient; the fields of `usage` with the two lifetimes, `message`, `message.content` and the timestamp of an assistant or user line are needed. The spec should say so, and that the existing "response names no model" warning stays.

### F2. The new wording of WAY-344 for the earlier form does not say what the "values that need the field" are for the cost

The task asks the spec to name the foundation sentences the route makes untrue together with their new wording. D3 (spec.md ll. 217-229) adds "one whose detailed section has neither of the two columns of the cache writes" to the list of earlier forms of WAY-344. That list sits in a sentence that goes on: "... and which gives the values that need that field as unknown, with no line `Error:`" (decisions.md l. 2758), and the *complies* line repeats it ("gives the values that need what that form never had as unknown", l. 2783). D2 and the Goals say the opposite for this form: the cost is the cost "it gives today", an approximation, "no new `unknown`".

If the foundation step adds the form to the list as D3 says, WAY-344 will read that the cost of a copy without the write columns is `unknown`, while the audit, as the spec builds it, gives a number. A later review of the code against WAY-344 would find a contradiction, or the foundation step would have to guess whether to write the exception. The two are consistent only if the entry states that the cost of an earlier form needs no field it lacks and is priced as input, an approximation, and that the values unknown for this form are only the ones that truly need a lost field. The older table of tokens by model already has the same property today (its cost is given, its share of fix rounds is `unknown`), so the fix is a short sentence in D3 for WAY-344: for the form without the write columns, the cost is given as the approximation and no value is made unknown by the missing columns. This is a wording the spec should fix and the foundation step should not guess.

## Judgment of the four readings the handoff names

1. Adding one field is a rework: accepted. D4's "whole reading under WAY-344" asks what the decision asks (every field the script needs of that file, no other file, one test), except where the list in D4 goes beyond "needs" (F1).
2. One write column alone is a missing field: accepted, and consistent with the two time lines.
3. Both write columns required in every table of the price list: accepted; the alternative contradicts WAY-344's "missing column ends with an error" for a reading the route reworks.
4. A Warning where the lifetimes do not add up: accepted.

## Reaches beyond the dispatch

- `task-cycle/spec/review.md`: the reviewer's variant of the method, as `SKILL.md` step 3 says.
- `foundations/decisions.md` ll. 2741-2852 (WAY-344 whole), 7309-7506 (WAY-330, WAY-337, WAY-339, WAY-350, whole): the dispatch names them.
- `foundations/` by search (`cache write`, `prompt cache`, `stage report`, `Files named`, `tokens by model`, `cycle_measures`, `exit code 2`): to look for entries besides WAY-339 and WAY-344 that the route makes untrue; none found.
- `foundations/invariants.md` ll. 395-427 (`audit-series-script-paths`) and `foundations/part_map.md` ll. 95-144.
- `foundations/glossary.md` ll. 183-196, after a search for `cache|stage report|stages.md|price`.
- `process-audit/audit_count.py` ll. 28-160, 800-1044 and 1235-1404; `process-audit/price_list.md` whole; `task-cycle/cycle_stages.py` ll. 1-260, 490-640, 674-783 and 855-1010; `task-cycle/cycle_measures.py` ll. 1-290; `task-cycle/skill/SKILL.md` ll. 556-590. All to check the spec's claims about the code.
- Real Claude Code transcripts under the Claude Code home (`grep -c` and `grep` of one line only, read-only, nothing written): to see whether `"stop_reason":null` occurs on assistant lines and whether any `user` or `assistant` line lacks `timestamp` or `message`. It does occur (F1); no such line lacks `timestamp` or `message` in the two files I looked at.

## Unread material

- `foundations/decisions.md`: WAY-38, WAY-07 and WAY-135 (named by the dispatch) not read; the spec's use of them (Python and standard library, rewrite in place, a spec only where a choice is open) matched what the other entries and the handoff say. WAY-330, WAY-337, WAY-339, WAY-344 and WAY-350 read whole.
- `foundations/invariants.md`: `script-language`, `script-imports` and `script-subprocesses` not read; `audit-series-script-paths` read whole.
- `foundations/part_map.md`: the entries `task-cycle` and `process-audit` read whole, and the lines around them.
- `foundations/glossary.md`: not read whole; I read ll. 183-196 and the lines a search for the route's terms returned.
- `process-audit/audit_count.py`: not read: ll. 160-800, 1044-1235 and 1404-end (other readings, the series code, the result writer); the series code that the task's rows 5 and 6 change was not opened.
- `task-cycle/cycle_stages.py`: not read: ll. 260-490 (the Codex reading) and 640-674; `task-cycle/cycle_measures.py` read ll. 1-290 only. No test file of either script was opened. `process-audit/SKILL.md` was not opened.

## Searches not found or unclear

- Not found: any sentence of the foundation besides those of WAY-339 and WAY-344 that the route makes untrue (searched as above).
- Unclear: whether the line `stop_reason` of the real transcripts is null on every Claude Code version the cycles run on; I saw it null on two of the transcripts I looked at, which is enough for F1.
- Unclear: whether a transcript line of type `user` or `assistant` without `timestamp` exists in real data; none in the two files I looked at, and the spec does not say how to read one (F1, `timestamp`).

## Working copies

None made: no worktree, clone, script or screenshot; nothing to remove. `.runs/spec-review/` was not created.
