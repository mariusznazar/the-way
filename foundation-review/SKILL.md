---
name: review-foundation
description: Use when a product's foundation has to be reviewed against the product — a request's description says the foundation waits for a review, or the human asks for one — reading the whole foundation and the unfixed remarks of the repository's merged requests, listing what to change, and marking the review done with a tag.
---

# Review the foundation

Reviews the foundation of one repository against the repository as it is today, with a human and
in one session: it reads every entry, sets the reasoning each decision gives against what the
product and its cycles show, checks the unfixed remarks that merged requests left behind, lists
what to change, has the whole list critiqued, goes through it with the human and marks the review
done with a tag (WAY-24, WAY-302). It changes nothing in the foundation or the code: a proposal the
human accepts becomes a task of the product's backlog, and the change reaches the foundation
through that task's cycle (WAY-14). One skill serves every product, and a review is made for one
repository at a time (WAY-304).

This skill lives in `foundation-review/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in, the directory `git rev-parse --show-toplevel` prints in the
session's working directory; in a product, it is the product's pinned `.the-way`. Each the-way
skill named below is the project skill of that name with the `the-way-` prefix. The repository
under review is the one the session works in — the-way itself, or a product that pins it — and the
review runs from that repository's root.

A request's description asks for this review once the main branch holds 30 merges since the last
review tag (WAY-300); the human may start it at any time.

## 1. Fix the range

- Fetch, and name the main branch the requests merge into. The commit its remote tip shows now is
  the checked commit: every later step reads the repository at it, and the tag marks it (step 7).
  Write it down at once.
- Find the last review: `git describe --tags --abbrev=0 --match 'foundation-review/*' <main
  branch>`, from the main branch and never from a task branch. A repository with no such tag
  answers that it found no names; its review begins at the start of its history (WAY-301).
- List the requests merged since: `git rev-list --merges --first-parent <tag>..<main branch>`,
  without the range for a repository with no tag; each merge names its request. Where the human
  names a request up to which another repository's review has already read the requests of this
  one, begin after it (WAY-304). A product that squashes or rebases its merges has no merge commit
  to list: read the requests from the host's list of merged requests instead.
- Find where the product keeps its tasks: the `## Backlog` section of the root `AGENTS.md`; where
  it names no place, ask once and offer to record the answer there. The data file of this review
  (step 4) stands in the task area, beside the task documents; a file in a repository that may be
  public holds no title of a private note. Where a data file of this review already stands there
  for the same range, resume from it and from the first step it has not finished.

## 2. Read the foundation

Read all of the foundation of the repository, each file whole: `foundations/decisions.md`,
`invariants.md`, `glossary.md`, `part_map.md` and `environment_facts.md`. Read `weak_points.md`
beside this skill for what to look for in each entry and for the checks to run (WAY-24, WAY-82,
WAY-305).

## 3. Check the unfixed remarks of the requests

Read `remarks.md` beside this skill: which remarks of the requests of step 1 are read, how each is
judged, and which are not raised again (WAY-303, WAY-304).

## 4. List the proposals

Read `proposals.md` beside this skill: the proposals about the foundation, the groups of remarks,
and the data file that holds the lists (WAY-302).

## 5. Have the set critiqued

When the list and the data file are complete, give the whole set to `critique`, as WAY-120 gives:
one fresh critic, with the proposals, the data file, the sources they stand on — the entries read,
the remarks and the evidence of their state — and the rules of this skill, without your defense.
The critic reads the remarks set aside as harmless as well, since they are the likeliest wrong
call. Check each observation against its evidence, give an explicit verdict on it and correct the
list and the data file before the human sees them. Do not show the human a set that has not been
critiqued.

## 6. Go through it with the human

Read `with_the_human.md` beside this skill for the order and the form: the proposals about the
foundation one by one, the groups of remarks as groups, and the tasks that follow from the human's
decisions (WAY-302).

## 7. Mark the review done

The review is done when the human has decided on every proposal and every group. Then mark it:

- Name the tag `foundation-review/YYYY-MM-DD` with today's date; where a tag of that date exists
  already, add `-2`, then `-3`. Put it on the checked commit of step 1, annotated, with
  `git tag -a <name> -m "<message>" <checked commit>`, also when the review changed nothing
  (WAY-301).
- The message gives the number of items checked and no title of a task or of a private note: the
  repository may be public.
- Show the human the name, the commit and the message, and push the tag with
  `git push origin <name>` on the human's yes: everyone with access to the repository sees a pushed
  tag, and only a human removes it.

Where the human ends the session before every decision is made, put no tag: the data file keeps
the decisions made, and the next run resumes from it (step 1). The next reminder counts from the
tag (WAY-300).

## Sharing the reading

Steps 2 and 3 read more than one agent holds at once. Divide the material in pieces that each fit
an agent — the decision log in consecutive ranges of entries, the requests in packs — and give a
fresh agent each piece with the checked commit, the rules of the step and the form of its answer:
for every entry or remark, its classification and the evidence, with the file and the place read at
the checked commit. Treat an agent's classification as a claim: read the place yourself for every
item you propose, and for a sample of those set aside. Another agent merges the items that two
pieces report twice. Hand an agent the work, never the verdict on what goes before the human.
