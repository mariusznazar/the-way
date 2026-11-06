FAIL 24e092ca8dd8ae2e7b6165133552e7590f73dc8c

# Review of the whole change — task `glossary-three-questions`

Range `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a..24e092ca8dd8ae2e7b6165133552e7590f73dc8c` (one commit,
`git rev-parse HEAD` in the worktree printed the head sha above). Variant: the review of the whole change,
one author, no spec, no plan, so no finding comes from a slice. Counts: 2 blocking, 6 Minor, 1 out of scope.

Paths below are relative to the worktree `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions`
(`foundations/decisions.md` is `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions\foundations\decisions.md`).

## Coverage of the task, item by item (all met except as the findings say)

| Task item | Where in the diff | Result |
|---|---|---|
| To do 1 / row 1 (narrower meaning, entry only where a sentence is read wrongly) | WAY-95 (`foundations/decisions.md:2016`), `elements/glossary/template.md:50-54` | met; wording follows the answer of question 1; "English files" comes from row 5 |
| To do 2 / row 4 (WAY-104 as a sentence test, both directions; Rationale, Rejected, Verification; "Two glossaries") | WAY-104 (`:2249`), `elements/glossary/template.md:20-30` | met in content; form defect F1; the *Rejected* item for "reported as a warning" is Minor M3 |
| To do 3 / row 5 (English text only) | WAY-99, WAY-97 (`:2077`), `elements/glossary/template.md:63-72, 95-97`, `elements/glossary/skill/decide_entry.md:10` | met; two places that still say "files git tracks" without "English" (M4) |
| To do 4 / row 3 (the `TODO — decision pending` replaced by the sentence test, carried by a decision) | `elements/glossary/template.md:60-62` names WAY-99; WAY-99 carries it (`:2110`) | met; the `TODO` is gone from the template (grep) |
| To do 5 / row 2 (new decision in `task-cycle`, one sentence in `task-cycle/review/SKILL.md` section 3) | WAY-293 (`foundations/decisions.md:8838`), `task-cycle/review/SKILL.md:113-117` | met in content; form defect F2; wording of the skill sentence M1 |

Source fidelity (WAY-134): the *Rejected* lists of WAY-95, WAY-99, WAY-104 and WAY-293 take the "Not chosen"
ways of questions 1, 1a, 1b, 2, 3 and nothing else I could find; the only addition is the tail of the WAY-104
"warning" item (M3). Nothing the task settles is left out: the Minor default with a cited sentence, the WAY-99
carve-out, the WAY-263 carve-out, both directions, "sentence the files already hold", English only.

Both directions and only on held sentences, in each place the test stands:
- WAY-99 (`:2112-2116`) and template `:60-62`: "true in the meaning of one use and false in the meaning of the
  other, whichever of the two the sentence uses ... a sentence made up for the test does not count" — both
  directions and held sentences only.
- WAY-104 (`:2251-2258`) and template `:20-27`: a sentence "that uses the word for the product's domain and could
  be read as the process's, or one that uses it for the process and could be read as the domain's"; "a sentence of
  the files" — both directions, held sentences only. The *Verification* examples show only the domain-use direction (M2).

Untouched, as required: WAY-263 (`:7670`) and its paragraph in `task-cycle/review/SKILL.md:109-112` have no hunk
in the diff (the skill diff only adds lines, removes none); WAY-161 (`:4345`) has no hunk. The WAY-99 renaming
finding is excluded by name in both WAY-293 and the skill sentence, so it is graded as before. WAY-293's rule
(Minor unless a held sentence read wrongly is cited, then "as any other finding") fits section 3's grades and the
blocking rule of WAY-161; a finding that blocks stays Critical/Important within the task.

The orchestrator's reading of the ambiguous instruction ("jego koszt" = the cost of the variant "reported as a
warning rather than an error"): the task text of To do 2 supports it grammatically (the variant is the subject of
the clause) and the author's text follows it; see M3 for what the text adds.

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

## Minor findings (within the task)

### M1 — the review skill's new sentence points at "the paragraph above", but it is the same paragraph, and it is vaguer than WAY-293

- Place: `task-cycle/review/SKILL.md:113-117`.
- The new sentences follow the WAY-263 sentence with no blank line (`git diff` context shows
  `qualification (WAY-263).` directly followed by `+A finding that a word`), so they sit in one Markdown paragraph with
  the WAY-263 sentence; "graded as the paragraph above gives" then points at the previous block (lines 105-112 in
  the same paragraph, or the grade list above it). Also, WAY-293 says what stays Important ("a finding that a
  glossary entry the change writes or changes departs from a foundation entry"), whereas the skill says only that such
  an entry "is graded as the paragraph above gives" — no wrong grade follows, because WAY-263 grades only departures
  and other findings fall to the general grades, but the skill is a second account of WAY-293 in different words.
  Suggested: "a finding that a glossary entry the change writes or changes departs from a foundation entry stays
  Important (WAY-263)". Minor: the reader of the skill ends in WAY-263 and WAY-293 either way.

### M2 — WAY-104 *Verification* examples do not match the binding text everywhere

- Place: `foundations/decisions.md:2262-2278` (WAY-104 *Verification*); `:2030-2037` (WAY-95 *Verification*).
- Third `violates` item of WAY-104: "every bare "map" of a game's decisions is rewritten to a phrase though no sentence
  reads it as the part map". The binding text says where a qualifier is taken and that a bare use no sentence reads
  otherwise "keeps the meaning it has there"; it does not forbid a qualifier elsewhere, so an agent comparing a change
  that qualifies such a "map" finds no violated sentence. The `complies` list shows only the domain-use direction
  (a bare process use readable as the domain's is not shown), although the binding text and the task carry both
  directions. WAY-95's `complies` list adds a game's "map" as a case that "takes none"; that is the field's own
  meaning, not a narrower one, and shows nothing of the new rule.
- Minor: polish of examples; the binding text is clear.

### M3 — WAY-104 *Rejected*, item "reported as a warning rather than an error": the task's reason is there, plus a tail the task does not give

- Place: `foundations/decisions.md:2285-2289`.
- The task asks the variant to stay in *Rejected* "z powodem, dla którego jego koszt jest teraz do przyjęcia". The
  text gives "one word carrying two meanings in the repository is a cost now accepted where no sentence reads in the
  other meaning" — the reason, as the orchestrator read it. It then adds "but the variant stays refused where a
  sentence can be read both ways, since a mark beside the word tells the reader nothing at the use". That second
  half is the author's own reasoning, not a reason the task commands (WAY-134: nothing added that the task does not
  settle), and the author reports the instruction as ambiguous (placement choice d). If the human meant the cost of
  the new rule instead, one clause changes.
- Minor: a clause of one item; the decision's binding text is unaffected. Worth showing the human at the merge.

### M4 — "files git tracks" without "English" remains in the template's *Not* bullet and in WAY-94

- Place: `elements/glossary/template.md:85` ("each meaning the word carried in the files git tracks"),
  `foundations/decisions.md:1993` (WAY-94: "carries or carried in the files git tracks").
- To do 3 asks the glossary template narrowed to English text; the sentence added at `template.md:69-72` says "The
  rules above bind English text", and the *Not* bullet is below it, so the bullet reads as unbounded. The author
  left WAY-94 and this bullet as outside the task's list (report, "Looked at and left alone"); the template bullet is
  in a file the task names. Minor: the meanings of a Polish file would not be recorded under the new rule anyway.

### M5 — the first clause of WAY-95 is still restated without the narrower-meaning limit in several files

- Place: `elements/glossary/skill/decide_entry.md:3-5` (a file the change edits at line 10), `elements/glossary/template.md:3-5, 46-47`,
  `elements/glossary/skill/SKILL.md:3` (description), `README.md:39, :76`.
- Each says a word "that means in the product something other than a reader ... takes it to mean" takes an entry.
  WAY-95 now says a narrower meaning takes one only where a sentence is read wrongly. In the template the limit stands
  in the next bullet, and `decide_entry.md` sends the word through "Which words take an entry" in its next steps, so
  the files lead to the limit; the description and README are summaries. By WAY-293 itself a finding of this kind
  without a read-wrongly sentence is Minor; I cite none. The author's choice not to touch the skill description (it
  would need `skill_entry_points.py --write`) is reasonable. Minor.

### M6 — the WAY-104 binding text does not say "only" where the task does

- Place: `foundations/decisions.md:2251-2256`. Row 4 says the process word gets a qualifier "tylko tam, gdzie" a
  sentence could be read in the second meaning. The entry says the word "takes a qualifier in a sentence ... that
  could otherwise be read in the other meaning" and, in the next sentence, that a bare use no sentence reads
  otherwise "keeps the meaning it has there"; the "only" is carried by the second sentence and by the *Rationale*
  ("qualifying it would only add words"), not by the binding sentence that names the qualifier. Together with M2
  (third `violates`) this leaves the force of "only" to be inferred. Minor: it reads correctly once both sentences are
  read; the fix for F1 (merging sentences 1 and 2) can carry it.

## Out-of-scope finding (does not block)

### O1 — WAY-240 and the testing-guidelines files state the "something other than in the field" rule for test levels without the narrowed limit of WAY-95

- Place: `foundations/decisions.md:6885-6910` (WAY-240 binding sentence and *Rationale* citing WAY-95),
  `product-guidelines/testing/settle.md:8-10`, `product-guidelines/testing/template.md:110-113`.
- WAY-240 requires a level whose name means in the product something other than in the field a glossary term and
  cites WAY-95 for it. After this change WAY-95 gives a narrower meaning an entry only where a sentence is read wrongly.
  WAY-240 is a rule of its own for test levels ("integration above all", defined by the resources a test may touch),
  not a restatement of WAY-95, so the two can be read together (a level defined by resources is read differently in
  sentences such as "integration tests may touch files"); but if they ever collide, no precedence is recorded
  (WAY-25). The task does not name it; the author reported it. A task for the human to create or decline.

## Declined to judge

- Rewriting in a product (loop2) the sentences that after the change read in a second meaning (`:2166`, `:530` of
  loop2's decisions) — the task's *Out of scope*.
- Whether `README.md:39` and `:76` (summaries) should state the narrower limit — summaries of the product's process,
  not rules; set aside as outside the task's list (see M5 for the part I did grade).
- Whether WAY-293 should `derive from` rather than `narrow` WAY-161 (WAY-263 derives from WAY-161 while limiting grades
  similarly) — the author chose `narrows` with a stated reason, the task fixes no relation, and the relation breaks
  no rule of the template; set aside as a choice of the author.
- Readability of the first binding sentence of WAY-99 (about 150 words, the test and the rename obligation in one
  sentence) — within the template's three-sentence limit once F1 is fixed elsewhere; style, not graded.

## Checks I ran (command and exit code)

- `git rev-parse HEAD` in the worktree: `24e092ca8dd8ae2e7b6165133552e7590f73dc8c` — matches the dispatch.
- `git diff 61c72fb..24e092c` and `git log 61c72fb..24e092c` (read in full); `git diff --stat`: 7 files, 191 insertions, 83 deletions.
- In a separate detached worktree of the head under the system temp directory (removed afterwards; the reviewed
  worktree, its index and branch untouched; `git status --short` there prints nothing):
  - `python -B elements/common/foundation_check.py .` -> `0 errors`, exit 0.
  - `python -B gate/run_tests.py task-cycle` -> 92 tests OK, exit 0.
- Python script (scratchpad-free, run with `python -B -` from a heredoc, read-only) counting sentences and the words
  "should"/"will" in the binding paragraphs of all 251 entries of `foundations/decisions.md`: WAY-104 -> 4 sentences,
  WAY-293 -> "should" (also reported WAY-80 and WAY-229 above three by my rough sentence splitter, and "will"/"should"
  in three older entries; I did not examine those, they are not in the range). Exit 0.
- `git grep` of the old phrases (`every file git tracks`, `git tracks`, `something other than`, `meaning other than`,
  `other than the usual`, `keeps there the`, `bare word`, `definition true of`, `decision pending: which decision`,
  `qualifier`, `narrower`) and of `WAY-95|WAY-97|WAY-99|WAY-104|WAY-161|WAY-263|WAY-293` outside `.runs`, `.claude`,
  `.agents`: the only `TODO — decision pending` hits left are in other templates; no `keeps there the`, `bare word`
  or `definition true of` is left; leftovers are M4, M5, O1 above.
- Manual: each of the three places of the sentence test (WAY-99, WAY-104, template) read for both directions and for
  the held-sentence limit (result above); WAY-263, WAY-161 and the review skill's paragraph compared with the diff
  (unchanged); the decisions template applied to the five entries (F1, F2).

Not run: the full `gate/run_tests.py` (the orchestrator's step 10); `gate/run_tests.py elements/common` (the change
edits no code and no test there; `foundation_check.py` is the check that reads the changed text).

## Reaches beyond the dispatch

- `elements/decisions/template.md` whole (form of an entry: sentence limit, banned words, *Rejected* rule) — to judge F1/F2.
- WAY-161, WAY-263, WAY-240, WAY-94 and WAY-93 (read whole in `foundations/decisions.md`), `task-cycle/skill/SKILL.md:343-350`
  (the sentence "The reviewer alone grades and scopes"; consistent with the new rule, which lives in `review-change`
  section 3 where that sentence says the grades are held), `product-guidelines/testing/settle.md` and `template.md`,
  `README.md:35-42`, `elements/glossary/skill/decide_entry.md:1-25`, `elements/common/foundation_check.py` (grep only,
  for a check of sentence count or banned words) — to find leftover statements of the old rule.
- The decisions I did not select as part of my own reading list (WAY-11, WAY-95, WAY-97, WAY-99, WAY-104, WAY-293 were
  read whole at the head; WAY-134 text taken from the template's reference and the task).

## Searches not found or unclear

- No script or test checks the sentence count or banned words of a binding paragraph (grep of `foundation_check.py`),
  so F1 and F2 pass the gate; found only by reading against the template.
- "jego koszt" in To do 2 is ambiguous (whose cost); I used the orchestrator's recorded reading and flagged the tail
  (M3).
- The edit of WAY-11 (`foundations/decisions.md:330`, "a meaning for which WAY-95 gives it an entry"), of
  `task-cycle/skill/return_step.md:10` and `task-cycle/record_template.md:154` is beyond the task's list; I found it
  a defensible follow-up of WAY-95 (the handoff asks for leftover places; those three restated the loose
  "a meaning other than the usual one"). Not graded as a finding; the wording "a meaning for which WAY-95 gives it an
  entry" is awkward but not wrong.
- Whether the human reads WAY-293 as `narrows WAY-161` or `derives from`: not settled by the task (see Declined).
- The task file's claim `elements/glossary/template.md:51-52` for the old `TODO` was for the base commit; at the head
  the `TODO` is gone (grep).
