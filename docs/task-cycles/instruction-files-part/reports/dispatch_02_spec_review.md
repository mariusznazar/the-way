# Dispatch 02 — spec review (task cycle step 7)

You review a spec of one the-way task cycle. You did not write it. The orchestrator (the session that
sent you) runs the cycle under Mariusz's delegation; you do not contact Mariusz, and nothing you
approve is his approval. Your boundary is your review: write no file, change nothing, return the full
review as the text of your final message.

## Method

Use Superpowers 6.4.1 `spec-document-reviewer-prompt.md` as your lens, read in full from
`C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\brainstorming\spec-document-reviewer-prompt.md`.
Beyond its checks, this cycle asks you to check the spec **against the frozen task and the current
foundation**: missing requirements, invented behaviour, contradictions with a decision or invariant,
silent expansion or narrowing of scope.

## Material

- Spec: `C:\Storage\repos\the-way-instruction-files-part\.runs\task-cycles\instruction-files-part\spec.md`
- Frozen task (Polish, binding): `…\frozen_task.md` beside it; run brief `…\reports\run_brief.md`.
- Foundation, from the process root `C:\Storage\repos\the-way-process` (252152a): `foundations/*.md`,
  `elements/<element>/template.md` and `skill/SKILL.md`, `elements/common/rules.md` and
  `way_of_working.md`, `agent-instructions/`, `gate/`, `probes/`.
- The prototype the spec starts from: `C:\Storage\repos\the-way-instruction-files\instruction-files\`.
- The m1l4 settlements behind task point 6 and the assessment findings behind points 2–5 (Polish):
  `…\reports\source_m1l4_notes.md`.
- You may run read-only commands, and experiments only in a scratch copy under
  `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\821bfb3e-7677-4acf-bd0e-ab8a94541c58\scratchpad\review\`.

## Check at least

1. Every numbered point of the task's "To do" and its acceptance criterion is covered, or its
   reading is stated and defensible. In particular: point 1 names `skill/SKILL.md` and the spec
   flattens the layout (A1); point 7 asks for facts "z sondami zbudowanymi z pomiarów prototypu" for
   what the decisions of point 6 **and** `tool_loading.md` rest on, and the spec writes documentation
   watches only for what decisions rest on (§5.2) — judge each reading against the foundation (e.g.
   WAY-73, WAY-81, `script-subprocesses`) and say whether it is forced, defensible or a narrowing.
2. Each of the six drafted decisions (§5.5) against its m1l4 settlement and the task's wording of
   point 6, against `principles.md` (does a binding sentence say more or less than the principle it
   adopts — e.g. "more than once" in WAY-130 against §7's treatment of a single occurrence), against
   WAY-05 (form), WAY-12 (level), WAY-26, WAY-27, WAY-100, and against the-way's own instruction files
   (would the-way's current files violate a decision the moment it merges, and which files count as
   "the-way's own instruction files" — root files, skills, entry points?).
3. The WAY-127 narrowing (§5.4) and the options' costs; whether flattening alone, without the
   narrowing, already brings the skill text into line.
4. The part entry (§5.1): failure modes, severities against the criticality scale, detection,
   dependencies (WAY-46, WAY-48); the trust-boundary table (§4.6) — anything a crafted file could
   still do.
5. The four check-script fixes (§4.5): does each meet the task's case, and is each opposite failure
   tested; is any fix over-fitted to one file.
6. Invariants (§5.6) and their tests: sentences checkable, WAY-69 authorship, WAY-03 read-only, the
   right part, *Rests on*.
7. Facts (§5.7): WAY-80, WAY-85, WAY-90; do the decisions' *Based on* match; is any fact unnamed.
8. Fingerprint renewals (WAY-31) — are the lists complete (search for `WAY-09@`, `WAY-127@`).
9. Order of work (§7) against WAY-01/WAY-03 (foundation step before dependent code) and the checks
   (§8) against `agent-instructions/README.md`.

## Report

Approved / approved after fixes / not approved. Then numbered findings, each with severity
(blocking, should fix, minor), the spec section, the evidence (file and line, or quote), and a
concrete fix. Name what you could not check.
