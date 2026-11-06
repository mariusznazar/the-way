# Findings to fix — blocking findings of the review of the whole change, head 24e092ca8dd8ae2e7b6165133552e7590f73dc8c

Copied word for word from `review-1.md` (lines 45-75). Source report: docs/task-cycles/glossary-three-questions/reports/review-1.md

## Blocking findings (Important, within the task)

### F1 — WAY-104 has four binding sentences; the decisions template allows one to three

- Place: `foundations/decisions.md:2251-2260` (the paragraph under the heading of WAY-104).
- What is wrong: the paragraph is: (1) "A word that the glossary of the-way holds ... as the domain's." (2) "A bare
  use that no sentence of those files reads in the other meaning keeps the meaning it has there." (3) "A qualified
  word takes a glossary entry only where WAY-95 gives a word one, and where the bare word itself has an entry ...
  for its domain meaning." (4) "The product's code, its interface and talk about the product use the word of the
  domain unchanged." `elements/decisions/template.md:94` says "One to three sentences: the first paragraph under
  the heading (WAY-05)". Before the change the entry had two sentences.
- Why it matters: the task requires the whole of WAY-104 rewritten, so the form of the rewritten entry is part of
  what is required; an entry over the template's limit is the kind of departure a later reviewer or the next author of
  the entry will have to repair, and the template is what an agent checks entries by (WAY-05, WAY-12).
- Evidence: a script that splits the binding paragraphs of the 251 entries at sentence ends gave 4 for WAY-104 (and
  2 for WAY-95, 2 for WAY-97, 3 for WAY-99, 2 for WAY-293); `elements/common/foundation_check.py` does not check the
  count (grep for "sentence" in it found nothing), so the gate's pass does not cover this. Fix: join sentence 2 to
  sentence 1 with a semicolon (as sentences 1 and 3 of the old text were joined), or move the last clause of 3 and the
  sentence 4 together.

### F2 — WAY-293's binding sentence uses the word "should", which the template bans there

- Place: `foundations/decisions.md:8840` ("a finding that a word should have a glossary entry").
- What is wrong: `elements/decisions/template.md:97-99` says "The words *should* and *will* ... do not appear" in
  binding sentences. The same phrase in `task-cycle/review/SKILL.md:113` is not a binding sentence of an entry and is
  not part of this finding.
- Why it matters: the new entry is the one the task requires in `task-cycle`; it breaks a rule of form that the
  entries around it keep (no other entry written after WAY-286 has the word in its binding paragraph — script and grep
  over `foundations/decisions.md`, only line 8840 hits after line 8700). The fix is a rewording ("a finding that a word
  needs a glossary entry" or "a finding about a missing glossary entry").
- Evidence: `grep -n -i "\bshould\b" foundations/decisions.md` restricted to lines after 8700 prints line 8840 only.
