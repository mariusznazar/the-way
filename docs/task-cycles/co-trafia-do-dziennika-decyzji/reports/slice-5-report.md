# Slice 5 report — The decisions template: where a settlement goes, parts of a question, the test that holds a sentence

## Status

`done`

## Commits

- `c8dcc56` Write where a settlement goes and the line decision: in the decisions template (base `12286a5`)

Worktree clean after the commit. Nothing pushed. No background process of mine is running (the gate run and the three waiting monitors have all ended).

## Files changed

| File | Diff |
|---|---|
| `elements/decisions/template.md` | +69 lines, -16 lines |

## What the template now holds

- Skeleton: the first paragraph answers the question; a second paragraph line for "a part of another question this entry answers, one paragraph for each"; the *Verification* line carries `invariants:`, the clause `tests:` and the pair for the part no invariant and no test holds.
- "Fields and their readers": rows *binding sentences* (the script compares them with the quotation of each line `decision:` and with the base) and *Verification* (the clause `tests:`, which the script does not read; the pair only for the part nothing holds).
- "Binding sentences": the first bullet gives one to three sentences for the question and one paragraph of one to three sentences for each attached part (WAY-05, WAY-19).
- "Decision or invariant": the bullet **Where it goes:** after **Plan test:**, with the five questions in D6's words and order, the first-yes rule, the threshold sentence, and the paragraph for the log of the-way (question 1 there, WAY-293). The bullet "Tests live only with invariants" is replaced by a bullet that says a test holds a sentence by a line `decision:`, that such a sentence gets no derived invariant, and that an invariant stays for a rule with no choice behind it and for a rule several decisions stand on (WAY-22, WAY-12).
- "Changing a decision": the sentence "a new rule next to an existing decision is a new question" is replaced by the WAY-19 rule: a part that cannot change without changing the entry is a sentence of it, in its own paragraph; a part that can change on its own gets its own number.
- "Verification": a bullet for the form of the line `decision:` (D3: comment in a tracked non-Markdown file, number as the heading writes it, one quotation in straight double quotes to end of line, no `"`, begins at a sentence start, three words or more, normalised spacing, stands at the test); a bullet for the clause `tests:` (no path, no test name, no number; the script does not read it; no second copy of the link, WAY-18); the pair only for the part no test holds; *Rationale* and *Rejected* kept whole where a test holds a sentence; a new example form `tests: …`.
- "Trade-off principles and non-goals": the last sentence now gives a checkable non-goal a derived invariant or a test with a line `decision:` and no invariant (WAY-22), brought in line with WAY-22 as it now reads.
- *Rationale* and *Rejected* rules: untouched.

## Checks

1. `python -B elements/common/foundation_check.py` on this worktree, exit 0, prints `0 errors`. It lists one item, `foundations/decisions.md:578: listed: WAY-17 is held by nothing`; a listed item stops nothing and the slice does not change WAY-17 (a decision of the plan's base, not edited here).
2. `python -B gate/run_tests.py elements/common`, exit 0: `Ran 198 tests in 281.747s`, `OK`. (It ran longer than four minutes; I ran it in the background and read its output in stretches.)

No check failed or did not run. The full gate was not run (the orchestrator's alone).

## Own-work check

The requirement my work most likely does not meet: D6 says to use the words of the five questions, their order, the first-yes rule, the threshold sentence and the paragraph for the log of the-way without paraphrase, and the template must not carry `should`, `will` or capitalised keywords in a binding sentence.

Check, run once from the worktree root: `grep -c -F` of each of the five question texts (in quotation marks), of the opening of the threshold sentence and of "Is it an instruction for how an agent works and" in `elements/decisions/template.md`, each count 1; and `grep -nw "should\|will"` on the template, which shows only line 112, the existing rule that forbids them. All counts were 1. The threshold sentence and the paragraph wrap across lines, so the grep proves the opening only; I read the rest against the spec by eye, word for word.

## Reaches beyond the dispatch

- `elements/common/foundation_check.py:79-81`, `:146` and `:702-706` (Grep on `invariants:|tests:|complies|violates`): to see what the script reads in *Verification*, so that the new skeleton line `invariants: … tests: … An agent compares …` leaves the `invariants:` reading intact. It does (check 1 passes). I did not read the script whole.
- `slice.md` beside `task-cycle/change/SKILL.md`, as the variant "a slice" names it.

## Unread material

- Read whole: WAY-02, WAY-05, WAY-12, WAY-17, WAY-18, WAY-19, WAY-22, WAY-35, WAY-36. WAY-26: read from its start to the start of its *Rejected*. WAY-293: read to the middle of its *Rationale* (45 lines from its heading), not to its end.
- Not read: WAY-07 and WAY-11 (the template's bullets that cite WAY-07 are unchanged; WAY-11 words nothing the template holds); `foundations/glossary.md:19-23`, `foundations/part_map.md:7-15` and `:65-75` (the change uses no term or part they define beyond words the template already used).
- The task passages `task.md:35`, `:39-40`, `:47-63`, `:76-81` were read inside one read of `task.md:30-84`; the spec ranges `:86-101`, `:129-141`, `:155-173` inside one read of `spec.md:60-184`.

## Searches not found or unclear

- `Tests live only with invariants` / `tests live only`: one occurrence in the repository's Markdown files outside the record, in the template's own bullet that I replaced. The spec's WAY-33 search for further entries that say it is the foundation step's, not mine.
- None unclear. The spec's D3 line about the quotation standing "in the binding sentences" and the template's phrase "once every run of spaces and line breaks is replaced by a single space" are the same normalisation as WAY-02's.

## Choices

- The skeleton's *Verification* line gives all three parts at once (`invariants:`, `tests:`, the pair); each part is optional and stands alone, which the "Verification" section's examples show (a third example `tests: …` added). Rejected: a separate skeleton line for the clause (the field stays one field). Cost if wrong: a reader may think all three are required; the section says each stands alone.
- The line `decision:` form is written in "Verification" (where the plan puts it), not in "Decision or invariant". Rejected: a new section (the plan names the existing ones).
- A paragraph for the log of the-way sits inside the bullet **Where it goes:** as a second indented paragraph, with the threshold sentence, rather than as separate bullets, so the bullet reads as one rule.
- I changed the non-goal sentence of "Trade-off principles and non-goals" (not named by the slice) because WAY-22 now says a sentence a test holds gets no derived invariant; the old sentence would contradict it, which the notes make mine to bring in line.

## Concerns

- The paragraph "Where it goes" is long for a bullet of this file; it is the spec's wording and the plan says the questions stand once, here. No cost beyond length.
- A decision whose sentence a test of a later slice holds carries a pair for now (D2). That rule stands in the skill and the return step (Slice 6), not in the template; I wrote nothing of it here.
- WAY-12 and the template now both say the clause `tests:` is not read by the script; the spec says the same (D3). No contradiction found between the template and any entry; I did not edit any entry.
