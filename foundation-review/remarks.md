# The unfixed remarks of merged requests

Read at step 3 of `SKILL.md`. The requests are those step 1 listed, of this repository only: a
review reads the unfixed remarks of its own repository, and the review of the-way reads a product's
requests only for evidence about the decisions of the-way (WAY-304).

## Which remarks

In each request's description, and in the comments under it, read every remark the cycle left
unfixed (WAY-303):

- the Minor findings, and the findings the reviewer marked outside the task's scope;
- the questions put to the human at the merge, those that ask whether a finding becomes a task
  (WAY-289) among them;
- the checks and states the request says were not run or not checked, and the blocking findings it
  says remained.

A request of an older form keeps these in whatever sections it has; read the same kinds. A remark
about the process itself, taken from a cycle's record, is not read: another review collects those.

## Answered remarks

A remark is not raised again when an answer to it is written down: a comment under the request in
which the human decides, or a later request that took the remark up or settled it. The merge is
not an answer. A question the request put to the human, with nothing written down after it, is
read and judged like any other remark; so is a remark whose answer is only that the request
merged. Record, for a remark set aside as answered, where its answer stands.

## Judging a remark

For each remark that is not answered, find the place it names in the repository at the checked
commit. Search by what the place holds, never by its line number, which moves; and follow the
history of the place since the request, as a remark is often fixed by a later change. Then give it
one result:

| Result | When |
|---|---|
| fixed | the place no longer holds what the remark describes |
| answered | its answer is written down (above) |
| standing and felt | it stands, and the product's user or the human working with the process will meet its effect (WAY-289) |
| standing and mismatched | it stands, and a text says something other than the code or another binding text |
| standing, gap in the tests | it stands, and a behaviour with a consequence has no test that would fail on its break |
| standing, harmless | it stands, and nothing is broken or misleading: a name, a wrap, a taste |
| undetermined | the place cannot be read, the effect cannot be established without running the product, or the request does not say what it meant |

Say in plain words what the remark does to whom — "a player who closes a menu and clicks a field
loses the first click", "someone who follows step 3 of the guide as written overwrites the earlier
backup" — and not only where the code is. Quote the reviewer's words and the place
the request gave, and the evidence of the state today, with file and place at the checked commit.
A remark you set aside as harmless needs a reason that a reader can contest; a remark that is
undetermined stays visible and is not rounded down.

Two requests often carry the same remark: join them under one line with both numbers.

## What goes forward

The remarks that stand as felt, mismatched or a gap in the tests, and the undetermined ones, go to
`proposals.md`, grouped there. The rest are counted by result, with the numbers of the requests
they come from, so that a critic can sample them.
