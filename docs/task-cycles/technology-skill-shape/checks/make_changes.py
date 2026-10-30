"""Writes changes.json: old piece (keyed by its first 50 characters) -> exact new wording."""
import json
import pathlib

c = {}


def add(prefix, *new):
    c[prefix[:50]] = list(new)


add("The form and rules of the Technology section — wh",
    "The form and rules of the Technology section — which choices it lists, its markers, the weighing and the tests of options — stand in `definition_template.md`; how a skill asks stands in `elements/common/way_of_working.md`; the critique stands in `elements/common/critique/SKILL.md`;",
    "this skill holds the order of the work and the rules that hold across it, and a file beside it holds the work of each step.")
add("The project level's directory, `project-level/`, is",
    "The project level's directory, `project-level/`, is there, and each skill named in this skill or in a file beside it is the project skill of that name with the `the-way-` prefix.")
add("Read the definition whole, `definition_template.md`",
    'Read the definition whole, `project-level/definition_template.md` in full, and the section "How a skill asks" of `elements/common/way_of_working.md`.')
add('Where "Technology" reads `TODO`, begin with step 1.',
    'Where "Technology" reads `TODO`, begin with the step "List the choices" (`list.md` beside this file).')
add("Where it holds a list, first take the look step 1 gi",
    'Where it holds a list, first take the look at the logs, the interface and the development data that `running_product.md` beside this file gives, add each matter it finds missing as an item ending `— open`, and, where it adds one, show the list again as the step "List the choices" does (`list.md` beside this file) before going on (WAY-121).')
add("Then show the list, ask whether it still holds, and",
    'Then show the list and ask whether it still holds; where the human adds or changes an item, follow the step "List the choices" (`list.md` beside this file) for it.',
    'Then resume the step "Settle the open choices" (`settle.md` beside this file) with the open items and the preferences written under them; a report of an open choice under `.runs/technology/` that reads `critique: passed` is reused, and the research of the others starts again.')
add("Where it holds a list with no open item, go to step",
    'Where it holds a list with no open item, go to the step "Close" (`close.md` beside this file).')
add("Then, where the project brings behaviour a user sees",
    "Then, where the project brings behaviour a user sees in the running product, take the look at its logs, its interface and its development data that `running_product.md` beside this file gives, and list each matter as it says.",
    "Where the project brings behaviour a user sees in the running product, look at the three matters of an agent's way to the running product — its logs, its interface and its development data — by the exception the template's Technology section, in `project-level/definition_template.md`, gives.")
add("With no open item, say so in one sentence and go to",
    'With no open item, say so in one sentence and go to the step "Close" (`close.md` beside this file).')
add("**Research.** Give each choice of the wave to a fre",
    "**Research.** Give each choice of the wave to a fresh agent of its own, all at once, with the definition, the choice and the preferences under it, the template's Technology section, the binding sentences of every decision the Technology list names `held by`, and the path of the file `research.md`, beside this file, which holds the agent's work.")
add("Each finds the options in their documentation, sta",
    "Find the options in their documentation, starting from what the definition needs of the choice, never from a fixed list of stacks, not even as a hint, and give each option its source: a page of its documentation with its version (WAY-122).")
add("**Weigh.** For each option the project's code is w",
    "**Weigh.** For each option the project's code is written in or against, read off its documentation and its public record of use the properties the template's Technology section lists, citing for each the page it was read from.")
add("**Consequences.** For each option kept, the agent s",
    "**Consequences.** For each option kept, say what it costs, where it runs, what keeping it running takes and what changing it later costs; every difference claimed between the options cites its source (WAY-123).")
add("In a choice of an agent's way to the running produc",
    "In a choice of an agent's way to the running product — the logs, the interface or the development data, the three matters the template's Technology section names — also say for each option whether an agent can use it, and an option an agent cannot use stays in the comparison with the lack \"an agent does not check the running product this way\" (WAY-166).")
add("It writes the comparison to `.runs/technology/<cho",
    "Write the comparison to `.runs/technology/<choice>.md`, the choice's name in lower case with hyphens for spaces, which the product's Git ignores, and end.",
    "The comparison of a choice is written to `.runs/technology/<choice>.md`, the choice's name in lower case with hyphens for spaces, which the product's Git ignores.")
add("**Critique.** Give one fresh agent, following `crit",
    "**Critique.** Give one fresh agent, following `critique`, whose file is `elements/common/critique/SKILL.md`, the whole comparison of a choice, its sources and the definition, as soon as that comparison is written, and ask it to refute every claimed difference no source supports.")
add("Write the risks the tests give into the choice's re",
    "Write the risks the tests give into the choice's report, `.runs/technology/<choice>.md`, so that a resumed step finds them, as sub-step 6, Choose, needs.")
add("Then give one fresh agent, following `critique`, th",
    "Then give one fresh agent, following `critique`, whose file is `elements/common/critique/SKILL.md`, the whole table with the risks and the definition, telling it that the risks are hypotheses with no source rather than differences claimed between options, so it does not strike them, and ask it for what one choice of the table contradicts in another; verify each observation (WAY-120, WAY-138).")
add("The recommended option taken as offered passes with",
    "The recommended option taken as offered passes without a further question; any other answer — an option whose weak point the table did not name, an answer in the human's own words, one that adds a reason or a condition — gets one question against it, anchored in those words or the material, the question the section \"How a skill asks\" of `elements/common/way_of_working.md` asks after a choice, asked here and not again (WAY-113).")
add("A finding of condition g on an item still open goe",
    "A finding of condition g on an item still open goes back to the step \"Settle the open choices\" (`settle.md` beside this file), any other finding of condition g to the step \"List the choices\" (`list.md` beside this file); any other finding goes back to `define-project`, which names where.")

pathlib.Path(__file__).with_name("changes.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(c))
