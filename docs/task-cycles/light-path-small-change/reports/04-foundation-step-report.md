# Foundation step report — Task 1 (stopped at Step 2 with a finding)

- Status: STOPPED before Step 3. One finding outside spec §8 (F1 below) needs the orchestrator's
  ruling; plan Task 1 Step 2 says such a finding is resolved before Step 3, and the prompt forbids
  rewording plan text.
- Worktree: `C:/Storage/repos/the-way-light-path`, branch `task/light-path-small-change`, HEAD
  c64a607, `git status --short` clean. No file edited, no guard run, no commit.
- Author email checked: `<author email>`.

## Step 1 — read (done)

Read in full from the worktree: `elements/common/way_of_working.md`, `elements/common/rules.md`,
`elements/decisions/template.md`, `elements/decisions/skill/SKILL.md`,
`elements/decisions/examples.md` (WAY-03, read in the log), `elements/invariants/template.md`,
`elements/invariants/skill/SKILL.md`, `elements/invariants/examples.md` (its five entries, read in
the file), `foundations/glossary.md`, `foundations/decisions.md` (all 3637 lines),
`foundations/invariants.md` (all 2046 lines), and `foundations/part_map.md` (record-invariant step 1
asks for it; the plan's list omits it). Also `task_frozen.md`, `spec.md`, `cycle.md`.

## Step 2 — whole-foundation search (WAY-33)

The four commands of the plan, run on c64a607 — every result as the plan expects:

- grep 1, six lines: `foundations/decisions.md:388`, `:403`, `:3547`; `foundations/invariants.md:256`,
  `:262` (`WAY-13@c6b33aa9`); `task-cycle/skill/SKILL.md:38`. `WAY-125@` nowhere.
- grep 2, six prose citations: `elements/part-map/template.md:164`, `:202`;
  `foundations/decisions.md:1274`, `:1279`; `task-cycle/skill/SKILL.md:51`, `:141` — all about how
  sharply a change is checked, which the new WAY-13 keeps: no edit.
- grep 3: `31`.
- grep 4: `light path` at `foundations/decisions.md:1304` (WAY-47 *Rationale*, other meaning) and
  `elements/part-map/test_format_guard.py:76`, `:1224` (fixtures); `light cycle`, `full cycle`
  nowhere.

Reading of the 31 task-cycle decisions and WAY-01, 03, 10, 11, 25, 30, 31, 33, 36, 45, 47, 48, 69,
95, 97, 99, 100, 114, 126 against the new wordings: every row of spec §8 confirmed. Glossary:
"foundation", "entry", "invariant", "invariant test" keep their glossary meaning in the new
wordings; no new term enters a binding part; no paraphrase of a term's definition found. WAY-05
checks on the new prose: no file, script or count named, no normative word outside binding
sentences, no "should"/"will". Part map `task-cycle` responsibility still true.

Record-decision step 2 ("name the one question the binding sentences answer"): WAY-125's new
first sentence adds the light-cycle exception and the switch-and-discard clause. Both serve the
existing question, "Which Superpowers methods does the autonomous task cycle adopt?" — they say
when the adopted methods are used in full and that a grown change returns to them from a fresh
design — so the skill's outcome "keep the question the rest serves" applies; no second entry
(WAY-19). Settled here; not a finding.

### F1 — WAY-29 against D13 (not in spec §8)

WAY-29/1, binding sentence 2 (`foundations/decisions.md:789-791`):

> A rationale an agent proposes for a human's decision goes to the human as a question, never into
> the entry; the rationale of a decision an agent takes in a task is the agent's to write.

The plan (Step 8, new text 1c) writes into WAY-125's *Rejected* the reason for "a task once made by
one agent finishing that way whatever it grows into — the grown change would merge without the
design it turned out to need". The task rejects that option ("wariant „raz przyjęte zadanie kończy
się lżejszą ścieżką” odrzucony") without a reason; the reason is the design agent's (spec D13). The
WAY-125 change is Mariusz's decision (the approved task orders it, ruling C5), so read literally
WAY-29 sends that reason to him as a question and keeps it out of the entry. WAY-29's *Rationale*
names exactly this risk: "a reason an agent writes looks exactly like a recorded one, and later
readers take it for the reason the decision was made".

Against that reading: WAY-29's question is "How is a decision recovered from an existing product
written?", and binding sentences answer their decision's question; `elements/decisions/template.md`
applies the rule only in its "Inherited decisions" section ("A rationale proposed by an agent goes
to a human as a question, never into the entry"); WAY-114 makes an entry's wording the agent's,
with the human accepting its meaning at the merge; and ruling C2 already flags D13 for the request.
Every other *Rationale*/*Rejected* sentence of the new WAY-13 and WAY-125 traces to the task's
"Need" or its answers in "Questions to settle".

Ways open:

1. Keep the item as the plan writes it, reading WAY-29 as binding recovered decisions only, and
   have the request name the reason as the agent's (as C2 already plans) and cite this reading.
   Cost: if Mariusz reads WAY-29 generally, he strikes or rewords one *Rejected* clause at the merge
   — prose outside the binding part, no fingerprint moves, nothing else follows.
2. Keep the rejected option but drop its reason from the entry, and ask Mariusz for the reason in
   the request. Cost: a plan text change (orchestrator's ruling), an item with no reason in the log
   until he answers, and one more question in the request.
3. Treat the literal reading as binding and stop for Mariusz now. Cost: the cycle waits on a prose
   clause of a *Rejected* field.

Recommendation: 1. The binding sentences of WAY-29 answer how a recovered decision is written, the
template places the rule there alone, and the request already puts the reason in front of Mariusz
as the agent's, which is what WAY-29's "goes to the human as a question" protects. Whichever way is
ruled, the ruling belongs in `cycle.md` (Questions table) with WAY-29 cited, and the request's
"Wording beyond the task's words" item 6 should say that the reason is the agent's and that WAY-29
was weighed.

## Steps 3–13

Not started. On a ruling, I continue from Step 3 exactly as the plan writes it (or with the ruled
change to item 6 of WAY-125's *Rejected*); nothing in Steps 3–7 or the fingerprints depends on F1,
since *Rejected* lies outside the binding part.

## For cycle.md (orchestrator to transcribe)

- Events: 02:01–now, foundation step — Step 1 read done; Step 2 search done, results as plan
  expects; finding F1 returned before Step 3.
- Questions table: F1 — WAY-29 sentence 2 against D13's agent-written *Rejected* reason;
  recommendation way 1.
- Return step / Request handoff: nothing yet.

---

# Continuation after ruling C9 — Steps 3–13 done

- Status: DONE. Commit b977e5f8d8a83f60b2ae7862bc86a0e3738c301e (`b977e5f`) on
  `task/light-path-small-change`, author <author email>, two files; not pushed. Message written
  to the session scratchpad (`commit-msg-t1.txt`) and committed with `git commit -F`, text as the
  plan's Step 13.
- Ruling C9 applied: WAY-125's *Rejected* ends at "...the spec would carry the shape of the abandoned
  code." — the D13 item and its joining "; " dropped. Every other word as the plan writes it.

## Results

| Step | Check | Result |
|---|---|---|
| 4 | decisions guard after WAY-13 | exit 0; `0 error(s), 6 warning(s), 5 unchecked`; placeholder warning at `:417`; check-by warnings WAY-03 (:71), WAY-21 (:597), WAY-52 (:1429), WAY-55 (:1511), WAY-69 (:1925) — the baseline five; `unchecked:` lines identical to baseline |
| 6 | WAY-13 fingerprint from the file | `97b17d59` |
| 9 | decisions guard after WAY-125 | exit 0; `0 error(s), 7 warning(s), 5 unchecked`; placeholder warnings at `:417` and `:3606` |
| 10 | WAY-125 fingerprint from the file | `68b2d563` (base `4c302238`); `WAY-125@` carried nowhere |
| 10 | invariants diagnostic, red half (before the link renewal) | exit 1; `1 error(s), 0 warning(s), 1 unchecked`; `foundations/invariants.md:262: error: foundation-change-path/1: \`WAY-13@c6b33aa9\` — the current fingerprint of WAY-13 after the merge is 97b17d59` |
| 11 | decisions guard `--base none --merge-onto none` | exit 0; `0 error(s), 7 warning(s), 5 unchecked`; unchecked lines identical |
| 11 | invariants guard, same | exit 0; `0 error(s), 0 warning(s), 3 unchecked`; unchecked lines identical |
| 11 | glossary guard, same | exit 0; `0 error(s), 0 warning(s), 5 unchecked`; unchecked lines identical |
| 11 | DIAGNOSTIC (not a pass) decisions `--merge-onto c64a607` | exit 1; `4 error(s), 7 warning(s), 2 unchecked`; errors exactly the four expected: `:388` WAY-13/1 differs from its copy on c64a607, `:417` placeholder, `:3558` WAY-125/1 differs, `:3606` placeholder — all caused by the in-place edits; no relation-fingerprint error |
| 11 | DIAGNOSTIC (not a pass) invariants `--merge-onto c64a607` | exit 0; `0 error(s), 0 warning(s), 1 unchecked` — green half: `WAY-13@97b17d59` current |
| 12 | `gate/run_tests.py elements/decisions` | Ran 169 tests, OK |
| 12 | `gate/run_tests.py elements/invariants` | Ran 233 tests, OK |
| 12 | `gate/run_tests.py gate` | Ran 96 tests, OK |
| 13 | `git diff --numstat` (before commit) | `67 35 foundations/decisions.md`, `1 1 foundations/invariants.md` (plan expected 68 35; one line fewer because of C9) |
| — | line endings / length | both files `i/lf w/lf`, no CR; no added line over 100 characters |

Line positions after the commit: WAY-13 block grows 31 → 42 lines (+11), WAY-125 heading at 3558,
its *Approved by* at 3606, as the plan says. WAY-125's block grows by 17 lines (plan: 18) — C9 removes
one line at its end, after the *Approved by*, so no line number the plan names moves.

## For cycle.md (orchestrator to transcribe)

- Request handoff → "What this request settles":
  - `WAY-13/1 — Rozmiar zadania może odchudzić przygotowanie i wykonanie zmiany (spec, plan, liczbę
    agentów), ale nigdy wyniku zadania ani sprawdzeń gotowej zmiany; to, czy zadanie zmienia
    fundament, i ostrość sprawdzeń dalej wyznacza wyłącznie to, czego zadanie dotyka.`
  - `WAY-125/1 — Metody Superpowers obowiązują w pełnym cyklu; małe zadanie bez zmiany fundamentu
    robi jeden wykonawca, od testów tam, gdzie zmienia zachowanie, z jednym końcowym przeglądem
    całości, a zmiana, która przerośnie tę ocenę albo dotknie fundamentu w sposób wymagający
    otwartego wyboru, zmiany znaczenia zatwierdzonej decyzji, sprzeczności z wpisem lub inwariantu
    albo jego testu, jest odrzucana i zaczyna się od nowa od świeżego projektu z raportem wykonawcy
    bez kodu.`
  - Wording beyond the task's words (spec §7, items 1–5 stand); item 6 (D13) no longer applies —
    the item was dropped under C9, so the entry carries no agent-written reason.
- *Review when*: WAY-13 stays `none` — the decision rests on no prediction; WAY-125 stays `none`.
- foundation-change-path/1: *Derives from* renewed to `WAY-13@97b17d59`; version stays 1 (a renewed
  link does not raise it, WAY-31 *Rejected*; no main branch, `elements/common/rules.md` "Version");
  *Method* stays `TODO`, nothing handed to a check author. Sentence re-read against the new WAY-13:
  "No change that, against {fork-point}, alters a foundation entry runs on the path for tasks that
  leave the foundation unchanged." — still holds; the light cycle is not one of WAY-13's paths, and a
  light-cycle touch of the foundation re-records the route as changed (spec D1, §8 row 1).
- Artifacts / Events: commit b977e5f — foundation step (Task 1); the one independent assessment
  (WAY-10) is the cycle's step 11, after Tasks 2 and 3.
- Verification table rows: the results table above; the two `--merge-onto c64a607` runs are
  diagnostics, not passes; `--merge-onto none` leaves relation and link fingerprints unchecked —
  checked by hand (fingerprints computed from the file) and by the diagnostic.

---

# Fix C10 — WAY-125's foundation-touch discard confined to the executor's work

- Source: final whole-branch review, "Important 1" (`.superpowers/sdd/plan/final-review.md:84-105`);
  ruling C10. Base HEAD c64d49a; Task 2–3 files untouched.
- Commit: 70f6bda5e0a0412654f20784a40e331b14e1b414 (`70f6bda`), author <author email>, only
  `foundations/decisions.md`, `4 2` in numstat; message via scratchpad file `commit-msg-c10.txt`
  and `git commit -F`; not pushed.
- Edits (word diff shows only these two insertions; rewrapped only the line holding the change,
  leaving short lines `decision, contradicts a` and `    discarded and the task starts`, as the plan's
  rewrap rule asks):
  1. binding sentence: "or whose touch of the foundation {+while that agent makes it+} needs a
     choice the task leaves open, …" — the clause now reads exactly as C10 gives it;
  2. *Verification* complies: "or whose touch of the foundation {+while the agent makes it+} writes
     an invariant, is discarded …".
- Record-decision checks: the change is in a binding sentence of an entry already changed in place
  on this branch (no main branch, WAY-07); *Approved by* stays `Mariusz, merge of <request link>`;
  the meaning sentence for the request gains the limit — proposed:
  `WAY-125/1 — Metody Superpowers obowiązują w pełnym cyklu; małe zadanie bez zmiany fundamentu
  robi jeden wykonawca, od testów tam, gdzie zmienia zachowanie, z jednym końcowym przeglądem
  całości, a zmiana, która przerośnie tę ocenę albo w trakcie pracy wykonawcy dotknie fundamentu w
  sposób wymagający otwartego wyboru, zmiany znaczenia zatwierdzonej decyzji, sprzeczności z wpisem
  lub inwariantu albo jego testu, jest odrzucana i zaczyna się od nowa od świeżego projektu z
  raportem wykonawcy bez kodu.`
  Nothing derives from WAY-125, so step 4.4 has nothing to follow.

| Check | Result |
|---|---|
| WAY-125 fingerprint (UTF-8 file bytes, `relation-model/fingerprint.py`) | `f4d471cc` (was `68b2d563`) |
| WAY-13 fingerprint | `97b17d59`, unchanged |
| carriers of `WAY-125@` (worktree, excluding .git and .runs) | none; the only textual hit is the git-ignored review file's prose (`.superpowers/sdd/plan/final-review.md:102`), not a reference |
| decisions guard `--base none --merge-onto none` | exit 0; `0 error(s), 7 warning(s), 5 unchecked`; placeholder warnings at `:417` and `:3608` (WAY-125's *Approved by* moved down two lines); unchecked lines identical to baseline |
| `gate/run_tests.py elements/decisions` | Ran 169 tests, OK |
| `gate/run_tests.py gate` | Ran 96 tests, OK |
| line length / endings | no added line over 100 characters; LF, no CR |

Line shift: WAY-125's *Approved by* is now at :3608 (was :3606); the `--merge-onto c64a607`
diagnostic, if rerun, would name `:3608` for its placeholder error.
