PASS 01ab269b7d36541d4b79069b63e0fa5f7d0d5514

# Review of the fix — decision-sources-and-leftouts

- Variant: review of a fix (`task-cycle/review/fix.md`). Fix range: `05b4648..01ab269`, one commit,
  one file (`foundations/decisions.md`, 33 added, 23 removed lines). The whole change now runs from
  `aba5ee9` to `01ab269`.
- `git rev-parse HEAD` gives `01ab269b7d36541d4b79069b63e0fa5f7d0d5514`, the head given.
- The fix raises no new Critical or Important finding. One new Minor finding (N1) does not block.

## Findings of the findings file

**I1: fixed.** WAY-142 *Rejected* (`foundations/decisions.md:4850-4852` at `01ab269`) now reads "the
milestones and the interview on the order of work of the practice of a roadmap of vertical slices —
left out of what the step takes from it". The estimates are gone. Both remaining elements are in
the practice: milestones (skill §"Milestone layer", map row "Milestone…") and the interview (skill
Step 5). The other items of WAY-142's *Rejected* still match the source; the reasons the fix added
to them are judged under M2. A search of the head for `the estimates` finds only `:3551`, a
different sentence in another entry.

**M1: fixed.** WAY-143 *Rationale* (`:4893-4895`) now says the practice's foundations stand "only
with what it unlocks — a slice, a blocking unknown it reduces or a way of verifying it enables".
These are the three things the course skill gives: line 344, "the downstream `S-NN` item it unlocks,
the blocking unknown it reduces, or the verification path it enables", and Step 8, check 10. The
fix says no more than the skill does.

**M2: fixed for the four entries the finding names.** I compared each reason the fix carries with
the course map's row, as I read it in the first review. I did not rely on the author's table.

| Entry, item | Reason carried | Map row | Verdict |
|---|---|---|---|
| WAY-138, known limitation recorded in an infrastructure document | such a document answers no question, and the decision of the choice carries it and its reasons | m1l5 row "`infrastructure.md` jako trzeci kontrakt": "`infrastructure.md` „nie odpowiada na żadne pytanie” … wybór i jego powody niosą decyzje the way" | same meaning |
| WAY-138, three-alternatives table | the step already compares the options of each choice, and its decision keeps those not chosen in *Rejected* | m1l5 row "Dwie techniki bez skilla": "tabelę trzech alternatyw krok technologii już robi (porównanie opcji, *Rejected*)" | same meaning |
| WAY-138, change of roles | no decision of the-way has several roles on its other side | same row: "w the way nie ma decyzji z kilkoma rolami po drugiej stronie" (the personal part is rightly not carried) | same meaning |
| WAY-142, scored readiness check | the definition passes its stricter readiness gate before the breakdown (WAY-118) | m2l1 row "Sprawdzenie gotowości PRD (0–4)": "the way ma ostrzejszą bramkę przed rozbiciem (… WAY-118 …)" | same meaning |
| WAY-142, fields that feed acceptance criteria, the "why here" sentence | the refinement of each task writes its acceptance criteria from its own analysis, and the order stands in the dependencies | m2l1 row "Kryteria akceptacji…": "kryteria akceptacji pisze krok doprecyzowania w dokumencie zadania z niezależnej analizy zadania … kolejność niesie kolumna „zależy od” planu" | same meaning |
| WAY-142, list of parked items | it copies what the definition puts out of scope | m2l1 row "Blokery zewnętrzne…": "*Parked* w A to kopia „Out of scope”" | says a little more than the row (N1) |
| WAY-142, state blocked by an unknown | the plan has a state of waiting for the human and places each open question where it is resolved | same row: "the way ma stan „czeka na człowieka” i „resolved in”". `project-level/plan/template.md:95` holds the state `waiting for human` ("the task's refinement waits for a human answer …"), and WAY-142's binding sentence holds "each open question … with where it is resolved" | same meaning; both facts hold |
| WAY-268, search engine for agents | a choice of a provider of search, not a step of the process | m2l4 row 4: "wybór dostawcy wyszukiwania, nie krok procesu" | same meaning |
| WAY-268, library documentation put into context ahead | an agent fetches the documentation when it needs it, rather than all of it ahead | m2l4 row 5: "dociągać informacje z dokumentacji, gdy są potrzebne, a nie zaciągać całej z góry" | same meaning |
| WAY-270, failure tool set up ahead | the step chooses the tool, with a deliberate absence among its options | m3l5 row 22: "narzędzie monitoringu wybiera się kwestią observability … (z opcją „bez narzędzia”), nie z góry Sentry ścieżką kursu" | same meaning |
| WAY-270, agent reaching failures through the tool's server | how an agent reads the record of the running product is a matter the step already settles (WAY-121) | m3l5 row 6: "agent czyta logi sam: WAY-121 (kwestia „logs” w kroku technologii)" | same meaning |

Leaving the code-stock item of WAY-142 without a reason is right: its map row is open, so the trace
holds no reason for it.

## New finding in the fix

### Minor

**N1: the reason given for WAY-142's parked list generalizes a trial observation.** It lies within
the task and does not block.

- Place: `foundations/decisions.md:4860`: "the practice's list of parked items, left out of what
  the step takes from it — it copies what the definition puts out of scope".
- The map row says only that Parked was a copy of Out of scope in trial A ("*Parked* w A to kopia
  „Out of scope”"). The course skill builds Parked from two things (Step 6g, line 416): it lifts the
  PRD's Non-Goals, and it appends anything the interview deferred. So the practice's list is mostly
  the out-of-scope items, plus items the interview put off.
- Why Minor: the reason holds for the main content of the list and changes no rule. A reader only
  learns less about the list than the skill holds.
- Possible wording: "it mostly copies what the definition puts out of scope".

No other new defect is in the fix. The binding text is untouched. The new wording "<element>, left
out of … — <reason>" keeps the form WAY-100 asks for.

## Checks run

| Command or method | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git log --oneline 05b4648..01ab269`; `git diff 05b4648 01ab269` | 0 | one commit, the head given |
| own script `compare_entries.py . aba5ee9 01ab269` (working copy) | 0 | binding changed: `['WAY-100']` only; 223 entries at both commits, none added or removed (acceptance criterion 1) |
| own script `compare_entries.py . 05b4648 01ab269` | 0 | binding changed: none; entries changed: WAY-138, 142, 143, 268, 270, the ones the findings name |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `git show 01ab269:foundations/decisions.md \| grep -n "the estimates"` | 0 | only `:3551`, another entry |
| search of the added lines for a vault name, a note link, a drive-letter path, `Users`, `vault`, `TODO` | 1 (no match) | 0 hits: privacy holds |
| manual: `project-level/plan/template.md:88-100` | — | state `waiting for human` exists |
| manual: each carried reason against its map row (table above) | — | 10 same in meaning, 1 broader (N1) |

Not run: the full gate (the orchestrator's) and no test directory. The fix changes only prose of
the decision log, which `foundation_check.py` covers.

## Reaches beyond the dispatch

- The course skill `10x-roadmap`, Step 6g (line 416), and the map rows, as read in my first review.
  Why: N1 and M1.

## Working copies

- `.runs/review-whole/` held only the comparison script. It was removed with `rm -rf` (exit 0), and
  `.runs/` holds only `task-cycles/`.

## Unread material

- For this review I did not reopen the course map. I compared the carried reasons with the row
  texts I extracted and read in my review of the whole change; every row the fix cites is among
  them. The rest is none.

## Searches not found or unclear

none
