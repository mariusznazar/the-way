# Return of a task from a closed request

Read from step 1 of `SKILL.md` when the human has said that the blocked request of a task is
closed.

This transition is supported only on the human's word (WAY-269): a task whose blocked request the
human closed returns to refinement, and its row reading `in cycle` or still `ready for cycle` goes
to `to refine`, with a change-log line naming the request. The document cell stays. Before moving
the row, remove that one cycle's trace, naming what goes to the human and removing it on the same
word, in this order:

1. its worktree, where it ran in one of its own; where it ran in a checkout that stays, only
   that checkout's ignored `.runs/task-cycles/<task-name>` directory;
2. its local branch, by name, which git refuses while a worktree holds it;
3. its branch on the host, by name, where the human has not deleted it;
4. the remote-tracking ref of that branch alone, by name, with `git branch -dr`, after item 3,
   since a fetch would otherwise bring it back.

Left in place, the trace shows as a conflict on a `to refine` row, and on a `ready for cycle` row
as a false proposal that the new cycle has started. Should a removal fail, the reader
(`plan_state.py`) reports the conflict, which goes to the human as `SKILL.md` step 1 gives for a
conflicting trace. The new cycle keeps the task's name on a new branch.
