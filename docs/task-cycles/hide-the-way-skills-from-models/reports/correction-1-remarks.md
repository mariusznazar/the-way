Remarks of the human for correction 1, word for word. Source: the comment https://github.com/mariusznazar/the-way/pull/154#issuecomment-7062821019 on the request (2026-11-21T12:48:30Z), which the session received as the input of the correction.

Uwagi doradcy dnia w imieniu Mariusza

1. Codex still loads the entry files that carry the new setting — checked by hand, nothing to fix here. A Codex session (codex-cli 0.163.0, model gpt-5.6-luna; the default model of this account is refused) opened in the folder of the task's worktree at 48e64f10, where both copies (.claude/skills and .agents/skills) carry `disable-model-invocation: true` in all 23 entry files, listed all 23 skills whose names start with `the-way-`. Note what this also shows: in Codex the skills stay visible to the model — Codex ignores the setting. Write this result into the record as the remark the item asks for.
2. Read them in this request: let a fresh reviewer read whole the four decisions named in item 2 (what assigns a file to a part of the repository, where a fragment of a skill stands, which citations become entries about the environment, how it is settled whether a rule of an instruction file works). The next task of the-way's queue changes skill files again (its own search in the return step), so a clause missed here would be built on.
3. Fix them here: the description of the part in the part map has to say that hiding from the model is Claude Code's behaviour, and that in Codex the skills stay visible to the model (see 1); the summary of the invariant test's failure message and the matching sentence in the instructions for agents name every cause the test reports, not three.

Items 4–6 accepted.

