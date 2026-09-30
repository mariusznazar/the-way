# The panel

What the panel assesses, what it decides and who sits on it are set by WAY-10; this file holds how
it is run. Steps 1, 3, 4 and 5 below follow WAY-10; step 2 is the way panels have been run, and no
decision sets it.

1. Each assessor receives the diff and the files of the commit it assesses — never the task's
   chronicle, never the author's reasoning, never the other assessor's assessment (WAY-10) — and a
   perspective named before it starts. The two assessors run on different models where two are
   available (WAY-10). One of the two perspectives names what of the change can be cut, or that
   nothing can (WAY-10).
2. Each assessor writes its remarks, marks the ones that block, and ends with one call: accept,
   accept with fixes, or redraft.
3. The settler receives both assessments whole and settles twice, reading them in one order and
   then in the swapped order (WAY-10). Each settlement checks every remark against the files of the
   repository — holds, holds in part, does not hold — and gives one recommendation: a call, the
   fixes that stay within the decisions in force, and the questions for a human.
4. A change of an invariant test's mechanics is decided by the panel where its two settlements
   agree, that is, give the same call with the same fixes; any other change, and one on which the
   two settlements differ, goes to a human with the diff, its effects, the two settlements and a
   recommendation (WAY-10).
5. Until the task cycle sets where the panel's record lives, the record — both assessments and the
   two settlements, one for each order, in short — goes into the message of the commit that carries
   the assessed change.

A pair of perspectives that has served changes to the foundation: *the agent that will work under
the change* applies it to real entries — twenty or more where the foundation holds that many — and
counts where it gives one answer, two or none; *consistency and form* checks each rule against the
decision it cites and names what can be cut.
