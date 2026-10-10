"""Apply the code review's five issues (scratch script, not committed)."""
import re
import sys
import textwrap

sys.path.insert(0, "relation-model")
from fingerprint import fingerprint  # noqa: E402

WIDTH = 100


def wrap(text, first="", rest=""):
    return textwrap.fill(text, WIDTH, initial_indent=first, subsequent_indent=rest,
                         break_long_words=False, break_on_hyphens=False)


def load(path):
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def save(path, text):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def swap(text, old_start, old_end, new):
    i = text.index(old_start)
    j = text.index(old_end, i) + len(old_end)
    return text[:i] + new + text[j:]


W140 = (
    "A task's effect outside the product's repository — on a server, in DNS, on keys or on an "
    "external account — is made only by a human, through a human action the task document names "
    "and places before the cycle or in it, while reading outside the repository stays with the "
    "agent and the cycle's record of the request and of the task's state in the backlog entry the "
    "product names (WAY-107) is no effect of the task. For the human actions placed in the cycle, "
    "the cycle does what the repository allows and opens a blocked draft request listing them, and "
    "the human performs them at the request; a human action the cycle finds that the task document "
    "does not name joins that list for the human to place, and the request opens as a blocked draft "
    "listing it even where the document places no human action in the cycle. The human places each "
    "human action the task document names while the task is refined, on the agent's proposal: "
    "before the cycle when the cycle's code needs its effect, such as an account, a key or a "
    "database, and in the cycle when it uses code the cycle writes, such as a deployment or a DNS "
    "record pointing to a new address.")
fp = fingerprint(W140)

# --- foundations/decisions.md -------------------------------------------------------------------
path = "foundations/decisions.md"
text = load(path)
start = text.index("### WAY-140/1")
head, entry = text[:start], text[start:]
entry = swap(entry, "A task's effect outside", "pointing to a new address.", wrap(W140))
old = ("An effect the cycle finds goes to the human like a named one, because the cycle may not "
       "make it, and the request is where the human meets it.")
new = ("A human action the cycle finds goes to the human like a named one, because the cycle may "
       "not perform it, and the request is where the human meets it.")
rationale_start = entry.index("*Rationale:*")
rationale_end = entry.index("\n*Rejected:*")
rationale = " ".join(entry[rationale_start:rationale_end].split())
assert old in rationale
entry = entry[:rationale_start] + wrap(rationale.replace(old, new)) + entry[rationale_end:]
head, count = re.subn(r"WAY-140@[0-9a-f]{8}", "WAY-140@" + fp, head)
assert count == 1
save(path, head + entry)

# --- foundations/glossary.md --------------------------------------------------------------------
path = "foundations/glossary.md"
text = load(path)
old = ("A human action is an effect of a task outside the product's repository that only a human "
       "makes.")
assert old in text
save(path, text.replace(old, "A human action is a step of a task outside the product's repository "
                             "that a human performs."))

# --- project-level/task/template.md -------------------------------------------------------------
path = "project-level/task/template.md"
text = load(path)
old = "- <action outside the repository> — before the cycle,"
assert old in text
text = text.replace(old, "- <human action outside the repository> — before the cycle,")
text = swap(text, "- **Human actions:** each effect", "names no action.", wrap(
    "- **Human actions:** each effect the task has outside the product's repository — on a server, "
    "in DNS, on keys or on an external account — is made only by a human, through a human action "
    "this section names (WAY-140). Reading outside the repository is no human action; it stays "
    "with the agent. Each human action states its placement, which the human sets while the task "
    "is refined, on the agent's proposal: `before the cycle` when the cycle's code needs its "
    "effect, such as an account, a key or a database, with `done` or `not done`; `in the cycle` "
    "when it uses code the cycle writes, such as a deployment or a DNS record pointing to a new "
    "address (WAY-140). Until the human places a human action, its placement reads `TODO`. The "
    "task is ready only when every human action before the cycle is done (WAY-124); the cycle "
    "opens a blocked draft request listing the human actions in the cycle, and the human performs "
    "them at the request (WAY-140). `none` means the task has no effect outside the repository. A "
    "task document written before this section existed names no human action.", "", "  "))
save(path, text)

# --- task-cycle/skill/SKILL.md: the copy of WAY-140's first sentence ----------------------------
path = "task-cycle/skill/SKILL.md"
text = load(path)
old = ("finish the task. An effect outside the product repository is a human action (WAY-140): for the\n"
       "   actions the task document places in the cycle,")
assert old in text
text = text.replace(old, (
    "finish the task. An effect outside the product repository is made only by a human, through a\n"
    "   human action (WAY-140): for the actions the task document places in the cycle,"))
save(path, text)

# --- project-level/task/skill/SKILL.md: the copy of WAY-140's first sentence --------------------
path = "project-level/task/skill/SKILL.md"
text = load(path)
old = ("- Name each effect the task has outside the product's repository as a human action under\n"
       "  *Human actions*; a read outside the repository stays with the agent (WAY-140).")
assert old in text
text = text.replace(old, (
    "- Name under *Human actions* the human action through which a human makes each effect the task\n"
    "  has outside the product's repository; a read outside the repository stays with the agent\n"
    "  (WAY-140)."))
save(path, text)

print("WAY-140", fp)
