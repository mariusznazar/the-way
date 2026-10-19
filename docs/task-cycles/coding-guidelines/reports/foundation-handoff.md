# Foundation handoff — coding guidelines (foundation step of the task cycle)

## Delegation

Mariusz asked for the-way's task cycle to take this task to a pull request and delegated
intermediate choices to the orchestrator. You are a foundation author. You never ask Mariusz
anything; a question goes back to the orchestrator in your report (the cycle asks the human only
through the request, and only where the foundation step allows a question: no recommendation, a
change of meaning of an approved decision, a row whose meaning cannot hold, or a value neither the
row nor your work gives).

## Worktree, commits and write boundaries

- Worktree `/home/user/the-way`, branch `claude/gallant-albattani-3k15lc`. Write only the
  foundation files your stage names, and commit them yourself (one commit per stage, or two where
  that helps), message in English, describing what the commit holds and what is expected to stay
  red until later stages, ending with these two lines after a blank line:

      Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
      Claude-Session: https://claude.ai/code/session_01DYywki95VF5wQGh3SzcQZB

  Do not push. Do not edit any other tracked file; write no code, no test.
- *Approved by* of every new or changed decision: `Mariusz, merge of <request link>` (literal
  placeholder; WAY-14; never a date). *Origin* and *Based on* as the spec gives.
- Reports: your full report to the path your stage names, check outputs beside it in
  `docs/task-cycles/coding-guidelines/reports/` (prefix `foundation-<stage>-`).

## Authoritative inputs (read whole)

1. Frozen task `docs/task-cycles/coding-guidelines/task-frozen.md` — *Settlements to record*
   rows are written whole, as entries of their kind; their wording is yours, their meaning the row's
   (WAY-134). The answers to questions 1–18 and the check questions K1–K3 give the rationale and
   rejected options.
2. Reviewed spec `docs/task-cycles/coding-guidelines/spec.md` — §2, §8 and §10 settle the entries,
   numbers, relations, verification levels and *Review when*; rulings C1–C21 in
   `reports/design-rulings.md` are applied there.
3. Plan `docs/task-cycles/coding-guidelines/plan.md` — "Foundation entries" and "Foundation stages".
4. The-way: `agent-instructions/README.md` (edit an existing decision in place before `main`;
   update every fingerprint and dependent of a changed binding part, WAY-31; search the whole
   foundation for unlinked effects, WAY-33); the element skill your stage names, read whole from
   this checkout with the files it names; the foundation by "Reading the foundation"
   (`elements/common/way_of_working.md`, WAY-150).

## Checks each stage runs (exit code and full output kept)

`python3 -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`
and the same for invariants and glossary; `python3 -B elements/part-map/format_guard.py
foundations/part_map.md --base none`; `python3 -B gate/run_tests.py <dir>` for `elements/decisions`,
`elements/invariants`, `elements/glossary`, `elements/part-map`, `relation-model`, `gate`. Python is
3.13.16 (the repository declares 3.14; record it). Errors expected because a later stage has not
run yet are named as such, each by its message.

## Report contract

Inputs and commits read; each entry written (identifier, one sentence of its meaning in Polish for
the request, WAY-114), its relations and fingerprints; renewals done; the whole-foundation search
(WAY-33): what you searched and what you found and how each finding was settled; choices you made
with the way rejected and cost if wrong; checks with command, exit code and output path; expected
reds; questions. Commits with changed-file list and added/removed line counts. Return a short
message: status, commit(s), checks summary, questions.

---

## Stage F1a (turn 1)

Skill: `the-way-record-decision` → `elements/decisions/skill/SKILL.md`. Write: WAY-167 and WAY-168
edited in place (spec §8.1, C20, C18, C19, C11); renew the `@47d9d53e` relations of WAY-171,
WAY-173 and WAY-188 to WAY-168's new fingerprint after reading each against the new binding part
(`guidelines-check-carrier`'s *Derives from* is renewed at F3, not here — say so); WAY-193 to
WAY-202 new (spec §8.2, §8.3). WAY-195: re-read every quotation from the public source yourself —
`https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/AGENTS.md`
(and other files of that commit you quote) and the paper's public copy
`https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf` — with path and line or
page; never copy a quotation from the task's private research; if a passage cannot be read, stop
and ask. Level 1 *Verification* identifiers name invariants written at F3; the guard's reports of
them as missing are expected until F3. Report: `reports/foundation.md` (section "F1a").

---

## Stage F1b (author B, fresh)

Skill: `the-way-record-decision`. Base: the commit F1a left (`a45956f`), which holds WAY-167 and
WAY-168 edited and WAY-193–WAY-202 new; read F1a's section of `reports/foundation.md` for its
choices (accepted provisionally by the orchestrator, C28) and "For later stages". Write WAY-203 to
WAY-212 new (spec §8.2, §2 for C2's plain words in WAY-203/WAY-204, §4.4 for WAY-204's rationale on
one fact per edition, C10 for WAY-206's two weak points, C20 for WAY-212's relation to WAY-167's
table). After your commit the decisions guard must report no reference to an unwritten decision;
level 1 invariants named and not yet written stay expected until F3. Search the whole foundation
(WAY-33) for the entries you add. Report: `reports/foundation.md` (section "F1b").

---

## Stages F2 and F3 (author B, resumed; you are the sentence author of every invariant of this task)

Base: `b03c5da`. Your F1b choices are accepted provisionally (C30).

- **F2** — `the-way-record-glossary-term` (`elements/glossary/skill/SKILL.md`): "exemplar" (row 24;
  the definition keeps what sets it apart from the plain sense, spec §2 and review Minor 11) and
  "standing check" (row 25); run the WAY-95 test on the plain-words meaning in WAY-203/WAY-204 and
  write a third term only if that test requires it (C2), saying so. `the-way-update-part-map`
  (`elements/part-map/skill/SKILL.md`): the two failure modes at `product-guidelines` (spec §8.6,
  C6; the second in C2's plain words). New files of later slices (`product-guidelines/coding/**`)
  are already claimed by `product-guidelines/**`; check it.
- **F3** — `the-way-record-invariant` (`elements/invariants/skill/SKILL.md`): `guidelines-check-carrier/1`
  edited in place, version kept (spec §8.5; its *Derives from* gains WAY-196 and renews WAY-168 to
  `@dc4a98a1`); `guidelines-check-form/1` *Derives from* gains WAY-202, sentence unchanged; new
  `guidelines-check-kind-index/1` (derives from WAY-167, WAY-212), `guidelines-check-exemplar/1`
  (WAY-198, WAY-199), `guidelines-check-example-files/1` (WAY-168), `gate-guidelines-example-evidence/1`
  (WAY-168; *Part* `gate · product-guidelines`; method `TODO` until a gate can). Methods and *Part*
  as the other `guidelines-check-*` (spec §8.5, plan "Foundation entries"). Write sentences only:
  no check, no test, no code (WAY-69 — the check author and the code authors are other agents).
  Every decision's level 1 identifier must stand in that invariant's *Derives from*.

Commit F2 and F3 (one or two commits). After F3 the decisions, invariants, glossary and part-map
guards report no error, save any you name with its reason. Search the whole foundation (WAY-33)
for what you add. Report: append sections "F2" and "F3" to `reports/foundation.md`, with each
invariant's sentence and its Polish meaning sentence, and the old and new sentence of
`guidelines-check-carrier/1` (WAY-57, for the request).
