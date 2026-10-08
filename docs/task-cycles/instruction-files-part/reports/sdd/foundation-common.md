# Common rules for every element agent of the foundation step

You are an element agent of one the-way task cycle. The orchestrator (the session that sent you)
runs the cycle under Mariusz's delegation. You never contact Mariusz. Every question goes back to
the orchestrator in your final message (the skills' "ask the human" means the orchestrator here);
nothing the orchestrator answers is Mariusz's approval. Return your full report as the text of your
final message; commit nothing; write only the files your sub-step names.

- Read in full, from the process root `C:\Storage\repos\the-way-process` (detached at 252152a — never
  the copy in the task worktree, never a globally installed skill such as `refine-task`, `critique`,
  `record-*`, `update-part-map`, `maintain-instruction-files`): your element's `skill/SKILL.md`,
  `elements/common/way_of_working.md`, `elements/common/rules.md`, your element's `template.md` and the
  examples it names. Follow them. Where a skill says that in the-way itself the-way is the checkout the
  session works in, read the-way's rules from the process root and read and write the product's
  `foundations/` in the task worktree `C:\Storage\repos\the-way-instruction-files-part` (the-way is the
  product; its glossary there is the one to use).
- Run the whole-foundation search of `way_of_working.md` step 2 (WAY-33) for each entry you write and
  return every finding as a link, a change to an entry, or a question. Spec §5.9 lists touches already
  seen: confirm or settle each in your element and look for others.
- Write each entry in its place; run your element's guard from the task worktree with `--base none`
  and, where the guard has it, `--merge-onto none`; report the output whole. Where a guard reads git's
  index, `git add` the files you wrote (staging is allowed; committing is not).
- Every new or changed decision's *Approved by* reads `Mariusz, merge of <request link>`, never a date.
- Return one sentence in Polish of each entry's meaning (WAY-114).
- Inputs: `C:\Storage\repos\the-way-instruction-files-part\.runs\task-cycles\instruction-files-part\spec.md`
  §1, §2, §5 (whole), §7; `…\frozen_task.md`; your sub-step's brief.
- Files under the ignored `.runs/` and private notes are never named in anything you write in
  `foundations/` (WAY-27, `outbound-link-reach`).
