# 7. The readiness gate

Step 7 of the skill `define-project`, whose `SKILL.md` lies beside this file; its items are 7.1 to
7.5.

In a turn dispatched through a refinement conversation path, `delegated_mode.md` beside this file
changes this step: never speak to the human directly, request the critique of 7.3 through the
conversation instead of running it, and write the fingerprint, the gate record and the `approved`
status only after the human's approval is recorded through the project orchestrator.

1. Run `python -B <the-way>/project-level/readiness_check.py <definition> --before-approval`. A
   finding of condition f goes back to step 5 (`find_entries.md` beside this file); a finding of
   condition g, or of condition a in "Technology", goes back to step 6 (`technology.md` beside
   this file); a finding of condition a inside a projected entry goes to the skill of its element
   in projected mode, which completes that entry's wording; any other finding goes back to step 4
   (`rounds.md` beside this file).
2. Search the whole foundation once for what the definition and its projected entries touch
   (WAY-118), with what each element's skill adds to the search of the foundation: the entries
   that name an entry the definition projects a change to; an entry that already states what a
   projected entry settles; and what the definition collides with that no written link joins — a
   decision whose binding sentences the project would break, an invariant, a glossary term the
   definition uses in another meaning, a fact the project contradicts. This is the one search of
   the whole foundation on the way to the gate: neither `find-foundation-entries` nor the skill of
   an element in projected mode makes one. Settle each finding before the gate: a projected change
   to the entry through the skill of its element in projected mode, a projected entry struck or
   turned into a change of the entry that already states it, shown to the human at 7.3, or the
   definition brought into line with it.
3. Run `critique` once on all finished projected entries, the definition and its sources
   (WAY-120). Verify its observations, correct proposals through the skills of their elements and
   bring any conflict with a human settlement back to the human. If an independent critic cannot
   run, say so and wait; the author's self-check does not meet this condition. Then show the
   projected entries as a list, each as its identifier and one sentence of its meaning in the
   human's language, with the whole entries in the definition for the human to read (WAY-114). The
   human approves their meaning, and may strike an entry or change its meaning; a changed meaning
   goes through the skill of its element in projected mode again, and where it changes the
   question of a decision an item of "Technology" names, the item takes the new question.
4. After the final review changes, run the check of 7.1 again; a finding goes where 7.1 sends it.
   On the human's approval, print the fingerprint with
   `python -B <the-way>/project-level/readiness_check.py <definition> --fingerprint`, write the
   gate record, and set the status line to `approved YYYY-MM-DD`. The gate record approves every
   projected entry; no entry carries a field of approval.
5. Run the check with no option; it must report nothing found. Tell the human what it reported,
   and that the approval and the search of 7.2 (condition c) rest on no script's check, and that
   the breakdown of the approved definition into tasks follows through `plan-project`
   (WAY-142).
