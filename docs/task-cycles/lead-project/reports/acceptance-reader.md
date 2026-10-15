# State-reader acceptance

Original full plan: `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Loop/plan_mvp_loop2.md`.
Disposable repository: `.runs/task-cycles/lead-project/acceptance-loop2`.
Confirmed source remote, read-only: `https://github.com/mariusznazar/loop2.git`.
The disposable repository already existed as a no-checkout clone. Its absent working files were not restored or treated as source-repository changes; the reader used its Git inventory/history and fetched only this clone.

Command, repeated against the original whole plan:

```text
python -B project-level/plan_state.py "C:/Storage/The Brain/The Brain/Notes/Projects/(P) Loop/plan_mvp_loop2.md" .runs/task-cycles/lead-project/acceptance-loop2
```

## Initial observations and corrections

The first run exited 0 but failed the task's acceptance: task 3 had only `ready for cycle -> in cycle`, then an unchecked PR outcome. The implementation assumed a filename `record.md`; actual retained records include `cycle.md`. Root's C13 ruling in `archive-recognition-ruling.md` established that an actual committed file within the exact reserved archive directory identifies record evidence, without a new filename/content schema.

A subsequent run after directory recognition exited 1, still lacked task 3 completion and reported a false conflict for task 2. `git log <main> -- <archive>` simplified away an archive added and removed within a merged side branch. A controlled no-fast-forward merge, removed archive and deleted task branch reproduced this failure. `--full-history` corrected the reading of reachable history.

The final run exited 0 and emitted exactly these proposals:

```text
integration: refs/remotes/origin/main 2b290f878115e26bd5f7c3e4415222f94367ed8b
propose 3 mag-w-lesie: ready for cycle -> in cycle
propose 3 mag-w-lesie: in cycle -> done
```

The full output is retained locally in `acceptance-reader-output.txt`. It includes exact archive paths and commits, including `docs/task-cycles/mag-w-lesie/cycle.md` at `c9644b21ec1d8124937d7e7ac7c8f6c49c6a79d9` and `0ae1664b38d89488e30819227e6adb536e96601d`, reachable from the fetched main commit above. It also extracts the actual PR pointer from retained record contents. Task 1 remains explicitly unchecked because no sufficient archive evidence exists; the other unstarted tasks remain unchecked without progress. These are observations, not rewritten plan states.

## Independent host association

Outside the reader, command:

```text
gh pr view 12 --repo mariusznazar/loop2 --json number,state,url,baseRefName,headRefName,mergeCommit,mergedAt
```

Exit 0, result retained in `acceptance-pr12.json`:

```json
{"baseRefName":"main","headRefName":"task/mag-w-lesie","mergeCommit":{"oid":"668baa091a8d89caceeeb070342f3aa3f506e109"},"mergedAt":"2026-10-13T22:17:18Z","number":12,"state":"MERGED","url":"https://github.com/mariusznazar/loop2/pull/12"}
```

Separate `git merge-base --is-ancestor <archive-commit> 668baa091a8d89caceeeb070342f3aa3f506e109` commands in the disposable clone exited 0 for both archive commits named above. The Git evidence and actual record PR pointer establish the association with the independently queried merged request. The reader itself never called `gh`.

## Source preservation

`acceptance-source-after.json` records the checks against `acceptance-source-baseline.json`: both original plan/definition SHA-256 values match, original repository HEAD remains `2b290f878115e26bd5f7c3e4415222f94367ed8b`, and original repository status remains empty. All three comparison flags are true. No source checkout fetch or document write occurred. Ordinary and independent command tests additionally compare original plan, definition and task bytes before and after reading.

All private source paths and these local evidence files remain in the ignored cycle area; no private fixture or source path is in tracked examples.
