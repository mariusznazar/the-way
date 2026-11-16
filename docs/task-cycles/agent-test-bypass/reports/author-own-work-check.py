"""Own-work check of the change: do the skills carry each element of the two decisions, with the
qualifications the decisions give (WAY-263: a restatement more broad or without a qualification)?

Usage: python -B own_work_check.py ROOT   (ROOT: a worktree or a directory of the same layout)
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])


def text(path: str) -> str:
    return re.sub(r"\s+", " ", (root / path).read_text(encoding="utf-8"))


review = text("task-cycle/review/SKILL.md")
change = text("task-cycle/change/SKILL.md")
skill = text("task-cycle/skill/SKILL.md")
template = text("task-cycle/skill/request_template.md")
decisions = text("foundations/decisions.md")

checks = [
    # WAY-409: the four signals, the qualifier that keeps the rule narrow, the grade, every review.
    ("review: branch or value for the input of a test",
     "a branch or a returned value made for the very input a test uses" in review),
    ("review: expected value written into the product's code",
     "expected value of a test written into the product's code" in review),
    ("review: comment naming a special case for a test",
     "a comment that names a special case for a test" in review),
    ("review: comparison outcome changed with no change to the test, overloaded operator",
     "no change to the test, such as an overloaded comparison operator" in review),
    ("review: narrow qualifier (only code that exists to make a test pass; a required special case is none)",
     "Only code whose branch, value or comparison exists to make a test pass is the finding" in review
     and "a special case that the requirement itself asks for is none" in review),
    ("review: graded Important at the least, blocks, in every review",
     "is Important at the least, in every review, so that it blocks" in review),
    # WAY-410, the author.
    ("change: writes no code for the input and changes neither the test nor its expected value",
     "write no code for the input of the test and change neither the test nor its expected value" in change),
    ("change: commits, returns questions naming the test, quoting the requirement, what it tried",
     "commit what you have and return the status `questions`" in change
     and "names the test, quotes the requirement and says what you tried" in change),
    ("change: a test of behaviour the task expressly changes is no contradiction",
     "behaviour the task expressly changes is no such contradiction: change it" in change),
    ("change: also the test it cannot pass by general code",
     "cannot make it pass by code that meets the requirement for every input" in change),
    # WAY-410, the orchestrator.
    ("skill: answers only from the four sources, quoting the passage",
     "only from the task, the spec, a decision or the sentence of an invariant" in skill),
    ("skill: never by the smallest reversible reading",
     "the smallest reversible reading never answers it" in skill),
    ("skill: no source -> blocked draft with the question under Needed from you",
     "open a blocked draft request that holds the question under *Needed from you*" in skill),
    ("skill: no retry for the executor of a slice that returns such a question",
     "gets no retry although a check of its slice fails" in skill),
    # The request template.
    ("template: a row of the table of variants for the question",
     "| A question about a test that no source settles" in template),
    ("template: kind 2 admits the question",
     "and a question about a test that no source settles (WAY-410)" in template),
    # The log.
    ("log: WAY-409 and WAY-410 are entries",
     "### WAY-409 " in decisions and "### WAY-410 " in decisions),
    ("log: WAY-410 narrows WAY-229",
     "**Relations:** derives from WAY-227 · narrows WAY-229" in decisions),
]

failed = 0
for name, ok in checks:
    print(("ok   " if ok else "FAIL ") + name)
    failed += 0 if ok else 1
print("failed:", failed)
sys.exit(1 if failed else 0)
