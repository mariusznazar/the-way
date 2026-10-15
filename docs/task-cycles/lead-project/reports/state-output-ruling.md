# State-reader output convention

The independent check author requested a distinguishable proposal row so a negative check cannot mistake an explanation mentioning done for an actual proposal. This is a reversible formatting choice within the approved human-readable CLI design, not a new workflow/state rule.

Each task has a header `task <n> <slug>: <current state>` and zero or more proposal lines `propose <n> <slug>: <from state> -> <to state>`. A proposal is only a line beginning with that exact propose prefix, without indentation or bullets. State values are the plan's literal English values; the separator is ASCII ` -> `.

Evidence rows use `evidence <n> <slug>: <details>`, unresolved task observations `unchecked <n> <slug>: <reason>`, and inconsistent task observations `conflict <n> <slug>: <reason>`. Global observations can use `unchecked: <reason>` and failures `error: <reason>`. Global header lines are `repository: <absolute path>` and, when established, `integration: <ref> <commit>`. Details/reasons are human-readable and not otherwise frozen; facts such as exact paths, refs and commit IDs must be present as the existing contract requires. An unavailable integration has no fabricated ref/commit.

Author choice: root under intermediate delegation. Alternative loose substring matching can mistake rejected evidence for a positive proposal; JSON would add a second output contract that the spec excludes. Cost if wrong: adjust reader and check together before final review; format is a small CLI convention. It is not human approval of foundation wording.
