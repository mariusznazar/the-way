# Findings of the review of the whole change, for the fix

Source: the review `reports/review-whole-report.md` (FAIL, head `60561fba`), cut word for word. Blocking: I-1 and I-2, each with the reviewer's mark `Contradiction: yes`. After them, the Minor findings of that review within the task (the reviewer marked none outside the task's scope), M-1 to M-4, which are fixed in the same fix.

## Findings

### Important

**I-1 — A correction's session takes the strongest model from the record, with no probe of its own**

Place: `task-cycle/skill/SKILL.md:462-464`, the sentence:

> Before the first dispatch of the class, write under *Strongest class* of the record each try, with
> the model asked for and the model the row gives, and the model fixed; a session that continues the
> cycle, a correction's, reads them there.

What is wrong: a correction after review runs in a new session of the orchestrator (step 12 names
"every session of this cycle's orchestrator, a correction's included"), and a correction dispatches
agents of the strongest class: it repeats "the return step included" what the remarks touch
(`task-cycle/skill/correction.md:50-51`), whose review runs on the strongest class (WAY-229, step 11),
and for item 14 it dispatches a fresh reviewer in place of the review of the whole change
(`correction.md:105-107`). The added sentence has that session read the model fixed by the probe of
an earlier session and ask for it, with no probe. Which models a session allows is set when the
session starts (the task's *Need* and *Context*: `--settings <plik>` per session), so a correction
session started with another list — the day advisor starts sessions with
`--settings …vox_deny.json --model sonnet`, while a cycle started by hand with no list may have fixed
a model that list keeps out — asks for the recorded model, gets the session's own model with no error,
and the review runs on the weaker model. Step 12 later writes `asked for X, worked on Y` in the
record, so the weaker review becomes visible but is not prevented.

Why it matters: this is the failure the task exists to remove (PR #160 in the task's *Context*: the
whole-change review, the fix and the review of the fix ran on Sonnet and the round was repeated). The
task's answer to its first question puts the probe on the model the session actually gives and takes
no model on faith; its *Not chosen* rejects "prośba o najmocniejszy model i zapis faktycznego modelu
bez próby — … przegląd dalej bywa słabszy, tylko jawnie", which is what the correction session now
does, and the reason Mariusz gives for the probe in every cycle ("Próba łapie też przypadek, gdy model
podany przy starcie przestał być dozwolony") applies to a model fixed in an earlier session in the
same way. The task did not ask for this carve-out; WAY-229 does not state it either (its paragraph 2
speaks of "every cycle, before its first dispatch"), so the skill adds a rule the entry does not
carry. A literal reading of "w każdym cyklu" could count the correction as the same cycle; the
consequence above is why I read the settlement by its reason and not that way.

Evidence: the lines quoted; `task-cycle/skill/correction.md:50-51, 105-107`; `task-cycle/skill/SKILL.md:681-685`
(sessions of a correction); task `## Questions to settle`, question 1, *Answer*, *Not chosen* item 3
and *Source*.

Fix direction: a session that continues the cycle probes again before its own first dispatch of the
strongest class (the record's *Strongest class* then gains the tries of that session), and WAY-229's
paragraph 2 says "in every session of a cycle" or equivalent.

Contradiction: yes — the task's answer to question 1 (*Questions to settle*, "próbnym wywołaniem w
każdym cyklu … nie przyjmowanym na wiarę") and its *Not chosen* item 3; *Settlements to record* row 1.

Slice: none (one-author route).

**I-2 — The exception to the base measure is wider than the task gives: every test of a slice's own *Checks*, not the announced test in the owner's *Checks***

Place: `foundations/decisions.md:6402-6403` (WAY-136, binding paragraph 3):

> a test that fails on the base too is no failing check of the slice, save a test of the slice's own
> *Checks*,

and the same breadth in `task-cycle/change/slice.md:25-26` ("The exception is a test of your slice's
*Checks*, which your slice owns: it is a failing check of your slice, though it failed on the base
too."), `task-cycle/skill/SKILL.md:507-508` ("a test that fails on the slice's base too is none, save a
test of the slice's *Checks* (WAY-136)"), and WAY-136's *Verification*,
`foundations/decisions.md:6432-6434` and `6445-6446`.

What is wrong: the task scopes the exception to the owner of an announced test. *To do* 3: "test,
który pada także na bazie …, nie jest błędem kawałka, poza testem z *Checks* kawałka-właściciela
(punkt 5)"; *To do* 5 and the answer to question 3 name the test announced in an earlier *Goal* and
written into the *Checks* of the slice that repairs it; *Decisions in play* for WAY-136: "test
zapowiedziany jako czerwony stoi też w *Checks* kawałka, który ma go naprawić, i jego porażka po tym
kawałku jest nieudanym sprawdzeniem tego kawałka". The answer to question 2 otherwise holds without
qualification: "test padający także na bazie nie jest błędem kawałka". The change makes every test of
a slice's own *Checks* that fails on the base too a failing check of the slice.

Why it matters: *Checks* are focused commands — the slice's tests and those of the code it reaches
(`task-cycle/plan/SKILL.md:174-182`), often a test file or a part's suite. A test already red at the
task's base (the checks step 4 records as failing on the base) that such a command runs is, under
the change, a failing check of a slice that did not make it: the slice gets a retry one class higher
(sub-step 4) and, on the strongest class or after the retry, stops the cycle. Under the task's rule
it is no failing check, reported with its base result. The handoff of this review asks that WAY-136's
binding sentences say what the settlements say, no more and no less; this one says more, and the
decision the change itself writes is restated more broadly than the task (WAY-263).

Evidence: the lines quoted; task `### To do` items 3 and 5, `### Questions to settle` questions 2 and
3, `## Decisions in play` WAY-136.

Fix direction: in the four places, narrow the exception to a test that a *Goal* of an earlier slice
announces and the slice's own *Checks* hold (the owner's announced test), for example in WAY-136:
"save a test that an earlier slice's *Goal* announces and the slice's own *Checks* hold".

Contradiction: yes — the task's answer to question 2 ("test padający także na bazie nie jest błędem
kawałka", *Settlements to record* row 2) with the exception of question 3 limited to the owner's
announced test (row 3).

Slice: none (one-author route).

### Minor

All four lie within the task.

**M-1 — The probe's reading of the row holds only for Claude Code, and "another model than the candidate" compares an alias with a model id**

Place: `task-cycle/skill/SKILL.md:450-458`: "with the description `model probe <n>` … the row of its
table named by that description gives, in its column *Subagent model*, the model that agent worked on
… Where the row gives another model than the candidate, the harness substituted one".

Reasoning: `cycle_stages.py` names a Claude Code subagent `<description> (<type>)`
(`task-cycle/stage_transcripts.py:729-731`), but a Codex subagent by `agent_path` or `agent_nickname`
(`stage_transcripts.py:472`), so in a Codex session no row is named by the description. The candidate
is what the orchestrator asks for (in Claude Code an alias such as `opus`), the row gives a model id
(`claude-opus-…`); the text does not say they are compared by family, and the documentation the task
quotes says a blocked family alias goes first to "the newest permitted version in that family" — an
orchestrator cannot tell from the text whether an older version of the same family counts as a
substitution (go one model down) or as the model asked for. The procedure is workable in Claude Code
with judgment, which is why this is Minor; one sentence would settle both: how the row is found where
the tool does not name it by the description, and that the row matches the candidate where it is a
model of the candidate's family.

**M-2 — The planner's sentence has the *Goal* write into another slice's *Checks*, and bars slices before the breaking one**

Place: `task-cycle/plan/SKILL.md:189-191`: "its *Goal* names each such test file and the slice that
makes it pass, and writes the same test into the *Checks* of that slice, which holds it and no earlier
slice's *Checks* does."

Reasoning: the subject of "writes" is "its *Goal*"; it is the planner who writes the test into the
owner's *Checks*. "No earlier slice's *Checks*" is earlier than the owner, which also bars the slices
before the breaking slice, where the test still passes; the earlier text barred only the slices
between ("no slice's *Checks* holds a test an earlier slice leaves failing until its owner has
passed"). Read literally it forbids a harmless check. Suggested: "its *Goal* names each such test file
and the slice that makes it pass; the plan writes the same test into the *Checks* of that slice, and
no slice between the two holds it in its *Checks*."

**M-3 — WAY-136's *Verification* says "the file's tests" where its binding sentence says "the same test"**

Place: `foundations/decisions.md:6428-6429` ("its *Goal* names the file and that slice and the
*Checks* of that slice hold the file's tests") against `6398-6400` ("its *Goal* names each such test
file and the slice that makes it pass and the *Checks* of that slice hold the same test").

Reasoning: the binding sentence itself mixes a test file (named in the *Goal*) and a test (held in
*Checks*); the *Verification* resolves it as "the file's tests". A reader comparing a plan with the
entry gets two units. One word in either place makes them agree.

**M-4 — The paths that stop the cycle early run `cycle_stages.py` "as step 12 gives" but are not told to set the models in the record**

Place: `task-cycle/skill/SKILL.md:696-700` (the new sentence that sets, from `stages.md`, the model
each agent worked on, in step 12) against the stops that run the script on their own:
`task-cycle/skill/SKILL.md:520-526` (a slice failed twice), `task-cycle/skill/blocked_finding.md:15`,
`task-cycle/skill/reserved_return.md:55`.

Reasoning: *To do* 2 asks that the record give for every agent the model it worked on. The stops
point to step 12 for running the script; whether "as step 12 gives" carries the following sentence
on setting the models is left to the reader, so a blocked request's record may keep the models asked
for, marked so — the case the request reaches the human with the least review. A clause in the
sentence ("Where `stages.md` stands, in step 12 and in each stop that runs the script, …") closes it.
