PASS

# Review of the revision of the spec of `scripts-after-foundation-review`

Reviewed: `.runs/task-cycles/scripts-after-foundation-review/spec.md` against `spec-reviewed.md` (compared with `diff`; only D3 (WAY-344 paragraph) and D4 changed), the designer's section *Revision* in `reports/designer-report.md`, and my report `reports/spec-review-report.md`. No test or other check was run.

## F1 (D4 list of fields) - resolved

The "at least" list is replaced by a closed list. I checked it against `task-cycle/cycle_stages.py` (`read_claude_agent`, `is_text`, `content_blocks`, `parse_time`) and against real Claude Code transcripts.

- *Stay as they are* names `timestamp` absent (line skipped before its type, as l. 516), `type`, `isMeta`, `message.model` absent or null (warning "response(s) name no model", model `unknown`, the audit prices that row `unknown`), `message.id` (fallback `uuid`), `message.stop_reason` null or absent, and the lenient reading of content blocks. Each matches what the code does today, so `stop_reason`, `model` and `id` no longer end real cycles with exit 2.
- *Needed* names `message` and `message.content` of a `user` or `assistant` line with a `timestamp`; `message.usage` with the four counts and `cache_creation` with both lifetimes for every non-synthetic assistant line; and a `timestamp` that is a time. I checked these on the real transcripts under the Claude Code home (read-only `grep`): in all 455 transcript files of one project directory, no non-synthetic assistant line lacks `ephemeral_1h_input_tokens`; in the two files I looked at earlier, no `user` or `assistant` line lacks `timestamp`, `message` or `content`; no file holds `"content":null`. The needed list therefore does not end real cycles with exit 2.
- The test paragraph now adds a pin of the lenient list (no model, `stop_reason` null, no `timestamp`, `uuid` with no `id`, all read as today with exit 0), so a build that makes a lenient field strict fails; the one WAY-344 test the decision asks for stays.
- Where `cycle_measures.py` and the list differ, the list governs. That settles my point about the model being no support for `stop_reason`.

Remaining point, not a finding: item 3 says the `timestamp` "of such a line" has to be a time, while the closing sentence says no field outside the two lists is read. The code parses `timestamp` of every line that has one before it looks at the type, so a bad timestamp on a line of another type is read too. A builder can take it either way (exit 2 for any line with a bad time, or only for `user` and `assistant`), neither changes the behaviour on real data, and the maker can settle it; I leave it.

## F2 (WAY-344 wording for the earlier form) - resolved

D3 now says that for a report without the two write columns the cost is given as the approximation (writes inside *Input*, priced as input), no value is made `unknown` by the missing columns, and the values that are `unknown` for the form are only those that truly need a field it lost. It names the older table of tokens by model as the precedent (its cost is given, its share of fix rounds is `unknown`), and says the list of earlier forms and the *complies* line carry that wording. That removes the contradiction between WAY-344's "gives the values that need that field as unknown" and the audit giving a number.

## New findings from the revision

None. The revision adds no requirement that the task excludes, no contradiction with the foundation entries I read, and nothing to guess where a wrong guess would matter. The exit code of `cycle_stages.py` stays 2 for a missing field and 1 for the rest. The three readings accepted before (lone write column, both write columns in every price table, Warning for lifetimes that do not add up) were not touched by the revision.

## Reaches beyond the dispatch

- `diff` of `spec-reviewed.md` and `spec.md`; `reports/designer-report.md` ll. 158-226 (*Revision*).
- `task-cycle/cycle_stages.py` ll. 470-492 (`is_text`, `content_blocks`), to check the lenient and needed reads of the list.
- Real Claude Code transcripts under the Claude Code home, read-only `grep` counts (non-synthetic assistant lines without the 1-hour lifetime; `"content":null`; user or assistant lines without `content`). Nothing written.

## Unread material

- Not re-read: the parts of the spec that did not change (D1, D2, D5, the goals, the foundation entries section); I relied on the `diff` and on my earlier review of them.
- The unread material of `reports/spec-review-report.md` stands: `foundations/decisions.md` WAY-38, WAY-07, WAY-135; the invariants `script-language`, `script-imports`, `script-subprocesses`; `foundations/glossary.md` read only in part; `process-audit/audit_count.py` ll. 160-800, 1044-1235 and 1404-end; `task-cycle/cycle_stages.py` ll. 260-470 and 640-674; `task-cycle/cycle_measures.py` read ll. 1-290 only; no test file; `process-audit/SKILL.md`.
- The transcript checks covered one project directory of the Claude Code home (455 files for the lifetimes) and two files for `timestamp`, `message` and `content`.

## Searches not found or unclear

- Not found: any line of a real transcript in the files I looked at that the needed list would make fail.
- Unclear: whether transcripts of other projects or of older Claude Code versions hold a non-synthetic assistant line without `cache_creation`; the designer asks the maker to prove it on a real session before the step is done, which is sufficient.

## Working copies

None made: no worktree, clone, script or screenshot; nothing to remove. `.runs/spec-review/` was not created.
