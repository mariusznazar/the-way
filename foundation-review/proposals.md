# The proposals and the data file

Read at step 4 of `SKILL.md`, once step 2 and step 3 have given their results. The list is for
the human to decide on: write it in plain words, so that each item is read without the code, and
explain a name of the process or of the repository the first time it appears.

## Proposals about the foundation

One proposal for each entry that needs a change, from `weak_points.md`. It holds:

- the entry, and the words that no longer hold, quoted whole;
- what the evidence shows, with its place at the checked commit;
- what to do: change, withdraw, add the entry that is missing, or run the check that was not run;
- what happens if the entry stays as it is, and what changing it costs — the work, and what in the
  foundation or the code the change reaches (WAY-33).

Small corrections of wording that do not change what an entry binds are not proposals one by one:
they gather into one collective task of the repository, listed in the data file.

## Decisions that describe a transitional state

Each decision of the list that `weak_points.md` gives for a transitional state is put to the human
with the sentence that describes the state quoted whole, what the decision says ends it, and the
question whether a task exists that ends it. Where the human names such a task, nothing is
proposed. Where none exists, the proposal is to create one, and it holds what happens if none is
made — the state stays in the product, and the decision goes on binding it — and what the task
costs. A task made on the human's yes follows `with_the_human.md`. The entry of the decision is not
changed and gains no field: the tasks of a product lie outside its repository, so an entry has no
name to give a task that stands in no project plan.

## Groups of entries that are no decisions

The entries that `weak_points.md` lists as no decisions are grouped by the place they go to, one
group for each place: a skill or an instruction file, the guidelines of a discipline, the product's
data or code, no entry, and a sentence of another entry. A group holds every entry of that place
that the run found, and its count stands beside its place. The human decides on whole groups, never
on part of one: the groups chosen go into one task of the product's backlog this time, and the
groups not chosen wait for the next review, which finds all the entries anew. The review chooses
no batch itself, however small its entries are.

Each group is put to the human with its place, its count, one entry quoted whole and where its
sentence would stand in that place, what happens if the group stays in the log — the log goes on
holding what is no decision, and an agent that reads it reads it again at each cycle — and what
moving it costs: the work, and the tests and entries that name it (WAY-33).

## Groups of remarks

The remarks that go forward from `remarks.md` are grouped by what one cycle can fix together — the
same file or area, the same kind of fix, the same moment — into these kinds:

- **a collective task** of the repository, a few in all, never one for each theme: a cycle fixes
  its remarks together, and a small remark is no task of its own;
- **a note to an existing task** of the backlog that touches the same code or text, found by a
  search of the backlog;
- **a note to a task waiting for a rewrite**, where a planned task is going to rewrite the code the
  remarks stand in, so that fixing it now would be done twice;
- **leave**, with a reason, for a remark that stands, breaks nothing the human cares about or is an
  accepted cost.

The human decides on groups, not on each remark: one remark's fate is settled when the task that
carries it is refined.

## The data file

One file for the whole review, in the task area step 1 found, named `foundation_review_<date>.md`
with the date of the checked commit. It holds:

- a head: the repository, the checked commit, the last review tag or `none`, the requests read,
  and the counts of every result of `remarks.md`;
- the remarks set aside, as a table of one line each: number, result, reason, or where its answer
  stands;
- one section for each group, with its kind, what it is about in one or two sentences, the number
  of remarks and a table of them, one line each (below);
- one section for the proposals about the foundation, the weak points of `weak_points.md` and the
  decisions that describe a transitional state, with the human's answer to each, whether a task
  exists or none and one is proposed;
- one section for the entries that are no decisions, with, under the group of each place, a table
  of one line for each entry (its number, the question, the place, the test line where one holds
  it), and the human's decision for each group: in the task this time, or waiting;
- under each group and proposal, the human's decision once it is made, with its date.

A table of remarks has the columns *Remark* (`<repository>#<request>-<k>`, with the numbers of both
when two requests carry it), *Result* (felt, mismatch, test gap or undetermined), *What happens*
(in plain words, to whom), *Reviewer's words*, *Place* (as the request gave it), *State today*
(evidence at the checked commit) and *Notes* (doubts, and what a critic or a check added).

A task that comes of a group points at its section of this file, and the section lists the remarks;
the task document does not copy the table.
