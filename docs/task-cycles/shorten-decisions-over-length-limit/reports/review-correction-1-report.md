PASS 711a146cc6ce58da7b0cf0d6e073420393bdce18

# Review of correction 1 — shorten-decisions-over-length-limit

Range: `010d9b39..711a146c` (one commit, `711a146c`). `git rev-parse HEAD` =
`711a146cc6ce58da7b0cf0d6e073420393bdce18`, as dispatched. The change touches one file,
`elements/decisions/template.md` (5 lines added, 5 removed), and only inside the first bullet of
"Changing a decision" (`elements/decisions/template.md:208-214`).

## Remarks

- **Remark 1 (fix in this request) — made.** The bullet now reads: "A part of another question that an
  existing entry answers, or a part of its own question that it sets apart, is a sentence of that
  entry where it cannot change without changing that entry; the first stands in a paragraph of its
  own and the second may, as "Binding sentences" gives. A part that can change on its own is a
  question of its own with its own number (WAY-19)."
  - **Against WAY-19** (`foundations/decisions.md:879-883`): the words naming the two kinds and the
    condition "where it cannot change without changing that entry" are WAY-19's words exactly.
  - **Against WAY-05 and "Binding sentences"** (`elements/decisions/template.md:137-143`): WAY-05
    gives "one paragraph … for each part of another question that it answers, and may carry a
    further such paragraph for each part of its own question that it sets apart". "Binding
    sentences" gives a part of another question "its own paragraph" and says a part of the entry's
    own question "may also have a paragraph of its own". The new clause "the first stands in a
    paragraph of its own and the second may" says the same and contradicts neither.
  - **The rest of the bullet:** "a part that can change on its own is a question of its own with its
    own number" is kept word for word, as is the sentence before it. A word diff (`git diff
    --word-diff`) shows that only the second sentence of the bullet changed; the other edited lines
    differ only in line breaks.
- **Remark 2 (let through, no task)** — asks for nothing; nothing changed. Correct.
- **Last paragraph (items 3–6 accepted)** — asks for nothing; nothing changed. Correct.

## Findings

### Critical

none

### Important

none

### Minor

none. "the first … the second" refers back to the two kinds named in the same sentence. It reads
clearly, and the author named it as its own weak point.

## The author's search for other copies of the old wording

The search holds. My own `git grep` over the whole tree at HEAD (outside `docs/task-cycles/`) looked
for "part of (the|a) question", "part(s) of (the|a|an) … question" and "part of the question an
existing". It found only:

- the entry form at `elements/decisions/template.md:34` ("a part of the question of the heading that
  the entry sets apart"), already the two-kind wording;
- WAY-05's *Verification* and *Rationale* (`foundations/decisions.md:719, 733`), which state WAY-05's
  own rule;
- WAY-19's *Rationale* (`:903`), a statement of its reason that names no kind;
- WAY-134's pair of examples (`:5502`) and the withdrawn number WAY-358 (`:11683`), which are about
  other things.

A second search, for every citation of WAY-19 and for "own question" or "another question" in
`elements`, `task-cycle`, `project-level`, `product-guidelines`, `agent-instructions` and
`guidelines`, found no other restatement of WAY-19's sentence on parts. No skill restates it. The
log's entries are outside this correction's bounds, and none of them restates the old wording as a
rule.

## Declined to judge

none

## Checks run

- `git rev-parse HEAD` — `711a146cc6ce58da7b0cf0d6e073420393bdce18`, exit 0.
- `git diff 010d9b39..711a146c` and `git diff --word-diff 010d9b39..711a146c` — one file, one bullet,
  as above.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, no `listed:` line (0 lines
  counted).
- The `git grep` searches named above.
- Not run: tests (`elements/decisions` holds no test, and the change is to a Markdown template); the
  full gate (CI's, WAY-160).

## Reaches beyond the dispatch

none

## Working copies

none made. One stray redirect of my own (`2>/tmp/x`) failed because that path is an existing
directory, so it wrote nothing anywhere. `.runs/review-whole/` stays empty.

## Unread material

none. I read whole: the handoff, the remarks, the author's report, `task-cycle/review/fix.md` (in the
previous round), and the template sections "Binding sentences" and "Changing a decision". WAY-05 and
WAY-19 were read whole in the review of the whole change and are unchanged since.

## Searches not found or unclear

none
