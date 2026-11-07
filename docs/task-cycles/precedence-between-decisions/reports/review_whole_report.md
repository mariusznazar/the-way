FAIL 9b44856c6b8bda6ea17f22808e3332694b026601

# Review of the whole change - precedence-between-decisions

Range `294af7f..9b44856` (one commit). `git rev-parse HEAD` printed `9b44856c6b8bda6ea17f22808e3332694b026601`;
the toplevel is the worktree root. No spec, no plan, no slices, no earlier review.

## Changed files (added / removed, from `git diff --numstat 294af7f..9b44856`)

| File | + | - |
|---|---|---|
| `foundations/decisions.md` | 33 | 7 |
| `elements/decisions/template.md` | 6 | 2 |
| `agent-instructions/README.md` | 6 | 3 |
| `task-cycle/skill/foundation_step.md` | 6 | 3 |
| `elements/decisions/skill/decide_entry.md` | 5 | 2 |
| `task-cycle/skill/request_template.md` | 5 | 3 |

Total 61 / 20. Markdown only; no code, no test file changed; no invariant changed (so no invariant test).

## Findings

### Critical

none

### Important (blocking; all inside the task)

**I1. WAY-25 *Rejected* says more than the human settled about the singular "the passage".**
Place: `foundations/decisions.md`, WAY-25 *Rejected*, last item (around line 681-683): "one passage of
what the human accepted in the singular - an outcome can come only from two passages read together,
and an agent reading the wording literally would stop where the outcome is given."
Source: task *Questions to settle* 3, third "Not chosen": "cytat jednego fragmentu ('the passage') - w
przypadku `logging-guidelines` wynik daje dopiero połączenie dwóch fragmentów, więc agent czytający
dosłownie stanąłby tam, gdzie zaczęła się sprawa". The source says that in one case the outcome came
only from the combination of two passages. The entry says, as a general statement, that an outcome
"can come only from two passages read together". Read plainly that is a universal ("only two
passages give an outcome"), which is false and contradicts the entry's own *Verification* (*complies*:
"in one passage or in two read together"). WAY-263 grades a changed entry that restates the human's
settlement more broadly or without its qualification as Important; the handoff asks that no wording
say more than was settled.
Why it matters: *Rejected* is what a later reader takes as the reason a way was dropped; this one
gives a reason that is false in general and mismatches the Verification a few lines above it.
Evidence: the two texts above, side by side. Fix: say what the source says, e.g. "an outcome can come
from two passages read together, and an agent reading the wording literally would stop where the
outcome is given".

### Minor (inside the task, non-blocking)

**M1. "often" in WAY-25 *Rejected*.** `foundations/decisions.md`, WAY-25 *Rejected*, item "an exception
only for a settlement that says which decision prevails - the outcome often follows from settlements
that do not say so". Source (Q1, first "Not chosen"): the wording "did not even cover the case that
started it" (one case). "Often" is a frequency the source does not give. The author reported the
rewording as a choice; the reason itself is faithful, the frequency is not. Fix: "the outcome can follow
from settlements that do not say so".

**M2. WAY-293 *Rationale* now states WAY-25 without the qualifier.** `foundations/decisions.md`,
WAY-293 rationale (line about "the agent that meets the collision may not settle it (WAY-25)").
WAY-25 now says "never settled silently" and allows recording where the accepted task document gives
the outcome. The author judged that WAY-293's case (task or spec exclusion; a spec is not accepted by
the human, WAY-135) still stops the agent. That holds for a spec, but a task document that itself
excludes an entry is a collision of exactly the kind WAY-25 now lets the cycle record. Unqualified,
the clause reads wider than WAY-25. Found by the search of WAY-33 the task asks for; a one-word
correction ("settle it silently") or an explicit note would close it. Checked also WAY-26, WAY-32,
WAY-172, WAY-268: they say why precedence is recorded or that without it the agent has nothing to
choose between; not contradicted.

**M3. `task-cycle/skill/request_template.md:194-196` takes the quoted passages "from the foundation
step's report" only.** The same item 6 takes entries from "the foundation step's and return step's
reports"; the return step "writes as this step writes" (`foundation_step.md`, header) and can record a
precedence too, keeping the passages in its own report. The wording leaves the return step's case
without a named source. Fix: "from the report of the step that wrote it".

### Out of scope (does not block)

**O1.** WAY-25 *Scope* is `decisions, task-cycle`. The change now writes WAY-25 into
`agent-instructions/README.md`, a file of the part `agent-instructions` (part map line 132-140), whose
agents do not read WAY-25 by their *Scope* selection. The README already stated the rule before
without citing WAY-25, and the task does not ask for a *Scope* change. Raise as a possible later task.

## Coverage of the task

- **To do 1** (WAY-25 binding sentence): met. The task's quoted sentence is a verbatim substring of
  `foundations/decisions.md` after whitespace normalization (script check, True).
- **To do 2** (examples): met. *Violates* gains "the change records a precedence that no passage of what
  the human accepted gives, or one its request does not name with those passages". *Complies* holds the
  stop case ("what the human accepted does not give the outcome, or the change may not write the
  decision that prevails, stops and asks") plus the record-and-name case (author's choice, see below).
- **To do 3** (rationale, *Rejected*): rationale describes the new decision (judgment stays the
  agent's, quoted passages check it, prevailing decision outside the repository goes to a human - all
  from Q1 and *Context*). *Rejected* carries the not-chosen of Q1 (two) and Q3 (three). Faithful except
  I1 and M1.
- **To do 4** (copies): `elements/decisions/template.md` (met), `agent-instructions/README.md` (met),
  `task-cycle/skill/foundation_step.md` (met; adds the `the cycle's` mark and the quoted passages in
  the report), `elements/decisions/skill/decide_entry.md` (met), `task-cycle/skill/request_template.md`
  item "Foundation entries the human did not see at the task document", now lines 190-198 (met, see
  M3). Line numbers: the item sits at 190-196 at the base, as the handoff says.
- **To do 5** (WAY-134 example): met; the task's quoted example is a verbatim substring after
  normalization (True). `elements/decisions/template.md` rule on *Rejected* is untouched (diff shows
  no change at lines 37, 59, 64, 224).
- **Questions 1-5**: Q1 met (record and name; stop where no outcome or the change cannot write the
  winner; "gives the outcome" left to the agent with the request as the safeguard). Q2 met. Q3 met
  (whole precedence - `narrows` and area - recorded; request names it with passages, plural). Q4 met.
  Q5 met (new *violates* item).
- **Context's entries citing WAY-25** (WAY-32, WAY-172, WAY-268, WAY-293) and the orchestrator's finds
  (WAY-26 at `foundations/decisions.md:709`-area, `elements/decisions/template.md:88`, `:202`): read;
  none contradicted except the wording gap in M2. Repository-wide grep for `WAY-25` and for
  `collid|precedence|stops the work|never settled` finds no other copy of the old rule (the
  `project-level` hits are about candidates colliding at the readiness gate, another process).
- *Settlements to record*: `none`; nothing to check.
- Author's choices judged: (a) *complies* holding both paths - not asked, but the pair would otherwise
  show no complying case of the new behaviour; acceptable, no finding. (b) *Rejected* rewording of the
  Q1 item - M1. (c) `foundation_step.md` mark `the cycle's` and quoted passages kept in the report -
  needed for the request's item 6 to quote them; acceptable. (d) "what he accepted" in the README -
  matches the file's register; fine.
- Foundation entries the change writes: WAY-25 (said above) and WAY-134 example. WAY-25 binding
  sentences, *Verification* and the copies agree with each other: the copies state the same two paths
  and the same condition ("the change may write the decision that prevails"). Template line says
  "otherwise the work stops and a human records the precedence by an edit" against WAY-25 "the agent
  stops and asks" - same meaning.

## Declined to judge

- Whether the *complies* example should say "task document" only, not also an approved plan (WAY-30
  names both): an example, not the binding sentence; the task does not address it.
- Whether the new path conflicts with WAY-30's pre-code approval of a change to a decision: the task
  itself settles that the sentence fits WAY-30 only where the accepted text gives the outcome, and the
  change keeps that condition.
- The `project-level` readiness-gate handling of colliding candidates (`project-level/skill/SKILL.md:155`):
  another process, outside the task.
- Whether "gives the outcome" should be made checkable: the task settles it as the agent's judgment.

## Checks run (from the worktree root)

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git rev-parse --show-toplevel` | 0 |
| `git diff --numstat 294af7f..9b44856`; `git log --oneline 294af7f..9b44856` | 0 |
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B task-cycle/private_paths_check.py <file>` for each of the six changed files | 0 each (`0 listed`) |
| `python -B gate/run_tests.py elements/common` | 0 (109 tests, OK) |
| `python -B gate/run_tests.py task-cycle` | 0 (187 tests, OK) |
| `python -B -` heredoc: whitespace-normalized substring test of the task's two quoted wordings in `foundations/decisions.md` | 0 (True, True) |
| `git status --short` after the runs | 0, empty |

Not run: the whole gate (the orchestrator's, WAY-160); `agent-instructions` tests (the author ran them
at 18 tests, exit 0, and no file of that test directory is read by name by a changed file as far as
the grep for test files shows - not repeated by me); `installation` tests, which read skill files by
copying them (the author did not run them either; I did not, as the whole gate covers them).

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md`: WAY-25 (whole), WAY-30 (whole), WAY-32 (whole), WAY-114 (whole), WAY-134
  (whole), WAY-293 (whole), WAY-26/172/268 (the passages citing WAY-25, with neighbouring lines), WAY-33
  (binding part and start of *Verification*). Why: the task's *Decisions in play* and *Context*, the
  WAY-33 search.
- `foundations/part_map.md` (grep for the agent-instructions part) and `foundations/invariants.md`,
  `glossary.md` (grep for `precedence|collid|the cycle's`; no hit). Why: parts touched, invariant and
  glossary entries stating the old rule.
- `elements/common/way_of_working.md` "Reading the foundation" (start). Why: the method named by the
  skill.
- Repository-wide grep (`WAY-25`, `collid`, `narrows`, `precedence`, `stops the work`, `never settled`)
  outside `.runs` and `.git`. Why: copies of the old rule.
- Test files that name the changed files (grep): `elements/common/test_foundation_check.py`,
  `task-cycle/test_request_check.py` and the `installation` tests; ran the two directories that hold
  them besides `installation`.

## Searches not found or unclear

- I did not read every decision whose *Scope* names `decisions`, `task-cycle` or `agent-instructions`
  whole (several hundred lines each); I read the entries listed above and searched the whole
  repository by identifier and words. A decision of those parts that states the old rule in other
  words, with none of the searched words, would be missed. No such entry found.
- The task's *To do* 1 and 5 give line numbers at `52889bc`; the contents were found by text, not by
  line, so the numbers were not needed. Unclear only: the task gives `request_template.md:174-180`,
  the handoff's reconciliation says 190-196; I used the handoff and the text.
- Whether a test or the request check parses item 6 of `request_template.md` for exact wording: the
  `task-cycle` tests pass, so no check reads the changed sentence in a way it breaks; I did not trace
  `request_check.py` itself.
