"""Apply the coordinator's rulings 2-4 to WAY-140 (scratch script, not committed)."""
import textwrap

PATH = "foundations/decisions.md"
WIDTH = 100


def wrap(text, first="", rest=""):
    return textwrap.fill(text, WIDTH, initial_indent=first, subsequent_indent=rest,
                         break_long_words=False, break_on_hyphens=False)


with open(PATH, encoding="utf-8", newline="") as handle:
    text = handle.read()

start = text.index("### WAY-140/1")
head, entry = text[:start], text[start:]


def swap(old_start, old_end, new):
    global entry
    i = entry.index(old_start)
    j = entry.index(old_end, i) + len(old_end)
    entry = entry[:i] + new + entry[j:]


swap("- **Relations:** derives from WAY-100@e7a74a18", "WAY-125@441e3a6a",
     "- **Relations:** derives from WAY-100@e7a74a18 · derives from WAY-107@0ffcebe1 · derives "
     "from\n  WAY-125@441e3a6a")
swap("  - complies: a task that sends mail", "while it makes the change;", wrap(
    "complies: a task that sends mail through an outside service names opening the account and "
    "creating its key as human actions before the cycle; a task that moves the product to a new "
    "address names pointing its DNS record there as a human action in the cycle, and the cycle, its "
    "code done, opens a blocked draft request listing it; the agent reads a server's free disk "
    "space while it makes the change; the cycle itself adds the request link to the task's entry in "
    "the product's backlog;", "  - ", "    "))
swap("  - violates: the cycle runs the deployment", "goes in\n    the cycle.", wrap(
    "violates: the cycle runs the deployment against the server itself; the cycle stops halfway and "
    "waits for the human to rotate a key; a task whose outcome needs a new key on an external "
    "account is ready with no human action named for it; the agent alone decides that a human "
    "action goes in the cycle; the cycle finds that its change needs a key the task document does "
    "not name and creates the key itself.", "  - ", "    "))
swap("*Rationale:* an effect outside the repository", "so it stays with\nthe agent.", wrap(
    "*Rationale:* an effect outside the repository is not undone by resetting a branch and does not "
    "show in the diff the human reviews, so the human who makes it sees what it changes; named in "
    "the task document, each human action is known before the cycle rather than found when the work "
    "stops on it. The request is the cycle's single point of human review (WAY-125), so a human "
    "action that uses the cycle's code waits for the request. An effect the cycle finds goes to the "
    "human like a named one, because the cycle may not make it, and the request is where the human "
    "meets it. A human action whose effect the code needs has to come first, and one that uses the "
    "code can only come after it; the human places each, because the human performs it. A read "
    "changes nothing outside the repository and the agent needs it to work, so it stays with the "
    "agent. The backlog record is the cycle's own account of its request, not something the task's "
    "outcome needs, so it stays with the cycle."))

with open(PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(head + entry)
