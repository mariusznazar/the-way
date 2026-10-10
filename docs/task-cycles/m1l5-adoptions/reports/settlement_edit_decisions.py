"""Apply the settlement's edits to foundations/decisions.md (scratch script, not committed)."""
import sys
import textwrap

sys.path.insert(0, "relation-model")
from fingerprint import fingerprint  # noqa: E402

PATH = "foundations/decisions.md"
WIDTH = 100


def para(text):
    return textwrap.fill(text, WIDTH, break_long_words=False, break_on_hyphens=False)


def item(text, first="  - ", rest="    "):
    return textwrap.fill(text, WIDTH, initial_indent=first, subsequent_indent=rest,
                         break_long_words=False, break_on_hyphens=False)


with open(PATH, encoding="utf-8", newline="") as handle:
    lines = handle.read().split("\n")


def replace(first, last, starts, ends, new):
    """Replace lines first..last (1-based, inclusive) after checking their ends."""
    block = lines[first - 1:last]
    assert block[0].startswith(starts), (first, block[0])
    assert block[-1].endswith(ends), (last, block[-1])
    lines[first - 1:last] = new.split("\n")


W140_BINDING = (
    "A task's effect outside the product's repository — on a server, in DNS, on keys or on an "
    "external account — is a human action, which the task document names and places before the "
    "cycle or in it, while reading outside the repository stays with the agent and the cycle's "
    "record of the request and of the task's state in the backlog entry the product names "
    "(WAY-107) is no effect of the task. For the human actions placed in the cycle, the cycle does "
    "what the repository allows and opens a blocked draft request listing them, and the human "
    "performs them at the request; an effect the cycle finds that the task document does not name "
    "joins that list for the human to place, and the request opens as a blocked draft where the "
    "document places no human action in the cycle. The human places each human action while the "
    "task is refined, on the agent's proposal: before the cycle when the cycle's code needs its "
    "effect, such as an account, a key or a database, and in the cycle when it uses code the cycle "
    "writes, such as a deployment or a DNS record pointing to a new address.")

W139_BINDING = (
    "The-way holds no skill of a product, only the list of what a product's deployment skill "
    "covers: a preview of deployments; where the secrets lie and how they are rotated; rollback, "
    "with its number of steps and what happens to the data; what the agent does and what the human "
    "does; and how to read the logs. When a task's outcome deploys the product or changes how or "
    "where it runs, the-way's skill `refine-task` checks, while it refines the task, that the "
    "product has a deployment skill covering every item of the list, and where it has none or an "
    "item is missing, the task gains an item of its To do for that work or the human splits that "
    "work into a task of its own.")

fp140 = fingerprint(W140_BINDING)

# Bottom-up, so earlier line numbers stay valid.
replace(4250, 4263, "*Rationale:* an effect outside", "after the work that needed it.", "\n".join([
    para("*Rationale:* an effect outside the repository is not undone by resetting a branch and "
         "does not show in the diff the human reviews, so the human who makes it sees what it "
         "changes; named in the task document, each human action is known before the cycle rather "
         "than found when the work stops on it. The request is the cycle's single point of human "
         "review (WAY-125), so a human action that uses the cycle's code waits for the request. A "
         "human action whose effect the code needs has to come first, and one that uses the code "
         "can only come after it; the human places each, because the human performs it. A read "
         "changes nothing outside the repository and the agent needs it to work, so it stays with "
         "the agent."),
    para("*Rejected:* the cycle making the effect itself — a reset would not undo it and the diff "
         "would not show it; the cycle pausing midway for the human — the human would be called "
         "between stages for each human action; every human action before the cycle — one that "
         "uses the cycle's code cannot come first; the agent placing each human action alone — the "
         "human performs it and is the one to fit it into the work; human actions listed only when "
         "someone asks for them — a step the human has to take comes to light after the work that "
         "needed it."),
]))
replace(4237, 4245, "  - complies: a task that sends mail", "    the cycle.",
        "\n".join([
            item("complies: a task that sends mail through an outside service names opening the "
                 "account and creating its key as human actions before the cycle, and it is not "
                 "ready until both exist; a task that moves the product to a new address names "
                 "pointing its DNS record there as a human action in the cycle, and the cycle, its "
                 "code done, opens a blocked draft request listing it; the agent reads a server's "
                 "free disk space while it makes the change;"),
            item("violates: the cycle runs the deployment against the server itself; the cycle "
                 "stops halfway and waits for the human to rotate a key; a task whose outcome needs "
                 "a new key on an external account is ready with no human action named for it; the "
                 "agent alone decides that a human action goes in the cycle."),
        ]))
replace(4221, 4229, "A task's effect outside", "pointing to a new address.", para(W140_BINDING))
replace(4208, 4214, "*Rationale:* how a product", "splits that work off.", para(
    "*Rationale:* how a product is deployed and operated depends on where and how it runs, which "
    "differs from product to product, so a skill of the-way would fit none of them; what such a "
    "skill has to answer is the same for every product, and a list in a binding sentence gives the "
    "refinement a thing to check. Knowledge of operating a product written in a document no step "
    "reads goes unread however concrete it is, while a skill of the product reaches the agent when "
    "it prepares a deployment. The check comes when a task first needs that knowledge, so the first "
    "task that deploys a product grows by its deployment skill, unless the human splits that work "
    "off."))
replace(4182, 4188, "The-way holds no skill", "a task of its own.", para(W139_BINDING))
replace(4147, 4151, "  - complies: a project settles", "foundation holds is not;", item(
    "complies: a project settles its store of data and its place to run, the table shows beside "
    "each option recommended the risks the three tests gave, each marked as a hypothesis, and the "
    "human who takes the recommended host finds those risks in the *Rationale* of its decision "
    "beside its lacks; a framework the definition names as a constraint is tested; a language a "
    "decision of the foundation holds is not;"))
replace(4104, 4107, "  - complies: two hosts", "costs less than the others;", item(
    "complies: two hosts that cost the same and take the same upkeep remain after the simplest and "
    "cheapest rule, and the one with a command-line tool and a deployment script is recommended; a "
    "host with no command-line tool stays in the comparison and is recommended where it costs less "
    "than the others;"))
replace(3573, 3578, "*Rationale:* a project can inform", "cannot finish its work.", para(
    "*Rationale:* a project can inform a task without owning it; the handoff must show which "
    "relationship applies so the next agent does not import work or dependencies the task never "
    "took on. A projected entry is wording already settled, and the task whose code first makes it "
    "true is the one that can show it holds; naming it before the cycle keeps one entry per rule. A "
    "human action placed before the cycle gives the cycle's code what it needs, so a cycle started "
    "before the human action is done cannot finish its work."))
replace(3557, 3557, "  WAY-126@35accf8b", "WAY-140@d02ede05",
        "  WAY-126@35accf8b · derives from WAY-134@b858b34f · derives from WAY-140@" + fp140)

with open(PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write("\n".join(lines))

print("WAY-139", fingerprint(W139_BINDING))
print("WAY-140", fp140)
